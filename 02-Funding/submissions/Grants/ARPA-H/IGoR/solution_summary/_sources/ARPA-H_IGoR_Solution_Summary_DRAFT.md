# ARPA-H IGoR: Solution Summary (DRAFT v1)

**ISO:** ARPA-H-SOL-26-155 (Proactive Health Office) · **PM:** Paul E. Sheehan, PhD · **Contact:** IGoR@arpa-h.gov
**Solution Summary due:** 2026-06-25, 12:00 ET · **Full proposal:** 2026-08-06 · **Proposers' Day:** June 9 (DC)
**Format rules (Appendix B):** English; sans-serif ≥11pt (Calibri/Arial/Avenir Next Pro Light); **5-page limit** (cover/company-profile pages + References Cited do NOT count); submit via solutions.arpa-h.gov (register early; SAM.gov UEI ✓). Non-gated: SS → encouraged/discouraged → proposal. LLM-assisted initial review.

> **⚠️ Strategic note (delete before submit):** IGoR requires every team to deliver **all four** technical components. Cytognosis is strongest on **#1 (mechanistic disease models)** and **#2 (AI orchestration)**, its core thesis. **#3 (layered protocol architecture)** and **#4 (distributed validated-lab marketplace)** require lab-automation / cloud-lab / robotics partners that Cytognosis does **not** have in-house. **A competitive IGoR proposal is necessarily a team.** The #1 pre-submission action is to recruit teaming partners for #3/#4 (candidates below). ARPA-H explicitly anticipates and supports teaming (see the IGoR Teaming page). This draft is sized to be trimmed to 5 pages.

---

## Cover / company profile (does not count toward 5 pages)
**Lead:** Cytognosis Foundation (Delaware 501(c)(3); EIN 39-4383634; Daly City, CA). **PI:** Shahin Mohammadi, PhD, who built the first single-cell molecular atlases of psychiatric/neurodegenerative disease (PsychENCODE, PsychAD, ROSMAP; *Science* 2024, *Nature* 2019), creator of ACTIONet. **Core collaborators:** Purdue Institute for Physical AI (Ananth Grama, AI/scalable compute); McLean Hospital (clinical/biobank); Mount Sinai (Roussos, multiscale brain omics). **Teaming partners to add for components 3–4:** a cloud-lab / lab-automation provider and a protocol-standardization group (see §6).

---

## 1. The opportunity (the bottleneck IGoR targets)
Biomedical knowledge is trapped in fragmented labs and unreproducible literature; for complex, multi-system diseases, insights cross fields by chance and cures take decades. IGoR's premise, a closed, AI-enabled loop of **mechanistic models → AI experiment design → reproducible protocols → validated lab data** that produces knowledge ≥10× faster, is the exact infrastructure missing from biomedicine. Cytognosis brings a disease domain where this loop is most needed and most measurable: **neuropsychiatric and neurodegenerative disease**, where mechanism is multi-scale (molecules → cells → circuits → behavior), reproducibility is poor, and current categorical models (DSM) demonstrably fail.

## 2. What we propose (across all four IGoR components) and what's new
We propose an IGoR ecosystem instance proven first on brain disease, built on **Cytoverse** (a multiscale, mechanistic, foundation-model representation of biology) driving an active-learning orchestration engine, coupled (via teaming) to standardized protocols and a validated-lab marketplace.

- **Component 1: Mechanistic disease models that encode causal biology across scales (Cytognosis lead).** Cytoverse: foundation models trained end-to-end across micro (genomic/single-cell), meso (connectomic), and macro (behavior) scales with cross-resolution attention; disease modeled as movement in a residual ("delta-from-healthy") space; causal structure encoded via mediation (genomics as inherited instrument; connectomics as exposome-sensitive mediator). *New:* causal, multi-scale, individual-resolution models rather than single-scale correlative ones.
- **Component 2: AI orchestration that finds knowledge gaps and designs optimal experiments (Cytognosis lead).** An agentic layer that reads the current model's uncertainty/residuals, identifies the highest-value-of-information gaps, and designs the next experiment (active learning + optimal experimental design), emitting machine-readable protocols. *New:* experiment selection driven by a mechanistic model's epistemic uncertainty, not heuristics.
- **Component 3: Layered protocol architecture for reproducible execution by any qualified lab (teamed).** A standardized, parameterized protocol representation (machine- and human-readable; versioned; Cytoplex-style validation) so the same experiment runs identically across labs. *Partner-led; Cytognosis contributes the schema/validation layer (LinkML/transferable from Yar/Cytonome).* 
- **Component 4: Distributed marketplace of validated laboratories returning gold-standard data (teamed).** Routing of designed experiments to qualified wet-labs (cloud-labs + academic cores), with QC/validation and standardized data return that feeds back into Components 1–2. *Partner-led (cloud-lab/automation provider); Cytognosis contributes data standards + the model-update loop.*

