# F5 Web Application Protection (WAF / WAAP) — Solution Area Reference (Doc 02)

doc_id: 02-web-app-protection
solution_area: Web Application Protection (WAF / WAAP)
doc_tag: WAF
products_covered: F5 Distributed Cloud WAF/WAAP (SaaS), F5 BIG-IP Advanced WAF (appliance/VE, ASM heritage), F5 WAF for NGINX (formerly NGINX App Protect WAF), F5 Distributed Cloud Web App Scanning
compiled: July 2026
primary_release_anchor: AppWorld 2026 (March 2026) + June 2026 WAAP expansion (AI-powered WAF risk scoring GA in Distributed Cloud release 2025.10.0)
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

This document covers F5's web application firewall (WAF) / web application and API protection (WAAP) story: protecting web apps against OWASP Top 10 attacks (injection, XSS, etc.), using attack signatures, behavioral/ML detection, virtual patching, and vulnerability scanning. This is the broadest and most commoditized F5 solution area — the value here is correct product routing and honest differentiation, not re-explaining what a WAF is.

F5 delivers WAF through one shared detection engine exposed via three delivery vehicles, plus a scanner:

- **F5 Distributed Cloud WAF / WAAP (SaaS)** — cloud-delivered WAF as a service, F5-operated global network, self-managed or fully managed. Carries the new AI-powered risk scoring capability.
- **F5 BIG-IP Advanced WAF (appliance / Virtual Edition)** — the on-prem/data-center incumbent, evolved from ASM. Deepest feature set, runs on classic BIG-IP TMOS.
- **F5 WAF for NGINX (formerly NGINX App Protect WAF)** — lightweight, declarative WAF that runs natively inside NGINX Plus / NGINX Ingress Controller; for DevOps / Kubernetes / CI/CD.
- **F5 Distributed Cloud Web App Scanning** — SaaS DAST + external attack surface management (Heyhack acquisition); feeds virtual-patch findings into BIG-IP Advanced WAF.

Key naming and lifecycle facts an SE must not get wrong (2026):
- NGINX App Protect WAF → **F5 WAF for NGINX** (rename mid-2025); now part of NGINX One.
- ASM → **BIG-IP Advanced WAF** (ASM End of Sale April 1, 2021).
- **Silverline is dead** — per F5 KB K000150427: "F5 announced the End of Life (EoL) of the Silverline platform, effective June 30, 2025… Distributed Cloud Platform – the designated replacement." (End-of-Sale emails went out March 2024, End-of-Life notice August 2024.)
- **BIG-IP Next is being discontinued** — F5 announced in August 2025 (KB K000152956, "Modernizing BIG-IP TMOS and discontinuing BIG-IP Next") it is modernizing classic BIG-IP TMOS and discontinuing BIG-IP Next as a general ADC/WAF platform. Do NOT pitch BIG-IP Next WAF as the future; classic BIG-IP (v17.1 minimum, v21.x newest) is the recommended platform.

Read Layer 2 for capability records (each self-contained), then Layer 3 for routing, disqualifiers, and competitive positioning.

## Layer 2 — Capability catalog

### [WAF] OWASP Top 10 signature-based protection
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: OWASP Top 10 / signature-based attack protection
- plain_description: Inspects HTTP/S requests and blocks classic web attacks (SQL injection, cross-site scripting, command injection, path traversal) by matching them against a large library of attack signatures.
- delivered_by: F5 Distributed Cloud WAF/WAAP, F5 BIG-IP Advanced WAF, F5 WAF for NGINX
- attribution_confidence: High
- customer_problem_solved: Baseline protection of web apps against the most common, high-volume exploit classes and a check-box for PCI DSS and similar compliance mandates.
- fit_signals: "We need a WAF in front of these apps for PCI." "We keep seeing SQLi/XSS attempts in our logs." "Audit flagged we have no WAF on this internet-facing app." "We got popped by Log4Shell / MOVEit and need faster coverage." Buyers may not know the term WAF — they describe "blocking hackers from our website" or "the security box in front of the app."
- disqualifiers: Purely internal apps with no untrusted traffic and compensating controls; teams who only need L3/L4 network firewalling (not app-layer); a shop fully satisfied with an existing CDN WAF and with no multi-environment consistency need.
- value_framing: All three F5 WAF engines share the same detection core and signature set, so you get consistent OWASP coverage whether the app is on-prem, in a container, or behind SaaS — one policy language, one efficacy story, across every environment.
- product_routing_note: Data center / existing BIG-IP → Advanced WAF. Kubernetes / NGINX / DevOps → F5 WAF for NGINX. No infrastructure / want SaaS → Distributed Cloud WAF.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com BIG-IP Advanced WAF page; docs.nginx.com F5 WAF for NGINX overview; f5.com Distributed Cloud WAF page

