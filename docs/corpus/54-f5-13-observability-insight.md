# F5 Observability & Insight — Solution Area Reference (Doc 13)

doc_id: 13-observability-insight
solution_area: Observability & Insight
doc_tag: OBS
products_covered: F5 Insight for ADSP, F5 AI Assistant (BIG-IP iRules / NGINX One / Distributed Cloud), F5 Distributed Cloud Synthetic Monitoring, F5 NGINX One Console (fleet visibility), F5 BIG-IP Telemetry Streaming, F5 AI Data Fabric, F5 Application Study Tool (AST, community); adjacent/retired: F5 Distributed Cloud AIP (formerly Threat Stack)
compiled: July 2026
primary_release_anchor: F5 Insight for ADSP GA for BIG-IP, AppWorld 2026 (March 11, 2026); F5 Insight v1.1 (May 2026); v1.2 (announced July 15, 2026)
refresh_priority: High — F5 Insight is ~4 months old, versioned roughly monthly, and NGINX/XC coverage plus SaaS delivery are still roadmap
last_validated: July 2026

---

## Layer 1 — Human orientation

**Observability & Insight** is the story of seeing what is happening across F5's own data planes — BIG-IP, NGINX, and F5 Distributed Cloud — and turning that telemetry into answers and recommended actions. It is deliberately scoped to F5-delivered visibility of F5-delivered traffic and infrastructure. It is NOT a general-purpose APM/observability platform play (Datadog, New Relic, Grafana Cloud, Splunk); F5's own public position is that Insight *complements* those tools rather than replacing them — per F5 DevCentral's "Introducing F5 Insight for ADSP": *"F5 Insight is not intended to replace SIEM solutions like Splunk or Sentinel but serves a different, complementary purpose."*

**Read this first — routing honesty:** Observability is rarely the *lead* pain on an SE call. It is almost always (a) an **attach/expansion** motion on top of an existing BIG-IP/NGINX/XC footprint, or (b) an **objection-neutralizer** when a consolidation deal triggers the fear "will we lose visibility if we standardize on F5?" Treat this solution area as a deal-strengthener and a way to prove ROI on the F5 estate, not as a standalone deal-maker. If a customer's primary ask is "replace our observability stack," that is a disqualifier, not a fit.

**Products that carry the story and how they differ in delivery model:**
- **F5 Insight for ADSP** — the anchor. GA for BIG-IP as of March 2026, delivered as **self-managed software** (a qcow/OVA VM running open-source components: OpenTelemetry Collector, VictoriaMetrics, Grafana; internally orchestrated by K3s). A **SaaS model is forthcoming (not yet shipped)**; NGINX and Distributed Cloud coverage are **roadmap**. Includes an AI assistant trained on F5 product knowledge, with MCP + LLM querying.
- **F5 AI Assistant** — natural-language operational aid embedded in BIG-IP (iRules), NGINX One, and Distributed Cloud consoles. Adjacent to observability (it explains/generates config and queries logs), consolidated here as one record; deep per-product content lives in the sibling product docs.
- **F5 Distributed Cloud Synthetic Monitoring** — SaaS synthetic (outside-in) monitoring of HTTP/DNS endpoints from global regions, part of the XC Observability service.
- **F5 NGINX One Console** — fleet-wide visibility/inventory for NGINX instances (covered in depth in sibling docs 05/10; only its observability facet is summarized here).
- **F5 BIG-IP Telemetry Streaming (TS)** — the pre-Insight, still-current mechanism to push BIG-IP telemetry *into* third-party tools (Datadog, Splunk, Dynatrace, Elastic). This is the honest answer to "we already have Datadog."

The **capability catalog (Layer 2)** is the core; each record is self-contained. **Layer 3** gives product routing, an aggregate disqualifier list, and bounded competitive/objection handling. An **appendix** tracks perishable naming and confidence.

---

## Layer 2 — Capability catalog

