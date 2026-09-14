# F5 AI Application Delivery & Security — Solution Area Reference (Doc 11)
doc_id: 11-ai-delivery-security
solution_area: AI Application Delivery & Security
doc_tag: AI
products_covered: F5 AI Security Platform (umbrella), F5 AI Guardrails, F5 AI Red Team, F5 AI Remediate, F5 AI Gateway, F5 NGINX (NGINX One / NGINX Plus / NGINX Open Source) MCP agentic observability, F5 BIG-IP Next for Kubernetes on NVIDIA BlueField DPUs, F5 BIG-IP / VELOS AI data delivery (S3), F5 Labs CASI/ARS leaderboards, SurePath AI (acquired)
compiled: July 2026
primary_release_anchor: F5 AI Security Platform launch + SurePath AI acquisition (June 22, 2026); prior anchors: AppWorld 2026 (March 11, 2026) and AI Guardrails/AI Red Team GA (January 14, 2026)
refresh_priority: High
last_validated: July 2026

---

## Layer 1 — Human orientation

This document covers F5's portfolio for **delivering and securing AI applications, models, and agentic traffic**. It is the fastest-moving area in the F5 corpus: F5 has made three AI-security acquisitions in roughly 18 months (LeakSignal, Feb/Mar 2025; CalypsoAI, Sept 2025; SurePath AI, June 2026) and reorganized the products under a new umbrella within that window. Treat all naming here as perishable.

**The mental model F5 itself uses** breaks into five distinct jobs, each with a different product and a different buyer:

1. **Secure the prompt/model path at runtime** — *F5 AI Guardrails* (runtime enforcement: prompt-injection, jailbreak, data-leak, toxicity, policy) and *F5 AI Gateway* (the Kubernetes-native proxy that sits inline between apps and LLM backends and also does routing, rate-limiting, PII redaction). Buyer: platform/AI engineering + CISO.
2. **Test the model before and during production** — *F5 AI Red Team* (automated adversarial testing, agent-swarm attacks, CASI/ARS risk scoring). Buyer: CISO / AppSec / AI governance.
3. **Close the loop between testing and enforcement** — *F5 AI Remediate* (turns Red Team findings into validated Guardrails packages with human approval). Buyer: SecOps / AppSec.
4. **Observe and govern AI use** — *F5 NGINX* MCP agentic observability (parses Model Context Protocol metadata in the traffic path; sanctioned vs shadow agents) and the newly acquired *SurePath AI*: network-based AI discovery plus workforce GenAI governance (role-based model access, prompt redaction, audit trails, sanctioned portal). Buyer: DevOps/SRE/platform + CISO.
5. **Deliver the AI infrastructure itself** — *BIG-IP Next for Kubernetes on NVIDIA BlueField DPUs* (GPU-cluster / AI-factory traffic, token governance, multi-tenancy) and *BIG-IP/VELOS AI data delivery* (S3 storage-path throughput). Buyer: infrastructure / AI platform engineering / neocloud providers.

As of June 22, 2026, F5 markets jobs 1–4 under the umbrella **F5 AI Security Platform** (governance, discovery, security testing, runtime protection, observability). The underlying products keep their own names. Job 5 is delivery/infrastructure, sold through the BIG-IP and NGINX lines, and is where the NVIDIA partnership lives.

**Scope boundaries (covered elsewhere):** classic API security for the APIs agents call → doc 01; bot-vs-AI-agent traffic classification (XC Bot Defense) → doc 03; general Kubernetes delivery → doc 10; observability (F5 Insight) and platform AI assistants → doc 13. These are cross-referenced but not detailed here.

**How to read Layer 2:** each capability is one self-contained record. `delivered_by` names the current F5 product(s); `attribution_confidence` flags whether the feature-to-product mapping is certain; `maturity_flag` and `source_currency_flag` flag GA vs announced and freshness. `fit_signals` are worked backward from the customer's pain to how it sounds on a call. `disqualifiers` exist to stop the downstream agent from over-fitting.

---

## Layer 2 — Capability catalog

