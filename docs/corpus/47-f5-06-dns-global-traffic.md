# F5 DNS & Global Traffic Management (GSLB) — Solution Area Reference (Doc 06)

doc_id: 06-dns-global-traffic
solution_area: DNS & Global Traffic Management (GSLB)
doc_tag: DNS
products_covered: BIG-IP DNS (formerly GTM), F5 Distributed Cloud DNS, F5 Distributed Cloud DNS Load Balancer, BIG-IP Next DNS CNF (service-provider, cross-ref doc 12)
compiled: July 2026
primary_release_anchor: F5 AppWorld 2026 (March 11, 2026) Distributed Cloud packaging changes; BIG-IP 17.5.x / 21.0 release train
refresh_priority: High
last_validated: July 2026

---

## Layer 1 — Human orientation

This document covers F5's DNS delivery and DNS-based global traffic steering. Two problems live here: (1) **authoritative DNS** — answering DNS queries at scale, securely; and (2) **GSLB (Global Server Load Balancing)** — using DNS answers to steer users to the best/closest/healthiest site across data centers and clouds, and to fail traffic over during outages. GSLB decides *which site's IP* to return; the local load balancer at that site then distributes traffic across servers — that local load balancing belongs to **doc 05**, not here.

F5 delivers this story through two main products with very different delivery models:

- **BIG-IP DNS** (renamed from **BIG-IP GTM / Global Traffic Manager** around v11.5; the "GTM" name is still ubiquitous on customer calls — record both). This is the on-prem/self-managed module: hardware appliance, virtual edition, or cloud-native. It owns GSLB "wide IPs," DNS Express (in-memory authoritative DNS), DNSSEC signing, a DNS firewall (with BIG-IP AFM), and hyperscale query performance. It is the incumbent in most existing F5 estates.
- **F5 Distributed Cloud DNS** (SaaS primary/secondary authoritative DNS) and **F5 Distributed Cloud DNS Load Balancer** (SaaS GSLB). Both run on F5's global anycast network, configured from the Distributed Cloud (XC) Console. These are the cloud-native/managed answer, best for multicloud and DevOps-driven teams. "XC" is common shorthand.

A hybrid pattern is explicitly supported and F5-documented: **BIG-IP DNS as hidden primary, XC DNS as authoritative secondary** — giving on-prem control of records plus cloud-scale resilience and DDoS absorption.

**How to read the rest:** Layer 2 is the capability catalog — one self-contained record per capability, each tagged `[DNS]`, each restating which F5 product delivers it and a confidence flag. Layer 3 is routing logic (which product to lead with), an aggregate disqualifier list, and bounded competitive/objection handling (including the "Route 53 already does this" objection). An appendix tracks perishable naming and what could not be verified. **Treat product attribution as the highest-value output; naming as the most perishable.**

---

## Layer 2 — Capability catalog

