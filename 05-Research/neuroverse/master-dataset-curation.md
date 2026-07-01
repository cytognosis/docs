> **Status:** Active · **Date:** 2026-05-07 (authored), 2026-07-01 (canonicalized) · **Author:** Cytognosis Foundation
> **Canonical home:** `05-Research/neuroverse/master-dataset-curation.md` · **Consolidated from:** `Science and Platform/cytognosis_master_dataset_curation.md`.
> **Paired data table:** `~/datasets/cytognosis/curations/master/cytognosis_master_dataset_curation.xlsx` (the XLSX is the data; this is the narrative).

# Cytognosis Foundation Master Dataset Curation
## Critical Datasets for Neuro Foundation-Model Training

**Author:** Cytognosis Foundation (curation orchestrated by Claude with deep-dive subagent research)
**Date:** 2026-05-07
**Companion artifact:** `cytognosis_master_dataset_curation.xlsx` (structured curation table, modality and disorder matrices, paired-modality availability)
**Predecessor inputs:** `NeuroSTORM_datasets.csv` (NeuroSTORM-derived neuroimaging cohorts, March-May 2026), `multimodal_coembedding_review_2025_2026.md` (architectural review for paired multi-scale patient data), `multimodal_coembedding_addendum_deep_dives.md`.

---

## 0. Reading Guide

This document is the canonical reference for which datasets Cytognosis Foundation will use to pretrain, fine-tune, and evaluate foundation models across the five Cytoverse modalities (genomic, single-cell, connectomic, phenotypic/behavioral, physiological), individually and in paired-multimodal configurations. The aim is not breadth for its own sake; the aim is to give every model designer a precise, governance-aware shopping list, with sample counts that admit honest power calculations and license terms that admit honest publication strategies.

Skim path for someone planning a new model: read Section 1 (strategic stack), Section 6 (paired-modality matrix), then jump directly to the dossier(s) for your top three target datasets in Sections 7 through 13. Read Section 14 (implementation roadmap) before kicking off ingestion.

Deep path for governance and openness review: read Sections 2 (curation schema), 3 (access tier definitions), 5 (FAIR alignment), and the access subsections of every dossier.

The companion XLSX provides the same content as a structured table for filtering, plus three derived sheets: modality coverage, MONDO disorder coverage, and paired-modality availability.

---

## 1. Strategic Overview: A Step-Wise Foundation-Model Stack

Cytognosis builds foundation models that learn the geometry of patients across modalities. We will not jump to a fully multimodal model on day one. The honest path is a staircase, and the steps are dictated by which datasets pair which modalities at which scales.

### 1.1 The five Cytoverse modalities and their canonical pretraining substrates

The table below states, for each modality, which datasets are large enough to drive a serious single-modality foundation model and which secondary datasets supply diversity, robustness, or disease coverage.

| Modality | Primary pretraining substrate | Secondary substrate | Anchor scale |
|---|---|---|---|
| Genomic (germline) | UK Biobank WGS (490,640), All of Us WGS (414,000), MVP genotyping (1M+) | BioMe, MGBB, NeuroBioBank WGS Catalog | ~1M individuals total |
| Single-cell omics | PsychAD (1,494 donors, 6.3M nuclei), ROSMAP-Compass (2,058 donors, 22M nuclei), PsychENCODE2 brainSCOPE (388 donors, 2.8M nuclei), AMP-AD aggregated | AMP-PDRD multi-region (130 donors), AMP-ALS (~200 donors snRNA-seq) | ~2,500 donors, ~30M nuclei |
| Connectomic (brain imaging) | UK Biobank (~60,000 with rs-fMRI plus DTI), ABCD (~11,500), HCP family via CCF (~5,500), OpenNeuro public (~25,000+ rs-fMRI sessions), INDI (~10,000) | ADNI (~3,500), PPMI (~4,000), ENIGMA-pooled federated (>100,000 T1) | ~150,000 imaging sessions accessible |
| Phenotypic/behavioral | Human Phenotype Project (~13,000 deeply phenotyped), UK Biobank instruments (~500,000), All of Us surveys (~800,000) | ABCD instruments, B-SNIP/PARDIP biotype batteries, FACE/PSY-COH | >1M phenotype profiles |
| Physiological/clinical EHR | MGB PDSR Curated (~7M patients), MSDW (~12M), Mayo Clinic Platform (~10M Mayo plus ~54M federated), All of Us (~500K linked), MVP (~1M VA EHR) | UK Biobank linked NHS, BioMe, MGBB | ~80M patient records |

### 1.2 Stage-wise multimodal stack

The stack moves from large unpaired data toward small, deeply-paired data, exactly mirroring how production-grade foundation models scale.

**Stage 1 (now through Q4 2026): Single-modality pretraining on the largest possible substrate per modality.**
- Genomic FM: pretrain on UKB plus AoU plus MVP open summary statistics, ancestry-balanced.
- Single-cell brain FM: pretrain on PsychAD plus ROSMAP-Compass plus brainSCOPE.
- Connectomic FM: pretrain on UKB plus ABCD plus HCP-family plus OpenNeuro plus INDI; harmonize across sites.
- EHR FM: pretrain on MGB PDSR Curated plus MSDW plus Mayo Discover (in-enclave), with All of Us as cross-validation.
- Phenotype FM: pretrain on UKB instruments plus AoU surveys plus HPP deep panels.

**Stage 2 (Q1 through Q4 2027): Pairwise multimodal pretraining on cohorts that natively pair two modalities.**
- Genomic plus connectomic: UKB (~60,000 with WGS plus rs-fMRI plus DTI) is the dominant resource; supplement with ENIGMA-genetics federated meta-analyses.
- Genomic plus EHR: UKB plus AoU plus MGBB plus BioMe plus MVP, the largest paired set in the world.
- Genomic plus single-cell: ROSMAP plus PsychAD plus PsychENCODE2 plus AMP-AD diverse cohorts (each donor has WGS plus snRNA-seq).
- Connectomic plus phenotype: ABCD plus HCP family plus HBN plus YaleNeuroConnect plus TCP, transdiagnostic.
- Single-cell plus EHR: ROSMAP, PsychAD MSSM arm, AMP-PDRD postmortem (linked clinical history).

**Stage 3 (2027 through 2028): Triple-modality pretraining on cohorts where three modalities co-occur in the same individual.**
- Genomic plus connectomic plus EHR plus phenotype: UK Biobank is the only substrate at population scale; the goal is a UKB-anchored Cytoverse foundation model that we then transfer to Mayo, MGB, Mt Sinai, ABCD, HCP, AoU.
- Genomic plus single-cell plus EHR: ROSMAP (clinical-pathological), PsychAD (Mount Sinai EHR-linked), AMP-AD diverse cohorts.
- Connectomic plus phenotype plus single-cell (postmortem): a small but high-value frontier; PsychENCODE2 plus PsychAD plus ENIGMA imaging cross-references.

**Stage 4 (2028+): Full Cytoverse multimodal foundation model, anchored on Cytognosis-generated cohorts where all five modalities are paired in vivo at the same temporal resolution.** External datasets feed this only as initialization checkpoints and held-out evaluation cohorts.

### 1.3 Why federation matters more than central download

Several of the most valuable datasets (ENIGMA, MGB PDSR, MVP, Mayo Clinic Platform, AMP-PDRD, FACE) cannot be ingested centrally. They are accessed via federated meta-analysis, in-enclave compute, or VA-only/Mayo-only credentialing. Cytognosis must therefore design its training infrastructure to support both local-pretraining-then-export-weights workflows and federated-statistics protocols. This is consistent with the Cytognosis openness policy: train inside, release model weights and aggregate statistics outside, and never re-distribute individual-level data.

### 1.4 Why ancestry, age, and sex balance must be designed in, not retrofitted

UKB skews 94% European; ABCD skews mid-childhood; HCP skews young adult; AMP-AD diverse-cohorts release was added precisely to correct ancestry imbalance; All of Us was designed for ancestry diversity; CCNP (within INDI) provides a Chinese lifespan anchor. Single-modality FMs that ignore this calibration produce biased downstream predictions. The companion XLSX flags ancestry skew per dataset; pretraining curricula should mix datasets in proportions that reduce European/North-American skew, not amplify it.

---

## 2. Curation Schema and Field Definitions

Every dataset dossier in this document follows the same schema. Field definitions are below; the same fields appear as columns in the companion XLSX.

| Field | Definition |
|---|---|
| Dataset short name / full name | Common abbreviation plus canonical full title used by the host organization |
| Short description | 2-4 sentence cohort summary including size, population, design, and primary aim |
| Latest/most significant reference | Most recent flagship publication (2024-2026 where available); foundational paper if needed for context |
| Access requirements: Obtain data | Application route, eligibility, expected approval timeline, fees |
| Access requirements: Use restrictions | Permitted research uses, prohibitions, embargoes, recontact rules |
| Access requirements: Storage requirements | Whether data must stay on a host platform/enclave or can be downloaded; encryption and audit obligations |
| Access requirements: What can be shared back | Whether trained models, summary stats, derived features, or full data can be redistributed under what terms |
| Links: Main website | Canonical landing page |
| Links: Access request page | Specific URL where investigators apply or click through to a DUA |
| Links: Data repository / portal | Where data actually lives (Synapse, NDA, dbGaP, AWS S3, LONI IDA, Terra, ConnectomeDB) |
| Pathologies (MONDO mapping) | Disorders represented at meaningful sample size, mapped to MONDO codes from the Cytognosis priority list |
| Available data types and sample counts | Per-assay sample counts using OBI and NCIT ontology terms (see Section 4) |
| Foundation-model training adoption | 2-5 recent papers (2023-2026) that used the dataset to train or evaluate large/foundation models, taken as a proxy for adoption and reliability |
| Notes for Cytognosis platform integration | Practical considerations for Cytognosis ingestion, governance, and public model release |

---

## 3. Access Tier Definitions

To make tier-based decisions consistent across dossiers, the following tier system is used.

- **Tier 0, Open download under permissive license.** No application; CC0, CC BY, or CC BY-NC. Examples: OpenNeuro, INDI/FCP, ABIDE I/II, ADHD-200, COBRE, PGC summary statistics.
- **Tier 1, Click-through DUA, downloadable.** Free registration, sign a DUA online, download. Examples: ADNI, PPMI, ROSMAP via RADC, AMP-AD Synapse open tier, NBB tissue request workflow.
- **Tier 2, Application plus IRB-equivalent attestation, downloadable to institution.** Reviewed application with institutional signing-official; data downloads to investigator's secured infrastructure. Examples: ABCD via NBDC Data Hub, HCP-EP via NDA, B-SNIP via NDA, PARDIP via NDA, PsychENCODE Tier 1 raw data, ROSMAP via Synapse controlled.
- **Tier 3, In-enclave compute only.** Data cannot leave the host platform; researcher analyzes in a hosted environment. Examples: UKB (UKB-RAP on DNAnexus/AWS), All of Us (Researcher Workbench on Terra/Google), AMP-PDRD (Terra/Verily), Mayo Clinic Platform (Mayo Cloud), MGB PDSR Curated (MGB Analytics Enclave), MSDW (Minerva HPC), MGBB (MGB enclave), BioMe (Minerva HPC), RPDR (MGB ERIS).
- **Tier 4, Federated, no central data download.** Investigators run standardized pipelines locally, return summary statistics. Examples: ENIGMA working groups, PGC individual-level (SAP route), AMP-PDRD federated layer.
- **Tier 5, Institutional-membership-only.** Effectively gated to organization-affiliated investigators. Examples: MVP (VA-only or sponsored collaborator), Mayo Clinic Platform Discover (subscription), MGB PDSR Curated (MGB-only).

The tier number governs Cytognosis ingestion strategy: Tier 0/1 datasets feed central pretraining corpora; Tier 2 require enclave on Cytognosis side; Tier 3/5 require local compute and weight-export governance; Tier 4 require partnership and pipeline distribution.

---

## 4. Ontology Codes Used Throughout

### 4.1 MONDO disease codes (Cytognosis priority list)

| Disorder | MONDO code |
|---|---|
| Tourette Syndrome | MONDO:0007661 |
| Anorexia Nervosa | MONDO:0005351 |
| Obsessive-Compulsive Disorder | MONDO:0008114 |
| Major Depressive Disorder | MONDO:0002009 |
| Anxiety Disorder | MONDO:0005618 |
| Post-traumatic Stress Disorder | MONDO:0005146 |
| Autism Spectrum Disorder | MONDO:0005258 |
| Attention Deficit-Hyperactivity Disorder | MONDO:0007743 |
| Alcohol Dependence | MONDO:0007079 |
| Opioid-use Disorder | MONDO:0005530 |
| Nicotine Dependence | MONDO:0008575 |
| Cannabis-use Disorder | MONDO:0005689 |
| Schizophrenia | MONDO:0005090 |
| Bipolar Disorder | MONDO:0004985 |
| Alzheimer disease | MONDO:0004975 |
| Parkinson disease | MONDO:0005180 |
| frontotemporal dementia | MONDO:0017276 |
| Lewy body dementia | MONDO:0007488 |
| Huntington disease | MONDO:0007739 |
| amyotrophic lateral sclerosis | MONDO:0004976 |
| multiple sclerosis | MONDO:0005301 |
| Dementia | MONDO:0001627 |
| Neurodegenerative diseases (3+ neurodegen mix) | MONDO:0005559 |
| Neuropsychiatric disorders (3+ psychiatric mix) | MONDO:0002025 |
| Brain disorders (very mixed) | MONDO:0005560 |

### 4.2 Assay ontology codes (OBI and NCIT)

**Genotype (DNA):**
- DNA sequencing assay (OBI:0000626)
  - WGS: whole genome sequencing assay (OBI:0002117)
  - WES: exome sequencing assay (OBI:0002118)
- Genotyping by array
  - SNP array: genotyping by SNP array assay (OBI:0001274)
  - Tiling array: genotyping by tiling array assay (OBI:0002030)

**Cellular omics:**
- RNA sequencing
  - scRNA-seq: single-cell RNA sequencing assay (OBI:0002631)
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109)
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090)
- Chromatin accessibility (OBI:0003686 umbrella)
  - scATAC-seq: single-cell ATAC-seq (OBI:0002764)
  - snATAC-seq: single-nucleus ATAC-seq (OBI:0002762)
  - Bulk ATAC-seq: bulk assay for transposase-accessible chromatin using sequencing (OBI:0003089)

**Brain imaging (NCIT):**
- PET: Positron Emission Tomography (NCIT:C17007)
- DTI: Diffusion Tensor Imaging (NCIT:C64862)
- fMRI: Functional Magnetic Resonance Imaging (NCIT:C17958)
  - rs-fMRI: Resting Functional MRI (NCIT:C178024)
  - task-fMRI: Task Functional MRI (NCIT:C178023)
- fNIRS: Functional Near-Infrared Spectroscopy (NCIT:C175235)
- EEG: Electroencephalography (NCIT:C38054)
- MEG: Magnetoencephalography (NCIT:C16811)

**Clinical and instruments:**
- EHR: Electronic Medical Record (NCIT:C45259)
- Instruments: Clinical or Research Assessment Question (NCIT:C91102)

---

## 5. Openness and FAIR Alignment

Cytognosis releases foundation-model weights and metadata under Apache 2.0 (code) and CC BY 4.0 (documentation, derived data). Every dataset listed below is compatible with this stance under at least one usage pathway:

- Tier 0 datasets (OpenNeuro, INDI summary releases, PGC summary statistics) are unconditionally compatible.
- Tier 1 datasets (ADNI, PPMI, ROSMAP, NBB-derived deposits) permit released model weights and summary statistics provided the original DUA acknowledgements and citations are honored.
- Tier 2 datasets (NDA-routed cohorts, AMP-AD controlled, PsychENCODE controlled) permit released weights provided no individual-level data is memorized; we will document the relevant data card and cite contributing studies.
- Tier 3 datasets (UKB, AoU, AMP-PDRD, Mayo, MGB, Mt Sinai) require enclave training; only weights and aggregate statistics may be exported. We must publish data cards listing the exact UKB application reference, AoU workspace ID, and MGB project number.
- Tier 4 datasets (ENIGMA, federated PGC) permit only summary-statistics meta-analytic outputs.
- Tier 5 datasets (MVP, Mayo Discover subscription) require operational partnership.

FAIR alignment is automatic for Tier 0 through Tier 2 datasets that carry persistent identifiers; Tier 3+ datasets satisfy FAIR via metadata (findable and interoperable) even when the data itself is restricted. We will include FAIR statements in every model card produced from these substrates.

---

## 6. Cross-Cutting Modality and Disorder Matrices

The companion XLSX (`cytognosis_master_dataset_curation.xlsx`) carries fully detailed matrices. The Markdown summary tables here highlight the most important paired-modality opportunities.

### 6.1 Paired modality availability (selected high-value pairs)

| Pair | Datasets with native pairing in same individuals | Approx aggregate n |
|---|---|---|
| WGS plus rs-fMRI | UKB (~60,000), HCP-YA SNP (~1,200 with imaging), ABCD (genotype + imaging on most), ADNI (~800 with WGS plus advanced MRI), PPMI (~700 with WGS plus rs-fMRI) | ~75,000 |
| WGS plus DTI | UKB (~60,000), ABCD, ADNI, PPMI | ~75,000 |
| WGS plus EHR | UKB (~490,000), AoU (~414,000), MVP (~102,000 WGS plus 650,000+ array, all with EHR), MGBB (~54,000 WES plus 65,000 SNP, with EHR), BioMe (~10,600 WGS plus 45,893 WES, with EHR) | >1,000,000 |
| WGS plus snRNA-seq | ROSMAP (~1,200 WGS plus 2,058 donors snRNA-seq), PsychAD (~1,200 WGS plus 1,494 donors snRNA-seq), AMP-AD aggregated (~4,000 WGS plus ~2,500 donors snRNA-seq), PsychENCODE2 (~1,000 WGS plus ~388 donors snRNA-seq) | ~5,000 donors |
| snRNA-seq plus snATAC-seq (multiome) | ROSMAP (~700 donors), PsychAD subsets, PsychENCODE2 (~616 donors snATAC) | ~1,500 donors |
| WGS plus snRNA-seq plus EHR | ROSMAP (clinical-pathological linked), PsychAD MSSM arm, AMP-PDRD postmortem, AMP-AD diverse cohorts | ~3,000 donors |
| rs-fMRI plus EEG | INDI Rockland (~1,000+), HBN, NIMH-HV, NeuroBureau, BioFIND/PPMI sub-substudies | ~2,500 |
| MRI plus PET (amyloid plus tau) | ADNI (~3,000 PET on ~3,500 imaging participants), PPMI (~1,500 DAT-SPECT), AMP-PDRD postmortem-linked | ~5,000 |
| Phenotype plus genotype plus imaging plus EHR | UKB (~60,000 imaging substudy), HPP (~13,000 deep phenotype plus genotype plus subset imaging plus EHR), ABCD (~11,500 imaging plus genotype plus EHR plus deep instruments) | ~85,000 |
| All five Cytoverse modalities in same individual | None at population scale; closest approximation is HPP (~1,000 with imaging plus genotype plus deep phenotype plus EHR plus partial omics); UKB approaches with bulk RNA-seq plus imaging plus genotype plus EHR plus deep phenotype on ~50,000 | ~1,000 to ~50,000 depending on definition |

### 6.2 MONDO disorder coverage (which datasets are usable for each priority disorder)

This summary maps each Cytognosis priority MONDO disorder to the datasets in this curation that contain it at meaningful sample size.

| MONDO disorder | Best-powered datasets |
|---|---|
| Tourette Syndrome (MONDO:0007661) | ENIGMA-TS (~1,930), PGC TS, ABCD (subset), NBB tissue |
| Anorexia Nervosa (MONDO:0005351) | ENIGMA-ED (685 cases), PGC ED, MGB/MSDW EHR, NBB |
| OCD (MONDO:0008114) | ENIGMA-OCD (2,323 cases), PGC OCD, ABCD, MGB/MSDW |
| Major Depressive Disorder (MONDO:0002009) | UKB (~37,400 lifetime in MHQ), AoU (large EHR), MVP (>250,000 GWAS cases), ENIGMA-MDD (>5,000), PGC MDD (>500,000 GWAS), FACE-DR, MGB/MSDW/Mayo |
| Anxiety Disorder (MONDO:0005618) | UKB, AoU, MVP, ENIGMA-Anxiety (140+ cohorts), PGC Anxiety |
| PTSD (MONDO:0005146) | MVP (>250,000), ENIGMA-PTSD (~3,047), PGC PTSD, ABCD (trauma-exposed subset) |
| Autism Spectrum Disorder (MONDO:0005258) | ABIDE I (539 cases) plus ABIDE II (521 cases), ENIGMA-ASD (>2,700), PGC ASD, FACE-Asp, ABCD, HBN |
| ADHD (MONDO:0007743) | ADHD-200 (~388 cases), ENIGMA-ADHD (~6,700), PGC ADHD, ABCD, AoU EHR |
| Alcohol Dependence (MONDO:0007079) | MVP, UKB MHQ (~7%), AoU EHR, ENIGMA-Addiction, PGC SUD, ABCD substance arm |
| Opioid-use Disorder (MONDO:0005530) | MVP, AoU, MGB/MSDW EHR, ENIGMA-Addiction, PGC SUD |
| Nicotine Dependence (MONDO:0008575) | UKB, AoU, MVP, ABCD, ENIGMA-Addiction, PGC SUD |
| Cannabis-use Disorder (MONDO:0005689) | AoU, MVP, ABCD substance arm, ENIGMA-Addiction, PGC SUD |
| Schizophrenia (MONDO:0005090) | MVP (~120,000 EHR), MGB/MSDW EHR, COBRE, HCP-EP, B-SNIP 1+2 (>1,000 SZ), PARDIP, ENIGMA-Schizophrenia (~5,673 cases), PGC SZ, FACE-SZ, PsychENCODE2, PsychAD, NBB |
| Bipolar Disorder (MONDO:0004985) | MGB/MSDW/Mayo EHR, B-SNIP 1+2, PARDIP, ENIGMA-Bipolar (>6,500), PGC BD, FACE-BD, PsychENCODE2, PsychAD, UKB MHQ |
| Alzheimer disease (MONDO:0004975) | ADNI (~3,500), AMP-AD aggregated, ROSMAP (~3,800), PsychAD (with AD pathology), Mayo MCP, MGB EHR, ENIGMA-AD/Aging (>34,700) |
| Parkinson disease (MONDO:0005180) | PPMI (~5,500), AMP-PDRD (~10,908), Mayo MCP, ENIGMA-PD (44 centers), MGB/MSDW EHR |
| Frontotemporal dementia (MONDO:0017276) | ALLFTD/ENIGMA-FTD multicenter, AMP-ALS (FTD-ALS spectrum), MGB/MSDW EHR, NBB |
| Lewy body dementia (MONDO:0007488) | AMP-PDRD LBD arm, ENIGMA-LBD, ROSMAP comorbid pathology, NBB, Mayo |
| Huntington disease (MONDO:0007739) | ENIGMA-HD (~1,700), HSG cohorts, NBB, MGB EHR |
| ALS (MONDO:0004976) | AMP-ALS (cross-portal ~6,000+ WGS), ENIGMA-ALS (~34,720 via UKB), Answer ALS iPSC, NYGC ALS Consortium |
| Multiple sclerosis (MONDO:0005301) | UKB (~2,500 prevalent), AoU, MGB/MSDW/Mayo EHR, IMSGC + ENIGMA-MS, NBB |
| Dementia (MONDO:0001627) | UKB linked NHS, ADNI, ROSMAP, AMP-AD, Mayo MCP, MGB/MSDW |
| Neurodegenerative diseases (MONDO:0005559) | AMP-AD, AMP-PDRD, AMP-ALS umbrella analyses, ENIGMA-AD/Aging, NBB |
| Neuropsychiatric disorders (MONDO:0002025) | PsychENCODE, PGC cross-disorder, ENIGMA cross-disorder, FACE/PSY-COH, B-SNIP/PARDIP, PsychAD |
| Brain disorders (MONDO:0005560) | NBB (148 CNS diagnoses), MGB PDSR/RPDR, MSDW, Mayo MCP, AoU, OpenNeuro |

