# Bundled Infrastructure & Modular Compute Plan

> Historical planning document. The architecture described below is now operational and is documented in the [Container Framework README](../../container_framework/README.md) and the [Deployment Walkthrough](deployment_walkthrough.md). This page is preserved as the original strategy record.

## Goal

Restructure Cytognosis infrastructure into two tiers to optimize compute costs, increase deployment flexibility, and support scaling Data Science / MLOps efforts:

1. **Core Services Bundle (always-on)** — a cost-optimized instance hosting lightweight, persistent services.
2. **Heavy Compute Nodes (on-demand)** — high-resource instances for heavy workloads, leveraging custom pre-packaged Docker images.

## Approved approach

Custom Docker images are pushed to the **GCP Artifact Registry** (private, IAM-protected) rather than to Docker Hub. The marginal storage / bandwidth cost is acceptable given the integrated IAM security and the fact that we only publish a small number of images.

## Final state (now realized)

### 1. Core services bundle

The original `cytohost` instance was re-architected as the **Core Node** running the [`core` stack](../../container_framework/configs/stacks/core.yaml):

- **Caddy** — reverse proxy with auto-HTTPS for every core subdomain.
- **Cal.com** — scheduling platform with PostgreSQL backend.
- **Excalidraw + Excalidraw Room** — collaborative whiteboard.
- **Mermaid Live Editor** — diagrams.
- **Logseq Web** — shared organizational knowledge base.
- **MLflow** — experiment-tracking server, with GCS as the default artifact root.

A separate **Zotero metadata** integration was originally planned in this bundle, but the [sovereign paper library architecture](../data-strategy/paper-library-architecture.md) replaced it: Zotero metadata syncs against Zotero's free cloud, and PDFs live on Google Drive. The `container_framework/configs/services/zotero.yaml` file is retained for the optional self-hosted-data-server path, but it is not part of the deployed `core` stack.

### 2. Heavy compute modules (Dockerized)

Built as focused images that can be deployed on-demand to heavy GCP instances or local developer machines via the [`research` stack](../../container_framework/configs/stacks/research.yaml):

- **Neo4j** — `container_framework/configs/services/neo4j.yaml`. Community Edition + APOC plugin. Sized for OLS4 ontology browsing and KG exploration.
- **Jupyter (Data Science)** — `container_framework/configs/services/jupyter.yaml`. Custom image (`cytognosis-compute/datascience:latest`) with Python, R, PyTorch, JAX, HuggingFace, and the MLflow client. Boots JupyterLab on port `8888`.
- **MLflow** — same image as the core bundle; included in the research stack so notebooks can log experiments to a co-located tracking server.

### 3. Artifact Registry layout

- **Project**: `cytognosis-infrastructure`
- **Registry repo**: `cytognosis-compute`
- **Region**: `us-central1`
- **Pull pattern**: `us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/<image>:<tag>`

CI builds and pushes are wired through GitHub Actions Workload Identity Federation (no long-lived JSON keys). See `.github/workflows/build-containers.yml`.

## Verification

- **Automated** — CI builds the `neo4j` and `datascience` images on every change to `compute_images/*` and verifies dependencies install cleanly.
- **Manual** — the [Deployment Walkthrough](deployment_walkthrough.md) records the live verification: 8 containers running on the Core Node behind Caddy, plus Neo4j on a dedicated research instance.

## Cross-references

- [Container Framework README](../../container_framework/README.md) — runtime architecture, `stack_manager.py` CLI.
- [Deployment Walkthrough](deployment_walkthrough.md) — what is currently running and where.
- [Cal.com Architecture](calcom_architecture.md) · [Logseq Knowledge Architecture](logseq_knowledge_architecture.md) · [MLflow Architecture](mlflow_architecture.md) · [Whiteboard / Mermaid Architecture](whiteboard_mermaid_architecture.md).
- [Sovereign Paper Library Architecture](../data-strategy/paper-library-architecture.md) — supersedes the originally planned self-hosted Zotero data server.
