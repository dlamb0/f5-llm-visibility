# Pilot Test Run — AI Delivery & Security (Category 11)

**Panel version:** AI-SEC pilot v1 · **Drafted:** September 14, 2026 · **Corpus basis:** doc 11 `52-f5-11-ai-delivery-security.md`, compiled July 2026, last validated July 2026 · **Status:** base prompts approved Sept 14; panel frozen (36 variants) and harness delivered (`harness/`). Engine tier decision: Sonnet-tier from each provider (see Section 3 and 7, revised).

> **Revision note (Sept 14, later same day).** Daniel chose the mid ("Sonnet") tier from each provider instead of the cheapest tier: Claude Sonnet, OpenAI's mid-tier model (trackers name it GPT-5.6 Terra at $2/$12 — verify the ID against `--list-models`), and Gemini Flash (not Flash-Lite, not Pro). Sections 1, 3 and 7 below were written for the cheapest tier; where they say "cheap tier" read "Sonnet tier." The re-priced budget is in Section 7's revision block. The "proof of instrument, not proof of position" framing still holds, but the model-tier caveat is now much weaker: these are current, widely deployed production models.

---

## 1. What this pilot is, and what it is not

This is a proof of instrument, not a proof of position. It runs the full methodology from knowledge base Section 3 — frozen prompt panel, 30 repetitions, search-off and search-on conditions, alias-based mention scoring, Wilson confidence intervals, share of model — on one category, using the cheapest current API tier from each of three providers. The output is a real Section 4 report with real numbers, built for well under $100, that shows F5 leadership exactly what the measurement program produces and what it would cost to run at full scale.

What it cannot do is tell leadership where F5 stands in AI security. Cheap-tier models are not what buyers use, and per the knowledge base you never describe API output as "what ChatGPT recommends" (Section 3.1, index notes). The numbers in this pilot describe three budget models on a specific date. Every slide that shows a mention rate must carry that label. What does transfer is the mechanism story: the gap between search-off and search-on, the stale-name rate, and the cited-domain list are qualitative findings about how these systems behave, and those are what the frontier-tier program would investigate properly.

One honest note on your $300 assumption: the knowledge base's $300–600 per cycle figure (Section 3.8) is for three frontier models across a 250-variant, all-category panel. A single-category frontier run is much smaller, and the dominant cost is the per-call search fee, not model tokens. A frontier model in the search-off condition only, for this panel, is roughly $15 at current list prices. I've included it as an optional add-on in Section 7 because it removes the "but that's a cheap model" objection for the parametric half of the story at almost no cost.

## 2. Why AI Security is a good pilot category, and why it is also the hardest

It is a good pilot because the mechanism story will be vivid. F5's AI security products are 2025–2026 vintage: AI Guardrails and AI Red Team went GA January 14, 2026; AI Remediate was announced March 2026; the AI Security Platform umbrella and the SurePath AI acquisition landed June 22, 2026 (doc 11, Layer 1). Any model whose effective training cutoff predates those dates cannot know F5 sells them, and effective cutoffs lag stated ones `[A2.12]` Strong. So the search-off condition should show F5 at or near zero, or naming CalypsoAI rather than F5 — and the search-on condition is where retrieval either rescues the brand or does not. That contrast is the single most persuasive slide for leadership, because it demonstrates that Path P (memory) and Path R (retrieval) are different problems with different levers and different timescales (knowledge base Section 1).

It is the hardest category for exactly the same reasons. The competitor set is unstable: Protect AI, Robust Intelligence, Prompt Security, and Lakera were all acquired in 2024–25 and models will cite the old standalone names (doc 11, 3c; alias table note). Scoring has to match old and new names for competitors as well as for F5. The expected stale-name rate for F5 is very high, and it should be presented as the parametric-age diagnostic it is (Section 3.4), not as a failure.

Expectation to set in advance, so nobody is surprised: search-off F5 Full-mention rate across the panel will likely be under 10%, with the few mentions concentrated on the gateway and PII-redaction prompts where "F5 AI Gateway" has existed since late 2024. This is inferred from the release dates above and from the log-linear recall finding `[A2.1]` Strong, applied to a brand — inferred from research on non-brand entities.

## 3. Engines, surface, and conditions

**Surface:** API only. No consumer-product tier in the pilot; it is manual, slow, and not needed to prove the instrument. Say so in the report.

**Engines (cheapest current tier per provider):** one OpenAI mini/nano-class model, one Gemini Flash-Lite-class model, one Claude Haiku-class model. Three providers because engine divergence is large `[A1.13]` Solid, `[C1.11]` Industry, and single-engine measurement is classified NOISE (Section 2.4). Pin the exact model ID at run time and log it on every row; the IDs below are placeholders until you confirm what your keys can reach.

