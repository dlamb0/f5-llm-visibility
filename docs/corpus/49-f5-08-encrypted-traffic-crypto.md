# F5 Encrypted Traffic Inspection & Cryptographic Modernization — Solution Area Reference (Doc 08)
doc_id: 08-encrypted-traffic-crypto
solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
doc_tag: SSLO
products_covered: F5 BIG-IP SSL Orchestrator (SSLO), BIG-IP Next SSL Orchestrator (discontinued platform — noted for the record only), BIG-IP (LTM/TMM PQC ciphers), BIG-IP Zero Trust Access (formerly APM — referenced only), F5 NGINX Plus, F5 Application Delivery and Security Platform (ADSP), F5 Distributed Cloud (XC — referenced only)
compiled: July 2026
primary_release_anchor: BIG-IP v21.1 GA (June 2026, announced June 4, 2026), including SSL Orchestrator v14 and two new NIST-compliant hybrid PQC cipher groups; F5 AppWorld 2026 (March 2026) security announcements
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

This document covers two related but distinct stories that both live at the TLS termination point in F5's portfolio:

1. **Encrypted traffic inspection** — F5 **BIG-IP SSL Orchestrator (SSLO)**. SSLO is a full-proxy that decrypts SSL/TLS **once**, dynamically steers the cleartext through the customer's existing security stack (NGFW, IPS/IDS, DLP, anti-malware, sandbox) via **dynamic service chaining**, then re-encrypts. Its value is orchestration and centralization, not just decryption: it replaces brittle "daisy-chained" inline devices and removes the need for every tool to do its own decryption.

2. **Cryptographic modernization / post-quantum readiness** — F5 positions the proxy (BIG-IP, and separately NGINX) as the place to adopt **hybrid post-quantum cryptography (PQC)** without rearchitecting applications. This is a crypto-agility story driven by "harvest now, decrypt later" and regulatory timelines (NIST, CNSA 2.0).

**How the products differ in delivery model:**
- **BIG-IP SSL Orchestrator** — delivered as a **standalone licensed BIG-IP** (SSLO base license) **or** as an **add-on to BIG-IP LTM** (LTM + SSL Forward Proxy add-on). Runs on BIG-IP hardware (iSeries, rSeries/VELOS) and Virtual Edition (VMware, KVM, Hyper-V, AWS, Azure, GCP). Configured via "Guided Configuration."
- **BIG-IP Next SSL Orchestrator** — an SSLO module existed on the BIG-IP Next platform (Limited Availability / evaluation only), but **the BIG-IP Next software line was discontinued** (per K000152956; final version 20.3 reached end of life April 30, 2025 — see sibling docs 05/14). Do not position it; classic BIG-IP SSLO on TMOS is the product.
- **PQC ciphers** — a BIG-IP TMOS/TMM feature (also in LTM), most recently expanded in **BIG-IP v21.1**. **NGINX** has a separate, independently-versioned PQC story.

**How to read the rest:** Layer 2 is the capability catalog (retrievable records). Layer 3 gives routing logic, honest disqualifiers, and bounded competitive/objection handling. The appendix tracks perishable naming and explicitly-unverified items. **Attribution caution:** SSLO and PQC are separate stories — do not tell an SE that "SSL Orchestrator does PQC" as if they are one feature. SSLO benefits from BIG-IP's cipher support (including hybrid PQC), but PQC cipher groups are a BIG-IP platform capability, not an SSLO-exclusive feature.

---

## Layer 2 — Capability catalog