### [OBS] Unified BIG-IP telemetry and analytics (F5 Insight)
- solution_area: Observability & Insight
- capability_name: Unified BIG-IP telemetry, dashboards, and analytics
- plain_description: Collects telemetry from a fleet of BIG-IP devices and presents curated dashboards (app health, performance, security, infrastructure, inventory) in one place, so teams stop logging into individual boxes to piece together what's happening.
- delivered_by: F5 Insight for ADSP (self-managed software); underlying open-source heritage from the community F5 Application Study Tool (AST)
- attribution_confidence: High
- customer_problem_solved: BIG-IP is often a "black box" — telemetry is trapped per-device; troubleshooting outages and Day-2 analysis across a fleet is slow and manual.
- fit_signals: "We have dozens of BIG-IPs and no single view of them." "When an app is slow we can't tell if it's the F5 or the backend." "Our BIG-IP is a black box." "It takes forever to do a health check across our LTM fleet." "We can't prove the value of our F5 investment to management." Teams doing manual iHealth/CLI sweeps; a recent outage where root cause took days; a fleet migration or refresh where they need utilization data to right-size.
- disqualifiers: No BIG-IP footprint (Insight is BIG-IP-anchored today). Customer already standardized BIG-IP telemetry into a mature Splunk/Datadog practice and is happy with it. Single small BIG-IP pair where per-device GUI is sufficient.
- value_framing: "Turn your BIG-IP estate from a black box into a data-rich platform — see fleet-wide health, prove ROI, and cut mean-time-to-repair, using open-source tooling you already know."
- product_routing_note: Only F5 Insight delivers this as a productized, supported solution today. For customers not ready to license Insight, the community Application Study Tool (AST) offers the same open-source stack unsupported.
- maturity_flag: GA (BIG-IP only)
- source_currency_flag: Current
- source: f5.com/products/f5-insight; f5.com blog "Announcing F5 Insight for ADSP" (Mar 11 2026); clouddocs.f5.com/products/insight

### [OBS] AI-assisted querying and operational narratives (F5 Insight)
- solution_area: Observability & Insight
- capability_name: Natural-language querying, recommendations, and operational narratives
- plain_description: Lets teams ask questions of their BIG-IP telemetry in plain language and get back AI-generated summaries, prioritized action items, and "what happened / what's impacted / what to do next" narratives, via MCP and LLM integration.
- delivered_by: F5 Insight for ADSP (with its built-in AI assistant trained on F5 product knowledge); powered in part by F5 AI Data Fabric (limited availability integration)
- attribution_confidence: High
- customer_problem_solved: Dashboard fatigue and alert overload — teams have data but not clarity; they don't know which of a thousand signals matters or what to do about it.
- fit_signals: "We have a dozen tools, a thousand alerts, and not enough signal." "By the time we correlate logs the incident is over." "Our junior engineers can't interpret BIG-IP data." "We want recommendations, not just more dashboards." Blame-wars between NetOps and AppOps about whose problem an incident is; a desire to democratize BIG-IP knowledge as senior BIG-IP experts retire.
- disqualifiers: Customer prohibits LLM integration or sending data to external models / has strict data-residency constraints (note the AI Data Fabric integration requires sharing data with F5 and is limited availability). Teams that want raw data export only.
- value_framing: "Move from firefighting to operational excellence — Insight turns scattered telemetry into a clear story and the next best action, with 30 years of F5 expertise baked in."
- product_routing_note: This is a differentiator of Insight specifically. The broader F5 AI Assistant (separate record) overlaps on natural-language interaction but is config-/policy-focused rather than telemetry-analytics-focused.
- maturity_flag: GA (core NL/MCP querying on BIG-IP); AI Data Fabric enrichment = Beta/Early Access (limited availability, requires data sharing)
- source_currency_flag: Current
- source: f5.com/products/f5-insight; f5.com blog "From dashboard fatigue to operational excellence" (Mar 26 2026); Network World (Mar 11 2026)

