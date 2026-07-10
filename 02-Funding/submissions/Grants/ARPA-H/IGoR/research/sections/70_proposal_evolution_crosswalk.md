## 70. Proposal evolution: variants as key contributions

**Purpose:** This section documents how the IGoR proposal has evolved across versions, identifies stable claims versus shifting parameters, and flags decisions made or still open. Writers should use the latest version (v4) as the source of truth for the full proposal.

---

### Version crosswalk table

| Version | Date | Prime/PI | Disease framing | Budget (midpoint) | Team additions | Notable scope/claim changes |
|---|---|---|---|---|---|---|
| **v0 (DRAFT)** | ~2026-05-31 | Cytognosis (Shahin PI) | "Neuropsychiatric and neurodegenerative disease"; brain as domain; no specific disease exemplar | Not specified; placeholder | Cytognosis + Purdue/IPAI (Grama) + McLean (clinical); cloud-lab/automation partner explicitly TBD | First draft; Cytoverse branding; four IGoR "components" not yet mapped to TA1-TA4; team gaps for TA3/TA4 explicitly flagged; no specific anchor disease or pilot experiment |
| **v1 (SS_REVISED_2026-06-02)** | 2026-06-02 | Cytognosis (Shahin PI); Purdue as sub | 22q11DS as Phase I-II exemplar; idiopathic schizophrenia as Phase III; bipolar mentioned cautiously | ~$30M ($25-60M range) | Cellanome (TA3/TA4; teaming in progress); Purdue/IPAI (TA1/TA2 support); Panome Bio (TA4 multi-omics, warm); Anne Carpenter (TA4 optical) | Four-pillar TA1 architecture named; SAMS-VAE, PDGrapher, AlphaGenome, scDesign3 committed; Spearman r >=0.4 TA2 Phase I metric added; 22q11DS TBX1-COMT-DGCR8 causal chain committed; factorized-PRS first appears (proprietary) |
| **v2 (SS_REVISED_2026-06-05)** | 2026-06-05 | IPAI/Purdue (Grama PI); Cytognosis as funded sub | Same disease framing; 22q11DS Phase I-II; SZ Phase III; bipolar cautious | ~$30M ($25-60M range) | Same as v1 + Panome Bio more prominent; Transfyr (TA3/TA4 observability, COI check pending); structure note: "if Cytognosis-prime, only cover page, PI line, BOE order swap" | Prime/sub flipped (key structural change); technical content (Pillars 1-4) identical; factorized-PRS proprietary marking formalized; Spearman r >=0.4 metric present but less prominent; BOE unchanged |
| **v3 (FULLPROPOSAL_DRAFT + COST_MODEL_2026-06-12)** | 2026-06-12 | IPAI/Purdue (Grama PI); Cytognosis sub | Schizophrenia (Phase I-II) + bipolar (Phase III); 22q11DS as Phase I cellular anchor | $50M ($13.5M / $15.0M / $21.5M across phases) | Phylo (Kexin Huang, TA2 co-lead; Biomni creator); SIFT (TA3 lead; LabOP); Illumina (TA4 lab 3; Billion Cell Atlas); 7-performer structure; DataTecnica named as alternate TA2; Transfyr held as alternate TA3 pending COI | Budget increased from $30M to $50M reflecting full 7-performer scope; SIFT replaces "Cellanome as TA3 lead" from v1-v2; Panome not in base team (optional add); Spearman r >=0.4 not in milestone table; de la Fuente et al. SENA-discrepancy-VAE added as additional framing; SCHEMA/Singh 2022 added explicitly; "spectral positional encoding" (proprietary, under review) noted in TA1 |
| **v4 (SS_DRAFT + FULLPROPOSAL as of 2026-06-14)** | 2026-06-14 | Same as v3 | Same as v3 | $50M (authoritative) | Same 7-performer structure | Authoritative version; this file and the research master sections use v4 as the source of truth |

---

### Stable core vs. evolving elements

**What has stayed constant across all versions:**

