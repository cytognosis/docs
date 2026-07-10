# Session e858c1e3 — IGoR Grant Proposal Development (Early Session)

**Session title:** IGoR grant proposal development
**Session ID:** local_e858c1e3-ea52-4085-9f6e-5c1c2f6765df
**Approximate date:** 2026-06-12 (dated artifacts produced: `IGoR_Solution_Summary`, `ONEPAGER_DRAFT.md`, `FULLPROPOSAL_DRAFT.md`, `COST_MODEL.md`)
**Rank in consolidation plan:** 15 (low recency; early session)
**Temporal authority:** Lower authority than ranks 0–8. Treat as baseline-only; all conflicts resolve in favor of higher-rank sessions.

---

## Summary

This was the **founding proposal-development session**: it produced the first complete set of IGoR draft deliverables (SS, full proposal C.1/C.2/C.3, TA1 partner one-pager, and the first price workbook). It also performed the first solicitation deep-read and established the initial team, disease, and cost decisions. Many of those early decisions were later revised in higher-rank sessions; this note flags each as SUPERSEDED or CONFLICTS accordingly.

---

## Baseline Decisions Captured

### Disease Strategy

| Item | This session's value | Consolidated state | Status |
|---|---|---|---|
| Primary disease (Phase I–II) | Schizophrenia | Schizophrenia | AGREES |
| Related second disease (Phase III) | Bipolar disorder | Bipolar disorder | AGREES |
| Cellular disease handle | 22q11.2 deletion + TBX1; iPSC-NGN2 neurons | Same | AGREES |
| Disease framing sequence | Schizophrenia primary, bipolar extension | Same | AGREES |

### Team / Roles (at time of session)

