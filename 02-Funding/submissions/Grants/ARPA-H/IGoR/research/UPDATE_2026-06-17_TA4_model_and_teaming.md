# TA4 Model + Teaming — Change Spec (2026-06-17)

**Status:** AUTHORITATIVE. This memo is the single source of truth for propagating today's updates across all live IGoR docs. Every downstream edit derives from Sections 2–8. Items in Section 9 are FLAGGED for human review and must not be auto-changed.

---

## 1. BLUF: five changes

1. **TA4 has two experimental arms.** Academic arm = **Matt Tegtmeyer's lab (Purdue)**, which runs all the wet-lab experiments. Industry arm = **Cellanome**. These are the two TA4 laboratories that satisfy the program's ">= 2 TA4 labs" requirement; additional labs are additive.
2. **Anne Carpenter is purely computational.** In all of her joint work with Matt, Anne does **interpretable models for morphology / cellular-imaging data**, not wet-lab. She runs **no bench**. Reclassify her everywhere from "TA4 experimental phenomics" to **computational morphology/imaging-model lead** (TA4 analysis + TA1/TA2 interpretability bridge).
3. **Both Matt and Anne are also on another IGoR team** (Indiana University prime, ~5 lead PIs; Matt and Anne participate, likely via a **Purdue subaward**). Allowed by the rules, but it is an effort/optics item to resolve before the **Aug 6** full proposal. See Section 7.
4. **Element Biosciences AVITI24 / Teton CytoProfiling** is a multi-modal same-cell platform Matt already uses. It is a comparator/complement to Cellanome. See Section 6.
5. **Cellanome engagement advanced** (eager; 3-person call 2026-06-17). Operating model under discussion: **R3200 placed in a PsychIGoR lab** vs **send cells/samples out to Cellanome**. Pricing pending. A proposed **head-to-head Cellanome vs Matt's-lab** comparison should be framed as a **cross-arm reproducibility milestone**, not the standing model. See Section 5.

---

## 2. The corrected TA4 model

| Layer | Who | What they do | Arm |
|---|---|---|---|
| **Experimental — academic** | **Matt Tegtmeyer lab, Purdue** | All wet-lab experiments: iPSC-neuron disease models; multi-modal same-cell readouts (uses **Element AVITI24 / Teton CytoProfiling**) | Academic TA4 lab |
| **Experimental — industry** | **Cellanome** | Live-cell imaging + same-cell scRNA-seq + Perturb-LINK CRISPR on the **R3200** | Industry TA4 lab |
| **Computational** | **Anne Carpenter (IPAI/Purdue)** | Interpretable models for morphology / cellular imaging; morphological profiling; consumes readouts from both arms | Analysis (not a TA4 wet lab) |

**Consequence for the ">= 2 TA4 labs" rule:** met by **Matt's academic lab + Cellanome** (industry), with Illumina/SPOC/others additive. Anne does **not** count as a wet lab; she is the computational layer.

