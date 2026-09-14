# LLM Memorization, Long-Tail Knowledge, and the Mechanics of Parametric Recall

## TL;DR
- Whether a model volunteers a given entity from parametric memory for an open-ended question is governed primarily by how often that entity — and its association with the relevant category — appeared in pretraining text: recall scales roughly log-linearly with frequency/duplication, collapses toward zero in the long tail, and is not rescued by simply making models larger.
- The mechanism is now fairly well understood: facts are stored as key-value associations in mid-layer feed-forward blocks, become *extractable* only when the same fact was seen in diverse/augmented forms during pretraining, and are hard to change after the fact — editing, fine-tuning, and continual training are brittle and can induce hallucination.
- Post-training (RLHF/instruction tuning) doesn't add knowledge but reshapes what gets *volunteered*, substantially reducing output diversity ("mode collapse") and amplifying popularity bias; retrieval/context can override parametric priors, but models often stubbornly favor their prior for high-confidence (popular) facts.

## Key Findings
1. **Frequency is the master variable.** Kandpal et al. (ICML 2023) show QA accuracy is strongly log-linearly correlated with the number of pretraining documents linking the question and answer entities; the long tail is essentially unlearned. Their BLOOM scaling trend on rare Natural Questions facts (<100 relevant documents) is log-linear with R²=0.98, and extrapolating implies one would need a BLOOM model with over 10^18 (one quintillion) parameters to match a strong supervised baseline or human performance on those tail questions.
2. **Duplication drives memorization log-linearly.** Carlini et al. (ICLR 2023) quantify that verbatim emission grows log-linearly with model size, duplication count, and prompt context length; Lee et al. (ACL 2022) find that over 1% of unprompted output is copied verbatim, and deduplication lets models "emit memorized text ten times less frequently" (dropping to roughly 0.1%).
3. **Popularity predicts factual recall.** Mallen et al. (ACL 2023, PopQA, 14k questions) and Sun et al. (Head-to-Tail, NAACL 2024, 18k QA pairs) show accuracy declines monotonically head→torso→tail, and scaling barely helps the tail; the best overall accuracy across the 16 LLMs Sun et al. evaluated is only ~31% on Head-to-Tail.
4. **Co-occurrence, not truth, is what's learned.** Kang & Choi (EMNLP Findings 2023) demonstrate a "co-occurrence bias": models prefer frequently co-occurring words over correct answers, and this bias survives scaling and fine-tuning.
5. **Storage vs. extraction.** Allen-Zhu & Li ("Physics of LM 3.1", ICML 2024) show knowledge is only extractable if it was *augmented* (paraphrased/varied) during pretraining; unaugmented facts can be memorized yet yield 0% QA accuracy.
6. **Mechanistic locus.** Geva et al. (EMNLP 2021) identify feed-forward layers as key-value memories; Meng et al. (ROME, NeurIPS 2022) localize factual associations to mid-layer MLPs and edit them.
7. **Editing/updating is brittle.** ROME/MEMIT and fine-tuning have ripple effects and can degrade general ability; Gekhman et al. (EMNLP 2024) show fine-tuning on new knowledge is learned slowly and *increases* hallucination.
8. **Corpus composition is skewed and quality-upweighted.** Wikipedia is upsampled far beyond its raw size (GPT-3 up to 3.4 epochs; LLaMA ~2.45 epochs), while Common Crawl is seen <once; this systematically privileges encyclopedic entities.
9. **Parametric-vs-retrieval conflicts.** Longpre et al. (EMNLP 2021), Xie et al. (ICLR 2024), and Wu et al. (ClashEval, NeurIPS 2024) show models can be both over-reliant on priors and over-swayed by context; ClashEval finds "LLMs are susceptible to adopting incorrect retrieved content, overriding their own correct prior knowledge over 60% of the time."
10. **Post-training reshapes what is volunteered.** Kirk et al. (ICLR 2024) find "RLHF does reduce output diversity substantially in the per-input setting, and still reduces it to a lesser extent in the cross-input setting" — improving OOD generalization while mode-collapsing outputs.

## Details (Sources)

### A. Foundational memorization & long-tail knowledge

