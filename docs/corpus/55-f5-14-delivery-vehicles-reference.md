# F5 Delivery Vehicles & Platform Reference (Doc 14)

doc_id: 14-delivery-vehicles-reference
solution_area: Delivery Vehicles & Platform Reference
doc_tag: PLAT
products_covered: rSeries, VELOS, iSeries, VIPRION, F5OS, BIG-IP TMOS (classic), BIG-IP Next, BIG-IP Virtual Edition (VE), BIG-IQ, F5 Insight, NGINX One / NGINX One Console, NGINX Plus, NGINX Open Source, F5 Distributed Cloud Services (Essentials/Enterprise), Customer Edge (CE), Flex Consumption Program (FCP)
compiled: July 2026
primary_release_anchor: F5 AppWorld 2026 (March 11, 2026) — ADSP evolution, F5 Insight GA, Distributed Cloud Essentials/Enterprise packaging; BIG-IP 21.0 (Nov 2025) and 21.1 (GA June 2026)
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

This is a thin lookup reference, not a pitch. Its job is to let a downstream agent interpret a platform/footprint statement heard on a sales call ("we have VIPRIONs," "we're on VELOS," "we bought NGINX One," "we're on 14.x") and immediately understand (a) what the thing is, (b) whether it signals a refresh/modernization opportunity, and (c) what the current/successor product is. Deep capability content (WAF, bot defense, DNS features, etc.) belongs to sibling documents — this doc covers only delivery vehicles, platforms, management planes, and packaging.

How F5's delivery vehicles relate:

- **Hardware appliances/chassis** run F5 software. The current generation is **rSeries** (appliance) and **VELOS** (chassis), both running the **F5OS** platform OS (Kubernetes-based). The prior generation is **iSeries** (appliance) and **VIPRION** (chassis), both running classic **BIG-IP TMOS** directly. Hearing a legacy platform name = a refresh conversation toward rSeries/VELOS.
- **BIG-IP software** comes in two lineages: classic **TMOS** (the 20-year-old software line, current LTS 17.x, next major 21.x) and **BIG-IP Next** (the re-architected line that F5 discontinued). The important, counterintuitive fact for 2026: **F5 reversed course — BIG-IP Next is discontinued and F5 is modernizing TMOS instead.** In F5's own words from the v21.0 launch blog: "many of you are likely aware of F5's recent decision to discontinue BIG-IP Next and refocus on modernizing the BIG-IP TMOS software suite… This new chapter begins today with the availability of F5 BIG-IP v21.0." TMOS is the go-forward software. (Scope note: the discontinuation covers the TMOS-successor ADC software line only — **BIG-IP Next for Kubernetes** and **BIG-IP Next CNFs** are separate, active product lines; see the BIG-IP Next record below and docs 10/11/12.)
- **Software/virtual form factors**: **BIG-IP Virtual Edition (VE)** runs the same TMOS software in hypervisors and public clouds (marketplace images).
- **Management planes**: **BIG-IQ** centrally manages BIG-IP (TMOS) fleets. **F5 Insight** (new at AppWorld 2026) is an observability/analytics plane for BIG-IP — it does not replace BIG-IQ.
- **SaaS / edge**: **F5 Distributed Cloud (XC)** is delivered as SaaS, with the **Customer Edge (CE)** node as its in-environment deployment vehicle. New simplified packaging (**Essentials** and **Enterprise**) replaced dozens of SKUs at AppWorld 2026.
- **NGINX**: **NGINX Open Source** (free) vs **NGINX Plus** (commercial). **NGINX One** is the unifying subscription package; **NGINX One Console** is its SaaS fleet-management plane (hosted in Distributed Cloud).
- **Consumption**: the **Flex Consumption Program (FCP)** is F5's enterprise-wide 3-year subscription spanning the portfolio.
- **Software delivery cadence (changed July 2026)**: F5 moved from quarterly to **monthly hardened software releases** — shipping the third Wednesday of every month, starting July 15, 2026 — across BIG-IP, BIG-IQ, F5OS, and NGINX, with **monthly security notifications** replacing the quarterly notification rhythm (first monthly notification August 19, 2026, covering vulnerabilities fixed in the July 15 release). Maintenance releases, major releases, and engineering hotfixes continue as needed. F5 urges customers to deploy each hardened release promptly and treat it as critical regardless of individual severity ratings, and is deliberately limiting per-fix disclosure detail to avoid handing attackers a vulnerability roadmap. (Source: f5.com blog "A faster release cadence: What's changing at F5, and what you need to do," July 6, 2026.)