### [WAF] Shared WAF engine across delivery models
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: Common WAF engine / signature set across three products
- plain_description: F5's Distributed Cloud WAF, BIG-IP Advanced WAF, and F5 WAF for NGINX are built on the same core WAF engine and signature technology, so detection behavior is broadly consistent across them.
- delivered_by: F5 Distributed Cloud WAF/WAAP, F5 BIG-IP Advanced WAF, F5 WAF for NGINX
- attribution_confidence: High
- customer_problem_solved: Inconsistent security posture and duplicated tuning effort when different app environments use different WAF vendors/engines.
- fit_signals: "Our cloud team uses one WAF, the data-center team uses another, and policies don't match." "We can't prove consistent protection across all our apps to auditors." "Every WAF migration means re-tuning from scratch."
- disqualifiers: A single-environment shop with one app footprint and no consistency pain; customers who only ever want the SaaS and will never touch the other form factors.
- value_framing: One engine, many form factors — author a policy once and enforce it at the edge, in the data center, or inside Kubernetes. Competing edge/CDN WAFs cannot follow your app on-prem or into a container the way F5 can.
- product_routing_note: Lead with whichever form factor matches the biggest slice of the customer's footprint; emphasize engine commonality when they span environments. Note the engines are NOT identical in features/operations — see the differences record.
- maturity_flag: GA
- source_currency_flag: Current
- source: DevCentral "F5 Distributed Cloud WAAP – Introducing the Distributed Cloud Web Application Firewall" (states XC WAAP shares its WAF engine with BIG-IP Advanced WAF and NGINX App Protect)

