# Source Index — LLM Brand Visibility Knowledge Base

**Status: v1.0, reviewed August 2026.** Scores were assigned by applying the rubric below to five Research reports plus targeted verification, and were reviewed without override. See "Scoring judgments the agent must be aware of" for where relevance and evidence quality diverge.

---

## Scoring rubric

Sources fall into three evidence classes. Each class has its own rubric because the classes answer different questions.

### Class A — Research (answers "is the lever proven?")

Four dimensions, each 0–3:

| Dim | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| **Venue** | Top-tier peer-reviewed (NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, KDD, WWW, SIGIR, USENIX Sec, Science, Mgmt Sci, TOIS) | Other peer-reviewed or top-tier workshop | Preprint from lab with established track record | Preprint, unknown or commercial authors |
| **Reproducibility** | Code + data/benchmark released | Partial (code or data) | Method fully described, nothing released | Insufficient to reproduce |
| **Scope** | Multi-model, multi-domain, large sample | Moderate (2+ models or domains) | Single domain or single model | Anecdotal / demo |
| **Corroboration** | Replicated by independent peer-reviewed work | Direction reproduced by others | Single study | Contradicted by stronger evidence |

**Total → Tier:** Strong 10–12 · Solid 7–9 · Provisional 4–6 · Weak 0–3

**Flags** (do not change score; change how the agent may use the source):
- `COI` — authors or funder sell a product that benefits from the finding
- `API-ONLY` — measured model APIs, typically search-off; not consumer product behavior
- `SINGLE-DOMAIN` — one product category; transfer to enterprise tech is untested
- `EXTRAPOLATED` — studies encyclopedic facts, not brands; brand relevance is inferred
- `SUPERSEDED-MODELS` — measured on models 2+ generations old
- `UNVERIFIED` — venue or affiliation not confirmed against a primary record

### Class B — Platform-official (answers "how does the mechanism work?")

