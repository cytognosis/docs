# Technical Data Infrastructure Strategy (HIPAA & PHI)

**Last Updated**: May 2026
**Status**: 🔵 ACTIVE — bucket taxonomy and project boundaries enforced; VPC-SC perimeter and Healthcare API integration in progress
**Maintainer**: Infrastructure Team

## 🎯 Overview

This document specifies the Google Cloud infrastructure requirements, architectures, and compliance controls that let Cytognosis securely access, store, host, and analyze sensitive multimodal human datasets (genomics from NIH NDA, UKBB, etc.). It is the technical enforcement layer for the [Data Governance Policy](policies/data-governance-policy.md) and the operational substrate for the [scholarly knowledge graph](scholarly-knowledge-graph.md).

---

## 🏗️ Core Architecture & Boundaries

To isolate sensitive data from public-facing infrastructure, Cytognosis utilizes a strict multi-project strategy.

### 1. Project Isolation
- **`cytognosis-phi-prod`**: The heavily fortified enclave strictly reserved for PHI (Protected Health Information) and sensitive genomics data.
- All external data (NIH NDA, UKBB) must be ingested directly into `cytognosis-phi-prod`. No PHI is ever allowed in `cytognosis-infrastructure`.

### 2. VPC Service Controls (VPC-SC)
- A **VPC Service Perimeter** must be established around the `cytognosis-phi-prod` project. 
- This zero-trust perimeter explicitly denies data exfiltration by blocking unapproved API calls bridging the secure project and the outside world, even if a user has valid IAM credentials.

---

## 🗄️ Storage & Compute Requirements

### GCS Buckets (The Data Lake Taxonomy)

To satisfy the stringent and diverse requirements for internal operations versus external collaborations under NIH NDA and UKBB, Cytognosis explicitly provisions distinct categorizations of GCS buckets:

#### 0. Public Media & Assets (`cytognosis`)
- **Project**: `cytognosis-infrastructure`
- **Purpose**: Global public storage for organization-wide assets (PDFs, media kits, public branding).
- **Compliance**: Standard Google-managed encryption. Publicly readable.

#### 1. Internal Operations (`cytognosis-internal`)
- **Project**: `cytognosis-infrastructure`
- **Purpose**: Broad non-PHI team operations, datasets, models, working files, and internal scripts.
- **Compliance**: Standard Google-managed encryption. Strict IAM for internal team members only. No PHI permitted.

#### 2. Public Data Sharing (`cytognosis-public-data`)
- **Project**: `cytognosis-data`
- **Purpose**: Broad open-science dissemination of thoroughly de-identified, aggregated research results.
- **Compliance**: Standard encryption. Public read access allowed. Data must pass through the DLP API before release to verify zero PHI.

#### 3. Internal Sensitive Data (`cytognosis-phi-core`)
- **Project**: `cytognosis-phi-prod`
- **Purpose**: The primary vault for raw genomics, DICOM imaging, and clinical data (e.g., NIH NDA raw imports).
- **Compliance**: 
  - **Location**: `us-central1` (Single-region preferred to restrict data residency boundaries).
  - **CMEK**: Customer-Managed Encryption Keys explicitly enforced. Default Google-managed keys are insufficient.
  - **VPC-SC**: Fully bounded within the VPC Service Perimeter.
  - **Auditing**: Cloud Audit Logs explicitly enabled for all `DATA_READ`/`DATA_WRITE` events.
  - **Access**: Uniform Bucket-Level Access enforced. No object-level ACLs.

#### 4. Sensitive Collaborations (`cytognosis-phi-collab-[id]`)
- **Project**: `cytognosis-phi-prod`
- **Purpose**: Highly restricted joint-analysis spaces specific to individual external partnerships (e.g., UKBB researchers).
- **Compliance**: 
  - **CMEK + VPC-SC** identically enforced. 
  - **IAM**: Bounded strictly to time-limited Service Account tokens matching the exact IRB roster. 
  - **Egress**: Researchers may only interact with this bucket via Vertex AI Workbench notebooks launched securely inside the VPC boundary, guaranteeing sensitive data cannot be downloaded locally to unmanaged external workstations.

### Databases (Cloud SQL & Healthcare API)
- **Cloud SQL (PostgreSQL)**: The `cytognosis-db-prod` instance must run natively on private IPs within the VPC. Public IP access must be permanently disabled. Database access is brokered through the Cloud SQL Auth Proxy.
- **Google Cloud Healthcare API**: For FHIR, HL7v2, and DICOM data, the GCP Healthcare API will be leveraged to provide managed, HIPAA-compliant storage and de-identification capabilities natively.

### Compute & Analysis Substrates
- **Cloud Run**: Containers processing PHI must be built from minimal, hardened base images (e.g., Distroless or Alpine) stored in the heavily restricted `phi-services` Artifact Registry.
- **Confidential Space / Confidential VMs**: For highly sensitive third-party workloads (e.g., federated learning across UKBB), we will provision Confidential Compute environments (AMD SEV) ensuring memory is hardware-encrypted even from Google Cloud hypervisors.

---

## 🔐 Compliance & Identity (IAM)

### HIPAA & BAA
- A **Business Associate Agreement (BAA)** is executed with Google Cloud covering the entire organization. Only BAA-covered services (Cloud SQL, GCS, Cloud Run, Healthcare API) may be used within `cytognosis-phi-prod`.

### External Data Mandates (NIH NDA, dbGaP, UKBB)
External data usage agreements require strict constraints:
- **dbGaP (Genotypes and Phenotypes)**: Requires explicit tracking of authorized users. Short-lived Service Account tokens and deeply restricted IAM groups will map directly to the approved IRB roster. Break-glass accounts will trigger PagerDuty alerts.
- **Data De-identification**: When preparing datasets for collaborative/public release, raw data must be run through the DLP (Data Loss Prevention) API or Healthcare API de-identification tools to scrub identifiers before leaving the VPC perimeter.

### Researcher Access
Collaborators interacting with the data will do so solely via:
1. **Vertex AI Workbench**: Jupyter notebooks provisioned firmly *inside* the VPC-SC perimeter without external internet egress routes. Data cannot be downloaded locally.
2. **Signed URLs**: Time-bound (e.g., 15-minute) cryptographic URLs for explicit secure payload delivery when externalizing non-PHI derivatives.

---

## 📈 Next Steps for Activation
1. Finalize the exact IAM mappings for the current research team.
2. Formally instantiate the VPC Service Perimeter around `cytognosis-phi-prod`.
3. Provision the CMEK keyrings in KMS for the incoming data lakes.