### [WAF] Engine differences between the three WAF products
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: What differs (not just what's shared) across the three engines
- plain_description: Although the three products share a detection core, they differ in policy model, management, form factor, and which advanced features are present — SEs must not assume feature parity.
- delivered_by: F5 Distributed Cloud WAF/WAAP, F5 BIG-IP Advanced WAF, F5 WAF for NGINX
- attribution_confidence: Medium
- customer_problem_solved: Prevents mis-scoping deals by clarifying that "same engine" does not mean "same product."
- fit_signals: "Can NGINX App Protect do the app-layer encryption our BIG-IP does?" "Is the SaaS WAF the same as our data-center WAF?" "We want the AI risk scoring on our on-prem BIG-IP."
- disqualifiers: Simple single-product deals where cross-product parity is not in question.
- value_framing: Position each product to its native strengths rather than promising identical features. Distributed Cloud WAF: SaaS operations, F5-run global network, AI risk scoring (GA today only here). BIG-IP Advanced WAF: deepest feature set (DataSafe application-layer encryption, behavioral L7 DoS, session-aware brute-force, XML/SOAP security), managed via TMOS GUI/declarative policy. F5 WAF for NGINX: declarative JSON policy compiled into a bundle, "over 7,500 advanced signatures, bot signatures and threat campaign protection" (f5.com, v5.9), runs natively in NGINX, lightweight/CI-CD-friendly, uses Violation Rating for blocking. Concrete differences: XML/binary WAF policy formats are a classic BIG-IP construct; F5 WAF for NGINX uses JSON declarative policy with Default and Strict reference policies; the AI-powered risk scoring is currently delivered only through Distributed Cloud — per Network World (June 2026), "The AI-powered WAF is currently delivered through Distributed Cloud. F5 said it is in active engineering work to bring the same capability to BIG-IP, Nginx Plus, and Nginx Open Source."
- product_routing_note: If a customer wants a capability that lives in only one engine (e.g., AI risk scoring, DataSafe), route to that product and flag the gap in others.
- maturity_flag: GA (base engines); AI risk scoring on BIG-IP/NGINX is Roadmap/Announced
- source_currency_flag: Current
- source: docs.nginx.com (declarative policy, Default/Strict, 7,500+ signatures, v5.9); f5.com Advanced WAF page (DataSafe, L7 DoS); Network World June 2026 (AI WAF "in active engineering work to bring the same capability to BIG-IP, Nginx Plus, and Nginx Open Source")

### [WAF] AI-powered risk scoring / outcome-based blocking
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: AI-powered WAF risk scoring (High/Medium/Low, block-by-score)
- plain_description: Instead of tuning hundreds/thousands of individual signatures, the WAF assigns each request a contextual risk score (High/Medium/Low) from multiple signals — signatures, attack indicators, and a continuously trained neural-network/ML model — and teams block based on the score.
- delivered_by: F5 Distributed Cloud WAF/WAAP (only, as GA today)
- attribution_confidence: High
- customer_problem_solved: Alert fatigue and slow time-to-blocking-mode caused by heavy manual signature tuning and false positives; catches novel/pre-signature attack patterns. As Kunal Anand, F5 Chief Product Officer, framed it (June 9, 2026): "Frontier AI has collapsed the window between discovery and exploitation. Attackers no longer need a CVE. They need a model and a target. We built a risk engine that learns continuously and scores every request dynamically, catching attack patterns before a signature exists to stop them."
- fit_signals: "We're stuck in monitor mode because we're scared of false positives." "My SecOps team drowns in WAF alerts." "Tuning the WAF takes weeks per app." "We got hit by an exploit before a signature existed." "We have hundreds of apps and can't tune them one by one."
- disqualifiers: Customers with a single app and a hand-tuned policy they're happy with; air-gapped/on-prem-only customers who cannot use the SaaS (AI WAF not yet GA on BIG-IP/NGINX); those who require full explainability of every block decision.
- value_framing: Move from configuration-heavy signature tuning to outcome-based enforcement — get to blocking mode sooner with fewer false positives. Joel Moses, F5 VP of strategic engineering, told Network World (June 2026) that "F5's false positive rate dropped from approximately 18% to approximately 1%." In SecureIQLab testing cited in F5's June 9, 2026 release, "F5 WAAP and F5 AI Guardrails achieved a 97.09% total security score, including 100% accuracy against key risks listed in the OWASP WAF Top 10 and API Top 10, as well as perfect scores for bot attack mitigation and Layer 7 DoS protection." (Both the FP figures and the lab score are F5-supplied / vendor-commissioned — cite as F5's claim, not independent fact.)
- product_routing_note: Lead with Distributed Cloud WAF for this. If the customer is committed to on-prem BIG-IP or NGINX, set expectations: capability is announced/in-engineering for those, not GA.
- maturity_flag: GA (Distributed Cloud, since release 2025.10.0 / March 2026; free 6-month trial through September 30, 2026). Roadmap/Announced for BIG-IP and NGINX.
- source_currency_flag: Current
- source: docs.cloud.f5.com "AI Powered Risk Scoring"; DevCentral "F5 Distributed Cloud AI-Powered WAF: From Signature Tuning to Outcomes"; F5 blog "Securing web apps without complexity"; Network World (June 2026); businesswire AppWorld release (March 11, 2026) and June 9, 2026 WAAP release

