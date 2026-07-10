# Neuroverse — Datasets, Cohorts & Modalities

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)
**Maintained by**: Shahin Mohammadi | **Last updated**: 2026-05-22
**Live tracker**: Google Sheets (Cytognosis Shared Drive → `02-Scientific-Platform`)

> [!NOTE]
> This document is the canonical reference for all Neuroverse data sources.
> Update both this file and the Google Sheets tracker when DUC status changes.

---

## Data Classification Tiers

All Neuroverse data is classified before handling. Tier determines storage bucket,
access controls, and processing environment.

| Tier | Label | Description | Storage |
|---|---|---|---|
| **L0** | Public Open | No consent restrictions; unrestricted download | `gs://cytognosis-public-data/` |
| **L1** | Registered Open | Requires account but no data use agreement | `gs://cytognosis-open-data/` |
| **L2** | Controlled | DUC/DAA required; no PHI | `gs://cytognosis-phi-prod-data/` (in phi-prod) |
| **L3** | Controlled + PHI | DUC + HIPAA BAA required; direct identifiers possible | `gs://cytognosis-phi-core/` (in phi-prod) |

---

## Batch 1: Foundation Cohorts (Initial DUC Submission Scope)

These are the priority cohorts for the Neuroverse foundation model's molecular and
clinical anchor. All require DUC submission as Cytognosis SAE as the computing environment.

| Cohort | Modalities | Sample Size | Disease Focus | Access Route | Data Tier | DUC Status | Cytognosis Lead | Site PI |
|---|---|---|---|---|---|---|---|---|
| **NeuroBioBank (NBB)** | WGS | ~10,000 | Multi-disorder postmortem | NDA DUC (NBB Permission Group) | L2 | ⏳ Pending | Shahin | Brad (HBTRC) |
| **PsychENCODE (PEC)** | scRNA-seq, snRNA-seq, bulk RNA-seq, ATAC-seq, Hi-C, WGS | ~3,000 brains | SCZ, BD, ASD, MDD, controls | NDA DUC (PEC Permission Group) | L2 | ⏳ Pending | Shahin / Brad | Brad |
| **PsychAD** | snRNA-seq, bulk RNA-seq | ~1,500 samples | AD and related dementias | NDA DUC | L2 | ⏳ Pending | Shahin | Brad |
| **ROSMAP** | Multi-omics + clinical + neuropath | ~3,500 participants | AD, MCI, cognitive aging | Synapse DUC (AD Knowledge Portal) | L2/L3 | ⏳ Pending | Shahin | (Jose — secondary) |

### Data Access Repositories for Batch 1

| Repository | URL | Relevant Cohorts | Notes |
|---|---|---|---|
| NIMH Data Archive (NDA) | https://nda.nih.gov | NBB, PEC, PsychAD, ABCD, B-SNIP | Main repository for NIH-funded psychiatric data |
| Synapse / AD Knowledge Portal | https://adknowledgeportal.synapse.org | ROSMAP | Managed by Sage Bionetworks; DUC via Synapse |

---

## Batch 2: Connectomics Anchors + Population Cohorts

Parallel DUC applications. Ananth Grama leads the connectomics-track cohorts.

| Cohort | Modalities | Sample Size | Disease Focus | Access Route | Data Tier | DUC Status | Cytognosis Lead | Site PI |
|---|---|---|---|---|---|---|---|---|
| **HCP Young Adult** | rs-fMRI, task fMRI, dMRI, sMRI, behavioral, genotypes | 1,206 | Healthy young adults | ConnectomeDB DUC | L1/L2 | ⏳ Pending | Ananth | Ananth |
| **ABCD Study** | Longitudinal multi-modal MRI, behavior, cognition, genomic arrays | ~11,900 youth | Pediatric brain development | NDA DUC (ABCD Permission Group) | L2 | ⏳ Pending | Ananth | Ananth |
| **UK Biobank (Brain MRI + WGS)** | WGS/WES/array, brain MRI (~100k), EHR linkages, labs, lifestyle | ~500,000 (~100k MRI) | Multi-disease, ICD-coded | UKB AMS application | L2 | ⏳ Pending | Shahin | Ananth (imaging) |
| **B-SNIP** | Multi-modal neuroimaging, neurophysiology, clinical, biospecimens | ~2,400 | Psychosis biotypes (SCZ, BD, schizoaffective) | NDA DUC | L2 | ⏳ Pending | Shahin | Brad |

### Data Access Repositories for Batch 2

| Repository | URL | Relevant Cohorts | Notes |
|---|---|---|---|
| ConnectomeDB | https://db.humanconnectome.org | HCP-YA | Open and Restricted tiers; free account |
| UK Biobank AMS | https://www.ukbiobank.ac.uk/enable-your-research | UK Biobank | Full institutional application; takes ~3-6 months |

---

## Batch 3: Clinical EHR + Biobank (Future)

These require additional regulatory infrastructure (IRB reliance from MGB/Mayo/Mt Sinai)
and are planned for 12+ months from now.

| Cohort | Modalities | Scale | Notes | Status |
|---|---|---|---|---|
| **All of Us** | EHR, genomics, surveys, wearables | ~800,000 | Researcher Workbench 2.0; data stays inside RW | ⏳ Future |
| **Million Veteran Program (MVP)** | WGS, EHR, surveys | ~700,000 | VA-managed; requires institutional VA partnership | ⏳ Future |
| **MGB Biobank** | EHR, WGS, biospecimens | ~120,000 | Direct relationship via Brad; HIPAA L3 | ⏳ Future |
| **Mayo Clinic Biobank** | EHR, multi-omics | ~80,000 | IRB + DUA with Mayo | ⏳ Future |
| **FondaMental FACE** | Multi-modal clinical (ASD, BD, TRD, SCZ) + biospecimens | ~12,000 | French cohort; GDPR applies | ⏳ Future |