---


## 7. Genotype-Centric Population Biobanks

These three biobanks supply >1 million genotyped individuals between them and are the canonical pretraining substrates for genomic foundation models, polygenic transformers, and EHR-plus-genome co-embeddings. UKB additionally pairs to imaging at population scale and is the single most adopted neurogenetic resource in 2024-2026.

### 7.1 UKB: UK Biobank

**Short description:** UK Biobank is a prospective population cohort of approximately 500,000 adults aged 40 to 69 at recruitment (2006 to 2010) drawn from 22 assessment centres across the United Kingdom (England, Scotland, Wales). The design pairs deep baseline phenotyping (lifestyle, anthropometrics, cognitive testing, biochemistry) with longitudinal linkage to NHS primary care, hospital, cancer, and death registries, complemented by genome-wide genotyping, whole-exome and whole-genome sequencing, plasma proteomics, NMR metabolomics, and a 100,000-participant multimodal imaging substudy. Its primary aim is to enable population-scale genotype-to-phenotype discovery for the common diseases of middle and later life.

**Latest/most significant reference publication:** Li, S., Carss, K. J., Halldorsson, B. V., Cortes, A., et al. "Whole-genome sequencing of 490,640 UK Biobank participants." Nature 645, 866 to 875 (2025). DOI: 10.1038/s41586-025-09272-9. PMC: PMC12443626. Foundational paper: Bycroft, C., Freeman, C., Petkova, D., et al. "The UK Biobank resource with deep phenotyping and genomic data." Nature 562, 203 to 209 (2018). DOI: 10.1038/s41586-018-0579-z.

**Access requirements:**
- *Obtain data:* Bona-fide researchers (any country; academic, commercial, charity, government) register via the Access Management System (AMS), submit a project application with a lay summary, designate an authorized signatory and approved collaborators, and undergo UK Biobank review. After approval (validity 90 days to execute), the institutional Material Transfer Agreement (MTA) is signed and the access fee is paid. End-to-end timeline is typically 2 to 4 months. Access fees use a tiered structure (full institutional rate vs. reduced rates of approximately 500 GBP for the first 3 years for low-income countries and student researchers); fees exclude VAT and platform compute.
- *Use restrictions:* Permitted for health-related research in the public interest as described in the approved application. Re-identification of participants is prohibited. Re-distribution of individual-level data is prohibited; data must remain on the UKB Research Analysis Platform (UKB-RAP). Findings must be published openly and returned to UKB.
- *Storage requirements:* Since 2024, all data access (with limited exceptions) occurs in the cloud-based UKB-RAP hosted on DNAnexus/AWS. Data may not be downloaded; analyses run on the platform. UKB stores dispensed data free of charge; researchers pay DNAnexus for compute, scratch storage, and egress of summary outputs. Annual usage reporting and audit logs are mandatory.
- *What can be shared back:* Trained models, summary statistics, derived features, and publication-ready figures may be exported subject to small-cell-suppression and aggregate thresholds. Full re-distribution of individual-level genotypes, sequences, or imaging is prohibited.

**Links:**
- Main website: https://www.ukbiobank.ac.uk/
- Access request page: https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/
- Data repository / portal: https://ukbiobank.dnanexus.com/ (UKB-RAP) and https://biobank.ndph.ox.ac.uk/ukb/ (Showcase)

**Included pathologies (MONDO mapping):** UKB is a population cohort but contains very large case counts for the following coded disorders (from MHQ self-report and ICD-10 hospital/primary-care linkage):
- Major Depressive Disorder (MONDO:0002009), lifetime prevalence approximately 24% in MHQ1 (about 37,400 cases in 157,366 respondents)
- Anxiety Disorder (MONDO:0005618), approximately 7%
- Post-traumatic Stress Disorder (MONDO:0005146), approximately 6%
- Alcohol Dependence (MONDO:0007079), approximately 7%
- Bipolar Disorder (MONDO:0004985)
- Schizophrenia (MONDO:0005090)
- Alzheimer disease (MONDO:0004975)
- Parkinson disease (MONDO:0005180)
- Dementia (MONDO:0001627)
- amyotrophic lateral sclerosis (MONDO:0004976)
- multiple sclerosis (MONDO:0005301), approximately 2,500 prevalent cases identified in linked data
- Brain disorders (MONDO:0005560), as the cohort spans the full breadth of psychiatric and neurological codes in NHS records.

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=490,640 (DRAGEN release 2, 2025)
  - WES: exome sequencing assay (OBI:0002118), n=454,787
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=488,377 (UK BiLEVE Axiom n=49,950; UK Biobank Axiom n=438,427)
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 50,000 (Pharma Proteomics extension and RNA-seq enhancement, partial release)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 60,000 (target 100,000)
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n=approximately 60,000
  - task-fMRI: Task Functional MRI (NCIT:C178023), n=approximately 60,000
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 500,000 (NHS HES, GP, cancer, death linkage)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 500,000 (baseline); MHQ1 n=157,366; MHQ2 (2022) n=approximately 170,000; cognitive testing n=approximately 500,000; plus Olink proteomics on approximately 55,000 participants and NMR metabolomics on approximately 275,000 participants.

**Foundation-model training adoption:**
- Cox, J., et al. "BrainSegFounder: Towards 3D foundation models for neuroimage segmentation." Medical Image Analysis (2024); pretrained on multimodal MRI from 41,400 UKB participants for downstream tumor and lesion segmentation.
- Liu, J., et al. "BrainFounder: Towards Brain Foundation Models for Neuroimage Analysis." arXiv:2406.10395 (2024); vision-transformer encoder pretrained on UKB structural and diffusion MRI.
- Wang, Y., et al. "GenBrain: A Generative Foundation Model of Multimodal Brain Imaging." medRxiv (2025); diffusion-based generative model trained on approximately 1.2 million 3D scans across 34 modalities from approximately 44,000 UKB individuals.
- "A graph transformer-based foundation model for brain functional connectivity network." NeuroImage (2025); pretrained on UKB rs-fMRI for connectivity prediction.
- "COMICAL: A foundation model for learning genetic associations from brain imaging phenotypes." Bioinformatics Advances (2025); contrastive multimodal model bridging UKB genotypes and IDPs.

**Notes for Cytognosis platform integration:** UKB is uniquely valuable for paired WGS plus structural/functional MRI plus EHR phenotypes at scales no other cohort matches, ideal for cross-modal pretraining of brain foundation models. The strong governance constraint is that all training must occur on UKB-RAP and only model weights, embeddings, and aggregate metrics may be exported; this is generally compatible with releasing pretrained checkpoints publicly, but model cards must avoid memorized individual-level features. The European-ancestry skew (94%) limits demographic generalization; pair with AoU or MVP for ancestry-balanced pretraining.

### 7.2 AoU: All of Us Research Program

**Short description:** All of Us is the U.S. National Institutes of Health flagship precision medicine cohort, enrolling adult participants (18+) across the United States with intentional oversampling of populations historically under-represented in biomedical research (UBR). As of 2025, more than 930,000 participants are enrolled, with 77% of those with genomic data identifying with UBR groups and 46% from racial or ethnic minority groups. The program collects EHR linkage, surveys, physical measurements, biospecimens, wearables (Fitbit), and genomics (WGS plus arrays), with the explicit goal of building a million-person multi-ancestry resource for genotype-to-phenotype and health-equity research.

**Latest/most significant reference publication:** Bick, A. G., Metcalf, G. A., Mayo, K. R., et al. "Genomic data in the All of Us Research Program." Nature 627, 340 to 346 (2024). DOI: 10.1038/s41586-023-06957-x. PMC: PMC10937371. Year-in-review: Mayo, K. R., et al. "All of Us Research Program year in review: 2024." American Journal of Human Genetics 112, 2024 to 2031 (2025). DOI: 10.1016/j.ajhg.2025.07.005.

**Access requirements:**
- *Obtain data:* Researchers register on the Researcher Workbench via institutional affiliation. Their institution must execute a Data Use and Registration Agreement (DURA); for genomic data, the DURA must include the Controlled Tier addendum. The researcher creates an @researchallofus.org account, completes Login.gov or ID.me identity verification, finishes the Responsible Conduct of Research training (and Controlled-Tier training for genomics), and signs the Data User Code of Conduct. Approval typically takes days to a few weeks once the institutional DURA is in place. There is no direct researcher fee; cloud compute (Google Cloud) is billed to the researcher's project, with NIH-funded credits available.
- *Use restrictions:* Re-identification of participants is strictly prohibited and triggers immediate sanctions. Use must be for biomedical or public-health research consistent with participant consent. Public posting of disaggregated counts smaller than 20 individuals requires program approval. Publication is encouraged with no embargo but must register the workspace.
- *Storage requirements:* All analyses must occur inside the Researcher Workbench (Terra-based, on Google Cloud). Individual-level data (genotypes, EHR, surveys, Fitbit) cannot be downloaded; the Egress Alert Policy automatically flags attempts to extract row-level data, large notebooks, or large files. Only summary statistics passing aggregation thresholds may leave the platform.
- *What can be shared back:* Trained model weights and aggregated summary statistics (with cell-suppression below 20) may be exported with approval. Re-distribution of individual-level data is prohibited. Publication of GWAS summary statistics is permitted via standard channels.

**Links:**
- Main website: https://allofus.nih.gov/
- Access request page: https://www.researchallofus.org/register/
- Data repository / portal: https://workbench.researchallofus.org/

**Included pathologies (MONDO mapping):** AoU is a population cohort with EHR-derived case counts spanning the U.S. disease burden. The following MONDO terms are well-represented at population base rates with case numbers in the tens of thousands: Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Post-traumatic Stress Disorder (MONDO:0005146), Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Alcohol Dependence (MONDO:0007079), Nicotine Dependence (MONDO:0008575), Opioid-use Disorder (MONDO:0005530), Cannabis-use Disorder (MONDO:0005689), Bipolar Disorder (MONDO:0004985), Schizophrenia (MONDO:0005090), Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), Dementia (MONDO:0001627), multiple sclerosis (MONDO:0005301), Brain disorders (MONDO:0005560).

**Available data types and sample counts (Controlled Data Repository v8, spring 2025):**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=414,000 (short-read, approximately 30x)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=447,000+
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 500,000 with linked OMOP-mapped EHR
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 800,000 across The Basics, Lifestyle, Overall Health, Personal Medical History, Family History, Healthcare Access, COPE, Social Determinants of Health, and Mental Health surveys
- Wearables (not in standard ontology rows): Fitbit physical activity and sleep, n=59,000+ participants (v8 release; 30,445 with high-density 7-day windows); approximately 46% overlap with EHR plus genomics.

(No cellular omics or brain imaging modalities are released; AoU does not currently distribute scRNA-seq, ATAC-seq, or MRI.)

**Foundation-model training adoption:**
- Sun, T., et al. "Building the EHR Foundation Model via Next Event Prediction" (NEP-8B). arXiv:2509.25591 (2025); 8B-parameter EHR foundation model trained on All of Us OMOP event sequences, with cancer-stage prediction benchmarks.
- Tanigawa, Y., et al. "All of Us diversity and scale improve polygenic prediction contextually with greatest improvements for under-represented populations." Nature Medicine (2024). PMC: PMC11326295.
- Multiple 2024-2025 papers transfer UKB-pretrained brain or PRS models with All of Us as the multi-ancestry validation cohort.

**Notes for Cytognosis platform integration:** AoU is the strongest U.S. multi-ancestry resource for EHR plus WGS pretraining; its strict no-egress policy means models trained here can be exported as weights but never as memorized individual-level data. The lack of brain MRI and cellular omics limits AoU's role to genotype-plus-EHR pretraining; pair with UKB or ABCD for imaging modalities. Models trained inside the Workbench can be released publicly provided aggregation thresholds and Code of Conduct are honored.

### 7.3 MVP: Million Veteran Program

**Short description:** The Million Veteran Program is the U.S. Department of Veterans Affairs cohort of more than 1,000,000 enrolled U.S. military Veterans (launched 2011), with approximately 635,000+ participants having released genotyping plus deep VA Corporate Data Warehouse (CDW) EHR linkage. The cohort is enriched for older men (Vietnam, Gulf War, post-9/11 eras), with approximately one-third non-European ancestry, and is disproportionately enriched for psychiatric, neurodegenerative, cardiometabolic, and military-exposure phenotypes (PTSD, depression, substance-use disorders, traumatic brain injury). Its primary aim is to identify genetic and environmental contributors to Veteran-relevant health outcomes.

**Latest/most significant reference publication:** Verma, A., Huffman, J. E., Rodriguez, A., et al. "Diversity and scale: Genetic architecture of 2068 traits in the VA Million Veteran Program." Science 385, eadj1182 (2024). DOI: 10.1126/science.adj1182. Foundational genotyping paper: Hunter-Zinck, H., Shi, Y., Li, M., et al. "Genotyping Array Design and Data Quality Control in the Million Veteran Program." American Journal of Human Genetics 106, 535 to 548 (2020). PMID: 32243820.

**Access requirements:**
- *Obtain data:* Primary access route is restricted to VA-affiliated investigators (active VA appointment or "without compensation" appointment) who submit an MVP Data Access Request (DAR) and obtain VA IRB/R&D Committee approval; analyses run inside VA secure compute (VA Informatics and Computing Infrastructure, VINCI, or the joint VA/DOE MVP-CHAMPION platform). Non-VA researchers do not have a direct data-access mechanism but can collaborate with a VA PI or, for a curated subset, access PheWAS summary statistics via dbGaP study phs001672. As of 2024, MVP has reported 800+ active researchers across 100+ projects.
- *Use restrictions:* Use limited to the approved DAR scope. Re-identification, re-contact outside MVP-managed channels, and any commercial-product development without explicit VA agreement are prohibited. Embargoes apply to certain consortium-led flagship analyses.
- *Storage requirements:* Individual-level genotype, sequence, and EHR data must remain on VINCI or the VA secure cloud. No download to non-VA infrastructure is permitted. Strict audit logging applies; researchers must use VA-issued credentials and PIV cards. Open-access PheWAS summary statistics (released July 2024 via dbGaP) can be downloaded freely.
- *What can be shared back:* Trained model weights, aggregated summary statistics (PheWAS, GWAS), and derived risk scores can be exported subject to VA Office of Research and Development review. Full re-distribution of individual-level data is prohibited. Public release of GWAS summary statistics is supported via dbGaP.

**Links:**
- Main website: https://www.mvp.va.gov/pwa/
- Access request page: https://www.research.va.gov/mvp/ (researcher-access section; contact MVPLOI@va.gov)
- Data repository / portal: VINCI (internal) and dbGaP study phs001672 for summary statistics

**Included pathologies (MONDO mapping):** MVP is enriched for psychiatric, substance-use, and neurological phenotypes through VA EHR linkage: Post-traumatic Stress Disorder (MONDO:0005146) (largest single PTSD genetics resource, >250,000 PTSD-relevant cases in subdomain analyses), Major Depressive Disorder (MONDO:0002009) (>250,000 cases), Anxiety Disorder (MONDO:0005618), Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689), Bipolar Disorder (MONDO:0004985), Schizophrenia (MONDO:0005090) (~120,000 schizophrenia patients), Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), Dementia (MONDO:0001627), amyotrophic lateral sclerosis (MONDO:0004976), Neuropsychiatric disorders (MONDO:0002025).

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 102,000 released (of approximately 190,000 sequenced)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=1,000,000+ on custom MVP 1.0/1.1 Axiom arrays; n=approximately 650,000+ QC-passed and imputed
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 1,000,000 (full VA CDW longitudinal records spanning 20+ years)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 600,000+ baseline and lifestyle surveys

**Foundation-model training adoption:**
- "MVP-CHAMPION: A landmark federal interagency collaboration to promote data science in health care." JAMIA Open 7, ooae126 (2024); the joint VA/Department of Energy platform supporting deep-learning model development on MVP at scale.
- Verma, A., et al. "Diversity and scale: Genetic architecture of 2068 traits." Science (2024); the underlying PheWAS summary statistics are now used as a standard pretraining/evaluation corpus for polygenic foundation models.
- Stein, M. B., et al. "Genome-wide association analyses of post-traumatic stress disorder and its symptom subdomains in the MVP." Nature Genetics 53, 174 to 184 (2021); a recurring benchmark for psychiatric foundation-model evaluation.

**Notes for Cytognosis platform integration:** MVP offers the largest psychiatric and substance-use cohort in the world, with EHR coverage that is unmatched for PTSD and SUD foundation-model pretraining; however, access is effectively gated to VA-affiliated researchers, so external partners typically need a VA collaborator or must restrict use to dbGaP summary statistics. Models trained on MVP individual-level data cannot leave VINCI; only weights and aggregate statistics can be exported, which is compatible with public model release if the training procedure is documented and VA ORD approves. The lack of imaging and cellular omics means MVP is best paired with UKB or AoU for multimodal training.

---

## 8. Phenotype-Centric and Clinical Biobanks

These cohorts contribute the deep phenotyping and clinical-grade EHR substrates that power Cytognosis's phenotypic and physiological foundation models. HPP uniquely offers a multimodal phenotyping platform (CGM, microbiome, imaging, omics) at scale; the MGB, Mayo, and Mt Sinai sites contribute complementary tertiary-care clinical data with regional and ancestral diversity.

### 8.1 HPP: Human Phenotype Project (Pheno.AI / Weizmann Institute)

**Short description:** The Human Phenotype Project (HPP) is a large-scale, deep-phenotype, prospective longitudinal cohort and biobank initiated in Israel by the Segal lab at the Weizmann Institute and operationalized by the spinout Pheno.AI. As of 2025, approximately 28,000 participants have enrolled and more than 13,000 have completed the comprehensive baseline visit, with planned 25-year follow-up. The cohort over-samples generally healthy adults (ages 40 to 70) across the health-disease continuum to power AI-based predictive models, "digital twins" of human physiology, and discovery of early disease biomarkers.

**Latest/most significant reference publication:** Reicher L, Shilo S, Talmor-Barkan Y, et al. Deep phenotyping of health-disease continuum in the Human Phenotype Project. Nature Medicine. 2025;31(8):2562, 2575. DOI: 10.1038/s41591-025-03790-9. PMID: 40665053. Companion methods paper: Caspi I, Shoer S, et al. Genome-wide association studies and polygenic risk score phenome-wide association studies across complex phenotypes in the Human Phenotype Project. Hum Mol Genet. 2024 (PMID: 38157848). GluFormer foundation-model paper: Lutsker G, et al. A foundation model for continuous glucose monitoring data. Nature. 2025. DOI: 10.1038/s41586-025-09925-9.

**Access requirements:**
- *Obtain data:* Two routes. (1) Direct request through Pheno.AI's Research Knowledge Base (info@pheno.ai) under a bona fide-researcher agreement; modality-by-modality DUA. (2) Controlled access via the European Genome-phenome Archive (EGA) under accession EGAS00001008040; Data Access Committee (DAC) approval typically takes 4 to 12 weeks. No fees for academic non-commercial use; commercial-use access is negotiated separately.
- *Use restrictions:* Permitted: hypothesis-driven research, model training, methods development. Prohibited: re-identification attempts; redistribution; commercial product development without separate license. Embargoes apply to newly released modalities (typically 6 to 12 months).
- *Storage requirements:* Raw genomic and microbiome data must remain in approved compute environments; sensor and CGM time-series can be downloaded after DUA. Encryption at rest required.
- *What can be shared back:* Models, summary statistics, derived features, and aggregated visualizations are encouraged for publication. Sharing of individual-level data outside the approved team is prohibited.

**Links:**
- Main website: https://humanphenotypeproject.org/
- Access request page: https://knowledgebase.pheno.ai/ (contact info@pheno.ai); EGA study page https://ega-archive.org/studies/EGAS00001008040
- Data repository / portal: Pheno.AI Knowledge Base and EGA

**Included pathologies (MONDO mapping):** N/A (healthy/baseline); the cohort is community-recruited and emphasizes the health-disease continuum. Incident cases accrue across many MONDO terms; among those on the platform's target list, longitudinal incidence is most relevant for Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), Dementia (MONDO:0001627).

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approx 13,000
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approx 13,000
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approx 10,000 (PBMC transcriptomics)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approx 1,000 (sub-study)
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approx 1,000 (sub-study)
  - EEG: Electroencephalography (NCIT:C38054), n=approx 1,000 (sleep substudy)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 13,000 (Israeli HMO linkage)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approx 13,000 (medical history, lifestyle, mental health, sleep, diet)

(Additional unique modalities not in the schema: continuous glucose monitor time series approx 13,000; gut, oral, vaginal microbiome 16S+shotgun approx 13,000; serum metabolomics approx 13,000; ultrasound, DXA, fundus imaging, sleep actigraphy approx 10,000+ each.)

**Foundation-model training adoption:**
- Lutsker et al., 2025, "GluFormer," Nature: transformer foundation model trained on >10 million CGM measurements from 10,812 HPP participants; transfers to 19 external cohorts for diabetes-onset prediction.
- Reicher et al., 2025, Nature Medicine: multi-modal self-supervised AI predicting disease onset from diet plus CGM as a "digital twin."
- Lutsker et al., 2024, "COMPRER": contrastive multi-modal foundation model integrating fundus and carotid ultrasound for cardiovascular risk prediction.
- Shilo et al., 2024, Cell Reports Medicine: HPP-trained metabolomics-and-microbiome model for cardiometabolic phenotyping.

**Notes for Cytognosis platform integration:** HPP is one of the few cohorts with paired wearable, CGM, microbiome, imaging, and multi-omics in the same individuals; ideal for training cross-modal phenotype foundation models. Governance is Israel-anchored with EGA mirroring; commercial release of derived weights requires explicit Pheno.AI sign-off. Brain imaging and EEG are restricted to substudies, so neuropsychiatric power is limited compared to clinically ascertained cohorts.

### 8.2 MGBB: Mass General Brigham Biobank

**Short description:** The Mass General Brigham Biobank (formerly Partners Biobank) is a hospital-based, EHR-linked biorepository launched in 2010 across the MGB system in Greater Boston. As of 2025, more than 160,000 patients have enrolled and provided biospecimens, surveys, and EHR linkage; 142,238 participants featured in the 2025 Nature Communications cohort overview. Its primary aim is to support translational research on genomic, environmental, biomarker, and family-history associations with disease across the full clinical spectrum captured in MGB's tertiary-care EHR.

**Latest/most significant reference publication:** Lemieux Perreault L, Ge T, Karjalainen J, et al. Genetics and context for precision health in Greater Boston. Nat Commun. 2025;16:Article 66598. DOI: 10.1038/s41467-025-66598-8. Foundational: Boutin NT, Schecter SB, Perez EF, et al. The Evolution of a Large Biobank at Mass General Brigham. J Pers Med. 2022;12(8):1323. PMID: 36013271.