Read each record below as self-contained. The EoL/EoS milestone table is the highest-value payload — legacy platform names on a call map to refresh timelines there.

## Layer 2 — Product records

### [PLAT] F5 rSeries
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 rSeries (appliance)
- former_names: none (positioned as the successor to iSeries); models r2000, r4000, r5000, r10000, r12000 series; FIPS models r5920-DF, r10920-DF
- what_it_is: F5's current-generation ADC hardware appliance line. A re-architected, API-first, multitenant platform running the F5OS-A operating system, which hosts BIG-IP (TMOS) tenants. Mid/high-end models (r5000/r10000/r12000) use FPGA hardware offload; entry models (r2000/r4000) do offload in software.
- role_in_deals: The recommended replacement target for iSeries refreshes. Footprint signal that a customer is on current hardware. Per F5's rSeries datasheet, the platform "uses FPGA technology to deliver twice the scale and performance of the iSeries generation."
- modernization_implication: Hearing "rSeries" = customer is already modernized on hardware. Upsell adjacencies: additional tenants (multitenant by default), pay-as-you-grow CPU licensing, BIG-IP 17.x/21.x software currency, F5 Insight attach.
- status: Current
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/rseries-adc-hardware-appliance; F5 rSeries datasheet; clouddocs.f5.com rSeries training

### [PLAT] F5 VELOS
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 VELOS (chassis)
- former_names: none (positioned as the successor to VIPRION); CX410 and CX1610 chassis; BX110 and BX520 blades
- what_it_is: F5's current-generation chassis-and-blade ADC hardware, running the F5OS-C platform OS (system controllers + chassis partitions). Hosts BIG-IP (TMOS) tenants. Scales to multi-terabit throughput; CX410 holds up to 8 BX110 blades, CX1610 up to 16 BX520 blades.
- role_in_deals: The recommended replacement target for VIPRION refreshes. Footprint signal that a customer needs chassis-class density/scale on current hardware.
- modernization_implication: Hearing "VELOS" = modernized chassis customer. Upsell adjacencies: chassis partitions, additional blades, software currency, F5 Insight.
- status: Current
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/velos-hardware-chassis-and-blades; techdocs.f5.com VELOS platform guide

### [PLAT] F5OS
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5OS (F5OS-A for rSeries, F5OS-C for VELOS)
- former_names: sometimes described as "F5OS-C" for the chassis variant
- what_it_is: The Kubernetes-based platform operating system layer on rSeries and VELOS. It manages tenants, networking, users, and system config, and hosts BIG-IP (TMOS) as guest tenants. Tightly integrated with TMOS.
- role_in_deals: Not sold standalone — it is the OS that ships with rSeries/VELOS. Its presence is what distinguishes current-gen hardware from iSeries/VIPRION (which run TMOS directly on the metal).
- modernization_implication: If a customer mentions F5OS, they are on current hardware. F5OS was originally described as the layer that would host the next-generation BIG-IP Next tenants; with BIG-IP Next discontinued, F5OS now hosts TMOS (17.x and 21.x) tenants going forward.
- status: Current
- source_currency_flag: Current
- source: clouddocs.f5.com F5OS provider overview; techdocs.f5.com

### [PLAT] BIG-IP iSeries (legacy appliance)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: BIG-IP iSeries
- former_names: iSeries; models i850, i2000/i2600/i2800, i4000/i4600/i4800, i5000/i5600/i5800, i7000, i10000, i11000; FIPS models i5820-DF, i7820-DF
- what_it_is: F5's prior-generation ADC appliance line, running classic BIG-IP TMOS directly on the appliance. Superseded by rSeries.
- role_in_deals: A hearing of "iSeries" on a call is a strong refresh trigger. EoS already occurred; EoSS/EoTS milestones are approaching (see milestone table).
- modernization_implication: Per K5903, "For iSeries or VIPRION hardware products, End of Software Support (EoSS) is scheduled for January 1, 2027; October 1, 2027; or April 1, 2026. To continue receiving software support, customers must transition to rSeries or VELOS hardware." The main iSeries line reached End of Sale January 1, 2024 (EoSS January 1, 2027); FIPS models i5820-DF/i7820-DF reached EoS January 1, 2026 (EoSS October 1, 2027). Replacement path is rSeries (e.g., i5820-DF → r5920-DF). Hardware and software lifecycles are independent — an iSeries under RMA can still be running out-of-support TMOS.
- status: EOL announced — EoS January 1, 2024 (main line); EoS January 1, 2026 (i5820-DF/i7820-DF FIPS)
- source_currency_flag: Current
- source: my.f5.com K000133583 (iSeries EoS); my.f5.com K000151744 (i5820-DF/i7820-DF EoS); K5903; K4309 lifecycle policy