### [OBS] Anomaly detection and proactive alerting (F5 Insight)
- solution_area: Observability & Insight
- capability_name: Real-time anomaly detection and actionable alerting
- plain_description: Continuously watches BIG-IP traffic and performance for abnormal behavior (e.g., connection-count deviations, error-rate spikes) and raises context-rich alerts so teams can act before users are affected.
- delivered_by: F5 Insight for ADSP
- attribution_confidence: High
- customer_problem_solved: Issues are discovered reactively (via user complaints) rather than proactively; static thresholds miss emerging problems.
- fit_signals: "We find out about problems when customers call." "We want to catch degradations before they become outages." "Our thresholds are all manual and always wrong." A history of preventable outages; MTTR is a tracked KPI the team is under pressure to improve.
- disqualifiers: No BIG-IP footprint. Customer's existing APM already does robust anomaly detection on this traffic and there is no gap.
- value_framing: "Spot abnormal traffic and performance changes fast, with alerts that tell your team where to start investigating — cut downtime and protect the digital experience."
- product_routing_note: Insight-specific. For outside-in (synthetic) early warning of user-facing issues, pair with XC Synthetic Monitoring (separate record).
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/f5-insight

### [OBS] Natural-language operations assistant across F5 consoles (F5 AI Assistant)
- solution_area: Observability & Insight
- capability_name: Platform AI assistant (BIG-IP iRules, NGINX One, Distributed Cloud)
- plain_description: A single natural-language assistant embedded across F5 product consoles that explains/generates/optimizes configuration (notably BIG-IP iRules), summarizes security events, and answers "how do I / what does this do" questions using F5-trained models.
- delivered_by: F5 AI Assistant — surfaced in BIG-IP (iRules code generation), F5 NGINX One (config guidance), and F5 Distributed Cloud Services (log/security-event querying); powered by F5 AI Data Fabric
- attribution_confidence: High
- customer_problem_solved: Deep F5 product expertise is scarce and slow to build; engineers waste time digging through docs and hand-writing complex config/iRules. Per F5's July 15, 2025 announcement, "Over 85% of BIG-IP customers rely on iRules, which power 70% of all BIG-IP instances globally" — and those scripts often outlive the engineers who wrote them.
- fit_signals: "Only one person here understands our iRules." "Onboarding a new BIG-IP admin takes months." "We spend hours in documentation." "Can it help us write/understand iRules?" SecOps drowning in XC WAAP events wanting to query them conversationally; iRules authored by staff who have since left the company.
- disqualifiers: This is an operational aid, not an observability platform — do not position it as the answer to "we need monitoring." Customers barred from LLM-assisted workflows.
- value_framing: "Make every engineer an expert — explain, generate, and optimize F5 config in plain English, with F5-validated outputs that never leave to third-party AI tools."
- product_routing_note: Cross-reference the per-product docs for depth (BIG-IP doc for iRules code generation; docs 05/10 for NGINX One assistant; XC/security docs for the Distributed Cloud assistant). Consolidated here because it is adjacent to, not the core of, observability. Distinct from the Insight AI assistant, which is telemetry-analytics-focused.
- maturity_flag: GA (XC assistant rolled out Dec 2024; NGINX One assistant 2025; BIG-IP iRules code generation previewed at AppWorld 2025 in February and made available July 15, 2025)
- source_currency_flag: Current
- source: f5.com/products/ai-assistant; f5.com blog "F5 AI Assistant Expands with iRules Code Generation" (Jul 15 2025); DevCentral "Introducing AI Assistant for F5 Distributed Cloud, NGINX One and BIG-IP"

### [OBS] Synthetic (outside-in) monitoring of apps and endpoints
- solution_area: Observability & Insight
- capability_name: F5 Distributed Cloud Synthetic Monitoring
- plain_description: Simulates user traffic against HTTP(S) and DNS endpoints from global regions to measure uptime, performance, and health, and to generate daily TLS reports/scores — independent of the data plane serving the app.
- delivered_by: F5 Distributed Cloud Synthetic Monitoring (part of the XC Observability service)
- attribution_confidence: High
- customer_problem_solved: No unbiased, geography-aware picture of the external digital experience; teams learn about regional outages/SLA breaches from customers.
- fit_signals: "We don't know how our app performs from other regions." "We need to prove our provider is meeting SLA." "We want to know the blast radius of an outage." "Detect issues before users call in." Global/consumer-facing apps; third-party/SaaS dependency SLA validation; certificate-expiry surprises.
- disqualifiers: Customer wants deep inside-out APM (code-level traces, DB spans) — synthetic monitoring is outside-in only. Customer has no XC footprint and no interest in XC. Internal-only apps not reachable from XC regions.
- value_framing: "See your app the way users in every region do — catch outages, SLA breaches, and TLS problems before your customers do, and quantify the blast radius."
- product_routing_note: XC-delivered and SaaS. Complementary to Insight (inside-out BIG-IP view) — the two answer different questions (external experience vs. internal F5 telemetry). Lead with Synthetic Monitoring when the pain is user-facing/global; lead with Insight when the pain is "what is my BIG-IP doing."
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/synthetic-monitoring; docs.cloud.f5.com/docs-v2/observability

