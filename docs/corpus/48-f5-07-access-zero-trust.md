# F5 Access Security & Zero Trust Application Access — Solution Area Reference (Doc 07)
doc_id: 07-access-zero-trust
solution_area: Access Security & Zero Trust Application Access
doc_tag: ZTA
products_covered: F5 BIG-IP Zero Trust Access (formerly BIG-IP Access Policy Manager / APM), F5 Access clients (BIG-IP Edge Client, F5 Access for mobile), BIG-IP APM orchestrated by F5 Distributed Cloud (MSP, Limited Availability), F5 Distributed Cloud Universal ZTNA / Zero Trust Domain Service (pre–Early Access)
compiled: July 2026
primary_release_anchor: F5 AppWorld 2026 (March 10–12, 2026) APM→Zero Trust Access rename; BIG-IP v21.1 GA (June 4, 2026)
refresh_priority: High
last_validated: July 2026

## Layer 1 — Human orientation

**Bottom line:** This solution area is F5's application-access story, delivered almost entirely by one product: the BIG-IP module historically called **Access Policy Manager (APM)**, which F5 **renamed "BIG-IP Zero Trust Access" at AppWorld 2026 (announced March 11, 2026)**. The single most important fact for an SE on a live call: **the rename is a marketing/branding change, not a functional one.** F5's own announcement says F5 "will continue to support the existing BIG-IP APM use cases" and the product "isn't going away; it's just changing its name." The module SKU, licensing, techdocs, release-note sections ("Access Policy Manager Fixes"), the `access-policy-manager` product URL, and the AWS Marketplace listings all still say "APM." Treat both names as the same thing and expect "APM" to persist in technical materials for years.

**What it does.** BIG-IP Zero Trust Access is a reverse-proxy access-control point that sits in front of applications and enforces identity- and context-aware policy on access. Core use cases: SSL/TLS VPN and IPsec VPN (remote access); identity-aware proxy (IAP) / per-app access with per-request policy evaluation; single sign-on across hybrid apps; identity federation and legacy-auth bridging (fronting Kerberos/NTLM/header-based/form-based legacy apps with modern SAML/OAuth/OIDC); VDI proxying (Citrix, VMware/Omnissa Horizon); and OAuth/OIDC authorization-server functions for APIs (cross-reference Doc 01 for API security depth).

**Delivery models.** (1) The dominant model is the **BIG-IP module** — an add-on to BIG-IP LTM or standalone — available as hardware (rSeries/VELOS; note iSeries/VIPRION are end-of-life for v21.1), Virtual Edition, and public-cloud marketplace, licensed perpetual/subscription/ELA. (2) **F5 Access clients** (BIG-IP Edge Client on Windows/macOS/Linux, F5 Access mobile apps) are the endpoint delivery detail for VPN and per-app VPN. (3) **BIG-IP APM orchestrated by F5 Distributed Cloud** is a Limited-Availability MSP offering that centrally manages/bills existing BIG-IP APM instances — it is an orchestration layer, not a new cloud data plane. (4) A separate **F5 Distributed Cloud "Universal ZTNA" / Zero Trust Domain Service** is documented but **pre–Early Access ("will enter Early Access soon") as of mid-2026** — do not pitch it as available.

**Honest market position.** F5 is **not a full SASE/SSE vendor**. It does not sell SWG, CASB, or DLP as a cloud-delivered secure-access edge, and F5 itself frames SASE and its own platform as complementary "dual planes": SASE/ZTNA secures the user/network access plane (forward proxy — who can connect); F5 secures the application plane via **Zero Trust Application Access (ZTAA)** (reverse proxy — what happens once traffic arrives). F5's differentiated, defensible story is **access for hybrid/on-prem/legacy apps**, especially bridging modern identity (Microsoft Entra ID, Okta) to legacy-auth apps that pure SSE vendors cannot front. A customer wanting full SASE with SWG/CASB is a routing-away signal (see Disqualifiers).

**How to read the rest.** Layer 2 is the capability catalog (one record per capability, each self-contained). Layer 3 gives product routing, aggregate disqualifiers, and bounded competitive/objection handling. The appendix tracks perishable naming and what was not verified.

## Layer 2 — Capability catalog

