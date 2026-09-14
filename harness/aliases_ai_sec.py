"""
Alias table for category 11 (AI Delivery & Security), derived from 12-alias-table.md
and doc 11 Layer 3c. Corpus compiled July 2026.

Scoring rules (KB 3.4 / alias table):
  Full 1.0      current F5 name, or any alias with "F5" in the same sentence
  Partial 0.5   F5-owned product name with no F5 attribution in the sentence (bare NGINX)
  Contextual .25 mention only in negative / historical / "alternatives to" framing
  stale_name    former or acquired name used as current (CalypsoAI, SurePath, LeakSignal)
  inaccurate    recommends discontinued BIG-IP Next (ADC line) as go-forward; scores 0
"""
import re

# --- F5 -------------------------------------------------------------------
# Each pattern is matched case-insensitively with word boundaries.
# kind: "full"   -> Full regardless of attribution (name itself is unambiguously F5)
#       "attrib" -> Full only if "F5" in the same sentence; otherwise ignored (too generic)
#       "partial"-> Full if F5 in sentence, else Partial (F5-owned but independently known)
#       "stale"  -> Full/Partial by attribution rule, plus stale_name flag
F5_ALIASES = [
    (r"F5\s+AI\s+Gateway", "full"),
    (r"F5\s+AI\s+Guardrails?", "full"),
    (r"F5\s+AI\s+Red\s+Team", "full"),
    (r"F5\s+AI\s+Remediate", "full"),
    (r"F5\s+AI\s+Security\s+Platform", "full"),
    (r"F5\s+Distributed\s+Cloud", "full"),
    (r"F5\s+XC\b", "full"),
    (r"F5\s+NGINX", "full"),
    (r"F5\s+Labs", "full"),
    (r"Comprehensive\s+AI\s+Security\s+Index", "full"),
    (r"Agentic\s+Resistance\s+Score", "full"),
    (r"BIG-?IP(?!\s+Next\b)", "full"),          # BIG-IP alone = Full; BIG-IP Next handled separately
    (r"BIG-?IP\s+Next\s+for\s+Kubernetes", "full"),
    (r"\bF5\b(?!\s*(key|button))", "full"),        # bare parent brand
    (r"\bAI\s+Guardrails?\b", "attrib"),
    (r"\bAI\s+Red\s+Team\b", "attrib"),
    (r"\bAI\s+Remediate\b", "attrib"),
    (r"\bCASI\b", "attrib"),
    (r"\bNGINX(?:\s+(Plus|One|Open\s+Source|OSS))?\b", "partial"),
    (r"\bCalypso\s?AI\b", "stale"),
    (r"\bSure\s?Path(?:\s+AI)?\b", "stale"),
    (r"\bLeak\s?Signal\b", "stale"),
    (r"\bVolterra\b", "stale"),
]

# Recommending the discontinued BIG-IP Next ADC line. Excludes the active Kubernetes/CNF products.
INACCURATE_PATTERNS = [
    r"BIG-?IP\s+Next(?!\s+(for\s+Kubernetes|CNFs?|SPK))",
]

# Sentence-level markers that turn a mention Contextual (negative/historical/alternatives framing).
CONTEXTUAL_MARKERS = [
    r"\bnot\b", r"\bno longer\b", r"\bhistorically\b", r"\bwas\b", r"\bwere\b", r"\bformerly\b",
    r"\balternatives? to\b", r"\binstead of\b", r"\brather than\b", r"\blacks?\b", r"\bdoesn'?t\b",
    r"\bisn'?t\b", r"\bdiscontinued\b", r"\bend[- ]of[- ]life\b", r"\bEoL\b", r"\bretired\b",
    r"\blegacy\b", r"\bavoid\b", r"\bweak(?:er|ness)?\b", r"\blimited\b", r"\bunlike\b",
]

# Markers that a mention is an active recommendation rather than a neutral listing.
RECOMMEND_MARKERS = [
    r"\brecommend", r"\bbest\b", r"\bstrong(?:est)?\b", r"\bleading\b", r"\btop\b", r"\bshould\b",
    r"\bgood (?:fit|choice|option)\b", r"\bideal\b", r"\bconsider\b", r"\bstart with\b",
]

