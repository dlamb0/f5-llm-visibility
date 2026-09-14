# F5 Bot Defense & Online Fraud — Solution Area Reference (Doc 03)
doc_id: 03-bot-defense-fraud
solution_area: Bot Defense & Online Fraud
doc_tag: BOT
products_covered: F5 Distributed Cloud Bot Defense, F5 Distributed Cloud Account Protection, F5 Distributed Cloud Authentication Intelligence (Legacy), F5 Distributed Cloud Data Intelligence, F5 Distributed Cloud Client-Side Defense, F5 Distributed Cloud Aggregator Management, BIG-IP Advanced WAF (Proactive Bot Defense), F5 WAF for NGINX (bot signatures)
compiled: July 2026
primary_release_anchor: F5 AppWorld 2026 (March 11, 2026) Bot Defense human/bot/AI-agent enhancements + F5–Skyfire agentic-commerce partnership (announced March 18, 2026)
refresh_priority: High
last_validated: July 2026

---

## Layer 1 — Human orientation

This document covers F5's bot-management and online-fraud portfolio — the product line that traces its heritage to F5's 2020 acquisition of **Shape Security**. The Shape brand is fully retired; these capabilities now live under **F5 Distributed Cloud (XC)** service names, with a basic bot tier also available on BIG-IP and NGINX.

The core problem: automated traffic now outweighs human traffic online. The 2026 Thales/Imperva Bad Bot Report ("Bad Bots in the Agentic Age") found bots accounted for **more than 53% of all web traffic in 2025** (up from 51% in 2024), with human activity down to 47% and 17.2 trillion bot requests blocked in 2025; F5's own product pages use the rounder "about 50% of all internet traffic" framing. Malicious automation drives credential stuffing, account takeover (ATO), carding/gift-card cracking, inventory hoarding/scalping, content scraping, and fake-account creation. As of 2026, the frontier has shifted again — F5's messaging now centers on distinguishing **humans vs. bots vs. AI agents**, and on *allowing* trusted AI agents (agentic commerce) rather than only blocking automation.

**Buyers here are frequently fraud and digital/e-commerce teams, not just security.** A fraud team measuring chargebacks, a digital team measuring login friction/conversion, and a security team measuring ATO can all own this budget. The `fit_signals` fields below are written to catch all three personas, including buyers who don't know "bot management" is a product category.

**How the products differ by delivery model:**
- **F5 Distributed Cloud Bot Defense** — the flagship. SaaS-managed ML/telemetry network with client-side JavaScript (web) and a Mobile SDK (native apps). Deployed via XC WAAP, BIG-IP connector/iApp, CDN connectors, or e-commerce cartridges. Backed by F5's SOC + TACTICS threat team.
- **Account Protection / Authentication Intelligence / Data Intelligence** — the fraud-scoring and friction-reduction layer that sits on top of Bot Defense telemetry. **Verify status carefully** (see ledger): Data Intelligence is current; Account Protection is Limited Availability; Authentication Intelligence is flagged "(Legacy)."
- **Client-Side Defense** — browser-side script monitoring for Magecart/formjacking; the PCI DSS 4.0.1 compliance play.
- **BIG-IP Advanced WAF / F5 WAF for NGINX bot signatures** — the *basic* self-managed tier; signature + header-anomaly + JS-challenge based. Honestly positioned below XC's ML network.

Read Layer 2 for capability records (each self-contained), Layer 3 for routing/competitive/objection handling, and the appendix for the naming/currency ledger — the most perishable part.

---

## Layer 2 — Capability catalog

### [BOT] Advanced bot detection (credential stuffing, ATO, carding, scraping, fake accounts)
- solution_area: Bot Defense & Online Fraud
- capability_name: Advanced malicious-bot detection and mitigation
- plain_description: Identifies and blocks automated attacks against login, checkout, account-creation, and other high-value flows using client-side signal collection, behavioral analysis, and a cross-customer ML network — without relying on CAPTCHA or IP blocklists.
- delivered_by: F5 Distributed Cloud Bot Defense
- attribution_confidence: High
- customer_problem_solved: Credential stuffing → ATO, carding/card-cracking, gift-card enumeration, inventory hoarding/scalping, content scraping, and fake-account creation cause fraud losses, chargebacks, degraded performance, and skewed analytics. Static WAF rules and CAPTCHA fail against retooling attackers.
- fit_signals: "Our login page gets hammered — huge spikes in failed logins." "We keep getting account takeovers / customer complaints about drained accounts." "Sneaker/console/ticket drops sell out in seconds to bots and real customers are furious." "Our gift-card balances are being drained." "CAPTCHA is hurting conversion but bots still get through." "Competitors seem to have all our pricing/inventory data." "Marketing says signups are up but they're all fake." Fraud team drowning in manual review queues. E-commerce, banking, airlines, gaming, media verticals.
- disqualifiers: Purely internal apps with no consumer login/checkout; very low-traffic sites where basic WAF bot signatures suffice; customers whose "bot" concern is really volumetric L7 DoS (→ doc 04) or generic OWASP signatures (→ doc 02).
- value_framing: "Adapts faster than criminals retool" — a managed ML network spanning the world's largest banks, retailers, and airlines gives a network effect: attacks seen elsewhere are already known to your defense. Near-zero false positives; removes friction (CAPTCHA/MFA) to protect conversion and revenue while stopping fraud.
- product_routing_note: Lead with XC Bot Defense for any serious/persistent bot problem. Use BIG-IP AWAF or NGINX bot signatures only when the customer wants a basic self-managed tier or already owns those platforms (see routing 3a).
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/bot-defense; docs.cloud.f5.com/docs-v2/bot-defense/concepts/about-bot-defense

