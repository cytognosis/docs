# Neuroverse — Action Plan
**Owner**: Shahin Mohammadi | **Last updated**: 2026-05-22

This document tracks the sequential steps required to move from the current state
(strategy documented, infrastructure provisioned, no data yet) to the first
Neuroverse training run.

---

## Current Blockers (Critical Path)

```
FWA from OHRP
    → SMART IRB Joinder
        → IRB Protocol approval (North Star, relying on Cytognosis IORG)
            → First NDA DUC submission (NBB)
                → Data ingestion
                    → Foundation model training
```

**Time estimate**: 4–8 months from FWA issuance to first model training.

---

## Phase 1: Regulatory Foundations

| Step | Task | Owner | Status | Dependencies |
|---|---|---|---|---|
| 1.1 | Obtain FWA (Federal Wide Assurance) from OHRP | Shahin | ⏳ In progress | None |
| 1.2 | File SMART IRB Joinder (Cytognosis as Relying Institution) | Shahin | ⏳ Pending 1.1 | FWA issued |
| 1.3 | Execute North Star IRB Protocol (multi-site reliance for Neuroverse) | Shahin + Brad + Ananth | ⏳ Pending 1.2 | SMART IRB Joinder |
| 1.4 | Finalize inter-institutional MOUs (Cytognosis–Purdue, Cytognosis–McLean) | Duane (legal) | ⏳ Drafted | Legal review needed |
| 1.5 | Complete NIST SP 800-171 self-assessment (required for first NDA DUC) | Shahin + Engineering | ⏳ Not started | GCP architecture stable |
| 1.6 | Document Cytognosis SAE as institutional computing environment | Shahin | ✅ Done | — |

---

## Phase 2: Training and Registration

| Step | Task | Owner | Status | Dependencies |
|---|---|---|---|---|
| 2.1 | Complete required CITI training (all Cytognosis Approved Users) | All personnel | ⏳ Pending | Personnel designated |
| 2.2 | Sign NIH Genomic Data User Code of Conduct (all Approved Users) | All personnel | ⏳ Pending | Personnel designated |
| 2.3 | Register on NDA (one-time institutional registration) | Shahin | ⏳ Pending | FWA |
| 2.4 | Register on Synapse (for ROSMAP) | Shahin | ⏳ Pending | None |
| 2.5 | Register on ConnectomeDB (for HCP) | Ananth | ⏳ Pending | None |

---

## Phase 3: DUC Submissions (Batch 1)

| Step | Dataset | Repository | Lead | Status | Dependencies |
|---|---|---|---|---|---|
| 3.1 | HCP Open Access (practice run) | ConnectomeDB | Ananth | ⏳ Pending 2.5 | Registration |
| 3.2 | NBB WGS | NDA | Shahin + Brad | ⏳ Pending 1.3, 1.5, 2.1-2.3 | IRB, NIST 800-171, training |
| 3.3 | PsychENCODE | NDA | Shahin + Brad | ⏳ Pending 3.2 approved | Post-NBB |
| 3.4 | PsychAD | NDA | Shahin | ⏳ Pending 3.2 approved | Post-NBB |
| 3.5 | ROSMAP | Synapse | Shahin | ⏳ Pending 2.4, 1.3 | IRB, training |

---

## Phase 4: Data Ingestion and Environment

| Step | Task | Owner | Status | Dependencies |
|---|---|---|---|---|
| 4.1 | Activate CMEK on phi-prod buckets | Engineering | ⏳ Trigger: first DUC approved | DUC approval |
| 4.2 | Enable object versioning on PHI buckets | Engineering | ⏳ Trigger: first data upload | 4.1 |
| 4.3 | Provision DUC-specific IAM groups | Engineering | ⏳ Trigger: DUC approved | 4.1 |
| 4.4 | Define preprocessing pipelines (fMRIPrep, PLINK2, STARsolo) | Engineering | ⏳ In parallel | Architecture docs |
| 4.5 | First NBB data transfer to Cytognosis SAE | Shahin + Brad | ⏳ Pending 3.2, 4.3 | DUC + IAM |
| 4.6 | VPC Service Controls perimeter activation | Engineering | ⏳ Trigger: first external PHI | PHI ingest |

---

## Phase 5: Neuroverse Model Training

| Step | Task | Owner | Status | Dependencies |
|---|---|---|---|---|
| 5.1 | Define model architecture (multi-modal foundation model spec) | Shahin + Ananth | ⏳ In progress | Scientific strategy |
| 5.2 | Implement training pipeline (Vertex AI + Purdue HPC) | Engineering + Ananth lab | ⏳ Pending 4.5 | Data available |
| 5.3 | Level 1 validation (transdiagnostic, molecular anchor only) | Shahin | ⏳ Pending 5.2 | Model trained |
| 5.4 | Level 2 validation (biotype recovery, requires connectomics) | Shahin + Ananth | ⏳ Pending 5.3 + Batch 2 data | Batch 2 DUCs |
| 5.5 | Level 3 validation (treatment dynamics, requires longitudinal) | Shahin + Ananth | ⏳ Pending 5.4 + ABCD | ABCD DUC |
| 5.6 | Member-inference evaluation (required before model release) | Shahin | ⏳ Post-training | Trained model |
| 5.7 | Open model release (weights + training code) | Shahin | ⏳ Post-5.6 | NIH approval + member-inference passing |

---

## Personnel Onboarding Flow

When adding a new Approved User to any Neuroverse cohort:

1. **PI confirms scope**: which datasets, which environments.
2. **IRB amendment**: add person to North Star protocol at their home institution.
3. **DUC amendment**: file with relevant DAC naming the new person.
4. **Training**: complete CITI + NIH Code of Conduct + Cytognosis HIPAA training.
5. **Provisioning**: add to DUC-specific IAM group(s); provision environment credentials.
6. **Tracking**: update master dataset tracker (Google Sheets + this repo).

**Target**: onboarding complete within 2 weeks of PI request, gated by DUC amendment
cycle times (typically 1–2 weeks at NDA).

---

## Roadmap

| Phase | Target Window | Key Outcomes |
|---|---|---|
| Regulatory | Months 1–3 | FWA issued, SMART IRB filed, MOUs executed, NIST 800-171 assessed |
| First DUC | Months 4–6 | NBB DUC submitted and approved; ROSMAP DUC submitted |
| Data ingestion | Months 6–10 | First molecular data in Cytognosis SAE; preprocessing pipelines running |
| Batch 2 DUCs | Months 8–14 | HCP, ABCD, B-SNIP DUCs; Purdue connectomics environment active |
| Training | Months 14–24 | Foundation model trained; Level 1+2 validation complete |
| Open release | Months 24+ | Member-inference eval passing; weights published |

---

## Key Contacts for DUC Navigation

| Dataset | Data Access Committee | Contact |
|---|---|---|
| NDA datasets (NBB, PEC, PsychAD, ABCD, B-SNIP) | NIMH DAC | https://nda.nih.gov |
| ROSMAP | AD Knowledge Portal DCC | Sage Bionetworks; portal@sagebionetworks.org |
| HCP | ConnectomeDB | https://db.humanconnectome.org |
| UK Biobank | UKB Access Management | https://www.ukbiobank.ac.uk |
