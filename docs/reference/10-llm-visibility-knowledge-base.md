# LLM Brand Visibility — Knowledge Base

**Version 1.0 · August 2026 · Companion to `11-source-index.md`**

---

## 0. How to use this document

**If you are the agent:** read this file in full before answering any question about LLM answer optimization, AI visibility, generative engine optimization, share of model, or how to make a brand appear in AI-generated recommendations. Every claim below carries a source reference (e.g., `[A1.1]`) and an evidence tier. When you make a recommendation, cite the reference and state the tier. Open the source index only when you need the score breakdown, flags, or URL. Open the underlying paper only when a user challenges a specific figure or asks for methodology detail.

**If you are a human:** this document is the distilled state of the evidence as of August 2026. Section 1 is the mental model. Section 2 is what works and what doesn't. Section 3 is how to measure. Sections 4–6 are reporting, competitive intelligence, and threats. The appendices hold foundations and the F5 worked example. Everything is cited so you can check it.

**Evidence tiers used throughout:**

| Label | Meaning | How the agent may use it |
|---|---|---|
| **Strong** | Class A, 10–12 | State as a finding |
| **Solid** | Class A, 7–9 | State as a finding with the caveat noted |
| **Provisional** | Class A, 4–6 | "Preliminary evidence suggests"; never the sole basis for a recommendation |
| **Weak** | Class A, 0–3 | Mention only to explain why it is not relied on |
| **Platform** | Class B | Authoritative for mechanism; not for strategy |
| **Industry** | Class C | "Industry data indicates"; must be paired with Strong/Solid/Platform before becoming a recommendation |
| **Inferred** | Any tier, flagged EXTRAPOLATED | The research studied something other than brands; the application is reasoned, not tested |

**Lever verdicts used in Section 2:**

- **PROVEN** — Strong or Solid Class A evidence, corroborated
- **PLAUSIBLE** — mechanism supported, effect not directly measured for brands
- **NOISE** — no evidence, or platform documentation explicitly says it does not matter
- **DO NOT RECOMMEND** — demonstrated effective but deceptive, against platform terms, or both

---

## 1. The mechanism model: three paths to a brand mention

When a language model names a brand in response to an open-ended question ("what should I use for X?"), the name arrived through one of three paths. They have different physics, different levers, different timescales, and different evidence quality. Nearly every confusion in this field comes from treating them as one thing.

### 1.1 Path P — Parametric recall (the model remembers you)

The brand-category association was present in pretraining data often enough, and in varied enough forms, that the model reproduces it without any external lookup.

**What is established (Strong, Inferred):**

- Recall of an entity scales roughly log-linearly with how many pretraining documents connect it to the relevant answer. The long tail is essentially unlearned, and making the model larger does not fix it. `[A2.1]` Kandpal et al. measured this for factual QA with R² = 0.98 on the scaling trend.
- Popularity predicts recall. Entities with high Wikipedia pageviews are recalled; unpopular ones are not, across model sizes. `[A2.4, A2.5]` The best model in Sun et al.'s Head-to-Tail benchmark reached only ~31% on tail facts.
- What the model learns is co-occurrence, not truth or relevance. It prefers the entity that most often appears next to the category term, even when that is wrong. `[A2.6]` This is the mechanism behind incumbent dominance: the incumbent co-occurs with the category term in more documents.
- A fact must appear in varied phrasings to become extractable. Memorized but unaugmented facts yield near-zero QA accuracy. `[A2.7]` One canonical sentence repeated verbatim is far weaker than the same association stated many ways across many sources.
- Reference-quality sources are upweighted. Published data mixtures show Wikipedia sampled at 2.5–3.4 epochs versus Common Crawl below 1 epoch. `[A2.22]` Closed frontier models do not disclose their mixtures, so this is Inferred for GPT, Claude, and Gemini.
- Post-training narrows what gets volunteered. RLHF reduces output diversity substantially. `[A2.17]` A model that "knows" twelve brands in a category will tend to volunteer the same three.
- Reasoning does not rescue weak storage. Chain-of-thought helps math and logic, not factual recall. `[A2.18]` A brand that is weakly stored will not surface because the model "thinks harder."
- The association must predate the model's effective knowledge cutoff, which often lags the stated one because of stale duplicated web content. `[A2.12]`
- Parametric associations are hard to change after training. Fine-tuning on new facts is slow and increases hallucination; model editing has ripple effects. `[A2.13]` There is no post-hoc patch a brand can request.

**What is not established:** none of these studies tested commercial brands. They tested birthdays, capitals, biographies, and arithmetic. The extension to "brand X for category Y" is reasoned from identical mechanisms but is untested. Every parametric recommendation must say so.

