"""
Shared plumbing for the F5 LLM-visibility harness.

One CSV per provider. Every row logs: provider, exact model ID, UTC timestamp,
condition (search_off / search_on), temperature, variant, repetition, prompt,
full response text, citation metadata, token usage, and any error.

Runs are resumable: rows already present in the output CSV are skipped, so a
crashed or rate-limited run can be restarted with the same command.
"""
import argparse
import csv
import json
import os
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

FIELDS = [
    "run_id", "provider", "model_id", "timestamp_utc", "condition", "temperature",
    "reasoning_setting", "panel_id", "variant_id", "base_id", "prompt_type",
    "paraphrase", "rep", "prompt_text", "response_text", "citations_json",
    "search_count", "input_tokens", "output_tokens", "latency_s", "error",
]

_lock = threading.Lock()


def parse_args(provider, default_model):
    p = argparse.ArgumentParser(description=f"{provider} harness")
    p.add_argument("--panel", default="panel_ai_sec_v1.json")
    p.add_argument("--model", default=default_model,
                   help="Exact model ID. Verify with --list-models first.")
    p.add_argument("--condition", choices=["search_off", "search_on", "both"], default="both")
    p.add_argument("--reps", type=int, default=30)
    p.add_argument("--out", default=None, help="Output CSV (default results/<provider>_<model>.csv)")
    p.add_argument("--workers", type=int, default=4, help="Concurrent requests")
    p.add_argument("--max-output-tokens", type=int, default=1500)
    p.add_argument("--temperature", type=float, default=None,
                   help="Leave unset to use the provider default (recommended, KB 3.3)")
    p.add_argument("--variants", default=None, help="Comma-separated variant IDs to run (default all)")
    p.add_argument("--limit", type=int, default=None, help="Stop after N new calls (smoke test)")
    p.add_argument("--dry-run", action="store_true", help="No API calls; writes fake rows to test the pipeline")
    p.add_argument("--list-models", action="store_true", help="Print models visible to this key and exit")
    return p.parse_args()


def load_panel(path, variants_filter=None):
    with open(path, encoding="utf-8") as f:
        panel = json.load(f)
    variants = panel["variants"]
    if variants_filter:
        keep = {v.strip() for v in variants_filter.split(",")}
        variants = [v for v in variants if v["variant_id"] in keep]
    return panel, variants


