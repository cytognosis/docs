> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps, New Team Members
> **Tags**: `infrastructure`, `index`, `gcp`
> **Last verified**: 2026-06-14 against gcloud

# Cytognosis Foundation — Master Infrastructure

## BLUF

Two live GCP projects (`cytognosis-infrastructure`, `cytognosis-phi-prod`). One VM (`cytohost`, e2-highmem-2, us-central1-b, 11 containers). Public website on Cloud Run. All infra docs link from here.

---

## Quick State Summary

| Resource | Current State |
|---|---|
| VM `cytohost` | e2-highmem-2, x86\_64, us-central1-b, RUNNING |
| cytohost external IP | 34.171.23.255 (ephemeral; static `cytohost-ip` 136.111.39.188 reserved but NOT attached) |
| Self-hosted containers | 11 running (see architecture.md) |
| Website | Cloud Run `cytognosis-website-v2` in `cytognosis-phi-prod` |
| `cytognosis-data` project | **Does not exist** (planned) |
| Auto-start/stop scheduler | **Not implemented** (Cloud Scheduler API disabled; roadmap) |

---

## Core Documentation

### 1. [Architecture Overview](architecture.md)

GCP project topology, compute (cytohost), full 11-container service matrix, Cloud Run services, domain architecture, data layer. **Start here.**

### 2. [DNS & GCP Architecture](DNS_AND_GCP_ARCHITECTURE.md)

Six Cloud DNS zones with dedup plan; canonical A/MX/TXT records per domain; pending remediation items (static IP attach, DNS dedup).

### 3. [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md)

Cloud Run migration rationale, CI/CD OIDC federation (`website-deployer`), Artifact Registry layout, developer spin-up.

### 4. [GCP Setup](gcp-setup.md)

Full GCS bucket inventory (16 buckets in `cytognosis-infrastructure`, 3 in `cytognosis-phi-prod`); IAM / service accounts; Workload Identity Federation config; Artifact Registry.

### 5. [Compute: Node Types](compute/node-types.md)

cytohost specs, SSH access, on-demand research compute tiers.

### 6. [CI/CD](ci-cd/)

- [OIDC Federation](ci-cd/oidc-federation.md) — Workload Identity pool `github-pool`, provider `github-provider`, SA bindings
- [Runner Setup](ci-cd/runner-setup.md) — Self-hosted GitHub Actions runner on cytohost
- [Website Deployment](ci-cd/website-deployment.md) — Full website CI/CD pipeline

### 7. [Self-Hosted Stack](self-hosted/)

- [README](self-hosted/README.md) — Hub for all self-hosted service docs
- [Deployment Walkthrough](self-hosted/deployment_walkthrough.md) — Live state: 11 containers, routing, DNS

### 8. [Container Framework](container-framework.md)

YAML-driven framework for managing the Docker stack. Service catalog, stack definitions, quick commands.

### 9. [Data Strategy & Compliance](data-strategy/README.md)

Unified data hub. Master strategy, public dataset strategy, dataset catalog, FAIRification mandate, HIPAA program, controlled-access SOPs (NIH NDA + academic partnerships), multimodal schemas, DUA template — plus the scholarly knowledge graph stack.

### 10. [Technical Data Infrastructure (HIPAA & PHI)](data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md)

GCS bucket taxonomy, VPC Service Controls, Cloud Healthcare API, Confidential Compute, and IAM controls for sensitive genomics and neuroscience datasets.

### 11. [Tools Catalog](tools/README.md)

Comprehensive 911-tool technology landscape across the Cytognosis 16-layer infrastructure stack. Includes master catalog, infrastructure deep-dive, and external repository directory.

### 12. [Reproducibility & FAIR Strategy](reproducibility/README.md)

Six-principle reproducibility framework. Schema strategy, artifact VFS/SWHID, environments/containers, provenance/lineage, SEEK/WorkflowHub, acceptance KPIs.

---

> [!NOTE]
> **HIPAA compliance dashboard**: [`data-strategy/compliance/HIPAA-STATUS.md`](data-strategy/compliance/HIPAA-STATUS.md)
>
> **NIH GDS 2025 requirements**: [`data-strategy/compliance/nih-gds-requirements.md`](data-strategy/compliance/nih-gds-requirements.md)