**Timescale:** 12–24 months from content change to model behavior change, because models retrain on that cadence. `[A1.14 notes; A2.12]` No attribution is possible: by the time a new model ships, everything else has changed too.

### 1.2 Path R — Retrieval / grounding (the model looks you up)

The model, or the system around it, runs a web search or queries an index, retrieves pages, and synthesizes an answer that cites them. Consumer products (ChatGPT search, Gemini, Copilot, Perplexity, Google AI Overviews/AI Mode) do this by default for most open-ended questions.

**What is established:**

- Content edits change citation rates. Adding statistics, quotations, and citations to a page raised its visibility in generative-engine answers by 30–40% on one metric and 15–30% on another. Keyword stuffing fell below baseline. `[A1.1]` Strong. Direction reproduced by `[A1.8, A1.9]`.
- The effect is largest for low-ranked sources and can hurt top-ranked ones. Rank-5 sources gained ~100–115%; rank-1 sources sometimes lost. `[A1.1]`
- Generative features are built on the existing search index. Google states its AI features are "rooted in core Search ranking and quality systems" and a page must be indexed and snippet-eligible to appear. `[B1.1]` Platform.
- Retrieval eligibility and training inclusion are governed by different crawlers. Blocking GPTBot does not block OAI-SearchBot; blocking ClaudeBot does not block Claude-SearchBot; Google-Extended is a training control with no Search effect. `[B1.3, B3.1, B4.1, B5.1, B6.1]` Platform.
- Retrieved content can override the model's prior. In ClashEval, models adopted retrieved content over their own correct prior more than 60% of the time; the more implausible the retrieved content, the more they fell back on the prior. `[A2.16]` Strong. This is the mechanism by which retrieval helps a challenger — and the reason it does not always help.
- Providers cite very different sources. Overlap between engines is low, and citation source mixes drift week to week (56–74% weekly drift for AI Mode and ChatGPT in one study). `[A1.13; C1.11]`
- Earned (third-party) media dominates citations over brand-owned content across engines. `[A1.9]` Solid; corroborated `[C1.1, C1.3, C1.5]`; one dissent `[C1.13]`.
- Freshness matters directionally. Roughly two-thirds of AI bot hits target content less than a year old. `[C1.8]` Industry; Microsoft names freshness among factors. `[B2.1]`

**Timescale:** days to weeks for crawl and index; a quarter to see stable citation-share movement.

### 1.3 Path C — Context (the model is told about you)

The brand enters through the system prompt, uploaded documents, organizational data, conversation memory, tool descriptions, or the agent harness. This is the dominant path in enterprise deployments and developer agents.

**What is established:**

- Enterprise copilots ground on tenant data first. Microsoft 365 Copilot retrieves from a per-tenant semantic index over Microsoft Graph, bounded by the user's permissions, and combines this with web grounding. `[B2.2]` Platform. Gemini for Workspace and Claude for Enterprise have equivalent connector-based grounding. `[B4.2]`
- Position in context matters. Models use information at the beginning and end of a context window better than the middle. `[A4.10]` Strong. Reordering candidates changes verdicts. `[A4.11]` Strong.
- Shopping agents show choice homogeneity, strong position bias, penalize sponsored tags, and reward platform endorsements; preferences reshuffle across model updates. `[A1.6]` Solid.
- Product descriptions that preserve facts, surface concrete attributes, and organize for comparison outperform other rewrites when the model is choosing among listed options. `[A1.8]` Solid.

**What is not established:** there is no research on developer agents (Claude Code, Cursor, Copilot) as a recommendation surface. ACES `[A1.6]` studies shopping agents. The mechanism (context dominates; the codebase and existing dependencies shape suggestions) is Inferred.

**Timescale:** immediate, but only within the deployment you control or influence.

### 1.4 Why the paths interact

- A brand strong on Path P will often override Path R content that contradicts it. `[A2.14, A2.15]` This is why incumbents survive challenger GEO for a while.
- A brand absent from Path P depends entirely on Path R and Path C. Retrieval is the proven rescue for tail entities. `[A2.1, A2.4]`
- Consumer product behavior is not API behavior. API calls, especially search-off, measure Path P; the consumer app usually measures P + R, sometimes + C (memory, personalization). Many studies conflate these. `[C1.9, C1.11, index notes]`

---

## 2. Signal catalog — every lever, with a verdict

Format: **Lever** · Path · Verdict · Evidence · Owning function · Timescale · Notes

### 2.1 Levers for Path R (retrieval) — the actionable set