### [BOT] Human vs. bot vs. AI-agent traffic classification
- solution_area: Bot Defense & Online Fraud
- capability_name: Human / bot / AI-agent traffic classification
- plain_description: Distinguishes three traffic classes — human users, conventional bots, and autonomous AI agents — and lets organizations set policy for which automated systems may interact with their apps.
- delivered_by: F5 Distributed Cloud Bot Defense
- attribution_confidence: High
- customer_problem_solved: AI agents (agentic browsers, shopping agents) behave like humans and evade traditional bot signals; treating all automation as "block" breaks legitimate agent-driven commerce, while treating it as "allow" invites abuse. Organizations lack visibility into whether a session is human-, bot-, or agent-driven.
- fit_signals: "We're seeing weird traffic that passes as human but behaves like a script." "Our analytics are distorted — huge traffic, no conversions." "Leadership is asking how we handle ChatGPT/Perplexity/agent shopping traffic." "We want to allow AI shopping assistants but not scrapers." Customers worried about agentic browsers, prompt-injection-driven sessions, or AI scraping of content.
- disqualifiers: Customers with no consumer-facing web/app surface; those whose AI concern is securing their own LLM apps (→ doc 11, AI-agent *security*), not managing inbound agent *traffic*.
- value_framing: F5 claims it can "definitively tell whether a browser session is AI-driven or human; this isn't guesswork," using high-confidence behavioral/interaction data rather than static signatures or identity claims. Enables governance: allow trusted agents, block ungoverned automation.
- product_routing_note: XC Bot Defense only. This is the AppWorld 2026 enhancement; pair with the agent-verification/allowlisting record below for the "enable agentic commerce" pitch.
- maturity_flag: GA (enhancements announced with GA-framing at AppWorld, March 11, 2026; verify exact rollout with F5 as some agent features are newer)
- source_currency_flag: Current
- source: businesswire.com F5 AppWorld press release (2026-03-11); networkworld.com AppWorld coverage; f5.com/company/blog/managing-ai-agents-with-trust-control-and-confidence

### [BOT] Verified AI-agent allowlisting / agentic commerce (Skyfire KYA)
- solution_area: Bot Defense & Online Fraud
- capability_name: Verified AI-agent allowlisting and agentic-commerce enablement
- plain_description: Recognizes AI agents carrying verified identity tokens and grants them appropriate access, turning previously-blocked automation into authenticated, monetizable interactions — including standard e-commerce checkout by agents.
- delivered_by: F5 Distributed Cloud Bot Defense (with Skyfire "Know Your Agent"/KYA integration; F5 also references support for Web Bot Auth)
- attribution_confidence: High
- customer_problem_solved: Merchants want to participate in agent-driven commerce without dropping their bot defenses; they need to tell a malicious agent apart from a verified agent acting for a real customer, and link agent requests to accountable/paying actors.
- fit_signals: "We want to open our store to AI shopping agents but keep bots out." "How do we monetize agent traffic instead of just blocking it?" "Our checkout flow needs to work for verified agents." Merchants/content providers discussing agentic commerce strategy, tokenized agent payments, or "Know Your Agent."
- disqualifiers: Non-commerce sites with no incentive to admit agents; customers not yet seeing meaningful agent traffic; anyone needing this in production before the stated availability date.
- value_framing: "Transform what was previously blocked automation into authenticated, monetizable interactions" — no re-platforming; KYA uses standard JWTs compatible with OAuth2/JWKS, interpreted at the edge. Positions the F5 customer to "confidently open their doors to the next generation of Internet traffic."
- product_routing_note: XC Bot Defense only. Note availability timing: F5 stated the Skyfire integration would be "available by April 30, 2026." Confirm GA before promising to a customer.
- maturity_flag: Roadmap/Announced → Early GA (announced 2026-03-18, targeted availability 2026-04-30)
- source_currency_flag: Current
- source: f5.com/company/news/press-releases/f5-skyfire-secure-agentic-commerce; businesswire.com (2026-03-18)