### [ZTA] Identity-Aware Proxy (IAP) / per-app zero trust access
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Identity-Aware Proxy (IAP) / per-request application access
- plain_description: A reverse proxy that authenticates and authorizes a user for one specific application at a time, re-checking identity and context on each new app request rather than granting broad network access.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM)
- attribution_confidence: High
- customer_problem_solved: Traditional VPNs grant broad network-level access after a single login, enabling lateral movement if credentials are stolen. IAP enforces least-privilege, one-app-at-a-time access to limit horizontal movement.
- fit_signals: "Once someone's on the VPN they can see the whole flat network"; "we failed a pen test / audit finding on lateral movement"; "we want per-application access, not network access"; "we're doing a zero-trust initiative and need a policy enforcement point in front of on-prem apps"; auditors citing NIST 800-207; a breach post-mortem showing an attacker pivoted from a VPN foothold.
- disqualifiers: Customer's apps are 100% modern SaaS already fronted by an IdP with per-app SSO and conditional access (Entra/Okta may suffice alone); customer wants agent-based network-layer ZTNA to arbitrary TCP/UDP services rather than reverse-proxy app access; greenfield cloud-native shop with no on-prem/legacy footprint.
- value_framing: "Turn every app request into a checkpoint. A stolen credential gets an attacker into one app under one policy — not your whole network. This is zero trust you can put in front of the legacy apps your SSE vendor can't touch."
- product_routing_note: Only BIG-IP Zero Trust Access delivers this in F5's portfolio today. If the customer wants cloud-delivered/agent ZTNA, F5's XC Universal ZTNA is pre–Early Access — do not commit.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; f5.com blog "Hello, F5 BIG-IP Zero Trust Access" (Mar 11 2026)

### [ZTA] SSL/TLS VPN remote access
- solution_area: Access Security & Zero Trust Application Access
- capability_name: SSL/TLS VPN (network access) and VPN replacement
- plain_description: Encrypted remote-access VPN tunneling to corporate resources via the BIG-IP Edge Client and F5 Access apps, with the option to migrate customers off broad VPN toward per-app access.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM); F5 Access clients (BIG-IP Edge Client for Windows/macOS/Linux; F5 Access for iOS/Android)
- attribution_confidence: High
- customer_problem_solved: Organizations running aging or vulnerable incumbent VPN appliances need a scalable, well-supported remote-access platform, ideally as a stepping stone to per-app zero trust.
- fit_signals: "Our Ivanti/Pulse boxes keep getting CVEs and we're patching under emergency directives"; "our VPN concentrator is going end-of-life"; "we're consolidating remote access onto the F5 boxes we already own for load balancing"; "we need to support 100k+ concurrent remote users"; incumbent-VPN CVE fatigue (Ivanti Connect Secure CVE-2025-0282 / CVE-2025-22457-class incidents).
- disqualifiers: Customer wants a cloud-delivered, appliance-free remote-access service with a global PoP backbone (that's SSE/ZTNA territory, not BIG-IP); very small orgs wanting a turnkey SaaS VPN; customers explicitly trying to eliminate all on-prem/edge appliances post-incident.
- value_framing: "Land on the VPN you need today, then phase down broad tunnels toward per-app access on the same platform — no rip-and-replace. Scales to 1M sessions per device / 2M per chassis."
- product_routing_note: Lead with BIG-IP module for existing F5 shops or those wanting on-prem control. Be candid that F5 is an appliance/VE model, not a cloud PoP model — if the buyer's core requirement is "no more boxes," this is a weak fit.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; techdocs.f5.com APM; BIG-IP APM datasheet (f5.com/pdf/data-sheet/big-ip-access-policy-manager-ds.pdf)

### [ZTA] IPsec VPN tunneling
- solution_area: Access Security & Zero Trust Application Access
- capability_name: IPsec VPN (client-to-site / site-to-site)
- plain_description: A private encrypted IPsec tunnel option for remote and site connections, added as an alternative to the historical TLS/SSL VPN.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM), BIG-IP v21.1+ with APM Clients 7.2.7+
- attribution_confidence: High
- customer_problem_solved: Some customers (often regulated/government) require IPsec rather than TLS VPN, or want to migrate existing SSL-VPN connectivity profiles to IPsec.
- fit_signals: "Our security standard mandates IPsec"; "we want to move our SSL-VPN users to IPsec"; government/defense buyers with IPsec requirements.
- disqualifiers: Customer is happy on TLS VPN and has no IPsec mandate; wants cloud-delivered IPsec-as-a-service.
- value_framing: "Convert an existing SSL-VPN connectivity profile to IPsec by changing one setting — familiar workflow, no new platform."
- product_routing_note: New/expanded in BIG-IP v21.1; note SSL→IPsec conversion is supported but IPsec→SSL is not (requires new profile). IPsec auth supports only machine-certificate auth in this release.
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com BIG-IP 21.1.0 New Features; techdocs.f5.com "Configuring Access IPsec VPN Tunnels" (edge-client-7-2-7)

