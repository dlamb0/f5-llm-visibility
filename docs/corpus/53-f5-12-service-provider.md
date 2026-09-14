# F5 Service Provider & Telco — Solution Area Reference (Doc 12)
doc_id: 12-service-provider
solution_area: Service Provider & Telco
doc_tag: SP
products_covered: BIG-IP Carrier-Grade NAT (CGNAT), BIG-IP Policy Enforcement Manager (PEM), BIG-IP Next Cloud-Native Network Functions (CNFs) [Edge Firewall CNF, CGNAT CNF, DNS CNF, Policy Enforcer CNF, Disaggregation/DAG CNF], BIG-IP Next Service Proxy for Kubernetes (SPK) / BIG-IP Next for Kubernetes, Carrier-Grade Aspen Mesh, S/Gi-LAN & N6-LAN consolidation solution, BIG-IP Diameter Traffic Management / Traffix SDC (legacy), VELOS & rSeries hardware
compiled: July 2026
primary_release_anchor: BIG-IP Next CNF 2.3 (early 2026; MPLS PE early-access, subscriber-aware PEM with Gx interface); CNF 2.0 GA (Red Hat Summit, May 2025)
refresh_priority: High — cloud-native SP naming churns fast (SPK→BIG-IP Next for Kubernetes rename; frequent CNF minor releases)
last_validated: July 2026

---

## Layer 1 — Human orientation

This document covers F5's **service-provider (SP) portfolio**: the products and use cases specific to telcos, mobile network operators (MNOs), MSOs/cable, and ISPs/WISPs. The buyer here is **network engineering and architecture** (not the enterprise security team). Fit signals use SP language: Gi-LAN/S-Gi-LAN, N6/N6-LAN, subscriber management, CG-NAT (IPv4) exhaustion, 5G standalone (SA) core, UPF, and cloud-native network functions (CNFs).

F5 delivers SP capabilities across three delivery models:

1. **Classic BIG-IP (TMOS)** — the mature, hardware-or-VNF form: **BIG-IP CGNAT**, **BIG-IP PEM** (policy enforcement/DPI), **BIG-IP AFM** (firewall/DDoS, cross-ref doc 04), **BIG-IP DNS** (cross-ref doc 06). These run on **VELOS** (chassis) and **rSeries** (appliance) carrier-grade hardware, or as Virtual Editions. This is where the bulk of installed SP revenue sits and where the deepest feature maturity is.
2. **BIG-IP Next Cloud-Native Network Functions (CNFs)** — Kubernetes-native, containerized re-implementations of those same functions (Edge Firewall CNF, CGNAT CNF, DNS CNF, Policy Enforcer CNF, plus a Disaggregation/DAG CNF), sharing F5's TMM data plane and Cloud-Native Engine (CNE). Aimed at 5G core / N6-LAN / edge. Current anchor: **CNF 2.0 (GA May 2025)**, advanced by **CNF 2.3 (early 2026)**.
3. **BIG-IP Next Service Proxy for Kubernetes (SPK)** — cloud-native infrastructure that adds telco protocol ingress/egress (Diameter, SIP, SCTP, GTP, HTTP/2) and networking that "vanilla" Kubernetes lacks, for 5G SA core clusters. Paired with **Carrier-Grade Aspen Mesh** for east-west. **Naming peril: SPK was renamed "BIG-IP Next for Kubernetes" starting at the 2.0.0-GA release** — but SPK branding persists in telco/5G-core certification contexts. Note also that "BIG-IP Next for Kubernetes" is now heavily marketed for AI-factory/DPU use cases; the telco-5G-core lineage is the SPK side and belongs here (the generic-Kubernetes/enterprise angle belongs to sibling doc 10).

**How to read the rest:** Layer 2 is the capability catalog (one self-contained record per capability). Layer 3 gives product-routing logic, an aggregated disqualifier list, and bounded competitive/objection handling. An appendix tracks perishable naming and confidence. **This is a deliberately flagged document** — some SP claims (named customers, per-server economics) are thin in public sources and are marked accordingly. Where attribution between classic BIG-IP and BIG-IP Next CNF is uncertain, it is flagged rather than guessed.

---

## Layer 2 — Capability catalog

