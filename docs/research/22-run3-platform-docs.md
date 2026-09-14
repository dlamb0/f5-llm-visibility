# Platform-Official Documentation on Source Selection, Grounding, and Citation in Generative Search

## TL;DR
- Providers converge on one architecture — retrieval-augmented generation (RAG) over an existing web index, with citations returned as structured metadata — but they disclose mechanism (which crawler does what, how citations are surfaced) far more than strategy (how sources are actually ranked or selected). Google, OpenAI, Anthropic, Perplexity, and Microsoft all now publish separate crawler user-agents for training vs. live search vs. user-triggered fetch, and blocking one does not block the others.
- The single most important, officially-stated distinction practitioners miss: **training-data inclusion and search/grounding inclusion are governed by different user-agents.** Google-Extended, GPTBot, ClaudeBot, and Applebot-Extended control model *training*; Googlebot, OAI-SearchBot, Claude-SearchBot, PerplexityBot, and Bingbot control *search/grounding* eligibility. Google explicitly says llms.txt and schema markup are NOT required for its AI features.
- Enterprise products ground differently from consumer ones: Microsoft 365 Copilot, Gemini for Workspace, ChatGPT Enterprise, and Claude for Enterprise retrieve from tenant/organizational data (via semantic indexes, connectors, and Microsoft Graph) under identity-based access controls, and combine that with web grounding, citing both — a mechanism the providers document but whose ranking they largely do not.

## Key Findings
- **Google is the most explicit about mechanism and myths.** Its Search Central guide states AI Overviews and AI Mode are "rooted in our core Search ranking and quality systems," use RAG (grounding) and "query fan-out," and that content must be indexed and eligible for a snippet to appear. It explicitly debunks llms.txt, "chunking," schema-as-requirement, and inauthentic mentions.
- **OpenAI, Anthropic, and Perplexity each publish a two- or three-tier crawler model.** OpenAI: GPTBot (training), OAI-SearchBot (search), ChatGPT-User (user fetch). Anthropic: ClaudeBot (training), Claude-SearchBot (search index), Claude-User (user fetch). Perplexity: PerplexityBot (search index), Perplexity-User (user fetch). In each case the user-triggered fetcher has weaker robots.txt guarantees than the crawlers.
- **Microsoft is the only provider offering first-party citation analytics.** The Bing Webmaster Tools "AI Performance" report (public preview February 2026) exposes "grounding queries" (Copilot's internally reformulated queries, not the user's prompt) and page-level citation counts across Copilot, Bing, and partner experiences.
- **Perplexity is the only major provider with a formal, publicly documented publisher revenue-share** (Comet Plus), paying an 80% share tied to human visits, citations, and agent actions.
- **xAI/Grok is a documentation gap:** xAI publishes no crawler documentation page and no official crawler user-agent; it documents Grok's `web_search` API tool and citations only. Meta documents a family of crawlers, one of which (meta-externalfetcher) may bypass robots.txt.

## Details

### GOOGLE

**Feature: AI Overviews & AI Mode (organic Search surfaces)**
- **Venue / doc type:** Google Search Central documentation help page, "Optimizing your website for generative AI features on Google Search."
- **URL:** https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- **Latest revision:** Last updated 2026-07-10 (UTC), per the page footer. Accessed August 27, 2026.
- **Core finding:** Google states its generative AI features "are rooted in our core Search ranking and quality systems" and rely on two named techniques: **RAG/grounding** ("relying on our core Search ranking systems to retrieve relevant, up-to-date web pages from our Search index") and **query fan-out** (concurrent related queries the model generates). Eligibility requires that a page "be indexed and eligible to be shown in Google Search with a snippet," plus inclusion in the Search Console generative-AI settings. Google frames "optimizing for generative AI search" as still being SEO, and points to E-E-A-T and "helpful, reliable, people-first content."
- **Mythbusting (documentation explicitly says NOT required):** LLMS.txt and other "special" markup ("Google Search itself doesn't use them"); "chunking" content; rewriting content just for AI; seeking inauthentic "mentions"; and over-focusing on structured data ("Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add").
- **Measurement:** A "Generative AI performance report" in Search Console is referenced.
- **Effect size:** N/A — documentation.
- **COI:** Google's own commercial interest in Search and its ecosystem (Merchant Center, Business Profile) is evident in the guidance.
- **Pathway:** Retrieval/grounding (primary); some context.

