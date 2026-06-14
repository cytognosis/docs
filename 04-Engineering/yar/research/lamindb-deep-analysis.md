---
title: "LaminDB, LaminHub, and scDataLoader: Deep Analysis for Cytognosis"
date: "2026-05-25"
source: "migrated from org/plans"
category: "research"
status: "current"
tags:
  - cytognosis
  - research
---

# LaminDB, LaminHub, and scDataLoader: Deep Analysis for Cytognosis

> **Date**: 2026-05-24
> **Author**: Cytognosis Research Team
> **Status**: Comprehensive analysis for integration assessment
> **Scope**: LaminDB core architecture, LaminHub SaaS, scDataLoader ML pipeline, comparison with Cytognosis cytoskeleton/cytos systems

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Background: Lamin Labs](#2-background-lamin-labs)
3. [Core Architecture](#3-core-architecture)
4. [Unique Capabilities Assessment](#4-unique-capabilities-assessment)
5. [Storage Backends](#5-storage-backends)
6. [Workflow Integration](#6-workflow-integration)
7. [LaminHub Analysis](#7-laminhub-analysis)
8. [scDataLoader Analysis](#8-scdataloader-analysis)
9. [Integration Assessment for Cytognosis](#9-integration-assessment-for-cytognosis)
10. [Detailed Component Map](#10-detailed-component-map)
11. [Risk Analysis](#11-risk-analysis)
12. [Recommendations](#12-recommendations)

---

## 1. Executive Summary

LaminDB is a lineage-native data lakehouse built specifically for biological R&D. Created by Alex Wolf (creator of Scanpy) and Sunny Sun, it provides a metadata registry layer (Django ORM on Postgres/SQLite) over cloud/local storage, with first-class support for biological ontologies (via bionty), data provenance tracking, and biological data formats (AnnData, zarr, TileDBSOMA, SpatialData, MuData).

**Key findings for Cytognosis:**

- LaminDB's provenance tracking system is significantly more mature than our current W3C PROV-J sidecar approach in cytoskeleton VFS
- Bionty (LaminDB's ontology module) overlaps substantially with our cytos KG ontology registry but uses a simpler, flatter model compared to our KGX-format knowledge graph
- The `MappedCollection` interface for virtual concatenation of AnnData files is directly relevant to our single-cell foundation model training pipeline
- scDataLoader builds on LaminDB's `MappedCollection` to provide PyTorch Lightning DataModules for large-scale model training
- LaminHub (the proprietary SaaS layer) provides UI, collaboration, and access control that we would need to build ourselves if using only the open-source core
- **Recommendation**: Adopt LaminDB as the metadata/provenance layer, keep our cytos KG for deep ontology reasoning, and evaluate scDataLoader for ML data loading

---

## 2. Background: Lamin Labs

### Company Overview

Lamin Labs was founded in **2022** by **Alex Wolf** and **Sunny Sun**, both formerly of Cellarity:

- **Alex Wolf (Co-Founder & CEO)**: Creator of Scanpy, the most widely used toolkit for single-cell analysis. Two decades of experience in R&D software, previously led the compute platform at Cellarity.
- **Sunny Sun (Co-Founder & President)**: Former Head of Computational Biology at Cellarity. Background in genome engineering and cell biology.

The company went through **Y Combinator S22** and has venture backing from Dimension Capital and industry leaders (founders from Cloudera, Aiven, Asimov). The company has offices in Munich, Germany and New York City.

### Mission and Positioning

Lamin Labs aims to solve the "bottleneck of closing the feedback loop across heterogeneous biological data modalities." LaminDB functions as a "git for R&D data," enabling researchers to manage datasets, metadata, and data lineage from personal projects to pharma-scale enterprise deployments. The product is fully open-source (Apache-2.0), with the proprietary LaminHub SaaS layer providing collaboration, access control, and UI.

### Ecosystem

The LaminDB ecosystem is modular, consisting of several interconnected repositories and packages:

| Package | Purpose |
|:--------|:--------|
| `lamindb` | Core library: API, lineage tracking, artifact management |
| `lnschema-core` | Core metadata schema (Django ORM models for registries) |
| `lamindb-setup` | Instance initialization, configuration, LaminHub client |
| `bionty` / `lnschema-bionty` | Biological ontology registries (Gene, Protein, CellType, etc.) |
| `lamin-utils` | Shared utilities across LaminDB and Bionty |
| `wetlab` | Wet-lab registries (Experiment, Well, Biosample, etc.) |

---

## 3. Core Architecture

### 3.1 Data Model

LaminDB structures its data model around four central entities managed as SQL-backed registries:

```
┌──────────────┐     creates      ┌──────────────┐
│  Transform   │─────────────────▶│     Run      │
│  (code/pipe) │                  │  (execution) │
└──────────────┘                  └──────┬───────┘
                                         │
                              inputs/outputs
                                         │
                                  ┌──────▼───────┐
                                  │   Artifact   │
                                  │  (data/model)│
                                  └──────────────┘
                                         │
                                    grouped by
                                         │
                                  ┌──────▼───────┐
                                  │  Collection  │
                                  │  (dataset)   │
                                  └──────────────┘
```

- **Artifact**: The core object representing datasets and models (files, folders, or array-like data such as `AnnData`, `DataFrame`, or `zarr`). An artifact serves as the interface for registration, access, and lineage. Each artifact has a content hash (for integrity and deduplication), suffix, size, and storage location.
- **Collection**: A versioned grouping or container for multiple artifacts, allowing users to organize datasets into logical sets.
- **Transform**: Represents the "code" or "process" that creates or manipulates data. This includes scripts, notebooks, functions, or pipelines. Transforms are versioned to ensure reproducibility, mapping specific source code versions to their executions.
- **Run**: Represents an execution of a Transform. A single transform can have many runs, each capturing the specific context of an execution (time, user, inputs, and outputs).

### 3.2 The Registry Pattern

The registry pattern is central to LaminDB's architecture. Registries are central classes that store `SQLRecord` objects, effectively serving as database tables that manage metadata entities.

```python
import lamindb as ln

# All registries use Django-like ORM syntax
artifact = ln.Artifact.get(key="my-dataset.h5ad")
results = ln.Artifact.filter(suffix=".h5ad", size__gt=1e9)
df = results.to_dataframe()
```

Registries are implemented as Django models, providing:
- **Type-safe queries**: Django's `filter()` with double-underscore lookups (`created_by__handle="user"`)
- **Relational joins**: Traverse relationships between entities
- **Migration support**: Schema evolution via Django migrations
- **Database agnostic**: Works with both PostgreSQL (production) and SQLite (local/development)

### 3.3 Provenance Tracking System

LaminDB tracks data lineage automatically by linking entities together. When a script or notebook is tracked (using `ln.track()`), the system creates a deterministic link between the code (Transform), the execution event (Run), and the data produced or consumed (Artifact).

```python
import lamindb as ln

# Start tracking — creates Transform + Run
ln.track()

# Any artifacts saved during this session are automatically
# linked to the current Run
artifact = ln.Artifact("output.h5ad", key="processed/my-data.h5ad")
artifact.save()

# The artifact now has:
# - artifact.run → the Run that created it
# - artifact.run.transform → the Transform (code) that was executed
# - artifact.run.input_artifacts → what was consumed
```

The provenance system supports:
- **Automatic Git sync**: `ln.settings.sync_git_repo` ensures every Transform is associated with a specific, hashed state of source code
- **Input/output tracking**: Artifacts consumed and produced by a Run are linked automatically
- **Parameter capture**: The `@ln.flow()` and `@ln.step()` decorators automatically capture function arguments as Run parameters
- **Environment tracking**: The compute environment (packages, versions) can be recorded

### 3.4 Feature and Label System

LaminDB annotates artifacts with **features** and **labels**:

- **Features** represent dimensions or variables (e.g., "organism", "temperature", gene names)
- **Labels** represent categories or values (e.g., "human", "effector T cell")
- **Schema** defines expected structure, data types, and required features for validation

```python
# Define a schema for expected features
schema = ln.Schema(
    name="my-experiment-schema",
    features=[
        ln.Feature(name="organism", dtype="cat"),
        ln.Feature(name="cell_type", dtype="cat"),
        ln.Feature(name="n_genes", dtype="int"),
    ],
)

# Annotate an artifact
artifact.features.set_values({"organism": "human", "cell_type": "T cell"})
artifact.ulabels.add(my_label)
```

---

## 4. Unique Capabilities Assessment

### 4.1 Provenance Tracking

| Aspect | LaminDB | DVC | MLflow | W&B |
|:-------|:--------|:----|:-------|:----|
| **Primary Focus** | Data lakehouse / Biology | Data & model versioning | MLOps lifecycle | Experiment tracking |
| **Lineage Approach** | Lineage-native: SQL-based registry | Git-like: hashes + Git commits | Run-centric: params, metrics, artifacts | Artifact-based: visual dashboard |
| **Bio-data Support** | First-class (AnnData, zarr, etc.) | File-agnostic | File-agnostic | File-agnostic |
| **Ontology Integration** | Built-in via bionty | None | None | None |
| **Best For** | Scientific R&D, bioinformatics | Version control, reproducibility | End-to-end model management | Visualization, collaboration |

**Assessment**: LaminDB's provenance tracking is unique in its biology-native integration. DVC, MLflow, and W&B can all track data lineage, but none provide integrated biological ontology validation, feature annotation, or the specific Transform → Run → Artifact graph that maps cleanly to scientific workflows.

**Comparison with Cytognosis**: Our cytoskeleton VFS uses W3C PROV-J sidecar files (`.prov.json`) written alongside each asset. This is lightweight and standards-compliant but lacks:
- Queryable lineage (our sidecars are individual JSON files, not a database)
- Automatic input/output tracking
- Git-integrated Transform versioning
- Cross-artifact lineage queries ("which code produced this dataset?")

### 4.2 Biological Ontology Integration (Bionty)

Bionty provides unified, programmatic access to 20+ public biological ontologies:

| Entity | Sources |
|:-------|:--------|
| Gene | Ensembl, NCBI Gene |
| Protein | UniProt |
| CellType | Cell Ontology |
| Tissue | Uberon |
| Disease | Mondo, Human Disease, ICD |
| Organism | NCBI Taxonomy, Ensembl Species |
| CellMarker | CellMarker |
| CellLine | Cell Line Ontology, Cellosaurus |
| Phenotype | HPO, PATO |
| Pathway | GO, Pathway Ontology |
| ExperimentalFactor | EFO |
| DevelopmentalStage | HsapDv, MmusDv |
| Ethnicity | HANCESTRO |

Key features:
- **Version control**: Track and switch between different ontology source versions
- **In-house extensions**: Create custom ontologies by extending public ones
- **Synonym mapping**: Standardize typos and synonyms to canonical terms
- **Validation**: Check if dataset metadata values map to known ontology terms

```python
import bionty as bt

# Look up a cell type
ct = bt.CellType.lookup()
ct.t_cell  # Returns CellType record with ontology ID, name, synonyms

# Validate a list of cell type names
bt.CellType.inspect(["T cell", "B cell", "fibroblast", "myocyte"])
```

**Comparison with Cytognosis cytos KG**: Our cytos KG (knowledge graph) system is architecturally different:

| Aspect | Bionty (LaminDB) | Cytos KG |
|:-------|:-----------------|:---------|
| **Data model** | Flat registries (SQL tables per entity type) | KGX-format graph (nodes.tsv + edges.tsv) |
| **Storage** | Django ORM (Postgres/SQLite) | DuckDB + Polars DataFrames |
| **Ontologies** | 20+ biological ontologies | 16+ ontologies (CL, Uberon, Mondo, HP, DOID, HANCESTRO, PATO, EFO, CHEBI, SWO, GENO, MaxO, HsapDv, MmusDv, EDAM, Cellosaurus, NCBITaxon) |
| **Cross-ontology** | Limited (per-entity lookups) | SSSOM cross-ontology mappings, UMLS normalized integration |
| **Reasoning** | No graph traversal/reasoning | BioLink model categories, hierarchical relationships |
| **Schema** | Django migrations | registry.yaml with OntologyResource dataclass |
| **Unique strength** | Integrated with data curation/validation | Deep semantic integration (SNOMED, UMLS), knowledge graph traversal |

Our cytos KG builder (`cytos/kg/builder.py`) assembles KGX-format nodes and edges from ontology term Parquet files, UMLS normalized Parquet, SNOMED concept/relationship Parquet, and cross-ontology SSSOM mappings. This is fundamentally a knowledge graph approach, not a flat registry approach. Bionty is simpler but more tightly integrated with data validation workflows.

### 4.3 Feature Annotation

LaminDB's feature annotation system allows tagging artifacts with structured metadata that becomes queryable:

```python
# Annotate an artifact with features
artifact.features.set_values({
    "organism": "human",
    "tissue": "blood",
    "n_cells": 50000,
    "assay": "10x Chromium 3' v3",
})

# Later, query by features
results = ln.Artifact.filter(
    features__organism="human",
    features__n_cells__gt=10000,
)
```

**Assessment**: This is relatively unique to LaminDB among data management tools. DVC/MLflow track parameters per run but don't provide structured feature annotation on data artifacts. This is valuable for scientific data catalogs where you want to find "all datasets with human T cells from blood."

**Alternatives**: A simple approach using a VFS + manifest (which is essentially what our cytoskeleton does) can achieve similar queryability with a well-designed metadata schema, but requires building the query layer ourselves.

### 4.4 Curation Workflows

LaminDB provides a structured curation workflow:

1. **Define schemas**: Specify expected features, data types, and constraints
2. **Initialize a Curator**: `ln.curators.DataFrameCurator` or `AnnDataCurator`
3. **Validate**: `curator.validate()` checks dataset against schema
4. **Standardize**: `curator.standardize()` fixes typos, maps synonyms
5. **Inspect**: `curator.inspect()` returns a report with recommended fixes
6. **Save**: `curator.save_artifact()` registers the validated artifact

```python
import lamindb as ln

# Define expected schema
schema = ln.Schema(
    name="sc-rna-seq",
    features=[
        ln.Feature(name="cell_type", dtype="cat", registries=[bt.CellType]),
        ln.Feature(name="tissue", dtype="cat", registries=[bt.Tissue]),
    ],
)

# Curate a dataset
curator = ln.curators.AnnDataCurator(adata, schema)
curator.validate()
# → Reports which values pass/fail validation
curator.standardize()
# → Maps "T-cell" → "T cell", etc.
artifact = curator.save_artifact(description="My curated scRNA-seq data")
```

**Assessment**: This is a high-value feature for Cytognosis. Our current approach to data standardization is ad-hoc. Bionty-backed curation would catch metadata inconsistencies before they propagate into downstream analyses.

### 4.5 CellxGene Integration

LaminDB provides a streamlined interface to the CZ CELLxGENE Census:

```python
import lamindb as ln

# Connect to the public CELLxGENE instance
db = ln.DB("laminlabs/cellxgene")

# Query datasets
artifacts = db.Artifact.filter(
    suffix=".h5ad",
    description__contains="immune",
    size__gt=1e9,
    cell_types__name__in=["B cell", "T cell"]
).to_dataframe()

# Load a dataset
artifact = db.Artifact.filter(key="some-key").first()
adata = artifact.load()  # Into memory
# OR
accessor = artifact.open()  # Lazy streaming
```

This also supports slicing via TileDB-SOMA for very large datasets without downloading the full Census.

---

## 5. Storage Backends

### 5.1 Supported Backends

LaminDB abstracts storage through the `Artifact` interface:

| Backend | Support Level | Implementation |
|:--------|:-------------|:---------------|
| Local filesystem | First-class | Direct path |
| AWS S3 | First-class | `fsspec` / `s3fs` |
| Google Cloud Storage | First-class | `fsspec` / `gcsfs` |
| Azure Blob Storage | Supported | `fsspec` / `adlfs` |
| HuggingFace | Supported | `fsspec` / `huggingface_hub` |

Storage roots are defined during instance initialization:

```python
# Initialize with S3 storage
lamin init --storage s3://my-bucket/lamindb

# Or local
lamin init --storage ./my-lamindb-instance
```

### 5.2 Data Format Support

LaminDB has deep, native integration with biological file formats:

| Format | Type | Support |
|:-------|:-----|:--------|
| AnnData / `.h5ad` | Single-cell RNA-seq | First-class: backed mode, streaming, feature extraction |
| Zarr | Array storage | First-class: used for spatial data, large arrays |
| TileDBSOMA | Single-cell arrays | First-class: Census integration, scalable queries |
| SpatialData | Spatial omics | Native: Xenium, Visium, MERFISH with Zarr/OME-NGFF |
| MuData | Multimodal | Supported: RNA + ATAC + protein combined objects |
| Parquet | Tabular data | Supported: standard DataFrame serialization |
| CSV/TSV | Tabular data | Supported: basic file tracking |
| FASTQ/BAM/VCF | Genomics | Supported: treated as opaque files with metadata |

### 5.3 Caching and Tiering Strategy

LaminDB does not implement a complex automated data-tiering layer. Its approach:

- **Metadata-first**: SQL metadata is always fast to query without pulling binary data
- **Lazy loading**: `artifact.open()` returns accessors that stream from storage
- **Content hashing**: SHA256 hashes for integrity and deduplication
- **Manual caching**: `artifact.cache()` downloads to local cache; `lamin load` for CLI staging
- **Backed mode**: Open `.h5ad` files in backed mode without full download

**Comparison with Cytognosis cytoskeleton VFS**: Our VFS is more explicit about storage backends:

| Aspect | LaminDB | Cytoskeleton VFS |
|:-------|:--------|:----------------|
| **Backend abstraction** | `fsspec`-based, configured at init | Abstract base class with `LocalVFS`, `S3VFS`, `GitHubVFS`, `GCSVFS` |
| **Content addressing** | SHA256 hash stored in DB | SWHID (Software Heritage Identifier, `swh:1:cnt:<sha1>`) |
| **Provenance per file** | Linked via Run in database | `.prov.json` sidecar (W3C PROV-J) |
| **Manifest** | SQL database | `store.yaml` + `ro-crate-metadata.json` (RO-Crate) |
| **Standards** | Proprietary schema (Django models) | W3C PROV, SWHID (ISO 18670:2025), RO-Crate 1.2 |

---

## 6. Workflow Integration

### 6.1 Supported Workflow Managers

LaminDB integrates with major workflow managers:

| Manager | Integration Method |
|:--------|:-------------------|
| **Python-native (Redun, Kedro, Prefect)** | `@ln.flow()` and `@ln.step()` decorators |
| **Nextflow** | CLI/API calls within pipeline steps |
| **Snakemake** | CLI/API calls within rules |
| **Airflow** | Python operator integration |

### 6.2 The `track()` Context Manager

`ln.track()` is the primary mechanism for recording provenance:

```python
import lamindb as ln

# Explicit tracking
ln.track()
# Creates a Transform for this script/notebook
# Creates a Run for this execution
# Any artifacts saved are linked to this Run

# All saved artifacts automatically get lineage:
artifact = ln.Artifact("output.h5ad", key="results/processed.h5ad")
artifact.save()
# artifact.run → current Run
# artifact.run.transform → this script's Transform
```

### 6.3 Decorators for Pipeline Functions

```python
import lamindb as ln

@ln.flow()
def my_pipeline(input_path: str, n_genes: int = 2000):
    """Main pipeline entry point — tracked automatically."""
    data = load_data(input_path)
    processed = preprocess(data, n_genes)
    save_results(processed)

@ln.step()
def preprocess(data, n_genes):
    """Individual step — granular lineage tracking."""
    # Processing logic
    return filtered_data
```

The decorators automatically capture:
- Function arguments as Run parameters
- CLI arguments (from `click`/`argparse`) via `run.cli_args`
- Stdout/stderr logging (with `@ln.flow()`)
- Timing and execution metadata

### 6.4 Transform Versioning

Transforms are versioned and can be synced with Git:

```python
# Configure Git sync
ln.settings.sync_git_repo = "~/repos/my-project"

# Now every Transform records the Git commit hash
# Enabling: "which exact code version produced this dataset?"
```

---

## 7. LaminHub Analysis

### 7.1 What LaminHub Provides

LaminHub is the proprietary SaaS layer on top of the open-source LaminDB core:

| Feature | Description |
|:--------|:------------|
| **Web UI** | Browse, search, and query the data lakehouse via browser |
| **Lineage visualization** | Interactive graphs showing data flow through transforms and runs |
| **LIMS & ELN** | Integration of experimental records, sheets, and notes with ontologies |
| **Versioning** | Management of data and code revisions with visual diff |
| **Collaboration** | GitHub-like permissions model for data |
| **REST API** | Auto-generated REST API for JavaScript web applications |

### 7.2 Deployment Architecture

- **LaminDB Core**: Open-source, self-hosted anywhere via `pip install lamindb`
- **LaminHub**: SaaS product hosted by Lamin Labs
- **Hybrid model**: Users interact with storage (S3, GCP, local) and databases (Postgres, SQLite) directly through Python, often bypassing REST API for core data operations

### 7.3 Access Management

LaminDB's access management uses **Spaces**, **Instances**, and **Organizations**:

- **Spaces**: Primary mechanism for restricting access within a LaminDB instance. Every database record resides in a space. Spaces have independent collaborator roles (Admin, Read, Write/Modify).
- **Roles & RBAC**: Role-based permission system. Access to storage locations (S3/GCS) is implied by permissions at instance and space levels via federated access tokens.
- **Hierarchy**: Users → Organizations → Teams → Instances → Spaces

### 7.4 Security & Compliance

| Feature | Detail |
|:--------|:-------|
| **SOC2** | Compliant |
| **HIPAA** | Supported |
| **ISO27001** | Monitoring |
| **SSO** | OIDC/Identity Providers |
| **Data encryption** | In transit and at rest |
| **Network security** | Postgres endpoints protected by vulnerability scans, IP whitelisting |
| **VPC deployment** | Enterprise plan: Postgres in customer's private VPC |

### 7.5 Pricing Tiers

| Tier | Storage | Collaboration | Security |
|:-----|:--------|:-------------|:---------|
| **Free** | Personal instances | Limited | Basic |
| **Team** | Team instances | Full collaboration | SOC2 |
| **Enterprise** | Custom | SSO, RBAC, audit logs | HIPAA, VPC, ISO27001 |

### 7.6 Assessment for Cytognosis

LaminHub provides significant value for collaboration and UI, but creates a SaaS dependency. For Cytognosis as a nonprofit:

- **Positive**: We would not need to build our own data browsing UI, lineage visualization, or access control system
- **Concern**: Vendor lock-in on the collaboration layer; data portability is fine (LaminDB core is open-source, data stays in our storage) but the UI/collaboration features are proprietary
- **Alternative**: We could build a minimal UI ourselves using LaminDB's REST API, or contribute to open-source tooling around LaminDB

---

## 8. scDataLoader Analysis

### 8.1 What scDataLoader Provides

scDataLoader is a specialized library and PyTorch Lightning `DataModule` designed for efficient large-scale training of single-cell foundation models (such as scPRINT). It integrates directly with LaminDB.

Key features:
- **Scalable data loading**: Load and stream thousands of datasets containing millions of cells without loading entire datasets into memory
- **LaminDB integration**: Built on `MappedCollection` interface for virtual concatenation
- **Preprocessing pipelines**: Per-dataset preprocessing (normalization, gene selection, train/test splitting) with metadata harmonization via bionty
- **ML readiness**: PyTorch Lightning `DataModule` with configurable train/val/test dataloaders

### 8.2 How MappedCollection Works

`MappedCollection` enables virtual concatenation and lazy loading:

```python
import lamindb as ln

# Get a collection of AnnData artifacts
collection = ln.Collection.get(key="my-sc-collection")

# Create a MappedCollection — virtually concatenates without loading
with collection.mapped(obs_keys=["cell_type"], join="inner") as dataset:
    print(f"#observations: {dataset.shape[0]}")
    
    # PyTorch-compatible __getitem__
    sample = dataset[5]  # Lazily fetches from the right underlying file
    
    # Use with PyTorch DataLoader
    from torch.utils.data import DataLoader
    loader = DataLoader(dataset, batch_size=32, num_workers=4)
```

Performance considerations:
- Local cache recommended for best performance
- Supports parallel data loading (`num_workers > 1`)
- Filtering via `obs_filter` for subset iteration
- For maximum throughput, `.h5ad` → `.parquet` + NVIDIA Merlin

### 8.3 scDataLoader for Model Training

```python
from scdataloader import DataModule

# Initialize with a LaminDB collection
datamodule = DataModule(
    collection_name="my-training-data",
    obs_keys=["cell_type", "organism"],
    batch_size=256,
    num_workers=8,
)

# Weighted random sampling by cell type frequencies
# Hierarchical loss support using ontology graphs
# Automatic train/val/test splits
```

### 8.4 Connection to scPRINT

scPRINT is a large cell model (LCM) developed by Jérémie Kalfon at the Institut Pasteur:

- **scPRINT v1**: Pre-trained on 50M+ human and mouse cells from CZ CELLxGENE Census
- **scPRINT v2**: Scaled to 350M cells across 16 species
- **Capabilities**: Gene network inference, expression denoising, cell/gene embeddings, cell label prediction (type, disease, sex, tissue)
- **Architecture**: Transformer-based, treats gene expression profiles as high-dimensional "sentences"

scDataLoader is the data infrastructure that makes scPRINT training feasible at this scale.

### 8.5 LaminDB Features Used by scDataLoader

| LaminDB Feature | How scDataLoader Uses It |
|:----------------|:-------------------------|
| `Collection` | Groups AnnData artifacts into training sets |
| `MappedCollection` | Virtual concatenation for streaming |
| `Artifact.cache()` | Local caching for performance |
| Bionty ontologies | Metadata harmonization across datasets |
| Feature annotation | Filtering datasets by biological features |
| `obs_filter` | Selecting subsets for balanced training |

### 8.6 Assessment for Cytognosis

scDataLoader is directly relevant to our single-cell foundation model training pipeline:

- **Adopt**: MappedCollection pattern for training on heterogeneous single-cell datasets
- **Evaluate**: scDataLoader as a dependency for our model training if we use LaminDB
- **Consider**: The hierarchical loss support via ontology graphs aligns with our cytos KG capabilities

---

## 9. Integration Assessment for Cytognosis

### 9.1 Component-by-Component Analysis

#### Cytoskeleton VFS vs. LaminDB Artifact Registry

**Current state**: Our cytoskeleton VFS (`cytoskeleton.vfs`) provides a backend-agnostic file system with:
- Abstract base class (`VFSBase`) with `put()`, `get()`, `open()`, `exists()`, `ls()`, `stat()`, `delete()`
- Concrete implementations: `LocalVFS`, `LocalGitVFS`, `GitHubVFS`, `S3VFS`, `GCSVFS`
- Provenance: W3C PROV-J sidecar `.prov.json` files with git SHA, user, timestamp, parent URIs
- Content addressing: SWHID (`swh:1:cnt:<sha1>`) computed from file content
- Store manifest: `store.yaml` + `ro-crate-metadata.json` (RO-Crate 1.2 compliant)

**LaminDB equivalent**: `Artifact` registry + `fsspec`-based storage
- More features: queryable metadata, feature annotation, automatic lineage tracking
- More mature: battle-tested at pharma companies, extensive test suite
- Less standards-compliant: proprietary Django ORM schema vs. our W3C PROV + SWHID + RO-Crate

**Recommendation**: **Adopt LaminDB** for the metadata/provenance layer while preserving our RO-Crate export capability. Our VFS is a lower-level primitive; LaminDB operates at a higher level of abstraction with more features. We can build a thin adapter that maps our VFS concepts to LaminDB's Artifact registry.

#### Cytos KG vs. Bionty

**Current state**: Our cytos KG (`cytos.kg`, `cytos.ontology`) provides:
- KGX-format knowledge graph (nodes.tsv + edges.tsv)
- DuckDB + Polars for graph assembly and querying
- 16+ ontologies with BioLink model categories
- UMLS integration (normalized Parquet from MRCONSO, MRREL, MRSTY, MRDEF)
- SNOMED concept/relationship integration
- Cross-ontology SSSOM mappings
- Hierarchical relationships and graph traversal

**Bionty equivalent**: Flat registries per entity type (CellType, Gene, Disease, etc.)
- Simpler API: `bt.CellType.lookup()`, `bt.CellType.inspect()`
- Integrated with curation workflows
- Version-controlled ontology sources
- No graph traversal, no cross-ontology reasoning, no UMLS/SNOMED

**Recommendation**: **Keep cytos KG** for deep ontology reasoning and knowledge graph capabilities. **Use bionty** as a lightweight front-end for data curation and validation. The two systems serve different purposes: bionty for "is this cell type name valid?" and cytos KG for "what diseases are associated with this cell type through which pathways?"

#### Store Manifest vs. LaminDB Instance

**Current state**: Our store manifest (`cytoskeleton.store.manifest`) provides:
- `store.yaml` at store root describing metadata
- `ro-crate-metadata.json` for RO-Crate compliance
- `StoreManifest` dataclass with name, backend, version, description, license, publisher

**LaminDB equivalent**: Instance configuration (SQL database + storage root)
- More capable: full SQL database for metadata, not just a manifest file
- Less portable: requires a running database, not a self-describing file

**Recommendation**: **Keep RO-Crate export** as a packaging/sharing mechanism, but adopt LaminDB instances as the primary metadata store.

### 9.2 Overlap and Conflict Areas

| Area | Our System | LaminDB | Conflict Level |
|:-----|:-----------|:--------|:---------------|
| File storage abstraction | cytoskeleton VFS | fsspec + Artifact | Low (complementary layers) |
| Provenance tracking | W3C PROV-J sidecars | Run → Transform → Artifact | Low (LaminDB is superset) |
| Content addressing | SWHID | SHA256 hash | Low (different schemes, both work) |
| Ontology lookup | cytos ontology registry | bionty | Medium (overlapping ontology sets) |
| Knowledge graph | cytos KG builder | None (bionty is flat) | None (no conflict) |
| Data curation | None (ad-hoc) | ln.curators | None (we gain capability) |
| ML data loading | None (custom) | MappedCollection + scDataLoader | None (we gain capability) |
| Store metadata | RO-Crate manifest | SQL database | Low (different purposes) |

### 9.3 Recommended Integration Strategy

**Phase 1: Evaluate (Weeks 1-2)**
- Install LaminDB in development environment
- Create a test instance with our single-cell datasets
- Validate bionty ontology coverage against our registry.yaml
- Test MappedCollection with our `.h5ad` files

**Phase 2: Adapt (Weeks 3-4)**
- Build a thin adapter layer: `cytoskeleton.lamindb` that maps our VFS concepts to LaminDB
- Create a bridge between bionty registries and cytos KG ontologies
- Implement RO-Crate export from LaminDB instances

**Phase 3: Integrate (Weeks 5-6)**
- Migrate our single-cell data catalog to LaminDB
- Set up curation workflows for incoming datasets
- Integrate scDataLoader into our model training pipeline
- Set up LaminDB instance on our GCS storage

**Phase 4: Optimize (Weeks 7-8)**
- Evaluate LaminHub vs. building our own UI
- Performance testing with large-scale datasets
- Document the integrated architecture
- Decide on long-term relationship (dependency vs. fork)

---

## 10. Detailed Component Map

| LaminDB Component | Our Equivalent | Unique to LaminDB? | Alternative Tools | Recommendation |
|:-------------------|:---------------|:--------------------|:-----------------|:---------------|
| **Artifact** (file/array registry) | cytoskeleton VFS `AssetStat` | No (concept exists elsewhere) | DVC, MLflow artifacts, HuggingFace Hub | **Adopt**: More queryable than our flat metadata |
| **Collection** (dataset grouping) | None (ad-hoc directories) | No | DVC pipelines, MLflow datasets | **Adopt**: We lack structured collection management |
| **Transform** (code tracking) | VFS `ProvenanceRecord.git_sha` | Partially (concept is common) | MLflow runs, DVC pipeline stages | **Adopt**: More granular than our git SHA tracking |
| **Run** (execution record) | VFS `ProvenanceRecord` | No | MLflow runs, W&B runs | **Adopt**: Queryable execution history |
| **Feature** (metadata dimensions) | None | Partially (rare in data tools) | Great Expectations, Pandera | **Adopt**: Enables structured data catalog |
| **Schema** (validation rules) | None | No | Pandera, Pydantic, Great Expectations | **Adopt**: We need data validation |
| **Bionty** (bio ontologies) | cytos `OntologyRegistry` | Yes (biology-specific) | OLS, BioPortal (web APIs only) | **Use alongside** cytos KG |
| **Curator** (data curation) | None | Partially unique | None integrated | **Adopt**: High-value for data quality |
| **MappedCollection** (virtual concat) | None | Relatively unique | Custom PyTorch datasets | **Adopt**: Critical for ML training |
| **`ln.track()`** (auto-provenance) | Manual `ProvenanceRecord` | Yes (auto-tracking) | MLflow auto-logging | **Adopt**: Reduces boilerplate |
| **`@ln.flow` / `@ln.step`** (decorators) | None | Partially unique | Prefect decorators, Kedro nodes | **Adopt**: Pipeline provenance |
| **Git sync** | Manual in VFS | No | DVC, MLflow + Git | **Adopt**: More automated |
| **LaminHub** (SaaS UI) | None | Yes (biology-focused) | Build custom, or use Metabase | **Evaluate**: Cost vs. build tradeoff |
| **Spaces** (access control) | None | Partially unique | AWS IAM, GCP IAM | **Evaluate**: May need for multi-team |
| **REST API** (auto-generated) | None | No | FastAPI, Django REST | **Skip**: We can build our own |
| **Store manifest** (RO-Crate) | `StoreManifest` + RO-Crate | No (ours is more standards-compliant) | RO-Crate tools, Dataverse | **Keep ours**: Standards compliance matters |
| **SWHID content addressing** | cytoskeleton VFS | No (our implementation) | git blob hashes | **Keep ours**: ISO 18670 compliance |
| **KGX knowledge graph** | cytos KG builder | No (our implementation) | Neo4j, Amazon Neptune | **Keep ours**: Unique capability |
| **UMLS/SNOMED integration** | cytos KG builder | No (our implementation) | UMLS API, MetaMap | **Keep ours**: Deep medical terminology |

---

## 11. Risk Analysis

### 11.1 Adoption Risks

| Risk | Severity | Likelihood | Mitigation |
|:-----|:---------|:-----------|:-----------|
| **Vendor dependency** on Lamin Labs | Medium | Medium | Use only open-source LaminDB core; avoid LaminHub lock-in |
| **Schema migration** complexity | Medium | High | Start fresh with LaminDB for new data; migrate existing data incrementally |
| **Bionty/cytos KG conflicts** | Low | Medium | Use bionty for curation, cytos KG for reasoning; build bridge |
| **Performance** at our scale | Low | Low | LaminDB is tested at pharma scale; our datasets are smaller |
| **Learning curve** for team | Medium | High | LaminDB API is Pythonic and well-documented |
| **API breaking changes** | Medium | Medium | Pin versions; LaminDB follows semver |
| **Open-source sustainability** | Medium | Low | Lamin Labs is VC-backed (YC S22); active development |

### 11.2 Non-Adoption Risks

| Risk | Severity | Likelihood | Mitigation |
|:-----|:---------|:-----------|:-----------|
| **Building equivalent** ourselves | High | High | Significant engineering effort for provenance, curation, ML data loading |
| **Missed ecosystem** integration | Medium | High | LaminDB is becoming standard in single-cell community |
| **Data quality** without curation tools | Medium | High | Ad-hoc validation is error-prone |
| **ML training** data pipeline complexity | Medium | High | MappedCollection solves a real problem we'll face |

---

## 12. Recommendations

### 12.1 Immediate Actions

1. **Install and evaluate LaminDB** with a subset of our single-cell data (1 week)
2. **Map ontology coverage**: Compare bionty's ontology sources against our `registry.yaml` (2 days)
3. **Test MappedCollection**: Benchmark against our current data loading approach (3 days)
4. **Prototype scDataLoader integration**: Wire up our model training script with scDataLoader (3 days)

### 12.2 Strategic Decisions

| Decision | Recommendation | Rationale |
|:---------|:---------------|:----------|
| Use LaminDB for metadata/provenance? | **Yes** | More mature than building our own; open-source; biology-native |
| Replace cytoskeleton VFS? | **No** (adapt) | Keep as low-level primitive; build LaminDB adapter on top |
| Replace cytos KG with bionty? | **No** | Different purposes: bionty for curation, cytos KG for reasoning |
| Use scDataLoader for ML? | **Yes** (evaluate) | Directly addresses our data loading needs for foundation model training |
| Subscribe to LaminHub? | **Defer** | Evaluate free tier first; build minimal UI ourselves if needed |
| Contribute upstream? | **Yes** | Contribute RO-Crate export, SWHID support, any improvements we make |

### 12.3 Architecture Vision

```
┌──────────────────────────────────────────────────────────────┐
│                    Cytognosis Platform                       │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │ cytos KG    │  │ LaminDB Core │  │ scDataLoader       │  │
│  │ (reasoning) │◄─┤ (metadata +  │──┤ (ML data loading)  │  │
│  │             │  │  provenance) │  │                    │  │
│  └──────┬──────┘  └──────┬───────┘  └────────────────────┘  │
│         │                │                                    │
│  ┌──────▼──────┐  ┌──────▼───────┐                           │
│  │ cytos       │  │ bionty       │                           │
│  │ ontology    │  │ (curation)   │                           │
│  │ registry    │  │              │                           │
│  └─────────────┘  └──────────────┘                           │
│         │                │                                    │
│  ┌──────▼────────────────▼───────┐                           │
│  │   cytoskeleton VFS            │                           │
│  │   (storage abstraction)       │                           │
│  └───────────────┬───────────────┘                           │
│                  │                                            │
├──────────────────▼───────────────────────────────────────────┤
│  Storage: GCS / S3 / Local                                   │
│  Database: PostgreSQL (production) / SQLite (development)    │
└──────────────────────────────────────────────────────────────┘
```

### 12.4 Key Principles

1. **Adopt, don't fork**: Use LaminDB as a dependency, contribute improvements upstream
2. **Layer, don't replace**: LaminDB sits above our VFS; cytos KG operates independently
3. **Standards first**: Maintain our W3C PROV, SWHID, RO-Crate compliance as export formats
4. **Open-source only**: Use LaminDB core (Apache-2.0); evaluate but don't depend on LaminHub SaaS
5. **Incremental migration**: New data goes through LaminDB; existing data migrated over time

---

## Appendix A: Source Code Patterns (Cytognosis)

### A.1 Cytoskeleton VFS Base Class

From `cytoskeleton/src/cytoskeleton/vfs/base.py`:

```python
@dataclass
class AssetStat:
    """Filesystem-agnostic stat result for a single asset."""
    uri: str              # Canonical relative URI
    size: int             # Asset size in bytes
    modified: datetime    # Last modification time (UTC)
    swhid: str | None     # Software Heritage Identifier

@dataclass
class ProvenanceRecord:
    """Provenance metadata attached to an asset write operation."""
    message: str          # Human-readable description
    agent: str | None     # User or system identifier
    git_sha: str | None   # Git commit hash
    git_repo: str | None  # Git remote URL
    parent_uris: list[str]  # URIs this asset was derived from
    timestamp: str        # ISO-8601 timestamp
```

### A.2 Cytoskeleton VFS Provenance (W3C PROV-J)

From `cytoskeleton/src/cytoskeleton/vfs/provenance.py`:

```python
def build_prov_document(uri, record, asset_size=None):
    """Build a W3C PROV-J document for an asset."""
    doc = {
        "@context": "https://www.w3.org/ns/prov.jsonld",
        "@type": "prov:Entity",
        "dcterms:identifier": uri,
        "prov:wasGeneratedBy": {
            "@type": "prov:Activity",
            "prov:startedAtTime": record.timestamp,
            "rdfs:comment": record.message,
        },
    }
    # ... agent, git context, parent URIs, etc.
    return doc

def write_prov_sidecar(asset_path, record, *, asset_uri=None):
    """Write a .prov.json sidecar next to asset_path."""
    doc = build_prov_document(uri, record, asset_size=size)
    sidecar_path = asset_path.with_suffix(asset_path.suffix + ".prov.json")
    sidecar_path.write_text(json.dumps(doc, indent=2) + "\n")
    return sidecar_path
```

### A.3 Cytos KG Builder

From `cytos/src/cytos/kg/builder.py`:

```python
# BioLink category mapping for each ontology
ONTOLOGY_CATEGORY_MAP = {
    "cl": "biolink:Cell",
    "uberon": "biolink:AnatomicalEntity",
    "mondo": "biolink:Disease",
    "hp": "biolink:PhenotypicFeature",
    "chebi": "biolink:ChemicalEntity",
    "efo": "biolink:ExperimentalFactor",
    "cellosaurus": "biolink:CellLine",
    # ... 16+ ontologies
}

# Output: KGX-format nodes and edges
# nodes.tsv: id, category, name, description, synonym, provided_by, source, deprecated
# edges.tsv: subject, predicate, object, relation, provided_by, category
```

### A.4 Cytos Ontology Registry

From `cytos/src/cytos/ontology/registry.py`:

```python
@dataclass
class OntologyResource:
    """A single ontology resource entry from the registry."""
    id: str
    name: str
    source: str
    download_url: str
    graph: str
    entity_types: list[str]
    version_installed: str
    owl_path: str
    present: bool
    size_mb: float | None = None

@dataclass
class OntologyRegistry:
    """Registry of all ontology resources managed by Cytos."""
    base_path: Path
    resources: dict[str, OntologyResource]
    schema_version: str = "1.0.0"
    
    @classmethod
    def load(cls, path=None) -> OntologyRegistry:
        """Load registry from registry.yaml."""
        # ...
```

---

## Appendix B: LaminDB API Quick Reference

```python
import lamindb as ln
import bionty as bt

# Instance management
ln.setup.init(storage="./my-instance")
ln.setup.init(storage="s3://my-bucket/lamindb")

# Tracking
ln.track()  # Start provenance tracking

# Artifacts
artifact = ln.Artifact("data.h5ad", key="raw/experiment-1.h5ad")
artifact.save()
artifact = ln.Artifact.get(key="raw/experiment-1.h5ad")
results = ln.Artifact.filter(suffix=".h5ad", size__gt=1e9)
df = results.to_dataframe()
adata = artifact.load()  # Full load
accessor = artifact.open()  # Lazy streaming

# Collections
collection = ln.Collection([artifact1, artifact2], name="my-collection")
collection.save()

# MappedCollection (for ML training)
with collection.mapped(obs_keys=["cell_type"], join="inner") as dataset:
    loader = DataLoader(dataset, batch_size=32)

# Bionty ontologies
bt.CellType.lookup()
bt.CellType.inspect(["T cell", "B cell"])
bt.Gene.from_source(symbol="TP53")

# Curation
curator = ln.curators.AnnDataCurator(adata, schema)
curator.validate()
curator.standardize()
artifact = curator.save_artifact(description="Curated data")

# Lineage queries
artifact.run  # The Run that created this artifact
artifact.run.transform  # The Transform (code) that was executed
artifact.run.input_artifacts.all()  # What was consumed
```

---

## Appendix C: References

- LaminDB Documentation: https://docs.lamin.ai
- LaminDB GitHub: https://github.com/laminlabs/lamindb
- Bionty Documentation: https://docs.lamin.ai/bionty
- scDataLoader GitHub: https://github.com/jkobject/scDataLoader
- LaminHub: https://lamin.ai
- scPRINT Paper: Kalfon et al., "scPRINT: pre-training on 50M cells for gene network inference"
- Scanpy: Wolf et al., "SCANPY: large-scale single-cell gene expression data analysis" (Genome Biology, 2018)