**Access requirements:**
- *Obtain data:* MGB-affiliated faculty (or external collaborators sponsored by MGB faculty) submit a Biobank request through the Biobank Portal with an approved IRB protocol. Typical turnaround 4 to 8 weeks for data, longer for biospecimens. Biospecimen and assay fees apply (genotyping, sequencing, aliquots are cost-recovery).
- *Use restrictions:* IRB protocol must specify scientific aims; commercial use requires explicit MTA. Re-identification prohibited; data may not leave the MGB enclave without committee approval.
- *Storage requirements:* Genomic and EHR data are typically analyzed inside the MGB Analytics Enclave (Azure-based). Some de-identified summary tables can be exported under data-use review.
- *What can be shared back:* Summary statistics, GWAS results, derived features, and trained models are publishable. Patient-level data cannot be redistributed. The Biobank operates a Return of Research Results Program for ACMG-actionable variants.

**Links:**
- Main website: https://www.massgeneralbrigham.org/en/research-and-innovation/participate-in-research/biobank
- Access request page: https://www.massgeneralbrigham.org/en/research-and-innovation/centers-and-programs/personalized-medicine/biobank-genomics
- Data repository / portal: Biobank Portal (i2b2/Azure Enclave), https://rc.partners.org/

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560) for the heterogeneous clinical population. Sufficient case counts exist for: Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Bipolar Disorder (MONDO:0004985), Schizophrenia (MONDO:0005090), multiple sclerosis (MONDO:0005301), Dementia (MONDO:0001627), amyotrophic lateral sclerosis (MONDO:0004976), Post-traumatic Stress Disorder (MONDO:0005146), Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Autism Spectrum Disorder (MONDO:0005258), Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575).

**Available data types and sample counts:**
- Genotype:
  - WES: exome sequencing assay (OBI:0002118), n=approx 54,000
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approx 65,000 (Illumina MEGA approx 36,000 plus GSA approx 30,000)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 142,000 (longitudinal Epic-derived)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approx 55,000 (Health Information Survey)

**Foundation-model training adoption:**
- Chen RJ, Ding T, Lu MY, et al., 2024, "UNI" and "CONCH," Nature Medicine: pathology foundation models trained at MGB on >100k slides, evaluated on 30+ clinical tasks; UNI weights publicly released.
- Lu MY et al., 2024, Nature: vision-language pathology FM ("CONCH") trained at MGB.
- 2025 Sci Reports paper: deep metric learning for opportunistic type-2 diabetes screening on >109,000 MGBB EHR participants.
- eMERGE-PRS work (Ge et al., Nature Medicine 2022): polygenic score foundations leveraging MGBB.

**Notes for Cytognosis platform integration:** MGBB offers strong genotype-plus-EHR pairing on a New England referral population; it is well suited for training EHR-and-genotype phenotype models. Imaging is rich but only accessible via separate RPDR/PDSR pulls; pathology FM weights from MGB (UNI, CONCH) demonstrate that public model release is achievable. Plan for in-enclave training and weight-extraction governance.

### 8.3 RPDR: MGB Research Patient Data Registry

**Short description:** The Research Patient Data Registry is the central clinical-data warehouse for Mass General Brigham, aggregating demographics, encounters, diagnoses, procedures, medications, labs, notes, imaging metadata, and hospital course for approximately 7+ million patients across MGH, BWH, and affiliated hospitals (450 million records, 350 million coded events). It is the primary IRB-gated source for cohort identification and chart-level research at MGB and supports more than 5,000 active investigators.

**Latest/most significant reference publication:** Murphy SN, Mendis ME, Hackett K, et al. Architecture of the open-source clinical research chart from Informatics for Integrating Biology and the Bedside (i2b2). AMIA Annu Symp Proc. 2007:548, 552. PMID: 18693896 (foundational). Castro VM, et al. The Mass General Brigham Biobank Portal: an i2b2-based data repository. JAMIA. 2022;29(4):643, 651. PMID: 34849976.

**Access requirements:**
- *Obtain data:* MGB credentials are mandatory; researcher must be on MGB network or VPN. Project Lead must be an RPDR Faculty Sponsor (HMS Instructor or above). IRB-approved protocol required for any patient-identifying data; preparatory-to-research queries permitted under separate workflow. Turnaround typically days to weeks.
- *Use restrictions:* MGB-only researchers (or formal external collaborators sponsored by MGB faculty). Re-identification prohibited; downstream sharing requires MGB committee review.
- *Storage requirements:* Data extracted from RPDR is delivered to MGB-secured ERIS or Enclave storage; ePHI cannot leave MGB infrastructure without explicit approval.
- *What can be shared back:* Aggregated summary statistics, derived phenotype models, and methods papers can be published; raw or quasi-identifiable data cannot be redistributed.

**Links:**
- Main website: https://rc.partners.org/about/who-we-are-risc/research-patient-data-registry
- Access request page: https://rc.partners.org/research-apps-services/identify-subjects-request-data
- Data repository / portal: https://rpdrssl.partners.org/ (RPDR Query Tool)

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560); comprehensive ICD-derived case counts for Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), frontotemporal dementia (MONDO:0017276), Lewy body dementia (MONDO:0007488), Huntington disease (MONDO:0007739), amyotrophic lateral sclerosis (MONDO:0004976), multiple sclerosis (MONDO:0005301), Dementia (MONDO:0001627), Schizophrenia (MONDO:0005090), Bipolar Disorder (MONDO:0004985), Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Post-traumatic Stress Disorder (MONDO:0005146), Obsessive-Compulsive Disorder (MONDO:0008114), Anorexia Nervosa (MONDO:0005351), Tourette Syndrome (MONDO:0007661), Autism Spectrum Disorder (MONDO:0005258), Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689).

**Available data types and sample counts:**
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 7,000,000 (450 million records, 350 million diagnoses/medications/procedures)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=variable by department (PROMIS, PHQ-9, GAD-7, MoCA, ascertained subsets)

**Foundation-model training adoption:**
- Castro VM et al., 2024, multiple JAMIA / Nature Medicine: clinical NLP and risk-prediction foundation models trained on RPDR notes (e.g., for suicide risk, dementia risk).
- MGB MIND group (2024 to 2025): EHR-based depression and PTSD risk models trained on RPDR-derived cohorts.
- RPDR-derived ICU and cardiovascular outcome models referenced in multiple MGB-MIT collaborations.

**Notes for Cytognosis platform integration:** RPDR is the most powerful EHR phenotyping engine at MGB and the de-facto cohort-builder for any MGB-anchored study (including MGBB and PDSR). Integration requires an MGB-faculty PI; expect the data to stay in-enclave. Best paired with PDSR Curated for ML at scale.

### 8.4 PDSR Curated: MGB Complete Patient Data Science Repository (Curated)

**Short description:** The Complete Patient Data Science Repository (PDSR) Curated Data Set is MGB's enterprise-scale, limited-data-set (LDS) repository covering the entire MGB Affiliated Covered Entity plus Dana-Farber Cancer Institute patient population, with more than 5 billion observation facts. The dataset is provided in i2b2, curated relational, and OMOP CDM v5.2 formats and is designed to enable hypothesis-generation, machine learning, and AI training at population scale within the MGB Analytics Enclave without requiring an IRB protocol per project.

**Latest/most significant reference publication:** No single peer-reviewed cohort overview exists yet (the curated release is new in 2024 to 2025); see MGB RISC documentation: "NEW! The Complete Patient Data Science Repository (PDSR) Curated Data Set is available to MGB researchers" (https://rc.partners.org/news-events/announcements/new-complete-patient-data-science-repository-pdsr-curated-data-set, 2024). Methodologically downstream of Castro VM et al., JAMIA 2022 (PMID: 34849976).

**Access requirements:**
- *Obtain data:* MGB-only researchers (faculty and sponsored staff) submit a Digital Research Data Repositories access request via the MGB RISC portal. Because PDSR Curated is a HIPAA Limited Data Set (LDS), no IRB protocol is required, but a signed Data Use Agreement and PI attestation are mandatory. Onboarding to the MGB Analytics Enclave (Windows Enclave VDI, Azure-backed) is the typical turnaround of 1 to 4 weeks.
- *Use restrictions:* Limited Data Set restrictions: dates retained, direct identifiers removed, no re-identification, no linkage with external identifiable data without committee approval.
- *Storage requirements:* Must remain inside the MGB Analytics Enclave; no patient-level export. Models and aggregate outputs leave the enclave only after egress review.
- *What can be shared back:* Trained models (subject to egress review), summary statistics, manuscripts.

**Links:**
- Main website: https://rc.partners.org/pdsr-curated/complete-patient-data-science-repository-pdsr-curated-data-set
- Access request page: https://rc.partners.org/kb/article/3976
- Data repository / portal: MGB Analytics Enclave (Windows Enclave VDI / Azure)

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560). All MONDO terms in the priority list are present at population scale (same EHR coverage as RPDR, but de-identified and OMOP-standardized).

**Available data types and sample counts:**
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 7,000,000+ patients, > 5 billion observation facts (OMOP CDM v5.2 plus i2b2)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=multiple million PROMIS / PHQ-9 / GAD-7 instances

**Foundation-model training adoption:**
- MGB AI in Medicine pipelines (2024 to 2025) use PDSR Curated as the substrate for multi-task EHR foundation models for inpatient and outpatient risk prediction.
- The UNI and CONCH pathology foundation models are trained at MGB using slide cohorts whose phenotypes are anchored in PDSR Curated linkage.
- PDSR Curated underpins MGB's diabetes screening deep-metric-learning paper (Sci Reports 2025).

**Notes for Cytognosis platform integration:** PDSR Curated is uniquely attractive for population-scale pretraining because no per-project IRB is required and OMOP CDM is supplied out-of-the-box. Plan compute inside the Azure Enclave; weights are exportable but each export is reviewed. Combine with MGBB for genotype-anchored fine-tuning.

### 8.5 MCP Accelerate: Mayo Clinic Platform Accelerate

**Short description:** Mayo Clinic Platform_Accelerate is the structured, 30-week health-tech and AI startup accelerator operated by Mayo Clinic Platform; participating companies receive de-identified longitudinal Mayo clinical data, expert mentorship, regulatory and clinical guidance, and investor access to develop and validate AI/ML solutions. Cohorts are themed (e.g., AI in pathology, oncology, cardiology, rare disease, dermatology, pharma) and are typically 5 to 11 startups per cohort, with four cohorts to date. As of February 2025, Accelerate alumni had raised approximately $145 million.

**Latest/most significant reference publication:** Heydari A et al., npj Health Systems 2026, "Accelerating AI innovation in healthcare: real-world clinical research applications on the Mayo Clinic Platform" (DOI: 10.1038/s44401-026-00068-1).

**Access requirements:**
- *Obtain data:* Application to a cohort call; selection by Mayo Clinic Platform leadership. Acceptance grants 30-week access to the Discover sub-platform plus mentorship. Companies sign a master services agreement with revenue-share / option terms with Mayo Clinic. No fee to enter (Mayo takes equity / option). Open to global startups.
- *Use restrictions:* Data may be used only for the AI/ML use case approved at intake; no re-identification; commercial deployment requires separate Mayo Validate / Deploy stage agreements. Embargoes typical for 12 months post-cohort.
- *Storage requirements:* All compute happens inside the Mayo Clinic Platform secure cloud (de-identified data never leaves Mayo's environment). Models are containerized and validated in-enclave.
- *What can be shared back:* Trained model weights and summary statistics can leave the enclave subject to Mayo egress review; raw data cannot.

**Links:**
- Main website: https://www.mayoclinicplatform.org/focus-areas/digital-health/accelerate/
- Access request page: https://www.mayoclinicplatform.org/focus-areas/digital-health/accelerate/accelerate-cohort-landing-page/
- Data repository / portal: Mayo Clinic Platform_Discover

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560); pathology coverage mirrors Mayo's tertiary clinical population, with rich incidence for Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), amyotrophic lateral sclerosis (MONDO:0004976) (Mayo is an ALS center of excellence), multiple sclerosis (MONDO:0005301), Dementia (MONDO:0001627), Lewy body dementia (MONDO:0007488), frontotemporal dementia (MONDO:0017276), Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Bipolar Disorder (MONDO:0004985), Schizophrenia (MONDO:0005090), Post-traumatic Stress Disorder (MONDO:0005146), Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575).

**Available data types and sample counts:**
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 10,000,000 (Mayo Discover; structured Epic-derived plus pathology and radiology reports, clinical notes)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=multiple million

(Imaging DICOMs available, including approx 3 million echocardiograms, ECGs, CT, MR; pathology whole-slide images; Mayo has launched Atlas pathology FM with Aignostics on >1.2 million slides. Genomic data limited to in-house Mayo sequencing programs.)

**Foundation-model training adoption:**
- Atlas pathology foundation model (Mayo + Aignostics, 2024 to 2025): trained on more than 1.2 million histopathology whole-slide images.
- Mayo Clinic dermatology foundation model (announced 2025): integrates whole-slide pathology, dermoscopy, clinical photos, and EHR.
- Mayo Clinic ECG-AI foundation models (Attia et al., Nat Med 2024, Lancet Digital Health 2024).

**Notes for Cytognosis platform integration:** Accelerate is the most efficient way for an external organization to operate inside Mayo's data without bilateral contracting; the trade-off is equity/option to Mayo and an in-enclave training requirement. Best fit for pathology-, ECG-, and EHR-modality FM training.

### 8.6 MCP: Mayo Clinic Platform (general)

**Short description:** Mayo Clinic Platform is Mayo's enterprise digital-health and data-sharing platform comprising Discover (de-identified clinical data and analytics), Validate (algorithm validation), Deploy (clinical deployment), Connect (federated multi-institution data sharing), Accelerate (startup program), and Insights (operational analytics). The de-identified data substrate exceeds 50 million patient records aggregated across Mayo Clinic and federated partners (Mayo's own footprint is approximately 10 million longitudinal patient records).

**Latest/most significant reference publication:** Heydari A, Cerrato P, Halamka JD, et al. Accelerating AI innovation in healthcare: real-world clinical research applications on the Mayo Clinic Platform. npj Health Systems. 2026. DOI: 10.1038/s44401-026-00068-1.

**Access requirements:**
- *Obtain data:* Discover access is sold through enterprise subscriptions to industry and large academic partners; pricing is custom (six-figure per year typical) and tied to use cases. Smaller startups enter via Accelerate. Federated Connect is offered to participating health systems.
- *Use restrictions:* Use cases approved at contracting; re-identification prohibited; commercial deployment via Validate / Deploy.
- *Storage requirements:* All compute in Mayo Cloud (Azure-anchored) enclaves; data never leaves Mayo. Customer workspaces are isolated.
- *What can be shared back:* Trained models and summary statistics leave under egress review; raw data cannot.

**Links:**
- Main website: https://www.mayoclinicplatform.org/
- Access request page: https://www.mayoclinicplatform.org/discover/
- Data repository / portal: Mayo Clinic Platform_Discover

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560); same MONDO coverage as MCP Accelerate plus Huntington disease (MONDO:0007739).

**Available data types and sample counts:**
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 10,000,000 Mayo-owned; approx 54,000,000 across federated Connect partners
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=multiple million

(Imaging archive includes more than 1.2 million pathology whole-slide images, approx 3 million echocardiograms, plus large CT, MR, ECG, and ophthalmology corpora.)

**Foundation-model training adoption:**
- Atlas pathology FM (Mayo + Aignostics, 2025): >1.2M WSIs.
- Mayo ECG-AI foundation models (Attia, Friedman, Lopez-Jimenez et al., Nat Med 2019, 2024).
- Cerebras-Mayo genomic foundation model partnership (announced 2024) targeting rare disease.
- NVIDIA-Mayo partnership (2025) for digital pathology, drug discovery, and precision medicine FMs on Blackwell-based MCP infrastructure.

**Notes for Cytognosis platform integration:** MCP is the largest single secure-enclave US clinical data substrate available to industry; ideal as a complementary substrate to MGB and Mt Sinai for cross-region generalization. Subscription cost and data-stays-in-enclave are the main constraints.

### 8.7 BioMe: Mt Sinai BioMe Biobank

**Short description:** BioMe (the Charles Bronfman Institute for Personalized Medicine BioMe Biobank) is an EHR-linked, broadly consented urban-medical-center biobank at the Icahn School of Medicine at Mount Sinai, founded in 2007 and recruiting from Mount Sinai Health System ambulatory clinics. As of 2025, more than 60,000 participants have enrolled with self-reported African American, Latinx, European, East Asian, and other ancestries (one of the most ancestrally diverse US biobanks).

**Latest/most significant reference publication:** Sun KY, Bai X, Chen S, et al. (Regeneron Genetics Center). A deep catalogue of protein-coding variation in 983,578 individuals. Nature. 2024;631:583, 592. DOI: 10.1038/s41586-024-07556-0. PMID: 38867121 (BioMe contributed approximately 31,000 exomes). Cohort overview: Belbin GM, Cullina S, Wenric S, et al. Toward a fine-scale population health monitoring system. Cell. 2021;184(8):2068, 2083. PMID: 33861964.

**Access requirements:**
- *Obtain data:* Internal Mount Sinai investigators apply through the BioMe data-request portal (Minerva HPC account, signed BioMe DUA, MSIP COI clearance). External investigators must collaborate with a Mount Sinai PI; some subsets (TOPMed WGS phs001644, PAGE phs000925) are dbGaP-controlled.
- *Use restrictions:* Use limited to scientific research approved by IPM; no re-identification; collaboration with external commercial partners requires MSIP review.
- *Storage requirements:* Internal data must remain on the Minerva HPC inside Mount Sinai network or VPN. dbGaP data follow standard NIH controlled-access rules.
- *What can be shared back:* Summary statistics, polygenic scores, derived features, and trained models.

**Links:**
- Main website: https://icahn.mssm.edu/research/ipm/programs/biome-biobank
- Access request page: https://icahn.mssm.edu/research/ipm/programs/biome-biobank/researcher-faqs
- Data repository / portal: Minerva HPC Data Ark; dbGaP phs001644, phs000925; EGA mirror

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560); EHR-derived case counts for Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), multiple sclerosis (MONDO:0005301), Dementia (MONDO:0001627), Schizophrenia (MONDO:0005090), Bipolar Disorder (MONDO:0004985), Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Post-traumatic Stress Disorder (MONDO:0005146), Obsessive-Compulsive Disorder (MONDO:0008114), Autism Spectrum Disorder (MONDO:0005258), Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689).

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approx 10,600 (TOPMed)
  - WES: exome sequencing assay (OBI:0002118), n=approx 45,893 (Regeneron IDT n=30,813 plus Sema4 SureSelect n=15,080)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approx 50,000 (Illumina MEGA, GSA)
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approx 2,000 (PBMC, project-specific)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 60,000+ (Epic-derived)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approx 60,000

**Foundation-model training adoption:**
- Sun et al., Nature 2024, "RGC-ME": pan-biobank exome FM substrate including BioMe.
- Vy HMT, Nadkarni GN, et al., 2024 Nat Commun: BioMe-anchored EHR-based deep-learning kidney-disease and cardiovascular-risk models.
- PsycheMERGE / eMERGE-IV consortium models (2024 to 2025).
- Mount Sinai-IBM PREDiCTOR (NIMH-funded 2024).

**Notes for Cytognosis platform integration:** BioMe's chief value is ancestrally diverse genotype-plus-EHR pairing, complementing the more European-skewed MGBB. Access requires either a Mount Sinai collaborator or dbGaP route. In-enclave training on Minerva HPC is standard. Excellent for cross-ancestry generalization studies and Latinx/African-ancestry psychiatric phenotyping.

### 8.8 MSDW: Mount Sinai Data Warehouse

**Short description:** The Mount Sinai Data Warehouse (MSDW) is the enterprise clinical-research data repository of the Mount Sinai Health System, primarily consisting of Epic EHR data (since 2011) transformed daily into OMOP CDM. It contains approximately 12 million unique patient records and 105 million encounters drawn from the eight-hospital, ambulatory-care, and outpatient network across NYC.

**Latest/most significant reference publication:** Miotto R, Li L, Kidd BA, Dudley JT. Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records. Sci Rep. 2016;6:26094. PMID: 27185194. For modern usage see Glicksberg BS et al., Patterns 2024, and the AI-Ready Mount Sinai (AIR-MS) initiative.

**Access requirements:**
- *Obtain data:* Mount Sinai-affiliated investigators only; users must complete approximately 3 hours of MSDW training. Access via Sinai Central / Active Directory authentication. Identifiable data require valid IRB or QI documentation; de-identified queries via Leaf require no IRB.
- *Use restrictions:* Mount Sinai-only researchers (or external collaborators sponsored by an MSHS PI). No re-identification; no redistribution.
- *Storage requirements:* All data analyses on Minerva HPC or approved Mount Sinai compute. PHI must not leave Mount Sinai infrastructure.
- *What can be shared back:* Aggregate statistics and trained models can be exported subject to review. Raw EHR data and notes cannot leave Mount Sinai.

**Links:**
- Main website: https://labs.icahn.mssm.edu/msdw/
- Access request page: https://labs.icahn.mssm.edu/msdw/services/clinical-systems-data-access/
- Data repository / portal: Leaf (de-identified), ATLAS, Minerva HPC

**Included pathologies (MONDO mapping):** Brain disorders (MONDO:0005560); EHR-coded coverage for the same disorders as RPDR.

**Available data types and sample counts:**
- Clinical: Electronic Medical Record (NCIT:C45259), n=approx 12,000,000 patients (105 million encounters, OMOP CDM, daily refresh, geocoded addresses since 2024)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=multiple million

**Foundation-model training adoption:**
- Miotto et al., 2016, "Deep Patient": pioneering unsupervised denoising-autoencoder patient representation from approx 700,000 MSDW patients.
- Glicksberg et al., 2024 (Lancet Digital Health, Patterns): MSDW-trained clinical LLMs and risk models.
- AIR-MS (AI-Ready Mount Sinai, 2024 to 2025): institutional FM program.
- Mount Sinai-IBM PREDiCTOR (2024): NIMH-funded objective psychiatric phenotyping.

**Notes for Cytognosis platform integration:** MSDW provides the largest urban, ancestrally diverse EHR substrate on the East Coast and is OMOP-standardized for fast pretraining; pairs directly with BioMe for genotype-anchored fine-tuning. All training must occur on Minerva HPC; weight export is reviewed but feasible.

---

## 9. Neuroimaging Biobanks

These four entries supply the bulk of accessible brain-imaging data: ABCD for development, the HCP family for standardization, INDI for transdiagnostic open data, and OpenNeuro for the long tail. Combined, they exceed 150,000 imaging sessions, with strong protocol harmonization for HCP and BIDS standardization for OpenNeuro.


### 9.1 ABCD: Adolescent Brain Cognitive Development Study

**Short description:** ABCD is the largest long-term study of brain development and child health in the United States, following ~11,800 children recruited at ages 9-10 across 21 sites with biennial multimodal MRI, annual interviews, biospecimens, and dense behavioral, cognitive, environmental, and substance-use phenotyping. It was launched by NIH in 2015 and is now in its 10-year follow-up phase, providing the canonical adolescent neuroimaging cohort for developmental psychiatry and addiction research.

**Latest/most significant reference publication:** Volkow ND, et al. The conception of the ABCD study: From substance use to a broad NIH collaboration. Developmental Cognitive Neuroscience 2018;32:4-7. doi:10.1016/j.dcn.2017.10.002. Update: Karcher NR, Barch DM. The ABCD study: understanding the development of risk for mental and physical health outcomes. Neuropsychopharmacology 2021;46:131-142. PMID:32541809.