**Large Language Models Struggle to Learn Long-Tail Knowledge**
- Authors: Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, Colin Raffel (UNC Chapel Hill; Google; UC Berkeley).
- Venue: ICML 2023 (PMLR v202, pp. 15696–15707). First arXiv v1 Nov 15 2022; v2 Jul 27 2023. URL: https://arxiv.org/abs/2211.08411
- Code/data: entity-linking pipeline released (associated GitHub).
- Models/platforms: GPT-Neo family, BLOOM up to 176B; GPT-3 via API; corpora Pile, ROOTS, C4, OpenWebText, Wikipedia; datasets TriviaQA, Natural Questions.
- Sample size: millions of pretraining documents entity-linked; thousands of QA pairs.
- Core finding: A model's ability to answer a fact question is strongly correlated with the number of pretraining documents relevant to that QA pair; larger models help only modestly; retrieval augmentation reduces dependence on pretraining frequency.
- Effect size: log-linear correlation between accuracy and relevant-document count (BLOOM on rare NQ facts, R²=0.98); extrapolation implies a model with over 10^18 parameters would be needed to reach a strong supervised/human baseline on the tail.
- Limitations: relevance approximated by entity co-occurrence, not true supporting evidence.
- Pathway: parametric recall (primary); retrieval (as remedy).

**Quantifying Memorization Across Neural Language Models**
- Authors: Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr, Chiyuan Zhang (Google; Princeton; ETH Zürich).
- Venue: ICLR 2023. arXiv v1 Feb 15 2022. URL: https://arxiv.org/abs/2202.07646. Data: https://github.com/ethz-spylab/lm_memorization_data
- Models: GPT-Neo family; GPT-J-6B on the Pile.
- Core finding: Verbatim memorization grows log-linearly with (1) model capacity, (2) number of duplicates of an example, (3) prompt context length. GPT-J memorizes at least 1% of the Pile.
- Pathway: parametric recall.

**Deduplicating Training Data Makes Language Models Better**
- Authors: Katherine Lee, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris Callison-Burch, Nicholas Carlini (Google; UPenn).
- Venue: ACL 2022, pp. 8424–8445. arXiv v1 Jul 14 2021. URL: https://arxiv.org/abs/2107.06499
- Core finding: Datasets contain massive duplication (a 61-word sentence appears 60,000+ times in C4); over 1% of unprompted output is copied verbatim from training data, and deduplication makes models "emit memorized text ten times less frequently" (to ~0.1%) while reducing >4% train-test overlap without hurting perplexity.
- Pathway: parametric recall (training-data hygiene).

**Extracting Training Data from Large Language Models** (Carlini et al., USENIX Security 2021) established that GPT-2 emits memorized sequences; foundational precursor. URL: https://arxiv.org/abs/2012.07805

### B. Popularity & frequency in factual QA

**When Not to Trust Language Models (PopQA)**
- Authors: Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, Hannaneh Hajishirzi (Univ. Washington; Johns Hopkins; Allen AI).
- Venue: ACL 2023, pp. 9802–9822. arXiv Dec 20 2022. URL: https://arxiv.org/abs/2212.10511. Code/data: https://github.com/AlexTMallen/adaptive-retrieval (PopQA, 14k questions).
- Models: GPT-Neo (1.3B–20B), OPT, GPT-3; 4 retrieval methods (BM25, Contriever, GenRead, vanilla).
- Core finding: Recall tracks entity popularity (Wikipedia pageviews); scaling fails to improve tail memorization; retrieval helps most on unpopular entities. Proposes Adaptive Retrieval (retrieve only below a popularity threshold), which improves accuracy while cutting inference cost.
- Pathway: parametric recall vs. retrieval.

**Head-to-Tail: How Knowledgeable are LLMs?**
- Authors: Kai Sun, Yifan Ethan Xu, Hanwen Zha, Yue Liu, Xin Luna Dong (Meta Reality Labs).
- Venue: NAACL 2024. arXiv Aug 20 2023. URL: https://arxiv.org/abs/2308.10168. Benchmark: 18k QA pairs (head/torso/tail).
- Models: 16 LLMs evaluated (v1 reported 14).
- Core finding: Accuracy declines head→torso→tail; the best overall accuracy across the evaluated LLMs is only ~31% on Head-to-Tail, and conventional enhancements don't reliably improve tail knowledge.
- Pathway: parametric recall.

