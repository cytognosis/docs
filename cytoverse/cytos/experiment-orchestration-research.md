---
title: "Experiment Orchestration: Definition, Execution, and Provenance"
date: "2026-05-25"
source: "migrated from org/plans"
category: "research"
status: "current"
tags:
  - cytognosis
  - research
---

# Experiment Orchestration: Definition, Execution, and Provenance

**Cytognosis Foundation, 2026-05-24 (draft v0.1)**
**Status**: Research complete, ready for architectural decisions

> This document is the comprehensive research companion to the [Reproducibility Strategy](file:///home/mohammadi/Documents/Claude/Projects/Infrastructure%20and%20Tooling/cytognosis_reproducibility_strategy.md) (§7 Provenance, §9 Happy Path) and the [RO-Crate Research](file:///home/mohammadi/repos/cytognosis/org/plans/experiment-rocrate-research.md). It covers how experiments are defined, executed on heterogeneous compute, and how provenance flows automatically from definition through execution to publication.

---

## Table of Contents

1. [Experiment Definition: RO-Crate + ISA](#1-experiment-definition-ro-crate--isa)
2. [Experiment Execution Layer](#2-experiment-execution-layer)
3. [Compute Environment Management](#3-compute-environment-management)
4. [Provenance Tracking](#4-provenance-tracking)
5. [Integration Architecture](#5-integration-architecture)
6. [Recommendations and Decisions](#6-recommendations-and-decisions)
7. [Open Questions](#7-open-questions)

---

## 1. Experiment Definition: RO-Crate + ISA

### 1.1 The Problem

Cytognosis runs diverse experiment types: knowledge graph builds, model training runs, data curation pipelines, schema validation runs, sensor data acquisition batches, and genomic analyses. Each has distinct inputs, outputs, parameters, and success criteria. Without a unified experiment description language, each team invents its own config format, making cross-experiment comparison, provenance linking, and FAIR publication impossible.

The Reproducibility Strategy (§4) commits to LinkML as the hub schema language and RO-Crate as the packaging format. This section specifies how experiments are described using the ISA Abstract Model, serialized as ISA-JSON, and packaged as RO-Crate.

### 1.2 RO-Crate Profile Hierarchy

The Workflow Run RO-Crate (WRROC) specification provides three hierarchical profiles for capturing computational provenance with increasing granularity:

| Profile | Specification URI | Granularity | Schema.org Core Type | Cytognosis Use |
|---------|-------------------|-------------|---------------------|----------------|
| **Process Run Crate** | `wfrun/process/0.4` | Single tool execution | `CreateAction` | Env locks, Docker builds, source downloads (implemented in `assets/manifest.py`) |
| **Workflow Run Crate** | `wfrun/workflow/0.4` | Full pipeline orchestration | `CreateAction` + `ComputerLanguage` | KG snapshots, training pipelines (implemented in `publish/rocrate.py`) |
| **Provenance Run Crate** | `wfrun/provenance/0.4` | Per-step internal detail | Nested `CreateAction` | Detailed training runs with per-step provenance (implemented in `publish/rocrate.py`) |
| **Workflow Testing RO-Crate** | `wfrun/test/0.1` | Test suite results | `TestAction` | CI/CD validation (not yet implemented) |

**Key WRROC concepts:**

- **Process Run Crate** is the foundational profile. It describes the execution of one or more software tools using `CreateAction`, even without a formal top-level workflow. It specifies how to represent the software, the execution, and associated inputs/outputs.
- **Workflow Run Crate** extends both Process Run Crate and Workflow RO-Crate profile. It describes computation orchestrated by a formal computational workflow, linking execution to the workflow definition and tracking parameter inputs and outputs.
- **Provenance Run Crate** is the most detailed profile. It extends Workflow Run Crate to include internal workflow execution details: individual tool executions, intermediate outputs, and specific step parameters.

WRROC aligns with W3C PROV and Schema.org to ensure interoperability across heterogeneous workflow management systems. The profiles are designed to be machine-actionable, enabling automated validation, comparison, and federation across workflow registries.

**Existing Cytognosis implementation:**

| File | Module | What It Does |
|------|--------|-------------|
| `cytoskeleton/assets/manifest.py` | cytoskeleton | Emits WRROC Process Run Crate fragments for env locks and Docker builds. No `ro-crate-py` dependency. Uses SWHID identifiers via `identity/swhid.py`. |
| `cytoskeleton/store/manifest.py` | cytoskeleton | `StoreManifest` dataclass + root `ro-crate-metadata.json` writer for asset stores. |
| `cytoskeleton/vfs/provenance.py` | cytoskeleton | W3C PROV-J compatible provenance tracking. Every VFS write gets a `.prov.json` sidecar recording who, when, from what git context, and derivation chain. |
| `cytos/publish/rocrate.py` | cytos | 471-line module using `ro-crate-py`. Three functions: source crate, snapshot crate, training run crate. |
| `cytos/pipelines/data_engineering/rocrate.py` | cytos | KG-level RO-Crate generator (raw JSON-LD). |

### 1.3 ISA Abstract Model as Experiment Description Language

The ISA (Investigation, Study, Assay) abstract model is the community standard for describing experimental metadata in the life sciences. It provides a three-tier hierarchy:

| ISA Entity | Purpose | Cytognosis Mapping |
|-----------|---------|-------------------|
| **Investigation** | Top-level project context: goals, publications, contacts | Cytognosis research programme (e.g., "Cytoscope Biomarkers") |
| **Study** | A specific unit of research with one or more assays | A specific experiment campaign (e.g., "HRV Predictive Models") |
| **Assay** | An analytical measurement or test performed on samples | A single experiment run (e.g., "LSTM Training v2.1") |

**ISA serialization formats:**

- **ISA-Tab**: Tabular (TSV) format, historically common for researchers to store and exchange metadata.
- **ISA-JSON**: JSON-based format implementing the same model, designed for machine consumption, programmatic manipulation, and integration into modern data pipelines. Documents adhere to JSON Schemas (e.g., `investigation_schema.json`).

**Why ISA for Cytognosis:**

1. ISA covers the full experiment lifecycle, not just ML training runs.
2. ISA-JSON maps cleanly to LinkML schemas via `class_uri` to `schema:*` types.
3. The FAIRDOM/SEEK ecosystem provides free federation for ISA-structured experiments.
4. RO-Crate profiles can wrap ISA-JSON as the experiment descriptor.
5. ISA is already supported by WorkflowHub, SEEK, and the broader FAIR ecosystem.

### 1.4 LinkML → ISA Mapping

The Reproducibility Strategy (§4) established LinkML as the canonical schema language. Here is how our LinkML classes map to ISA entities:

| LinkML Class | ISA Entity | Schema.org Type | Notes |
|-------------|-----------|-----------------|-------|
| `ExperimentCampaign` | `Investigation` | `schema:ResearchProject` | Top-level grouping |
| `ExperimentSeries` | `Study` | `schema:Dataset` | Series of related runs |
| `ExperimentRun` | `Assay` | `schema:CreateAction` | Single execution |
| `DatasetManifest` | `Source/Sample` | `schema:Dataset` | Input data description |
| `ProvenanceRecord` | `Process` | `schema:Action` | Processing step |
| `ScholarlyResource` | `Publication` | `schema:ScholarlyArticle` | Linked publications |
| `MLModel` | `DataFile` | `schema:SoftwareApplication` | Model checkpoint |

The mapping leverages the `class_uri` field in LinkML to assign Schema.org types, ensuring that LinkML-defined entities can be serialized as both ISA-JSON and RO-Crate JSON-LD without information loss.

### 1.5 FAIR-Compliant Resource Descriptions

Every experiment input must be described with sufficient metadata for independent reproduction:

| Resource Type | Identifier Scheme | Resolution | Example |
|--------------|-------------------|------------|---------|
| Code | SWHID (ISO 18670:2025) | Software Heritage Archive | `swh:1:rev:2c79bff0a06...` |
| Data | SHA-256 / DVC MD5 | VFS driver chain | `sha256:f5bf89d001...` |
| Models | HuggingFace ref / SWHID | HF Hub / VFS | `hf:cytognosis/cytoscope-base@a1b2c3d` |
| Docker images | OCI digest | Container registry | `ghcr.io/cytognosis/ml@sha256:...` |
| Environments | Lockfile hash | cytoskeleton VFS | `cytognosis://locked/ml.cuda@v2.1.0` |
| Schemas | URI + version | w3id.org / cytoskeleton store | `https://w3id.org/cytognosis/schema/v0.4.0` |
| Publications | DOI | DOI.org / Zenodo | `doi:10.5281/zenodo.12345` |

The cytoskeleton VFS (`vfs/base.py`) already provides a backend-agnostic `AssetStat` that includes SWHID identifiers computed on `put()`. The provenance system (`vfs/provenance.py`) writes W3C PROV-J sidecars alongside every asset, recording the git context, derivation chain, and timestamps.

---

## 2. Experiment Execution Layer

### 2.1 Evaluation Criteria

Each execution engine is evaluated against:

1. **Compute abstraction**: How does it represent and schedule computational tasks?
2. **Environment management**: How does it handle Docker, Conda, virtual environments?
3. **GPU scheduling**: Can it request, allocate, and manage GPU resources?
4. **Cost model**: Pay-per-use vs. reserved, serverless vs. managed?
5. **Provenance**: Does it emit machine-readable provenance (RO-Crate, W3C PROV)?
6. **Incremental execution**: Can it skip unchanged tasks?
7. **Multi-backend**: Can it run on local, HPC, and cloud?
8. **Cytognosis fit**: How well does it integrate with our existing stack?

### 2.2 Execution Engine Comparison

#### redun (Already Used by Cytognosis)

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Pure Python tasks with lazy expressions. Scheduler evaluates to DAG dynamically via graph reduction. Supports Common Subexpression Elimination (CSE). |
| **Environment management** | Executes within any Python environment. Docker via custom executors. No built-in container orchestration. |
| **GPU scheduling** | No native GPU awareness. Relies on underlying infrastructure (SLURM, K8s). |
| **Cost** | Free, open-source (Apache-2.0). Infrastructure costs depend on backend. |
| **Provenance** | Content-addressed caching using `eval_hash` → `value_hash` mapping. Call Graphs recorded to database (SQLite/Postgres). Tracks both data and code changes via AST hashing. |
| **Incremental** | Excellent. Hashes individual Python functions and data to detect changes. Reuses intermediate results across workflows. |
| **Multi-backend** | Local, AWS Batch, SLURM. GCP support via custom executors. |
| **Cytognosis fit** | Already in `pyproject.toml`. Pure Python, matches our stack. Needs `redun-rocrate` plugin to emit WRROC from Call Graphs. |

**Key strengths:**
- Lazy expressions and graph reduction provide the most natural Python workflow authoring experience.
- Content-addressed caching is deeply integrated, tracking file hashes (path, size, mtime triplet) and function AST hashes.
- Every execution creates a durable Call Graph for provenance replay.

**Key gaps:**
- No native RO-Crate emission (critical gap, solvable via plugin).
- No built-in GPU scheduling.
- Limited cloud backend ecosystem compared to Nextflow.

#### Nextflow + nf-core

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Dataflow programming with channels. Groovy DSL for process definitions. |
| **Environment management** | First-class: Docker, Singularity/Apptainer, Conda. Per-process container directives. |
| **GPU scheduling** | `accelerator` directive for GPU requests. Supports SLURM GPU partitions, cloud GPU instances. |
| **Cost** | Free, open-source (Apache-2.0). Seqera Platform (commercial) for enterprise features. |
| **Provenance** | `nf-prov` plugin (v1.4+) emits Workflow Run RO-Crate natively. |
| **Incremental** | Cached processes via `-resume`. Work directory hash-based. |
| **Multi-backend** | Excellent: local, SLURM, PBS, LSF, SGE, AWS Batch, Google Cloud Life Sciences, Azure Batch, Kubernetes. |
| **Cytognosis fit** | Gold standard for bioinformatics. nf-core community provides 100+ validated pipelines. Native WRROC emission is a major advantage. |

**Key strengths:**
- Native WRROC provenance via `nf-prov` plugin, no custom development needed.
- Best-in-class multi-backend support ("write once, run anywhere").
- nf-core ecosystem provides production-quality bioinformatics pipelines.
- Declarative GPU resource specification per process.

**Key gaps:**
- Groovy DSL is unfamiliar to Python-centric data science teams.
- Overkill for simple ML training runs.
- nf-core pipelines are bioinformatics-focused, not ML-focused.

#### Kubeflow Pipelines

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | DAG-based orchestrator built on Kubernetes (Argo Workflows). Each step is a containerized pod. |
| **Environment management** | Kubernetes-native. Each step runs in its own container image. |
| **GPU scheduling** | Kubernetes scheduler with Volcano or Kueue. GPU node affinity, taints, tolerations. High control but requires platform engineering. |
| **Cost** | Free, open-source. Requires K8s cluster (GKE, EKS, etc.). |
| **Provenance** | ML Metadata (MLMD) store. No native RO-Crate support. |
| **Incremental** | Task caching via Argo. |
| **Multi-backend** | Kubernetes only (but K8s runs anywhere). |
| **Cytognosis fit** | Heavy operational overhead. Best for enterprise K8s standardization. Overkill for a small team. |

#### Ray (Train, Serve, Tune)

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Unified Python framework with actor-based, fine-grained tasks. `@ray.remote` to scale across CPUs and GPUs without distributed systems code. |
| **Environment management** | Ray runtime. Docker via KubeRay on Kubernetes. |
| **GPU scheduling** | Ray-native internal scheduler optimized for low-latency NCCL/distributed PyTorch communication. Superior for distributed training. |
| **Cost** | Free, open-source. Anyscale (commercial) for managed Ray. |
| **Provenance** | No native provenance. Integrates with MLflow/W&B for tracking. |
| **Incremental** | No native caching at the workflow level. |
| **Multi-backend** | Local, Kubernetes (KubeRay), SLURM (via ray-on-slurm). |
| **Cytognosis fit** | Best choice for distributed training workloads. Not a workflow orchestrator, but excellent as the compute runtime within redun/Nextflow orchestrated pipelines. |

**Key strengths:**
- Ray Train simplifies distributed model training (PyTorch, TensorFlow) by abstracting multi-node communication (DDP, DeepSpeed).
- Ray Serve enables scalable model serving with complex inference pipelines and dynamic batching.
- Unified framework: Ray Data (preprocessing) → Ray Tune (HPO) → Ray Train (training) → Ray Serve (serving).

#### Dask / Dask-CUDA

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Task-graph based (DAGs). Parallel computing extending Pandas/NumPy APIs. |
| **Environment management** | Python environments. Dask-distributed workers. |
| **GPU scheduling** | Dask-CUDA provides GPU-accelerated DataFrames (cuDF). |
| **Cost** | Free, open-source. Coiled (commercial) for managed Dask. |
| **Provenance** | No native provenance tracking. |
| **Incremental** | Lazy evaluation, but no persistent caching across runs. |
| **Multi-backend** | Local, SLURM, Kubernetes, cloud (via Dask Gateway). |
| **Cytognosis fit** | Best for data-centric parallelism (scaling Pandas/NumPy). More lightweight than Ray but lacks specialized ML libraries. Good for preprocessing stages. |

#### SLURM

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | HPC job scheduler / resource manager. Batch-job and MPI-based. |
| **Environment management** | Module system, Singularity/Apptainer containers. |
| **GPU scheduling** | Excellent: gang scheduling (all nodes start simultaneously), fair-share resource management, `--gres=gpu:N` directives. |
| **Cost** | Free, open-source. Requires dedicated HPC infrastructure. |
| **Provenance** | Job accounting logs only. No structured provenance. |
| **Incremental** | None. Each job is independent. |
| **Multi-backend** | HPC clusters only. |
| **Cytognosis fit** | Infrastructure layer, not a workflow engine. Run redun/Ray on top of SLURM for distributed training on HPC. |

**Key role:** SLURM manages nodes, GPU allocation, and queueing. A common pattern is submitting a SLURM job to allocate nodes, then launching a Ray cluster within that allocation. SLURM remains dominant in research HPC due to robust batch workload handling and simpler script-based job submission.

#### Cloud Run Jobs (GCP)

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Serverless, run-to-completion containerized tasks. |
| **Environment management** | Docker containers only. |
| **GPU scheduling** | GPU support via NVIDIA L4/T4 instances. Limited compared to GKE. |
| **Cost** | Pay-per-use (100ms increments). Generous free tier. Scale to zero. |
| **Provenance** | None. Basic job logs only. |
| **Incremental** | None. |
| **Multi-backend** | GCP only. |
| **Cytognosis fit** | Ideal for lightweight batch tasks: data transformations, simple inference, post-training tasks. Not suitable for complex ML pipelines. Cost-effective for intermittent workloads. |

#### Vertex AI Pipelines (GCP)

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Managed DAG-based orchestrator using Kubeflow Pipelines SDK. Serverless/managed cloud. |
| **Environment management** | Managed containers. Vertex AI handles provisioning, scaling, cleanup. |
| **GPU scheduling** | Cloud-managed: define machine type, GPU/TPU in pipeline config. Vertex AI handles provisioning. |
| **Cost** | Pay-per-use (compute-hour + platform fees). Spot VMs for cost reduction. Higher overhead than Cloud Run due to platform features. |
| **Provenance** | Vertex AI Metadata. ML artifact tracking. No native RO-Crate. |
| **Incremental** | Pipeline caching. |
| **Multi-backend** | GCP only. |
| **Cytognosis fit** | Path of least resistance for GCP-native teams. Good for complex multi-step ML pipelines. Automated experiment tracking and model registry. |

#### Snakemake (8.x/9.x)

| Dimension | Assessment |
|-----------|-----------|
| **Compute abstraction** | Python-based DSL. File-based, rule-oriented execution model. |
| **Environment management** | Conda, Docker, Singularity/Apptainer. Per-rule environments. |
| **GPU scheduling** | GPU resource allocation within rules. Requires more manual configuration than Nextflow. |
| **Cost** | Free, open-source (MIT). |
| **Provenance** | Workflow reports with DAG visualization. No native RO-Crate support (unlike Nextflow's nf-prov). |
| **Incremental** | File timestamp-based. Rebuilds only changed targets. |
| **Multi-backend** | Local, SLURM, cloud (plugin architecture in 8.x/9.x). Pluggable execution backends. |
| **Cytognosis fit** | Strong alternative to Nextflow for Python-centric teams. Growing catalog but smaller ecosystem than nf-core. Better suited for academic/HPC environments. |

**Key differentiator vs. Nextflow:** Snakemake uses Python-based DSL (familiar to our team) vs. Nextflow's Groovy DSL. However, Nextflow has native WRROC provenance via nf-prov, a much larger community (nf-core), and superior cloud-native execution support.

### 2.3 Execution Engine Summary Matrix

| Engine | Compute Model | GPU Support | RO-Crate | Incremental | Multi-Backend | Cytognosis Fit |
|--------|--------------|-------------|----------|-------------|--------------|----------------|
| **redun** | Python DAG (lazy) | Via infra | Plugin needed | ★★★★★ | ★★★☆☆ | ★★★★★ (already used) |
| **Nextflow** | Dataflow channels | Native directive | Native (nf-prov) | ★★★★☆ | ★★★★★ | ★★★★☆ (bioinformatics) |
| **Kubeflow** | K8s pods (DAG) | K8s scheduler | None | ★★★☆☆ | ★★☆☆☆ (K8s only) | ★★☆☆☆ (heavy ops) |
| **Ray** | Actor/task (Python) | Native scheduler | None | ★☆☆☆☆ | ★★★☆☆ | ★★★★☆ (dist. training) |
| **Dask** | Task-graph (DAG) | Dask-CUDA | None | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ (preprocessing) |
| **SLURM** | Batch jobs | `--gres=gpu` | None | ☆☆☆☆☆ | ★☆☆☆☆ (HPC only) | ★★★☆☆ (infra layer) |
| **Cloud Run Jobs** | Serverless container | Limited | None | ☆☆☆☆☆ | ★☆☆☆☆ (GCP only) | ★★☆☆☆ (simple tasks) |
| **Vertex AI** | Managed DAG (KFP) | Cloud-managed | None | ★★★☆☆ | ★☆☆☆☆ (GCP only) | ★★★☆☆ (GCP ML) |
| **Snakemake** | Rule-based (Python) | Per-rule | None | ★★★★☆ | ★★★★☆ | ★★★☆☆ (alternative) |

---

## 3. Compute Environment Management

### 3.1 Cytoskeleton as the Environment Authority

The Reproducibility Strategy (§6) establishes cytoskeleton as the owner of all compute environments. cytoskeleton provides:

1. **Component YAML definitions** (`configs/components/`): Pixi-based component specifications defining dependencies.
2. **Environment compositions** (`configs/environments/`): Assemblies of components into complete environments (e.g., `ml.cuda`, `genomics.hpc`).
3. **Locked environments** (`locked/`): Fully resolved, deterministic lockfiles for every environment × platform matrix.
4. **Docker images** (`docker/`): Container images built from locked environments.
5. **SWHID identifiers**: Every artifact (lockfile, Dockerfile, image) gets a Software Heritage Identifier for immutable content-addressing.
6. **Process Run Crate fragments**: Every build operation emits a WRROC Process Run Crate fragment via `assets/manifest.py`.

### 3.2 Environment Lifecycle in Experiments

```
┌─────────────────────────────────────────────────────────────────┐
│                    Experiment Environment Flow                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Experiment config references environment:                    │
│     execution_environment: ml.cuda@v2.1.0                        │
│                                                                  │
│  2. cytoskeleton resolves the environment:                       │
│     - Fetch locked/ml.cuda.py313.lock from VFS                  │
│     - Validate lockfile hash against store manifest              │
│     - Record pull as CreateAction in Process Run Crate           │
│                                                                  │
│  3. Compute backend materializes the environment:                │
│     - Local: pixi install from lockfile                          │
│     - Docker: Pull ghcr.io/cytognosis/ml-cuda:v2.1.0            │
│     - Cloud: Specify container image in job config               │
│     - HPC: Singularity/Apptainer from Docker image               │
│                                                                  │
│  4. Execution runs within the locked environment                 │
│                                                                  │
│  5. Environment metadata embedded in output RO-Crate:            │
│     - SoftwareApplication entity with SWHID                      │
│     - Container digest (OCI sha256)                              │
│     - Lockfile reference                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Multi-Backend Abstraction

The execution layer must abstract the physical compute backend. The VFS (`vfs/base.py`) already provides backend-agnostic storage. We need an analogous abstraction for compute:

| Backend | Environment Materialization | GPU Access | Job Submission |
|---------|---------------------------|------------|----------------|
| **Local** | `pixi install` from lockfile or Docker container | Direct CUDA | Python subprocess |
| **Docker** | `docker run` with image from cytoskeleton | `--gpus all` | Docker CLI/API |
| **GCP (Cloud Run)** | Container image in job spec | GPU machine type | Cloud Run Jobs API |
| **GCP (Vertex AI)** | Container image in pipeline spec | Machine type + GPU count | Vertex AI SDK |
| **GCP (GKE/Ray)** | KubeRay cluster with container image | K8s GPU scheduling | KubeRay operator |
| **HPC (SLURM)** | Singularity/Apptainer from Docker image | `--gres=gpu:N` | `sbatch` script |

The `cytoskeleton run` command (proposed) would select the backend based on experiment config and available infrastructure, then delegate to the appropriate executor.

### 3.4 Cost Considerations

| Backend | Cost Model | GPU Cost (approx) | Idle Cost | Best For |
|---------|-----------|-------------------|-----------|----------|
| Local | Hardware amortization | $0 (existing) | N/A | Development, small experiments |
| Cloud Run Jobs | Pay-per-use (100ms) | ~$0.50/hr (L4) | $0 | Lightweight batch tasks |
| Vertex AI | Compute-hour + platform | ~$1.50/hr (L4) | $0 | Complex ML pipelines |
| GKE + Ray | Node-hour | ~$0.80/hr (L4) | Cluster idle cost | Distributed training |
| HPC (SLURM) | Allocated hours | $0 (grant-funded) | N/A | Academic compute grants |

**Recommendation:** Start with local + Docker for development. Use Cloud Run Jobs for lightweight batch tasks. Use Vertex AI or GKE + Ray for GPU training. Target HPC/SLURM for large-scale academic compute grants.

---

## 4. Provenance Tracking

### 4.1 The Provenance Problem

The Reproducibility Strategy (§7) identifies provenance as the critical gap. Provenance must be:

1. **Automated**: Captured inline during execution, not post-hoc.
2. **Layered**: Multiple systems can contribute provenance at different granularities.
3. **Standardized**: W3C PROV and RO-Crate for interoperability.
4. **Queryable**: Stored in a database for lineage queries and impact analysis.
5. **Publishable**: Emitted as FAIR-compliant RO-Crate for external consumption.

### 4.2 Provenance Tool Comparison

#### redun Provenance

- **Mechanism**: Content-addressed task caching with Call Graph recording. Every execution creates a durable Call Graph stored in SQLite or Postgres.
- **Granularity**: Per-task (function-level). Tracks input/output data hashes and code AST hashes.
- **Data reactivity**: Hashes in-memory values and external data sources. Files hashed via (path, size, mtime) triplet.
- **Code reactivity**: Hashes individual Python functions and compares against historical Call Graphs.
- **Queryable**: `redun log` CLI for browsing execution history. SQL backend for programmatic queries.
- **Gap**: No native RO-Crate emission. Call Graphs are redun-specific, not interoperable.

#### LaminDB Provenance

- **Mechanism**: Lineage-native data framework. Three core concepts: Artifacts, Transforms, Runs.
- **Artifacts**: Central registry for datasets and models (files, folders, `.h5ad`, `.zarr`, `.parquet`). Each artifact tracks creator, storage location, and the Run that created it.
- **Transforms**: Represent code/jobs (notebooks, scripts, functions, pipelines). Versioned, mapping transform version to source code version. Consistent with OpenLineage specification.
- **Runs**: Actual executions of a Transform. Each distinguished by time, user, input data, environment.
- **Automatic tracking**: `ln.track()` at the beginning of a notebook/script links subsequent artifact creation to the current run and transform.
- **Queryable**: Relational database (PostgreSQL/SQLite). `artifact.run`, `artifact.transform`, `run.input_artifacts` for lineage traversal.
- **Gap**: Not a workflow engine. Requires manual integration with execution layer. No native RO-Crate support.

#### DVC (Data Version Control)

- **Mechanism**: Git-based data and model versioning with pipeline tracking.
- **Data versioning**: `.dvc` files tracked by Git, pointing to large files in cloud storage (S3, GCS, Azure).
- **Pipeline management**: `dvc.yaml` defines reproducible stages (preprocess → train → evaluate).
- **Provenance**: DVC commit hash links to exact data + code version. Integrates with MLflow by storing DVC hash as MLflow parameter.
- **Incremental**: File hash-based. Only reruns changed stages.
- **Gap**: DVC owns data-to-training lineage. MLflow owns training-to-deployment lineage. Need both for full coverage.

#### MLflow

- **Mechanism**: Experiment tracking, model registry, deployment lifecycle.
- **Experiment tracking**: Records hyperparameters, metrics, artifacts during runs. Rich UI for comparison.
- **Model registry**: Central hub for model versions (staging, production tagging).
- **Cost**: Free, open-source. Platform-agnostic, no vendor lock-in.
- **Gap**: Limited for large dataset versioning (use DVC). Basic collaboration features. Requires manual infrastructure setup.

#### Weights & Biases (W&B)

- **Mechanism**: SaaS experiment tracking with best-in-class UI and collaboration.
- **Strengths**: Intuitive real-time dashboards. Excellent for team collaboration, sharing reports, visualizing performance.
- **Gap**: SaaS dependency (vendor lock-in concerns for a nonprofit). Data residency considerations. Cost at scale.

### 4.3 Provenance Architecture: Layered Approach

No single tool covers all provenance needs. The recommendation is a layered architecture:

```
┌────────────────────────────────────────────────────────────────┐
│                    Provenance Layer Stack                        │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 4: PUBLICATION                                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  RO-Crate (WRROC profiles)                               │    │
│  │  - Workflow Run Crate from redun-rocrate plugin           │    │
│  │  - Workflow Run Crate from nf-prov (Nextflow)             │    │
│  │  - Process Run Crate from cytoskeleton                    │    │
│  │  → Published to WorkflowHub, Zenodo, SEEK                 │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Layer 3: EXPERIMENT TRACKING                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  MLflow (self-hosted)                                     │    │
│  │  - Hyperparameters, metrics, artifacts                    │    │
│  │  - Model registry (staging/production)                    │    │
│  │  - Experiment comparison UI                               │    │
│  │  → Metadata wrapped into RO-Crate via mlflow-rocrate      │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Layer 2: ARTIFACT REGISTRY                                      │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  LaminDB (artifact + lineage registry)                    │    │
│  │  - Artifact → Run → Transform lineage                     │    │
│  │  - Dataset/model versioning with biological metadata       │    │
│  │  - Queryable lineage graph                                │    │
│  │  → Feeds into RO-Crate data entities                      │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Layer 1: WORKFLOW ENGINE                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  redun (ML/data) + Nextflow (genomics)                    │    │
│  │  - Call Graph / DAG execution records                     │    │
│  │  - Content-addressed caching (redun)                      │    │
│  │  - Process caching (Nextflow -resume)                     │    │
│  │  → Foundation for Layer 4 RO-Crate emission               │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Layer 0: DATA VERSIONING                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  DVC + cytoskeleton VFS                                   │    │
│  │  - .dvc files in Git for large data                       │    │
│  │  - SWHID for code artifacts                               │    │
│  │  - W3C PROV-J sidecars (vfs/provenance.py)                │    │
│  │  → Data-to-training lineage foundation                    │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

### 4.4 Primary Provenance Tool: redun + LaminDB

**Recommendation:** Use redun as the primary workflow engine (Layer 1) with LaminDB as the artifact registry (Layer 2). The combination provides:

1. **redun**: Content-addressed caching, Call Graph lineage, and Python-native workflow authoring.
2. **LaminDB**: Structured artifact registry with biological metadata, queryable lineage, and OpenLineage-compatible transforms.
3. **MLflow**: Experiment tracking UI and model registry (Layer 3), feeding metadata into RO-Crate.
4. **DVC**: Data versioning for large datasets, bridging data-to-training lineage (Layer 0).
5. **RO-Crate**: Publication-ready provenance packages (Layer 4), emitted automatically.

The layered approach means each tool handles its strength without overlap:
- DVC + VFS handle raw data versioning.
- redun handles workflow execution and caching.
- LaminDB handles artifact metadata and lineage queries.
- MLflow handles experiment comparison and model lifecycle.
- RO-Crate handles FAIR-compliant publication.

---

## 5. Integration Architecture

### 5.1 End-to-End Flow

The complete experiment lifecycle from definition through publication:

```
┌───────────────┐     ┌────────────────┐     ┌──────────────────┐
│  1. DEFINE    │────▶│  2. RESOLVE    │────▶│  3. EXECUTE      │
│               │     │                │     │                  │
│ experiment.   │     │ Pull inputs    │     │ Run workflow     │
│ yaml (ISA)    │     │ from VFS       │     │ (redun/Nextflow) │
│               │     │ Lock envs      │     │ Track with MLflow│
│               │     │ Verify hashes  │     │ Log to LaminDB   │
└───────────────┘     └────────────────┘     └────────┬─────────┘
                                                       │
                                                       ▼
┌───────────────┐     ┌────────────────┐     ┌──────────────────┐
│  6. PUBLISH   │◀────│  5. PACKAGE    │◀────│  4. COLLECT      │
│               │     │                │     │                  │
│ WorkflowHub   │     │ Emit WRROC     │     │ Gather outputs   │
│ Zenodo (DOI)  │     │ Validate crate │     │ Push to VFS      │
│ SEEK          │     │ Sign with SWHID│     │ Update manifests │
└───────────────┘     └────────────────┘     └──────────────────┘
```

### 5.2 Detailed Flow

1. **Define**: Researcher writes `experiment.yaml` (ISA-JSON compliant) specifying:
   - Investigation/Study/Assay hierarchy
   - Input data references (SHA-256, SWHID, DVC refs)
   - Environment reference (cytoskeleton env@version)
   - Parameters (hyperparameters, config values)
   - Execution engine (redun, Nextflow, cloud-run-jobs)
   - Compute backend (local, GCP, HPC)

2. **Resolve**: `cytoskeleton run` resolves all inputs:
   - Fetches locked environment from VFS store
   - Validates all input hashes against store manifest
   - Records each pull as `CreateAction` in Process Run Crate fragment
   - Materializes environment (pixi install, docker pull, etc.)

3. **Execute**: Workflow engine runs the experiment:
   - redun evaluates lazy expressions, builds DAG, executes tasks
   - MLflow logs parameters, metrics, artifacts during execution
   - LaminDB tracks artifact creation with Run/Transform lineage
   - GPU resources allocated via backend (SLURM, K8s, Cloud)

4. **Collect**: On completion, gather all outputs:
   - Model checkpoints, metrics, logs pushed to VFS store
   - LaminDB artifacts registered with metadata
   - Store manifest updated via `update_root_crate()`
   - VFS backend provides version history

5. **Package**: Emit FAIR-compliant provenance:
   - `redun-rocrate` plugin converts Call Graph → Workflow Run Crate
   - `nf-prov` emits WRROC natively (Nextflow pipelines)
   - MLflow metadata wrapped via enhanced `create_training_run_crate()`
   - Crate validated against WRROC profiles
   - SWHID and SHA-256 identifiers embedded

6. **Publish**: Push to external registries:
   - WorkflowHub: Workflow registration with RO-Crate
   - Zenodo: DOI minting for reproducible archives
   - SEEK: ISA-structured experiment metadata
   - FAIR Signposting headers on published crates

### 5.3 The `cytoskeleton run` Command

The unified CLI entry point for experiment execution:

```bash
# Run a training experiment
cytoskeleton run configs/experiments/hrv-lstm-v2.yaml

# Run with explicit backend
cytoskeleton run configs/experiments/hrv-lstm-v2.yaml --backend gcp

# Run a Nextflow pipeline
cytoskeleton run pipelines/genomics/variant-calling.nf --engine nextflow

# Dry run (resolve inputs, validate config, don't execute)
cytoskeleton run configs/experiments/hrv-lstm-v2.yaml --dry-run
```

The config YAML:

```yaml
# configs/experiments/hrv-lstm-v2.yaml
id: hrv-lstm-v2
engine: redun                    # redun | nextflow | cloud-run-jobs
backend: auto                    # auto | local | gcp | hpc

execution_environment: ml.cuda@v2.1.0

inputs:
  - cytognosis://data/sha256:91d4...   # ABCD HRV features
  - cytognosis://model/hf:cytognosis/cytoscope-base@a1b2c3d  # pretrained base

parameters:
  learning_rate: 0.001
  batch_size: 64
  epochs: 100
  hidden_dim: 256

resources:
  gpu: 1
  gpu_type: nvidia-l4
  memory: 16Gi
  cpu: 4

tracking:
  mlflow_experiment: hrv-lstm
  lamindb_project: cytoscope

isa:
  investigation: cytoscope-biomarkers
  study: hrv-predictive-models
  assay_type: deep-learning-training
```

### 5.4 Cross-System Identity Resolution

Every system uses different identifiers. The VFS and crate-emitter must resolve between them:

| System | Identifier Type | Example | Resolution |
|--------|----------------|---------|------------|
| Code | SWHID | `swh:1:rev:2c79bff0a06...` | SWH Archive API |
| Data | SHA-256 / DVC MD5 | `sha256:f5bf89d001...` | VFS driver chain |
| Models | HuggingFace ref | `hf:cytognosis/cytoscope-base@a1b2c3d` | HF Hub API |
| Containers | OCI digest | `ghcr.io/cytognosis/ml@sha256:...` | Container registry |
| Environments | Lockfile hash | `cytognosis://locked/ml.cuda@v2.1.0` | cytoskeleton VFS |
| Experiments | MLflow run ID | `mlflow:run/abc123` | MLflow Tracking Server |
| Artifacts | LaminDB UID | `lamin:artifact/xyz789` | LaminDB instance |
| Publications | DOI | `doi:10.5281/zenodo.12345` | DOI.org |

The VFS `AssetStat` dataclass already captures SWHID identifiers (via `identity/swhid.py`) and the provenance system (`vfs/provenance.py`) records derivation chains. The crate emitter must extend this to resolve cross-system identifiers into RO-Crate `@id` URIs.

---

## 6. Recommendations and Decisions

### 6.1 Execution Engine Strategy

| Domain | Primary Engine | Secondary | Rationale |
|--------|---------------|-----------|-----------|
| **ML / Deep Learning** | redun | Ray (compute runtime) | Already in stack. Pure Python. Content-addressed caching. Ray for distributed training within redun tasks. |
| **Genomics / Bioinformatics** | Nextflow | — | nf-core ecosystem. Native WRROC via nf-prov. Best multi-backend support. |
| **Data Engineering** | redun | Dask (parallel compute) | Python-native. Dask for scaling Pandas/NumPy operations within redun tasks. |
| **Lightweight Batch** | Cloud Run Jobs | — | Serverless, cost-effective, simple containerized tasks. |
| **Large-Scale Training** | Ray on SLURM/GKE | — | Distributed training (DDP, DeepSpeed) with native GPU scheduling. |

### 6.2 Provenance Strategy

| Layer | Tool | Role | Priority |
|-------|------|------|----------|
| **L0: Data Versioning** | DVC + cytoskeleton VFS | Version large datasets. SWHID for code. W3C PROV-J sidecars. | Already implemented |
| **L1: Workflow Engine** | redun + Nextflow | Call Graph/DAG lineage. Content-addressed caching. | Active use |
| **L2: Artifact Registry** | LaminDB | Artifact → Run → Transform lineage. Biological metadata. | To implement |
| **L3: Experiment Tracking** | MLflow (self-hosted) | Hyperparameters, metrics, model registry. Experiment UI. | To deploy |
| **L4: Publication** | RO-Crate (WRROC) | FAIR-compliant provenance packages. | Partially implemented |

### 6.3 Critical Path Items

1. **Build `redun-rocrate` plugin**: Convert redun Call Graphs to Workflow Run Crates. This is the highest-priority gap.
2. **Build `mlflow-rocrate` bridge**: Wrap MLflow experiment metadata into RO-Crate `CreateAction` + `FormalParameter` entities. No existing package exists.
3. **Deploy self-hosted MLflow**: MLflow Tracking Server on GCP for experiment comparison UI.
4. **Integrate LaminDB**: Wire LaminDB artifact registry into the experiment lifecycle for queryable lineage.
5. **Implement `cytoskeleton run`**: Unified CLI entry point with backend selection, environment resolution, and provenance emission.
6. **Define Experiment Run Crate profile**: Custom WRROC profile extending Provenance Run Crate with MLflow metadata mapping.

### 6.4 Architecture Decision Records

| Decision | Choice | Rationale | Alternatives Considered |
|----------|--------|-----------|------------------------|
| Primary ML workflow engine | redun | Already in stack, Python-native, content-addressed caching | Kubeflow (too heavy), Snakemake (less ML-focused) |
| Primary genomics engine | Nextflow | Native WRROC, nf-core ecosystem, multi-backend | Snakemake (smaller ecosystem, no native RO-Crate) |
| Distributed compute runtime | Ray | Best GPU scheduling, unified train/serve/tune | Dask (weaker ML support), raw SLURM (no abstraction) |
| Experiment tracking UI | MLflow (self-hosted) | Open-source, no vendor lock-in, extensible | W&B (SaaS lock-in), Aim (smaller community) |
| Artifact registry | LaminDB | Lineage-native, biological metadata, OpenLineage-compatible | DVC alone (no structured lineage queries) |
| Provenance publication | RO-Crate (WRROC) | FAIR standard, WorkflowHub/Zenodo compatible | W3C PROV alone (not packaging standard) |
| Experiment description | ISA-JSON via LinkML | Community standard, SEEK/FAIRDOM compatible | Custom YAML (not interoperable) |

---

## 7. Open Questions

1. **Kedro migration timing**: The cytos KG pipeline currently uses Kedro for `data_engineering`. Should we migrate Kedro → redun now, or keep Kedro and add a Kedro → Workflow Run Crate emitter? The Reproducibility Strategy recommends keeping Kedro for now and adding the emitter.

2. **LaminDB deployment model**: Self-hosted vs. Lamin Hub. For a nonprofit, self-hosted (PostgreSQL on GCP) gives full control. Lamin Hub provides convenience. Recommendation: start self-hosted for data sovereignty.

3. **MLflow server infrastructure**: GCP Cloud Run (serverless) vs. GCE VM vs. GKE. For a small team, Cloud Run with Cloud SQL (PostgreSQL) backend is simplest and most cost-effective.

4. **Ray cluster management**: Persistent Ray cluster on GKE vs. ephemeral Ray-on-SLURM. For cost optimization, ephemeral clusters that spin up per experiment and tear down after completion.

5. **RO-Crate validation in CI**: Should every merge to `main` trigger RO-Crate validation via `roc-validator`? Yes, but only for changed crate metadata files.

6. **ISA registration**: Register Cytognosis as a Project on FAIRDOMHub (free federation) or self-host SEEK? Start as a FAIRDOMHub Project, self-host later when data volume/privacy needs require it.

7. **WorkflowHub registration**: Register Cytognosis as a Programme + Project on workflowhub.eu (nf-core does this) or self-host? Start on workflowhub.eu, self-host later for PHI workflow control.

8. **Cost allocation**: How to attribute compute costs to specific experiments for grant reporting? MLflow experiment tags can carry grant/project codes, and Cloud billing labels can be set per job.

---

## References

- [Reproducibility Strategy](file:///home/mohammadi/Documents/Claude/Projects/Infrastructure%20and%20Tooling/cytognosis_reproducibility_strategy.md)
- [RO-Crate Research](file:///home/mohammadi/repos/cytognosis/org/plans/experiment-rocrate-research.md)
- [WRROC Specification](https://w3id.org/ro/wfrun)
- [ISA Abstract Model](https://isa-tools.org)
- [redun Documentation](https://insitro.github.io/redun)
- [LaminDB Documentation](https://lamin.ai)
- [MLflow Documentation](https://mlflow.org)
- [Nextflow Documentation](https://nextflow.io)
- [nf-prov Plugin](https://github.com/nextflow-io/nf-prov)
- [cytoskeleton Source](file:///home/mohammadi/repos/cytognosis/cytoskeleton/src/cytoskeleton)
