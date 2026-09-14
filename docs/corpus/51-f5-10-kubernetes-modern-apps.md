# F5 Kubernetes & Modern Application Delivery — Solution Area Reference (Doc 10)

doc_id: 10-kubernetes-modern-apps
solution_area: Kubernetes & Modern Application Delivery
doc_tag: K8S
products_covered: F5 NGINX Gateway Fabric, F5 NGINX Ingress Controller, F5 BIG-IP Container Ingress Services (CIS), F5 IngressLink, BIG-IP Next for Kubernetes / Service Proxy for Kubernetes (SPK), F5 WAF for NGINX (insertion only), NGINX One (packaging), Red Hat OpenShift joint solutions
compiled: July 2026
primary_release_anchor: F5 AppWorld 2026 (March 10–12, 2026, Fontainebleau Las Vegas); ingress-nginx retirement March 2026; NGINX Gateway Fabric 2.6.6 (June 26, 2026)
refresh_priority: High
last_validated: July 2026

---

## Layer 1 — Human orientation

This document covers how F5 gets traffic into Kubernetes clusters: ingress, the Gateway API transition, connecting the BIG-IP hardware/software estate to container platforms, and inserting F5 security at Kubernetes entry points. It is doc 10 in the F5 solution-area knowledge base.

**The lead story is a time-sensitive lifecycle event.** The Kubernetes community project `ingress-nginx` (the community-maintained controller, repo `kubernetes/ingress-nginx`) was retired in March 2026. This is the single most important fit signal in this document, and it is chronically confused with F5's own product. Three distinct things must be kept straight:

1. **`ingress-nginx`** (community project, `kubernetes/ingress-nginx`) — RETIRED March 2026. Best-effort maintenance ended; after retirement there are no further releases, bug fixes, or CVE patches, and the repo is read-only. This is NOT an F5 product. The retirement was announced by Kubernetes SIG Network and the Security Response Committee on November 11, 2025.
2. **F5 NGINX Ingress Controller** (`nginxinc/kubernetes-ingress`, now `nginx/kubernetes-ingress`) — a DIFFERENT, actively-maintained F5/NGINX product, Apache 2.0 OSS plus a commercial NGINX Plus edition. NOT affected by the retirement.
3. **The Kubernetes Ingress API itself** — NOT deprecated, NOT removed, but "feature-frozen." Active development moved to the Gateway API.

The scale is large: per internal Datadog research cited in the Kubernetes Steering and Security Response Committees' January 29, 2026 statement, "about 50% of cloud native environments currently rely on this tool." (Third-party migration guides cite a wider 40–62% range for affected clusters.)

F5 delivers Kubernetes traffic management through several products that differ mainly in *delivery model* and *buyer persona*:

- **F5 NGINX Gateway Fabric (NGF)** — F5's Gateway API implementation, NGINX data plane. The strategic long-term landing spot. Platform-team-led, Kubernetes-native.
- **F5 NGINX Ingress Controller (NIC)** — F5's supported Ingress-API controller; the low-friction "stay on Ingress but get a supported vendor" path, with a bridge to NGF later.
- **F5 BIG-IP Container Ingress Services (CIS)** — connects existing BIG-IP devices to Kubernetes/OpenShift. NetOps-led; exposes cluster services through the BIG-IP estate you already run.
- **F5 IngressLink** — a two-tier integration pairing BIG-IP (edge) with NGINX Ingress Controller (in-cluster).
- **BIG-IP Next for Kubernetes / SPK** — a Kubernetes-native ingress/egress gateway; enterprise-side scope here (telco/5G belongs to doc 12).
- **F5 WAF for NGINX** — security insertion at the NGINX gateway/ingress layer (covered only as an insertion point; deep WAF content in docs 01/02).

How to read the rest: Layer 2 is the capability catalog (one self-contained record per capability, each restating solution area and delivering product). Layer 3 gives product routing, disqualifiers, and bounded competitive/objection handling. The appendix tracks perishable naming and what was not verifiable.

---

## Layer 2 — Capability catalog

