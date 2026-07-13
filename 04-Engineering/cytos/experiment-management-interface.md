---
title: "Experiment Management Interface: Design and Tool Analysis"
date: "2026-05-25"
source: "migrated from org/plans"
category: "research"
status: "current"
tags:
  - cytognosis
  - research
---

# Experiment Management Interface: Design and Tool Analysis

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Cytognosis Foundation, 2026-05-24 (draft v0.1)**
**Status**: Research complete, ready for design decisions

> This document is the companion to the [Experiment Orchestration Research](experiment-orchestration-research.md), which covers experiment definition, execution engines, and provenance tracking. This document focuses on the **user-facing interface** for browsing, comparing, and managing experiments across all Cytognosis workloads, not just ML training runs.

---

## Table of Contents

1. [Existing Tools Comparison](#1-existing-tools-comparison)
2. [Beyond ML Experiments: Cytognosis Scope](#2-beyond-ml-experiments-cytognosis-scope)
3. [Key Views](#3-key-views)
4. [Integration with the Provenance System](#4-integration-with-the-provenance-system)
5. [Relationship to Published Experiments](#5-relationship-to-published-experiments)
6. [Technical Architecture](#6-technical-architecture)
7. [Implementation Roadmap](#7-implementation-roadmap)
8. [Open Questions](#8-open-questions)

---

## 1. Existing Tools Comparison

### 1.1 Evaluation Criteria

Each tool is evaluated against Cytognosis-specific requirements that go beyond standard ML experiment tracking:

| Criterion | Why It Matters for Cytognosis |
|-----------|-------------------------------|
| **Open-source / self-hostable** | 501(c)(3) nonprofit; no SaaS vendor lock-in. Data sovereignty for PHI-adjacent workloads. |
| **Non-ML experiment support** | KG builds, data curation, schema validation, sensor acquisition are first-class experiment types. |
| **Provenance interoperability** | Must feed into RO-Crate (WRROC) publication pipeline. W3C PROV compatibility. |
| **Cost tracking** | Grant-funded compute requires per-experiment cost attribution for reporting. |
| **Extensible metadata schema** | ISA-JSON and LinkML experiment descriptors must be queryable through the UI. |
| **Comparison views** | Cross-type experiment comparison (e.g., compare KG build quality across schema versions). |
| **Team collaboration** | Small team (< 10 researchers), shared dashboards, annotation/tagging. |
| **API-first** | Programmatic access for CI/CD integration, automated reporting, and RO-Crate emission. |

### 1.2 Tool-by-Tool Analysis

#### MLflow (v2.x, self-hosted)

| Dimension | Assessment |
|-----------|-----------|
| **Core strength** | Open-source standard for experiment tracking. Covers tracking, model registry, deployment lifecycle. Platform-agnostic, no vendor lock-in. |
| **UI capabilities** | Run list with filtering/sorting. Metric comparison charts (parallel coordinates, scatter). Artifact browser. Model registry with staging/production lifecycle. |
| **Non-ML support** | Weak. The data model assumes ML runs (parameters, metrics, artifacts). No first-class support for KG builds, schema validation, or data curation pipelines. Custom metrics can approximate non-ML tracking but the UI labels and affordances are ML-centric. |
| **Provenance** | Run-level: logs parameters, metrics, artifacts, source code version. No native RO-Crate emission. No W3C PROV support. Gap solvable via `mlflow-rocrate` bridge (see orchestration research §4.4). |
| **Cost tracking** | No native support. Can log cost as a custom metric, but no aggregation, budgeting, or grant-code attribution. |
| **Extensibility** | Tags and custom metrics provide limited schema extension. No LinkML/ISA-JSON integration. REST API is comprehensive. |
| **Collaboration** | Basic. Shared tracking server. No commenting, annotation, or report-sharing features in open-source edition. |
| **Deployment** | Self-hosted on Cloud Run + Cloud SQL (PostgreSQL). Lightweight. Recommended in orchestration research §6.2. |
| **Cytognosis fit** | ★★★☆☆ — Already selected as Layer 3 in the provenance stack (orchestration research §4.3). Serves as the experiment tracking backend, but the UI needs a custom frontend to support non-ML experiment types and Cytognosis-specific views. |

#### Weights & Biases (W&B)

| Dimension | Assessment |
|-----------|-----------|
| **Core strength** | Best-in-class developer experience. Intuitive real-time dashboards. Excellent team collaboration with shared reports, annotations, and visualizations. |
| **UI capabilities** | Rich interactive dashboards. Parallel coordinates, custom panels, report builder. Sweeps visualization for hyperparameter search. Artifact lineage graph. Tables for structured data comparison. |
| **Non-ML support** | Moderate. W&B Tables and Artifacts can track arbitrary structured data, but the mental model and UI language are ML-centric ("runs," "sweeps," "models"). |
| **Provenance** | Run-level tracking with artifact lineage. No RO-Crate or W3C PROV support. Proprietary lineage format. |
| **Cost tracking** | No native compute cost tracking. |
| **Extensibility** | Custom panels, report templates. No LinkML/ISA-JSON awareness. |
| **Collaboration** | Industry-leading. Shared workspaces, report sharing, commenting, team dashboards. |
| **Deployment** | SaaS-first. Self-hosted "Dedicated Cloud" and "Server" options exist but require enterprise licensing. |
| **Cytognosis fit** | ★★☆☆☆ — SaaS dependency is a dealbreaker for a nonprofit focused on data sovereignty. The UI/UX is the gold standard to learn from, but the licensing model and closed-source nature make it unsuitable as the primary platform. |

#### Aim (v4.x)

| Dimension | Assessment |
|-----------|-----------|
| **Core strength** | High-performance, local-first experiment tracker. Designed for speed with large numbers of runs. Open-source (Apache-2.0). |
| **UI capabilities** | Fast run explorer with grouping and filtering. Metric comparison with interactive charts. Image, audio, text, and distribution tracking. Custom visualizations via Aim UI SDK. |
| **Non-ML support** | Better than MLflow. Aim's flexible metadata model tracks arbitrary objects (images, distributions, text). The `aim.Run` API accepts custom metadata without ML-specific constraints. |
| **Provenance** | Run-level tracking. No RO-Crate or W3C PROV. Local storage (RocksDB-based). |
| **Cost tracking** | No native support. |
| **Extensibility** | Plugin system for custom visualizations. Python SDK for programmatic access. No LinkML integration. |
| **Collaboration** | Limited. Primarily local/single-user. Remote tracking server available but collaboration features are minimal. |
| **Deployment** | Local-first (single binary). Can run as a remote server. Lightweight, no database dependency (uses RocksDB). |
| **Cytognosis fit** | ★★★☆☆ — The local-first, high-performance approach is appealing. The flexible metadata model handles non-ML experiments better than MLflow. However, the smaller community and limited collaboration features are concerns for a growing team. |

#### ClearML

| Dimension | Assessment |
|-----------|-----------|
| **Core strength** | End-to-end MLOps platform. Combines experiment tracking, pipeline orchestration, data management, and model serving in one platform. Open-source server + commercial enterprise. |
| **UI capabilities** | Comprehensive dashboard with experiment comparison, model lineage, pipeline visualization. Dataset versioning UI. Resource monitoring (GPU utilization, cost). Auto-logging with minimal code changes. |
| **Non-ML support** | Moderate. ClearML Pipelines can orchestrate arbitrary tasks, and the dataset management features support non-ML data workflows. The UI remains ML-focused. |
| **Provenance** | Strong within ClearML's ecosystem. Task lineage, dataset versioning, model provenance. No RO-Crate or W3C PROV interoperability. |
| **Cost tracking** | Built-in resource monitoring shows GPU utilization and compute time per task. No grant-code attribution or budget tracking. |
| **Extensibility** | REST API, Python SDK, webhook integrations. No LinkML/ISA-JSON support. |
| **Collaboration** | Good. Shared projects, user management, access control. Commenting and annotation on experiments. |
| **Deployment** | Open-source self-hosted server (ClearML Server). Enterprise features require paid license. |
| **Cytognosis fit** | ★★☆☆☆ — The all-in-one approach conflicts with our layered provenance architecture (orchestration research §4.3). We already use redun + Nextflow for orchestration and LaminDB for artifact registry. Adopting ClearML would create redundant layers. The resource monitoring features are valuable to learn from. |

#### Neptune.ai

| Dimension | Assessment |
|-----------|-----------|
| **Core strength** | Enterprise-grade experiment tracking optimized for scalability and metadata management. Handles millions of runs. Strong in regulated industries. |
| **UI capabilities** | Scalable run explorer with advanced filtering. Custom dashboards. Comparison tables. Artifact tracking with version history. |
| **Non-ML support** | Weak. Primarily designed for ML experiment tracking. The data model is flexible but the UI and documentation focus entirely on ML workflows. |
| **Provenance** | Run-level tracking with artifact lineage. Model registry. No RO-Crate or W3C PROV support. |
| **Cost tracking** | No native compute cost tracking. |
| **Extensibility** | REST API, Python SDK, integrations with major ML frameworks. No LinkML/ISA-JSON support. |
| **Collaboration** | Strong. Shared workspaces, team management, commenting. Designed for enterprise teams. |
| **Deployment** | SaaS-only (usage-based pricing). No self-hosted option. |
| **Cytognosis fit** | ★☆☆☆☆ — SaaS-only with usage-based pricing is incompatible with nonprofit budget constraints. No self-hosting option eliminates it from consideration. The scalability design is informative but not critical at our current scale. |

### 1.3 Summary Matrix

| Capability | MLflow | W&B | Aim | ClearML | Neptune |
|-----------|--------|-----|-----|---------|---------|
| **Open-source** | ✅ Apache-2.0 | ❌ SaaS | ✅ Apache-2.0 | ✅ + Enterprise | ❌ SaaS |
| **Self-hostable** | ✅ Easy | ⚠️ Enterprise only | ✅ Easy | ✅ Easy | ❌ No |
| **Non-ML experiments** | ⚠️ Weak | ⚠️ Moderate | ✅ Flexible | ⚠️ Moderate | ⚠️ Weak |
| **RO-Crate / W3C PROV** | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |
| **Cost tracking** | ❌ None | ❌ None | ❌ None | ⚠️ Resource monitor | ❌ None |
| **ISA/LinkML aware** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **API-first** | ✅ REST | ✅ SDK | ✅ SDK | ✅ REST + SDK | ✅ REST + SDK |
| **Collaboration** | ⚠️ Basic | ✅ Best | ⚠️ Limited | ✅ Good | ✅ Good |
| **Community size** | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ |

### 1.4 Key Finding

No existing tool satisfies Cytognosis requirements. Every tool assumes ML-only experiment tracking, none support RO-Crate provenance, none integrate with ISA/LinkML metadata schemas, and none provide grant-aware cost tracking. The recommendation is:

1. **Use MLflow as the backend** for experiment tracking (Layer 3 in the provenance stack, already decided in orchestration research).
2. **Build a custom frontend** (the Experiment Management Interface) that queries MLflow, LaminDB, and the RO-Crate publication registry to present a unified view across all experiment types.
3. **Learn from W&B's UX** for dashboard design, interactive comparison, and collaboration patterns.
4. **Learn from ClearML's resource monitoring** for cost tracking and GPU utilization views.

---

## 2. Beyond ML Experiments: Cytognosis Scope

### 2.1 The Problem

Standard experiment trackers assume a narrow workflow: configure hyperparameters → train model → log metrics → compare runs. Cytognosis runs at least eight distinct experiment types, each with different inputs, outputs, success criteria, and lifecycle stages.

### 2.2 Experiment Type Taxonomy

| Experiment Type | Inputs | Outputs | Success Criteria | Tracking Needs |
|----------------|--------|---------|-----------------|----------------|
| **ML Training** | Dataset, hyperparams, pretrained model | Model checkpoint, metrics, loss curves | Validation metric (AUC, F1, MAE) | Standard MLflow: params, metrics, artifacts |
| **Knowledge Graph Build** | Source ontologies, raw data, schema version, mapping rules | KG snapshot (RDF/JSON-LD), validation report, statistics | SHACL validation pass rate, entity count, edge density, reasoning consistency | Schema version tracking, entity/edge statistics, SHACL reports, diff against previous KG version |
| **Data Curation Pipeline** | Raw datasets, curation rules, quality thresholds | Curated dataset, QC report, rejection log | Pass rate, data quality score, completeness | Quality metrics over time, rejection analysis, curation rule versioning |
| **Schema Validation** | LinkML schema, instance data, SHACL shapes | Validation report, conformance matrix | Conformance rate, breaking change count | Schema evolution tracking, cross-version conformance comparison |
| **Sensor Data Acquisition** | Sensor configuration, calibration data, acquisition protocol | Raw signal data, quality metrics, calibration report | Signal-to-noise ratio, data completeness, calibration drift | Sensor health monitoring, acquisition batch tracking, calibration history |
| **Genomic Analysis** | FASTQ/BAM files, reference genome, pipeline version | VCF, QC metrics, annotation results | Variant call quality, coverage depth, concordance | Sample tracking, pipeline version comparison, QC dashboards |
| **Inference / Serving** | Model version, input batch, serving config | Predictions, latency metrics, confidence scores | Latency P50/P99, throughput, prediction quality | Model version A/B comparison, latency monitoring, drift detection |
| **Benchmark / Evaluation** | Model(s), evaluation dataset(s), metric suite | Benchmark results, comparison tables | Metric improvement over baseline | Cross-model comparison, leaderboard, regression detection |

### 2.3 Unified Metadata Model

Every experiment type shares a common metadata skeleton, defined by the ISA mapping from the orchestration research (§1.4):

```yaml
# Common experiment metadata (ISA-compatible)
experiment:
  id: "exp-2026-05-24-kg-build-v3"
  type: knowledge_graph_build          # from taxonomy above
  
  # ISA hierarchy
  investigation: cytoscope-biomarkers
  study: disease-ontology-integration
  assay_type: knowledge-graph-build
  
  # Universal fields
  created_by: shahin@cytognosis.org
  created_at: "2026-05-24T10:30:00Z"
  status: completed                    # pending | running | completed | failed
  execution_engine: redun
  compute_backend: local
  environment: data.core@v1.3.0
  
  # Cost tracking
  cost:
    compute_seconds: 3420
    gpu_seconds: 0
    estimated_cost_usd: 0.00
    grant_code: "NSF-2412345"
    
  # Provenance links
  provenance:
    redun_execution_id: "exec-abc123"
    lamindb_run_id: "run-xyz789"
    rocrate_id: null                   # populated after publication
    
  # Type-specific metadata (varies by experiment type)
  type_metadata:
    schema_version: "v0.4.0"
    source_ontologies: ["DO", "HPO", "MONDO"]
    entity_count: 145230
    edge_count: 892341
    shacl_pass_rate: 0.9847
```

The `type_metadata` section is polymorphic, defined by LinkML discriminated unions. Each experiment type has its own LinkML class extending a common `ExperimentRun` base. This is the critical gap that no existing tool addresses: experiment-type-aware metadata with schema validation.

---

## 3. Key Views

### 3.1 View Architecture

The Experiment Management Interface provides six primary views, each addressing a distinct user workflow:

```
┌─────────────────────────────────────────────────────────────────┐
│                  Experiment Management Interface                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ Run List │ │Run Detail│ │Comparison│ │ Param    │           │
│  │          │ │          │ │          │ │ Search   │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
│                                                                  │
│  ┌──────────┐ ┌──────────┐                                      │
│  │  Cost    │ │  FAIR    │                                      │
│  │ Tracking │ │ Readiness│                                      │
│  └──────────┘ └──────────┘                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Run List View

**Purpose**: Browse, filter, and sort all experiments across types.

**Key features**:

- **Unified listing** across all experiment types (ML training, KG builds, data curation, etc.) with type-specific icons and color coding following Cytognosis brand colors
- **Faceted filtering**: by experiment type, status (pending/running/completed/failed), investigator, date range, ISA investigation/study, environment version, compute backend, grant code
- **Column customization**: users select which metadata columns to display (type-specific columns auto-populate based on experiment type filter)
- **Bulk actions**: tag, compare, export to CSV, trigger RO-Crate publication
- **Quick metrics**: inline sparklines for key metrics (loss curve for ML, entity count trend for KG, quality score for curation)

**Data sources**: MLflow Tracking API (runs), LaminDB (artifact metadata), cytoskeleton VFS (provenance records)

### 3.3 Run Detail View

**Purpose**: Deep inspection of a single experiment run.

**Layout** (tabbed interface):

| Tab | Contents |
|-----|----------|
| **Overview** | Experiment metadata card (ISA hierarchy, status, timing, cost). Type-specific summary panel. Links to related runs (parent/child, same study). |
| **Parameters** | All input parameters, grouped by category. Diff against previous run in the same study. Environment specification with lockfile reference. |
| **Metrics** | Interactive charts for all logged metrics. For ML: loss curves, validation metrics over epochs. For KG: entity/edge counts, SHACL pass rates. For curation: quality scores, rejection rates. |
| **Artifacts** | File browser for all outputs. Preview for common formats (images, tables, JSON, YAML). Download links with integrity hashes (SHA-256). LaminDB artifact metadata. |
| **Provenance** | Visual lineage graph showing data flow from inputs through processing steps to outputs. Derived from redun Call Graph and/or LaminDB Run→Transform→Artifact chain. Links to W3C PROV-J sidecars. |
| **Environment** | Full environment specification: cytoskeleton environment name and version, lockfile contents, Docker image digest, SWHID identifiers. Diff against other runs. |
| **Logs** | Execution logs (stdout/stderr). Resource utilization timeline (CPU, GPU, memory). Error traces for failed runs. |
| **Publication** | RO-Crate status (draft/validated/published). FAIR readiness checklist. Links to published crate on WorkflowHub/Zenodo. DOI if minted. |

### 3.4 Comparison View

**Purpose**: Side-by-side comparison of two or more runs.

**Key features**:

- **Cross-type comparison**: Compare a KG build run against a schema validation run to correlate schema changes with KG quality metrics
- **Metric overlay**: Plot the same metric across multiple runs on a single chart (e.g., SHACL pass rate across three KG build versions)
- **Parameter diff**: Highlight parameter differences between runs (similar to a code diff but for experiment configs)
- **Environment diff**: Show differences in execution environments (package versions, container images)
- **Artifact diff**: For structured outputs (JSON, YAML, CSV), show content diffs. For KG snapshots, show entity/edge count deltas
- **Statistical significance**: For ML experiments, built-in statistical tests (paired t-test, bootstrap confidence intervals) comparing metric distributions across runs

**Design reference**: W&B's comparison tables and parallel coordinates are the UX benchmark. The implementation should support the same interactive exploration patterns while extending to non-ML experiment types.

### 3.5 Parameter Search View

**Purpose**: Explore the parameter space across many runs to identify optimal configurations.

**Key features**:

- **Parallel coordinates plot**: Each axis represents a parameter or metric. Lines connecting values across axes are colored by a selected objective metric. Brushing on any axis filters runs
- **Scatter matrix**: Pairwise scatter plots of selected parameters and metrics for identifying correlations
- **Hyperparameter importance**: For ML experiments, compute and display parameter importance scores (e.g., fANOVA, random forest feature importance) to guide future experiments
- **Suggested next runs**: Based on Bayesian optimization or Gaussian process models, suggest parameter configurations likely to improve the objective metric
- **Non-ML parameter search**: For KG builds, explore how different schema versions, source ontology combinations, or mapping rule sets affect quality metrics. For data curation, explore how quality thresholds affect pass rates and downstream data utility

### 3.6 Cost Tracking View

**Purpose**: Monitor, attribute, and forecast compute costs for grant reporting and budget management.

**Key features**:

- **Per-experiment cost**: Compute cost breakdown by experiment (CPU hours, GPU hours, storage, network). Derived from Cloud Billing API (GCP), SLURM accounting, or local time tracking
- **Grant-code attribution**: Each experiment carries a `grant_code` tag. Roll up costs by grant for quarterly reporting. Export cost reports as CSV/PDF for grant deliverables
- **Budget alerts**: Set per-grant or per-investigation compute budgets. Alert when spending approaches thresholds
- **Cost trend analysis**: Time-series charts showing compute spend by experiment type, compute backend, and grant code
- **Cost comparison**: Compare the cost-per-quality-unit across runs (e.g., cost per point of AUC improvement, cost per 1000 KG entities validated)
- **Forecasting**: Based on historical cost data, project future spending for budget planning

**Data sources**: GCP Cloud Billing export (BigQuery), SLURM `sacct` accounting data, MLflow custom metrics (for self-reported timing), Cloud Run Jobs execution logs

### 3.7 FAIR Readiness View

**Purpose**: Track how close each experiment is to being FAIR-published as an RO-Crate.

**Key features**:

- **Readiness checklist per run**: Automated checks for each FAIR criterion:
  - ☐ All inputs have content-addressed identifiers (SHA-256, SWHID)
  - ☐ Execution environment is locked (cytoskeleton lockfile hash recorded)
  - ☐ All outputs are registered in LaminDB with metadata
  - ☐ Provenance chain is complete (redun Call Graph or nf-prov WRROC)
  - ☐ ISA metadata is complete (investigation, study, assay fields populated)
  - ☐ RO-Crate manifest is valid (`roc-validator` passes)
  - ☐ No proprietary data formats in outputs
  - ☐ License specified for all artifacts
- **Aggregate dashboard**: Bar chart showing FAIR readiness scores across all experiments, grouped by investigation/study
- **One-click publish**: For runs that pass all checks, trigger RO-Crate packaging and publication to WorkflowHub/Zenodo
- **Gap analysis**: For runs that fail checks, show which specific gaps need to be addressed before publication

---

## 4. Integration with the Provenance System

### 4.1 Provenance Layer Mapping

The interface sits at the top of the provenance layer stack defined in the orchestration research (§4.3). It reads from all four layers but writes to none of them directly:

```
┌───────────────────────────────────────────────────────────────┐
│          Experiment Management Interface (read-only)           │
│                                                                │
│  Queries:                                                      │
│  ├── Layer 3: MLflow → run metadata, params, metrics           │
│  ├── Layer 2: LaminDB → artifact lineage, biological metadata  │
│  ├── Layer 1: redun → Call Graph, caching status               │
│  ├── Layer 0: DVC/VFS → data versions, SWHID identifiers       │
│  └── Layer 4: RO-Crate registry → publication status, DOIs     │
│                                                                │
│  Triggers (write actions, delegated):                          │
│  ├── RO-Crate packaging → cytoskeleton publish CLI             │
│  ├── WorkflowHub/Zenodo push → publish pipeline                │
│  └── Experiment re-run → cytoskeleton run CLI                  │
└───────────────────────────────────────────────────────────────┘
```

### 4.2 Data Flow Architecture

The interface aggregates data from multiple backends through a unified API layer:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MLflow     │  │   LaminDB    │  │   redun DB   │
│  (Postgres)  │  │  (Postgres)  │  │  (Postgres)  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └────────┬────────┘                 │
                │                          │
       ┌────────▼──────────────────────────▼───────┐
       │         Experiment API (FastAPI)            │
       │                                             │
       │  /api/v1/runs          → unified run list   │
       │  /api/v1/runs/{id}     → run detail         │
       │  /api/v1/compare       → comparison data    │
       │  /api/v1/costs         → cost aggregation   │
       │  /api/v1/provenance    → lineage graph       │
       │  /api/v1/fair          → readiness checks   │
       │  /api/v1/publish       → trigger publishing │
       └────────────────┬──────────────────────────┘
                        │
       ┌────────────────▼──────────────────────────┐
       │         Frontend (React + Cytognosis DS)    │
       │                                             │
       │  Run List | Detail | Compare | Search       │
       │  Cost Tracking | FAIR Readiness             │
       └─────────────────────────────────────────────┘
```

### 4.3 Cross-System Identity Resolution

The API layer resolves identifiers across systems to present a unified view. Each experiment run has multiple identities:

| System | Identifier | Resolution Method |
|--------|-----------|-------------------|
| MLflow | `mlflow:run/abc123` | MLflow Tracking API |
| LaminDB | `lamin:run/xyz789` | LaminDB Python API |
| redun | `redun:exec/def456` | redun SQL backend |
| cytoskeleton VFS | `cytognosis://...` | VFS driver chain |
| RO-Crate | `doi:10.5281/zenodo.12345` | DOI resolution |
| Git | `swh:1:rev:2c79bff0a06...` | SWH Archive API |

The Experiment API maintains a lightweight mapping table linking these identities for each experiment run. This table is populated automatically during the experiment lifecycle:

1. **On experiment start**: `cytoskeleton run` creates the MLflow run, the LaminDB run, and the redun execution, then writes all three IDs to the mapping table
2. **On experiment completion**: The mapping table is updated with output artifact IDs (LaminDB UIDs, VFS paths)
3. **On publication**: The RO-Crate ID and DOI are added to the mapping table

### 4.4 Provenance Lineage Visualization

The Run Detail → Provenance tab renders an interactive lineage graph derived from multiple sources:

- **redun Call Graph**: Shows the DAG of Python function calls, their input/output hashes, and caching decisions. Each node links to the function source code (via SWHID)
- **LaminDB lineage**: Shows Artifact → Run → Transform relationships. Each artifact node links to its VFS storage location and metadata
- **VFS provenance**: Shows W3C PROV-J derivation chains from `vfs/provenance.py`. Each node includes git context (commit hash, branch, author)

The lineage graph merges these three sources into a unified DAG, with nodes colored by source system (MLflow = Azure #3B7DD6, LaminDB = Teal #14A3A3, redun = Violet #8B3FC7, VFS = Indigo #5145A8).

---

## 5. Relationship to Published Experiments

### 5.1 Publication Lifecycle

Experiments move through a defined lifecycle from execution to FAIR publication:

```
  ┌──────┐    ┌──────────┐    ┌──────────┐    ┌───────────┐    ┌──────────┐
  │Draft │───▶│Validated │───▶│Packaged  │───▶│Published  │───▶│Archived  │
  │      │    │          │    │          │    │           │    │          │
  │No RO-│    │FAIR check│    │RO-Crate  │    │WorkflowHub│    │Zenodo DOI│
  │Crate │    │passes    │    │emitted   │    │/SEEK      │    │minted    │
  └──────┘    └──────────┘    └──────────┘    └───────────┘    └──────────┘
```

The FAIR Readiness View (§3.7) tracks each run's position in this lifecycle. The interface provides:

- **Batch publication**: Select multiple completed runs and publish them as a collection (e.g., all runs in an ISA Study)
- **Dependency-aware publishing**: When publishing a run, automatically check if its input data and upstream runs are also published. If not, prompt the user to publish the dependency chain
- **Version linking**: When a new version of an experiment is published, automatically link it to previous versions via `schema:isBasedOn` in the RO-Crate metadata

### 5.2 Central Experiment Repository

Published experiments feed into a central repository that serves as the Cytognosis experiment catalog:

| Repository | Purpose | Content |
|-----------|---------|---------|
| **WorkflowHub** | Workflow registration | Workflow definitions (Nextflow, redun) with RO-Crate metadata. Linked to nf-core community for bioinformatics pipelines. |
| **Zenodo** | Archival + DOI minting | Complete experiment packages (code + data + results + provenance). Immutable, citable, FAIR. |
| **FAIRDOMHub / SEEK** | ISA-structured metadata | Investigation → Study → Assay hierarchy. Federation with the FAIRDOM ecosystem. |
| **Internal catalog** | Team discovery | Searchable index of all experiments (published and unpublished). Links to external repositories for published items. |

### 5.3 Internal Catalog Integration

The Experiment Management Interface doubles as the internal catalog. The Run List View shows all experiments, with published ones marked with their external identifiers:

- Published runs display a DOI badge linking to Zenodo
- WorkflowHub-registered workflows display the WorkflowHub ID
- SEEK-registered experiments display the SEEK project/assay link

The catalog supports:

- **Search by DOI**: Enter a DOI to find the corresponding internal experiment run
- **Citation export**: Generate BibTeX, RIS, or CSL-JSON citations for published experiments
- **Reproducibility link**: Each published experiment includes a "Reproduce" button that generates the `cytoskeleton run` command to re-execute the experiment from its RO-Crate specification
- **Impact tracking**: For published experiments, display citation counts (via OpenAlex/Crossref) and reuse metrics (via WorkflowHub download counts)

### 5.4 SEEK/FAIRDOMHub Synchronization

The ISA metadata from each experiment maps directly to SEEK's data model:

| Interface Field | SEEK Entity | Sync Direction |
|----------------|-------------|----------------|
| Investigation | SEEK Investigation | Push on publish |
| Study | SEEK Study | Push on publish |
| Assay (experiment run) | SEEK Assay | Push on publish |
| Artifacts | SEEK Data Files | Push on publish |
| Protocols | SEEK SOPs | Push on publish |
| Publications | SEEK Publications | Bidirectional |

Synchronization is triggered by the "Publish to SEEK" action in the FAIR Readiness View. The sync uses the SEEK JSON API to create or update entities, maintaining a local mapping table for identity resolution.

---

## 6. Technical Architecture

### 6.1 Stack Selection

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Frontend** | React + TypeScript | Cytognosis standard (react-expert skill). Rich interactive visualization requirements. |
| **Design system** | Cytognosis Design System | Dark theme (bg #0A0A14), glassmorphism, Phosphor Icons, Inter font. Brand colors from fluorescent dye wavelengths. |
| **API** | FastAPI (Python) | Cytognosis standard (fastapi-expert skill). Async I/O for querying multiple backends. OpenAPI schema auto-generation. |
| **Charting** | Plotly.js / D3.js | Interactive charts for metric comparison, parallel coordinates, lineage graphs. |
| **Graph viz** | Cytoscape.js | Lineage graph rendering (provenance DAG). Supports large graphs with layout algorithms. |
| **Auth** | Firebase Auth | Cytognosis standard. Team-level access control for experiments. |
| **Caching** | Redis | Cache aggregated query results across MLflow, LaminDB, and redun backends. |

### 6.2 API Design

The Experiment API provides a unified interface over the heterogeneous backend systems:

```python
# Simplified API route structure (FastAPI)

@router.get("/api/v1/runs")
async def list_runs(
    experiment_type: ExperimentType | None = None,
    status: RunStatus | None = None,
    investigation: str | None = None,
    study: str | None = None,
    grant_code: str | None = None,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    sort_by: str = "created_at",
    limit: int = 50,
    offset: int = 0,
) -> PaginatedResponse[UnifiedRun]:
    """Query MLflow + LaminDB + redun, merge by identity mapping."""
    ...

@router.get("/api/v1/runs/{run_id}")
async def get_run(run_id: str) -> UnifiedRunDetail:
    """Aggregate full detail from all backend systems."""
    ...

@router.post("/api/v1/runs/{run_id}/publish")
async def publish_run(run_id: str, target: PublishTarget) -> PublishResult:
    """Trigger RO-Crate packaging and publication."""
    ...

@router.get("/api/v1/costs")
async def get_costs(
    grant_code: str | None = None,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    group_by: str = "experiment_type",
) -> CostReport:
    """Aggregate costs from Cloud Billing, SLURM, and local tracking."""
    ...
```

### 6.3 Deployment

| Component | Deployment Target | Notes |
|-----------|------------------|-------|
| Frontend | Firebase Hosting | Static SPA, CDN-served |
| API | Cloud Run | Serverless, auto-scaling, cost-effective |
| MLflow Server | Cloud Run + Cloud SQL | Shared PostgreSQL backend |
| LaminDB | Cloud SQL (PostgreSQL) | Shared or separate instance |
| redun DB | Cloud SQL (PostgreSQL) | Shared instance |
| Redis | Memorystore (GCP) | Managed Redis for caching |
| Identity mapping | Cloud SQL (PostgreSQL) | Lightweight table, co-located with API |

---

## 7. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)

- Deploy MLflow Tracking Server on Cloud Run + Cloud SQL
- Build Experiment API with `/runs` endpoint querying MLflow
- Implement Run List View with basic filtering (type, status, date)
- Implement Run Detail View with Overview and Metrics tabs
- Wire up identity mapping table (MLflow run ID ↔ experiment config)

### Phase 2: Provenance Integration (Weeks 5-8)

- Integrate LaminDB as data source for artifact metadata and lineage
- Integrate redun Call Graph queries for provenance visualization
- Build the Provenance tab in Run Detail View (lineage DAG with Cytoscape.js)
- Implement Comparison View with parameter diff and metric overlay
- Add VFS provenance (W3C PROV-J sidecar) data to lineage graph

### Phase 3: Cost and FAIR (Weeks 9-12)

- Build Cost Tracking View with GCP Cloud Billing integration
- Implement grant-code attribution and cost roll-up reports
- Build FAIR Readiness View with automated checklist evaluation
- Implement one-click RO-Crate packaging via `cytoskeleton publish` CLI
- Add publication workflow (WorkflowHub, Zenodo, SEEK push)

### Phase 4: Advanced Features (Weeks 13-16)

- Build Parameter Search View with parallel coordinates and scatter matrix
- Implement cross-type experiment comparison
- Add suggested next runs (Bayesian optimization integration)
- Build internal catalog with DOI search, citation export, and reproducibility links
- Performance optimization (Redis caching, pagination, lazy loading)

---

## 8. Open Questions

1. **MLflow as sole tracking backend vs. direct LaminDB tracking**: Should non-ML experiments (KG builds, schema validation) log to MLflow at all, or should they log directly to LaminDB with the Experiment API providing the unified view? MLflow's data model is ML-centric; forcing KG build metrics into MLflow parameters/metrics may be awkward.

2. **Real-time streaming**: Should the Run Detail View support real-time metric streaming (WebSocket) for long-running experiments, or is periodic polling sufficient? Real-time adds complexity but improves the experience for multi-hour training runs.

3. **Access control granularity**: Should access control be per-investigation, per-study, or per-run? For PHI-adjacent genomic analyses, fine-grained access control may be necessary. Firebase Auth provides user-level auth; row-level security would need to be implemented in the API layer.

4. **Offline/local mode**: Should the interface support a local mode (e.g., `cytoskeleton ui` launches a local web server) for development and offline use? This would reduce cloud dependency during active experimentation.

5. **Notification system**: Should the interface provide notifications for experiment completion, budget alerts, and FAIR readiness changes? If so, email, Slack, or in-app notifications?

6. **Custom dashboards**: Should users be able to create custom dashboard layouts (à la W&B Reports), or are the six fixed views sufficient for the initial release?

7. **Mobile support**: Is a responsive/mobile layout needed for monitoring long-running experiments from mobile devices, or is desktop-only acceptable?

---

## References

- [Experiment Orchestration Research](experiment-orchestration-research.md)
- [Reproducibility Strategy](file:///home/mohammadi/Documents/Claude/Projects/Infrastructure%20and%20Tooling/cytognosis_reproducibility_strategy.md)
- [RO-Crate Research](file:///home/mohammadi/repos/cytognosis/org/plans/experiment-rocrate-research.md)
- [MLflow Documentation](https://mlflow.org)
- [Weights & Biases Documentation](https://docs.wandb.ai)
- [Aim Documentation](https://aimstack.readthedocs.io)
- [ClearML Documentation](https://clear.ml/docs)
- [Neptune.ai Documentation](https://docs.neptune.ai)
- [LaminDB Documentation](https://lamin.ai)
- [ISA Tools](https://isa-tools.org)
- [WorkflowHub](https://workflowhub.eu)
- [SEEK / FAIRDOMHub](https://fairdomhub.org)
- [cytoskeleton Source](file:///home/mohammadi/repos/cytognosis/cytoskeleton/src/cytoskeleton)