### [WAF] Behavioral / ML threat detection and malicious user detection
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: Behavioral protection and malicious-user ranking
- plain_description: Beyond signatures, the WAF profiles client behavior to identify and rank suspicious/malicious users and take action even when no known signature is triggered.
- delivered_by: F5 Distributed Cloud WAF/WAAP, F5 BIG-IP Advanced WAF, F5 WAF for NGINX (behavioral L7 DoS / adaptive learning)
- attribution_confidence: Medium
- customer_problem_solved: Zero-day and evasive attacks that don't match a signature; distinguishing genuinely bad actors from benign anomalies.
- fit_signals: "Signatures alone keep missing things." "We want to catch bad actors before there's a CVE." "We need to spot abuse patterns, not just single-request attacks."
- disqualifiers: Customers who only want a basic signature WAF for compliance and won't operationalize behavioral findings. (Note: full bot defense / fraud is doc 03, not here.)
- value_framing: Combine signatures with behavioral tracking so you catch clients that never trip a known signature — reducing reliance on perfect signature tuning.
- product_routing_note: Behavioral L7 DoS depth is strongest on BIG-IP Advanced WAF and F5 WAF for NGINX (ML-based L7 DoS); malicious-user detection is a Distributed Cloud WAAP feature. Keep bot/fraud specifics in doc 03.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com Distributed Cloud WAF page (signature + behavioral); WWT WAAP article (malicious user detection); f5.com F5 WAF for NGINX (behavioral L7 DoS ML)

### [WAF] Virtual patching via scanner integration
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: Virtual patching (Web App Scanning → BIG-IP Advanced WAF)
- plain_description: Vulnerabilities found by F5 Distributed Cloud Web App Scanning can be exported to BIG-IP Advanced WAF, which applies a targeted virtual patch at the delivery layer to protect the app at runtime while the real code fix works through dev/test.
- delivered_by: F5 BIG-IP Advanced WAF (enforcement) + F5 Distributed Cloud Web App Scanning (findings)
- attribution_confidence: High
- customer_problem_solved: The shrinking window between vulnerability discovery and exploitation — buys time to remediate code without leaving the app exposed.
- fit_signals: "We can't patch fast enough to keep up with disclosures." "Our patch cycle takes weeks but exploits land in hours." "We need a stopgap for a critical CVE until dev ships a fix." "Legacy app we can't easily modify but must protect."
- disqualifiers: Customers with no vulnerability-scanning practice and no intent to start; those who won't run BIG-IP Advanced WAF as the enforcement point; teams who treat virtual patching as a permanent substitute for fixing code (F5's own spokesperson positioned it as "a tool in your arsenal," not a substitute for fixing the underlying code).
- value_framing: Close the gap from "found" to "protected" — scan finds it, Advanced WAF patches it virtually at runtime, dev fixes the code on its own schedule. Uses the Vulnerability Assessment Policy Template; findings import as suggested policy updates and you can re-scan to validate.
- product_routing_note: This specific automated workflow is anchored on BIG-IP Advanced WAF + Web App Scanning. Do not attribute the same automated import/patch flow to NGINX or Distributed Cloud WAF without verification.
- maturity_flag: GA (integration demonstrated); "enhanced" virtual patching positioned in June 2026 WAAP expansion
- source_currency_flag: Current
- source: DevCentral "F5 BIG-IP Virtual Patching With Web App Scanning Results"; F5 press release June 9, 2026; Network World June 2026

### [WAF] External attack surface management + DAST (Web App Scanning)
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: F5 Distributed Cloud Web App Scanning (Recon + Scan)
- plain_description: A SaaS service that continuously discovers your internet-facing apps/APIs (Recon / external attack surface management) and runs automated penetration testing / dynamic application security testing (Scan / DAST) to find vulnerabilities, with remediation guidance.
- delivered_by: F5 Distributed Cloud Web App Scanning
- attribution_confidence: High
- customer_problem_solved: Unknown/shadow internet-facing assets and undiscovered vulnerabilities; the manual toil of continuous scanning; compliance evidence.
- fit_signals: "We don't know everything we have exposed on the internet." "We need pen-test-style coverage but can't run manual pen tests continuously." "Compliance wants regular vulnerability assessments (SOC 2 / ISO 27001 / PCI)." "We're standing up LLM/AI apps and need to test them for OWASP LLM risks."
- disqualifiers: Customers who only want inline blocking and have a separate mature DAST/EASM tool they're committed to; purely internal apps with no external surface.
- value_framing: Discover what you're exposing and test it automatically — then feed findings straight into virtual patching. Heritage: F5 acquired Denmark-based Heyhack (founded 2022) on February 26, 2024, launching the capability as F5 Distributed Cloud Web App Scanning (announced March 11, 2024, then under EVP/Chief Product Officer Kara Sprague); on-prem scanner deployment via Docker exists for internal targets. Includes an LLM testing suite covering the OWASP Top 10 for LLMs.
- product_routing_note: Routing anchor for scanning + virtual patching. API-specific discovery/testing as an API story belongs to doc 01; keep this record focused on web-app scanning and the WAF virtual-patch tie-in.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com Web App Scanning page; docs.cloud.f5.com Web App Scanning Overview; DevCentral "Introducing F5 Distributed Cloud Web App Scanning"; globalsecuritymag / F5 press release (Heyhack acquisition)