---

## Modality Coverage Matrix

| Modality | Batch 1 | Batch 2 | Batch 3 | Primary Standard |
|---|---|---|---|---|
| Whole Genome Sequencing (WGS) | NBB, PEC | HCP-YA, UK Biobank | MVP, MGB | GA4GH VRS, VCF/BCF, CRAM |
| Single-cell RNA-seq (scRNA-seq) | PEC, PsychAD | — | — | CELLxGENE schema, AnnData |
| snRNA-seq | PEC, PsychAD, ROSMAP | — | — | CELLxGENE schema, AnnData |
| Bulk RNA-seq | PEC, PsychAD, ROSMAP | — | — | ENCODE pipeline, FASTQ/BAM |
| ATAC-seq | PEC | — | — | ENCODE pipeline |
| Hi-C | PEC | — | — | Juicer, .hic format |
| rs-fMRI | — | HCP-YA, ABCD, UK Biobank | All of Us | BIDS, NWB, fMRIPrep |
| task fMRI | — | HCP-YA, ABCD | — | BIDS, NWB |
| dMRI (diffusion) | — | HCP-YA | UK Biobank | BIDS, TRK/TCK |
| sMRI (structural) | — | HCP-YA, ABCD, UK Biobank | All of Us | BIDS, NIfTI |
| Neuropathology | ROSMAP | — | MGB | Custom schemas |
| Clinical / EHR | ROSMAP | UK Biobank | All of Us, MGB, Mayo | FHIR R4, OMOP |
| Neurophysiology | — | B-SNIP | — | BIDS-EEG, NWB |
| Behavioral / cognitive | — | HCP-YA, ABCD, B-SNIP | All of Us | NDA data dictionary |

---

## Data Volumes (Estimated)

| Source | Raw size | Processed size | Storage tier |
|---|---|---|---|
| NBB WGS (~10k samples × ~30 GB CRAM) | ~300 TB | ~30 TB (VCF) | phi-prod cold |
| PEC scRNA/snRNA/ATAC | ~50 TB | ~5 TB (AnnData) | phi-prod standard |
| PsychAD snRNA-seq | ~20 TB | ~2 TB (AnnData) | phi-prod standard |
| ROSMAP multi-omics | ~30 TB | ~5 TB | phi-prod standard |
| HCP-YA MRI | ~50 TB | ~10 TB (processed) | phi-prod standard |
| ABCD MRI (longitudinal) | ~100 TB | ~20 TB | phi-prod standard |
| UK Biobank imaging (~100k) | ~500 TB | ~80 TB (subset) | phi-prod cold |
| B-SNIP | ~5 TB | ~1 TB | phi-prod standard |
| **Total (all batches 1+2 active)** | **~1 PB** | **~150 TB** | see above |

> Current `cytognosis-phi-prod` is provisioned but empty. Storage costs activate at
> first data ingest. Budget planning should target ~$1,500-3,000/month at steady-state
> for batch 1+2 processed data.

---

## Public Cohorts (No DUC Required)

These can be ingested immediately into `gs://cytognosis-open-data/`.

| Dataset | Modalities | Scale | Access | Notes |
|---|---|---|---|---|
| OpenNeuro | fMRI, MRI (hundreds of studies) | ~10,000 studies | Public, BIDS | https://openneuro.org |
| DANDI Archive | Ephys, imaging (NWB format) | Growing | Public, CC0 | https://dandiarchive.org |
| HCP Open Access | rs-fMRI, sMRI | 1,206 (subset) | Free account | https://db.humanconnectome.org |
| Allen Brain Atlas | Gene expression, cell types, connectivity | — | Public API | https://portal.brain-map.org |
| Allen Cell Types Database | Electrophysiology + morphology + transcriptomics | ~5,000 cells | Public | https://celltypes.brain-map.org |
| GTEx v10 | Bulk RNA-seq (49 tissues) | ~1,000 donors | Public (v10 open) | https://gtexportal.org |
| BrainSpan | Developmental transcriptomics | 16 stages × 16 regions | Public | https://brainspan.org |
| PsychENCODE open-access | Summary statistics, processed counts | — | Public subset | https://psychencode.org |
| ENCODE Portal | Functional genomics (brain cell types) | Thousands of experiments | Public | https://www.encodeproject.org |

---

## DUC Submission Sequence

The order of DUC submissions is determined by: (1) which cohorts are most critical for
Level 1 validation, and (2) which data access routes are simplest to navigate first.

**Recommended sequence:**
1. **NDA registration** — one-time; needed for all NDA cohorts (NBB, PEC, PsychAD, ABCD, B-SNIP)
2. **HCP Open Access** — free registration; de-risks technical setup before controlled data
3. **NBB WGS** (NDA DUC) — molecular anchor for Level 1; Brad has existing NBB relationships
4. **PsychENCODE** (NDA DUC) — largest multi-modal source; most complex
5. **PsychAD** (NDA DUC) — AD-focused single-cell; straightforward
6. **ROSMAP** (Synapse DUC) — AD multi-omics; separate repository system
7. **B-SNIP** (NDA DUC) — psychosis biotypes; needed for Level 2
8. **ABCD** (NDA DUC) — pediatric longitudinal; needed for Level 3
9. **UK Biobank** (AMS) — large-scale; 3-6 month process; start application early

**Prerequisites before first NDA DUC:**
- FWA issued by OHRP
- SMART IRB joinder filed
- IRB protocol approved (initial or reliance)
- Cytognosis SAE formally established as institutional computing environment
- NIST 800-171 self-assessment completed
