# Internal Python Package Registry (cytognosis-python)

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `artifact-registry`, `python`, `pypi`, `packages`

**Last verified: 2026-06-14** — `cytognosis-python` registry confirmed in `cytognosis-infrastructure`, `us-central1`, 4.425 MB.

## Overview

Cytognosis maintains a private Python package registry in **GCP Artifact Registry**.
Internal packages (e.g., `cytognosis-yar`, shared utilities) are published here
instead of public PyPI.

| Field | Value |
|---|---|
| Registry name | `cytognosis-python` |
| Project | `cytognosis-infrastructure` |
| Region | `us-central1` |
| Format | Python (PEP 503 simple index) |
| Simple index URL | `https://us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/` |
| Upload URL | `https://us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/` |

## Installing from the Registry

### uv (recommended)

```toml
# pyproject.toml — add to all projects using internal packages
[[tool.uv.index]]
name = "cytognosis"
url = "https://us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/"

# Install alongside public PyPI packages normally
# uv add cytognosis-yar
```

Authentication is handled automatically via `gcloud auth login` (local) or
OIDC/ADC (CI/CD). No `.netrc` or token files needed.

### pip

```bash
pip install --extra-index-url \
  https://oauth2accesstoken:$(gcloud auth print-access-token)@us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/ \
  cytognosis-yar
```

## Publishing a Package

### From CI (GitHub Actions — uses website-deployer OIDC)

```yaml
- uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
    service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"

- name: Build and publish
  run: |
    uv build
    uv publish \
      --index-url https://us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/ \
      --username=oauth2accesstoken \
      --password=$(gcloud auth print-access-token)
```

### From local

```bash
# Authenticate
gcloud auth login

# Build
uv build

# Publish
uv publish \
  --index-url https://us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/ \
  --username=oauth2accesstoken \
  --password=$(gcloud auth print-access-token)
```

## npm Registry (Planned)

When `cytoskills` revision is complete, create the npm registry:

```bash
gcloud artifacts repositories create cytognosis-npm \
  --repository-format=npm \
  --location=us-central1 \
  --project=cytognosis-infrastructure \
  --description="Cytognosis internal npm packages"
```

Publish URL: `https://us-central1-npm.pkg.dev/cytognosis-infrastructure/cytognosis-npm/`

See [registry-auth.md](registry-auth.md) for auth patterns.