**Reproducibility angle (use deliberately):** the academic arm (Matt's lab + Element AVITI24) and the industry arm (Cellanome R3200) give **two independent multi-modal readout platforms**, enabling a built-in **cross-arm / cross-platform concordance check** that maps directly onto the program's concordance gates (85% intra/cross-team). Anne's computational morphology models are the common analysis layer that makes the two arms comparable.

---

## 3. Anne Carpenter — role correction

| | OLD (wrong) | NEW (correct) |
|---|---|---|
| Role label | "TA4 experimental phenomics" | **Computational morphology/imaging-model lead** (interpretable models; TA4 analysis + TA1/TA2 bridge) |
| Bench/wet-lab | Implied Cell Painting wet bench at Purdue/Broad | **None.** Purely computational. The actual imaging/experiments are run by Matt's lab (and Cellanome) |
| Affiliation | IPAI/Purdue (joining ~Sep 2026; transition at Broad) | Unchanged: IPAI/Purdue, mid-move |
| Cost-model footprint | Wet-lab equipment / "Carpenter bench" / ~$2M Broad "Cell Painting infrastructure" subaward | **Personnel + compute**, not wet-lab capex. Broad transitional subaward (if retained) is for **computational/analysis continuity**, not wet infrastructure. **$ figures = FLAG (Section 9)** |

**Downstream:** Anne remains a strong **lead-PI candidate** on the merits (computational leadership + reputation), but the draw must be framed as **computational**, not experimental. Note the tension in Section 7: a potential lead PI who is also on a competing team needs explicit resolution.

---

## 4. Matt Tegtmeyer — academic experimental arm

- **Role:** the **academic experimental engine of TA4**. His lab runs all the wet-lab experiments (iPSC-neuron disease models + multi-modal readouts). Confirmed Purdue faculty; confirmed on our team 2026-06-15.
- **Platform:** has hands-on experience with **Element AVITI24 / Teton CytoProfiling** (Section 6). This is a team capability to surface.
- **Division of labor with Anne:** Matt = experiments; Anne = computational morphology/imaging models. Non-overlapping and complementary.
- **Dual-team:** also on the IU-prime IGoR team (Section 7).

---

## 5. Cellanome — engagement update + decisions

- **Status:** advancing. Eager to work together; 3 Cellanome staff on the **2026-06-17** call. Upgrade from "in discussion" to **advancing (industry TA4 arm)**.
- **Operating-model decision (OPEN):** (a) place a **Cellanome R3200 in a PsychIGoR lab** (capex + in-house control + capability building) vs (b) **send cells/samples to Cellanome** (opex; they execute). Cellanome will send **pricing**; decide after numbers arrive.
- **Current lean:** partially toward send-out (Cellanome executes), prompted by framing a **head-to-head Cellanome vs Matt's-lab** comparison as a reproducibility metric.
- **Reframe (recommended):** keep the head-to-head as a **one-time Phase I cross-arm reproducibility milestone** (Matt's lab + Element AVITI24 vs Cellanome R3200), then converge on the most cost-effective primary readout for scale-up. Do **not** let the comparison default the whole workplan to Cellanome. Risks to manage: (i) cost/dependency if Cellanome runs everything; (ii) optics of benchmarking your own academic arm against your industry partner as a standing model; (iii) under-building in-house capability. This turns the "head-to-head" from a slip into a designed concordance feature aligned with the program's gates.

---

## 6. Element Biosciences AVITI24 / Teton CytoProfiling (verified 2026-06-17)

Source: https://www.elementbiosciences.com/products/aviti24/cytoprofiling

- **What it is:** single-cell **and** spatial co-detection of **RNA, protein, phospho-protein, and cell morphology** from one sample at subcellular resolution; imaging + in-situ sequencing via Avidity Base Chemistry (ABC); next-day results; <1 hr sample prep; **hundreds of thousands to millions of cells**.
- **Modalities:** morphology (nucleus, membrane, actin, ER, Golgi, mitochondria — **Cell-Painting-style organelle features**, onboard segmentation + feature extraction); **RNA** 350-plex subcellular (1000s transcripts/cell); **protein** 50-plex (surface, intracellular, phospho); **DISS** (Direct In Sample Sequencing) for untargeted 3' RNA, **in-situ CRISPR-guide sequencing**, and expressed-mutation detection.
- **Neuroscience panel** exists (neurodifferentiation, neurotransmission/synaptic, neurodegeneration, neuroinflammation) — directly relevant to Matt's iPSC-neuron work.
- **Vs Cellanome:** **Overlap** = multi-modal same-cell readouts (RNA + protein + morphology) and CRISPR-perturbation readout (Element DISS in-situ guide reads vs Cellanome Perturb-LINK). **Differences:** Element = **fixed-cell in-situ, very high scale, next-day, has a neuro panel, natively outputs Cell-Painting-like morphology** (which feeds Anne's models directly); Cellanome = **live-cell / temporal**, nanoscale single-cell isolation, same-cell scRNA-seq on the R3200. Treat them as **orthogonal/complementary**, not redundant; the differences are the basis of the cross-arm concordance story.
- **How to use it in docs:** list Element AVITI24/Teton as the **academic-arm multi-modal platform Matt brings**, and as the **cross-platform comparator** to Cellanome. Do **not** assert a formal Element partnership/teaming agreement (none stated); it is a platform Matt uses. **FLAG** any teaming claim for confirmation.

---

## 7. Dual-team (IU) status — both Anne and Matt

- **Facts:** the other IGoR team has **Indiana University as prime** and **~5 lead PIs**; **both Anne and Matt** participate, **likely via a Purdue subaward** (to be confirmed).
- **Rules recap (from `IGoR_Participation_Rules_Memo_2026-06-17.md`):**
  - IU-prime is a **different legal entity** from our Purdue/IPAI prime, so the two **primes do not collide**. Good.
  - An org may be a **sub-performer on multiple proposals** (explicit, App A §5.1). So **Purdue as a sub on the IU team while priming ours is allowed**.
  - **No person-level cap** exists, so Anne and Matt may be named on both. The constraints are **committed effort <= 100%**, **reviewer optics** (same PM, Paul E. Sheehan, reviews all ~3 awards), and a **post-award sub de-duplication** rule if the same Purdue bench does overlapping same-TA work on two selected teams.
- **Elevated concern:** both of our TA4 anchors (and our potential lead-PI candidate, Anne) are on a competing team. Resolve before **Aug 6**. **Not a blocker for the Jun 25 Solution Summary** (no effort/OCI disclosure at that stage).
- **Confirm at the Jun 29–Jul 3 Purdue visit:** (1) IU is prime on the other team (not Purdue); (2) Matt and Anne are **primary on PsychIGoR**, light/defined on the IU team, with non-overlapping committed hours; (3) the Purdue-subaward routing on the IU team and that the **same iPSC-neuron bench / compute is not double-committed**; (4) if Anne is our lead PI, that her IU-team role is minimal and disclosed.

---

## 8. Per-doc propagation map

Apply Sections 2–7 to each LIVE doc below. Preserve each doc's existing voice, structure, and formatting. Keep the **restricted-content firewall** intact (no factorized-PRS / SPEAR internals / personal-genomic anchor in any shareable/onepager/teaming doc). No em dashes; Oxford comma; bold for emphasis.

### Tier-0 truth / living
| Doc | Key changes |
|---|---|
| `partnerships/TEAM_TRACKER.md` | Reclassify Anne row to computational morphology/imaging-model lead (no bench); rewrite Matt row as academic experimental TA4 arm + Element platform; fix the structural NOTE (the in-house wet-lab is **Matt's** lab, not "Carpenter + Tegtmeyer benches"; Anne is computational); upgrade Cellanome row to advancing + R3200-in-lab-vs-send-out + pricing pending; add Element as Matt's platform under TA4 notes; **expand the existing Matt COI/dual-team WARNING to include Anne + IU/5-PI + Purdue-subaward**; add Cellanome 2026-06-17 to engagement intel |
| `materials/IGoR_Comprehensive_Reference.md` | Update the TA4 truth: two arms (Matt academic / Cellanome industry), Anne computational; add Element as academic-arm platform; keep concordance-gate numbers unchanged |
| `partnerships/CANDIDATE_DOSSIER.md` | Anne entry → computational (not experimental phenomics); Cellanome entry → advancing + operating-model options; add Element note under TA4 readout platforms |
| `research/sections/90_open_decisions_and_gaps.md` | Add open decisions: (a) R3200 in-lab vs send-out (pending pricing); (b) Element-vs-Cellanome roles (orthogonal, confirm non-redundant); (c) Anne/Matt effort split + IU-team resolution before Aug 6; (d) cost-model $ re-derivation after the Anne reattribution |

### Active submission
| Doc | Key changes |
|---|---|
| `solution_summary/IGoR_Solution_Summary.md`, `sections/3_proposed_work.md`, `sections/4_team.md` | TA4 = Matt academic arm + Cellanome industry arm; Anne computational; Element as academic-arm platform. Keep within SS page limits; team is non-binding at this stage |
| `full_proposal/C1_Technical_and_Management_Proposal.md` | Same TA4 model + roles; reproducibility/concordance framing via two arms; Anne computational |
| `full_proposal/C2_Task_Description_Document.md` | Tasks/roles reflect Matt = experiments, Anne = computational analysis, Cellanome = industry execution; add the cross-arm concordance milestone |
| `full_proposal/C3_Price_Proposal.md` | Reflect corrected attribution; **do not invent numbers — FLAG (Section 9)** |
| `full_proposal/costs/COST_MODEL_DETAILED_2026-06-16.md` (+ `COST_MODEL.md`) | Reattribute Anne to personnel/compute (no wet-lab capex / no "Carpenter bench"); equipment stand-up = Matt's bench + imaging; add a Cellanome line with **both** options (R3200 capex vs send-out opex) as TBD-pending-pricing; **all dollar figures FLAGGED for Shahin/Ananth** |

### Partner-facing + research/deep-dive
| Doc | Key changes |
|---|---|
| `partnerships/onepagers/TA4_Cellanome.md` | Cellanome = industry TA4 arm; advancing; operating-model options; concordance role |
| `partnerships/outreach/Carpenter_Anne_outreach.md` | Anne = computational lead; reframe the draw; note lead-PI-vs-IU-team tension |
| `partnerships/outreach/Cellanome_Dwight_decision_email_2026-06-16.md` | Reflect 2026-06-17 call outcome + next step (pricing) |
| `partnerships/onepagers/00_IGoR_Program_Overview.md`, `01_For_Ananth_Science_Seeking_Logistics.md` | TA4 two-arm model; Anne computational; Element mention where readouts are described |
| `partnerships/partner_onepager/IGoR_OnePager.md` + `sections/40_team_and_contact.md` | Team descriptions: Matt academic arm, Anne computational, Cellanome industry arm |
| `research/IGoR_Research_Master.md` (+ `_shareable`), `sections/00_executive_overview.md`, `34_contrib_TA3_TA4_execution.md`, `60_team_consortium_and_cost.md` | TA4 model + roles + Element; concordance framing |
| `research/deep_dives/TA4_labs__full.md` + `__brief.md` | Add **Element AVITI24/Teton CytoProfiling** to the TA4 readout-platform landscape with the Cellanome comparison from Section 6 |
| `research/deep_dives/IFACE_TA4_TA1__full.md` + `__brief.md` | Readout-to-model interface: Element/Cellanome readouts → Anne's computational morphology models → TA1 |
| `research/FACT_CHECK_AND_CAPABILITIES_2026-06-16.md` | Add Element capability facts (Section 6); correct Anne capability (computational) |
| `STAGE_TWO_PLAN.md` | Reflect TA4 model + the Aug-6 effort/IU resolution action |
| `research/IGoR_Participation_Rules_Memo_2026-06-17.md` | Expand the Matt section to **Matt + Anne**, IU prime + ~5 PIs + likely Purdue subaward; reaffirm rules verdict |

---

## 9. FLAGGED for human review (do NOT auto-change)

1. **All cost-model dollar figures.** The Anne reattribution (wet-lab capex → personnel/compute), the Broad transitional subaward rationale, the Purdue equipment stand-up scope, and the new Cellanome line (R3200 capex vs send-out opex) change the numbers. **Shahin/Ananth re-derive; do not fabricate.**
2. **Figures/SVGs:** `figures/TA4_experiment_marketplace.svg`, `figures/IGoR_TA_loop_diagram.(svg|mmd)`, `figures/README.md` may depict Anne as experimental or omit the two-arm split. **Flag for manual redraw**; do not hand-edit SVG geometry blindly.
3. **IU-team specifics** (IU is prime; ~5 PIs; Purdue-subaward routing; Anne/Matt effort split) — confirm with Matt at the Purdue visit; treat as founder-reported until confirmed in writing.
4. **PI succession** — if Anne is to be lead PI, reconcile with her IU-team participation before locking the cover.
5. **Element teaming status** — Element is a **platform Matt uses**, not a confirmed teaming partner. Do not claim a partnership without confirmation.

## 10. Guardrails (not changing)
- **TA1 stays in-house** (Cytognosis + IPAI + students; no external TA1 partners).
- **Restricted-content firewall** stays intact.
- Concordance gates (85% intra/cross-team, 90% marketplace), phase durations (18/18/24), and cycle-time targets (4x/10x) are unchanged; verify against `materials/IGoR_Comprehensive_Reference.md`.
- Voice: authoritative, compassionate, optimistic; no "revolutionary/breakthrough/cure".