### [K8S] ingress-nginx retirement migration (Gateway API transition)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Migration off retired community ingress-nginx to a supported Gateway API / NGINX path
- plain_description: The community `ingress-nginx` controller — which per Datadog research relied on by about 50% of cloud native environments — was retired in March 2026, so teams must move to a maintained alternative; F5 offers both a supported Ingress controller and a Gateway API implementation as landing spots.
- delivered_by: F5 NGINX Gateway Fabric (strategic target); F5 NGINX Ingress Controller (low-friction interim); migration via the open-source `ingress2gateway` CLI (Kubernetes SIG-Network project, with an F5-authored NGINX provider) and a web-based "Ingress-NGINX Migration Tool" at kubernetes.nginx.org
- attribution_confidence: High
- customer_problem_solved: Running an unmaintained, unpatched component in the critical request path creates a growing security exposure and audit/compliance finding (SOC 2, PCI-DSS, HIPAA) once CVE patches stop.
- fit_signals: "We run ingress-nginx and just heard it's being retired / archived"; "our security team flagged the ingress controller as end-of-life"; "we need a Gateway API migration plan"; "auditors flagged EOL software in our request path"; mentions of IngressNightmare / CVE-2025-1974; platform team mid-migration weighing Traefik vs NGINX vs Envoy; "we're on a hosted platform (RKE2, IBM Cloud, Alibaba ACK) that shipped ingress-nginx by default."
- disqualifiers: Customer never used the community controller (e.g., already on a cloud-managed gateway, Istio, or Traefik) and has no NGINX affinity; pure greenfield with no Ingress legacy who can start straight on Gateway API with any vendor.
- value_framing: "Keep the NGINX technology your clusters were built on, but land on something with a full-time F5 engineering team, CVE SLAs, and a clear roadmap — either stay on the Ingress API with our supported controller now, or move to Gateway API with NGINX Gateway Fabric when you're ready."
- product_routing_note: Lead with NGINX Ingress Controller when the customer wants minimal disruption and to stay on the Ingress API short-term; lead with NGINX Gateway Fabric when they want to modernize once and adopt Gateway API. Both are valid F5 landing spots; NGF is the strategic direction.
- maturity_flag: GA
- source_currency_flag: Current
- source: kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/; kubernetes.io/blog/2026/01/29/ingress-nginx-statement/; blog.nginx.org (Ingress NGINX Alternative); docs.nginx.com/nginx-gateway-fabric/install/ingress-to-gateway/

### [K8S] Gateway API implementation (NGINX Gateway Fabric)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Kubernetes Gateway API traffic management with NGINX data plane
- plain_description: NGINX Gateway Fabric implements the Kubernetes Gateway API — the modern, role-oriented replacement for Ingress — using NGINX as the data plane, with control plane and data plane split into separate deployments.
- delivered_by: F5 NGINX Gateway Fabric (NGF)
- attribution_confidence: High
- customer_problem_solved: Legacy Ingress relied on annotation sprawl and was feature-frozen; Gateway API gives expressive, portable, role-separated routing (platform teams own Gateways/GatewayClasses, app teams own Routes) with reusable declarative policy.
- fit_signals: "We're standardizing on Gateway API"; "we want to get off annotation-heavy Ingress"; "platform team needs to delegate routing to app teams safely"; "we run multiple clusters and every cluster is its own snowflake"; "we want portability across clouds"; teams asking about HTTPRoute, GatewayClass, canary/weighted routing, model-aware/AI inference routing.
- disqualifiers: Team explicitly wants to stay on the Ingress API with minimal change (route to NIC instead); small single-cluster shop happy with a cloud-managed gateway; org with deep Istio/Envoy mesh investment already covering north-south via Gateway API.
- value_framing: "One conformant Gateway API implementation across every cluster and cloud, with the NGINX data plane you trust, plus enterprise NGINX Plus features (dynamic reconfiguration, session persistence, live metrics) and optional F5 WAF — all Kubernetes-native."
- product_routing_note: NGF is the strategic default for Gateway API. When the customer is not ready to leave the Ingress API, route to NIC and note NGF as the later bridge (they can run Ingress and Gateway API side by side).
- maturity_flag: GA (latest release NGF 2.6.6, June 26, 2026; conformant to Gateway API v1.5.1; NGINX Plus R37.0 data plane)
- source_currency_flag: Current
- source: f5.com/products/nginx/nginx-gateway-fabric; docs.nginx.com/nginx-gateway-fabric/; blog.nginx.org NGF 2.3.0 / 2.4.0 release notes; github.com/nginx/nginx-gateway-fabric CHANGELOG

### [K8S] supported Ingress-API controller (NGINX Ingress Controller)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Enterprise-supported Ingress controller on the Kubernetes Ingress API
- plain_description: F5 NGINX Ingress Controller is F5/NGINX's own controller (distinct from the retired community project) that implements the Kubernetes Ingress API plus richer NGINX custom resources, available as Apache 2.0 open source and as a commercial NGINX Plus edition.
- delivered_by: F5 NGINX Ingress Controller (NIC), repo nginx/kubernetes-ingress (formerly nginxinc/kubernetes-ingress)
- attribution_confidence: High
- customer_problem_solved: Teams leaving the retired community controller who want the smallest possible learning curve — same NGINX engine, direct annotation mappings, plus VirtualServer/Policy/TransportServer CRDs to escape annotation sprawl — with vendor CVE fixes and support.
- fit_signals: "We like NGINX and just want something supported that works"; "we can't do a full Gateway API rewrite right now"; "we need a vendor with an SLA and a roadmap for our ingress"; "we need to stay on the Ingress API for compliance/procurement reasons"; "who patches our ingress CVEs now that the community project is dead?"
- disqualifiers: Customer wants to modernize to Gateway API in one move (route to NGF); customer has no NGINX affinity and prefers Envoy/Traefik; cloud-managed-only shop.
- value_framing: "A drop-in-spirit NGINX controller with a full-time F5 team, Apache 2.0 OSS forever, direct migration tooling from the community controller, and a clean bridge to Gateway API via NGINX Gateway Fabric when you're ready — no dead end."
- product_routing_note: Lead here for risk-averse, NGINX-comfortable teams who want to stay on the Ingress API. Pair with NGF messaging as the future path. Note the NGINX Plus edition adds active health checks, dynamic reconfiguration, session persistence, JWT/OIDC. Recent releases (5.3.0, 5.4.0) added CORS support, configuration validation, and expanded annotation compatibility specifically to ease ingress-nginx migration.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/nginx/nginx-ingress-controller; blog.nginx.org (NGINX Ingress Controller 5.3.0 / 5.4.0); community.f5.com (Ingress NGINX Alternative)

