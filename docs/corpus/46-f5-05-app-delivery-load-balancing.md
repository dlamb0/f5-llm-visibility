# F5 Application Delivery & Load Balancing (ADC) — Solution Area Reference (Doc 05)
doc_id: 05-app-delivery-load-balancing
solution_area: Application Delivery & Load Balancing (ADC)
doc_tag: ADC
products_covered: BIG-IP LTM (TMOS), BIG-IP v21.x (modernized TMOS), F5 rSeries/VELOS hardware (F5OS), BIG-IP Virtual Edition, F5 NGINX Plus / NGINX One, F5 NGINXaaS for Azure, F5 Distributed Cloud App Connect / Load Balancer, F5 AI Assistant (iRules)
compiled: July 2026
primary_release_anchor: BIG-IP v21.1 GA (Q2 CY2026, announced AppWorld March 2026); AppWorld 2026
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

This document covers F5's heritage business: Layer 4–7 load balancing, traffic management, SSL/TLS offload, health monitoring, high availability, and programmability (iRules), across the full delivery-model spectrum from hardware to SaaS. In 2026 the live sales motions here are **not** feature novelty — they are **competitive displacement** (Citrix NetScaler and VMware Avi churn), **hardware refresh** (iSeries end-of-support), and **platform modernization** (classic TMOS moving to BIG-IP v21.x on rSeries/VELOS).

**The single most important naming correction for 2026:** F5 has **discontinued BIG-IP Next** as the re-platform for classic BIG-IP. In 2025 F5 announced it would stop development of BIG-IP Next and instead **modernize BIG-IP TMOS**, folding many capabilities originally envisioned for Next into the BIG-IP v21.x TMOS line. BIG-IP Next 20.3 was the final version and reached end of life April 30, 2025. The names "BIG-IP Next for Kubernetes" (BNK) and "BIG-IP Next Cloud-Native Network Functions" (CNFs) survive and are actively developed — but those are service-provider/Kubernetes products covered in sibling docs (10 for K8s), not the ADC re-platform. **Do not tell a customer to migrate to "BIG-IP Next" for classic LTM/ADC use cases.** The go-forward path is BIG-IP v21.x TMOS on rSeries/VELOS.

Which product carries the ADC story depends on the customer's footprint:
- **BIG-IP LTM (on TMOS, now v21.x)** — the flagship full-proxy ADC. On-prem/data-center, hardware (rSeries/VELOS) or Virtual Edition. Deep traffic engineering, iRules, SSL offload, FIPS.
- **F5 NGINX Plus / NGINX One** — lightweight software reverse proxy/load balancer for cloud-native, containerized, and DevOps-owned environments. NGINX One is the unified enterprise subscription/SaaS-console packaging.
- **F5 NGINXaaS for Azure** — fully managed NGINX (ADC-as-a-Service) native to Azure Marketplace.
- **F5 Distributed Cloud (XC) App Connect / Load Balancer** — SaaS-delivered multi-cloud load balancing and app connectivity.

Read Layer 2 as the capability catalog (each record is self-contained and retrievable on its own). Layer 3 gives routing logic, disqualifiers, and bounded competitive/objection handling. The appendix tracks perishable naming and confidence.

## Layer 2 — Capability catalog

### [ADC] L4–L7 load balancing and traffic management
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          L4–L7 load balancing and traffic management
- plain_description:        Distributes client traffic across pools of servers using health- and performance-aware algorithms, operating from simple Layer 4 (TCP/UDP) through full Layer 7 (HTTP) decisions.
- delivered_by:             BIG-IP LTM (TMOS v21.x); F5 NGINX Plus / NGINX One; F5 NGINXaaS for Azure; F5 Distributed Cloud App Connect / Load Balancer
- attribution_confidence:   High
- customer_problem_solved:  Keeps applications available and performant under load; prevents single-server overload and outages; enables scaling and maintenance without downtime.
- fit_signals:              "Our load balancers are end of life"; "we need to scale this app without downtime"; "app goes down when one server fails"; "we're standardizing traffic management across data centers"; mentions of VIPs, pools, nodes, persistence/sticky sessions; blue-green or canary rollout goals; a team running homegrown or basic cloud LB hitting limits.
- disqualifiers:            Purely static single-server web apps; teams fully satisfied with a cloud-provider LB for a single-cloud, HTTP-only workload with no advanced persistence/policy needs; very small shops where a free reverse proxy suffices.
- value_framing:            F5 was named the 2024 market-share leader in both the Application Delivery Controller and the overall Application Security & Delivery categories by S&P Global Market Intelligence / 451 Research (analyst report, May 2025); per F5's Oct 15, 2025 8-K reporting, BIG-IP is used by roughly 57,000 companies including 85% of the Fortune 500 (third-party citation — verify). Full-proxy architecture gives granular control over every connection, not just round-robin distribution — availability, performance, and application-aware decisions in flight.
- product_routing_note:     Lead with BIG-IP LTM for on-prem/data-center, regulated, or deep-traffic-engineering needs. Lead with NGINX Plus/One for cloud-native, containerized, DevOps-owned workloads. Lead with Distributed Cloud for multi-cloud SaaS-delivered LB. Lead with NGINXaaS for Azure-native managed.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com (BIG-IP LTM; Load Balancing Your Applications; analyst reports); nginx.com product pages; docs.cloud.f5.com

