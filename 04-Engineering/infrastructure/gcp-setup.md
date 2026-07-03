> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `gcp`, `buckets`, `iam`, `artifact-registry`, `oidc`
> **Last verified**: 2026-06-19 against gcloud

# GCP Project Setup

## BLUF

Two live projects: `cytognosis-infrastructure` (DNS, IAM, buckets, compute) and `cytognosis-phi-prod` (Cloud Run, PHI storage). `cytognosis-data` does not exist. 14 total GCS buckets (11 infra + 3 phi-prod). Three service accounts: `website-deployer`, `stories-api-sa`, `cytohost-sa`. OIDC pool `github-pool` is in `cytognosis-infrastructure`.

---

## Project Layout

| Project ID | Project Number | Purpose | Region | Status |
|---|---|---|---|---|
| `cytognosis-infrastructure` | 517562623935 | DNS zones, IAM root, Artifact Registry, GCS buckets, Compute Engine (cytohost) | us-central1 | **Live** |
| `cytognosis-phi-prod` | 143911445857 | Website (Cloud Run), user data, HIPAA workloads | us-central1 | **Live** |
| `cytognosis-data` | — | Data platform, BigQuery, analytics | us-central1 | **Planned — does not exist** |

> [!NOTE]
> Cloud Run API, Cloud Functions API, and Cloud Scheduler API are all **disabled** in `cytognosis-infrastructure`. Cloud Run services live exclusively in `cytognosis-phi-prod`.

---

## Cloud Storage Buckets

### cytognosis-infrastructure (11 buckets)

| Bucket | Versioning | Retention Lock | Notes |
|---|---|---|---|
| `gs://cytognosis/` | No | No | Brand reserve; potential sub-folders in future |
| `gs://cytognosis-artifacts/` | **Yes** | No | Metadata, manifests, provenance, MLflow artifacts |
| `gs://cytognosis-audit-7yr/` | No | **7yr locked** | Created 2026-05-18; immutable, tamper-evident |
| `gs://cytognosis-data-hub/` | **Yes** | No | DVC cache, datasets; lifecycle 60d→Nearline, 180d→Coldline |
| `gs://cytognosis-internal/` | No | No | Internal team files |
| `gs://cytognosis-phi-prod/` | **Yes** | **7yr locked** | Labels: compliance=hipaa, data-class=phi; cannot delete until 2033 |
| `gs://cytognosis-public-data/` | No | No | De-identified public datasets |
| `gs://cytonome/` | No | No | Pillar brand reserve |
| `gs://cytoscope/` | No | No | Pillar brand reserve |
| `gs://cytoverse/` | No | No | Pillar brand reserve |
| `gs://neuroverse/` | No | No | Pillar brand reserve |

> [!NOTE]
> `gs://cytognosis-artifacts` replaces the previous `gs://cytognosis-mlflow-artifacts`. MLflow uses `gs://cytognosis-artifacts/mlflow/` as its artifact root. Non-MLflow metadata (manifests, provenance, catalog indexes) lives alongside.
> Deleted 2026-06-19: `cytoagent`, `cytoexplorer`, `cytomark`, `cytopilot`, `cytoskeleton` (non-pillar brand reserves), `cytognosis-restricted-prod`, `cytognosis-mlflow-artifacts`.

### cytognosis-phi-prod (3 buckets)

| Bucket | Versioning | Retention | KMS | Notes |
|---|---|---|---|---|
| `gs://cytognosis-phi-collab/` | **Yes** | 7-day soft delete | **CMEK: phi-bucket-key** | External PHI collaborations (sub-prefixes per DUC/partner) |
| `gs://cytognosis-phi-core/` | **Yes** | 7-day soft delete | **CMEK: phi-bucket-key** | Raw PHI genomic/clinical data |
| `gs://cytognosis-phi-prod_cloudbuild/` | No | No | None | Cloud Build staging (auto-created by GCP); 30-day lifecycle |

Both PHI buckets use CMEK: keyring `phi-keyring`, key `phi-bucket-key` in us-central1. Verified via `gcloud` 2026-06-19.