Together these close the loop: model → gap → experiment design → reproducible protocol → validated data → model refinement, targeting ≥10× faster validated-knowledge generation, demonstrated on brain disease.

## 3. Why it will work / why us / why now
- **Why us:** the PI built the multi-cohort single-cell brain atlases that are the foundation for Component 1; ACTIONet is used across the psychiatric-genomics consortia; Purdue/IPAI brings foundation-model + scalable-compute depth (and a $250M Lilly–Purdue alliance signal). We are the team that built the data this loop learns from.
- **Why now:** foundation-model methods + paired multimodal datasets (PsychENCODE 388 paired, ROSMAP, NeuroBioBank) make multiscale mechanistic models tractable; cloud-lab automation makes Components 3–4 feasible; ARPA-H's OT/teaming model is the only vehicle that can convene all four across sectors.
- **Open-science fit:** Cytognosis's open, versioned model releases (Apache 2.0/CC BY) directly serve IGoR's reproducibility and interoperability goals.

## 4. Milestones, metrics, phases (5-year, 3-phase)
- **Phase 1 (de-risk the loop on one disease):** stand up Cytoverse v1 for a focused brain-disease question; AI-orchestration v1 proposes experiments; partner labs execute a first standardized protocol set; metric = reproducibility across ≥2 labs + first model-refinement cycle. **Go/no-go:** cross-lab concordance + measurable cycle-time reduction.
- **Phase 2 (scale the loop):** multiple disease questions; expand the lab marketplace; demonstrate ≥10× knowledge-generation rate on benchmarked tasks vs. conventional approaches; prospective validation.
- **Phase 3 (generalize):** extend beyond brain disease; harden the protocol/marketplace standards as community infrastructure.
*(Map exact metrics/milestones to Appendix A's stated program metrics in the full proposal.)*

## 5. (Heilmeier, condensed)
**What/why-now/who-cares:** above. **Limits today:** siloed, single-scale, unreproducible. **What's new:** causal multiscale models + uncertainty-driven experiment design + reproducible protocols + validated-lab loop. **Risks:** integration across 4 components; wet-lab throughput; standardization adoption, mitigated by teaming and phased go/no-gos. **Cost/exams:** per Appendix A/C (full proposal).

## 6. Team & teaming plan (critical)
- **Cytognosis (lead):** Components 1–2; data/model standards for 3–4. PI Mohammadi + Purdue/IPAI (Grama).
- **Needed partners (recruit before/at full-proposal):**
  - **Cloud-lab / lab-automation** for Component 4. Candidates: Emerald Cloud Lab, Strateos/Transcriptic-type providers, or a major academic automation core. **Action: reach out now via the IGoR Teaming page + Proposers' Day (June 9).**
  - **Protocol-standardization / robotics** group for Component 3, an academic automation/standards lab.
  - **Clinical/biobank** (McLean, Mount Sinai) for disease-domain validation data.
- Use the ARPA-H IGoR Teaming profiles + Proposers' Day to fill 3/4 gaps; this is the gating dependency for competitiveness.

## 7. Immediate actions
1. **Register on solutions.arpa-h.gov now** (SAM.gov UEI ✓; registration 7–10 business days for the portal/SAM).
2. **Attend/stream Proposers' Day (June 9)**; post a Teaming profile seeking cloud-lab + protocol-standardization partners.
3. **Secure ≥1 lab-automation partner** for Components 3–4 before committing to a full proposal.
4. **Trim this draft to the 5-page Appendix B model** (≥11pt sans-serif; cover/company-profile + References don't count).
5. Confirm whether pursuing IGoR (a PHO *program*) alongside an **HSF** Mission-Office ISO is permissible (likely yes; different mechanisms; verify with IGoR@arpa-h.gov).

*Sources: ARPA-H IGoR program page + SOL-26-155 (sam.gov opp 287ec68e…), retrieved 2026-05-31.*