- The **TA1 thesis:** a self-updating, mechanistic, multiscale causal disease model that treats disease genotype as a soft intervention on cell state. This framing is present in every version.
- **"Not an LLM wrapper"** (TA2 hard line): appears verbatim in v1, v2, and v3. Non-negotiable; required by IGoR.
- **22q11DS as Phase I anchor:** every version from v1 onward commits to 22q11DS as the Phase I-II cellular exemplar, with the TBX1-COMT-DGCR8-to-circuit causal chain as the specific deliverable.
- **Four-pillar TA1 architecture** (Pillars 1-4): named from v1 onward; the individual pillar definitions have not changed substantively.
- **Core method stack:** SAMS-VAE, PDGrapher, scDesign3, AlphaGenome, CS-CORE, TransBox box embeddings, MONDO/CL/UBERON/GO, and PsychENCODE data committed in v1 and retained in all subsequent versions.
- **Open-source licensing:** Apache 2.0 code, CC BY 4.0 documentation, in every version.
- **Factorized-PRS as proprietary IP:** marked proprietary in v1 and all subsequent versions; not described in partner-facing materials.
- **Cytognosis nonprofit mission as open-science steward:** present in every version.

**What has changed and why:**

| Parameter | Change | Direction | Reason |
|---|---|---|---|
| Prime/PI | Cytognosis (Shahin) -> IPAI/Purdue (Grama) | v1 -> v2 | Strategic: Purdue's track record and F&A carry win odds; real sub-award still funds Cytognosis |
| Total budget | ~$30M -> $50M | v2 -> v3 | Full 7-performer scope; solicitation states no ceiling; $50M is right-sized for 4-TA, 3-phase, multi-lab |
| Team structure | 3 performers -> 7 performers | v2 -> v3 | Added Phylo (TA2), SIFT (TA3), Illumina (TA4); reflects IGoR requirement for >=3 modalities and >=2 TA4 labs |
| TA3 lead | Cellanome as TA3 execution -> SIFT as TA3 lead | v2 -> v3 | SIFT (LabOP developers) is the appropriate standards/protocol lead; Cellanome is exclusively TA4 |
| Spearman r >=0.4 TA2 metric | Present in v1 go/no-go -> absent from v3 milestone table | v1 -> v3 | Dropped in the consolidation of milestones; should be restored (see section 50) |
| Panome Bio | Prominent TA4 partner in v2 -> optional add in v3 | v2 -> v3 | Illumina replaces Panome as the third named TA4 lab; Panome remains an option |
| Disease title | "Neuropsychiatric" (v0) -> "22q11DS to idiopathic schizophrenia" (v1-v2) -> "Schizophrenia to Bipolar Disorder" (v3) | v0 -> v3 | Bipolar promoted to the title in v3 to make Phase III extension explicit and to satisfy the IGoR two-disease requirement |
| SENA-discrepancy-VAE framing | Not present (v0-v2) -> added as an additional reference (v3) | v2 -> v3 | De la Fuente et al. ICLR 2025 published; cited alongside SAMS-VAE to acknowledge the causal identifiability landscape; does not replace SAMS-VAE as the mechanism-shift backbone |

---

### Open decisions that affect the proposal (as of 2026-06-14)

These must be resolved before the full proposal deadline (2026-08-06):

| Decision | Status | Urgency |
|---|---|---|
| PI: Ananth sole PI vs. Shahin co-PI | Gated on Purdue visiting-scholar appointment | HIGH |
| Confirm IPAI's formal appetite to be prime | Not yet formally committed | HIGH |
| Cellanome teaming agreement signed | Structure agreed; NDA pending | HIGH |
| Named software architect (human, not PI, not an AI agent) | KEY GAP | HIGH |
| Backup PM (Patty Purcell availability risk) | Not yet recruited | HIGH |
| Spearman r >=0.4 metric: restore in full proposal? | Recommendation: restore | Medium |
| Transfyr COI check | Not resolved | Medium |
| Carpenter route: Broad now vs. IPAI; sub-award vs. informal | Open | Medium |
| Panome Bio: optional add or base team? | Open | Medium |
