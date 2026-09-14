# f5-llm-visibility

Measurement program for how large language models name F5 (and competitors) in answers to open-ended category questions. Methodology follows the LLM Brand Visibility knowledge base (Section 3: frozen prompt panels, 30+ repetitions, search-off and search-on conditions, alias-based mention scoring, Wilson confidence intervals, share of model).

## Layout

| Path | What | Who changes it |
|---|---|---|
| `harness/` | Provider scripts, scorer, cost report, and the frozen panel JSON | Claude (code), nobody (frozen panels) |
| `docs/` | Pilot plan, human-readable panel record, per-cycle notes | Claude |
| `docs/reference/` | Snapshots of the knowledge base, alias table, corpus index, and the corpus doc(s) a panel was built from | Claude, when the Project versions change |
| `results/` | Raw harness CSVs from each run, plus the filled-in spot-check file | Daniel, after each run |
| `reports/` | Section 4 reports and leadership front sheets, one folder per cycle | Claude |

## Cycle workflow

1. Panel is frozen in `harness/panel_<cat>_v<N>.json` and recorded in `docs/`.
2. Daniel runs the harness locally (see `harness/README.md`), then commits `results/<cycle>/*.csv` and the completed `spot_check_sample.csv`.
3. Claude reads the results from the repo, scores, and commits `reports/<cycle>/`.
4. Any change to prompts, aliases, or competitor sets is a commit with a message saying why; a prompt change is a new panel version and breaks cross-cycle comparison for that category.

## Current cycle

**AI-SEC-v1** — category 11 (AI Delivery & Security), 12 base prompts x 3 = 36 variants, 30 reps, both conditions, three Sonnet-tier engines. Plan: `docs/60-pilot-plan-ai-security-v1.md`. Budget ~$105 list, ~$155 with contingency.

This repo is private. Results contain full model responses; reports carry F5-internal framing.