### [WAF] Managed WAF service (post-Silverline)
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: Fully managed WAF delivered from F5 SOC
- plain_description: Customers can consume Distributed Cloud WAF/WAAP either self-managed or as a fully managed service deployed, tuned, and monitored 24x7 by certified F5 experts in F5's Security Operations Center.
- delivered_by: F5 Distributed Cloud WAF/WAAP (Managed Service)
- attribution_confidence: High
- customer_problem_solved: Lack of in-house WAF expertise / SecOps headcount; need for 24x7 coverage and ongoing policy tuning without hiring.
- fit_signals: "We don't have the staff to run and tune a WAF." "We need someone watching this 24x7." "We were a Silverline managed WAF customer — what now?" "We want to outsource day-to-day security operations."
- disqualifiers: Customers with a mature in-house SecOps team who want full control; those wanting a self-managed appliance only.
- value_framing: F5 runs it for you — configuration, ongoing policy management, tuning, and reporting, backed 24x7 by F5's SOC. This is the designated home for former Silverline Managed WAF customers.
- product_routing_note: For any customer mentioning Silverline, route to Distributed Cloud (WAAP offers comparable-or-better functionality). Silverline is End of Life (June 30, 2025) — do not propose it. BIG-IP and NGINX are customer-managed (or via partner MSPs), not F5-SOC-managed in the same way.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com Distributed Cloud Managed Services / SOC pages; f5.com Distributed Cloud WAF Managed Service datasheet; my.f5.com K000150427 (Silverline EoL); f5.com Silverline-to-Distributed-Cloud migration webinar

### [WAF] Threat campaigns and threat intelligence
- solution_area: Web Application Protection (WAF / WAAP)
- capability_name: Threat Campaigns / timely signature updates
- plain_description: F5 pushes curated "Threat Campaigns" and frequent signature updates based on F5 Labs research so the WAF recognizes active, real-world exploit campaigns with high confidence and low false positives.
- delivered_by: F5 Distributed Cloud WAF/WAAP, F5 BIG-IP Advanced WAF, F5 WAF for NGINX
- attribution_confidence: High
- customer_problem_solved: Keeping protection current against fast-moving campaigns without heavy in-house threat research.
- fit_signals: "How fast do you cover new CVEs like Log4Shell?" "We can't keep our rules current." "We want high-confidence blocking without a flood of false positives."
- disqualifiers: Customers who only need static baseline OWASP coverage and don't value curated intel.
- value_framing: F5 Labs-driven Threat Campaigns let you enable a default policy and get coverage for major vulnerabilities (e.g., Log4Shell, MOVEit) with minimal tuning.
- product_routing_note: Available across all three engines; lead with the customer's primary form factor.
- maturity_flag: GA
- source_currency_flag: Current
- source: DevCentral Distributed Cloud WAAP intro (Threat Campaigns, Log4Shell/MOVEit); f5.com F5 WAF for NGINX (threat campaign protection)

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

Route on the customer's dominant footprint and operating preference:

- **Existing BIG-IP / data-center / on-prem, appliance mindset →** BIG-IP Advanced WAF. Deepest feature set (DataSafe app-layer encryption, behavioral L7 DoS, XML/SOAP, session-aware brute-force). It is the enforcement point for the scanner-driven virtual patching workflow. Runs on classic BIG-IP TMOS — F5's recommended, actively developed platform (v17.1 min, v21.x newest).
- **Kubernetes / microservices / NGINX shops / DevSecOps / CI-CD →** F5 WAF for NGINX (formerly NGINX App Protect WAF). Declarative JSON policy, runs natively in NGINX Plus / NGINX Ingress Controller, part of NGINX One. Strong fit where the WAF must live in the data path as code. Especially relevant for customers rebuilding Kubernetes ingress after the community ingress-nginx end-of-life.
- **No infrastructure appetite / multicloud / want SaaS / want it managed →** Distributed Cloud WAF/WAAP. Only home (today, GA) for AI-powered risk scoring; available self-managed or F5-SOC-managed. Designated replacement for Silverline.
- **Vulnerability discovery + virtual patching →** Distributed Cloud Web App Scanning (findings) + BIG-IP Advanced WAF (enforcement).

**Coexistence / hybrid:** F5 publicly documents tiered hybrid architectures pairing Distributed Cloud WAF (edge) with BIG-IP Advanced WAF (data center), managed as code via a shared CI/CD pipeline — a legitimate "and," not "or," when a customer spans edge and data center.

**Migration notes (public sources only):**
- **ASM → Advanced WAF:** ASM End of Sale April 1, 2021; policies are functionally identical and eligible ASM customers (STANDALONE, ADD-ON, or BEST bundle, running v14.1+ with active support) can reactivate their license to upgrade to Advanced WAF at no cost.
- **Silverline → Distributed Cloud:** Silverline End of Life June 30, 2025; Distributed Cloud is the designated replacement; F5 provides migration support and an on-demand webinar.
- **BIG-IP Next:** F5 announced (August 2025, KB K000152956) it is modernizing BIG-IP TMOS and discontinuing BIG-IP Next as a general ADC/WAF platform; BIG-IP Next final version was 20.3 (reached end of life April 30, 2025 per F5 support-policy content). Do NOT position BIG-IP Next WAF as a forward platform. Classic BIG-IP TMOS is the recommended path, with F5 stating it "will ensure continuity of BIG-IP TMOS software with future releases" and continued investment in rSeries/VELOS hardware. (BIG-IP Next for Kubernetes and Cloud-Native Network Functions are separate and NOT discontinued.) The prior BIG-IP → BIG-IP Next WAF migration path (declarative JSON only; "WAF policies in XML or Binary formats are not currently supported on BIG-IP Next," per clouddocs; via BIG-IP Next Central Manager / JOURNEYS tool) is now largely moot for new deals.

### 3b. Disqualifiers / anti-patterns (aggregate)

Signals this solution area is a weak fit or "not now":
- **Purely internal apps, no untrusted traffic** — app-layer WAF value is low; may only need network controls.
- **Customer is fully satisfied with a single-environment CDN/cloud WAF and has no consistency, depth, or on-prem need** — F5's differentiation (multi-environment, depth, AI scoring, virtual patching) won't land; don't force it.
- **The real need is bot/fraud, DDoS, API-specific security, or AI/LLM guardrails** — those are doc 03, doc 04, doc 01, and doc 11 respectively. WAF may be adjacent but is not the lead.
- **No SecOps capacity and no interest in a managed service** — a self-managed appliance WAF will sit in monitor mode forever; steer to managed service or descope.
- **Air-gapped / on-prem-only customer demanding AI risk scoring today** — not GA off Distributed Cloud; set expectations.
- **Customer wants BIG-IP Next as their strategic platform** — it's being discontinued; reset to classic BIG-IP or another form factor.

### 3c. Competitive positioning and objection handling (all lower confidence)

All competitive claims below are lower-confidence and should be validated per-deal. Market consolidates fast; verify status.

**Edge/CDN WAAPs — Cloudflare, Akamai, Fastly (Fastly Next-Gen WAF = the former Signal Sciences, acquired 2020 for $775M, now fully integrated as NGWAF):** These are strong where the customer's priority is CDN + edge WAF in one and apps are already fronted by that CDN. F5's public differentiators: deployment flexibility across on-prem, data center, container, and multicloud (a CDN WAF generally cannot follow the app on-prem or into a pod), one shared engine/policy across environments, and depth (DataSafe, behavioral L7 DoS). Flag as lower confidence.