### [K8S] config migration automation (ingress2gateway / Ingress-NGINX Migration Tool)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Automated conversion of existing Ingress config to Gateway API / NGINX resources
- plain_description: Tooling that reads existing Ingress resources and annotations and outputs equivalent Gateway API resources (for NGF) or NGINX Ingress Controller equivalents, reducing manual rewrite effort during migration.
- delivered_by: Open-source `ingress2gateway` CLI (Kubernetes SIG-Network subproject with an F5-authored NGINX provider) for the Gateway API path; a web-based "Ingress-NGINX Migration Tool" hosted at kubernetes.nginx.org for the community-ingress-nginx → F5 NGINX Ingress Controller path. F5 surfaced this "automation tooling" at AppWorld 2026 (March 2026).
- attribution_confidence: Medium — the migration CLI is a community SIG project (F5 contributed the NGINX provider), not a distinct F5-branded product. Network World reported F5 "added automation tooling to help customers migrate existing configurations to the new API. An open-source version is available alongside a commercial version bundled with NGINX Plus as part of the NGINX One package" — but no separately-branded commercial migration *product* was found in NGINX product docs; the commercial dimension is the destination NGF/NGINX Plus in NGINX One.
- customer_problem_solved: Manual migration of many Ingress objects and provider-specific annotations to a new model is error-prone and slow; automated conversion accelerates and de-risks the cutover.
- fit_signals: "We have hundreds of Ingress resources and annotations to migrate"; "how much of our config carries over automatically?"; "we're worried about annotation parity and snippets during migration."
- disqualifiers: Small config footprint where manual conversion is trivial; teams not migrating from Ingress at all.
- value_framing: "Convert most of your existing Ingress config automatically, then review and test — not a hand rewrite from scratch."
- product_routing_note: Position `ingress2gateway` (NGINX provider) for teams heading to NGF/Gateway API; position the web migration tool for teams moving from community ingress-nginx to NIC. Note both tools convert core Ingress only — CRDs (e.g. VirtualServer) and some annotations still need manual work.
- maturity_flag: GA (ingress2gateway is a released community CLI, v1.1.0; the web tool is publicly available)
- source_currency_flag: Current
- source: docs.nginx.com/nginx-gateway-fabric/install/ingress-to-gateway/; blog.nginx.org/blog/migrating-from-nic-to-ngf; kubernetes.nginx.org; networkworld.com article 4143922 (AppWorld 2026)

### [K8S] BIG-IP-to-cluster service exposure (Container Ingress Services)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Exposing Kubernetes/OpenShift services through existing BIG-IP devices
- plain_description: F5 BIG-IP Container Ingress Services (CIS) runs inside Kubernetes/OpenShift, watches the cluster API, and dynamically programs an external BIG-IP (via AS3) so services can be exposed and load-balanced through the BIG-IP estate the org already runs.
- delivered_by: F5 BIG-IP Container Ingress Services (CIS) — controller image k8s-bigip-ctlr
- attribution_confidence: High
- customer_problem_solved: NetOps-standardized organizations want cluster services fronted by the BIG-IP they already operate (with its L4-L7 services, WAF, SSL visibility, IPAM, identity-aware ingress) instead of standing up a separate in-cluster edge, and they need BIG-IP pools to track pod churn automatically.
- fit_signals: "All our north-south traffic goes through BIG-IP and we want Kubernetes to be no different"; "NetOps owns the load balancers, not the app teams"; "we're on OpenShift and standardized on F5"; "we need SSL inspection / IPAM / identity-aware access in front of the cluster"; "we want multi-cluster ingress / blue-green OpenShift migrations."
- disqualifiers: Platform-team-led shops with no BIG-IP estate and no desire for hardware/edge appliances (route to NGINX-native NGF/NIC); pure cloud-native greenfield; teams wanting everything managed inside the cluster.
- value_framing: "Extend the BIG-IP you already trust into Kubernetes without manual reconfiguration — CIS keeps BIG-IP pools in sync with pods automatically, and you keep your existing NetOps controls, WAF, and visibility at the edge."
- product_routing_note: Lead with CIS for NetOps-led BIG-IP shops. Where the customer also wants an efficient in-cluster ingress tier, pair CIS with NGINX Ingress Controller via IngressLink. CIS is open source and support is included with any existing BIG-IP support entitlement. CIS multi-cluster ingress (per-application blue/green OpenShift migrations) is called out by Red Hat as unique in the market.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/container-ingress-services; clouddocs.f5.com/containers/latest/; redhat.com/en/blog/multi-cluster-red-hat-openshift-ingress-f5-big-ip