Three dimensions, each 0–3: **Specificity** (names concrete mechanisms, user-agents, fields), **Recency** (dated within 6 months = 3, 12 months = 2, older = 1, undated = 0), **Primary** (fetched from provider's own page = 3, provider blog = 2, secondary coverage of provider statement = 1, inferred = 0).

Class B sources are authoritative about mechanism regardless of score; the score governs how much confidence to place in specific details.

### Class C — Industry studies (answers "what are others seeing?")

Four dimensions, each 0–3: **Sample** (size and breadth), **Disclosure** (prompts, runs, temperature, model versions, search on/off published), **Independence** (publisher does not sell the tool that produces the metric), **Corroboration** (by Class A or independent Class C).

Class C sources may be cited for current-state observation. They may not, on their own, be the basis for a recommendation; the agent must find Class A or B support first.

---

## Class A — Research

### A1. Direct GEO / AI-visibility literature

| # | Source | Venue | Repro | Scope | Corrob | Total | Tier | Flags |
|---|---|---|---|---|---|---|---|---|
| A1.1 | **Aggarwal et al., "GEO: Generative Engine Optimization"** — KDD 2024. arXiv 2311.09735. https://arxiv.org/abs/2311.09735 · Code/bench: https://generative-engines.com/GEO/ | 3 | 3 | 3 | 2 | **11** | Strong | SUPERSEDED-MODELS (gpt-3.5-turbo) |
| A1.2 | **Pfrommer et al., "Ranking Manipulation for Conversational Search Engines"** — EMNLP 2024. arXiv 2406.03589. https://aclanthology.org/2024.emnlp-main.534/ · Code: https://github.com/spfrommer/cse-ranking-manipulation | 3 | 3 | 2 | 2 | **10** | Strong | — |
| A1.3 | **Nestaas, Debenedetti, Tramèr, "Adversarial Search Engine Optimization for LLMs"** — ICLR 2025 (verified). arXiv 2406.18382. https://arxiv.org/abs/2406.18382 | 3 | 1 | 2 | 2 | **8** | Solid | — |
| A1.4 | **Filandrianos et al., "Bias Beware: Cognitive Biases on LLM-Driven Product Recommendations"** — EMNLP 2025. arXiv 2502.01349. https://aclanthology.org/2025.emnlp-main.1140/ | 3 | 1 | 2 | 2 | **8** | Solid | — |
| A1.5 | **Kamruzzaman, Nguyen, Kim, "Global is Good, Local is Bad? Brand Bias in LLMs"** — EMNLP 2024. arXiv 2406.13997. https://aclanthology.org/2024.emnlp-main.707/ · Code: https://github.com/hieuminh65/LLM-Brand-Bias | 3 | 3 | 2 | 2 | **10** | Strong | SINGLE-DOMAIN (consumer goods) |
| A1.6 | **Allouah et al., "What Is Your AI Agent Buying?" (ACES)** — WWW 2026. arXiv 2508.02630. https://arxiv.org/abs/2508.02630 · Sandbox: https://ace.mycustomai.io/ | 3 | 2 | 3 | 1 | **9** | Solid | — |
| A1.7 | **Kumar & Lakkaraju, "Manipulating LLMs to Increase Product Visibility"** — arXiv preprint 2404.07981 (Harvard). https://arxiv.org/abs/2404.07981 | 1 | 3 | 1 | 2 | **7** | Solid | UNVERIFIED (venue) |
| A1.8 | **Bagga et al., "E-GEO: Testbed for GEO in E-Commerce"** — arXiv 2511.20867 (MIT/Columbia). https://arxiv.org/abs/2511.20867 · Code: https://github.com/psbagga17/E-GEO | 1 | 3 | 2 | 1 | **7** | Solid | SINGLE-DOMAIN, API-ONLY |
| A1.9 | **Chen, Wang, Chen, Koudas, "GEO: How to Dominate AI Search"** — arXiv 2509.08919 (U. Toronto). https://arxiv.org/abs/2509.08919 | 1 | 1 | 3 | 2 | **7** | Solid | Acknowledgments thank a GEO vendor (ktau.ai) — treat as soft COI |
| A1.10 | **Rienecker et al., "Auditing Preferences for Brands and Cultures in LLMs" (ChoiceEval)** — arXiv 2603.18300 (Oxford). https://arxiv.org/abs/2603.18300 | 1 | 2 | 3 | 1 | **7** | Solid | Author attribution inconsistent across citing papers |
| A1.11 | **Chu & Hou, "Incumbent Advantage"** — arXiv 2606.17443 (Trine / Texas A&M). https://arxiv.org/abs/2606.17443 | 0 | 1 | 2 | 2 | **5** | Provisional | API-ONLY, SINGLE-DOMAIN (skincare), very recent |
| A1.12 | **Kumar (Arlen) & Palkhouski, "GEO-16 Framework in B2B SaaS"** — arXiv 2509.10762. https://arxiv.org/abs/2509.10762 | 0 | 1 | 2 | 1 | **4** | Provisional | COI (Wrodium). Note: B2B SaaS focus makes it the closest domain match to enterprise tech |
| A1.13 | **Yang, "News Source Citing Patterns in AI Search Systems"** — arXiv 2507.05301. https://arxiv.org/abs/2507.05301 · Code: https://github.com/yang3kc/ai_search_arena | 1 | 3 | 3 | 1 | **8** | Solid | UNVERIFIED (affiliation); news domain, not commercial brands |
| A1.14 | **Jack, "Prominence-Stratified Failure Modes… 37,000-Run Audit"** — arXiv 2605.27439. https://arxiv.org/abs/2605.27439 | 0 | 1 | 3 | 1 | **5** | Provisional | COI (Unusual.ai research series) |
| A1.15 | **"Who Owns the AI Recommendation?"** — arXiv 2606.23057. https://arxiv.org/abs/2606.23057 | 0 | 0 | 2 | 1 | **3** | Weak | Relies on vendor data; authorship not established |
| A1.16 | **Lichtenberg, Buchholz, Schwöbel, "LLMs as Recommender Systems: Popularity Bias"** — Gen-IR @ SIGIR 2024. arXiv 2406.01285. https://arxiv.org/abs/2406.01285 | 2 | 1 | 2 | 0 | **5** | Provisional | COI (Amazon); lone counterpoint — LLMs *less* popularity-biased than CF baselines. Keep as the honest dissent. |
| A1.17 | **C-SEO Bench: "Does Conversational SEO Work?"** — arXiv 2506.11097. https://arxiv.org/abs/2506.11097 | — | — | — | — | — | **UNSCORED** | Surfaced during verification; not covered by any run. Appears to be a benchmark testing whether GEO tactics hold. Needs a read before scoring. |

### A2. Parametric recall foundations (memorization, long-tail, mechanism)

| # | Source | Venue | Repro | Scope | Corrob | Total | Tier | Flags |
|---|---|---|---|---|---|---|---|---|
| A2.1 | **Kandpal et al., "LLMs Struggle to Learn Long-Tail Knowledge"** — ICML 2023. https://arxiv.org/abs/2211.08411 | 3 | 2 | 3 | 3 | **11** | Strong | EXTRAPOLATED |
| A2.2 | **Carlini et al., "Quantifying Memorization Across Neural LMs"** — ICLR 2023. https://arxiv.org/abs/2202.07646 · Data: https://github.com/ethz-spylab/lm_memorization_data | 3 | 3 | 3 | 3 | **12** | Strong | EXTRAPOLATED |
| A2.3 | **Lee et al., "Deduplicating Training Data Makes LMs Better"** — ACL 2022. https://arxiv.org/abs/2107.06499 | 3 | 2 | 3 | 3 | **11** | Strong | EXTRAPOLATED |
| A2.4 | **Mallen et al., "When Not to Trust LMs" (PopQA)** — ACL 2023. https://arxiv.org/abs/2212.10511 · Code: https://github.com/AlexTMallen/adaptive-retrieval | 3 | 3 | 3 | 3 | **12** | Strong | EXTRAPOLATED — but the closest foundation to brand recall (popularity → recall) |
| A2.5 | **Sun et al., "Head-to-Tail: How Knowledgeable are LLMs?"** — NAACL 2024. https://arxiv.org/abs/2308.10168 | 3 | 3 | 3 | 3 | **12** | Strong | COI (Meta), EXTRAPOLATED |
| A2.6 | **Kang & Choi, "Impact of Co-occurrence on Factual Knowledge"** — EMNLP Findings 2023. https://arxiv.org/abs/2310.08256 · Code: https://github.com/CheongWoong/impact_of_cooccurrence | 2 | 3 | 2 | 2 | **9** | Solid | EXTRAPOLATED — key for "brand + category must co-occur" |
| A2.7 | **Allen-Zhu & Li, "Physics of LMs 3.1: Knowledge Storage and Extraction"** — ICML 2024. https://arxiv.org/abs/2309.14316 | 3 | 1 | 2 | 2 | **8** | Solid | COI (Meta), EXTRAPOLATED — key for "varied phrasing" claim |
| A2.8 | **Razeghi et al., "Pretraining Term Frequencies on Few-Shot Reasoning"** — EMNLP Findings 2022. https://arxiv.org/abs/2202.07206 | 2 | 2 | 2 | 3 | **9** | Solid | EXTRAPOLATED |
| A2.9 | **Elazar et al., "What's In My Big Data?" (WIMBD)** — ICLR 2024. https://arxiv.org/abs/2310.20707 · https://github.com/allenai/wimbd | 3 | 3 | 3 | 2 | **11** | Strong | Tooling for corpus analysis |
| A2.10 | **Geva et al., "Transformer FFN Layers Are Key-Value Memories"** — EMNLP 2021. https://arxiv.org/abs/2012.14913 | 3 | 3 | 2 | 3 | **11** | Strong | Mechanism only |
| A2.11 | **Meng et al., "Locating and Editing Factual Associations in GPT" (ROME)** — NeurIPS 2022. https://arxiv.org/abs/2202.05262 · https://rome.baulab.info/ | 3 | 3 | 2 | 3 | **11** | Strong | Mechanism only |
| A2.12 | **Cheng et al., "Dated Data: Tracing Knowledge Cutoffs"** — COLM 2024. https://arxiv.org/abs/2403.12958 · https://github.com/nexync/dated_data | 2 | 3 | 3 | 2 | **10** | Strong | Effective-cutoff lag |
| A2.13 | **Gekhman et al., "Does Fine-Tuning on New Knowledge Encourage Hallucinations?"** — EMNLP 2024. https://arxiv.org/abs/2405.05904 | 3 | 1 | 2 | 2 | **8** | Solid | COI (Google) — supports "can't patch parametric after the fact" |
| A2.14 | **Longpre et al., "Entity-Based Knowledge Conflicts in QA"** — EMNLP 2021. https://arxiv.org/abs/2109.05052 | 3 | 3 | 2 | 3 | **11** | Strong | COI (Apple) |
| A2.15 | **Xie et al., "Adaptive Chameleon or Stubborn Sloth"** — ICLR 2024. https://arxiv.org/abs/2305.13300 | 3 | 2 | 3 | 3 | **11** | Strong | Parametric vs retrieval conflict |
| A2.16 | **Wu, Wu, Zou, "ClashEval"** — NeurIPS 2024. https://arxiv.org/abs/2404.10198 | 3 | 2 | 3 | 2 | **10** | Strong | Retrieved content overrides prior >60% of the time |
| A2.17 | **Kirk et al., "Effects of RLHF on Generalisation and Diversity"** — ICLR 2024. https://arxiv.org/abs/2310.06452 | 3 | 2 | 2 | 2 | **9** | Solid | COI (Meta co-authors); mode-collapse → fewer brands volunteered |
| A2.18 | **Sprague et al., "To CoT or not to CoT?"** — ICLR 2025. https://arxiv.org/abs/2409.12183 · Code released | 3 | 3 | 3 | 2 | **11** | Strong | Reasoning does not rescue weak parametric recall |
| A2.19 | **Grosse et al., "LLM Generalization with Influence Functions"** — arXiv 2308.03296 (Anthropic). https://arxiv.org/abs/2308.03296 | 1 | 1 | 2 | 1 | **5** | Provisional | COI (Anthropic); attribution methodology |
| A2.20 | **Qi, Fernández, Bisazza, "Cross-Lingual Consistency of Factual Knowledge"** — EMNLP 2023. https://arxiv.org/abs/2310.10378 | 3 | 2 | 3 | 2 | **10** | Strong | Multilingual foundation |
| A2.21 | **von Rad et al., "Cross-Lingual Factual Recall via Consistency-Driven RL" (PolyFact)** — arXiv 2606.06586 (UCL). https://arxiv.org/abs/2606.06586 | 1 | 3 | 2 | 1 | **7** | Solid | Recent preprint |
| A2.22 | **Data-mixture disclosures**: GPT-3 (Brown et al., NeurIPS 2020, arXiv 2005.14165); LLaMA 1 (arXiv 2302.13971); Llama 3 (arXiv 2407.21783); The Pile (arXiv 2101.00027); Dolma (ACL 2024, arXiv 2402.00159); FineWeb (NeurIPS 2024 D&B, arXiv 2406.17557); DoReMi (NeurIPS 2023, arXiv 2305.10429) | 3 | 2 | 3 | 3 | **11** | Strong | COI (vendor self-report); establishes Wikipedia/reference upweighting. Closed frontier models do not disclose. |
| A2.23 | Cited-secondhand cluster (not re-verified by Run 2): TempLAMA, TemporalWiki, RealTime QA, FreshLLMs; MEMIT, MEND, ripple-effects, "Model Editing Can Hurt"; Knowledge Conflicts survey (arXiv 2403.08319); LIMA; URIAL; Santurkar; Recitation-Augmented LMs; GenRead | — | — | — | — | — | **UNSCORED** | Agent may cite the direction these support (staleness; editing brittleness; alignment-as-style) but not specific figures until verified. |

### A3. Adversarial / manipulation research (awareness only — see usage rules)

| # | Source | Venue | Repro | Scope | Corrob | Total | Tier | Flags |
|---|---|---|---|---|---|---|---|---|
| A3.1 | **Zou et al., "PoisonedRAG"** — USENIX Security 2025. https://arxiv.org/abs/2402.07867 · Code released | 3 | 3 | 3 | 2 | **11** | Strong | DO-NOT-RECOMMEND |
| A3.2 | **Greshake et al., "Not What You've Signed Up For" (indirect prompt injection)** — AISec @ CCS 2023. https://arxiv.org/abs/2302.12173 · https://github.com/greshake/llm-security | 2 | 3 | 2 | 3 | **10** | Strong | DO-NOT-RECOMMEND; foundational mechanism; OWASP LLM01:2025 |
| A3.3 | **SPLX, "AI-targeted cloaking"** (Vlahov & Eymery, Oct 2025). https://splx.ai/blog/ai-targeted-cloaking-openai-atlas | 0 | 2 | 1 | 2 | **5** | Provisional | COI (security vendor); corroborated by press; DO-NOT-RECOMMEND |
| A3.4 | 2025–26 preprint cluster: Dynamics of Adversarial Attacks (2501.00745); Poisoned-MRAG (2503.06254); Cross-Modal Content Optimization (2510.03612); SIREN (2607.21951); One Polluted Page (2606.13610); FilterRAG (2508.02835); RAG poisoning traceback (2504.21668) | 1 | 1 | 1 | 1 | **4** | Provisional | DO-NOT-RECOMMEND; effect sizes preliminary |
| A3.5 | **Google Search Central Spam Policies** (May 15, 2026 clarification extending spam policies to AI Overviews / AI Mode). https://developers.google.com/search/docs/essentials/spam-policies | — | — | — | — | — | **Class B** | Cross-listed; see B1.4 |

### A4. Recommender-system and IR bias foundations

| # | Source | Venue | Repro | Scope | Corrob | Total | Tier | Flags |
|---|---|---|---|---|---|---|---|---|
| A4.1 | **Salganik, Dodds, Watts, "Inequality and Unpredictability in an Artificial Cultural Market"** — Science 2006. DOI 10.1126/science.1121066 | 3 | 2 | 3 | 3 | **11** | Strong | Cumulative advantage; quality sets floor/ceiling |
| A4.2 | **Fleder & Hosanagar, "Blockbuster Culture's Next Rise or Fall"** — Management Science 2009 | 3 | 1 | 2 | 3 | **9** | Solid | Recommenders concentrate demand |
| A4.3 | **Chen et al., "Bias and Debias in Recommender System: A Survey"** — ACM TOIS 2023. https://arxiv.org/abs/2010.03240 | 3 | 2 | 3 | 3 | **11** | Strong | Taxonomy; companion GitHub |
| A4.4 | **Abdollahpouri, Burke, Mobasher** — popularity-bias series (RecSys 2017; FLAIRS 2019, arXiv 1901.07555) | 2 | 2 | 2 | 3 | **9** | Solid | Long-tail re-ranking |
| A4.5 | **Joachims et al., "Accurately Interpreting Clickthrough Data"** — SIGIR 2005 | 3 | 1 | 2 | 3 | **9** | Solid | Position bias, eye-tracking |
| A4.6 | **Craswell et al., "Click Position-Bias Models"** — WSDM 2008 | 3 | 1 | 2 | 3 | **9** | Solid | Cascade model |
| A4.7 | **Chaney, Stewart, Engelhardt, "Algorithmic Confounding"** — RecSys 2018. https://arxiv.org/abs/1710.11214 | 3 | 2 | 2 | 2 | **9** | Solid | Feedback loops homogenize |
| A4.8 | **Jiang et al., "Degenerate Feedback Loops in Recommender Systems"** — AIES 2019. https://arxiv.org/abs/1902.10730 | 2 | 1 | 2 | 2 | **7** | Solid | Exploration breaks lock-in |
| A4.9 | **Mansoury et al., "Feedback Loop and Bias Amplification"** — CIKM 2020 | 3 | 1 | 2 | 2 | **8** | Solid | — |
| A4.10 | **Liu et al., "Lost in the Middle"** — TACL 2024. https://arxiv.org/abs/2307.03172 | 3 | 3 | 3 | 3 | **12** | Strong | Position bias in LLM context |
| A4.11 | **Wang et al., "LLMs are not Fair Evaluators"** — ACL 2024. https://arxiv.org/abs/2305.17926 | 3 | 3 | 2 | 3 | **11** | Strong | Order bias |
| A4.12 | **Hou et al., "LLMs are Zero-Shot Rankers for Recommender Systems"** — ECIR 2024. https://arxiv.org/abs/2305.08845 · https://github.com/RUCAIBox/LLMRank | 2 | 3 | 2 | 2 | **9** | Solid | Popularity + position bias in LLM ranking |
| A4.13 | **Dai et al., "Uncovering ChatGPT's Capabilities in Recommender Systems"** — RecSys 2023. https://arxiv.org/abs/2305.02182 | 3 | 3 | 2 | 2 | **10** | Strong | SUPERSEDED-MODELS |
| A4.14 | **Deldjoo & Di Noia, "CFaiRLLM"** — ACM TIST 2025. https://arxiv.org/abs/2403.05668 | 2 | 1 | 2 | 1 | **6** | Provisional | Fairness framing |
| A4.15 | Position-bias extensions: "Evaluating Position Bias in LLM Recommendations" (arXiv 2508.02020); Wang et al., "Eliminating Position Bias" (ICLR 2025) | 2 | 1 | 2 | 2 | **7** | Solid | — |

---

## Class B — Platform-official documentation

| # | Source | Spec | Recency | Primary | Total | Notes |
|---|---|---|---|---|---|---|
| B1.1 | **Google Search Central, "Optimizing your website for generative AI features"** — updated 2026-07-10. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 3 | 3 | 3 | **9** | The single most useful Class B source. Explicitly debunks llms.txt, chunking, schema-as-requirement, inauthentic mentions. States AI features are "rooted in core Search ranking." |
| B1.2 | **Gemini API "Grounding with Google Search"** — https://ai.google.dev/gemini-api/docs/google-search (Firebase variant updated 2026-08-24) | 3 | 3 | 3 | **9** | Documents groundingMetadata, query fan-out; Google-Extended disallow excludes page from grounding |
| B1.3 | **Google-Extended crawler token** — Google crawler docs; announced Sept 28, 2023 | 3 | 1 | 3 | **7** | Training/grounding control; no Search impact |
| B1.4 | **Google Spam Policies** (May 15, 2026 AI clarification) — https://developers.google.com/search/docs/essentials/spam-policies | 3 | 3 | 3 | **9** | "Attempting to manipulate generative AI responses" is now named spam |
| B2.1 | **Bing Webmaster Blog, "AI Visibility Insights"** — June 16, 2026. https://blogs.bing.com/search/June-2026/... | 3 | 3 | 2 | **8** | Only first-party citation analytics; defines "grounding queries"; Citation Share is "observational, not a ranking system" |
| B2.2 | **Microsoft Learn, "Semantic indexing for Microsoft 365 Copilot"** — https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot | 3 | 2 | 3 | **8** | Enterprise grounding on tenant data; identity-bounded; not used to train |
| B2.3 | **IndexNow** — via Bing/Microsoft Learn coverage | 2 | 1 | 1 | **4** | Discovery only; "does not guarantee indexing, ranking, or citation." Primary spec not fetched. |
| B3.1 | **OpenAI, "Overview of OpenAI Crawlers"** — https://developers.openai.com/api/docs/bots | 3 | 3 | 3 | **9** | GPTBot (training) / OAI-SearchBot (search) / ChatGPT-User (fetch) are independent |
| B3.2 | **OpenAI Help Center, "Publishers and Developers FAQ"** — https://help.openai.com/en/articles/12627856 | 3 | 3 | 3 | **9** | "Any public website can appear in ChatGPT search"; utm_source=chatgpt.com |
| B3.3 | OpenAI content licensing deals (AP, News Corp, Dotdash Meredith, Axel Springer, Hearst, Future, Axios) — press/filing-sourced | 1 | 2 | 1 | **4** | Commercial discoverability, not documented ranking mechanics |
| B4.1 | **Anthropic, "Does Anthropic crawl data from the web…"** — updated April 7, 2026. https://support.anthropic.com/en/articles/8896518 | 3 | 3 | 3 | **9** | ClaudeBot / Claude-SearchBot / Claude-User; all respect robots.txt |
| B4.2 | **Claude API web search + Citations docs** | 3 | 3 | 3 | **9** | Citations always on for web search; cited_text/title/url |
| B5.1 | **Perplexity, "Perplexity Crawlers"** — https://docs.perplexity.ai/docs/resources/perplexity-crawlers | 3 | 2 | 3 | **8** | PerplexityBot (search, not training); Perplexity-User "generally ignores robots.txt" |
| B5.2 | **Perplexity Comet Plus publisher program** — Aug 25, 2025 post + Axios coverage | 2 | 2 | 2 | **6** | 80/20 revenue share; $42.5M pool |
| B6.1 | **Apple, "About Applebot"** — https://support.apple.com/en-us/119829 | 3 | 2 | 3 | **8** | Applebot-Extended = training opt-out only |
| B6.2 | **Brave Summarizer** — https://brave.com/blog/ai-summarizer/ + API docs | 2 | 1 | 3 | **6** | Own index; own LLMs |
| B6.3 | **Meta AI crawlers** — https://developers.facebook.com/docs/sharing/webmasters/web-crawlers | 3 | 1 | 2 | **6** | meta-externalfetcher may bypass robots.txt; page could not be directly fetched (429) |
| B6.4 | **xAI / Grok** — docs.x.ai web_search tool only (updated May 27, 2026) | 1 | 3 | 3 | **7** | Documentation gap is the finding: no crawler UA published |
| B7.1 | **OWASP GenAI, LLM01:2025 Prompt Injection** — https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 3 | 2 | 3 | **8** | Standards body, not a platform; cross-listed for A3 |

---

## Class C — Industry studies and tooling

| # | Source | Sample | Discl | Indep | Corrob | Total | Notes |
|---|---|---|---|---|---|---|---|
| C1.1 | **Ahrefs, "Top Brand Visibility Factors… 75k Brands"** — Dec 2025 / updated Aug 2026. https://ahrefs.com/blog/ai-brand-visibility-correlations/ | 3 | 1 | 0 | 2 | **6** | YouTube mentions ρ≈0.737; backlinks ρ≈0.218. Authors explicitly say correlation ≠ causation. Sells Brand Radar. |
| C1.2 | Ahrefs companion studies (12% overlap with top-10; AI-generated content citation; 17M-citation freshness) | 3 | 1 | 0 | 1 | **5** | — |
| C1.3 | **Semrush AI Visibility Index / citation studies** — 2026, 126M prompts. https://www.semrush.com/news/463141-... | 3 | 1 | 0 | 2 | **6** | Partly synthetic prompts; sells the toolkit |
| C1.4 | **Semrush + Kevin Indig, Authority Score vs AI mentions** — Oct 2025 | 2 | 1 | 1 | 1 | **5** | Authority Score predicts topic owner only 52.5% of the time |
| C1.5 | **SparkToro / Gumshoe, "consideration set" study** — Jan 2026. 600 volunteers, 2,961 runs, 60–100 runs per prompt | 2 | 2 | 1 | 3 | **8** | Best-designed industry study; per-response rank is noise, consideration set is stable. Fishkin sells audience tooling but not an AI-visibility tracker. |
| C1.6 | **SparkToro / Similarweb zero-click 2026** — June 8, 2026 | 3 | 2 | 1 | 1 | **7** | 68% zero-click; AI Mode only 0.34% of searches |
| C1.7 | **Similarweb, "Downstream Impact of AI Visibility"** — June 21, 2026 | 1 | 2 | 0 | 0 | **3** | 2.5× visit lift; three brand pairs; US desktop only; unreplicated |
| C1.8 | **Seer Interactive recency studies** — Oct 2025 / 2026 | 2 | 2 | 0 | 1 | **5** | Log-hit proxy, not citation; sells GEO services |
| C1.9 | **Profound, "How query language reshapes AI citations"** — Apr 2026, 3.25B citations, 14 countries. https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations | 3 | 1 | 0 | 2 | **6** | Language > geography; collection method not stated |
| C1.10 | Profound "Parrot Problem" / 27M-prompt earned-media / 15,155-brand config studies | 3 | 0 | 0 | 1 | **4** | — |
| C1.11 | **SISTRIX, "AI Citation Drift"** — May 2026, 82,619 prompts, 1.5M snapshots, 6 countries, 17 weeks. https://www.sistrix.com/blog/ai-citation-drift-... | 3 | 2 | 0 | 2 | **7** | Browser-interface monitoring; ChatGPT cites 68% English sources for German queries; weekly drift 56–74% |
| C1.12 | **BrightEdge** AIO presence tracking, mention/citation ratios | 3 | 0 | 0 | 1 | **4** | SERP parsing; methodology undisclosed |
| C1.13 | **Yext** 6.8M-citation study (Oct 2025) | 3 | 1 | 0 | 1 | **5** | "86% of citations from sources brands control" — conflicts directionally with earned-media findings; Yext sells listings management |
| C1.14 | **Kevin Indig / Growth Memo** research series | 2 | 1 | 1 | 1 | **5** | Independent analyst; some paywalled |
| C1.15 | **Gartner** (Feb 2024, 25% search decline by 2026 — later clarified as scenario) and **Forrester** (89% → 94% B2B buyer genAI adoption) | 2 | 1 | 2 | 1 | **6** | Adoption context for the business case, not visibility mechanics |
| C1.16 | ZipTie / QuickSEO source-count and overlap figures | 1 | 0 | 0 | 1 | **2** | — |
| C2 | **Tooling catalog** (Profound, Similarweb, Semrush, Ahrefs Brand Radar, Otterly, Peec, Evertune, and ~25 others) | — | — | — | — | — | Not scored as evidence. Retained as build-vs-buy reference with the three-architecture taxonomy (API prompting / browser automation / consumer panel). |

---

## Conflicts between reports, and resolutions

1. **Nestaas et al. venue.** Run 1: "could not confirm." Run 5: ICLR 2025. **Verified ICLR 2025** via proceedings listing. Scored accordingly.
2. **Two "GEO" preprints with adjacent IDs.** Run 1 suspected 2509.08919 and 2509.10762 might be duplicates. They are distinct: 2509.08919 is Chen et al. (U. Toronto); 2509.10762 is Kumar & Palkhouski (Wrodium, GEO-16). Both indexed separately.
3. **Kamruzzaman page numbers** differ between runs (12704–12721 vs 12695–12702). Immaterial; venue confirmed.
4. **ChoiceEval attribution.** arXiv lists Rienecker et al.; some citing papers say "Chen et al." Indexed under Rienecker with a note.
5. **Earned media vs owned content.** Chen et al. and most vendors say earned media dominates citations; Yext says 86% come from brand-controlled sources. Not reconciled. Likely explained by Yext counting listings (Yelp, Google Business Profile) as "controlled." The agent should treat this as unresolved and category-dependent.
6. **LLM popularity bias.** Lichtenberg (Amazon) finds LLMs *less* popularity-biased than collaborative filtering; everything else finds strong incumbent bias. Resolution: Lichtenberg measures a different thing (LLM as ranker over a candidate list vs. LLM volunteering brands from memory). Both can be true. Kept as the honest dissent.

## Gaps the runs did not fill

- **No study measures enterprise B2B technology categories directly.** GEO-16 (B2B SaaS, Provisional) is the closest. Everything else is consumer goods, news, or encyclopedic facts. The agent must state this when advising on F5-type categories.
- **No controlled experiment on the parametric pathway for brands.** All parametric evidence is EXTRAPOLATED from encyclopedic-fact research. This is the single largest epistemic gap and must be labeled on every parametric recommendation.
- **No source separates search-on from search-off systematically** across consumer products. The methodology section must require it.
- **C-SEO Bench** (A1.17) unread. If it is a negative replication of GEO tactics, it would lower A1.1's corroboration score. Priority follow-up.
- **Agent-harness surface** (Claude Code, Cursor, Copilot) has zero direct evidence. ACES (A1.6) is the only adjacent work and covers shopping agents, not developer tools.
- **Run 2's secondhand cluster** (A2.23) needs primary verification before any specific figure is used.

## Scoring judgments the agent must be aware of

These are places where relevance and evidence quality pull in opposite directions. The scores were kept as assigned; the notes explain why, so the agent does not silently over- or under-weight them.

- **A1.11 Chu & Hou ("Incumbent Advantage") is the most directly relevant paper in the corpus and one of the weakest by rubric.** It is the only study that isolates *why* a known brand wins and what breaks that advantage. It is also a two-month-old preprint, single-domain (skincare), API-only with search off, and from an institution without a track record in this field. The agent should use its findings as the leading hypothesis for incumbent dynamics and frame them as "preliminary evidence suggests" until replicated. If a replication appears, this source moves to Solid; if a negative replication appears, drop it to Weak.
- **A1.12 GEO-16 is the only study in a domain adjacent to enterprise technology (B2B SaaS) and is scored Provisional.** Commercial research entity, single study, page-quality correlations only. The agent may cite it as the closest available evidence for B2B citation behavior but must pair it with A1.1 before turning any pillar into a recommendation.
- **C1.5 SparkToro consideration-set study is the highest-scored Class C source because of its design (60–100 runs per prompt, published method), not its venue.** It is still not peer-reviewed. Its central claim — per-response rank is noise, the consideration set is the stable asset — should be treated as the working assumption for the testing methodology, and the agent should explicitly recommend the same repetition count.
- **All parametric-pathway evidence is EXTRAPOLATED.** No study in the corpus tests whether commercial brands follow the frequency-drives-recall law demonstrated for encyclopedic facts. The mechanism is almost certainly identical, but the agent must attach "inferred from research on non-brand entities" to every parametric-pathway recommendation and must never present parametric lift as a measurable, attributable outcome.
- **B1.1 Google's official guidance is the strongest "noise" verdict available.** llms.txt, content chunking, rewriting-for-AI, seeking inauthentic mentions, and schema-as-a-requirement are explicitly stated not to matter for Google's generative surfaces. When a user proposes one of these, the agent should cite B1.1 directly. This verdict applies to Google's surfaces; other providers have not stated equivalents, so the agent should say "no provider documents this as a signal" rather than "this does nothing everywhere."
- **Earned media dominance is the most actionable and best-corroborated lever in the corpus.** Supported across Class A (A1.9), Class B (B1.1's warning against inauthentic mentions implies authentic ones matter), and Class C (C1.1, C1.3, C1.5), with one directional dissent (C1.13 Yext, likely a definitional difference over listings). The agent should lead with this lever for any brand whose buyers research in documentation, forums, and analyst content.
- **A1.16 Lichtenberg is retained as the honest dissent on popularity bias.** It measures LLM-as-ranker over a supplied list, not LLM-as-volunteer from memory. The agent should cite it when a user claims "LLMs always favor incumbents" to keep the claim precise.
- **A1.17 C-SEO Bench is unscored and could lower A1.1's corroboration.** Until read, the agent should mention its existence when stating the GEO lift figures and note that a replication benchmark exists whose result is not yet incorporated.

## Proposed usage rules for the agent (to be carried into the system prompt)

- Every recommendation cites at least one source by index number and states its tier.
- Strong/Solid Class A → may be stated as a finding.
- Provisional Class A → stated as "preliminary evidence suggests"; never as the sole basis.
- Class B → authoritative for mechanism; never cited for "what to do" beyond eligibility hygiene.
- Class C → "industry data indicates"; must be paired with Class A or B before becoming a recommendation.
- EXTRAPOLATED sources → recommendation must carry the phrase "inferred from research on non-brand entities."
- DO-NOT-RECOMMEND sources → cited only in competitive-intelligence and detection contexts.