### [SSLO] Decrypt-once centralized SSL/TLS inspection
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Decrypt-once centralized SSL/TLS decryption and re-encryption (full-proxy)
- plain_description: A single device decrypts encrypted traffic one time, hands the cleartext to the security tools that need it, then re-encrypts before sending it on — instead of every security appliance decrypting the same traffic independently.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on). (A BIG-IP Next SSLO module existed but the BIG-IP Next platform is discontinued — do not position it.)
- attribution_confidence: High
- customer_problem_solved: The web is now almost entirely encrypted — per Google's Transparency Report (Oct 2025), HTTPS on Android surpassed 99% and Chrome desktop has sat at 93–96% since April 2018, and W3Techs (Jan 2026) reports 92.6% of the top 100,000 websites use HTTPS by default — and a large share of malware hides inside that encryption (WatchGuard's Q1 2025 Internet Security Report found 71% of malware now arrives over encrypted connections). Each security tool decrypting the same traffic separately is slow, costly, and duplicative, and many tools decrypt poorly or not at all.
- fit_signals: "We're blind to encrypted traffic." "Every security tool decrypts its own traffic and they're all falling over." "Our firewall's throughput tanks when we turn on decryption." "We have a decryption blind spot on outbound traffic." Buyers describe CPU/throughput problems on NGFW/IPS when SSL inspection is enabled; note that the vast majority of their traffic is now TLS; worry about malware/C2/exfiltration hidden in HTTPS.
- disqualifiers: Fully cloud-native/SaaS shops with no on-prem inspection stack to feed; organizations that have standardized on a cloud SASE/SSE provider (Zscaler, Prisma Access) for decryption; environments where a single NGFW comfortably handles decryption at current scale.
- value_framing: "Decrypt once, inspect with everything, re-encrypt — offload the crypto burden from your security tools so they run faster and last longer, and stop paying for decryption capacity on every box."
- product_routing_note: Lead with BIG-IP SSL Orchestrator (GA, on classic BIG-IP TMOS). If a customer mentions BIG-IP Next SSL Orchestrator, correct the record: the BIG-IP Next platform was discontinued (final v20.3 EoL April 30, 2025); the go-forward is SSLO on classic BIG-IP.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/ssl-orchestrator; techdocs.f5.com SSLO release notes 21.1.0-14.0; DevCentral "Introduction to BIG-IP SSL Orchestrator"; Google Transparency Report (Oct 2025); WatchGuard Q1 2025 Internet Security Report; W3Techs (Jan 2026)

### [SSLO] Dynamic service chaining
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Dynamic, policy-based security service chaining
- plain_description: Instead of hard-wiring security devices in a fixed line ("daisy chain"), SSLO sends decrypted traffic to independently-addressable security services in logical chains that vary by traffic type, and load-balances/health-monitors each service.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on)
- attribution_confidence: High
- customer_problem_solved: Manually chained inline devices are fragile — adding, removing, or scaling a tool means re-architecting the wire; a single failed device can break the whole chain; you can't send different traffic to different tools.
- fit_signals: "Adding a new security tool means re-cabling and a change window." "If one IPS goes down the whole path goes down." "We can't scale our DLP independently of our firewall." "We want to send guest traffic through fewer tools than employee traffic." Descriptions of inline devices bumped in series; complaints about maintenance windows to insert tools; desire to load-balance across multiple identical appliances.
- disqualifiers: Single-tool environments (just one NGFW) with no plans to add inspection tools; organizations with no appetite to route decrypted traffic through third-party tools.
- value_framing: "Insert, remove, scale, and bypass security tools with policy — not cabling. Chain the right tools to the right traffic, and keep inspecting even when a device fails."
- product_routing_note: SSLO only. This is SSLO's signature differentiator vs. plain decryption appliances.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/ssl-orchestrator; clouddocs.f5.com SSLO deployment guide (service chaining vs. daisy chaining); SSLO release notes 21.1.0-14.0 (up to 50 devices per L2 inspection service)

### [SSLO] Context-based traffic steering and selective decryption/bypass
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Context engine for traffic classification, steering, and decryption bypass
- plain_description: A policy engine decides what to decrypt, what to bypass, and which service chain to use, based on URL category, IP reputation, geolocation, and flow context — e.g., bypassing decryption of banking/healthcare traffic for privacy/compliance.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on)
- attribution_confidence: High
- customer_problem_solved: Blanket decryption creates privacy/legal exposure (decrypting employee banking/health sessions) and wastes inspection capacity; organizations need to decrypt selectively while still enforcing policy.
- fit_signals: "We can't decrypt banking or healthcare traffic for privacy reasons." "We need to bypass certain categories but inspect everything else." "Compliance requires we prove we don't intercept sensitive personal sessions." Mentions of GDPR/HIPAA/PCI constraints on decryption; need to steer by user group or destination category.
- disqualifiers: Environments that decrypt everything with no bypass requirements; very small deployments where per-category policy is overkill.
- value_framing: "Decrypt what you must, bypass what you shouldn't touch — with policy driven by URL category, IP reputation, and geolocation, so you stay compliant and efficient."
- product_routing_note: SSLO only. Context engine leverages F5 URL categorization / IP Intelligence subscriptions.
- maturity_flag: GA
- source_currency_flag: Current
- source: Trellix/F5 SSLO joint solution guide; clouddocs.f5.com SSLO deployment guide

