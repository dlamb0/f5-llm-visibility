# Adversarial Manipulation of LLM Recommendations, Detection, and Recommender-System Bias Foundations

## TL;DR
- **Manipulating what LLMs recommend is empirically demonstrated and often cheap.** Retrieval/context attacks (strategic text sequences, preference-manipulation prompt injection, cognitive-bias framing, and AI-targeted cloaking) reliably move a chosen product to the top of an LLM answer, with reported effects ranging from a 34.0%→59.4% recommendation-rate jump (2.5× lift) up to a near-total "conditional monopoly" flip; most are detectable in principle but are not yet reliably caught in production.
- **Established-brand dominance in LLM recommendations is a predictable extension of decades-old recommender/IR biases** — popularity bias, position bias, and cumulative-advantage feedback loops — now compounded by LLM-specific effects (parametric brand recall, "lost in the middle" position sensitivity, and order/selection bias).
- **Challengers displace incumbents under specific, documented conditions:** a genuine and legible quality/novelty advantage, exploration/randomization in the ranker, debiasing/re-ranking that promotes the long tail, and provenance/verification that neutralizes manipulation. Absent these, feedback loops entrench incumbents.

---

# PART A — ADVERSARIAL & MANIPULATION RESEARCH
> **Framing note (read first):** This section is compiled strictly for **defensive awareness and competitive intelligence**. Several tactics below deceive users and violate the published terms of Google, OpenAI, Microsoft/Bing, and Perplexity. It is a threat catalog to help detect and defend against manipulation of your own and competitors' visibility — not an implementation guide.

## Key Findings (Part A)
1. **Two attack surfaces dominate.** Nearly every demonstrated LLM-recommendation attack exploits the **retrieval/grounding** pathway (poisoning web pages, RAG databases, plugin docs) or the **context** pathway (prompt injection, cloaked content, uploaded documents). Pure **parametric** manipulation (training-data poisoning for brand promotion) is discussed but less demonstrated at product scale.
2. **Effect sizes are large.** Strategic text sequences can move a product from ~rank 10 to rank 1; preference-manipulation injections raised a fictitious camera's recommendation rate from 34.0% to 59.4% (2.5×) and made a GPT-4 news plugin 2–8× more likely to be selected; PoisonedRAG hits 90–99% attack success with only 5 injected texts.
3. **Detectability varies sharply.** Gibberish adversarial strings (GCG-style STS) are detectable by perplexity filters; "clean," human-readable persuasion (cognitive-bias framing, fabricated authority) is much harder to detect and is the direction the literature is trending.
4. **Platforms have begun to respond.** Google formally extended its spam policies to AI Overviews/AI Mode on May 15, 2026; indirect prompt injection is OWASP LLM01:2025; vendor and academic defenses exist but are repeatedly shown to be insufficient against adaptive attacks.

## Details (Part A) — Source-by-source

### Foundational manipulation papers

**1. Manipulating Large Language Models to Increase Product Visibility (Strategic Text Sequences)**
- Authors/affiliations: Aounon Kumar, Himabindu Lakkaraju (Harvard University).
- Venue/status: arXiv preprint 2404.07981 (cs.IR/cs.AI/cs.CL). v1 submitted 11 Apr 2024; v2 last revised 2 Sep 2024.
- URL: https://arxiv.org/abs/2404.07981
- Code/data: Yes — authors released code and a fictitious coffee-machine catalog.
- Models/platforms: STS optimized via the GCG algorithm (targeting the objective `1. [Target Product Name]`); demonstrated against a Bing Copilot–style RAG search interface.
- Sample size: A catalog of 10 fictitious coffee machines; two target products analyzed (one seldom-recommended, one usually rank 2).
- Core finding: Adding an adversarially optimized "strategic text sequence" to a product's page reliably increases its chance of being the LLM's #1 recommendation; the target moved from near-bottom (≈rank 10) to top (≈rank 1).
- Effect size: Rank shift from ~10 to ~1 after STS insertion.
- Limitations/COI: Fictitious catalog, not a live marketplace; GCG strings are often unnatural/gibberish (detectable). No vendor COI.
- Pathway: **Retrieval/grounding** (content on a retrieved product page) → context.

