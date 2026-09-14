# coverage-matrix.md — Product → Document Coverage

Purpose: an auditable guarantee that every GA F5 product/module appears in the corpus somewhere, even though the corpus is keyed by solution area. Update this table as research sessions complete and as F5's portfolio changes.

**Status: reconciled against the finished docs in the July 2026 validation pass.** All former "verify" rows were resolved by the research sessions; resolutions are recorded in the Notes column. New products that landed during research (June 2026 wave) have been added.

Legend: **P** = primary coverage, **s** = secondary/cross-reference.

| Product / module (current name) | Former names | 01 API | 02 WAF | 03 BOT | 04 DDOS | 05 ADC | 06 DNS | 07 ZTA | 08 SSLO | 09 MCN | 10 K8S | 11 AI | 12 SP | 13 OBS | 14 PLAT | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XC API Security | (Wib capabilities, absorbed) | P | s | | | | | | | | | s | | | | |
| F5 API Security Local Edition | (predecessor: "local API discovery" EA, Dec 2025) | P | | | | | | | | | | | | | | NEW product, GA Jun 9 2026; on-prem/air-gapped; BIG-IP Advanced WAF enforcement |
| XC WAF / WAAP | | s | P | | | | | | | | | s | | | | AI risk scoring GA in XC (announced Mar 2026, expanded Jun 2026); BIG-IP/NGINX = roadmap |
| XC Web App Scanning | (Heyhack, acq. Feb 2024) | s | P | | | | | | | | | | | | | Name confirmed current (doc 02) |
| XC Bot Defense | Shape | s | | P | | | | | | | | s | | | | Human/bot/AI-agent classification (Mar 2026); Skyfire KYA integration |
| XC Account Protection | Shape AI Fraud Engine (SAFE) | | | P | | | | | | | | | | | | Resolved: **Limited Availability, not GA** (docs Jul 2026); product page removed in site consolidation |
| XC Authentication Intelligence | | | | P | | | | | | | | | | | | Resolved: flagged "(Legacy)", apparently sunset — do not lead new deals; no formal EoS notice found |
| XC Data Intelligence | | | | P | | | | | | | | | | | | Added: current fraud-telemetry SKU (doc 03) |
| XC Aggregator Management | | | | P | | | | | | | | | | | | Added: open-banking managed service (doc 03) |
| XC Client-Side Defense | | | | P | | | | | | | | | | | | PCI DSS 4.0.1 driver (6.4.3 / 11.6.1) |
| XC DDoS Mitigation | Silverline DDoS (retired, EoL 30 Jun 2025) | | | | P | | | | | | | | s | | | |
| BIG-IP DDoS Hybrid Defender (DHD) | Herculon lineage | | | | P | | | | | | | | | | | Added: still marketed mid-2026; packaging / post-Silverline cloud-signaling = verify (doc 04) |
| XC App Delivery / LB (App Connect LB) | | | | | | P | s | | | s | s | | | | | |
| XC DNS / DNS Load Balancer | | | | | | | P | | | | | | s | | | Two distinct SaaS products — don't conflate |
| XC Network Connect | | | | | | | | | | P | | | | | | |
| XC App Connect | | | | | | | | | | P | | | | | | |
| XC App Stack | | | | | | | | | | s | s | | | | s | Resolved: live but de-emphasized in 2026 packaging; deliberately covered as CE substrate only (doc 09) — no P is intentional |
| XC Customer Edge (CE) | Volterra heritage | | | | | | | | | P | | | | | s | |
| XC Synthetic Monitoring | | | | | | | | | | | | | | P | | Added: part of XC Observability (doc 13) |
| BIG-IP LTM | | | | | | P | | | | | | | | | s | |
| BIG-IP DNS | GTM | | | | | | P | | | | | | s | | | |
| BIG-IP Advanced WAF | ASM (EoS Apr 2021) | P | P | s | | | | | | | | | | | | |
| BIG-IP Zero Trust Access | APM (renamed Mar 2026, branding-only) | s | | | | | | P | s | | | | | | | "APM" persists in techdocs/SKUs |
| BIG-IP AFM (incl. CGNAT features) | | | | | P | | | | | | | | P | | | AFM as general network firewall = documented coverage gap (see below) |
| BIG-IP Policy Enforcement Manager (PEM) | | | | | | | | | | | | | P | | | Resolved: cloud-native equivalent = Policy Enforcer CNF (Gx integration in CNF 2.3) |
| F5 SSL Orchestrator (SSLO) | | | | | | | | | P | | | | | | | SSLO v14 ships with BIG-IP v21.1 |
| BIG-IP Next (TMOS-successor ADC line) | | | s | | | s | | s | s | | | | s | | P | Resolved: **DISCONTINUED** (K000152956); final v20.3 EoL Apr 30 2025; go-forward is TMOS v21.x. BNK/CNFs are separate and continue (rows below) |
| BIG-IP Next CNFs (Edge FW, CGNAT, DNS, Policy Enforcer, DAG) | | | | | | | s | | | | | | P | | | Active line: CNF 2.0 GA May 2025; CNF 2.3 early 2026 |
| BIG-IP Next for Kubernetes | BIG-IP Next SPK (renamed at 2.0.0-GA) | | | | | | | | | | P | P | P | | | Resolved name/scope: telco/5G angle = doc 12; enterprise K8s = doc 10; DPU/AI-factory = doc 11 (2.0.0-GA is BlueField-3-only) |
| NGINX Plus / NGINX One | | s | | | | P | | | | | P | s | | s | P | NGINX One GA Sep 17 2024 |
| NGINX Open Source | | | | | | s | | | | | s | s | | | P | MCP traffic visibility GA in OSS (Mar 2026) |
| F5 WAF for NGINX | NGINX App Protect WAF (renamed ~mid-2025, v5.9) | P | P | s | | | | | | | s | | | | | |
| F5 DoS for NGINX | NGINX App Protect DoS (renamed Sep 2025) | | | | P | | | | | | s | | | | | Resolved: current name confirmed (doc 04) |
| NGINX Gateway Fabric (NGF) | | | | | | | | | | | P | s | | | | NGF 2.6.6 (Jun 2026); Gateway API v1.5.1 |
| NGINX Ingress Controller (NIC) | | | | | | | | | | | P | | | | | Resolved precisely: community `ingress-nginx` retired Mar 2026 (NOT the F5 product); NIC actively maintained |
| BIG-IP Container Ingress Services (CIS) | | | | | | | | | | | P | | | | | |
| F5 IngressLink (BIG-IP + NIC integration) | | | | | | | | | | | P | | | | | Added: two-tier CIS/NIC integration (doc 10) |
| NGINXaaS for Azure | | | | | | P | | | | | s | | | | s | Resolved: GA, actively developed (NGINX Plus R36, 2026); NGINXaaS for Google Cloud = verify per deal |
| F5 AI Gateway | | s | | | | | | | | | | P | | | | GA ~Feb 2025; relationship to AI Security Platform umbrella = unverified (doc 11) |
| F5 AI Red Team | CalypsoAI (acq. completed ~Sep 2025) | | | | | | | | | | | P | | | | GA Jan 14 2026 |
| F5 AI Guardrails | CalypsoAI | | | | | | | | | | | P | | | | Resolved: product name confirmed; GA Jan 14 2026 |
| F5 AI Remediate | | | | | | | | | | | | P | | | | Announced Mar 11 2026; standalone GA date unconfirmed (doc 11) |
| F5 AI Security Platform (umbrella) + SurePath AI discovery | SurePath AI (acq. announced Jun 22 2026) | | | | | | | | | | | P | | | | Added: launched Jun 22 2026; SurePath post-integration naming/GA = unsettled; pre-acq SaaS/site live under F5 banner — doc 11 carries discovery + workforce-governance records (Jul 2026) |
| F5 Insight for ADSP | (Threat Stack + Fletch heritage; AST community predecessor) | | | | | | | | | | | s | | P | s | GA for BIG-IP Mar 2026; self-managed only (SaaS forthcoming); NGINX/XC coverage = roadmap; v1.2 Jul 2026 |
| Platform AI assistants (BIG-IP/NGINX/XC) | | | | | | s | | | | | | s | | P | | iRules code generation GA Jul 2025 |
| BIG-IP Telemetry Streaming (TS) | | | | | | | | | | | | | | P | | Added: the "keep your Datadog/Splunk" coexistence answer (doc 13) |
| BIG-IQ | | | | | | | | | | | | | | s | P | Resolved: current (8.4.x), complementary to Insight — NOT superseded |
| NGINX One Console | Instance Manager capabilities; supersedes Amplify (EoL 31 Jan 2026) | | | | | | | | | | s | | | s | P | |
| rSeries / VELOS / F5OS | | | | | s | s | | | | | | | s | | P | |
| iSeries / VIPRION (legacy) | | | | | | s | | | | | | | | | P | EoS/EoSS dates in doc 14 milestone table = refresh triggers |
| BIG-IP Virtual Edition | | | | | | s | | | | | | | | | P | |
| XC packaging tiers: Essentials / Enterprise (Mar 2026) | dozens of per-service SKUs | s | s | s | s | | | | | s | | | | | P | Tier names captured in doc 14; per-tier feature matrix not fully public |

