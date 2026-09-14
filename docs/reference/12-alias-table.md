# alias-table.md — Mention scoring aliases for F5

Derived from `41-coverage-matrix.md` (July 2026 validation). Regenerate whenever the coverage matrix changes. Matching is case-insensitive; match on the longest alias first to avoid "NGINX" matching inside "F5 NGINX Plus".

## Scoring rules that use this table

- **Full (1.0):** any Current name, or any alias with "F5" within the same sentence.
- **Partial (0.5):** an alias or product name with no F5 attribution in the sentence (typically bare "NGINX").
- **Stale (counted as Full or Partial per above, plus flagged `stale_name`):** a Former or Retired name used as if current. Report stale-name rate per engine per category; it is a direct proxy for the age of the engine's parametric knowledge of F5.
- **Inaccurate (0, flagged `inaccurate`):** a recommendation to adopt a discontinued, retired, or non-sellable product (see the Inaccurate list). Report inaccurate-mention rate separately; these are mentions that harm.
- **Ambiguous (do not count; flagged `ambiguous`):** terms that may or may not refer to F5. Resolve by context or exclude.

## Current names, former names, and category

| Current name | Former / alias names | Category (doc) | Notes |
|---|---|---|---|
| F5 | — | all | Parent brand |
| F5 Distributed Cloud, XC, Distributed Cloud Services | Volterra | 01,02,03,04,05,06,09,11 | "Volterra" is stale |
| XC API Security | Wib | 01 | "Wib" is stale |
| F5 API Security Local Edition | local API discovery (EA) | 01 | New Jun 2026; models may not know it |
| XC WAF, XC WAAP | Silverline WAF | 02 | "Silverline" is retired → Inaccurate if recommended |
| XC Web App Scanning | Heyhack | 02 | |
| XC Bot Defense | Shape, Shape Security, Shape Enterprise Defense | 03 | "Shape" is stale |
| XC Account Protection | Shape AI Fraud Engine, SAFE | 03 | Limited Availability; recommending as GA is Inaccurate |
| XC Authentication Intelligence | — | 03 | Legacy/sunset; recommending it is Inaccurate |
| XC Data Intelligence | — | 03 | |
| XC Aggregator Management | — | 03 | |
| XC Client-Side Defense | — | 03 | |
| XC DDoS Mitigation | Silverline DDoS | 04 | "Silverline" retired → Inaccurate if recommended |
| BIG-IP DDoS Hybrid Defender, DHD | Herculon | 04 | |
| F5 DoS for NGINX | NGINX App Protect DoS | 04 | Renamed Sep 2025 |
| XC App Connect, XC Load Balancer, XC App Delivery | — | 05, 09 | |
| BIG-IP LTM, BIG-IP, TMOS | Local Traffic Manager | 05 | "BIG-IP" alone = Full |
| BIG-IP Virtual Edition, BIG-IP VE | — | 05 | |
| rSeries, VELOS, F5OS | — | 05, 14 | Hardware; Full |
| iSeries, VIPRION | — | 14 | Legacy hardware; stale if recommended for new purchase |
| NGINX Plus, NGINX One, F5 NGINX | — | 05, 10, 14 | "NGINX Plus" bare = Partial; "F5 NGINX" = Full |
| NGINX Open Source, NGINX OSS, nginx | — | 05, 10, 14 | Bare "nginx" = Partial; see Ambiguous |
| NGINXaaS for Azure | — | 05 | |
| F5 WAF for NGINX | NGINX App Protect WAF, NAP, App Protect | 01, 02 | Renamed ~mid-2025 |
| NGINX Gateway Fabric, NGF | — | 10 | |
| NGINX Ingress Controller, NIC (F5) | — | 10 | See Ambiguous: not the community ingress-nginx |
| BIG-IP Container Ingress Services, CIS | — | 10 | |
| F5 IngressLink | — | 10 | |
| BIG-IP Next for Kubernetes, BNK | BIG-IP Next SPK, SPK, Service Proxy for Kubernetes | 10, 11, 12 | Active product; do not confuse with discontinued BIG-IP Next ADC |
| BIG-IP Next CNFs | — | 12 | Active |
| BIG-IP DNS | GTM, Global Traffic Manager | 06 | "GTM" is stale |
| XC DNS, XC DNS Load Balancer | — | 06 | Two products; count either |
| BIG-IP Advanced WAF | ASM, Application Security Manager | 01, 02 | "ASM" is stale (EoS 2021) |
| BIG-IP Zero Trust Access | APM, Access Policy Manager | 07 | Renamed Mar 2026, branding-only; "APM" is stale but very common |
| BIG-IP AFM | Advanced Firewall Manager | 04, 12 | |
| BIG-IP PEM | Policy Enforcement Manager | 12 | |
| F5 SSL Orchestrator, SSLO | — | 08 | |
| XC Network Connect | — | 09 | |
| XC Customer Edge, CE | Volterra node | 09 | |
| XC App Stack | — | 09 | Substrate; count as Full, low priority |
| F5 AI Gateway | — | 11 | |
| F5 AI Red Team | CalypsoAI | 11 | |
| F5 AI Guardrails | CalypsoAI | 11 | |
| F5 AI Remediate | — | 11 | GA unconfirmed |
| F5 AI Security Platform | SurePath AI | 11 | Jun 2026; models likely unaware |
| F5 Insight for ADSP | Threat Stack, Distributed Cloud AIP, Fletch | 13 | "Threat Stack" and "AIP" are retired → stale |
| XC Synthetic Monitoring | — | 13 | |
| BIG-IP Telemetry Streaming | — | 13 | |
| BIG-IQ | — | 13, 14 | Current |
| NGINX One Console | NGINX Instance Manager, NGINX Amplify | 14 | "Amplify" retired Jan 2026 → stale |
| iRules | — | 05 | Programmability; counts as Full (unambiguously F5) |