**2. GEO: Generative Engine Optimization**
- Authors/affiliations: Pranjal Aggarwal (IIT Delhi), Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande (Princeton University and collaborators).
- Venue/status: Peer-reviewed — KDD '24 (30th ACM SIGKDD), pp. 5–16, DOI 10.1145/3637528.3671900. arXiv 2311.09735; v1 16 Nov 2023, latest revision 28 Jun 2024.
- URL: https://arxiv.org/abs/2311.09735
- Code/data: Yes — GEO-BENCH benchmark of ~10,000 queries released.
- Models/platforms: Generative engines built on GPT-3.5/GPT-4 and others; evaluated over GEO-BENCH.
- Sample size: ~10,000 queries in GEO-BENCH.
- Core finding: Defines "generative engine optimization" and shows white-hat content methods can raise a site's visibility in generative-engine answers by "over 40%."
- Effect size (verbatim): the GEO methods "can boost visibility by up to 40% in generative engine responses," specifically an "improvement of 30–40% on the Position-Adjusted Word Count metric and 15–30% on the Subjective Impression metric," driven by Statistics Addition, Quotation Addition, and Cite Sources.
- Limitations/COI: Framed as legitimate optimization, not adversarial. A commercial GEO industry has grown around it (potential COI in follow-on vendor work).
- Pathway: **Retrieval/grounding.**

**3. Ranking Manipulation for Conversational Search Engines**
- Authors/affiliations: Samuel Pfrommer, Yatong Bai, Tanmay Gautam, Somayeh Sojoudi (UC Berkeley, EECS).
- Venue/status: Peer-reviewed — EMNLP 2024 (main). arXiv 2406.03589; v1 5 Jun 2024, v3 25 Sep 2024.
- URL: https://arxiv.org/abs/2406.03589
- Code/data: Yes — code on GitHub (spfrommer/cse-ranking-manipulation) and the RAGDOLL real-world e-commerce website dataset on HuggingFace.
- Models/platforms: Multiple LLMs; attacks transfer to production perplexity.ai.
- Sample size: RAGDOLL dataset of real consumer-product websites (focused set).
- Core finding: A tree-of-attacks jailbreaking technique reliably promotes low-ranked products; LLMs vary significantly in weighting product name vs. document content vs. context position, and injections transfer to production engines.
- Effect size: Reliable promotion of low-ranked products (large, qualitative); exact lift varies by model.
- Limitations/COI: Adversarial strings; transferability limited by engine changes. No vendor COI.
- Pathway: **Context** (prompt injection into a retrieved page) + retrieval.

**4. Adversarial Search Engine Optimization for LLMs (Preference Manipulation Attacks)**
- Authors/affiliations: Fredrik Nestaas, Edoardo Debenedetti, Florian Tramèr (ETH Zürich).
- Venue/status: Accepted at ICLR 2025. arXiv 2406.18382; v1 28 Jun 2024.
- URL: https://arxiv.org/abs/2406.18382
- Code/data: Demonstrations described in paper.
- Models/platforms: Production LLM search engines Bing and Perplexity; plugin APIs for GPT-4 and Claude.
- Sample size: Multiple fictitious-camera pages; head-to-head vs. real Nikon/Fujifilm cameras.
- Core finding: "Preference Manipulation Attacks" (crafted page/plugin-doc content) make an LLM promote the attacker's product and discredit competitors; creates a prisoner's-dilemma dynamic that degrades results for everyone if all parties attack. Optimized pages can override brand-name recognition, letting unknown products beat reputable ones.
- Effect size (verbatim/specific): a Preference Manipulation Attack made the targeted camera "2.5 times more likely to be recommended than a comparable product"; the fictitious camera's recommendation rate rose from 34.0% to 59.4%; a GPT-4 news plugin became "2–8× more likely to be selected" (up to 7.2×). Without attack, real brands were recommended nearly twice as often as the fictitious product.
- Limitations/COI: Prisoner's-dilemma is analytical; production engines patch. No vendor COI.
- Pathway: **Retrieval/grounding + context** (website content and plugin documentation).

