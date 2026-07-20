# Integration Details: DagsHub, LaminDB, redun, DVC, scDataLoader, TileDB

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `product`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> All code examples are from actual documentation or verified repos, not invented.

---

## 1. DagsHub: What It Actually Is

**DagsHub is a SaaS wrapper around tools you already have.**

| What DagsHub provides | What you already use | Same thing? |
|---|---|---|
| Git hosting | GitHub | YES — DagsHub mirrors GitHub repos |
| DVC remote storage | GCS bucket (`gs://cytognosis-data-hub/`) | YES — DagsHub hosts a DVC remote for you |
| MLflow tracking server | Self-hosted MLflow on cytohost | YES — DagsHub runs an MLflow instance per repo |
| Label Studio integration | Nothing | **NEW** — image/text annotation tool |
| Data Engine (query unstructured data) | Nothing | **NEW** — SQL-like queries over dataset metadata |
| Collaboration UI | GitHub UI | Similar, with ML-specific features (diff data, preview notebooks) |

**Pricing**: Free tier (1 user, 10GB), $9/user/mo (Pro), $119/user/mo (Team with Data Engine).

**Verdict**: You already run GitHub + DVC + MLflow. DagsHub would eliminate self-hosting MLflow and managing your own DVC remote, but at $119/user/mo for the full features. The Data Engine and Label Studio are genuinely new capabilities, but not priorities for Cytognosis right now.

**DagsHub ML Workspace**: A Docker image (`dagshub/ml-workspace`) bundling Jupyter + VS Code + TensorBoard + SSH. Fork of `ml-tooling/ml-workspace`. Last meaningful commit: July 2024. **Dead project. Skip.**

---

## 2. LaminDB ↔ redun: How They Actually Interface

