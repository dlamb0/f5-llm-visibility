# F5 DDoS Protection — Solution Area Reference (Doc 04)
doc_id: 04-ddos-protection
solution_area: DDoS Protection
doc_tag: DDOS
products_covered: F5 Distributed Cloud DDoS Mitigation (SaaS, formerly Silverline DDoS Protection); BIG-IP Advanced Firewall Manager (AFM) DoS/DDoS; BIG-IP DDoS Hybrid Defender (DHD); F5 DoS for NGINX (formerly NGINX App Protect DoS); rSeries/VELOS FPGA-assisted mitigation (delivery detail)
compiled: July 2026
primary_release_anchor: F5 WAF for NGINX / F5 DoS for NGINX v5.9 rename (Sep 2025); F5 XC SaaS release highlights through Mar 2026 (configurable L7 DDoS RPS thresholds, CAPTCHA/JS-challenge as L7 DDoS actions); Silverline EoL 30 Jun 2025
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

This document covers F5's Distributed Denial of Service (DDoS) mitigation story across the three attack tiers — volumetric (L3/4), protocol, and application-layer (L7) — and across three delivery models: SaaS/cloud scrubbing, on-prem appliance/software, and cloud-native (NGINX). The core value of this doc is **routing**: matching the customer's problem and architecture to the right F5 vehicle.

The four F5 vehicles, and how they differ:

- **F5 Distributed Cloud (XC) DDoS Mitigation** — a managed, SaaS-delivered cloud scrubbing service running on F5's Global Network. This is F5's answer to large volumetric attacks that would saturate an on-prem pipe. It is the **direct replacement for the retired Silverline DDoS Protection** (Silverline reached End of Life 30 June 2025), so installed-base customers will say "Silverline" on calls. Delivered in Routed Mode (BGP, for customers with their own /24+ prefix) or Proxy Mode (DNS-based, for app-level protection), in Always-On or Always-Available (on-demand) subscriptions, backed by F5's Security Operations Center (SOC).
- **BIG-IP Advanced Firewall Manager (AFM)** — the on-prem/virtual network firewall whose DoS/DDoS profiles deliver surgical, stateful L3–L7 mitigation in the data center, with hardware acceleration on F5 appliances. DDoS is one of four AFM features; AFM as a general network firewall is NOT covered by any doc in this corpus (a documented coverage gap — see coverage-matrix.md); this doc covers only its DoS/DDoS features.
- **BIG-IP DDoS Hybrid Defender (DHD)** — a purpose-built, BIG-IP-based on-prem DDoS appliance/VE for multi-layer L3–L7 mitigation with hybrid cloud signaling. Still marketed by F5 as of mid-2026, but check packaging carefully (see naming perils).
- **F5 DoS for NGINX** (formerly NGINX App Protect DoS) — behavioral, machine-learning L7 DoS protection running natively on NGINX Plus and NGINX Ingress Controller, part of the NGINX One premium package. This is the app-team / DevOps / Kubernetes vehicle.

Hardware (rSeries, VELOS) is a **delivery detail** under AFM/DHD: F5 FPGAs (ePVA lineage) offload SYN-flood and 100+ attack-vector mitigation at line rate.

Read Layer 2 for the capability catalog (one self-contained record per capability). Read Layer 3 for product-routing decision logic, disqualifiers, and bounded competitive/objection handling. The appendix tracks perishable naming and unverified items.

Scope boundaries: per-endpoint API rate limiting as an API story → doc 01; non-DoS bot abuse → doc 03; general network firewall → not covered in this corpus (documented gap — see coverage-matrix.md); service-provider-scale DDoS detail → doc 12 (brief cross-reference here only).

## Layer 2 — Capability catalog

