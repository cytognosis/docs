# CI/CD — Website Deployment Pipeline

## Overview

All Cytognosis web deployments use **Workload Identity Federation (OIDC)** — no long-lived
service account keys exist anywhere. GitHub Actions exchanges a short-lived GitHub JWT for
a GCP access token at runtime.

## Architecture

```
GitHub push → Actions workflow → OIDC token exchange → GCP credentials
                                        ↓
                               website-deployer SA
                                        ↓
                          docker build + push → cytognosis-website-v2
                                        ↓
                               gcloud run deploy → Cloud Run (us-central1)
```

## Repository: `cytognosis/website`

**Workflow file**: `.github/workflows/deploy.yml`

| Variable | Value |
|---|---|
| `PROJECT_ID` | `cytognosis-phi-prod` |
| `REGION` | `us-central1` |
| `SERVICE` | `cytognosis-website-v2` |
| `REPO_NAME` | `cytognosis-website-v2` |
| Image registry | `us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:<sha>` |
| Cloud Run URL | `https://cytognosis-website-v2-tdmthpm4va-uc.a.run.app` |

**Runtime secrets** (from Secret Manager in `cytognosis-phi-prod`):
- `website-session-key` → `SECRET_KEY`
- `website-db-url` → `DATABASE_URL`
- `website-client-id` → `GOOGLE_CLIENT_ID`
- `website-client-secret` → `GOOGLE_CLIENT_SECRET`

## Service Account

`website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com`

**Roles on `cytognosis-infrastructure`**: `storage.objectAdmin`, `compute.loadBalancerAdmin`
**Roles on `cytognosis-phi-prod`**: `artifactregistry.writer`, `run.admin`,
`iam.serviceAccountUser`, `secretmanager.secretAccessor`

See [service-accounts.md](../service-accounts.md) for full SA inventory.

## Adding a New Deployment Workflow

Any repo under `github.com/cytognosis/` can use `website-deployer` via OIDC.
No per-repo registration is needed — the pool condition is org-wide.

```yaml
# Minimum workflow snippet for any Cytognosis repo
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

## Registry Cleanup Policy

`cytognosis-website-v2` has an automated cleanup policy:
- Keep 5 most recent image versions
- Delete all others older than 24h
- Runs automatically; no manual pruning needed

---
*See also: [oidc-federation.md](oidc-federation.md) · [runner-setup.md](runner-setup.md)*