### [SSLO] Full-proxy TLS 1.3 interception (inbound and outbound)
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: TLS 1.3 full-proxy interception for forward and reverse proxy
- plain_description: SSLO terminates and re-originates TLS as a true full proxy, supporting TLS 1.3 on client side, server side, or both, for both outbound (forward proxy, certificate forging) and inbound (reverse proxy) flows.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on)
- attribution_confidence: High
- customer_problem_solved: TLS 1.3 — which now accounts for roughly 90% of TLS connections per Cloudflare, with TLS 1.2 (~10%) in decline — mandates perfect forward secrecy, which breaks passive/tap-based decryption that relied on static keys; inspecting modern encrypted traffic requires an inline full proxy.
- fit_signals: "Our passive decryption tap stopped working when sites moved to TLS 1.3." "We need forward secrecy but still need to inspect." "We're moving to TLS 1.3 everywhere and losing visibility." Mentions of PFS, ephemeral keys, tap/mirror inspection breaking.
- disqualifiers: Organizations relying solely on passive/out-of-band inspection who will not deploy an inline proxy; environments where clients cannot be made to trust an internal CA (required for outbound forward-proxy interception).
- value_framing: "TLS 1.3 killed passive decryption; SSLO's full proxy terminates and re-encrypts TLS 1.3 inline, so you keep both forward secrecy and visibility."
- product_routing_note: SSLO for orchestration; note that BIG-IP LTM alone is also a TLS 1.3 full proxy but without service chaining. TLS 1.3 outbound (forward proxy) arrived in SSLO 7.1/7.2; inbound in SSLO 6.0.
- maturity_flag: GA
- source_currency_flag: Current
- source: clouddocs.f5.com SSLO deployment guide §4.4 "Managing Cryptography"; clouddocs.f5.com "What's new in SSL Orchestrator 7"; Cloudflare (TLS version distribution)

### [SSLO] Encrypted Client Hello (ECH) handling — UNVERIFIED for SSLO
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: TLS 1.3 Encrypted Client Hello (ECH) inspection behavior
- plain_description: ECH (RFC 9849, finalized March 2026) encrypts the SNI in the ClientHello, blinding any inspection that relies on reading SNI. How SSLO specifically handles ECH is not documented by F5 in public sources.
- delivered_by: Unverified for F5 BIG-IP SSL Orchestrator. NGINX Plus (37.0) supports ECH as a TLS server feature (different product, not an inspection capability).
- attribution_confidence: Low
- customer_problem_solved: (Potential) preserving inspection/policy when clients adopt ECH and SNI is no longer visible in cleartext.
- fit_signals: "We're worried ECH will blind our SNI-based filtering." "Chrome/Firefox are turning on ECH — what happens to our inspection?" "Our SNI-based category bypass rules may break."
- disqualifiers: Organizations not yet seeing ECH; environments where all inspected clients are managed and trust the internal CA (inline MITM proxies decrypt content regardless of ECH, though SNI-based bypass policy can still be affected).
- value_framing: Do NOT assert an F5 ECH story. Analytically: an inline full proxy that terminates the client TLS session (client trusts SSLO's CA) can still inspect decrypted content even with ECH, but SSLO's SNI-based bypass/steering decisions could be degraded unless ECH is stripped/downgraded. F5 has published no guidance confirming this for SSLO.
- product_routing_note: If asked, be honest: "F5 has not published SSLO-specific ECH guidance as of mid-2026." Contrast: Cisco Secure Firewall and Fortinet FortiGate have published explicit ECH-handling (strip/block) controls; F5 SSLO has no equivalent public doc. Flag this to the SE as an open question, not a proven gap or a proven capability.
- maturity_flag: Unknown
- source_currency_flag: Unverified
- source: RFC 9849 (TLS Encrypted Client Hello, March 2026); targeted F5-source research found no F5 SSLO/BIG-IP ECH documentation; DevCentral "F5 NGINX Plus 37.0 release" (ECH is an NGINX server feature)

### [SSLO] Flexible topologies and inspection device types
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Multiple deployment topologies and inspection service types
- plain_description: SSLO supports transparent and explicit forward proxy, reverse proxy (inbound gateway), Layer 2 "bump-in-the-wire," and Layer 3 routed topologies, and can steer to Layer 2/Layer 3 inline devices, HTTP proxies, ICAP servers (DLP), and receive-only TAP devices.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on)
- attribution_confidence: High
- customer_problem_solved: Existing security tools sit at different network layers and can't be moved; SSLO must integrate into whatever architecture already exists without re-architecting the network. As F5's own architecture guide notes, "SSLO is almost never first in an enterprise architecture" — the other security devices are already there.
- fit_signals: "Our IPS is a layer 2 device, our DLP uses ICAP, and we have a passive forensics tap — we need all of them fed." "We can't move our existing security devices." Descriptions of a heterogeneous, already-installed tool set.
- disqualifiers: Greenfield with a single inspection tool and no topology constraints; pure cloud-native environments.
- value_framing: "Integrate SSLO into your existing architecture — L2, L3, explicit/transparent proxy, ICAP, TAP — without ripping out or re-cabling the security tools you already own."
- product_routing_note: SSLO only. F5 tested up to 8 devices per service historically; SSLO v14 raises L2 inspection service scale to 50 devices.
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com "What is F5 SSL Orchestrator"; SSLO Architecture Guide; SSLO release notes 21.1.0-14.0