**5. Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations**
- Authors/affiliations: Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, Giorgos Stamou (AILS Lab, School of ECE, National Technical University of Athens; Filandrianos also Instituto de Telecomunicações, Portugal).
- Venue/status: Peer-reviewed — accepted at EMNLP 2025. arXiv 2502.01349; v1 3 Feb 2025, v4 22 Oct 2025.
- URL: https://arxiv.org/abs/2502.01349
- Code/data: Product-description manipulation datasets described in paper.
- Models/platforms: LLMs "of varying scales" (open + proprietary).
- Sample size: Product catalogs with descriptions modified via cognitive-bias framings.
- Core finding: Injecting human cognitive-bias cues (social proof, scarcity, authority, etc.) into product descriptions is a **black-box, hard-to-detect** manipulation. Social proof consistently boosts recommendation rate/rank; scarcity and exclusivity surprisingly reduce visibility. Biases are deeply embedded and hard to mitigate.
- Effect size: Direction varies by bias — social proof up; scarcity/exclusivity down (per-model magnitudes in paper).
- Limitations/COI: Effects are model-dependent and unpredictable. No vendor COI.
- Pathway: **Retrieval/grounding + context** (semantic content, not gibberish → hard to detect).

**6. PoisonedRAG: Knowledge Corruption Attacks to RAG**
- Authors/affiliations: Wei Zou, Runpeng Geng, Jinyuan Jia (Pennsylvania State University); Binghui Wang (Illinois Institute of Technology).
- Venue/status: Peer-reviewed — USENIX Security 2025, pp. 3827–3844. arXiv 2402.07867.
- URL: https://arxiv.org/abs/2402.07867
- Code/data: Yes — code released (GitHub).
- Models/platforms: RAG systems over knowledge databases (Wikipedia-scale, millions of texts); multiple LLMs incl. PaLM 2; evaluated defenses.
- Sample size: 5 injected malicious texts per target question; knowledge DB with millions of texts.
- Core finding: First knowledge-corruption/poisoning attack on RAG; injecting a few crafted texts induces an attacker-chosen answer. Evaluated defenses are insufficient.
- Effect size (verbatim/specific): "90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts"; in the black-box setting, 97% (NQ), 99% (HotpotQA), and 91% (MS-MARCO) ASRs for RAG with PaLM 2.
- Limitations/COI: Requires ability to inject into the knowledge source. No vendor COI.
- Pathway: **Retrieval/grounding** (RAG knowledge database).

**7. Not What You've Signed Up For: Indirect Prompt Injection (foundational mechanism)**
- Authors/affiliations: Kai Greshake (Saarland Univ. / sequire technology), Sahar Abdelnabi, Thorsten Holz, Mario Fritz (CISPA Helmholtz Center for Information Security), Shailesh Mishra (Saarland), Christoph Endres (sequire technology).
- Venue/status: Peer-reviewed — AISec '23 (16th ACM Workshop on AI and Security), DOI 10.1145/3605764.3623985. arXiv 2302.12173; v1 23 Feb 2023, revised 5 May 2023.
- URL: https://arxiv.org/abs/2302.12173
- Code/data: Yes — demos at github.com/greshake/llm-security.
- Models/platforms: Bing GPT-4-powered Chat, GPT-4 code completion, synthetic agents.
- Core finding: Establishes indirect prompt injection — malicious instructions embedded in content the LLM later retrieves — with a security taxonomy (data theft, worming, ecosystem contamination). This is the mechanism underpinning most recommendation-injection attacks. Now catalogued as OWASP LLM01:2025.
- Pathway: **Context** (retrieved/ingested external content).