### [PLAT] BIG-IP VIPRION (legacy chassis)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: BIG-IP VIPRION
- former_names: VIPRION; B2150/B2250 blades, C2200/C2400 (2000-series) chassis; older B4200/B4300 blades, C4400/C4480 (4000-series) chassis
- what_it_is: F5's prior-generation chassis-and-blade ADC hardware, running classic BIG-IP TMOS. Superseded by VELOS.
- role_in_deals: "We have VIPRIONs" is one of the strongest refresh triggers in the F5 install base — chassis-class, aging, with EoSS reached. Route toward VELOS.
- modernization_implication: VIPRION 2000-series (B2150, B2250, C2200, C2400) reached EoS April 1, 2023; EoSS April 1, 2026 (per K95877400 and K5903). Older 4000-series reached EoL years earlier (EoTS April 1, 2021). Replacement path is VELOS (CX410/CX1610). Customers at/past EoSS receive no CVE/security fixes.
- status: EOL announced — EoS April 1, 2023 (2000-series); older 4000-series retired
- source_currency_flag: Current
- source: my.f5.com K95877400 (VIPRION 2000-series EoS); my.f5.com K14291 (VIPRION 4000-series EoS); K5903; K4309

### [PLAT] BIG-IP (classic / TMOS)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: BIG-IP (TMOS software)
- former_names: "classic BIG-IP," "TMOS," "BIG-IP classic" — distinct from BIG-IP Next
- what_it_is: F5's flagship application delivery and security software, running the Traffic Management Operating System (TMOS). ~20-year lineage. Runs on iSeries/VIPRION directly, as tenants on rSeries/VELOS (F5OS), and as Virtual Edition. Modules include LTM, DNS (formerly GTM), Advanced WAF/ASM, APM (now BIG-IP Zero Trust Access), AFM, SSL Orchestrator.
- role_in_deals: The core install base. Version heard on a call drives EoSD/EoTS implications (see table). Current LTS is 17.1.x/17.5.x; 21.0 shipped Nov 2025; 21.1 GA June 2026 (announced June 4, 2026).
- modernization_implication: F5 recommends running v17.1 at minimum. v16.1.x reached EoSD/EoTS July 31, 2025 (FIPS Validated platforms and VE FIPS Addon license extend to July 31, 2026 per K000139937); v15.1.x EoTS Dec 31, 2024 (non-FIPS). "We're on 14.x/15.x/16.x" = software refresh needed. Support windows are shortening: per K5903, "Beginning with BIG-IP 21.0.0, Short-Term Stability Releases will have a software lifecycle of 9 months—reduced from 12 months… Beginning with BIG-IP 21.1.0, Long-Term Stability Releases will have a three-year Standard Support phase from First customer ship date, reduced from four years with previous software versions." Separately, as of July 2026 F5 ships hardened software releases monthly (third Wednesday of each month, starting July 15, 2026) with monthly security notifications (first: August 19, 2026) across BIG-IP, BIG-IQ, F5OS, and NGINX — customers on a quarterly patching rhythm need a faster upgrade process (f5.com blog, July 6, 2026).
- status: Current — go-forward software line
- source_currency_flag: Current
- source: my.f5.com K5903 (BIG-IP software support policy); K000139937; K000152956; f5.com/products/big-ip-upgrade