| Person / Org | Role in this session | Consolidated state | Status |
|---|---|---|---|
| IPAI/Grama | Prime; PI | Prime; PI (confirmed) | AGREES |
| Cytognosis/Shahin | TA1+TA2 co-lead; submitter | Same | AGREES |
| Anne Carpenter | Listed as a candidate; cost attributed tentatively to Broad sub (~$2M) | **Confirmed in-house at IPAI/Purdue; NO Broad subaward; cost reattributed to IPAI/Purdue computational** | SUPERSEDED (rank 1 abd69da7 resolved this) |
| Phylo / Kexin Huang | Listed as primary TA2 partner (agentic science) | Optional / TBD | SUPERSEDED — demoted to optional in higher-rank sessions |
| DataTecnica / Faraz | Listed as alternate TA2 partner | Still alternate; OCI clearance required (Faraz = NIH contractor) | AGREES (still flagged as alternate pending legal) |
| SIFT / Dan Bryce | Listed as TA3 primary; **framing unclear — transcript shows "TA3 primary"** | TA3 lead; scoped Bayesian VOI layer for TA2 only — NOT TA2 co-lead | SUPERSEDED (rank 5 2ee7cd56 clarified SIFT's TA2 role) |
| Cellanome | Listed as TA4.1 industry arm | Same; confirmed advancing | AGREES |
| Illumina | Listed as TA4.2 third partner | Optional / TBD | SUPERSEDED — demoted to optional |
| Transfyr | Listed as optional TA3 candidate | **DECLINED 2026-06-18** | SUPERSEDED |
| Patricia Purcell | Not yet named as PM | PM confirmed; labor accrues to Cytognosis | ADDS (PM not yet assigned in this session) |
| Elham / architect | Not named in this session | Elham = interim placeholder; Cytognosis hire planned | ADDS |
| Anna Merkoulovitch | Not mentioned | Off market; no longer a candidate | N/A |

### Budget (first version)

| Item | This session's value | Consolidated state | Status |
|---|---|---|---|
| Total ARPA-H request | **$50.0M over 60 months** | $50.0M over 60 months | AGREES |
| Phase I (18 mo) | $13.5M | $13.5M | AGREES |
| Phase II (18 mo) | $15.0M | $15.0M | AGREES |
| Phase III (24 mo) | $21.5M | $21.5M | AGREES |
| Total with in-kind | ~$54.0M (~$4M in-kind) | ~$54.0M | AGREES |
| Cellanome | Not separately called out in transcript (cost model was draft) | $8.0M placeholder (pending June 23) | ADDS |
| Anne Carpenter cost | ~$2M under Broad subaward | ~$2M reattributed to IPAI/Purdue; Broad line removed | SUPERSEDED |
| ~31 cost figures flagged | Not flagged yet (first draft) | 31 figures flagged `[FLAG 2026-06-17]` in COST_MODEL_DETAILED_2026-06-16.md; need re-derivation | SUPERSEDED (flagging done in rank 4 f3f4021c) |
| Source-of-truth budget file | `COST_MODEL.md` (first version, 2026-06-12) | `full_proposal/costs/COST_MODEL_DETAILED_2026-06-16.md` (2026-06-16 supersedes) | SUPERSEDED |

### TA4 Platform Decision

| Item | This session | Consolidated state | Status |
|---|---|---|---|
| Live-cell platform | Cellanome R3200 identified as the live-cell arm | Cellanome R3200 confirmed | AGREES |
| Element Teton | Not clearly distinguished from Cellanome; session transcript shows "Carpenter + Cellanome" as core TA4 without explicit Element role | Element = Tegtmeyer fixed-cell academic arm ONLY; disqualified for live-cell/calcium imaging. "Element Teton CytoProfiling" was later inserted in SS text and flagged for removal. | SUPERSEDED (rank 2 27fe559e and rank 0 config resolved this) |
| Phase I functional readout | Not explicitly stated in transcript summary | Single-cell calcium imaging (NOT MEA) | ADDS — this clarification came in later sessions |
| MEA electrophysiology | Possibly implied (TA3 schema referenced MEA) | OUT — not Phase I readout; TA3 schema needs rework | SUPERSEDED |

### TA3 Standards

| Item | This session | Consolidated state | Status |
|---|---|---|---|
| LabOP/PAML | Named as TA3 backbone | Confirmed; Bartley et al. 2023 citation | AGREES |
| SiLA 2 citation | Not captured explicitly in transcript summary; session predates the Juchli/Ulrich correction | Juchli 2022 doi:10.1007/10_2022_204 (corrected in rank 7 90daed69) | SUPERSEDED (citation correction post-dates this session) |
| LinkML + Biolink | Named as semantic foundation | Confirmed; single foundation across all TAs | AGREES |
| RFC governance overlay | Named as novel Cytognosis contribution | Same | AGREES |

### Program Facts

| Item | This session | Consolidated state | Status |
|---|---|---|---|
| Solicitation | ARPA-H-SOL-26-155 | Same | AGREES |
| Instrument | OT (Other Transaction) | Same | AGREES |
| Solution Summary due | 2026-06-25, 12:00 PM ET | Same | AGREES |
| Full proposal due | 2026-08-06, 12:00 PM ET | Same | AGREES |
| Program Manager | Not explicitly stated in this session (Vodovotz placeholder may have been live) | Paul E. Sheehan Ph.D. (corrected in rank 4 f3f4021c from "Vodovotz" template placeholder) | SUPERSEDED — if Vodovotz was in these drafts, it was corrected later |
| Team name | Not named "PsychIGoR" — session predates the name lock | PsychIGoR (locked 2026-06-18) | SUPERSEDED — name adopted in rank 1 abd69da7 |

### Eligibility Flags (raised in this session)

| Flag | This session | Consolidated state | Status |
|---|---|---|---|
| DataTecnica / Faraz (NIH contractor) | Flagged as optional/alternate pending OCI clearance | Still alternate; OCI clearance required before Aug 6 | AGREES |
| Transfyr (founder = former ARPA-H director) | Flagged as optional pending OCI clearance | DECLINED 2026-06-18 (outreach, not legal disqualification) | SUPERSEDED (moot) |

### Citation Corrections (identified in this session)

These corrections were identified during this session's research subagent pass and are foundational:

| Claim corrected | Correction | Consolidated state | Status |
|---|---|---|---|
| "Strong genetic risk factor" phrasing in Tegtmeyer et al. 2025 | Paper does NOT contain this phrase; cite epidemiology separately (22q11DS consortium / Schneider et al.) | Same guidance in consolidated state | AGREES |
| Genetic support: "Nelson-first" | Correct order is Minikel 2024 (2.6x) + Nelson 2015 + King 2019 | Minikel 2024 confirmed | AGREES |
| PubMed KG: PKG25S4 | PKG25S4 not yet released (~July 2026); cite PKG 2.0 (Xu et al. 2025); note PKG25S4 as forthcoming | Same guidance | AGREES |

---

## Artifacts Produced in This Session

| File | Notes |
|---|---|
| `IGoR_Solution_Summary` (2026-06-12 draft) | First SS draft; later superseded by updated version with Element removal, Phase III column fix, em-dash cleanup, Juchli DOI addition |
| `ONEPAGER_DRAFT.md` | TA1 partner one-pager; kept factorized-PRS proprietary | 
| `FULLPROPOSAL_DRAFT.md` | First C.1/C.2/C.3 draft; ~18 of 40 pages; superseded by 2026-06-16 versions |
| `COST_MODEL.md` | First price model; superseded by `COST_MODEL_DETAILED_2026-06-16.md` |

---

## Summary: CONFLICTS vs SUPERSEDED

**No live conflicts found.** All discrepancies between this session and the consolidated state are **superseded by higher-rank later sessions**, not contradictions of facts that are still live. Specifically:

- Anne Carpenter's affiliation (Broad sub → IPAI/Purdue in-house) was resolved in rank 1
- SIFT's TA2 role (ambiguous → scoped VOI only, not co-lead) was resolved in rank 5
- Element Teton's platform role (ambiguous → fixed-cell only, not live-cell) was resolved in rank 2
- MEA electrophysiology (possible readout → explicitly out) was resolved in rank 2 and 7
- SiLA 2 citation (uncorrected in this session → Juchli 2022 DOI) was corrected in rank 7
- Team name (unnamed → PsychIGoR) was locked in rank 1
- PM identity (Vodovotz placeholder → Sheehan confirmed) was corrected in rank 4
- Phylo and Illumina (primary partners → optional) were demoted in higher-rank sessions
- Transfyr (OCI candidate → declined) was resolved in rank 1

**Items this session ADDS relative to what was in the consolidation (informational only):**
- First explicit articulation of the Phase III "second related disease" rule → schizophrenia (I–II) / bipolar (III) mapping
- First explicit ≥2-TA4-labs constraint acknowledgment
- First citation corrections (Minikel ordering, PKG25S4 timing, Tegtmeyer phrasing)
- OCI flag on DataTecnica/Faraz and Transfyr (both still present in consolidated state)

---

*Extraction complete. No edits made to proposal, cost, or one-pager files.*
