# f5-llm-visibility

Measurement program for how large language models name F5 (and competitors) in answers to open-ended category questions, plus the evidence base and F5 solution corpus it is built on. This repo is the **canonical home for everything**: the knowledge base, the source index, the F5 corpus, panels, harness code, raw results, and reports. The Claude Project "LLM Brand Visibility Advisor" holds only the operating instructions (a copy is in `docs/PROJECT-INSTRUCTIONS.md`) and reads from here.

## Layout

| Path | What | Changes via |
|---|---|---|
| `docs/reference/` | Knowledge base (`10`), source index (`11`), alias table (`12`), corpus index (`40`), coverage matrix (`41`) | PR; alias table regenerates when the coverage matrix changes |
| `docs/research/` | The five research runs (`20`–`24`) the knowledge base was distilled from | PR; rarely |
| `docs/corpus/` | F5 solution-area corpus, docs 01–14 (`42`–`55`). Doc 14 is a lookup reference, never a panel category | PR; a refresh bumps `compiled` / `last_validated` and regenerates affected panels |
| `docs/` | Pilot plan (`60`), human-readable panel records (`61`…), Project instructions | PR |
| `harness/` | Provider scripts, scorer, cost report, frozen panel JSON | PR; frozen panels are never edited, only versioned |
| `results/` | Raw harness CSVs and completed spot-check files, one folder per cycle | Daniel commits after each run |
| `reports/` | Section 4 reports and leadership front sheets, one folder per cycle | Claude, via PR |

## Working agreement

- **Every change goes through a pull request**, including Claude's. Claude may merge its own PRs. The PR description says what changed and why; the commit carries the session link so a change can be traced back to the conversation that made it.
- Direct pushes to `main` are for nothing. (The first six commits on Sept 14, 2026 predate this rule.)
- A prompt-panel edit is a new panel version and breaks cross-cycle comparison for that category; the PR must say so.
- Reference docs carry their own dates (`Version`, `compiled`, `last_validated`). A PR that changes one updates the date in the file.
- Results are data: never hand-edited. If a run is bad, the folder is deleted in a PR that says why, and the run is redone.

## Cycle workflow

1. Panel is frozen in `harness/panel_<cat>_v<N>.json` and recorded in `docs/`.
2. Daniel runs the harness locally (see `harness/README.md`), then commits `results/<cycle>/*.csv` and the completed `spot_check_sample.csv`.
3. Claude reads the results from the repo, scores, and opens a PR adding `reports/<cycle>/`.
4. Findings that change the evidence base (a new source, a re-scored lever) go into `docs/reference/` by PR with the date updated.

## Current cycle

**AI-SEC-v1** — category 11 (AI Delivery & Security), 12 base prompts × 3 = 36 variants, 30 reps, both conditions, three Sonnet-tier engines. Plan: `docs/60-pilot-plan-ai-security-v1.md`. Budget ~$105 list, ~$155 with contingency. Status: harness delivered; waiting on model-ID pinning and the run.

This repo is private. Results contain full model responses; reports carry F5-internal framing.