**Earned third-party coverage in sources the engines trust**
Path R (and P over time) · **PROVEN** · `[A1.9]` Solid, `[C1.1, C1.3, C1.5]` Industry, `[B1.1]` Platform (warns against inauthentic mentions, implying authentic ones matter) · PR/AR, DevRel, community · 1–2 quarters
The single best-corroborated lever. Reviews, comparisons, tutorials, forum answers, analyst coverage, and conference content on domains the engines already cite. Which domains are trusted varies by engine and language `[C1.9, C1.11]`; measure first. YouTube mentions had the strongest correlation with visibility in the largest industry study (ρ ≈ 0.737) `[C1.1]` — Industry, correlational.

**Statistics, quotations, and citations in owned content**
Path R · **PROVEN** · `[A1.1]` Strong; direction reproduced `[A1.8, A1.9]` · Content/docs · Weeks to index, a quarter to measure
Concrete numbers, quotable sentences attributed to named sources, and outbound citations to authoritative pages. Effect strongest for pages not already ranking well. Note: one unread benchmark `[A1.17]` may revise the magnitude.

**Crawler access hygiene**
Path R · **PROVEN** (mechanism) · `[B1.3, B3.1, B4.1, B5.1, B6.1]` Platform · Web/infra · Days
Allow the search crawlers (Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, PerplexityBot, meta-webindexer) regardless of the training decision. Check server logs for 403/429 to these agents. WAFs commonly block them by accident. This is a prerequisite, not an optimization.

**Indexed and snippet-eligible pages with server-rendered content and semantic HTML**
Path R · **PROVEN** (eligibility) · `[B1.1]` Platform; `[A1.12]` Provisional for magnitude · Web/content · Weeks
Google's stated prerequisite. GEO-16 found semantic HTML and metadata correlate with citation (Provisional, COI). Treat as hygiene.

**Freshness and dated updates**
Path R · **PLAUSIBLE** · `[C1.8]` Industry, `[B2.1]` Platform names it as a factor · Content · Ongoing
Directional evidence only. Do not fake dates; update content substantively.

**Comparison-ready, fact-dense product content matched to buyer intent**
Path R and C · **PROVEN** in e-commerce · `[A1.8]` Solid, `[A1.6]` Solid · Product marketing · Weeks
The "universally effective" GEO strategy from E-GEO: preserve facts, surface concrete attributes, organize for comparison, match query intent. Consumer-goods evidence; transfer to enterprise tech is Inferred.

**Q&A-structured content**
Path R · **PLAUSIBLE** · `[C1.3]` Industry (25% citation advantage claimed) · Content · Weeks
Single vendor finding. Plausible because it matches how grounding queries are phrased `[B2.1]`.

**Per-language content and tracking**
Path R and P · **PROVEN** that visibility does not transfer across languages · `[A2.20]` Strong, `[A2.21]` Solid, `[C1.9, C1.11]` Industry · Content/localization · Quarters
Cross-lingual factual consistency is low and scaling does not fix it. ChatGPT cited 68% English sources for German queries. English tracking is a proxy at best. Each target language is a separate optimization problem.

**Structured data / schema markup**
Path R · **NOISE for AI features specifically** · `[B1.1]` Platform: "not required for generative AI search" · Keep for rich results only
Google explicitly says no special schema is needed. No other provider documents schema as an AI signal.

**llms.txt**
Path R · **NOISE** · `[B1.1]` Platform: Google "doesn't use them"; no provider documents it as a signal
Harmless, useless.

**Content "chunking" or rewriting for AI**
Path R · **NOISE** · `[B1.1]` Platform, explicitly debunked
Write for readers; the models read the same thing.

**Keyword stuffing**
Path R · **NOISE, possibly harmful** · `[A1.1]` Strong: fell below baseline · —
The one classic SEO tactic the peer-reviewed evidence says backfires.

**Backlinks / domain authority as a direct AI signal**
Path R · **PLAUSIBLE but weak** · `[C1.1]` backlinks ρ ≈ 0.218; `[C1.4]` Authority Score predicts topic owner 52.5% of the time · —
Matters for being indexed and ranking, which is the prerequisite `[B1.1]`, but does not predict AI mentions well on its own.

**IndexNow**
Path R (Bing/Copilot) · **PLAUSIBLE for discovery only** · `[B2.3]` Platform: "does not guarantee indexing, ranking, or citation" · Web · Days
Reduces discovery lag on Bing surfaces. Not a citation lever.