### [SSLO] Inbound (reverse proxy) inspection and security-tool offload
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Inbound decryption and inspection for published applications
- plain_description: For traffic coming from the internet to the organization's own applications, SSLO decrypts inbound TLS, steers it through inspection tools (e.g., IPS/WAF), and re-encrypts — protecting published apps from inbound threats hidden in encryption.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on)
- attribution_confidence: High
- customer_problem_solved: Inbound ransomware/malware and exploits can hide in encrypted requests to public-facing apps; inspection tools need cleartext at the edge.
- fit_signals: "We need to inspect inbound traffic to our banking/e-commerce app for hidden threats." "Web shells on our servers used our own TLS keys and we never saw the traffic." Mentions of reverse-proxy inspection, inbound IPS, protecting published applications.
- disqualifiers: Organizations whose inbound apps are entirely behind a cloud WAF/CDN that already decrypts and inspects; no on-prem inbound inspection tools.
- value_framing: "Expose inbound threats hiding in encryption before they reach your apps, and offload inbound decryption from your IPS/WAF."
- product_routing_note: SSLO for orchestration/steering. Scope boundary: pure TLS offload for app performance belongs to LTM (sibling doc 05), not here.
- maturity_flag: GA
- source_currency_flag: Current
- source: DevCentral "Introduction to BIG-IP SSL Orchestrator" (inbound/outbound topologies); f5.com SSLO product page