### [PLAT] BIG-IP Next
- solution_area: Delivery Vehicles & Platform Reference
- product_name: BIG-IP Next
- former_names: marketed as "the next generation of BIG-IP software"; components included BIG-IP Next Central Manager, BIG-IP Next LTM/WAF/Access/DNS
- what_it_is: A re-architected BIG-IP software line (separate control/data planes, containerized, managed by BIG-IP Next Central Manager) that F5 developed as the intended successor to TMOS. Modules had reached availability including LTM, WAF, Access, DNS, and SSLO.
- role_in_deals: CRITICAL CURRENCY NOTE — F5 made a strategic decision to STOP development of BIG-IP Next and instead modernize TMOS. Per K5903: "F5 has made the strategic decision to stop development of BIG-IP Next and instead modernize its BIG-IP TMOS software. BIG-IP Next 20.3 was the final version of BIG-IP Next, and this version reached end of life on April 30, 2025. For more information, refer to K000152956." If a customer says "we're planning to move to BIG-IP Next," correct gently: the go-forward path is TMOS 17.x → 21.x on rSeries/VELOS.
- modernization_implication: Do not position BIG-IP Next as the future. F5 committed to continuity of TMOS with future 17.x releases and continued hardware investment (rSeries/VELOS supporting 17.x and 21.x). Central Manager was BIG-IP Next's management plane; with Next discontinued, BIG-IQ remains the TMOS management plane.
- status: Retired/absorbed — development stopped; final version 20.3 reached EoL April 30, 2025; strategy folded back into TMOS modernization. IMPORTANT DISAMBIGUATION: this applies to the TMOS-successor ADC software line only — "BIG-IP Next for Kubernetes" (SPK lineage / NVIDIA DPU) and "BIG-IP Next Cloud-Native Network Functions (CNFs)" are separate, actively developed product lines and are NOT discontinued (see docs 10, 11, 12)
- source_currency_flag: Current
- source: my.f5.com K000152956 (BIG-IP strategic update: Modernizing BIG-IP TMOS and discontinuing BIG-IP Next); K5903; f5.com/company/blog (BIG-IP v21.0 launch)

### [PLAT] BIG-IP Virtual Edition (VE)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: BIG-IP Virtual Edition (VE)
- former_names: BIG-IP VE; "Per-App VE" for the per-application variant; cloud "PAYG" marketplace editions
- what_it_is: The software/virtual form factor of BIG-IP (TMOS), deployable on hypervisors (VMware, KVM, Hyper-V) and public clouds (AWS, Azure, GCP, Alibaba, IBM Cloud, OCI) via marketplace images. Same TMOS software and modules as hardware.
- role_in_deals: Footprint signal for hybrid/cloud customers. Marketplace PAYG editions come in GOOD/BETTER/BEST (GBB) license bundles at various throughput tiers. Refresh/attach: hardware-to-VE migration (supply-chain flexibility), cloud migration, Flex Consumption licensing.
- modernization_implication: VE lifecycle aligns with the BIG-IP software version in use (e.g., 15.x VE EoSD/EoTS Dec 31, 2024). A customer on old VE software needs the same version upgrade as hardware. Consumption models: subscription, PAYG/utility, FCP, BYOL, perpetual.
- status: Current
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/virtual-editions; AWS Marketplace F5 BIG-IP VE listings

### [PLAT] BIG-IQ
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 BIG-IQ Centralized Management
- former_names: BIG-IQ Centralized Management (CM)
- what_it_is: The centralized management plane for BIG-IP (TMOS) fleets — device discovery/inventory, TMOS software upgrades, license management (including VE license pools), config backup/restore, and security policy management for ASM/AFM. Available as hardware or Virtual Edition.
- role_in_deals: Attach for customers with multiple BIG-IP devices. Current release line is 8.4.x (8.4.0 March 2025; 8.4.1/8.4.2 add support for BIG-IP 17.5.1.x and 21.0).
- modernization_implication: BIG-IQ remains current and is a key ADSP component. It is NOT superseded by F5 Insight — Insight is observability/analytics, BIG-IQ is management/orchestration/licensing. Do not assert that Insight replaces BIG-IQ. With BIG-IP Next discontinued, BIG-IP Next Central Manager is not the go-forward manager; BIG-IQ manages the TMOS fleet.
- status: Current
- source_currency_flag: Current
- source: techdocs.f5.com BIG-IQ 8.4.0 release notes; community.f5.com "What's New in BIG-IQ v8.4.1"