**Paid placement / provider content deals**
Path R · **PLAUSIBLE, not organic** · `[B3.3, B5.2]` · Commercial · —
OpenAI licensing deals and Perplexity's revenue share affect discoverability for publishers, not ranking mechanics. ChatGPT ads exist on free tiers. Not a lever for a B2B vendor's organic visibility; monitor for competitor sponsorship.

### 2.2 Levers for Path P (parametric) — slow, unattributable, all Inferred

**Sustained, high-frequency brand–category co-occurrence across many independent domains**
Path P · **PLAUSIBLE (Inferred from Strong)** · `[A2.1, A2.4, A2.6]` · PR/AR, DevRel, docs, community · 12–24 months
The model learns "X is a load balancer" by seeing X near "load balancer" in thousands of documents from many sources. Docs, forums, Q&A sites, tutorials, conference talks, job postings, comparison articles, and Wikipedia all contribute. Volume and independence of sources matter more than any single authoritative page.

**Varied phrasing of the association**
Path P · **PLAUSIBLE (Inferred from Solid)** · `[A2.7]` · Content/PR · 12–24 months
The same fact restated many ways is extractable; one boilerplate sentence syndicated everywhere is not. Encourage third parties to describe the brand in their own words.

**Presence in reference-class sources (Wikipedia, standards bodies, academic papers, major documentation hubs)**
Path P · **PLAUSIBLE (Inferred)** · `[A2.22]` data mixtures upweight these · PR/AR, DevRel · Years
Likely disproportionate weight per mention. Exact weighting undisclosed for frontier models. Wikipedia presence should be accurate and stable, not promotional; editing it promotionally violates Wikipedia policy and would be caught.

**Getting the association in before the next training cutoff**
Path P · **PLAUSIBLE (Inferred from Strong)** · `[A2.12]` · All · Continuous
Content published today may not affect any model for a year or more, and effective cutoffs lag stated ones.

**Fine-tuning, model editing, or "training partnerships" to fix a brand's representation**
Path P · **NOISE for a brand** · `[A2.13]` Strong, `[A2.11]` · —
Not available to brands, and the research shows post-hoc knowledge injection is brittle. Any vendor selling "get your brand into the model" is selling Path R or nothing.

**Training-data seeding at scale (mass content generation to flood the corpus)**
Path P · **DO NOT RECOMMEND** · `[A3.4]`; Google spam policy `[B1.4]` names scaled content abuse · —
Slow, unattributable, likely caught as spam, and deceptive if the content is not genuine.

### 2.3 Levers for Path C (context) — control what you can

**Enterprise knowledge presence (tenant documents, connectors, internal wikis)**
Path C · **PROVEN (mechanism)** · `[B2.2, B4.2]` Platform · IT, sales enablement · Weeks
If a buyer's Copilot grounds on their tenant data, the brand appears when it is in that data: RFP responses, vendor evaluations, architecture docs, past contracts. This is a sales-enablement lever, not a marketing one: make it easy for customers to have accurate, current material about you inside their systems.

**Fact-dense, comparison-structured product content**
Path C · **PROVEN in shopping agents** · `[A1.6, A1.8]` Solid · Product marketing · Weeks
When the model is choosing among options it was handed, concrete attributes beat persuasive prose.

**Developer-facing documentation, SDKs, and examples in code-adjacent sources**
Path C and P · **PLAUSIBLE (Inferred)** · No direct evidence; mechanism from `[A4.10]` and `[A1.6]` · DevRel · Quarters
For developer agents, the codebase and installed dependencies are the context. Being the thing already in the repo, or the thing whose docs the agent fetches cleanly, is the lever. Unmeasured.

**Position and ordering in any list the model sees**
Path C · **PROVEN** · `[A4.10, A4.11]` Strong · Whoever controls the list · Immediate
Only controllable in your own deployments or partner integrations. Not a public lever.

### 2.4 What is almost certainly noise (consolidated)

Ranked by how often vendors sell it:
1. llms.txt `[B1.1]`
2. Schema markup specifically for AI `[B1.1]`
3. "AI rank position" as a metric — per-response rank is random; the consideration set is the stable unit `[C1.5]`
4. Rewriting or chunking content for AI `[B1.1]`
5. Keyword density or stuffing `[A1.1]`
6. Backlink campaigns aimed at AI visibility `[C1.1, C1.4]`
7. Blocking training crawlers to "protect" visibility (it changes nothing about search inclusion) `[B1.3, B3.1, B4.1]`
8. Single-engine measurement — engines diverge sharply `[A1.13, C1.11]`
9. Any promise of parametric lift within a quarter `[A2.12]`

---

## 3. Testing methodology

