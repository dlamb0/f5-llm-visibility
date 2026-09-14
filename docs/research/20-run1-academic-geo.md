# Academic Literature on Generative Engine Optimization and AI Brand Visibility (2023–2026)

## TL;DR
- A real, fast-growing academic literature now exists on how brands and websites become visible in LLM answers, anchored by Aggarwal et al.'s "GEO" (KDD 2024) and Pfrommer et al.'s "Ranking Manipulation" (EMNLP 2024); the strongest, most-replicated finding is that adding citations, quotations, statistics, and authority/social-proof language reliably raises a source's or product's visibility, while classic keyword stuffing does not.
- The evidence splits cleanly by pathway: parametric-recall work (Mallen et al.; brand-bias audits) shows popular/incumbent/global brands dominate open-ended recommendations; retrieval/grounding work (GEO, adversarial-SEO papers) shows content edits and prompt injections move citations; context-pathway work (agentic e-commerce, position bias) shows system-prompt/harness factors dominate agent purchases.
- Peer-reviewed anchors exist at KDD, EMNLP, ACL, and a SIGIR workshop, but the bulk of 2025–2026 output is arXiv preprints (many not yet peer-reviewed), and a large parallel vendor literature (Profound, BrightEdge, Semrush, Yext) is non-peer-reviewed and often conflicts with, or outruns, the academic record.

## Key Findings
- **The field has a clear genealogy.** Aggarwal et al. (2024) coined "Generative Engine Optimization" and is the citation hub. Two independent lines extend it: (1) an **adversarial/security** line (Kumar & Lakkaraju; Pfrommer et al.; Nestaas et al.) treating visibility as an attack surface, and (2) a **marketing/bias** line (Kamruzzaman et al.; Lichtenberg et al.; Filandrianos et al.; the "Incumbent Advantage" and ChoiceEval audits) treating it as a market-fairness problem.
- **Content properties that raise visibility are now fairly well established for the retrieval pathway.** Cite Sources, Quotation Addition, and Statistics Addition are the top GEO methods; fluency/readability edits also help; keyword stuffing fails or backfires. Multiple later papers reproduce the direction of these effects.
- **Brand/incumbent bias is the most consistent parametric finding.** Independent studies converge that LLMs over-recommend popular, global, and incumbent brands in open-ended category questions.
- **Cross-model divergence is large and repeatedly measured.** Providers cite different sources, in different volumes, and rarely agree on a top recommendation — though the precise numbers come mostly from vendor reports.
- **Measurement is fragmenting.** "Share of Model," Position-Adjusted Word Count, GEO-16, ChoiceEval, and ACES are competing metrics; only Aggarwal's and Lichtenberg's are peer-reviewed-adjacent with released code.

## Details

### Pathway 1 — Parametric recall (training-data-driven visibility)

**Mallen, Asai, Zhong, Das, Khashabi, Hajishirzi — "When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories."**
- Affiliations: University of Washington / Allen Institute for AI (and collaborators). Venue: **ACL 2023** (peer-reviewed, long paper, pp. 9802–9822). First arXiv 2212.10511 (Dec 2022); last revised v4.
- URL: https://arxiv.org/abs/2212.10511 ; ACL: https://aclanthology.org/2023.acl-long.546/ . Code/data released (PopQA, 14k questions): https://github.com/AlexTMallen/adaptive-retrieval
- Models: GPT-3 (davinci-003), GPT-J 6B, GPT-Neo 2.7B, and ~10 LMs; 4 augmentation methods. Sample: 14k PopQA questions + EntityQuestions.
- Core finding: LMs recall popular entities from parametric memory but fail on long-tail entities; scaling does not fix the tail; retrieval closes the gap for unpopular entities but can hurt popular ones. This is the foundational mechanism behind "popular brands are recalled without retrieval."
- Effect size: GPT-3 davinci-003 scored only ~19% on the 4,000 least-popular questions; Adaptive Retrieval improved accuracy 5.3% and halved API cost.
- Pathway: **parametric** (with retrieval contrast). No commercial conflict of interest.