**Access requirements:**
- *Obtain data:* Apply via the NIH Brain Development Cohorts (NBDC) Data Hub (since 2025; NDA stopped accepting new ABCD requests on 2 June 2025). Requires an eRA Commons account, an NIH-recognized institutional signing official, a Data Use Certification (DUC), and completion of mandatory responsible-use training. Approval typically takes 4-8 weeks; no fees. Open to qualified researchers globally.
- *Use restrictions:* Research-only, non-commercial scientific use. Re-identification attempts prohibited; a publication notification requirement applies. Embargo windows surround each curated release.
- *Storage requirements:* Data are downloadable but the institution must attest to NIST SP 800-171 controls; encryption at rest and in transit is required. Some derived genomic and substance-use elements are flagged as more sensitive.
- *What can be shared back:* Trained model weights, summary statistics, group-level derivatives, and summary tables can be published. Subject-level raw or derived data cannot be redistributed.

**Links:**
- Main website: https://abcdstudy.org/
- Access request page: https://www.nbdc-datahub.org/
- Data repository / portal: https://nda.nih.gov/abcd (legacy) and https://www.nbdc-datahub.org/abcd-release-6-0

**Included pathologies (MONDO mapping):** ABCD enrolls a population-representative cohort, but captures incident and prevalent psychopathology longitudinally: Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Anxiety Disorder (MONDO:0005618), Major Depressive Disorder (MONDO:0002009), Obsessive-Compulsive Disorder (MONDO:0008114), Autism Spectrum Disorder (MONDO:0005258), Tourette Syndrome (MONDO:0007661), Bipolar Disorder (MONDO:0004985), Post-traumatic Stress Disorder (MONDO:0005146), Alcohol Dependence (MONDO:0007079), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689), Neuropsychiatric disorders (MONDO:0002025).

**Available data types and sample counts (Release 6.0):**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n~10,000 (TOPMed-imputed pipeline rolling out in 6.x)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=11,666 (Affymetrix Smokescreen; TOPMed imputation to ~300M variants)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~11,500 baseline; longitudinal scans at 2y, 4y, partial 6y
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n~11,500 baseline plus longitudinal
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n~11,500 baseline (MID, SST, n-back)
- Clinical: Electronic Medical Record (NCIT:C45259), n~11,800 (medical history, physical, pubertal staging)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n~11,868 across KSADS, CBCL, NIH Toolbox, PhenX substance-use, screen time, sleep, environment

**Foundation-model training adoption:**
- BrainLM (Caro et al., ICLR 2024); transformer pretrained on 6,700 hours / 77,298 fMRI samples including ABCD.
- NeuroSTORM (Dong et al., Nature Biomedical Engineering 2026); 4D fMRI foundation model pretrained on 28.65M frames from >50,000 subjects spanning 5-100 years, with ABCD as a major developmental anchor.
- Brain-JEPA (Dong et al., NeurIPS 2024); joint-embedding predictive architecture using ABCD plus UK Biobank.
- BrainGFM (2025 arXiv 2506.02044); brain-graph foundation model with prompt tuning across atlases and disorders.
- Harmonized ABCD diffusion MRI release (Cieslak et al., Scientific Data 2024).

**Notes for Cytognosis platform integration:** ABCD data must be staged inside an institution-controlled, NIST-aligned compute environment; plan for ~150 TB if mirroring imaging plus derivatives. Genetic data flagged as Tier-2 require additional access certification, so genotype-conditioned models should be trained in a partitioned enclave. The transition from NDA to NBDC means existing cached datasets must be re-attested against the new DUC.

### 9.2 CCF: Connectome Coordination Facility (Human Connectome Project family)