The purpose of measurement is to detect changes in the probability that a brand appears in the answer to an open-ended category question, per engine, per surface, per language, over time, relative to competitors. Everything below follows from the finding that per-response output is noise and the consideration set is the signal. `[C1.5]`

### 3.1 The three surfaces

| Surface | What it measures | Method | Cadence | Reliability |
|---|---|---|---|---|
| **API** | Path P (search off) and P+R (search on), no personalization | Scripted harness | Weekly to monthly | High; reproducible |
| **Consumer product** | What buyers see: P + R + memory + product system prompt | Manual panel or browser automation on clean accounts | Monthly | Medium; noisy, unscriptable, changes without notice |
| **Agent harness** | Developer tools with codebase context | Manual scenario tests | Quarterly | Low; no established method |

The API tier is the instrument; the consumer tier is the ground truth check; the agent tier is exploratory. Report them separately. Never describe API results as "what ChatGPT recommends." `[index notes]`

### 3.2 Prompt panel design

- **Categories:** one panel per solution category (the agent regenerates this from the F5 corpus when provided).
- **Prompts per category:** 10–20 base prompts covering the buyer's phrasing spectrum: problem-first ("my API gateway can't handle X"), category-first ("best load balancer for Y"), comparison ("A vs B for Z"), constraint-led ("cheapest / most secure / Kubernetes-native option for W"), and persona-led ("as a platform engineer at a bank…").
- **Paraphrases:** 3–5 per base prompt. Phrasing sensitivity is documented. `[A1.9]`
- **Do not include the brand name** in open-ended prompts. That measures aided recall, a different quantity. Run a separate aided panel if wanted.
- **Language:** native-language prompts, not translations, for every market that matters. `[C1.9]`
- **Versioning:** the panel is frozen per cycle. Changing prompts mid-cycle invalidates comparison.

### 3.3 Run parameters

- **Repetitions:** 30 minimum, 60–100 preferred, per prompt variant per model per condition. `[C1.5]` Below 30, confidence intervals on mention rate are typically wider than ±10 points and the result is uninterpretable.
- **Temperature:** the product default (usually 1.0 or provider default), not 0. Temperature 0 does not produce determinism and does not represent what users see.
- **Conditions:** search-off and search-on as separate runs where the API allows. Log the condition on every row.
- **Model pinning:** record exact model ID and date on every row. Never compare across model versions; re-baseline on every release. `[A1.6]` shows model updates reshuffle outcomes.
- **Output capture:** full response text, plus any citation metadata the API returns.

### 3.4 Mention scoring

**Tiered scheme (default; requires human sign-off before first baseline):**

| Tier | Definition | Weight |
|---|---|---|
| Full | Parent brand named, or a product named with the parent brand attached | 1.0 |
| Partial | Product named without the parent brand (e.g., "NGINX" alone) | 0.5 |
| Contextual | Brand appears only in a negative, historical, or "alternatives to" framing | 0.25 |
| None | Absent | 0 |

Report the unweighted Full-only rate and the weighted rate side by side. Whether Partial counts is a brand-architecture decision, not a measurement one; the agent proposes, the organization decides.

**Alias and accuracy handling (added after corpus review).** Models trained on older data use former product names and may recommend discontinued products. The scoring pass therefore uses an alias table (`12-alias-table.md` for F5) and records two additional flags per mention:
- `stale_name` — a former or retired name used as current (e.g., "APM," "GTM," "Shape," "Silverline"). Scored per the Full/Partial rules, but the **stale-name rate per engine per category is reported separately**. It is the only cheap, direct observable of how old an engine's parametric knowledge of the brand is, and it should move when a new model generation ships.
- `inaccurate` — a recommendation to adopt a discontinued, retired, or non-sellable product as a go-forward choice. Scores 0 and is reported as an **inaccurate-mention rate**. These mentions harm the brand and are a Path R target: the correction needs to exist in the sources the engine retrieves.
A historical reference ("X was discontinued") is Contextual (0.25), not inaccurate.

**Also capture per response:**
- Position of first mention (report as distribution, not a "rank")
- Whether the mention is a recommendation, a neutral listing, or a caveat
- Which competitors appear (the competitor set per category comes from the corpus)
- Cited sources, if any (Path R diagnostics)

### 3.5 Metrics

- **Mention rate** = responses containing a Full mention ÷ total responses, per prompt, per model, per condition. Report with a 95% confidence interval (Wilson interval is fine).
- **Share of model** = brand mention rate ÷ sum of mention rates across the tracked competitor set, per category. Relative measure; the useful one for leadership.
- **Consideration-set membership** = share of prompts where the brand exceeds 55% mention rate. `[C1.5]` uses this threshold for "stable presence."
- **Cited-domain distribution** (search-on only) = which domains are cited, how often, and whether the brand's owned and earned domains appear.
- **Category aggregate** = mean of category mention rates, weighted by category priority if the organization supplies weights.

