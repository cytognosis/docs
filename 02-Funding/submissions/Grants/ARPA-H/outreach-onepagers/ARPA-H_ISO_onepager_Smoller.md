# From Cross-Disorder Genomic Architecture to a Mechanistic, Dimensional Map of Psychiatric Disease

**Outreach to:** Jordan W. Smoller, MD, ScD, Massachusetts General Hospital, Broad Institute; MGB Center for Precision Psychiatry.
**From:** Shahin Mohammadi, PhD, Founder & CEO, Cytognosis Foundation (501(c)(3)); TA1/TA2 sub-lead, PsychIGoR consortium (IPAI/Purdue prime, PI Ananth Grama).
**Contact:** mohammadi@cytognosis.org
**Date:** 2026-07-14

## Why we are writing

Your cross-disorder work (PGC, iPSYCH, the MGB precision-psychiatry program) has spent a decade demonstrating what the field now accepts: **psychiatric disorders are dimensional, transdiagnostic, and genetically shared across DSM categories**. Grotzinger et al. 2025 formalized this in a five-factor genomic scaffold across 14 disorders; the Ruzicka-Mohammadi single-cell atlas (*Science* 2024) formalized it at the cell type level for schizophrenia; the SCHEMA rare-variant series formalized it at the gene level; and the Beam-Etkin and Quah RDoC neuroimaging work formalized it at the circuit level.

What is still missing is a **single mechanistic model** that ties genotype to molecular pathway to cell type to circuit to symptom on a continuous, longitudinally updatable coordinate system, and that treats disease-associated genetic variation as the causal perturbation rather than as a correlational risk score. That is what we propose to build, and it is why we would like your input.

## The gap and the reframe

Two frames have dominated psychiatric genetics. One treats the polygenic score as a single blended risk number; the other treats individual credible sets as candidate targets. Neither yields a mechanistic model of how the genotype drives the cellular and circuit phenotype, and neither respects that patients with the same DSM label are biologically heterogeneous while patients across different labels share biology.

Our reframe: **disease-associated genetic variation is the causal perturbation operator** on a latent causal model of cellular biological processes, in the same identifiability setting as recent causal-disentanglement work with soft interventions (Zhang et al. 2023, Bereket-Karaletsos SAMS-VAE 2023). This inverts the virtual-cell paradigm (Bunne et al. 2024) so that natural population genetics is treated as the intervention, and it is what makes our model mechanistic, multiscale, and clinically grounded rather than correlational.

## The map: continuous, transdiagnostic, cell-type-aware, self-updating

We are building a **universal dimensional map of the human psyche** with four properties, each grounded in prior art:

1. **Continuous dimensional axes**, in the tradition of Surreal-GAN and the 9 dimensional neuroimaging endophenotypes (Nat Biomed Eng 2025), the 5 brain-aging dimensions (Nat Med 2024), and the MULTI Consortium organ-age axes (Nat Med 2026). Each axis is monotonic, disentangled, healthy-reference-anchored, and open to genetic validation.
2. **Transdiagnostic, aligned with Grotzinger 2025.** Axes map to your five-factor genomic scaffold (Compulsive, Schizophrenia-Bipolar, Neurodevelopmental, Internalizing, Substance Use) and to RDoC and HiTOP.
3. **Cell-type-aware.** Anchored in PsychENCODE brainSCOPE (24 cell types), PsychAD, and the Ruzicka-Mohammadi multi-cohort schizophrenia atlas, so a shift on a dimensional axis translates directly to a cell-type-specific gene program.
4. **Self-updating.** Ontology-conditioned, closed-loop, updates from every new experiment and every new patient cohort with sub-24-hour latency by Phase II. This is the TA1 core of our IGoR proposal, and it is not a wrapper around a large language model.

**We hold one method confidential.** A factorization approach to patient polygenic variation, which yields sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes, is under IP protection and not shared in outreach. Its precedent and precise novelty claim can be discussed under CDA.