**Kamruzzaman, Nguyen, Kim — "'Global is Good, Local is Bad?': Understanding Brand Bias in LLMs."**
- Affiliation: University of South Florida. Venue: **EMNLP 2024 (main)**, peer-reviewed, pp. 12704–12721. arXiv 2406.13997 (Jun 2024).
- URL: https://aclanthology.org/2024.emnlp-main.707/ ; https://arxiv.org/abs/2406.13997
- Models/sample: probes multiple LLMs across four brand categories using a curated dataset; completion tasks in both directions (e.g., shoe/clothing brands).
- Core finding: LLMs associate global brands with positive attributes and local brands with negative ones, recommend luxury brands for high-income and non-luxury for low-income personas, and exhibit country-of-origin effects.
- Pathway: **parametric**. No stated commercial COI.

**Lichtenberg, Buchholz, Schwöbel — "Large Language Models as Recommender Systems: A Study of Popularity Bias."**
- Affiliation: Amazon Music / Amazon Web Services (Berlin). Venue: **Gen-IR @ SIGIR 2024 workshop** (workshop, not main track). arXiv 2406.01285 (Jun 2024).
- URL: https://arxiv.org/abs/2406.01285 ; https://www.amazon.science/publications/large-language-models-as-recommender-systems-a-study-of-popularity-bias
- Models: gpt-3.5-turbo-0613, gpt-4-1106-preview, claude-instant-1.2, claude-2.1. Sample: MovieLens 10M subsample, 1000 users × 5 folds.
- Core finding: **a counterpoint result** — a simple LLM recommender exhibits *less* popularity bias than traditional recommender baselines, even without mitigation. Proposes a new popularity-bias metric.
- Pathway: **parametric**. COI: authors are Amazon employees (product/vendor context).

**Rienecker, Mpofu, Goel, Datta, Zhao, Danielsson, Thorsen — "Auditing Preferences for Brands and Cultures in LLMs" (ChoiceEval).**
- Affiliation: University of Oxford (and collaborators). Venue: **arXiv preprint 2603.18300** (Mar 2026), not yet peer-reviewed. (Note: some citing papers mis-attribute this to "Chen et al. 2026, arXiv 2603.18300" — the arXiv record lists Rienecker et al.; flagging the discrepancy.)
- URL: https://arxiv.org/abs/2603.18300
- Models: Gemini, GPT, DeepSeek. Sample: ~2,000 persona-diverse questions across topics (running shoes, hotel chains, travel destinations).
- Core finding: models prefer similar brands/cultures regardless of persona, and systematically over-represent US entities relative to their real global competitive position (provider-of-origin bias).
- Pathway: **parametric** (realistic-usage audit). Released as a reproducible framework.

**Chu, Hou et al. — "Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems."**
- Affiliations: Trine University; Texas A&M University. Venue: **arXiv preprint 2606.17443** (2026), not peer-reviewed.
- URL: https://arxiv.org/abs/2606.17443
- Models: GPT-4o-mini, Claude Sonnet, Gemini (paper states "Gemini 3 Flash"); skincare category + search-good robustness check.
- Core finding: a "Conditional Monopoly" — well-known brands are recommended 100% of the time when all products have identical specs, but a +0.1-star competitor advantage breaks it; authority-style/fabricated-clinical language is worth ~+0.17 rating points ("Bias Surplus Value"); multi-brand GEO competition becomes a social dilemma (per-brand payoff proxy collapses from +0.802 to +0.007 when all adopt it, and non-participating brands get zero recommendations).
- Pathway: **parametric + context** (parametric recall plus description manipulation). No stated COI.

### Pathway 2 — Retrieval / grounding (web search, RAG)

**Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande — "GEO: Generative Engine Optimization" (the anchor).**
- Affiliations: IIT Delhi (Aggarwal, equal contribution), Princeton (Murahari, equal; Narasimhan; Deshpande), independent (Rajpurohit, Kalyan). Venue: **KDD 2024** (peer-reviewed, pp. 5–16, DOI 10.1145/3637528.3671900). arXiv 2311.09735: v1 16 Nov 2023, v2 28 May 2024, v3 28 Jun 2024.
- URL: https://arxiv.org/abs/2311.09735 . Code/data: https://generative-engines.com/GEO/ (v1 referenced https://github.com/GEO-optim/GEO). Benchmark GEO-bench released.
- Models/setup: two-step generative engine — top-5 Google results + **gpt-3.5-turbo**, 5 samples at temperature 0.7; real-world validation on **Perplexity.ai**. Subjective metric scored via GPT-3.5 (G-Eval); query tagging/synthesis via GPT-4.
- Sample: GEO-bench = **10,000 queries** (8K/1K/1K train/val/test), 9 data sources (MS MARCO, ORCAS-1, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity.ai Discover, ELI-5, GPT-4-generated), 25 domains; 80% informational / 10% transactional / 10% navigational.
- Core finding: black-box content edits raise source visibility in AI answers by up to 40%; the top methods are Cite Sources, Quotation Addition, and Statistics Addition (+30–40% on Position-Adjusted Word Count, +15–30% on Subjective Impression). Two metrics defined: Position-Adjusted Word Count and Subjective Impression.
- Effect sizes (Table 1, baseline 19.3 on both metrics — Position-Adjusted Word Count / Subjective Impression): Quotation Addition 27.2 / 24.7 (highest), Statistics Addition 25.2 / 23.7, Cite Sources 24.6 / 21.9, Fluency Optimization 24.7 / 21.9, Easy-to-Understand 22.0 / 20.5; **Keyword Stuffing 17.7 — below baseline on the objective metric (hurts)**; Authoritative showed no significant gain on the objective metric. GEO helps low-ranked sources most (Rank-5: Cite Sources +115.1%, Quotation +99.7%, Statistics +97.9%) and can *hurt* Rank-1 sources (Cite Sources −30.3%). Best combination (Fluency + Statistics) beats any single method by >5.5%. Perplexity.ai real-world result: up to 37% (reported as 22% Position-Adjusted Word Count / 37% Subjective Impression).
- Limitations (stated, verbatim-sourced): methods must adapt as GEs evolve; did not evaluate effect on search rankings; query distribution may drift over time; labeling is partly subjective.
- Pathway: **retrieval/grounding**. No commercial COI (academic).

**Kumar, Lakkaraju — "Manipulating Large Language Models to Increase Product Visibility."**
- Affiliation: Harvard University. Venue: **arXiv preprint 2404.07981** (Apr 2024; v2 Sep 2024); widely cited but I could not confirm a peer-reviewed venue.
- URL: https://arxiv.org/abs/2404.07981v2
- Models: demonstrated on LLM search (Bing Copilot referenced); fictitious catalog of coffee machines; two target products; 200 independent evaluations. Uses Greedy Coordinate Gradient (white-box) to optimize a "strategic text sequence" (STS).
- Core finding: adding an STS to a product page reliably moves a target product to the top recommendation, including one that seldom appeared before.
- Pathway: **retrieval/grounding + context** (injected page text). No commercial COI.

**Pfrommer, Bai, Gautam, Sojoudi — "Ranking Manipulation for Conversational Search Engines."**
- Affiliation: UC Berkeley (EECS). Venue: **EMNLP 2024 (main)**, peer-reviewed, pp. 9523–9552, DOI 10.18653/v1/2024.emnlp-main.534. arXiv 2406.03589 (Jun 2024; v3 Sep 2024). Cited by later work per Semantic Scholar/scite.
- URL: https://aclanthology.org/2024.emnlp-main.534/ . Code + RAGDOLL dataset released: https://github.com/spfrommer/cse-ranking-manipulation (dataset on HuggingFace).
- Models: production engines (Bing, Perplexity) and plugin APIs (GPT-4, Claude); real-world consumer-product website dataset (RAGDOLL). Introduces a tree-of-attacks prompt-injection procedure.
- Core finding: prompt injection into a product's website text reliably reorders the sources a conversational engine lists; decomposes ranking variance into product name, description content, and list position.
- Pathway: **retrieval/grounding + context**. No commercial COI.