### 3.6 Statistical minimums before claiming a change

- Two cycles on the same model version with non-overlapping confidence intervals on mention rate, or
- A consistent-direction change across at least three of four tracked engines on the same panel.
Anything less is noise. Weekly citation drift of 56–74% has been measured on some engines. `[C1.11]`

### 3.7 Consumer-tier protocol

- Fresh accounts, no memory, no history, default settings, per engine, per region.
- The same base prompts as the API panel, 10 runs each (manual cost constrains this).
- Screenshot and transcribe. Score with the same scheme.
- Compare to the API search-on condition; large divergence indicates product-layer effects (system prompt, personalization, ads).

### 3.8 Harness cost reference

At August 2026 list prices, ~5,000 calls per frontier model per cycle (250 variants × 10 reps × 2 conditions) costs roughly $100–200 including search tool fees; three models ≈ $300–600 per cycle. Engineering time dominates.

### 3.9 Build versus buy

Third-party tools fall into three architectures: API prompting, browser automation of the consumer product, and licensed consumer panels. `[C2]` Only the panel architecture provides real-user prompt data, which cannot be built in-house. Almost none disclose repetitions, temperature, or search condition. Recommendation: build the API harness (cheap, controllable), buy one browser-automation tool for multi-language consumer coverage, and consider one panel tool only if real prompt-volume data is needed for the business case.

---

## 4. Report template

Each cycle produces one report per category plus an aggregate. Sections:

1. **Header:** cycle date, panel version, models and versions, conditions, repetition count.
2. **Headline:** category share of model, this cycle vs. last, with CI. One sentence on whether the change is statistically meaningful per Section 3.6.
3. **Mention rate table:** brand and each tracked competitor × engine × condition. Full and weighted rates.
4. **Consideration-set status:** which prompts the brand is stable in (>55%), emerging in (25–55%), or absent from (<25%).
5. **Path diagnosis:** search-off vs search-on gap. Large search-on gain → Path R is carrying the brand; Path P is weak. Similar rates → Path P is strong. Search-on *lower* → retrieved content is hurting; investigate cited domains.
6. **Cited-domain analysis:** top cited domains per engine; brand's owned and earned presence among them; gaps.
7. **Competitor movements:** any competitor with a change exceeding Section 3.6 thresholds; check Section 5 patterns.
8. **Consumer-tier check:** agreement or divergence with API tier.
9. **Recommendation queue:** ranked by (evidence tier × expected effect × feasibility), each tagged with lever, path, owning function, timescale, and source reference. Parametric recommendations carry the Inferred label.
10. **Caveats:** model releases during the cycle, panel changes, known confounds.

---

## 5. Competitive intelligence

### 5.1 What to track

- Competitor mention rates and share of model on the same panel (Section 3).
- Cited domains that carry competitors but not the brand — these are earned-media targets.
- Sudden competitor movements exceeding Section 3.6 thresholds.

### 5.2 How incumbents lose and challengers win

Evidence from recommender-system research (Strong) and one directly relevant LLM preprint (Provisional):

- Incumbency acts as a tiebreaker, not a moat. With identical attributes the known brand won 100% of trials; a small legible advantage for a challenger (+0.075 rating, ~7% price, ~1.6× reviews) flipped the outcome. Product attributes explained 82% of ranking variance; brand identity 1.2%. `[A1.11]` Provisional, single-domain.
- Quality sets a floor and ceiling; social influence determines the middle. `[A4.1]` Strong.
- Feedback loops amplify popularity absent exploration or debiasing. `[A4.7, A4.8, A4.9]` Solid.
- Retrieved content overrides the prior most of the time, but less when it is implausible. `[A2.16]` Strong. A challenger's claims need to be credible and third-party-verifiable to override an incumbent's parametric advantage.

Practical reading for a challenger: make the differentiating attributes concrete, verifiable, and present in the sources the engines retrieve. Practical reading for an incumbent: parametric advantage decays as retrieval dominates; defend by being present in fresh, cited, third-party content, not by relying on memory.

### 5.3 Prisoner's dilemma

When one competitor adopts GEO tactics it gains; when all do, individual gains collapse and non-participants get nothing. `[A1.3]` Solid, `[A1.11]` Provisional. Implication: the cost of not participating rises as the category adopts, but the ceiling on returns falls. Budget accordingly and prioritize levers that also serve human readers.

