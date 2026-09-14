# Brand Visibility in LLM Answers: Industry Studies, Measurement Tooling, and Multilingual/Regional Evidence

## TL;DR
- **The measurement market is real but methodologically shaky.** A cluster of large-sample vendor studies (Ahrefs 75k brands, Semrush 126M prompts, Seer, SparkToro) converge on a few robust findings — earned/third-party media and off-site mentions (YouTube, Reddit, Wikipedia) drive AI visibility far more than backlinks or on-page SEO, "big-brand bias" is strong, and per-response rankings are effectively random noise — but most studies conflate correlation with causation, rarely publish prompts, and each vendor sells a tool that benefits from the finding.
- **Tooling splits into three data architectures**, and the distinction is the single most important build-vs-buy variable: (1) synthetic prompting of model APIs/interfaces (most trackers), (2) browser automation of the consumer product (Otterly, Peec, SISTRIX), and (3) licensed consumer-panel/clickstream data (Profound, Similarweb, Semrush/Adobe). No tool fully separates search-on/grounded from search-off/ungrounded modes, and few disclose runs-per-prompt or temperature.
- **Visibility does not transfer across languages** — this is the strongest cross-source conclusion. Peer-reviewed work (Kamruzzaman et al. EMNLP 2024; Qi et al. EMNLP 2023) shows global-brand and cross-lingual-consistency bias, and 2026 vendor data (Profound's 3.25B-citation language study; SISTRIX's finding that ChatGPT cites 68% English sources even for German queries) corroborate that AI visibility work must be done per-language and per-platform.

## Key Findings

**Corroborated by both academia and industry:**
1. **Earned/third-party media dominates citations over brand-owned content.** A preprint (Chen et al., arXiv:2509.08919) and multiple vendor datasets agree AI search structurally favors third-party authoritative sources.
2. **"Big-brand / incumbent" bias is strong.** Academic (Kamruzzaman EMNLP 2024; the "Incumbent Advantage" preprint showing 100% recommendation of known brands when specs are identical) matches Ahrefs' finding that established brands dominate, especially in Google AI Mode.
3. **AI answers are non-deterministic and volatile.** Academic consensus (no model is deterministic at temperature 0) matches vendor observations (SparkToro: <1-in-100 chance of an identical list across runs; Semrush: Reddit citations fell from ~60% to ~10% in weeks).
4. **Language changes outputs.** Cross-lingual consistency research (Qi et al. 2023; PolyFact 2026) matches Profound/SISTRIX vendor data.

**Industry claims NOT well-corroborated by peer-reviewed work:**
- Specific "correlation" rankings of ranking factors (e.g., Ahrefs' YouTube-mentions Spearman ≈0.737) are vendor analyses, not peer-reviewed, and are explicitly correlational (Ahrefs' own authors note "correlation does not equal causation").
- Revenue/traffic multipliers ("ChatGPT visitors convert at 23x," "2.5x more site visits") are single-vendor panel findings without replication.
- "82–95% of citations come from earned media" is a widely-repeated range built from mixed vendor sources and one preprint; the precise percentages vary by study and are not independently validated.

## Details

### PART A — INDUSTRY / VENDOR STUDIES

**Ahrefs — "Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews (75k Brands Studied)"**
- Authors: Louise Linehan (Content Marketer), Xibeijia Guan (data scientist); reviewed by Ryan Law. Ahrefs (commercial SEO tool vendor — sells Brand Radar).
- Vendor blog. Published December 12, 2025; last modified August 12, 2026. URL: https://ahrefs.com/blog/ai-brand-visibility-correlations/
- Code/data: not released.
- Platforms: ChatGPT, Google AI Mode, Google AI Overviews (version identifiers not stated).
- Sample: 75,000 brands. Methodology (per The Next Web coverage, May 2026): filtered to domains with Domain Rating >40 and at least one keyword at 800+ monthly searches.
- Core finding: YouTube mentions show the strongest correlation with AI visibility (Spearman ≈0.737, consistent across all three platforms), outperforming every other factor; YouTube mention impressions ≈0.717; branded web mentions ≈0.664; backlinks only ≈0.218; classic authority metrics correlate weakly for ChatGPT (branded search volume 0.352, Domain Rating 0.266). AI Mode rewards established brands more than emerging ones.
- Effect size: Spearman correlation coefficients as above.
- Limitations/COI: purely correlational (authors explicitly state "correlation does not equal causation"); Ahrefs sells the tool (Brand Radar) that produces the metric. Prompts not published.
- Pathway: primarily parametric recall + retrieval (measures brand mentions in outputs, not mechanism).

