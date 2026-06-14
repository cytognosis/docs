# Cytos Provenance & Data Management

> Last updated: 2026-05-12 | Provenance stack: **DVC + RO-Crate + Sidecars + Run History**

## 1. Data Manifest (`data/manifest.yaml`)

The manifest is the single source of truth for all data sources. It declares:

| Field | Purpose | Example |
|-------|---------|---------|
| `version` | Release identifier | `2026AA` |
| `release_date` | Official release date | `2026-05-01` |
| `license_class` | Access classification | `controlled` / `open` |
| `license_spdx` | SPDX license ID | `UMLS-License` |
| `parser` | Format parser type | `rrf`, `rf2`, `owl` |
| `raw_uri` | URI template to raw source | `${CYTOS_DATA_ROOT}/UMLS/...` |
| `parquet_uri` | URI template to processed Parquet | `${CYTOS_DATA_ROOT}/UMLS/parquet/2026AA` |
| `files` | Per-file metadata | description, expected row count |

## 2. Data Lake Organization (Canonical)

```
/home/mohammadi/datasets/             ← Git + DVC initialized
├── .dvc/                             ← DVC config
├── .gitignore                        ← Large files excluded, text files tracked
├── README.md                         ← Structure documentation
├── 01-ontologies/          75GB      ← OWL/OBO ontology files
├── 02-vocabularies/        76GB      ← UMLS, SNOMED CT, MeSH
├── 03-knowledge-graphs/   440GB      ← External KGs
├── 04-identifiers/        178GB      ← Cross-reference databases
├── 05-annotations/         12GB      ← CellxGene, HRA, topic areas
├── 06-genotype/           103GB      ← WGS/WES data
├── 07-single-cell/                   ← TileDB-SOMA stores
├── 08-neuroimaging/       319GB      ← BIDS/NWB datasets
├── 09-literature/                    ← Papers, BibTeX
├── 10-embeddings/          34GB      ← Pre-computed embeddings
├── 11-benchmarks/          23GB      ← Benchmark datasets
├── 12-network/            200GB      ← Biological networks
└── 13-cell-lines/                    ← Cell line reference data
```

Backward-compatible symlinks: `genotype` → `06-genotype`, `neuro` → `08-neuroimaging`, etc.

## 3. Provenance Layers

### Layer 1: DVC Pipeline (Active) ✅

DVC tracks 10 pipeline stages in `dvc.yaml`:

| Stage | Deps | Outs |
|-------|------|------|
| `topic_areas` | `05-annotations/topic-areas/` | `topic_nodes.tsv`, `topic_edges.tsv` |
| `monarch_merge` | `monarch-kg.duckdb` | `monarch_nodes.tsv`, `monarch_edges.tsv`, `monarch_mappings.tsv` |
| `primekg_convert` | `kg.csv` | `primekg_nodes.tsv`, `primekg_edges.tsv` |
| `opentargets_ingest` | `25.03/` | `opentargets_nodes.tsv`, `opentargets_edges.tsv` |
| `unichem_xrefs` | `reference.tsv` | `unichem_edges.tsv` |
| `neo4j_export` | All node/edge TSVs | Neo4j `cytos` database |
| `rocrate` | `nodes.tsv`, `edges.tsv` | `ro-crate-metadata.json` |
| `test` | Node TSVs + test file | pytest results |

### Layer 2: RO-Crate Metadata (Active) ✅

`data/kg/ro-crate-metadata.json` tracks 9 data sources with licenses:

| Source | License | Version |
|--------|---------|---------|
| Cytos Core | Various (OBO, UMLS, CC-BY) | 2026.05 |
| PKG2.0 | CC0 1.0 | 2.0 |
| Monarch | CC-BY 4.0 | 2025-03 |
| PrimeKG | CC-BY 4.0 | 1.0 |
| Open Targets | CC-BY 4.0 | 25.03 |
| UniChem | CC-BY-SA 3.0 | 2025-07 |
| AIO | CC-BY 4.0 | 2024 |
| CSO 3.5 | CC-BY 4.0 | 3.5 |
| ROADMAP | CC-BY 4.0 | 2024 |

17 TSV/JSON artifacts tracked with sizes, timestamps, and content types.

### Layer 3: Per-File Sidecars

Every Parquet file has a co-located `.provenance.yaml`:

```yaml
source: umls
source_version: 2026AA
release_date: '2026-05-01'
license_class: controlled
license_spdx: UMLS-License
sha256: f5bf89d001459f55...
file_size_bytes: 720380031
transform_step: parquet_conversion
retrieval_date: '2026-05-12'
agent: cytos
manifest_path: data/manifest.yaml
```

Coverage: 56 UMLS + 92 SNOMED = 148 provenance sidecars.

### Layer 4: Run History (Append-only)

Each KG build creates a timestamped log in `data/provenance/runs/`.

### Layer 5: Edge-Level Provenance

Every edge carries its source in the `provided_by` field:

| Edge Source | `provided_by` Value |
|-------------|---------------------|
| Ontology hierarchy | Source ontology prefix |
| UMLS broader/narrower | Source vocabulary SAB |
| Monarch | `monarch` |
| PrimeKG | `primekg` |
| Open Targets | `opentargets` |
| PlaNet | `planet` |
| UniChem | `unichem` |
| Ensembl xrefs | `ensembl_115` |
| SSSOM mappings | Mapping set source |
| Topic areas | `aio`, `cso3.5`, `roadmap` |
| PKG2.0 | `pkg2.0` |

## 4. New Release Adaptation

To update to UMLS 2027AA:

1. Download new release to `datasets/02-vocabularies/UMLS/umls-2027AA-metathesaurus-full/`
2. Run RRF → Parquet conversion
3. Update `params.yaml`: source paths
4. Run `dvc repro` to rebuild all downstream stages
5. Provenance sidecars auto-generated with new SHA-256 checksums
6. RO-Crate metadata auto-updated via `rocrate` stage

## 5. Infrastructure Status

| Tool | Role | Status |
|------|------|--------|
| **DVC** | Pipeline reproducibility, 10 stages | ✅ Active |
| **RO-Crate** | FAIR provenance packaging (9 sources) | ✅ Active |
| **Dagster** | Orchestration (5 assets, 3 jobs) | ✅ Installed |
| **Neo4j** | Graph database (80.7M rels) | ✅ Running |
| **GCS remote** | Cloud storage backend for DVC | ⬜ Planned |