### [DDOS] Cloud volumetric scrubbing (L3/4) via SaaS edge
- solution_area: DDoS Protection
- capability_name: Cloud volumetric (routed) DDoS scrubbing at the network edge
- plain_description: F5 absorbs and filters massive network-layer floods (TCP/SYN, UDP, ICMP, reflection/amplification) in its global scrubbing network before the traffic ever reaches the customer's pipe, returning clean traffic via BGP or GRE tunnel.
- delivered_by: F5 Distributed Cloud DDoS Mitigation (SaaS; formerly Silverline DDoS Protection)
- attribution_confidence: High
- customer_problem_solved: Volumetric attacks that exceed the customer's internet circuit or on-prem device capacity — no on-box solution can help once the upstream pipe is saturated.
- fit_signals: "Our pipe got saturated and we went dark," "the attack was bigger than our firewall could handle," "we need something upstream of our data center," "we run our own IP space / advertise our own prefixes," "we got a ransom DDoS note," "our ISP null-routed us and that took us offline too," gaming/finance/SaaS with public IP ranges, prior 100Gbps+ incident (F5 Labs' 2024 DDoS Attack Trends report notes attacks consistently above 100Gbps and many over 500Gbps in 2023, with the largest single attack peaking at 1Tbps).
- disqualifiers: Customer has no publicly routable prefix and only needs a single web app protected (use Proxy Mode / XC WAAP instead); attacks are purely application-layer low-and-slow (volumetric scrubbing won't help); customer is fully inside one hyperscaler and content with that cloud's native DDoS.
- value_framing: Keep the business online during multi-terabit attacks; mitigation happens close to the attack source, not at your doorstep; you don't grow your own pipe or staff to survive a flood.
- product_routing_note: Lead with XC DDoS for volumetric/routed scenarios and customers wanting a managed service. If the customer already runs BIG-IP on-prem and wants primary on-box defense with cloud overflow, pair XC (or DHD) with hybrid signaling.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/distributed-cloud-services/l3-and-l7-ddos-attack-mitigation; docs.cloud.f5.com "Set Up L3/L4 Routed DDoS Mitigation"; DevCentral "Guide to F5 Volumetric (Routed) DDoS Protection"

### [DDOS] Routed Mode vs Proxy Mode onboarding
- solution_area: DDoS Protection
- capability_name: Routed (BGP) vs Proxy (DNS) deployment modes for XC DDoS
- plain_description: XC DDoS can be onboarded two ways — Routed Mode advertises the customer's own IP prefix via BGP so all inbound traffic transits F5 scrubbing; Proxy Mode uses DNS/authoritative resolution and F5 application load balancers to protect specific apps without owning a routable subnet.
- delivered_by: F5 Distributed Cloud DDoS Mitigation (SaaS)
- attribution_confidence: High
- customer_problem_solved: Different customers have different network footprints; the deployment mode determines whether F5 protects a whole network block or a defined set of applications.
- fit_signals: "We own a /24 and want the whole block protected" (Routed); "we don't control a full subnet, we just need these apps covered" (Proxy); "we can't make routing changes but we can change DNS"; "we're hosted in AWS/Azure but want F5 to scrub."
- disqualifiers: Not a differentiator for customers who only need on-prem/localized protection; irrelevant to NGINX-only app teams.
- value_framing: Flexible onboarding — protect your whole network via BGP, or just the apps that matter via a simple DNS change with minimal network disruption.
- product_routing_note: Routed Mode requires a publicly advertisable Class C (/24) or more specific prefix; if the customer lacks one, Proxy Mode with XC load balancers is the path (F5's docs bundle ten load balancers with a Proxy Mode deployment). Proxy Mode overlaps with XC WAAP (doc 01/03) — coordinate.
- maturity_flag: GA
- source_currency_flag: Current
- source: docs.cloud.f5.com "Set Up L3/L4 Routed DDoS Mitigation"; f5.com service description PDF

### [DDOS] Application-layer (L7) DDoS mitigation in the cloud
- solution_area: DDoS Protection
- capability_name: Cloud L7 DoS/DDoS mitigation (HTTP floods, slowloris, DNS floods)
- plain_description: F5's cloud platform detects and mitigates application-targeted attacks — HTTP GET/POST floods, slow-and-low attacks, DNS reflection/amplification — using AI/ML behavioral analysis, rate limiting, and challenge actions (CAPTCHA / JS challenge).
- delivered_by: F5 Distributed Cloud DDoS Mitigation / XC WAAP (SaaS)
- attribution_confidence: High
- customer_problem_solved: Sophisticated attacks that don't saturate bandwidth but exhaust application resources (login pages, search APIs, checkout flows), rendering the app unavailable to real users.
- fit_signals: "The site slowed to a crawl but our bandwidth graphs looked normal," "our login/search endpoint keeps getting hammered," "attackers target our most expensive pages," "we saw a flood of legit-looking HTTP requests," WordPress/pingback abuse, DNS NXDOMAIN floods (F5 Labs found DNS QUERY/NXDOMAIN floods were the single most common attack vector in 2023, appearing in roughly 26% of events).
- disqualifiers: Purely volumetric L3/4 problems (handled by scrubbing tier); customers whose L7 concern is really API rate limiting (→ doc 01) or credential-stuffing bots without a DoS effect (→ doc 03).
- value_framing: Stop the attacks that slip under the bandwidth radar; distinguish good traffic from bad without blocking real users.
- product_routing_note: L3/4 mitigation is included/on-by-default in the XC platform; L7 DoS detection/mitigation is configured per load balancer. As of the Mar 2026 XC release, the RPS threshold for L7 DDoS detection is customer-configurable (engaging when the threshold is exceeded and origin health degrades), and CAPTCHA/JS challenge can be set as L7 DDoS mitigation or protection actions. Note overlap with doc 01 (API) and doc 03 (bots) — keep DoS framing here.
- maturity_flag: GA
- source_currency_flag: Current
- source: DevCentral "F5 Distributed Cloud L3-L7 DDoS Mitigation"; docs.cloud.f5.com Release Changelogs (Mar 2026)

### [DDOS] Managed SOC service, SLA, and forensic reporting
- solution_area: DDoS Protection
- capability_name: Managed 24x7 SOC, SLA commitments, and attack visibility
- plain_description: F5 operates the XC DDoS service as a managed offering with a 24x7 Security Operations Center that monitors, alerts, and applies human-led mitigations, backed by published SLA commitments and a console with before/during/after attack forensics.
- delivered_by: F5 Distributed Cloud DDoS Mitigation (SaaS)
- attribution_confidence: High
- customer_problem_solved: Customers lacking in-house DDoS expertise or round-the-clock coverage need experts to run mitigation and prove it worked (for execs, auditors, and post-incident review).
- fit_signals: "We don't have a 24/7 security team," "we need someone to call when we're under attack," "our board wants an SLA," "we need after-action reports for compliance," "last time we spent hours manually chasing an attack."
- disqualifiers: Customers with mature in-house DDoS teams who want full self-service control and are cost-sensitive to a managed premium; on-prem-only requirements driven by data residency.
- value_framing: F5 experts fight the attack for you, with contractual SLA and full forensic reporting — you don't build a SOC to survive DDoS.
- product_routing_note: The managed SOC is core to XC DDoS and the former Silverline story; for self-managed on-prem, route to AFM/DHD instead. F5's XC DDoS service description states a **99.99% uptime SLA, a 15-minute Time to Notify (TTN), and a 15-minute Time to Mitigate (TTM)** — with the note that edge auto-mitigation occurs in seconds; the 99.99% figure is confirmed on the live f5.com product page ("24x7 support by certified F5 experts in our SOC, offering 99.99% uptime SLAs"). Legacy Silverline documents cited 99.999% uptime — do not conflate; the current authoritative figure is 99.99%.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com service description PDF "F5 Distributed Cloud DDoS Mitigation Managed Service"; f5.com XC DDoS product page

### [DDOS] Global Network scrubbing capacity and footprint
- solution_area: DDoS Protection
- capability_name: Multi-terabit global scrubbing capacity and Regional Edge footprint
- plain_description: F5's Distributed Cloud backbone and scrubbing infrastructure is engineered for the largest attacks, with multi-terabit capacity distributed across Regional Edges in global metro markets.
- delivered_by: F5 Distributed Cloud DDoS Mitigation (SaaS)
- attribution_confidence: High
- customer_problem_solved: Absorbing attacks whose scale (hundreds of Gbps to multi-Tbps) exceeds any single data center or on-prem device.
- fit_signals: "How big an attack can you actually absorb?" "We were told our last attack peaked over 500Gbps," "we need global coverage close to our users," latency-sensitive workloads wanting scrubbing near the source.
- disqualifiers: Small orgs whose realistic threat is well within on-prem capacity; single-region apps with no volumetric exposure.
- value_framing: Capacity headroom you'll never build yourself, positioned close to attack sources worldwide.
- product_routing_note: Use capacity numbers carefully — F5's public figures vary by document (see appendix). F5's current Distributed Cloud DDoS Mitigation solution-overview PDF states the backbone and scrubbing infrastructure is "designed to handle today's largest and most complex DDoS attacks with more than 12+ Tbps of combined scrubbing capacity"; the 2023 service description separately cites 13 Tbps across 24 Regional Edges in 22 metro regions; the live product page uses only "multi-terabit." Treat exact figures as possibly stale and confirm at deal time.
- maturity_flag: GA
- source_currency_flag: Possibly stale (specific figures date to 2022–2023)
- source: f5.com Distributed Cloud DDoS Mitigation solution-overview PDF; f5.com service description PDF; f5.com XC DDoS product page

### [DDOS] On-prem stateful L3–L7 DoS profiles (AFM)
- solution_area: DDoS Protection
- capability_name: BIG-IP AFM DoS/DDoS device and per-object protection profiles
- plain_description: BIG-IP AFM applies DoS/DDoS protection at two levels — device protection (whole BIG-IP) and protection profiles (per virtual server / protected object) — using 100+ attack vectors, automatic/manual thresholds, dynamic signatures, bad-actor detection, and blacklisting (incl. RTBH / IP-shun to upstream routers).
- delivered_by: BIG-IP Advanced Firewall Manager (AFM); also delivered on rSeries/VELOS hardware and BIG-IP VE
- attribution_confidence: High
- customer_problem_solved: Surgical, stateful mitigation of network and protocol attacks inside the data center, with granular per-application policy — for orgs that must keep protection on-prem.
- fit_signals: "We already run BIG-IP," "we need DDoS protection in our own data center," "data residency/compliance means we can't send traffic to a cloud scrubber," "we want per-application thresholds," "we run F5 LTM and want to add DDoS," service providers protecting infrastructure and subscribers.
- disqualifiers: The realistic threat is volumetric flooding that would saturate the internet circuit (on-box can't help a saturated pipe — need cloud scrubbing); app teams in Kubernetes wanting software-native L7 DoS (→ F5 DoS for NGINX); customer wants a fully managed service.
- value_framing: Precise, stateful, hardware-accelerated protection where you control it; consolidate firewall + DDoS + DNS security on one platform.
- product_routing_note: Lead with AFM when the customer already owns BIG-IP and wants network firewall + DDoS consolidated on-prem. For a dedicated, purpose-built DDoS box with hybrid signaling, consider DHD. AFM as a general firewall is not covered in this corpus (documented gap) — keep DoS framing here.
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com "About AFM DoS/DDoS Protection" (17.1); f5.com AFM product page; my.f5.com K000137915

### [DDOS] Purpose-built on-prem hybrid DDoS appliance (DDoS Hybrid Defender)
- solution_area: DDoS Protection
- capability_name: BIG-IP DDoS Hybrid Defender multi-layer on-prem mitigation with cloud signaling
- plain_description: DHD is a purpose-built, BIG-IP-based DDoS solution offering multi-layered L3–L7 mitigation (behavioral DoS, dynamic signatures, full SSL decryption, anti-bot) deployable inline, out-of-band, or bridged, with the ability to signal cloud scrubbing when the pipe is threatened.
- delivered_by: BIG-IP DDoS Hybrid Defender (DHD)
- attribution_confidence: Medium (product still marketed mid-2026, but packaging/relationship to AFM and next-gen platforms is a naming peril — verify)
- customer_problem_solved: Organizations wanting a dedicated, self-tuning on-prem DDoS device (not just an AFM add-on) that combines stateful and stateless defense and can burst to cloud scrubbing.
- fit_signals: "We want a dedicated DDoS box, not just a firewall feature," "we need inline sub-second mitigation with SSL visibility," "we want on-prem primary with cloud backup," "we already evaluated DHD," API-gateway front ends needing fast L7 behavioral DoS.
- disqualifiers: Cloud-native/DevOps teams (→ NGINX); customers who only need DoS profiles on existing BIG-IP (AFM suffices); fully managed-service seekers (→ XC).
- value_framing: One appliance for blended network + application attacks with full SSL decryption and line-rate hardware assist; stateful protection with stateless scale.
- product_routing_note: DHD and AFM overlap heavily (DHD is built on the BIG-IP DoS engine). Historically DHD signaled to Silverline for cloud offload; with Silverline retired, verify the current cloud-signaling target. Do not assert a specific DHD-to-BIG-IP-Next migration path — not confirmed in public sources. (Note: older Herculon-branded DHD/iSeries appliances went End-of-Sale; DevCentral community threads as recent as 2026 show open questions about DHD on F5OS/rSeries — treat as unresolved.)
- maturity_flag: GA (verify packaging)
- source_currency_flag: Possibly stale
- source: f5.com/products/big-ip-services/ddos-hybrid-defender; techdocs.f5.com DHD Setup (updated 02/27/2025)

### [DDOS] Behavioral L7 DoS for NGINX (cloud-native)
- solution_area: DDoS Protection
- capability_name: F5 DoS for NGINX — machine-learning application-layer DoS protection
- plain_description: A lightweight, software-native L7 DoS module running on NGINX Plus and NGINX Ingress Controller that uses machine learning to baseline normal behavior and auto-mitigate anomalies (HTTP GET/POST floods, slow attacks like Slowloris/Slow POST/Slow Read, Challenger Collapsar), tracking 300+ behavior metrics with adaptive no-touch policy and eBPF/XDP-accelerated mitigation.
- delivered_by: F5 DoS for NGINX (formerly NGINX App Protect DoS); part of the NGINX One premium package
- attribution_confidence: High
- customer_problem_solved: App and platform teams in DevOps/Kubernetes environments need consistent L7 DoS protection deployed as code, per-pod or at the ingress, without a heavyweight appliance.
- fit_signals: "We're cloud-native / Kubernetes-first," "we run NGINX Plus or NGINX Ingress Controller," "our app teams own security, not a central NetOps team," "we want security as code in the CI/CD pipeline," "we need per-service DoS protection at the pod level," microservices/API-gateway architectures.
- disqualifiers: Volumetric L3/4 attacks (NGINX can't absorb a flood — need XC scrubbing); traditional on-prem network teams without NGINX; customers not using NGINX at all.
- value_framing: DoS protection that lives with the app, deploys as code, scales in Kubernetes, and needs no manual tuning — single-vendor consolidation with the rest of the NGINX stack.
- product_routing_note: Lead with F5 DoS for NGINX for cloud-native/DevOps buyers already on NGINX. Name check: renamed from "NGINX App Protect DoS"; its sibling WAF was renamed to "F5 WAF for NGINX" at v5.9 (Sep 2025); the DoS product is now "F5 DoS for NGINX." Both are in NGINX One. gRPC/HTTP2 support was added after v1 (v2), WebSocket in v4 — verify version if the customer asks about protocol coverage.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/nginx/f5-waf-for-nginx/denial-of-service; docs.nginx.com/nginx-app-protect-dos; DevCentral "Introducing F5 WAF for NGINX" (rename)

### [DDOS] Hardware-accelerated (FPGA) mitigation
- solution_area: DDoS Protection
- capability_name: FPGA/ePVA hardware-accelerated DDoS and SYN-flood mitigation
- plain_description: F5 appliances (rSeries mid/high-end, VELOS blades) use FPGAs (the ePVA lineage) to offload SYN-flood protection and detection/mitigation of 100+ DoS/DDoS attack vectors at line rate, keeping legitimate traffic flowing and freeing CPU.
- delivered_by: rSeries (r5000/r10000 with FPGAs), VELOS (BX110/BX520 blades); underpinning BIG-IP AFM / DHD
- attribution_confidence: High
- customer_problem_solved: Sustaining mitigation at very high throughput (100Gbps+) without CPU exhaustion, so one application under attack doesn't degrade others.
- fit_signals: "We need line-rate DDoS at the data-center edge," "we're a service provider / 5G / high-throughput environment," "we can't have DDoS processing starve our CPUs," "we're refreshing from VIPRION/iSeries to rSeries/VELOS."
- disqualifiers: SaaS/cloud-native buyers (irrelevant — no appliance); small enterprises whose throughput needs are met in software (rSeries r2000/r4000 have no FPGA and perform these functions in software).
- value_framing: Hardware that mitigates in silicon at line rate, so attacks don't cost you performance; consolidate services on modern FPGA platforms and lower TCO.
- product_routing_note: Position hardware as a delivery detail of AFM/DHD, not a standalone DDoS product. Note r2000/r4000 lack FPGAs (software mitigation). Cross-reference doc 12 for service-provider scale (S/Gi-LAN/N6 consolidation, 5G).
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com rSeries & VELOS product pages; clouddocs.f5.com rSeries/VELOS Performance and Sizing

### [DDOS] Hybrid signaling (on-prem to cloud scrubbing)
- solution_area: DDoS Protection
- capability_name: Hybrid signaling / cloud offload when the pipe is threatened
- plain_description: On-prem F5 devices detect volumetric attacks locally and signal for cloud scrubbing; the customer or SOC redirects the attacked prefix (via BGP/API) to F5's cloud so the flood is scrubbed upstream before it saturates the internet link.
- delivered_by: BIG-IP AFM / DDoS Hybrid Defender (on-prem detection) + F5 Distributed Cloud DDoS Mitigation (cloud scrubbing)
- attribution_confidence: Medium (mechanism well documented historically with Silverline; verify current XC signaling integration specifics)
- customer_problem_solved: On-prem devices give surgical control under normal conditions but fail when the upstream pipe saturates; hybrid signaling gives on-box primary defense with cloud burst capacity for the big attacks.
- fit_signals: "We want on-prem control but need a safety net for the huge attacks," "we run multiple transit providers," "we want automatic failover to cloud scrubbing," "our appliance can't handle a full volumetric attack."
- disqualifiers: Cloud-native/SaaS-only customers (no on-prem device to signal from); customers content with a single delivery model.
- value_framing: Best of both worlds — precise local mitigation plus multi-terabit cloud capacity that engages only when you need it.
- product_routing_note: Historically DHD/AFM signaled to Silverline (the documented "Hybrid Signaling" feature); with Silverline EoL, the modern pattern is on-prem BIG-IP + XC cloud scrubbing (attack prefix announced via API/Console and BGP peering/GRE). Public documentation of the exact XC hybrid-signaling handshake is thinner than the old Silverline docs — flag as "verify" and avoid over-claiming automation.
- maturity_flag: GA (legacy Silverline path); XC integration specifics — verify
- source_currency_flag: Possibly stale
- source: wtit.com Silverline DDoS (Hybrid Signaling); wtit.com F5 XC DDoS (cloud activation); techdocs.f5.com DHD

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

Route on the customer's dominant problem, footprint, and operating model:

- **Volumetric attack exceeding the pipe / owns IP space / wants managed** → **F5 Distributed Cloud DDoS Mitigation** (Routed Mode, Always-On or Always-Available). This is also the landing spot for any customer mentioning **Silverline** (retired; migrate to XC — see below).
- **No routable prefix, protect specific web apps, DNS-based onboarding** → **XC DDoS Proxy Mode** / XC WAAP (coordinate with doc 01/03).
- **On-prem/data-center requirement, already owns BIG-IP, wants firewall + DDoS consolidation, data residency** → **BIG-IP AFM** DoS profiles.
- **Wants a dedicated, purpose-built on-prem DDoS device with SSL visibility and cloud burst** → **BIG-IP DDoS Hybrid Defender** (verify packaging).
- **Cloud-native / Kubernetes / DevOps, runs NGINX, security-as-code** → **F5 DoS for NGINX** (NGINX One).
- **Very high throughput / line-rate at the edge / service provider** → AFM or DHD **on rSeries/VELOS** FPGA hardware (delivery detail; cross-ref doc 12 for SP scale).
- **Wants on-prem primary + cloud safety net** → **hybrid**: on-prem BIG-IP (AFM/DHD) + XC cloud scrubbing.

Buyer persona tells: NetOps/SecOps and network architects → AFM/DHD/XC Routed; DevOps/platform/app teams → F5 DoS for NGINX; CISO/exec wanting managed + SLA → XC managed SOC.

**Silverline → XC migration framing (installed base):** F5 announced Silverline End of Life effective **30 June 2025** (End-of-Sale March 2024). The designated replacement is the **F5 Distributed Cloud platform**, positioned as more capable (WAAP vs. Silverline's WAF-centric scope) with a larger global network (F5's own case study describes Distributed Cloud as "not only a WAF but web application and API protection … more robust"). F5 migrated its own f5.com off Silverline to XC. When a customer says "we use Silverline for DDoS," treat it as an **active migration opportunity to XC DDoS**, and reference F5's white-glove managed migration support. Do not tell a customer Silverline is still available for new purchase — it is not.

Coexistence: A customer can run any combination (or none). Common healthy combinations: BIG-IP AFM/DHD on-prem + XC cloud scrubbing (hybrid); NGINX DoS at the app tier + XC at the edge. Do not assume an existing footprint.

Where the public record is thin: the exact current hybrid-signaling handshake between on-prem BIG-IP and XC (post-Silverline) is not as clearly documented as the old Silverline integration — do not invent official F5 automation claims.

### 3b. Disqualifiers / anti-patterns (aggregate)

Signals this solution area is a weak fit or "not now":

- **"Our attacks are all application-layer / we just need to rate-limit an API"** → likely an API story (doc 01), not volumetric DDoS.
- **"We're worried about scrapers/credential stuffing"** without an availability impact → bot management (doc 03), not DoS.
- **"We only need a general firewall"** → not a DDoS conversation; note the corpus has no network-firewall doc (documented gap) — flag for the SE rather than forcing a DDoS pitch.
- **Small org, low public profile, no volumetric exposure, everything in one hyperscaler already covered by that cloud's native DDoS** → weak fit for a dedicated F5 DDoS buy; note the honest limits below in objection handling.
- **No NGINX and no BIG-IP and no appetite for a managed SaaS** → no natural F5 vehicle; too early.
- **Pure data-residency lock with zero tolerance for any cloud** → cloud scrubbing disqualified; only on-prem AFM/DHD applies, and only if volumetric scale is within pipe capacity.

### 3c. Competitive positioning and objection handling (all lower confidence)

Treat all competitive claims as lower-confidence; verify at deal time. The DDoS market consolidates fast, and third-party comparison sources are of mixed reliability.

**Cloud scrubbing — Cloudflare, Akamai Prolexic, AWS Shield / Azure DDoS.**
- Cloudflare: very large anycast network (Cloudflare's Q4 2025 DDoS threat report states its global network "has officially crossed 500 Tbps of external capacity"; it reports mitigating a record 31.4 Tbps attack in Nov 2025), strong self-service and free/low tiers for HTTP; non-HTTP protection requires Magic Transit (enterprise BGP). F5's counter: managed SOC with human-led mitigation and a hybrid on-prem+cloud story for customers who already own BIG-IP/NGINX.
- Akamai Prolexic: established, dedicated scrubbing centers, strong enterprise SLAs and BGP diversion; third-party sources note it is a mitigation service with limited between-attack visibility. F5's counter: same managed-SOC/BGP-scrubbing category, plus F5's broader app-security platform (WAAP, NGINX, BIG-IP) for single-vendor consolidation.
- AWS Shield / Azure DDoS: strong native integration but effectively bounded to that cloud (Microsoft disclosed a 15.72 Tbps Azure-mitigated flood in Oct 2025, underscoring hyperscaler scale — but native protection stays within that provider's environment). F5's counter: cloud-agnostic protection across on-prem, multi-cloud, and edge — see the ISP/cloud objection below.

**Dedicated appliances — NETSCOUT Arbor, Radware, A10.**
- NETSCOUT (Arbor): appliance-first DDoS pedigree, strong in service-provider/ISP; NETSCOUT also acquired DigiCert's DDoS/WAF services (now folded into NETSCOUT), and per Omdia's DDoS Prevention Technology Market Tracker was a top-two vendor in 2H24. F5's counter: consolidation of firewall + DDoS + DNS + app security on BIG-IP, and a cloud scrubbing option under one vendor.
- Radware: DefensePro appliances + cloud, independent (NASDAQ-listed, part of the Rad Group). A10: Thunder TPS appliances (A10 Networks, independent). F5's counter: same platform-consolidation and hybrid narrative; FPGA line-rate hardware.
- Verify independence/acquisition status at deal time — this market moves.

**ISP-provided mitigation.** Common baseline; frequently blackhole/null-route based.

**Objection: "Our ISP / cloud provider already includes DDoS protection."**
Response (evidence-based, non-disparaging): ISP and hyperscaler-native DDoS are genuinely effective for coarse volumetric floods, but have three well-documented gaps: (1) **ISP mitigation often relies on blackholing/null-routing**, which stops the flood by taking the victim IP offline — the attacker's goal (unavailability) is still achieved; (2) native cloud DDoS is typically **bounded to that provider's own environment**, leaving hybrid/multi-cloud/on-prem assets uncovered and offering limited packet-level forensics; (3) both are weaker against **sophisticated application-layer (L7) and low-and-slow attacks** that don't saturate bandwidth — these need behavioral L7 detection (XC L7 DoS or F5 DoS for NGINX). Position F5 as complementary where those gaps matter: managed SOC, cross-environment coverage, L7 behavioral mitigation, and full attack forensics. F5 Labs' DDoS trend data is useful value framing here — the 2024 DDoS Attack Trends report recorded 2,127 attacks in 2023 (a 112% year-over-year rise), with the telecommunications and banking sectors each seeing an approximately fivefold increase in incidents, and software/computer services the single most-targeted sector at 37% of attacks.

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify every refresh):**
- **Silverline DDoS Protection** → **retired; End of Life 30 June 2025** (EoS March 2024). Replacement: **F5 Distributed Cloud DDoS Mitigation**. Installed-base customers will still say "Silverline." High confidence, sourced (my.f5.com K000150427).
- **NGINX App Protect DoS** → **F5 DoS for NGINX**; sibling **NGINX App Protect WAF** → **F5 WAF for NGINX** (v5.9, Sep 2025). Both in **NGINX One** premium package. Functionality/code/config unchanged — branding only. High confidence, sourced (docs.nginx.com; DevCentral).
- **DDoS Hybrid Defender (DHD)** → still marketed by F5 as of mid-2026 (product page live), but its relationship to AFM and to current platforms (rSeries/F5OS) is a live question, and older Herculon-branded DHD appliances went End-of-Sale. (The BIG-IP Next ADC line is discontinued — K000152956, see docs 05/14 — so a "DHD on BIG-IP Next" path is moot, not merely unverified.) **Verify packaging and cloud-signaling target (post-Silverline).**
- **XC DDoS capacity/footprint figures** — "more than 12+ Tbps" (current solution-overview PDF), 13 Tbps / 24 Regional Edges / 22 metro regions (2023 service description), "multi-terabit" (live product page). F5's own documents conflict (one older PDF even says "3 Tbps" in one section). Treat specific numbers as possibly stale.

**Explicitly not verified (do not assert):**
- The exact current hybrid-signaling handshake/automation between on-prem BIG-IP (AFM/DHD) and XC cloud scrubbing after Silverline's retirement.
- Whether DHD has a formally announced go-forward packaging or a specific rSeries/VELOS-only SKU. (A migration path to BIG-IP Next is no longer a question to verify — that ADC line is discontinued, K000152956.)
- Current precise scrubbing capacity — F5 sources give 12+ Tbps and 13 Tbps in different documents and "multi-terabit" on the live page; no single reconciled current figure was found.
- Whether the 99.99% (XC) vs 99.999% (legacy Silverline) uptime difference reflects a deliberate SLA change or documentation drift — the current authoritative figure is 99.99%, with 15-minute TTN and 15-minute TTM carried over from the Silverline SLA.

**Primary sources leaned on:** f5.com XC DDoS product page, solution-overview PDF, and service-description PDF; docs.cloud.f5.com (Routed DDoS, release changelogs through Mar 2026); techdocs.f5.com (AFM DoS, DHD Setup); docs.nginx.com (F5 DoS/WAF for NGINX); f5.com rSeries/VELOS pages and clouddocs sizing guides; my.f5.com K000150427 (Silverline EoL); DevCentral technical articles; F5 Labs 2023/2024 DDoS attack trend reports.
**Third-party sources (competitive reality-check, lower trust):** Gartner Peer Insights; Cloudflare Q4 2025 DDoS threat report; Omdia market-share reference (via NETSCOUT); Flowtriq, Fastly, Indusface, Kentik comparison commentary. SEO "best tools" listicles treated as low-trust and not used for F5 feature attribution.