## Inaccurate list (mention counts 0, flag `inaccurate`)

A recommendation to adopt any of these as a current or go-forward product:

- **BIG-IP Next** (the ADC software line) — discontinued; final v20.3 EoL Apr 30 2025. Highest-risk error; expect models trained 2023–2024 to recommend it. Distinguish from BIG-IP Next for Kubernetes / CNFs, which are active.
- **Silverline** (any service) — retired Jun 30 2025.
- **NGINX Amplify** — retired Jan 31 2026.
- **NGINX ModSecurity WAF** — EoS Apr 2022.
- **Traffix SDC** — wind-down, installed-base only.
- **XC Authentication Intelligence** — legacy/sunset.
- **XC Account Protection** described as GA — it is Limited Availability.
- **XC Universal ZTNA** — pre-Early Access, not sellable.
- **Aspen Mesh** — status uncertain; flag rather than score.

A historical mention ("F5 discontinued BIG-IP Next") is Contextual (0.25), not Inaccurate.

## Ambiguous terms (exclude unless context resolves)

- **nginx / NGINX** — refers to open-source NGINX (F5-owned, Partial) unless context indicates the community fork or a generic reverse proxy concept. Bare "nginx" in a Kubernetes context may mean `ingress-nginx`, the retired community project, which is **not** F5's product. Score Partial only when the context is proxy/load balancing; flag `ambiguous` in ingress contexts.
- **"F5"** as a keyboard key or refresh action — exclude by context.
- **"Shape"** — exclude unless paired with security, bot, or fraud terms.
- **"Volterra"** — near-unambiguous but very stale; flag `stale_name`.

## Competitor sets (names only, for share-of-model denominators)

Seeded from each doc's Layer 3c (names the corpus names explicitly), supplemented with obvious category incumbents the corpus omits. Names marked † appear in the corpus; unmarked names are additions for the visibility agent to confirm against the corpus or the market before the first baseline. The corpus flags 3c positioning as lower confidence; names are sufficient here.

| Category (doc) | Competitors to track |
|---|---|
| 01 API Security | Salt Security†, Akamai API Security† (ex-Noname), Traceable†, Cequence†, Imperva†, Wallarm†, 42Crunch†, Cloudflare, Apigee, Kong |
| 02 WAAP | ModSecurity/Coraza†, Akamai, Cloudflare, Imperva, AWS WAF, Azure Front Door/App Gateway, Fastly, Radware |
| 03 Bot / Fraud | Akamai†, Cloudflare†, DataDome†, HUMAN Security†, Arkose Labs†, Imperva, Kasada, Fastly |
| 04 DDoS | ISP-provided mitigation† (the corpus's main foil), Cloudflare, Akamai Prolexic, Radware, Netscout Arbor, AWS Shield, Azure DDoS, Corero |
| 05 ADC | Citrix NetScaler†, VMware Avi (Broadcom)†, A10†, Radware Alteon†, HAProxy†, Envoy†, AWS ALB/NLB†, Azure LB/App Gateway†, Google Cloud LB†, Kemp (Progress), Traefik |
| 06 DNS / GSLB | IBM NS1 Connect†, Citrix NetScaler GSLB†, AWS Route 53†, Cloudflare, Akamai Edge DNS, Azure Traffic Manager, Infoblox, BlueCat |
| 07 Access / ZTA | Cisco AnyConnect / Secure Client†, Ivanti (Pulse)†, Zscaler, Palo Alto Prisma Access, Cloudflare Access, Netskope, Okta, Microsoft Entra, Citrix Gateway, Fortinet |
| 08 SSL Orchestration | Gigamon (GigaSMART)†, A10 Thunder SSLi†, Broadcom†, Palo Alto, Fortinet, Cisco, Netscout |
| 09 Multicloud Networking | Aviatrix†, Alkira†, Prosimo†, Cisco, Cloudflare, Megaport, hyperscaler transit gateways |
| 10 Kubernetes | Envoy / Envoy Gateway†, HAProxy†, Istio†, Kong†, Traefik†, kgateway (ex-Gloo)†, ingress-nginx (community, retired), Cilium, AWS Load Balancer Controller, GKE Gateway |
| 11 AI Delivery & Security | HiddenLayer†, Lakera (Check Point)†, Protect AI (Palo Alto)†, Robust Intelligence (Cisco)†, Prompt Security (SentinelOne)†, Cloudflare AI Gateway, Kong AI Gateway, Zscaler, Netskope, Portkey, LiteLLM. Note: several standalone names were acquired 2025–26; models may cite the old standalone names. |
| 12 Service Provider | Ericsson†, Nokia†, FD.io/VPP open-source NAT†, A10, Juniper, Cisco, Casa, Radware |
| 13 Observability | Grafana† (corpus notes F5 builds on it — coexistence, not displacement), Datadog, Splunk, Dynatrace, New Relic, Elastic, ThousandEyes, Catchpoint |

Regenerate this table when Layer 3c changes. Verify names against the corpus rather than this file if they disagree; the corpus is authoritative.
