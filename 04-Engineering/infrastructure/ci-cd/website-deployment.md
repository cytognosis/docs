> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `ci-cd`, `cloud-run`, `oidc`, `website`
> **Last verified**: 2026-06-14 against gcloud

> [!WARNING]
> **Website redesign in progress.** The deployment pipeline, Dockerfile, and Cloud Run config may change when the new website lands. The OIDC/WIF setup and `website-deployer` SA remain valid regardless. Re-verify after redesign merge.

# CI/CD — Website Deployment Pipeline

## BLUF

Deployments push to `cytognosis-phi-prod` Cloud Run via OIDC. The WIF pool `github-pool` and service account `website-deployer` both live in `cytognosis-infrastructure`. No long-lived keys exist.

---

## Architecture

```
GitHub push → Actions workflow → OIDC token exchange → GCP credentials
                                         ↓
                                website-deployer SA (cytognosis-infrastructure)
                                         ↓
                           docker build + push → cytognosis-website-v2 registry
                                         ↓
                                gcloud run deploy → Cloud Run (cytognosis-phi-prod, us-central1)
```

---

## Repository: `cytognosis/website`

**Workflow file**: `.github/workflows/deploy.yml`

| Variable | Value |
|---|---|
| `PROJECT_ID` | `cytognosis-phi-prod` |
| `REGION` | `us-central1` |
| `SERVICE` | `cytognosis-website-v2` |
| `REPO_NAME` | `cytognosis-website-v2` |
| Image registry | `us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:<sha>` |
| Cloud Run URL | https://cytognosis-website-v2-tdmthpm4va-uc.a.run.app |

**Runtime secrets** (from Secret Manager in `cytognosis-phi-prod`):

| Secret name | Env var |
|---|---|
| `website-session-key` | `SECRET_KEY` |
| `website-db-url` | `DATABASE_URL` |
| `website-client-id` | `GOOGLE_CLIENT_ID` |
| `website-client-secret` | `GOOGLE_CLIENT_SECRET` |

---

## Service Account

`website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com`

| Project | Roles |
|---|---|
| `cytognosis-infrastructure` | `storage.objectAdmin`, `compute.loadBalancerAdmin` |
| `cytognosis-phi-prod` | `artifactregistry.writer`, `run.admin`, `iam.serviceAccountUser`, `secretmanager.secretAccessor` |

---

## Adding a New Deployment Workflow

Any repo under `github.com/cytognosis/` can use `website-deployer` via OIDC. No per-repo registration is needed — the pool condition is org-wide (`attribute.repository_owner == "cytognosis"`).

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

---

## Registry Cleanup Policy

`cytognosis-website-v2` has an automated cleanup policy:

- Keep 5 most recent image versions
- Delete all others older than 24h
- Runs automatically; no manual pruning needed

---

## Cross-References

| Document | Relationship |
|---|---|
| [CI/CD: OIDC Federation](oidc-federation.md) | WIF pool and provider setup |
| [CI/CD: Runner Setup](runner-setup.md) | Self-hosted runner on cytohost |
| [Hosting & Deployment](../HOSTING_AND_DEPLOYMENT.md) | Cloud Run architecture |
| [Service Accounts](../service-accounts.md) | SA inventory |
