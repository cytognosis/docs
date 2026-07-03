# MLOps & Infrastructure Architecture Evaluation

> **Status**: Historical evaluation — MLflow now deployed on cytohost.
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `mlflow`, `mlops`, `self-hosted`, `compute`

**Last verified: 2026-06-19** — MLflow runs on `cytohost` (`e2-highmem-2`, `us-central1-b`) as part of the core stack. Artifact bucket is `gs://cytognosis-artifacts` (unified, created 2026-06-19; MLflow uses the `/mlflow/` prefix). The former `gs://cytognosis-mlflow-artifacts` was merged into this unified bucket. The `e2-micro`/`e2-small` options and dynamic spin-up approach described below were evaluated but not chosen; the consolidated cytohost architecture was the outcome.

Based on earlier work to optimize instance resources and evaluate MLOps platforms, here is the assessment and proposed architecture for Cytognosis Foundation.

---

## 🏗️ 1. Infrastructure Split: Zotero vs. Neo4j

You correctly identified that keeping a heavy instance running continuously when only lightweight tools need 24/7 access is inefficient.

### Proposed Architecture

**Service A: Zotero Dataserver (Always-On/Lightweight)**
- **Resource Needs:** Extremely low. It just synchronizes text metadata (SQL queries).
- **Setup:** Isolate Zotero onto an `e2-micro` or `e2-small` instance.
- **Availability:** Run 24/7 (or 24/5) so researchers never face sync errors when updating their libraries. Because it's a micro-instance, 24/7 costs are negligible (~$5-$10/month).

**Service B: Neo4j & Data Science Tools (Heavy/On-Demand)**
- **Resource Needs:** High memory/CPU (`e2-standard-4` to `n2-highmem-8`).
- **Setup:** Continue using Docker Compose on a dedicated heavy instance with a persistent mounted disk for the graph database.
- **Dynamic Spin-Up Strategy:**
  1. **User-Triggered:** Create a lightweight internal Slack bot or a simple Google Apps Script button ("Start Neo4j Server") that triggers a GCP Cloud Function to run `gcloud compute instances start`.
  2. **Auto-Shutdown:** Deploy a lightweight cron script inside the Neo4j instance that monitors CPU/Network idle time. If no active queries execute for 2 hours, the instance automatically shuts itself down (`sudo shutdown -h now`).
  3. **Result:** You only pay for the heavy 16GB-32GB RAM instances precisely when graph algorithms or heavy computations are running.

---

## 🤖 2. MLOps Platform Evaluation

Evaluating MLflow, Kubeflow, and Weights & Biases (W&B) for self-hosting at Cytognosis, weighing ease of installation, pricing, and organizational fit.

### 🥇 MLflow
**Best Fit: Baseline Experiment Tracking & Easy Self-Hosting**
- **Ease of Installation:** Extremely easy. A robust production setup simply requires running the open-source MLflow Docker container, linking it to a PostgreSQL database (like our Neo4j stack), and pointing the artifact store to a Google Cloud Storage (GCS) bucket.
- **Pricing:** 100% Free and Open Source.
- **Organizational Fit:** Highly recommended as your starting MLOps tool. It is framework-agnostic, excellent for standardizing how the team tracks hyperparameter tuning, and seamless to maintain on a basic GCP VM.

### 🥈 Weights & Biases (W&B) Self-Hosted
**Best Fit: Deep Learning/LLMs (If budget permits)**
- **Ease of Installation:** Medium/Hard. They offer a local Docker image, but production self-hosting heavily recommends a Kubernetes (K8s) cluster using their Helm charts, adding infrastructure complexity.
- **Pricing:** Very Expensive / Custom. While W&B has a "Free Self-Hosted" tier, it is **strictly limited to personal use**. Corporate self-hosting requires the Advanced Enterprise tier, forcing you to engage sales (quotes range from $150-$300+ per user/month, primarily targeting massive enterprises with IP compliance needs).
- **Organizational Fit:** W&B offers the absolute best UI and experiment visualization on the market, especially for LLMs. However, the commercial licensing constraints on the self-hosted version make it difficult to justify unless the organization is heavily funded specifically for AI model training.

### 🥉 Kubeflow
**Best Fit: Kubernetes-Native Enterprises**
- **Ease of Installation:** Extremely Difficult. Kubeflow is not just an application; it is an operating system for ML on top of Kubernetes. It requires deep K8s expertise, complex manifests, and a minimum of cluster footprint (e.g., 4+ CPUs, 16GB+ RAM just for the control plane).
- **Pricing:** 100% Free and Open Source.
- **Organizational Fit:** Not recommended at this stage unless Cytognosis already utilizes Google Kubernetes Engine (GKE) for all infrastructure. The total cost of ownership comes from the dedicated DevOps headcount required simply to keep the Kubeflow cluster running and upgraded.

---

## 🐋 3. Container Runtime Evaluation: Podman & Toolbx vs. Docker

As we shift toward modular, containerized heavy compute nodes (Neo4j, Data Science integrations), evaluating the underlying container runtime is critical for security and resource efficiency.

### Podman (Daemonless Container Engine)
**Best Fit: Secure, Resource-Constrained Environments**
- **Architecture:** Unlike Docker, which relies on a heavy, central background daemon (`dockerd`) running as root, **Podman is daemonless** and operates using a fork-exec model. 
- **Security:** Podman's default support for **rootless containers** is a massive advantage for multi-tenant data science environments. If a data scientist runs a compromised container, the attacker only gains user-level privileges, not root access to the GCP host VM.
- **Resource Usage:** Given our new `e2-small` Core Bundle architecture, Podman's lack of a persistent background daemon means a significantly lower idle memory footprint compared to Docker.
- **Compatibility:** Podman offers a nearly identical CLI to Docker (`alias docker=podman`). Your researchers will not need to learn new commands to spin up the Jupyter or Neo4j images from the Artifact Registry.

### Containertoolbx (Toolbx)
**Best Fit: Interactive Data Science Workspaces**
- **Functionality:** Built on top of Podman, Toolbx creates interactive command-line environments. It bridges the gap between full container isolation and local development comfort.
- **Organizational Fit:** Highly recommended for your Data Science team. Toolbx allows a researcher to spin up a container (e.g., loaded with CUDA, PyTorch, and R) that transparently mounts their host `home` directory, networking, and GPU sockets. 
- **Advantage:** A researcher can maintain 5 different Toolbx environments for 5 different ML projects without polluting their primary operating system (or the underlying GCP Spot Instance OS) with conflicting python dependencies, while still interacting with the system as if everything was installed locally.

---

## 🎯 Next Steps & Conclusion
1. **Infrastructure:** We can restructure the current monolithic `research-stack-server` by migrating Zotero to an isolated `e2-micro`, and implement the on-demand idle-shutdown scripts for Neo4j.
2. **MLOps:** I highly recommend proceeding with **MLflow**. We can easily fold an `mlflow-server` Docker container into your existing data science infrastructure stack, utilizing GCS for robust, cheap artifact storage.
3. **Container Runtime:** I strongly suggest adopting **Podman** as the default engine on the GCP Heavy Compute instances, dropping Docker. We should also encourage the internal ML team to utilize **Toolbx** for their interactive development spaces to keep the underlying compute instances clean.