**Integration type**: Semi-native. There is a dedicated example repo [`laminlabs/redun-lamin`](https://github.com/laminlabs/redun-lamin), but **no automatic plugin**. You write glue code.

**The core pattern**: You call `ln.track()` at the start of your redun entry point, register artifacts with `ln.Artifact()` as they're produced, and call `ln.finish()` at the end. LaminDB does NOT auto-capture redun's call graph.

```python
import lamindb as ln
from redun import task

# ─── A normal redun task: does NOT know about LaminDB ───
@task()
def preprocess(input_path: str) -> str:
    import pandas as pd
    df = pd.read_csv(input_path)
    df = df.dropna()
    output_path = "processed.parquet"
    df.to_parquet(output_path)
    return output_path

# ─── A redun task that registers output in LaminDB ───
@task()
def register_output(output_path: str):
    artifact = ln.Artifact(
        output_path,
        key=f"pipeline/results/{output_path}",
        description="Preprocessed training data",
    ).save()
    return artifact

# ─── Entry point: starts LaminDB tracking ───
@task()
def main(input_path: str):
    ln.track()  # Creates a Transform + Run in LaminDB
    
    output_path = preprocess(input_path)
    artifact = register_output(output_path)
    
    ln.finish()  # Closes the Run
    return artifact
```

**What LaminDB captures from this**:
- A `Transform` record (the script/notebook identity)
- A `Run` record (this specific execution, with timestamp, user, environment)
- An `Artifact` record linked to the Run (the output file, with hash, size, type)
- Feature annotations if you add them (via Bionty ontologies)

**What LaminDB does NOT capture**:
- redun's call graph (which tasks called which)
- redun's AST hashes (code change detection)
- redun's cache hits/misses
- Intermediate results between tasks

**The CytognosisExecutor design** in [provenance-lineage.md](../../04-Engineering/infrastructure/reproducibility/provenance-lineage.md) proposes a deeper integration — a custom redun Executor that calls `log_to_lamindb()` after EVERY task, not just at the entry point. That's custom glue code we would write:

```python
# FROM OUR DESIGN DOC (not yet implemented)
class CytognosisExecutor(Executor):
    def submit(self, job):
        result = self.run(job, image)
        # ... hash outputs, emit RO-Crate ...
        log_to_lamindb(job, result, crate)  # ← per-task registration
        log_to_mlflow(job, result)
```

**LaminDB's own decorator alternative** (no redun needed):

```python
import lamindb as ln

@ln.step()  # LaminDB's own lightweight pipeline decorator
def subset_data(data: ln.Artifact, feature_name: str):
    df = data.to_df()
    subset_df = df[[feature_name]]
    return ln.Artifact.from_df(subset_df, key="subsetted.parquet")

@ln.flow()  # LaminDB's own entry-point decorator
def my_pipeline(input_key: str, feature: str):
    input_artifact = ln.Artifact.get(key=input_key)
    result = subset_data(input_artifact, feature)
    return result
```

> [!WARNING]
> Do NOT use `@ln.flow()` on a redun `@task()` function — they conflict. Use `ln.track()`/`ln.finish()` when inside redun.

---

## 3. redun ↔ DVC: How They Interface

**Integration type**: **ZERO native integration.** They are completely independent tools. You write manual glue code.

**Pattern: redun consuming DVC-tracked data**

```python
from redun import task
import dvc.api

@task()
def load_dvc_data(dvc_path: str, git_rev: str = "main") -> str:
    """Resolve a DVC-tracked file to its actual storage URL."""
    # dvc.api.get_url resolves the .dvc pointer to the actual GCS/S3 URL
    data_url = dvc.api.get_url(
        path=dvc_path,
        repo="~/repos/cytognosis/cytos",
        rev=git_rev,
    )
    return data_url

@task()
def process(data_url: str) -> str:
    import pandas as pd
    df = pd.read_parquet(data_url)
    # ... process ...
    output = "output.parquet"
    df.to_parquet(output)
    return output

@task()
def main():
    url = load_dvc_data("data/kg/nodes.tsv", git_rev="v0.4.0")
    return process(url)
```

**Pattern: DVC tracking redun outputs** (post-hoc):

```python
@task()
def track_with_dvc(output_path: str) -> str:
    """After redun produces output, add it to DVC."""
    import subprocess
    subprocess.run(["dvc", "add", output_path], check=True)
    subprocess.run(["dvc", "push"], check=True)
    return output_path
```

**Why they coexist without deep integration**: redun has its own content-addressed cache (hashes code AST + data). DVC has its own content-addressed cache (hashes file content). They serve different purposes:
- **DVC**: "Give me version X of this dataset" (data versioning, tied to Git)
- **redun**: "Skip this computation because the code+inputs haven't changed" (execution caching, tied to function ASTs)

They overlap in hashing data but for different reasons. Neither project has any plans to integrate with the other.

---

## 4. scDataLoader ↔ LaminDB: Native First-Class Integration

**What scDataLoader is**: A PyTorch/Lightning DataModule for single-cell RNA-seq data, built by Jérémie Kalfon. Used by [scPRINT](https://github.com/jkobject/scPRINT) (a single-cell foundation model). It is built ON TOP of LaminDB — LaminDB is not optional.

**The data flow**:

```
CELLxGENE Census (TileDB-SOMA)
    ↓ ingested into
LaminDB Collection (many AnnData Artifacts)
    ↓ streamed via
MappedCollection (memory-efficient, no full load)
    ↓ wrapped by
scDataLoader DataModule (PyTorch DataLoader)
    ↓ consumed by
PyTorch Lightning Trainer (GPU training)
```

**Concrete code**:

```python
from scdataloader import DataModule

# This single call does everything:
# 1. Finds the LaminDB Collection by name
# 2. Opens it as a MappedCollection (streaming, not loading into RAM)
# 3. Wraps it in a PyTorch DataLoader with batching/shuffling
# 4. Uses Bionty ontologies for label encoding (cell types → integers)
datamodule = DataModule(
    collection_name="preprocessed dataset",   # LaminDB Collection key
    organisms=["NCBITaxon:9606"],             # Human (NCBI Taxonomy via Bionty)
    max_len=1000,                              # Top 1000 genes
    batch_size=64,
    num_workers=4,
    validation_split=0.1,
)
datamodule.setup()

# Standard PyTorch Lightning usage
for batch in datamodule.train_dataloader():
    x = batch["X"]           # Gene expression tensor [64, 1000]
    labels = batch["cell_type"]  # Ontology-backed integer labels
    # ... train model ...
```

**What happens under the hood**:

```python
import lamindb as ln

# scDataLoader calls this internally:
collection = ln.Collection.get(key="preprocessed dataset")

# Then uses MappedCollection for zero-copy streaming
with collection.mapped(obs_keys=["cell_type"], join="inner") as mapped:
    # mapped[i] returns a dict with "X" and metadata
    # No full AnnData loading — reads only requested slices
    print(mapped.shape)   # e.g. (500000, 20000)
    sample = mapped[0]    # Single cell: {"X": array, "cell_type": "T cell"}
```

**Preprocessing** (also LaminDB-native):

```python
from scdataloader import LaminPreprocessor

preprocessor = LaminPreprocessor(
    collection_name="raw_cellxgene",
    organisms=["NCBITaxon:9606"],
    do_gene_selection=True,
    n_top_genes=2000,
)
preprocessor.preprocess()
# Creates a NEW LaminDB Collection "preprocessed dataset"
# with normalized, filtered AnnData Artifacts
```

---

## 5. LaminDB ↔ TileDB-SOMA: Native First-Class Integration

LaminDB has **dedicated APIs** for TileDB-SOMA. This is how CELLxGENE Census data gets managed.

**Pattern 1: Save AnnData as SOMA Experiment via LaminDB**

```python
import lamindb as ln
import anndata as ad

ln.track()

adata = ad.read_h5ad("my_data.h5ad")

# This converts AnnData → TileDB-SOMA AND registers in LaminDB
soma_artifact = ln.integrations.save_tiledbsoma_experiment(
    [adata],                          # Can pass multiple AnnData objects
    description="RNA-seq experiment",
    measurement_name="RNA",
    obs_id_name="obs_id",
    var_id_name="var_id",
)
# soma_artifact is now an ln.Artifact backed by TileDB-SOMA on disk/cloud
```

**Pattern 2: Open and query a SOMA Artifact**

```python
artifact = ln.Artifact.get(description="RNA-seq experiment")

# Open returns a tiledbsoma.Experiment — full SOMA API available
with artifact.open() as experiment:
    # Query observation metadata
    obs_df = experiment.obs.read(
        column_names=["cell_type", "tissue"],
    ).concat().to_pandas()
    
    # Slice expression matrix
    X = experiment.ms["RNA"].X["data"]
    # Efficient: reads only requested rows/columns from disk
```

**Pattern 3: Validate with ontologies before saving**

```python
import lamindb as ln
import bionty as bt
from lamindb.curators import TiledbsomaExperimentCurator

ln.track()

# Define what the SOMA experiment MUST contain
obs_schema = ln.Schema(
    name="cell_obs_schema",
    features=[
        ln.Feature(name="cell_type", dtype=bt.CellType).save(),
        ln.Feature(name="tissue", dtype=bt.Tissue).save(),
        ln.Feature(name="disease", dtype=bt.Disease).save(),
    ],
).save()

# Validate against ontologies BEFORE saving
curator = TiledbsomaExperimentCurator(
    dataset="path/to/experiment",
    schema=obs_schema,
)
curator.validate()  # Raises if cell types/tissues don't match ontology

# Save validated experiment
artifact = curator.save_artifact(description="Validated scRNA-seq")
```

**What other storage backends does LaminDB support?**

| Backend | How LaminDB uses it | Status |
|---|---|---|
| **Local filesystem** | Default. Artifacts stored in `~/.lamindb/` | ✅ Native |
| **AWS S3** | `ln.setup.storage.set("s3://bucket")` | ✅ Native |
| **GCS** | `ln.setup.storage.set("gs://bucket")` | ✅ Native |
| **TileDB-SOMA** | `ln.integrations.save_tiledbsoma_experiment()` | ✅ Native |
| **AnnData (h5ad)** | `ln.Artifact(adata)` directly | ✅ Native |
| **Parquet/DataFrame** | `ln.Artifact.from_df(df)` | ✅ Native |
| **Zarr** | Via AnnData's Zarr backend | ⚠️ Indirect |
| **TileDB arrays (non-SOMA)** | No dedicated API | ❌ Manual |

---

## 6. TileDB Cloud: What It Adds Over Open-Source TileDB

**Open-source TileDB** (MIT license) = a storage engine. Stores multi-dimensional arrays on disk/S3/GCS with ACID transactions, versioning (time-travel), and compression.

**TileDB Cloud** (proprietary, $50K-$250K+/yr) = a managed platform that adds:

| Feature | Open-source TileDB | TileDB Cloud adds |
|---|---|---|
| **Storage** | Local/S3/GCS arrays | Same, but managed |
| **Versioning** | Time-travel (native) | Same |
| **Compute** | None — you run your own code | **Serverless UDFs**: run Python/R functions ON the data without moving it |
| **Task graphs** | None | **DAG-based orchestration**: chain UDFs into pipelines |
| **Catalog** | None | **Asset catalog**: browse arrays, groups, UDFs with ACLs |
| **Sharing** | None | **Multi-user ACLs**: share arrays/UDFs with specific users/orgs |
| **Notebooks** | None | **Hosted Jupyter**: notebooks that run UDFs on TileDB Cloud infra |
| **Audit** | None | **Access logging**: who accessed what, when |
| **TileDB-VCF** | CLI tool for VCF → array | **Population genomics platform**: ingest → store → query → analyze VCFs at cohort scale |
| **TileDB-SOMA** | Python library | **Managed single-cell**: CELLxGENE-style queries without self-hosting |

**TileDB Cloud UDF example** (the compute layer):

```python
import tiledb.cloud

# Define a function that runs ON TileDB Cloud (serverless)
def analyze_vcf(vcf_uri: str, region: str):
    import tiledb
    import tiledbvcf
    ds = tiledbvcf.Dataset(vcf_uri)
    df = ds.read(regions=[region], attrs=["sample_name", "alleles", "fmt_DP"])
    return df.describe()

# Execute remotely — data never leaves TileDB Cloud
result = tiledb.cloud.udf.exec(
    analyze_vcf,
    vcf_uri="tiledb://my-org/ukb-wgs-500k",
    region="chr17:7571720-7590868",  # TP53 region
    namespace="my-org",
)
```

**TileDB Cloud task graph** (the orchestration layer):

```python
import tiledb.cloud
from tiledb.cloud.dag import DAG

dag = DAG(name="vcf_analysis", namespace="my-org")

# Stage 1: ingest VCFs
ingest = dag.submit(ingest_vcf, vcf_paths=["s3://..."], name="ingest")

# Stage 2: QC (depends on ingest)
qc = dag.submit(run_qc, depends_on=[ingest], name="qc")

# Stage 3: Analysis (depends on QC)
analyze = dag.submit(analyze_cohort, depends_on=[qc], name="analyze")

# Execute the DAG
dag.compute()
dag.wait()
```

**How TileDB Cloud overlaps with our stack**:

| Our tool | TileDB Cloud overlap | Who wins? |
|---|---|---|
| **DVC** | TileDB has time-travel versioning | **DVC** — TileDB only versions arrays, not arbitrary files |
| **redun** | TileDB has DAG task graphs | **redun** — AST hashing, pluggable executors, content-addressed cache. TileDB DAGs are simple job chains |
| **LaminDB** | TileDB has an asset catalog | **LaminDB** — ontology-grounded features, lineage graph, Bionty. TileDB catalog is just name/ACL |
| **MLflow** | TileDB can store artifacts | **MLflow** — dedicated experiment tracking UI, model registry. TileDB has no ML-specific features |
| **GCS** | TileDB Cloud hosts data | **GCS** — we already pay for it, no lock-in |

**Verdict**: Use open-source TileDB Embedded (MIT) for TileDB-VCF and TileDB-SOMA on our own GCS. Skip TileDB Cloud ($50K+/yr) — its compute/catalog/orchestration features are weaker than our dedicated tools.

---

## 7. Summary: What Integrates Natively vs What Needs Glue

```
                    NATIVE                          GLUE CODE
                    ──────                          ──────────
LaminDB ↔ TileDB-SOMA    ✅ First-class API        
LaminDB ↔ AnnData        ✅ First-class API        
scDataLoader ↔ LaminDB   ✅ Built on top of it     
LaminDB ↔ redun          ⚠️ Example repo exists    Manual ln.track()/finish()
LaminDB ↔ MLflow                                    Manual log_to_mlflow()
redun ↔ DVC                                         Manual dvc.api calls
redun ↔ RO-Crate         ⚠️ redun_rocrate.py       124 LOC bridge (exists in cytos)
DVC ↔ Git                ✅ First-class             
```

The tools that are natively integrated (LaminDB ↔ SOMA, scDataLoader ↔ LaminDB) just work. The tools that need glue (LaminDB ↔ redun, redun ↔ DVC) require the `CytognosisExecutor` custom code we've designed but not yet built.
