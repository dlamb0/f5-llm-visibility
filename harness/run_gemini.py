"""Gemini harness. Requires GEMINI_API_KEY (Gemini Developer API, not Vertex).

  python run_gemini.py --list-models
  python run_gemini.py --model <exact-id> --dry-run --limit 10
  python run_gemini.py --model <exact-id>

Search-on uses Grounding with Google Search. Thinking budget is set to 0 where
the model allows it (reasoning does not help recall, KB [A2.18]); models that
cannot disable thinking fall back to the default and the row records which.
"""
import os
import sys

from common import parse_args, run

DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")  # VERIFY with --list-models

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("pip install google-genai", file=sys.stderr)
    raise

_client = None


def client():
    global _client
    if _client is None:
        _client = genai.Client()
    return _client


def list_models():
    out = []
    for m in client().models.list():
        out.append(m.name)
    return sorted(out)


def _extract(resp):
    text = getattr(resp, "text", "") or ""
    cites, searches = [], 0
    cands = getattr(resp, "candidates", None) or []
    if cands:
        gm = getattr(cands[0], "grounding_metadata", None)
        if gm:
            for ch in getattr(gm, "grounding_chunks", None) or []:
                w = getattr(ch, "web", None)
                if w:
                    cites.append({"url": getattr(w, "uri", ""), "title": getattr(w, "title", "")})
            searches = len(getattr(gm, "web_search_queries", None) or [])
    u = getattr(resp, "usage_metadata", None)
    itok = getattr(u, "prompt_token_count", "") if u else ""
    otok = getattr(u, "candidates_token_count", "") if u else ""
    thoughts = getattr(u, "thoughts_token_count", None) if u else None
    if thoughts:
        otok = (otok or 0) + thoughts
    return text, cites, searches, itok, otok, getattr(resp, "model_version", None)


def call(prompt, cond, args):
    tools = [types.Tool(google_search=types.GoogleSearch())] if cond == "search_on" else None
    common = dict(max_output_tokens=args.max_output_tokens, tools=tools)
    if args.temperature is not None:
        common["temperature"] = args.temperature

    attempts = [
        (types.GenerateContentConfig(**common, thinking_config=types.ThinkingConfig(thinking_budget=0)), "thinking_budget=0"),
        (types.GenerateContentConfig(**common), "thinking=default"),
    ]
    last = None
    for cfg, label in attempts:
        try:
            resp = client().models.generate_content(model=args.model, contents=prompt, config=cfg)
            text, cites, sc, itok, otok, mid = _extract(resp)
            return text, cites, sc, itok, otok, label, mid
        except Exception as e:  # noqa: BLE001
            last = e
            msg = str(e).lower()
            if "thinking" in msg or "budget" in msg or "invalid" in msg:
                continue
            raise
    raise last


if __name__ == "__main__":
    a = parse_args("gemini", DEFAULT_MODEL)
    run("gemini", a, call, list_models)
