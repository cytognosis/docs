# Element Bio Teton vs Cellanome R3200 — IGoR TA4 Platform Comparison

**Source:** Session `local_27fe559e-10d0-448e-8beb-7b041a59a575`
**Session title:** "Element Bio Teton vs Cellanome R3200"
**Session recency:** idle; no explicit date in transcript; session recency rank 2 (2nd most recent)
**Consolidated:** 2026-06-19

---

## Summary

These are opposite-paradigm platforms. **Element Teton** is a fixed-cell, high-plex endpoint readout (millions of cells, 350 RNA + ~88 protein + morphology in <24 h, but cells are formaldehyde-fixed first — zero live function). **Cellanome R3200** keeps tens of thousands of cells alive in programmable compartments (CellCage enclosures), images them over days, perturbs them on-chip (chemical + pooled CRISPR), then performs same-cell whole-transcriptome RNA-seq.

For IGoR TA4's decision-critical dimension (calcium imaging / electrophysiology / live-cell functional readout), **only Cellanome qualifies**. Element Teton is disqualified by fixation. The session yielded three deliverables (ADHD-brief .md, external one-pager .pdf, side-by-side .pptx) stored in the IGoR TA4 `deep_dives` folder.

---

## Key Facts (with dates/source)

All facts from session transcript; no explicit date stated. Session recency rank 2 (2nd most recent).

### Element Biosciences Teton / AVITI24 CytoProfiling

| Attribute | Value |
|-----------|-------|
| Cell state | **Fixed (formaldehyde-fixed before profiling)** — zero live function |
| RNA plex | ~350 RNA targets |
| Protein plex | ~88 protein targets |
| Morphology | Yes (imaging included) |
| Throughput | Millions of cells per run |
| Time | <24 h from sample to readout |
| Live-cell capability | None — incompatible |
| Calcium imaging | **Disqualified** (cells are fixed) |
| Electrophysiology | None |
| Genetic perturbation | Not intrinsic (endpoint only) |
| Source verified | Element product sheet + user guide (fixation step confirmed via primary sources) |

### Cellanome R3200

| Attribute | Value |
|-----------|-------|
| Cell state | **Live** — cells maintained alive in programmable CellCage compartments |
| Throughput | Tens of thousands of enclosures per run |
| Imaging | Continuous live-cell imaging over days |
| RNA-seq | Same-cell whole-transcriptome RNA-seq (at end of live imaging) |
| Perturbation — chemical | Yes, on-chip |
| Perturbation — genetic | Pooled CRISPR on-chip |
| Multimodal | Live imaging + RNA-seq from the same cell |
| Calcium imaging | **Confirmed for slow, multi-day neuronal activity**; sub-second spike-resolved firing is **unconfirmed** (flagged as open question for Dwight) |
| Electrophysiology | None (no MEA, no patch clamp); calcium is an optical proxy only |
| Launch timing | AGBT 2026 showcase (confirmed via GenomeWeb) |
| Source verified | Cellanome neurobiology page + GenomeWeb AGBT 2026 + Psomagen R3200 explainer; "R3200" name, CellCage, neuronal calcium activity, same-cell RNA-seq all independently confirmed |

---

## Decisions

1. **Cellanome R3200 is the chosen TA4 platform** for live-cell functional profiling in IGoR. Element Teton does not qualify for any workflow requiring live cells or functional readout.
2. **Element Teton is not needed** for IGoR TA4 as scoped in this session. It could serve as a complementary high-plex endpoint tool if fixed-cell profiling at scale is added, but this was not a stated requirement.
3. **Calcium imaging is the Phase I functional neuronal readout** modality (consistent with the MEMORY.md entry `igor-functional-readout-calcium.md`). Cellanome is the instrument enabling this.
4. **Neither platform does true electrophysiology.** MEA or patch-clamp would require a separate external rig. The session concluded this is not a gap given the imaging stack fold (Cellanome/Carpenter).
5. **Three partner-facing deliverables were produced** (ADHD brief .md, external one-pager .pdf, side-by-side .pptx) — all in IGoR TA4 `deep_dives` folder, with Cytognosis branding restrained (PsychIGoR prime = IPAI/Grama).

---

## Open Items

1. **Dwight calcium-imaging response pending.** Fast sub-second spike-resolved firing from Cellanome R3200 is unconfirmed. Must pin down with Dwight (presumably a Cellanome contact) before relying on it in the Solution Summary or full proposal.
2. **If Cellanome delivers slow calcium imaging only,** a separate electrophysiology rig (MEA) may need to be added as a TA4 instrument — this would reopen the MEA schema that was noted as needing rework in the TA3 integrated design memory.
3. **Footer attribution on deliverables.** External pieces use restrained Cytognosis branding. If they go out under the PsychIGoR team banner rather than Cytognosis, the footer needs swapping.
4. **SS per-performer cost table re-derivation** still pending (per MEMORY.md `project-igor-team-2026-06-18.md`). Element vs Cellanome capex/opex split would feed into this.
5. **Capex vs opex / send-out model** for R3200 was not explicitly resolved in the transcript text. The Psomagen blog was cited as an explainer, suggesting a send-out / service model exists, but no pricing numbers were captured in the transcript summary.

---

## Conflicts to Flag

1. **MEMORY.md `project-igor-ta3-integrated-design.md`** notes "deep-dive MEA schema to be reworked in full-proposal build." This session confirms no MEA is planned for TA4 (calcium imaging is the readout via Cellanome). These are not directly contradictory — MEA rework may refer to removing/de-scoping MEA from the TA3 protocol schema — but the two docs should be reconciled explicitly to avoid reviewers seeing a MEA reference in TA3 scaffolding.
2. **Cellanome throughput language.** MEMORY.md `project-igor-team-2026-06-18.md` does not quote a throughput number. This session says "tens of thousands of enclosures per run." Ensure this number is consistently used across all SS and full-proposal cost/throughput tables once confirmed with Cellanome.
3. **No pricing / capex numbers captured.** The original user query asked about "costs/pricing, capex-vs-opex/send-out model." The transcript summary does not include any dollar figures for either platform. These are missing from this extraction and must be sourced separately before completing the SS per-performer cost table.
