# Framing: Verifiability/Interpretability vs Cognitive-Liberty (and the carve)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-11 · **Reading time:** ~6 min · Companion to the Coefficient + EA Funds dossier.

> **If you only read one thing:** Lead the **technical** claim with **verifiability and deployment control**, with **CAP/Cytoplex as the crown-jewel artifact**, and keep **cognitive-liberty as the values motivation**. Do **not** label Cytoverse "interpretability" (to these funders that means mechanistic interpretability of frontier LLMs, and the mismatch will hurt). Your healthcare-can't-be-a-black-box thesis is correct and fundable, but it must be anchored to specific technical-safety problems (faithfulness, activation monitoring, control), not to "healthcare AI ethics," a category EA funders avoid.

---

## Verdict (honest)

- **Interpretability is heavily funded** (~$3M to $8M/yr across EA funders), but the word means **mechanistic interpretability of frontier LLMs** (circuits, SAEs, features). Evals/benchmarking is actually the larger category by dollars.
- **CAP/Cytoplex is the strongest fit of anything we have.** A built, tested (93 passing tests) on-device control layer that blocks unverified diagnosis or treatment claims, forces calibrated uncertainty, and prevents manipulative optimization maps directly onto Coefficient's 2025 TAIS RFP starred areas: **"applications of white-box techniques," "activation monitoring"** (explicitly including detectors for when a model is about to output a false statement, "lie detectors for LLMs"), **"control evaluations,"** and **"alternatives to adversarial training."** LTFF has funded the adjacent honesty/"Discovering Latent Knowledge" work. That we have already built and deployed it is rare and compelling.
- **Cytoverse axes are defensible but not the lead.** Frame them as **interpretable-by-design representations that make outputs falsifiable**, not as a standalone interpretability contribution. Expert reviewers (for example Manifund regrantor Neel Nanda) would otherwise read it as representation learning, not AI-safety interpretability.
- **Causal, hypothesis-generating outputs** map to verifiability (falsifiable equals verifiable), credible if framed as "outputs independently verifiable against clinical and experimental ground truth."

**Risks to manage:** (1) "interpretability for healthcare AI" can be mis-filed as healthcare AI ethics, which EA funders treat as out of lane; anchor to technical safety. (2) Our model is a bespoke biomedical model, not a frontier LLM, so reviewers may see it as narrow; counter with "CAP is domain-agnostic guardrail design; the primitives generalize to any high-stakes LLM deployment."

---

## Combine, do not choose

Cognitive-liberty is the **WHY** (what values and stakes are involved). Verifiability and control is the **HOW** (the technical contribution to the AI-safety agenda). They are motivation plus method, not competitors. Make the **technical safety contribution the primary claim**, and mental health the **motivating example** of the highest-stakes near-term deployment where hallucinations and manipulation cause direct, sometimes irreversible harm.

---

## Per-funder framing

| Funder | Lead framing | Note |
|---|---|---|
| **EA LTFF** | **Verifiability/control, anchored on CAP** | Maps to LTFF's control + output-monitoring + faithfulness priorities. Cognitive-liberty = motivation only. |
| **Coefficient Career Transition** | **Combined A+B** | "Senior computational neuroscientist bringing rare signal from the highest-stakes deployment domain into technical AI safety." Their own page lists computational-biology-to-AI-safety as a prototypical funded pivot. |
| **Coefficient Capacity Building** | **Verifiability/control, domain-general** | CAP as reusable open-source AI-safety infrastructure; healthcare is the motivating use case, not the scope. |
| **Manifund** | **Open-source CAP release** (control framing) | Regrantors (Neel Nanda, Marius Hobbhahn) recognize a tested control layer as legitimate safety work. |
| **Biswas** | Unchanged (health) | No AI-safety vocabulary. |

---

## The carve (thesis + 5 deliverables)

**Thesis:** Biomedical and mental-health AI is the highest-stakes near-term deployment: outputs influence treatment, hallucinations cause direct harm, and engagement-maximizing optimization can exploit vulnerable users, yet these systems are the least constrained by formal safety requirements. Cytognosis builds AI-safety infrastructure for exactly this context: an interpretable-by-design foundation model (Cytoverse) whose continuous, biologically grounded axes generate falsifiable hypotheses for clinical validation, and CAP/Cytoplex, an open-source on-device control layer (93 passing safety tests) that blocks unverified clinical claims, enforces calibrated uncertainty, and prevents manipulative reward optimization. The primitives are domain-general and extend to any high-stakes LLM deployment.

| # | Deliverable | True to our work | Legible as AI safety |
|---|---|---|---|
| 1 | **Open-source CAP/Cytoplex v1.0** + 93-test safety suite + integration guide | Built | Strong (control infrastructure) |
| 2 | **Calibrated-uncertainty benchmark** for biomedical AI outputs | Core CAP function | Strong (maps to output-fidelity / "lie detector" agenda; generalizes) |
| 3 | **Cytoverse axes-vs-labels ablation** showing continuous axes give more verifiable predictions than black-box labels | Core Cytoverse claim | Partial (frame as interpretable-by-design, hallucination prevention at the representation level) |
| 4 | **Causal falsifiable-hypothesis pipeline** with a clinical validation protocol co-designed with Brad | Built | Strong (operationalizes faithfulness/verifiability) |
| 5 | **Deployment safety case study**: mental-health LLM with vs without CAP, quantifying unverified-claim rate, manipulative-framing rate, hallucination reduction | First deployment | Strong (rare empirical safety evidence for real deployment) |

**Lead with Coefficient Career Transition** (your runway grant; combined framing fits the 250-word format). **Second: Manifund** for the open-source CAP release (fastest proof-of-funding and public track record).

---

## New federal pipeline (add now; each needs an academic PI via Purdue/Grama and, for ARPA-H, a health-system partner)

| Program | Fit | Note |
|---|---|---|
| **ARPA-H PRECISE-AI** | **Strongest CAP match** | Explicitly funds "detect and mitigate AI-model degradation in clinical settings" — what CAP does. Verify current solicitation status. |
| **NSF Safe Learning-Enabled Systems (SLES)** | High | "Safety verification in uncertain environments"; healthcare is an explicit deployment context; Coefficient co-funds. |
| **NSF Ethical and Responsible AI (ER2)** | Medium-High | Trustworthy AI incl. calibration and interpretability; typical $500K to $1.5M / 3 yr. |
| **NIST AI Safety Institute / AI RMF** | Medium | CAP's structured-uncertainty outputs align with the RMF Measure and Govern functions. |

---

## What this refines in the dossier

Keep the "open-source AI-safety infrastructure" positioning, but the **lead technical claim becomes verifiability and deployment control (CAP)**, with cognitive-liberty as motivation. Update each application's framing-lead accordingly, and do not over-claim "interpretability" for Cytoverse.

---

## Sources

[Coefficient TAIS RFP research areas](https://coefficientgiving.org/tais-rfp-research-areas/); [Coefficient Career Development and Transition](https://coefficientgiving.org/funds/global-catastrophic-risks-opportunities/career-development-and-transition-funding/); [LTFF payout report](https://forum.effectivealtruism.org/posts/pJyCWzevPHsycj4oQ/long-term-future-fund-may-2023-to-march-2024-payout); [Manifund 2025 regrants](https://forum.effectivealtruism.org/posts/fFEkKdoAKchSZm2RA/manifund-2025-regrants); [NSF SLES $10.9M](https://www.nsf.gov/news/nsf-invests-10-9m-development-safe-ai-tech); [ARPA-H open funding](https://arpa-h.gov/explore-funding/open-funding-opportunities).