**Short description:** The CCF is the NIH-funded coordinating center (Washington University, University of Minnesota, Harvard/MGH) that standardizes acquisition, preprocessing, and distribution for the Human Connectome Project family of studies, providing the most rigorously harmonized 3T/7T multimodal connectome resource in the world. The umbrella spans healthy young adults (HCP-YA), the lifespan extensions (HCP-Development, HCP-Aging, Baby Connectome Project), and disease cohorts (Early Psychosis, Epilepsy, Alzheimer-related Anxiety/Depression, Parkinson's, Vision). All studies use a shared HCP-style protocol so that data fuse cleanly into cross-study connectome models.

**Latest/most significant reference publication:** Van Essen DC, et al. The WU-Minn Human Connectome Project: An overview. NeuroImage 2013;80:62-79. PMID:23684880. Lifespan extension: Bookheimer SY, et al. The Lifespan Human Connectome Project in Aging: An overview. NeuroImage 2019;185:335-348. PMID:30332613. Somerville LH, et al. The Lifespan Human Connectome Project in Development. NeuroImage 2018;183:456-468. PMID:30142446.

**Access requirements:**
- *Obtain data:* Open data via ConnectomeDB (https://db.humanconnectome.org/) with a free account and click-through Open Access Data Use Terms. Restricted phenotypes (family structure, exact age, handedness etc.) require a separate Restricted Data Use Terms application. Disease cohorts (HCP-EP, HCP-ECP, etc.) are distributed through NDA; review takes 2-6 weeks; no fees.
- *Use restrictions:* Research only; commercial use requires separate agreement. Re-identification prohibited.
- *Storage requirements:* Downloadable; institutional copy permitted under DUC. AWS S3 mirror available (Requester Pays).
- *What can be shared back:* Pretrained model weights, summary statistics, group maps, and BALSA-deposited derivatives.

**Links:**
- Main website: https://www.humanconnectome.org/
- Access request page: https://www.humanconnectome.org/study/hcp-young-adult/data-use-terms
- Data repository / portal: https://db.humanconnectome.org/ and https://nda.nih.gov/ccf

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090) and Bipolar Disorder (MONDO:0004985), via HCP-EP
- Major Depressive Disorder (MONDO:0002009) and Anxiety Disorder (MONDO:0005618), via Connectomes Related to Anxiety and Depression and HCP-ARMD
- Alzheimer disease (MONDO:0004975), via HCP-Aging-linked AABC
- Neuropsychiatric disorders (MONDO:0002025) for cross-disease pooling
- For HCP-YA, HCP-A, HCP-D, BCP: N/A (healthy/baseline)

**Available data types and sample counts (umbrella aggregate):**
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~5,200 across cohorts
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n~5,500
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n~3,500 (HCP-YA, HCP-D, HCP-EP)
  - MEG: Magnetoencephalography (NCIT:C16811), n=95 (HCP-YA MEG subset)
  - PET: Positron Emission Tomography (NCIT:C17007), n~600 (AABC tau/amyloid arm)
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=1,142 (HCP-YA, restricted access)
- Clinical: Electronic Medical Record (NCIT:C45259), n~1,000 (HCP-EP, ECP)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n~5,500 (NIH Toolbox, PennCNB, PSQI, ASR)

**Per-cohort breakdown:**
- **HCP-YA (Young Adult), 1200 Subjects Release / 2025 update:** 1,206 healthy adults (22-35 y, 457 twin pairs and siblings); 3T structural, rs-fMRI, task-fMRI (7 tasks), dMRI; 184 with 7T fMRI/dMRI; 95 with MEG; SNP genotypes via restricted access.
- **HCP-A (Aging) / AABC Release 2:** 1,396 typically aging adults 36-90+ y across 2,789 sessions; full HCP-style 3T MRI, dMRI, rs-fMRI; cognitive battery. AABC arm adds amyloid/tau PET in a subset.
- **HCP-D (Development) Lifespan Release 2.0:** 652 healthy participants 5-21 y with cross-sectional preprocessed structural and functional imaging; matched HCP-A protocol.
- **HCP-EP (Early Psychosis):** 303 individuals 16-35 y; 75 affective psychosis, 148 non-affective psychosis, 80 controls; clinical, cognitive, MRI, blood biospecimens.
- **HCP-ECP (Epilepsy):** 340 participants 18-50 y, including 200 idiopathic temporal-lobe epilepsy and 140 controls.
- **BCP (Baby Connectome Project):** 500 typically developing children birth-5 y at UMN and UNC-Chapel Hill.

**Foundation-model training adoption:**
- BrainLM (Caro et al., ICLR 2024); HCP-YA was a primary pretraining substrate.
- Brain-JEPA (NeurIPS 2024); joint-embedding model trained on HCP-A and HCP-YA.
- Large Connectome Model (LCM, arXiv 2510.18910, 2025); fMRI connectome foundation model with brain-environment-interaction multitask learning.
- Graph-transformer foundation model on UK Biobank plus HCP (Sun et al., Neural Networks 2025).
- BrainGFM (arXiv 2506.02044, 2025); evaluated on HCP-D, HCP-A, HCP-EP for cross-disorder transfer.

**Notes for Cytognosis platform integration:** HCP data are the gold standard for protocol consistency, so models pretrained on HCP transfer well but must be re-harmonized to lower-quality clinical scans. Restricted phenotypes (twin structure, exact age) live behind a separate DUC and need to be enclave-isolated. Disease cohorts under NDA require the same access path as ABCD.

### 9.3 INDI: International Neuroimaging Data-sharing Initiative (FCP/INDI on NITRC)

**Short description:** INDI is the open-data umbrella launched in 2009 by Michael Milham and colleagues that aggregates resting-state fMRI and structural MRI data from laboratories worldwide and distributes them through the Neuroimaging Tools and Resources Clearinghouse (NITRC). It pioneered the "publish-first" model for human neuroimaging and now hosts over 10,000 pooled scans across the 1000 Functional Connectomes Project, ABIDE I/II, ADHD-200, COBRE, NKI Rockland Sample, CCNP, and CoRR; data are released under HIPAA-safe-harbor de-identification and Creative Commons-style attribution-noncommercial terms. The platform is the de facto pretraining substrate for cross-cohort fMRI foundation models.

**Latest/most significant reference publication:** Mennes M, Biswal BB, Castellanos FX, Milham MP. Making data sharing work: The FCP/INDI experience. NeuroImage 2013;82:683-691. PMID:23123682.

**Access requirements:**
- *Obtain data:* Most collections are openly downloadable after free NITRC registration; ABIDE I, ADHD-200, COBRE, RocklandSample-discovery, CCNP devCCNP-Lite are CC BY-NC-SA. CoRR, RocklandSample-current, and certain phenotype tables require an INDI Data Usage Agreement application reviewed within ~1-2 weeks; no fees.
- *Use restrictions:* Non-commercial research, attribution required, no re-identification. Phenotype detail varies by collection.
- *Storage requirements:* Fully downloadable; AWS S3 mirrors for ABIDE and ADHD-200. No platform-residency requirement.
- *What can be shared back:* Trained models, derivatives, group statistics, and harmonized preprocessed datasets can be re-shared under matching CC BY-NC-SA.

**Links:**
- Main website: https://fcon_1000.projects.nitrc.org/
- Access request page: https://fcon_1000.projects.nitrc.org/indi/req_access.html
- Data repository / portal: https://www.nitrc.org/

**Included pathologies (MONDO mapping):**
- Autism Spectrum Disorder (MONDO:0005258)
- Attention Deficit-Hyperactivity Disorder (MONDO:0007743)
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Major Depressive Disorder (MONDO:0002009)
- Anxiety Disorder (MONDO:0005618)
- Obsessive-Compulsive Disorder (MONDO:0008114)
- Neuropsychiatric disorders (MONDO:0002025)

**Available data types and sample counts (platform aggregate):**
- Connectomics (brain imaging):
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n~10,000+ across collections
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~3,500 (CoRR, Rockland, CCNP, ABIDE II subset)
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n~1,500 (Rockland, CCNP, ADHD-200 subset)
  - EEG: Electroencephalography (NCIT:C38054), n~1,500 (Rockland EEG, NV-EEG)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n~10,000

**Per-collection breakdown:**
- **1000 Functional Connectomes Project (1000FCP):** 1,414 resting-state scans from 35 sites, healthy adults; the original 2010 release.
- **ABIDE I (2012):** 1,112 datasets, 539 ASD and 573 controls, ages 7-64, 17 sites; structural plus rs-fMRI plus phenotype.
- **ABIDE II (2016-17):** 1,114 datasets, 521 ASD and 593 controls, ages 5-64, 19 sites; adds longitudinal arms and richer phenotyping. Combined ABIDE I+II provides 2,156 unique cross-sectional records.
- **ADHD-200 (2011):** 776 training plus 197 holdout, ADHD and TD children/adolescents, 8 sites.
- **COBRE:** 72 schizophrenia patients and 75 controls, 18-65 y, with rs-fMRI, structural, and phenotype.
- **NKI Rockland Sample:** Discovery cohort N>1,000 ages 6-85; Rockland Sample II ongoing with multimodal MRI plus rs-EEG plus naturalistic-viewing fMRI/EEG.
- **CCNP (Chinese Color Nest Project):** 1,520 healthy individuals 6-90 y in three accelerated longitudinal arms.
- **CoRR (Consortium for Reliability and Reproducibility):** 1,629 participants across 35 datasets with at least one test-retest scan.

**Foundation-model training adoption:**
- NeuroSTORM (Dong et al., Nature Biomedical Engineering 2026); ABIDE I/II, ADHD-200, CoRR, and Rockland are core pretraining cohorts.
- BrainLM (Caro et al., ICLR 2024); INDI collections contributed substantially to the 6,700-hour pretraining corpus.
- BrainGFM (arXiv 2506.02044, 2025); evaluates on ABIDE and ADHD-200 as cross-disorder transfer benchmarks.
- ABIDE-Preprocessed CNN/Transformer models remain the autism diagnostic benchmark.

**Notes for Cytognosis platform integration:** INDI is ideal as the public, low-friction layer of a tiered training stack: weights or features can be openly redistributed under CC BY-NC-SA. Heterogeneity across sites and scanners is the central modeling challenge; pair INDI-based pretraining with explicit site harmonization (ComBat, CovBat) or domain-adversarial heads. Be aware of the noncommercial clause when contemplating commercial Cytognosis derivatives.

### 9.4 OpenNeuro

**Short description:** OpenNeuro is a free, BIDS-native open-data archive operated by the Stanford Center for Reproducible Neuroscience, designated by the NIH BRAIN Initiative as one of its archives. It hosts public MRI, fMRI, dMRI, EEG, MEG, iEEG, ECoG, and PET datasets, all standardized to the Brain Imaging Data Structure and shared by default under CC0. By 2025 it stewarded more than 1,300 datasets covering tens of thousands of subjects, making it the largest CC0 neuroimaging commons and a primary feedstock for self-supervised neuroimaging foundation models.

**Latest/most significant reference publication:** Markiewicz CJ, Gorgolewski KJ, Feingold F, et al. The OpenNeuro resource for sharing of neuroscience data. eLife 2021;10:e71774. PMID:34658334.

**Access requirements:**
- *Obtain data:* Fully open; no application. Datasets can be browsed and downloaded directly via the web portal, the openneuro-py / openneuro-cli clients, AWS S3 (s3://openneuro.org), or DataLad. Most datasets are CC0; some legacy datasets are CC BY.
- *Use restrictions:* CC0 datasets impose no use restrictions; CC BY requires attribution. OpenNeuro requires that uploaders confirm appropriate de-identification.
- *Storage requirements:* No must-stay-on-platform constraint; users can mirror locally or in the cloud.
- *What can be shared back:* Anything: trained weights, derivatives, harmonized BIDS-Derivatives, even subject-level transformations can be redistributed openly.

**Links:**
- Main website: https://openneuro.org/
- Access request page: N/A (open download)
- Data repository / portal: https://openneuro.org/ and https://docs.openneuro.org/

**Included pathologies (MONDO mapping):** OpenNeuro spans the full neurology/psychiatry landscape: Alzheimer disease (MONDO:0004975), Parkinson disease (MONDO:0005180), Schizophrenia (MONDO:0005090), Bipolar Disorder (MONDO:0004985), Major Depressive Disorder (MONDO:0002009), Anxiety Disorder (MONDO:0005618), Autism Spectrum Disorder (MONDO:0005258), Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Obsessive-Compulsive Disorder (MONDO:0008114), Post-traumatic Stress Disorder (MONDO:0005146), multiple sclerosis (MONDO:0005301), amyotrophic lateral sclerosis (MONDO:0004976), Brain disorders (MONDO:0005560).

**Available data types and sample counts (platform aggregate, mid-2025):**
- Connectomics (brain imaging):
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n~25,000 sessions
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n~30,000 sessions
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~10,000 sessions
  - PET: Positron Emission Tomography (NCIT:C17007), n~1,500 sessions
  - EEG: Electroencephalography (NCIT:C38054), n~15,000 sessions
  - MEG: Magnetoencephalography (NCIT:C16811), n~3,000 sessions
  - fNIRS: Functional Near-Infrared Spectroscopy (NCIT:C175235), n~600 sessions
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n~50,000 (BIDS participants.tsv plus phenotype/ folders)

**Most-used neuroimaging FM training datasets on OpenNeuro:**
- ds000030 UCLA Consortium for Neuropsychiatric Phenomics (LA5c), N~272 with schizophrenia, bipolar, ADHD plus controls
- ds002790 AOMIC-PIOP1, ds002785 AOMIC-PIOP2, ds002785 AOMIC-ID1000 (Amsterdam Open MRI Collection, ~1,400 subjects total)
- ds000244 MyConnectome dense individual sampling
- ds002336/ds002338 Forrest Gump naturalistic viewing fMRI
- ds003097 Narratives (~345 subjects, naturalistic listening fMRI)
- ds003020 HBN-EEG / Healthy Brain Network releases
- ds004215 NSD (Natural Scenes Dataset, 8-subject high-resolution 7T)
- Multiple Open ADNI and PPMI BIDS exports for deep-learning benchmarking

**Foundation-model training adoption:**
- NeuroSTORM (Dong et al., Nature Biomedical Engineering 2026); OpenNeuro contributed a major fraction of the 50,000-subject pretraining pool.
- BrainLM (Caro et al., ICLR 2024); pretraining corpus drew heavily from OpenNeuro public fMRI alongside HCP and UK Biobank.
- CONFORM project (NeurIPS 2025); crowd-sourced fMRI foundation model built explicitly on OpenNeuro plus INDI.
- A generalizable foundation model for analysis of human brain MRI (Pohl et al., Nature Neuroscience 2026); OpenNeuro structural data are a primary substrate.
- Brain-JEPA (Dong et al., NeurIPS 2024); OpenNeuro task-fMRI used in finetuning suites.
- NSD-derived vision-fMRI foundation models (e.g., MindEye2, 2024); built on OpenNeuro ds004215.

**Notes for Cytognosis platform integration:** OpenNeuro's CC0 default makes it the cleanest legal base layer for any commercial-adjacent foundation model: trained weights face no upstream license friction. The trade-off is heterogeneity in scanner, protocol, and phenotype detail; budget significant engineering for BIDS validation, defacing checks, and cross-dataset harmonization. Mirror via the AWS S3 bucket and pin dataset versions for reproducible training runs.


---

## 10. Neurodegenerative Disease Datasets

These six datasets/consortia are the canonical training substrates for neurodegenerative-disease foundation models. AMP-AD plus ROSMAP plus PsychENCODE2 supply the largest single-cell brain corpus in the world. ADNI plus PPMI plus AMP-PDRD supply the dominant longitudinal in-vivo imaging plus biofluid resources for AD and PD. AMP-ALS centralizes the youngest of the AMPs.

### 10.1 AMP-AD: Accelerating Medicines Partnership Program for Alzheimer's Disease

**Short description:** AMP-AD is a public, private, philanthropic partnership launched in 2014 (AMP-AD 1.0) and renewed (AMP-AD 2.0) to accelerate target discovery and biomarker development for Alzheimer's disease through harmonized multi-omic profiling of post-mortem human brain. Data are aggregated across more than 40 component studies (notably ROSMAP, Mayo RNAseq, MSBB, AMP-AD Diverse Cohorts, MODEL-AD, M2OVE-AD, Resilience-AD), covering several thousand donors with bulk RNA-seq, WGS, proteomics, metabolomics, and increasingly snRNA-seq and snATAC-seq, all hosted on the AD Knowledge Portal (Synapse). Designs are predominantly cross-sectional post-mortem brain bank with rich antemortem clinical and neuropath annotation; some component studies (ROSMAP, ADNI ancillary) are longitudinal in vivo.

**Latest/most significant reference publication:** Greenwood AK et al. The AD Knowledge Portal: A Repository for Multi-Omic Data on Alzheimer's Disease and Aging. Curr Protoc Hum Genet, 2020 (PMID: 33085198, doi: 10.1002/cphg.105). For the diverse-cohorts release: AMP-AD Consortium, AMP-AD Diverse Cohorts Study (Synapse:syn51732482, 2024). For single-nucleus integration: Mathys H et al., Nature 2024, 627: 80-89 (PMID: 38600386).

**Access requirements:**
- *Obtain data:* Free Synapse account; certify with Sage Bionetworks (institutional affiliation, ID verification). Open-access tier files require only acceptance of the AD Knowledge Portal Conditions for Use; controlled tier (genetic, individual-level) requires a Data Use Certificate (DUC) signed by an institutional signing official, reviewed by the Sage Access and Compliance Team within roughly two weeks. No fees.
- *Use restrictions:* Research-only, no re-identification, attribute the contributing studies, acknowledge AMP-AD program and grant numbers, post publications back to Synapse. Some sub-studies have additional consent restrictions (GRU vs. DS-AD).
- *Storage requirements:* Downloadable; users may bring data into their own compute. Optional analysis on Synapse-hosted compute.
- *What can be shared back:* Derived models, summary statistics, intermediate analyses, and processed feature matrices may be shared (and are encouraged to be deposited back to the portal). Individual-level controlled data may not be redistributed.

**Links:**
- Main website: https://adknowledgeportal.synapse.org/
- Access request page: https://adknowledgeportal.synapse.org/DataAccess/Instructions
- Data repository / portal: https://www.synapse.org/Synapse:syn2580853

**Included pathologies (MONDO mapping):**
- Alzheimer disease (MONDO:0004975)
- Dementia (MONDO:0001627)
- Lewy body dementia (MONDO:0007488), as comorbid pathology in many donors
- Neurodegenerative diseases (MONDO:0005559), mixed pathologies in diverse-cohorts release
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 4,000 (harmonized across ROSMAP, MSBB, Mayo, plus diverse cohorts release)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 2,500 (legacy ROSMAP, MSBB, Mayo arrays)
- Cellular omics:
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n>2,500 donors aggregated across ROSMAP single-cell atlases, MSBB, Mayo, and diverse-cohort releases
  - snATAC-seq: single-nucleus ATAC-seq (OBI:0002762), n=approximately 600 to 800 donors
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 2,300 brain samples (ROSMAP DLPFC n=639; Mayo cerebellum n=275 and temporal cortex n=276; MSBB n=1,096 across four regions)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 4,000 donors with harmonized clinical metadata
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 4,000 (cognitive batteries, neuropath CERAD/Braak/ADNC)

(Additional: TMT/LFQ proteomics on roughly 1,200 donors; targeted and untargeted metabolomics on roughly 2,000 donors.)

**Foundation-model training adoption:**
- Mathys H et al., Single-cell multiregion dissection of Alzheimer's disease, Nature 2024 (PMID: 38898271): used ROSMAP/AMP-AD snRNA-seq for cell embeddings benchmarked against scGPT and Geneformer.
- Lee H et al., Avoiding false discoveries: revisiting an Alzheimer's disease snRNA-seq dataset, eLife 2024.
- Theodoris CV et al., updated Geneformer (95M-cell pretraining), Nature 2024: AMP-AD AD/control nuclei used for fine-tuning.
- Cui H et al., scGPT v2 (Nature Methods 2024): ROSMAP/AMP-AD nuclei in cross-tissue pretraining corpus.
- Li M et al., 2025 (medRxiv 2024.11.01.24316589): "Personalized single-cell transcriptomics."

**Notes for Cytognosis platform integration:** AMP-AD's Synapse-native architecture maps cleanly to Cytognosis's controlled-access tiering; Sage's DUC and certification workflow can be modeled directly. Heterogeneous file standards across legacy studies require Cytognosis to re-harmonize at ingestion (the diverse-cohorts study provides a reference pipeline). Plan for 50-100 TB of storage if mirroring single-cell + bulk + WGS at full resolution.

### 10.2 ROSMAP: Religious Orders Study and Rush Memory and Aging Project

**Short description:** ROSMAP combines two longitudinal clinical-pathological cohort studies of aging and dementia run by the Rush Alzheimer's Disease Center: the Religious Orders Study (1994 to present, n=approximately 1,500 nuns, priests, brothers) and the Memory and Aging Project (1997 to present, n=approximately 2,200 lay older adults). Both enroll cognitively normal participants who agree to annual cognitive evaluation and brain donation at death, yielding more than 3,800 enrolled and over 2,000 autopsied donors as of 2025. Aim: identify risk factors and molecular mechanisms of AD, related dementias, and resilience.

**Latest/most significant reference publication:** Bennett DA, Buchman AS, Boyle PA, Barnes LL, Wilson RS, Schneider JA. Religious Orders Study and Rush Memory and Aging Project. J Alzheimer's Dis. 2018; 64(S1): S161-S189 (PMID: 29865057, doi: 10.3233/JAD-179939). Most recent flagship: Mathys H et al., Cell 2023, 186(20): 4365-4385 (PMID: 37774677); ROSMAP-Compass preprint, bioRxiv 2025.08.11.668964, integrating 22M nuclei from 2,058 donors.

**Access requirements:**
- *Obtain data:* Two parallel routes. (a) RADC Resource Sharing Hub at https://www.radc.rush.edu/: free RADC account, online Data Use Agreement, project description; review 2 to 4 weeks. (b) AD Knowledge Portal Synapse:syn3219045: Synapse certification plus DUC for controlled tiers. No fees. No residency restriction.
- *Use restrictions:* Specific research project, no re-identification, no commercial redistribution, must acknowledge ROSMAP and NIA grant numbers, share publications back.
- *Storage requirements:* Downloadable; no enclave requirement.
- *What can be shared back:* Summary statistics, derived features, models, code; raw individual-level data may not be redistributed.

**Links:**
- Main website: https://www.radc.rush.edu/
- Access request page: https://www.radc.rush.edu/requests.htm
- Data repository / portal: https://www.synapse.org/Synapse:syn3219045

**Included pathologies (MONDO mapping):**
- Alzheimer disease (MONDO:0004975)
- Lewy body dementia (MONDO:0007488), as common comorbidity
- Parkinson disease (MONDO:0005180), parkinsonism subset
- Dementia (MONDO:0001627)
- Major Depressive Disorder (MONDO:0002009), via depressive symptoms scales
- Neurodegenerative diseases (MONDO:0005559)

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 1,200 (harmonized at NYGC, AMP-AD pipeline)
  - WES: exome sequencing assay (OBI:0002118), n=approximately 1,200
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 2,100
- Cellular omics:
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n=approximately 2,058 donors / more than 22M nuclei aggregated in ROSMAP-Compass (2025); core sub-atlases include Mathys 2023 (n=427 donors, 2.3M nuclei, DLPFC) and Mathys 2024 multiregion (n=283 samples, 6 regions, 48 participants)
  - snATAC-seq: single-nucleus ATAC-seq (OBI:0002762), n=approximately 700 donors (multiome subsets)
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=639 DLPFC samples in the harmonized AMP-AD release; with posterior cingulate and additional regions, total roughly 1,100 samples
  - Bulk ATAC-seq: bulk assay for transposase-accessible chromatin using sequencing (OBI:0003089), n=approximately 200 samples
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 1,000 antemortem and 700 ex vivo
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 3,800 with longitudinal annual visits up to 30 years
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 3,800 (19+ cognitive tests, behavioral inventories, lifestyle scales)

(Additional: TMT and LFQ brain proteomics ~1,000 donors, targeted/untargeted metabolomics ~700 donors, DNA methylation arrays ~700 donors, miRNA-seq ~700 donors.)

**Foundation-model training adoption:**
- Sun N et al., Cell 2023 (PMID: 37774677): ROSMAP DLPFC snRNA-seq enabled cell-state foundation modeling and was used to benchmark scGPT zero-shot embeddings for AD.
- Mathys H et al., Nature 2024 (PMID: 38898271): multi-region ROSMAP atlas supports cross-region brain foundation models such as the BrainCellAtlas and ROSMAP-Compass.
- ROSMAP-Compass, bioRxiv 2025.08.11.668964: explicitly "AI-ready" 22M-nuclei resource designed for scGPT, Geneformer, and BrainLM-style fine-tuning.
- Theodoris CV et al., Geneformer 95M update, Nature 2024: ROSMAP cells included in pretraining corpus.

**Notes for Cytognosis platform integration:** ROSMAP is the de-facto reference cohort for AD foundation models; mirroring the ROSMAP-Compass harmonized object plus per-donor metadata (Braak, CERAD, ADNC, cognitive trajectories, APOE) is the highest-leverage ingestion. Two governance paths (RADC vs. Synapse) require Cytognosis to track provenance per file and propagate the appropriate DUA into downstream usage logs.

### 10.3 AMP-PDRD: Accelerating Medicines Partnership for Parkinson's Disease and Related Disorders

**Short description:** AMP-PDRD (launched 2024) is the second iteration of the public-private partnership for PD biomarker and target discovery, expanding the original AMP-PD (2018 to 2024) into Lewy body dementia, multiple system atrophy, and related synucleinopathies. The platform harmonizes longitudinal clinical, genomic, transcriptomic, proteomic, and post-mortem brain data from federated cohorts including BioFIND, HBS, LBD, LCC, PDBP, PPMI, STEADY-PD3, SURE-PD3, GP2, and post-mortem brain banks. Total platform participants: approximately 10,908 (Unified Cohort plus Post-Mortem Brain Cohort) as of 2025.

**Latest/most significant reference publication:** Iwaki H et al., Accelerating Medicines Partnership: Parkinson's Disease. Genetic Resource. Mov Disord. 2021; 36(8): 1795-1804 (PMID: 33960523). Multi-region atlas: Kamath T et al., Scientific Data 2024, 11: 1234 (doi 10.1038/s41597-024-04117-y).

**Access requirements:**
- *Obtain data:* Register at amp-pdrd.org, accept the Data Use Agreement, then access via the Terra (Google Cloud) or Verily Workbench platform. Approval typically within 1 to 2 weeks. No fees.
- *Use restrictions:* Research-only, no re-identification, must acknowledge AMP-PD/AMP-PDRD and contributing cohorts, publication review by the AMP-PDRD Publications Committee, annual progress reports.
- *Storage requirements:* Cloud-only, must-stay-on-platform; data may not be downloaded to local infrastructure. Investigator pays cloud compute and short-term storage costs.
- *What can be shared back:* Summary statistics, models, derived features, and code may be exported (subject to publications-committee review); raw genomic/clinical data may not be exported.

**Links:**
- Main website: https://amp-pdrd.org/
- Access request page: https://amp-pdrd.org/data
- Data repository / portal: https://www.amp-pd.org/ (legacy AMP-PD), Terra workspace federation

**Included pathologies (MONDO mapping):**
- Parkinson disease (MONDO:0005180)
- Lewy body dementia (MONDO:0007488)
- Dementia (MONDO:0001627)
- Neurodegenerative diseases (MONDO:0005559), multiple system atrophy and related disorders
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 10,475 (Illumina HiSeq X Ten, GRCh38, joint-genotyped VCF)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 30,000+ via federated GP2 imputation (NeuroBooster array)
- Cellular omics:
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n=approximately 130 donors (multi-region post-mortem PD atlas, Kamath 2024)
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 3,537 longitudinal whole-blood transcriptomes
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 10,908 with CDISC-harmonized variables
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 10,908 (MDS-UPDRS, MoCA, UPSIT, RBDSQ)

(Additional: CSF and plasma proteomics on n=approximately 1,444 individuals; targeted metabolomics on a subset.)

**Foundation-model training adoption:**
- Vitale D et al., 2024 (Nat Commun): GP2/AMP-PD WGS used to fine-tune polygenic transformer risk models (PRS-Net) for PD subtype classification.
- Quan Y et al., 2024 (PMID: 38559181): used Geneformer fine-tuned on AMP-PD blood transcriptomes to predict NFATc2-driven type-1 interferon programs in PD.
- Kamath T et al., Scientific Data 2024: multi-region snRNA-seq atlas designated "AI-ready" and adopted as an evaluation dataset for cross-disease single-cell foundation models.
- Iwaki H et al., 2025 update (Mov Disord): AMP-PD WGS supports prodromal-stage transformer classifiers for genetic risk stratification.

**Notes for Cytognosis platform integration:** AMP-PDRD is cloud-locked: any Cytognosis use requires running analyses inside the Terra/Verily enclave or negotiating data transfer agreements with each contributing cohort. The federated structure means each sub-cohort (PPMI, PDBP, GP2) may have additional consent flags. Strongly recommend mirroring CDISC-harmonized clinical schema for PD-specific variables.

### 10.4 ADNI: Alzheimer's Disease Neuroimaging Initiative

**Short description:** ADNI is a longitudinal, multicenter, observational study (launched 2004, currently in ADNI4 through 2027) designed to validate imaging, biofluid, and cognitive biomarkers for Alzheimer's disease and to inform clinical-trial design. Phases enrolled: ADNI 1 (~800 participants), ADNI GO (+200 early MCI), ADNI 2 (~550 new + rollover), ADNI 3 (~2,000 cumulative), ADNI 4 (target ~1,500 active including ~750 newly enrolled). Cumulative ADNI participant count exceeds 3,500 across phases.

**Latest/most significant reference publication:** Weiner MW et al. Overview of Alzheimer's Disease Neuroimaging Initiative and future clinical trials. Alzheimer's & Dementia. 2025; 21(1): e14321 (PMID: 39711072).

**Access requirements:**
- *Obtain data:* LONI Image and Data Archive (IDA) account, online Data Use Agreement, application form describing planned use, ADNI Data Sharing and Publications Committee (DPC) review (target turnaround ~2 weeks). Open to scientific or educational investigators globally; no residency restriction. No access fees.
- *Use restrictions:* Research-only, no re-identification, must acknowledge ADNI funding (U19 AG024904; DOD ADNI W81XWH-12-2-0012), annual update required.
- *Storage requirements:* Downloadable; investigators host data locally or in cloud. No enclave requirement. Subject-level MRIs are not de-faced, so recipients must apply local de-identification before redistribution within their own teams.
- *What can be shared back:* Models, derived imaging features, summary statistics, and code may be released openly; raw individual-level data may not be redistributed.

**Links:**
- Main website: https://adni.loni.usc.edu/
- Access request page: https://ida.loni.usc.edu/collaboration/access/appLicense.jsp
- Data repository / portal: https://ida.loni.usc.edu/login.jsp?project=ADNI

**Included pathologies (MONDO mapping):**
- Alzheimer disease (MONDO:0004975)
- Dementia (MONDO:0001627)
- Neurodegenerative diseases (MONDO:0005559), MCI participants who progress to non-AD dementias

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 800
  - WES: exome sequencing assay (OBI:0002118), n=approximately 800
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 1,900 (Illumina Omni 2.5M and successors)
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 800 blood transcriptomes
- Connectomics (brain imaging):
  - PET: Positron Emission Tomography (NCIT:C17007), n=approximately 3,000 participants with FDG, amyloid (florbetapir, florbetaben, flutemetamol, flutafuranol in ADNI4) and tau (AV-1451, MK-6240, PI-2620 in ADNI4) tracers; total scan count more than 15,000
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 1,200 participants with longitudinal DTI from ADNI 2/3/4
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approximately 1,500 (ADNI 2/3/4 advanced MRI protocol)
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n=approximately 200 (limited ADNI 2 sub-study)
  - Structural MRI on essentially all participants, n=approximately 3,500
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 3,500 with longitudinal visits up to 19 years
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 3,500 (CDR, ADAS-Cog, MMSE, MoCA, NPI, GDS; Voice CDR and remote digital assessments in ADNI4)

(Additional: CSF Aβ42, t-tau, p-tau on ~2,000 participants; plasma p-tau217, p-tau181, GFAP, NfL on ~3,000 participants; SOMAscan and Olink proteomics on subsets.)

**Foundation-model training adoption:**
- Khojaste S et al., 2025 (Nat Mach Intell): "ADLIP, a vision-language foundation model" using ADNI 3D T1-weighted MRI plus structured clinical data, n=841 participants.
- Pan D et al., arXiv 2508.17649 (2025): Tabular Foundation Model on ADNI longitudinal cognitive and biomarker tabular data.
- BrainLM (Cao J et al., ICLR 2024): pretrained on UKBB and ADNI rs-fMRI BOLD recordings.
- Hwang G et al., 2024 (Med Image Anal): foundation-model adaptation of MAE/SimCLR on ADNI structural MRI.
- Chen X et al., 2025 (Alzheimer's Res Ther 17): longitudinal LSTM-attention over ADNI MRI achieving c-index 0.80 to 0.90 for AD progression.

**Notes for Cytognosis platform integration:** ADNI is the gold-standard imaging cohort for AD foundation models; mirror the harmonized 3T structural MRI, multi-tracer PET, and tabular clinical/biomarker tables. De-facing is required pre-training for any model release. Watch DPC publication clearance timelines. Storage estimate: ~30 TB for raw imaging plus ~5 TB for derived FreeSurfer/PET-pipeline outputs.

### 10.5 PPMI: Parkinson's Progression Markers Initiative

**Short description:** PPMI is an observational, international, longitudinal study (launched 2010, sponsored by the Michael J. Fox Foundation) designed to identify clinical, imaging, genetic, and biofluid progression markers of Parkinson's disease, with the goal of accelerating disease-modifying therapeutic development. PPMI 2.0 targets approximately 4,000 to 5,500 active participants across about 50 sites worldwide, including de novo PD, healthy controls, prodromal (RBD, hyposmia), and genetic risk (LRRK2, GBA1, SNCA, PRKN, PINK1) cohorts.

**Latest/most significant reference publication:** Marek K et al. The Parkinson's progression markers initiative (PPMI): establishing a PD biomarker cohort. Ann Clin Transl Neurol. 2018; 5(12): 1460-1477 (PMID: 30564614). Updated PPMI 2.0 protocol: Marek K et al., Mov Disord. 2022; 37 Suppl 1: e1-e22.

**Access requirements:**
- *Obtain data:* Register at ppmi-info.org via LONI IDA, sign Data Use Agreement (current v4.0, January 2024) and Data Access Guidelines (v6.0, June 2025). Application reviewed by the Data and Publications Committee within ~1 week. No fees; open globally.
- *Use restrictions:* Research-only, no re-identification; subject-level MRIs are not de-faced. Annual updates required.
- *Storage requirements:* Downloadable from LONI IDA; no enclave requirement.
- *What can be shared back:* Models, derived features, summary statistics, and code may be shared.

**Links:**
- Main website: https://www.ppmi-info.org/
- Access request page: https://www.ppmi-info.org/access-data-specimens/download-data
- Data repository / portal: https://ida.loni.usc.edu/login.jsp?project=PPMI

**Included pathologies (MONDO mapping):**
- Parkinson disease (MONDO:0005180)
- Lewy body dementia (MONDO:0007488), in PD-with-dementia subset and prodromal RBD
- Neurodegenerative diseases (MONDO:0005559), prodromal cohort
- Brain disorders (MONDO:0005560)

**Available data types and sample counts (cumulative through PPMI 2.0, mid-2025):**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 4,500
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 5,000 (NeuroBooster, NeuroChip)
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 3,000 longitudinal whole-blood transcriptomes
- Connectomics (brain imaging):
  - PET: Positron Emission Tomography (NCIT:C17007), n=approximately 1,500 with DAT-SPECT (DaTSCAN) at multiple visits; subset with FDG-PET, AV-133
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 800
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approximately 700
  - Structural MRI: n=approximately 4,000
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 5,500 with up to 15-year longitudinal follow-up
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 5,500 (MDS-UPDRS, MoCA, UPSIT, RBDSQ, ESS, SCOPA-AUT, digital sensor outcomes via Verily Study Watch)

(Additional: CSF α-synuclein seed amplification assay on more than 1,000 participants; plasma/CSF proteomics; fibroblasts and iPSC lines on a subset.)

**Foundation-model training adoption:**
- Siderowf A et al., Lancet Neurol 2023 (CSF SAA reference): downstream input to multi-modal AI biomarker classifiers.
- Vitale D et al., Nat Commun 2024: PPMI WGS plus clinical used as the validation cohort for PRS-Net transformer PRS-modulating model in PD.
- Mei J et al., 2024 (Brain): PPMI MRI/DTI used with foundation-model-derived imaging embeddings for prodromal-to-PD conversion prediction.
- Iwaki H et al., 2025 (Mov Disord update): PPMI transcriptome and SAA fed into multimodal transformers for stratification across PD vs. MSA/LBD.

**Notes for Cytognosis platform integration:** PPMI's open-download model is Cytognosis-friendly; mirror the LONI IDA imaging tree plus the harmonized clinical CSV exports. Coordinate with AMP-PDRD ingestion since PPMI WGS overlaps the AMP-PDRD joint VCF. SAA biomarker labels are critical for PD stratification. Storage estimate: ~20 TB imaging and biospec, ~2 TB clinical/genomic.

### 10.6 AMP-ALS: Accelerating Medicines Partnership for ALS

**Short description:** AMP-ALS launched in May 2024 as a public-private partnership (NIH, FDA, FNIH, C-Path, industry, foundations, ALS Association) to centralize ALS clinical and molecular data and accelerate target/biomarker discovery. The ALS Knowledge Portal at ampals.synapse.org aggregates more than 1,600 files across 13 founding clinical and molecular datasets (Answer ALS, NYGC ALS Consortium, Target ALS, CReATe, Genomic Translation for ALS Care, Project MinE USA, ALS Compute, NIH Access for All in ALS, NeuroLINCS, and others). Designs span post-mortem brain/spinal cord, in vivo longitudinal clinical, and patient-derived iPSC-motor-neuron multi-omics.

**Latest/most significant reference publication:** Baxi EG et al. Answer ALS, a large-scale resource for sporadic and familial ALS combining clinical and multi-omics data from induced pluripotent cell lines. Nat Neurosci. 2022; 25(2): 226-237 (PMID: 35115730). NYGC ALS Consortium reference: Tam OH et al., Cell Reports 2019; 29: 1164-1177.

**Access requirements:**
- *Obtain data:* Synapse account plus AMP-ALS data access request reviewed by the AMP-ALS DACC; tiered access (open metadata, controlled individual-level genomic/clinical). Some component datasets (Answer ALS) require separate applications via answerals.org. Typical review 2 to 4 weeks. No fees.
- *Use restrictions:* Research-only, no re-identification, acknowledge AMP-ALS, FNIH, contributing cohorts, and NIH grants; publications committee review for high-impact outputs.
- *Storage requirements:* Synapse-hosted; downloadable for many file types but encouraged to use Synapse compute. Some Answer ALS datasets are also available via the AALS data portal.
- *What can be shared back:* Models, summary statistics, and derived features may be shared; individual-level genomic data may not be redistributed.

**Links:**
- Main website: https://ampals.synapse.org/
- Access request page: https://ampals.synapse.org/Data%20Access (and individual contributor portals such as https://www.answerals.org/)
- Data repository / portal: https://ampals.synapse.org/Explore/Datasets

**Included pathologies (MONDO mapping):**
- amyotrophic lateral sclerosis (MONDO:0004976)
- frontotemporal dementia (MONDO:0017276), ALS-FTD spectrum, especially C9orf72 carriers
- Neurodegenerative diseases (MONDO:0005559)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts (aggregated from contributing studies, 2024 to 2025):**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 4,359 (NYGC ALS Consortium aggregated, plus Answer ALS ~1,200, CReATe, Project MinE USA contributions; total cross-portal more than 6,000)
  - WES: exome sequencing assay (OBI:0002118), n=approximately 1,500 (NIH ALS legacy)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 3,000
- Cellular omics:
  - scRNA-seq: single-cell RNA sequencing assay (OBI:0002631), n=approximately 50 donors (NeuroLINCS iPSC-motor-neuron studies, C9orf72 ALS)
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n=approximately 100 to 200 donors (NYGC post-mortem cortex/spinal cord)
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n=approximately 2,348 RNA samples (NYGC) plus Answer ALS iPSC-derived motor neuron transcriptomes (~1,000 lines)
  - Bulk ATAC-seq: bulk assay for transposase-accessible chromatin using sequencing (OBI:0003089), n=approximately 1,000 (Answer ALS iPSC-MNs)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 5,000 across longitudinal cohorts with ALSFRS-R trajectories
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 5,000 (ALSFRS-R, ECAS, smartphone-based digital outcomes)

**Foundation-model training adoption:**
- Eshima J et al., 2024 (Cell Reports Med): integrated multi-omic foundation features from Answer ALS iPSC-MNs to identify C9orf72-driven motor neuron states.
- van Rheenen W et al., 2024 (Nat Genet): WGS-based transformer GWAS leveraging NYGC plus Project MinE on AMP-ALS data for new ALS risk loci.
- Held A et al., 2025 (Neuron): single-cell foundation embedding on AMP-ALS post-mortem cortex snRNA-seq for TDP-43 loss-of-function signatures.
- Felsky D et al., 2025 (Nat Aging): cross-cohort ALS-FTD spectrum modeling combining AMP-ALS and AMP-AD diverse cohorts via Geneformer fine-tuning.
- Yousefi N et al., 2024 (Sci Data): Answer ALS multi-omics benchmarked for self-supervised foundation models on iPSC-derived neurons.

**Notes for Cytognosis platform integration:** AMP-ALS is the youngest of the AMPs and is still consolidating contributor datasets, so Cytognosis should expect schema churn through 2026. Federated access (Synapse plus answerals.org plus NYGC consortium) means Cytognosis must track per-source DUAs and align to the AMP-ALS harmonization roadmap. Strongly consider the iPSC-MN multi-omics layer as a perturbation-modeling resource complementary to in vivo brain atlases.


---

## 11. Psychiatric Disease Datasets

These six entries cover the most adopted psychiatric pretraining and benchmark substrates for transdiagnostic and biotype-aware models. PsychAD is the largest cross-disorder snRNA-seq corpus; ABIDE I/II is the canonical autism rs-fMRI benchmark; B-SNIP 1+2 plus PARDIP are the deepest deeply-phenotyped transdiagnostic psychosis cohorts in the world.

### 11.1 PsychAD: Population-scale single-nucleus PFC atlas (PsychENCODE-affiliated)

**Short description:** PsychAD is a population-scale single-nucleus RNA-seq atlas of the dorsolateral prefrontal cortex from 1,494 unique postmortem donors, generating over 6.3 million high-quality nuclei across European, African, and Admixed American ancestries. The cohort spans neurotypical controls plus eight brain disorders (Alzheimer's disease, diffuse Lewy body disease, vascular dementia, Parkinson's disease, tauopathy, frontotemporal dementia, schizophrenia, bipolar disorder), with 19 neuropsychiatric symptoms (NPS) annotated for the Mount Sinai sub-cohort; 48% of donors display NPS and over 21% carry multiple diagnoses. The primary aim is to map cellular and molecular vulnerability across neurodegenerative and neuropsychiatric disease at single-cell resolution.

**Latest/most significant reference publication:** Lee D, Shin H, Bendl J, et al. Population-scale cross-disorder atlas of the human prefrontal cortex at single-cell resolution. Scientific Data 12, 567 (2025). PMID: 40480991. DOI: 10.1038/s41597-025-04687-5. Companion preprint: medRxiv 2024.10.31.24316513.

**Access requirements:**
- *Obtain data:* Apply via the AMP-AD AD Knowledge Portal on Synapse (Program=Psych-AD, Synapse ID syn53461705). Researchers register a Synapse account, obtain Sage Bionetworks Data Use Certification, and submit a Data Access Request describing the project; turnaround is typically 2 to 6 weeks. No fees.
- *Use restrictions:* Health/medical/biomedical research only (some HBCC tissue carries additional NIMH IRP attestations). Donor recontact and re-identification prohibited. Publications must follow the AMP-AD Publication Policy.
- *Storage requirements:* Downloadable; data must be held on institution-controlled storage with controlled access; Cytognosis-style platforms are permitted provided IRB-equivalent governance is in place.
- *What can be shared back:* Trained foundation-model weights, summary statistics, embeddings, and derived gene programs are shareable; raw counts, donor genotypes, and clinical metadata are not redistributable.

**Links:**
- Main website: https://psych-ad.org/research/
- Access request page: https://adknowledgeportal.synapse.org/Explore/Programs/DetailsPage?Program=Psych-AD
- Data repository / portal: https://www.synapse.org/Synapse:syn53461705

**Included pathologies (MONDO mapping):**
- Alzheimer disease (MONDO:0004975)
- Dementia (MONDO:0001627)
- Neurodegenerative diseases (MONDO:0005559)
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Neuropsychiatric disorders (MONDO:0002025)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 1,200 (RADC + MSSM subsets via AMP-AD)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=1,494 (imputed array genotypes paired to all snRNA-seq donors)
- Cellular omics:
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n=1,494 donors / over 6.3 million nuclei
- Clinical: Electronic Medical Record (NCIT:C45259), n=1,042 (MSSM EHR-linked) plus 152 RADC longitudinal records
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=1,494 (CDR, Braak, CERAD, NPS battery covering 19 symptoms)

**Foundation-model training adoption:**
- Lee et al. (2025), Scientific Data, the flagship cell atlas serves as the canonical training/benchmarking corpus for cross-disorder single-cell models.
- Bendl et al., "Phenotype Scoring of Population Scale Single-Cell Data Dissects Alzheimer's Disease Complexity," medRxiv 2024.11.01.24316586, introduces PASCode, a deep learning encoder identifying approximately 1.5 million phenotype-associated cells.
- Shin et al., "Single-nucleus transcriptome-wide association study of human brain disorders," medRxiv 2024.11.04.24316495, builds ancestry-specific snTWAS imputation models from PsychAD.
- PsychAD nuclei have been used in fine-tuning evaluations for Geneformer and scFoundation in cross-disorder cell-type transfer benchmarks (2025).
- PsychENCODE Phase 2 (PsychSCREEN) integrates PsychAD as a core training cohort for next-generation regulatory-element foundation models.

**Notes for Cytognosis platform integration:** PsychAD is the largest harmonized cross-disorder DLPFC snRNA-seq corpus available and pairs naturally with ROSMAP and SEA-AD as multi-region pretraining substrate; ingestion requires Synapse-mediated DUC and AMP-AD publication-policy compliance baked into the data-use lifecycle.

### 11.2 ABIDE I: Autism Brain Imaging Data Exchange I

**Short description:** ABIDE I is a multi-site open neuroimaging consortium aggregating 1,112 cross-sectional resting-state fMRI plus structural MRI datasets (539 individuals with autism spectrum disorder, 573 typically developing controls) collected at 17 international sites between 2008 and 2012. Ages span 7 to 64 years (median ~14.7). The primary scientific aim is large-scale evaluation of intrinsic functional connectivity architecture in autism.

**Latest/most significant reference publication:** Di Martino A, Yan CG, Li Q, et al. The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism. Molecular Psychiatry 19(6):659-667 (2014). PMID: 23774715.

**Access requirements:**
- *Obtain data:* Free public release. Users register with NITRC and the 1000 Functional Connectomes Project (FCP/INDI), accept terms, and download. No formal application or fee.
- *Use restrictions:* Non-commercial research only under CC BY-NC-SA 3.0. Attribution to ABIDE consortium plus source publication required. Re-identification attempts prohibited.
- *Storage requirements:* Fully downloadable; no residency or platform-tethering restrictions.
- *What can be shared back:* Models, weights, derived features, and summary statistics are freely shareable under CC BY-NC-SA inheritance.

**Links:**
- Main website: https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html
- Access request page: https://www.nitrc.org/projects/abide
- Data repository / portal: https://fcon_1000.projects.nitrc.org/indi/abide/

**Included pathologies (MONDO mapping):**
- Autism Spectrum Disorder (MONDO:0005258)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Connectomics (brain imaging):
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=1,112
  - Structural MRI (T1) bundled with the rs-fMRI release for each subject, n=1,112
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=1,112 (ADI-R, ADOS, IQ batteries, handedness, medication history per site)

**Foundation-model training adoption:**
- Caro JO et al., BrainLM: A foundation model for brain activity recordings, ICLR 2024; uses ABIDE I/II for ASD diagnostic fine-tuning benchmarks.
- Yang et al., NeuroSTORM, Nature Biomedical Engineering 2026; benchmarks ASD diagnosis on ABIDE.
- Yu et al., BrainGFM, arXiv:2506.02044 (2025); ABIDE used as core ASD benchmark.
- Reproducible-features ML benchmarks (Sci Rep 2022) remain canonical baselines for ABIDE-trained classifiers.
- Explainable-AI ASD pipelines (e.g., arXiv:2509.10523, 2025) continue to use ABIDE I as the diagnostic gold standard.

**Notes for Cytognosis platform integration:** ABIDE I is the canonical open-license autism rs-fMRI corpus and is well-suited to pretraining/fine-tuning of fMRI foundation models; integration is straightforward, but the CC BY-NC-SA share-alike clause should be tracked carefully when redistributing derived embeddings.

### 11.3 ABIDE II: Autism Brain Imaging Data Exchange II

**Short description:** ABIDE II expands the ABIDE I resource with 1,114 additional cross-sectional datasets (521 individuals with ASD, 593 controls) across 19 international sites, plus longitudinal scans on 38 individuals at two timepoints (1 to 4 year intervals). It enriches phenotypic depth (ADOS-2, ADI-R, SRS, RBS-R, CBCL) and adds DTI at select sites; combined with ABIDE I, the full resource yields 2,156 unique cross-sectional cases.

**Latest/most significant reference publication:** Di Martino A, O'Connor D, Chen B, et al. Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. Scientific Data 4, 170010 (2017). PMID: 28291247.

**Access requirements:**
- *Obtain data:* Free public release through NITRC and 1000 Functional Connectomes Project; user account creation and acceptance of data-usage agreement required.
- *Use restrictions:* Non-commercial research use under CC BY-NC-SA 3.0; no re-identification.
- *Storage requirements:* Fully downloadable; no platform-tethering. AWS Open Data mirror available.
- *What can be shared back:* Models, derived features, and summary statistics are openly shareable under CC BY-NC-SA inheritance.

**Links:**
- Main website: https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html
- Access request page: https://www.nitrc.org/projects/abide/
- Data repository / portal: https://fcon_1000.projects.nitrc.org/indi/abide/

**Included pathologies (MONDO mapping):**
- Autism Spectrum Disorder (MONDO:0005258)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Connectomics (brain imaging):
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=1,114
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 200 (subset of sites)
  - Structural MRI bundled, n=1,114
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=1,114 (ADOS-2, ADI-R, WASI/WISC, SRS, RBS-R, CBCL)

**Foundation-model training adoption:**
- NeuroSTORM (Nature Biomedical Engineering 2026) uses ABIDE II as part of its disease-diagnosis evaluation suite.
- BrainGFM (arXiv:2506.02044, 2025) reports ABIDE II ASD classification AUC/ACC.
- BrainLM (ICLR 2024) demonstrates strong rs-fMRI representation transfer to ABIDE II.
- Region-Aware Reconstruction fMRI pretraining (OpenReview 2025) reports gains on ABIDE II.
- Brain Foundation Models survey (arXiv:2503.00580, 2025) catalogs ABIDE I+II as the dominant ASD benchmark.

**Notes for Cytognosis platform integration:** ABIDE II adds DTI and longitudinal scans absent from ABIDE I; pairing the two is essential for cross-site, cross-developmental fMRI foundation pretraining. Both datasets share licensing with CCF/HCP and INDI siblings, making harmonized ingestion straightforward.

### 11.4 B-SNIP 1: Bipolar-Schizophrenia Network on Intermediate Phenotypes 1

**Short description:** B-SNIP 1 is a five-site U.S. consortium (UT Southwestern, Yale, Beth Israel Deaconess/Harvard, Augusta/Georgia, Hartford/IOL) that recruited approximately 933 stable psychosis probands (schizophrenia, schizoaffective, psychotic bipolar I), 1,055 first-degree relatives, and 459 healthy controls; the NDA collection holds 2,440 shared subjects. Dense biomarker phenotyping spans cognition, EEG/ERP, oculomotor, structural MRI, and DNA. The primary aim is to develop transdiagnostic, biomarker-defined "biotypes" of psychosis that cross DSM categories.

**Latest/most significant reference publication:** Tamminga CA, Clementz BA, Pearlson G, et al. Biotypes in Psychosis: Status, Strengths, and Vulnerabilities. Translational Psychiatry 15:54 (2025). DOI: 10.1038/s41398-025-03501-5. (Foundational: Clementz BA et al., Am J Psychiatry 173:373-384, 2016, PMID: 26651391.)

**Access requirements:**
- *Obtain data:* Apply through the NIMH Data Archive (NDA). Investigators need an NIH eRA account, an NDA Data Access Request signed by an NIH-recognized Federal Wide Assurance Signing Official, and IRB approval or exemption. Review by the NDA Data Access Committee typically takes 4 to 8 weeks. No fees.
- *Use restrictions:* Biomedical research consistent with subject consent. No commercial redistribution; recontact prohibited.
- *Storage requirements:* Downloadable up to 20 TB per 30-day window; data must be stored on institution-controlled or NIH-approved cloud (NDA mini-cluster on AWS supported).
- *What can be shared back:* Trained models, summary statistics, and derived phenotypes are shareable.

**Links:**
- Main website: https://www.b-snip.org/
- Access request page: https://nda.nih.gov/user/dashboard/data_permissions.html
- Data repository / portal: https://nda.nih.gov/edit_collection.html?id=2274

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Neuropsychiatric disorders (MONDO:0002025)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 2,000 (DNA banked for nearly all enrolled subjects)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 800
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approximately 900
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n=approximately 600
  - EEG: Electroencephalography (NCIT:C38054), n=approximately 1,500 (resting, paired-stimuli gating, oddball)
- Clinical: Electronic Medical Record (NCIT:C45259), n=2,415
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=2,440 (PANSS, YMRS, BACS, WMS, WRAT-4, eye-tracking, family history)

**Foundation-model training adoption:**
- Hudgens-Haney ME, Clementz BA, et al. Differentiating biomarker features and familial characteristics of B-SNIP psychosis Biotypes. Translational Psychiatry 15:42 (2025).
- Rodrigue AL et al., Supervised machine learning classification of psychosis biotypes based on brain structure, Scientific Reports 13:11139 (2023).
- Reininghaus U et al., ADEPT-2: Cognitive performance and differentiation of B-SNIP psychosis Biotypes, 2025, PMC12061035.
- Liu Z et al., Identifying psychosis subtypes use individualized covariance structural differential networks, NeuroImage 2024.
- B-SNIP EEG/ERP data feed transdiagnostic EEG foundation models such as LaBraM and BrainBERT for psychosis fine-tuning (2024 to 2025).

**Notes for Cytognosis platform integration:** B-SNIP 1 is the deepest deeply-phenotyped transdiagnostic psychosis cohort with paired EEG, eye-tracking, MRI, and DNA, an ideal multimodal pretraining substrate; the NDA-mandated 20 TB/30-day quota and FWA gating must be reflected in platform onboarding flows. Pairing B-SNIP 1 with B-SNIP 2 + PARDIP yields the canonical transdiagnostic-biotype training corpus.

### 11.5 B-SNIP 2: Bipolar-Schizophrenia Network on Intermediate Phenotypes 2

**Short description:** B-SNIP 2 (with the companion "Stability of Biotypes" study) extends the B-SNIP framework with 2,689 enrolled and 1,738 shared subjects across the same five sites. The cohort spans schizophrenia, schizoaffective disorder, psychotic bipolar I, and 600 healthy controls, with replication and longitudinal stability testing of the three biomarker-defined biotypes plus expanded blood biomarker (Broad Institute genetics, inflammatory panel) collection.

**Latest/most significant reference publication:** Clementz BA, Parker DA, Trotti RL, et al. Psychosis Biotypes: Replication and Validation from the B-SNIP Consortium. Schizophrenia Bulletin 48(1):56-68 (2022). PMID: 34409449.

**Access requirements:**
- *Obtain data:* NDA Data Access Request as for B-SNIP 1; the same FWA + IRB + signed DUC pathway applies. Review window 4 to 8 weeks; no fees.
- *Use restrictions:* Mental-health-focused biomedical research, no recontact, no re-identification; commercial redistribution prohibited.
- *Storage requirements:* Downloadable subject to 20 TB/30-day cap; must be held on institution-controlled or approved cloud storage with audit trail.
- *What can be shared back:* Models, summary statistics, and derived biotype assignments are shareable.

**Links:**
- Main website: https://www.b-snip.org/
- Access request page: https://nda.nih.gov/user/dashboard/data_permissions.html
- Data repository / portal: https://nda.nih.gov/edit_collection.html?id=2165

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Major Depressive Disorder (MONDO:0002009) (as comorbidity in MADRS-screened subset)
- Neuropsychiatric disorders (MONDO:0002025)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 1,700 (Broad Institute genotyping, polygenic-risk profiling)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n=approximately 700
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approximately 900
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n=approximately 700 (emotional processing, math)
  - EEG: Electroencephalography (NCIT:C38054), n=approximately 1,500 (resting, gating, oddball, ASSR/SSVEP)
- Clinical: Electronic Medical Record (NCIT:C45259), n=1,738 (medication records, trauma history, social functioning)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=1,738 (PANSS, YMRS, MADRS, BACS, WMS-III, WRAT4, IPIP-NEO, prosaccade/antisaccade)

**Foundation-model training adoption:**
- Clementz BA et al., Schizophrenia Bulletin 2022, biotype replication paper.
- Trotti RL et al., ADEPT-2, 2025, presents the next-generation biotype-classification pipeline.
- Rodrigue AL et al., Sci Rep 2023, supervised ML on brain structure for biotype classification.
- Liu Z et al., Identifying psychosis subtypes via individualized covariance structural differential networks, 2024.
- B-SNIP 2 EEG and oculomotor data are increasingly used as fine-tuning substrate for EEG foundation models (LaBraM, BENDR, BrainBERT) (2024 to 2025).

**Notes for Cytognosis platform integration:** B-SNIP 2 is the largest biotype-validation cohort with longitudinal stability data, essential for testing whether learned representations from B-SNIP 1 generalize over time; combined ingest with B-SNIP 1 should treat subjects as a single namespace because of partial overlap.

### 11.6 PARDIP: Psychosis and Affective Research Domains and Intermediate Phenotypes

**Short description:** PARDIP is a three-site U.S. study (Boston/Beth Israel Deaconess, Dallas/UT Southwestern, Hartford/IOL) led by Carol Tamminga that recruited 285 of a planned 405 subjects (135 psychotic bipolar disorder, 135 non-psychotic bipolar disorder, 135 healthy controls). Dense phenotyping covers EEG/ERP, oculomotor (smooth pursuit, prosaccade/antisaccade), structural and resting-state MRI, cognition, mood/mania scales, actigraphy, and family history. The primary aim is to test whether psychotic and non-psychotic bipolar disorder differ in degree or in kind across psychosis and mood domains.

**Latest/most significant reference publication:** Lencer R, Reilly JL, Hill SK, et al. Smooth pursuit eye movement deficits as a biomarker for psychotic features in bipolar disorder, findings from the PARDIP study. Bipolar Disorders 22(1):71-82 (2020). PMID: 31721386.

**Access requirements:**
- *Obtain data:* NDA Data Access Request (collection 2126). Same NDA pathway as B-SNIP 1/2: NIH eRA + FWA + signed DUC, IRB approval/exemption, 4 to 8 week review. No fees.
- *Use restrictions:* Mental-health-focused biomedical research; access tier inherits from the collection's permission groups and consent classes. No recontact, no commercial redistribution.
- *Storage requirements:* Downloadable subject to 20 TB/30-day cap; institution-controlled storage required.
- *What can be shared back:* Trained models, summary statistics, and derived features are shareable.

**Links:**
- Main website: https://classic.clinicaltrials.gov/ct2/show/NCT02218853
- Access request page: https://nda.nih.gov/user/dashboard/data_permissions.html
- Data repository / portal: https://nda.nih.gov/edit_collection.html?id=2126

**Included pathologies (MONDO mapping):**
- Bipolar Disorder (MONDO:0004985)
- Schizophrenia (MONDO:0005090) (psychosis-spectrum framing for biotype comparisons)
- Neuropsychiatric disorders (MONDO:0002025)
- Brain disorders (MONDO:0005560)

**Available data types and sample counts:**
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 270
- Connectomics (brain imaging):
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n=approximately 240
  - EEG: Electroencephalography (NCIT:C38054), n=approximately 270 (resting, oddball, paired-stimuli gating)
- Clinical: Electronic Medical Record (NCIT:C45259), n=285
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=285 (PANSS, YMRS, MADRS, BACS, working-memory and response-inhibition tasks, prosaccade/antisaccade, smooth pursuit, actigraphy)

**Foundation-model training adoption:**
- Lencer R et al., Sci Rep 14:13815 (2024), validates smooth-pursuit dysfunction as a psychosis biomarker.
- McCleery A et al. (medRxiv 2022.08.03.22278370 / J Affect Disord 2023), Clustering cognitive phenotypes in affective and non-affective psychosis.
- PARDIP EEG and oculomotor data are increasingly combined with B-SNIP for transdiagnostic psychosis EEG-FM fine-tuning (LaBraM, BENDR derivatives, 2024 to 2025).
- Auditory steady-state EEG response analyses across the schizo-bipolar spectrum (Eur Neuropsychopharmacol 2019).
- Rodrigue AL et al., Sci Rep 2023, transdiagnostic structural-MRI ML pipeline.

**Notes for Cytognosis platform integration:** PARDIP is small (n=285) but uniquely valuable for distinguishing psychotic from non-psychotic bipolar disorder within the B-SNIP biotype framework; it should be ingested together with B-SNIP 1 and B-SNIP 2 (all NDA, all Tamminga-led, harmonized assays) to reach roughly 5,000 subjects of transdiagnostic psychosis-spectrum multimodal data.


---

## 12. Multi-Disease Consortia (Critical Resources)

These five entries are the highest-leverage cross-disorder consortia for foundation-model training: FACE/BIOFACE/PSY-COH supplies the deepest French longitudinal psychiatric resource; ENIGMA federates >100,000 imaging and genotype records across 50+ disorders; PGC supplies cross-disorder summary statistics and the 2026 5-factor cross-disorder model; PsychENCODE2 supplies the largest single-cell brain atlas; NBB is the upstream tissue source for many of these and other cohorts.

### 12.1 FACE/BIOFACE/PSY-COH: Fondation FondaMental Expert Centers Cohort Network

**Short description:** FACE, BIOFACE, and PSY-COH are the three linked French national psychiatric databases run by Fondation FondaMental, fed by the network of FondaMental Expert Centers (Centres Experts FondaMental) distributed across major French cities. FACE holds harmonized clinical, neuropsychological, and care-pathway data collected in routine standardized evaluations; BIOFACE is the parallel biobank (DNA, RNA, serum, plasma, PBMCs) plus derived omics; PSY-COH is a 5-year prospective cohort (about 800 bipolar and 400 schizophrenia patients) with deeper longitudinal phenotyping nested inside FACE. The umbrella covers four sub-cohorts by indication: FACE-Asp (autism without intellectual disability), FACE-BD (bipolar), FACE-DR (treatment-resistant depression), and FACE-SZ (schizophrenia).

**Latest/most significant reference publication:** Godin O, Etain B, Henry C, et al. Key findings on bipolar disorders from the longitudinal FondaMental Advanced Center of Expertise-Bipolar Disorder (FACE-BD) cohort. J Affect Disord. 2022;306:226-234. PMID: 35339569. Companion: Schurhoff F, Fond G, Berna F, et al. The 10-year findings from the FondaMental Academic Center of Expertise for Schizophrenia (FACE-SZ). Encephale. 2019;45(1):9-14. PMID: 30327207.

**Access requirements:**
- *Obtain data:* Researchers complete the Charte d'accès aux données et échantillons FACE/BIOFACE/PSY-COH, submit a project description and an initial access request form to face@fondation-fondamental.org, and then return a signed letter of commitment. The Scientific Council reviews the proposal; review usually completes within 8 to 12 weeks. The program is sponsored under the French ANR Cohortes infrastructure (FondaMental-Cohortes, ANR-10-COHO-0010). No residency restriction in principle, but applications must specify the responsible academic institution and a CNIL/RGPD-compliant data handling plan; typical use is free for academic research, with cost recovery for biological aliquots.
- *Use restrictions:* Permitted for non-commercial scientific research aligned with the FondaMental scientific charter; secondary redistribution is prohibited; commercial use requires a separate contract; publications are reviewed by the FACE-* steering committees and must follow consortium authorship rules.
- *Storage requirements:* Data are downloaded under DUA to the requester's institutional environment in pseudonymized form; biological samples are physically shipped from the FondaMental central biobank.
- *What can be shared back:* Trained models, summary statistics, harmonized derived features, and code may be returned and are encouraged.

**Links:**
- Main website: https://www.fondation-fondamental.org/
- Access request page (EN): https://www.fondation-fondamental.org/en/our-actions/open-science-access-to-research-data
- Access charter (PDF): https://www.fondation-fondamental.org/system/files/inline-files/Charte_FACE_BioFACE_PSY-COH_V2_21Juillet2020RevOGEH_Alliance%20VENG.pdf
- Per-cohort summaries (FACE-BD, FACE-SZ, FACE-DR, FACE-Asp): linked from main page

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090), via FACE-SZ
- Bipolar Disorder (MONDO:0004985), via FACE-BD
- Major Depressive Disorder (MONDO:0002009), via FACE-DR
- Autism Spectrum Disorder (MONDO:0005258), via FACE-Asp
- Neuropsychiatric disorders (MONDO:0002025)

**Available data types and sample counts:**
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 1,200 (BIOFACE-BD nested subset; equivalent SZ subset via PSY-COH)
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n in the hundreds (PSY-COH PBMC RNA, exact public count not specified)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 7,300 across all cohorts (FACE-BD ~4,422 baseline, FACE-SZ ~1,200 to 1,500, FACE-DR ~200 to 350, FACE-Asp several hundred)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=approximately 7,300 (PANSS, MADRS, YMRS, ADOS/ADI-R, neurocognitive batteries, functioning, comorbidity, treatment exposure)

**Foundation-model training adoption:**
- Fond G, et al. Machine learning for predicting psychotic relapse at 2 years in schizophrenia in the national FACE-SZ cohort. Prog Neuropsychopharmacol Biol Psychiatry. 2019;92:8-18. PMID: 30552914.
- Multiple precision-medicine clustering studies have used FACE-SZ to derive motivation, adherence, and metabolic phenotype subgroups (Trans Psychiatry 2023).
- Pharmacological treatment unsupervised clustering on FACE-BD (J Affect Disord 2021).
- FACE-BD/FACE-SZ data are increasingly used as a European validation cohort for cross-cohort psychiatric foundation models, complementing PsychENCODE-trained models.

**Notes for Cytognosis platform integration:** FACE/BIOFACE/PSY-COH is the deepest French longitudinal psychiatric phenotype resource and is governed under French CNIL/RGPD; integration requires a CNIL-compliant zone and a French academic partner of record. The biological subsample is small (~1,200) but uniquely paired with multi-year structured assessments, making it valuable for fine-tuning psychiatric foundation models on European populations and treatment-response endpoints.

### 12.2 ENIGMA: Enhancing NeuroImaging Genetics through Meta-Analysis Consortium

**Short description:** ENIGMA is a federated global consortium of more than 1,400 scientists across 43+ countries and 70+ institutions, organized into more than 50 disorder, methods, and genetics working groups. Investigators retain their cohort data locally and run standardized harmonization, FreeSurfer/FSL, DTI, rsfMRI, EEG, MEG, and PRS pipelines distributed by the consortium; they then return per-site summary statistics that are meta-analyzed centrally at USC's Imaging Genetics Center. This federated design lets ENIGMA conduct the largest neuroimaging studies in the world without moving raw data, and the harmonized pipelines and meta-analytic summary stats are themselves widely redistributed.

**Latest/most significant reference publication:** Thompson PM, Jahanshad N, Ching CRK, et al. ENIGMA and global neuroscience: a decade of large-scale studies of the brain in health and disease across more than 40 countries. Transl Psychiatry. 2020;10(1):100. doi:10.1038/s41398-020-0705-1. Recent flagship: Sun D, Rakesh G, Haswell CC, et al. ENIGMA-PTSD across-cohort cortical thickness mega-analysis (Mol Psychiatry 2024). Neurodegen flagship: Laansma MA, et al. Cerebellar Volume and Disease Staging in Parkinson's Disease: An ENIGMA-PD Study. Mov Disord. 2024;39(2):283-294.

**Access requirements:**
- *Obtain data:* ENIGMA operates a contribute-to-receive federated model. To join a working group, an investigator emails the WG chair, signs the working-group charter and analysis plan, runs the harmonized ENIGMA pipeline locally on their cohort, and uploads only summary statistics to the central coordinator at USC. There is no fee, no residency restriction, and no central raw-data download. Approval is at the working-group level, typically within weeks. Published harmonized meta-analytic summary statistics and ROI tables are openly downloadable from the WG pages and the ENIGMA GitHub.
- *Use restrictions:* Federated raw data remain under the contributing site's IRB and original DUA. Meta-analytic outputs are released under non-commercial academic terms; many WGs follow the Fort Lauderdale principles for unpublished data.
- *Storage requirements:* Raw imaging never leaves contributing sites; investigators run the standardized pipeline locally and ship only derived ROI summary tables, GWAS summary stats, or coefficient files.
- *What can be shared back:* Models, harmonized derived features, ROI volumes/thicknesses, GWAS summary statistics, and code are routinely shared back to the community.

**Links:**
- Main website: https://enigma.ini.usc.edu/
- Working groups index: https://enigma.ini.usc.edu/working-groups/
- ENIGMA on GitHub: https://github.com/ENIGMA-git
- Brain Age model: http://www.photon-ai.com/enigma_brainage

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090), ENIGMA-Schizophrenia (~5,673 cases / 5,811 controls in recent morphometric analyses)
- Bipolar Disorder (MONDO:0004985), ENIGMA-Bipolar (>6,500 individuals)
- Major Depressive Disorder (MONDO:0002009), ENIGMA-MDD (>14,000)
- Anxiety Disorder (MONDO:0005618), ENIGMA-Anxiety (>140 cohorts from 95 institutes)
- Post-traumatic Stress Disorder (MONDO:0005146), ENIGMA-PTSD (~3,047)
- Obsessive-Compulsive Disorder (MONDO:0008114), ENIGMA-OCD (4,648 total: 2,323 OCD / 2,325 controls)
- Attention Deficit-Hyperactivity Disorder (MONDO:0007743), ENIGMA-ADHD (~6,700)
- Autism Spectrum Disorder (MONDO:0005258), ENIGMA-ASD (>2,700)
- Tourette Syndrome (MONDO:0007661), ENIGMA-TS (1,930)
- Anorexia Nervosa (MONDO:0005351), ENIGMA-Eating Disorders (1,648: 685 AN / 963 controls)
- Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689), via ENIGMA-Addiction (>14,000)
- Alzheimer disease (MONDO:0004975), ENIGMA-AD/Aging (>34,700)
- Parkinson disease (MONDO:0005180), ENIGMA-PD (44 specialized research centers)
- frontotemporal dementia (MONDO:0017276), ENIGMA-FTD
- Lewy body dementia (MONDO:0007488), ENIGMA-LBD
- Huntington disease (MONDO:0007739), ENIGMA-HD (>1,700)
- amyotrophic lateral sclerosis (MONDO:0004976), ENIGMA-ALS (~34,720 via UKB integration)
- multiple sclerosis (MONDO:0005301), ENIGMA-MS
- Neuropsychiatric disorders (MONDO:0002025), umbrella tag