### [OBS] NGINX fleet visibility and monitoring (NGINX One Console)
- solution_area: Observability & Insight
- capability_name: NGINX One Console fleet visibility
- plain_description: A SaaS console giving a single view of all NGINX instances (OSS and Plus) across environments — inventory, health/performance metrics, config, certificate status, and CVE/vulnerability flags — with metrics collected via an embedded OpenTelemetry collector in the NGINX Agent.
- delivered_by: F5 NGINX One (NGINX One Console)
- attribution_confidence: High
- customer_problem_solved: NGINX sprawl — teams don't know how many instances they run, which are vulnerable, or which certs are expiring; no unified NGINX observability.
- fit_signals: "We have NGINX everywhere and no inventory." "We don't know which NGINX instances are out of date or vulnerable." "We can't see our NGINX fleet in one place." Platform/DevOps teams standardizing NGINX at scale; audit/compliance drivers (PCI/GDPR) needing config and cert visibility.
- disqualifiers: Deep NGINX One content belongs in sibling docs 05/10 — do not position full NGINX One capability here. Customer with a single NGINX instance. AI-agent/MCP traffic observability in NGINX belongs to doc 11, not here.
- value_framing: "One console for every NGINX instance — see health, vulnerabilities, and certs across the whole fleet, and export telemetry to your existing observability backend via OpenTelemetry."
- product_routing_note: Summarized here only for its observability facet; route detailed NGINX One opportunities to docs 05/10. Metrics can be exported to Prometheus/Splunk/OTel backends, so it coexists with third-party observability rather than replacing it.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/nginx/one-console; docs.nginx.com/nginx-one-console; f5.com blog "How F5 NGINX One Enhances Management and Observability"