**Nestaas, Debenedetti, Tramèr — "Adversarial Search Engine Optimization for Large Language Models."**
- Affiliation: ETH Zurich. Venue: arXiv 2406.18382 (Jun 2024); one aggregator lists it as ICLR-associated, but I could not confirm the peer-reviewed venue — flagging as preprint.
- URL: https://arxiv.org/abs/2406.18382
- Models: production LLM search engines (Bing, Perplexity) and plugin APIs for GPT-4 and Claude.
- Core finding: introduces "Preference Manipulation Attacks" — crafted website/plugin content makes an LLM promote attacker products and discredit competitors; leads to a prisoner's-dilemma where collective attacking degrades output for everyone.
- Pathway: **context/retrieval** (injected external content). No commercial COI.

**Filandrianos, Dimitriou, Lymperaiou, Thomas, Stamou — "Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations."**
- Affiliation: National Technical University of Athens. Venue: **EMNLP 2025 (main)**, peer-reviewed, pp. 22397–22426, DOI 10.18653/v1/2025.emnlp-main.1140. arXiv 2502.01349 (Feb 2025; revised through Oct 2025).
- URL: https://aclanthology.org/2025.emnlp-main.1140/ ; https://arxiv.org/abs/2502.01349
- Models: multiple LLMs of varying scale; categories include coffee machines, cameras, books.
- Core finding: cognitive biases embedded in product descriptions are black-box levers — **social proof consistently boosts** recommendation rate/ranking, while **scarcity and exclusivity surprisingly reduce** visibility; effects are unpredictable across models.
- Pathway: **context/retrieval** (description edits). No commercial COI.

**Bagga, Farias, Korkotashvili, Peng, Wu — "E-GEO: A Testbed for Generative Engine Optimization in E-Commerce."**
- Affiliations: MIT (Operations Research Center; Sloan; EECS), Columbia GSB (Peng). Venue: **arXiv preprint 2511.20867** (Nov 2025), not yet peer-reviewed.
- URL: https://arxiv.org/abs/2511.20867 . Code/data: https://github.com/psbagga17/E-GEO
- Models: GPT-4o as generative engine + GPT-4o rewriter; E-GEO benchmark = 7,000+ realistic multi-sentence product queries (sourced from r/BuyItForLife) with listings; 15 rewriting heuristics evaluated.
- Core finding: a lightweight iterative prompt-optimization algorithm beats heuristic rewrites and reveals a stable, **domain-agnostic "universally effective" GEO strategy** — preserve facts, surface concrete attributes, organize for comparison, match buyer intent.
- Limitation (stated): English-only; demographic skew toward North American durable goods.
- Pathway: **retrieval/grounding**. No commercial COI.

**Kumar (Arlen), Palkhouski — "AI Answer Engine Citation Behavior: Bringing the GEO-16 Framework in B2B SaaS."**
- Affiliation: listed as UC Berkeley / Wrodium Research. Venue: **arXiv preprint 2509.10762** (Sep 2025), not peer-reviewed; note a possibly overlapping/duplicate identifier 2509.08919 ("Generative Engine Optimization: How to Dominate AI Search") appears in the same cluster.
- URL: https://arxiv.org/abs/2509.10762
- Models/sample: 70 prompts, 1,702 citations, 1,100 URLs across Brave Summary, Google AI Overviews, and Perplexity (sonar-pro); 16 B2B SaaS verticals. Introduces GEO-16 (16-pillar page-quality score).
- Core finding: page-quality signals predict citation (odds ratio 4.2, 95% CI [3.1, 5.7]); strongest pillars are Metadata & Freshness (r=0.68), Semantic HTML (r=0.65), Structured Data (r=0.63); pages with G≥0.70 and ≥12 pillar hits hit a 78% cross-engine citation rate. Engines differ sharply (mean GEO quality of cited pages: Brave 0.727, Google AIO 0.687, Perplexity 0.300).
- COI: authors affiliated with a commercial research entity (Wrodium); vendor-adjacent.
- Pathway: **retrieval/grounding**.

