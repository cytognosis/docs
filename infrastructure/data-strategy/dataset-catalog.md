# Cytognosis Dataset Catalog & Stratification

This document serves as the comprehensive registry of datasets managed, accessed, or integrated by the Cytognosis Foundation. It details the stratification of highly restricted neuro-related datasets, their corresponding access restrictions, and the underlying infrastructure requirements necessary to ensure full regulatory and security compliance (HIPAA, NIH NDA, etc.).

> [!NOTE]
> **Neuroverse cohort detail**: For the full dataset-by-dataset breakdown of the Neuroverse program
> (batches 1-3, modality coverage matrix, data volumes, DUC submission sequence), see
> [programs/neuroverse/datasets-cohorts.md](../programs/neuroverse/datasets-cohorts.md).
> The compliance requirements for these cohorts are tracked in
> [HIPAA-STATUS.md](compliance/HIPAA-STATUS.md) and [nih-gds-requirements.md](compliance/nih-gds-requirements.md).

## 1. Dataset Stratification

Datasets are stratified by their modality and origin. This catalog focuses heavily on neurological and psychiatric datasets that form the core of Cytognosis's precision health and interception models.

### 1.1 Genotype Data

Raw and processed DNA sequence information used to identify genetic risk architectures.

- **Whole-Genome Sequencing (WGS)**: Deep sequencing variants (e.g., from PsychENCODE and NeuroBioBank (NBB)).
- **Whole-Exome Sequencing (WES)**: Protein-coding region variants.
- **Single Nucleotide Polymorphism (SNP) Arrays**: Common variant genotyping used extensively in GWAS cohorts.

### 1.2 Genomic & Functional Data

Data reflecting gene expression and regulation, crucial for causal AI and cellular intelligence.

- **Transcriptomic (RNA-seq)**: Bulk and single-cell/single-nucleus RNA sequencing (scRNA-seq/snRNA-seq) capturing dynamic gene expression states. Sourced heavily from **PsychENCODE**, **ROSMAP**, and **PsychAD**.
- **Epigenomic**: ATAC-seq, ChIP-seq, and DNA methylation profiling measuring chromatin accessibility and regulatory elements.

### 1.3 Neuroimaging Data

In-vivo structural and functional mapping of the central nervous system.

- **fMRI (Functional MRI)**: Resting-state and task-based functional connectivity.
- **Structural MRI & DTI**: High-resolution anatomical mapping and white matter tractography.
- **PET (Positron Emission Tomography)**: Metabolic and molecular imaging, critical for neurodegenerative cohorts (e.g., **AMP-AD**).
- **Electrophysiology (EEG/MEG)**: High-temporal resolution brain activity mapping, key components of the **B-SNIP 1 & 2** (Bipolar-Schizophrenia Network on Intermediate Phenotypes) datasets.

### 1.4 EHR & Clinical Data

Deep longitudinal health phenotypes.

- **Structured EHR**: ICD-10/11 diagnoses, CPT procedure codes, lab results, and biometrics.
- **Clinical Assessment Scales**: Gold-standard psychiatric and neurological symptom severity scores (e.g., PANSS, MADRS, MoCA).
- **Classification Levels**: EHR data requires strict de-identification (Safe Harbor or Expert Determination) before entering analytical enclaves, unless explicit patient consent is digitally managed via Cytognosis primary collection tools (e.g., forms/cal.com).

### 1.5 Wearables & Continuous Biosensing

High-frequency longitudinal physiological data mapping temporal dynamics.

- **Actigraphy & Sleep Logging**: Derived from standard datasets or platforms like OURA.
- **Cardiovascular Dynamics**: Heart Rate Variability (HRV) and continuous HR from Apple Watch.
- **Metabolic Tracking**: Continuous Glucose Monitoring (CGM) streams integrated for systemic metabolic health tracking.

---

## 2. Access Restrictions & Data Use Limitations

Because these datasets often contain sensitive, re-identifiable human subject data (PHI/PII or dbGaP/NDA tier data), strict access tiers are enforced.

### 2.1 Access Tiers

| Tier | Description | Example Datasets | Access Requirements |
| --- | --- | --- | --- |
| **Tier 1: Open Access** | Summary statistics, fully aggregated data, open-source cohorts. | 1000 Genomes, GWAS summary stats | Publicly available. |
| **Tier 2: Registered Access** | De-identified clinical or wearable data. | Processed OURA aggregates, mock datasets | Requires user registration and click-through Data Use Agreement (DUA). |
| **Tier 3: Controlled Access** | Individual-level genotype, genomic, and rich phenotypic data. | PsychENCODE, ROSMAP, NBB, B-SNIP | Requires formal Data Access Request (DAR), Institutional Review Board (IRB) approval, Federalwide Assurance (FWA), and signed Data Use Certification (DUC). |
| **Tier 4: Highly Restricted** | Identified PHI, raw internal longitudinal data with direct identifiers. | Internal Cytognosis cohort raw data | Restricted to core staff with documented HIPAA training and formal business need. Governed by Business Associate Agreements (BAAs). |

### 2.2 Sharing Limitations (Team vs. Collaborators)

- **Internal Team**: Core Cytognosis engineers and scientists have access to Tier 1-3 data *only* within provisioned, audited cloud enclaves. Raw Tier 4 access is restricted to the Data Security Officer (DSO) or explicitly authorized personnel.
- **External Collaborators**: Cannot directly access Cytognosis controlled-access (Tier 3) boundaries. Collaborators must independently apply for DARs through the respective repository (e.g., NIH NDA). Joint analysis happens via federated learning or by sharing non-identifiable summary statistics.

---

## 3. Infrastructure Requirements

To satisfy the Data Use Certifications (DUCs) for Tier 3 and Tier 4 data, the Cytognosis Google Cloud Platform (GCP) infrastructure must enforce the following technical controls.

### 3.1 Encryption Standards

- **At Rest**: All storage buckets (`cytognosis-phi-prod`, `cytognosis-phi-core`) and databases containing Tier 3/4 data must utilize **Customer-Managed Encryption Keys (CMEK)** via Google Cloud Key Management Service (KMS). Default Google-managed keys are insufficient for our highest security tier.
- **In Transit**: Mandatory TLS 1.2+ for all data movement. Intra-VPC traffic holding PHI must also be encrypted.

### 3.2 Authentication & Authorization

- **Identity Provider**: Google Workspace serves as the central IdP.
- **Multi-Factor Authentication (MFA)**: Hardware security keys (FIDO2) or time-based OTP are strictly enforced for all identities accessing the `cytognosis-phi-prod` environments.
- **Role-Based Access Control (RBAC)**: Enforced via Google Cloud IAM. Permissions are granted via Workspace Groups (e.g., `gcp-data-scientists@cytognosis.org`), never directly to individual user accounts.
- **Least Privilege**: Temporary, just-in-time (JIT) access is preferred for any elevated operational tasks.

### 3.3 Account Separation & Network Boundaries

- **Environment Isolation**: The `cytognosis-phi-prod` project is completely isolated from `cytognosis-infrastructure` and public-facing projects.
- **VPC Service Controls (VPC-SC)**: A rigorous perimeter is placed around the data projects. Exporting data out of the VPC requires explicit egress rules approved by the DSO.
- **No Public IP Addresses**: Compute instances handling governed datasets do not have public IP addresses. They utilize Cloud NAT and Identity-Aware Proxy (IAP) for secure administrative access.
- **Auditing**: Cloud Audit Logs (Data Access logging) are shipped to a centralized, tamper-evident log sink with retention policies matching regulatory minimums (e.g., 6 years for HIPAA).