### [OBS] Export BIG-IP telemetry to third-party observability tools (Telemetry Streaming)
- solution_area: Observability & Insight
- capability_name: BIG-IP Telemetry Streaming (TS) to third-party analytics
- plain_description: A BIG-IP extension (configured declaratively via AS3/TS) that streams system, LTM, and WAF/ASM telemetry to external analytics platforms such as Datadog, Splunk, Elastic, and Dynatrace.
- delivered_by: F5 BIG-IP Telemetry Streaming (TS); also SNMP-based collection via vendor integrations
- attribution_confidence: High
- customer_problem_solved: Customers with an established observability platform want BIG-IP data *in that platform*, not in yet another F5 tool.
- fit_signals: "We already standardized on Datadog/Splunk — just get F5 data into it." "Our SOC lives in Splunk." "We don't want another single pane of glass." Mandate to consolidate on one observability platform; existing SIEM/APM investment the team won't abandon.
- disqualifiers: Customer wants F5-curated dashboards/analytics and expertise baked in (that's Insight, not TS). Customer wants natural-language/AI narratives (TS is raw streaming only).
- value_framing: "Keep the tools you love — stream BIG-IP telemetry straight into Datadog, Splunk, Elastic, or Dynatrace, so consolidating on F5 never means losing visibility."
- product_routing_note: This is the honest answer to the "we already have Datadog, why another tool?" objection. Lead with TS (coexistence) when the customer is committed to a third-party platform; lead with Insight when they want F5-specific curated analytics the general tools don't provide. The two are not mutually exclusive.
- maturity_flag: GA (long-standing)
- source_currency_flag: Current
- source: clouddocs.f5.com/products/extensions/f5-telemetry-streaming; DevCentral "Visualizing Metrics with F5 Telemetry Streaming and Datadog"; docs.datadoghq.com/integrations/snmp-f5

### [OBS] Cross-product data enrichment and intelligence (AI Data Fabric)
- solution_area: Observability & Insight
- capability_name: F5 AI Data Fabric (cross-customer/cross-product intelligence)
- plain_description: F5's internal data platform (introduced 2024) that aggregates data across F5 products and applies models to enrich them with contextual, cross-customer insights — the substrate that powers F5's AI assistants and, optionally, Insight's app discovery/health scoring.
- delivered_by: F5 AI Data Fabric (underpins F5 AI Assistant and F5 Insight enrichment); heritage includes the Threat Stack (2022) and Fletch (June 2025) acquisitions
- attribution_confidence: Medium (it is infrastructure behind products, not a standalone SKU customers buy; attribution of specific end-user features to AIDF vs. the product surface is sometimes blurred in F5 messaging)
- customer_problem_solved: Individual telemetry lacks context; cross-customer/threat-intel enrichment and automated app classification improve prioritization.
- fit_signals: Rarely a customer-led ask. Surfaces indirectly when a customer wants automatic app discovery/classification or health/security scoring, or asks "how does your AI know what good looks like?"
- disqualifiers: Not something to sell directly. Customers with strict data-sharing/residency limits (AIDF enrichment requires sharing data with F5 and is limited availability).
- value_framing: "F5's AI Data Fabric continuously enriches your telemetry with cross-customer context, so you get better guidance — not just more data."
- product_routing_note: Position as an enabler behind Insight and the AI Assistant, not as a product to route to on its own. Heritage context for customer questions: F5 acquired agentic-AI security startup Fletch (San Francisco, founded 2020, ~15 employees, led by CEO Grant Wernick) around June 5, 2025; F5's Chris Ford said "The Fletch technology will help accelerate our security analytics story with agentic AI," integrated into the AI Data Fabric.
- maturity_flag: GA as internal platform; customer-facing enrichment via Insight = Beta/Early Access (limited availability)
- source_currency_flag: Current
- source: f5.com blog "How F5 Is Unlocking the Power of AI"; f5.com/products/f5-insight (AI Data Fabric limited-availability note); Dark Reading / Network World on Fletch acquisition

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Start from the customer's existing F5 footprint — this solution area is almost always an attach motion.**

- **Customer owns BIG-IP (on-prem or VE), wants to see/prove/troubleshoot it →** Lead with **F5 Insight for ADSP**. It is BIG-IP-anchored, GA, and self-managed today. Confirm they can run a VM (≈8 vCPU / 16 GB RAM / ~500 GB) and reach BIG-IP over iControl REST. If they are not ready to license/deploy a supported product, point them to the community **Application Study Tool (AST)** as an unsupported on-ramp.
- **Customer is committed to a third-party observability/SIEM platform (Datadog, Splunk, Elastic, Dynatrace) →** Lead with **BIG-IP Telemetry Streaming (TS)** for coexistence. Do not fight the incumbent platform. Introduce Insight only as an additive, F5-curated layer for BIG-IP-specific analytics the general tool doesn't provide.
- **Customer's pain is user-facing/global experience, SLA validation, or "detect before users call" →** Lead with **F5 Distributed Cloud Synthetic Monitoring** (SaaS, outside-in). Best when they have or will adopt XC.
- **Customer runs sprawling NGINX (OSS/Plus) →** Route to **NGINX One Console** for fleet visibility, but hand off deep NGINX One scoping to sibling docs 05/10. For AI-agent/MCP traffic observability in NGINX, route to doc 11.
- **Buyer persona cues:** NetOps/ITOps and application owners → Insight (BIG-IP). SRE/DevOps/platform teams committed to their own stack → TS + coexistence, or NGINX One. SecOps → note that security event visibility often lives in the security products (SIEM export handled in the security docs, not here).

**Delivery-model routing:**
- On-prem / self-managed / air-gapped preference → **Insight self-managed** (supports connected and disconnected/air-gapped licensing modes).
- SaaS preference for BIG-IP observability → **not available yet** (Insight SaaS is forthcoming). Set expectations honestly; do not promise a date.
- SaaS-native, cloud/edge → **XC Synthetic Monitoring** and **NGINX One Console** are already SaaS.

**Coexistence / migration notes:**
- Insight and third-party APM/SIEM are **complementary**, not either/or: Insight for F5-curated BIG-IP analytics + TS to feed the customer's platform.
- **Insight vs. AST:** Insight is the productized, supported evolution of the community AST open-source stack; AST uses Prometheus while Insight uses VictoriaMetrics (plus ClickHouse for storage internally) and adds licensing, HA/enterprise SLAs, an AI assistant, and (limited-availability) AI Data Fabric enrichment. There is an AST→Insight migration guide in the Insight docs.
- Where the public record does not clearly support a routing recommendation (e.g., exact Insight packaging/pricing, or NGINX/XC coverage timelines), say so rather than inventing official F5 guidance.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **No F5 data-plane footprint.** Insight is BIG-IP-anchored; NGINX/XC coverage is roadmap. Greenfield prospects with no BIG-IP/NGINX/XC get little from this area today — weak fit / too early.
- **"Replace our observability stack" as the primary ask.** F5's own position is complement-not-replace. If the customer wants a general APM/observability platform, this is the wrong solution area.
- **Single-pane-of-glass mandate already standardized on another platform.** If they've mandated Datadog/Splunk/Grafana as *the* pane of glass, lead with TS coexistence, not Insight-as-replacement; positioning Insight as "another single pane of glass" will lose (F5's own marketing explicitly says "you don't need another single pane of glass").
- **Observability pitched as the lead deal-maker.** It is an attach/expansion or objection-neutralizer. If it's the whole pitch, the deal is thin.
- **Hard prohibition on LLM/data-sharing.** Insight's AI narratives use MCP/LLM integration, and AI Data Fabric enrichment requires sharing data with F5 (limited availability). Strict data-residency shops should scope to the non-AI dashboards/TS only.
- **SaaS-first requirement for BIG-IP observability.** Insight SaaS has not shipped. Don't commit to a timeline.
- **Wrong sibling scope.** Deep NGINX One (docs 05/10), NGINX AI-agent/MCP traffic observability (doc 11), and SIEM export from security products (security docs) are out of scope here — don't over-claim them.

