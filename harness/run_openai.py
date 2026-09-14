"""OpenAI harness. Requires OPENAI_API_KEY. Uses the Responses API.

  python run_openai.py --list-models
  python run_openai.py --model <exact-id> --dry-run --limit 10
  python run_openai.py --model <exact-id>              # both conditions, 30 reps

Search-on uses the built-in web_search tool; the per-call search fee is logged
implicitly via search_count. Reasoning effort is forced to the minimum the model
accepts (reasoning does not help factual recall, KB [A2.18]) and falls back
cleanly for models that do not take a reasoning parameter.
"""
import os
import sys

from common import parse_args, run

DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-terra")  # VERIFY with --list-models

try:
    from openai import OpenAI
except ImportError:
    print("pip install openai", file=sys.stderr)
    raise

_client = None


def client():
    global _client
    if _client is None:
        _client = OpenAI()
    return _client


def list_models():
    return sorted(m.id for m in client().models.list().data)


def _extract(resp):
    text = getattr(resp, "output_text", "") or ""
    cites, searches = [], 0
    for item in getattr(resp, "output", []) or []:
        t = getattr(item, "type", "")
        if t == "web_search_call":
            searches += 1
        elif t == "message":
            for part in getattr(item, "content", []) or []:
                for ann in getattr(part, "annotations", []) or []:
                    if getattr(ann, "type", "") == "url_citation":
                        cites.append({"url": getattr(ann, "url", ""), "title": getattr(ann, "title", "")})
    u = getattr(resp, "usage", None)
    itok = getattr(u, "input_tokens", "") if u else ""
    otok = getattr(u, "output_tokens", "") if u else ""
    return text, cites, searches, itok, otok, getattr(resp, "model", None)


def call(prompt, cond, args):
    base = dict(model=args.model, input=prompt, max_output_tokens=args.max_output_tokens, store=False)
    if cond == "search_on":
        base["tools"] = [{"type": "web_search"}]
        base["tool_choice"] = "auto"
    if args.temperature is not None:
        base["temperature"] = args.temperature

    # Try minimal reasoning first; fall back if the model rejects the parameter.
    attempts = [
        ({**base, "reasoning": {"effort": "minimal"}}, "reasoning=minimal"),
        ({**base, "reasoning": {"effort": "low"}}, "reasoning=low"),
        (base, "reasoning=n/a"),
    ]
    last = None
    for kwargs, label in attempts:
        try:
            resp = client().responses.create(**kwargs)
            text, cites, sc, itok, otok, mid = _extract(resp)
            return text, cites, sc, itok, otok, label, mid
        except Exception as e:  # noqa: BLE001
            last = e
            msg = str(e).lower()
            if "reasoning" in msg or "unsupported" in msg or "not supported" in msg or "invalid" in msg:
                continue
            raise
    raise last


if __name__ == "__main__":
    a = parse_args("openai", DEFAULT_MODEL)
    run("openai", a, call, list_models)
