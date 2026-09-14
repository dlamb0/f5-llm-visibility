# docs/reference/

The canonical evidence base and scoring references. These are not snapshots; this is where they live and where they change (by PR, with the in-file date updated).

| File | What | Date in file |
|---|---|---|
| `10-llm-visibility-knowledge-base.md` | The distilled state of the evidence: mechanism model, lever catalog with verdicts, testing methodology, report template, competitive intelligence, threats | v1.0, August 2026 |
| `11-source-index.md` | Evidence register: every `[A1.1]`-style reference with class, score, tier, flags, URL | — |
| `12-alias-table.md` | F5 current/former/retired names, inaccurate list, ambiguous terms, per-category competitor sets. Derived from `41` | July 2026 validation |
| `40-f5-corpus-index.md` | Entry point to the F5 corpus (sanitized; safe for any repo). How the visibility agent uses the corpus | — |
| `41-coverage-matrix.md` | Maps every GA F5 product to the corpus docs that cover it; former-name and retired-product tables | — |

The corpus docs themselves are in `docs/corpus/`; the research runs the knowledge base was built from are in `docs/research/`.

Update triggers (from the knowledge base, Appendix C): a controlled study of brand recall on the parametric path; any study of developer agents as recommendation surfaces; provider disclosure of source-selection signals; C-SEO Bench read and scored; every frontier model release (re-baseline).
