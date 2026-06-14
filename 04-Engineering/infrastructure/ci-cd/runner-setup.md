> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `ci-cd`, `github-actions`, `runner`, `cytohost`
> **Last verified**: 2026-06-14 against gcloud

# Self-Hosted Runner Setup

## BLUF

The GitHub Actions self-hosted runner runs on `cytohost` (`e2-highmem-2`, x86\_64, us-central1-b). Runner labels: `[self-hosted, linux, X64, cytohost]`. The default compute SA is disabled — workflows must use OIDC for GCP access.

---

## Current State

| Field | Value |
|---|---|
| Host | `cytohost` |
| Machine type | `e2-highmem-2` (x86\_64) — NOT ARM64 |
| Zone | us-central1-b |
| Runner labels | `self-hosted`, `linux`, `X64`, `cytohost` |
| Scope | org-level (cytognosis) |
| Runner group | Default |

> [!WARNING]
> All prior documentation referencing `arm64` runner labels, ARM64 binaries, or `t2a-standard-2` for this runner is stale and incorrect. cytohost is x86\_64.

---

## Registration Steps

```bash
# SSH into cytohost
gcloud compute ssh cytohost --zone=us-central1-b --project=cytognosis-infrastructure --tunnel-through-iap

# Create runner directory
mkdir -p ~/actions-runner && cd ~/actions-runner

# Download x86_64 runner binary (check latest: github.com/actions/runner/releases)
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-x64-2.319.1.tar.gz
tar xzf ./actions-runner-linux-x64.tar.gz

# Generate registration token (expires in 1hr — do this right before ./config.sh)
# Go to: https://github.com/organizations/cytognosis/settings/actions/runners/new
# Copy the token shown

# Configure for the org
./config.sh \
  --url https://github.com/cytognosis \
  --token <TOKEN_FROM_GITHUB> \
  --name cytohost \
  --labels "self-hosted,linux,X64,cytohost" \
  --runnergroup Default \
  --unattended

# Install as systemd service
sudo ./svc.sh install
sudo ./svc.sh start
sudo systemctl status actions.runner.cytognosis.cytohost
```

---

## Using the Runner in Workflows

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, X64, cytohost]
    steps:
      - uses: actions/checkout@v4
      # ... rest of job
```

For jobs that must run on GitHub-hosted runners:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

---

## GCP Authentication on the Runner

The default compute SA on cytohost is intentionally disabled. Any workflow using `gcloud` or GCP SDKs on the self-hosted runner **must** use OIDC — same as GitHub-hosted runners.

```yaml
# Required in any workflow needing GCP access
permissions:
  contents: read
  id-token: write

steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
      service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"
```

Do not attempt to use Application Default Credentials from the runner's attached SA — it is disabled and will fail.

---

## Runner Maintenance

```bash
# Check runner status
sudo systemctl status actions.runner.cytognosis.cytohost

# View logs
sudo journalctl -u actions.runner.cytognosis.cytohost -f

# Update runner binary
sudo ./svc.sh stop
./config.sh remove --token <TOKEN>
# Re-download new x64 binary, re-run config.sh + svc.sh install/start

# If node is replaced: deregister old runner first
# GitHub org settings → Actions → Runners → delete stale entry
```

---

## Cross-References

| Document | Relationship |
|---|---|
| [Compute: Node Types](../compute/node-types.md) | cytohost hardware specs |
| [CI/CD: OIDC Federation](oidc-federation.md) | WIF setup detail |
| [CI/CD: Website Deployment](website-deployment.md) | Example workflow using OIDC |