### [PLAT] F5 Insight (for ADSP)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 Insight for ADSP
- former_names: none (new; grew from an internal F5 field-engineering project; draws on Threat Stack and Fletch acquisitions)
- what_it_is: An observability/analytics plane for the F5 ADSP, initially for BIG-IP. Uses open-source components (OpenTelemetry collector, VictoriaMetrics time-series DB, Grafana dashboards) plus an AI assistant (MCP + LLM integration). Deployed as a lightweight qcow image; available self-managed with a SaaS model forthcoming.
- role_in_deals: Attach/adjacency for BIG-IP customers wanting unified visibility and, as of v1.2 (July 2026), fleet software-lifecycle visibility and guided TMOS update workflows. Announced GA at AppWorld 2026 (March 2026).
- modernization_implication: Hearing "F5 Insight" = customer is engaging with the modern ADSP observability story. It complements, and does not replace, BIG-IQ. Plans to extend beyond BIG-IP to NGINX and Distributed Cloud were stated as forward-looking.
- status: Current — GA for BIG-IP (announced AppWorld 2026)
- source_currency_flag: Current
- source: f5.com/products/f5-insight; f5.com press release (AppWorld 2026); Network World coverage; BusinessWire (July 15, 2026 fleet management)

### [PLAT] NGINX One / NGINX One Console
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 NGINX One (package) / F5 NGINX One Console (management plane)
- former_names: NGINX One Console launched March 2024; supersedes NGINX Amplify (Amplify retires January 31, 2026) for monitoring; incorporates NGINX Instance Manager capabilities
- what_it_is: NGINX One is an all-in-one subscription package unifying NGINX capabilities (NGINX Plus, NGINX Ingress Controller / Gateway Fabric, NGINX One Console, NGINX Instance Manager, and support; F5 WAF for NGINX in the premium tier/as add-on). NGINX One Console is its SaaS fleet-management service, hosted in F5 Distributed Cloud — centralized config, monitoring, CVE detection, certificate management, and an AI assistant across NGINX Open Source and NGINX Plus instances.
- role_in_deals: "We bought NGINX One" = customer has the unified NGINX subscription and console access. Console is included with NGINX and Distributed Cloud subscriptions. Fleet-management footprint signal; adjacency to Distributed Cloud security services.
- modernization_implication: Existing NGINX customers can move to NGINX One at no extra charge (contact account manager). Amplify users must migrate before Jan 31, 2026. Console adds enterprise fleet features on top of open-source NGINX — an on-ramp to NGINX Plus/commercial conversations.
- status: Current
- source_currency_flag: Current
- source: docs.nginx.com/nginx-one-console; f5.com/products/nginx/one and /one-console; blog.nginx.org (Amplify EoL); community.f5.com NGINX One Console updates

### [PLAT] NGINX Open Source vs NGINX Plus
- solution_area: Delivery Vehicles & Platform Reference
- product_name: NGINX Open Source (free) / F5 NGINX Plus (commercial)
- former_names: "NGINX OSS"; NGINX Plus sometimes "NGINX subscription"
- what_it_is: NGINX Open Source is the free, BSD-licensed web server / reverse proxy / load balancer. NGINX Plus is the commercial edition on the same core engine, adding enterprise capabilities and vendor support.
- role_in_deals: "We use NGINX open source" = commercial conversion opportunity toward NGINX Plus / NGINX One. What Plus adds over OSS: active health checks, dynamic upstream reconfiguration without reloads, session persistence, the live activity monitoring dashboard, API-driven configuration, JWT/OIDC authentication, enhanced DNS service discovery, key-value store, clustering/HA state sharing, and 24×7 commercial support.
- modernization_implication: OSS in production = candidate for Plus (operational risk reduction, support) and for NGINX One (fleet visibility, CVE detection). F5 WAF for NGINX (formerly NGINX App Protect) attaches to Plus as an add-on.
- status: Current (both)
- source_currency_flag: Current
- source: docs.nginx.com; f5.com/products/nginx; third-party comparisons

