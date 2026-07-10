# Neuroverse: A Multiscale, Multimodal Foundation Model and Universal Coordinate System for the Human Brain and Psyche

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**A Cytognosis Foundation research program**
**In collaboration with McLean Hospital / Mass General Brigham and Purdue University**

---

## 1. The Problem

Psychiatric and neurodegenerative conditions remain organized around categorical diagnoses defined by symptom clusters. This framing has known limitations: most psychiatric diagnoses share substantial genetic, neural, and behavioral structure with neighboring diagnoses; within any single diagnosis, patients differ dramatically in their underlying biology; and even when biologically meaningful subtypes are discovered, they are typically defined on a single disorder using a single modality, leaving the field with a patchwork of partial maps that do not compose.

What is missing is a unified, individual-level coordinate system that places every person on a continuous map of brain function, structure, molecular biology, and behavior. Such a map should be:

- **Structurally accurate across disorders.** The known relationships between conditions (the genetic overlap between schizophrenia and bipolar disorder; the developmental continuity between autism and schizophrenia; the dimensional structure described by RDoC and HiTOP; the cross-disorder genotypic factors recovered from large GWAS studies) should be recoverable from coordinates on the map, not imposed onto it.
- **Diagnostically informative within disorders.** Published biotypes for depression, psychosis, autism, and Alzheimer's disease, even when defined on a single disorder using a single modality, should be recoverable from a person's coordinates derived from a different modality entirely. A biotype defined on functional connectivity should survive translation to a coordinate derived from gene expression, and vice versa.
- **Sensitive to within-person change under treatment.** A person's position on the map should shift in interpretable, reproducible directions when they receive an intervention that works for them; treatment responders and non-responders should separate cleanly in the coordinate space.

The Neuroverse program builds this map.

---

## 2. The Approach

Cytognosis, in collaboration with the Ruzicka group at McLean Hospital and the Grama group at Purdue's Physical AI Center, will train a multiscale, multimodal foundation model on the largest available aggregation of human brain and behavioral data, spanning postmortem genomics and single-cell molecular profiles, structural and functional neuroimaging, behavioral and cognitive assessments, and clinical phenotype. The model learns a continuous coordinate system over individuals, which we call the Neuroverse.

The Neuroverse coordinate system is not a classifier. It is a representation. A new individual projected into the Neuroverse occupies a position that captures their structural risk, their functional state, their molecular profile, and their behavioral patterning, jointly. Downstream uses, including diagnosis, biotype assignment, treatment selection, and trajectory forecasting, are derived from operations on these coordinates.

The model architecture is foundation-model in design: pretrained on the full data aggregation, then adapted to specific scientific and clinical tasks through lightweight downstream models. Pretrained weights and the canonical coordinate system are open by default; downstream models can be retrained for specific populations and questions.

---

## 3. The Three-Level Validation Framework

Neuroverse must be validated against three operationally distinct claims. Each level has its own datasets and its own metrics. A model that satisfies one level but fails another is not yet the Neuroverse we are building.

### Level 1: Transdiagnostic structural accuracy across disorders

**Claim.** The Neuroverse coordinate system recapitulates known cross-disorder relationships and localizes psychiatric and neurodegenerative diagnoses in a manner consistent with established transdiagnostic frameworks.

**Anchors.** RDoC functional domains, HiTOP spectra and subfactors, the five published genotypic factors spanning fourteen psychiatric disorders from cross-disorder GWAS factor analyses, the p-factor literature, and the cross-disorder genetic correlation matrices from the Psychiatric Genomics Consortium.

**Metrics.**
- Canonical correlation and Procrustes alignment between Neuroverse latent axes and HiTOP spectra.
- Cophenetic correlation between Neuroverse-derived disorder dendrograms and published transdiagnostic hierarchies.
- Rank preservation (Spearman) between Neuroverse-derived disorder coordinates and PGC cross-disorder genetic correlation matrices.
- ROC-AUC for diagnosis-versus-control separation per disorder, plus the disorder-versus-disorder separation matrix.

### Level 2: Within-disorder biotype recovery