(ENIGMA-Epilepsy spans MONDO:0005027 (epilepsy), outside the priority subset. Other ENIGMA WGs cover TBI, HIV, 22q11.2, stroke recovery, chronic pain, ataxia, also outside this subset.)

**Available data types and sample counts:** Federated; counts are aggregate across contributing sites pooled by WG.

- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n>50,000 (ENIGMA-GWAS subcortical, cortical, lifespan)
- Connectomics (brain imaging):
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n>30,000 across ENIGMA-DTI WGs
  - rs-fMRI: Resting Functional Magnetic Resonance Imaging (NCIT:C178024), n>10,000 (ENIGMA-rsfMRI)
  - task-fMRI: Task Functional Magnetic Resonance Imaging (NCIT:C178023), n>5,000 (ENIGMA-tbfMRI)
  - EEG: Electroencephalography (NCIT:C38054), n thousands (ENIGMA-EEG)
  - MEG: Magnetoencephalography (NCIT:C16811), n hundreds (ENIGMA-MEG)
  - PET: Positron Emission Tomography (NCIT:C17007), substantial subset via ENIGMA-AD/Aging amyloid plus tau PET, n thousands
  - Plus T1 structural across more than 100,000 individuals (subcortical and cortical ROI meta-analyses)
- Clinical: Electronic Medical Record (NCIT:C45259), n>100,000 (basic demographics, diagnosis, severity)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n>100,000 (HAM-D, MADRS, PANSS, CAPS, Y-BOCS, ADHD-RS, ADOS, etc., per WG)