### [PLAT] F5 Distributed Cloud Services — packaging (Essentials / Enterprise)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 Distributed Cloud Services (XC) — Essentials and Enterprise packages
- former_names: previously sold as dozens of individual service SKUs / à la carte (WAAP, Bot Defense, API Security, CDN, DNS, Multi-Cloud Network Connect, App Stack, etc.)
- what_it_is: F5's SaaS-based security, networking, and app-management platform. At AppWorld 2026 (March 2026) F5 replaced dozens of SKUs with two consumption-based starter packages. Essentials: foundational app delivery and security — WAF, API protection, DDoS mitigation, and content delivery (CDN), for public-facing apps. Enterprise: builds on Essentials for advanced security, hybrid multicloud, internal application protection, and deeper visibility/control.
- role_in_deals: "We're on XC" or "we bought Distributed Cloud" — determine which package. New bundles simplify buying and expansion. Consumption metered across a small number of consistent metrics.
- modernization_implication: Older XC customers may still be on legacy per-service SKUs; the Essentials/Enterprise packaging is the current buying motion. Tier names are new as of March 2026 — treat as perishable.
- status: Current — packaging announced AppWorld 2026 (March 11, 2026)
- source_currency_flag: Current
- source: f5.com blog "F5 Distributed Cloud Services reimagined for the platform era"; BusinessWire AppWorld 2026 press release

### [PLAT] Customer Edge (CE) node
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 Distributed Cloud Customer Edge (CE)
- former_names: sometimes referenced by Volterra heritage (ves.io); "Secure Mesh Site" / "App Stack Site" are CE deployment personas
- what_it_is: The software-defined deployment vehicle that extends the F5 Distributed Cloud SaaS platform into customer environments (data centers, public clouds, edge). A Linux-based software appliance (ISO or K8s deployment spec) deployed in a VM, K8s cluster, commodity hardware, or F5 edge hardware. Registers to the F5 Global Network via zero-touch provisioning; single-node for POC, three-node cluster for production HA.
- role_in_deals: "We have a CE" / "Customer Edge" = customer is running XC services locally. Two personas: Mesh (networking/security enforcement + distributed load balancing) and App Stack (managed K8s for hosting workloads).
- modernization_implication: CE is the on-ramp to consuming XC security/networking services in-environment. Footprint signal for multicloud networking and local WAAP enforcement. Upgraded centrally from the XC Console.
- status: Current
- source_currency_flag: Current
- source: docs.cloud.f5.com Customer Edge concepts; f5.com CE deployable software datasheet

### [PLAT] Flex Consumption Program (FCP)
- solution_area: Delivery Vehicles & Platform Reference
- product_name: F5 Flex Consumption Program (FCP)
- former_names: "Flexible Consumption Program"; FCP-B is the Distributed Cloud variant
- what_it_is: F5's enterprise-wide, 3-year (36-month) subscription that grants access to a full suite of F5 products with deploy-as-needed flexibility and annual true-up/true-forward reconciliation against a spend commitment. One of F5's consumption options alongside perpetual, term subscription, and utility (PAYG).
- role_in_deals: A licensing/consumption signal, not a product. "We're on FCP" = enterprise agreement customer with portfolio-wide flexibility; expansion is frictionless (self-service licensing). Applies across BIG-IP, VE, BIG-IQ, and Distributed Cloud.
- modernization_implication: FCP customers can shift spend between products/form factors — a lever for hardware-to-software or on-prem-to-SaaS migration without renegotiating. Subscription program terms last updated March 13, 2026.
- status: Current
- source_currency_flag: Current
- source: f5.com/products/get-f5/flex-consumption-program; f5.com subscription program terms; docs.cloud.f5.com FCP for Distributed Cloud

## EOL / EOS milestone table (legacy hardware & software) — highest-value payload

Dates below are the refresh-trigger payload. Hardware and software lifecycles are independent (K4309, K5903). F5 default policy (stated verbatim in K4309): "three (3) years after the EoS date is the default hardware product EoSS date, and four (4) years after the hardware product EoSS date is the default hardware product EoTS and EoRMA dates."

