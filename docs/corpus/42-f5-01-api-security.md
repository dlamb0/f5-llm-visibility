# F5 API Security — Solution Area Reference (Doc 01)
doc_id: 01-api-security
solution_area: API Security
doc_tag: API-SEC
products_covered: F5 Distributed Cloud (XC) API Security, F5 API Security Local Edition, F5 BIG-IP Advanced WAF, F5 WAF for NGINX (formerly NGINX App Protect WAF), F5 NGINX Plus (API gateway)
compiled: July 2026
primary_release_anchor: F5 WAAP/API security release of June 9, 2026 (introduced F5 API Security Local Edition; expanded the AI-powered risk scoring that GA'd in XC release 2025.10.0, March 2026). Prior anchors: AppWorld 2026 (March 11, 2026) and XC Services 7.0 (December 2025).
refresh_priority: High — three material naming/packaging changes and one new product landed between Dec 2025 and Jun 2026.
last_validated: July 2026

---

## Layer 1 — Human orientation

### What F5 API Security is

F5 does not sell one API-security product. It delivers API-security capabilities through several vehicles, all now branded under the **F5 Application Delivery and Security Platform (ADSP)**:

1. **F5 Distributed Cloud (XC) API Security** — the SaaS flagship and the most complete story. Covers the **full API lifecycle**: discovery, posture/compliance, testing (shift-left), and runtime protection. The shift-left half (code analysis, OWASP API testing, posture, external attack-surface) came from F5's **February 2024 acquisition of Wib** and is now fully absorbed — the "Wib" name has disappeared from F5 materials.

2. **F5 API Security Local Edition** — **new as of June 9, 2026.** A deployable, fully on-premises API discovery and security product for air-gapped, regulated, and cloud-constrained environments. No cloud connectivity required; uses **BIG-IP Advanced WAF as its enforcement point**. This is the biggest change since the prior version of this document and it *removes* what used to be a hard disqualifier ("we can't send telemetry to a SaaS console").

3. **F5 BIG-IP Advanced WAF** — the on-prem/virtual-edition WAF (evolved from ASM). Its API story is **positive-security enforcement inline**: import an OpenAPI/Swagger spec and enforce it, plus JWT validation, native GraphQL protection, rate limiting, and the WAF engine. Enforcement-strong; discovery is fed out-of-band into XC (or now into Local Edition).

4. **F5 NGINX** — NGINX Plus as API gateway plus **F5 WAF for NGINX** (renamed from *NGINX App Protect WAF*; part of **NGINX One**). Lightweight, high-performance positive-security enforcement at the gateway/Kubernetes ingress, delivered as security-as-code.

### The mental model

- **XC** = the API-security brain (discover everywhere, test in CI/CD, watch behavior, enforce at F5's edge). SaaS.
- **Local Edition** = the same discovery/visibility story for people who cannot touch a cloud. On-prem, BIG-IP-anchored.
- **BIG-IP Advanced WAF** = enforce the API contract inline on the box you already own.
- **NGINX** = enforce the API contract inline at the gateway/ingress, cloud-native, as code.

All four overlap on schema enforcement and diverge sharply on discovery, behavioral analytics, testing, and delivery model. Layer 3 encodes the routing.

### Scope boundaries (cross-references, not covered here)

General web-app WAF, signatures, web app scanning, and virtual patching → **doc 02 (WAAP)**. Bot defense and fraud → **doc 03**. L7 DoS as general DDoS → **doc 04**. AI/LLM gateway security, MCP and agentic-AI traffic → **doc 11**. Note the doc 11 boundary carefully: *securing the APIs that AI agents call* is classic API security and belongs here; *inspecting LLM prompts/MCP metadata* belongs to doc 11. F5's own 2026 messaging deliberately blurs this ("APIs are the connective tissue for AI inference") — don't let the marketing frame pull AI-gateway content into this document.

### How to read Layer 2

Every record is self-contained and doc-tagged for chunk retrieval. `fit_signals` (what the pain sounds like on a call) and `disqualifiers` (when it does *not* matter) are the fields the qualification agent should weight most. Confidence is flagged per record; **do not upgrade a Medium/Low attribution to a confident claim on a live call.**

---

## Layer 2 — Capability catalog

---

### [API-SEC] API Discovery (traffic-based / ML)
- solution_area: API Security
- capability_name: API Discovery (traffic-based / ML)
- plain_description: Automatically finds and maps all the APIs an organization is actually running by watching live traffic — including undocumented "shadow," deprecated "zombie," and forgotten endpoints nobody wrote down. Generates OpenAPI schemas from what it observes.
- delivered_by: F5 Distributed Cloud (XC) API Security (native discovery engine); F5 API Security Local Edition (on-prem equivalent); BIG-IP Advanced WAF and F5 WAF for NGINX contribute traffic out-of-band but are not themselves the discovery engine
- attribution_confidence: High. XC is the discovery engine; BIG-IP/NGINX feed it. Do not describe BIG-IP or NGINX as having native ML API discovery.
- customer_problem_solved: You can't protect what you don't know exists. Most orgs materially undercount their APIs; unmanaged endpoints are a primary breach vector.
- fit_signals: "We don't have a full inventory of our APIs." "Developers spin up endpoints without telling security." "We found an API during an incident that nobody knew was exposed." "Our Swagger docs are out of date / don't match production." "We think we have shadow or zombie APIs." An auditor asked for an API inventory they couldn't produce. Recent M&A leaving unknown estates.
- disqualifiers: Small, fully-documented API surface already inventoried under a rigorous design-first process; purely internal APIs with no exposure and mature internal cataloging; customer already runs a discovery tool they're happy with and is not consolidating.
- value_framing: "You can't secure or even risk-rank an API you don't know about. We continuously discover the APIs you're actually running — including the ones that bypassed your process — and turn that into a living inventory with generated schemas."
- product_routing_note: Lead with **XC** in every case. If the customer is cloud-hesitant, route to the out-of-band discovery record below; if they are air-gapped or sovereignty-constrained, route to **F5 API Security Local Edition**. Discovery is the standard wedge for an immature account — sell visibility first, not the full lifecycle.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/api-security; docs.cloud.f5.com "Enable API Endpoint Discovery and Schema Learning"; DevCentral "Out of the Shadows: API Security, Discovery, and Inventory"

---

### [API-SEC] Out-of-Band Discovery Across Multiple Data Planes (BIG-IP, NGINX, Kong, Apigee)
- solution_area: API Security
- capability_name: Out-of-Band Discovery Across Multiple Data Planes (BIG-IP, NGINX, Kong, Apigee)
- plain_description: Discovers and inventories APIs from traffic flowing through F5 and non-F5 proxies and gateways without sitting inline — no added latency, no new failure point, no application changes — and surfaces everything centrally in the XC console.
- delivered_by: F5 Distributed Cloud (XC) API Security (aggregation point); ingests from BIG-IP (TMOS 15.1+), NGINX OSS/Plus, Kong, and Apigee
- attribution_confidence: High — named explicitly in F5's March 2026 AppWorld blog and press release, with a docs.cloud.f5.com how-to for the BIG-IP virtual-server integration.
- customer_problem_solved: APIs flow through many gateways; teams can't get one inventory without touching every app. Inline discovery tools raise latency, reliability, and operational-complexity objections that kill deals in performance-sensitive industries.
- fit_signals: "We have APIs behind lots of different gateways — Kong, Apigee, NGINX, BIG-IP." "We can't add another hop / we can't touch the data path." "Even a few milliseconds of latency is a dealbreaker" (financial services, e-commerce, media). "We can't change our apps just to get API visibility." "We already run BIG-IP and want API visibility without a forklift." "We tried an inline API security tool and it caused an outage / we won't risk one."
- disqualifiers: Single-gateway estate already fully inventoried; customer explicitly wants inline enforcement rather than passive visibility; environments with no external connectivity at all (route to Local Edition instead).
- value_framing: "Get one API inventory across every proxy and gateway you already run — F5 or not — without re-architecting a single app, without adding a hop, and without putting anything new in your data path."
- product_routing_note: **This is the key coexistence hook.** It lets you land **XC** in an established **BIG-IP or NGINX** account as an out-of-band add-on rather than a replacement. Lead with it whenever the customer is cloud-hesitant but wants discovery. Note the maturity history below and confirm the specific integration the customer needs.
- maturity_flag: GA. Note the trajectory: the Dec 2025 (XC 7.0) blog labelled the multi-proxy and universal log-collection options **early access**; by the March 2026 AppWorld blog the EA labels were dropped and they are described as supported verified integrations. **Verify per-integration status before promising a specific one** — especially the "universal / any gateway" log-collection option, which is the least clearly described.
- source_currency_flag: Current
- source: f5.com blog "API security without compromise: Introducing flexible new discovery options with F5 API security" (11 Mar 2026); f5.com press release "F5 Advances Enterprise Application Security for the AI and Post-quantum Era" (11 Mar 2026); docs.cloud.f5.com BIG-IP virtual-server discovery how-to; prior EA status from f5.com blog "Stay ahead of API security risks…" (Dec 2025)

---

### [API-SEC] On-Premises / Air-Gapped API Discovery and Protection (F5 API Security Local Edition)
- solution_area: API Security
- capability_name: On-Premises / Air-Gapped API Discovery and Protection (F5 API Security Local Edition)
- plain_description: A deployable software product that delivers API discovery, visibility, risk scoring, and blocking entirely on-premises, with its own local console and no cloud connectivity or external data sharing. Uses BIG-IP Advanced WAF as the enforcement point.
- delivered_by: F5 API Security Local Edition (standalone product); F5 BIG-IP Advanced WAF (enforcement point)
- attribution_confidence: High for existence, positioning, and the BIG-IP dependency — announced as a named product with its own f5.com product page. Medium on operational detail (scale, sizing, exact console feature parity with XC) — **not found in public sources.**
- customer_problem_solved: Regulated, sovereign, and air-gapped organizations have been structurally excluded from modern API security because every credible product was SaaS. Data sovereignty rules and classified environments forbid telemetry leaving the premises.
- fit_signals: "We can't send any data to a vendor cloud." "We're air-gapped." "Data sovereignty / data residency won't allow it." "We're defense / intelligence / government / critical infrastructure." "Our regulator won't accept a SaaS security console." "We looked at API security vendors and they were all cloud-only, so we did nothing." "Our most sensitive workloads can't phone home." Also: a customer who previously rejected XC on data-residency grounds — this is a re-open signal.
- disqualifiers: Customer is happy with SaaS (XC is the richer product — don't downsell into Local Edition); customer has no BIG-IP and won't buy one (enforcement depends on BIG-IP Advanced WAF integration); customer wants shift-left code analysis and OWASP testing — **public sources describe Local Edition as discovery, visibility, risk scoring, and blocking, not the full Wib-derived lifecycle. Do not promise testing/code analysis parity with XC.**
- value_framing: "You no longer have to choose between API security and your compliance boundary. Full API visibility, risk scoring, and enforcement — running entirely inside your own walls, with nothing leaving the building."
- product_routing_note: Lead with **Local Edition** only where cloud is genuinely off the table; otherwise lead with XC. Requires a **BIG-IP Advanced WAF** enforcement point — this makes it a natural attach for an existing BIG-IP estate and a two-product conversation for a greenfield air-gapped prospect. Predecessor: the "local API discovery" early-access capability announced Dec 2025 and the "deployable software option" described at AppWorld March 2026; productized and named June 2026.
- maturity_flag: GA (announced 9 June 2026)
- source_currency_flag: Current
- source: f5.com press release "F5 expands AI-powered WAAP solutions to arm enterprises against frontier AI threats and stop attacks before exploitation" (9 Jun 2026); f5.com/products/api-security-local-edition; f5.com blog "API security without compromise…" (Mar 2026)

---

### [API-SEC] Positive Security Model / OpenAPI Schema Enforcement
- solution_area: API Security
- capability_name: Positive Security Model / OpenAPI Schema Enforcement
- plain_description: Enforce an "only allow exactly what the API spec permits" model — valid endpoints, methods, parameters, data types, payloads — and block anything that deviates. The spec can be an existing OpenAPI/Swagger file or one learned from live traffic.
- delivered_by: F5 Distributed Cloud (XC) API Security; F5 BIG-IP Advanced WAF; F5 WAF for NGINX (formerly NGINX App Protect WAF)
- attribution_confidence: High — the one capability all three genuinely deliver, each with primary-source documentation.
- customer_problem_solved: Negative-security (block-known-bad) misses novel and business-logic abuse. Enforcing the contract shrinks the attack surface to only intended behavior and rejects malformed or abusive requests.
- fit_signals: "We already maintain OpenAPI/Swagger specs and want to actually enforce them." "We want to block anything that doesn't match the contract." "We're getting malformed requests hitting endpoints." "We do design-first API development." Mentions of parameter tampering, unexpected HTTP methods, or mass-assignment worries. "Our WAF policy and our API spec have drifted apart."
- disqualifiers: No specs and no appetite to generate them (start with discovery instead — it generates schemas); extremely volatile APIs changing many times a day where strict enforcement without pipeline automation would produce constant false positives; a team unwilling to own policy maintenance.
- value_framing: "Turn your API spec into an enforced security policy. If it's not in the contract, it doesn't get through — and you can wire it into CI/CD so the policy updates when the API does."
- product_routing_note: Route by where traffic terminates. **NGINX** for cloud-native/Kubernetes gateway enforcement as code. **BIG-IP Advanced WAF** for on-prem appliance/VE. **XC** for SaaS enforcement at F5's edge unified with discovery/testing. Implementation detail worth knowing on a technical call: on BIG-IP, re-importing an updated spec erases prior entities except signatures and meta-characters — relevant to CI/CD design.
- maturity_flag: GA (all three)
- source_currency_flag: Current
- source: BIG-IP: techdocs.f5.com "Working with OpenAPI" (BIG-IP ASM Implementations 17.x); NGINX: docs.nginx.com + f5.com blog "Secure Your API Gateway with NGINX App Protect WAF"; XC: f5.com/products/distributed-cloud-services/api-security

---

### [API-SEC] Sensitive Data Detection and Leakage Prevention
- solution_area: API Security
- capability_name: Sensitive Data Detection and Leakage Prevention
- plain_description: Inspect API requests and responses to find sensitive data (PII, PCI, credentials, data tied to GDPR/HIPAA) flowing through APIs, identify which fields carry it, and limit, mask, or block it.
- delivered_by: F5 Distributed Cloud (XC) API Security (primary); F5 API Security Local Edition (surfaces security risks on-prem — exact sensitive-data parity with XC **unverified**)
- attribution_confidence: High for XC. **Low for BIG-IP and NGINX — do not attribute XC-style API data classification to either.** BIG-IP DataSafe (client-side field encryption) and DataGuard (response filtering) are adjacent credential/response features, not equivalent; flag the distinction rather than blur it.
- customer_problem_solved: APIs routinely over-return data (excessive data exposure, OWASP API3). Organizations leak PII/PCI through poorly designed responses without knowing it.
- fit_signals: "We're worried our APIs return more data than they should." "We had — or nearly had — a data exposure through an API." "We need to prove PII/PCI isn't leaking through APIs for our audit." "Auditors want to know what sensitive data our APIs expose." "We don't know which APIs touch regulated data." Data-residency or masking requirements.
- disqualifiers: APIs carrying no sensitive or regulated data (public read-only reference data); no compliance or privacy driver; data classification already handled by a DSPM tool the customer won't displace.
- value_framing: "See exactly which APIs touch PII, PCI, or regulated data — and stop over-exposure before it becomes a breach or an audit finding."
- product_routing_note: Lead with **XC**. Pairs naturally with API Discovery and Authentication-State Detection as a "discover → classify → risk-rank" narrative. If the customer only has BIG-IP and raises *credential* protection, DataSafe is adjacent and worth mentioning — explicitly as a different thing.
- maturity_flag: GA (XC)
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/api-security; docs.cloud.f5.com "Sensitive Data Discovery"; F5 Solution Overview "F5 Distributed Cloud API Security"; Gartner Peer Insights (F5 XC API Security)

---

### [API-SEC] Behavioral Anomaly Detection (ML-based runtime monitoring)
- solution_area: API Security
- capability_name: Behavioral Anomaly Detection (ML-based runtime monitoring)
- plain_description: Continuously baseline normal API behavior with machine learning and flag anomalies — unusual call patterns, abuse, or attacks that look like legitimate traffic and slip past signatures and rate limits.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: High for XC as the ML behavioral engine for APIs. Note BIG-IP and NGINX have their own behavioral L7 DoS analytics — a different capability (see doc 04). Don't conflate.
- customer_problem_solved: The most damaging API attacks — business-logic abuse, low-and-slow reconnaissance, credential abuse with valid tokens — look like normal traffic and evade static controls.
- fit_signals: "Attackers are using valid tokens/credentials against us." "We're seeing odd but not obviously malicious API usage." "Rate limits and our WAF aren't catching business-logic abuse." "We need to detect abuse, not just known attack signatures." Mentions of scraping, enumeration, inventory hoarding, or account takeover via APIs.
- disqualifiers: Very low-traffic APIs where ML has no baseline to learn from; customer wants only deterministic block-lists, not probabilistic detection; no SecOps capacity to triage anomaly alerts (they'll buy it and ignore it).
- value_framing: "Schema enforcement stops malformed requests. Behavioral analytics catches the attacker who is technically inside the contract but abusing your business logic — the attacks that actually cause breaches."
- product_routing_note: **XC** only. This is a strong reason to bring XC into a BIG-IP/NGINX account that already enforces schemas — position it as the analytics layer their inline proxies structurally lack.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/api-security; Gartner Peer Insights (F5 XC API Security)

---

### [API-SEC] Authentication-State Detection and API Risk Scoring
- solution_area: API Security
- capability_name: Authentication-State Detection and API Risk Scoring
- plain_description: Identify and baseline whether API endpoints are authenticated, and score which APIs are risky — for example a sensitive endpoint exposed without authentication.
- delivered_by: F5 Distributed Cloud (XC) API Security; F5 API Security Local Edition (risk scoring on-prem)
- attribution_confidence: High — "Authentication Discovery and Risk Scoring" is a named feature in the XC API Security product page and solution overview.
- customer_problem_solved: Unauthenticated or weakly authenticated sensitive endpoints are a top breach source; teams have no way to rank which APIs to fix first.
- fit_signals: "We're not sure which of our APIs are actually behind auth." "We need to prioritize which APIs to remediate — we can't fix them all." "We suspect some sensitive endpoints are exposed without login." "We want a risk score per endpoint." "Our pen test found an unauthenticated endpoint and we don't know if there are others."
- disqualifiers: Uniform, well-understood, audited auth across all APIs; a surface small enough that risk ranking is trivial.
- value_framing: "We tell you which APIs are unauthenticated, sensitive, and therefore your highest risk — so remediation is prioritized by real exposure instead of guesswork."
- product_routing_note: **XC** (or **Local Edition** on-prem). Do not confuse this with the AI-powered *request* risk scoring in XC WAF (separate record, different thing, different product). This one scores **API endpoints**; that one scores **individual requests**.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/api-security; F5 Solution Overview "F5 Distributed Cloud API Security"; f5.com press release (9 Jun 2026) for Local Edition risk scoring

---

### [API-SEC] Inline Runtime API Protection (rate limiting, IP reputation, endpoint blocking)
- solution_area: API Security
- capability_name: Inline Runtime API Protection (rate limiting, IP reputation, endpoint blocking)
- plain_description: Actively block and throttle abusive API traffic in the data path — per-endpoint rate limiting, IP-reputation and allow/deny enforcement, and blocking of suspicious endpoints via a granular L7 policy engine.
- delivered_by: F5 Distributed Cloud (XC) API Security; F5 BIG-IP Advanced WAF; F5 WAF for NGINX; F5 API Security Local Edition (blocking via BIG-IP Advanced WAF)
- attribution_confidence: High — documented for each.
- customer_problem_solved: APIs get hammered by automated abuse, scraping, and brute force; static WAF rules alone don't throttle by API context.
- fit_signals: "Our APIs are getting scraped or brute-forced." "We need per-endpoint rate limits." "We want to throttle abusive clients without blocking everyone." "We need to shut down a specific endpoint fast when it's being abused."
- disqualifiers: Internal-only APIs with trusted, low-volume traffic and no abuse exposure; abuse already handled by an upstream control the customer is satisfied with. **Cross-reference:** general/volumetric DDoS belongs to doc 04; bot-specific abuse and fraud belong to doc 03 — if the call is really about bots, route there.
- value_framing: "Stop API abuse in the data path — throttle by endpoint, block bad-reputation sources, and shut down abused endpoints without touching the application."
- product_routing_note: Route by where traffic terminates: **NGINX** at cloud-native gateway/ingress; **BIG-IP** on-prem; **XC** at F5's global edge; **Local Edition + BIG-IP** in air-gapped environments. For surgical per-endpoint limits inside the DC, BIG-IP/NGINX; for enforcement in front of everything, XC's edge.
- maturity_flag: GA (all)
- source_currency_flag: Current
- source: F5 Solution Overview "F5 Distributed Cloud API Security" (App and API Security Enforcement Engine); my.f5.com K44584132 (BIG-IP Guided Config: rate limiting, allowlist/denylist); f5.com/products/nginx/f5-waf-for-nginx

---

### [API-SEC] API Authentication Enforcement (JWT validation, OAuth scope)
- solution_area: API Security
- capability_name: API Authentication Enforcement (JWT validation, OAuth scope)
- plain_description: Validate and enforce API authentication tokens in the data path — check JWT existence, structure, validity period, and signature; enforce OAuth scopes; deny requests that fail validation before they reach the app.
- delivered_by: F5 BIG-IP Advanced WAF (JWT; OAuth scope via BIG-IP Zero Trust Access, formerly BIG-IP APM); F5 NGINX Plus (gateway-level JWT/OAuth)
- attribution_confidence: High for BIG-IP (JWT and OAuth well documented in techdocs) and NGINX Plus (core gateway function). **Medium on XC's native token-validation depth — lead with BIG-IP or NGINX for deep token enforcement, not XC.**
- customer_problem_solved: Broken authentication (OWASP API2) is a top API risk; teams need well-formed, signed, authorized tokens enforced at the edge rather than trusting the application to do it.
- fit_signals: "We need to validate JWTs / verify signatures at the gateway." "We want to enforce OAuth scopes on our APIs." "Our apps trust tokens they probably shouldn't." "We want to offload token validation from app teams to the proxy." "Every microservice re-implements auth slightly differently."
- disqualifiers: Auth fully and correctly handled by an identity/gateway layer the customer won't move; APIs with no authentication requirement by design.
- value_framing: "Enforce token validity and authorization at the proxy — reject malformed, unsigned, expired, or out-of-scope tokens before they ever touch your application."
- product_routing_note: **On-prem token enforcement → BIG-IP Advanced WAF (+ BIG-IP Zero Trust Access for OAuth).** **Cloud-native/gateway → NGINX Plus.** Use XC's authentication-state *detection* to find where enforcement is missing, then enforce with BIG-IP/NGINX — that's a clean two-product narrative. **Naming alert:** F5 announced at AppWorld (11 Mar 2026) that **BIG-IP Access Policy Manager (APM) is becoming BIG-IP Zero Trust Access**. Older F5 docs (including K44584132 and the API Protection Concepts pages) still say "APM." Both names are live in the field; ZTAA is the go-forward name. The broader zero-trust story is out of scope here — only the OAuth/API-protection piece belongs to this document.
- maturity_flag: GA
- source_currency_flag: Current for the capability; naming in the underlying techdocs is **Possibly stale** (still "APM")
- source: techdocs.f5.com "API Security" (JWT, BIG-IP ASM Implementations 17.5); techdocs.f5.com "API Protection Concepts" (APM OAuth scope agent); my.f5.com K44584132; f5.com press release + blog "Hello, F5 BIG-IP Zero Trust Access" (11 Mar 2026)

---

### [API-SEC] GraphQL and gRPC API Protection
- solution_area: API Security
- capability_name: GraphQL and gRPC API Protection
- plain_description: Extend API protection beyond REST to GraphQL and gRPC — parsing these formats correctly, applying signatures to the right parts of the payload, and enforcing GraphQL-specific limits like query depth, batched-query count, and introspection blocking.
- delivered_by: F5 BIG-IP Advanced WAF (GraphQL native since v16.1; REST/JSON/XML/GWT); F5 WAF for NGINX (REST, GraphQL, gRPC); F5 Distributed Cloud (XC) API Security (detects API types incl. GraphQL/gRPC/SOAP/XML-RPC in discovery; GraphQL inspection controls)
- attribution_confidence: High for BIG-IP and NGINX — **upgraded from the prior version of this document, which rested on a third-party review.** Now confirmed by primary F5 sources. Medium for XC: GraphQL discovery and inspection (max query length, structure depth, batched-query limits) are documented; **XC gRPC protection depth is not clearly documented — an open F5 feature-request exists for XC API Security gRPC, which suggests gaps. Do not claim XC gRPC protection depth on a call.**
- customer_problem_solved: Modern microservice and mobile back-ends increasingly use GraphQL/gRPC. A URL-and-query-string-oriented WAF can't protect GraphQL, which operates on a single endpoint — policies must analyze at the query level. GraphQL also enables batching and deeply nested queries that cause resource-exhaustion DoS.
- fit_signals: "A lot of our APIs are GraphQL, not REST." "Our WAF can't parse our GraphQL traffic / it just sees one URL." "We're getting false positives on GraphQL because the WAF scans the whole request." "We have gRPC between microservices we need to inspect." "We're worried about deeply nested or batched GraphQL queries taking us down." "Someone can introspect our schema."
- disqualifiers: Pure REST/JSON estate with no GraphQL or gRPC; internal-only gRPC on a fully trusted mesh with no threat model.
- value_framing: "Your API estate isn't just REST. GraphQL needs query-level policy — depth limits, batching limits, introspection control — not URL filtering. We parse it natively instead of waving it through as an opaque blob."
- product_routing_note: **BIG-IP Advanced WAF** for GraphQL on-prem (dedicated GraphQL policy template + content profile, configurable via GUI, REST, or declarative policy — strong for CI/CD). **F5 WAF for NGINX** for gRPC-heavy or cloud-native estates (explicit REST/GraphQL/gRPC support). **XC** for GraphQL discovery/inspection; **route gRPC-depth questions away from XC** until verified.
- maturity_flag: GA (BIG-IP GraphQL since v16.1; NGINX REST/GraphQL/gRPC). Unknown for XC gRPC protection depth.
- source_currency_flag: Current
- source: f5.com blog "Securing GraphQL APIs with F5 Advanced WAF"; techdocs.f5.com BIG-IP 16.1/17.0 release notes (GraphQL profile, violations); DevCentral "Securing GraphQL with Advanced WAF declarative policies"; f5.com/products/nginx/f5-waf-for-nginx; docs.cloud.f5.com API Attributes (type detection); DevCentral "Beyond REST: Protecting GraphQL" (XC inspection controls)

---

### [API-SEC] API Code Analysis (shift-left / build-time)
- solution_area: API Security
- capability_name: API Code Analysis (shift-left / build-time)
- plain_description: Analyze application source code and integrate with API code repositories to discover API endpoints and assess their risks before deployment, so problems are caught in development rather than production.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: High — originally from the Wib acquisition, explicitly stated in F5's own press release and blog; the capability persists on the current XC API Security product page ("seamlessly integrate into API code repositories to begin discovering, testing and monitoring your APIs earlier in the development lifecycle").
- customer_problem_solved: Finding API vulnerabilities only at runtime is late and expensive; teams want to shrink the window during which a vulnerable API is live.
- fit_signals: "We want to shift API security left." "We find API vulns too late, in production." "We want security in the CI/CD pipeline, not just at the edge." "Dev teams ship APIs faster than security can review them." "Our AppSec and our network security teams don't talk." A DevSecOps mandate.
- disqualifiers: Customer only wants runtime protection and won't integrate with dev pipelines; no access to source code (securing third-party APIs only); a security team with no developer relationship or influence; **air-gapped customers on Local Edition — this is XC-only.**
- value_framing: "Catch API risks in code, before they ship — shrink the window where a vulnerable API is live and exploitable, instead of finding out during an incident."
- product_routing_note: **XC** only. Differentiator versus proxy-only competitors *and* versus F5's own BIG-IP/NGINX. Use when the buyer is AppSec/DevSecOps rather than NetOps. Do not promise this in a Local Edition deal.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com blog "F5 Is Shifting Left to Protect APIs"; f5.com press release "F5 Transforms Application Security for the AI Era" (Feb 2024); f5.com/products/distributed-cloud-services/api-security

---

### [API-SEC] Dynamic API Testing (OWASP API Top 10)
- solution_area: API Security
- capability_name: Dynamic API Testing (OWASP API Top 10)
- plain_description: Actively probe APIs for vulnerabilities and validate suspected threats, testing for specific OWASP API Top 10 weaknesses — broken object-level authorization (BOLA), broken authentication, broken object property-level authorization, unrestricted resource consumption, and broken function-level authorization.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: High — F5 press releases name the specific OWASP API categories covered: API1 (BOLA), API2 (Broken Authentication), API3 (BOPLA), API4 (Unrestricted Resource Consumption), API5 (BFLA).
- customer_problem_solved: Static enforcement doesn't tell you whether an API is *exploitable*. Authorization flaws in particular can't be found by signatures — they require actually testing whether user A can reach user B's object.
- fit_signals: "We're worried about BOLA / broken object-level authorization." "Our pen test found API authorization issues and we need continuous testing, not annual." "We need to test our APIs against the OWASP API Top 10." "We want to know which vulns are actually exploitable, not a list of theoretical findings." "We have endpoints where each user should only see their own data and we're not confident that holds."
- disqualifiers: A mature dedicated API-testing/DAST program the customer is satisfied with; no non-prod environment and unwillingness to test in production; testing outside this buyer's remit; **Local Edition customers — XC-only.**
- value_framing: "Don't wait for an attacker or next year's pen test to find your authorization flaws. Continuously test against the OWASP API Top 10 and validate what's actually exploitable."
- product_routing_note: **XC** only. Coverage has expanded steadily — the Dec 2025 (7.0) release added API1/API4 scenarios and enhanced detection across API1/API2/API3/API5. Cite that when a customer asks "how current is this?"
- maturity_flag: GA, actively expanding
- source_currency_flag: Current
- source: f5.com press release "F5 Elevates ADSP with Comprehensive API Discovery and Application Delivery Enhancements" (Dec 2025); f5.com blog "Stay ahead of API security risks with our latest F5 Distributed Cloud release"; Help Net Security (11 Dec 2025)

---

### [API-SEC] API Compliance and Posture Management
- solution_area: API Security
- capability_name: API Compliance and Posture Management
- plain_description: Assess whether APIs meet regulatory and security-posture requirements, with real-time standards and compliance reporting for security operations teams and CISOs.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: Medium-High. Named in F5's Feb 2024 press release ("API compliance analysis," "posture management") and consistent with current lifecycle positioning. **The exact current form and naming of compliance reporting is not clearly described in current public materials — describe the capability, don't promise a named dashboard.**
- customer_problem_solved: Teams struggle to prove API security posture and governance to auditors and leadership across a sprawling estate.
- fit_signals: "We need to report API compliance to auditors or the board." "We have a governance gap on APIs." "Our CISO wants a posture view across all our APIs." "We're driven by PCI/HIPAA/GDPR on our APIs." "We can't show real-time API compliance status — it's a spreadsheet exercise."
- disqualifiers: No compliance or governance driver; posture already covered by a GRC/ASPM tool the customer won't displace; an engineering-only buyer with no reporting obligation.
- value_framing: "Give your CISO and your auditors a real-time, standards-aligned view of API posture — turn API governance from a quarterly spreadsheet into continuous reporting."
- product_routing_note: **XC**. Strongest when the economic buyer is a CISO or compliance owner rather than a hands-on engineer. Pair with discovery (you can't report on what you haven't found).
- maturity_flag: GA
- source_currency_flag: Possibly stale (naming//form of reporting)
- source: f5.com press release "F5 Transforms Application Security for the AI Era" (Feb 2024); F5 Solution Overview "F5 Distributed Cloud API Security"

---

### [API-SEC] External API Attack-Surface Assessment
- solution_area: API Security
- capability_name: External API Attack-Surface Assessment
- plain_description: Monitor an organization's public-facing assets from the outside in for newly appearing APIs and APIs operating outside security governance — an attacker's-eye view of the external API footprint.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: Medium. Described as "API threat surface assessment" in F5's Feb 2024 shift-left blog; third-party summaries reference external crawling as a discovery input. **Current productized naming not confirmed in current F5 materials — describe the capability, flag the name.** Note the adjacent, separately-named **F5 Distributed Cloud Web App Scanning** covers external discovery of exposed web apps and APIs (that product belongs to doc 02).
- customer_problem_solved: APIs get exposed publicly without security's knowledge; orgs lack an outside-in view of what an attacker can already see.
- fit_signals: "We don't know what we're exposing to the internet." "We want an attacker's-eye view of our external footprint." "Developers publish public APIs bypassing our process." "We've grown by acquisition and don't have a unified external inventory." "Shadow IT keeps standing things up in cloud accounts we don't manage."
- disqualifiers: No external/public API exposure; external footprint already continuously monitored by an EASM tool the customer is happy with.
- value_framing: "See the APIs an attacker sees. Catch newly exposed and ungoverned public APIs before someone else finds them."
- product_routing_note: **XC**. Complements traffic-based discovery (inside-out) with an outside-in view — sell the pair as "complete inventory." If the conversation drifts to scanning web apps generally, that's **doc 02**.
- maturity_flag: GA (naming Unknown)
- source_currency_flag: Possibly stale
- source: f5.com blog "F5 Is Shifting Left to Protect APIs" (Feb 2024); Gartner Peer Insights (F5 XC API Security — external crawling as discovery input)

---

### [API-SEC] CI/CD Pipeline Integration (security-as-code for API policy)
- solution_area: API Security
- capability_name: CI/CD Pipeline Integration (security-as-code for API policy)
- plain_description: Manage and deploy API security policy as code alongside the API itself — pull specs from a repo, update policy automatically as the API changes, and integrate into CI/CD and GitOps workflows.
- delivered_by: F5 WAF for NGINX (declarative, native to the model); F5 BIG-IP Advanced WAF (declarative JSON policy, OAS import, AS3); F5 Distributed Cloud (XC) API Security (API-first, Terraform provider, vesctl CLI)
- attribution_confidence: High — documented for all three; most native for NGINX.
- customer_problem_solved: Manual, ticket-driven WAF/API policy updates can't keep pace with API release velocity; policy drifts from the actual API contract.
- fit_signals: "We want security policy in our pipeline / as code." "Our WAF changes need approvals and lag releases by weeks." "We do GitOps." "Dev teams own deployment and won't wait on a security ticket." "We want the policy to update when the spec updates." "Security is the bottleneck in our release process."
- disqualifiers: Traditional change-managed ops with no CI/CD; a team that prefers GUI-driven manual policy and isn't automating; **note the tension** — a customer with no pipeline maturity will struggle with strict schema enforcement (see the Positive Security record's disqualifiers).
- value_framing: "Ship API security at the speed of your releases. Policy lives in the repo with the API, updates in the pipeline, and never drifts from the contract."
- product_routing_note: **NGINX** for cloud-native/DevOps-first buyers — declarative is the native model and the WAF is embedded in the gateway. **BIG-IP** declarative WAF (JSON) + AS3 for customers automating an existing BIG-IP estate. **XC** for SaaS/API-first automation (Terraform).
- maturity_flag: GA (all three)
- source_currency_flag: Current
- source: DevCentral "Advanced WAF v16.0 — Declarative API"; my.f5.com K44584132 (CI/CD Guided Config); docs.nginx.com; f5.com blog "Secure Your API Gateway with NGINX App Protect WAF"; DevCentral hybrid-architecture DevSecOps article

---

### [API-SEC] AI Assistant for API Security (natural-language querying)
- solution_area: API Security
- capability_name: AI Assistant for API Security (natural-language querying)
- plain_description: A natural-language assistant in the Distributed Cloud console that lets teams query API security events, explain incidents, and get context and actionable recommendations without deep tooling expertise.
- delivered_by: F5 Distributed Cloud (XC) API Security
- attribution_confidence: High — **resolved since the prior version of this document.** The XC API Security product page explicitly lists the AI assistant for API security events, and docs.cloud.f5.com documents it in the WAAP workspace with an "Explain with AI" action. Powered by F5 AI Data Fabric.
- customer_problem_solved: Stretched security teams can't quickly interrogate API telemetry or triage alerts; expertise is the bottleneck and alert fatigue is real.
- fit_signals: "Our team is stretched thin / we have no API-security specialists." "We want to ask questions in plain language instead of building queries." "We're drowning in alerts and can't tell which matter." "Investigation takes us days." Interest in AI-assisted operations.
- disqualifiers: Customer distrusts AI-assisted tooling for security decisions; regulated environment restricting such features; buyer indifferent to console UX; **air-gapped customers — Local Edition has its own local console; assistant parity is unverified.**
- value_framing: "Let your team ask 'what happened with this API?' in plain English and get an explanation plus recommended next steps — without needing a specialist for every question."
- product_routing_note: **XC** only. A supporting/differentiating capability, not a lead. Use to reinforce the consolidated, easier-to-operate platform message. **Status resolved: GA — the prior 'verify before promising' caveat can be dropped.**
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/api-security; docs.cloud.f5.com "AI Assistant for WAAP" and "Use AI Assistant"; f5.com blog "Introducing the AI Assistant for F5 Distributed Cloud Services"

---

### [API-SEC] AI-Powered Request Risk Scoring (XC WAF — applies to API traffic)
- solution_area: API Security
- capability_name: AI-Powered Request Risk Scoring (XC WAF — applies to API traffic)
- plain_description: A continuously trained neural-network risk engine that gives every inbound request a numerical, multi-signal risk score rather than a binary block/allow, aiming to catch novel exploit patterns before a signature exists.
- delivered_by: F5 Distributed Cloud WAF (a WAF capability — see doc 02); F5 API Security Local Edition has its own separate on-prem "risk scoring and blocking"
- attribution_confidence: **Medium — attribute carefully; this is the most easily over-claimed item in this document.** F5 attributes AI-powered risk scoring to **F5 Distributed Cloud WAF**, not to XC API Security as a named feature. Public sources say it scores "every request," and SecureIQLab testing of F5 WAAP reported 100% accuracy against key risks in **both** the OWASP WAF Top 10 and the **OWASP API Top 10** — so API traffic traversing XC WAF is clearly in scope. But **no public source states that risk scoring is an API-endpoint-aware feature of XC API Security.** Say "F5's Distributed Cloud WAF scores every request, including requests to your API endpoints" — do **not** say "XC API Security includes AI risk scoring."
- customer_problem_solved: Frontier AI models have collapsed the gap between vulnerability discovery and exploitation; attackers no longer need a published CVE. Signature-based defenses are structurally behind, and signature tuning burns SecOps time.
- fit_signals: "We're worried about zero-days / attacks with no signature yet." "Our WAF is all false positives and endless tuning." "We can't patch fast enough." "AI-generated attacks are outpacing our signatures." "We want context on a request, not just blocked/allowed."
- disqualifiers: Customer wants deterministic, explainable rules only; not running traffic through XC WAF (the capability is bound to that data path); **if the conversation is really about general WAF efficacy rather than APIs, this belongs to doc 02.**
- value_framing: "Signatures only catch what's already been named. A continuously trained risk engine scores every request — including those hitting your APIs — so novel exploit patterns get caught before a signature exists."
- product_routing_note: This is primarily a **doc 02 (WAAP)** story; it appears here only because API traffic is scored and SEs will hear it in API conversations. Lead with it in an API deal **only** as reinforcement of the platform argument. For on-prem/air-gapped, **Local Edition** has its own risk scoring — a distinct implementation; don't imply they're the same engine.
- maturity_flag: GA (GA in Distributed Cloud release 2025.10.0, March 2026, per docs.cloud.f5.com; expanded and heavily promoted in the 9 Jun 2026 WAAP release — see doc 02)
- source_currency_flag: Current
- source: docs.cloud.f5.com "AI Powered Risk Scoring" (GA in release 2025.10.0); f5.com press release "F5 expands AI-powered WAAP solutions…" (9 Jun 2026); f5.com press release "F5 Advances Enterprise Application Security for the AI and Post-quantum Era" (11 Mar 2026); Help Net Security (10 Jun 2026)

---

### [API-SEC] SIEM / Telemetry Integration and Forensics (adjacent-enabling)
- solution_area: API Security
- capability_name: SIEM / Telemetry Integration and Forensics (adjacent-enabling)
- plain_description: Feed API security events, analytics, and forensic detail into SIEMs and data lakes for centralized analysis and investigation. *Adjacent: an integration/observability enabler, not an API-security control in itself.*
- delivered_by: F5 Distributed Cloud (XC) API Security (Splunk, Datadog, Opsgenie, Slack integrations); F5 WAF for NGINX (attack logs to SIEM); F5 BIG-IP Advanced WAF (ASM logging)
- attribution_confidence: High for existence of logging/SIEM feeds; Medium on per-product API-specific forensic depth.
- customer_problem_solved: Security teams need API events in existing SOC tooling; insufficient logging and monitoring is itself an OWASP API risk (API10).
- fit_signals: "We need API security events in our SIEM / Splunk / data lake." "Our SOC needs forensic detail on API incidents." "We have to satisfy logging and monitoring requirements for APIs." "Nobody would notice if an API were being abused right now."
- disqualifiers: No SOC or SIEM and no plan for one; customer wants a self-contained console with no external integration.
- value_framing: "API security events land where your SOC already works — full forensic context in your SIEM, closing the insufficient-logging gap."
- product_routing_note: Not a lead capability — use to answer integration objections. All products can feed a SIEM; XC centralizes analytics. Labelled adjacent deliberately; don't build a pitch on it.
- maturity_flag: GA
- source_currency_flag: Current
- source: WorldTech IT / F5 XC materials (Splunk, Datadog integrations); f5.com blog "Secure Your API Gateway with NGINX App Protect WAF" (SIEM logging, API10)

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product Routing

**First principle:** XC is the API-security *brain* (discovery, behavioral analytics, testing, posture). BIG-IP and NGINX are inline *enforcement* points where traffic already terminates. Local Edition is the brain for people who can't reach the cloud. Most complete deals lead with XC and attach it to the customer's existing inline footprint. Enforcement-only deals lead with BIG-IP or NGINX.

**Routing by customer situation:**

- **Already runs NGINX at ingress, no WAF / no API security.**
  → Attach **F5 WAF for NGINX** in place for schema enforcement and OWASP API protection with minimal added latency (WAF embedded in the gateway = one fewer hop). Then attach **XC** out-of-band for discovery, behavioral analytics, and testing the gateway structurally can't provide. Classic land-and-expand.

- **Runs BIG-IP on-prem, cloud-hesitant.**
  → Enforce on the **BIG-IP Advanced WAF** they already own (OpenAPI import, JSON schema, JWT, GraphQL, rate limiting). Bring **XC** in as **out-of-band API discovery** (TMOS 15.1+) — visibility without a SaaS data path. Emphasize the no-latency, no-new-failure-point framing from F5's March 2026 discovery messaging; it's built for exactly this objection.

- **Cannot use cloud at all (air-gapped, sovereign, classified, regulated).**
  → **F5 API Security Local Edition** + **BIG-IP Advanced WAF** as enforcement. This is new as of June 2026 and is the single biggest change to routing since the prior version of this doc. **Re-open any account previously lost or stalled on data-residency grounds.** Be honest that Local Edition is scoped to discovery/visibility/risk-scoring/blocking — do not promise XC's shift-left testing.

- **Cloud-native / greenfield / SaaS-first.**
  → **XC** as the unified SaaS platform, and/or **NGINX** for cloud-native/Kubernetes inline enforcement as code. Don't lead with BIG-IP absent an on-prem, hardware, or FIPS requirement.

- **Wants managed / SaaS.** → **XC**. F5 runs the platform and the global edge.

- **Wants self-managed / full control / on-prem data path.** → **BIG-IP Advanced WAF** (max control, iRules, hardware) or **NGINX** (lightweight software). Add **Local Edition** if the constraint is regulatory rather than preferential.

- **Buyer is AppSec / DevSecOps.** → Lead with **XC** shift-left (code analysis, OWASP testing, posture) and CI/CD-as-code. This is where XC differentiates from proxy-only competitors *and* from F5's own inline products.

- **Buyer is CISO / compliance owner.** → Lead with **XC** discovery + posture/compliance reporting + sensitive-data detection + risk scoring. In regulated/sovereign contexts, **Local Edition** is now the compliance-native answer.

- **Buyer is NetOps / infrastructure.** → Lead with the inline product they already run; frame XC as visibility that doesn't disturb their data path.

**Coexistence and migration notes (what the SE should say):**
- Running more than one F5 product here is architecture, not redundancy. BIG-IP/NGINX enforce inline where traffic lives; XC discovers across all of them and adds analytics and testing the proxies lack. The multi-data-plane discovery explicitly ingests from BIG-IP, NGINX, Kong, and Apigee into one inventory.
- The honest coexistence pitch: **"enforce where you already are; see and test from XC."** Don't position XC as replacing a working BIG-IP/NGINX enforcement layer.
- Useful architectural fact for technical audiences: F5 uses the **BIG-IP Advanced WAF engine as the core of F5 WAF for NGINX and XC WAAP**, so policy intent is broadly portable across form factors. A common pattern is broad protection at the XC edge with strict per-app positive-security policy at NGINX/BIG-IP closer to the app.
- **Where the public record is thin:** F5 publishes no crisp official "if X then product Y" API-security decision matrix. The routing above is synthesized from product positioning and delivery-model differences — **not** a quoted F5 playbook. If asked "what does F5 officially recommend," say the guidance follows delivery model and constraints, and cite the product pages. Don't invent official guidance.

---

### 3b. Disqualifiers / Anti-Patterns (Aggregate)

Observable call signals that F5 API Security is a **weak fit or too early**, with reasoning.

- **"All our APIs are internal microservices, trusted east-west, nothing exposed."** → Weak fit for the external attack-surface and edge-enforcement story. Internal BOLA/authorization testing may still apply, but the urgency and the standard value framing don't land. Qualify for internal authorization concerns before pushing. Note XC's Enterprise package does extend to internal apps — so this is a de-prioritize, not an automatic no.

- **"No compliance or privacy driver."** → Removes a major lever (posture reporting, sensitive-data detection). Not disqualifying alone; fall back to breach-risk framing, but expect a longer, weaker deal.

- **"We have no API inventory and aren't sure we have an API problem."** → *A discovery lead, not a disqualifier* — but they're not ready to buy runtime protection or testing. Lead with **discovery only**. Flag as "early — start with visibility." Over-pitching the full lifecycle here loses the deal.

- **"Our API gateway / platform already covers this."** → Not a disqualifier; a specific objection (see 3c). Don't concede, don't oversell.

- **"Tiny, fully documented, design-first API surface, already enforced and audited."** → Low urgency for discovery/testing. Inline enforcement via NGINX/BIG-IP may still fit. De-prioritize the lifecycle story.

- **"We won't send any telemetry to a SaaS console."** → **No longer a disqualifier as of June 2026.** Route to **F5 API Security Local Edition**. *(This entry was a genuine disqualifier in the prior version of this document — it has been superseded. Verify Local Edition fits their specific enforcement needs, since it depends on BIG-IP.)*

- **"No budget owner for API security; it's nobody's job."** → Organizational too-early signal. The deal stalls on ownership regardless of technical fit. Flag as "no economic buyer identified."

- **"We can't tolerate any latency or new failure point in the data path."** → Not a disqualifier for F5 specifically — this is precisely the objection out-of-band discovery was built to answer. But it *does* disqualify an inline-first pitch. Lead with out-of-band discovery, not inline enforcement.

- **The conversation is actually about AI/LLM prompts, MCP, or agentic traffic.** → Route to **doc 11**. F5's own messaging conflates these with API security; the downstream agent should not.

---

### 3c. Competitive Positioning and Objection Handling (bounded — all lower confidence)

> **Confidence caveat for this whole section.** Competitive claims are lower-confidence and move fast. Lead with what F5 claims and what its architecture supports — not head-to-head "F5 beats X" assertions you can't verify. Verify independence/acquisition status before naming anyone.

**Consolidation status (re-verified as of mid-2026 — Medium confidence, third-party sourced):**

| Vendor | Status | Note |
|---|---|---|
| **Salt Security** | **Independent** | Still the pure-play benchmark. Shipped an agentic AI security platform (Mar 2026) and Salt Code (Jun 2026); "Ask Pepper AI" assistant (Dec 2025). Detection-oriented, out-of-band — relies on third-party enforcement. |
| **Cequence** | **Independent** | Unified API protection; native inline blocking; strong on bot/business-logic abuse. Leader, 2025 KuppingerCole. |
| **Wallarm** | **Independent** | WAF + API protection combined; inline blocking; developer-oriented. |
| **Akamai API Security** | **Absorbed** — Noname (Jun 2024, ~$450M) + earlier Neosec | Sold within Akamai's edge/WAAP portfolio; positioned as vendor-neutral across CDNs/gateways; CI/CD testing strength. |
| **Traceable** | **Absorbed** — merged with Harness (Mar 2025) | Now "Traceable by Harness," inside a DevSecOps platform. Distributed-tracing heritage → strong BOLA/authorization context. |
| **42Crunch** | **Absorbed** — Palo Alto Networks (Sept 2024) | Spec-audit and shift-left heritage; now inside Palo Alto's platform. |
| **Imperva** | **Absorbed** — Thales (Dec 2023) | WAF-extension approach to API security. |

The strategic read for an SE: **the pure-play category is narrowing and API security is being absorbed into platforms.** That trend is F5's friend — it's the same argument F5 makes. A customer buying a standalone pure-play in 2026 should expect it to sit inside a larger platform within a normal contract term.

**The three alternative categories:**

1. **Dedicated / pure-play API security vendors** (Salt, Cequence, Wallarm; Akamai and Harness as absorbed variants).
   *F5's stated angle:* a **single platform** spanning discovery + testing + posture + runtime, **eliminating separate API-security tools**, from a vendor already in the data path of a large share of the world's applications. Two structural F5 advantages worth stating plainly: (a) **enforce anywhere** — SaaS edge, on-prem appliance, cloud-native gateway, or fully air-gapped — which no pure-play matches; (b) **out-of-band discovery across non-F5 gateways** (Kong, Apigee), so F5 can add value without displacing the gateway.
   *Be honest:* Salt/Cequence/Wallarm have strong specialist reputations, and some (Cequence, Wallarm) offer native inline blocking that pure detection tools lack. Don't claim F5 wins specific feature battles you can't evidence.

2. **Cloud-native WAAPs** (Cloudflare, Akamai, Imperva/Thales, hyperscaler WAFs).
   *F5's stated angle:* F5 offers WAAP too (via XC), but pairs it with **full-lifecycle API security including shift-left code analysis and testing** that edge-only WAAPs typically lack, plus enforcement flexibility beyond edge-only — including on-prem and air-gapped, which edge-native vendors structurally cannot do.

3. **"We'll just use our API gateway / it's built into our platform"** (Kong, Apigee, Gravitee, MuleSoft, cloud gateways). **The most common deal-killer — handle directly below.**

**The API-gateway objection (specific treatment):**

The framing that **an API gateway is not equivalent to API security** is industry consensus, not just an F5 talking point — Imperva, Salt, Cequence, and independent commentary all make the same argument. Useful supporting point: **Gartner itself** (cited in F5's March 2026 release) advises organizations to evaluate platform solutions first and notes many will need to **combine a CDN, WAF, or API threat-protection solution *with* an API gateway**, while minimizing moving parts to avoid "proxy overload." That's a third-party anchor for "gateway *and* API security," not "gateway *or*."

Four points that hold up publicly:

- **A gateway only governs the APIs routed through it.** Shadow, zombie, and directly exposed APIs bypass it entirely and are therefore invisible to it. Discovery is the gap.
- **Gateways operate one transaction at a time against known patterns.** The most damaging attacks — business-logic abuse and BOLA with valid tokens — look like legitimate traffic and require behavioral analysis correlated over time.
- **Gateways don't classify the data flowing through them.** They can't tell you which APIs leak PII/PCI.
- **Gateways don't test your APIs for vulnerabilities.** No shift-left code analysis, no OWASP API Top 10 testing.

*F5's positioning:* gateways are **complementary, not competitive**. Note the nuance that makes F5's version of this argument unusually strong: **NGINX is itself an API gateway**, and F5's own message is that embedding the WAF *in* the gateway removes a hop that separate WAF+gateway architectures require. So with F5 the choice isn't "gateway vs. API security" — it's "gateway plus API security from one vendor, one fewer hop." And for a customer committed to Kong or Apigee, F5 doesn't ask them to rip it out: out-of-band discovery ingests from those gateways.

**Rules for staying honest:**
- Don't assert head-to-head wins (e.g. "F5's behavioral detection beats Salt's") — not publicly verifiable.
- Do lead with verifiable structural advantages: full-lifecycle single platform; enforce anywhere including air-gapped; already in the data path if they run any F5; discovery across non-F5 gateways.
- The **SecureIQLab 2026** result (F5 WAAP + AI Guardrails: 97.09% total security score; 100% against key OWASP WAF Top 10 and API Top 10 risks; perfect bot and L7 DoS scores) is a **third-party-validated** data point and the strongest citable proof in this section — but it tests **WAAP**, not XC API Security in isolation. Cite it precisely.
- Flag competitive claims as your read of public positioning; defer to F5 competitive enablement for authoritative head-to-heads.

---

## Appendix — Naming, currency & confidence ledger

### Perishable naming to watch (highest-churn part of this document)

| Current name | Former / also known as | Notes |
|---|---|---|
| **F5 Application Delivery and Security Platform (ADSP)** | — | Umbrella brand for the whole portfolio. Stable through mid-2026. |
| **F5 WAF for NGINX** | **NGINX App Protect WAF** | Rename confirmed still current (docs.nginx.com states "formerly known as NGINX App Protect WAF"). Part of the **NGINX One** package. Both names live in the field. |
| **F5 BIG-IP Zero Trust Access** | **BIG-IP Access Policy Manager (APM)** | **New rename, AppWorld 11 Mar 2026.** Matters here because OAuth/API protection historically ran through APM. Underlying techdocs (incl. K44584132) still say "APM." Expect both names on calls. |
| **F5 API Security Local Edition** | (predecessor: "local API discovery," early access, Dec 2025) | **New product, 9 Jun 2026.** Air-gapped/on-prem. |
| **F5 Distributed Cloud Services — Essentials / Enterprise packages** | Dozens of individual SKUs; older "Base Package" | **New packaging, AppWorld Mar 2026.** Both tiers include API security. Essentials = quick start, public-facing apps (WAF, API protection, DDoS, CDN). Enterprise = internal + external apps, behavioral analysis, client-side, deeper visibility. Consumption-based metering. **Packaging detail beyond this is not public — do not quote prices.** |
| **Wib** | — | Acquired Feb 2024, fully absorbed. The name no longer appears in current F5 materials; the shift-left capabilities remain. Use "XC API Security," not "Wib," with customers. |
| **XC Services 7.0** (Dec 2025) | — | Prior release anchor, now superseded by AppWorld 2026 (Mar) and the WAAP release (Jun). |

### Resolved since the prior version of this document

- **XC AI assistant GA status** → **Resolved: GA.** Documented in docs.cloud.f5.com and named on the XC API Security product page for API security events.
- **GraphQL/gRPC depth** → **Resolved.** BIG-IP GraphQL confirmed native since v16.1 via primary sources (upgraded from a third-party review). NGINX REST/GraphQL/gRPC confirmed on the F5 product page. XC GraphQL discovery + inspection confirmed; **XC gRPC depth remains unverified.**
- **Non-F5 proxy discovery (Kong, Apigee, universal, air-gapped) GA vs. EA** → **Resolved.** EA labels present in Dec 2025 were dropped by the Mar 2026 AppWorld blog; air-gapped productized as Local Edition in Jun 2026. Verify per-integration for the universal log-collection option.
- **"API security fusion engine" naming** → **Resolved as: do not use.** The term appears only in F5's Feb 2024 shift-left blog and **does not appear in any current F5 material.** The underlying correlation concept survives (the solution overview describes correlating good/bad actor activity and sensitive data), but there is no evidence it was productized under that name. **Do not say "fusion engine" to a customer.** The prior doc's record for it has been removed rather than carried forward.

### Explicitly not verified — do not assert

- **XC gRPC protection depth** — Unverified; an open F5 feature request for XC API Security gRPC suggests gaps. Route gRPC-depth questions to NGINX.
- **F5 API Security Local Edition operational detail** — scale, sizing, console feature parity with XC, and whether any shift-left/testing capability is included. Public sources describe discovery, visibility, risk scoring, and blocking only. **Do not promise XC parity.**
- **Whether AI-powered risk scoring is API-endpoint-aware** — F5 attributes it to Distributed Cloud **WAF** scoring every request. No public source frames it as an XC API Security feature. See that record's attribution note.
- **Current form/naming of API compliance reporting** and **external attack-surface assessment** — capabilities are real; current productized names are not confirmed.
- **Any official F5 API-security product-routing matrix** — not found. Layer 3a is synthesized.
- **Pricing/packaging SKU detail** — beyond the existence of Essentials/Enterprise and that both include API security, no current public pricing was found. Flag currency if you find any.
- **FedRAMP status** — f5.com describes XC Services as FedRAMP "In Process" targeting Moderate. Verify current status before citing to a public-sector customer; this is exactly the kind of claim that ages badly and where Local Edition may be the better answer anyway.

### Sources leaned on

**Primary (F5):** f5.com/products/distributed-cloud-services/api-security; f5.com/products/api-security-local-edition; f5.com/products/nginx/f5-waf-for-nginx; f5.com/products/big-ip-services/advanced-waf; f5.com/products/get-f5/compare; press releases "F5 expands AI-powered WAAP solutions…" (9 Jun 2026), "F5 Advances Enterprise Application Security for the AI and Post-quantum Era" (11 Mar 2026), "F5 Strengthens Its ADSP…" (11 Mar 2026), "F5 Elevates ADSP…" (10 Dec 2025), "F5 Transforms Application Security for the AI Era" (Feb 2024); blogs "API security without compromise: Introducing flexible new discovery options" (Mar 2026), "F5 Distributed Cloud Services reimagined for the platform era" (Apr 2026), "F5 Is Shifting Left to Protect APIs," "Securing GraphQL APIs with F5 Advanced WAF," "Secure Your API Gateway with NGINX App Protect WAF," "Introducing the AI Assistant for F5 Distributed Cloud Services"; techdocs.f5.com (BIG-IP ASM "Working with OpenAPI," "API Security," "API Protection Concepts," 16.1/17.0 release notes); docs.cloud.f5.com (API endpoint discovery/schema learning, AI Assistant for WAAP, BIG-IP virtual-server discovery); docs.nginx.com; my.f5.com K44584132; DevCentral technical articles; F5 Solution Overview "F5 Distributed Cloud API Security" (PDF).

**Third-party (competitive reality-check, lower trust):** Gartner Peer Insights (F5 XC API Security; BIG-IP Advanced WAF); Help Net Security (Dec 2025, Jun 2026); SiliconANGLE (Mar 2026); CRN/theoutpost (AppWorld 2026 packaging); Dark Reading; SDxCentral; acquisition reporting (Akamai/Noname, Harness/Traceable, Palo Alto/42Crunch); Tracxn/PitchBook (vendor independence status). SEO "best API security tools" listicles treated as low-trust and used only to cross-check acquisition status. WAFPlanet was relied on in the prior version for BIG-IP GraphQL/gRPC; that claim has since been **replaced with primary F5 sourcing** and the third-party dependency retired.
