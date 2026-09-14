# 40-f5-corpus-index.md — Entry point to the F5 solution corpus (sanitized)

Derived from `agents.md` Part A. Internal SharePoint routing and the Gemini paste-ready block are deliberately omitted: this file is safe to place in any Project or repository. The original `agents.md` must not be uploaded because Part B embeds live internal URLs with user-identifying parameters.

**How the visibility agent uses this corpus**
- Solution areas = test-panel categories (docs 01–13). Doc 14 is a lookup reference; do not panel it.
- `fit_signals` fields in each `### [TAG]` record are the raw material for open-ended prompts. Strip every F5 product and brand name before use; keep the customer's phrasing.
- Layer 3c of each doc is the competitor set for that category. Use names only; the corpus marks 3c as lower confidence for positioning claims, which the visibility agent does not need.
- `41-coverage-matrix.md` "Former names" and "Known retired/absorbed" tables are the alias source for mention scoring (see `12-alias-table.md`).
- Record the corpus `compiled` / `last_validated` date on every panel and report. A corpus refresh triggers panel regeneration.

## Part A — Corpus documentation

### Purpose

The consuming agent reads a sales-call transcript or detailed meeting notes and helps an F5 Sales Engineer by: (1) judging which F5 solution areas fit the customer's stated pains, (2) routing to the right F5 product(s) given the customer's existing footprint, and (3) drafting pitch angles, objection handling, and follow-up discovery questions — with honest "weak fit" and "not yet" verdicts when warranted.

### Corpus map

Documents live in `docs/`. Every capability record is self-contained: it begins with a `### [TAG]` heading and restates its solution area and products, so retrieved chunks identify themselves.

| Doc | Solution area | Tag | Lead pain signals (abbreviated) | Products |
|---|---|---|---|---|
| 01-api-security.md | API Security | API-SEC | Unknown/shadow APIs, API breach or leak worry, OWASP API Top 10, spec enforcement, API compliance, air-gapped/sovereign API security | XC API Security, F5 API Security Local Edition (on-prem/air-gapped, new Jun 2026), BIG-IP Advanced WAF, F5 WAF for NGINX, NGINX Plus |
| 02-web-app-protection.md | Web App Protection (WAAP) | WAF | Web attacks, OWASP Top 10, WAF tuning fatigue, virtual patching, scanner findings, AI risk scoring interest | XC WAF, BIG-IP Advanced WAF, F5 WAF for NGINX, XC Web App Scanning |
| 03-bot-defense-fraud.md | Bot Defense & Online Fraud | BOT | Credential stuffing, ATO, scraping, carding, fake accounts, Magecart/PCI 4.0 client-side, AI-agent traffic, agentic commerce | XC Bot Defense, Client-Side Defense, Data Intelligence, Aggregator Management, Account Protection (Limited Availability) |
| 04-ddos-protection.md | DDoS Protection | DDOS | Attacks/outages, extortion threats, ISP mitigation gaps, L7 floods | XC DDoS, BIG-IP AFM, DDoS Hybrid Defender, F5 DoS for NGINX (formerly NGINX App Protect DoS) |
| 05-app-delivery-load-balancing.md | App Delivery & Load Balancing | ADC | NetScaler/Avi displacement, hardware EOL/refresh, availability incidents, TLS/PQC, iRules estate | BIG-IP LTM (TMOS v21.x — NOT BIG-IP Next), NGINX Plus/One, NGINXaaS for Azure, XC App Connect/LB |
| 06-dns-global-traffic.md | DNS & Global Traffic (GSLB) | DNS | DR/failover pain, multi-DC or hybrid steering, DNS outage/attack, DNSSEC | BIG-IP DNS (formerly GTM), XC DNS, XC DNS Load Balancer |
| 07-access-zero-trust.md | Access & Zero Trust | ZTA | VPN replacement, VPN CVE fatigue, legacy-app SSO/identity bridging, VDI, per-app access | BIG-IP Zero Trust Access (formerly APM; rename is branding-only) |
| 08-encrypted-traffic-crypto.md | Encrypted Traffic Inspection & Crypto | SSLO | Blind to encrypted traffic, per-tool decryption sprawl, PQC / harvest-now-decrypt-later | SSL Orchestrator, BIG-IP PQC ciphers, NGINX PQC |
| 09-multicloud-networking.md | Multicloud Networking | MCN | Transit-gateway sprawl, M&A network integration, IP overlap, app connectivity across clouds | XC Network Connect, App Connect, Customer Edge (CE) |
| 10-kubernetes-modern-apps.md | Kubernetes & Modern Apps | K8S | ingress-nginx retirement (community project, Mar 2026), Gateway API migration, OpenShift, exposing k8s via BIG-IP | NGINX Gateway Fabric, NGINX Ingress Controller, CIS, IngressLink, BIG-IP Next for Kubernetes (enterprise angle) |
| 11-ai-delivery-security.md | AI Delivery & Security | AI | LLM app security, prompt injection, AI red-teaming, shadow AI agents/MCP, workforce GenAI governance, GPU/AI factory buildout | AI Security Platform (umbrella, Jun 2026), AI Gateway, AI Red Team, AI Guardrails, AI Remediate, SurePath AI (discovery + workforce governance), BIG-IP Next for K8s (DPU), NGINX MCP visibility |
| 12-service-provider.md | Service Provider & Telco | SP | CGNAT/IPv4 exhaustion, Gi-LAN/N6 consolidation, 5G core CNFs, subscriber policy | CGNAT, PEM, BIG-IP Next CNFs, SPK / BIG-IP Next for Kubernetes (telco angle) |
| 13-observability-insight.md | Observability & Insight | OBS | Visibility gaps across F5 estate, troubleshooting blame-wars, consolidation visibility fears | F5 Insight for ADSP, platform AI assistants, XC Synthetic Monitoring, NGINX One Console, Telemetry Streaming |
| 14-delivery-vehicles-reference.md | Platform Reference | PLAT | Mentions of hardware/platforms/packaging (VIPRION, iSeries, rSeries, VELOS, TMOS, NGINX One, XC tiers) — lookup, not a pitch | Hardware, F5OS, TMOS/BIG-IP Next lifecycle, BIG-IQ, NGINX One, XC packaging (Essentials/Enterprise), FCP |