**Imperva — now owned by Thales (acquisition completed December 4, 2023).** Imperva is a credible enterprise/regulated-industry competitor with strong compliance features and (per third parties) near-zero-false-positive managed rules enabling day-one blocking mode. F5's counter: breadth of deployment models and the shared-engine consistency story. Verify current Thales/Imperva product branding per deal.

**Hyperscaler WAFs (AWS WAF, Azure WAF, Google Cloud Armor):** Cheap and native to one cloud, but weak for multicloud/on-prem consistency and generally shallower on advanced protections. F5's counter: single policy across every environment vs. per-cloud silos.

**Open source (ModSecurity / Coraza + OWASP Core Rule Set):** ModSecurity moved to OWASP stewardship (transfer January 2024) after Trustwave's commercial EoL (July 2024); Coraza is the Go-based successor. Note F5's own NGINX ModSecurity WAF went End of Sale April 1, 2022 and is EoL. F5's counter (per F5's own NGINX blog): F5 Labs-curated rules vs. generic CRS, precompiled bytecode performance vs. regex evaluation, and commercial support — relevant for teams that adopted ModSecurity on NGINX and now face its wind-down.

**The core objection — "our CDN / cloud provider WAF is good enough":** Acknowledge it, then reframe. Per F5's own channel guidance: caching needs shouldn't dictate security policy — many customers use a CDN for static caching while dynamic pages and APIs are protected separately, and F5 WAAP complements the existing CDN rather than replacing it. The strongest wedge is when the customer has apps beyond the CDN's reach (on-prem, other clouds, containers) and needs consistent policy and deeper protection everywhere, plus AI risk scoring to cut tuning/false positives.

## Appendix — Naming, currency & confidence ledger

**Perishable naming / lifecycle to watch:**
- NGINX App Protect WAF → **F5 WAF for NGINX** (rename ~mid-2025; v5.9 released September 2025); "F5 DoS for NGINX" is the DoS sibling; both part of NGINX One. Legacy name still widely used by customers.
- ASM → **BIG-IP Advanced WAF** (ASM EoS April 1, 2021).
- **Silverline** — End of Life June 30, 2025; replaced by Distributed Cloud. Do not sell.
- **BIG-IP Next** — discontinued as general ADC/WAF platform (announced Aug 2025, KB K000152956); classic BIG-IP TMOS is the path forward. BIG-IP Next for Kubernetes / CNF are separate and continue.
- XC / Distributed Cloud packaging — F5 introduced simplified starter packages "Essentials" and "Enterprise" (AppWorld 2026); a WAAP base bundle exists. Exact tier contents are perishable — verify at quote time.

**Explicitly NOT verified (do not assert):**
- Exact per-feature parity table between BIG-IP Next WAF and classic Advanced WAF (the clouddocs mapping table is JS-rendered and could not be captured verbatim beyond the "XML or Binary formats are not currently supported on BIG-IP Next" statement) — largely moot given Next discontinuation.
- Whether DataSafe / app-layer encryption, Anti-Bot Mobile SDK, behavioral DoS, and XML/SOAP security are present on BIG-IP Next — unverified; do not claim.
- The "~18% → ~1%" false-positive figure (attributed to F5 VP Joel Moses) and the 97.09% SecureIQLab total-security score are F5-supplied / vendor-commissioned — cite as F5's claim, not independent fact.
- Precise wording/dates inside my.f5.com KBs K000152956, K000156713, K000153073 (JS-gated); substance corroborated via F5's own GitHub (F5Networks archived repos referencing K000152956) and DevCentral.
- Precise "2029 TMOS extension" figure circulating in third-party commentary — not confirmed in an F5 primary source.

**Primary sources leaned on:** f5.com product pages (Distributed Cloud WAF, BIG-IP Advanced WAF, F5 WAF for NGINX, Web App Scanning, Managed Services/SOC); docs.cloud.f5.com; clouddocs.f5.com; docs.nginx.com; DevCentral (community.f5.com); my.f5.com KBs; F5 press releases (businesswire, investors.f5.com); F5 blog. **Third-party (competitive reality-check, lower trust):** Network World, Help Net Security, Thales/Imperva press, OWASP/CRS, Fastly docs, PeerSpot/Gartner Peer Insights, WAFPlanet.