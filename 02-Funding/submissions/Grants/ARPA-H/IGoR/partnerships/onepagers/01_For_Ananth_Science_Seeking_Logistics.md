# Team PsychIGoR for ARPA-H IGoR: the science, who we are seeking, and logistics

**For Ananth. Internal alignment ahead of partner outreach. Not for distribution.** Updated 2026-06-14.

## The science we are proposing

**Thesis.** Treat **disease-associated genetic variation as a causal soft intervention** on cell state, and learn a model that separates disease from treatment. This makes the disease model causal and updatable, not correlational, which is exactly what IGoR's closed loop needs.

**TA1, comprehensive disease models (our core, in-house).** Four pillars:

- **Paired clinical and cellular modeling.** Isogenic iPSC pairs and patient clinical cohorts live in **one pathway-space shift model**, so cellular and clinical evidence constrain the same disease axes and culture artifacts (for example differentiation effects) do not masquerade as disease signal.
- **Genomic factorization.** We initialize from **pretrained genomic foundation models** and factor the result into a small set of sparse, interpretable, transdiagnostic **disease-axis factors** that double as candidate biotypes. The detailed method is proprietary; novelty is claimed precisely against the nearest published pathway-score precedent.
- **Causal generative modeling.** A **three-latent structural causal model** separates the cell's **basal state**, the **disease effect** (causal on cell state), and a **treatment effect** that acts either directly on the cell (a side-effect route) or by modulating the disease (the therapeutic route). This makes efficacy versus side-effect liability an identifiable prediction.
- **Ontology-conditioned experiment design** feeding TA2.

**TA2, the New Science Engine (we lead).** A non-LLM-wrapper engine that interrogates the **TA1 model's own** uncertain parameters and conflicting edges to choose the highest-value experiment, through a hypothesis tournament, model-grounded planning, and test-time simulation pre-screening.

**Phase I anchor, the phenotypic-triage screen.** Across the penetrant-variant panel (22q11.2 and TBX1, plus high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, GRIA3, CUL1), engineered as **isogenic pairs**, we measure **transcriptomic, morphological, and functional calcium-imaging** phenotypes, extending Anne Carpenter's published 22q11 Cell Painting work to more variants and readouts, to select the lines and disease axes the model is built on.

## Who we are seeking, by technical area

> **TA1 stays in-house** (Cytognosis, IPAI, and students). The only adjacent exception is the genomic sequence-to-embedding step (Francesco Paolo Casale), inside or outside IGoR.

| TA | Need | Top targets (priority order) | Status |
|---|---|---|---|
| **TA2** | Optional add-ons; we lead | SIFT (planning and scheduling), Phylo (Kexin Huang, warm) | Outreach |
| **TA3** | One interoperable-protocol lead | SIFT / LabOP (Dan Bryce), with Tim Fallon (UCSD) as alt or co-lead; Triple Ring for ARPA-H-grade systems and compliance | Email ready |
| **TA4 academic arm** | Academic experimental lab (runs all wet-lab experiments) | Matt Tegtmeyer lab, Purdue (confirmed 2026-06-15); fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing) | Confirmed |
| **TA4 industry arm** | Industry execution partner | Cellanome (R3200; live-cell imaging, same-cell scRNA-seq, Perturb-LINK CRISPR); advancing, 2026-06-17 call; operating model under discussion | Advancing |
| **TA4 computational** | Interpretable morphology and imaging models | Anne Carpenter (IPAI/Purdue); purely computational, no wet bench; consumes readouts from both TA4 arms | Committed ~90% |
| **TA4 sequencing** | High-throughput sequencing add-on | Illumina (warm via Sebastian Pineda) | Outreach |

**Worth your attention.** **Triple Ring Technologies** is a **confirmed ARPA-H awardee** (POSEIDON) and can carry systems integration, ISO compliance, and ARPA-H contracting know-how. (Operant BioPharma looked like a neuro TA4 fit on science, but their teaming post shows they want to be the disease-model anchor and are seeking capabilities we do not provide, so they are parked.) The functional readout is single-cell **calcium imaging**, an imaging modality our live-cell and high-content partners already cover, so there is no separate electrophysiology-lab gap. Full comparison in `CANDIDATE_DOSSIER.md`.

**TA4 two-arm structure.** Matt's academic lab and Cellanome together satisfy the program's at-least-two-labs requirement. They are complementary: Matt's lab runs fixed-cell high-plex readouts at high scale (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing); Cellanome provides live-cell and temporal readouts the fixed-cell academic arm cannot. A Phase I cross-platform concordance run (same iPSC samples through both arms) maps directly onto the program's concordance gates and frames the comparison as a built-in reproducibility milestone, not a competition. Anne Carpenter's computational morphology models are the common analysis layer across both arms.

**Parallel-candidate rule.** Several candidates are in parallel discussion. We never imply anyone is committed, and we never signal an empty roster; we say we are "in active discussion and finalizing the experimental team." NDAs route through Duane Valz.

**Status as of 2026-06-18.** **Dan Bryce** (SIFT, TA3 plus scoped TA2 VOI planning) formally accepted 2026-06-18. **SPOC** declined 2026-06-18. **Kexin Huang** (Phylo, TA2) is awaiting reply. **Anna Merkoulovitch** (architect candidate) is off market; architect role is a planned Cytognosis hire (recruiting), with Elham Jebalbarezi Sarbijan (IPAI) as interim placeholder.

## Logistics

- **Prime and PI:** IPAI, Purdue University; Ananth Grama. **Team name:** PsychIGoR. **TA1/TA2 lead:** Cytognosis (Shahin). **Clinical:** Brad Ruzicka, McLean (cohort interpretation and data governance, no new clinical trials). **TA4 academic arm:** Matt Tegtmeyer lab, Purdue (wet-lab experiments, fixed-cell high-plex readouts). **TA4 industry arm:** Cellanome (advancing). **TA4 computational:** Anne Carpenter (IPAI/Purdue; interpretable morphology and imaging models; no wet bench). **PM:** Patricia Purcell (part-time). **Architect:** planned Cytognosis hire (recruiting); Elham Jebalbarezi Sarbijan (IPAI) interim architect.
- **Budget and structure:** about **$50M over five years**, three phases (roughly 18, 18, 24 months), phase-gated. OT agreement (flexible IP and data rights).
- **Disease framing:** schizophrenia, extending to bipolar; penetrant genetic forms as isogenic cellular models.
- **Openness and IP:** open standards and reproducibility by design (a fit for the ARPA-H mandate); our proprietary methods are firewalled and marked where they appear.
- **Human subjects:** existing or biobank, de-identified samples and secondary analysis only (PsychENCODE, ROSMAP, McLean data); FWA and IRB in place; no new human-subjects research in scope.
- **Deadlines:** Solution Summary **June 25, 2026**; full proposal **early August 2026**.

**Immediate asks of you.** Confirm IPAI-prime resourcing (students and postdocs for TA1/TA2); react to the TA4 target set (Carpenter, Cellanome, Illumina, with Xaira as a stretch); confirm the TA3 route (SIFT versus UCSD for LabOP); and flag anyone in your network for the TA3 and TA4 roles.

**Contact.** Shahin Mohammadi, mohammadi@cytognosis.org.