`41-coverage-matrix.md` maps every GA F5 product to the docs that cover it — use it to answer "where is product X documented?" It also records documented coverage gaps (e.g., XC CDN, AFM as a general firewall).

### Portfolio facts the agent must not get wrong (highest-risk, validated July 2026)

- **BIG-IP Next (the TMOS-successor ADC software line) is DISCONTINUED** (final v20.3 EoL April 30, 2025). Never recommend migrating to it; the go-forward is modernized BIG-IP TMOS v21.x on rSeries/VELOS. **BIG-IP Next for Kubernetes and BIG-IP Next CNFs are separate, active products** — do not conflate.
- **Silverline is retired** (EoL June 30, 2025) → route to Distributed Cloud.
- The retired **community `ingress-nginx`** project (March 2026) is **not** F5's NGINX Ingress Controller — the F5 product is actively maintained. Keep the two straight.
- **APM → BIG-IP Zero Trust Access** (March 2026) is a branding-only rename; "APM" persists in techdocs/SKUs.
- **XC Universal ZTNA is pre–Early Access** — not sellable; F5's shipping access product is the BIG-IP module.

### Procedure for the consuming agent

1. **Extract signals** from the transcript: pains, incidents, compliance drivers, architecture patterns, named vendors/products, existing F5 footprint, buyer roles, and explicit asks.
2. **Map signals to solution areas** using the table above and each doc's `fit_signals` fields. Multiple areas per call is normal; rank them by signal strength.
3. **Check disqualifiers first.** Every doc has per-capability `disqualifiers` and an aggregate anti-pattern section (Layer 3b). If disqualifiers dominate, say "weak fit" or "not now" with the reasons — this is a valid, valuable output.
4. **Route the product** using the matched doc's Layer 3a, keyed on the customer's footprint (existing BIG-IP/NGINX/XC or greenfield), delivery preference (SaaS vs self-managed vs on-prem vs air-gapped), and buyer persona. Platform/hardware mentions get interpreted via doc 14.
5. **Build the pitch** from `value_framing` and `customer_problem_solved` fields, in the customer's own language from the transcript. Use Layer 3c for objections and competitors — always with its confidence caveats.
6. **Suggest discovery questions** for signals that were ambiguous — what the SE should ask next to confirm or kill the fit.

### Non-negotiable confidence rules

- Never upgrade a record's `attribution_confidence` or `source_currency_flag`. If a record says Medium/Low or Possibly stale/Unverified, the output to the SE must carry that caveat (e.g., "verify current support before asserting on the call").
- Never invent capabilities, packaging, pricing, or official F5 routing guidance not present in the corpus. "The knowledge base doesn't establish that — flag for F5 competitive/product enablement" is the correct answer.
- Competitive claims are always presented as F5's stated positioning or public consensus, never as verified head-to-head wins.
- Product names are perishable. When a doc lists former names, use the current name and note the alias (SEs and customers use old names constantly — match on both, output the current one).
- These documents are compiled from public sources on a stated date (Layer 0 `compiled` field). For anything after that date, say so.