**Yang (Kai-Cheng) — "News Source Citing Patterns in AI Search Systems."**
- Affiliation: author record indicates Northeastern University (verify). Venue: **arXiv preprint 2507.05301** (Jul 2025), cs.IR; not confirmed peer-reviewed. Code released: https://github.com/yang3kc/ai_search_arena
- URL: https://arxiv.org/abs/2507.05301
- Sample: AI Search Arena dataset — 24,000+ conversations, 65,000 responses, 366,000+ citations, 12 AI search models from OpenAI, Perplexity, Google.
- Core finding: models from the same provider cite similarly; providers differ; OpenAI models cite news at higher rates; citations concentrate on a few outlets with a consistent liberal lean; low-credibility sources rarely cited; source politics/quality don't predict user satisfaction.
- Pathway: **retrieval/grounding**. No commercial COI.

### Pathway 3 — Context (system prompts, agent harnesses, position, memory)

**Allouah, Besbes, Figueroa, Kanoria, Kumar — "What Is Your AI Agent Buying? … Agentic E-Commerce" (ACES).**
- Affiliation: Columbia University (Business School / IEOR). Venue: **ACM Web Conference (WWW) 2026** (accepted; pp. 8697–8700 in one record) and Columbia Business School Research Paper No. 381574 / **SSRN 5381574**. arXiv 2508.02630 (Aug 2025).
- URL: https://arxiv.org/abs/2508.02630 ; SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5381574 . ACES sandbox: https://ace.mycustomai.io/
- Models: frontier VLM agents (GPT-4.1, Claude, Gemini) in a programmable mock marketplace; randomizes position, price, ratings, reviews, sponsored tags, endorsements.
- Core finding: agents show choice homogeneity (demand concentrates on a few "modal" products); preferences are unstable across model updates; strong but heterogeneous position bias (all favor top row, differ on columns) persisting even in text-only interfaces; agents penalize sponsored tags and reward platform endorsements; seller-side query-conditional description tweaks drive significant market-share gains.
- Pathway: **context** (agent harness, position, prompt). COI: none stated; industry-relevant.

**Jack — "Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit."**
- Venue: **arXiv preprint 2605.27439** (2026), vendor-affiliated (Unusual.ai Research Series); not peer-reviewed.
- URL: https://arxiv.org/abs/2605.27439
- Sample: 37,000 runs across providers; stratifies brands by a prominence "ladder" (L1–L5).
- Core finding: retrieval-augmented commercial chat is bimodal — high-prominence (L1–L2) brands are reliably reachable while low-prominence (L4–L5) are "catastrophically" unreachable, rather than a smooth popularity gradient; documents earned-media-over-owned-content bias.
- COI: authored under a commercial research series (Unusual.ai). Pathway: **retrieval + context**.

**"Who Owns the AI Recommendation? A Multi-Industry Empirical Map of Brand Category Ownership Across LLMs."**
- Venue: **arXiv preprint 2606.23057** (2026), not peer-reviewed.
- URL: https://arxiv.org/abs/2606.23057
- Sample: large-scale mapping across five industries; multiple platforms.
- Core finding: brand recommendations are shaped by parametric knowledge plus retrieved sources; dominance follows concentration patterns and differs across platforms; cites vendor data that a brand can hold ~24% "Share of Model" on one platform and <1% on another.
- Pathway: **parametric + retrieval**. COI: none stated but vendor-adjacent framing.