| Platform / Version | End of Sale (EoS) | End of Software Support (EoSS) | End of Technical Support (EoTS) | Replacement | Source |
|---|---|---|---|---|---|
| VIPRION 2000-series (B2150, B2250, C2200, C2400) | April 1, 2023 | April 1, 2026 | April 1, 2030 (default policy; not stated verbatim in EoS notice) | VELOS (CX410/CX1610) | K95877400; K5903; K4309 |
| VIPRION 4000-series (B4200/C4400) | April 1, 2014 | reached EoL | April 1, 2021 | VELOS | K14291 |
| BIG-IP iSeries main line (i850, i2000, i4000, i5000, i7000, i10000, i11000) | January 1, 2024 | January 1, 2027 | January 1, 2031 (default policy; not stated verbatim) | rSeries (r2000/r4000/r5000/r10000) | K000133583; K5903; K4309 |
| BIG-IP iSeries FIPS (i5820-DF, i7820-DF) | January 1, 2026 | October 1, 2027 | Oct 1, 2031 (EoRMA stated; EoTS not published verbatim) | rSeries r5920-DF / r10920-DF | K000151744 |
| BIG-IP TMOS 14.1.x | — | December 31, 2023 | December 31, 2023 | Upgrade to 17.1+ | K5903 |
| BIG-IP TMOS 15.1.x (non-FIPS) | — | December 31, 2024 | December 31, 2024 | Upgrade to 17.1+ | K5903 |
| BIG-IP TMOS 16.1.x | — | July 31, 2025 (EoSD) | July 31, 2025 (FIPS Validated platforms / VE FIPS Addon to July 31, 2026) | Upgrade to 17.1+ | K5903; K000139937 |
| BIG-IP TMOS 17.1.x (LTS) | — | March 31, 2027 (EoSD/EoTS) | March 31, 2027 | Currently supported | K5903 |
| BIG-IP TMOS 17.5.x (LTS) | — | January 1, 2029 | January 1, 2029 | Currently supported | K5903 |
| BIG-IP Next (final v20.3) | — | April 30, 2025 (EoL) | April 30, 2025 | TMOS 17.x/21.x | K5903; K000152956 |

Seed K-articles for the downstream agent: **K5903** (BIG-IP software support policy), **K4309** (hardware lifecycle policy), **K11478** (EoL/EoS index), **K9476** (hardware/software compatibility matrix), **K000152956** (BIG-IP Next discontinuation), **K000139937** (16.1.x EoL), **K95877400** / **K000133583** / **K000151744** (specific EoS announcements).

## Layer 3 — Routing / interpretation guidance

### 3a. Interpreting footprint statements (keyed on what's heard)

- **"We have VIPRIONs"** → Strongest chassis refresh trigger. 2000-series EoSS was April 1, 2026 — customer is at/past end of software support, no CVE fixes. Route toward **VELOS**. High urgency.
- **"We're on iSeries"** → Appliance refresh trigger. Main line EoSS January 1, 2027; FIPS models EoSS October 1, 2027. Route toward **rSeries**. Medium-high urgency (window closing).
- **"We're on VELOS / rSeries"** → Already modernized on hardware. Pivot to software currency (17.x/21.x), additional tenants/blades, F5 Insight attach. Not a hardware refresh.
- **"We're on 14.x / 15.x / 16.x TMOS"** → Software refresh (EoSD/EoTS reached or imminent). F5 recommends minimum v17.1; 21.x for latest features. This is independent of hardware — flag even if hardware is current.
- **"We're planning to move to BIG-IP Next"** → Correct the record: BIG-IP Next is discontinued (final v20.3 EoL April 30, 2025). Go-forward is modernized **TMOS 17.x → 21.x** on rSeries/VELOS. (Public record, K000152956 / K5903.)
- **"We use NGINX open source"** → Commercial conversation: **NGINX Plus** (support, active health checks, dynamic reconfig, dashboard) and **NGINX One** (fleet visibility, CVE detection via Console).
- **"We bought NGINX One"** → Customer has the unified subscription + Console. Confirm they've onboarded instances; adjacency to Distributed Cloud security. Amplify users must migrate by Jan 31, 2026.
- **"We use BIG-IQ"** → Management-plane customer. Confirm version (8.4.x current). F5 Insight is a complementary observability attach, not a replacement.
- **"We're on Distributed Cloud / XC"** → Determine package (Essentials vs Enterprise, new March 2026) or legacy per-service SKUs. CE nodes indicate in-environment enforcement.
- **"We're on FCP / Flex"** → Enterprise agreement; expansion is frictionless. Lever for form-factor migration.
- **"We patch F5 quarterly" / "we wait for the quarterly security notification"** → Update the mental model: as of July 2026, F5 ships hardened releases **monthly** (third Wednesday of each month) with monthly security notifications for BIG-IP, BIG-IQ, F5OS, and NGINX, and urges prompt deployment of each release, treated as critical regardless of individual CVE ratings. This is an operational-readiness conversation — and an attach angle for BIG-IQ (fleet upgrades) and F5 Insight (fleet software-lifecycle visibility, guided TMOS update workflows).