## Known retired/absorbed (document as historical aliases only — customers still say these names)
| Retired name | Fate | Where noted |
|---|---|---|
| Silverline (managed services incl. DDoS/WAF) | EoL 30 Jun 2025; migrated to Distributed Cloud | docs 02, 04 |
| Shape Security | Became XC Bot Defense / Account Protection | doc 03 |
| Threat Stack / Distributed Cloud AIP | AIP retired Aug 13, 2024; tech resurfaced in F5 Insight / AI Data Fabric | doc 13 |
| Wib | Folded into XC API Security; name gone from F5 materials | doc 01 |
| Heyhack | Became XC Web App Scanning (Mar 2024) | doc 02 |
| CalypsoAI | Became F5 AI Red Team / AI Guardrails | doc 11 |
| LeakSignal | Tech in AI Gateway data-leak detection/redaction | doc 11 |
| SurePath AI | Acquired Jun 2026 → AI-discovery & workforce-governance pillar of F5 AI Security Platform (pre-acq SaaS/site still live under F5 banner) | doc 11 |
| Fletch | Tech in F5 Insight / AI Data Fabric | doc 13 |
| NGINX App Protect WAF | Renamed F5 WAF for NGINX | docs 01, 02 |
| NGINX App Protect DoS | Renamed F5 DoS for NGINX (Sep 2025) | doc 04 |
| NGINX Amplify | Retires Jan 31, 2026; superseded by NGINX One Console | doc 14 |
| APM | Renamed BIG-IP Zero Trust Access (Mar 2026; branding-only) | doc 07 |
| GTM | Renamed BIG-IP DNS | doc 06 |
| BIG-IP Next (ADC software line) | Discontinued (K000152956); final v20.3 EoL Apr 30, 2025; folded into TMOS modernization. BNK/CNFs continue | docs 02, 05, 14 |
| Traffix SDC (Diameter/SIP signaling) | Resolved: legacy/wind-down — "End of Support extension" KB exists (K000133773) but exact EoS dates are not public; installed-base only, do not sell net-new | doc 12 |
| Aspen Mesh (Carrier-Grade) | Status uncertain: historically GA alongside SPK; current investment level not documented in recent public sources — verify before quoting | doc 12 |

## Documented coverage gaps (per the audit rule)
| Gap | Status / reason | Recorded |
|---|---|---|
| **XC CDN** | GA product (bundled in Essentials/Enterprise; referenced in docs 09/14) but has **no primary doc**. Rationale: CDN is rarely the lead pain for an SE-qualification agent; decide at next refresh whether to add it to doc 05's scope or accept the exclusion permanently. | Jul 2026 validation |
| **BIG-IP AFM as a general network firewall** | Doc 04 covers AFM's DoS/DDoS features only, and doc 12 its SP consolidation role; the enterprise network-firewall use case has no doc. If firewall-led deals appear in transcripts, consider a 15th solution area or extend doc 04's scope. | Jul 2026 validation |
| **F5 AI Data Fabric** | Deliberately not a matrix row: internal platform/substrate, not a sellable SKU (doc 13). | Jul 2026 validation |

## Audit rule
A product with no **P** anywhere is a coverage gap: either add it to an existing doc's scope, create a new solution area, or record it in the "Documented coverage gaps" table above with date and reason. (XC App Stack's no-P status is an intentional, recorded exception — substrate only.)