### [BOT] Mobile app bot protection (Mobile SDK)
- solution_area: Bot Defense & Online Fraud
- capability_name: Native mobile app bot protection via Mobile SDK
- plain_description: A native SDK embedded in iOS/Android apps collects device telemetry and attaches it as headers to outbound requests, so Bot Defense can tell legitimate mobile users from automated/emulated traffic hitting mobile API backends.
- delivered_by: F5 Distributed Cloud Bot Defense (F5 Distributed Cloud Mobile SDK; optional no-code Mobile SDK Integrator; Promon partnership for no-code integration)
- attribution_confidence: High
- customer_problem_solved: Traditional JS-based bot defenses don't work in native mobile apps, leaving mobile API endpoints exposed to credential stuffing, fake accounts, scraping, and DoS. Mobile dev resources are scarce.
- fit_signals: "Most of our traffic/attacks are on our mobile app now." "We can protect the website but the mobile API is wide open." "We don't have mobile dev cycles to instrument the app." Banking/retail/gaming apps with heavy mobile usage; teams citing attacks bypassing web controls by hitting mobile endpoints.
- disqualifiers: Web-only businesses; customers unwilling to embed an SDK or ship an app update (proxy-only deployment cannot replicate mobile telemetry).
- value_framing: Consistent protection across web, mobile, and API; no-code SDK Integrator ties into CI/CD, and the Promon integration lets teams instrument apps "without touching app code in minutes." (Note: Forrester specifically praised F5's mobile SDK — see 3c — so this is a genuine, analyst-recognized strength.)
- product_routing_note: XC Bot Defense only. Requires app instrumentation — flag this as an SDK dependency (see instrumentation record).
- maturity_flag: GA (Mobile SDK GA; note some self-service/policy features flagged Early Access in docs)
- source_currency_flag: Current
- source: docs.cloud.f5.com/docs-v2/bot-defense/plan-bot-advanced/mobile; f5.com/resources/solution-guides/implement-f5-bot-defense-with-ease-in-mobile-apps-with-promon-sdk-integrator

### [BOT] Managed service / SOC + threat research (TACTICS)
- solution_area: Bot Defense & Online Fraud
- capability_name: Managed bot service with 24/7 SOC and threat research
- plain_description: F5 offers tiered service models where its Security Operations Center and TACTICS threat-intelligence team monitor traffic, respond to attacker retooling, and update rules — rather than leaving the customer to self-tune.
- delivered_by: F5 Distributed Cloud Bot Defense (managed-service tiers; F5 Managed Services TAMs/Solution Architects; TACTICS threat team)
- attribution_confidence: High
- customer_problem_solved: Attackers retool within minutes; self-tuned tools fall behind and consume scarce security-team time. Customers need humans-in-the-loop who counter new automation patterns continuously.
- fit_signals: "We don't have the headcount to constantly tune bot rules." "Every time we block them they come back different." "We need someone watching this 24/7." Lean security teams; orgs that bought a self-service bot tool and still got beaten. Regulated/enterprise buyers wanting an accountable managed partner.
- disqualifiers: Customers who explicitly want full self-management/control and have the expertise (F5 also offers self-managed tiers); very cost-sensitive buyers unwilling to pay for managed service.
- value_framing: A real differentiator vs. self-tuned tools — F5 describes fully managed (dedicated SOC + TACTICS), augmented/shared-SOC, and self-managed options. The TACTICS team "brings human experts into the loop," managing over 1 billion attack vectors/transactions per day; F5 operates global SOC locations (at least Poland, US, Canada, Mexico, India, Singapore per its Trust Center). Deterrence economics ("make successful attacks too costly").
- product_routing_note: Use to differentiate XC Bot Defense from self-tuned CDN modules and cheaper tools. Match tier to the customer's staffing and control preferences.
- maturity_flag: GA
- source_currency_flag: Current
- source: docs.cloud.f5.com/docs-v2/bot-defense/concepts/about-bot-defense; f5.com/products/distributed-cloud-services/managed-services; f5.com/company/trust-center/distributed-cloud-bot-defense (SOC locations)

### [BOT] Client-Side Defense (Magecart / formjacking / PCI DSS 4.0.1)
- solution_area: Bot Defense & Online Fraud
- capability_name: Client-side script monitoring and data-exfiltration mitigation
- plain_description: Operates in the browser to monitor first- and third-party JavaScript on web pages in real time, maintains a script inventory, validates script integrity, alerts on anomalous/malicious behavior, and blocks unauthorized data-exfiltration network calls with one-click mitigation.
- delivered_by: F5 Distributed Cloud Client-Side Defense (deployable via XC WAAP and via BIG-IP 17.1+ native connectivity)
- attribution_confidence: High
- customer_problem_solved: Magecart/formjacking/digital-skimming and web supply-chain attacks steal card data and PII directly in the browser — invisible to server-side WAFs. Merchants also face PCI DSS 4.0.1 requirements 6.4.3 and 11.6.1.
- fit_signals: "We take card payments online and need to hit the new PCI script rules." "Our QSA is asking about payment-page script inventory / tamper detection." "We have dozens of third-party scripts on checkout and no visibility." "We got hit by (or fear) a Magecart/skimming attack." E-commerce, retail, travel, any card-not-present merchant; compliance/QSA-driven conversations.
- disqualifiers: Businesses that don't process card payments in-browser (e.g., fully redirect to a hosted processor with no scripts that can affect payment security — verify SAQ eligibility); non-e-commerce apps; server-side-only threat concerns (→ doc 02).
- value_framing: Unlike server-side tools, it operates in the browser itself, giving real-time monitoring, integrity validation, and alerting "as it happens." "Purpose-built to address the client-side requirements outlined in PCI DSS v4.0.1" — 6.4.3 (script inventory/authorization) and 11.6.1 (tamper/change detection). These two requirements became **mandatory on March 31, 2025** (future-dated best practices since March 2022; deadline unchanged by the v4.0.1 revision published June 11, 2024). Compliance + brand/fraud protection in one.
- product_routing_note: Distinct product from Bot Defense; often sold alongside it. BIG-IP 17.1+ customers can run it as a self-managed connected service; XC WAAP customers enable it in the platform.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/client-side-defense; f5.com/company/blog/distributed-cloud-client-side-defense-prepares-customers-for-pci-dss; blog.pcisecuritystandards.org (6.4.3/11.6.1 effective date); community.f5.com (BIG-IP 17.1 enablement)

### [BOT] Account Protection (online fraud scoring)
- solution_area: Bot Defense & Online Fraud
- capability_name: Real-time transaction fraud scoring (post-login / manual fraud)
- plain_description: A closed-loop AI engine scores transactions across the user journey using telemetry, behavioral, and environmental signals to detect human-driven fraud that bot tools miss, giving fraud teams block/review/challenge/allow recommendations.
- delivered_by: F5 Distributed Cloud Account Protection (formerly Shape AI Fraud Engine / SAFE)
- attribution_confidence: High (attribution); Medium (current availability — see maturity flag)
- customer_problem_solved: Fraud that survives bot mitigation — manual fraud, mule accounts, human fraud rings — evades traditional rule/score tools; fraud teams face high false positives and heavy manual-review queues.
- fit_signals: "Bots aren't our only problem — we have organized human fraud." "Our fraud team is buried in manual reviews." "We want fewer transactions flagged for review without more losses." "Our current fraud engine misses too much / too many false positives." Banks, fintech, money transfer, e-commerce fraud teams. Buyer is often a fraud/risk leader, not security.
- disqualifiers: Customers whose problem is purely automated bots (Bot Defense alone suffices); those unwilling to deploy the Account Protection JS tag; anyone needing a fully GA, broadly-available product today (currently Limited Availability).
- value_framing: A converged security+fraud solution on unified telemetry ("over a billion transactions per day"); F5 markets identifying "2x fraud" vs. current solutions "in Fortune 500 production environments" and reducing consumer friction "by up to 90%" (both are F5 marketing claims — see ledger; not independently verified). Bridges the silo between security and fraud teams.
- product_routing_note: Sits on top of Bot Defense telemetry conceptually, but its only stated deployment prerequisite is the Account Protection JS tag (v2.3.5+), NOT a Bot Defense deployment. Lead with this only for a fraud-team buyer with human-fraud pain; confirm Limited Availability status and onboarding with F5 before positioning.
- maturity_flag: Beta/Early Access (F5 docs, updated July 2026, describe it as "currently in Limited Availability")
- source_currency_flag: Possibly stale (marketing efficacy claims survive mainly on reseller mirrors / F5 CDN PDFs; standalone product page appears removed in site consolidation — verify)
- source: docs.cloud.f5.com/docs-v2/account-protection/faqs/account-protection; docs.cloud.f5.com/docs/how-to/advanced-security/analyst-station; F5 Account Protection datasheet (CDN)

### [BOT] Authentication Intelligence (login friction reduction)
- solution_area: Bot Defense & Online Fraud
- capability_name: Returning-user recognition / session extension
- plain_description: Recognizes known-good returning users on known devices (using history, uniqueness, and integrity signals) to safely extend login sessions or reduce re-authentication/MFA friction, without increasing fraud risk.
- delivered_by: F5 Distributed Cloud Authentication Intelligence (Legacy)
- attribution_confidence: High (attribution); Low (currency — apparently sunset)
- customer_problem_solved: MFA and frequent logins create friction that drives cart abandonment and lost revenue; businesses want to reward known-good users with longer sessions without opening the door to ATO.
- fit_signals: "Our login/MFA friction is killing conversion." "We want to extend sessions for known customers safely." "Guest checkout is beating logged-in checkout." Digital/revenue-owner buyers focused on conversion and CX.
- disqualifiers: Any greenfield recommendation — this product is flagged "(Legacy)" and appears sunset; do not lead new deals with it. Security-only buyers with no CX/revenue mandate.
- value_framing: (Historical) Increase topline revenue by eliminating login friction for legitimate returning consumers while maintaining security. NOTE: position the friction-reduction *outcome*, but route to current products/F5 guidance rather than promising this SKU.
- product_routing_note: Treat as legacy. If a customer wants friction reduction, flag that naming/packaging has changed and defer to current F5 guidance (possibly folded into Bot Defense/Account Protection). Do not assert it is currently sold.
- maturity_flag: Unknown (Gartner Peer Insights lists it as "(Legacy)"; no explicit F5 end-of-sale notice found)
- source_currency_flag: Possibly stale
- source: docs.cloud.f5.com/docs/how-to/advanced-security/authentication-intelligence; Gartner Peer Insights "(Legacy)" listing

### [BOT] Data Intelligence (fraud telemetry enrichment)
- solution_area: Bot Defense & Online Fraud
- capability_name: High-fidelity telemetry enrichment for third-party fraud engines
- plain_description: A cloud data service that collects obfuscated client-side signals (behavior, device, network) via a JS tag and feeds high-fidelity intelligence into a customer's existing fraud decision engine to improve detection and cut false positives.
- delivered_by: F5 Distributed Cloud Data Intelligence
- attribution_confidence: High
- customer_problem_solved: Customers with an established fraud stack don't want to rip and replace; they want better signal (device/behavioral/network) to feed existing models and reduce fraud losses and false positives.
- fit_signals: "We already have a fraud engine but need better signals." "We want device/behavioral intelligence without changing our decisioning." "Our false-positive rate is too high." Fraud teams with incumbent platforms (Sift/Forter/in-house) seeking augmentation.
- disqualifiers: Customers who want an end-to-end fraud decision/blocking product (→ Account Protection) rather than enrichment; those unwilling to deploy a JS tag.
- value_framing: Augment, don't replace — integrates with existing fraud ecosystems and staff skill sets; F5's JS obfuscation protects signal integrity against reverse engineering. Only one of the three fraud SKUs with a clearly current f5.com product page (©2026).
- product_routing_note: Lead with Data Intelligence for fraud teams committed to their existing decision engine; lead with Account Protection when they want F5 to do the scoring/decisioning.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/data-intelligence-platform

### [BOT] Aggregator Management (open banking)
- solution_area: Bot Defense & Online Fraud
- capability_name: Financial data aggregator / third-party-provider traffic management
- plain_description: Labels login traffic as human, automated, or aggregator; enforces that aggregators access only authorized data via authorized channels within predefined limits; and detects credential stuffing hidden inside aggregator traffic.
- delivered_by: F5 Distributed Cloud Aggregator Management (a managed service extending Bot Defense)
- attribution_confidence: High
- customer_problem_solved: In open banking, financial data aggregators use valid customer credentials to scrape data and can be abused as an ATO vector; most FIs are blind to how much aggregator traffic they carry and cannot enforce usage policies.
- fit_signals: "We're a bank and can't tell aggregator traffic from customer traffic." "Open banking / PSD2 is forcing us to allow third-party access but we can't control it." "Aggregators are scraping more than they should." Financial institutions, open-banking programs.
- disqualifiers: Non-financial-services customers; FIs with no open-banking/aggregator exposure.
- value_framing: "Gain the benefits of aggregators without the risk" — visibility and least-privilege control over aggregator access, built on the Bot Defense engine and a global network of known aggregators from top FIs.
- product_routing_note: Financial-services-specific; extends Bot Defense. Route here only for FI/open-banking conversations.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/aggregator-management

### [BOT] Basic bot defense on BIG-IP Advanced WAF
- solution_area: Bot Defense & Online Fraud
- capability_name: Proactive Bot Defense (signatures, header anomalies, JS challenge) on BIG-IP
- plain_description: BIG-IP Advanced WAF classifies clients using browser/mobile verification tests, bot signatures, and anomaly detection, and can block/CAPTCHA/rate-limit; a JavaScript challenge is sent to first-time browsers to weed out non-browser automation.
- delivered_by: BIG-IP Advanced WAF (Proactive Bot Defense; Anti-Bot Mobile Security SDK; bot signature live updates)
- attribution_confidence: High
- customer_problem_solved: On-prem/BIG-IP customers need baseline protection against web scraping, brute force, and L7-DoS-adjacent automation without adding a SaaS service.
- fit_signals: "We already run BIG-IP AWAF and want to turn on bot protection." "We need basic bot blocking on-prem, not a managed network." Existing BIG-IP shops; on-prem/regulated environments; teams wanting to self-manage.
- disqualifiers: Sophisticated/persistent bot problems (credential stuffing at scale, retooling adversaries) — this tier is signature/challenge-based and will be outrun; carding/ATO at scale; customers needing cross-customer ML network effect.
- value_framing: Honest positioning: this is the *basic tier* — good for baseline hygiene on infrastructure you already own. For advanced, adaptive, retooling-resistant defense, step up to XC Bot Defense's ML/telemetry network and SOC.
- product_routing_note: Position as baseline or coexistence, not as equivalent to XC Bot Defense. BIG-IP can also act as an insertion point (native module/iApp) that routes traffic to XC Bot Defense — the recommended path when the problem is advanced.
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com (BIG-IP ASM/AWAF Configuring Bot Defense); f5.com/products/big-ip-services/advanced-waf

### [BOT] Basic bot signatures on F5 WAF for NGINX
- solution_area: Bot Defense & Online Fraud
- capability_name: Bot signature + header-anomaly detection on F5 WAF for NGINX
- plain_description: Detects clients that falsely claim to be browsers or search engines by inspecting User-Agent/URI against a bot-signature package and checking HTTP-header anomalies, classifying traffic as trusted/untrusted/malicious bots with per-class actions (default: detect trusted, alarm untrusted, block malicious).
- delivered_by: F5 WAF for NGINX (formerly NGINX App Protect WAF; app-protect-bot-signatures package)
- attribution_confidence: High
- customer_problem_solved: DevOps/Kubernetes teams running NGINX need lightweight, declarative bot protection integrated into CI/CD without a separate appliance or SaaS.
- fit_signals: "We run NGINX/NGINX App Protect and want bot signatures in our pipeline." "We need declarative, as-code bot rules for Kubernetes." Platform/DevSecOps teams; container-native shops.
- disqualifiers: Advanced/persistent bot problems (same limits as the BIG-IP basic tier — signature/header based, not an ML network); carding/ATO at scale.
- value_framing: Honest positioning: lightweight signature-based tier for DevOps environments. Escalate to XC Bot Defense for adaptive, retooling-resistant protection.
- product_routing_note: Basic tier / coexistence. Bot signatures update independently of the core package. Not equivalent to XC Bot Defense.
- maturity_flag: GA
- source_currency_flag: Current
- source: docs.nginx.com/waf/policies/bot-signatures/; f5.com/products/nginx/f5-waf-for-nginx

### [BOT] JavaScript / SDK instrumentation vs. proxy-only deployment
- solution_area: Bot Defense & Online Fraud
- capability_name: Deployment/instrumentation model (JS + Mobile SDK telemetry vs. proxy)
- plain_description: XC Bot Defense's high-fidelity detection depends on client-side telemetry: injected JavaScript for web browsers and the Mobile SDK for native apps. Traffic is routed through insertion points (XC LB, BIG-IP connector/iApp, CDN connectors) that add/inspect telemetry headers before requests reach the origin.
- delivered_by: F5 Distributed Cloud Bot Defense (JS injection + Mobile SDK; connectors for BIG-IP, CDNs, Salesforce Commerce Cloud, Adobe Commerce)
- attribution_confidence: High
- customer_problem_solved: Technical objection — teams need to know what must be instrumented. Full-fidelity web detection needs JS injection; mobile needs the SDK embedded in the app; a proxy-only path exists but does not replicate the client-side signal richness.
- fit_signals: "How much do we have to change our app to deploy this?" "Can we do this without touching our code / at the CDN?" "Do we have to embed an SDK in our mobile app?" Architecture/technical-evaluation stage conversations.
- disqualifiers: N/A (this is a cross-cutting deployment reality, relevant whenever XC Bot Defense is proposed).
- value_framing: Flexible insertion — connectors for CDNs, BIG-IP (native module/iApp), and e-commerce platforms mean many customers deploy without deep app changes; but be transparent that best efficacy on web requires JS injection and mobile requires the SDK. API-mode deployment exists but requires F5 to provision infrastructure (cannot be self-serviced).
- product_routing_note: Set expectations early: web = JS tag; native mobile = Mobile SDK (app update required); the Mobile SDK Integrator/Promon enable no-code integration. Proxy-only/API-mode is possible but check efficacy trade-offs with F5.
- maturity_flag: GA
- source_currency_flag: Current
- source: docs.cloud.f5.com/docs-v2/bot-defense/plan-bot-advanced/overview; docs.cloud.f5.com/docs-v2/bot-defense/how-tos/plan-bot-defense

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**By buyer persona:**
- **Fraud / risk team, human-fraud pain** → lead with Account Protection (confirm Limited Availability) or Data Intelligence (if they keep their existing fraud engine). Emphasize the security↔fraud "power of two" narrative.
- **Security team, bot/ATO pain** → lead with XC Bot Defense.
- **Digital / e-commerce / revenue owner, friction & conversion pain** → the friction-reduction outcome historically owned by Authentication Intelligence; because that SKU is Legacy, frame the outcome and route to current F5 guidance / Bot Defense.
- **Compliance / QSA-driven, card payments** → Client-Side Defense (PCI DSS 4.0.1 6.4.3 & 11.6.1).
- **Financial institution, open banking** → Aggregator Management.

**By existing footprint / architecture:**
- **Greenfield / SaaS-preference** → XC Bot Defense via XC WAAP (SaaS-managed).
- **Existing BIG-IP, on-prem, mission-critical** → BIG-IP as insertion point routing to XC Bot Defense (native module/iApp), or BIG-IP AWAF Proactive Bot Defense for a basic self-managed tier. Client-Side Defense available natively on BIG-IP 17.1+.
- **CDN-fronted (CloudFront, Cloudflare)** → XC Bot Defense CDN connectors.
- **E-commerce platform (Salesforce Commerce Cloud, Adobe Commerce)** → XC Bot Defense certified cartridge/connector.
- **NGINX / Kubernetes / DevOps** → F5 WAF for NGINX bot signatures for a basic tier; escalate to XC Bot Defense for advanced needs.

**Self-managed vs. managed:** F5 offers fully managed (dedicated SOC + TACTICS), augmented/shared-SOC, self-managed SaaS, and self-managed hybrid (BIG-IP + NGINX). Match to staffing and control preference.

**Coexistence / migration:** BIG-IP and NGINX basic bot tiers can coexist with XC Bot Defense (basic on the data plane, advanced in the ML network). The recommended pattern for advanced problems is to keep BIG-IP/NGINX as the enforcement/insertion point and route decisions to XC. Where public docs don't specify a migration path, say so rather than inventing official guidance (no F5-published BIG-IP/NGINX→XC migration playbook was located).

### 3b. Disqualifiers / anti-patterns (aggregate)

- **No consumer-facing login/checkout/account surface** → bot/fraud story is weak; likely doc 02 (WAF) or doc 01 (API) fits better.
- **Problem is really volumetric L7 DoS** → doc 04, not this area.
- **Problem is generic OWASP signature coverage** → doc 02.
- **Problem is securing the customer's own LLM/AI app** → doc 11 (AI security); here we only *manage inbound* agent traffic.
- **Very low traffic / low fraud exposure** → basic BIG-IP/NGINX bot signatures may be enough; don't over-sell XC.
- **Customer refuses any client-side instrumentation** (no JS, no SDK) → XC Bot Defense efficacy is constrained; set expectations or reconsider fit.
- **Customer wants a fully GA, broadly available fraud-scoring SKU today** → Account Protection is Limited Availability; don't over-promise.
- **Greenfield ask specifically for "Authentication Intelligence"** → flag Legacy status; don't lead with it.

### 3c. Competitive positioning and objection handling (LOWER CONFIDENCE — verify each on live deal)

Market context: Forrester renamed the category to **"Bot and Agent Trust Management"** in late 2025 (per third-party commentary), reflecting the AI-agent shift — consistent with F5's human/bot/agent messaging.

**F5's own analyst standing:** F5 was named a **Strong Performer** (not a Leader) in *The Forrester Wave™: Bot Management Software, Q3 2024*, where Forrester highlighted F5's mobile protection — F5 is "the only vendor whose mobile SDK can extend into a mobile application shielding tool" (per F5's own blog citing the report). Use the mobile-SDK strength; do not overstate F5's overall Wave placement.

**Dedicated bot vendors:**
- **HUMAN Security** — independent; raised $50M+ growth funding (Oct 2024, led by WestCap, ~$300M total raised). Named a **Leader** in *The Forrester Wave™: Bot Management Software, Q3 2024* (analyst Sandy Carielli), with top scores in nine criteria including Detection Models and Mobile App and API Protection. (HUMAN and some third parties also cite a "Bot and Agent Trust Management, Q2 2026" Wave leadership; that specific 2026 wave could not be verified against a Forrester source — flag, don't assert.) Strong threat-research/takedown reputation (3ve, Methbot, PARETO, VASTFLUX). *Confidence: Medium on facts, Low on head-to-head.*
- **DataDome** — independent; Paris/NY; **~$81–82M total raised, last major round the $42M Series C announced March 30, 2023** (led by InfraVia Growth, with Elephant and ISAI). Its ML analyzes ~5 trillion signals/day across 26+ points of presence and it says it "autonomously stops over 350 billion attacks annually." Strong CDN-augmentation and PCI (Page Protect) positioning; 24/7 SOC. *Note active DataDome↔Arkose patent litigation (D. Del. 1:23-cv-01467; PTAB IPRs, 2025) — both remain independent.*
- **Arkose Labs** — independent; challenge/proof-of-work + device model; ~20% of customers Fortune 500.

F5's stated differentiators vs. dedicated vendors (public evidence): the cross-customer ML network effect across "the world's largest banks, retailers, and airlines"; JS/telemetry obfuscation (F5 says it developed the "first virtual machine (VM)-based obfuscation defense in JavaScript"); the managed SOC + TACTICS human threat team; and unified security+fraud+delivery on one platform (ADSP). Flag as F5 claims, not verified head-to-head wins.

**CDN-bundled bot management (Cloudflare, Akamai):**
- **Akamai** — its Bot Manager is built on the **Shape Security** technology Akamai licensed; widely cited by third parties as an enterprise "gold standard" for bot management.
- **Cloudflare** — bot management bundled into its platform; strength is a unified/easy dashboard; a free tier covers basic protections.

**Objection: "Our CDN's bot module is included for free."**
Response (evidence-based): CDN-bundled modules are typically signature/rate-limit/heuristic tiers optimized for breadth and ease, not the retooling-resistant, cross-industry ML network + human SOC that F5 (Shape heritage) provides. Even dedicated vendors position themselves this way — DataDome's own founder notes many customers "choose us to augment the out-of-the-box bot management features CDNs like Cloudflare and Akamai offer." Reframe from cost to *efficacy and loss avoidance*: F5 Labs' 2025 Advanced Persistent Bots Report (analyzing 207 billion transactions) shows attackers continuously evolve to bypass even sophisticated controls, and that after mitigation ~10.6% of web login traffic still came from malicious sources on average; independent data underscores the stakes — the 2025 Imperva Bad Bot Report found **account-takeover attacks rose 40% in 2024, with financial services the single most-targeted sector at 22% of all ATO incidents.** Ask: what's your measured ATO/carding/chargeback rate today, and who tunes the CDN module when attackers retool next week? Note that Akamai's own bot capability derives from Shape technology — F5 owns and continues to develop that lineage directly.

**Fraud platforms (Sift, Forter) — adjacent, different buyer:** these are fraud-decisioning platforms owned by fraud teams. F5 Data Intelligence *feeds* such engines rather than replacing them; Account Protection competes more directly when the customer wants F5 to do the decisioning. Position as complementary/augmentation unless the customer explicitly wants to replace their fraud engine.

All competitive claims above are lower-confidence and should be verified against current, named sources on a live deal; the bot/fraud market consolidates quickly.

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify every engagement):**
- **Shape Security** branding is fully retired. Heritage names: Shape Enterprise Defense / Shape Integrated Bot Defense → **F5 Distributed Cloud Bot Defense**; **Shape AI Fraud Engine (SAFE)** → **F5 Distributed Cloud Account Protection**. Silverline Shape Defense also folded into XC Bot Defense.
- **F5 WAF for NGINX** = formerly **NGINX App Protect WAF**.
- **BIG-IP APM** repositioned as **BIG-IP Zero Trust Access** (AppWorld 2026) — not a bot product, noted only to avoid confusion.
- **"F5 DCS" / "XC"** both refer to F5 Distributed Cloud.

**Status flags (highest-risk — do not overstate):**
- **F5 Distributed Cloud Account Protection** — docs updated July 2026 say it is **Limited Availability, not GA**. Efficacy claims ("2x fraud," "up to 90% friction reduction," and a "177% more fraud" figure for a North American bank) trace to F5 CDN PDFs / reseller mirrors; the standalone f5.com product page appears removed in the site consolidation. Treat marketing figures as unverified F5 claims. Only stated deployment prerequisite is the Account Protection JS tag (v2.3.5+), not Bot Defense.
- **F5 Distributed Cloud Authentication Intelligence** — flagged **"(Legacy)"** by Gartner Peer Insights; docs and a datasheet remain online but no live product page. Strongly implied sunset; **no explicit F5 end-of-sale notice found** — do not assert discontinuation as fact, but do not lead new deals with it.
- **F5 Distributed Cloud Data Intelligence** — the only fraud SKU with a clearly current f5.com product page (©2026).
- **Human/bot/AI-agent classification** — announced at AppWorld (2026-03-11); treat as current but verify exact GA scope of the newest agent features.
- **Skyfire KYA agent allowlisting** — announced 2026-03-18, targeted availability **by April 30, 2026**; confirm GA before committing to a customer.

**Explicitly NOT verified (do not assert):**
- Whether Authentication Intelligence's function has been formally folded into Bot Defense or Account Protection.
- Exact GA date/scope of the AppWorld 2026 Bot Defense agent-classification enhancements beyond the press-release framing.
- The "Forrester Wave: Bot and Agent Trust Management, Q2 2026" naming/results (cited by HUMAN and some third parties but not confirmed against a Forrester source).
- Any head-to-head efficacy win vs. named competitors.
- Whether a BIG-IP/NGINX→XC migration has an official F5-published playbook (not located).

**Primary sources leaned on:** f5.com product pages (Bot Defense, Client-Side Defense, Data Intelligence, Aggregator Management, Managed Services, Bot & Risk Management); docs.cloud.f5.com and techdocs.f5.com (Bot Defense, Account Protection, Authentication Intelligence, Mobile SDK, BIG-IP bot defense); docs.nginx.com (bot signatures); f5.com/company/blog and press releases (PCI DSS 4.0.1; AppWorld 2026; Skyfire); f5.com/company/trust-center (SOC locations); F5 Labs 2025 Advanced Persistent Bots Report.
**Third-party sources (competitive reality-check / market data, lower trust):** BusinessWire/NetworkWorld/SiliconANGLE (AppWorld coverage); PCI SSC blog (6.4.3/11.6.1 deadlines); HUMAN/DataDome/Arkose company, funding, and litigation sources; 2025 & 2026 Thales/Imperva Bad Bot Reports (traffic and ATO statistics); Forrester Wave commentary (via third parties and F5 blog); Gartner Peer Insights (Legacy tag).