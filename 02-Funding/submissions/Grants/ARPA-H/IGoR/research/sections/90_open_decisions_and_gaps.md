## 90. Open decisions, gaps, and pre-submission actions

> [!NOTE]
> Consolidated from the proposal variants, the cost model, the partner slate, and the carried-over QA items from the retired `_build/` logs. Ordered so that items needing no outreach come first.

### Do now (no outreach needed)

| Item | Action | Source |
|---|---|---|
| **Budget figure is authoritative** | Treat **$50M** (COST_MODEL 2026-06-12) as final; purge any lingering $30M references | section 60 |
| **sVAE+ citation unverified** | Verify Lopez et al. (arXiv:2211.03553) details or remove it from the reference list | QA carryover |
| **PKG25S4 not yet published** | Cite PKG 2.0 (Xu et al. 2025), dataset version PKG24S4; do not cite PKG25S4 as current | QA carryover |
| **22q11.2 risk-stat citation scope** | Use Tegtmeyer et al. 2025 only for the cellular phenotype; cite a dedicated epidemiology source (for example Schneider et al.) for the psychosis-risk multiplier | QA carryover |
| **"89% irreproducible" claim** | Add an inline citation (for example Begley and Ellis, or Ioannidis) where the statistic appears | section 50, QA |
| **STATE author list** | Complete the author list from the bioRxiv page before citing | QA carryover |
| **Dropped Spearman r >= 0.4 TA2 metric** | Decide whether to restore the quantitative ranking metric dropped between v3 and v4; recommended to restore | section 50 |
| **B12 falsifiability test** | Decide whether to reinstate the methylcobalamin reversion test in the Phase I anchor (present in v3, absent in v4) | section 41 |
| **One-pager staleness** | Update `partnerships/partner_onepager/` to the final roster (SIFT as TA3 lead, Illumina as TA4) before any new sharing | section 70 |
| **Proprietary page marking** | At final formatting, mark every page describing the factorization "Proprietary" (do not use "Confidential") | reference Appendix |

### Needs a decision or outreach

| Item | Status | Owner / next step |
|---|---|---|
| **Software architect (required role)** | **Open gap.** Must be a named human, distinct from PI and PM; about $240K loaded in the model | Recruit and name before the full proposal |
| **Prime and PI** | Base case is IPAI/Purdue prime, Grama PI; flipping to Cytognosis-prime changes only the cover and BOE order | Confirm with Grama before the cover is locked |
| **PI succession (pending)** | PI succession (pending): the PI seat may move from Ananth Grama to Anne Carpenter if she accepts the lead-PI invitation (see partnerships/outreach/Carpenter_Anne_outreach.md, Email 2). With Ananth's support he would shift to co-PI; the prime stays at IPAI/Purdue. Keep Ananth Grama as PI in all submission fields until Anne confirms. | Confirm with Anne Carpenter; consult Ananth Grama |
| **Project manager** | Patty Purcell named "in discussion"; flagged availability risk | Line up a backup PM now |
| **Cellanome (TA4) operating model (added 2026-06-17)** | **Open.** Two options: (a) R3200 placed **in a PsychIGoR lab** (capex, in-house control, capability building); (b) **send cells/samples to Cellanome** (opex, Cellanome executes). Pricing pending from Cellanome; decide after numbers arrive. Framing: treat the head-to-head with Matt's academic arm as a **one-time Phase I cross-arm concordance milestone**, not the standing model | Receive Cellanome pricing; decide in-lab vs send-out; update cost model **[FLAG 2026-06-17: re-derive after Anne reattribution]** |
| **Element AVITI24 vs Cellanome roles (added 2026-06-17)** | **Open.** Confirm Element and Cellanome are orthogonal (Element = fixed-cell, high-scale, next-day; Cellanome = live-cell, temporal) and non-redundant in the workplan. Risks to avoid: treating them as interchangeable, or letting the Cellanome head-to-head implicitly make Cellanome the primary readout and under-build in-house capability | Confirm at the Jun 29-Jul 3 Purdue visit; map each modality to one platform in the TDD task table |
| **Anne Carpenter + Matt Tegtmeyer effort split and IU-team resolution (added 2026-06-17)** | **Open; resolve before Aug 6.** Both are also named on the IU-prime IGoR team (~5 lead PIs; likely Purdue subaward). Concern is elevated because (1) Matt is our sole academic experimental TA4 arm and (2) Anne is our lead-PI candidate. Confirm: Matt primary on PsychIGoR + light/defined on IU team with non-overlapping committed hours; Anne same; the Purdue iPSC-neuron bench and Anne's compute are not double-committed; if Anne is lead PI, her IU role is minimal and disclosed | Resolve at Jun 29-Jul 3 Purdue visit; **not a blocker for the Jun 25 Solution Summary** |
| **Cost-model re-derivation after Anne reattribution (added 2026-06-17)** | **Open.** Anne was previously attributed as a wet-lab contributor (Carpenter bench, Cell Painting infrastructure capex, ~$2M Broad "Cell Painting infrastructure" subaward). Corrected role is **personnel and compute only**; wet-lab equipment and stand-up belongs under Matt's bench and imaging. All cost-model dollar figures for Anne are **[FLAG 2026-06-17: re-derive after Anne reattribution]**; Shahin/Ananth re-derive; do not use prior figures | Shahin/Ananth re-derive cost model; update `full_proposal/costs/COST_MODEL_DETAILED_2026-06-16.md` |
| **Cellanome (TA4)** | Advancing; NDA pending; operating-model decision pending (see above) | Close NDA; decide in-lab vs send-out after pricing |
| **Illumina (TA4)** | "Key contact in discussion"; soften or confirm language before submission | Confirm commitment or reword |
| **Transfyr (TA3 candidate)** | **Declined 2026-06-18.** Removed from all rosters and team tables. File retained in onepagers/ for reference. | Closed |
| **DataTecnica (TA2 alternate)** | Pending OCI/eligibility clearance | Resolve only if Phylo falls through |

> [!WARNING]
> **Eligibility and OCI are gating.** Any team member with current or recent ARPA-H support-service ties must be disclosed with an OCI mitigation plan; the proposal is non-conforming if it does not address all four TAs and all three phases, or if the concept has already been funded or selected elsewhere. See the reference Appendix B and consult counsel (Duane Valz).

### Consistency checks before submission

- **Disease title alignment:** the full-proposal title frames "schizophrenia to bipolar" while the one-pager still leads with 22q11DS; align the framing or explain the relationship.
- **Citation set drift:** AlphaGenome, ROSMAP, and PsychAD appear in early variants but not in the latest reference lists; reinstate in biosketches or the references if they support the track-record claims.
- **Restricted content firewall:** confirm the factorized-PRS method (section 31), SPEAR internals (section 32), and the personal-genomic anchor (section 41) do not appear in any `shareable` build, one-pager, or teaming page.
- **Cross-document numbers:** phase durations (18, 18, 24), concordance gates (85% intra/cross-team, 90% marketplace), and cycle-time targets (4x, 10x) must match the solicitation truth in `../materials/IGoR_Comprehensive_Reference.md`.
