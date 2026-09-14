# F5 LLM-visibility harness — AI Security pilot (panel AI-SEC-v1)

Design and scoring follow `10-llm-visibility-knowledge-base.md` Section 3. The harness executes; the scorer applies the alias table; the analysis and report come afterwards from `scored/`.

## Setup

```
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=...  GEMINI_API_KEY=...  ANTHROPIC_API_KEY=...
```

## 1. Pin the model IDs (do this first)

The defaults in the scripts are placeholders. List what your keys can reach and pick the Sonnet-tier model from each provider:

```
python run_openai.py --list-models
python run_gemini.py --list-models
python run_anthropic.py --list-models
```

Pick a **dated/pinned ID** where one exists rather than a `-latest` alias, so the model can't change under you mid-cycle (KB 3.3). Write the three IDs down; they go in the report header.

## 2. Smoke test (costs cents)

```
python run_openai.py    --model <id> --limit 6
python run_gemini.py    --model <id> --limit 6
python run_anthropic.py --model <id> --limit 6
python score.py
```

Open `results/*.csv` and confirm: `response_text` is populated, `search_count` is 1 for `search_on` rows and 0 for `search_off`, `citations_json` is non-empty on search_on, `reasoning_setting` shows what the model accepted. If `search_count` is 0 on search_on rows, the tool call didn't happen — stop and check the tool syntax for that SDK version before spending money.

## 3. Full run (36 variants × 30 reps × 2 conditions = 2,160 calls per engine)

```
python run_openai.py    --model <id>
python run_gemini.py    --model <id>
python run_anthropic.py --model <id>
```

Runs are resumable: re-run the same command after a crash or rate-limit stall and it skips finished rows and retries errored ones. `--workers 4` is the default; lower it if you hit 429s. Rough wall time at 4 workers: 1–3 hours per provider. Run them in parallel in three terminals.

If a provider ships a new model version mid-run, the `model_id` column will show it (it's taken from the response where the API reports it). Any variant whose 30 reps span two IDs must be re-run on one ID; the scorer keys on `model_id`, so mixed rows will show up as a separate engine.

## 4. Score

```
python score.py
```

Outputs in `scored/`:

- `scored_rows.csv` — every response with F5 tier (Full / Partial / Contextual / None), weighted score, `stale_name`, `inaccurate`, first-mention position, framing, competitors named, cited domains.
- `mention_rates.csv` — per engine × condition × base prompt (+ ALL) with Wilson 95% CIs, stale-name and inaccurate rates, competitor rates.
- `share_of_model.csv` — F5 rate ÷ sum of tracked-set rates. Two versions: confirmed competitor set only, and full set.
- `consideration_set.csv` — stable (>55%) / emerging / absent per base prompt.
- `cited_domains.csv` — search-on only. Which domains each engine cites, whether they're F5-owned, and which competitors are named in responses that cite them. Domains that carry competitors and not F5 are the earned-media target list.
- `spot_check_sample.csv` — every Contextual / stale / inaccurate row plus a random 10%. Fill in `human_verdict` (agree / Full / Partial / Contextual / None) and `human_note`. This is the human pass the method requires.
- `summary.md` — the readout.

## 5. Measured cost

```
python cost_report.py --price openai=<in>,<out>,<search> --price gemini=<in>,<out>,<search> --price anthropic=<in>,<out>,<search>
```

Prices per million tokens and per search call, from your actual bills. This replaces the plan's estimate for the scale-up slide.

## 6. Commit the results

Copy `results/*.csv` and the completed `scored/spot_check_sample.csv` into the repo's top-level `results/<cycle>/` folder and commit. Claude scores and reports from there.

## What not to do

Don't edit `panel_ai_sec_v1.json` once a single real call has been made; that's v2 and a new cycle. Don't set `--temperature 0`. Don't add a system prompt. Don't compare rows across different `model_id`s. Don't present any per-response position as a rank.

## Files

| File | Role |
|---|---|
| `panel_ai_sec_v1.json` | Frozen prompt panel, 12 base × 3 = 36 variants, corpus doc 11 (compiled July 2026) |
| `common.py` | CSV logging, resume, retries, threading, dry-run |
| `run_openai.py` / `run_gemini.py` / `run_anthropic.py` | One harness per provider |
| `aliases_ai_sec.py` | Category-11 alias table: F5 names, stale names, inaccurate patterns, competitor set, watchlist |
| `score.py` | Scorer and summary tables |
| `cost_report.py` | Measured cost from logged usage |