---

## 6. Threats and manipulation — awareness only

**Framing:** the tactics below are documented, often effective, and either deceptive, against platform terms, or both. They are here so the agent can recognize them in a competitor's behavior and advise on detection and reporting. The agent does not recommend them, does not provide implementation detail, and states this when asked.

| Tactic | Path | Reported effect | Detectability | Status |
|---|---|---|---|---|
| Strategic text sequences (optimized strings on a page) | R | rank ~10 → 1 `[A1.7]` | High (gibberish, perplexity filters) | DO NOT RECOMMEND |
| Preference-manipulation prompt injection in page or plugin text | R, C | 34% → 59% recommendation rate; plugins 2–8× `[A1.3]` | Medium | DO NOT RECOMMEND; OWASP LLM01 `[B7.1]` |
| Fabricated authority / social-proof framing | R, C | Broke incumbent monopoly 73% of trials `[A1.11]`; social proof boosts, scarcity backfires `[A1.4]` | Low (human-readable) | DO NOT RECOMMEND when fabricated; authentic, verifiable proof is a legitimate lever |
| RAG / knowledge-base poisoning | R | 90–99% success with 5 injected texts `[A3.1]` | Medium; defenses insufficient | DO NOT RECOMMEND |
| AI-targeted cloaking (different content served to AI user-agents) | R, C | Full leaderboard flips `[A3.3]` | Trivial in principle; not caught in practice | DO NOT RECOMMEND; explicit Google spam violation `[B1.4]` |
| Mass-produced listicle / doorway pages | R | Variable | Increasing under `[B1.4]` | DO NOT RECOMMEND |
| Training-data seeding at scale | P | Undemonstrated at product scale | Low | DO NOT RECOMMEND |

**Detection patterns to watch in competitors** `[Run 5 synthesis]`:
- Rank or mention-rate jump with no change in real-world signals (reviews, pricing, releases, coverage)
- Page content differs when fetched as an AI user-agent versus a browser
- Uniform superlative or "clinically proven"-style language across many third-party pages pointing to one brand
- Competitor claims appearing verbatim as facts in AI answers, traceable to a few recent low-quality sources
- Your own brand described using content you never published