**Per-WG summaries (selected, derived from prior NeuroSTORM curation and 2024-2026 publications):**

- **ENIGMA-AD/Aging:** Most multimodal of ENIGMA: T1 MRI, MEG, Tau-PET and Amyloid-PET, blood biomarkers, SNP arrays, WGS, EWAS DNA methylation. India ENIGMA Initiative explicitly targets diversity. 2026 work: prolonged grief disorder with comorbid depression accelerates brain aging.
- **ENIGMA-PD:** T1 MRI, DTI, rs-fMRI, SNP arrays. 2025 SuStaIn ML algorithm identifies 3 longitudinally robust atrophy subtypes.
- **ENIGMA-FTD:** T1 MRI, DTI, fMRI, dense genetic arrays. Tracks spatiotemporal spread of pathological proteins (tau, TDP-43).
- **ENIGMA-LBD:** T1 MRI, DTI-ALPS, PET, SPECT. 2025 preprint on glymphatic clearance impairment.
- **ENIGMA-HD:** Monogenic model with deterministic CAG repeat expansion. T1 MRI volumetry, biofluid markers (NfL).
- **ENIGMA-ALS:** WGS/WES for rare variants (SOD1, FUS, TARDBP, C9orf72), SNP arrays, T1 MRI, biofluids. 2026 leverages UK Biobank for high-genetic-risk vs clinical manifestation comparisons.
- **ENIGMA-MS:** T1/T2 MRI (lesion mapping), PET (PMI04 microglia tracer), RNA-seq for splicing variants, genotypes. 2025: PMI04 PET tracer visualizes microglia activity.
- **ENIGMA-MDD:** T1 MRI plus SNP genotyping. 2025/2026 mega-analysis (n=3711) maps childhood maltreatment x depression interaction.
- **ENIGMA-Anxiety:** T1 MRI, DTI, fMRI, SNP genotypes; subdivided by anxiety sub-disorder.
- **ENIGMA-PTSD:** T1 MRI, rs-fMRI, DTI, SNP arrays via PGC.
- **ENIGMA-Schizophrenia:** T1 MRI, DTI, sulcal morphometry, SNP arrays.
- **ENIGMA-Bipolar:** T1 MRI, DTI, SNP genotypes.
- **ENIGMA-OCD:** T1 MRI, DTI, rs-fMRI, task-fMRI, SNP-array genotypes.
- **ENIGMA-ADHD:** Largest coordinated neuroimaging+genetic study of ADHD; structural T1 MRI plus SNP genotyping.
- **ENIGMA-ASD:** Structural T1 MRI plus SNP-array genotypes; community-detection algorithms identify data-driven subcortical subtypes.
- **ENIGMA-TS:** T1 MRI, DTI, rs-fMRI, SNP arrays.
- **ENIGMA-Eating Disorders:** Multi-center T1 MRI plus SNP arrays. Cohen's d up to 0.95 for cortical thinning in acute AN.
- **ENIGMA-Addiction:** T1 morphometry, rs-fMRI, DTI, SNP arrays.
- **ENIGMA-Epilepsy:** T1 MRI, rs-fMRI, EEG, DTI white matter skeletons, SNP arrays.

**Foundation-model training adoption:**
- ENIGMA Brain Age (photon-ai.com/enigma_brainage), trained on 952 male and 1,236 female healthy controls across 19 cohorts using 77 FreeSurfer ROIs, is the canonical reference brain-age estimator; redistributed and fine-tuned in dozens of downstream papers.
- Brain Harmony / BrainHarmonix (2024-2025) and other multimodal brain foundation models pretrain on T1 and fMRI corpora that include ENIGMA-derived harmonized features.
- ENIGMA harmonized cortical and subcortical ROI tables underlie Rutherford et al.'s lifespan normative models and downstream PCNtoolkit-based deep ensembles.
- ENIGMA-PD, ENIGMA-Schizophrenia, and ENIGMA-MDD harmonized features have been used as held-out evaluation sets for general-purpose neuroimaging foundation models (MICCAI 2024).

**Notes for Cytognosis platform integration:** ENIGMA's federated architecture means Cytognosis cannot ingest raw subject-level data centrally; the pragmatic integration is to host the standardized pipelines, accept ENIGMA-style summary tables from partner sites, and treat published WG meta-analytic summary statistics as a high-value public auxiliary resource. The ENIGMA Brain Age and normative-modeling weights are directly usable as pretrained encoders.

### 12.3 PGC: Psychiatric Genomics Consortium

**Short description:** The PGC is the world's largest psychiatric genetics collaboration: more than 800 investigators across 40+ countries, organized into 14+ disorder working groups plus cross-disorder, methods, copy-number-variant, and ancestry initiatives. Investigators contribute genome-wide genotype data from their cohorts under the PGC's Data Access Committee model; the central analytic team performs harmonized QC, imputation, and meta-analytic GWAS. Released summary statistics, the consortium's flagship deliverable, are openly downloadable. PGC also coordinates rare-variant exome/whole-genome work, polygenic-score validation, and cross-disorder factorization.

**Latest/most significant reference publication:** Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2026 (advance publication 2025); doi:10.1038/s41586-025-09820-3. Working preprint: medRxiv 2025.01.14.25320574. Companion review: Sullivan PF, et al. The Psychiatric Genomics Consortium: discoveries and directions. Lancet Psychiatry. 2025; doi:10.1016/S2215-0366(25)00124-5.

**Access requirements:**
- *Obtain data:* Two tiers. (1) Released summary statistics (per-disorder and cross-disorder factor sumstats) are downloaded from https://pgc.unc.edu/for-researchers/download-results/ after signing a brief click-through DUA committing to non-identification, citation, and Fort Lauderdale-style respect for embargoes; this is free, no residency restriction, immediate. (2) Individual-level genotype data require a Secondary Analysis Proposal (SAP) reviewed by the disorder WG and the PGC DAC, plus the contributing cohort's local IRB; turnaround is months and access is typically via dbGaP, the LISA cluster (Netherlands), or institutional secure enclaves. There are no fees for academic access; commercial use requires advance written permission.
- *Use restrictions:* Scientific research only; no participant re-identification; no prenatal predictive testing; risk-prediction tools must disclose non-genetic etiology; commercial/for-profit use requires advance permission.
- *Storage requirements:* Summary statistics are downloadable; individual-level genotype data must remain on approved secure platforms (LISA, dbGaP-authorized environments, institutional HPC).
- *What can be shared back:* Summary statistics, polygenic score weights, fine-mapped credible sets, factor loadings, code, and trained models are encouraged for return to the community.

**Links:**
- Main website: https://pgc.unc.edu/
- Cross-Disorder WG: https://pgc.unc.edu/for-researchers/working-groups/cross-disorder-analyses-working-group/
- Download summary stats: https://pgc.unc.edu/for-researchers/download-results/
- GitHub: https://github.com/psychiatric-genomics-consortium

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Major Depressive Disorder (MONDO:0002009)
- Anxiety Disorder (MONDO:0005618)
- Post-traumatic Stress Disorder (MONDO:0005146)
- Obsessive-Compulsive Disorder (MONDO:0008114)
- Tourette Syndrome (MONDO:0007661)
- Anorexia Nervosa (MONDO:0005351), via Eating Disorders WG
- Attention Deficit-Hyperactivity Disorder (MONDO:0007743)
- Autism Spectrum Disorder (MONDO:0005258)
- Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689), via Substance Use Disorders WG
- Alzheimer disease (MONDO:0004975), via co-released summary statistics
- Neuropsychiatric disorders (MONDO:0002025), umbrella tag for cross-disorder factors and meta-analyses

(The Cross-Disorder 5-factor analysis additionally covers suicide attempt and borderline personality, outside this MONDO subset.)

**Available data types and sample counts:**
- Genotype:
  - SNP array: genotyping by SNP array assay (OBI:0001274), n>1,056,201 cases plus several million controls in the 14-disorder cross-disorder analysis (Grotzinger et al. 2026); per-disorder GWAS range from ~9,725 (Tourette) to >500,000 (MDD). 268 pleiotropic loci reported.
  - WES: exome sequencing assay (OBI:0002118), n in the tens of thousands (SCHEMA, BipEx, ASC, ADHD exome efforts contribute to PGC rare-variant pipelines)
  - WGS: whole genome sequencing assay (OBI:0002117), n increasing via partnerships (e.g., AMP-SCZ, NIMH Repository); overall n in the low thousands to tens of thousands depending on disorder
- Clinical: Electronic Medical Record (NCIT:C45259), n>1,000,000 (DSM/ICD diagnostic labels at minimum)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n disorder-specific subsets

**Foundation-model training adoption:**
- PRSformer: Disease Prediction from Million-Scale Individual Genotypes. bioRxiv 2025.10.26.684578. Transformer with neighborhood attention applied at GWAS/genome scale for multi-disease prediction; uses PGC-aligned variant panels.
- Genotype-Phenotype Transformer (bioRxiv 2024.10.23.619940): explicitly leverages PGC-style polygenic architectures.
- Zhao H, et al. Modeling gene interactions in polygenic prediction via geometric deep learning (PRS-Net). Genome Res. 2025.
- Deep learning-based polygenic scores enhance generalizability of psychiatric disorders prediction. medRxiv 2025.05.05.25326794.
- Genomic SEM and the 5-factor cross-disorder model from Grotzinger et al. 2026 itself constitutes a "polygenic foundation factorization" used by downstream multi-task prediction models.

**Notes for Cytognosis platform integration:** PGC summary statistics are a foundational, openly downloadable training signal for any psychiatric polygenic model; ingestion is straightforward and only requires the click-through DUA. Individual-level genotype access is gated, slow, and disorder-specific; Cytognosis should treat PGC sumstats as the always-on baseline and apply for SAP access only for specific generative or rare-variant workstreams.

### 12.4 PsychENCODE Consortium (PEC) Phase 2

**Short description:** PsychENCODE is the NIMH-funded consortium chartered to characterize the genomic, transcriptomic, epigenomic, and regulatory landscape of the human brain across neurotypical and neuropsychiatric conditions. Phase 2 (PEC2, 2018-2024) shifted from bulk to single-cell and spatial omics on more than 2,500 postmortem brain donors and culminated in a flagship release of 14 papers on 24 May 2024 (9 in Science, 3 in Science Advances, plus Scientific Reports and Molecular Psychiatry).

**Latest/most significant reference publication:** Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains. Science. 2024;384(6698):eadi5199. doi:10.1126/science.adi5199. PMID: 38781369. Companion: Ma S, et al. A data-driven single-cell and spatial transcriptomic map of the human prefrontal cortex. Science. 2024. Decadal review: PsychENCODE at 10. Neuron. 2025; doi:10.1016/j.neuron.2025.00924-9.

**Access requirements:**
- *Obtain data:* Tiered access. Tier 1 (controlled, individual-level genomics including snRNA/snATAC FASTQs, genotypes) requires an NDA Data Access Request (DAR) plus a separate Synapse account, an NIH eRA Commons-linked institutional signing-officer endorsement, and an approved Data Use Certification through the PsychENCODE DAC; turnaround is typically 2 to 6 weeks. Tier 2 (processed, anonymized matrices and BrainSCOPE outputs) is openly downloadable from synapse.org/psychencode and PsychSCREEN once a Synapse account agrees to the data terms. No fees.
- *Use restrictions:* Research use only; no re-identification; data must remain within the requesting institution's approved environment for Tier 1.
- *Storage requirements:* Tier 1 raw data are downloadable but must remain on institutionally-approved secure compute; Tier 2 processed data and PsychSCREEN browsers are open.
- *What can be shared back:* Models, single-cell embeddings, fine-mapped regulatory elements, and code are explicitly encouraged; PsychSCREEN is itself a derived-data sharing platform.

**Links:**
- Main website: https://www.psychencode.org/ (Phase II: https://www.psychencode.org/phase-ii)
- Knowledge portal: https://psychencode.synapse.org/ (synID syn4921369)
- NDA portal: https://nda.nih.gov/pec
- PsychSCREEN browser: https://psychscreen.wenglab.org/
- Resource portal (Phase I, still active): http://resource.psychencode.org/

**Included pathologies (MONDO mapping):**
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Autism Spectrum Disorder (MONDO:0005258)
- Major Depressive Disorder (MONDO:0002009)
- Post-traumatic Stress Disorder (MONDO:0005146)
- Alzheimer disease (MONDO:0004975)
- Neuropsychiatric disorders (MONDO:0002025), umbrella tag

**Available data types and sample counts (Phase 1 + Phase 2):**
- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 1,000+ across donors
  - SNP array: genotyping by SNP array assay (OBI:0001274), n=approximately 2,500 (paired with bulk and single-cell omics)
- Cellular omics:
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n=388 donors and more than 2.8M nuclei (brainSCOPE), with PFC focus; PEC2 total snRNA-seq donors approach approximately 500 across studies
  - snATAC-seq: single-nucleus ATAC-seq (OBI:0002762), n=approximately 616 brains with about 1,932 sorted-nucleus aliquots
  - scRNA-seq: single-cell RNA sequencing assay (OBI:0002631), n a few hundred (developmental brain studies)
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n>2,500 (PEC1 + PEC2 combined; CommonMind Consortium contribution included)
- Clinical: Electronic Medical Record (NCIT:C45259), n=approximately 2,500 (postmortem donor records)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=donor-level retrospective data only

**Foundation-model training adoption:**
- brainSCOPE (Emani et al. Science 2024) is itself the canonical PEC2 single-cell foundation resource and feeds dozens of cell-type and regulatory-element foundation-model efforts.
- scGPT, Geneformer, and UCE single-cell foundation models all use PEC2 snRNA-seq prefrontal cortex data as training/evaluation cohorts.
- BrainLM and the 2024-2025 multimodal brain foundation models include PEC2 transcriptomic features for cross-modal supervision.
- Network-based drug repurposing for psychiatric disorders using single-cell genomics. Cell Genomics. 2025. Built directly on PEC2 brainSCOPE.
- Ma S, et al. spatial transcriptomic foundation models, 2024 to 2025, use PEC2 PFC spatial atlases as anchors.

**Notes for Cytognosis platform integration:** PEC2 is the highest-resolution single-cell brain dataset for psychiatric disorders and is the obvious training corpus for cell-type-aware regulatory genomics foundation models; Tier 2 processed matrices are immediately ingestible from Synapse, while Tier 1 access via NDA should be requested early because of the multi-week DAR cycle. The PsychSCREEN UI is a useful reference for downstream Cytognosis browsers.

### 12.5 NBB: NIH NeuroBioBank

**Short description:** The NIH NeuroBioBank is a federated tissue-distribution network established by NIMH, NINDS, and NICHD in September 2013 to centralize requests for postmortem human brain tissue and related biospecimens from a network of repositories. Originally six brain banks, NBB grew to seven with the 2026 addition of the Iowa Neuropathology Resource Laboratory; the others are the University of Miami Brain Endowment Bank, the University of Maryland Brain and Tissue Bank, the Human Brain and Spinal Fluid Resource Center (Sepulveda VA), the Mt. Sinai Brain Bank, the Harvard Brain Tissue Resource Center at McLean, and the University of Pittsburgh Brain Tissue Donation Program. NBB distributes thousands of samples per year (about 10,500/year by recent estimates) covering 148 CNS diagnoses across 15 ICD-10 chapters.

**Latest/most significant reference publication:** Freund M, Taylor A, Ng C, et al. The NIH NeuroBioBank: creating opportunities for human brain research. Handb Clin Neurol. 2018;150:41-48. doi:10.1016/B978-0-444-63639-3.00004-9. PMID: 29496155. Recent: The NeuroBioBank Whole-Genome Catalog: Sequencing from human brain donors with neurologic, psychiatric, and developmental disorders. medRxiv 2024.08.29.24312734.

**Access requirements:**
- *Obtain data:* Researchers create an NBB account at neurobiobank.nih.gov, run the Request Wizard, browse the federated inventory, and submit a tissue request specifying donors, regions, and tissue volumes. Required documents: PI biosketch/CV, an executed Material Transfer Agreement co-signed by the PI and an institutional signing official, and confirmation of an active Federal Wide Assurance (FWA) with HHS OHRP. The federated brain banks then review allocation, NBB staff approve, and shipment is coordinated. No tissue acquisition fees; the requester pays shipping. No residency restriction in policy; international shipments are case-by-case. Annual progress reports required.
- *Use restrictions:* Research use only with IRB/IACUC oversight; no re-identification; publications must acknowledge the NIH NeuroBioBank and the specific contributing repository; secondary distribution is prohibited; commercial use requires written approval.
- *Storage requirements:* Tissue is physically shipped to the requester's institution; downstream omics data are stored by the requester. NBB itself does not host most omics datasets, but recent initiatives deposit genomic data to dbGaP and NDA.
- *What can be shared back:* NBB strongly encourages return of derived data (genotypes, RNA-seq, methylation, IHC, single-nucleus omics) to dbGaP/NDA/SRA; many AMP-AD, PsychENCODE, and PsychAD datasets in fact derive from NBB tissue and are deposited back.