### Data Hub Layout

```
gs://cytognosis-data-hub/
├── dvc-cache/                 Content-addressed DVC cache (shared across projects)
├── processed/
│   └── cytos/dvc/             Cytos project DVC remote
├── purdue/
│   ├── active/                Collaborator active workspace
│   └── delivered/             Finalized deliveries
├── shared/
│   ├── soma/                  TileDB-SOMA exports
│   ├── gwas/                  GWAS summary statistics
│   ├── embeddings/            Feature vectors
│   └── reference/             GRCh38, GENCODE GTFs
├── public-mirror/             Public dataset mirrors
└── manifests/                 Dataset manifest JSONs
```

---

## IAM: Service Accounts

| Account | Project | Purpose | Disabled? |
|---|---|---|---|
| `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` | cytognosis-infrastructure | CI/CD Cloud Run deployments | No |
| `cytohost-sa@cytognosis-infrastructure.iam.gserviceaccount.com` | cytognosis-infrastructure | Compute Engine SA attached to cytohost (OS Login enabled) | No |
| `stories-api-sa@cytognosis-phi-prod.iam.gserviceaccount.com` | cytognosis-phi-prod | Stories API runtime SA | No |
| `517562623935-compute@developer.gserviceaccount.com` | cytognosis-infrastructure | Default compute SA (replaced by cytohost-sa) | **Yes — intentionally disabled** |

> [!IMPORTANT]
> The `website-deployer` SA is in **`cytognosis-infrastructure`**, not `cytognosis-phi-prod`. Any OIDC config referencing `website-deployer@cytognosis-phi-prod` is incorrect.
>
> `dvc-reader@cytognosis-data` and `dvc-writer@cytognosis-data` SAs referenced in older docs do NOT exist — they depend on the `cytognosis-data` project, which has not been provisioned.
>
> The default compute SA on cytohost has been replaced by `cytohost-sa` with OS Login enabled (2026-06-19).

---

## Workload Identity Federation

```yaml
# Minimum OIDC auth snippet for any Cytognosis GitHub Actions workflow
- uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
    service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"
```

| Field | Value |
|---|---|
| Pool | `github-pool` |
| Provider | `github-provider` |
| Issuer | `https://token.actions.githubusercontent.com` |
| Condition | `attribute.repository_owner == "cytognosis"` (all org repos) |
| Project | `cytognosis-infrastructure` (517562623935) |

---

## Artifact Registry

| Registry | Format | Location | Size | Purpose |
|---|---|---|---|---|
| `cytognosis-infrastructure/cytognosis-compute` | Docker | us-central1 | 0 MB (empty) | Internal compute images |
| `cytognosis-infrastructure/cytognosis-python` | Python | us-central1 | ~4.4 MB | Internal PyPI packages |
| `cytognosis-infrastructure/cytognosis-npm` | npm | us-central1 | ~0.05 MB | Internal npm packages |
| `cytognosis-phi-prod/cytognosis-website-v2` | Docker | us-central1 | ~594 MB | Website container images |
| `cytognosis-phi-prod/phi-services` | Docker | us (multi-region) | ~82 MB | HIPAA-compliant service containers |

---

## Authentication

### Application Default Credentials (local dev)

```bash
gcloud auth application-default login
# Creates ~/.config/gcloud/application_default_credentials.json
```

### Service Account Keys (avoid)

Prefer Workload Identity Federation. SA keys are only for local development when WIF is unavailable:

```bash
gcloud iam service-accounts keys create key.json \
    --iam-account=website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com
```

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](architecture.md) | Full topology |
| [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md) | Cloud Run + CI/CD |
| [CI/CD: OIDC Federation](ci-cd/oidc-federation.md) | WIF detailed setup |
| [Service Accounts](service-accounts.md) | Canonical SA inventory |
| [DVC Strategy](dvc-strategy.md) | Data version control |
| [Container Framework](container-framework.md) | Self-hosted stack |