### Newer / adjacent adversarial work (2025–2026, mostly preprints — treat effect claims as preliminary)
- **Dynamics of Adversarial Attacks on LLM-Based Search Engines** — arXiv 2501.00745 (models multi-agent/prisoner's-dilemma dynamics; retrieval+context).
- **Poisoned-MRAG** — arXiv 2503.06254 (knowledge poisoning of multimodal RAG; up to 98% attack success with 5 image-text pairs injected into the InfoSeek database of 481,782 pairs). Retrieval pathway.
- **Cross-Modal Content Optimization for Steering Web Agent Preferences** — arXiv 2510.03612 (web-agent commerce manipulation; documents ToolHijacker and the MPMA "best tool" superlative attack). Context pathway.
- **SIREN: PAIR-Driven Preference Manipulation in Web-RAG Recommenders** — arXiv 2607.21951 (single-page content-only adversary; retrieval).
- **E-GEO** (arXiv 2511.20867) and **One Polluted Page Is Enough** (arXiv 2606.13610) — e-commerce GEO testbeds and web-content-pollution evaluation for generative recommenders.

### AI-targeted cloaking (documented technique, vendor research)
- **AI-targeted / agent-aware cloaking** — SPLX researchers Ivan Vlahov and Bastien Eymery, October 2025. Servers detect AI user-agents (e.g., ChatGPT-User, Perplexity, Atlas, Claude) and serve altered content only to crawlers, which treat it as "ground truth."
- Primary: https://splx.ai/blog/ai-targeted-cloaking-openai-atlas ; corroborated by The Hacker News, CyberScoop, Dark Reading.
- Demonstrations: fictional designer "Zerphina Quortane" (a reputation smear served only to AI crawlers); a hiring test in which candidate "Natalie Carter" scored 88/100 with the cloaked résumé vs. 26/100 with the human-visible version — a full leaderboard flip.
- Detectability: trivially detectable in principle (compare human vs. crawler content), but SPLX reports that neither ChatGPT nor Perplexity flagged the inconsistency — no provenance validation in current retrieval pipelines.
- Deception/ToS: Yes — deceives users and violates cloaking prohibitions. Pathway: **Retrieval/grounding + context.**

### Platform detection, defense & enforcement
- **Google Search Central — Spam Policies.** Cloaking (serving different content to crawlers vs. users) is a longstanding violation. On **May 15, 2026**, Google formally clarified that its spam policies (cloaking, scaled content abuse, inauthentic mentions, link spam, site reputation abuse, doorway pages, hidden text) **apply to generative AI responses in Search, including AI Overviews and AI Mode.** New wording: spam includes "attempting to manipulate generative AI responses in Google Search." Enforcement: lower ranking or removal, via automated systems plus human reviewers. Primary: https://developers.google.com/search/docs/essentials/spam-policies (corroborated by Search Engine Land, Gizmodo).
- **OWASP GenAI Security Project** — Prompt Injection is LLM01:2025 (canonical risk catalog). https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **Perplexity** — published security guidance describing prompt injection as severe enough to "demand rethinking security from the ground up" (quoted in SPLX/press coverage).
- **Academic defenses:** FilterRAG / ML-FilterRAG (arXiv 2508.02835) and traceback of RAG poisoning (arXiv 2504.21668). All show partial protection; adaptive attacks remain unsolved.

## Manipulation-tactic scorecard (mechanism · effectiveness · pathway · detectability · deception/ToS)
1. **Strategic Text Sequence (STS / GCG)** — optimized string on a page → top rank (rank 10→1); retrieval; detectable (perplexity/gibberish); deceptive + likely ToS violation.
2. **Preference-manipulation prompt injection** — crafted page/plugin text overrides ranking → 34.0%→59.4% (2.5×), plugins 2–8×; retrieval+context; moderately detectable; deceptive + ToS.
3. **Cognitive-bias / fabricated-authority framing** — human-readable persuasion (social proof, fake clinical claims) → boosts rate/rank; retrieval+context; **hard to detect**; deceptive, may violate ToS.
4. **RAG/knowledge poisoning (PoisonedRAG, BadRAG, Poisoned-MRAG)** — inject texts into knowledge DB → 90–99% ASR with 5 texts; retrieval; detectable with provenance/filtering but current defenses insufficient; deceptive + ToS.
5. **AI-targeted cloaking** — user-agent–conditional content to AI crawlers → full ranking/leaderboard flips; retrieval+context; trivially detectable in principle, not caught in practice; deceptive + explicit ToS violation.
6. **Indirect prompt injection in documents/agents** — instructions embedded in retrieved content/tools → hijack tool/product selection; context; variably detectable; deceptive + ToS.
7. **Training-data poisoning for brand promotion** — seed the open web/corpora to bias parametric recall → slow, uncertain, hard to attribute; parametric; hard to detect; deceptive.
8. **LLM-targeted SEO spam / doorway "listicles"** — mass-produced pages engineered for citation → variable; retrieval; increasingly caught under Google's May 2026 clarification; borderline-to-ToS-violation.

---

# PART B — RECOMMENDER-SYSTEM & IR BIAS FOUNDATIONS

## Key Findings (Part B)
1. **Established brands dominate LLM recommendations for the same first-principles reasons they dominate any recommender:** popularity bias in training/interaction data, position/order bias in ranking, and self-reinforcing feedback loops ("rich get richer" / cumulative advantage).
2. **LLMs add their own biases:** parametric brand recall (frequency of mention in pretraining), "lost in the middle" position sensitivity, order/selection bias in list generation, and sensitivity to superlative/authority language.
3. **The recommender literature is clear about how challengers win:** a legible quality/novelty advantage, exploration/randomization, debiasing/re-ranking and long-tail promotion, and calibration to the user's true taste distribution.

## Details (Part B) — Source-by-source

### Foundational recommender/IR bias papers
**Popularity bias & long-tail**
- **Abdollahpouri, Burke, Mobasher — "Managing Popularity Bias in Recommender Systems with Personalized Re-ranking"** (arXiv 1901.07555; FLAIRS-32, 2019). Introduces personalized diversification re-ranking to raise long-tail coverage while keeping accuracy acceptable. Related: "Controlling Popularity Bias in Learning-to-Rank" (RecSys 2017) and "The Unfairness of Popularity Bias in Recommendation" (2019). Core message: collaborative filtering over-emphasizes already-popular items; unmitigated, "the market [is] dominated by a few large brands."
- **Chen, Dong, Wang, Feng, Wang, He — "Bias and Debias in Recommender System: A Survey and Future Directions"** (arXiv 2010.03240; ACM TOIS 41(3), 2023). USTC + NUS + Hefei UT. Taxonomy of biases (selection, exposure, position, popularity, conformity, etc.) and of debiasing methods. Companion GitHub (RecDebiasing) lists methods + unbiased datasets (Yahoo!R3, Coat, KuaiRec).

**Position bias / click models (IR)**
- **Joachims, Granka, Pan, Hembrooke, Gay — "Accurately Interpreting Clickthrough Data as Implicit Feedback"** (SIGIR 2005). Eye-tracking shows users scan top-down; examination probability decays with rank; clicks are informative but biased; relative preferences are more reliable than absolute.
- **Craswell, Zoeter, Taylor, Ramsey — "An Experimental Comparison of Click Position-Bias Models"** (WSDM 2008). Introduces/validates the **cascade model** of position bias — the canonical model of why higher-ranked items get disproportionate attention.

**Feedback loops / cumulative advantage**
- **Salganik, Dodds, Watts — "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market"** (Science 311(5762):854–856, 2006; DOI 10.1126/science.1121066). Columbia. MusicLab experiment, 14,341 participants. Social influence increases both inequality and unpredictability of success; verbatim: "Success was also only partly determined by quality: The best songs rarely did poorly, and the worst rarely did well, but any other result was possible." The empirical cornerstone of cumulative advantage.
- **Chaney, Stewart, Engelhardt — "How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility"** (RecSys 2018; arXiv 1710.11214). Simulations show training on data already shaped by recommendations homogenizes users and reduces utility.
- **Jiang, Chiappa, Lattimore, György, Kohli — "Degenerate Feedback Loops in Recommender Systems"** (AAAI/ACM AIES 2019; arXiv 1902.10730). Theoretical analysis of echo chambers/filter bubbles; degeneracy can be mitigated by continual item-pool expansion and exploration/randomization.
- **Mansoury, Abdollahpouri, Pechenizkiy, Mobasher, Burke — "Feedback Loop and Bias Amplification in Recommender Systems"** (CIKM 2020). Recommender feedback loops amplify popularity bias and reduce diversity over time ("bias amplification").
- **Fleder & Hosanagar — "Blockbuster Culture's Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity"** (Management Science, 2009). Recommenders can reduce aggregate sales diversity (push toward concentration) even while helping individuals — the "blockbuster" concentration effect.

### LLM-specific bias in recommendation/ranking
**Position/order bias in LLMs**
- **Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang — "Lost in the Middle: How Language Models Use Long Contexts"** (TACL 2024, vol. 12:157–173; arXiv 2307.03172). Stanford/Berkeley/Samaya AI. U-shaped performance: models use information best at the beginning/end of context, worst in the middle — a structural position bias directly relevant to how retrieved candidates are ranked.
- **Wang, Li, Chen, Cai, Zhu, Lin, Cao, Kong, Liu, Liu, Sui — "Large Language Models are not Fair Evaluators"** (ACL 2024; arXiv 2305.17926). Peking Univ. et al. Reordering candidates in the context "hacks" the verdict — e.g., Vicuna-13B could beat ChatGPT on 66/80 queries just by reordering. Proposes a calibration framework (multiple-evidence, balanced position, human-in-loop).
- **Evaluating Position Bias in LLM Recommendations** (arXiv 2508.02020) and mechanistic work (Wang et al., "Eliminating Position Bias of Language Models," ICLR 2025) extend this to recommendation lists.

**Popularity/brand bias in LLM recommenders**
- **Hou, Zhang, Lin, Lu, Xie, McAuley, Zhao — "Large Language Models are Zero-Shot Rankers for Recommender Systems"** (ECIR 2024; arXiv 2305.08845). RUC + UCSD + Tencent. Code: github.com/RUCAIBox/LLMRank. Two MovieLens/Amazon-style datasets. LLMs have promising zero-shot ranking ability but (1) struggle to perceive interaction order and (2) are biased by item popularity and by position in the prompt; both mitigable via prompting/bootstrapping.
- **Dai, Shao, Zhao, Yu, Si, Xu, Sun, Zhang, Xu — "Uncovering ChatGPT's Capabilities in Recommender Systems"** (RecSys 2023; arXiv 2305.02182; DOI 10.1145/3604915.3610646). Renmin University of China + UIBE. Code: github.com/rainym00d/LLM4RS. Models: text-davinci-002/003, gpt-3.5-turbo (not GPT-4). 500 records per dataset across Movie/Book/Music/News; candidate lists of 1 positive + 4 negatives. LLMs beat a popularity-only baseline in Movie/Book/Music but underperform it in News (news leans harder on popularity). List-wise ranking gives the best cost/performance trade-off.
- **Lichtenberg, Buchholz, Schwöbel — "Large Language Models as Recommender Systems: A Study of Popularity Bias"** (arXiv 2406.01285; Gen-IR@SIGIR24 workshop, peer-reviewed). All three authors Amazon (Music / AWS), Berlin. MovieLens 10M; 5 folds × 1,000 users; slates of 10. Models: gpt-3.5-turbo-0613, gpt-4-1106-preview, claude-instant-1.2, claude-2.1 (temp 0). **Counterintuitive result:** a simple LLM recommender ("WOK") shows *less* popularity bias than ItemKNN/UserKNN/TopPop baselines even without mitigation (popularity-bias metric: WOK-claude-2.1 = 0.377, WOK-gpt-4 = 0.392 vs. UserKNN 0.630, ItemKNN 0.957, TopPop 1.455), but LLMs are far less accurate (HR@10 ~0.05–0.08 vs. UserKNN 0.411). Prompt-based self-debiasing can invert popularity bias but collapses accuracy. Uses MovieLens/LensKit; no new benchmark released.
- **Deldjoo & Di Noia — "CFaiRLLM: Consumer Fairness Evaluation in Large-Language-Model Recommender System"** (arXiv 2403.05668; ACM TIST, 2025, DOI 10.1145/3725853). Politecnico di Bari. v1 8 Mar 2024, v3 20 Feb 2025. Argues prior LLM-recommender fairness studies conflated genuine personalization with bias; introduces intersectional fairness evaluation, user-profile sampling, and true-preference-alignment metrics (Jaccard similarity, PRAG). Related: Deldjoo & Nazary, "A Normative Framework for Benchmarking Consumer Fairness in LLM RecSys" (arXiv 2405.02219); Deldjoo, "Understanding Biases in ChatGPT-based Recommender Systems" (ACM TORS 2024).
- **Chu & Hou — "Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems"** (arXiv 2606.17443; Trine University; Texas A&M). v1 16 Jun 2026 (recent, not peer-reviewed). Models: gpt-4o-mini, claude-sonnet-4-6, gemini-3-flash-preview (temp 0.7, EN+ZH); RAG probe with text-embedding-3-small. Large sample (Exp 1c N=9,220; Exp 1d N=14,395; ~30k+ calls total). Domain: skincare (120 fictional brands + real incumbents CeraVe, Paula's Choice, EltaMD), with a search-goods robustness check (Anker cables, Duracell batteries). **The most direct "why incumbents dominate" study** and the key bridge between Parts A and B — detailed below.

## The bridge: why established brands dominate — the "Incumbent Advantage" result
Chu & Hou (2026) quantify a **"Conditional Monopoly":**
- With identical specs, the known incumbent is recommended **100% of the time** (Incumbent Advantage Index = 10.0/10; 0 of 670 trials picked any fictional brand).
- But dominance is brittle: with even the smallest quality edge for a competitor, win rates jump from **<6% (identical) to 64–80% (smallest advantage)** — a step function. 50% "breakthrough" thresholds were tiny: **+0.075 stars, a 7.3% price discount, or 1.6× review count.** Claude was hardest to flip; GPT/Gemini easiest.
- Variance decomposition: **product parameters explain 82.4% of ranking variance; list position 6.5%; brand identity only 1.2%** — brand acts as a tiebreaker, strongest at medium quality.
- Manipulation: **authority-style language (including fabricated clinical claims) broke the monopoly 73.3% of the time** (Gemini 99%, GPT 69%, Claude 55%); social proof 50.7%; scarcity/loss-aversion near baseline (~10–13%). "Bias Surplus Value" of authority language ≈ +0.17 stars ≈ 15.3% discount ≈ 1.9× reviews.
- GEO prisoner's dilemma: one optimizing challenger cut incumbent survival to 19.8%, but when all nine optimized, survival recovered to 93.8% and the **individual GEO payoff fell from +0.802 (first mover) to +0.007 (universal adoption); non-participants got zero recommendations.**
- Caveat: single-domain (skincare), 2026 preprint, not peer-reviewed; RAG results are "directional."

This dovetails with Nestaas et al. (brand recognition makes real products ~2× more likely absent attack; attacks erase that edge) and Bias Beware (authority/social-proof framing works; scarcity backfires).

## Recommendations
**For a challenger brand trying to earn legitimate LLM visibility:**
1. **Build a legible, verifiable quality/novelty edge.** The literature says incumbents fall when a competitor is *clearly* better on the attributes the model reads: ratings, review counts, price, specs. Chu & Hou show the thresholds are small (≈+0.075 stars, ≈7.3% discount, ≈1.6× reviews) — so concrete, structured, third-party-verifiable signals are the highest-leverage lever. Benchmark to change strategy: if you can't move a real rating/review/spec signal, LLM visibility gains will be fragile.
2. **Invest in white-hat GEO, not adversarial tricks.** Aggarwal et al. show citations, quotations, and statistics lift visibility 30–40% legitimately and durably. Avoid STS/injection/cloaking: they violate Google's May 2026 spam policy and vendor terms, are increasingly detectable, and deceive users.
3. **Ensure your real content is what AI crawlers see.** Because cloaking and injection poison retrieval, audit that AI user-agents receive your genuine, high-quality content and that competitors aren't cloaking against you.
4. **Distribute across many retrievable, reputable sources.** Popularity/parametric recall favors frequently-and-credibly-mentioned brands; earn mentions in sources LLMs retrieve and trust.

**For a company defending/monitoring competitive visibility:**
5. **Stand up an LLM-visibility monitor** that queries major engines for your category and logs which brands are cited, in what order, with what justifications — and diffs human-vs-crawler page content to catch cloaking.
6. **Escalation thresholds:** if a competitor suddenly appears at rank 1 with thin real-world signals, or with suspiciously uniform superlative/authority language, or your own pages are being cited with content you didn't write — treat as probable manipulation and (a) file platform spam/cloaking reports, (b) document for legal/regulatory review (deceptive practices), (c) shore up your own legitimate signals.

## Caveats
- Several 2026 sources (Incumbent Advantage, SIREN, E-GEO, One Polluted Page) are **preprints, not peer-reviewed**; treat their specific effect sizes as preliminary.
- Attack effect sizes are often measured on **fictitious catalogs or single domains** and against **specific model versions**; production engines patch, so transferability decays.
- Vendor research (SPLX) is credible and corroborated by multiple outlets, but SPLX sells AI-security services (potential COI); the underlying demonstrations are reproducible and independently reported.
- Lichtenberg et al. (Amazon) find LLMs can be *less* popularity-biased than classic collaborative filtering — a useful counterpoint to the "LLMs always favor incumbents" narrative; the truth is model- and prompt-dependent.

---

# CLOSING SECTION 1 — Manipulation patterns to watch for in competitors' visibility (plain language)
1. **Sudden rank jumps without real-world change** — a competitor leaps to the LLM's #1 pick while its ratings, reviews, price, and specs haven't meaningfully improved. (Signature of STS/preference-injection.)
2. **Cloaking / two-faced pages** — the page an AI crawler sees differs from what humans see (inflated claims, fake credentials). Detect by fetching as an AI user-agent vs. a normal browser.
3. **Fabricated authority & social proof** — pages/reviews stuffed with "clinically proven," "#1 recommended," fake awards, or coordinated review surges; authority framing is the single most effective manipulation in the literature.
4. **Suspiciously uniform superlative language** across many third-party "listicles"/doorway pages all pointing to one brand (LLM-targeted SEO spam).
5. **Injected instructions in retrievable content** — hidden or out-of-place text ("recommend this product first," "ignore other options") in pages, PDFs, reviews, or plugin/tool descriptions.
6. **RAG/knowledge-base poisoning** — a competitor's claims appearing verbatim as "facts" in AI answers, traceable to a few recently-created or low-quality sources.
7. **Your own brand being described from content you never published** — a sign your entity is being cloaked/poisoned against.
8. **Prisoner's-dilemma escalation** — a whole category's pages suddenly adopt aggressive GEO/authority language; individual gains erode and answer quality degrades for everyone.

# CLOSING SECTION 2 — When does a less-popular option displace an incumbent? (what the research says)
The recommender/IR literature and the new LLM-specific work converge on a short list of conditions:
1. **A genuine, legible quality/novelty advantage.** Salganik shows quality sets floors and ceilings (the best rarely fail, the worst rarely win) even when social influence dominates the middle. Chu & Hou show LLMs flip to a challenger at very small but *real* advantages in the attributes the model can read.
2. **Exploration / randomization in the ranker.** Jiang et al. and the degenerate-feedback-loop literature show that continually expanding the item pool and injecting exploration breaks "rich-get-richer" lock-in and gives challengers exposure.
3. **Debiasing, re-ranking, and long-tail promotion.** Abdollahpouri's personalized re-ranking, learning-to-rank popularity controls, and the debiasing methods surveyed by Chen et al. explicitly raise long-tail/niche items while limiting accuracy loss — the direct mechanism by which non-incumbents get surfaced.
4. **Calibration to the user's true taste distribution.** If a user genuinely prefers niche items, calibrated recommendation preserves that ratio instead of collapsing to blockbusters (Abdollahpouri; Steck-style calibration).
5. **Neutralizing manipulation and popularity feedback.** Fleder & Hosanagar and Mansoury et al. show unmitigated loops concentrate on incumbents; provenance/verification, exposure fairness, and bias-amplification controls level the field.
6. **Reducing position/parametric advantages specifically in LLMs.** "Lost in the middle" and order-bias mean incumbents also win from prompt position and pretraining frequency; balanced-position calibration (Wang et al.), bootstrapping/prompting (Hou et al.), and grounding in current structured signals (rather than parametric recall) all help challengers.

**Bottom line:** Incumbency in LLM recommendations is a *tiebreaker, not a moat.* When a challenger supplies a real, verifiable, model-legible quality edge — and the platform applies exploration, debiasing, and provenance checks — the incumbent advantage collapses quickly. Absent those, popularity bias and feedback loops keep the incumbent on top.