**Impact of Pretraining Term Frequencies on Few-Shot (Numerical) Reasoning**
- Authors: Yasaman Razeghi, Robert L. Logan IV, Matt Gardner, Sameer Singh (UC Irvine; AI2).
- Venue: EMNLP Findings 2022, pp. 840–854. arXiv Feb 15 2022. URL: https://arxiv.org/abs/2202.07206
- Models: GPT-J-6B and GPT-based models pretrained on the Pile.
- Core finding: Accuracy on arithmetic/unit-conversion instances correlates with the frequency of the operands' terms in pretraining — up to 70% absolute higher accuracy on the top-10% vs bottom-10% frequent terms. Raises the question of how much "reasoning" is really pretraining-frequency lookup.
- Citations: ~108 (Semantic Scholar, checked Aug 2026).
- Pathway: parametric recall.

### C. Co-occurrence & corpus-content effects

**Impact of Co-occurrence on Factual Knowledge of LLMs**
- Authors: Cheongwoong Kang, Jaesik Choi (KAIST).
- Venue: EMNLP Findings 2023, pp. 7721–7735. arXiv Oct 12 2023. URL: https://arxiv.org/abs/2310.08256. Code: https://github.com/CheongWoong/impact_of_cooccurrence
- Core finding: A "co-occurrence bias" — models prefer frequently co-occurring words over correct answers, and struggle to recall facts whose subject and object rarely co-occur. Bias persists across scale and fine-tuning; debiased fine-tuning helps only for facts seen during fine-tuning, not for unseen rare facts.
- Pathway: parametric recall.

**What's In My Big Data? (WIMBD)**
- Authors: Yanai Elazar, Akshita Bhagia, Ian Magnusson, Abhilasha Ravichander, Dustin Schwenk, Alane Suhr, Pete Walsh, Dirk Groeneveld, Luca Soldaini, Sameer Singh, Hannaneh Hajishirzi, Noah A. Smith, Jesse Dodge (Allen AI; UW; UC Irvine; UC Berkeley).
- Venue: ICLR 2024. arXiv Oct 31 2023. URL: https://arxiv.org/abs/2310.20707. Platform: https://github.com/allenai/wimbd
- Sample: 10 corpora (C4, The Pile, RedPajama, etc.), >35 TB analyzed; 16 analyses.
- Core finding: Reveals high prevalence of duplicate/synthetic/low-quality content, PII, and benchmark contamination; provides count/search over corpora to ground model behavior in data statistics.
- Pathway: parametric recall (data-side).

### D. Mechanistic storage & recall

**Transformer Feed-Forward Layers Are Key-Value Memories**
- Authors: Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy (Tel-Aviv Univ.; Allen AI; Cornell Tech).
- Venue: EMNLP 2021, pp. 5484–5495. arXiv Dec 29 2020. URL: https://arxiv.org/abs/2012.14913. Code: https://github.com/mega002/ff-layers
- Core finding: FFN layers (two-thirds of parameters) act as key-value memories; keys match training textual patterns, values induce output-vocabulary distributions; lower layers capture shallow, upper layers semantic patterns.
- Pathway: parametric recall (mechanism).

**Locating and Editing Factual Associations in GPT (ROME)**
- Authors: Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov (MIT CSAIL; Northeastern; Technion).
- Venue: NeurIPS 2022. arXiv Feb 10 2022. URL: https://arxiv.org/abs/2202.05262. Project: https://rome.baulab.info/. Code: https://github.com/kmeng01/rome
- Models: GPT-2 XL (1.5B), GPT-J (6B).
- Core finding: Causal tracing shows mid-layer FFN modules at the last subject token mediate factual recall; Rank-One Model Editing edits a single weight matrix to change a fact and generalize it. Introduced CounterFact dataset.
- Pathway: parametric recall (mechanism + editing).

**Physics of Language Models: Part 3.1, Knowledge Storage and Extraction**
- Authors: Zeyuan Allen-Zhu (Meta/FAIR), Yuanzhi Li (MBZUAI).
- Venue: ICML 2024 (pp. 1067–1077). arXiv Sep 25 2023. URL: https://arxiv.org/abs/2309.14316
- Core finding: In a controlled biography setting, reliable knowledge *extraction* requires *augmentation* (paraphrase, shuffling, translation) during pretraining; without it, knowledge is memorized but yields ~0% QA accuracy regardless of later instruction tuning. Recommends rewriting pretraining data and mixing in instruction data early.
- Pathway: parametric recall (mechanism).

