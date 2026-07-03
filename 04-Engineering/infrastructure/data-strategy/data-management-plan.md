# Cytognosis Data Management Plan (DMP)

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, compliance, grant writers
> **Tags**: `dmp`, `fair`, `hipaa`, `nih-gds`

**Status**: Active | **Last Updated**: 2026-06-14

This document outlines the master data strategy for the Cytognosis Foundation, aligning with NIH GDS policy and our FAIR data principles.

## 1. Data Types and Sources

- **Public Data (`gs://cytognosis-public-data`)**: De-identified, open-access datasets (e.g., benchmark data, synthetic profiles).
- **Internal Data (`gs://cytognosis-internal`)**: Internal development, non-PHI operational data, testing data.
- **Shared Hub (`gs://cytognosis-data-hub`)**: Processed datasets shared with external collaborators (e.g., Purdue).
- **Sensitive PHI Core (`gs://cytognosis-phi-core`)**: Raw genomic/clinical PHI, L3 controlled data.
- **PHI Collaboration (`gs://cytognosis-phi-collab`)**: External PHI collaboration data, CMEK-encrypted, governed by Data Use Certifications.

## 2. FAIR Data Repositories

Cytognosis enforces FAIR (Findable, Accessible, Interoperable, Reusable) principles via the following stack:

1. **FAIRDOM-SEEK** (`hub.cytognosis.org`): The central metadata registry for Investigations, Studies, Assays, and DataFiles.
2. **WorkflowHub** (`workflows.cytognosis.org`): RO-Crate registry for computational workflows.
3. **LaminDB** (Planned): Internal data artifact registry.
4. **Zoekt** (`code.cytognosis.org`): Internal fast code search index.

## 3. Storage Infrastructure

Data is stored in Google Cloud Storage (GCS) utilizing uniform bucket-level access.
- **Audit Logs (`gs://cytognosis-audit-7yr`)**: 7-year immutable retention policy enforced via Cloud Storage Bucket Lock.
- **Location**: All data resides in `us-central1`.
- **Encryption**: CMEK (`phi-keyring`/`phi-bucket-key`) on PHI buckets; Google-managed on non-PHI buckets.

## 4. Access and Security

- **PHI Access**: Restricted via Google Workspace/IAM to authorized researchers only. Requires HIPAA training and DUC sign-off.
- **Federated Identity**: External collaborators authenticate via ELIXIR-AAI mapping to Cytognosis Google Workspace Groups.

## 5. Provenance and Lineage

All data artifacts are tracked using a 4-layer provenance stack:
1. **DVC**: Content-addressed hashing for data files.
2. **redun**: Execution provenance for pipelines.
3. **MLflow**: Model and experiment tracking.
4. **RO-Crate**: Standardized packaging for publication.

Every asset registered in the VFS receives a Software Heritage Identifier (SWHID) and a W3C PROV-J sidecar file.