Where the public record does not clearly support a specific routing recommendation (e.g., exact successor SKU mapping for every legacy model, or whether a given customer's XC contract auto-migrates to Essentials/Enterprise), say so rather than inventing official F5 guidance.

### 3b. Disqualifiers / anti-patterns (platform refresh is a weak fit or "not now")

- Hardware is current-gen (rSeries/VELOS) and software is 17.1+/21.x — no refresh trigger; look to attach/upsell instead.
- Customer explicitly mid-migration to a competitor or to a pure-cloud/software strategy — a hardware refresh pitch may be tone-deaf; lead with VE/XC/NGINX software motions.
- Customer just completed a refresh (recent rSeries/VELOS purchase) — not a near-term hardware opportunity.
- Small/edge footprint where an appliance refresh is over-scoped — VE or CE may fit better.
- Legacy platform still within EoSS window AND under a compliance freeze — timing may be "not now" but keep the EoSS date on the radar.

### 3c. Bounded competitive / objection notes (platform-refresh only; lower confidence)

- **"We're virtualizing everything / moving off hardware."** — Legitimate; F5's answer is BIG-IP VE (same TMOS, marketplace images) and Distributed Cloud/NGINX for cloud-native. Note FPGA hardware offload (rSeries/VELOS) still matters for crypto-heavy/CGNAT/DDoS workloads; virtualization trades that for flexibility. (Lower confidence — depends on workload.)
- **"Third-party maintenance is cheaper than refreshing."** — Third parties (e.g., Park Place) extend support on EoL F5 hardware, but past EoSS F5 provides no CVE/security fixes or software development — a security/compliance risk, not just a support one. (Flagged; third-party sourcing.)
- **"We'll just stay on our current TMOS version."** — Past EoSD/EoTS means no hotfixes or security patches; independent of hardware support status. (Public, K5903.)

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (F5 renames frequently):**
- BIG-IP APM → **BIG-IP Zero Trust Access** (renamed; APM use cases continue).
- BIG-IP GTM → **BIG-IP DNS** (long-standing rename; both terms heard).
- ASM → **Advanced WAF** (both terms in use).
- NGINX App Protect → **F5 WAF for NGINX** (renamed).
- Distributed Cloud service SKUs → **Essentials / Enterprise** packages (new March 2026; treat tier names as perishable).
- "BIG-IP Next" — now a discontinued line, not the future; watch for stale collateral still positioning it as next-gen.

**Explicitly not verified / do not assert:**
- Exact EoTS/EoRMA dates for VIPRION 2000-series and iSeries main line are derived from F5 default lifecycle policy (EoSS + 4 yrs) via K4309, not stated verbatim in each EoS announcement — flagged in the table as "default policy."
- EoTS for iSeries FIPS i5820-DF/i7820-DF is not published verbatim (K000151744 lists EoS/EoSS/EoRMA only); EoRMA is Oct 1, 2031.
- Whether F5 Insight supersedes any BIG-IQ functionality: NOT asserted — public sources position Insight as observability and BIG-IQ as management; they are complementary.
- Whether F5 WAF for NGINX is in the base NGINX One subscription vs. a premium/add-on tier: F5 messaging is inconsistent; treat WAF as premium-tier/add-on, not universally bundled in all tiers.

**Primary sources leaned on:** my.f5.com K-articles (K5903, K4309, K11478, K9476, K000152956, K000139937, K95877400, K000133583, K000151744, K15073); techdocs.f5.com and clouddocs.f5.com (rSeries/VELOS/F5OS, BIG-IQ release notes); f5.com product pages, blog, and AppWorld 2026 press release; f5.com blog "A faster release cadence: What's changing at F5, and what you need to do" (July 6, 2026 — monthly hardened releases and monthly security notifications); docs.nginx.com and blog.nginx.org; DevCentral (community.f5.com).

**Third-party / lower-trust sources (corroboration only):** WorldTech IT (F5 partner, reproduces K4309/K5903 tables), Park Place Technologies (third-party maintenance), Network World / SiliconANGLE / CRN / BusinessWire / Help Net Security (AppWorld 2026 and July 2026 coverage). Treated as corroborating, not primary, for feature/attribution claims.