### [ADC] SSL/TLS offload and encryption management
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          SSL/TLS offload, termination, and re-encryption
- plain_description:        Terminates and re-encrypts SSL/TLS at the delivery tier so back-end servers are relieved of crypto processing, and gives a central point to manage certificates and ciphers.
- delivered_by:             BIG-IP LTM (TMOS v21.x, with hardware crypto on rSeries/VELOS); F5 NGINX Plus / NGINX One; F5 NGINXaaS for Azure
- attribution_confidence:   High
- customer_problem_solved:  Reduces CPU burden on application servers; centralizes certificate lifecycle and cipher policy; enables inspection and consistent encryption posture from client to server.
- fit_signals:              "Our servers are burning CPU on SSL"; "we have certificate sprawl / expired-cert outages"; "we need one place to enforce TLS policy"; "we need FIPS/hardware crypto"; high-throughput HTTPS sites; forward-secrecy / ECC requirements; regulated environments.
- disqualifiers:            Workloads where TLS must remain end-to-end with no termination point (re-encryption addresses most of these); tiny deployments without crypto load concerns.
- value_framing:            BIG-IP delivers dedicated hardware crypto — F5 states rSeries offloads SSL processing up to 3x with FPGA acceleration, up to 200K TPS SSL offload and up to 140K TPS P-256. Protect the whole user experience by encrypting everywhere without paying the server-CPU tax; central cert/cipher control reduces outage risk.
- product_routing_note:     BIG-IP on rSeries/VELOS when hardware crypto, FIPS, or highest TPS matter. NGINX Plus/NGINXaaS for software-tier termination in cloud-native/Azure contexts.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com (rSeries appliance page; BIG-IP LTM); docs.nginx.com

### [ADC] Post-quantum cryptography (hybrid PQC) at the delivery tier
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          Hybrid post-quantum TLS cipher support
- plain_description:        Terminates TLS using hybrid ciphers that combine classical (ECC) key exchange with NIST-standardized quantum-resistant algorithms (ML-KEM), protecting traffic against "harvest-now, decrypt-later" attacks without re-architecting apps.
- delivered_by:             BIG-IP (TMOS) — v17.5.x introduced X25519_ML-KEM-768 support; v21.1 adds SecP256r1ML-KEM-768 and SecP384r1ML-KEM-1024. BIG-IP Zero Trust Access (formerly BIG-IP APM) adds quantum-resistant VPN tunneling (X25519 + ML-KEM-768). (Deep inspection / broader PQC strategy → doc 08.)
- attribution_confidence:   High
- customer_problem_solved:  Lets organizations start meeting NIST/FIPS 203 post-quantum guidance and address "harvest-now, decrypt-later" risk at the infrastructure layer, protecting even legacy/IoT/OT endpoints that can't be upgraded.
- fit_signals:              "We have a post-quantum mandate / NCSC or NIST timeline to meet"; "auditors are asking about crypto-agility"; government, finance, healthcare, or defense; long-lived sensitive data (PII/PHI/IP); "we can't touch the legacy apps but need quantum-safe encryption."
- disqualifiers:            Organizations with no compliance driver and short-lived, low-sensitivity data; teams not yet on v17.5+/v21.1-capable platforms (note: v21.x is not supported on iSeries — see hardware records).
- value_framing:            Apply quantum-safe encryption where TLS terminates — no app re-architecture. Both new ciphers are built on NIST FIPS 203 parameters; hybrid ciphers keep backward compatibility while closing the harvest-now-decrypt-later gap years ahead of operational quantum computers.
- product_routing_note:     BIG-IP TMOS v21.1 for delivery-tier PQC. Cross-reference doc 08 for broader crypto/inspection strategy. Requires rSeries/VELOS or VE running v21.1 (not iSeries).
- maturity_flag:            GA (v21.1 GA'd Q2 CY2026; the AppWorld March 2026 material was a pre-announcement/sneak peek — v21.1 is now generally available per F5's GA blog)
- source_currency_flag:     Current
- source:                   f5.com/company/blog (BIG-IP v21.1 GA; sneak peek v21.1; F5 extends NIST-compliant PQC); techdocs.f5.com