### [DNS] GSLB / intelligent global traffic steering (wide IPs)
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: GSLB / intelligent global traffic steering
- plain_description: Returns different DNS answers to different users so they reach the best data center or cloud region, based on health, location, latency, capacity, or business policy. In BIG-IP DNS this is configured as a "wide IP" (a FQDN mapped to pools of virtual servers across sites).
- delivered_by: BIG-IP DNS (wide IPs, pools, topology records); F5 Distributed Cloud DNS Load Balancer (SaaS GSLB with load-balancing rules and geo-proximity)
- attribution_confidence: High
- customer_problem_solved: Users hit a slow, distant, or failed site; no automated way to send traffic to the best-performing or geographically appropriate location across multiple data centers/clouds.
- fit_signals: "We have two (or three) data centers and no smart way to send users to the right one." "Our failover is a manual DNS change we make by hand." "We're active/passive and want active/active." "Users in Europe are hitting our US site." "We spun up a second region in AWS/Azure and need to split traffic." Mentions of GDPR/data-residency steering. Mentions of "GTM wide IPs" (existing F5 shop).
- disqualifiers: Single site / single region with no failover requirement. Purely internal app with one IP. Team only needs local server load balancing (that's doc 05). Latency-sensitive steering better solved at the anycast/network layer (doc 09).
- value_framing: "Turn DNS into an availability and performance control point — automatically send every user to the site that's up and closest, and fail whole sites over without a human touching a record at 2 a.m."
- product_routing_note: Existing BIG-IP/on-prem estate or need for deep policy/iRules control → BIG-IP DNS. Cloud-native/multicloud, DevOps pipeline, no appliances → XC DNS Load Balancer. See Layer 3a.
- maturity_flag: GA (both)
- source_currency_flag: Current
- source: f5.com/solutions/use-cases/global-server-load-balancing-gslb; f5.com/products/big-ip-services/big-ip-dns; techdocs.f5.com BIG-IP GTM Configuration (wide IPs); f5.com/products/distributed-cloud-services/dns-load-balancer

### [DNS] Disaster recovery / site failover
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: DR / automated site failover
- plain_description: Detects when a data center or app is down via health monitoring and automatically redirects DNS answers to a healthy/backup site, so users keep getting served.
- delivered_by: BIG-IP DNS (Active/Active, Active/Passive, Active/DR-Only site options; whole-site or per-app failover); F5 Distributed Cloud DNS Load Balancer (automatic primary-site failure detection, zero-touch failover to recovery instances)
- attribution_confidence: High
- customer_problem_solved: Outages cause downtime because failover is manual, slow, error-prone, or untested; business-continuity/DR requirements aren't met.
- fit_signals: "Our last DR test failed / took hours." "Failover is a runbook someone runs manually." "We have a DR site that just sits there and we're not sure it works." "We need active/passive or active/DR-only." "Compliance/auditors want a tested failover." "We had an outage and couldn't shift traffic fast enough." Often surfaces after a painful incident.
- disqualifiers: No secondary/DR site exists (nothing to fail over to). RTO is met by lower layers (e.g., in-region cloud AZ failover handled by a cloud LB). Application state can't tolerate DNS-TTL-bound failover timing (DNS failover is not instantaneous — see caveats).
- value_framing: "Make failover automatic and provably reliable — fail an entire site or just one affected app, without manual DNS edits, and stop dreading the DR test."
- product_routing_note: Existing BIG-IP estate / on-prem control → BIG-IP DNS site options (Active/Active, Active/Passive, Active/DR-Only); cloud-native or multicloud with no appliances → XC DNS Load Balancer zero-touch failover (see Layer 3a). SE caveat: DNS-based failover is TTL-bound; clients/resolvers cache answers, so cutover is not instant.
- maturity_flag: GA (both)
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/big-ip-dns (Active/Active, Active/Passive, Active/DR Only); f5.com/products/distributed-cloud-services/dns-load-balancer (zero-touch failover); community.f5.com "Using Distributed Cloud DNS Load Balancer with Geo-Proximity and failover scenarios"

### [DNS] Authoritative DNS at scale (DNS Express / hyperscale)
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: High-performance authoritative DNS
- plain_description: Answers DNS queries authoritatively at very high volume. BIG-IP DNS's "DNS Express" loads zones into memory (via zone transfer from a primary) and answers from RAM, absorbing spikes and floods.
- delivered_by: BIG-IP DNS (DNS Express in-memory engine; multicore scaling; IP Anycast integration); F5 Distributed Cloud DNS (SaaS primary/secondary authoritative DNS on global anycast, auto-scaling)
- attribution_confidence: High
- customer_problem_solved: Legacy BIND/on-prem DNS can't scale to query spikes or DDoS volumes; DNS becomes a bottleneck or single point of failure for every app. Per F5's Intelligent DNS Scale white paper, "BIND typically scales to only 50,000 responses per second (RPS), making it vulnerable to both legitimate and malicious DNS surges."
- fit_signals: "Our DNS falls over under load / during attacks." "We're still running BIND and it doesn't scale." "DNS is a bottleneck." "We need to offload/mask our back-end DNS." Service-provider/large-enterprise query volumes (see doc 12 cross-ref). "We want DNS caching to cut latency."
- disqualifiers: Small zone, low query volume, no performance pain. Team only needs internal name resolution for a handful of records. Full DDI lifecycle management need (Infoblox/BlueCat territory — see Layer 3c).
- value_framing: "Make DNS a hardened, hyperscale front door instead of a fragile dependency — answer from memory, survive spikes and floods, and shrink DNS latency." Performance envelope: BIG-IP DNS "hyperscales authoritative DNS up to 100 million query responses per second (RPS)" with a fully loaded chassis (Rapid Response Mode on 5050s and above adds "up to 200 percent of normal max query RPS"; Virtual Edition scales in increments of 250,000 RPS). Per F5's Intelligent DNS Scale white paper, "each BIG-IP device can answer approximately 125,000 to 200,000 requests per second, scaling up to more than 50 million query RPS, greater than 12 times the capacity of a typical primary DNS server."
- product_routing_note: On-prem/high-RPS/appliance → BIG-IP DNS with DNS Express. SaaS/global/no-infrastructure → XC DNS. Service-provider cloud-native → BIG-IP Next DNS CNF (doc 12).
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com "Configuring DNS Express"; f5.com/products/big-ip-services/big-ip-dns (100M RPS, DNS Express >50M RPS); F5 Intelligent DNS Scale white paper; BIG-IP DNS datasheet (RRM, VE increments); f5.com/products/distributed-cloud-services/dns

### [DNS] DNSSEC signing and validation
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: DNSSEC
- plain_description: Cryptographically signs DNS responses so resolvers can verify they're authentic and unaltered, preventing spoofing/cache poisoning. Note DNSSEC signs but does not encrypt.
- delivered_by: BIG-IP DNS (real-time signing incl. for GSLB answers; ZSK/KSK management; FIPS/HSM via Thales; ECDSA support); F5 Distributed Cloud DNS (built-in signing + automated key management/rollover for primary zones; DS record export; preserves BIG-IP-signed zones when XC is secondary)
- attribution_confidence: High
- customer_problem_solved: DNS hijacking/cache-poisoning risk; compliance mandates requiring signed DNS; difficulty deploying/maintaining DNSSEC and key rollover.
- fit_signals: "We have a compliance/regulatory requirement for DNSSEC." "We're worried about DNS spoofing/cache poisoning." "DNSSEC key management is painful." "Auditors flagged our DNS." Government/finance/critical-infrastructure buyers.
- disqualifiers: No compliance driver and low threat concern. Team conflates DNSSEC with encryption (they may actually want DoH/DoT — different capability). Note: traditional DNSSEC and dynamic GSLB answers are in tension; F5 signs GSLB responses in real time, which is a differentiator but adds complexity.
- value_framing: "Get signed, tamper-evident DNS — including for your GSLB answers — with key management handled for you, so compliance and anti-spoofing are covered without a DNSSEC science project." For key custody, per the F5 BIG-IP DNS Service Provider datasheet: "You can use BIG-IP DNS with FIPS cards that provide 140-2 support for securing your [DNSSEC] keys."
- product_routing_note: On-prem signing authority / FIPS-HSM requirement → BIG-IP DNS. SaaS-managed signing with automated rollover → XC DNS. Hybrid: BIG-IP signs as hidden primary, XC serves signed zone as secondary (signatures preserved).
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com "Configuring DNSSEC"; community.f5.com "The BIG-IP GTM: Configuring DNSSEC"; f5.com/company/blog "Secure hybrid enterprise DNSSEC with F5 Distributed Cloud DNS"; BIG-IP DNS datasheet and Service Provider datasheet (FIPS 140-2 / Thales HSM)

### [DNS] DNS DDoS / DNS firewall protection
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: DNS-specific DDoS / DNS firewall
- plain_description: Protects DNS infrastructure from volumetric floods (UDP floods, NXDOMAIN floods, amplification/reflection) and malformed packets, and can block queries to malicious domains via reputation feeds (RPZ / SURBL / Spamhaus).
- delivered_by: BIG-IP DNS (DNS firewall services; combined with BIG-IP AFM for volumetric protection; Response Policy Zones); F5 Distributed Cloud DNS / DNS Load Balancer (built-in L7 DNS DDoS absorption on anycast network)
- attribution_confidence: High (note: full volumetric DNS DDoS on BIG-IP is delivered *with* AFM — attribution split noted)
- customer_problem_solved: DNS is a favored DDoS target; an unprotected DNS layer takes down every dependent service.
- fit_signals: "We've been hit by DNS floods / amplification attacks." "Our DNS is exposed and we're worried about DDoS." "We want to block malware domains at the DNS layer." Post-incident conversations.
- disqualifiers: General/non-DNS DDoS protection need → that's doc 04. Pure recursive-resolver security/filtering at branch/endpoint (BlueCat Edge / Infoblox territory). Note the scope boundary: this record is DNS-flood-specific only.
- value_framing: "Keep DNS answering through an attack — absorb DNS floods and block malicious domains so an attack on DNS doesn't cascade into a full outage."
- product_routing_note: On-prem, needs AFM for full volumetric coverage → BIG-IP DNS + AFM. SaaS with attack absorption on F5's network → XC DNS. Broader DDoS story → cross-ref doc 04.
- maturity_flag: GA
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/big-ip-dns; BIG-IP DNS datasheet; f5.com Service Provider BIG-IP DNS datasheet; f5.com/products/distributed-cloud-services/dns

### [DNS] Encrypted DNS (DoH / DoT / ODoH)
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Encrypted DNS transport
- plain_description: Terminates and resolves DNS over HTTPS (DoH) and DNS over TLS (DoT) so DNS queries/responses can't be read or tampered with in transit; newer BIG-IP adds Oblivious DoH (ODoH).
- delivered_by: BIG-IP DNS (DoH/DoT without impacting RPS; ODoH via HPKE and SVCB/HTTPS RR support added in 17.5.x train)
- attribution_confidence: Medium (DoH/DoT High for BIG-IP; ODoH tied to specific 17.5.x release — confirm version. XC encrypted-transport support not separately verified here — do not assert for XC.)
- customer_problem_solved: Plaintext DNS leaks user activity and is an on-path tamper/amplification vector; browsers push DoH that bypasses enterprise DNS controls.
- fit_signals: "Browsers are doing their own DoH and bypassing our DNS." "We need to terminate encrypted DNS." "Privacy/regulatory requirement to encrypt DNS." Service-provider last-mile privacy concerns.
- disqualifiers: No privacy/encryption requirement. Team actually needs DNSSEC (authenticity, not confidentiality) — different capability.
- value_framing: "Take back control of encrypted DNS — terminate DoH/DoT at your edge so you keep visibility and policy while meeting privacy requirements."
- product_routing_note: Lead with BIG-IP DNS; do not attribute ODoH to XC without verification.
- maturity_flag: GA (DoH/DoT); ODoH GA in BIG-IP 17.5.x (confirm exact build)
- source_currency_flag: Current
- source: f5.com/products/big-ip-services/big-ip-dns; BIG-IP DNS datasheet; sysin.org BIG-IP 17.5.x release notes (ODoH/HPKE/SVCB)

### [DNS] Hybrid DNS: BIG-IP DNS primary + XC DNS secondary
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Hybrid on-prem/SaaS DNS resilience
- plain_description: Run on-prem BIG-IP DNS as a hidden primary (source of truth for records) and F5 Distributed Cloud DNS as the internet-facing authoritative secondary, receiving records by zone transfer (AXFR/IXFR, TSIG-secured) — combining on-prem control with cloud scale, anycast reach, and DDoS absorption.
- delivered_by: BIG-IP DNS (hidden primary, DNSSEC signing authority) + F5 Distributed Cloud DNS (authoritative secondary); can also run in reverse (XC primary, BIG-IP failover)
- attribution_confidence: High (publicly documented pattern with step-by-step F5 KB and DevCentral articles)
- customer_problem_solved: Want cloud DNS resilience/scale but must keep record control on-prem for security/compliance; want a backup path if either SaaS or on-prem DNS is unavailable.
- fit_signals: "We want cloud DNS but can't give up on-prem control." "We need a secondary DNS provider for resilience/regulatory redundancy." "We already run GTM and want to add cloud scale/DDoS protection." "We want to migrate to cloud DNS gradually."
- disqualifiers: Greenfield with no on-prem DNS (just use XC primary). No BIG-IP DNS footprint and no desire for one. Note: GSLB wide-IP config does NOT sync via zone transfer between BIG-IP and XC — only standard records and DNSSEC records transfer; wide-IP/GSLB parity requires API/scripting (documented limitation).
- value_framing: "Best of both: keep your records and DNSSEC signing on-prem, put a global, attack-absorbing anycast secondary in front of them, and gain a mutual failover path."
- product_routing_note: This is the flagship coexistence story for existing BIG-IP DNS shops adding cloud. Lead BIG-IP DNS as primary; position XC DNS as the secondary add-on.
- maturity_flag: GA
- source_currency_flag: Current
- source: my.f5.com KB K000147071 "How to set up F5 Distributed Cloud DNS as Secondary for BIG-IP DNS (GTM)"; community.f5.com "The Power of &: F5 Hybrid DNS solution"; f5.com/company/blog "Fortifying DNS Resilience and Performance with Hybrid Architecture"; f5.com/company/blog "Secure hybrid enterprise DNSSEC with F5 Distributed Cloud DNS"

### [DNS] Geo-proximity / data-residency steering
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Geolocation / geo-proximity routing
- plain_description: Routes users to a specific region's instance based on their location — for latency (nearest site) or for keeping user data region-specific (e.g., GDPR), with catch-all rules for overflow/DR.
- delivered_by: F5 Distributed Cloud DNS Load Balancer (geo-proximity rules, EDNS client-subnet aware); BIG-IP DNS (topology records, proximity-based load balancing)
- attribution_confidence: High
- customer_problem_solved: Need to reduce latency by locality and/or enforce data-residency/compliance by keeping EU users on EU infrastructure.
- fit_signals: "We need to keep EU user data in the EU." "GDPR/data-sovereignty requirement." "Users should hit the closest region." "We want to silo traffic by geography."
- disqualifiers: Single-region footprint. No latency or residency concern. Network-layer anycast already solves proximity (doc 09).
- value_framing: "Steer users by geography for speed and compliance at once — EU users stay on EU infrastructure, everyone hits their nearest site, and overflow still has a home."
- product_routing_note: Cloud/multicloud → XC DNS Load Balancer (rule-based, EDNS subnet). On-prem/existing GTM → BIG-IP DNS topology records.
- maturity_flag: GA
- source_currency_flag: Current
- source: community.f5.com "Using Distributed Cloud DNS Load Balancer with Geo-Proximity and failover scenarios"; community.f5.com "F5 XC Distributed Cloud DNS GSLB implementing Split-DNS"; f5.com/solutions/use-cases/global-server-load-balancing-gslb

### [DNS] Application health monitoring for steering decisions
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Health-aware GSLB monitoring
- plain_description: Continuously checks the health of sites/apps/servers (aggregating multiple monitors, 18+ out-of-box app monitors like SAP/Oracle/LDAP/mySQL) so GSLB only returns answers pointing to healthy resources.
- delivered_by: BIG-IP DNS (multi-level monitors, out-of-box app health checks, integrates with LTM); F5 Distributed Cloud DNS Load Balancer (health checks to origins/pool members; additional health checks are a metered add-on)
- attribution_confidence: High
- customer_problem_solved: DNS keeps handing out addresses of dead/degraded resources because it has no view of app health; false positives cause needless failovers.
- fit_signals: "DNS keeps sending users to servers that are actually down." "We get false-positive failovers." "We need app-aware, not just ping, health checks." "We want to check SAP/Oracle/DB health before routing."
- disqualifiers: Static single endpoint. No failover/steering in play. Simple TCP-port check already sufficient and provided by existing tooling.
- value_framing: "Only ever hand out an address that's actually working — deep, aggregated health checks stop DNS from sending users into a black hole."
- product_routing_note: Depth of monitors and app-specific checks favor BIG-IP DNS; XC provides health checks natively as a managed service (watch the per-health-check metering).
- maturity_flag: GA
- source_currency_flag: Current
- source: BIG-IP DNS datasheet (18+ app monitors); cdw.com F5-XC-O-ADN-DNS-HC (XC additional health check SKU); f5.com/products/distributed-cloud-services/dns-load-balancer

### [DNS] Cloud migration / gradual traffic shifting
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Weighted / ratio traffic shifting for migration
- plain_description: Uses weighted or ratio load-balancing across pools/sites to move a controlled percentage of traffic from one environment to another (e.g., data center → cloud) gradually, and roll back fast if something breaks.
- delivered_by: BIG-IP DNS (ratio/weighted load-balancing methods on wide-IP pools); F5 Distributed Cloud DNS Load Balancer (load-balancing rules with scores/priorities)
- attribution_confidence: Medium (capability is real via LB methods; "migration use case" framing is F5-consistent but is an applied pattern, not a single named feature)
- customer_problem_solved: Big-bang cloud cutovers are risky; teams want to canary a small slice of production traffic to a new environment and scale up as confidence grows.
- fit_signals: "We're migrating to the cloud and don't want a big-bang cutover." "We want to send 5% of traffic to the new region and ramp." "We need to be able to roll back fast." "Lift-and-shift in progress."
- disqualifiers: No migration underway. Cutover already handled by a service-mesh/ingress canary at L7 (doc 05/09). Instant rollback required (DNS TTL caching limits this).
- value_framing: "De-risk your cloud migration — shift traffic a slice at a time by DNS weight, watch it, and roll back in a TTL if needed."
- product_routing_note: Existing GTM → BIG-IP DNS ratio methods. Cloud-native migration → XC DNS Load Balancer scored rules.
- maturity_flag: GA
- source_currency_flag: Current
- source: techdocs.f5.com BIG-IP GTM (load balancing methods, ratio/persistence); community.f5.com XC DNS LB split-DNS/scoring article

### [DNS] Service-provider / carrier-scale DNS (cross-reference)
- solution_area: DNS & Global Traffic Management (GSLB)
- capability_name: Carrier-grade / cloud-native DNS (brief)
- plain_description: DNS delivery for telco/ISP/5G scale, including caching resolvers, DNS64, and DNS acceleration, delivered as Kubernetes-native cloud-native network functions.
- delivered_by: BIG-IP Next DNS CNF (F5BigDnsApp — resolution, caching, DNS64); BIG-IP DNS service-provider edition (NAPTR, 3G/4G/5G 3GPP, IPv6/DNS64)
- attribution_confidence: High
- customer_problem_solved: Service providers need hyperscale, low-latency DNS in cloud-native 5G core architectures with horizontal scaling.
- fit_signals: "We're a carrier/ISP building 5G standalone core." "We need cloud-native DNS on Kubernetes/OpenShift." "N6/SGi-LAN DNS." "Subscriber-scale DNS caching."
- disqualifiers: Enterprise (non-carrier) use — use BIG-IP DNS or XC. This record is a pointer only.
- value_framing: (Cross-reference — see doc 12 for the service-provider story.)
- product_routing_note: **Keep brief — full service-provider DNS treatment belongs to doc 12.** Route carrier opportunities there.
- maturity_flag: GA (CNF 2.0 GA 2025)
- source_currency_flag: Current
- source: f5.com/products/big-ip/next/cloud-native-network-functions; f5.com Service Provider BIG-IP DNS datasheet; community.f5.com BIG-IP Next CNF; cross-ref doc 12

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Lead with BIG-IP DNS (formerly GTM) when:**
- The customer already runs BIG-IP (LTM/AFM/APM) — GSLB provisions as a module and reuses existing health monitors, iRules, and management. Highest-probability signal.
- On-prem or hardware/virtual-edition preference; data-sovereignty or air-gapped constraints on where DNS records live.
- Deep policy customization needed (iRules on DNS, complex topology, ratio/persistence tuning).
- FIPS/HSM DNSSEC key handling required (Thales HSM integration).
- Very high authoritative RPS on-prem (DNS Express in-memory, up to 100M RPS on fully loaded chassis per F5 datasheet).

**Lead with F5 Distributed Cloud DNS / DNS Load Balancer when:**
- Cloud-native/multicloud footprint; no appetite to run appliances.
- DevOps-driven team wanting API/Terraform-style config and fast provisioning.
- Global reach and built-in anycast DDoS absorption wanted as a service.
- Buyer wants OpEx/consumption pricing, not appliance CapEx.
- Distinguish the two XC products: **XC DNS** = authoritative primary/secondary DNS hosting; **XC DNS Load Balancer** = the GSLB/traffic-steering layer (geo-proximity, health-based failover). A customer wanting steering needs the DNS Load Balancer; a customer just wanting managed authoritative DNS needs XC DNS.

**Coexistence / migration:**
- The documented flagship hybrid is **BIG-IP DNS (hidden primary) + XC DNS (authoritative secondary)** via TSIG-secured zone transfer — the natural expansion path for existing GTM shops adding cloud resilience without ripping anything out.
- **Caveat for the SE:** GSLB **wide-IP configuration does not transfer** between BIG-IP DNS and XC via zone transfer (wide IPs are non-standard records). Only standard DNS records and DNSSEC records sync. Achieving GSLB parity across both requires API automation/scripting — set this expectation explicitly.

**Where the public record is thin (do not overstate):** F5's public materials do not give a crisp official decision tree for "when XC DNS Load Balancer should replace BIG-IP DNS GSLB" versus coexist. Treat replace-vs-coexist as a discovery conversation, not settled F5 guidance.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **Pure DDI requirement (DNS + DHCP + IPAM lifecycle management).** This is **Infoblox / BlueCat** territory, not F5. F5 BIG-IP DNS does GSLB and authoritative DNS delivery; it is **not** a DDI platform and has no DHCP/IPAM. If the customer's core need is IP address management, DHCP, and centralized DNS record administration across the enterprise, F5 is the wrong lead — at most it integrates alongside (F5 GSLB with Infoblox as hidden primary is a documented pattern). Do not position F5 as a DDI replacement.
- **Single site, single region, no failover need.** GSLB/DR value collapses to near zero.
- **They only need local server load balancing.** That's doc 05 (LTM / local traffic).
- **General (non-DNS) DDoS.** That's doc 04.
- **Multicloud network fabric / connectivity.** That's doc 09.
- **Recursive-resolver security / endpoint DNS filtering at branches.** Closer to BlueCat Edge / Infoblox / Cisco Umbrella than to F5's authoritative+GSLB story.
- **Instant, zero-loss failover expectation.** DNS-based failover is TTL-bound and never instantaneous (clients/resolvers cache); if the RTO is sub-second, DNS steering alone won't meet it — flag honestly.
- **Tiny zone, low volume, no performance/security pain.** Cloud registrar DNS or a basic managed DNS is cheaper and sufficient.

### 3c. Competitive positioning & objection handling (BOUNDED — all lower confidence)

*All competitive claims below are lower-confidence and market-perishable; verify at deal time. This market consolidates quickly.*

**Managed/cloud DNS (AWS Route 53, Azure DNS, Google Cloud DNS, Cloudflare, IBM NS1 Connect).**
- Reality check: these are strong, cheap, and "good enough" for many GSLB-lite needs (weighted, latency, geo, failover routing). NS1 is now **IBM NS1 Connect** — IBM signed the definitive agreement to acquire NSONE, Inc. on February 28, 2023 and closed the acquisition in Q1 2023 (March 31, 2023 per PitchBook), with NS1 folded into IBM Software. Verify independence status in any deal (no longer a standalone startup).
- F5's defensible differentiators (public-evidence-based, not head-to-head "wins"): consistent policy/steering across **on-prem + multicloud + hybrid** (not locked to one cloud); deep, app-aware aggregated health checks; real-time DNSSEC signing of GSLB answers; and the hybrid on-prem-primary/cloud-secondary architecture. Cloud-vendor DNS is strongest when the customer is all-in on that one cloud; F5's angle is heterogeneity and control.

**"Route 53 health checks already give us this" (address specifically).**
- Acknowledge: yes, Route 53 does DNS-based GSLB — health checks, failover, latency/geo/weighted routing — and it's inexpensive and highly available. For an AWS-centric shop, it is often genuinely sufficient. Don't pretend otherwise.
- Then probe where Route 53 is weaker: (1) **it's AWS-centric** — steering consistently across other clouds and on-prem data centers, with one policy model, is exactly F5's multicloud/hybrid story; (2) **health-check depth** — Route 53 health checks are HTTP/HTTPS/TCP with calculated checks; BIG-IP DNS aggregates multiple monitors and ships 18+ app-specific monitors (SAP/Oracle/LDAP/DB), reducing false failovers; (3) **failover latency** — both are TTL/propagation-bound, and per NGINX's own Route 53 GSLB deployment guide "it can take up to three minutes for Route 53 to begin routing traffic to another region" with "a built-in limitation" of roughly two minutes regardless of TTL; F5 gives finer control (ratio, persistence, topology, iRules) and on-prem control of records; (4) **DNSSEC + GSLB together** and on-prem/FIPS key custody. Frame it as: "If you're 100% AWS and your health needs are simple, Route 53 is fine. The moment you have a second cloud, a data center, deep app health, or record-custody/compliance needs, that's where F5 earns its place." (Confidence: medium — Route 53 feature specifics from AWS/NGINX docs; positioning is directional.)

**Legacy GSLB appliances (Citrix/NetScaler GSLB).**
- Naming: "Citrix ADC" is now **NetScaler**, owned by **Cloud Software Group** (post-2022 Citrix/TIBCO take-private). Verify branding when a customer says "Citrix GSLB."
- NetScaler GSLB is a credible incumbent doing DNS-subzone-delegated GSLB with proximity/active-passive. F5's differentiators are directional: DNS Express hyperscale, breadth of health monitors, real-time DNSSEC, and the SaaS/hybrid options. Avoid unverifiable "we're faster" claims. (Confidence: low.)

**DDI vendors (Infoblox, BlueCat) — adjacent, different problem.**
- These solve **DNS/DHCP/IPAM lifecycle management**, not GSLB/traffic steering. They are frequently **complementary, not competitive**: a documented pattern is Infoblox as hidden primary/DDI system-of-record with **F5 GSLB delegated a subzone** for intelligent steering. Third-party comparisons note F5 "is not the best for DDI/DNS security" because it isn't a DDI product — that's expected and fine. Do not try to win a DDI bake-off with F5; instead position coexistence. (Confidence: medium — F5+Infoblox integration white papers are primary F5 sources.)

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify every cycle):**
- **GTM → BIG-IP DNS.** Renamed ~v11.5; "GTM" still dominant in customer/field speech and in config paths (`DNS >> GSLB`). Always record both.
- **XC DNS vs XC DNS Load Balancer.** Two distinct SaaS products: XC DNS = authoritative primary/secondary DNS hosting; XC DNS Load Balancer = SaaS GSLB. Don't conflate.
- **AppWorld 2026 packaging shift (March 11, 2026).** F5 introduced **Essentials** and **Enterprise** starter packages for Distributed Cloud Services; per the AppWorld press release they "simplify subscriptions while reducing friction and replacing dozens of SKUs with value-driven bundles" (with IDC's Paul Nicholson quoted; BIG-IP v21.1 GA "targeted for the second quarter of calendar year 2026"). The standalone **product marketing pages for XC DNS and XC DNS Load Balancer remain live (©2026)**, so the product *names* persist, but *commercial buying* shifted toward the two bundles plus consumption/add-on SKUs.
- **NS1 → IBM NS1 Connect** (acquired Q1 2023). **Citrix ADC → NetScaler** (Cloud Software Group). Verify both at deal time.
- **BIG-IP Next / CNF** branding for cloud-native and service-provider DNS (doc 12).
- BIG-IP software train: 17.5.x is the current LTS-era branch; **21.0** has shipped in the release matrix. GSLB/GTM remains a provisioned module across these.

**Explicitly NOT verified (do not assert):**
- Whether DNS or DNS Load Balancer / GSLB is an **explicit named line item inside the Essentials or Enterprise bundle** feature table — could not be confirmed in public sources. The full "Compare F5 Distributed Cloud Services" table and base-package datasheet were not fully machine-readable. DNS appears to remain associated with separate consumption/add-on SKUs. **Treat bundle-inclusion of DNS as unverified.**
- Whether **XC DNS supports encrypted DNS transport (DoH/DoT/ODoH)** the way BIG-IP DNS does — not verified; do not attribute to XC.
- Exact BIG-IP build where **ODoH** became GA (tied to 17.5.x train per third-party release-notes source; confirm on techdocs.f5.com).
- Precise, current list pricing for XC DNS / DNS Load Balancer — public pages show no list price; reseller/marketplace SKUs (e.g., per-record F5-XC-O-ADN-DNS-LB, per-health-check F5-XC-O-ADN-DNS-HC) are indicative only and contract-dependent.

**Primary F5 sources leaned on:** f5.com product pages (BIG-IP DNS; XC DNS; XC DNS Load Balancer; enterprise-dns; GSLB use case); techdocs.f5.com (DNS Express, DNSSEC, GTM config); my.f5.com KB K000147071; f5.com blogs (hybrid DNS resilience; hybrid DNSSEC); BIG-IP DNS datasheets (enterprise + service provider); F5 Intelligent DNS Scale white paper; docs.cloud.f5.com (XC DNS zone management); f5.com AppWorld 2026 press release + Distributed Cloud packaging blog.
**Third-party sources (competitive reality-check, lower trust):** AWS re:Post / docs.nginx.com (Route 53 GSLB behavior & TTL/propagation limits); PeerSpot (F5 vs Infoblox/BlueCat); Gartner Peer Insights (DDI market); Network World (IBM/NS1); Wikipedia/NetScaler (Citrix→NetScaler/Cloud Software Group); endoflife.date & WorldTech IT (BIG-IP release matrix); CDW/AWS Marketplace (XC SKUs).
**Confidence posture:** Feature/attribution claims for BIG-IP DNS and XC DNS/DNS-LB are High and primarily F5-sourced. Competitive claims are all lower-confidence and directional. Packaging/pricing is the most perishable element after naming.