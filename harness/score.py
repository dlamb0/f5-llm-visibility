"""
Scorer for harness output. Reads every CSV in results/, applies the category-11
alias table, and writes:

  scored/scored_rows.csv            one row per response with F5 + competitor scores
  scored/mention_rates.csv          engine x condition x base (and ALL) with Wilson 95% CIs
  scored/share_of_model.csv         engine x condition: F5 rate / sum of tracked-set rates
  scored/consideration_set.csv      per base prompt: stable (>55%) / emerging (25-55%) / absent (<25%)
  scored/cited_domains.csv          search_on only: domain counts per engine, F5-owned flag, competitor co-mentions
  scored/spot_check_sample.csv      10% random + every Contextual / stale / inaccurate row, for human review
  scored/summary.md                 human-readable readout

Usage:  python score.py [--results results] [--out scored] [--seed 7]
"""
import argparse
import csv
import glob
import json
import math
import os
import random
import re
from collections import Counter, defaultdict
from urllib.parse import urlparse

import aliases_ai_sec as A

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def domain_of(url):
    try:
        h = urlparse(url).netloc.lower()
        return h[4:] if h.startswith("www.") else h
    except Exception:  # noqa: BLE001
        return ""


def score_f5(text, f5_pats, inacc_pats, ctx_re, rec_re):
    """Returns dict with tier, score, stale, inaccurate, first_pos, framing, matched aliases."""
    best = 0.0
    tier = "None"
    stale = False
    inacc = False
    matched = []
    first_pos = None
    framing = "none"
    n = max(len(text), 1)

    sentences = SENT_SPLIT.split(text)
    offset = 0
    for s in sentences:
        s_start = text.find(s, offset) if s else offset
        offset = s_start + len(s)
        has_f5 = re.search(r"\bF5\b", s, re.IGNORECASE) is not None
        is_ctx = ctx_re.search(s) is not None
        is_rec = rec_re.search(s) is not None

        # inaccurate check (BIG-IP Next ADC as go-forward)
        for ip in inacc_pats:
            m = ip.search(s)
            if m:
                if is_ctx:
                    # "F5 discontinued BIG-IP Next" -> Contextual, not inaccurate
                    tier_c, sc = "Contextual", 0.25
                    matched.append("BIG-IP Next (historical)")
                    if sc > best:
                        best, tier = sc, tier_c
                else:
                    inacc = True
                    matched.append("BIG-IP Next (INACCURATE)")
                if first_pos is None:
                    first_pos = (s_start + m.start()) / n

        for pat, kind in f5_pats:
            m = pat.search(s)
            if not m:
                continue
            if kind == "attrib" and not has_f5:
                continue  # generic term, no attribution -> ignore
            if kind == "full" or (kind in ("partial", "stale") and has_f5):
                sc, t = 1.0, "Full"
            else:  # partial/stale without attribution
                sc, t = 0.5, "Partial"
            if kind == "stale":
                stale = True
            if is_ctx:
                sc, t = min(sc, 0.25), "Contextual"
            matched.append(m.group(0))
            if first_pos is None:
                first_pos = (s_start + m.start()) / n
            if sc > best:
                best, tier = sc, t
            if t != "Contextual":
                framing = "recommend" if is_rec else ("list" if framing != "recommend" else framing)
            elif framing == "none":
                framing = "caveat"

    return {"f5_tier": tier, "f5_score": best if not inacc or best > 0 else 0.0, "f5_stale": stale,
            "f5_inaccurate": inacc, "f5_first_pos": "" if first_pos is None else round(first_pos, 3),
            "f5_framing": framing, "f5_matched": "; ".join(dict.fromkeys(matched))}


