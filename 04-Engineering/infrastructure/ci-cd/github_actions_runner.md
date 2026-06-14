# GitHub Actions Self-Hosted Runner Setup

Since we are running heavy cross-platform deployments (such as `flutter build linux` and compiling heavy Python modules), moving our heavy workload runners to our high-compute GCP infrastructure (`research-stack-server`, `e2-standard-4`) will yield faster builds and significantly reduce GitHub Action minute usage limits.

## Setting Up on `research-stack-server`

1. **SSH into the GCP instance:**
```bash
gcloud compute ssh research-stack-server --project cytognosis-infrastructure --zone us-central1-a
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