### 3c. Competitive positioning and objection handling (bounded — all lower confidence)

**Note:** F5 does not primarily compete head-to-head in the general observability market. The named vendors below appear as *incumbents the customer already owns*, not as products F5 displaces. All competitive claims are lower-confidence and reflect F5's *stated* angle.

- **General observability / APM (Datadog, New Relic) — positioned as COMPLEMENTS.** F5's public, stated differentiator: general APM tools don't cover app-delivery-specific telemetry from the F5 data plane, and F5 says demand for Insight came directly from customers running Datadog/New Relic who "needed something different." F5 SVP/GM Shawn Wormke told Network World (Mar 11 2026): *"At this point, we've had over 400 customers who were demoing and using and giving feedback on the product"* — vendor-stated, not independently audited. (Lower confidence: this is F5's framing, not an independent benchmark.) *Verify independence:* Datadog and New Relic remain independent observability vendors as of 2026.
- **Grafana — partly F5's own substrate.** Insight ships curated **Grafana** dashboards on an open-source stack, so "Grafana" is often not a competitor but a shared component. Differentiator: F5 pre-builds and curates the dashboards with 30 years of F5 expertise vs. a customer building their own.
- **Splunk / SIEM — complement, not compete.** F5's stated position (DevCentral, "Introducing F5 Insight for ADSP") is verbatim: *"F5 Insight is not intended to replace SIEM solutions like Splunk or Sentinel but serves a different, complementary purpose."* BIG-IP data can be streamed into Splunk via TS. SIEM export from F5 *security* products is covered in the security docs, not here.

**The core objection — "We already have Datadog (or Splunk/New Relic). Why another tool?"**
Best response, in order:
1. **Agree and coexist.** "You shouldn't rip that out. We can stream BIG-IP telemetry straight into Datadog via Telemetry Streaming so you keep your single pane of glass." (This is the honest, credible opener.)
2. **Name the gap.** "General APM tools don't surface app-delivery-specific BIG-IP telemetry — iRules usage, virtual-server/pool health, SSL/handshake metrics, WAF posture — the way an F5-built tool does. That's exactly the gap customers running Datadog and New Relic told us they had." (F5's stated angle.)
3. **Value, not overlap.** "Insight is curated by F5 with recommendations and operational narratives specific to BIG-IP — it makes your F5 estate a proven asset and helps you right-size and prove ROI, alongside your existing platform, not instead of it."
4. **Don't oversell.** If the customer is fully satisfied with their BIG-IP visibility in the incumbent tool, concede it's a weak fit and pivot — observability is an attach motion, not a forced sale.

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify on every deal):**
- **"F5 Insight" vs. "F5 Insight for ADSP"** — same product; F5 uses both. The full name is "F5 Insight for ADSP"; it is a component of the "XOps" pillar of the F5 Application Delivery and Security Platform (ADSP).
- **SaaS status** — as of July 2026 the SaaS model is **forthcoming/planned, NOT shipped**. Only self-managed software is GA. Do not assert a SaaS availability date.
- **Data-plane coverage** — Insight is **BIG-IP only** today; **NGINX and Distributed Cloud coverage are roadmap/announced**, not GA. Capture per-data-plane maturity precisely on every call.
- **Threat Stack → Distributed Cloud AIP → RETIRED.** Threat Stack (acquired 2022) became **F5 Distributed Cloud App Infrastructure Protection (AIP)**, sometimes marketed as "Advanced Infrastructure Protection." **The AIP service was retired effective August 13, 2024** (per F5 Distributed Cloud technical docs). If a customer asks "what happened to Threat Stack / AIP," the answer is: absorbed into F5 Distributed Cloud, then retired in Aug 2024; its heritage/technology (with Fletch) now feeds F5's AI Data Fabric and the security-analytics story behind Insight. AIP is NOT a current sellable product.
- **F5 AI Assistant** vs. **Insight's built-in AI assistant** — two related but distinct things. The platform AI Assistant is config/policy/log-query focused across BIG-IP/NGINX/XC; Insight's assistant is telemetry-analytics focused on BIG-IP. Don't conflate.
- **Application Study Tool (AST)** — community/open-source predecessor of Insight; unsupported by F5. Insight is the supported product evolution.
- **BIG-IP version anchor** — Insight v1.1 (May 2026) documents BIG-IP **17.5.x** with LTM required and iControl REST enabled. **v1.2 was announced July 15, 2026**, adding fleet-management workflows for BIG-IP devices (fleet-wide software-lifecycle visibility, guided update workflows, role-based access controls, and a tamper-evident AI audit trail). Versioning is roughly monthly — treat specifics as perishable.

**Explicitly NOT verified (do not assert):**
- Insight **pricing, subscription tier, or whether it is free/included vs. tied to a BIG-IP support contract** — not found in public sources. Licensing is enforced via an F5 entitlement (storage-GB cap + expiry date; "eval" and "paid" entitlement types appear in the docs), but the commercial model is not public. Say "contact F5 / see buying options."
- A firm **SaaS ship date** or **NGINX/XC coverage date** for Insight — not published.
- Exact contents of the Insight datasheet/solution-overview PDFs — the CDN blocked automated retrieval; claims here are drawn from the F5 product page, blog, press release, and clouddocs.
- The **~400-customer preview** figure is F5 executive commentary (Shawn Wormke to Network World) — treat as vendor-stated, not independently audited.

**Primary sources leaned on:** f5.com/products/f5-insight; f5.com/products/ai-assistant; f5.com/products/nginx/one-console; f5.com/products/distributed-cloud-services/synthetic-monitoring; f5.com press release "F5 Strengthens Its ADSP…" (Mar 11 2026); f5.com blogs (Insight six questions; dashboard fatigue/XOps; F5 AI Assistant iRules code generation Jul 15 2025; Unlocking the Power of AI); clouddocs.f5.com/products/insight (incl. release notes v1.1, licensing/entitlements, deployment guides); clouddocs telemetry-streaming; docs.cloud.f5.com Observability/Synthetic Monitoring & AIP-retired notice; docs.nginx.com/nginx-one-console; DevCentral (Introducing F5 Insight for ADSP; AI Assistant; Application Study Tool; TS+Datadog/Dynatrace).
**Third-party sources (competitive/reality-check):** Network World (Mar 11 2026 ADSP coverage; Fletch acquisition); SiliconANGLE; CRN; Investing.com; Dark Reading (Fletch); Help Net Security (iRules code generation; Insight v1.2); G2 / TrustRadius (AIP status); docs.datadoghq.com (F5 SNMP/TS integration).