def score_competitors(text, comps, watch):
    out, standalone_only = {}, {}
    for name, d in comps.items():
        hit = any(p.search(text) for p in d["aliases"])
        acq = any(p.search(text) for p in d["acquirer"]) if d["acquirer"] else False
        out[name] = int(hit or acq)
        if d["acquirer"]:
            standalone_only[name] = int(hit and not acq)
    watch_hits = [n for n, pats in watch.items() if any(p.search(text) for p in pats)]
    return out, standalone_only, watch_hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="results")
    ap.add_argument("--out", default="scored")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    random.seed(args.seed)
    os.makedirs(args.out, exist_ok=True)

    f5_pats, inacc_pats, ctx_re, rec_re, comps, watch = A.compile_all()
    comp_names = list(comps.keys())

    rows = []
    for path in sorted(glob.glob(os.path.join(args.results, "*.csv"))):
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("error"):
                    continue
                rows.append(r)
    if not rows:
        print("No scored rows: results/ is empty or every row errored.")
        return

    scored = []
    for r in rows:
        text = r["response_text"] or ""
        s = score_f5(text, f5_pats, inacc_pats, ctx_re, rec_re)
        c, so, wh = score_competitors(text, comps, watch)
        try:
            cites = json.loads(r.get("citations_json") or "[]")
        except json.JSONDecodeError:
            cites = []
        domains = sorted({domain_of(x.get("url", "")) for x in cites if x.get("url")})
        engine = f"{r['provider']}:{r['model_id']}"
        out = {
            "engine": engine, "provider": r["provider"], "model_id": r["model_id"], "condition": r["condition"],
            "timestamp_utc": r["timestamp_utc"], "variant_id": r["variant_id"], "base_id": r["base_id"],
            "prompt_type": r["prompt_type"], "rep": r["rep"], **s,
            "f5_full": int(s["f5_tier"] == "Full"), "f5_weighted": s["f5_score"],
            "competitors_named": "; ".join(n for n in comp_names if c[n]),
            "competitor_standalone_only": "; ".join(n for n, v in so.items() if v),
            "watchlist_named": "; ".join(wh),
            "cited_domains": "; ".join(domains), "n_citations": len(cites),
            "search_count": r.get("search_count", ""), "response_text": text,
        }
        for n in comp_names:
            out[f"c::{n}"] = c[n]
        scored.append(out)

    # --- scored rows
    fields = list(scored[0].keys())
    with open(os.path.join(args.out, "scored_rows.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(scored)

    # --- mention rates: engine x condition x base (+ ALL)
    groups = defaultdict(list)
    for s in scored:
        groups[(s["engine"], s["condition"], s["base_id"])].append(s)
        groups[(s["engine"], s["condition"], "ALL")].append(s)
    rate_rows = []
    for (eng, cond, base), g in sorted(groups.items()):
        n = len(g)
        k = sum(x["f5_full"] for x in g)
        lo, hi = wilson(k, n)
        row = {"engine": eng, "condition": cond, "base_id": base, "n": n,
               "f5_full_rate": round(k / n, 3), "ci_lo": round(lo, 3), "ci_hi": round(hi, 3),
               "f5_weighted_rate": round(sum(x["f5_weighted"] for x in g) / n, 3),
               "f5_any_rate": round(sum(1 for x in g if x["f5_tier"] != "None") / n, 3),
               "stale_name_rate": round(sum(x["f5_stale"] for x in g) / n, 3),
               "inaccurate_rate": round(sum(x["f5_inaccurate"] for x in g) / n, 3)}
        for cn in comp_names:
            row[f"c::{cn}"] = round(sum(x[f"c::{cn}"] for x in g) / n, 3)
        rate_rows.append(row)
    with open(os.path.join(args.out, "mention_rates.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rate_rows[0].keys()))
        w.writeheader()
        w.writerows(rate_rows)

    # --- share of model (ALL rows per engine x condition; confirmed set and full set)
    som_rows = []
    for r in rate_rows:
        if r["base_id"] != "ALL":
            continue
        conf = [cn for cn in comp_names if comps[cn]["confirmed"]]
        denom_conf = r["f5_full_rate"] + sum(r[f"c::{cn}"] for cn in conf)
        denom_all = r["f5_full_rate"] + sum(r[f"c::{cn}"] for cn in comp_names)
        som_rows.append({"engine": r["engine"], "condition": r["condition"], "n": r["n"],
                         "f5_full_rate": r["f5_full_rate"],
                         "share_of_model_confirmed_set": round(r["f5_full_rate"] / denom_conf, 3) if denom_conf else "",
                         "share_of_model_full_set": round(r["f5_full_rate"] / denom_all, 3) if denom_all else "",
                         "top_competitors": "; ".join(f"{cn}={r[f'c::{cn}']}" for cn in sorted(comp_names, key=lambda c: -r[f"c::{c}"])[:5])})
    with open(os.path.join(args.out, "share_of_model.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(som_rows[0].keys()))
        w.writeheader()
        w.writerows(som_rows)

    # --- consideration set
    cs_rows = []
    for r in rate_rows:
        if r["base_id"] == "ALL":
            continue
        p = r["f5_full_rate"]
        status = "stable" if p > 0.55 else ("emerging" if p >= 0.25 else "absent")
        cs_rows.append({"engine": r["engine"], "condition": r["condition"], "base_id": r["base_id"],
                        "n": r["n"], "f5_full_rate": p, "ci_lo": r["ci_lo"], "ci_hi": r["ci_hi"], "status": status})
    with open(os.path.join(args.out, "consideration_set.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(cs_rows[0].keys()))
        w.writeheader()
        w.writerows(cs_rows)

    # --- cited domains (search_on)
    dom_rows = []
    by_eng = defaultdict(list)
    for s in scored:
        if s["condition"] == "search_on":
            by_eng[s["engine"]].append(s)
    for eng, g in by_eng.items():
        n_on = len(g)
        counts, comention, f5mention = Counter(), defaultdict(Counter), Counter()
        for s in g:
            doms = [d for d in s["cited_domains"].split("; ") if d]
            for d in doms:
                counts[d] += 1
                if s["f5_tier"] in ("Full", "Partial"):
                    f5mention[d] += 1
                for cn in comp_names:
                    if s[f"c::{cn}"]:
                        comention[d][cn] += 1
        for d, c in counts.most_common():
            dom_rows.append({"engine": eng, "domain": d, "responses_citing": c,
                             "share_of_search_on_responses": round(c / n_on, 3),
                             "f5_owned": int(any(d == o or d.endswith("." + o) for o in A.F5_OWNED_DOMAINS)),
                             "responses_citing_that_mention_f5": f5mention[d],
                             "competitor_comentions": "; ".join(f"{k}={v}" for k, v in comention[d].most_common(5))})
    if dom_rows:
        with open(os.path.join(args.out, "cited_domains.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(dom_rows[0].keys()))
            w.writeheader()
            w.writerows(dom_rows)

    # --- spot-check sample
    must = [s for s in scored if s["f5_tier"] == "Contextual" or s["f5_stale"] or s["f5_inaccurate"]]
    rest = [s for s in scored if s not in must]
    sample = must + random.sample(rest, min(len(rest), max(1, len(scored) // 10)))
    with open(os.path.join(args.out, "spot_check_sample.csv"), "w", newline="", encoding="utf-8") as f:
        cols = ["engine", "condition", "variant_id", "rep", "f5_tier", "f5_score", "f5_stale", "f5_inaccurate",
                "f5_framing", "f5_matched", "competitors_named", "human_verdict", "human_note", "response_text"]
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for s in sample:
            w.writerow({**s, "human_verdict": "", "human_note": ""})

    # --- summary.md
    engines = sorted({s["engine"] for s in scored})
    lines = ["# Scoring summary", "",
             f"Rows scored: {len(scored)} across {len(engines)} engine(s). Spot-check sample: {len(sample)} rows "
             f"({len(must)} mandatory + random 10%).", ""]
    lines += ["## Category aggregate (base_id = ALL)", "",
              "| Engine | Condition | n | F5 Full rate [95% CI] | Weighted | Stale-name | Inaccurate | Share of model (confirmed set) |",
              "|---|---|---|---|---|---|---|---|"]
    som_idx = {(r["engine"], r["condition"]): r for r in som_rows}
    for r in rate_rows:
        if r["base_id"] != "ALL":
            continue
        som = som_idx[(r["engine"], r["condition"])]["share_of_model_confirmed_set"]
        lines.append(f"| {r['engine']} | {r['condition']} | {r['n']} | {r['f5_full_rate']:.1%} [{r['ci_lo']:.1%}–{r['ci_hi']:.1%}] "
                     f"| {r['f5_weighted_rate']:.1%} | {r['stale_name_rate']:.1%} | {r['inaccurate_rate']:.1%} | {som if som == '' else f'{som:.1%}'} |")
    lines += ["", "## Path diagnosis (search_on minus search_off, F5 Full rate)", ""]
    for eng in engines:
        off = next((r for r in rate_rows if r["engine"] == eng and r["condition"] == "search_off" and r["base_id"] == "ALL"), None)
        on = next((r for r in rate_rows if r["engine"] == eng and r["condition"] == "search_on" and r["base_id"] == "ALL"), None)
        if off and on:
            gap = on["f5_full_rate"] - off["f5_full_rate"]
            overlap = not (on["ci_lo"] > off["ci_hi"] or off["ci_lo"] > on["ci_hi"])
            verdict = ("CIs overlap: no claimable gap" if overlap else
                       ("Path R carrying the brand; Path P weak" if gap > 0 else "Search-on LOWER: retrieved content hurting; inspect cited domains"))
            lines.append(f"- {eng}: off {off['f5_full_rate']:.1%} → on {on['f5_full_rate']:.1%} (Δ {gap:+.1%}). {verdict}.")
        else:
            lines.append(f"- {eng}: only one condition present; no diagnosis.")
    lines += ["", "## Competitor rates (ALL, per engine × condition)", ""]
    for r in rate_rows:
        if r["base_id"] != "ALL":
            continue
        top = sorted(comp_names, key=lambda c: -r[f"c::{c}"])[:8]
        lines.append(f"- {r['engine']} / {r['condition']}: " + ", ".join(f"{c} {r[f'c::{c}']:.0%}" for c in top))
    wl = Counter()
    for s in scored:
        for n in s["watchlist_named"].split("; "):
            if n:
                wl[n] += 1
    if wl:
        lines += ["", "## Watchlist names seen (not in denominator)", ""]
        lines += [f"- {n}: {c} responses ({c/len(scored):.1%})" + ("  ← >5%, consider promoting next cycle" if c / len(scored) > 0.05 else "") for n, c in wl.most_common(15)]
    if dom_rows:
        lines += ["", "## Top cited domains (search_on)", ""]
        for eng in engines:
            top = [d for d in dom_rows if d["engine"] == eng][:10]
            if top:
                lines.append(f"**{eng}**")
                lines += [f"- {d['domain']}: {d['responses_citing']} ({d['share_of_search_on_responses']:.0%}){' [F5-owned]' if d['f5_owned'] else ''}; competitor co-mentions: {d['competitor_comentions'] or '—'}" for d in top]
                lines.append("")
    lines += ["", "*Unconfirmed competitor names (not yet signed off): " +
              ", ".join(n for n in comp_names if not comps[n]["confirmed"]) + ". share_of_model_confirmed_set excludes them.*"]
    with open(os.path.join(args.out, "summary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