### [ZTA] SSO and identity federation across hybrid apps
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Single sign-on and identity federation (SAML/OAuth/OIDC)
- plain_description: One login for users across cloud, SaaS, and on-prem apps, with BIG-IP acting as a SAML IdP or SP and federating identity across applications.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM)
- attribution_confidence: High
- customer_problem_solved: Users juggle multiple logins across apps of different eras; security teams want centralized authentication and a single control point for access policy.
- fit_signals: "We have a mix of cloud and on-prem apps and want one sign-on experience"; "we need an SP-initiated and IdP-initiated SAML flow in front of internal apps"; "we run our own IdP and need chaining/federation"; universities and enterprises citing thousands of users across many virtual servers.
- disqualifiers: All apps already natively support modern SSO through the customer's IdP with no proxy needed; customer has no on-prem or non-standard apps.
- value_framing: "One catalog, one login, whether the app is SAML-enabled or not — and F5 becomes the enforcement point where you attach MFA and conditional access."
- product_routing_note: Frequently deployed alongside Okta or Microsoft Entra ID (see legacy-auth bridging record). BIG-IP module only.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; f5.com/solutions/use-cases/control-app-access-with-zero-trust

### [ZTA] Legacy authentication bridging (SAML/OIDC in front of Kerberos/NTLM/header/form-based apps)
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Modern-to-legacy authentication bridging / protocol transition
- plain_description: BIG-IP sits in front of an old application that only speaks Kerberos, NTLM, header-based, or form-based auth, and lets a modern IdP (Entra ID, Okta) pre-authenticate the user — translating the modern token into whatever the legacy app understands.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM), integrated with Microsoft Entra ID (Secure Hybrid Access) and Okta
- attribution_confidence: High
- customer_problem_solved: A large share of on-prem apps (SAP, Oracle, custom apps) can't do SAML/OAuth and can't be modernized quickly; without a bridge they're excluded from conditional access, MFA, and SSO. This is precisely the gap SSE/ZTNA vendors cannot close.
- fit_signals: "We're going all-in on Entra/Okta but have a pile of old apps that can't do modern auth"; "we want conditional access and MFA in front of a header-based/Kerberos app"; "we're replacing ADFS / retiring the WAP proxy"; "we can't modernize these apps this year but need them in our zero-trust scope"; migration/decoupling projects fronting ADFS.
- disqualifiers: Customer has no legacy/classic apps (pure modern SaaS/cloud-native); customer will retire the legacy apps imminently rather than front them; the app already supports OIDC/SAML directly.
- value_framing: "This is the thing Zscaler and Netskope can't do. F5 puts modern identity — Entra conditional access, MFA, passwordless — in front of the Kerberos/NTLM/header apps you can't rewrite, so they finally join your zero-trust architecture instead of being carved out of it."
- product_routing_note: This is F5's single most defensible differentiator in this solution area. Microsoft documents this as "Secure Hybrid Access (SHA)" with Easy Button guided-config templates; use Microsoft Learn F5 integration docs as third-party corroboration. BIG-IP module only.
- maturity_flag: GA
- source_currency_flag: Current
- source: learn.microsoft.com "Integrate F5 BIG-IP with Microsoft Entra ID" and Kerberos/header/form-based SSO tutorials; f5.com BIG-IP APM datasheet; DevCentral "Harnessing the power of F5 BIG-IP APM and Microsoft"

### [ZTA] VDI proxying (Citrix / VMware-Omnissa Horizon)
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Virtual desktop / published-app proxy (VDI)
- plain_description: BIG-IP acts as a secure proxy and pre-authentication gateway in front of Citrix and VMware/Omnissa Horizon environments, including native protocol proxying (PCoIP, Blast Extreme, Citrix ICA) and optional replacement of StoreFront/Web Interface tiers.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM)
- attribution_confidence: High
- customer_problem_solved: VDI deployments need scalable, secure remote access, pre-authentication, MFA, and smart-card support in front of thousands of virtual desktops, plus consolidation of separate proxy tiers.
- fit_signals: "We front Citrix/Horizon with F5 for remote access and want to add MFA/smart cards"; "we want to collapse our StoreFront/security-server tiers"; "we need PCoIP/Blast proxy for remote desktop users"; federal customers using CAC/smart-card auth to VDI.
- disqualifiers: Customer has no VDI, or has moved to a DaaS that includes its own access gateway; customer's VDI vendor gateway already meets all requirements.
- value_framing: "Consolidate the VDI access and pre-auth tier onto BIG-IP, add MFA/smart-card and per-session policy, and proxy the native display protocols securely."
- product_routing_note: BIG-IP module only. Verify current protocol/version support against the APM Client Compatibility Matrix — much VDI deployment-guide material predates the VMware→Omnissa Horizon rebrand (Broadcom spun out EUC as Omnissa in 2024) and the Citrix→Cloud Software Group changes; treat specific version claims as possibly stale.
- maturity_flag: GA
- source_currency_flag: Possibly stale (deployment guides predate Omnissa/Citrix rebrands; capability current, version details may lag)
- source: techdocs.f5.com BIG-IP APM Client Compatibility Matrix; f5.com/pdf/deployment-guides/citrix-vdi-iapp-dg.pdf; f5.com VMware Horizon deployment guides

