# LaminDB, LaminHub, and scDataLoader: Deep Analysis

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, data scientists
> **Tags**: `lamindb`, `provenance`, `data-lakehouse`, `single-cell`, `ml`

**Origin**: Imported from `https://github.com/cytognosis/org/blob/main/plans/research/lamindb-deep-analysis.md` (Antigravity session, 2026-05-24). Revised to cytognosis-doc evaluation template.

> [!NOTE]
> **If you only read one section**: §1 (Executive Summary) and §9.3 (Recommended Integration Strategy).

---

## 1. Executive Summary

LaminDB is a lineage-native data lakehouse built specifically for biological R&D. Created by Alex Wolf (creator of Scanpy) and Sunny Sun, it provides a metadata registry layer (Django ORM on Postgres/SQLite) over cloud/local storage, with first-class support for biological ontologies (via bionty), data provenance tracking, and biological data formats (AnnData, zarr, TileDBSOMA, SpatialData, MuData).

**Key findings for Cytognosis:**

- LaminDB's provenance tracking is significantly more mature than our current W3C PROV-J sidecar approach in cytoskeleton VFS.
- Bionty (LaminDB's ontology module) overlaps substantially with our cytos KG ontology registry but uses a simpler, flatter model.
- The `MappedCollection` interface for virtual concatenation of AnnData files is directly relevant to our single-cell foundation model training pipeline.
- scDataLoader builds on LaminDB's `MappedCollection` to provide PyTorch Lightning DataModules for large-scale model training.
- LaminHub (the proprietary SaaS layer) provides UI, collaboration, and access control that we would need to build ourselves if using only the open-source core.

**Recommendation**: Adopt LaminDB as the metadata/provenance layer. Keep our cytos KG for deep ontology reasoning. Evaluate scDataLoader for ML data loading.

---

## 2. Background: Lamin Labs

Founded 2022 by **Alex Wolf** (creator of Scanpy) and **Sunny Sun** (formerly Head of Computational Biology at Cellarity). Y Combinator S22. Offices in Munich and New York.

Mission: solve the "bottleneck of closing the feedback loop across heterogeneous biological data modalities." LaminDB functions as "git for R&D data."

**Ecosystem packages:**

| Package | Purpose |
|:--------|:--------|
| `lamindb` | Core library: API, lineage tracking, artifact management |
| `lnschema-core` | Core metadata schema (Django ORM models) |
| `lamindb-setup` | Instance initialization, LaminHub client |
| `bionty` / `lnschema-bionty` | Biological ontology registries (Gene, Protein, CellType, etc.) |
| `wetlab` | Wet-lab registries (Experiment, Well, Biosample, etc.) |

---

## 3. Core architecture

### 3.1 Data model

```
Transform (code/pipe)  ─creates→  Run (execution)
                                       │
                                inputs/outputs
                                       │
                                  Artifact (data/model)
                                       │
                                   grouped by
                                       │
                                  Collection (dataset)
```

- **Artifact**: Core object representing datasets and models. Has content hash, suffix, size, storage location.
- **Collection**: Versioned grouping of multiple artifacts.
- **Transform**: The code or process that creates/manipulates data. Versioned.
- **Run**: An execution of a Transform. Links inputs and outputs automatically.

### 3.2 Provenance tracking

```python
import lamindb as ln

ln.track()  # Creates Transform + Run; any artifacts saved are linked

artifact = ln.Artifact("output.h5ad", key="processed/my-data.h5ad")
artifact.save()
# artifact.run → the Run that created it
# artifact.run.transform → the Transform (code) that was executed
```

Supports automatic Git sync (`ln.settings.sync_git_repo`), input/output tracking, parameter capture via `@ln.flow()` and `@ln.step()` decorators, and environment tracking.

---

## 4. Unique capabilities

### 4.1 Provenance comparison

| Aspect | LaminDB | DVC | MLflow | Cytoskeleton VFS |
|:-------|:--------|:----|:-------|:----------------|
| Primary focus | Data lakehouse / Biology | Data/model versioning | MLOps lifecycle | Standards-compliant VFS |
| Lineage approach | SQL-based registry | Git-like hashes | Run-centric | W3C PROV-J sidecars |
| Bio-data support | First-class | File-agnostic | File-agnostic | File-agnostic |
| Ontology integration | Built-in via bionty | None | None | None |
| Queryable lineage | Yes (SQL) | Limited | Yes | No (individual JSON files) |

### 4.2 Bionty ontology coverage

20+ public biological ontologies: Gene (Ensembl, NCBI), Protein (UniProt), CellType (CL), Tissue (Uberon), Disease (Mondo, ICD), Organism (NCBI Taxonomy), Phenotype (HPO), Pathway (GO), ExperimentalFactor (EFO), and more.

**Comparison with cytos KG:**

| Aspect | Bionty (LaminDB) | Cytos KG |
|:-------|:-----------------|:---------|
| Data model | Flat registries (SQL tables per entity) | KGX-format graph (nodes.tsv + edges.tsv) |
| Storage | Django ORM (Postgres/SQLite) | DuckDB + Polars DataFrames |
| Ontologies | 20+ | 16+ (CL, Uberon, Mondo, HP, CHEBI, EFO, etc.) |
| Cross-ontology | Limited (per-entity lookups) | SSSOM mappings, UMLS normalized |
| Reasoning | No graph traversal | BioLink model categories, hierarchical relationships |
| Unique strength | Integrated data validation | Deep semantic integration, graph traversal |

**Recommendation**: Use bionty for data curation and validation ("is this cell type name valid?"). Keep cytos KG for deep reasoning ("what diseases are associated with this cell type through which pathways?").

### 4.3 MappedCollection for ML training

```python
collection = ln.Collection.get(key="my-sc-collection")
with collection.mapped(obs_keys=["cell_type"], join="inner") as dataset:
    loader = DataLoader(dataset, batch_size=32, num_workers=4)
```

This enables virtual concatenation of thousands of AnnData files without loading into memory. scDataLoader wraps this into a PyTorch Lightning DataModule.

---

## 5. Storage backends

LaminDB supports local filesystem, AWS S3, GCS, Azure Blob, HuggingFace — all via `fsspec`. Storage root is defined at instance init:

```bash
lamin init --storage gs://cytognosis-data-hub/lamindb
```

**Comparison with cytoskeleton VFS:**

| Aspect | LaminDB | Cytoskeleton VFS |
|:-------|:--------|:----------------|
| Backend abstraction | fsspec-based | Abstract base class with LocalVFS, S3VFS, GCSVFS |
| Content addressing | SHA256 hash | SWHID (ISO 18670:2025) |
| Provenance per file | Linked via Run in database | `.prov.json` sidecar (W3C PROV-J) |
| Manifest | SQL database | `store.yaml` + RO-Crate 1.2 |
| Standards | Proprietary Django schema | W3C PROV, SWHID, RO-Crate |

---

## 6. LaminHub SaaS layer

LaminHub provides: web UI for browsing/searching, lineage visualization, LIMS and ELN integration, versioning UI, GitHub-like collaboration, auto-generated REST API.

| Tier | Storage | Collaboration | Security |
|:-----|:--------|:-------------|:---------|
| Free | Personal instances | Limited | Basic |
| Team | Team instances | Full | SOC2 |
| Enterprise | Custom | SSO, RBAC, audit logs | HIPAA, VPC, ISO27001 |

**Assessment**: LaminHub is valuable for UI/collaboration but creates a SaaS dependency. For Cytognosis as a nonprofit, evaluate free tier first and build a minimal UI ourselves using LaminDB's REST API if needed.

---

## 7. scDataLoader for foundation model training

scDataLoader is a PyTorch Lightning `DataModule` for training single-cell foundation models (scPRINT). Key features:

- Stream thousands of datasets containing millions of cells without loading into memory.
- Per-dataset preprocessing (normalization, gene selection) with bionty metadata harmonization.
- Hierarchical loss support using ontology graphs.
- Automatic train/val/test splits.

```python
from scdataloader import DataModule

datamodule = DataModule(
    collection_name="my-training-data",
    obs_keys=["cell_type", "organism"],
    batch_size=256,
    num_workers=8,
)
```

**Assessment**: scDataLoader is directly relevant to our single-cell foundation model training pipeline. Adopt alongside LaminDB if we adopt LaminDB.

---

## 8. Integration assessment

### 8.1 Overlap and conflict areas

| Area | Our system | LaminDB | Conflict level |
|:-----|:-----------|:--------|:---------------|
| File storage abstraction | cytoskeleton VFS | fsspec + Artifact | Low (complementary layers) |
| Provenance tracking | W3C PROV-J sidecars | Run → Transform → Artifact | Low (LaminDB is superset) |
| Content addressing | SWHID | SHA256 hash | Low (different schemes, both work) |
| Ontology lookup | cytos ontology registry | bionty | Medium (overlapping ontology sets) |
| Knowledge graph | cytos KG builder | None (bionty is flat) | None |
| Data curation | None (ad-hoc) | ln.curators | None (we gain capability) |
| ML data loading | None (custom) | MappedCollection + scDataLoader | None (we gain capability) |

### 8.2 Recommended integration strategy

**Phase 1 (Weeks 1–2)**: Install LaminDB in development. Create test instance with our single-cell datasets. Validate bionty coverage against `registry.yaml`. Test MappedCollection with our `.h5ad` files.

**Phase 2 (Weeks 3–4)**: Build thin adapter layer `cytoskeleton.lamindb` mapping our VFS concepts to LaminDB. Create bridge between bionty registries and cytos KG. Implement RO-Crate export from LaminDB instances.

**Phase 3 (Weeks 5–6)**: Migrate single-cell data catalog to LaminDB. Set up curation workflows. Integrate scDataLoader into model training pipeline. Set up LaminDB instance on GCS storage.

**Phase 4 (Weeks 7–8)**: Evaluate LaminHub vs. building our own UI. Performance testing. Document the integrated architecture. Decide on long-term relationship.

---

## 9. Strategic decisions

| Decision | Recommendation | Rationale |
|:---------|:---------------|:----------|
| Use LaminDB for metadata/provenance? | **Yes** | More mature than building our own; open-source; biology-native |
| Replace cytoskeleton VFS? | **No — adapt** | Keep as low-level primitive; build LaminDB adapter on top |
| Replace cytos KG with bionty? | **No** | Different purposes: bionty for curation, cytos KG for reasoning |
| Use scDataLoader for ML? | **Yes — evaluate** | Directly addresses our data loading needs |
| Subscribe to LaminHub? | **Defer** | Evaluate free tier first |
| Contribute upstream? | **Yes** | Contribute RO-Crate export, SWHID support |

### 9.1 Architecture vision

```
Cytognosis Platform
├── cytos KG (deep ontology reasoning)  ←── LaminDB Core (metadata + provenance)  ──→  scDataLoader (ML)
│                                                    │
│                                              bionty (curation)
│                                                    │
└───────────────── cytoskeleton VFS (storage abstraction) ──────────────────────────
                              │
         Storage: GCS (us-central1) / Local (Strix Halo)
         Database: PostgreSQL (production) / SQLite (development)
```

### 9.2 Key principles

1. **Adopt, don't fork**: Use LaminDB as a dependency, contribute improvements upstream.
2. **Layer, don't replace**: LaminDB sits above our VFS; cytos KG operates independently.
3. **Standards first**: Maintain W3C PROV, SWHID, RO-Crate compliance as export formats.
4. **Open-source only**: Use LaminDB core (Apache-2.0); evaluate but don't depend on LaminHub SaaS.
5. **Incremental migration**: New data goes through LaminDB; existing data migrated over time.

---

## 10. Risk analysis

| Risk | Severity | Likelihood | Mitigation |
|:-----|:---------|:-----------|:-----------|
| Vendor dependency on Lamin Labs | Medium | Medium | Use only open-source LaminDB core |
| Schema migration complexity | Medium | High | Start fresh with LaminDB for new data; migrate incrementally |
| Bionty / cytos KG conflicts | Low | Medium | Use bionty for curation, cytos KG for reasoning; build bridge |
| Learning curve for team | Medium | High | LaminDB API is Pythonic and well-documented |
| API breaking changes | Medium | Medium | Pin versions; LaminDB follows semver |

---

## Related docs

- [data-infrastructure-overview.md](data-infrastructure-overview.md)
- [TECHNICAL_DATA_INFRASTRUCTURE.md](TECHNICAL_DATA_INFRASTRUCTURE.md)
- [tiledbvcf-hail-assessment.md](tiledbvcf-hail-assessment.md)
- [storage-architecture.md](../storage-architecture.md)

## References

- LaminDB Documentation: https://docs.lamin.ai
- LaminDB GitHub: https://github.com/laminlabs/lamindb
- Bionty Documentation: https://docs.lamin.ai/bionty
- scDataLoader GitHub: https://github.com/jkobject/scDataLoader
- scPRINT Paper: Kalfon et al., "scPRINT: pre-training on 50M cells for gene network inference"