### [AI] Inline LLM prompt/response security proxy (AI Gateway)
- solution_area:            AI Application Delivery & Security
- capability_name:          Inline LLM prompt/response security proxy (AI Gateway)
- plain_description:        A containerized, Kubernetes-native proxy that sits between applications and LLM backends (OpenAI, Azure OpenAI, Anthropic, Ollama, self-hosted models) inspecting inbound prompts and outbound responses, redacting PII, and routing/rate-limiting traffic to models.
- delivered_by:             F5 AI Gateway
- attribution_confidence:   High
- customer_problem_solved:  AI apps are non-deterministic; inputs and outputs vary and evolve, so a traditional WAF cannot tell whether a message is a prompt-injection attempt or whether a response is leaking sensitive data. Teams also need to control LLM cost and route across multiple model backends.
- fit_signals:              "We're standing up an internal chatbot/copilot and legal/security won't let it go to production." "We're calling OpenAI and Anthropic and want one control point." "We don't want prompts with customer PII leaving our network." "We need to cache and rate-limit LLM calls to control token spend." "We're running open-source models (DeepSeek, Qwen, Llama) on our own GPUs and need a proxy in front."
- disqualifiers:            Customer consumes AI only through a finished SaaS product (e.g., a vendor's copilot) with no self-hosted model and no insertion point for a proxy. No Kubernetes/container platform and no willingness to run one. Pure batch/offline inference with no request-level policy need.
- value_framing:            "The best proxy in the world for app traffic, now in front of your models." One inline enforcement point for OWASP LLM Top 10 risks, PII redaction, model routing, and cost control — deployable anywhere your models run, integrated with the F5 platform you already operate.
- product_routing_note:     Lead with AI Gateway when the customer needs an inline data-plane proxy and traffic steering/routing/caching, not just a policy engine. Where the need is purely runtime policy/guardrails across many models and environments, lead with AI Guardrails (which can run without the full gateway). The two are complementary; Guardrails enforcement can be applied at the AI Gateway insertion point.
- maturity_flag:            GA (announced GA at AppWorld, late Feb 2025; originally introduced Nov 2024)
- source_currency_flag:     Current
- source:                   f5.com AI Gateway announcement (businesswire, Nov 2024); DevOps.com AppWorld 2025 coverage; aigateway.clouddocs.f5.com (docs, Helm chart, processors); Network World "F5 gateway works to protect and manage AI applications"

### [AI] Prompt-injection, jailbreak, and OWASP LLM Top 10 detection
- solution_area:            AI Application Delivery & Security
- capability_name:          Prompt-injection, jailbreak, and OWASP LLM Top 10 detection
- plain_description:        Detects and optionally blocks prompt-injection, jailbreak, insecure output handling, model denial-of-service, sensitive-information disclosure, and model-theft attempts against LLM-backed apps.
- delivered_by:             F5 AI Gateway (Prompt Injection processor); F5 AI Guardrails (runtime adversarial-threat protection)
- attribution_confidence:   High
- customer_problem_solved:  LLMs can be manipulated by crafted inputs to ignore system instructions, exfiltrate data, or produce harmful output; traditional network/WAF controls do not operate at the semantic layer where these attacks occur.
- fit_signals:              "Someone on the team demoed a jailbreak of our chatbot." "We're worried a user could trick the model into revealing its system prompt or another customer's data." "Security review flagged prompt injection as a blocker." "Our retrieved documents (RAG) could carry hidden instructions."
- disqualifiers:            No LLM/generative feature in production or planned. AI use is entirely a third-party SaaS where the customer cannot insert inspection. (Note: the AI Gateway Prompt Injection processor only supports English-language prompts as documented — flag this limitation for multilingual deployments.)
- value_framing:            An inline, model-agnostic inspection layer that treats AI threats the way enterprise security has always treated network threats — with enforceable, auditable policy — inbound (before the model sees the prompt) and outbound (before the user sees the response). In SecureIQLab 2026 WAAP validation, integrating F5 AI Guardrails into F5 WAAP raised measured LLM security effectiveness from 19% to 97%, blocking 95% of prompt injection (LLM01) and 100% of improper output handling (LLM05).
- product_routing_note:     If the customer wants this at the traffic-proxy/data-plane layer, AI Gateway. If they want it as a model-agnostic runtime policy layer spanning many models/clouds with explainability and audit trails, AI Guardrails. Both draw on F5 Labs' threat library.
- maturity_flag:            GA
- source_currency_flag:     Current
- source:                   aigateway.clouddocs.f5.com/processors/prompt-injection.html; f5.com/products/ai-guardrails; f5.com blog "Independent tests reveal F5 provides strong protection" (SecureIQLab); F5 AI Guardrails/Red Team GA press release (Jan 14, 2026)

### [AI] Runtime AI guardrails (model-agnostic policy enforcement)
- solution_area:            AI Application Delivery & Security
- capability_name:          Runtime AI guardrails (model-agnostic policy enforcement)
- plain_description:        A model-agnostic runtime security layer that enforces consistent policy across every AI model, app, and agent in any cloud or deployment environment — blocking adversarial threats, preventing data leakage, moderating harmful/biased/toxic output, and constraining agent tool calls and privileges.
- delivered_by:             F5 AI Guardrails (CalypsoAI heritage)
- attribution_confidence:   High
- customer_problem_solved:  Enterprises run many models (proprietary, open-source, fine-tuned variants) across many environments; each carries a different risk profile and model-provider safety filters are inconsistent and not portable. Regulated industries also need explainability and audit trails for why a prompt was allowed or blocked.
- fit_signals:              "We have models from three different providers plus some open-source ones and no consistent policy across them." "Compliance wants an audit trail of every AI interaction for the EU AI Act / GDPR / HIPAA." "We need to run this on-prem or air-gapped." "We're giving agents tool access and worry about excessive agency / privilege escalation." "We need PII, PCI, and PHI guardrails on day one."
- disqualifiers:            Single-model, single-cloud deployment fully covered by the provider's own filters and with no compliance/audit driver. No production AI. AI fully outsourced with no enforcement insertion point.
- value_framing:            Write your governance policy once and enforce it consistently across every model, cloud, and agent — with explainability ("why was this blocked?") and audit-ready templates for GDPR, HIPAA, and the EU AI Act. Full functionality on-prem and fully air-gapped. In independent SecureIQLab WAAP testing, F5 AI Guardrails blocked 97% of all LLM attacks.
- product_routing_note:     Lead product for CISO/AI-governance buyers who care about policy consistency, explainability, and compliance across a heterogeneous model estate. Pairs with AI Red Team (testing) and AI Remediate (loop closure). Delivered as part of the F5 AI Security Platform umbrella (June 2026).
- maturity_flag:            GA (January 14, 2026)
- source_currency_flag:     Current
- source:                   f5.com/products/ai-guardrails; f5.com press release "F5 accelerates AI security with integrated runtime protection" (Jan 14, 2026); f5.com/company/blog/what-are-ai-guardrails

### [AI] Automated adversarial AI testing / red-teaming
- solution_area:            AI Application Delivery & Security
- capability_name:          Automated adversarial AI testing / red-teaming
- plain_description:        Automated, scalable adversarial testing that unleashes swarms of autonomous agents to simulate thousands of attack patterns against a customer's specific model/app/agent deployment, producing risk-scored, explainable findings.
- delivered_by:             F5 AI Red Team (CalypsoAI heritage)
- attribution_confidence:   High
- customer_problem_solved:  Manual red-teaming cannot keep pace with monthly model updates and the explosion of attack techniques; security teams lack time to probe obscure, worst-case exploits before models reach production.
- fit_signals:              "We don't have a full-time AI red team." "Every time we update the model we're not sure what new vulnerabilities we introduced." "We need evidence of testing for a model-risk sign-off / model card." "We want to compare model providers on security before we pick one."
- disqualifiers:            No self-managed or customer-specific model deployment to test (pure consumption of a locked SaaS). Organization with no AI governance mandate and no production AI plans.
- value_framing:            A continuous "eye in the sky" that runs the industry's threat library (10,000+ new attack patterns added monthly) against your actual deployment, finds where a breach would hurt most, and converts each finding into an enforceable guardrail — moving you from "we hope it's safe" to "we tested it."
- product_routing_note:     Lead for CISO/AppSec buyers focused on assurance and model selection. Findings feed AI Remediate → AI Guardrails. The public-facing model rankings are the F5 Labs CASI/ARS leaderboards (separate record).
- maturity_flag:            GA (January 14, 2026)
- source_currency_flag:     Current
- source:                   f5.com/products/ai-red-team; f5.com press release (Jan 14, 2026); f5.com/company/blog/what-are-ai-guardrails; SecureIQLab AI Guardrails efficacy report (f5.com/go/report/f5-ai-guardrails-efficacy-test) — 19,679 real-world attack simulations across 10 attack categories, testing conducted entirely by SecureIQLab with no F5 involvement in test design or execution

### [AI] Test-to-enforcement loop closure (AI Remediate)
- solution_area:            AI Application Delivery & Security
- capability_name:          Test-to-enforcement loop closure (AI Remediate)
- plain_description:        Bridges the gap between vulnerabilities found by AI Red Team and runtime protections enforced by AI Guardrails, by automatically creating, optimizing, and validating targeted guardrail packages — with a human-approval step before they go live.
- delivered_by:             F5 AI Remediate
- attribution_confidence:   High
- customer_problem_solved:  Even when teams find AI vulnerabilities, translating findings into coordinated, enforceable runtime controls lags behind because it is manual and fragmented, leaving exposure windows open.
- fit_signals:              "We find issues in testing but it takes weeks to actually enforce a fix." "We want remediation but we're not comfortable auto-deploying policy without human review." "Our red-team findings and our runtime controls live in different tools."
- disqualifiers:            Customer does not own both the testing (Red Team) and enforcement (Guardrails) halves — Remediate is the connective tissue between them and has little standalone value without both. No production AI.
- value_framing:            Close the loop from "found a risk" to "enforced a fix" in hours instead of weeks — evidence-backed guardrail packages, deployed with human approval, without disrupting live AI apps.
- product_routing_note:     Only routes when AI Red Team and AI Guardrails are both in play (or being sold together). Not a standalone lead. Capture maturity precisely: announced at AppWorld 2026 (March 11, 2026); treat as newest of the CalypsoAI-heritage line.
- maturity_flag:            Roadmap/Announced → likely GA/early (announced at AppWorld March 11, 2026 as "new to the F5 ADSP"; public sources describe it as launched but do not give an explicit standalone GA date — flag as not fully confirmed)
- source_currency_flag:     Current
- source:                   businesswire "F5 Advances Enterprise Application Security for the AI and Post-quantum Era" (March 11, 2026); Network World "F5 brings new visibility and AI controls" (March 2026); SiliconANGLE AppWorld 2026 coverage

### [AI] Agentic observability via MCP traffic parsing
- solution_area:            AI Application Delivery & Security
- capability_name:          Agentic observability via MCP traffic parsing
- plain_description:        NGINX parses and inspects Model Context Protocol (MCP) metadata directly in the traffic path to surface per-agent request patterns, latency, throughput, and error signals — giving visibility into both sanctioned and shadow AI-agent activity without deploying a separate AI gateway.
- delivered_by:             F5 NGINX (MCP traffic visibility GA in NGINX Open Source; enterprise support and advanced capabilities via F5 NGINX Plus, part of NGINX One)
- attribution_confidence:   High
- customer_problem_solved:  Autonomous AI agents generate a new class of traffic traditional tools cannot parse; teams cannot tell what agents are doing, which are sanctioned, or where they're calling — a visibility and governance gap.
- fit_signals:              "We can't see what our AI agents are actually doing." "Developers are spinning up agents and we don't know which are sanctioned." "We need per-agent latency/error metrics." "We already run NGINX in front of our apps and don't want to add another gateway."
- disqualifiers:            No agentic/MCP traffic in the environment. No NGINX in the traffic path and no willingness to introduce it. Need for deep network-wide AI discovery beyond the NGINX data path (that is SurePath AI territory — see separate record).
- value_framing:            Because NGINX already sits in a privileged spot in your traffic path, you get agent visibility — sanctioned and shadow — from the gateway you already run, with no separate AI gateway and less tool sprawl.
- product_routing_note:     Lead for DevOps/SRE/platform buyers who already run NGINX. For enterprise support/SLA, position NGINX Plus / NGINX One. For network-wide (not just NGINX-path) AI discovery and intent classification, route to SurePath AI / the AI Security Platform discovery pillar. Note BIG-IP v21.1 also adds MCP protection + session persistence (separate delivery vehicle).
- maturity_flag:            GA (MCP traffic visibility GA in NGINX Open Source, announced AppWorld March 11, 2026; enterprise via NGINX Plus)
- source_currency_flag:     Current
- source:                   businesswire/f5.com "F5 strengthens its ADSP..." (March 11, 2026); Network World "F5 brings new visibility and AI controls to Big-IP, NGINX"; f5.com/products/nginx/nginx-plus

### [AI] Network-based AI discovery, intent classification & shadow-AI detection
- solution_area:            AI Application Delivery & Security
- capability_name:          Network-based AI discovery, intent classification & shadow-AI detection
- plain_description:        Inline/out-of-band inspection of corporate network traffic to discover every AI app, agent, and MCP tool call (sanctioned or not), classify usage by intent, and detect shadow AI — integrating with existing SASE, DLP, SIEM, and identity systems. Deploys via network redirects and out-of-band analysis, with no changes to existing application architectures and no direct app integrations required.
- delivered_by:             SurePath AI (acquired by F5, announced June 22, 2026; positioned as the "AI discovery" pillar of the F5 AI Security Platform)
- attribution_confidence:   Medium (capability and acquisition confirmed via primary F5 sources; exact final product name/branding post-integration and GA state not yet established in public sources)
- customer_problem_solved:  Enterprises cannot govern AI they cannot see; employees and agents use unsanctioned AI tools ("shadow AI"), creating data-leak and compliance risk that endpoint/app-level tools miss.
- fit_signals:              "We have no idea how many AI tools our employees are using." "Security wants to detect and control shadow AI without breaking sanctioned use." "We want to steer agents to approved destinations." "We need this to plug into our existing SASE/DLP/SIEM, not replace it." "Agentless on managed devices is a requirement."
- disqualifiers:            Organization with tight, fully-inventoried AI usage and no shadow-AI concern. No corporate network insertion point (fully remote SaaS consumption outside managed network). Customers wanting only in-app runtime enforcement rather than discovery.
- value_framing:            You can't secure what you can't see — continuous, network-based discovery of every AI app, agent, and MCP tool call, feeding directly into testing (Red Team) and enforcement (Guardrails) so discovery, testing, and enforcement form one adaptive loop.
- product_routing_note:     New (June 2026). Route to CISO/network-security buyers who lead with a visibility/shadow-AI problem. Distinct from NGINX MCP observability (which is scoped to the NGINX traffic path); SurePath is network-wide and integrates with SASE/DLP/SIEM. Pair with the workforce-governance record below (find shadow use → govern it). Note: SurePath's pre-acquisition SaaS remains live (surepath.ai, now bannered "part of F5") — the Roadmap/Announced flag refers to its F5-integrated form. Treat naming and packaging as unsettled; verify current SKU before quoting.
- maturity_flag:            Roadmap/Announced (acquisition announced June 22, 2026; terms undisclosed; integration in progress; no public GA milestone)
- source_currency_flag:     Possibly stale (fast-moving; verify post-acquisition status and branding)
- source:                   F5 press release/blog "F5 Launches AI Security Platform..." and SurePath AI acquisition (June 22, 2026); surepath.ai (product site, live under "part of F5" banner, July 2026); Security Boulevard / Help Net Security / GeekWire coverage (June 2026); stocktitan.net FFIV news

### [AI] Workforce GenAI usage governance (sanctioned-use enablement, redaction, private-model access)
- solution_area:            AI Application Delivery & Security
- capability_name:          Workforce GenAI usage governance (sanctioned-use enablement, redaction, private-model access)
- plain_description:        Governs how employees use generative AI: role-based access policies to public and private models, detection and redaction of sensitive data in prompts, recording of interactions for audit, and a branded enterprise GenAI portal — enabling safe sanctioned use instead of blanket blocking.
- delivered_by:             SurePath AI (acquired by F5, announced June 22, 2026; positioned within the F5 AI Security Platform — post-acquisition naming/packaging unsettled)
- attribution_confidence:   High for the capabilities as documented in SurePath's own public product materials; Medium for how they will surface as F5 features/SKUs post-integration
- customer_problem_solved:  Blanket-blocking GenAI drives usage underground (shadow AI) while unmanaged use leaks sensitive data; organizations need to channel employees to sanctioned public/private models with policy, redaction, and audit trails.
- fit_signals:              "Employees are pasting customer data into ChatGPT." "We blocked AI tools and people just work around it." "We want to give staff a sanctioned AI portal instead of saying no." "Legal/compliance wants every AI interaction recorded and auditable." "We're standing up private models and need role-based access for employees." "We need group-based policies for who can use which model."
- disqualifiers:            No workforce GenAI usage concern (purely customer-facing AI apps — route to the AI Gateway / AI Guardrails records); organizations wanting only coarse network blocking (a SWG/DNS filter may suffice); the need is securing the customer's own LLM applications rather than employee use of AI tools.
- value_framing:            "Don't just find shadow AI — replace it. Route employees to approved models with the data protection and audit trail your compliance team needs, so 'yes, safely' beats 'no.'" (SurePath's own pre-acquisition framing: "GenAI is already in your workplace. We'll help you find it, secure it, and make it work for you.")
- product_routing_note:     Pair with the network-based discovery record above (find shadow use → govern it). Boundary with siblings: F5 AI Gateway and AI Guardrails secure the customer's *own* AI applications and model paths; this capability governs *employee* use of GenAI tools and internal models. Capabilities are documented from SurePath's pre-acquisition public materials — verify current F5 packaging/naming before quoting.
- maturity_flag:            GA as SurePath's pre-acquisition SaaS (product site live, SOC 2 noted); Roadmap/Announced as an F5-integrated offering (no public F5 GA/packaging statement as of July 2026)
- source_currency_flag:     Possibly stale (fast-moving post-acquisition; verify)
- source:                   surepath.ai (product site: policy-driven guardrails, sensitive-data redaction, private-model access, audit trails, enterprise portal; "now a part of F5" banner); f5.com press release "F5 Launches AI Security Platform..." (June 22, 2026); GeekWire (June 2026, company background)

### [AI] Unified AI security platform (governance + discovery + testing + runtime + observability)
- solution_area:            AI Application Delivery & Security
- capability_name:          Unified AI security platform (governance + discovery + testing + runtime + observability)
- plain_description:        An umbrella offering that unifies F5's AI-security products into one continuous loop — AI governance, AI discovery, AI security testing, AI runtime protection, and AI observability — so discovery feeds testing, testing feeds enforcement, and enforcement feeds the next round of discovery.
- delivered_by:             F5 AI Security Platform (umbrella over F5 AI Guardrails, F5 AI Red Team, AI Remediate/auto-remediation, and SurePath AI discovery)
- attribution_confidence:   High (that the umbrella exists and unifies these components); Medium on exact component boundaries and which SKUs are bundled vs sold separately
- customer_problem_solved:  AI security has been a patchwork of point tools (red-team consultancies, gateway startups, DLP, monitoring); enterprises want fewer consoles, fewer gaps, and one operational model spanning discovery-to-enforcement.
- fit_signals:              "We've been evaluating five different AI-security point tools." "The board wants one story for enterprise AI risk." "We want testing and runtime enforcement to actually talk to each other." "We need governance, discovery, testing, and runtime in one platform."
- disqualifiers:            Customer needs only one narrow capability (e.g., just a gateway proxy, or just model testing) and has no appetite for a platform. Very small AI footprint. Fully outsourced AI.
- value_framing:            One adaptive platform for enterprise AI risk — see it (discovery), test it (red team), enforce it (guardrails), prove it (observability/audit) — built on 30 years of application-layer expertise and F5's WAAP stack, deployable on-prem, air-gapped, hybrid, or public cloud. F5 states the platform stress-tests against more than 140,000 attack patterns and cites up to 98.2% runtime security efficacy in independent testing.
- product_routing_note:     Umbrella framing for CISO-level conversations. For an engineer with one concrete pain, route to the specific component instead. Do not overstate bundling — components retain their own names and (in some cases) separate purchase paths; verify packaging.
- maturity_flag:            Roadmap/Announced (platform launched June 22, 2026; component products Guardrails/Red Team are GA; no explicit platform-level GA/pricing statement in public sources)
- source_currency_flag:     Possibly stale (very recent; verify)
- source:                   F5 press release/blog "F5 Launches AI Security Platform to Put Security Leaders in Control of Enterprise AI Risk" (June 22, 2026); businesswire; stocktitan.net FFIV

### [AI] AI model risk benchmarking (CASI / ARS leaderboards)
- solution_area:            AI Application Delivery & Security
- capability_name:          AI model risk benchmarking (CASI / ARS leaderboards)
- plain_description:        Publicly published, monthly-updated benchmarks — the Comprehensive AI Security Index (CASI) and Agentic Resistance Score (ARS) — that rank prominent AI models on security resilience, performance, risk-to-performance ratio, and cost of security, drawn from F5's AI vulnerability library.
- delivered_by:             F5 Labs (CASI/ARS leaderboards); the same agentic red-teaming is available tailored to a customer's environment via F5 AI Red Team
- attribution_confidence:   High
- customer_problem_solved:  Model providers publish their own safety notes but enterprises lack an independent, consistent yardstick to compare model risk before selecting and deploying a model.
- fit_signals:              "How do we choose which model is safest for production?" "We need an independent security benchmark to justify our model choice to risk/compliance." "We want to track whether our chosen model is getting more or less secure over time."
- disqualifiers:            Model choice already locked and immovable; no governance requirement to justify it. No production AI.
- value_framing:            A monthly, evidence-based "report card" for model security — so model selection is a documented risk decision, not a vendor-marketing bet — and the same testing engine can be pointed at your own deployment via AI Red Team.
- product_routing_note:     Use as a door-opener / credibility asset with CISO and AI-governance buyers; it is threat-intelligence content, not a sold product. Converts naturally into an AI Red Team engagement.
- maturity_flag:            GA (live, updated monthly)
- source_currency_flag:     Current
- source:                   f5.com/labs/casi; f5.com/company/blog/introducing-the-casi-leaderboard; f5.com press release "F5 Labs sets new standard for AI security benchmarking"

### [AI] AI-factory / GPU-cluster traffic delivery on DPUs
- solution_area:            AI Application Delivery & Security
- capability_name:          AI-factory / GPU-cluster traffic delivery on DPUs
- plain_description:        A Kubernetes-native traffic-management and security layer that runs natively on NVIDIA BlueField DPUs, offloading networking, TLS/encryption, AI-aware load balancing, and traffic management off host CPUs/GPUs to raise token throughput, cut latency, and enable secure multi-tenant GPU infrastructure.
- delivered_by:             F5 BIG-IP Next for Kubernetes (deployed on NVIDIA BlueField-3 DPUs; expansion to BlueField-4 announced for gigascale)
- attribution_confidence:   High
- customer_problem_solved:  Large-scale AI training/inference strains traditional network infrastructure; GPUs sit idle waiting on data-path work, and cloud/GPU providers need secure multi-tenancy and token-level governance to monetize shared infrastructure.
- fit_signals:              "We're building our own GPU cluster / AI factory / sovereign AI environment." "We're a neocloud / GPU-as-a-service provider and need multi-tenant isolation." "Our GPUs are underutilized and cost per token is too high." "We need token governance / chargeback per tenant." "We run inference on Kubernetes and want to offload networking to DPUs."
- disqualifiers:            Customer consumes AI from public cloud APIs and owns no GPU infrastructure. No Kubernetes / no NVIDIA BlueField DPUs. Small-scale experimentation not yet at production/factory scale.
- value_framing:            Treat token production as a measurable business metric — offload the data path to BlueField DPUs so GPUs do only inference, raising GPU yield and lowering cost per token with no model changes, plus secure multi-tenancy and token governance for shared AI platforms. F5-validated (Tolly Group) on BlueField-3: up to 40% higher token throughput, 61% faster time-to-first-token, 34% lower latency. Announced BlueField-4 expansion targets +30% token-generation capacity and multi-tenant networking at speeds up to 800 Gb/s.
- product_routing_note:     Buyer is infrastructure / AI-platform engineering and, distinctively, neocloud/GPU-cloud providers and service providers — not the CISO or app team. Requires NVIDIA BlueField DPU hardware; this is a joint F5–NVIDIA motion (GTC / AI Factory validated design). Verify BlueField-3 vs BlueField-4 scope per deal.
- maturity_flag:            GA on BlueField-3 (GA announced 2025; enhanced capabilities announced March 17, 2026); BlueField-4 expansion Announced (roadmap, gigascale)
- source_currency_flag:     Current
- source:                   f5.com/products/big-ip/next/kubernetes-on-nvidia-bluefield-dpu; f5.com press release "F5 and NVIDIA advance AI factory economics" (March 17, 2026); f5.com/company/news/press-releases/f5-gigascale-ai-nvidia-bluefield-4-dpus; NVIDIA developer blog (SoftBank PoC); clouddocs.f5.com/bigip-next-for-kubernetes

### [AI] High-throughput AI data delivery for S3 storage
- solution_area:            AI Application Delivery & Security
- capability_name:          High-throughput AI data delivery for S3 storage
- plain_description:        Using BIG-IP (and VELOS/rSeries hardware) as an application delivery controller in front of S3-compatible object storage to load-balance and secure the data path for AI training, fine-tuning, and RAG pipelines — optimizing throughput, DNS/health-based routing, TLS offload, and DDoS/WAF protection.
- delivered_by:             F5 BIG-IP (LTM, DNS, AFM, Advanced WAF, DDoS Hybrid Defender); F5 VELOS / rSeries hardware; integrations with S3-compatible stores (Dell ObjectScale, MinIO, NetApp StorageGRID, Scality RING)
- attribution_confidence:   High
- customer_problem_solved:  AI pipelines need high-throughput, low-latency, resilient access to object storage; bottlenecks in storage networking leave expensive GPUs idle and pipelines fragile, and storage endpoints need protection from malicious traffic and poisoning.
- fit_signals:              "Our GPUs are starving because the storage data path is a bottleneck." "We standardized on S3-compatible object storage (MinIO/Dell/NetApp/Scality) for AI data." "We need to secure and load-balance traffic to our datasets across sites." "We're moving huge training datasets across hybrid/multicloud and throughput is inconsistent."
- disqualifiers:            No self-managed storage data path (fully managed cloud storage with provider-handled delivery). No large-scale training/RAG ingestion need. This is largely a repositioning of established BIG-IP ADC capabilities for the AI storage use case — flag that it is delivery/performance, not AI-specific security intelligence.
- value_framing:            An ADC in front of your object store is a control point that protects stores from surges, smooths throughput to keep GPUs fed, and centralizes TLS/DDoS/WAF and governance across hybrid multicloud S3. In SecureIQLab validated testing (published April 2, 2026), in a high-latency SD-WAN multicloud scenario (75 ms latency, 2 ms jitter), F5 VELOS with BIG-IP LTM in front of a MinIO cluster increased S3 throughput from 9.5 Gbps to 41.2 Gbps — a 332% improvement.
- product_routing_note:     Infrastructure/storage-architect buyer. Lead with BIG-IP/VELOS where the customer already has an F5 footprint or needs terabit-scale hardware. Note this leans on partner storage ecosystems; much of the capability is mature ADC function applied to S3 (new S3-tuned TCP/SSL profiles in BIG-IP v21.0). Do not oversell as novel AI security.
- maturity_flag:            GA (S3-specific profiles in BIG-IP v21.0, late 2025; partner validations 2025–2026)
- source_currency_flag:     Current
- source:                   f5.com/solutions/use-cases/ai-data-delivery; f5.com/company/blog/fueling-the-ai-data-pipeline-with-f5-and-s3-compatible-storage; f5.com press release "F5 and Scality expand partnership" (Feb 2026); f5.com/go/report SecureIQLab MinIO validation (April 2, 2026)

### [AI] AI data-in-transit leak detection & PII redaction
- solution_area:            AI Application Delivery & Security
- capability_name:          AI data-in-transit leak detection & PII redaction
- plain_description:        Inline classification of AI prompts and responses to detect and redact/block/log sensitive data (PII, financial data, PHI, source code, proprietary content) before it leaves approved environments, using a real-time data-classification engine.
- delivered_by:             F5 AI Gateway (data leakage detection & prevention, powered by technology from the LeakSignal acquisition); related BIG-IP SSL Orchestrator AI data protection for encrypted-traffic visibility
- attribution_confidence:   High
- customer_problem_solved:  When AI apps touch real data, prompts and responses can leak PII/PHI/IP; teams need inline, policy-driven redaction and an audit trail without relying on external proxies or endpoint agents.
- fit_signals:              "We can't let customer PII or source code end up in a prompt to an external model." "Compliance needs proof that sensitive data is redacted before it leaves." "We need to detect sensitive data in AI responses, not just requests." "We're worried about data leaking to external AI over encrypted channels."
- disqualifiers:            No sensitive data in AI interactions. AI fully offline/air-gapped with no egress concern already handled by other DLP. Customer with mature dedicated DLP covering AI paths and no gateway insertion point.
- value_framing:            A real-time data-classification engine embedded where prompts and responses actually flow — redact or block sensitive data inline, log every transformation for audit, and write the policy once for consistent enforcement across environments.
- product_routing_note:     Ties to AI Gateway as the insertion point; the underlying tech came from F5's Feb/Mar 2025 LeakSignal acquisition (now integrated, not sold as "LeakSignal"). For shadow-AI/egress visibility across encrypted traffic, BIG-IP SSL Orchestrator is the vehicle. Confirm current feature availability per release.
- maturity_flag:            GA (data leakage detection & prevention added to AI Gateway, 2025; SSL Orchestrator AI data protection announced with planned availability late 2025 — verify)
- source_currency_flag:     Current
- source:                   f5.com/company/blog/ai-gateway-receives-new-data-leakage-detection-and-prevention-functionality; f5.com press release "...Data Leakage Detection and Prevention for Securing AI Workloads"; f5.com/company/blog/strengthening-data-protection-and-governance-for-ai-applications (LeakSignal)

---

## Layer 3 — Product routing logic and pitch support

### 3a. Product routing

**Start from the customer's dominant pain and footprint, then map to the product:**

- **"We're deploying an internal LLM app/copilot and security is blocking us."** → Lead with **AI Gateway** (inline proxy: prompt-injection, PII redaction, routing) and/or **AI Guardrails** (runtime policy + explainability + compliance). If they're pre-production and want assurance, add **AI Red Team**. If regulated (finance/healthcare), lead with Guardrails' EU AI Act/PII/PHI compliance framing.
- **"We can't see what our AI agents are doing."** → If they already run **NGINX**, lead with **NGINX MCP agentic observability** (fastest, no new gateway). If the need is network-wide shadow-AI discovery across SASE/DLP/SIEM, route to **SurePath AI** / the AI Security Platform discovery pillar.
- **"Employees are using unsanctioned AI tools / pasting data into chatbots."** → **SurePath AI**: discovery to find the shadow use, then the workforce-governance capabilities (role-based model access, prompt redaction, audit trails, sanctioned portal) to channel it. Capabilities documented from pre-acquisition SurePath materials — verify F5 packaging before quoting (acquired June 22, 2026).
- **"We're building GPU infrastructure / an AI factory / we're a neocloud."** → **BIG-IP Next for Kubernetes on NVIDIA BlueField DPUs.** This is an infrastructure sale requiring BlueField hardware; different buyer (platform/infra), different motion (joint with NVIDIA).
- **"Our GPUs starve on the storage path / we standardized on S3."** → **BIG-IP / VELOS AI data delivery.** Mature ADC capability repositioned for AI; storage-architect buyer.
- **"We need one platform for enterprise AI risk."** → **F5 AI Security Platform** umbrella (governance + discovery + testing + runtime + observability). CISO-level. Drill into components for engineers.

**By footprint:**
- *Existing NGINX / NGINX One customer:* MCP agentic observability and AI Gateway (Kubernetes-native) are the lowest-friction entry points.
- *Existing BIG-IP customer:* AI data delivery (S3), BIG-IP v21.1 MCP protection, and BIG-IP Next for Kubernetes extend a trusted footprint; the CalypsoAI-heritage AI security products layer on top via ADSP.
- *Greenfield / no F5 footprint:* AI Guardrails + AI Red Team are model- and infrastructure-agnostic and can land without an existing F5 data plane; AI Gateway needs a container platform.
- *Deployment preference:* on-prem/air-gapped strongly favors F5 (Guardrails runs fully air-gapped) vs cloud-only competitors. SaaS-only shops with no insertion point are weak fits for the inline products.

**Coexistence / migration notes:** AI Gateway and AI Guardrails overlap on prompt-injection/data-leak detection — position AI Gateway as the data-plane proxy (routing, caching, PII) and Guardrails as the model-agnostic runtime policy/enforcement + explainability layer; they are complementary, not either/or. NGINX MCP observability and SurePath AI both address "agent visibility" but at different scopes (NGINX traffic path vs network-wide discovery) — do not present them as interchangeable. Where the public record doesn't clearly state official routing (e.g., exact bundling within the AI Security Platform, standalone SKU status of AI Remediate, or whether AI Gateway sits formally inside the AI Security Platform umbrella), say so rather than inventing F5 guidance.

### 3b. Disqualifiers / anti-patterns (aggregate)

- **No AI in production and none planned.** The entire solution area is not yet relevant; revisit later.
- **AI fully outsourced to a SaaS vendor with no self-hosted model and no gateway/network insertion point.** Inline products (AI Gateway, Guardrails runtime, data-leak redaction) have nowhere to sit. SurePath-style network discovery may still apply if traffic crosses the corporate network — confirm.
- **No Kubernetes / container platform and unwilling to adopt one** → AI Gateway (Kubernetes-native) is a poor fit; consider Guardrails or NGINX-path options instead.
- **Single model, single cloud, fully covered by provider filters, no compliance/audit driver** → Guardrails' model-agnostic and explainability value is muted.
- **No GPU infrastructure owned** → BIG-IP Next for Kubernetes on DPUs and S3 data delivery are irrelevant; these are for builders/operators of AI infrastructure.
- **Customer wants only one narrow capability and rejects a platform** → sell the single component; do not push the umbrella.
- **Multilingual prompt-injection requirement** → note the AI Gateway Prompt Injection processor is documented as English-only; flag as a gap.
- **AI Remediate without both Red Team and Guardrails** → little standalone value.

### 3c. Competitive positioning and objection handling (all lower confidence)

*All competitive claims below are lower-confidence and should be verified before use on a call; this market consolidates fast.*

**Category 1 — LLM security / guardrail vendors.** This category has consolidated aggressively into platform players, which is itself a differentiator F5 can cite ("point tools are being absorbed; buy the platform"):
- **Protect AI → Palo Alto Networks** (acquisition completed July 2025, ~$634.5M final consideration per PANW filings; now part of Prisma AIRS). *Lower confidence.*
- **Robust Intelligence → Cisco** (acquired, reported ~$400M, 2024). *Lower confidence.*
- **Prompt Security → SentinelOne** (acquisition completed Sept 5, 2025, ~$133.6M cash plus stock/options; folded into Singularity). *Lower confidence.*
- **Lakera → Check Point** (acquired 2025). *Lower confidence.*
- **HiddenLayer** (independent pure-play as of last public reporting — verify). *Lower confidence.*
F5's stated differentiators (public evidence): model-agnostic runtime enforcement across any cloud incl. fully air-gapped; explainability/audit trails for regulated industries; the CalypsoAI-heritage vulnerability library (10,000+ new attack patterns/month) feeding a closed discover→test→enforce loop; and integration with F5's existing WAAP/API-security/DDoS stack so AI security sits alongside app security. F5 also emphasizes inference-layer protection (vs training-model focus) — Maddison publicly claimed CalypsoAI "won out on inference security" in head-to-head evaluations (vendor claim, not independent).

**Category 2 — AI gateways.** Kong AI Gateway, Portkey, LiteLLM, cloud-provider AI gateways (Cloudflare AI Gateway, Google Apigee/Vertex, AWS), Envoy AI Gateway, TrueFoundry. These emphasize multi-LLM routing, caching, token budgeting, observability; guardrail depth varies. F5's differentiator is coupling gateway function with enterprise-grade security (OWASP LLM Top 10, LeakSignal-derived data-leak redaction) and the broader ADSP/WAAP platform, plus air-gapped/on-prem deployment. *Note:* Kong's own benchmarks (self-published) claim large throughput advantages over Portkey/LiteLLM — cite only as vendor-sourced. F5 does not publicly publish head-to-head gateway throughput vs these, so avoid unverifiable performance claims.

**Category 3 — doing it in-app with framework guardrails** (NeMo Guardrails, native SDK guardrails, provider moderation endpoints). F5's counter: framework/in-app guardrails are inconsistent across teams and models, hard to audit centrally, and don't give a single enforcement/observability plane; an inline, model-agnostic layer enforces policy once across the whole estate.

**Objection: "Our LLM provider already has safety filters."**
Response (supported by public F5 evidence): Provider filters are a baseline tuned to the *provider's* compliance obligations and risk appetite, not your enterprise's use cases, data definitions, or regulatory obligations — and they don't extend across the other models you run. Per the F5 AI Guardrails product page: "In recent SecureIQLab testing of foundational models' built-in guardrails against sophisticated AI attacks, roughly 13% of attacks were successfully blocked." By contrast, F5's own SecureIQLab WAAP validation reports that adding F5 AI Guardrails raised LLM security effectiveness from 19% to 97% (95% of prompt injection, 100% of improper output handling). Provider filters also give you no consistent cross-model audit trail, no explainability for *why* something was blocked, no on-prem/air-gapped option, and no control over data redaction before prompts leave your environment. F5 AI Guardrails is model-agnostic, enforces your policy consistently across every model and cloud, and produces the audit trail regulated industries need. (Cite only the SecureIQLab figures F5 publicly states; do not claim a specific head-to-head "win" against a named competitor beyond published data.)

---

## Appendix — Naming, currency & confidence ledger

**Perishable naming to watch (verify on every refresh):**
- **F5 AI Security Platform** — umbrella launched June 22, 2026; unifies Guardrails + Red Team + AI Remediate/auto-remediation + SurePath AI discovery under governance/discovery/testing/runtime/observability pillars. Component products retained their own names at launch. Verify whether F5 later collapses component names into the platform brand.
- **SurePath AI** — acquired June 22, 2026 (terms undisclosed; Denver-based, founded 2023, ~19 employees, ~$6M raised, CEO Casey Bleeker, per GeekWire). Post-integration product name/branding and GA state NOT yet established in public sources. The pre-acquisition SaaS and product site remain live (surepath.ai, bannered "SurePath AI is now a part of F5") and document both discovery and workforce-governance capabilities — covered as two Layer 2 records. Verify SKU before quoting.
- **F5 AI Guardrails / F5 AI Red Team** — CalypsoAI heritage (acquisition completed ~late Sept 2025; ~$180M). GA January 14, 2026. Names unchanged as of June 2026 (High confidence).
- **F5 AI Remediate** — announced AppWorld March 11, 2026. Standalone GA date not explicitly confirmed in public sources; described as "new to the F5 ADSP."
- **F5 AI Gateway** — GA since ~Feb 2025 (introduced Nov 2024). Note: the June 2026 AI Security Platform launch materials prominently named Guardrails, Red Team, and SurePath but did NOT prominently name "AI Gateway"; its exact relationship to the new umbrella is not clearly established in public sources. Do not conflate with F5's separate "API Gateway." Verify.
- **BIG-IP Next for Kubernetes (on NVIDIA BlueField-3, expanding to BlueField-4)** — name stable; verify DPU generation per deal.
- **BIG-IP Zero Trust Access** — formerly BIG-IP Access Policy Manager (APM); renamed at AppWorld 2026 (adjacent; see doc 07, Access & Zero Trust).
- **CASI / ARS leaderboards** — F5 Labs (CalypsoAI heritage); CASI = Comprehensive AI Security Index, ARS = Agentic Resistance Score.

**Explicitly NOT verified (do not assert):**
- Whether F5 AI Gateway is formally inside the F5 AI Security Platform umbrella or positioned separately.
- Standalone GA date and pricing/packaging of F5 AI Remediate.
- SurePath AI post-integration name, GA date, and pricing.
- Any head-to-head performance or efficacy "win" of F5 vs a named competitor beyond figures F5/SecureIQLab/Tolly publicly state.
- Current independence of HiddenLayer and any other unlisted guardrail vendors as of mid-2026.
- Exact current version/feature scope of AI Gateway beyond documented changelog entries (Core images up to ~v1.3.0 observed in public docs; verify latest).
- The minor discrepancy between F5's "up to 98.2%" (platform launch) and "98.3%"/"97%" (AI Guardrails page / WAAP test) efficacy figures — treat all as F5-cited SecureIQLab numbers, context-dependent, not a single fixed benchmark.

**Primary sources leaned on:** f5.com product pages (AI Gateway, AI Guardrails, AI Red Team, BIG-IP Next for Kubernetes on BlueField, AI data delivery, AI Security Platform); f5.com press releases and corporate blog; aigateway.clouddocs.f5.com and clouddocs.f5.com (docs/changelogs); f5.com/labs (CASI/ARS); f5.com/go/report SecureIQLab validations; businesswire and F5 investor releases; NVIDIA developer blog. **Third-party reality-checks:** Network World, SiliconANGLE, DevOps.com, Dark Reading, Help Net Security, Fierce Network, CRN; SEC filings (Palo Alto/Protect AI, SentinelOne/Prompt Security) for competitor consolidation; Kong/Spheron/APIScout for AI-gateway competitive landscape (vendor/SEO — low trust).