### [ZTA] Endpoint posture / device integrity checks
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Device posture, integrity checks, and step-up authentication
- plain_description: Before and during access, BIG-IP checks device security state and can demand additional authentication (e.g., MFA) when risk warrants, integrating with MDM/EMM and third-party risk engines.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM), with F5 Access Guard; MDM/EMM integrations (Microsoft Intune, VMware/Omnissa Horizon ONE (AirWatch), IBM MaaS360)
- attribution_confidence: High
- customer_problem_solved: Access decisions shouldn't rest on credentials alone; posture and context (device health, location, sensitivity) should gate and escalate authentication.
- fit_signals: "We want to check device compliance before granting access"; "we use Intune and want posture to feed access policy"; "we need step-up MFA for sensitive apps"; "we want to plug a UEBA/risk engine into access decisions."
- disqualifiers: Customer relies entirely on their IdP's/endpoint vendor's posture (e.g., Entra conditional access + Intune) and doesn't want a second enforcement point; no MFA/posture requirements.
- value_framing: "Continuous, context-aware checks — not just at login — and escalate to MFA exactly when the device, location, or data sensitivity calls for it."
- product_routing_note: Intune posture and Entra conditional access are commonly integrated via APM's Access Guided Configuration ("Easy Button"). BIG-IP module only.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; learn.microsoft.com F5 BIG-IP + Entra ID; DevCentral Intune endpoint compliance article

### [ZTA] OAuth/OIDC authorization server & API access (incl. Dynamic Client Registration)
- solution_area: Access Security & Zero Trust Application Access
- capability_name: OAuth 2.0 / OIDC authorization server and API authorization, with Dynamic Client Registration (DCR)
- plain_description: BIG-IP acts as an OAuth 2.0 authorization server / OIDC provider to authorize access to APIs and apps, and (new) lets clients — including AI agents and MCP servers — register themselves programmatically instead of manual pre-configuration.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM); DCR added in BIG-IP v21.1
- attribution_confidence: High (attribution to the access module); note API *security* depth belongs to Doc 01
- customer_problem_solved: APIs and modern clients need standards-based authorization; onboarding new clients (agents, MCP servers, CI/CD) manually is slow and doesn't scale.
- fit_signals: "We need an OAuth/OIDC authorization server in front of our APIs"; "we're standing up AI agents / MCP servers that need to register and get credentials automatically"; "our DevOps pipeline should request access programmatically."
- disqualifiers: Full API discovery/schema enforcement/threat protection is wanted — that's F5 Distributed Cloud API Security / Doc 01, not this module; customer already has a dedicated API gateway/authorization server.
- value_framing: "Standards-based API authorization on the same box that fronts your apps — and DCR lets agents and pipelines self-register securely instead of waiting on a ticket."
- product_routing_note: Cross-reference Doc 01 for API security. DCR is RFC 7591-based and, per F5, aimed at AI agents/MCP/IoT. Lead with this only when the need is authorization, not full API protection.
- maturity_flag: GA (DCR GA in v21.1)
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; techdocs.f5.com BIG-IP 21.1.0 New Features (OAuth 2.0 DCR / RFC 7591); f5.com blog v21.1 GA (Jun 4 2026)

### [ZTA] Access Guided Configuration (AGC) / Visual Policy Editor
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Access Guided Configuration (AGC) and Visual Policy Editor (VPE)
- plain_description: Configuration tooling — a guided template workflow (AGC, incl. the Microsoft "Easy Button") and a graphical policy editor (VPE) — to onboard apps and build access policies without hand-coding.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM)
- attribution_confidence: High
- customer_problem_solved: Access policy can be complex; templates and a visual editor lower deployment time and skill barriers, including for Entra conditional access and legacy-app onboarding.
- fit_signals: "How hard is it to configure / how long to onboard an app?"; "we don't have deep F5 skills on staff"; "we want templates for Entra/Azure AD conditional access."
- disqualifiers: Not a standalone buying driver; irrelevant if the customer isn't buying the module.
- value_framing: "Templated onboarding — including a Microsoft 'Easy Button' — plus a visual policy canvas, so you're not scripting policy from scratch."
- product_routing_note: Terminology is current on f5.com and techdocs ("Access Guided Configuration," "Visual Policy Editor," "Zero Trust–Identity Aware Proxy" template). BIG-IP module only.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/zero-trust-access; techdocs.f5.com "About zero trust" (per-request policies)