### E. Temporal knowledge, recency & cutoffs

**Dated Data: Tracing Knowledge Cutoffs in LLMs**
- Authors: Jeffrey Cheng, Marc Marone, Orion Weller, Dawn Lawrie, Daniel Khashabi, Benjamin Van Durme (Johns Hopkins).
- Venue: COLM 2024 (also OpenReview). arXiv Mar 19 2024. URL: https://arxiv.org/abs/2403.12958. Code: https://github.com/nexync/dated_data
- Core finding: The "effective cutoff" (when a model's knowledge is actually concentrated) often differs sharply from the reported cutoff, due to duplicated/near-duplicate old CommonCrawl content and stale Wikipedia dumps.
- Pathway: parametric recall (temporal).

Also relevant (secondary to this report's core, cited here for completeness): Dhingra et al. TempLAMA; Jang et al. TemporalWiki; Kasai et al. RealTime QA; Vu et al. FreshLLMs/FreshQA — all establish that parametric knowledge is static/staleness-prone and that search augmentation is needed for post-cutoff facts. (Primary sources not re-verified in this pass; note as such.)

### F. Corpus composition & data mixtures

**GPT-3 — "Language Models are Few-Shot Learners"** (Brown et al., NeurIPS 2020; arXiv:2005.14165). Data mixture (Table 2.2): Common Crawl 410B tokens, 60% weight, 0.44 epochs; WebText2 19B, 22%, 2.9 epochs; Books1 12B, 8%, 1.9 epochs; Books2 55B, 8%, 0.43 epochs; **Wikipedia 3B, 3%, 3.4 epochs**. Verbatim: higher-quality datasets are deliberately oversampled so that "some datasets are seen up to 3.4 times during training while other datasets are seen less than once" (Wikipedia is the 3.4× dataset; CommonCrawl and Books2 seen <once).

**The Pile** (Gao et al., EleutherAI; arXiv:2101.00027). 825 GiB, 22 subsets; upweights higher-quality academic/professional sources (PubMed, ArXiv, StackExchange, GitHub, Wikipedia, Books3). Abstract: "increased training dataset diversity improves general cross-domain knowledge and downstream generalization capability."

**LLaMA 1** (Touvron et al., Meta; arXiv:2302.13971). ~1.4T tokens. Table 1 sampling proportions / epochs: CommonCrawl 67%/1.10; C4 15%/1.06; GitHub 4.5%/0.64; **Wikipedia 4.5%/2.45**; **Books 4.5%/2.23**; ArXiv 2.5%/1.06; StackExchange 2.0%/1.03. Verbatim: "each token is used only once during training, with the exception of the Wikipedia and Books domains, over which we perform approximately two epochs."

**Llama 3** (Grattafiori et al., Meta; arXiv:2407.21783). ~15T (15.6T) tokens. Verbatim data mix: "roughly 50% of tokens corresponding to general knowledge, 25% of mathematical and reasoning tokens, 17% code tokens, and 8% multilingual tokens." A knowledge classifier downsamples over-represented categories (e.g., arts/entertainment); late-training annealing upsamples high-quality math/code data.

**DoReMi** (Xie et al., NeurIPS 2023; arXiv:2305.10429). Domain Reweighting with Minimax Optimization: trains a 280M proxy with Group DRO to set domain weights for an 8B model (30× larger); on the Pile it "improves perplexity across all domains, even when it downweights a domain," improves average few-shot accuracy by 6.5 points, and reaches baseline accuracy with 2.6× fewer training steps.

**Dolma** (Soldaini et al., ACL 2024; arXiv:2402.00159). ~3T-token open corpus: "web content, scientific papers, code, public-domain books, social media, and encyclopedic materials." Used to train OLMo. Code/data released.

**FineWeb** (Penedo et al., NeurIPS 2024 Datasets & Benchmarks, Spotlight; arXiv:2406.17557). 15T tokens from 96 Common Crawl snapshots; outperforms other open datasets (RefinedWeb, C4, RedPajama, Dolma) on matched ablations; FineWeb-Edu (1.3T educational tokens) "dramatically better performance on knowledge- and reasoning-intensive benchmarks like MMLU and ARC."

**Studying Large Language Model Generalization with Influence Functions**
- Authors: Roger Grosse, Juhan Bae, Cem Anil, and 14 others (Anthropic; Univ. Toronto).
- Venue: arXiv preprint Aug 7 2023. URL: https://arxiv.org/abs/2308.03296. Official: https://www.anthropic.com/news/studying-large-language-model-generalization-with-influence-functions
- Models: transformer LMs at ~810M, 6.4B, 22B, 52B.
- Core finding: Uses EK-FAC to scale influence functions to 52B; generalization patterns become more abstract with scale; influences are sparse and decay to near-zero when key-phrase order is flipped (a limitation tied to the "reversal curse").
- Pathway: parametric recall (attribution).

### G. Knowledge editing & the difficulty of changing associations

- **ROME/MEMIT** (Meng et al.) enable targeted edits but at scale accumulate errors. Editing surveys and critique papers ("Editing LLMs: Problems, Methods, Opportunities"; "Unveiling the Pitfalls of Knowledge Editing"; Cohen et al. ripple-effects; "Model Editing Can Hurt General Abilities") document that edits fail to propagate to logically entailed facts and can degrade unrelated capabilities. (Referenced via the knowledge-conflict/editing literature; primary abstracts not all re-verified this pass — flagged.)
- **Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?**
  - Authors: Zorik Gekhman, Gal Yona, Roee Aharoni, Matan Eyal, Amir Feder, Roi Reichart, Jonathan Herzig (Google; Technion).
  - Venue: EMNLP 2024, pp. 7765–7784. arXiv May 9 2024. URL: https://arxiv.org/abs/2405.05904
  - Core finding: In controlled closed-book QA, examples introducing new knowledge are learned much more slowly than knowledge-consistent examples; as the model finally fits them, they *linearly* increase its tendency to hallucinate — supporting the view that facts are mostly acquired in pretraining and fine-tuning teaches use, not new facts.
  - Pathway: parametric recall (updating difficulty).

### H. Parametric vs. retrieval/context conflicts

**Entity-Based Knowledge Conflicts in Question Answering**
- Authors: Shayne Longpre, Kartik Perisetla, Anthony Chen, Nikhil Ramesh, Chris DuBois, Sameer Singh (Apple; UC Irvine).
- Venue: EMNLP 2021, pp. 7052–7063. arXiv Sep 10 2021. URL: https://arxiv.org/abs/2109.05052. Framework released.
- Core finding: When context is edited to contradict memorized facts (entity substitution), models often ignore context and cling to memorized answers (a hallucination source); a mitigation improves OOD generalization by 4–7%.
- Pathway: parametric recall vs. retrieval/context.

**Adaptive Chameleon or Stubborn Sloth (Xie et al.)** — ICLR 2024, arXiv:2305.13300. Finds models are highly receptive to coherent external evidence but display strong confirmation bias toward parametric priors when evidence conflicts. Pathway: parametric vs. retrieval.

**ClashEval: Quantifying the Tug-of-War Between an LLM's Internal Prior and External Evidence**
- Authors: Kevin Wu, Eric Wu, James Zou (Stanford).
- Venue: NeurIPS 2024. arXiv:2404.10198.
- Sample: over 1,200 questions across six domains.
- Models: 6 top LLMs incl. GPT-4o and Claude Opus.
- Core finding: "LLMs are susceptible to adopting incorrect retrieved content, overriding their own correct prior knowledge over 60% of the time"; the more implausible the retrieved content, the more the model falls back on its prior. Claude Opus adheres to incorrect contextual information ~30% less than GPT-4o.
- Pathway: retrieval vs. parametric.

**Knowledge Conflicts for LLMs: A Survey** (Xu et al., EMNLP 2024, arXiv:2403.08319) — taxonomizes context-memory, inter-context, and intra-memory conflicts. (Cited; abstract not re-verified this pass.)

### I. Post-training (RLHF/instruction tuning) effects on what is volunteered

**Understanding the Effects of RLHF on LLM Generalisation and Diversity**
- Authors: Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu (UCL; Meta; Oxford).
- Venue: ICLR 2024. arXiv Oct 10 2023. URL: https://arxiv.org/abs/2310.06452
- Models: LLaMA-7B, OPT; TL;DR summarization and AlpacaFarm instruction-following; stages SFT, reward modeling/Best-of-N, PPO-RLHF.
- Core finding: RLHF generalizes better OOD than SFT but "does reduce output diversity substantially in the per-input setting, and still reduces it to a lesser extent in the cross-input setting" — a generalization↔diversity tradeoff (mode collapse).
- Pathway: parametric recall (which entities are volunteered/suppressed).

Related (cited, primary abstracts not all re-verified this pass): Zhou et al. "LIMA" superficial alignment hypothesis; Lin et al. "The Unlocking Spell on Base LLMs" (URIAL); Santurkar et al. "Whose Opinions Do Language Models Reflect"; Hou et al. "LLMs are Zero-Shot Rankers" (recommendation popularity bias); Deldjoo fairness-of-LLM-recommenders. These collectively indicate alignment mostly changes style/format and can amplify popularity bias while narrowing the range of volunteered entities.

### J. Reasoning / CoT and parametric recall

**To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning**
- Authors: Zayne Sprague, Fangcong Yin, Juan Diego Rodriguez, Dongwei Jiang, Manya Wadhwa, Prasann Singhal, Xinyu Zhao, Xi Ye, Kyle Mahowald, Greg Durrett (UT Austin; JHU; Princeton).
- Venue: ICLR 2025. arXiv Sep 18 2024. URL: https://arxiv.org/abs/2409.12183. Code: https://github.com/Zayne-sprague/To-CoT-or-not-to-CoT
- Sample: meta-analysis of 100+ papers; 20 datasets × 14 models.
- Core finding: CoT's benefits are concentrated in math/symbolic/logical tasks; on knowledge-heavy MMLU, CoT ≈ direct answering unless symbolic operations are involved. Implication: CoT does not meaningfully unlock additional *factual* recall of long-tail entities; recall is bounded by what was stored.
- Pathway: parametric recall (surfacing).

Related recall-surfacing work (cited): Sun et al. "Recitation-Augmented Language Models" (ICLR 2023) and Yu et al. "Generate rather than Retrieve" (ICLR 2023) show that prompting a model to first recite/generate relevant passages from parametric memory can improve closed-book QA — i.e., structured self-prompting can surface stored knowledge, but cannot create knowledge that was never stored. (Primary abstracts not re-verified this pass.)

## Recommendations (a plain-language brand-presence model)

For a model trained on web text to *volunteer a brand for a category without web search*, the following must hold. Each element is tagged **[Supported]**, **[Inferred]**, or **[Speculative]**.

1. **The brand must appear frequently in pretraining text, not just exist. [Supported]** Recall scales log-linearly with document frequency/duplication (Kandpal; Carlini; Mallen; Sun). A brand below the effective frequency threshold is effectively invisible to parametric recall.
2. **The brand must co-occur explicitly and repeatedly with the category term. [Supported]** It is the *subject–object co-occurrence* that is learned, not abstract "relevance" (Kang & Choi; Elazar). A brand mentioned often but rarely alongside its category will lose to more frequently co-occurring competitors — this is exactly the co-occurrence bias.
3. **The association must appear in many *varied* phrasings and contexts. [Supported]** Allen-Zhu & Li show unaugmented facts are memorized but not extractable; diversity of phrasing is what makes knowledge answerable. One canonical sentence repeated verbatim is far weaker than the same fact restated many ways.
4. **Presence should be concentrated in upweighted, high-quality sources. [Inferred]** Wikipedia and curated/academic/reference sources are oversampled relative to raw Common Crawl (GPT-3 Wikipedia 3.4 epochs vs CC 0.44; LLaMA Wikipedia 2.45 epochs; Llama 3's knowledge classifier downsamples "over-represented" web categories). A Wikipedia entity page and structured references likely carry disproportionate weight per mention. Exact per-source influence is model-specific and not fully disclosed. [Inferred/Speculative for any specific model]
5. **Popularity compounds. [Supported]** Head entities are recalled reliably; torso/tail entities are not, and scaling doesn't fix this (Mallen; Sun — best overall Head-to-Tail accuracy only ~31%). Popularity/pageview-like signals correlate with recall.
6. **The association must predate the effective knowledge cutoff. [Supported]** Effective cutoffs lag reported cutoffs and vary by topic (Cheng et al.); recent brand facts may be absent even for "current" models absent retrieval.
7. **Once wrong or missing, it is hard to fix by fine-tuning. [Supported]** Editing has ripple effects and can hurt general ability; fine-tuning new facts is slow and increases hallucination (Gekhman). Durable change comes from pretraining-scale presence, not post-hoc patches.
8. **Post-training narrows what gets volunteered toward the popular/typical. [Supported for diversity effect; Inferred for brand specifics]** RLHF reduces output diversity/mode-collapses (Kirk), and recommendation work indicates popularity bias — so aligned models likely volunteer a small set of the most frequent brands and suppress long-tail ones even when stored.
9. **Reasoning/CoT will not rescue a weakly-stored brand. [Supported/Inferred]** CoT mainly helps math/symbolic tasks, not factual recall (Sprague); recitation/generate-then-read can surface *stored* knowledge (Sun; Yu) but cannot manufacture unstored associations. [Inferred that this applies specifically to brand recall.]
10. **If parametric presence is weak, the reliable path is retrieval/context. [Supported]** Retrieval augmentation is what rescues the long tail (Kandpal; Mallen) — but retrieved content only wins conflicts sometimes (Longpre; Xie; Wu/ClashEval), so for a well-known competitor the model may still override retrieval with its prior.

**Staged actions for a brand:**
- **Stage 1 (baseline):** Establish high-frequency, high-quality, varied textual presence tying the brand to its category across many independent domains (reference pages, documentation, Q&A/forum discussion, reputable editorial). Benchmark: is the brand recalled zero-shot for its category by a current open model (e.g., Llama 3, OLMo) without search?
- **Stage 2 (if absent from parametric memory):** Prioritize retrieval-surface optimization (content that RAG/search systems will fetch) since that is the proven lever for tail entities. Benchmark: does the brand appear when the model has web access?
- **Stage 3 (monitor):** Track whether post-training/popularity effects suppress the brand relative to head competitors; re-test across model versions given shifting effective cutoffs.

**Thresholds that change the recommendation:** If frequency-based recall research is superseded by architectures that decouple recall from raw frequency, elements 1–2 weaken. If a model vendor discloses per-source weighting, element 4 moves from Inferred to Supported. If the brand becomes a "head" entity (reliably recalled zero-shot), shift budget from retrieval optimization back to defending parametric presence.

## Caveats
- **Frequency proxies, not ground truth.** Most "frequency" measures are entity co-occurrence counts or Wikipedia pageviews, not true supporting-evidence counts (Kandpal; Mallen). Correlations are strong but the mechanism is approximated.
- **Model/version specificity.** Data-mixture disclosures (GPT-3, LLaMA, Llama 3) are self-reported by vendors with commercial interests; closed frontier models (GPT-4-class, Claude, Gemini) do not disclose mixtures, so element 4 of the brand model is inferential for them.
- **"Brand recall" is an extrapolation.** Nearly all cited work studies encyclopedic facts (birthdays, capitals, biographies), not commercial brand-for-category recommendation. The brand model is a reasoned extension, explicitly tagged Inferred/Speculative where it goes beyond the evidence.
- **Some sources cited secondhand.** TempLAMA, TemporalWiki, RealTime QA, FreshQA/FreshLLMs, several knowledge-editing papers (MEMIT, MEND, ripple-effects, "Model Editing Can Hurt"), the Knowledge Conflicts survey, LIMA/URIAL/Santurkar/Hou/Deldjoo, and Recitation/GenRead were identified via citing literature rather than fully re-verified primary abstracts in this pass; treat their specific figures as pending primary confirmation.
- **Citation counts** are provided only where directly observed (e.g., Razeghi ~108 on Semantic Scholar, checked Aug 2026); most were not machine-read in this pass and are omitted rather than guessed.
- **Vendor conflicts of interest:** Head-to-Tail (Meta), influence-functions (Anthropic), Gekhman (Google), Kirk (Meta co-authors), and the data-mixture papers are produced by organizations that build and sell LLMs; findings are broadly corroborated across independent academic groups, which mitigates but does not eliminate bias.