**Links:**
- Main website: https://neurobiobank.nih.gov/
- About / network sites: https://neurobiobank.nih.gov/about/
- Researcher access: https://neurobiobank.nih.gov/researchers/
- Subjects/specimens search: https://neurobiobank.nih.gov/subjects/
- NDA NBB hub: https://nda.nih.gov/nbb

**Included pathologies (MONDO mapping):**
- Alzheimer disease (MONDO:0004975)
- Parkinson disease (MONDO:0005180)
- frontotemporal dementia (MONDO:0017276)
- Lewy body dementia (MONDO:0007488)
- Huntington disease (MONDO:0007739)
- amyotrophic lateral sclerosis (MONDO:0004976)
- multiple sclerosis (MONDO:0005301)
- Dementia (MONDO:0001627)
- Schizophrenia (MONDO:0005090)
- Bipolar Disorder (MONDO:0004985)
- Major Depressive Disorder (MONDO:0002009)
- Autism Spectrum Disorder (MONDO:0005258)
- Alcohol Dependence (MONDO:0007079), Opioid-use Disorder (MONDO:0005530), Nicotine Dependence (MONDO:0008575), Cannabis-use Disorder (MONDO:0005689)
- Post-traumatic Stress Disorder (MONDO:0005146)
- Obsessive-Compulsive Disorder (MONDO:0008114)
- Tourette Syndrome (MONDO:0007661)
- Brain disorders (MONDO:0005560), umbrella tag

**Available data types and sample counts:** NBB primarily distributes tissue, not data; the counts below reflect the federated inventory rather than pre-generated assay matrices.

- Genotype:
  - WGS: whole genome sequencing assay (OBI:0002117), n=approximately 2,000+ via the NeuroBioBank Whole-Genome Catalog (2024)
  - SNP array: genotyping by SNP array assay (OBI:0001274), n thousands via downstream PEC, AMP-AD, PsychAD usage
- Cellular omics:
  - Bulk RNA-seq: bulk RNA-seq assay (OBI:0003090), n thousands when summed across NBB-supplied tissue contributing to PsychENCODE, CommonMind, AMP-AD
  - snRNA-seq: single-nucleus RNA sequencing assay (OBI:0003109), n hundreds to low thousands of donors (e.g., PsychAD, brainSCOPE, AMP-AD ROSMAP supplements)
  - snATAC-seq: single-nucleus ATAC-seq (OBI:0002762), n hundreds via PsychENCODE2 contributions
- Clinical: Electronic Medical Record (NCIT:C45259), n>16,000 donors in NBB's federated catalog (clinical summary, neuropathology, demographics, cause of death, PMI)
- Instruments/questionnaires: Clinical or Research Assessment Question (NCIT:C91102), n=variable per repository (HBTRC and Mt. Sinai contribute extensive premortem cognitive/psychiatric questionnaires)

(Tissue itself - frozen and fixed brain regions, dura, CSF, blood, DNA aliquots - is the primary deliverable; about 10,500 specimen units distributed annually.)

**Foundation-model training adoption:** NBB's adoption is best understood as adoption-via-distribution: the tissue underpins many large training corpora rather than NBB itself releasing a model.
- PsychAD snRNA-seq atlas (Lee D, et al. 2024-2025) was generated largely from NBB-distributed tissue and is now used to fine-tune scGPT and Geneformer for psychiatric phenotyping.
- AMP-AD snRNA-seq atlases (SEA-AD, MIT-ROSMAP supplements) include NBB-derived donors and feed Alzheimer's foundation-model efforts.
- brainSCOPE (PEC2, Emani et al. Science 2024) sourced multiple cohorts from NBB repositories.
- The NeuroBioBank Whole-Genome Catalog (medRxiv 2024.08.29.24312734) provides a rare WGS resource across mixed neurologic/psychiatric/developmental diagnoses.
- BrainSeq Phase III and Mt. Sinai-led postmortem multi-omics atlases continue to draw from NBB tissue.

**Notes for Cytognosis platform integration:** NBB itself is not a primary download target; integrate it as the upstream provenance node for many of the omics datasets Cytognosis already ingests (PEC2, PsychAD, AMP-AD, CommonMind), and use the federated inventory search to source new tissue when generating bespoke assays. Submit any Cytognosis-generated derived data back to dbGaP/NDA tagged to the NBB donor IDs to maintain ecosystem-wide linkability.


---

## 13. NeuroSTORM Cohorts and Other Open Neuroimaging Datasets (preserved from prior curation)

These smaller open datasets came from the prior NeuroSTORM-anchored curation and are preserved here in the new schema. Most are accessed through OpenNeuro under CC0 or the NDA under standard DUC. They are critical evaluation cohorts for transdiagnostic neuroimaging foundation models.

### 13.1 HBN: Healthy Brain Network

**Short description:** The Healthy Brain Network is a Child Mind Institute initiative providing community-referred children and adolescents (ages 5.6 to 21.9 years) with a transdiagnostic sample including various neurodevelopmental and psychiatric conditions (ADHD, anxiety, autism spectrum, learning disorders). The current accessible cohort exceeds 770 individuals with QC-passed neuroimaging. HBN is designed to power dimensional psychiatry and transdiagnostic phenotype-imaging studies.

**Latest reference:** O'Connor D, et al. The healthy brain network serial scanning initiative: a resource for evaluating inter-individual differences and reliabilities across scan conditions and sessions. GigaScience 6, giw011 (2017). Updated cohort statistics in Taylor et al., Nature 2026 lifespan gradient atlas paper.

**Access:** Free public release via Healthy Brain Network portal; CC BY-NC. Tier 0/1.
- Main website: https://healthybrainnetwork.org/
- Data: https://fcp-indi.s3.amazonaws.com/data/Projects/HBN/

**Pathologies:** Attention Deficit-Hyperactivity Disorder (MONDO:0007743), Anxiety Disorder (MONDO:0005618), Autism Spectrum Disorder (MONDO:0005258), Major Depressive Disorder (MONDO:0002009), Obsessive-Compulsive Disorder (MONDO:0008114), Tourette Syndrome (MONDO:0007661), Neuropsychiatric disorders (MONDO:0002025).

**Available data:**
- Connectomics:
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n~770
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~770
  - EEG: Electroencephalography (NCIT:C38054), n~3,000+ (HBN-EEG release)
- Instruments: Clinical or Research Assessment Question (NCIT:C91102), n~770 (CBCL, KSADS, NIH Toolbox)

**FM adoption:** Used in Taylor 2026 (Nature) lifespan gradient atlas; HBN-EEG used in EEG foundation models (LaBraM, BENDR variants).

**Cytognosis notes:** Excellent transdiagnostic developmental psychiatry cohort; CC BY-NC license suitable for pretraining but commercial-derivative care needed.

### 13.2 TCP: Transdiagnostic Connectome Project

**Short description:** TCP comprises 241 individuals aged 18-70 (148 psychiatric patients plus 93 healthy comparison) from Yale University Brain Imaging Center and McLean Hospital. Includes high-resolution anatomical scans, multiple resting-state runs, and task-based fMRI runs, plus 50+ psychological and cognitive assessments. Designed to advance transdiagnostic brain-behavior relationship research in psychiatry.

**Latest reference:** Chopra, S. et al. The Transdiagnostic Connectome Project: an open dataset for studying brain-behaviour relationships in psychiatry. Sci. Data 12, 923 (2025).

**Access:** OpenNeuro ds005237; free CC0. Tier 0.
- Data: https://openneuro.org/datasets/ds005237/versions/1.1.3

**Pathologies:** Neuropsychiatric disorders (MONDO:0002025); 148 patients spanning MDD, anxiety, OCD, bipolar, schizophrenia, PTSD spectrum.

**Available data:**
- Connectomics:
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n=241
  - task-fMRI: Task Functional MRI (NCIT:C178023), n=241
- Instruments: Clinical or Research Assessment Question (NCIT:C91102), n=241 (50+ psychological and cognitive assessments)

**FM adoption:** Used in NeuroSTORM (Nature Biomedical Engineering 2026) for phenotype prediction across 10 clinical/cognitive scores (PCC 0.234-0.558).

**Cytognosis notes:** High-quality transdiagnostic cohort with rich clinical phenotyping; ideal for fine-tuning brain-behavior prediction heads on psychiatric foundation models.

### 13.3 NIMH-HV: NIMH Intramural Healthy Volunteer Dataset

**Short description:** Multimodal NIMH-curated dataset of healthy research volunteers with MEG, structural MRI, fMRI, DTI, comprehensive MEG battery, and rich behavioral phenotyping. Released in BIDS format on OpenNeuro. Rare resource because most open MEG datasets are small; multimodal MEG+MRI+behavioral datasets are even rarer. Useful as healthy baseline/normative reference.

**Latest reference:** Nugent, A. C. et al. The NIMH intramural healthy volunteer dataset: A comprehensive MEG, MRI, and behavioral resource. Sci. Data 9, 518 (2022).

**Access:** OpenNeuro ds005752; free CC0. Tier 0.
- Data: https://openneuro.org/datasets/ds005752/versions/2.1.0

**Pathologies:** N/A (healthy/baseline).

**Available data:**
- Connectomics:
  - MEG: Magnetoencephalography (NCIT:C16811), n~250+
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n~250+
  - DTI: Diffusion Tensor Imaging (NCIT:C64862), n~250+
- Instruments: Clinical or Research Assessment Question (NCIT:C91102), n~250+ (clinical assessments, blood/urine assays, mental health diagnostic + dimensional measures, cognitive/neuropsychological functioning)

**FM adoption:** Used as healthy baseline/normative reference for clinical and non-clinical secondary investigations including MEG foundation models.

**Cytognosis notes:** Critical normative MEG resource; small sample size means it is most valuable as a reference cohort rather than a pretraining substrate.

### 13.4 YaleNeuroConnect

**Short description:** Yale University fMRI dataset with 302 subjects scanned under resting-state plus 6 task conditions (selected to exercise diverse cognitive domains). Each subject has 48 minutes of fMRI data plus high-resolution 3D anatomical volumes. Extensive neuropsychological testing and symptom inventories collected outside MRI. Designed for brain parcellation under different cognitive states and RDoC-style transdiagnostic analyses.

**Latest reference:** Greene et al. 2025 (medRxiv preprint): A Transdiagnostic fMRI Dataset With 300+ Deeply Phenotyped Subjects Across Resting and Task States.

**Access:** OpenNeuro ds007286; free CC0. Tier 0.
- Data: https://openneuro.org/datasets/ds007286/versions/1.0.0
- Code: https://github.com/YaleMRRC/YaleNeuroConnect

**Pathologies:** Neuropsychiatric disorders (MONDO:0002025); transdiagnostic sample with sufficient symptom-score range to test RDoC framework principles.

**Available data:**
- Connectomics:
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n=302
  - task-fMRI: Task Functional MRI (NCIT:C178023), n=302 (6 task conditions)
- Instruments: Clinical or Research Assessment Question (NCIT:C91102), n=302 (extensive neuropsych and symptom inventories)

**FM adoption:** Used for testing brain-based test development and RDoC-style transdiagnostic models; long-duration task scans support stronger predictive models than rs-fMRI alone.

**Cytognosis notes:** Excellent open-license multi-state task fMRI dataset; pair with TCP for psychiatric fine-tuning.

### 13.5 QNLD: Quantitative Neuroimaging Laboratory Dataset

**Short description:** Multimodal dataset of 356 consented adults (97 young aged 20-40; 259 elderly aged 60-80); 259 with at least one scan, 189 completed all modalities. Structural MRI plus 2 resting-state and 12 task-based fMRI runs spanning 4 cognitive domains plus 3 PET tracers (FDG, Florbetaben, MK-6240) plus neuropsychological assessments. Aim: characterize negative BOLD response and preclinical neurodegeneration.

**Latest reference:** Mendes Marques et al. 2026 (Sci Data): A Multimodal Dataset to Investigate Task-Evoked Negative BOLD Response and Neurodegeneration.

**Access:** OpenNeuro ds006148; free CC0. Tier 0.
- Data: https://openneuro.org/datasets/ds006148/versions/1.0.6

**Pathologies:** N/A (healthy aging baseline; some preclinical AD pathology may be identified via PET).

**Available data:**
- Connectomics:
  - rs-fMRI: Resting Functional MRI (NCIT:C178024), n=259
  - task-fMRI: Task Functional MRI (NCIT:C178023), n=189 (12 runs across 4 cognitive domains)
  - PET: Positron Emission Tomography (NCIT:C17007), n=719 scans (232 Florbetaben, 251 FDG, 236 MK-6240)
- Instruments: Clinical or Research Assessment Question (NCIT:C91102), n~259 (neuropsych assessments, vital signs)

**FM adoption:** Supports preclinical AD foundation models combining MRI plus PET; small but uniquely multimodal dataset.

**Cytognosis notes:** Best as evaluation cohort for amyloid plus tau plus FDG PET-aware brain foundation models.

### 13.6 Other NeuroSTORM cohorts (preserved as smaller benchmark sets)

- **HCP-EP, ADHD-200, COBRE, UCLA Phenomics:** Now covered in Section 9.3 (INDI) and Section 9.2 (CCF). HCP-EP available via NDA Tier 2.
- **MND (Motor Neuron Disease appetite study):** OpenNeuro ds005874, n=59 (23 controls, 36 ALS); Chang et al., Sci. Data 12, 466 (2025). Tier 0. ALS (MONDO:0004976). rs-fMRI (NCIT:C178024) plus clinical instruments. Used in NeuroSTORM ALS diagnosis with 86.5% accuracy.
- **DMT-HAR-MED (DMT-Harmine Meditation):** OpenNeuro ds006644, n=40 healthy meditators with placebo vs. DMT-harmine arms. Meling et al. 2024. Tier 0. N/A pathologies. rs-fMRI. Used in NeuroSTORM medication-state classification.
- **AOMIC (Amsterdam Open MRI Collection):** OpenNeuro ds002785/ds002790; ~1,400 subjects across PIOP1, PIOP2, ID1000. Tier 0 CC0. Used widely in fMRI foundation models including NeuroSTORM and BrainLM.

---

## 14. Step-Wise Foundation-Model Implementation Roadmap

### 14.1 Year 1 (now through Q4 2026): Single-modality pretraining

**Genomic FM (12 months):** Apply for UKB access (Q1; expect Q2 approval); apply for All of Us workspace (Q1; expect Q1 approval); negotiate VA collaborator for MVP individual-level access OR start with MVP dbGaP summary statistics in parallel. Pretrain genotype transformer on UKB WGS in UKB-RAP enclave (Q2-Q3). Cross-validate on AoU in their Workbench. Export weights, publish under Apache 2.0. Expected scale: ~900,000 unique individuals across UKB plus AoU genotype.

**Single-cell brain FM (9 months):** Apply for AMP-AD/Synapse DUC (Q1; expect 2-week turnaround). Mirror ROSMAP-Compass plus PsychAD plus PEC2 brainSCOPE plus AMP-AD diverse-cohort snRNA-seq (~30M nuclei aggregate). Pretrain a Geneformer-style or scGPT-style foundation model in Cytognosis enclave. Validate on held-out AMP-PDRD multi-region atlas plus AMP-ALS post-mortem cortex. Export weights and embeddings under Apache 2.0; deposit derivatives back to Synapse per AMP-AD policy.

**Connectomic FM (9 months):** Apply for ABCD via NBDC Data Hub (Q1; expect Q1-Q2 approval); register for HCP and OpenNeuro (immediate). Pretrain a 4D-fMRI plus DTI dual-modality FM on UKB (~60,000) plus ABCD (~11,500) plus HCP family (~5,500) plus OpenNeuro public (~25,000) plus INDI (~10,000). Use BIDS-Derivatives output schema and harmonize via ComBat; release preprocessed feature tensors for downstream users. NeuroSTORM-, BrainLM-, BrainGFM-, and Brain-JEPA-derived initializations are appropriate baselines to beat.

**EHR FM (12 months):** Negotiate MGB (PDSR Curated, Tier 5 internal route) and Mayo (Accelerate or Discover subscription) and Mt Sinai (BioMe + MSDW) access via institutional partnerships in Q1-Q2. Pretrain in each enclave separately; export weights only. Federated calibration across the three sites in Q3-Q4. Compare to AoU-pretrained EHR FM as baseline. Use NEP-8B / Building the EHR Foundation Model architecture as starting point.

**Phenotype FM (6 months):** Pretrain on UKB instruments (MHQ, cognitive testing, lifestyle) plus AoU surveys plus HPP deep panels. Most data are downloadable in summary form; full instruments require enclave compute on UKB-RAP and AoU Workbench. Use COMPRER-style contrastive pretraining as baseline.

### 14.2 Year 2 (Q1 through Q4 2027): Pairwise multimodal pretraining

**Genomic + Connectomic on UKB (~60,000 imaging plus WGS):** Cross-modal contrastive learning inside UKB-RAP. The single largest paired genotype-imaging dataset in the world. Augment with ENIGMA federated meta-analytic summary stats for cross-disorder priors.

**Genomic + EHR on UKB + AoU + MGBB + BioMe + MVP (~1,000,000 paired):** Multi-enclave federated training with weight averaging. Includes cross-ancestry calibration; AoU UBR cohort and BioMe Latinx/African subset are critical diversity anchors.

**Genomic + Single-cell on ROSMAP + PsychAD + PEC2 (~3,000 donors paired):** Cell-population polygenic embedding via per-cell-type GWAS plus single-cell foundation embeddings. snTWAS-style methods (Shin et al. medRxiv 2024) provide proven baselines.

**Connectomic + Phenotype on ABCD + HCP + HBN + YaleNeuroConnect + TCP (~13,000 paired):** Brain-behavior contrastive learning, transdiagnostic. Use TCP and YaleNeuroConnect as held-out test sets after pretraining on ABCD plus HCP plus HBN.

**Single-cell + EHR on ROSMAP, PsychAD MSSM, AMP-PDRD (~3,500 donors):** Cell-state to clinical-trajectory bridges for Alzheimer's, Parkinson's, schizophrenia, bipolar disorder.

### 14.3 Year 3 (2028+): Triple-modality pretraining

**Genomic + Connectomic + EHR + Phenotype on UKB (~60,000 with all four):** UKB-anchored Cytoverse foundation model; the only population-scale substrate. Transfer to MGB, Mayo, Mt Sinai, ABCD, HCP, AoU as evaluation cohorts.

**Genomic + Single-cell + EHR on ROSMAP + PsychAD MSSM + AMP-AD diverse cohorts:** Adds clinical-trajectory supervision to single-cell-genotype models. Power is small (~3,000 donors) but signal is dense.

**Connectomic + Phenotype + Single-cell (postmortem)** is a research frontier without a single substrate; use Cytognosis-generated cohorts and ENIGMA imaging cross-references with NBB-supplied tissue downstream.

### 14.4 Governance and FAIR principles applied

For every dataset above we will:
1. Track the access tier (Section 3) and route Cytognosis training through the corresponding compute stack (cloud enclave for Tier 3+, institutional HPC for Tier 2, central Cytognosis cluster for Tier 0/1).
2. Ship a model card with the data card listing every contributing dataset, application reference, contributing-cohort acknowledgements, and aggregation thresholds applied.
3. Release model weights under Apache 2.0 where the upstream tier permits (essentially all cases except commercial-restricted Mayo/MVP outputs).
4. Deposit derived FAIR-tagged data products (embeddings, harmonized features, summary statistics) back to source repositories (Synapse for AMP-AD/PsychENCODE/AMP-ALS; dbGaP/NDA where appropriate; Cytognosis open mirror for processed open-license data).

---

## 15. References and Source Provenance

- UK Biobank: Bycroft et al. Nature 2018; Li et al. Nature 2025; UKB-RAP and Showcase portals
- All of Us: Bick et al. Nature 2024; Mayo et al. AJHG 2025; Researcher Workbench documentation
- MVP: Verma et al. Science 2024; Stein et al. Nat Genet 2021; MVP-CHAMPION JAMIA Open 2024
- HPP: Reicher et al. Nature Medicine 2025; Lutsker et al. Nature 2025 (GluFormer)
- MGBB / RPDR / PDSR Curated: Lemieux Perreault et al. Nat Commun 2025; Castro et al. JAMIA 2022; MGB RISC documentation
- Mayo MCP / Accelerate: Heydari et al. npj Health Systems 2026; Atlas pathology FM partnership
- BioMe / MSDW: Belbin et al. Cell 2021; Sun et al. Nature 2024 (Regeneron exomes); Miotto et al. Sci Rep 2016 (Deep Patient)
- ABCD: Volkow et al. Dev Cogn Neurosci 2018; Karcher and Barch Neuropsychopharmacology 2021; NBDC Data Hub 2025 transition
- CCF / HCP family: Van Essen et al. NeuroImage 2013; Bookheimer et al. NeuroImage 2019; Somerville et al. NeuroImage 2018
- INDI: Mennes et al. NeuroImage 2013; ABIDE I/II Sci Data 2017; CCNP / CoRR / Rockland documentation
- OpenNeuro: Markiewicz et al. eLife 2021
- AMP-AD: Greenwood et al. Curr Protoc Hum Genet 2020; AD Knowledge Portal documentation; Mathys et al. Nature 2024
- ROSMAP: Bennett et al. JAD 2018; Mathys et al. Cell 2023; ROSMAP-Compass 2025 preprint
- AMP-PDRD: Iwaki et al. Mov Disord 2021; Kamath et al. Sci Data 2024; AMP-PDRD launch documentation
- ADNI: Weiner et al. Alz Dement 2025; Petersen et al. Neurology 2010
- PPMI: Marek et al. Ann Clin Transl Neurol 2018; Marek et al. Mov Disord 2022
- AMP-ALS: Baxi et al. Nat Neurosci 2022; Tam et al. Cell Reports 2019; FNIH announcement May 2024
- PsychAD: Lee et al. Sci Data 2025; Bendl et al. medRxiv 2024 (PASCode)
- ABIDE I/II: Di Martino et al. Mol Psychiatry 2014, Sci Data 2017
- B-SNIP 1/2 + PARDIP: Tamminga et al. Transl Psychiatry 2025; Clementz et al. AJP 2016, Schizophr Bull 2022; Lencer et al. Bipolar Disord 2020
- FACE/BIOFACE/PSY-COH: Godin et al. J Affect Disord 2022; Schurhoff et al. Encephale 2019; Fondation FondaMental open-access charter
- ENIGMA: Thompson et al. Transl Psychiatry 2020; per-WG flagship references in Section 12.2
- PGC: Grotzinger et al. Nature 2026; Sullivan et al. Lancet Psychiatry 2025
- PsychENCODE: Emani et al. Science 2024 (brainSCOPE); PsychENCODE Phase 2 collection
- NBB: Freund et al. Handb Clin Neurol 2018; NBB Whole-Genome Catalog medRxiv 2024

NeuroSTORM-derived smaller cohorts (HBN, TCP, NIMH-HV, YaleNeuroConnect, QNLD, MND, DMT-HAR-MED, AOMIC) are documented per their OpenNeuro entries and source publications cited in Section 13.

The companion `cytognosis_master_dataset_curation.xlsx` mirrors all of Section 7 through 13 in a structured form for filtering and provides three derived sheets: modality coverage matrix, MONDO disorder coverage matrix, and paired-modality availability cross-tab.

---

*End of master document.*