**Conditions:** search-off (no tools) and search-on (provider's native web search / grounding tool), as separate runs with the condition logged per row. Note for the report that the three providers' search tools are not equivalent instruments: Gemini grounding, OpenAI's web search tool, and Anthropic's web search differ in what they retrieve and how many searches they run per call. Cap searches per call at one where the API allows, both for cost and for comparability.

**Temperature:** provider default. Not zero (Section 3.3).

**System prompt:** none, or the provider's default. Do not add instructions like "list vendors" — that changes what is being measured. The prompts themselves are phrased so that naming products is the natural answer.

**Language and region:** English, US, only. State this as a scope limit in the report; cross-lingual visibility does not transfer `[A2.20]` Strong.

## 4. Prompt panel — AI-SEC pilot v1

Built from doc 11 `fit_signals`, jobs 1–4 (runtime security, testing, observability/discovery, workforce governance), with every F5 brand and product name removed and the customer's phrasing kept. Twelve base prompts, each with two paraphrases, giving 36 variants. If you want to trim to ten, drop B8 and B12 first; they are the least buyer-natural.

Prompt types follow Section 3.2: problem-first, category-first, comparison, constraint-led, persona-led. Base prompts are marked with their type. Paraphrases must preserve the type and the intent; they vary wording only.

| ID | Type | Base prompt |
|---|---|---|
| B1 | Problem-first | We're standing up an internal chatbot on top of an LLM and our security team won't let it go to production. What products or tools should we be looking at to secure it? |
| B2 | Category-first | We're calling OpenAI and Anthropic from several internal apps and want one control point in front of all of them for security, PII redaction, and cost control. What are the leading options? |
| B3 | Problem-first | Someone on our team demoed a jailbreak of our customer-facing chatbot. What products detect and block prompt injection and jailbreak attempts at runtime? |
| B4 | Persona-led | I'm a platform engineer at a bank. We run models from three providers plus some open-source ones on our own GPUs, with no consistent security policy across them, and compliance wants an audit trail of every AI interaction for the EU AI Act. What should we evaluate? |
| B5 | Constraint-led | What's the best AI gateway for Kubernetes that can front both self-hosted Llama models and OpenAI, with rate limiting, caching, and PII redaction, and can run on-prem or air-gapped? |
| B6 | Problem-first | We can't let customer PII or source code end up in prompts sent to an external model, and compliance needs proof it was redacted before it left. What tools do this inline? |
| B7 | Category-first | We don't have a full-time AI red team. What automated tools exist for adversarial testing of LLM applications and agents before they go to production? |
| B8 | Constraint-led | We need an independent security benchmark to justify our choice of LLM provider to our risk committee. Are there published rankings of model security, and what vendors offer testing against our own deployment? |
| B9 | Problem-first | Developers are spinning up AI agents and MCP tools and we can't see what they're actually doing or which ones are sanctioned. What gives us visibility into agent traffic? |
| B10 | Problem-first | Employees are pasting customer data into ChatGPT. We blocked it and people just work around the block. What products let us give staff a sanctioned AI portal with data redaction and an audit trail instead? |
| B11 | Constraint-led | We have no idea how many AI tools our employees are using. What detects shadow AI on the corporate network, agentless on managed devices, and plugs into our existing SASE, DLP, and SIEM rather than replacing them? |
| B12 | Comparison | Compare the leading enterprise AI security platforms for a CISO who wants governance, discovery, security testing, and runtime protection in one place rather than five point tools. |

**Paraphrase rules.** Two per base prompt (P-a, P-b). Keep the buyer role, the constraint, and the ask; change sentence structure and vocabulary. Do not introduce or remove a constraint. The full paraphrase set is frozen in `harness/panel_ai_sec_v1.json` and recorded in `docs/61-panel-ai-sec-v1.md`; it is never edited mid-cycle (Section 3.2).

**What is deliberately excluded.** Jobs 5 (DPU/AI-factory delivery, S3 data path) per your scope decision — different buyer, different competitor set, and doc 11 itself flags the S3 case as repositioned ADC function. AI Remediate is not prompted standalone because the corpus says it has no standalone value without Red Team and Guardrails. No aided-recall prompts ("is F5 a good option for…") in this pilot; that is a separate quantity (Section 3.2) and can be a follow-on.

## 5. Scoring

**F5 alias set for this category** (from `12-alias-table.md`, doc 11 rows): F5 AI Gateway, F5 AI Guardrails, F5 AI Red Team, F5 AI Remediate, F5 AI Security Platform, F5 Labs CASI/ARS, NGINX with MCP context, BIG-IP Next for Kubernetes (if it appears on a job 1–4 prompt, count it but note it is off-scope). Stale names to match and flag `stale_name`: CalypsoAI, SurePath AI, LeakSignal. "F5" bare with a security context counts Full. Bare "NGINX" counts Partial (0.5) and is the Partial-weight sign-off decision from Section 3.4; for the pilot, report Full-only and weighted side by side and let leadership see both.

**Inaccurate flag** in this category: any recommendation of BIG-IP Next (the discontinued ADC line) as a go-forward product. Unlikely on these prompts, but the scorer checks anyway, because it is the highest-risk error in the corpus and worth a sentence in the report if it appears even once.

**Competitor set** (share-of-model denominator). From the alias table, doc 11 row, with the corpus-marked names first: HiddenLayer, Lakera (now Check Point), Protect AI (now Palo Alto Networks / Prisma AIRS), Robust Intelligence (now Cisco), Prompt Security (now SentinelOne), Cloudflare AI Gateway, Kong AI Gateway, Zscaler, Netskope, Portkey, LiteLLM. Each acquired vendor is scored under both its standalone name and its acquirer's product name, and the standalone-name-only mentions are reported as a competitor stale-name rate too — it is the same parametric-age diagnostic pointed at the field. Names the alias table lists as unconfirmed additions (Zscaler, Netskope, Portkey, LiteLLM) and any I would add for jobs 1–4 (NVIDIA NeMo Guardrails, AWS Bedrock Guardrails, Azure AI Content Safety, Google Model Armor, Cisco AI Defense as the current Robust Intelligence name) need your confirmation before the first baseline, per the project rule on unmarked names. Anything else that shows up in more than 5% of responses gets added to a watch list and reported, but not to the denominator mid-cycle.

**Per-response capture:** Full/Partial/Contextual/None for F5 and each competitor; `stale_name`; `inaccurate`; position of first F5 mention; recommendation versus neutral listing versus caveat; cited domains (search-on).

**Scorer:** regex over the alias table for the first pass, then a human spot-check on a random 10% of responses plus every response flagged Contextual or ambiguous. For 6,480 responses that is ~650 to eyeball, which is an afternoon. An LLM-assisted scoring pass is possible and cheap but adds a second model's judgment to the measurement; for the pilot I would keep it regex plus human, so the method is explainable to leadership without caveats.

## 6. Run parameters and what the statistics can and cannot say

36 variants × 30 repetitions × 2 conditions = 2,160 calls per engine, 6,480 total. Thirty is the Section 3.3 floor.

Be clear with leadership about resolution. At n = 30 per variant, a 50% mention rate has a Wilson 95% interval of roughly 33–67%, and a 10% rate has an interval of roughly 4–26%. Per-variant numbers are therefore coarse. Pooling the three paraphrases gives n = 90 per base prompt (50% → 40–60%; 10% → 5–18%), and the category aggregate is n = 1,080 per engine per condition (50% → 47–53%). Report at base-prompt and category level; show per-variant only as a phrasing-sensitivity exhibit `[A1.9]`. There is no "last cycle" to compare against, so the Section 3.6 change thresholds do not apply; the report says this explicitly and shows what a second cycle would need to look like to claim movement.

## 7. Budget

Prices below are September 2026 list prices as reported by third-party trackers; confirm on the provider pricing pages when you set up billing, and expect the OpenAI search-fee line in particular to need checking. Assumptions: ~200 input and ~600 output tokens per search-off call; ~4,000 input (retrieved content) and ~900 output per search-on call; one search per search-on call.

| Line | Basis | Estimate |
|---|---|---|
| OpenAI mini/nano tier, tokens, both conditions | $0.15 in / $0.60 out per M (4o-mini-class reference) | ~$1.50 |
| OpenAI web search fee | 1,080 calls × ~$0.010 (verify) | ~$11 |
| Gemini Flash-Lite, tokens, both conditions | $0.25 in / $1.50 out per M | ~$3.50 |
| Gemini grounding fee | 1,080 calls; within the 5,000/month free allowance for Gemini 3 models | $0 |
| Claude Haiku, tokens, both conditions | $1.00 in / $5.00 out per M | ~$12.50 |
| Anthropic web search fee | 1,080 calls × $0.010, capped at one search per call | ~$11 |
| **Subtotal, three cheap engines** | | **~$40** |
| Contingency (retries, longer outputs, a second search per call slipping through) | 50% | ~$20 |
| **Pilot budget** | | **~$60** |
| Optional add-on: one frontier model, search-off only | 1,080 calls at $4 in / $20 out per M | ~$16 |
| **Pilot with frontier search-off add-on** | | **~$80** |

**Revised budget — Sonnet tier (decision Sept 14).** Same assumptions, same 2,160 calls per engine. Where the cost goes, in order: output tokens (the biggest line at this tier), search-on input tokens (~4,000 retrieved tokens per call), search fees (identical at any tier), and hidden reasoning tokens (the harness forces reasoning/thinking to minimum where the API allows, since reasoning does not help recall `[A2.18]` Strong).

| Line | Basis | Estimate |
|---|---|---|
| OpenAI mid tier, tokens, both conditions | $2 in / $12 out per M (verify) | ~$31 |
| OpenAI web search fee | 1,080 × ~$0.010 (verify) | ~$11 |
| Gemini Flash, tokens, both conditions | $0.75 in / $3.75 out per M (promotional; doubles Jan 2027) | ~$10 |
| Gemini grounding fee | within the 5,000/month free allowance | $0 |
| Claude Sonnet, tokens, both conditions | $3 in / $15 out per M | ~$41 |
| Anthropic web search fee | 1,080 × $0.010, max_uses=1 | ~$11 |
| **Subtotal, three Sonnet-tier engines** | | **~$105** |
| Contingency (retries, longer outputs, reasoning tokens that can't be disabled) | 50% | ~$50 |
| **Pilot budget** | | **~$155** |

For reference, the same panel on the cheapest tier was ~$40 (~$60 with contingency) and on the flagship tier ~$150–180 (~$225–270 with contingency). The Sonnet tier buys most of the credibility of the flagship run for a bit over half the money. `cost_report.py` in the harness turns the logged token counts into a measured figure once the run is done; use that, not this table, for the scale-up slide.

For the scale-up conversation, the full program is roughly: 13 categories × ~36 variants × 30 reps × 2 conditions × 3 frontier engines ≈ 84,000 calls per cycle. At frontier token prices and current search fees that lands in the low four figures per cycle, with engineering and scoring time dominating, which is consistent with the knowledge base's framing (Section 3.8). The pilot's per-call cost data replaces that estimate with a measured one.

## 8. Timeline

Day 1: panel frozen and harness delivered (done Sept 14). Day 2–3: Daniel pins model IDs, smoke-tests, runs the harnesses locally; at provider rate limits this is a few hours of wall time, mostly waiting. Commit `results/`. Day 3–4: scoring, human spot-check, analysis. Day 5: report per Section 4 plus a two-slide summary for leadership, committed to `reports/`.

## 9. What the leadership deliverable says

The report follows Section 4 exactly, with a one-page front sheet written for a non-technical reader. The front sheet makes four points, in order.

First, the instrument works: here is a frozen panel, here are 6,480 logged responses, here are mention rates with confidence intervals and a share-of-model number for AI security across three engines, all reproducible from the CSVs.

Second, the mechanism is visible in the data: here is the search-off rate next to the search-on rate for F5 and for each competitor, and here is the stale-name rate showing that these models' memory of the category predates F5's product launches. Explain in one paragraph that the search-off number is the 12–24-month problem with no attribution `[A2.12]` and the search-on number is the one-to-two-quarter problem where earned coverage in cited domains is the proven lever `[A1.9]` Solid, `[A1.1]` Strong.

Third, the cited-domain list is an action list: here are the domains the engines cite for AI security prompts, here is which of them mention competitors and not F5, and that is the earned-media target list for the AI security PR and DevRel functions (Section 5.1). This is the slide that turns measurement into a request for a program.

Fourth, the caveats, stated plainly: Sonnet-tier models, English only, API surface only, one cycle so no change claims, and a corpus compiled July 2026. Then the scale-up cost, measured rather than estimated.

**What this run is and is not a representation of (added Sept 14).** It is a true measurement of how three current production models answer these prompts on the API surface on a given date. It is not "F5's position" as leadership will hear it, for reasons independent of model tier: the API surface is not the consumer product (Section 3.1); Perplexity, Copilot, and Google AI Mode are not covered `[A1.13]`, `[C1.11]`; one category, English only, one cycle; constructed prompts rather than real prompt volume (Section 3.9). The tier caveat is the smaller one: search-on is driven by retrieved content `[A2.16]` Strong, and on search-off a mid-tier model is a slightly pessimistic instrument for tail recall `[A2.1]`, `[A2.4]` — inferred from research on non-brand entities. The cheapest upgrade from instrument proof to first real read is the Section 3.7 consumer-tier check: the 12 base prompts, 10 runs each, fresh accounts in ChatGPT, Gemini, and Perplexity, scored with the same alias table.

## 10. Things that would break the pilot

Running with the brand name in the prompts (that measures aided recall). Changing a prompt after the first call. Comparing across model IDs if a provider ships an update mid-run — log the ID and re-run any variant that spans two IDs. Presenting any per-response "rank." Presenting the cheap-tier numbers as F5's market position. Treating a Gemini grounded call and an OpenAI web-search call as the same instrument without saying they differ.

---

*Panel prompts are derived from `52-f5-11-ai-delivery-security.md` (compiled July 2026). A corpus refresh regenerates this panel as v2 and breaks cross-cycle comparison for this category.*