### [ADC] iRules programmability
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          iRules / iRules LX traffic programmability
- plain_description:        A scripting capability (TCL-based, with Node.js via iRules LX) that lets operators inspect and manipulate traffic in flight — rewriting headers, custom routing, real-time fixes, and features beyond standard config.
- delivered_by:             BIG-IP LTM (TMOS v21.x)
- attribution_confidence:   High
- customer_problem_solved:  Solves application-delivery problems that off-the-shelf config can't — custom routing, header manipulation, patching back-end issues in flight, bespoke security/authentication logic.
- fit_signals:              "We have hundreds of iRules we can't lose"; "our F5 does custom logic no other box can replicate"; "we patched a backend bug with an iRule"; deep in-house F5 expertise; anxiety about migrating away because of iRules lock-in; requests for HTTP redirects, custom persistence, maintenance pages.
- disqualifiers:            Greenfield teams wanting declarative/GitOps-only config; simple apps whose needs are met by native config; DevOps teams who explicitly reject imperative scripting.
- value_framing:            iRules are F5's signature differentiator. Per F5's July 15, 2025 blog, "Over 85% of BIG-IP customers rely on iRules, which power 70% of all BIG-IP instances globally"; F5 describes "the ability to manipulate data in flight in an almost unrestricted way" as "unmatched in the industry." They are both immense value and real lock-in — a switching-cost anchor for retention and a migration hurdle competitors must overcome.
- product_routing_note:     BIG-IP only. When a customer's iRules estate is large, it is a strong retention signal and an argument against rip-and-replace by a competitor. Note competitors (Avi, Loadbalancer.org) claim partial iRules conversion.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com/company/blog (iRules code generation, 2025-07-15); DevCentral (Introducing the F5 AI Assistant for BIG-IP)

### [ADC] F5 AI Assistant for iRules (generate/explain/optimize)
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          F5 AI Assistant — iRules code generation
- plain_description:        A natural-language assistant that explains existing iRules, generates new validated iRules from plain-English descriptions, and optimizes/debugs them, lowering the TCL skills barrier.
- delivered_by:             F5 AI Assistant (part of F5 Application Delivery and Security Platform), for BIG-IP; unified across BIG-IP, NGINX One, and Distributed Cloud
- attribution_confidence:   High
- customer_problem_solved:  Addresses the shrinking TCL skills pool and slow, error-prone manual iRules work; lets any operator adapt policy quickly.
- fit_signals:              "We're losing our iRules greybeards"; "only one person understands our iRules"; "iRules changes take days"; teams worried about programmability skills gaps; interest in AI-assisted operations.
- disqualifiers:            Shops with no iRules footprint; customers barred from AI-assisted tooling by policy; NGINX-only or Distributed-Cloud-only environments (assistant covers those but not for iRules specifically).
- value_framing:            Preview shown at AppWorld 2025 (Feb 2025); iRules code generation reached availability July 15, 2025. Per F5's AI Assistant framing, the Explain/Generate/Optimize functions "eliminate the manual guesswork" for iRules that are "complex, time-intensive, and… persist long after their authors have moved on," letting teams generate and validate complex iRules in minutes rather than days — de-risking the iRules skills gap customers cite as a reason to leave BIG-IP.
- product_routing_note:     BIG-IP customers with iRules estates. Reinforces the iRules retention story.
- maturity_flag:            GA (iRules code generation availability announced July 2025; preview was AppWorld Feb 2025)
- source_currency_flag:     Current
- source:                   f5.com/company/blog (AI Assistant expands with iRules code generation, 2025-07-15); helpnetsecurity.com; DevCentral

### [ADC] Health monitoring and high availability
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          Health monitoring, failover, and high availability
- plain_description:        Actively and passively checks server/app health and removes unhealthy members from rotation; provides device-level failover and clustering so the delivery tier itself has no single point of failure.
- delivered_by:             BIG-IP LTM (TMOS v21.x, ScaleN clustering); F5 NGINX Plus / NGINX One (active health checks); F5 NGINXaaS for Azure (active-active, availability zones, 99.95% uptime SLA on Standard V3)
- attribution_confidence:   High
- customer_problem_solved:  Prevents outages by routing away from failed components and by making the load balancer itself redundant; maintains uptime SLAs.
- fit_signals:              "We had an outage because traffic kept hitting a dead server"; "we need active/active HA"; "we need to hit a 99.9%+ uptime SLA"; disaster-recovery and failover requirements; complaints that basic cloud LB health checks are too coarse.
- disqualifiers:            Non-critical internal tools with no uptime requirement; single-instance dev/test.
- value_framing:            Active health checks (a paid NGINX Plus differentiator over OSS) and BIG-IP ScaleN clustering keep apps up during failures and maintenance; NGINXaaS Standard V3 offers a 99.95% uptime SLA with active-active across Azure availability zones.
- product_routing_note:     BIG-IP for data-center HA pairs/clusters. NGINX Plus/One for software-tier active health checks. NGINXaaS for managed Azure HA. GSLB/DNS-based failover across sites → doc 06.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com (BIG-IP LTM); nginx.com (NGINX Plus feature matrix); docs.nginx.com (NGINXaaS overview/billing)