### [K8S] two-tier BIG-IP + NGINX ingress (IngressLink)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Coordinated BIG-IP edge + NGINX Ingress Controller in-cluster tier
- plain_description: F5 IngressLink uses a CRD to link CIS/BIG-IP (outside the cluster, as L3/4 edge load balancer) with NGINX Ingress Controller instances (inside the cluster), so BIG-IP automatically adapts as the NGINX Ingress pods scale.
- delivered_by: F5 IngressLink (combines BIG-IP, CIS, and NGINX Ingress Controller)
- attribution_confidence: High
- customer_problem_solved: Organizations that split responsibilities between NetOps (BIG-IP edge) and DevOps (NGINX in-cluster) want the two tiers to stay coordinated automatically rather than through manual handoffs.
- fit_signals: "NetOps runs the edge, DevOps runs ingress inside the cluster, and they don't coordinate well"; "we want BIG-IP at the perimeter and NGINX handling ingress"; "we need the edge LB to track our ingress pods automatically."
- disqualifiers: Single-team platform shops; no BIG-IP estate; teams wanting a single ingress tier only.
- value_framing: "Best of both: BIG-IP perimeter controls plus efficient NGINX in-cluster ingress, kept in sync automatically across the NetOps/DevOps boundary."
- product_routing_note: Position IngressLink only when both a BIG-IP edge and an in-cluster NGINX tier are in play. If the customer is heading to Gateway API, note IngressLink is tied to NGINX Ingress Controller (Ingress API), not NGF. In IngressLink, BIG-IP typically does L3/4 and TLS/WAF may sit on the NGINX tier — confirm the intended split per deal.
- maturity_flag: GA
- source_currency_flag: Current
- source: clouddocs.f5.com/containers/latest/userguide/ingresslink/; f5.com/company/blog/nginx/deploying-big-ip-nginx-ingress-controller-same-architecture

### [K8S] Kubernetes-native ingress/egress gateway (BIG-IP Next for Kubernetes / SPK, enterprise)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: In-cluster ingress/egress control plane with the BIG-IP TMM data plane
- plain_description: BIG-IP Next Service Proxy for Kubernetes (SPK) — renamed BIG-IP Next for Kubernetes from the 2.0.0 release — is headless, Kubernetes-native software running inside the cluster that provides a single point of ingress/egress networking, security, and visibility using the BIG-IP TMM data plane and Kubernetes CRDs.
- delivered_by: BIG-IP Next for Kubernetes (formerly BIG-IP Next Service Proxy for Kubernetes / SPK)
- attribution_confidence: Medium — enterprise-side positioning; the product's origin and heaviest documentation are telco/5G (SCTP, Diameter, GTP, SIP), which belongs to doc 12. Enterprise use cases (multi-network integration, egress control, security boundary) are documented but the enterprise framing is thinner in public sources.
- customer_problem_solved: Kubernetes networking was designed for HTTP/HTTPS with a single external gateway and ignores egress; SPK/BIG-IP Next for Kubernetes adds a central, high-performance ingress AND egress control point with firewalling, topology hiding, and per-workload visibility, aligned to Kubernetes patterns.
- fit_signals: "We need egress control, not just ingress"; "we need protocols beyond HTTP or multiple external networks"; "we need a security boundary between the cluster and the outside network"; "we need per-subscriber/per-workload traffic visibility."
- disqualifiers: Standard HTTP/HTTPS north-south only (route to NGF/NIC/CIS); telco/5G core signaling use cases (belongs to doc 12); AI-infrastructure/DPU workloads (belongs to doc 11).
- value_framing: "A Kubernetes-native, high-performance ingress and egress gateway with the proven BIG-IP TMM data plane and enterprise security, for clusters whose networking needs exceed plain HTTP ingress."
- product_routing_note: Only surface for enterprise cases needing egress control, multi-network, or a hard security boundary. For ordinary app ingress, route to NGF/NIC/CIS. Send telco to doc 12, AI/DPU to doc 11.
- maturity_flag: GA (BIG-IP Next for Kubernetes 2.0.0-GA; note 2.0.0-GA supported only on NVIDIA BlueField-3 DPU — a doc 11 concern; earlier SPK 1.7.x host-based releases exist)
- source_currency_flag: Current
- source: f5.com/products/big-ip/next/big-ip-next-for-kubernetes; my.f5.com K89026308 (lifecycle policy / rename); community.f5.com SPK technical article 300547