**Claim.** The Neuroverse captures within-disorder heterogeneity and recapitulates published disease-specific biotypes, despite those biotypes having been defined on single disorders, often using a single modality.

**Anchors.** Drysdale et al. depression biotypes; Clementz et al. psychosis biotypes from B-SNIP; cell-type subtype panels from the recent multi-cohort schizophrenia and bipolar genomics work; AD subtypes from ROSMAP.

**Metrics.**
- Adjusted Rand Index and Normalized Mutual Information between Neuroverse-derived clusters and published biotype labels on shared individuals.
- Cross-modality biotype recovery: biotypes defined on fMRI should be recoverable from Neuroverse coordinates derived from molecular data alone, and vice versa.
- Silhouette and stability metrics for Neuroverse-discovered subtypes under consensus clustering across resamples.
- Out-of-sample biotype prediction AUC on held-out cohorts.

### Level 3: Sensitivity to individual treatment effects

**Claim.** Neuroverse coordinates shift in interpretable, reproducible directions under intervention. The shifts are large enough to separate treatment responders from non-responders, stable enough to be reliable in untreated subjects, and continuous enough to track session-level changes in densely-sampled individuals.

**Anchors.** Public and shared pre/post intervention datasets (TMS for depression, ketamine, SSRI); densely-sampled longitudinal cohorts where available; ABCD repeated-measures developmental trajectories as a developmental analog.