### [SSLO] Encrypted-threat, DLP, and Shadow AI visibility use cases
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Use-case coverage — ransomware, data exfiltration, DLP, Shadow AI/GenAI visibility
- plain_description: By exposing decrypted traffic to inspection tools, SSLO supports outbound data-exfiltration and ransomware defense, DLP enforcement (via ICAP), and (per F5's stated roadmap/announcements) detection and control of unsanctioned GenAI/Shadow AI use in encrypted flows.
- delivered_by: F5 BIG-IP SSL Orchestrator (standalone or LTM add-on); DLP/NGFW/sandbox are third-party partners, not F5 products
- attribution_confidence: Medium
- customer_problem_solved: Sensitive data and malware move over encrypted channels and through unsanctioned AI tools, creating blind spots that traditional controls miss.
- fit_signals: "We can't see what data is going to ChatGPT/GenAI tools." "We need DLP on encrypted outbound traffic." "Ransomware and exfiltration to drop zones are hiding in HTTPS." Mentions of Shadow AI governance, encrypted DLP, C2 detection.
- disqualifiers: Organizations enforcing AI/DLP policy entirely at a cloud SSE/CASB layer; no on-prem DLP tooling.
- value_framing: "Turn encrypted blind spots into enforcement points — feed DLP, anti-malware, and AI-governance tools the cleartext they need."
- product_routing_note: SSLO delivers the visibility/steering; the DLP/AI classification may be a partner tool or F5's own emerging AI data-protection features. F5's SSLO Shadow-AI/AI-data-protection capability was announced (July 2025) with planned availability in late 2025 — verify GA status before positioning as shipping.
- maturity_flag: GA (core inspection) / Roadmap-to-GA (AI data protection specifics — verify)
- source_currency_flag: Possibly stale
- source: f5.com SSLO product page (Shadow AI, ransomware sections); F5 press release (July 2025) "Data Leakage Detection and Prevention" (planned availability late 2025)

### [SSLO] Hybrid post-quantum cryptography (PQC) ciphers on BIG-IP
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: NIST-compliant hybrid PQC cipher support (BIG-IP)
- plain_description: BIG-IP supports hybrid TLS key exchange combining classical and quantum-resistant algorithms, so the proxy can negotiate quantum-safe key exchange with clients/servers while staying compatible with existing crypto.
- delivered_by: F5 BIG-IP (TMOS/TMM; BIG-IP LTM); enabled at the proxy for client-side, server-side, and SSL Forward Proxy use cases
- attribution_confidence: High
- customer_problem_solved: "Harvest now, decrypt later" — adversaries capture encrypted data today to decrypt once quantum computers mature; long-lived sensitive data must be protected now.
- fit_signals: "We have data that must stay confidential for 10+ years." "Our regulator/CNSA 2.0/NIST timeline requires PQC planning." "We can't rewrite our apps to add PQC." Government, defense, finance, healthcare buyers; mentions of Q-Day, harvest-now-decrypt-later, FIPS 203/ML-KEM.
- disqualifiers: Organizations with no long-confidentiality data and no regulatory PQC driver; teams whose endpoints/clients don't yet support PQC ciphers (though the proxy can still be readied first).
- value_framing: "Enable quantum-safe key exchange at the proxy without rearchitecting your apps — this is F5's stated claim: hybrid PQC is implemented in the platform (ADSP/BIG-IP), so legacy and modern apps get quantum-ready protection at the termination point."
- product_routing_note: BIG-IP (LTM/TMM) carries this; SSLO benefits from BIG-IP cipher support but PQC is not an SSLO-exclusive feature. BIG-IP Zero Trust Access (formerly APM) separately adds quantum-resistant VPN tunneling (sibling doc 07 — do not cover in depth). Timeline: first hybrid key exchange (X25519_ML-KEM-768) in v17.5.0; FIPS 203 in v17.5.1; two new NIST-compliant hybrid cipher groups (SecP256r1ML-KEM-768, SecP384r1ML-KEM-1024) in v21.1.
- maturity_flag: GA (v21.1)
- source_currency_flag: Current
- source: f5.com/company/blog "F5 BIG-IP v21.1 is now generally available"; f5.com/company/blog "F5 extends NIST-compliant PQC cipher support"; DevCentral "What's new in BIG-IP v21.1"

### [SSLO] Crypto-agility and centralized cipher/key management
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: Crypto-agile architecture, centralized cipher management, and HSM/key integration
- plain_description: F5 positions BIG-IP as a central control point where cryptographic policy (ciphers, hybrid PQC, TLS versions, certificate/key lifecycle) can be updated and rolled back across many apps without touching the apps themselves; keys can be protected in integrated or network HSMs.
- delivered_by: F5 BIG-IP (LTM/TMM); F5 ADSP framing; integrated HSM on select F5 hardware; third-party network HSM/KMS via PKCS#11 (Thales Luna, Fortanix DSM, AWS CloudHSM, Equinix SmartKey)
- attribution_confidence: Medium
- customer_problem_solved: PQC and shrinking certificate lifetimes require rapidly changing crypto across a large estate with zero downtime; per-app crypto changes are unmanageable and legacy/IoT/OT endpoints can't be modified.
- fit_signals: "We need to swap ciphers fast as standards change." "We can't touch our legacy/OT endpoints but need them behind quantum-safe crypto." "We need FIPS 140-2/140-3 Level 3 key protection." Mentions of crypto-agility, certificate lifecycle, HSM/FIPS compliance, centralized cipher policy.
- disqualifiers: Small single-app environments; organizations that manage crypto natively at each app and don't want a central proxy.
- value_framing: "Centralize crypto at the proxy: update ciphers and adopt PQC across your whole estate without re-architecting apps, and protect keys in FIPS-validated HSMs."
- product_routing_note: BIG-IP carries the cipher/HSM story. Note: F5's integrated HSM is FIPS-validated up to FIPS 140-2/140-3 Level 3 on select platforms (e.g., 10350v-F, rSeries/VELOS -DF SKUs with NITROX HSMs); F5 does not manufacture a network HSM but supports third-party network HSMs via PKCS#11. Confirm current per-platform FIPS certification status before making compliance claims.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/solutions/post-quantum-cryptography-readiness; f5.com/company/blog "F5 joins NIST PQC project"; f5.com/company/certifications; techdocs.f5.com "Hardware HSM Setup and Administration"; Thales/Fortanix integration docs

### [SSLO] Post-quantum cryptography on NGINX (separate delivery)
- solution_area: Encrypted Traffic Inspection & Cryptographic Modernization
- capability_name: PQC support in F5 NGINX
- plain_description: F5 NGINX supports PQC hybrid key exchange via the Open Quantum Safe provider for OpenSSL 3.x; availability depends on the OpenSSL version NGINX is built against.
- delivered_by: F5 NGINX Plus (PQC introduced in NGINX Plus R33) and NGINX Open Source / Ingress / Gateway Fabric (via OpenSSL 3.5+ or oqs-provider)
- attribution_confidence: High
- customer_problem_solved: Organizations running NGINX-fronted apps/APIs/microservices need quantum-safe key exchange without moving to BIG-IP.
- fit_signals: "We front our apps/APIs with NGINX and need PQC there." "We use NGINX Ingress/Gateway Fabric in Kubernetes and want quantum-safe TLS." Mentions of NGINX, Kubernetes ingress, microservices, OpenSSL versions.
- disqualifiers: Environments that don't use NGINX; teams that need turnkey PQC (NGINX PQC often requires manual OpenSSL/oqs-provider configuration and specific base images).
- value_framing: "Quantum-safe key exchange for your NGINX-fronted apps and APIs — but plan for OpenSSL version dependencies and manual configuration."
- product_routing_note: NGINX carries this independently of BIG-IP. Do not conflate NGINX PQC with BIG-IP PQC cipher groups — different products, different versions, different config. NGINX Plus R33 supports the final ML-KEM768 spec (manual enable); the base OS / OpenSSL version determines availability (OpenSSL 3.5+ enables several NIST PQC algorithms by default; Debian 12–based images do not, Alpine 3.22 / Debian 13 do).
- maturity_flag: GA (NGINX Plus R33+, with caveats)
- source_currency_flag: Current
- source: blog.nginx.org "Post-Quantum Cryptography (PQC) support in NGINX"; DevCentral "Post-Quantum Cryptography: Building Resilience" (NGINX Plus R33); F5 Labs "The State of PQC on the Web"

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Lead with BIG-IP SSL Orchestrator for the inspection story when:**
- The customer has an **on-prem or colo security stack** (NGFW, IPS/IDS, DLP, sandbox) and wants to feed multiple tools from one decryption point.
- They describe **decryption performance problems on firewalls**, **daisy-chained inline devices**, or **re-architecture pain** when adding tools.
- They need **selective decryption/bypass** for compliance (banking/healthcare/PII).
- Footprint signals: already own **BIG-IP LTM** → position SSLO as the **LTM + SSL Forward Proxy add-on** (lower friction, reuses existing platform). Greenfield or security-team-owned budget → position **standalone SSLO license**.

**Coexistence / migration notes:**
- SSLO commonly sits alongside existing NGFW/IPS/DLP — it does not replace them; it orchestrates them. This is a strength in the pitch ("keep your tools, make them work better").
- **BIG-IP Next SSL Orchestrator** existed only as **Limited Availability / evaluation** on the BIG-IP Next platform (e.g., BIG-IP Next 20.2.0; HA for SSLO was never supported from BIG-IP Next Central Manager) — and **the BIG-IP Next software line has since been discontinued** (K000152956; final v20.3 EoL April 30, 2025; see docs 05/14). Do **not** recommend it; there is no "BIG-IP Next journey" for SSLO. Classic BIG-IP SSLO (v14 on BIG-IP v21.1) is the go-forward product.

**Lead with BIG-IP (LTM/TMM) PQC ciphers for the crypto-modernization story when:**
- The customer terminates TLS on BIG-IP and has **harvest-now-decrypt-later** exposure or a **regulatory PQC driver** (government/defense/CNSA 2.0, finance, healthcare).
- They want PQC **without rearchitecting apps** — F5's stated positioning is to enable it at the proxy.

**Lead with NGINX PQC when:**
- The apps/APIs are **NGINX-fronted** (including Kubernetes ingress/Gateway Fabric) and the customer wants PQC there rather than on BIG-IP.

**Where the public record is thin (state honestly, do not invent F5 guidance):**
- Whether **F5 Distributed Cloud (XC)** offers PQC cipher **termination** in its data plane is **not clearly established** in public sources — F5 Labs used XC telemetry to *measure* the PQC readiness of web clients, and F5 markets PQC as an ADSP-wide/crypto-agile story, but a specific "XC terminates hybrid PQC ciphers" claim is **Unverified**. Do not assert it.
- **SSLO-specific ECH handling** is **not documented** by F5 (see capability record). Treat as an open question.

### 3b. Disqualifiers / anti-patterns (aggregate)

Signals that this solution area is a weak fit or "too early":
1. **Cloud-first / no on-prem inspection stack.** If decryption and inspection are fully handled by a cloud SASE/SSE provider (Zscaler, Prisma Access) and there is no on-prem tool chain, SSLO has little to orchestrate. Weak fit.
2. **Single inspection tool, no growth.** One NGFW comfortably doing its own decryption at current scale, with no plan to add tools — SSLO's orchestration value is muted.
3. **No inline proxy tolerance.** If the org will only do passive/tap inspection and cannot deploy an inline full proxy or distribute an internal CA to clients, outbound SSLO interception won't work.
4. **No long-confidentiality data and no PQC mandate.** For the PQC story, an org with no regulatory driver and no long-lived-secret data can legitimately defer — position it as "plan now, low urgency" rather than overselling.
5. **BYOD-heavy environments** where an internal CA can't be pushed to devices limit outbound interception (an industry-wide constraint, not F5-specific).
6. **"We already do PQC natively in our apps."** If a customer has genuine app-level crypto-agility, the proxy-level PQC pitch is weaker (though centralization/legacy-wrapping may still apply).

### 3c. Competitive positioning and objection handling (bounded — all lower confidence)

**Market context (lower confidence):** Named players in SSL/TLS inspection include **F5 (SSL Orchestrator)**, **A10 Networks (Thunder SSLi)**, **Gigamon (GigaSMART)**, **Broadcom/Symantec (SSL Visibility Appliance)**, plus **NGFW-native decryption** from **Palo Alto, Fortinet, Cisco, Check Point**, and **cloud SASE/SSE** (Zscaler, Palo Alto Prisma Access). Third-party market write-ups list F5, A10, Gigamon, Cisco, Broadcom, Fortinet, Check Point, and Palo Alto as the leading SSL-inspection vendors. All competitive claims below are lower-confidence and should be validated per deal — this market consolidates fast.

**Category 1 — Dedicated decryption appliances (Gigamon GigaSMART, A10 Thunder SSLi, Broadcom/Symantec SSL Visibility Appliance).**
- Verify current independence: A10 Networks and Gigamon remain independent vendors; Symantec's SSL Visibility Appliance is now under **Broadcom**. Verify status per deal.
- F5's stated differentiators (supported by public evidence): **dynamic service chaining** with independent addressability/scaling of tools (vs. simpler decrypt-and-forward), **full-proxy architecture**, **context-based steering**, and breadth of topologies (L2/L3/explicit/transparent/ICAP/TAP). A10 SSLi is a strong price/performance decryption play but is more decryption-centric; Gigamon's strength is the broader visibility/observability pipeline.
- Note honestly: A10 Thunder SSLi is also delivered as a module (Thunder CFW) or dedicated appliance, similar to SSLO's packaging flexibility, and A10 markets a "decrypt once, send to many devices, re-encrypt" secure-decrypt-zone architecture that closely parallels SSLO's. The differentiation is orchestration depth, not the basic decrypt-once concept.

**Category 2 — NGFW built-in decryption (Palo Alto, Fortinet, Cisco, Check Point).** Source of the most common objection (below).

**Category 3 — Doing nothing / passive inspection.** TLS 1.3's mandatory forward secrecy has broken passive/tap decryption, forcing a move to inline proxy architectures. "Doing nothing" increasingly means growing blind spots as encryption exceeds 90%+ of web traffic and 71% of malware arrives encrypted (WatchGuard Q1 2025).

**Primary objection: "Our firewall already decrypts."**
- Acknowledge it's true — NGFWs can decrypt. But:
  1. **Performance.** Turning on inspection features sharply cuts NGFW throughput even before TLS-decryption overhead is added. Palo Alto's own PA-5200 Series datasheet rates the PA-5260 at 72.2 Gbps App-ID firewall throughput but only 30 Gbps with Threat Prevention enabled — roughly a 58% drop — and enabling SSL decryption compounds it further; Palo Alto community threads report SSL-decrypt making internet performance "almost unusable" and 5x slower connections when under-sized. Third-party testing similarly cites large TLS-inspection throughput reductions on FortiGate SPU platforms. Decrypting on every device multiplies this cost.
  2. **Duplication.** If you have an NGFW *and* an IPS *and* a DLP, each decrypting the same traffic is wasteful; SSLO decrypts once and feeds all of them.
  3. **Rigidity.** NGFW-native decryption doesn't dynamically service-chain to your other tools or scale them independently.
  4. **Tool lifespan/cost.** Offloading decryption lets existing security tools spend 100% of their cycles on inspection, deferring hardware upgrades.
- Honest boundary: if the customer truly has a single NGFW handling all inspection at comfortable scale, the objection may stand — this is a disqualifier, not a fight to force.

**PQC-specific competitive note (lower confidence):** F5's differentiator is enabling **hybrid PQC at the proxy without rearchitecting apps** and centralizing crypto-agility across a mixed estate — framed as an ADSP platform advantage vs. per-app or per-endpoint PQC retrofits. For context on the edge-provider comparison: Cloudflare has enabled hybrid X25519MLKEM768 by default on all TLS 1.3 connections since October 2022, and per Cloudflare Radar over 50% of human web traffic was post-quantum encrypted by October 2025 (jumping from ~29% to ~52% within about a week of iOS 26 shipping in mid-September 2025). F5's angle is enterprise control, on-prem/hybrid coverage, legacy-wrapping, and centralized management rather than default-on edge PQC. Validate any head-to-head claim.

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch:**
- **BIG-IP SSL Orchestrator (SSLO)** — current. Packaged as **standalone SSLO base license** or **LTM + SSL Forward Proxy add-on**. Current module version **SSL Orchestrator v14**, shipping with **BIG-IP v21.1 (GA June 2026, announced June 4, 2026)**.
- **BIG-IP Next SSL Orchestrator** — existed on BIG-IP Next (e.g., 20.2.0) as Limited Availability / evaluation only, but **the BIG-IP Next platform was discontinued** (K000152956; final v20.3 EoL April 30, 2025 — see docs 05/14). Do not position it in any form. (Note: BIG-IP Next for Kubernetes / CNFs are separate, active product lines and are unaffected.)
- **BIG-IP APM → BIG-IP Zero Trust Access** — APM is being renamed/evolved to **BIG-IP Zero Trust Access** (announced AppWorld 2026). Relevant here only because it carries **quantum-resistant VPN tunneling**; the access/VPN story belongs to sibling doc 07.
- **F5 ADSP (Application Delivery and Security Platform)** — the umbrella F5 now uses for the portfolio, including SSLO and PQC.
- PQC cipher naming: **hybrid X25519_ML-KEM-768** (v17.5.0, initially an early draft "X25519Kyber768Draft00" that F5 Labs notes is **not** compatible with the final spec); **FIPS 203 / ML-KEM** support in v17.5.1; two new NIST-compliant hybrid groups **SecP256r1ML-KEM-768** and **SecP384r1ML-KEM-1024** in v21.1.

**Explicitly NOT verified (do not assert):**
- **SSLO-specific ECH (Encrypted Client Hello) handling** — no F5 public documentation found (targeted research across techdocs, clouddocs, my.f5.com, DevCentral, F5 Labs). ECH appears in F5-owned content only as an **NGINX server-side** feature (NGINX Plus 37.0 / NGINX OSS 1.29.4), which is unrelated to SSLO inspection. Open question.
- **F5 Distributed Cloud (XC) PQC cipher termination** in the data plane — not established in public sources; F5 Labs used XC telemetry to measure client PQC readiness, which is different from XC offering PQC termination.
- **Exact GA status of SSLO's AI data-protection / Shadow AI features** — announced July 2025 with planned availability late 2025; confirm before positioning as shipping.
- **Per-platform FIPS 140-2/140-3 certification status** — changes over time (certs move to "historical" on the CMVP list); verify current status before compliance claims. Note also that F5's integrated HSM is FIPS-validated but the BIG-IP systems are not themselves Level 3 validated as whole systems.
- Specific SSLO performance/throughput numbers — see F5 SSLO platform datasheets; not reproduced here.

**Regulatory driver dates (for PQC context; third-party and NIST/NSA sources):**
- **NIST FIPS 203/204/205** finalized **August 13, 2024** (ML-KEM, ML-DSA, SLH-DSA).
- **NIST IR 8547** (initial public draft, Nov 2024): RSA-2048/ECC P-256 **deprecated by 2030**, quantum-vulnerable public-key algorithms **disallowed by 2035**.
- **NSA CNSA 2.0** (Sept 2022): new National Security System acquisitions must support CNSA 2.0 from **Jan 1, 2027**; traditional networking equipment (VPNs/routers) exclusive use by **2030**; operating systems and cloud/web services exclusive use by **2033**; broad full transition targeted **2033–2035** (NSM-10 end goal ~2035); specifies **ML-KEM-1024** and **ML-DSA-87**.
- F5 press materials cite **Gartner** projecting asymmetric cryptography unsafe by **2029** and fully breakable by **2034** — attribute to Gartner via F5, not as F5's own claim. (Directionally corroborated by Cloudflare, which targets 2029 for full post-quantum security.)

**Primary sources leaned on:** f5.com SSL Orchestrator product page; techdocs.f5.com and clouddocs.f5.com SSLO deployment/architecture guides and release notes (21.1.0-14.0); DevCentral (Introduction to SSLO, What's new in BIG-IP v21.1, What's new in SSLO v14, NGINX PQC); f5.com/company/blog PQC posts; f5.com/solutions/post-quantum-cryptography-readiness; f5.com press releases (AppWorld 2026, PQC solutions); F5 Labs "State of PQC on the Web"; blog.nginx.org PQC; f5.com/company/certifications; techdocs.f5.com Hardware HSM administration.
**Third-party sources (competitive/reality-check, lower trust):** A10 Networks, Gigamon, PeerSpot, Palo Alto PA-5200 datasheet and LIVEcommunity threads, Fortinet/Cisco decryption docs, NIST/NSA/CNSA materials, RFC 9849, WatchGuard Internet Security Report, Google Transparency Report, W3Techs, Cloudflare Radar, Network World, Fierce Network.