### [K8S] Kubernetes-native WAF insertion (F5 WAF for NGINX)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Security insertion at the Kubernetes gateway/ingress layer
- plain_description: F5 WAF for NGINX attaches enterprise WAF protection at the NGINX entry point in Kubernetes, working with both NGINX Gateway Fabric and NGINX Ingress Controller through Kubernetes-native, declarative (JSON/YAML) policy workflows.
- delivered_by: F5 WAF for NGINX (integrated with F5 NGINX Gateway Fabric and F5 NGINX Ingress Controller). Deep WAF capability content lives in docs 01/02.
- attribution_confidence: High (for the insertion-point fact; capability depth deferred to docs 01/02)
- customer_problem_solved: As the Kubernetes gateway becomes the highest-value attack target, security and platform teams need consistent WAF protection across services/clusters applied through cluster-native workflows rather than one-off manual changes.
- fit_signals: "We need OWASP/API protection right at our Kubernetes ingress"; "our WAF policy lives 'somewhere else' and we want it in cluster workflows"; "we need security-as-code / declarative WAF policy in our pipelines"; "we're on OpenShift and need certified WAF at the gateway."
- disqualifiers: WAF capability/feature questions themselves (route to docs 01/02); non-Kubernetes WAF; customers with no NGINX ingress/gateway footprint.
- value_framing: "Bring F5's WAF directly into your Kubernetes gateway workflow — one consistent, automated, security-as-code experience across both NGINX Gateway Fabric and NGINX Ingress Controller."
- product_routing_note: Treat as an insertion point that strengthens NGF/NIC deals; hand WAF depth to docs 01/02. F5 WAF for NGINX support first shipped in NGINX Gateway Fabric 2.6, which NGINX described as "one of the first Gateway API implementations to offer enterprise-grade WAF capabilities natively." On OpenShift, note the certified operator for F5 WAF for NGINX on NGF (May 2026 Red Hat announcement).
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/company/blog/waf-for-nginx-now-integrates-with-f5-nginx-gateway; blog.nginx.org (NGF 2.6 release); f5.com press release (Red Hat Kubernetes/AI application security, May 2026)

### [K8S] Red Hat OpenShift joint solutions
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Certified F5 solutions on Red Hat OpenShift
- plain_description: F5 and Red Hat maintain certified integrations for OpenShift, spanning NGINX Gateway Fabric (certified operator), F5 WAF for NGINX on NGF, CIS (certified operator), and — announced at AppWorld 2026 — certified OpenShift Operators for F5's AI security products plus AI quickstarts.
- delivered_by: F5 NGINX Gateway Fabric (certified for OpenShift); F5 WAF for NGINX on NGF (certified operator); F5 BIG-IP Container Ingress Services (certified operator); F5 AI Guardrails & F5 AI Red Team (certified OpenShift Operators — AI-security, cross-reference docs 01/02/11)
- attribution_confidence: High
- customer_problem_solved: OpenShift-standardized (often regulated) enterprises want vendor-certified, lifecycle-managed integrations that install through familiar OpenShift/OLM workflows rather than bespoke deployments.
- fit_signals: The customer says "OpenShift" (strong fit signal on its own); "we need Red Hat–certified operators"; "we run regulated workloads on OpenShift and need vendor-backed ingress/security"; "we want OLM-managed install and upgrades."
- disqualifiers: Non-OpenShift Kubernetes (still fits F5 products, just not the OpenShift-specific certification angle); pure cloud-managed Kubernetes with no OpenShift.
- value_framing: "F5 traffic management and security certified and lifecycle-managed on OpenShift — installed and upgraded through the OperatorHub/OLM workflows your platform team already uses."
- product_routing_note: When "OpenShift" is mentioned, lead with the relevant certified F5 product (NGF or CIS for ingress; F5 WAF for NGINX for security) and note the certification. NOTE — two distinct AppWorld/2026 Red Hat announcement waves exist: (a) the AppWorld 2026 (March) announcement centered on certified OpenShift Operators for F5 AI Guardrails and F5 AI Red Team plus AI quickstarts; (b) a May 11, 2026 expanded-portfolio announcement led with F5 WAF for NGINX on NGINX Gateway Fabric. Route AI-security depth to docs 01/02/11. NGF was separately certified for OpenShift (NGF 2.2 certified operator; OpenShift 4.19+ ships native Gateway API).
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/company/blog/f5-nginx-gateway-fabric-is-a-certified-solution-for-red-hat-openshift; investors.f5.com AppWorld 2026 Red Hat press release; f5.com/company/news/press-releases (Red Hat, May 2026); catalog.redhat.com (CIS operator); community.f5.com NGF-on-OpenShift guide 344686

### [K8S] automatic backend/pod tracking
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Native reconciliation of load-balancer upstreams with Kubernetes pod state
- plain_description: F5's Kubernetes traffic products watch cluster state and keep their upstreams/pools aligned with the current set of pods automatically, so autoscaling, rolling deployments, and pod replacement don't require manual config edits.
- delivered_by: F5 NGINX Ingress Controller; F5 NGINX Gateway Fabric; F5 BIG-IP Container Ingress Services (keeps BIG-IP pools synced)
- attribution_confidence: High
- customer_problem_solved: In dynamic clusters, backends change constantly; a traffic layer that needs manual reconfiguration on every scaling event doesn't fit how Kubernetes actually runs.
- fit_signals: "Our pods scale up and down constantly"; "we don't want anyone hand-editing upstream lists"; "we need the edge/ingress to track pod churn automatically"; "we do frequent rolling deployments."
- disqualifiers: Static workloads that rarely change; non-Kubernetes environments.
- value_framing: "Your traffic layer follows Kubernetes automatically — scale, deploy, and replace pods without touching load-balancer config."
- product_routing_note: This is a shared strength across NIC, NGF, and CIS; use it to reinforce whichever product the buyer persona points to. NGINX Plus data plane adds dynamic upstream reconfiguration without reloads.
- maturity_flag: GA
- source_currency_flag: Current
- source: blog.nginx.org/blog/built-for-change-how-nginx-ingress-controller-and-nginx-gateway-fabric-handle-kubernetes-backend-changes-natively; f5.com/company/blog/nginx/deploying-big-ip-nginx-ingress-controller-same-architecture