**Metrics.**
- Effect size (Cohen's d) of Neuroverse coordinate shifts pre-versus-post intervention, against permuted baselines.
- Intraclass correlation coefficient for individual coordinates in untreated subjects (test-retest reliability).
- Responder-versus-non-responder separability AUC in coordinate space.
- For densely sampled individuals, trajectory recovery: session-level coordinate changes recovered against published session-level annotations.

---

## 4. Why These Three Levels, Together

Each level alone is insufficient.

A model that satisfies only Level 1 is a classifier that organizes diagnoses but does not see individuals. A model that satisfies only Level 2 reproduces published clusters but does not place those clusters in a broader space, and does not generalize to new disorders. A model that satisfies only Level 3 captures within-individual dynamics but does not provide the cross-individual frame of reference needed to interpret those dynamics.

A model that satisfies all three levels is the map we want: cross-disorder by construction, individual-level by construction, and dynamic enough to track change. The validation framework forces the model design to honor all three constraints, not optimize one at the expense of the others.

---

## 5. The Data Aggregation

The Neuroverse is trained on a carefully selected aggregation of existing, consented, controlled-access research data spanning the full set of relevant modalities and a broad sample of psychiatric and neurodegenerative phenotypes. All initial data are reanalyses of already-published or already-released-under-DUC cohorts.

**Postmortem genomic and single-cell.** NeuroBioBank, PsychENCODE, PsychAD, ROSMAP. These contribute the molecular-level resolution needed to anchor disease axes in cell-type-specific transcriptional and chromatin states, and to validate against the recent multi-cohort genomic work in schizophrenia, bipolar disorder, and Alzheimer's disease.

**Connectomic and structural neuroimaging.** Human Connectome Project, ABCD, B-SNIP, UK Biobank, and the relevant ENIGMA Consortium working groups for cross-disorder neuroimaging. These contribute functional and structural brain measurements at scales from individual subjects (HCP) to hundreds of thousands of participants (UK Biobank).

**Transdiagnostic clinical cohorts.** FondaMental FACE cohorts (autism spectrum, bipolar disorder, treatment-resistant depression, schizophrenia, with biospecimens), and over time, All of Us, Million Veteran Program, and institutional biobanks at Mass General Brigham, Mayo Clinic, and Mount Sinai for clinical and EHR depth.

**Cross-disorder genomics.** Psychiatric Genomics Consortium summary statistics provide a population-genetic baseline against which Neuroverse genetic structure is evaluated; PGC individual-level data, where accessible, provide independent within-disorder genomic signal.

A complete dataset specification is maintained in a companion document; this strategy document gives the rationale for inclusion of each modality.

---

## 6. Why This Team, This Moment

The Neuroverse program assembles three groups with the right combination of platform, domain expertise, and computational depth:

**Cytognosis Foundation** brings the platform thesis (a continuous, disease-agnostic coordinate system for human health), the integrative computational framework, and the open scientific infrastructure to make the resulting model and its derived coordinates available to the broader research community.

**The Ruzicka group at McLean Hospital / Mass General Brigham** brings deep expertise in postmortem brain biology, recent leadership on multi-cohort genomic studies of schizophrenia, bipolar disorder, and related conditions, and direct institutional standing within the NeuroBioBank and PsychENCODE consortia.

**The Grama group at Purdue University's Physical AI Center** brings the computational architecture, high-performance computing infrastructure, and deep expertise in foundation-model training and large-scale neural network systems. The collaboration leverages an existing AD/ADRD P30 grant linking Cytognosis and Purdue.

This combination, postmortem molecular biology depth at McLean, connectomics and computational architecture at Purdue, and integrative platform leadership at Cytognosis, matches the structure of the data aggregation and the structure of the three-level validation framework directly.

---

## 7. Why Now

Three convergent developments make the Neuroverse program tractable at this moment:

1. **The dimensional transdiagnostic frameworks have matured.** RDoC and HiTOP are no longer aspirational; they are operational. The five cross-disorder genotypic factors and the broader p-factor literature provide concrete benchmarks for Level 1 validation.
2. **The relevant data is aggregable.** The cohorts named above did not exist together a decade ago. Today, NeuroBioBank, PsychENCODE, PsychAD, ROSMAP, ABCD, UK Biobank, B-SNIP, and the ENIGMA working groups collectively span the modalities and the disorders needed to train and validate a transdiagnostic foundation model. Programs like All of Us and MVP are adding population-scale depth.
3. **Foundation-model training methodology has matured.** Multimodal foundation models with hundreds of millions of parameters trained on heterogeneous data are now standard practice in computer vision, natural language, and biology. The transfer to neuroscience and psychiatry is the natural next step.

---

## 8. Outputs

The Neuroverse program produces three categories of output, all aligned with Cytognosis's openness policy:

**Open scientific outputs.** Peer-reviewed publications describing the model, the coordinate system, and the validation against all three levels; aggregate validation metrics and figures; documentation of the canonical disease axes and their molecular, neural, and behavioral correlates.

**Open model outputs.** Pre-trained weights for the Neuroverse foundation model under a permissive license, with documented evaluation showing no member-inference exposure of training-set individuals. Coordinate embeddings on consented public cohorts (HCP open-access tier, OpenNeuro, and equivalents). Training pipelines and configurations as open-source code in the Cytognosis GitHub organization.

**Derived analyses.** Application of the trained Neuroverse to specific scientific and clinical questions, leading to follow-on grants, publications, and translational programs. The first such applications will be transdiagnostic biotype mapping across the existing data aggregation; longitudinal trajectory modeling in ABCD; and treatment-response coordinate dynamics in cohorts with pre/post intervention data.

---

## 9. Beyond Neuroverse: The Broader Trajectory

Neuroverse is the first instantiation of Cytognosis's Cytoverse coordinate system, applied to brain and psyche as the first scientific domain. The same coordinate-system framework extends naturally to other disease areas (autoimmune conditions, anchored by ongoing work at the University of Manchester; metabolic conditions; oncologic conditions) and to other data modalities. The platform thesis is disease-agnostic by construction; psychiatric and neurodegenerative conditions are the entry point chosen because the data, the frameworks, and the team are ready for it now.

The success criterion for Neuroverse, beyond satisfying the three-level validation framework, is to serve as a working demonstration that a continuous, multimodal, individual-level coordinate system can be built, validated, and shared openly, and can outperform categorical diagnostic frameworks on questions that matter to patients and to the field.

---

## 10. Contact

| Role | Name | Institution |
|---|---|---|
| Principal Investigator | Shahin Mohammadi, PhD | Cytognosis Foundation |
| Site PI (genomics, single-cell) | Brad Ruzicka, MD PhD | McLean Hospital / Mass General Brigham / Harvard |
| Site PI (connectomics, computational architecture) | Ananth Grama, PhD | Purdue University |
| Inquiries | mohammadi@cytognosis.org | |
