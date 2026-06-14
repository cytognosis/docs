# GCP Project Setup

> v1.0 | Last updated: 2026-05-26

## Project Layout

| Project ID | Purpose | Region | Classification |
|------------|---------|--------|----------------|
| `cytognosis-infrastructure` | DNS, IAM root, Artifact Registry, legacy buckets | us-central1 | Management |
| `cytognosis-phi-prod` | Website (Cloud Run), user data, HIPAA workloads | us-central1 | **Sensitive (PHI)** |
| `cytognosis-data` | Data platform, BigQuery, analytics | us-central1 | Regulated |

## Cloud Storage Buckets

### Data Hub (`cytognosis-data`)

```
gs://cytognosis-data-hub/
├── dvc-cache/                 # Content-addressed DVC cache (md5 → blob)
│                                Shared across all projects
├── processed/
│   └── cytos/dvc/             # Cytos project DVC remote
├── purdue/
│   ├── active/                # Collaborator active workspace
│   └── delivered/             # Finalized deliveries
├── shared/
│   ├── soma/                  # TileDB-SOMA exports
│   ├── gwas/                  # GWAS summary statistics
│   ├── embeddings/            # Feature vectors
│   └── reference/             # GRCh38, GENCODE GTFs
├── public-mirror/             # Public dataset mirrors
└── manifests/                 # Dataset manifest JSONs
```

### PHI Production (`cytognosis-phi-prod`)

```
gs://cytognosis-phi-prod/
├── dvc-cache/                 # HIPAA-compliant DVC cache
├── pec/                       # PsychENCODE data
└── clinical/                  # Clinical partner data
```

Protected by VPC Service Controls, Cloud Healthcare API, and Confidential Compute.

## IAM Configuration

### Service Accounts

| Account | Purpose | Roles |
|---------|---------|-------|
| `website-deployer@cytognosis-phi-prod` | CI/CD Cloud Run deployments | Cloud Run Admin, Storage Object Viewer |
| `dvc-reader@cytognosis-data` | Read-only DVC access | Storage Object Viewer on data-hub |
| `dvc-writer@cytognosis-data` | Read-write DVC access | Storage Object Admin on data-hub |

### Workload Identity Federation

GitHub Actions uses OIDC federation (no long-lived JSON keys):

```yaml
# .github/workflows/deploy.yml
- uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: 'projects/123/locations/global/workloadIdentityPools/github/providers/cytognosis'
    service_account: 'website-deployer@cytognosis-phi-prod.iam.gserviceaccount.com'
```

## Artifact Registry

Container images push to GCP Artifact Registry:

```
us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/
├── neo4j-cytognosis:latest
├── surrealdb-cytognosis:latest
├── jupyter-cytognosis:latest
└── caddy-cytognosis:latest
```

## DNS Configuration

### Cloud DNS Zones

| Zone | Domain | Status |
|------|--------|--------|
| `cg-org` | cytognosis.org | Active canonical |
| `cg-com` | cytognosis.com | Active canonical |
| `cg-ai` | cytognosis.ai | Active canonical |
| `org-zone` | cytognosis.org | Legacy fallback |
| `com-zone` | cytognosis.com | Legacy fallback |
| `ai-zone` | cytognosis.ai | Legacy fallback |

### Key DNS Records

```
# Cloud Run (serverless)
@       A      216.239.32.21, 216.239.34.21, 216.239.36.21, 216.239.38.21
www     CNAME  ghs.googlehosted.com.

# Core services (cytohost VM)
cal     A      136.111.39.188
code    A      136.111.39.188
hub     A      136.111.39.188
```

## Authentication

### Application Default Credentials

```bash
gcloud auth application-default login
# Creates ~/.config/gcloud/application_default_credentials.json
```

### Service Account Key (CI/CD only)

```bash
# Prefer Workload Identity Federation
# Only use key files for local development if WIF unavailable
gcloud iam service-accounts keys create key.json \
    --iam-account=dvc-writer@cytognosis-data.iam.gserviceaccount.com
```

## Related Documentation

- [Architecture Overview](architecture.md)
- [Container Framework](container-framework.md)
- [DVC Strategy](dvc-strategy.md)
