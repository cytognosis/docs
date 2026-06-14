# Self-Hosted Runner Setup (ARM64)

## Current State

The GitHub Actions self-hosted runner runs on `cytohost` (or its ARM successor).
It provides the `[self-hosted, linux, arm64]` label for jobs that need:
- Access to GCP APIs without internet egress charges
- Docker builds with GCP Artifact Registry auth via ADC
- ARM64 native builds for the ARM-based host

**Runner status**: Re-register after each node migration (ARM runner binary required).

## Registration Steps (post-ARM migration)

```bash
# SSH into cytohost (t2a-standard-2, us-central1-b)
gcloud compute ssh cytohost --zone=us-central1-b --project=cytognosis-infrastructure

# Create runner directory
mkdir -p ~/actions-runner && cd ~/actions-runner

# Download ARM64 runner binary (check latest at github.com/actions/runner/releases)
curl -o actions-runner-linux-arm64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-arm64-2.319.1.tar.gz
tar xzf ./actions-runner-linux-arm64.tar.gz

# Generate registration token (expires in 1hr — do this right before ./config.sh)
# Go to: https://github.com/organizations/cytognosis/settings/actions/runners/new
# Copy the token shown

# Configure for the org (not a single repo)
./config.sh \
  --url https://github.com/cytognosis \
  --token <TOKEN_FROM_GITHUB> \
  --name cytohost \
  --labels "self-hosted,linux,arm64" \
  --runnergroup Default \
  --unattended

# Install as systemd service (persists across reboots)
sudo ./svc.sh install
sudo ./svc.sh start
sudo systemctl status actions.runner.cytognosis.cytohost
```

## Using the Runner in Workflows

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, arm64]
    steps:
      - uses: actions/checkout@v4
      # ... rest of job
```

For jobs that must run on GitHub-hosted runners (e.g., macOS builds):
```yaml
jobs:
  build:
    runs-on: ubuntu-latest   # GitHub-hosted fallback
```

## Runner Maintenance

```bash
# Check runner status
sudo systemctl status actions.runner.cytognosis.cytohost

# View logs
sudo journalctl -u actions.runner.cytognosis.cytohost -f

# Update runner binary
sudo ./svc.sh stop
./config.sh remove --token <TOKEN>
# re-download new binary, re-run config.sh + svc.sh install/start

# If node is replaced: deregister old runner first
# GitHub org settings → Actions → Runners → delete stale entry
```

## ADC (Application Default Credentials) on the Runner

The runner node uses its Compute Engine service account for ADC. Since we disabled
the default compute SA, any workflow using `gcloud` or GCP SDKs on the self-hosted
runner must either:

1. **Use OIDC in the workflow** (recommended — same as GitHub-hosted)
2. **Attach a dedicated SA to the node** at instance creation time:

```bash
# When creating the instance, attach website-deployer SA
gcloud compute instances create cytohost \
  --service-account=website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com \
  --scopes=cloud-platform \
  --zone=us-central1-b
```

Option 1 (OIDC in workflow) is preferred — it works identically on both self-hosted
and GitHub-hosted runners and doesn't require the node to have a SA attached.