def existing_keys(out_path):
    done = set()
    if not os.path.exists(out_path):
        return done
    with open(out_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("error"):
                done.add((row["condition"], row["variant_id"], int(row["rep"])))
    return done


def build_jobs(panel, variants, conditions, reps, done):
    jobs = []
    for cond in conditions:
        for v in variants:
            for r in range(1, reps + 1):
                if (cond, v["variant_id"], r) not in done:
                    jobs.append((cond, v, r))
    random.shuffle(jobs)  # spread conditions/variants over time so rate limits and drift hit evenly
    return jobs


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def with_retries(fn, attempts=6, base=2.0):
    last = None
    for i in range(attempts):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last = e
            msg = str(e).lower()
            retryable = any(k in msg for k in ("rate", "429", "overloaded", "503", "502", "timeout", "temporar", "connection"))
            if not retryable or i == attempts - 1:
                raise
            time.sleep(base * (2 ** i) + random.random())
    raise last


def fake_response(v, cond):
    """Dry-run stand-in. Deliberately includes F5 aliases, competitors, a stale name,
    an inaccurate recommendation, and a citation so the scorer can be exercised."""
    pool = [
        "For runtime protection look at Lakera Guard, Protect AI's Layer, and F5 AI Guardrails. CalypsoAI is another option. Kong AI Gateway or Portkey can front the models.",
        "Options include HiddenLayer, Prompt Security, Cloudflare AI Gateway, and NGINX as a reverse proxy. For DPU offload you could also migrate to BIG-IP Next.",
        "Zscaler and Netskope cover shadow AI discovery. Robust Intelligence (now Cisco AI Defense) handles model validation. F5 was historically an ADC vendor, not an AI security vendor.",
        "LiteLLM is a popular open-source gateway. Palo Alto Prisma AIRS bundles Protect AI. Check Point acquired Lakera in 2025.",
    ]
    text = random.choice(pool)
    cites = [{"url": "https://www.example-review-site.com/ai-security-tools", "title": "Best AI security tools"}] if cond == "search_on" else []
    return text, cites, (1 if cond == "search_on" else 0), 200, 120


def run(provider, args, call_fn, list_models_fn=None):
    """call_fn(prompt_text, condition, args) -> (text, citations(list), search_count, in_tok, out_tok, reasoning_setting, model_id_reported)"""
    if args.list_models:
        if list_models_fn:
            for m in list_models_fn():
                print(m)
        else:
            print("Model listing not implemented for this provider; check the provider console.")
        return

    panel, variants = load_panel(args.panel, args.variants)
    conditions = ["search_off", "search_on"] if args.condition == "both" else [args.condition]
    os.makedirs("results", exist_ok=True)
    out_path = args.out or os.path.join("results", f"{provider}_{args.model.replace('/', '_')}.csv")
    done = existing_keys(out_path)
    jobs = build_jobs(panel, variants, conditions, args.reps, done)
    if args.limit:
        jobs = jobs[: args.limit]
    run_id = f"{panel['panel_id']}_{provider}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    print(f"[{provider}] model={args.model} panel={panel['panel_id']} conditions={conditions} "
          f"reps={args.reps} already_done={len(done)} to_do={len(jobs)} out={out_path}")
    if not jobs:
        return

    new_file = not os.path.exists(out_path)
    fh = open(out_path, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(fh, fieldnames=FIELDS)
    if new_file:
        writer.writeheader()
        fh.flush()

    def one(job):
        cond, v, rep = job
        t0 = time.time()
        row = {
            "run_id": run_id, "provider": provider, "model_id": args.model, "timestamp_utc": utc_now(),
            "condition": cond, "temperature": "default" if args.temperature is None else args.temperature,
            "reasoning_setting": "", "panel_id": panel["panel_id"], "variant_id": v["variant_id"],
            "base_id": v["base_id"], "prompt_type": v["type"], "paraphrase": v["paraphrase"], "rep": rep,
            "prompt_text": v["text"], "response_text": "", "citations_json": "[]", "search_count": 0,
            "input_tokens": "", "output_tokens": "", "latency_s": "", "error": "",
        }
        try:
            if args.dry_run:
                text, cites, sc, itok, otok = fake_response(v, cond)
                rs, mid = "dry-run", args.model
                time.sleep(0.01)
            else:
                text, cites, sc, itok, otok, rs, mid = with_retries(lambda: call_fn(v["text"], cond, args))
            row.update({"response_text": text, "citations_json": json.dumps(cites, ensure_ascii=False),
                        "search_count": sc, "input_tokens": itok, "output_tokens": otok,
                        "reasoning_setting": rs, "model_id": mid or args.model})
        except Exception as e:  # noqa: BLE001
            row["error"] = f"{type(e).__name__}: {e}"[:500]
        row["latency_s"] = round(time.time() - t0, 2)
        with _lock:
            writer.writerow(row)
            fh.flush()
        return row

    n_ok = n_err = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(one, j) for j in jobs]
        for i, f in enumerate(as_completed(futs), 1):
            r = f.result()
            if r["error"]:
                n_err += 1
            else:
                n_ok += 1
            if i % 25 == 0 or i == len(jobs):
                print(f"  {i}/{len(jobs)} done  ok={n_ok} err={n_err}", file=sys.stderr)
    fh.close()
    print(f"[{provider}] finished. ok={n_ok} err={n_err}. Re-run the same command to retry errored rows.")