### [SP] Carrier-Grade NAT (CGNAT) / IPv4 exhaustion management
- solution_area: Service Provider & Telco
- capability_name: Carrier-Grade NAT (CGNAT) — large-scale IPv4/IPv6 address translation
- plain_description: Lets a provider share a small pool of public IPv4 addresses across many subscribers, and bridge IPv4 and IPv6, so they can keep growing without buying scarce IPv4 space.
- delivered_by: BIG-IP CGNAT (classic TMOS, on VELOS/rSeries/VE), often combined with BIG-IP AFM; BIG-IP Next CGNAT CNF (cloud-native form)
- attribution_confidence: High
- customer_problem_solved: IPv4 address exhaustion; need to extend IPv4 life while migrating to IPv6; regulatory/lawful-intercept logging of address translations ("support the generation of millions of logging records to comply with regional authorities' requests").
- fit_signals: "We're out of IPv4 and RIR transfers are too expensive"; "we need to log every NAT translation for law enforcement / data retention"; "our CGN box is maxing out on concurrent sessions"; ISP/WISP subscriber growth outpacing public IP allocation; "we need DS-Lite / NAT64 / 464XLAT for our IPv6 rollout"; logging cost/volume complaints ("our NAT logs are overwhelming our collectors").
- disqualifiers: Fully IPv6-native greenfield with no IPv4 legacy; a customer whose packet-core vendor (Ericsson/Nokia) already bundles NAT in the UPF/PGW and has no appetite to disaggregate; small enterprise NAT (not carrier scale).
- value_framing: Reclaim public IPv4 — per F5's CGNAT product page, "NAPT and PBA let service providers exponentially scale available source addresses," with F5's solution overview citing "as high as 35-to-1 return on a large-scale NAT (LSN) pool resource" via port block allocation. Reduce logging cost via PBA/deterministic NAT and IPFIX compression, and consolidate NAT with firewall/DDoS on one platform.
- product_routing_note: Lead with classic BIG-IP CGNAT for mature, high-scale, hardware-accelerated needs — per F5's CGNAT page it "handles close to 1.5 billion concurrent sessions and more than 1 Tbps of throughput," and "Offloading to an Intel SmartNIC, can improve throughput by 30%." Lead with BIG-IP Next CGNAT CNF only when the customer is deploying a Kubernetes/OpenShift 5G core or edge and explicitly wants cloud-native. They can coexist during migration.
- maturity_flag: GA (both classic and CNF form)
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/carrier-grade-nat; f5.com/resources/solution-guides/how-big-ip-cgnat-provides-network-scalability-solution-overview; f5.com/products/big-ip/next/cloud-native-network-functions; techdocs.f5.com BIG-IP CGNAT Implementations

