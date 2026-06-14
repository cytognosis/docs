# Registry Authentication

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `artifact-registry`, `auth`, `oidc`, `docker`, `python`

**Last verified: 2026-06-14** — OIDC pool `github-pool` / provider `github-provider` confirmed ACTIVE in `cytognosis-infrastructure`. Workload identity provider resource: `projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider`.

## Authentication Methods

### Local Development (gcloud ADC)

```bash
# One-time setup
gcloud auth login
gcloud auth configure-docker us-central1-docker.pkg.dev

# After this, all registry access works automatically:
docker pull us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/datascience:latest
uv add cytognosis-yar  # finds it via [[tool.uv.index]]
```

### CI/CD (GitHub Actions — OIDC, no keys)

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
      service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"

  # Docker: configure auth
  - run: gcloud auth configure-docker us-central1-docker.pkg.dev

  # Python: use access token
  - run: |
      TOKEN=$(gcloud auth print-access-token)
      pip install --extra-index-url \
        https://oauth2accesstoken:${TOKEN}@us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/ \
        cytognosis-yar
```

### External Collaborators (read-only service account key)

For Purdue students or external collaborators who need to pull a specific package
but cannot use OIDC:

```bash
# Create a read-only SA for the collaborator
gcloud iam service-accounts create collab-reader \
  --display-name="External collaborator read-only" \
  --project=cytognosis-infrastructure

gcloud projects add-iam-policy-binding cytognosis-infrastructure \
  --member="serviceAccount:collab-reader@cytognosis-infrastructure.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"

# Generate a short-lived key (share this, rotate/delete after project ends)
gcloud iam service-accounts keys create /tmp/collab-key.json \
  --iam-account=collab-reader@cytognosis-infrastructure.iam.gserviceaccount.com

# Collaborator uses:
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/collab-key.json
pip install --extra-index-url \
  https://oauth2accesstoken:$(gcloud auth print-access-token)@us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/ \
  cytognosis-yar
```

> **Note**: Delete collaborator SA keys when the project ends. Prefer signed URLs
> or direct dataset sharing (see data-hub.md) over giving collaborators registry access.

## Registry URLs Reference

| Registry | Type | URL |
|---|---|---|
| `cytognosis-compute` | Docker | `us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/` |
| `cytognosis-python` | Python | `us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/` |
| `cytognosis-website-v2` | Docker | `us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/` |
| `phi-services` | Docker | `us-central1-docker.pkg.dev/cytognosis-phi-prod/phi-services/` |
| `cytognosis-npm` (planned) | npm | `us-central1-npm.pkg.dev/cytognosis-infrastructure/cytognosis-npm/` |