**Feature: Gemini API "Grounding with Google Search"**
- **Venue / doc type:** Google AI for Developers (Gemini API) documentation; parallel pages on Google Cloud (Vertex/Agent Platform) and Firebase.
- **URL:** https://ai.google.dev/gemini-api/docs/google-search
- **Latest revision:** Firebase variant last updated 2026-08-24 (UTC); accessed August 27, 2026.
- **Core finding:** With the `google_search` tool enabled, the model decides whether to search, generates one or more queries, synthesizes results, and returns a response with **inline `url_citation` annotations** (each with `start_index`/`end_index`) and a `groundingMetadata` object (`webSearchQueries`, `groundingChunks`, `groundingSupports`, `searchEntryPoint`). The Firebase page states plainly: "Google Search does not use web pages for grounding that have disallowed Google-Extended." A daily limit of one million grounding queries is documented.
- **Enterprise variant:** "Grounding with your search API" lets a customer supply their own retrieval endpoint; a request supports up to 10 grounding sources and can combine custom search with Google Search.
- **Effect size:** N/A.
- **Pathway:** Retrieval/grounding.

**Crawler/token: Google-Extended**
- **Venue:** Google crawler documentation; announced on the Google blog.
- **Core finding:** Google-Extended is a robots.txt control token (not a fetching user-agent). It was announced September 28, 2023 by Danielle Romain, Google VP of Trust, as "a new control that web publishers can use to manage whether their sites help improve Bard and Vertex AI generative APIs, including future generations of models that power those products." Google states it "doesn't crawl web pages" — it is a standalone product token that governs whether already-crawled content may be used for Gemini training and grounding, with no impact on Search inclusion or ranking. Googlebot does the actual crawling.
- **Pathway:** Parametric recall (training) + retrieval/grounding control.

### MICROSOFT

**Feature: Copilot & Bing generative answers; Bing Webmaster Tools "AI Performance"**
- **Venue / doc type:** Bing Search Blog / Bing Webmaster Blog official posts; Microsoft Learn docs.
- **URL:** https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare (authored by Microsoft AI product managers Krishna Madhavan, Meenaz Merchant, Saral Nigam, Trishna Shah; dated June 16, 2026). The original AI Performance report launched in a February 2026 public-preview post.
- **Core finding:** Microsoft defines **grounding** as "the source material and web evidence the system uses to support and cite its response," and defines **grounding queries** as the queries the AI generates internally to retrieve content — explicitly *not* the user's original prompt. The AI Performance report shows cited pages and citation counts across "Microsoft Copilot, Bing, and select partner AI experiences." June 2026 added Intents (query classification), Topics (thematic clusters), Citation Share (a site's share of citations for a grounding query, described as "an observational metric — not a ranking system"), and Compare. Microsoft states citation patterns shift due to "changes in user behavior, evolving models, freshness signals, partner refresh cycles."
- **Grounding-query→page mapping** was added March 2026, letting owners see which pages are cited for a grounding query and vice versa (one query can map to many pages).
- **Effect size:** N/A for documentation; one third-party (Otterly) reported 647 grounding queries and 30,398 grounding events across 173 pages for its own domain over ~3 months — flagged as vendor self-report, not Microsoft data.
- **COI:** Microsoft's commercial interest in Bing index adoption and Copilot.
- **Pathway:** Retrieval/grounding.