### [ADC] Hardware platform: rSeries / VELOS (F5OS) and the iSeries refresh
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          Next-gen ADC hardware (rSeries appliances, VELOS chassis) on F5OS
- plain_description:        F5's current hardware ADC platforms, built on the Kubernetes/microservices-based F5OS with multitenancy by default, replacing the legacy iSeries appliances and VIPRION chassis.
- delivered_by:             F5 rSeries (appliances), F5 VELOS (chassis) running F5OS; host BIG-IP (TMOS) tenants
- attribution_confidence:   High
- customer_problem_solved:  Provides a supported, higher-performance, automatable hardware path as iSeries/VIPRION reach end of support; enables consolidation and side-by-side migration via tenants.
- fit_signals:              "Our F5s are going end of support"; "we're on i2600/i5000/i7000/i10000/i11000"; "we're on VIPRION"; hardware refresh budget cycles; "we need FIPS hardware"; performance/throughput ceilings; data-center consolidation projects.
- disqualifiers:            Customers going all-in on public cloud with no data-center hardware future; workloads better served by VE or SaaS.
- value_framing:            iSeries End of Sale was effective January 1, 2024; End of Software Support (EoSS) for iSeries/VIPRION is scheduled for January 1, 2027, October 1, 2027, or April 1, 2026 depending on model. Critically, **BIG-IP 21.x is not supported on iSeries** — to get v21.x (PQC, AI-era features) customers must move to rSeries/VELOS. rSeries claims up to 2x scale/performance over prior gen and supports side-by-side migration via tenants. This is a strong, date-driven call trigger.
- product_routing_note:     rSeries for appliance form factor; VELOS for chassis/service-provider density. Both run classic BIG-IP TMOS tenants (KubeVirt/F5OS). Note: earlier F5 messaging tied these platforms to "BIG-IP Next tenants" — with Next discontinued for ADC, the tenant story is now BIG-IP v21.x TMOS.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   my.f5.com K000133583 (iSeries EoS), K000151744 (i5820-DF/i7820-DF EoS), K9476 (HW/SW matrix), K4309 (lifecycle policy); f5.com (rSeries, VELOS)

### [ADC] BIG-IP Virtual Edition (software ADC)
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          BIG-IP Virtual Edition (VE)
- plain_description:        The full BIG-IP TMOS software running as a virtual machine on hypervisors or public cloud, licensed by vCPU/bandwidth.
- delivered_by:             BIG-IP VE (TMOS v21.x)
- attribution_confidence:   High
- customer_problem_solved:  Delivers BIG-IP features (LTM, iRules, SSL) without dedicated hardware; supports cloud migration and hybrid consistency with on-prem BIG-IP.
- fit_signals:              "We want the same BIG-IP config in cloud and on-prem"; "we're lifting BIG-IP into AWS/Azure/GCP"; "we don't want more hardware"; VMware/hypervisor consolidation; teams needing iRules parity in virtualized environments.
- disqualifiers:            Workloads needing hardware crypto/FIPS or highest TPS (route to rSeries/VELOS); cloud-native teams who'd prefer NGINX or Distributed Cloud.
- value_framing:            Same TMOS feature set and iRules, deployed anywhere; consistent operating model across form factors. Flexible licensing (perpetual, subscription, Flex Consumption) avoids hardware lead times.
- product_routing_note:     VE for hypervisor/cloud BIG-IP consistency; competitors highlight VE throughput caps (Kemp/Loadbalancer.org market "uncapped" licenses) — position Flex Consumption and rSeries where caps bite.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com (BIG-IP Next LTM data sheet — VE licensing by vCPU/bandwidth; BIG-IP upgrade page)

