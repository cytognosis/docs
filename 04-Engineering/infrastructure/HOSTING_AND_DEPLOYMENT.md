> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `hosting`, `cloud-run`, `ci-cd`, `oidc`, `artifact-registry`
> **Variants**: Technical (this doc) - Readable (same filename in Obsidian vault: 04-Engineering/infrastructure/) - Agent (n/a)
> **Last verified**: 2026-06-14 against gcloud

# Hosting & Deployment Architecture

## BLUF

The public website runs on Cloud Run in `cytognosis-phi-prod`. All deployments use OIDC (no long-lived keys). The `website-deployer` service account lives in `cytognosis-infrastructure`. Cloud Run API is disabled in `cytognosis-infrastructure` — website deployment targets `cytognosis-phi-prod` only.

---

## 1. Cloud Run: Website

### Why Cloud Run

Historically the Cytognosis frontend was statically hosted in Google Cloud Storage. Migration to Cloud Run was required for:

- Dynamic form handling and OAuth/OIDC login integrations
- SQLite/SQLModel parsing and HIPAA-ready data processing
- Backend computational capabilities that static buckets cannot provide

### Current Deployment

| Field | Value |
|---|---|
| Service | `cytognosis-website-v2` |
| Project | `cytognosis-phi-prod` (NOT `cytognosis-infrastructure`) |
| Region | `us-central1` |
| Tech stack | Python 3.13, FastAPI, Uvicorn, SQLModel, Jinja2 |
| Cloud Run URL | https://cytognosis-website-v2-tdmthpm4va-uc.a.run.app |
| Image | `us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:<sha>` |
| Last deployed | 2026-06-09 (by ali.mohammadi@cytognosis.org) |

**Additional Cloud Run service**: `stories-api` (also in `cytognosis-phi-prod`; last deployed 2025-12-09).

> [!NOTE]
> Cloud Run API is **disabled** in `cytognosis-infrastructure`. All Cloud Run services live exclusively in `cytognosis-phi-prod`.

---

## 2. CI/CD Operations

### Workload Identity Federation (OIDC)

All deployments use short-lived OIDC tokens. No long-lived JSON service account keys exist.

```
GitHub push → Actions workflow → OIDC token exchange → GCP credentials
                                         ↓
                                website-deployer SA (cytognosis-infrastructure)
                                         ↓
                           docker build + push → cytognosis-website-v2 registry
                                         ↓
                                gcloud run deploy → Cloud Run (cytognosis-phi-prod)
```

| Field | Value |
|---|---|
| WIF pool | `github-pool` (project `cytognosis-infrastructure`, number 517562623935) |
| Provider | `github-provider` |
| Condition | `attribute.repository_owner == "cytognosis"` (org-wide; all repos) |
| Service account | `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` |
| SA roles on `cytognosis-infrastructure` | `storage.objectAdmin`, `compute.loadBalancerAdmin` |
| SA roles on `cytognosis-phi-prod` | `artifactregistry.writer`, `run.admin`, `iam.serviceAccountUser`, `secretmanager.secretAccessor` |

**Minimum workflow snippet** for any Cytognosis repo:

```yaml
permissions:
  contents: read
  id-token: write      # REQUIRED for OIDC token

steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
      service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"

  - uses: google-github-actions/setup-gcloud@v2
    with:
      project_id: cytognosis-phi-prod
```

> [!IMPORTANT]
> The service account suffix is `@cytognosis-infrastructure.iam.gserviceaccount.com`. Any reference to `@cytognosis-phi-prod` for the `website-deployer` SA is incorrect.

---

## 3. Artifact Registries

| Registry path | Project | Format | Purpose |
|---|---|---|---|
| `us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/` | `cytognosis-infrastructure` | Docker | Internal compute images (empty as of 2026-06-14) |
| `us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/` | `cytognosis-infrastructure` | Python | Internal Python packages (PyPI mirror) |
| `us-central1.pkg.dev/cytognosis-infrastructure/cytognosis-npm/` | `cytognosis-infrastructure` | npm | Internal npm packages |
| `us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/` | `cytognosis-phi-prod` | Docker | Website container images (active, ~594 MB) |
| `us-docker.pkg.dev/cytognosis-phi-prod/phi-services/` | `cytognosis-phi-prod` | Docker | HIPAA-compliant service containers (~82 MB) |

**Registry cleanup**: `cytognosis-website-v2` keeps 5 most recent versions; others deleted after 24h. No manual pruning required.

---

## 4. Runtime Secrets (Website)

Secrets are stored in Secret Manager (`cytognosis-phi-prod`):

| Secret name | Env var |
|---|---|
| `website-session-key` | `SECRET_KEY` |
| `website-db-url` | `DATABASE_URL` |
| `website-client-id` | `GOOGLE_CLIENT_ID` |
| `website-client-secret` | `GOOGLE_CLIENT_SECRET` |

---

## 5. Developer Spin-Up

Local development bypasses Docker Compose for rapid frontend iteration:

```bash
# 1. Install dependencies
uv sync

# 2. Start ASGI server
uv run uvicorn main:app --port 8000 --reload
```

Local deployments use SQLite (`database.db`) to mirror Cloud SQL schema before production deployments.

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](architecture.md) | Full topology |
| [CI/CD: OIDC Federation](ci-cd/oidc-federation.md) | Detailed WIF setup |
| [CI/CD: Website Deployment](ci-cd/website-deployment.md) | Full pipeline detail |
| [GCP Setup](gcp-setup.md) | Bucket and IAM inventory |
| [Service Accounts](service-accounts.md) | SA inventory |