**Feature: Microsoft 365 Copilot (enterprise grounding)**
- **Venue / doc type:** Microsoft Learn documentation ("Semantic indexing for Microsoft 365 Copilot"; "Microsoft 365 Copilot connectors overview"; Copilot Studio "Knowledge sources").
- **URL:** https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot
- **Core finding:** Copilot grounds on a per-tenant **semantic index** built on Microsoft Graph. Documented flow: user prompt → Copilot accesses Graph + semantic index (pre-processing) → modified prompt to LLM → LLM response → Graph/semantic-index post-processing → response with citations. Microsoft states grounding "only accesses content that the current user is authorized to access" (identity-based access boundary) and that "prompts, responses, and data accessed through semantic indexing aren't used to train foundation LLMs." External data requires a **Microsoft Graph connector** (synced connectors ingest into the semantic index and are citable; federated connectors return content live from an MCP server without storing it, with links at the bottom of the response). Copilot Studio's "Tenant graph grounding with semantic search" toggle governs semantic retrieval quality for agents.
- **Pathway:** Context (tenant documents, connectors) + retrieval/grounding (web via Bing).

**Protocol: IndexNow**
- **Core finding (from primary Bing guidance referenced in coverage):** IndexNow notifies participating engines (Bing, Yandex, Naver, Seznam) of new/changed/deleted URLs to speed discovery. It removes discovery lag but is not itself a ranking or citation signal; Google does not support IndexNow. (Primary IndexNow spec not directly fetched; sourced via Bing/Microsoft Learn coverage — flagged.)
- **Pathway:** Retrieval/grounding (discovery only).

### OPENAI

**Crawlers: GPTBot, OAI-SearchBot, ChatGPT-User**
- **Venue / doc type:** OpenAI platform docs ("Overview of OpenAI Crawlers") and OpenAI Help Center ("Publishers and Developers - FAQ").
- **URL:** https://developers.openai.com/api/docs/bots ; https://help.openai.com/en/articles/12627856-publishers-and-developers-faq (Help Center page updated within ~24 hours of access; accessed August 27, 2026).
- **Core finding:** OpenAI documents three independent user-agents: **GPTBot** ("used to make our generative AI foundation models more useful and safe" — i.e., training); **OAI-SearchBot** ("used to link to and surface websites in search results… not used to crawl content to train"); **ChatGPT-User** (user-triggered fetch for ChatGPT/Custom GPTs/GPT Actions; "not used for crawling the web in any automatic fashion, nor to crawl content for generative AI training"). Each setting is independent: a site can allow OAI-SearchBot while disallowing GPTBot. Robots.txt changes for search take ~24 hours to reflect. When both GPTBot and OAI-SearchBot are allowed, OpenAI may use one crawl for both to avoid duplicate crawling.
- **Citation behavior (Publisher FAQ):** "Any public website can appear in ChatGPT search"; to be included in summaries/snippets, don't block OAI-SearchBot. If OpenAI obtains a disallowed page's URL from a third-party search provider or by crawling other pages and has relevance signals, it "may surface just the link and page title" — controllable via `noindex`. Referral traffic carries `utm_source=chatgpt.com`.
- **Content partnerships:** OpenAI discloses licensing/partnership deals via press releases; these are commercial arrangements affecting discoverability, not documented ranking mechanics (flagged as secondary/press-sourced):
  - **Associated Press** (July 13, 2023) — "the first of its kind between a major AI vendor and media outlet" (VentureBeat). Per the joint statement, "The arrangement sees OpenAI licensing part of AP's text archive, while AP will leverage OpenAI's technology and product expertise"; financial terms undisclosed.
  - **News Corp** (May 2024) — reported at over $250 million over five years in cash and OpenAI credits (The Wall Street Journal, Bruell/Schechner/Seetharaman, May 23, 2024), described as "among the biggest, if not the biggest, reached to date"; News Corp CEO Robert Thomson called it "an historic agreement [that] will set new standards for veracity, for virtue and for value in the digital age."
  - **Dotdash Meredith / IAC** — OpenAI pays "a minimum of around $16 million per year" (the fixed, not variable, component), per Adweek's review of IAC filings; IAC CFO Chris Halpin told analysts Q3 2024 licensing revenue "was up about $4.1 million year over year… The lion's share of that would be driven by the OpenAI license." OpenAI models also power Dotdash Meredith's ad-targeting product.
  - Other named deals include Axel Springer, Hearst, Future plc, and Axios (with OpenAI funding four Axios Local newsrooms).