### [ADC] F5 NGINX Plus / NGINX One (software reverse proxy, LB, caching)
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          NGINX Plus / NGINX One software application delivery
- plain_description:        A lightweight software data plane providing L4/L7 load balancing, reverse proxy, content caching, and API gateway; NGINX One is the unified enterprise subscription that bundles NGINX components with a SaaS management console.
- delivered_by:             F5 NGINX Plus (data plane); F5 NGINX One (enterprise subscription: NGINX Plus, NGINX Ingress Controller, NGINX Gateway Fabric, NGINX One Console, NGINX Instance Manager, plus optional NGINX App Protect)
- attribution_confidence:   High
- customer_problem_solved:  Delivers enterprise app-delivery features (active health checks, session persistence, dynamic reconfiguration, live monitoring) on software, close to cloud-native and containerized apps, with centralized fleet management.
- fit_signals:              "We run NGINX OSS everywhere and need support/health checks"; "we have NGINX sprawl we can't see or govern"; DevOps/platform teams; Kubernetes and microservices; API gateway needs; "we want software LB, not appliances"; consolidating point tools.
- disqualifiers:            Customers needing hardware crypto/FIPS or the deepest L7 traffic engineering (route to BIG-IP); shops content with unsupported OSS and no governance need.
- value_framing:            NGINX One consolidates formerly separate NGINX SKUs under one enterprise license with a SaaS console for observability, CVE/config recommendations, and policy enforcement across the whole NGINX fleet — "one SKU," reduced tool sprawl. NGINX Plus adds active health checks, session persistence, and dynamic reconfiguration over OSS. NGINX One reached GA September 17, 2024.
- product_routing_note:     NGINX One for enterprises wanting unified NGINX governance/SaaS console; NGINX Plus standalone for a single data plane. Integrates with BIG-IP (CIS) for Kubernetes endpoints. Kubernetes ingress/gateway specifics → doc 10.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com/products/nginx; f5.com/go/faq/nginx-faq; f5.com press release (NGINX One GA, Sept 2024)

### [ADC] F5 NGINXaaS for Azure (managed ADC-as-a-Service)
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          NGINXaaS for Azure
- plain_description:        A fully managed NGINX (Plus) service co-developed by F5 and Microsoft, native to Azure, sold through the Azure Marketplace with consumption billing and F5-managed infrastructure.
- delivered_by:             F5 NGINXaaS for Azure
- attribution_confidence:   High
- customer_problem_solved:  Gives Azure customers commercial-grade NGINX load balancing/ADC without operating it themselves; integrates with Azure Monitor, Key Vault, Entra, and Azure billing.
- fit_signals:              "We're Azure-first and want managed load balancing"; "we don't want to run NGINX ourselves"; "we need Azure-native billing/monitoring"; AKS/Kubernetes on Azure; teams wanting consumption pricing (NCUs).
- disqualifiers:            Non-Azure or multi-cloud-neutral shops (route to Distributed Cloud or self-managed NGINX); needs beyond the managed feature set (NGINXaaS omits some NGINX Plus features).
- value_framing:            ADCaaS on the fast NGINX data plane with active-active HA, dynamic autoscaling, and a 99.95% uptime SLA (Standard V3), billed by consumption (NGINX Capacity Units) through Azure — no operational toil, F5 manages the infrastructure. Actively developed (running NGINX Plus R36 in 2026).
- product_routing_note:     Azure-native managed use cases. F5 also references NGINXaaS for Google Cloud on its product pages — verify status/region per deal. For multi-cloud SaaS LB, prefer Distributed Cloud.
- maturity_flag:            GA (GA on Azure; confirmed current via 2026 NGINXaaS changelog)
- source_currency_flag:     Current
- source:                   docs.nginx.com/nginxaas/azure (overview, billing, changelog 2026); f5.com/products/nginx/f5-nginxaas-for-azure; azure.microsoft.com blog (GA)

### [ADC] F5 Distributed Cloud — multi-cloud load balancing / App Connect
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          Distributed Cloud App Connect / Load Balancer (SaaS, multi-cloud LB)
- plain_description:        SaaS-delivered load balancing and secure app-to-app connectivity that spans clouds, data centers, and edge, with a single policy and console and an optional F5 global backbone.
- delivered_by:             F5 Distributed Cloud (XC) App Connect; Distributed Cloud Load Balancer and Kubernetes Gateway
- attribution_confidence:   High
- customer_problem_solved:  Connects and load-balances apps across multiple clouds/regions with consistent L4–L7 policy, avoiding per-cloud tool sprawl and IP-overlap constraints; eases hybrid multi-cloud migrations.
- fit_signals:              "Our apps are spread across AWS, Azure, GCP and on-prem and it's a mess"; "we need one policy across clouds"; "we're migrating apps between clouds without downtime"; "cloud LBs don't span providers"; distributed/edge workloads; IP overlap headaches.
- disqualifiers:            Single-cloud, single-region apps well served by a native cloud LB; customers wanting on-prem hardware control; air-gapped environments.
- value_framing:            One SaaS console and one policy for load balancing across any cloud/edge, with global server load balancing and endpoint-health distribution across clusters — migrate and connect apps across environments without re-plumbing networks or fighting IP overlap. (Multi-cloud network fabric specifics → doc 09; DNS-based steering → doc 06.)
- product_routing_note:     Lead with Distributed Cloud for SaaS-delivered, multi-cloud LB and app connectivity. Coexists with BIG-IP (service discovery) and NGINX. Kubernetes gateway specifics → doc 10.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com/products/distributed-cloud-services/app-connect; docs.cloud.f5.com; wtit.com (XC LB overview)