**Response:** document, file platform spam reports (Google's policy now names AI manipulation explicitly `[B1.4]`), escalate to legal if deceptive, and shore up legitimate signals.

---

## 7. Multilingual and regional findings

- Factual knowledge consistency across languages is low; larger models are more accurate but not more consistent. `[A2.20]` Strong.
- Cross-lingual inconsistency is more a problem of access than of missing knowledge; targeted training improves it, but brands cannot request that. `[A2.21]` Solid.
- Query language, more than geography, determines the source mix. Social-citation rates, YouTube share, and Reddit share vary sharply by language. `[C1.9]` Industry.
- ChatGPT cited 68% English sources for German queries while Google AI Mode cited 80% German domains. `[C1.11]` Industry. The engines' source pools barely overlap for non-English markets.
- LLMs favor global brands over local ones and show country-of-origin effects. `[A1.5]` Strong; US entities over-represented relative to real market position. `[A1.10]` Solid.
- Google AI Overviews rolled out to 200+ countries and 40+ languages by May 2025; regulatory delays affected the EU and France. `[Run 4]`

**Implication:** treat each target language as a separate program with its own panel, competitor set, and earned-media targets.

---

## Appendix A — Foundations (condensed)

**A.1 Recommender-system bias.** Collaborative filtering over-recommends popular items; re-ranking can promote the long tail at some accuracy cost. `[A4.3, A4.4]` Recommenders can reduce aggregate diversity even while helping individuals. `[A4.2]` Training on data already shaped by recommendations homogenizes users. `[A4.7]` Exploration and item-pool expansion break lock-in. `[A4.8]` Feedback loops amplify bias over time. `[A4.9]`

**A.2 Position bias in ranked lists.** Users scan top-down; examination decays with rank. `[A4.5, A4.6]` LLMs inherit an analogous bias: best use of context at beginning and end. `[A4.10]` Reordering candidates changes LLM judgments. `[A4.11]` LLMs as rankers are biased by item popularity and prompt position. `[A4.12]`

**A.3 The dissent.** A simple LLM recommender showed less popularity bias than collaborative-filtering baselines, though with much lower accuracy. `[A1.16]` Provisional, COI. This measured ranking over a supplied list, not volunteering from memory. Keep the distinction.

**A.4 Marketing vocabulary.** *Unaided recall*: the brand is named without being prompted with it — what open-ended prompts measure. *Aided recall*: the brand is recognized when named — what "is X a good option?" prompts measure. *Share of voice*: proportion of category conversation a brand occupies — the ancestor of share of model. *Consideration set*: the brands a buyer actively weighs — the stable unit in LLM answers. `[C1.5]` Cumulative advantage: success breeds success independent of quality beyond a floor. `[A4.1]`

**A.5 Memorization mechanics.** Verbatim memorization grows log-linearly with model size, duplication, and context length. `[A2.2]` Deduplication reduces verbatim emission tenfold. `[A2.3]` Facts are stored as key-value associations in mid-layer feed-forward blocks and can be located and edited, with side effects. `[A2.10, A2.11]` Arithmetic accuracy tracks operand frequency in pretraining, suggesting much "reasoning" is frequency lookup. `[A2.8]`

## Appendix B — F5 worked example (illustrative; the corpus supersedes this)

**Observation that started this project:** an open-ended enterprise load-balancing prompt to a frontier model without search returned F5 BIG-IP in the hardware/ADC tier with pros and cons, NGINX and NGINX Plus in the software tier without F5 attribution, and no F5 mention in the cloud-native or Kubernetes tiers.

**Path diagnosis (Inferred):** F5 has strong parametric presence for "ADC / hardware load balancer" — decades of documentation, certifications, community content, and being the reference point competitors are compared against `[A2.1, A2.6]`. NGINX has independent parametric presence that predates the 2019 acquisition; the brand–parent association is weaker in the corpus than either brand alone. Cloud-native and Kubernetes categories are dominated by co-occurrence with hyperscaler and CNCF terms.

**Scoring implication:** under the tiered scheme, the NGINX mention is Partial (0.5). Whether that counts is the sign-off decision flagged in Section 3.4.

**Where the levers point (illustrative, not prescriptive):**
- Path R, PROVEN: earned coverage in the domains engines cite for Kubernetes and API-gateway queries; fact-dense comparison content for F5 Distributed Cloud and NGINX Ingress in the phrasing platform engineers use.
- Path P, Inferred: sustained "F5 NGINX" co-occurrence in third-party content so the parent association strengthens over the next training cycles; presence in reference-class sources for the multicloud and AI-infrastructure categories where the association is new.
- Path C, PROVEN mechanism: sales enablement material that customers keep in their tenant systems, so Copilot-grounded evaluations surface current F5 positioning.
- Noise to decline: llms.txt, AI-specific schema, "AI rank tracking" dashboards, blocking training crawlers.

**Categories to panel (from the corpus, docs 01–13):** API Security; Web App Protection (WAAP); Bot Defense & Online Fraud; DDoS Protection; App Delivery & Load Balancing (ADC); DNS & Global Traffic (GSLB); Access & Zero Trust; Encrypted Traffic Inspection & Crypto; Multicloud Networking; Kubernetes & Modern Apps; AI Delivery & Security; Service Provider & Telco (distinct buyer population — use telco personas); Observability & Insight. Doc 14 (platform reference) is not a category. Prompts come from each doc's `fit_signals`; competitor sets from `12-alias-table.md`.

**F5-specific measurement notes:**
- Expect high stale-name rates on Access (APM), DNS (GTM), and Bot (Shape) categories; treat them as parametric-age readings, not failures.
- Expect some engines to recommend BIG-IP Next as the ADC modernization path. That is an `inaccurate` mention and the single most important Path R correction target: the discontinuation must be present in retrievable third-party content, not only in F5's knowledge base.
- Bare "NGINX" without F5 attribution will be the most common Partial. Its weight is the sign-off decision.
- Several 2025–26 acquisitions in AI security (Lakera, Protect AI, Robust Intelligence, SurePath) mean competitor names in that category are unstable in both directions; track old and new names.

---

## Appendix C — Open questions and update triggers

- **C-SEO Bench** `[A1.17]`: read and score. If it fails to replicate GEO lift on current models, downgrade Section 2.1's statistics/quotations lever from PROVEN to PLAUSIBLE.
- **Any controlled study of brand recall on the parametric path.** Would move Section 1.1 from Inferred to Strong.
- **Any study of developer agents as recommendation surfaces.** Would fill the Path C gap.
- **Provider disclosure of source-selection signals.** Would move Section 2.1 hygiene items from eligibility to ranking.
- **Convergence of engines on citation behavior.** Would restore single-engine measurement (currently NOISE).
- **Ad integration expanding to paid tiers or enterprise products.** Would shift budget analysis toward paid placement.
- **Model release cadence.** Every frontier release requires re-baselining; the agent should ask for the model list and versions at the start of any analysis.

*End of knowledge base.*
