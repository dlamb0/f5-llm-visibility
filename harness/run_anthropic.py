"""Anthropic harness. Requires ANTHROPIC_API_KEY.

  python run_anthropic.py --list-models
  python run_anthropic.py --model <exact-id> --dry-run --limit 10
  python run_anthropic.py --model <exact-id>

Search-on uses the server-side web_search tool with max_uses=1 so each call
incurs at most one search fee and the instrument is comparable across engines.
Extended thinking is left off (the default), per KB [A2.18].
"""
import os
import sys

from common import parse_args, run

DEFAULT_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")  # VERIFY with --list-models

try:
    import anthropic
except ImportError:
    print("pip install anthropic", file=sys.stderr)
    raise

_client = None


def client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def list_models():
    return sorted(m.id for m in client().models.list(limit=100).data)


def _extract(resp):
    texts, cites, searches = [], [], 0
    for b in resp.content:
        t = getattr(b, "type", "")
        if t == "text":
            texts.append(b.text)
            for c in getattr(b, "citations", None) or []:
                if getattr(c, "type", "") == "web_search_result_location":
                    cites.append({"url": getattr(c, "url", ""), "title": getattr(c, "title", "")})
        elif t == "server_tool_use":
            searches += 1
    u = getattr(resp, "usage", None)
    stu = getattr(u, "server_tool_use", None) if u else None
    if stu and getattr(stu, "web_search_requests", None) is not None:
        searches = stu.web_search_requests
    itok = getattr(u, "input_tokens", "") if u else ""
    otok = getattr(u, "output_tokens", "") if u else ""
    # dedupe citations by url
    seen, uniq = set(), []
    for c in cites:
        if c["url"] not in seen:
            seen.add(c["url"])
            uniq.append(c)
    return "".join(texts), uniq, searches, itok, otok, getattr(resp, "model", None)


def call(prompt, cond, args):
    kwargs = dict(model=args.model, max_tokens=args.max_output_tokens,
                  messages=[{"role": "user", "content": prompt}])
    if cond == "search_on":
        kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 1}]
    if args.temperature is not None:
        kwargs["temperature"] = args.temperature
    resp = client().messages.create(**kwargs)
    text, cites, sc, itok, otok, mid = _extract(resp)
    return text, cites, sc, itok, otok, "thinking=off(default)", mid


if __name__ == "__main__":
    a = parse_args("anthropic", DEFAULT_MODEL)
    run("anthropic", a, call, list_models)