### [ADC] Flexible licensing and consumption models
- solution_area:            Application Delivery & Load Balancing (ADC)
- capability_name:          Licensing flexibility (perpetual, subscription, Flex Consumption Program)
- plain_description:        F5's range of buying models — perpetual licenses, term subscriptions, the Flex Consumption Program (FCP, a multi-year enterprise agreement with usage-based true-up), and utility/pay-as-you-go via cloud marketplaces.
- delivered_by:             Applies across BIG-IP VE, NGINX, rSeries/VELOS software, F5 Distributed Cloud; FCP is the flagship enterprise agreement
- attribution_confidence:   High
- customer_problem_solved:  Aligns spend to usage, removes procurement lead time (self-service licensing), and lets customers keep CapEx (perpetual) or OpEx (subscription/FCP) as their finance model requires.
- fit_signals:              "Our competitor forced us onto subscription-only and prices spiked"; "we can't do OpEx / we can only do CapEx"; "procurement takes months to license a new instance"; "we want to scale cost with usage"; frustration with NetScaler's licensing shift.
- disqualifiers:            Small single-instance buyers with no scaling or portability need.
- value_framing:            Unlike vendors that went subscription-only, F5 still offers perpetual, subscription, FCP, and utility — the customer's choice of CapEx vs OpEx. FCP: one 3-year agreement across the F5 portfolio, annual spend adjusted to actual usage, self-service licensing. One quoted F5 customer (a NetOps engineer at a large mobile operator) reports delivering "a new F5 BIG-IP fully licensed within a few hours" under FCP versus roughly three months under perpetual procurement. Direct counter to NetScaler's forced-subscription pain.
- product_routing_note:     FCP for enterprises wanting one agreement across BIG-IP/NGINX/XC. Perpetual for CapEx-only/regulated buyers. Utility/CSPP via AWS/Azure/GCP marketplaces.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   f5.com/products/get-f5/flex-consumption-program; f5.com/company/blog (ADC licensing options); f5.com/company/policies/subscription-program-terms

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**By existing footprint:**
- **Already runs BIG-IP (classic TMOS / iSeries / VIPRION):** Lead with BIG-IP v21.x on rSeries/VELOS (hardware refresh) or BIG-IP VE (virtual). Anchor on iRules retention and EoSS dates. **Do not route them to "BIG-IP Next"** — it is discontinued for ADC; the modernization path is v21.x TMOS.
- **Cloud-native / DevOps / Kubernetes-heavy:** Lead with NGINX Plus / NGINX One. If Azure-first and wants managed, NGINXaaS for Azure. (K8s ingress/gateway detail → doc 10.)
- **Multi-cloud, wants SaaS and single policy:** Lead with F5 Distributed Cloud App Connect / Load Balancer.
- **Greenfield / no F5 footprint:** Match to architecture — data-center/regulated → BIG-IP; cloud-native → NGINX; multi-cloud SaaS → Distributed Cloud.

**By buyer persona:** NetOps/infrastructure and security-regulated buyers → BIG-IP. DevOps/platform-engineering buyers → NGINX One. Cloud architects wanting managed/SaaS → NGINXaaS or Distributed Cloud.

**By delivery-model preference:** Hardware/FIPS/highest-TPS → rSeries/VELOS. Self-managed software → BIG-IP VE or NGINX Plus. Managed → NGINXaaS for Azure. SaaS multi-cloud → Distributed Cloud.

**Coexistence / migration notes:** BIG-IP, NGINX, and Distributed Cloud are complementary — NGINX Plus integrates with BIG-IP via Container Ingress Services (CIS) to expose Kubernetes endpoints; Distributed Cloud supports BIG-IP and Kubernetes service discovery. rSeries/VELOS run classic BIG-IP TMOS tenants for side-by-side version migration. Where public sources don't specify an official routing rule (e.g., NGINXaaS for Google Cloud availability by region, or exact FCP product eligibility per deal), say so and defer to the F5 account team rather than inventing guidance.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **Single-cloud, single-region, HTTP-only app fully served by a native cloud LB** with no advanced persistence, programmability, or cross-cloud need — weak fit; a cloud LB genuinely suffices.
- **Very small or static workloads** (single server, internal tool, no uptime SLA) — free OSS reverse proxy or the cloud's built-in LB is adequate; F5 is over-provisioning.
- **Customer explicitly committed to eliminating all hardware and all commercial LB spend** and standardizing on open-source (Envoy/HAProxy/NGINX OSS) with in-house SRE ownership — F5 must compete on software (NGINX/XC), not hardware; the hardware pitch is a non-starter.
- **Customer expecting to move to "BIG-IP Next" for classic ADC** — anti-pattern: correct the record (Next discontinued for ADC; go-forward is v21.x TMOS) rather than affirming.
- **Air-gapped / no cloud connectivity** — SaaS (Distributed Cloud, NGINX One console, NGINXaaS) is a weak fit; lead with self-contained BIG-IP/NGINX Plus.
- **No compliance driver + short-lived low-sensitivity data** — the PQC story is "too early"; don't over-index on quantum urgency.
- **No iRules and declarative/GitOps-only culture** — the iRules value/lock-in narrative won't land; lead with NGINX/declarative AS3 instead.