# --- Competitors -----------------------------------------------------------
# name -> {"aliases": [...standalone/product names...], "acquirer": [...] or None, "confirmed": bool}
# confirmed=True: named in the corpus (doc 11 Layer 3c / alias table †). False: proposed addition, awaiting sign-off.
COMPETITORS = {
    "HiddenLayer":                 {"aliases": [r"Hidden\s?Layer"], "acquirer": None, "confirmed": True},
    "Lakera (Check Point)":        {"aliases": [r"\bLakera\b"], "acquirer": [r"Check\s?Point"], "confirmed": True},
    "Protect AI (Palo Alto)":      {"aliases": [r"Protect\s?AI\b"], "acquirer": [r"Palo\s+Alto", r"Prisma\s+AIRS"], "confirmed": True},
    "Robust Intelligence (Cisco)": {"aliases": [r"Robust\s+Intelligence"], "acquirer": [r"Cisco\s+AI\s+Defense", r"\bCisco\b"], "confirmed": True},
    "Prompt Security (SentinelOne)": {"aliases": [r"Prompt\s+Security"], "acquirer": [r"Sentinel\s?One"], "confirmed": True},
    "Cloudflare":                  {"aliases": [r"\bCloudflare\b"], "acquirer": None, "confirmed": True},
    "Kong":                        {"aliases": [r"(?<!Hong\s)\bKong\b"], "acquirer": None, "confirmed": True},
    "Zscaler":                     {"aliases": [r"\bZscaler\b"], "acquirer": None, "confirmed": False},
    "Netskope":                    {"aliases": [r"\bNetskope\b"], "acquirer": None, "confirmed": False},
    "Portkey":                     {"aliases": [r"\bPortkey\b"], "acquirer": None, "confirmed": False},
    "LiteLLM":                     {"aliases": [r"\bLite\s?LLM\b"], "acquirer": None, "confirmed": False},
    "NVIDIA NeMo Guardrails":      {"aliases": [r"NeMo\s+Guardrails", r"NVIDIA\s+NeMo"], "acquirer": None, "confirmed": False},
    "AWS Bedrock Guardrails":      {"aliases": [r"Bedrock\s+Guardrails", r"Amazon\s+Bedrock"], "acquirer": None, "confirmed": False},
    "Azure AI Content Safety":     {"aliases": [r"Azure\s+AI\s+Content\s+Safety", r"Azure\s+Content\s+Safety"], "acquirer": None, "confirmed": False},
    "Google Model Armor":          {"aliases": [r"Model\s+Armor"], "acquirer": None, "confirmed": False},
}

# Counted and reported, but NOT in the share-of-model denominator unless promoted after the first baseline.
WATCHLIST = {
    "Microsoft Purview": [r"\bPurview\b"],
    "Noma Security": [r"\bNoma\b"],
    "Aim Security": [r"\bAim\s+Security\b"],
    "Arthur AI": [r"\bArthur\s?AI\b"],
    "WhyLabs": [r"\bWhyLabs\b"],
    "Credo AI": [r"\bCredo\s?AI\b"],
    "Guardrails AI": [r"\bGuardrails\s?AI\b"],
    "Llama Guard": [r"\bLlama\s?Guard\b"],
    "Pillar Security": [r"\bPillar\s+Security\b"],
    "Lasso Security": [r"\bLasso\b"],
    "Zenity": [r"\bZenity\b"],
    "Harmonic Security": [r"\bHarmonic\b"],
    "Nightfall": [r"\bNightfall\b"],
    "Vectra": [r"\bVectra\b"],
    "Wiz": [r"\bWiz\b"],
    "Datadog LLM Observability": [r"\bDatadog\b"],
    "TrueFoundry": [r"\bTrueFoundry\b"],
    "Envoy AI Gateway": [r"\bEnvoy\s+AI\s+Gateway\b"],
    "Apigee": [r"\bApigee\b"],
    "Traceable": [r"\bTraceable\b"],
    "Akamai": [r"\bAkamai\b"],
    "Imperva": [r"\bImperva\b"],
    "Radware": [r"\bRadware\b"],
    "Fortinet": [r"\bFortinet\b"],
    "CrowdStrike": [r"\bCrowdStrike\b"],
    "Garak": [r"\bgarak\b"],
    "PyRIT": [r"\bPyRIT\b"],
    "Promptfoo": [r"\bpromptfoo\b"],
    "Mindgard": [r"\bMindgard\b"],
}

F5_OWNED_DOMAINS = ["f5.com", "nginx.com", "nginx.org", "surepath.ai", "calypsoai.com"]


def compile_all():
    flags = re.IGNORECASE
    f5 = [(re.compile(p, flags), k) for p, k in F5_ALIASES]
    inacc = [re.compile(p, flags) for p in INACCURATE_PATTERNS]
    ctx = re.compile("|".join(CONTEXTUAL_MARKERS), flags)
    rec = re.compile("|".join(RECOMMEND_MARKERS), flags)
    comps = {n: {"aliases": [re.compile(a, flags) for a in d["aliases"]],
                 "acquirer": [re.compile(a, flags) for a in d["acquirer"]] if d["acquirer"] else None,
                 "confirmed": d["confirmed"]} for n, d in COMPETITORS.items()}
    watch = {n: [re.compile(a, flags) for a in pats] for n, pats in WATCHLIST.items()}
    return f5, inacc, ctx, rec, comps, watch