## The penetrant anchor: 22q11.2 and TBX1

Idiopathic schizophrenia is mostly polygenic and hard to model in a dish. We anchor first on **penetrant, near-Mendelian forms**, exactly the move that made neurodegeneration cellular biology tractable through APP/PSEN1 for Alzheimer and LRRK2/SNCA for Parkinson.

| Handle | Evidence |
|---|---|
| **22q11.2 deletion syndrome** | Lifetime psychosis risk ~25%, pooled psychotic-disorder prevalence 11.5% (Schneider 2023), ~0.3-1% of schizophrenia cohorts, spans PRODH, DGCR8, COMT, TBX1, GNB1L |
| **TBX1 (used precisely)** | Tbx1+/- mice show reduced PPI (Paylor 2006), corticogenesis disruption (Vitelli 2017), oligodendrocyte myelination deficits (Kim-Bhatt 2025). We frame TBX1 as a high-penetrance developmental handle within 22q11DS, not as a nonsyndromic schizophrenia gene (Funke 2007 caveat stated up front) |
| **High-OR SCHEMA genes** | SETD1A, CUL1, XPO7, GRIN2A, GRIA3, CACNA1G, TRIO, SP4, HERC1, RB1CC1 (Singh et al. 2022) |

The Phase I anchor experiment is a **phenotypic-triage screen across isogenic iPSC pairs** (CRISPR-introduced variants on a common healthy background, paired with matched controls). We measure transcriptomic (scRNA-seq), morphological (Cell Painting), and functional (single-cell calcium imaging) phenotypes across the penetrant-variant panel, producing a ranked variant-to-phenotype map. Strong-signal lines anchor the causal model; the axes then project idiopathic, polygenic schizophrenia onto the same coordinate system, which is the Phase III generalization to transdiagnostic psychiatry.

The founder identity is worth stating once. Shahin's 37-year diagnostic odyssey resolved through self-directed genomic analysis identifying an ultra-rare TBX1 mutation; that specific personal-genomic anchor sits in a restricted section of the proposal and is used with care. The scientific case for TBX1 stands or falls on the published evidence, not the personal one.

## What we would value from you

- **A conversation on the transdiagnostic framing** and whether the five-factor Grotzinger scaffold is the right axis system to align on, or whether an alternative (HiTOP, RDoC, an emergent factor structure from the map itself) is preferable as the reference frame.
- **Input on the penetrant-anchor strategy** vs. an alternative anchor set (e.g., high-OR SCHEMA genes as primary, 22q11.2 as secondary).
- **Guidance on cohort access** for translational validation (MGB Biobank, PGC data, iPSYCH linkages) at Phase III.
- **Whether a formal collaboration role fits** the MGB Center for Precision Psychiatry; the consortium has room for a translational-genetics anchor at McLean/Broad/MGB.

The PsychIGoR consortium is fully assembled (IPAI/Purdue prime with Ananth Grama as PI; Cytognosis TA1/TA2 sub-lead; Matt Tegtmeyer lab at Purdue for wet-lab experiments; Anne Carpenter at IPAI/Purdue for computational morphology; Brad Ruzicka at McLean/HMS for clinical co-lead; SIFT for TA3; Cellanome for live-cell perturbation; Illumina for perturbation-scale sequencing). Solution Summary submitted 2026-06-25; $42.9M full proposal due 2026-08-13.

**Shahin Mohammadi, PhD.** Founder & CEO, Cytognosis Foundation. Twenty years in computational biology (MIT, Broad Institute, insitro, GenBio AI); first author on the Ruzicka-Mohammadi *Science* 2024 multi-cohort schizophrenia single-cell atlas; co-author on the Mathys-Mohammadi *Nature* 2019 ROSMAP Alzheimer atlas. Cytognosis Foundation is a 501(c)(3) built to release the map openly, so precision psychiatry becomes a human right, not a privilege.