### 3c. Competitive positioning and objection handling (bounded — all lower confidence)

All competitive claims below are **lower-confidence** and based on public/third-party sources; verify per deal. This market consolidates fast — always re-check vendor status.

**Legacy ADC vendors:**
- **Citrix NetScaler** — owned by **Cloud Software Group** (formed September 2022 when Vista Equity Partners and Evergreen Coast Capital, an Elliott affiliate, took Citrix private for $16.5B and merged it with TIBCO). **Not Broadcom** — a common error to avoid on calls. The live displacement driver is licensing: Citrix ended perpetual licensing (hardware perpetual ~March 2023, VPX perpetual ~March 2025), moved to subscription-only, and mandates migration to the cloud-tethered License Activation Service (LAS) by **April 15, 2026**, after which unmigrated file-based licenses stop working (virtual desktops fail to boot, NetScaler instances stop validating). Loadbalancer.org's Joshua Turnbull told Channel Futures that customers "are pretty shocked when they get their renewal quotes that have often increased by up to 200% compared to last year… It's a fairly staggering increase," citing a U.K. NHS Trust that received a 200% increase three weeks before its renewal deadline. F5's *stated* counter: it retains perpetual/subscription/FCP/utility choice; there is an official DevCentral CodeShare Perl script (community.f5.com/kb/codeshare/citrix-netscaler-to-f5-big-ip/277635) to convert NetScaler configs to BIG-IP — note it is **legacy** (targets NetScaler v7–v9 and BIG-IP 9.4.x output), so treat it as a starting aid, not a turnkey tool — plus partner-led migration webinars (e.g., F5 + WorldTech IT "Moving Beyond NetScaler"). No F5-branded standalone NetScaler-displacement *program* distinct from these was found. *Objection "our NetScaler is fine":* acknowledge, then surface the April 15, 2026 LAS cutoff and renewal-cost reality.
- **VMware Avi Load Balancer** (formerly Avi Networks / NSX Advanced Load Balancer) — now owned by **Broadcom** (completed VMware acquisition Nov 22, 2023). This churn IS Broadcom-driven (post-acquisition licensing/packaging upheaval). Note Broadcom publishes its own **F5-to-Avi** conversion tool (claims ~75% of iRules auto-convertible, the rest rewritten in DataScript/Lua), so F5 faces displacement pressure in *both* directions; the retention counter is the depth of the iRules estate and BIG-IP's hardware/FIPS story.
- **A10 Networks** — independent, publicly traded (NYSE: ATEN) as of 2025–2026 (verified via SEC filings; no acquisition). A niche but real competitor in service-provider/CGNAT and DDoS-adjacent ADC deals.
- **Radware (Alteon)** — independent, publicly traded (NASDAQ: RDWR) as of 2025–2026 (verified via SEC 6-K filings; no acquisition — disregard any "acquired by Cato" rumor, which conflates Cato's unrelated Aim Security purchase). Competes mainly in ADC + application-security bundles.

**Software / open-source:** HAProxy, NGINX OSS itself, Envoy. F5's answer is largely **to offer the software tier** (NGINX Plus/One) rather than fight it — position enterprise support, active health checks, session persistence, dynamic reconfiguration, CVE/patch governance, and the NGINX One SaaS console against unsupported OSS and tool sprawl. Against Envoy/HAProxy in DevOps shops, lead with NGINX One governance and F5 backing, not with BIG-IP.

**Cloud-native LBs (AWS ALB/NLB, Azure LB/App Gateway, GCP):** F5's *stated* differentiation is depth (full-proxy L7 control, iRules programmability, advanced persistence, deep telemetry), consistency across hybrid/multi-cloud via one policy, and hardware crypto/FIPS where required.

**Objection: "cloud LBs are good enough now."** Bounded, honest answer: for a single-cloud, single-region, standard-HTTP app, a native cloud LB often *is* sufficient — say so (see disqualifiers). F5 wins when the customer needs (a) consistent policy/observability *across* clouds and on-prem, (b) programmability/advanced traffic logic cloud LBs don't offer, (c) hardware crypto/FIPS/highest-TPS, or (d) to avoid re-implementing delivery/security separately in every cloud. Route to Distributed Cloud (multi-cloud SaaS) or NGINX (portable software), not to hardware, here.

**Objection: "we're moving off hardware ADCs entirely."** Don't fight the premise — F5 has a full software/SaaS answer: BIG-IP VE (same TMOS/iRules, no hardware), NGINX Plus/One (software), NGINXaaS (managed), and Distributed Cloud (SaaS). The pitch shifts from "refresh your appliances" to "keep your F5 operating model and iRules investment while going software/SaaS," with Flex Consumption to align spend. Reserve the hardware pitch for FIPS/highest-TPS/data-center-consolidation cases.

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify every engagement):**
- **BIG-IP Next: DISCONTINUED for ADC.** F5 stopped BIG-IP Next development in 2025 and is modernizing BIG-IP TMOS (v21.0 GA Nov 18, 2025; v21.1 GA June 2026 — F5 GA blog dated June 4, 2026). Final Next version 20.3 reached EoL April 30, 2025. Ref: K000152956 (could not be fetched directly — behind my.f5.com JS/login wall; corroborated via F5 blogs, DevCentral, WorldTech IT). **"BIG-IP Next for Kubernetes" (BNK) and "BIG-IP Next Cloud-Native Network Functions (CNFs)" still exist and are actively developed** (CNF 2.3, early 2026) — these are service-provider/K8s products (→ doc 10), NOT the ADC re-platform. Easy to conflate — keep distinct.
- **BIG-IP APM → BIG-IP Zero Trust Access** (rename seen in v21.1 PQC materials). Access is largely a sibling-doc topic, but the rename appears in delivery/PQC contexts.
- **"ADC 3.0"** — an F5 *marketing* framing introduced at AppWorld 2025 (Locoh-Donou: ADC 1.0 = hardware appliances; 2.0 = cloud-native services; 3.0 = converged delivery+security platform). Tied to the **F5 Application Delivery and Security Platform (ADSP)** branding, still in use into 2026. Treat as positioning language, not a product.
- **NGINX One vs NGINX Plus:** NGINX Plus is the data plane; NGINX One is the enterprise subscription bundling Plus + Ingress Controller + Gateway Fabric + One Console + Instance Manager (+ optional App Protect) with a SaaS console. GA September 17, 2024. Don't use interchangeably.
- **NGINXaaS:** confirmed current on Azure (2026 changelog, NGINX Plus R36). NGINXaaS for Google Cloud is referenced on F5/NGINX pages — verify status/region per deal.
- **Hardware:** iSeries EoS 1 Jan 2024; EoSS 1 Jan 2027 / 1 Oct 2027 / 1 Apr 2026 by model; **BIG-IP 21.x not supported on iSeries.** rSeries/VELOS on F5OS are the go-forward.