### The vendor/non-academic layer (flagged, not primary)
A large body of practitioner measurement circulates widely and is internally consistent on *direction*, but is **non-peer-reviewed, methodologically opaque, and commercially motivated** — treat it as hypotheses, not findings:
- **Profound** — the "Parrot Problem" report analyzed 50,000 prompts across seven industries and found "nearly half of every AI response includes unsolicited comparisons, opinions, and recommendations the user never asked for" (Profound also reports 97.4% of AI citations coming from non-Tier-1 earned media across 27M prompts; and, in May 2026 tracking of 15,155 brand configurations, a median 8-point visibility gap between a brand's best- and worst-performing Google model).
- **BrightEdge AI Catalyst** — "ChatGPT: Mentions 3.2× MORE than cites (2.37 mentions vs. 0.73 citations)," contrasted with "Google AIO: Cites 2.4× MORE than mentions (14.30 citations vs. 6.02 mentions)" and "Google AI Mode: Cites 6× MORE (9.49 vs 1.59)."
- **Yext, Inc.** (NYSE: YEXT) press release, Oct 9, 2025, analyzing 6.8M AI citations from 1.6M queries per model (July 1–Aug 31, 2025): "OpenAI leans on listings (48.7%)," with the headline finding that "86% of citations come from sources brands already control" (first-party websites 44%, listings 42%); authors Christian Ward, Anthony Rinaldi, Adam Abernathy, Alan Ai.
- **Semrush + Kevin Indig** (October 2025, 1,000 randomly selected domains via Semrush's AI Visibility Toolkit): "Authority Score correlates with AI mentions at a Pearson coefficient of 0.65 and Spearman of 0.57, but with AI Share of Voice at only 0.23 Pearson and 0.36 Spearman." A companion Semrush/Indig study of 1,094 US categories found Authority Score predicted the topic owner in only 52.5% of head-to-head comparisons — "coin-flip territory."
- **ZipTie / QuickSEO** — "Perplexity provides 21.87 sources per response on average, compared to ChatGPT's 7.92"; "only 11% of domains are cited by both ChatGPT and Perplexity."

The **"Share of Model" metric originates in this vendor layer** (popularized by Profound/Foundation), not in peer-reviewed work.

### Venue/status summary
- **Peer-reviewed, top-tier:** Aggarwal (KDD 2024); Pfrommer (EMNLP 2024); Kamruzzaman (EMNLP 2024); Filandrianos (EMNLP 2025); Mallen (ACL 2023); Allouah (WWW 2026, accepted).
- **Peer-reviewed workshop:** Lichtenberg (Gen-IR@SIGIR 2024).
- **Preprint only (not yet peer-reviewed):** Kumar & Lakkaraju; Nestaas et al.; E-GEO; ChoiceEval; Incumbent Advantage; GEO-16; News Source Citing; Prominence-Stratified; Who Owns the AI Recommendation.

## Claims corroborated by more than one independent study
1. **Citations, quotations, and statistics increase source/product visibility in AI answers.** (Aggarwal KDD 2024; reproduced in direction by E-GEO 2025 and GEO-16 2025.)
2. **Keyword stuffing — the classic SEO tactic — does not transfer to generative engines.** (Aggarwal 2024, where it fell below baseline; echoed by E-GEO 2025 and by Nestaas 2024's contrast between coherent persuasive content and detectable injections.)
3. **LLMs over-recommend popular/incumbent/global brands in open-ended category questions.** (Kamruzzaman EMNLP 2024; Kumar & Lakkaraju 2024; Incumbent Advantage 2026; ChoiceEval 2026; grounded mechanistically by Mallen ACL 2023.)
4. **Popularity/parametric recall is entity-frequency-driven; retrieval is needed for the long tail.** (Mallen ACL 2023; Prominence-Stratified 2026; Lichtenberg 2024 as a partial counterpoint.)
5. **Prompt injection / strategic text in retrieved content can reorder or hijack recommendations.** (Kumar & Lakkaraju 2024; Pfrommer EMNLP 2024; Nestaas 2024.)
6. **Authority and social-proof language shift recommendations more than most other edits.** (Filandrianos EMNLP 2025; Incumbent Advantage 2026.)
7. **Providers diverge sharply in which sources they cite and how many.** (Yang 2507.05301; GEO-16 2509.10762; corroborated in direction by multiple vendor studies.)
8. **Position/order bias materially affects what agents and rerankers surface.** (Allouah WWW 2026; Pfrommer EMNLP 2024; and related reranking work.)
9. **Multi-actor GEO adoption creates a collective-action / prisoner's-dilemma degradation.** (Nestaas 2024; Incumbent Advantage 2026.)

## Claims that rest on a single study only
- The specific **"up to 40%" visibility lift** and per-method magnitudes (Quotation Addition to 27.2, Rank-5 sources +115.1%) — Aggarwal et al. only.
- **"Conditional Monopoly" / +0.17-rating "Bias Surplus Value" / payoff collapse +0.802→+0.007** — Incumbent Advantage only.
- **GEO-16 operating point (G≥0.70 & ≥12 pillars → 78% cross-engine citation; odds ratio 4.2)** — GEO-16 only.
- **A "universally effective," domain-agnostic optimized GEO prompt** — E-GEO only (and in tension with Aggarwal's domain-specificity claim).
- **LLM recommenders show *less* popularity bias than traditional recommenders** — Lichtenberg only (a lone counterpoint).
- **Agents penalize sponsored tags but reward platform endorsements; model updates reshuffle market shares** — Allouah/ACES only.
- **Bimodal (not gradient) prominence reachability (L1–L2 high, L4–L5 catastrophic)** — Prominence-Stratified audit only.
- **Consistent liberal lean and outlet concentration in AI-search news citations** — Yang only (in the LLM-search setting).
- **US-entity over-representation across personas** — ChoiceEval only.

## Recommendations
- **If you act on one evidence-based lever now:** invest in being cited by high-authority third-party sources and add verifiable statistics, quotations, and inline citations to your own pages. This is the single claim with peer-reviewed support (Aggarwal, KDD 2024) reproduced in direction by two later preprints. Benchmark: track whether target queries begin surfacing your source in Perplexity/Google AIO before scaling spend.
- **Optimize per pathway.** For parametric visibility (brand recall without retrieval), the lever is long-run prominence in training-corpus-heavy sources (Wikipedia, widely-cited reference material) — slow, and it cannot be prompt-hacked. For retrieval visibility, the lever is crawlable, well-structured, freshly-dated, citation-dense pages (GEO-16's strongest pillars: Metadata & Freshness, Semantic HTML, Structured Data). For context/agent visibility, the lever is clean, comparison-ready product descriptions matched to buyer intent (E-GEO; ACES).
- **Do not rely on keyword stuffing or on transplanting classic SEO wholesale** — the peer-reviewed evidence says it fails or backfires in generative engines.
- **Measure across ≥4 providers, not one.** Cross-model divergence is one of the best-supported findings; single-engine measurement is unreliable. Use a fixed prompt set and compute a mention/share metric per engine.
- **Treat vendor "Share of Model" dashboards as directional, not authoritative.** Adopt the concept for benchmarking but validate against your own controlled prompt panel.
- **Thresholds that would change these recommendations:** (1) a well-powered replication showing citation/statistics edits *fail* on current frontier models with live retrieval; (2) evidence that providers converge on shared citation behavior (would restore single-engine measurement); (3) advertising integrations materially overriding organic visibility — OpenAI began its US ChatGPT ads pilot on February 9, 2026 (announced Jan 16, 2026), showing ads on Free and Go tiers only, with first advertisers including Target, Adobe, Williams-Sonoma and Albertsons, and expanded on Aug 11, 2026 to the UK, Mexico, Brazil, Japan, and South Korea — which would shift budget from GEO toward paid placement.

## Caveats
- **Most 2025–2026 sources are un-peer-reviewed arXiv preprints**, several from commercially interested authors (Wrodium, Unusual.ai, Amazon). Effect sizes from these should be treated as provisional.
- **Model versions matter and churn fast.** Aggarwal used gpt-3.5-turbo; later work uses GPT-4o, Claude, Gemini. Findings may not transfer across generations — Allouah explicitly shows model updates reshuffle outcomes.
- **Citation-count verification is limited.** I confirmed venue/acceptance for the peer-reviewed anchors but could not independently verify precise forward-citation counts for each paper; where a citing relationship is asserted it is based on reference lists seen in the sources, not a citation-index lookup.
- **Identifier conflicts flagged:** ChoiceEval (arXiv 2603.18300) is attributed in the arXiv listing to Rienecker et al., but at least one citing paper labels it "Chen et al. 2026." Two GEO-16-cluster preprints (2509.10762 and 2509.08919) may be related or duplicate efforts; I have not fully disambiguated them.
- **Vendor statistics conflict on specifics** (e.g., differing cross-platform overlap and citation-share percentages) even where they agree on direction; I have not reconciled them and do not treat them as established.
- Some affiliations (e.g., Yang's institution) are inferred from author records and should be verified before publication.