### [K8S] AI inference-aware routing (Gateway API Inference Extension)
- solution_area: Kubernetes & Modern Application Delivery
- capability_name: Model-aware traffic routing for in-cluster AI inference
- plain_description: NGINX Gateway Fabric supports the Gateway API Inference Extension, routing requests by model type/version and cost/performance profile to self-hosted generative-AI models on Kubernetes, using an endpoint picker for inference-aware load balancing.
- delivered_by: F5 NGINX Gateway Fabric
- attribution_confidence: High (as a traffic-management capability; deep AI-workload/DPU content belongs to doc 11)
- customer_problem_solved: AI inference traffic is unpredictable (variable prompt sizes/compute); static load balancing overloads some backends and underuses others, wasting expensive GPU capacity.
- fit_signals: "We're self-hosting models on Kubernetes and need smart routing"; "we run multiple model versions / LoRA adapters and need to split traffic"; "we want to route lower-value requests to cheaper models"; "GPU utilization is killing our budget."
- disqualifiers: No in-cluster AI inference; teams whose AI routing is handled by a dedicated AI gateway (cross-reference doc 11); pure classic web/API ingress.
- value_framing: "Bring AI inference into your standard Kubernetes traffic model — route by model and runtime signals to protect GPU spend and user experience, using the same Gateway API you use for everything else."
- product_routing_note: Surface for NGF deals involving self-hosted models, but route AI-infrastructure depth (DPUs, BIG-IP Next for Kubernetes on BlueField) to doc 11.
- maturity_flag: GA (Inference Extension support in NGF; the upstream extension itself is an evolving Kubernetes project — Istio and cloud vendors' support is in beta/experimental)
- source_currency_flag: Current
- source: docs.nginx.com/nginx-gateway-fabric/how-to/gateway-api-inference-extension/; f5.com/company/blog/standardize-ai-delivery-with-f5-nginx-gateway-fabric

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Core buyer split (most important routing axis).** Kubernetes ingress deals at F5 divide by persona:

- **NetOps-led, BIG-IP-standardized shops** → lead with **BIG-IP Container Ingress Services (CIS)**. Signal: "all north-south goes through BIG-IP," "NetOps owns the load balancers," existing BIG-IP estate, SSL inspection/IPAM/identity-aware ingress requirements, OpenShift + F5 standardization. If they also want an efficient in-cluster tier, add **IngressLink** (BIG-IP edge + NGINX Ingress Controller).
- **Platform-team-led, NGINX-native shops** → lead with **NGINX Gateway Fabric (NGF)** for Gateway API adopters, or **NGINX Ingress Controller (NIC)** for teams staying on the Ingress API short-term. Signal: DevOps/platform team owns ingress, Kubernetes-native/self-service culture, annotation fatigue, multi-cluster portability goals.

**Ingress API vs Gateway API (within the NGINX-native path).**
- Want minimal change / stay on Ingress API / procurement or compliance reasons to keep Ingress → **NIC** now, with **NGF** as the documented bridge later (they can run both side by side).
- Want to modernize once and adopt the strategic standard → **NGF**.

**On-prem vs cloud-native vs SaaS.**
- Heavy on-prem / hybrid with existing appliances → CIS (and IngressLink) or NGF/NIC on-cluster.
- Cloud-native / multi-cloud portability → NGF (portable Gateway API resources).
- SaaS ingress to clusters via F5 Distributed Cloud (XC) → mention as a routing option only; deep content in docs 05/09. Do not pitch XC ingress depth here.

**Self-managed vs managed / packaging.**
- OSS / self-managed → NGF OSS or NIC OSS (Apache 2.0).
- Commercial / supported → NGINX Plus data plane; the **NGINX One** package bundles NGINX Plus, NGINX Ingress Controller, Gateway API (NGF), F5 WAF for NGINX, and the NGINX One console. Use NGINX One to answer "we want one thing to buy and manage." NGF connects to and is managed via the NGINX One Console (since NGF 2.1.0, August 2025).

**OpenShift.** When the customer says "OpenShift," treat it as a strong fit signal and lead with the certified F5 product for their need (NGF or CIS for ingress; F5 WAF for NGINX for security), emphasizing Red Hat certification and OLM lifecycle management.

**Coexistence & migration.** NGF and NIC can run side by side; Ingress and Gateway API can coexist during migration. CIS + NIC coexist via IngressLink. The migration tools (`ingress2gateway` NGINX provider → Gateway API/NGF; web Ingress-NGINX Migration Tool → NIC) support staged cutovers. Where public F5 guidance doesn't state a specific recommendation (e.g., an official "always pick NGF over NIC" rule), do not invent it — present both as valid landing spots with NGF as the stated strategic direction.

**Enterprise SPK / BIG-IP Next for Kubernetes** is a narrower routing target: only when egress control, non-HTTP protocols, multi-network, or a hard cluster security boundary are in play. Telco/5G → doc 12; AI/DPU → doc 11.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **"We never used the community ingress-nginx and have no NGINX affinity."** The retirement urgency doesn't apply; don't force the migration pitch. Qualify for Gateway API interest instead.
- **Pure cloud-managed, single-cloud, single-cluster shop happy with ALB/AGIC/GKE Gateway.** Weak fit for on-cluster F5 ingress; see the cloud-gateway objection below before conceding.
- **No BIG-IP estate and no appliance appetite.** Don't lead with CIS/IngressLink; route to NGINX-native.
- **WAF capability/feature deep-dives.** Not this doc — route to docs 01/02. F5 WAF for NGINX appears here only as an insertion point.
- **Telco/5G core signaling (SCTP, Diameter, GTP, SIP).** Route to doc 12, not SPK-as-enterprise here.
- **AI infrastructure / DPU / GPU-node data-path acceleration.** Route to doc 11; only inference-aware *routing* via NGF Gateway API belongs here.
- **F5 Distributed Cloud SaaS ingress depth.** Mention as an option; depth in docs 05/09.
- **Static, rarely-changing workloads.** The dynamic pod-tracking value is muted; lead with something else.

### 3c. Competitive positioning and objection handling (all lower-confidence, flagged)

*All competitive claims below are bounded and should be treated as lower-confidence. This market consolidates fast; verify vendor status at deal time.*

**Vendor independence/status check (as of mid-2026):**
- **Kong Inc.** — independent, private, well-funded. Per Kong's November 19, 2024 press release: "closed a $175 million in up-round Series E financing…at a $2 billion valuation…brings Kong's total capital raised to $345 million," led by Tiger Global, co-led by Balderton. Acquired OpenMeter (Sep 2025). Gateway API implementation (Kong Ingress / Kong Gateway). Confidence: Medium.
- **Traefik Labs** — independent, private, Series A (~$11–15M total, Lyon/SF). Per Traefik Labs' March 24, 2026 KubeCon EU press release: "IBM Cloud, Nutanix, OVHcloud, SUSE, TIBCO, and additional platform vendors…have each independently selected Traefik Proxy." Traefik Proxy 3.7 ("Langres") GA'd an Ingress NGINX Provider with "85+ supported Ingress NGINX annotations…covering more than 90% of real-world usage"; SUSE makes Traefik the default in RKE2 "starting with v1.36." No acquisitions. Confidence: Medium.
- **Envoy / Envoy Gateway** — CNCF graduated project (Envoy graduated November 28, 2018); vendor-neutral, not owned by one company. Confidence: High.
- **Istio** — CNCF graduated; Gateway API adopted, ambient mode maturing (ambient multicluster beta and Gateway API Inference Extension beta announced at KubeCon EU 2026); commercial distributions via Solo.io (Gloo). Confidence: High.
- **kgateway (formerly Gloo/Gloo OSS)** — Solo.io donated Gloo to CNCF, renamed kgateway (sandbox); Envoy-based. Confidence: Medium.
- **HAProxy** — HAProxy Technologies, independent; conformant Gateway API implementation since v0.17. Confidence: Medium.
- **Cloud-managed:** AWS Load Balancer Controller reached GA with Gateway API support (v3.x, 2026); GKE Gateway controller (passes v1.5.0 core conformance); Azure AGIC / Application Gateway for Containers. Confidence: High.

**Category positioning (public-evidence-based, not head-to-head benchmarks):**

- **vs other Gateway API implementations (Envoy Gateway, Istio, Traefik, Kong, HAProxy, kgateway):** F5's public differentiators are (1) staying on the NGINX data plane clusters were built on — minimal retraining for ingress-nginx/NGINX shops; (2) a supported vendor path with CVE SLAs and roadmap; (3) NGINX Plus enterprise features (dynamic reconfiguration, session persistence, latency-aware LB, live metrics) plus integrated F5 WAF; (4) one implementation portable across clouds and on-prem. Per NGINX's own NGF 2.3.0 blog, "NGF now constitutes the majority of all downloads for ingress and Kubernetes traffic management and is among the most popular Gateway API implementations in the CNCF" (the same blog also stated NGF was "one of only five generally available Gateway API implementations" at that release — treat the "five" figure as an F5 self-description tied to the community status page at that date, not an independently re-verified fact). Do NOT claim performance superiority over Envoy/Istio without a cited benchmark — third-party commentary often rates Istio highly on control-plane efficiency.

- **vs service mesh overlap (Istio ambient, Cilium):** These blur north-south and east-west. F5's honest framing: if the customer already runs a mesh that covers Gateway API north-south, NGF may be redundant for ingress; NGF's angle is teams who want dedicated, NGINX-based north-south without adopting a full mesh. Flag as lower-confidence and situational.

- **Objection: "We'll just use the cloud provider's gateway controller (ALB/AGIC/GKE Gateway)."** Legitimate for single-cloud, deeply cloud-integrated deployments — concede that's the path of least resistance there. Counter-points supported by public sources: (1) cloud controllers inherit their LB's feature limits — e.g., third-party analysis notes AWS's Gateway API support historically lacked TCPRoute/UDPRoute, forcing a disjointed model for raw TCP/UDP; (2) portability — cloud-native controllers don't move across clouds or on-prem, so multi-cloud/hybrid orgs get a different control model per environment, whereas NGF gives one portable Gateway API implementation everywhere; (3) advanced policy, WAF, and enterprise support may require cloud-specific CRDs or separate products. Recommend: for single-cloud with no portability need, the cloud controller is reasonable; for hybrid/multi-cloud/on-prem or where consistent NGINX+WAF is wanted, standardize on NGF.

- **Objection: "We're already covered by X."** If X is the retired community ingress-nginx, that's the opening — it's unmaintained (no CVE patches post-March 2026) and an audit finding. If X is a maintained competitor (Traefik/Kong/Envoy/Istio), don't disparage; qualify for NGINX affinity, enterprise support/SLA needs, F5 WAF integration, and portability, and fall back to coexistence rather than rip-and-replace. Note Traefik is marketing itself hardest as the ingress-nginx "drop-in" (>90% annotation coverage claim) — expect it as the most common competitive encounter on retirement-driven deals.

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (F5 renames frequently — verify every engagement):**
- **`ingress-nginx` (community) vs F5 "NGINX Ingress Controller" (NIC):** the single most-confused pair. `ingress-nginx` = `kubernetes/ingress-nginx`, community, RETIRED March 2026 (announced by SIG Network + Security Response Committee, Nov 11, 2025). NIC = `nginx/kubernetes-ingress` (formerly `nginxinc/kubernetes-ingress`), F5, actively maintained, OSS (Apache 2.0) + commercial. Always confirm which one a customer means.
- **NGINX Gateway Fabric (NGF)** — OSS project + NGINX Plus commercial data plane; connects to/managed via NGINX One Console (since NGF 2.1.0, Aug 2025). Latest release NGF 2.6.6 (June 26, 2026); Gateway API v1.5.1, NGINX Plus R37.0. "Commercial version bundled in the NGINX One package" is F5/press framing (Network World) — confirmed as NGINX One connectivity + private-registry Plus images, not independently confirmed as a distinct bundle SKU. Flag as such.
- **BIG-IP Next Service Proxy for Kubernetes (SPK) → BIG-IP Next for Kubernetes** — renamed from the 2.0.0 release (per my.f5.com K89026308). Docs are consolidating; "SPK," "BIG-IP Next for Kubernetes (Host)," and "(DPU)" variants all appear. 2.0.0-GA supported only on NVIDIA BlueField-3 DPU (a doc 11 concern). Enterprise vs telco framing overlaps heavily; telco/5G belongs to doc 12.
- **NGINX One** — packaging umbrella (NGINX Plus, NIC, Gateway API/NGF, F5 WAF for NGINX, NGINX One Console). Packaging composition is perishable.
- **F5 WAF for NGINX** — the current name for the NGINX-layer WAF; older material may say "NGINX App Protect WAF." Insertion point only here.
- **CIS** — "BIG-IP Container Ingress Services," controller image `k8s-bigip-ctlr`; name stable but sometimes shortened to "F5 BIG-IP Controller for Kubernetes."

**Explicitly NOT verified (do not assert):**
- Whether the AppWorld 2026 "migration automation tooling" is anything more than the community `ingress2gateway` CLI (F5 NGINX provider) plus the web Ingress-NGINX Migration Tool — no distinct F5-branded commercial migration *product* was found in public sources.
- The exact "commercial NGF bundled in NGINX One" as a separately-priced SKU — only NGINX One connectivity and commercial Plus images were confirmed.
- The "one of only five GA Gateway API implementations" claim beyond F5's own NGF 2.3.0 blog citing the community status page at that date.
- Any head-to-head performance claims between NGF and Envoy/Istio/Traefik — not verified; do not assert.
- Precise enterprise (non-telco) adoption or feature scope of BIG-IP Next for Kubernetes/SPK beyond documented capabilities.
- Exact percentage of clusters using community ingress-nginx — Datadog's figure is "about 50% of cloud native environments" (kubernetes.io Jan 29, 2026 statement); third-party guides cite a wider 40–62% range. Treat as approximate.

**Primary sources leaned on:** kubernetes.io official blog (retirement Nov 11, 2025 + Jan 29, 2026 statement); f5.com product pages (NGF, NIC, CIS, BIG-IP Next for Kubernetes, NGINX One); docs.nginx.com; blog.nginx.org; community.f5.com / DevCentral; clouddocs.f5.com; investors.f5.com and f5.com press releases (AppWorld 2026, Red Hat May 2026); catalog.redhat.com; my.f5.com KB K89026308 (lifecycle policy); github.com/nginx/nginx-gateway-fabric CHANGELOG.
**Third-party sources for competitive reality-check:** Network World (AppWorld 2026 coverage, article 4143922); Google Open Source Blog; AWS/Fastly/Kong/Solo.io blogs; CNCF; Gateway API SIG implementations list; Traefik Labs press (Mar 24, 2026); Kong press (Nov 19, 2024); Tracxn/PitchBook/Crunchbase (vendor status); InfoQ (AWS Gateway API GA). Treat SEO listicles (G2/Slashdot) as low-trust.