**Ahrefs — companion studies:** "Only 12% of AI Cited URLs Rank in Google's Top 10" (15,000 prompts; ChatGPT, Gemini, Copilot, Perplexity; https://ahrefs.com/blog/ai-search-overlap/); "AI Overviews Cite AI-Generated Content More Than Human Writing" (1M SERPs, 1.9M URLs; https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/); 17M-citation freshness analysis (AI-cited content 25.7% fresher than traditional organic). All vendor-published, correlational, prompts largely unpublished.

**Semrush — AI Visibility Index (2026, expanded) and January 2026 citation study**
- Publisher: Semrush (an Adobe company; commercial SEO/AI-visibility vendor).
- News release, February–May 2026. URL: https://www.semrush.com/news/463141-semrush-releases-expanded-2026-ai-visibility-index-analyzing-126-million-ai-search-prompts/
- Sample: original AI Visibility Index (Sept 2025) 2,500 prompts, expanded to 126 million U.S. AI search prompts (Jan–Apr 2026); a separate large-scale study of 230,000 prompts / 100M+ citations across ChatGPT, Google AI Mode, Perplexity; a January 2026 study of 304,805 AI-cited URLs vs 921,614 traditionally ranked URLs.
- Core finding: A small set of domains (Reddit, LinkedIn, Wikipedia, Medium, YouTube, Google properties) dominates AI citations; these hierarchies do not mirror Google's top 10. Mentions ≠ citations (on Gemini, overlap between mentioned brands and cited domains can be as low as 30%). Q&A format shows a 25.45% citation advantage.
- Data source: Semrush's prompt database (239M+ prompts/responses) built from direct API integration where possible, user-behavior analysis, and synthetic prompt generation — i.e., partly synthetic/modeled, not raw consumer behavior.
- Limitations/COI: vendor sells the AI Visibility Toolkit; prompts not published; "synthetic prompt generation" means some data is modeled, not observed.
- Pathway: retrieval/grounding (citations) + parametric (mentions).

**Seer Interactive — "Study: AI Brand Visibility and Content Recency" (Oct 2025) and 2026 follow-up**
- Publisher: Seer Interactive (digital marketing agency). URL: https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency; 2026: https://www.seerinteractive.com/insights/study-content-recencys-impact-on-ai-visibility-in-2026
- Sample: 5,000+ URLs (2025); 2026 study 7,683 pages / 47,097 citations across ChatGPT, Gemini, Perplexity (Mar–Jun 2026).
- Core finding: Strong recency bias — ~65% of AI bot hits target content from the past year, 89% within three years, only 6% older than six years. Recency requirement varies by vertical (Financial Services demands freshest; Travel/Energy more evergreen-tolerant).
- Method: analyzed AI-bot log-file hits and cited URLs (a crawl-behavior proxy, not direct answer-output measurement).
- Limitations/COI: agency sells GEO services; log-hit frequency is a proxy for citation, not citation itself.
- Pathway: retrieval/grounding.

**SparkToro — "consideration set" / AI-rankings-are-noise study (Jan 2026)**
- Authors: Rand Fishkin (SparkToro), co-authored with Patrick O'Donnell (Gumshoe.ai).
- Published January 2026. Method: 600 volunteers, 2,961 prompt runs across ChatGPT, Claude, and Google AI across 12 product/service categories, Nov–Dec 2025, with 60–100 runs per prompt.
- Core finding: Per-response rank is effectively random; the stable asset is the "consideration set." Across 994 AI responses, headphone brands (Bose, Sony, Sennheiser, Apple) appeared 55–77% of the time regardless of phrasing; in one stable category, City of Hope appeared in 69 of 71 responses for West Coast cancer-care hospitals. Fishkin's verbatim conclusion: "any tool that gives a 'ranking position in AI' is full of baloney." Brands appearing 70%+ of the time shared deep earned-media presence.
- Limitations/COI: SparkToro sells audience-research tooling; full prompt list availability not confirmed.
- Pathway: parametric recall + retrieval.
- **Also SparkToro/Similarweb 2026 zero-click study** (Rand Fishkin, published June 8, 2026, on Similarweb US desktop+mobile panel Jan–Apr 2026): 68.01% of US Google searches ended without a click (up from 60.45% in 2024); only 0.34% of searches reached AI Mode — so AI Overviews, not AI Mode, drive current zero-click growth. Note the panel-comparability caveat Fishkin himself flags (stitches Jumpshot 2016/2019, Datos/Semrush 2024, Similarweb 2026).

**Similarweb — "The Downstream Impact of AI Visibility" (June 21, 2026)**
- Publisher: Similarweb (clickstream/panel data vendor).
- Sample: real user journeys across three verticals (Finance, Travel, Beauty), six months (July–Dec 2025) of US desktop panel clickstream + a Jan 2026 survey. Brand pairs: Amex vs Capital One, Skyscanner vs Kayak, Sephora vs Ulta.
- Core finding: Per Similarweb's own report, "users recommended a brand by ChatGPT were 2.5 times more likely to visit that brand's site within seven days than a competitor's." Notably, 55.9% of those AI-influenced visits arrived through search rather than a direct AI referral; AI-influenced visitors averaged 12.0 pages / 11.8 minutes vs 6.5 pages / 5.6 minutes for others. First study to use panel clickstream (not modeled estimates) to link AI recommendation to downstream traffic.
- Limitations/COI: vendor sells the panel/AI-visibility product; US desktop panel only; small brand-pair sample; correlation not causation (the 55.9%-via-search finding shows AI recommendation and branded-search demand are entangled).
- Pathway: consumer-facing product behavior (measures downstream traffic, not mechanism).

**Kevin Indig / Growth Memo** — ongoing research series (e.g., "State of AI Search Optimization 2026," Jan 5, 2026; a UX study of 70 users / 400+ AI Overview encounters / 29 hours of think-aloud sessions; a topical-authority analysis of 50,000+ brands; an 846K-session clickstream study). URL: https://www.growth-memo.com. Independent analyst (advises Ramp, Reddit, Dropbox, etc.); some content paywalled; a recurring theme is that aggregate AI dashboards mask per-engine invisibility ("A brand can look dominant in an aggregate AI dashboard and be invisible in two of three engines").

**BrightEdge** — AIO presence tracking (Generative Parser): AIO presence grew ~30%→~48% of tracked queries Feb 2025→Feb 2026 (+58% YoY); ~52% of queries trigger no AIO; ~17% of AIO-cited sources also rank organic top 10. Vendor SERP-parsing data. URL: https://www.brightedge.com/resources/weekly-ai-search-insights/ai-overviews-one-year-presence-size-citing

**Analyst coverage:** Gartner's press release (February 19, 2024), quoting VP Analyst Alan Antin, states: "By 2026, traditional search engine volume will drop 25%, with search marketing losing market share to AI chatbots and other virtual agents." Antin later clarified (Big Technology interview) that the figure reflects scenario modeling, not certainty. Forrester's Buyers' Journey Survey (report "B2B Buyer Adoption Of Generative AI," Nov 20, 2024) found: "In less than two years, 89% of B2B buyers have adopted generative AI (genAI), naming it one of the top sources of self-guided information in every phase of their buying process." Forrester's later State Of Business Buying, 2026 (BusinessWire, Jan 21, 2026; ~18,000 global buyers) raised this figure to 94%. First-party Gartner/Forrester GEO Magic-Quadrant-style reports were not located as primary documents in this research.

**⚠️ API-vs-consumer-product conflation flag:** Many industry studies and the "Incumbent Advantage" academic preprint query model APIs (often with search off, and at set temperatures) but describe results as consumer-product behavior ("ChatGPT recommends…"). Profound's own comparison notes that "API-based access to base models captures responses that can differ meaningfully from what real users see through front-end interfaces." Semrush's database uses "synthetic prompt generation." This is the single most common validity problem in the space.

### PART B — TOOLING CATALOG

Three data architectures (the key build-vs-buy axis):
- **(A) Synthetic prompting of model APIs / interfaces** — runs a defined prompt set against models on a schedule.
- **(B) Browser automation of the consumer product** — queries the actual front-end "the way a human user does."
- **(C) Licensed consumer-panel / clickstream data** — analyzes real users' AI conversations or downstream clicks.

**Profound** — Architecture C (plus response analysis and crawler tracking). Licenses 1.3B+ anonymized conversations from double-opt-in consumer panels (GDPR/CCPA compliant), tens of millions of prompts/month, weekly refresh, multi-region (US, UK, Canada, Germany, France, and more). "Share of Model"/Profound Index leaderboard. Captures browser-rendered consumer experience (described by third parties as the most accurate current technique). SOC 2 Type II. Enterprise pricing (custom). Coined/popularized "share of model" alongside Foundation. Distinguishes mentions vs citations; does not clearly separate search-on/off in public docs.

**Similarweb AI Brand Visibility + AI Traffic** — Architecture C. Tracks ChatGPT, Perplexity, Gemini, AI Mode for visibility; referral traffic from Copilot, Claude, DeepSeek, Grok. Based on its decade-old clickstream panel. Entry ~$99/mo for 150 prompts; higher tiers ($399/$649) buy the rest of the Similarweb platform, not more AI coverage.

**Semrush AI Visibility Toolkit / Enterprise AIO** — Architecture A+C hybrid (239M+ prompt database via API integration + synthetic generation + user-behavior analysis). Six reports (Visibility Overview, Competitor Research, Prompt Research, Brand Performance, Prompt Tracking, AI Search Site Audit). AI Visibility Score = mentions relative to median of top competitors. Prompt Tracking updates daily. Coverage expanding by country (32 countries / 261M prompts as of May 2026). Adobe integration ("Adobe Brand Visibility," ~300M consented AI prompts).

**Ahrefs Brand Radar** — Architecture A/B (searches long-tail queries across Google/Bing and asks the same to assistants). Tracks mentions/citations across AI Overviews, ChatGPT, plus YouTube/Reddit/TikTok signals. Entry ~$828/mo including required base plan (per Otterly's comparison).

**Otterly.AI** — Architecture B (real web-interface monitoring, not API). Tracks all 7 engines (ChatGPT, Perplexity, AI Overviews, Gemini, Copilot, AI Mode, Claude). Best-in-class multi-country: 50–65+ countries and languages, with a published per-country×engine availability matrix. Public API, MCP server, Looker Studio connector. Pricing from $29/mo (Lite, 15 prompts) to ~$422/mo (Premium); engine add-ons per tier.

**Peec AI** — Architecture B (UI scraping). All six engines (ChatGPT, Perplexity, AI Overviews, Gemini, Claude, AI Mode) on base plans (some add-on). Multilingual citation tracking (115+ languages); unlimited countries/languages, priced by prompts × models. Distinguishes content "used" vs "cited." Runs each prompt once per 24h per model. Raised $29M. Pricing €89–€199+/mo (Starter/Pro), unlimited team seats.

**Evertune** — Architecture C-lite. EverPanel consumer panel of ~25M people; clusters prompts into topics rather than tracking keywords. Limitation: panel is a sliver of global AI usage; also uses API-based access to base models.

**Others catalogued (from vendor/comparison pages):** Conductor (2026 AI Overview Benchmarks, 21.9M queries), seoClarity, Scrunch AI (enterprise, custom pricing), Goodie AI, Athena HQ (~$295/mo, monitoring-first), Bluefish AI, Rankscale, ZipTie, Xfunnel, AirOps (Kevin Indig's "State of AI Search"), Adobe LLM Optimizer, HubSpot AEO Grader, Writesonic GEO, Gauge, Waikay, Am I Cited, ModelMonitor, LLMrefs, Nightwatch, SE Ranking AI, Moz AI, Yext Scout. Most are Architecture A or B; pricing and methodology vary and are often undisclosed.

**Variance handling across tools:** Practitioner consensus (and vendor docs) hold that reliable share-of-model requires ~60–100 runs per prompt (matching SparkToro's academic-grade design); most consumer tools run each prompt far fewer times (Peec: once/24h/model). Election-forecasting-style approaches use 250–500 high-intent queries per brand. Temperature is rarely disclosed. Almost no tool cleanly separates grounded (search-on) from ungrounded (search-off) modes — a major measurement gap.

### PART C — MULTILINGUAL & REGIONAL

**ACADEMIC (peer-reviewed and preprint):**

**Kamruzzaman, Nguyen & Kim — "'Global is Good, Local is Bad?': Understanding Brand Bias in LLMs"** — EMNLP 2024 (peer-reviewed, ACL Anthology, pp. 12695–12702). Authors: Mahammed Kamruzzaman, Hieu Minh Nguyen, Gene Louis Kim (Univ. of South Florida). URL: https://aclanthology.org/2024.emnlp-main.707/ (arXiv:2406.13997). Code/data released: https://github.com/hieuminh65/LLM-Brand-Bias. Models: GPT-4o, Llama-3-8B, Gemma-7B, Mistral-7B. Sample: curated dataset across four brand categories (shoes, clothing, beverages, electronics), global vs local brands. Core finding: consistent bias favoring global brands with positive attributes and recommending luxury gifts to high-income countries; country-of-origin effects can boost local-brand preference in specific contexts. Effect sizes: e.g., GPT-4o recommended global brands ~98–100% for shoes/clothing/beverages. Pathway: parametric recall (probing training-data bias). Limitation: smaller/older open models; probing, not live product behavior.

**Qi, Fernández & Bisazza — "Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models"** — EMNLP 2023 (peer-reviewed). arXiv:2310.10378. Proposes RankC metric. Finding: large factual-knowledge variation across languages; increasing model size raises accuracy but NOT cross-lingual consistency. Pathway: parametric recall.

**von Rad et al. — "Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning"** (University College London, Centre for AI, arXiv:2606.06586, 2026). Introduces PolyFact (100K Wikidata facts, 12 languages), tested on Qwen-2.5-7B and OLMo-2-1124-7B. Finding: cross-lingual factual inconsistency is "less a problem of missing knowledge than of unreliable access"; GRPO improves consistency and generalization to unseen languages. Code/data released. Pathway: parametric recall.

**"Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems"** (arXiv:2606.17443, 2026; preprint). Models: GPT-4o-mini, Claude Sonnet, Gemini 3 Flash, in English and Chinese, temp 0.7, 20–30 reps/cell. Finding: "Conditional Monopoly" — known brand recommended 100% of 670 valid trials (IAI=10.0) when specs identical, across both languages and all subcategories; dominance breaks with a +0.1-star competitor advantage; authority-style/fabricated-clinical marketing language breaks the monopoly at a Bias Surplus Value of +0.17 rating points. Pathway: parametric recall + context (manipulated descriptions). Flag: API-based, search-off — describes model behavior, not consumer product.

**Chen, Wang, Chen & Koudas — "Generative Engine Optimization: How to Dominate AI Search"** (Univ. of Toronto, arXiv:2509.08919, Sept 10, 2025; preprint, not peer-reviewed). Large-scale controlled experiments across multiple verticals, languages, and query paraphrases on ChatGPT, Perplexity, Gemini vs Google. Finding: AI search shows "systematic and overwhelming bias towards Earned media over Brand-owned and Social content," unlike Google's balanced mix; engines differ in domain diversity, freshness, cross-language stability, and phrasing sensitivity; explicitly recommends "engine-specific and language-aware strategies" and overcoming "big brand bias." Pathway: retrieval/grounding.

**Related fairness/bias and GEO works:** Bias Beware (cognitive biases as adversarial levers, National Technical University of Athens, arXiv:2502.01349); Cold-Start recommender bias (arXiv:2508.20401, Gemma 3 / Llama 3.2); Gender/Race product-recommendation bias (arXiv:2602.08124, AINA 2025); Linguistic/dialectal bias in recommendations (arXiv:2604.25456); GEO founding paper (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande — Princeton/Georgia Tech/Allen AI/IIT Delhi, KDD 2024, arXiv:2311.09735 — GEO-bench ~10,000 queries across 9 datasets; optimization lifts visibility 22–41% on Position-Adjusted Word Count/Subjective Impression, +115% for position-5 pages).

**INDUSTRY (multilingual/regional):**

**Profound — "How query language reshapes AI citations"** (Davis McCain, April 21, 2026; data March 2026). URL: https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations. Sample: 3.25 billion AI citations; 7 models; 14 countries filtered to native-language prompts (US/GB/AU English, DE German, FR French, IT Italian, ES/MX Spanish, BR Portuguese, JP Japanese, SE Swedish, IN Hindi, SA/AE Arabic). Core finding: query LANGUAGE is the dominant force (over geography). Google AI Overviews social-citation rate 15.3% vs Gemini 3.6%; AIO social rate Mexico 22.5% / Spain 20.0% (~1.4x English) while ChatGPT is ~0.5x English in Spanish. YouTube share of Google AIO social citations: English 38% vs Portuguese-BR 65% vs Arabic 26% (Arabic is the only language where YouTube loses the top spot, to Instagram at 29%). ChatGPT social citations are 51–76% Reddit in every country. Explicit conclusion: "tracking prompts in local languages is not optional. English-language tracking is a proxy at best, a blind spot at worst." Data-collection mechanism (API vs automation) not stated in the post.

**SISTRIX — "AI Citation Drift: How stable are sources in AI search results?"** (Johannes Beus, founder, May 1, 2026, updated May 12). URL: https://www.sistrix.com/blog/ai-citation-drift-how-stable-are-sources-in-ai-search-results/. Sample: 82,619 qualified prompts / 1,548,213 snapshots; 6 countries (DE, US, UK, IT, ES, FR); 3 platforms (Google AI Mode, AI Overviews, ChatGPT Search); 17 weeks (Dec 2025–Apr 2026). Browser/interface monitoring via SISTRIX AI Research Index. Core findings: **language bias** — in AI Mode, 80% of core domains are German for German queries, but ChatGPT cites 68% English sources even for German queries ("the source pools of the two platforms can hardly overlap for the German market"); AIO and AI Mode cite different domains 83% of the time (Jaccard 0.17); weekly citation drift AIO 5%, AI Mode 56%, ChatGPT 74%; ChatGPT drift differs by country (Germany 74% vs France 42%, attributed to differing crawl coverage by language). Conclusion: "Platform-specific citation strategies are… not optional, but a fundamental requirement."

**Google AI Overviews rollout timeline by market:** US only (May 14, 2024) → UK, India, Japan, Indonesia, Mexico, Brazil in local languages (Aug 15, 2024) → 100+ countries, 6 languages — English, Hindi, Indonesian, Japanese, Portuguese, Spanish (Oct 28, 2024) → EU (Austria, Belgium, Germany, Ireland, Italy, Poland, Portugal, Spain, Switzerland; March 26, 2025, delayed partly by the Digital Markets Act) → 200+ countries / 40+ languages, ~2B monthly users (Google I/O, May 2025). France faced regulatory delay (reported by vendor/secondary sources).

**Vendor multi-country coverage:** Otterly.AI (50–65+ countries/languages, per-country×engine availability matrix; notes ChatGPT/Perplexity localize responses by country); Semrush expanded to 32 countries / 261M prompts (May 14, 2026); Peec AI (unlimited countries, 115+ languages).

**⚠️ Unverified regional figures:** The widely-repeated "non-English markets see 15–30% lower AIO trigger rates (BrightEdge 2026)" and "English 30% / Hindi 28% / Spanish 24% trigger rates (Semrush)" appear only in a secondary aggregator (searchlab.nl), not on primary vendor pages — treat as unconfirmed.

### Corroboration Map: Academia vs Industry
| Claim | Academic support | Industry support | Verdict |
|---|---|---|---|
| Earned media > brand-owned in AI citations | Chen et al. (preprint) | Semrush, SparkToro, Seer, Yext | Corroborated (industry stronger; academic is preprint) |
| Big-brand/incumbent bias | Kamruzzaman EMNLP 2024; Incumbent Advantage preprint | Ahrefs 75k | Corroborated |
| Non-determinism / rank is noise | General LLM literature | SparkToro, Semrush | Corroborated |
| Visibility varies by language; must optimize per-language | Qi et al. 2023; PolyFact 2026; Chen et al. | Profound, SISTRIX | Corroborated |
| Recency bias | Weak (freshness in training) | Seer, Ahrefs | Industry-only, plausible |
| Specific factor correlations (YouTube ≈0.737) | None | Ahrefs | Industry-only, correlational |
| Traffic/revenue multipliers (2.5x, 23x) | None | Similarweb, Ahrefs | Industry-only, unreplicated |

### Recurring Methodological Weaknesses
1. **Single-run / low-run sampling** despite non-determinism (reliable share-of-model needs ~60–100 runs/prompt, per SparkToro's design; most tools run 1×/day).
2. **No confidence intervals or significance testing** in vendor reports.
3. **Unpublished prompts and prompt sets** — non-reproducible.
4. **API-vs-consumer-product conflation** — querying base-model APIs (often search-off) but reporting as "ChatGPT recommends…"
5. **No search-on/off (grounded/ungrounded) distinction.**
6. **Unstated model versions and dates** — critical given weeks-scale volatility.
7. **Cherry-picked verticals / small brand samples** (e.g., three brand pairs).
8. **Vendor self-interest** — every study sells the tool that produces the metric.
9. **Correlation-causation conflation** — correlational factor studies presented as optimization playbooks (Ahrefs at least flags this explicitly).
10. **Proxy metrics** — log-file bot hits or synthetic prompts standing in for real citations/behavior.
11. **Panel comparability** — stitching different clickstream panels across years (SparkToro's own caveat).

## Recommendations

**Stage 1 — Calibrate (weeks 1–4).** Build a lightweight in-house harness before buying: define a 250–500 prompt set of real category questions, run each prompt 30–100 times per model, at a fixed temperature, with explicit search-on and search-off configurations logged separately, recording model version and date every run. This directly addresses weaknesses 1, 3, 4, 5, 6. Benchmark your DIY share-of-model against a cheap tool (Otterly at $29/mo or Peec Starter) to sanity-check.

**Stage 2 — Buy for coverage you can't replicate (months 2–3).** License one panel/clickstream tool (Profound or Similarweb) for real-user prompt-volume and downstream-traffic data — this is the one thing you cannot build. Add one browser-automation tracker (Otterly or Peec) if you need multi-country/multi-language monitoring, because visibility does not transfer across languages.

**Stage 3 — Localize (months 3–6).** Treat every target language as a separate optimization problem. Track prompts in-language (not translated), and expect different citation source mixes per language (Profound/SISTRIX). Prioritize earned media in the third-party publications each engine trusts in that market.

**Benchmarks that change the plan:**
- If DIY share-of-model has confidence intervals wider than ±10 points at 30 runs, increase to 100 runs before trusting any vendor number.
- If a vendor cannot state runs-per-prompt, temperature, model version, and search-on/off, treat its absolute numbers as directional only.
- If AI referral traffic exceeds ~5% of total organic (currently ChatGPT ~0.2%, Perplexity <2% per SparkToro), shift budget from measurement toward conversion instrumentation.
- If your brand appears in <55% of consideration-set responses (SparkToro's stability threshold), the problem is earned-media presence, not on-page formatting.

## Caveats
- This space changes on a weekly-to-monthly cadence; citation-source mixes shift dramatically (Semrush saw Reddit fall from ~60% to ~10% in weeks; SISTRIX measured 56–74% weekly citation drift in AI Mode/ChatGPT). All figures are point-in-time (2025–2026).
- Several headline vendor numbers could only be verified in secondary coverage or are single-vendor findings without replication; these are flagged inline.
- Two of the most-cited GEO/bias works (Chen et al. 2509.08919; Incumbent Advantage 2606.17443) are preprints, not peer-reviewed, and the latter uses search-off API calls.
- The distinction between what a tool *measures* (API vs browser vs panel) and what it *claims to represent* (consumer product behavior) is the dominant source of error across the entire field — weight sources accordingly.
- Author lists, sample sizes, and URLs are reported as found; where a field was not disclosed by the source, it is marked "not stated." First-party Gartner/Forrester GEO market reports, and the primary Google rollout blog posts for every market date, were not all independently fetched — dates are corroborated via multiple vendor/secondary sources.