### [SP] Subscriber-aware policy enforcement & DPI (PEM)
- solution_area: Service Provider & Telco
- capability_name: Policy Enforcement Manager (PEM) — traffic classification, subscriber awareness, TCP/video optimization
- plain_description: Identifies who the subscriber is and what apps they're using, then enforces per-subscriber policy — bandwidth tiers, video pacing, URL filtering, traffic steering — and feeds usage data to charging systems.
- delivered_by: BIG-IP PEM (classic TMOS, available as hardware, VNF, or CNF); BIG-IP Next Policy Enforcer CNF (cloud-native form; subscriber-aware PEM with Gx interface integration added in CNF 2.3)
- attribution_confidence: High
- customer_problem_solved: Declining ARPU and rising traffic cost; need to monetize tiered plans, control congestion (esp. encrypted ABR video), enforce fair use, detect tethering, and integrate with PCRF/OCS charging.
- fit_signals: "We want to build plan tiers / zero-rating / parental controls"; "encrypted video is eating our RAN" (PEM detects/paces encrypted ABR incl. UDP/QUIC and classifies 4,000+ apps); "we need to detect tethering"; "we need subscriber identity from RADIUS/DHCP correlated to flows (IP, IMSI, username)"; "our PCRF/OCS needs a Gx enforcement point"; "we want to steer traffic into value-added services (service chaining)."
- disqualifiers: Operators who bought DPI/PCEF inside the packet-core vendor's stack; pure transport/wholesale players with no subscriber relationship; enterprises (this is an SP capability — do not pitch as enterprise security).
- value_framing: Monetize the network with subscriber/app intelligence, protect premium RAN capacity by pacing ABR video (F5's S/Gi-LAN materials cite rate-paced ABR video reducing network bandwidth usage "by up to 71%"), and lower TCO by consolidating classification + enforcement on one platform instead of a standalone DPI appliance.
- product_routing_note: Classic BIG-IP PEM for mature mobile-core Gx/Gi deployments and highest scale. Policy Enforcer CNF for cloud-native 5G/N6 with Gx integration (CNF 2.3+). Confirm the specific classification/optimization feature exists in the CNF form before promising parity — the CNF line is still catching up to classic PEM.
- maturity_flag: GA (classic); GA with evolving parity (Policy Enforcer CNF)
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/policy-enforcement-manager; f5.com PEM datasheet; techdocs.f5.com PEM Implementations; DevCentral "CNF 2.3 What's New"

### [SP] Cloud-native network functions for 5G core / N6-LAN / edge (CNFs)
- solution_area: Service Provider & Telco
- capability_name: BIG-IP Next Cloud-Native Network Functions (CNFs)
- plain_description: Containerized, Kubernetes-native versions of F5's firewall, CGNAT, DNS, and policy functions that run inside a telco's 5G core or edge clusters and scale like other cloud-native software.
- delivered_by: BIG-IP Next CNFs — Edge Firewall CNF (from AFM), CGNAT CNF, DNS CNF, Policy Enforcer CNF (from PEM), Disaggregation (DAG) CNF; on F5 Cloud-Native Engine (CNE); deployable on Red Hat OpenShift, Azure, and on NVIDIA BlueField-3 DPUs
- attribution_confidence: High
- customer_problem_solved: Need to consolidate S/Gi-LAN/N6 point products, cut CapEx/OpEx and power, and scale user-plane services elastically in a Kubernetes 5G SA core without VM-era overhead.
- fit_signals: "We're building a standalone 5G core on OpenShift/Kubernetes"; "we want to consolidate N6-LAN/Gi-LAN functions"; "our NFV VMs are burning CPU and power"; "we need CGNAT+firewall+DNS as containers in the same cluster as our UPF"; "we're looking at BlueField DPUs / AI-RAN / distributed N6-LAN at the edge"; fixed-wireless-access (FWA) growth straining Gi-LAN capacity.
- disqualifiers: Operators with no Kubernetes/cloud-native core plan (classic BIG-IP is the better fit); a fully vendor-locked single-stack core (Ericsson/Nokia) where the UPF already bundles these functions and there's no disaggregation mandate; hyperscaler-built cores where the cloud provider supplies the network functions.
- value_framing: Per F5's CNF 2.0 press release (May 2025), the solution delivers "33% lower CPU utilization" and "consolidates services to reduce infrastructure costs by over 60%," via a shared zero-copy/single-pass TMM data plane, plus independent scaling of data and control planes and DPU offload that frees host CPU for revenue apps. **Flag: F5 explicitly labels these as forward-looking "potential benefits" — "Each customer's unique environment, objectives, and constraints could impact potential benefits."** Treat as vendor projections, not guaranteed outcomes.
- product_routing_note: Lead with CNFs only when the customer is genuinely cloud-native (Kubernetes/OpenShift) in the core or edge. For 5G-core ingress/signaling and inter-cluster traffic, pair CNFs with SPK (BIG-IP Next for Kubernetes) and Aspen Mesh. For classic VNF/hardware environments, route to classic BIG-IP CGNAT/PEM/AFM instead.
- maturity_flag: GA (CNF 2.0, May 2025; CNF 2.3 early 2026). MPLS provider-edge support is Early Access in 2.3.
- source_currency_flag: Current
- source: f5.com/products/big-ip/next/cloud-native-network-functions; f5.com/company/news/press-releases/secure-cloud-native-network-functionality-ai-applications (CNF 2.0); DevCentral "CNF 2.3 What's New"; redhat.com N6-LAN with F5

### [SP] Gi-LAN / N6-LAN consolidation (architectural story)
- solution_area: Service Provider & Telco
- capability_name: S/Gi-LAN & N6-LAN service consolidation
- plain_description: Instead of a chain of separate boxes (NAT, firewall, DPI, video/TCP optimization, DNS) between the mobile core and the internet, run all those functions on one F5 platform.
- delivered_by: Classic BIG-IP (CGNAT + PEM + AFM + DNS as consolidated NFV/Gi-LAN packages on VELOS/rSeries/VE); BIG-IP Next CNFs (cloud-native N6-LAN consolidation, incl. distributed N6-LAN on BlueField-3 DPUs)
- attribution_confidence: High
- customer_problem_solved: Device sprawl in the Gi-LAN/N6-LAN drives up CapEx, OpEx, latency, and power; multiple single-function vendors are hard to manage and scale.
- fit_signals: "We have too many point products between the PGW/UPF and the internet"; "each Gi-LAN function is a separate vendor/appliance"; "we want to reduce hops/latency and power"; "we're re-architecting Gi-LAN for N6 as we move to 5G SA"; "FWA growth is forcing a Gi-LAN capacity upgrade."
- disqualifiers: Operators who have outsourced the whole user plane to a single packet-core vendor and won't disaggregate; very small operators with only one or two Gi-LAN functions (consolidation ROI is weak).
- value_framing: Per F5's S/Gi-LAN consolidation page, "Consolidating and virtualizing your S/Gi-LAN/N6 services can result in up to a 60% reduction in CapEx and OpEx—while boosting performance and lowering latency," achieved via a zero-copy, single-pass ("single-hop") data plane and one common management framework. (Consistent with the "over 60%" infrastructure-cost figure F5 cites for CNF 2.0.)
- product_routing_note: This is a solution story, not a single SKU — lead with whichever functions the customer runs today (usually CGNAT + firewall), then expand. Classic BIG-IP for NFV/hardware; CNFs for Kubernetes-native cores. Cross-ref doc 04 (DDoS) and doc 06 (DNS) for those functions' depth.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/solutions/service-providers/sgi-lan-consolidation; f5.com/solutions/use-cases/n6-lan-services-for-service-providers; redhat.com/architect "Telco 5G N6 LAN Consolidation with F5"

### [SP] Cloud-native 5G core ingress/egress & telco-protocol proxy (SPK)
- solution_area: Service Provider & Telco
- capability_name: Service Proxy for Kubernetes (SPK) / BIG-IP Next for Kubernetes — telco/5G side
- plain_description: Adds carrier-grade networking and telco-protocol handling (Diameter, SIP, SCTP, GTP, HTTP/2) to Kubernetes/OpenShift so a 5G standalone core's containerized network functions can talk to legacy 4G and the outside world securely.
- delivered_by: BIG-IP Next Service Proxy for Kubernetes (SPK) — renamed BIG-IP Next for Kubernetes at 2.0.0-GA; uses containerized TMM + CRDs on OpenShift/OVN-Kubernetes with SR-IOV; paired with Carrier-Grade Aspen Mesh for east-west
- attribution_confidence: High
- customer_problem_solved: "Vanilla" Kubernetes can't natively handle telco signaling protocols, N/S cluster ingress security, or the networking constructs 5G cores need; operators need a 4G↔5G bridge and lawful-intercept-capable visibility.
- fit_signals: "We're standing up a 5G SA core on OpenShift and Kubernetes networking isn't enough"; "we need Diameter/SIP/SCTP/GTP ingress into our cluster"; "we need a signaling firewall at cluster edge"; "we need packet capture / lawful intercept in the K8s core"; "we're bridging 4G signaling while we roll out 5G SA."
- disqualifiers: Operators not using Kubernetes for the core; hyperscaler-hosted cores where the cloud provides ingress; single-vendor vertical stacks where the core vendor's own service mesh/proxy is mandated.
- value_framing: Purpose-built carrier-grade K8s networking that "vanilla" K8s lacks — telco protocol support, per-service secure proxy/cluster firewall, automated service discovery — reducing complexity and speeding a safe 4G→5G transition. F5 states SPK is "GA and currently in production with large scale telcos."
- product_routing_note: Lead with SPK for 5G-core ingress/signaling; pair with CNFs (user-plane/N6 functions) and Aspen Mesh (east-west observability/mTLS). Naming peril: use "BIG-IP Next for Kubernetes" for current releases but expect customers to still say "SPK." Do NOT conflate with the AI-factory/DPU positioning of BIG-IP Next for Kubernetes (that's the doc 10 / AI-infra angle).
- maturity_flag: GA (SPK GA since ~2021; renamed at 2.0.0-GA). Some 1.7.x SPK releases were Limited Availability.
- source_currency_flag: Current
- source: clouddocs.f5.com/service-proxy; f5.com/company/blog/simplify-5g-network-architecture-with-kubernetes-service-proxy; my.f5.com K89026308 (lifecycle policy; rename note)

### [SP] East-west 5G core service mesh (Carrier-Grade Aspen Mesh)
- solution_area: Service Provider & Telco
- capability_name: Carrier-Grade Aspen Mesh — 5G core service mesh
- plain_description: A telco-grade service mesh that secures, observes, and controls the traffic flowing between the containerized network functions inside and between 5G core clusters.
- delivered_by: Carrier-Grade Aspen Mesh (companion to SPK/BIG-IP Next for Kubernetes)
- attribution_confidence: Medium (public product detail is thinner than SPK/CNF; verify current packaging/roadmap status before quoting specifics)
- customer_problem_solved: East-west (inter-CNF) traffic in a 5G SA core needs mTLS encryption/authentication, observability for revenue assurance, and packet capture for troubleshooting and lawful intercept — beyond what N/S proxies provide.
- fit_signals: "We need mTLS between multi-vendor CNFs"; "we need east-west visibility / revenue assurance in the 5G core"; "we need packet capture for lawful intercept inside the cluster"; "we want an operator-owned mesh independent of our CNF vendors."
- disqualifiers: Operators standardizing on a different/open-source mesh; single-vendor cores with a mandated mesh; non-Kubernetes cores.
- value_framing: An operator-owned, 3GPP-compatible, carrier-grade mesh that sits independent of CNFs — so the operator controls security and observability of its most important asset (the network).
- product_routing_note: Only relevant alongside a Kubernetes 5G core; sell with SPK + CNFs. If public roadmap detail is unclear on a live call, flag as "verify current status" rather than over-promising.
- maturity_flag: Unknown/Verify (GA historically; current investment level not clearly documented in recent public sources)
- source_currency_flag: Possibly stale
- source: businesswire.com F5 2020 SPK/Aspen Mesh launch; f5.com/resources/solution-guides/5g-sba-solution-overview

### [SP] Diameter/SIP signaling (Traffix heritage)
- solution_area: Service Provider & Telco
- capability_name: Diameter/SIP signaling — DRA/DEA, signaling firewall, interworking
- plain_description: Routes and secures 4G signaling (Diameter/SS7/SIP) between network elements and roaming partners, and bridges 4G↔5G signaling.
- delivered_by: BIG-IP Diameter Traffic Management (DRA/DEA, Diameter Firewall, Overload Control) on BIG-IP; F5 Traffix Signaling Delivery Controller (SDC) — legacy standalone product
- attribution_confidence: Medium
- customer_problem_solved: Diameter signaling growth, secure roaming (GSMA FS.19), overload/DDoS protection on signaling, and 4G→5G signaling interworking.
- fit_signals: "We need a Diameter Routing Agent / Edge Agent"; "we need a signaling firewall for roaming"; "we're managing 4G signaling while introducing 5G"; "Diameter overload is threatening availability."
- disqualifiers: Greenfield 5G SA using HTTP/2 SBA signaling with no Diameter legacy; operators whose core vendor supplies the DRA/SEPP; any prospect where you'd be selling net-new Traffix SDC (treat as legacy — see below).
- value_framing: Mature 4G signaling with an interworking path to 5G. **Be honest: F5's go-forward signaling story is BIG-IP Diameter Traffic Management, not net-new Traffix SDC.**
- product_routing_note: Treat Traffix SDC as legacy/installed-base. F5 maintained SDC docs into 2025 (release notes for v5.2.0 show an updated date of 08/11/2025), a reseller (SHI) notes "limited stock," and F5 publishes a KB titled "End of Support extension for SDC" (K000133773) — all indicating a product in wind-down. Do NOT lead with signaling on a modern 5G pitch unless the customer explicitly has a Diameter need; verify exact End-of-Sale/End-of-Support dates in my.f5.com (K000133773, K14402) before committing.
- maturity_flag: GA but Legacy/wind-down (Traffix SDC); GA (BIG-IP Diameter Traffic Management)
- source_currency_flag: Possibly stale (verify EoS)
- source: techdocs.f5.com Traffix SDC release notes v5.2.0; my.f5.com K000133773 / K14402; f5.com Diameter Traffic Management use-cases PDF

### [SP] Carrier-scale DNS (cross-reference)
- solution_area: Service Provider & Telco
- capability_name: SP-scale DNS (DNS Express, DNS64/NAT64, DNS caching)
- plain_description: High-volume DNS for subscribers — fast caching resolvers, authoritative acceleration, and DNS64 paired with NAT64 for IPv6 migration.
- delivered_by: BIG-IP DNS (classic, incl. DNS Express) and BIG-IP Next DNS CNF (cloud-native; DNS caching, DoH). Cross-ref doc 06 for depth.
- attribution_confidence: High
- customer_problem_solved: Millions of subscriber DNS queries, DNS DDoS, latency, and IPv6 transition (DNS64 alongside CGNAT NAT64).
- fit_signals: "We need a hyperscale subscriber DNS / resolver"; "DNS DDoS is hitting us"; "we need DNS64 with our NAT64"; "we want to cut DNS latency at the edge"; "localized DNS (LDNS) in the Gi-LAN/N6."
- disqualifiers: DNS handled by another platform the customer won't displace; enterprise DNS (not SP scale).
- value_framing: DNS as one consolidated function in the Gi-LAN/N6 (with CGNAT/firewall). Per F5's CNF product page, the DNS CNF can "Enable DNS caching and reduce DNS latency up to 80%" and decrypt/resolve DoH "without impacting RPS."
- product_routing_note: This doc references DNS only as part of the SP consolidation story — route DNS-specific depth to doc 06. Pair DNS64 with CGNAT NAT64 for IPv6 migration deals.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip/next/cloud-native-network-functions (DNS CNF); cross-ref doc 06

### [SP] DDoS for SP networks (cross-reference)
- solution_area: Service Provider & Telco
- capability_name: Network/subscriber DDoS protection at SP scale
- plain_description: Protects the SP network and NAT pools from volumetric and protocol DDoS, at carrier scale.
- delivered_by: BIG-IP AFM (with CGNAT/PEM), BIG-IP Next Edge Firewall CNF (firewall+DDoS+IPS from AFM). Cross-ref doc 04 for depth.
- attribution_confidence: High
- customer_problem_solved: DDoS against subscribers, NAT pools, DNS, and signaling; need mitigation integrated with the Gi-LAN/N6 rather than a separate scrubbing tier.
- fit_signals: "We need to defend our CGNAT pools from DDoS"; "signaling/DNS DDoS"; "carrier-scale network firewall + DDoS in the N6/Gi-LAN"; "edge firewall for our 5G core clusters."
- disqualifiers: Enterprise DDoS (doc 04); dedicated upstream scrubbing already in place and sufficient.
- value_framing: DDoS consolidated with firewall/NAT on one carrier-grade platform (hardware-assisted on VELOS/rSeries; CNCF-certified Edge Firewall CNF for Kubernetes).
- product_routing_note: Reference only — route DDoS depth to doc 04. In SP deals, DDoS usually rides along with CGNAT/AFM or the Edge Firewall CNF rather than as a standalone sale.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com CNF page (Edge Firewall CNF, CNCF-certified); cross-ref doc 04

### [SP] Carrier-grade hardware & multi-tenancy (VELOS / rSeries)
- solution_area: Service Provider & Telco
- capability_name: VELOS / rSeries carrier-grade hardware (delivery detail)
- plain_description: F5's high-throughput chassis (VELOS) and appliances (rSeries), running the F5OS platform layer, on which SP software functions run as isolated multi-tenant instances.
- delivered_by: VELOS (CX1610/CX410 chassis, BX520/BX110 blades), rSeries appliances, both on F5OS; host classic BIG-IP CGNAT/PEM/AFM/DNS tenants. (Earlier F5 messaging said these platforms would also host "BIG-IP Next tenants" — with the BIG-IP Next ADC line discontinued (K000152956), the tenant story is classic TMOS 17.x/21.x; see docs 05/14. BIG-IP Next CNFs / BNK are separate, active Kubernetes-native lines, not F5OS tenants.)
- attribution_confidence: High
- customer_problem_solved: Need for NEBS-compliant, hardware-accelerated (FPGA/L4 offload, crypto), multi-terabit, multi-tenant platforms for SP-scale traffic and tenant isolation.
- fit_signals: "We need NEBS-compliant carrier hardware"; "hardware offload for CGNAT/DDoS/crypto at terabit scale"; "multi-tenant isolation for managed services"; "chassis consolidation to cut rack/power"; "we're refreshing VIPRION."
- disqualifiers: Pure public-cloud or COTS-only cloud-native strategy (route to VE/CNFs); small deployments where an appliance is overkill.
- value_framing: Carrier-grade throughput and hardware offload — per F5, VELOS "scales to 6Tbps of high-speed throughput" with FPGA offload for CGNAT/DDoS/SSL and "80 million connections per second" firewall performance — plus F5OS multi-tenancy that bridges classic and cloud-native tenants on one NEBS-compliant platform.
- product_routing_note: Hardware is a delivery detail beneath the CGNAT/PEM/AFM/DNS functions — lead with the function and the consolidation story; position VELOS/rSeries as the carrier-grade substrate. Note VIPRION is prior-generation; VELOS is the current chassis.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/velos-hardware-chassis-and-blades; f5.com rSeries data sheet; my.f5.com K86001294 (F5OS support matrix)

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing (keyed on customer situation)

**By architecture / delivery model:**
- **Classic VNF or hardware SP network (most installed base):** Lead with **classic BIG-IP CGNAT and PEM** on **VELOS/rSeries** (or VE). Deepest feature maturity, highest scale, hardware offload. This is the safe default for a customer who is not cloud-native in the core.
- **Kubernetes/OpenShift 5G SA core or edge:** Lead with **BIG-IP Next CNFs** (CGNAT/Edge Firewall/DNS/Policy Enforcer/DAG) for user-plane/N6 functions, **SPK (BIG-IP Next for Kubernetes)** for signaling/ingress, and **Aspen Mesh** for east-west.
- **DPU / AI-RAN / distributed N6-LAN at the edge:** CNFs on **NVIDIA BlueField-3 DPUs** (GA anticipated June 2025 per F5's MWC announcement). Frees host CPU; positions for edge AI.
- **Public cloud:** BIG-IP VE (CGNAT/PEM) or CNFs on Azure/OpenShift.

**By buyer persona:** Network engineering/architecture is the buyer. Frame in SP terms (subscriber, Gi-LAN/N6, UPF, ARPU, TCO), not enterprise-security terms.

**Coexistence & migration (classic ↔ CNF):** F5's public guidance is that CNFs will "eventually replace the analogous classic BIG-IP VNFs," and that CNF features will "match and eventually surpass" the VNFs over time — i.e., **classic remains the parity leader today**. Recommended migration path (per F5 blog): start CNFs in a greenfield edge network as a low-risk pilot, keep monetizing 4G on classic during the transition, and expand CNFs as the Kubernetes core matures. On a live call, do **not** promise CNF feature parity with classic PEM/CGNAT without checking the specific feature — flag it.

**Named deployment reference (thin public record):** The one publicly named Tier-1 CNF deployment is **Rakuten** — per F5's 2022 press release with Rakuten Symphony, "F5's BIG-IP Next CNFs will also be deployed by Rakuten Mobile in its 5G network in Japan," offered through Rakuten's Symworld marketplace. Note this was future-tense at announcement (April 2022) and is the result of a multi-year Rakuten–F5 collaboration. Beyond Rakuten, F5 uses anonymized language ("large scale telcos," "leading service providers"). Do not attribute deployments to unnamed operators.

**Where the public record is thin:** F5 does not publish per-server or per-subscriber licensing economics; CNFs/SPK use a cluster-level, flexible-consumption/subscription usage-reported model. Do not invent official pricing or per-server license guidance — route economics questions to a quote.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **Single-vendor, vertically integrated packet core (Ericsson/Nokia) with no disaggregation mandate.** If the UPF/PGW already bundles NAT, firewall, and DPI and the customer is happy, F5's consolidation ROI is weak. (See objection handling below.)
- **Hyperscaler-built/-hosted core.** If the core runs on and is supplied by a hyperscaler's network functions, there's limited room for F5 SP functions.
- **No Kubernetes/cloud-native plan** → don't pitch CNFs/SPK; route to classic BIG-IP.
- **Fully IPv6-native greenfield with no IPv4 legacy** → CGNAT relevance is low.
- **Pure transport/wholesale player with no subscriber relationship** → PEM/subscriber-aware capabilities don't apply.
- **Enterprise buyer / enterprise use case** → this is the wrong doc; SP functions are priced and scaled for carriers.
- **Net-new signaling (Traffix SDC) on a modern 5G pitch** → treat SDC as legacy; lead with cloud-native, not signaling, unless there's an explicit Diameter need.
- **Very small operator with one or two Gi-LAN functions** → consolidation story doesn't pay off.

### 3c. Competitive positioning & objection handling (bounded — all LOWER CONFIDENCE)

All competitive claims below are lower-confidence and should be validated per-deal. Prefer F5's public differentiators over head-to-head "win" claims.

- **A10 Networks (Thunder CGN) — the primary CGNAT head-to-head.** A10 is the most direct CGNAT rival; both are perennial leaders in the CGNAT category on peer-review trackers (PeerSpot shows A10 and F5 trading mindshare year to year). A10 competes hard on price/performance-per-rack and all-in-one Thunder CFW (CGNAT+firewall+DDoS). **F5's public differentiators:** consolidation with the broader BIG-IP SP suite (PEM subscriber-awareness, DNS, AFM) on one platform, carrier-grade scale (~1.5B sessions, >1 Tbps), and a cloud-native CGNAT CNF path. **Important nuance:** A10 also powers **Ericsson's Packet Core Firewall** — so in Ericsson accounts you may face A10 *inside* the core, not as a standalone.
- **Ericsson / Nokia (NEP full-stack).** These are network equipment providers whose 5G cores bundle user-plane functions (Ericsson Packet Core Gateway bundles NAT, firewall, video/TCP optimization, probes; Packet Core Firewall powered by A10, which Ericsson claims cuts user-plane security TCO "by more than 50 percent" vs dedicated solutions). F5's counter: disaggregation and best-of-breed avoid vendor lock-in and let operators select functions on merit/price; F5's cloud-native functions are multi-vendor and platform-agnostic. (Ericsson is also listed as an F5 CNF ecosystem partner — the relationship is coopetition.)
- **VPP-based open source (FD.io) NAT.** Open-source VPP offers basic NAT44/NAT64; vendors like NFWare and Netgate (TNSR) build commercial CGNAT on it. Even NFWare's own materials concede open-source VPP NAT "does not answer growing CSPs' requirements to a fully functioned Carrier-Grade NAT solution." F5's counter: open-source VPP NAT lacks full carrier-grade CGNAT features (deterministic NAT, PBA logging economics, integrated firewall/DDoS/subscriber-awareness, vendor support). Frame as build-vs-buy and compliance-logging risk.
- **Sandvine-class DPI (for PEM comparisons) — VERIFY STATUS.** Sandvine went through CCAA/Chapter 15 bankruptcy restructuring (filed Nov 2024) and **rebranded to AppLogic Networks in early March 2025**, after U.S. Entity List placement (Feb 2024) and removal (Oct 21, 2024). It exited many non-democratic markets (committing to exit Egypt by Dec 31, 2025) and shifted to software-only. This transition has created DPI displacement opportunities. F5's counter: PEM combines classification + active enforcement + charging integration on a supported, financially stable platform, vs a standalone DPI vendor in transition. (Do not overstate — AppLogic remains operating with a large customer base.)

**Objection: "Our packet core vendor already bundles these functions."**
Acknowledge it's often true (Ericsson Packet Core Gateway/Firewall, Nokia). Then reframe on: (1) **avoiding lock-in** and preserving best-of-breed/price leverage; (2) **consolidation across a broader function set** (CGNAT + subscriber-aware PEM + DNS + firewall/DDoS on one platform vs a partial bundle); (3) **multi-vendor/cloud-native portability** (F5 CNFs run on OpenShift/Azure/DPUs and interoperate with other vendors' CNFs); (4) **logging/compliance depth** for CGNAT (deterministic NAT, PBA, IPFIX) that thin bundled NAT may not match. If the customer is fully committed to the single-vendor stack and happy, mark it a weak fit (see 3b) rather than forcing the deal.

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify every cycle):**
- **SPK → "BIG-IP Next for Kubernetes."** SPK was renamed BIG-IP Next for Kubernetes at the 2.0.0-GA release (per my.f5.com K89026308). But "BIG-IP Next for Kubernetes" is now also the brand for the AI-factory/DPU product (doc 10 territory). In telco/5G-core certification contexts, "SPK" branding persists. Always disambiguate telco-5G-core-SPK from AI-infra-BIG-IP-Next-for-Kubernetes.
- **BIG-IP Next (TMOS-replacement ADC) is being discontinued** — F5 decided to modernize BIG-IP TMOS instead; BIG-IP Next 20.x reached end of life April 30, 2025 (my.f5.com K000152956). **This does NOT apply to BIG-IP Next CNFs / SPK / BIG-IP Next for Kubernetes**, which are separate, active cloud-native product lines. Do not conflate.
- **CNF catalog (current):** Edge Firewall CNF, CGNAT CNF, DNS CNF, Policy Enforcer CNF, Disaggregation (DAG) CNF. Anchor: CNF 2.0 (GA May 2025) → CNF 2.3 (early 2026).
- **Traffix SDC** — legacy; verify exact End-of-Sale/End-of-Support dates.
- **VIPRION → VELOS** (chassis generations); rSeries replaces iSeries for modern F5OS appliances.

**Explicitly NOT verified (do not assert):**
- Exact Traffix SDC End-of-Sale/End-of-Support dates (my.f5.com KBs K000133773 and K14402 are login/JS-gated; not readable in public sources). The existence of an "End of Support extension" article implies a scheduled EoS was extended, but the date is not public.
- Current investment level / roadmap status of Carrier-Grade Aspen Mesh (public detail is thin/older).
- Per-server and per-subscriber licensing economics for CNFs/PEM/CGNAT (not published publicly).
- Named Tier-1 telco customers beyond Rakuten (F5 uses anonymized "large-scale telcos"/"leading service providers" language). Rakuten Symphony/Rakuten Mobile is the one publicly named CNF deployment (announced April 2022, future-tense at announcement).
- CNF-vs-classic feature parity on any specific PEM/CGNAT feature — verify per feature before promising.
- The "up to 60%" CapEx/OpEx and "33% lower CPU" figures are F5's own forward-looking/"potential benefit" marketing claims, not independently verified outcomes.

**Primary sources leaned on:** f5.com service-provider solution pages (service-providers, sgi-lan-consolidation, n6-lan-services, mobility-and-5g-evolution); f5.com CNF product page and CNF 2.0 press release; f5.com CGNAT and PEM product pages/datasheets; clouddocs.f5.com (SPK/Service Proxy); techdocs.f5.com (PEM, CGNAT, Traffix SDC release notes); my.f5.com KBs (K89026308 lifecycle policy, K86001294 F5OS matrix, K000152956 BIG-IP Next discontinuation); DevCentral (CNF 2.2/2.3 what's-new, CNF-for-OpenShift). **Third-party for reality-checking:** Red Hat (N6-LAN architecture), PeerSpot (A10 vs F5 CGNAT), Ericsson (Packet Core Gateway/Firewall + A10), FD.io/Netgate/NFWare (VPP NAT), Light Reading / The Logic / Business Wire / Access Now (Sandvine→AppLogic), SDxCentral/Fierce Network (SPK launch context and MWC 2026). SEO "best tools" listicles were treated as low-trust and not relied upon for attribution.