### [ZTA] PQC-ready VPN and access
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Post-quantum cryptography (PQC) for VPN/access
- plain_description: Quantum-resistant hybrid key exchange (X25519 + ML-KEM-768) for TLS/SSL VPN tunneling and access, aligning to NIST/FIPS 203, to protect against "harvest now, decrypt later" threats.
- delivered_by: F5 BIG-IP Zero Trust Access (formerly BIG-IP APM) and its clients; BIG-IP v21.1
- attribution_confidence: High
- customer_problem_solved: Long-lived VPN-tunneled data captured today could be decrypted by future quantum computers; regulated customers face NIST/FIPS PQC-migration pressure.
- fit_signals: "We need a PQC/quantum-safe migration plan"; "our regulator/agency mandates NIST PQC ciphers"; "we worry about harvest-now-decrypt-later on our VPN traffic"; government/defense and financial buyers.
- disqualifiers: Customer has no PQC mandate or roadmap pressure; not a near-term concern for the buyer.
- value_framing: "Quantum-resistant VPN tunneling on the platform you already run — crypto-agility for compliance today and Q-Day tomorrow."
- product_routing_note: BIG-IP module. PQC VPN tunneling shipped in v21.1 (GA June 2026); IPsec PQC signaled as future ("not-too-distant future") — flag as roadmap, not shipped.
- maturity_flag: GA (TLS/SSL VPN PQC in v21.1); Roadmap/Announced (IPsec PQC)
- source_currency_flag: Current
- source: f5.com blog "BIG-IP v21.1 is now generally available" (Jun 4 2026); f5.com blog "sneak peek into BIG-IP v21.1"