**Explicitly not verified / do not assert:**
- Exact contents of my.f5.com K-articles (K000152956, K4309, K9476, K000133583, K000151744) — pages are behind a JavaScript/login wall and could not be fetched directly; dates and statements corroborated via F5 blogs, WorldTech IT, Loadbalancer.org, and F5 support-policy summaries. Treat specific per-SKU dates as "verify on my.f5.com."
- An **"sSeries"** hardware line — mentioned by one partner blog (WorldTech IT) only; unconfirmed in primary F5 sources. Do not assert.
- The Fortune-500 / ~57,000-companies install-base figure — a third-party citation of F5's Oct 15, 2025 8-K, not read directly from the filing; verify before quoting.
- Any F5-branded, standalone "NetScaler displacement program" distinct from the DevCentral CodeShare script and partner-led (WorldTech IT/Carahsoft) webinars — not found; do not claim an official program.
- Precise v21.1 GA calendar date — F5 stated Q2 CY2026 / "next few months" from AppWorld (March 2026); the F5 GA blog ("BIG-IP v21.1 is now generally available," dated June 4, 2026 — see doc 07) confirms GA in June 2026.

**Primary sources leaned on:** f5.com (product, blog, press releases, analyst reports: BIG-IP LTM, rSeries, VELOS, NGINX, NGINXaaS, Distributed Cloud, FCP, v21.0/v21.1, AI Assistant, PQC); techdocs.f5.com; docs.nginx.com; docs.cloud.f5.com; DevCentral (community.f5.com); azure.microsoft.com; businesswire.com. **Third-party (competitive reality-check, lower trust):** Channel Futures, The Register, Citrix Community, Broadcom TechDocs, WorldTech IT, Loadbalancer.org, Kemp, Gartner Peer Insights, SEC filings (A10, Radware, F5 status), NBC News (Broadcom–VMware close).