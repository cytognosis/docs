# DVC Configuration Guide

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, data scientists
> **Tags**: `dvc`, `gcs`, `data-versioning`, `pipeline`

> **Status**: Operational (v3.67.1 with GCS support)
> **Updated**: 2026-06-14

**Last verified: 2026-06-14** — `gs://cytognosis-data-hub` confirmed with versioning ON and lifecycle rules (60d Nearline, 180d Coldline). `gs://cytognosis-mlflow-artifacts` NOW EXISTS (created 2026-06-14, `us-central1`). DVC remotes use `cytognosis-infrastructure` and `cytognosis-phi-prod` projects only; `cytognosis-data` project does NOT exist.

## Installation

DVC is installed in the `cytognosis` conda environment with GCS support:

```bash
# Activate environment
conda activate cytognosis

# Verify
dvc version
# Expected: DVC version: 3.67.1, Supports: gs (gcsfs = 2024.12.0)
```

Binary location: `/home/mohammadi/miniforge3/envs/cytognosis/bin/dvc`

## Remote Configuration

### Datasets Repository (central data lake)

The datasets repo at `~/datasets` uses a shared DVC cache on GCS:

```bash
# Already configured — verify with:
cd ~/datasets
dvc remote list
# Expected: data-hub  gs://cytognosis-data-hub/dvc-cache/  (default)
```

### Per-Project Remotes

Each project (e.g., cytos) has its own DVC remote path under the data hub:

```bash
# cytos project — already configured
cd ~/repos/cytognosis/cytos
dvc remote list
# Expected: data-hub  gs://cytognosis-data-hub/processed/cytos/dvc/  (default)
```

To add a new project:
```bash
cd ~/repos/cytognosis/<project>
dvc remote add -d data-hub gs://cytognosis-data-hub/processed/<project>/dvc/
```

## GCS Bucket Organization

```
gs://cytognosis-data-hub/
├── dvc-cache/                 # Content-addressed DVC cache (md5 → blob)
│                                Shared across all projects
├── processed/
│   └── cytos/dvc/             # cytos project DVC remote
├── purdue/
│   ├── active/                # Collaborator active workspace
│   └── delivered/             # Finalized deliveries
├── shared/
│   ├── soma/                  # TileDB-SOMA exports
│   ├── gwas/                  # GWAS summary statistics
│   ├── embeddings/            # Feature vectors
│   └── reference/             # GRCh38, GENCODE GTFs
├── public-mirror/             # Public dataset mirrors
└── manifests/                 # Dataset manifest JSONs (interim catalog)
```

## Common Workflows

### Track a new dataset

```bash
cd ~/datasets
dvc add 01-ontologies/go/go-plus.owl
git add 01-ontologies/go/go-plus.owl.dvc .gitignore
git commit -m "feat: track GO-Plus ontology via DVC"
dvc push
git push
```

### Pull a dataset on another machine

```bash
git clone git@github.com:cytognosis/datasets.git
cd datasets
dvc pull  # Downloads from gs://cytognosis-data-hub/dvc-cache/
```

### Check what's tracked

```bash
dvc status           # Show which files have changed
dvc diff             # Show diff between commits
dvc data status      # Show DVC-tracked files
```

### Run the cytos KG pipeline

```bash
cd ~/repos/cytognosis/cytos
dvc repro            # Run all pipeline stages
dvc repro topic_areas  # Run a single stage
```

## Pipeline Stages (cytos)

The cytos KG build pipeline (`dvc.yaml`) has 10 stages:

| Stage | Description | Dependencies |
|-------|-------------|-------------|
| `topic_areas` | Topic area ontology ingestion | `05-annotations/topic-areas/` |
| `monarch_merge` | Monarch KG merge | `monarch-kg.duckdb` |
| `primekg_convert` | PrimeKG conversion | `kg.csv` |
| `opentargets_ingest` | Open Targets ingestion | `open-targets/25.03/` |
| `unichem_xrefs` | UniChem cross-references | `UniChem/reference.tsv` |
| `normalize_predicates` | Predicate normalization | `edges.tsv` |
| `reclassify_nodes` | Node reclassification | `nodes.tsv` |
| `neo4j_export` | Neo4j bulk import | All node/edge files |
| `rocrate` | RO-Crate metadata generation | `nodes.tsv`, `edges.tsv` |
| `test` | Pipeline tests | Test files + data |

## Integration with Provenance Stack

DVC operates at Layer 0 (Data Versioning) of the 5-layer provenance architecture:

```
L0: DVC + VFS         ← Content-addressed hashes, SWHID for code
L1: redun / Nextflow  ← Workflow DAG lineage
L2: Artifact Registry ← Queryable metadata
L3: MLflow            ← Experiment tracking
L4: RO-Crate          ← FAIR publication packages
```

DVC md5 hashes are embedded in:
- W3C PROV-J provenance sidecars (`.provenance.yaml`)
- RO-Crate metadata (`ro-crate-metadata.json`)
- Dataset manifest files (`manifests/<dataset>.manifest.json`)

## Authentication

DVC uses gcloud Application Default Credentials (ADC):

```bash
gcloud auth application-default login
# This creates ~/.config/gcloud/application_default_credentials.json
```

For CI/CD, use Workload Identity Federation (OIDC) or a service account key.
