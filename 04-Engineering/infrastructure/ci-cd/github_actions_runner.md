# GitHub Actions Self-Hosted Runner Setup

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `github-actions`, `ci-cd`, `self-hosted-runner`

**Last verified: 2026-06-14** — runner is installed on `cytohost` (`e2-highmem-2`, `us-central1-b`). The `research-stack-server` referenced below no longer exists; `cytohost` is the current runner host.

> [!IMPORTANT]
> The instance name in the commands below (`research-stack-server`) is stale. The current runner host is **`cytohost`** in zone `us-central1-b`. See [runner-setup.md](runner-setup.md) for the current operational configuration.

For heavy cross-platform deployments (such as compiling heavy Python modules and building Docker images), the self-hosted runner on `cytohost` (`e2-highmem-2`, 16 GB RAM) handles all CI workloads across the cytognosis org.

## Setting Up on `cytohost` (current — replaces `research-stack-server`)

1. **SSH into the GCP instance:**
```bash
gcloud compute ssh cytohost --project cytognosis-infrastructure --zone us-central1-b
```

2. **Download the GitHub Actions Runner payload:**
Follow the latest runner installation steps from your Repo Settings → Actions → Runners → "New self-hosted runner".
Typically, this looks like:
```bash
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.316.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz
```

3. **Configure the runner:**
```bash
# Add the labels 'self-hosted' and 'linux' to map exactly to the release workflow.
./config.sh --url https://github.com/cytognosis/Yar --token <YOUR_RUNNER_REGISTRATION_TOKEN> --labels linux,self-hosted
```

4. **Install as a Persistent Service:**
To ensure the runner survives server restarts:
```bash
sudo ./svc.sh install
sudo ./svc.sh start
```

## Configuring Target Workflows
Within our `.github/workflows/`, any workload bound for this heavy-duty machine must target `runs-on: [self-hosted, linux]`.

If setting this up for a newly consolidated server, please ensure all system dependencies required for builds are installed via `apt` (e.g., `clang`, `cmake`, `ninja-build`).