### [ZTA] BIG-IP APM orchestrated by F5 Distributed Cloud (MSP)
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Centralized orchestration/billing of BIG-IP APM via F5 Distributed Cloud (MSP)
- plain_description: An F5 Distributed Cloud workspace that centrally manages, monitors, and meters existing BIG-IP APM instances across sites — primarily for managed service providers. It is a management/billing layer, not a new cloud access data plane.
- delivered_by: F5 Distributed Cloud (orchestrating BIG-IP APM instances on public cloud, bare metal, F5 App Stack, or F5OS)
- attribution_confidence: High
- customer_problem_solved: MSPs and large operators running many BIG-IP APM instances want centralized operations, health/usage visibility, and utilization-based billing across customers/sites.
- fit_signals: "We're an MSP deploying APM for multiple customers and want one console and consumption billing"; "we run APM across many sites and want central health/usage."
- disqualifiers: Single-enterprise customers not operating multi-tenant/multi-site APM at scale; anyone expecting a cloud-native SaaS access data plane (this isn't one).
- value_framing: "Run the full BIG-IP APM feature set, but manage and meter it centrally across all your sites and tenants."
- product_routing_note: Limited Availability (LA), MSP-gated (contact via BIG-IPOnF5XC@f5.com). Do not position as GA or as a standalone cloud ZTNA service.
- maturity_flag: Beta/Early Access (Limited Availability)
- source_currency_flag: Current
- source: docs.cloud.f5.com/docs-v2/bigip-apm and /how-tos/external-service-management/deploy-manage-big-ip-apm

### [ZTA] F5 Distributed Cloud Universal ZTNA / Zero Trust Domain Service
- solution_area: Access Security & Zero Trust Application Access
- capability_name: Cloud-delivered Universal ZTNA (Zero Trust Domain Service)
- plain_description: A documented F5 Distributed Cloud service intended to deliver cloud-native zero-trust access, but not yet launched — it is still pre–Early Access as of mid-2026.
- delivered_by: F5 Distributed Cloud (Zero Trust Domain Service)
- attribution_confidence: Medium (exists in docs; scope/features not GA-verifiable)
- customer_problem_solved: (Intended) cloud-delivered, IdP-integrated zero-trust access without deploying access appliances — but this is aspirational until it ships.
- fit_signals: A customer explicitly asking F5 for a cloud-delivered/agent ZTNA alternative to the BIG-IP appliance model; note this is a gap-probe, not a fit signal for something you can sell today.
- disqualifiers: Any near-term requirement — this is not sellable/committable now. If the customer needs cloud ZTNA today, this does not meet it.
- value_framing: Do not pitch as available. At most: "F5 has a cloud-delivered ZTNA service in development; today the shipping F5 answer is the BIG-IP Zero Trust Access module."
- product_routing_note: Pre–Early Access ("will enter Early Access soon"); an XC ZTNA console tile was temporarily removed "while the program undergoes continued development." Treat as roadmap only. Do not conflate with the BIG-IP module.
- maturity_flag: Roadmap/Announced (pre–Early Access)
- source_currency_flag: Current
- source: docs.cloud.f5.com/docs-v2/uztna; docs.cloud.f5.com SaaS release-notes changelog (ZTNA tile removal)

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Default answer:** For essentially every application-access opportunity in this solution area, the product is **BIG-IP Zero Trust Access (formerly APM)**, delivered as a BIG-IP module. There is no shipping F5 cloud-native ZTNA alternative as of mid-2026.

- **Existing F5 BIG-IP customer (LTM/WAF/etc.):** Strongest fit. APM/Zero Trust Access is an add-on module to their existing BIG-IP (hardware, VE, or cloud). Lead with consolidation: same platform, same ops team, add access. Confirm hardware currency — v21.1 does **not** run on legacy iSeries/VIPRION; those customers must move to rSeries/VELOS or Virtual Edition, which is itself a migration trigger to discuss.
- **On-prem / hybrid / legacy-app heavy shop:** Strongest use-case fit. Lead with legacy-auth bridging (Entra/Okta in front of Kerberos/NTLM/header/form-based apps), IAP, and SSO. This is where F5 wins against SSE vendors.
- **Cloud-native / SaaS-only greenfield:** Weak fit. If they have no on-prem/legacy apps and want cloud-delivered secure access, route toward their IdP's capabilities and/or an SSE/ZTNA vendor; be honest that F5's shipping product is an appliance/VE reverse proxy.
- **Wants "no more appliances" after a VPN incident:** Weak-to-moderate fit. F5 can replace the incumbent VPN, but it's still an edge/VE reverse-proxy model. If the buyer's hard requirement is a cloud PoP model with no boxes, F5's shipping answer doesn't meet it (XC Universal ZTNA is pre-EA).
- **Self-managed vs managed:** Enterprises self-manage the BIG-IP module. MSPs/multi-site operators wanting central management + consumption billing of many APM instances are the audience for **BIG-IP APM orchestrated by F5 Distributed Cloud** (Limited Availability, MSP-gated) — set expectations that it's an orchestration layer, not a new data plane, and is LA.
- **Buyer persona:** NetOps/SecOps and identity/IAM teams who already own or trust BIG-IP. For pure cloud-security/SASE buyers, F5 is a complement, not the platform.

**Coexistence / migration notes.** F5 explicitly positions BIG-IP Zero Trust Access as complementary to SASE/SSE (dual-plane: SASE = user/network access plane via forward proxy; F5 = application plane via reverse proxy / ZTAA). A customer can run Zscaler/Netskope for user-to-network access **and** F5 for application-plane access and legacy-auth bridging simultaneously; this is F5's recommended framing, not a concession. Migration from broad SSL-VPN toward per-app IAP happens on the same platform incrementally. SSL-VPN connectivity profiles can be converted to IPsec (not vice-versa).

**Where the public record is thin — do not invent guidance.** F5 does not publish a clean "when to use the BIG-IP module vs. XC Universal ZTNA" decision matrix, because XC Universal ZTNA hasn't shipped. Do not fabricate official routing between them. Similarly, there is **no BIG-IP Next access/APM module** to route to: F5 discontinued BIG-IP Next in 2025 and is folding its intended capabilities into BIG-IP TMOS (v21.x). Do not reference a "BIG-IP Next APM."

### 3b. Disqualifiers / anti-patterns (aggregate)

- **"We want full SASE with SWG and CASB."** Routing-away signal. F5 does not sell SWG/CASB/DLP as a secure-access edge and frames SASE as a complementary plane. Route to an SSE vendor; position F5 only for the application plane / legacy bridging alongside it.
- **"We want cloud-delivered ZTNA with no appliances, available now."** F5's shipping product is a reverse-proxy appliance/VE. XC Universal ZTNA is pre–Early Access. Weak fit today; don't over-promise the roadmap.
- **"All our apps are modern SaaS behind Okta/Entra already."** The IdP may already deliver SSO/conditional access per app; F5's incremental value (legacy bridging, reverse-proxy enforcement) may be low. Qualify hard for on-prem/legacy apps before pursuing.
- **"We're eliminating on-prem edge devices after a breach."** Sensitivity is high post-incident (including F5's own October 2025 breach, below). If the driver is "get rid of internet-facing appliances," an on-prem BIG-IP may be a hard sell; acknowledge it honestly.
- **"We need API discovery/schema enforcement/threat protection."** That's Doc 01 (API security), not this module's OAuth authorization function.
- **Very small orgs wanting turnkey SaaS remote access.** Operational weight of BIG-IP is likely a poor match.
- **Buyer wants agent-based access to arbitrary TCP/UDP services across a mesh.** That's network-layer ZTNA; F5's shipping strength is reverse-proxy application access.

### 3c. Competitive positioning and objection handling (bounded — lower confidence)

All competitive claims below are lower-confidence and reflect F5's *stated* positioning plus third-party market context, not verified head-to-head wins. This market consolidates quickly; re-verify vendor status each refresh.

**Category 1 — Cloud SSE/ZTNA (Zscaler, Netskope, Palo Alto Prisma Access, Cloudflare Access/One).** All four remain independent as of mid-2026 (Zscaler and Netskope are standalone public companies; Prisma Access is Palo Alto Networks; Cloudflare Access is part of Cloudflare One). These are cloud-delivered, PoP-based, forward-proxy secure-access platforms. Per the **Gartner Magic Quadrant for Security Service Edge published May 20, 2025**, the three Leaders are **Netskope, Zscaler, and Palo Alto Networks** (Netskope placed furthest on Completeness of Vision; Zscaler leads on Ability to Execute); **Cloudflare is evaluated but is not a Leader**. **F5 is not an SSE Magic Quadrant vendor at all.** F5's *stated* differentiator: reverse-proxy application-plane access (ZTAA) with per-request Layer 7 control, and legacy-auth bridging for apps these SSE vendors cannot front. Lower confidence on any "F5 wins" claim.

**Category 2 — Legacy/enterprise VPN (Cisco, Ivanti).** Cisco AnyConnect is now **Cisco Secure Client** (rebrand; AnyConnect persists as the VPN module) — still Cisco, independent. Ivanti Connect Secure (formerly Pulse Connect Secure) is still Ivanti and has been a repeat victim of severe, in-the-wild-exploited vulnerabilities: Mandiant/Google confirm China-nexus actor **UNC5221 exploited CVE-2025-0282** (zero-day RCE from mid-December 2024, unauthenticated stack buffer overflow) and **CVE-2025-22457** (CVSS 9.0, exploited from mid-March 2025 by reverse-engineering Ivanti's Feb 11, 2025 patch), deploying the TRAILBLAZE dropper and BRUSHFIRE backdoor. End-of-support **Pulse Connect Secure 9.1x reached End-of-Support Dec 31, 2024 and will not be patched** for CVE-2025-22457; affected versions include Ivanti Connect Secure 22.7R2.5 and earlier. F5's *stated* angle: a scalable remote-access platform and a migration path from broad VPN to per-app zero trust. **Caution:** F5 itself is not immune — see the breach note below; use VPN-CVE-fatigue framing carefully and honestly.

**Category 3 — Identity vendors' app proxies (Microsoft Entra Application Proxy / Private Access, Okta).** Both are partners *and* overlap competitors. Microsoft explicitly documents F5 BIG-IP as the recommended way to bridge legacy-auth apps into Entra (Secure Hybrid Access) — so F5's strongest differentiator is co-marketed by Microsoft. F5's *stated* angle: for Kerberos/header/form-based apps and complex per-request policy, BIG-IP goes further than Entra App Proxy alone. Lower confidence; treat Microsoft as a frenemy.

**The specific objection: "We're already going all-in on Zscaler/SASE — why keep an access appliance?"**
Recommended, evidence-supported response: "Zscaler and F5 solve different halves of zero trust. Zscaler (SSE) secures the user/network access plane — who can connect and reach the network — as a forward proxy. F5 secures the application plane as a reverse proxy: what a request can actually do once it arrives, per-request, at Layer 7. Crucially, F5 fronts your Kerberos/NTLM/header-based legacy apps with modern identity (Entra/Okta conditional access, MFA) — the apps SSE can't natively bridge. F5 itself calls these complementary planes, not competitors. Keep Zscaler for user access; use F5 to bring your legacy and on-prem apps into the same zero-trust policy and to enforce application-layer controls SSE doesn't." This maps to F5's published "dual-plane" positioning and Microsoft's Secure Hybrid Access documentation. (Confidence: medium; positioning is F5-stated and Microsoft-corroborated, but the "why keep it" ROI depends on the customer's legacy footprint — qualify it.)

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (highest rename risk in the corpus):**
- **BIG-IP Access Policy Manager (APM) → BIG-IP Zero Trust Access.** Announced at AppWorld 2026 (blog dated March 11, 2026). Confirmed **branding-only**: F5 states existing APM use cases continue; no functional removal at rename. "APM" persists in: techdocs.f5.com, release-note sections ("Access Policy Manager Fixes"), the module/SKU name (e.g., "Access Policy (APM)" provisioning; F5-ADD-BIG-USER add-on licenses), the `f5.com/products/big-ip-services/access-policy-manager` URL (which now renders the Zero Trust Access page), AWS Marketplace, and Microsoft Learn docs. Expect both names in circulation for years. Always record both.
- **"Identity Aware Proxy (IAP)," "Access Guided Configuration (AGC)," "Visual Policy Editor (VPE)"** — all current terminology on f5.com and techdocs as of mid-2026.
- **BIG-IP Next** — discontinued in 2025; intended capabilities being folded into BIG-IP TMOS (v21.x). **No BIG-IP Next APM/access module exists.** Do not reference one.
- **Competitor renames:** Cisco AnyConnect → **Cisco Secure Client** (AnyConnect remains the VPN module). Ivanti Connect Secure = formerly Pulse Connect Secure; client is **Ivanti Secure Access Client** (formerly Pulse Secure client). VMware Horizon → **Omnissa Horizon** (Broadcom spun out VMware EUC as Omnissa, 2024; KKR-backed). VMware/AirWatch appears on F5 pages as "VMware Horizon ONE (AirWatch)" — likely stale branding.

**Release anchors:** APM→Zero Trust Access rename = AppWorld 2026 (March 10–12, 2026). BIG-IP v21.1 = **GA June 4, 2026** (per DevCentral/F5 blog), delivering (in the access module) IPsec VPN tunneling, OAuth 2.0 Dynamic Client Registration (RFC 7591), PQC TLS/SSL VPN tunneling, HTTP Connector in per-session policies, and native SAML auth in Edge Client. Agent2Agent (A2A) protocol support in v21.1 is **experimental** (not production). IPsec PQC is **roadmap** ("not-too-distant future"). BIG-IP v21.1 drops support for legacy iSeries/VIPRION hardware.

**Explicitly NOT verified / do not assert:**
- Any GA F5 cloud-native/SaaS ZTNA product. XC "Universal ZTNA" / Zero Trust Domain Service is **pre–Early Access** ("will enter Early Access soon"); an XC ZTNA console tile was temporarily removed pending development. Do not claim GA.
- Head-to-head competitive "wins" vs Zscaler/Netskope/Prisma/Cloudflare/Okta/Entra — unverified; only F5's *stated* positioning is documented.
- Specific current VDI client/protocol version support — deployment guides predate Omnissa/Citrix rebrands; verify against the live APM Client Compatibility Matrix.
- Exact licensing/SKU changes (if any) tied to the rename — no evidence of SKU renaming found; module still licensed/provisioned as "APM." Treat any packaging change as unverified.

**Context note — F5 October 2025 breach (affects honest value framing):** In October 2025 F5 disclosed a nation-state breach in which attackers had **long-term access (at least 12 months per F5's SEC Form 8-K and Bloomberg, Oct 16, 2025; F5 learned of it Aug 9, 2025 and delayed disclosure at DOJ request)** and exfiltrated portions of BIG-IP source code and undisclosed-vulnerability information. Attribution to **China-nexus actor UNC5221** and the **BRICKSTORM backdoor** is per Google Threat Intelligence Group/Mandiant (Mandiant notes BRICKSTORM averages a 393-day dwell time). **CISA issued Emergency Directive ED 26-01 "Mitigate Vulnerabilities in F5 Devices" on Oct 15, 2025**, ordering federal agencies to apply updates by Oct 22 and report inventory by Oct 29, 2025; CISA Acting Director Madhu Gottumukkala warned that "these same risks extend to any organization using this technology, potentially leading to a catastrophic compromise of critical information systems." F5 states no evidence of source-code tampering or access to CRM/financial/support-case/iHealth systems, and no known critical/RCE undisclosed vulns. Relevance here: (1) BIG-IP Zero Trust Access runs on BIG-IP, so "VPN appliance CVE fatigue" arguments against Ivanti/Cisco cut both ways — use honestly; (2) it reinforces hardening of management interfaces and patch currency as part of any BIG-IP access pitch. Confidence: high (CISA, F5 SEC filing, Mandiant, multiple security vendors).

**Primary sources leaned on:** f5.com product page (BIG-IP Zero Trust Access); f5.com blog (rename announcement Mar 11 2026; v21.1 GA Jun 4 2026; v21.1 sneak peek); f5.com AppWorld press release / Business Wire (Mar 11 2026); techdocs.f5.com (BIG-IP 21.1 new features, IPsec VPN config, APM Client Compatibility Matrix, "About zero trust"); docs.cloud.f5.com (BIG-IP APM on XC; Universal ZTNA; SaaS changelog); BIG-IP APM datasheet. **Third-party corroboration:** Microsoft Learn (F5 + Entra Secure Hybrid Access); DevCentral community articles; Gartner Magic Quadrant for SSE (May 20 2025) / TrustRadius reviews; Google/Mandiant, Rapid7, CISA, Palo Alto Unit 42, Help Net Security, Bloomberg (Ivanti CVEs, F5 breach); Omnissa/Citrix/TechTarget (VDI rebrands); SSE market comparisons (lower trust).