- **COI:** OpenAI's commercial interest in ChatGPT and its partner ecosystem.
- **Pathway:** Parametric (GPTBot/training), retrieval (OAI-SearchBot), context/agentic (ChatGPT-User).

### ANTHROPIC

**Crawlers: ClaudeBot, Claude-User, Claude-SearchBot**
- **Venue / doc type:** Anthropic Help Center article, "Does Anthropic crawl data from the web, and how can site owners block the crawler?"
- **URL:** https://support.anthropic.com/en/articles/8896518 (canonical support.claude.com); last updated April 7, 2026.
- **Core finding:** Three bots: **ClaudeBot** (collects web content that may contribute to training; blocking excludes future materials from training datasets); **Claude-User** (user-initiated fetch when someone asks Claude a question; blocking "prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search"); **Claude-SearchBot** (navigates the web "to improve search result quality"; blocking "prevents our system from indexing your content for search optimization"). Anthropic states all its bots respect robots.txt directives and Crawl-delay, and respect anti-circumvention (won't bypass CAPTCHAs). Legacy agents Claude-Web and Anthropic-AI are deprecated. Notably, unlike OpenAI/Perplexity, Anthropic does **not** carve out a robots.txt exception for its user-triggered fetcher.
- **Feature: Claude web search & citations (API):** Per Claude docs, web search "includes citations for sources drawn from search results," citations are always enabled for web search, and each result location returns `cited_text`, `title`, `url`; displaying citations to end users is required. Separately, the Citations feature grounds Claude in user-provided documents, returning exact supporting passages. Web search is GA on the Anthropic API (per the Claude blog) and available in claude.ai (Free/Pro/Max/Team/Enterprise).
- **Enterprise:** Claude for Enterprise/Team uses connectors and admin-enabled web search; the Citations API grounds answers in customer source documents with passage-level attribution.
- **COI:** Anthropic's commercial interest in Claude.
- **Pathway:** Parametric (ClaudeBot), retrieval (Claude-SearchBot/web search), context (Citations, connectors), agentic (Claude-User).

### PERPLEXITY

**Crawlers: PerplexityBot, Perplexity-User**
- **Venue / doc type:** Perplexity documentation, "Perplexity Crawlers."
- **URL:** https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- **Core finding:** **PerplexityBot** "is designed to surface and link websites in search results on Perplexity… not used to crawl content for AI foundation models"; to appear, allow it in robots.txt. **Perplexity-User** "supports user actions… When users ask Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page"; the docs state that "since a user requested the fetch, this fetcher generally ignores robots.txt rules." Changes take up to 24 hours. Perplexity publishes IP-range JSON endpoints and WAF configuration guidance.
- **Feature: Comet Plus / Publisher Program:** Per Perplexity's official "Introducing Comet Plus" post, Comet Plus is a subscription that distributes revenue to participating publishers "based on three types of internet traffic: human visits, search citations, and agent actions," minus a compute fee. The $5/month subscription was announced August 25, 2025, paying 80% to publishers and retaining 20% for compute, from an initial $42.5M pool; per Axios (August 26, 2025), Perplexity head of publisher partnerships Jessica Chan confirmed the "$42.5 million pool to compensate early publishing partners," with launch partners including CNN, Condé Nast, Fortune, The Washington Post, and the LA Times.
- **COI:** Perplexity's commercial interest; program launched amid publisher lawsuits (Dow Jones, Forbes, Condé Nast, News Corp).
- **Pathway:** Retrieval (PerplexityBot), context/agentic (Perplexity-User).

### OTHER PLATFORMS

**Apple — Applebot / Applebot-Extended**
- **Venue:** Apple Support, "About Applebot." URL: https://support.apple.com/en-us/119829
- **Core finding:** **Applebot** crawls to power Spotlight, Siri, Safari; data "may also be used to help train Apple foundation models." **Applebot-Extended** is a control token (not a crawler) that lets publishers opt out of training use "while still remaining in search results." Disallowing Applebot-Extended does not remove a site from Apple search results.
- **Pathway:** Parametric (Applebot-Extended controls training) + retrieval (Applebot for search/Siri).

**Brave — Summarizer / AI Answers**
- **Venue:** Brave blog ("Introducing the Summarizer," 2023) and Brave Search API documentation.
- **URL:** https://brave.com/blog/ai-summarizer/ ; https://api-dashboard.search.brave.com/app/documentation/summarizer-search
- **Core finding:** Brave states the Summarizer sources data "solely from web search results" over its own independent index, aggregating multiple sources with "source attribution… cited at all times via links." It runs Brave's own LLMs (not OpenAI). The API supports `inline_references=true` for inline citations. Chief of Search Josep M. Pujol is quoted.
- **Pathway:** Retrieval/grounding.

**xAI — Grok (DOCUMENTATION GAP)**
- **Core finding:** xAI publishes **no dedicated crawler documentation page and no official crawler user-agent token or robots.txt directive** for Grok's web fetching. Third-party bot directories cite tokens like "GrokBot/1.0" or "Grok-DeepSearch/1.0," but these are unverified against any x.ai source; operator reports (including a Cloudflare statement) indicate Grok's retrieval traffic does not reliably self-identify. xAI *does* officially document Grok's **`web_search` API tool** and a **Citations** page (docs.x.ai/developers/tools/web-search, last updated May 27, 2026), including `allowed_domains`/`excluded_domains` controls (max 5 each) and a documented `citations`/`sources` return — but this describes API behavior, not a crawler, and does not disclose source-ranking methodology. A separate `x_search` tool searches X/Twitter posts.
- **Pathway:** Retrieval (API-level); training-crawler behavior undocumented.

**Meta — Meta AI crawlers**
- **Venue:** Meta developer docs, "Web crawlers." URL: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers (crawler section added ~late July 2024; no visible last-updated date).
- **Core finding (per subagent verbatim capture):** **meta-externalagent** ("crawls the web for use cases such as training foundation AI models or improving products by indexing content directly"; respects robots.txt); **meta-externalfetcher** ("fetches individual links at a user's request… evaluating and improving agentic AI capabilities"; **"this crawler may bypass robots.txt rules"**); **meta-webindexer** ("Allowing Meta-WebIndexer… helps us cite and link to your content in Meta AI's responses"; respects robots.txt); **meta-externalads** (advertising/business products; respects robots.txt). Meta AI displays sources ("You can see Meta AI's sources by selecting Sources under its response," per Meta Help Center). Which external search index powers Meta AI grounding is not stated in Meta primary docs.
- **Pathway:** Parametric (meta-externalagent), retrieval (meta-webindexer), context/agentic (meta-externalfetcher).

### Comparison table — what each provider has publicly stated

| Provider | Separate training vs. search crawler? | User-fetch respects robots.txt? | Discloses ranking/selection signals? | Citation mechanism documented? | First-party citation analytics? | Publisher revenue program? |
|---|---|---|---|---|---|---|
| Google | Google-Extended (train) vs Googlebot (search) | Googlebot governs all | Partly (E-E-A-T, core ranking, indexed+snippet-eligible); no AI-specific signals | Yes (inline `url_citation`, `groundingMetadata`) | Search Console Generative AI report | No |
| Microsoft/Bing | Bingbot (search) + IndexNow; training via separate policies | Copilot uses Bing index | No explicit ranking; names "grounding queries," freshness as a factor | Yes (cited pages) | Yes — AI Performance report (most detailed) | No |
| OpenAI | GPTBot vs OAI-SearchBot vs ChatGPT-User | ChatGPT-User: weaker guarantees | No | Yes (links + utm_source) | No | Licensing deals (not a formal program) |
| Anthropic | ClaudeBot vs Claude-SearchBot vs Claude-User | Claude-User respects robots.txt | No | Yes (cited_text/title/url; required to display) | No | No |
| Perplexity | PerplexityBot (search) vs Perplexity-User | Perplexity-User "generally ignores robots.txt" | No | Yes (numbered citations) | No | Yes — Comet Plus (80/20) |
| Apple | Applebot-Extended (train) vs Applebot (search) | N/A | No | Limited | No | No |
| Brave | Own index | N/A | No | Yes (inline references) | No | No |
| xAI/Grok | Not documented | Not documented | No | API-level citations only | No | No |
| Meta | meta-externalagent vs meta-webindexer | meta-externalfetcher may bypass | No | Yes ("Sources") | No | Licensing (two-tier, reported) |

### Per-provider crawler user-agent table

| Provider | User-agent | Stated purpose | Respects robots.txt? | Official doc |
|---|---|---|---|---|
| Google | Googlebot | Search index (feeds AI Overviews/AI Mode) | Yes | developers.google.com/search |
| Google | Google-Extended | Control token for Gemini training/grounding (not a crawler) | Yes (token) | Google crawler docs |
| OpenAI | GPTBot | Foundation-model training | Yes | developers.openai.com/api/docs/bots |
| OpenAI | OAI-SearchBot | ChatGPT search surfacing (not training) | Yes | same |
| OpenAI | ChatGPT-User | User-triggered fetch (ChatGPT, Custom GPTs, GPT Actions) | Weaker guarantees | same |
| Anthropic | ClaudeBot | Training | Yes | support.anthropic.com/en/articles/8896518 |
| Anthropic | Claude-SearchBot | Search index for Claude search | Yes | same |
| Anthropic | Claude-User | User-triggered fetch | Yes | same |
| Perplexity | PerplexityBot | Search index (not training) | Yes | docs.perplexity.ai |
| Perplexity | Perplexity-User | User-triggered fetch | "Generally ignores robots.txt" | same |
| Apple | Applebot | Search (Spotlight, Siri, Safari); may also train | Yes | support.apple.com/en-us/119829 |
| Apple | Applebot-Extended | Control token to opt out of AI training | Yes (token) | same |
| Meta | meta-externalagent | Training / indexing | Yes | developers.facebook.com/docs/sharing/webmasters/web-crawlers |
| Meta | meta-externalfetcher | User-triggered fetch / agentic | "May bypass robots.txt rules" | same |
| Meta | meta-webindexer | Search index for Meta AI citations | Yes | same |
| Meta | meta-externalads | Advertising/business products | Yes | same |
| xAI/Grok | Not officially documented | — | Not documented | none (API docs only: docs.x.ai) |

### Common practitioner claims NOT supported by official documentation

1. **"llms.txt affects AI citations / rankings."** Google's documentation explicitly says it doesn't use llms.txt and that maintaining one "will neither harm nor help your site's visibility." No major provider documents llms.txt as a citation signal.
2. **"Schema markup is required for AI Overviews."** Google explicitly: "Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add" (though it remains useful for rich results).
3. **"AI Overviews only cite the top-10 organic results."** Google documents RAG + query fan-out over its index; it does not state a top-10 restriction, and fan-out deliberately pulls varied results.
4. **"ChatGPT search is just Bing."** OpenAI documents its own OAI-SearchBot crawler and index for ChatGPT search; it is not documented as a Bing passthrough. (Bing powers Microsoft Copilot, and historically powered SearchGPT's early prototype, but current ChatGPT search inclusion is governed by OAI-SearchBot.)
5. **"Perplexity ranks by domain authority."** Perplexity documents only that PerplexityBot must be allowed for inclusion; it does not publish any domain-authority ranking signal.
6. **"Freshness is a direct, standalone citation signal."** Microsoft lists "freshness signals" among many factors that shift citation patterns and recommends IndexNow for faster discovery, but frames freshness as removing discovery lag, not as a guaranteed citation lever; IndexNow "does not guarantee indexing, ranking, or citation."
7. **"Blocking GPTBot (or ClaudeBot) removes you from AI search answers."** Officially false: blocking the training crawler does not block the search crawler or user fetcher. To leave ChatGPT search you must address OAI-SearchBot; for Claude, Claude-SearchBot/Claude-User.
8. **"Google-Extended / Applebot-Extended blocking hurts search rankings."** Both companies state these training tokens have no effect on search inclusion or ranking.
9. **"Grounding queries in Bing are the user's search terms."** Microsoft explicitly says grounding queries are the AI's internally reformulated queries, not the user's prompt.
10. **"A partnership guarantees citations."** Providers document partnerships as affecting discoverability, not as overriding relevance/ranking; Google's docs warn against expecting favorable placement from "mentions."

## Recommendations

**Stage 1 — Fix the crawler-access foundation (this week).** Audit robots.txt against each provider's *three-tier* model. To be eligible for AI search/grounding while retaining training control, allow the search crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot, meta-webindexer) and decide separately on training crawlers (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, meta-externalagent). Verify you are not accidentally blocking search bots via WAF/429 rate-limits — a documented common failure. **Benchmark that changes the plan:** if server logs show search crawlers receiving 403/429, fix that before any content work.

**Stage 2 — Meet documented eligibility, not myths.** Ensure pages are indexed and snippet-eligible (Google's stated prerequisite), server-render key content, and use clean semantic HTML. Do **not** invest in llms.txt, content "chunking," or schema *solely* for AI features — Google says these don't help its AI surfaces. Keep schema for rich results and keep IndexNow for fast Bing/Copilot discovery of frequently-updated pages. **Threshold:** treat schema/IndexNow as discovery/eligibility hygiene, not citation levers.

**Stage 3 — Instrument with first-party data.** Verify in Bing Webmaster Tools and use the AI Performance report (the only first-party citation dataset) to see grounding queries, cited pages, and Citation Share. Use Google Search Console's Generative AI performance report for Google surfaces. Track `utm_source=chatgpt.com` referrals. **Benchmark:** if Citation Share for priority grounding queries is flat or falling over a Compare period, revisit content depth/freshness for those topics.

**Stage 4 — Enterprise deployments.** For Microsoft 365 Copilot, prioritize semantic-index coverage and Graph connectors for the tenant data you want cited, and confirm identity-based access boundaries; for Gemini/Vertex and Claude/OpenAI enterprise, use the documented grounding/Citations APIs (custom search endpoints, source documents) so answers cite tenant sources with passage-level attribution. **Threshold:** measure grounding quality (share of answers with correct tenant citations) before broadening rollout.

**Stage 5 — Publisher economics.** If you are a publisher, evaluate Perplexity Comet Plus and OpenAI/Meta licensing on their documented terms (usage-based vs. flat-fee), recognizing providers do not guarantee citations in exchange.

## Caveats
- **Mechanism vs. strategy.** Per the task's framing, treat provider statements as authoritative about *mechanism* (which crawler does what; how citations are surfaced) and non-authoritative about *strategy*. No provider discloses its actual source-ranking or selection algorithm for generative answers.
- **Documentation drift.** These pages change frequently. Dates captured: Google AI-optimization guide 2026-07-10; Firebase grounding 2026-08-24; Anthropic crawler article April 7, 2026; Bing AI-visibility post June 16, 2026; OpenAI Publisher FAQ updated within a day of access; xAI web-search tool May 27, 2026. Re-verify before relying on any specific claim.
- **Secondary sourcing flagged inline.** Comet Plus terms (80/20, $42.5M, $5/mo, launch partners) trace to Perplexity's post plus Axios (Aug 26, 2025); OpenAI deal values (News Corp WSJ May 23, 2024; Dotdash Meredith via Adweek/IAC filings; AP via VentureBeat) are press/filing-sourced; the Otterly grounding-event figures, IndexNow specifics, and Meta's two-tier citation model come from vendor/press coverage, not the providers' primary mechanism docs.
- **xAI is a genuine gap:** absence of official crawler documentation is itself the finding; do not treat third-party "GrokBot" tokens as authoritative. Meta's live developer page could not be directly fetched (429 rate-limiting); its crawler text was captured via search-result extraction of the official page and cross-confirmed.
- **Enrichment note:** several Microsoft Learn enterprise pages and the OpenAI/Perplexity primary blog posts were corroborated through both primary fetches and secondary coverage; where only secondary coverage exists it is labeled.