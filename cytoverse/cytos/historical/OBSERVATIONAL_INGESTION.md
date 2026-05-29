# Observational Data Ingestion Architecture

> Last updated: 2026-05-12 | Status: IMPLEMENTING

## Overview

This document defines the ingestion pipeline for observational data into the Cytos
Observation Graph. Observational data are empirical measurements produced by Sensors
(assays) at Locations (tissues), conforming to Schemas (data standards).

## Sensor Triple Applied

```
Sensor (WHAT)          → Location (WHERE)         → Schema (HOW)
─────────────────────────────────────────────────────────────────
snRNA-seq (OBI:0003109) → DLPFC (UBERON:0000451)  → cellxgene v5.2
GWAS array (OBI:0001271)→ whole body (UBERON:0013702)→ GWAS-SSF v1.0
WGS (OBI:0002117)      → whole body              → VRS v2.0 + VCF v4.2
```

## Data Sources

### Single-Cell RNA-seq

| Dataset | Location | Cells | Tissue | Disease | Status |
|---------|----------|------:|--------|---------|--------|
| HBCA cortex sample | `05-annotations/cellxgene/hbca/` | 28,051 | Brain cortex | Healthy | ✅ SOMA exists |
| PEC CMC | `08-neuroimaging/PEC/synapse/rna/CMC/` | ~200K | DLPFC | SCZ+Control | To ingest |
| PEC SZBDMulti-Seq | `08-neuroimaging/PEC/synapse/rna/SZBDMulti-Seq_update_Feb2023/` | ~150K | DLPFC | SZ+BD | To ingest |
| PEC DevBrain | `08-neuroimaging/PEC/synapse/rna/DevBrain-snRNAseq/` | ~100K | Brain | Developmental | To ingest |
| PEC UCLA-ASD | `08-neuroimaging/PEC/synapse/rna/UCLA-ASD/` | ~100K | Brain | ASD | To ingest |

### Genotype Data

| Dataset | Type | Location | Variants | Disease | Status |
|---------|------|----------|----------|---------|--------|
| PGC SCZ 2022 | GWAS summary stats | `06-genotype/gwas/scz2022.zip` | ~10M | Schizophrenia | To ingest |
| PGC BIP 2024 | GWAS summary stats | `06-genotype/gwas/bip2024.zip` | ~10M | Bipolar | To ingest |
| PGC ADHD 2022 | GWAS summary stats | `06-genotype/gwas/adhd2022.zip` | ~10M | ADHD | To ingest |
| PGC ASD 2019 | GWAS summary stats | `06-genotype/gwas/asd2019.zip` | ~10M | ASD | To ingest |
| PGC PTSD 2024 | GWAS summary stats | `06-genotype/gwas/ptsd2024.zip` | ~10M | PTSD | To ingest |
| Olivia WGS | Individual WGS VCF | `06-genotype/personal/Olivia/` | ~5M | Individual | To ingest |
| PEC WGS | Multi-sample VCF | `08-neuroimaging/PEC/synapse/genotype/` | ~2M | SCZ cohort | To ingest |

## Storage Backends

### TileDB-SOMA (Single-Cell)

Each dataset → one SOMAExperiment:
- `obs`: Cell metadata DataFrame (CellxGene schema fields)
- `var`: Gene metadata DataFrame
- `X/data`: Expression matrix (sparse CSR)
- `obsm/X_umap`: Embeddings

### TileDB-VCF (Genotypes)

Two stores:
- **Individual VCF store**: Per-sample VCF files (Olivia, PEC WGS)
- **GWAS summary store**: Parquet-backed (not VCF) since GWAS are summary statistics

## BioCypher Integration

BioCypher is used as the **KG-linkage layer**, not the storage layer:

```python
# BioCypher generates nodes/edges that link observations to the semantic KG
bcy = BioCypher(
    schema_config="biocypher_config.yaml",
    biocypher_config="biocypher_docker_config.yaml",
)

# Adapter produces observation-to-entity edges
adapter = SingleCellAdapter(soma_path="hbca_cortex.soma")
bcy.add(adapter)

# Output: KGX edges like:
# (HBCA_cell_001, biolink:has_cell_type, CL:0000540)  # neuron
# (HBCA_cell_001, biolink:located_in, UBERON:0001384)  # primary motor cortex
# (HBCA_dataset, biolink:has_assay, OBI:0003109)       # snRNA-seq
```

## Pipeline Stages

```
1. EXTRACT: Read source format (h5ad, VCF, GWAS TSV)
2. VALIDATE: Check against schema (CellxGene 5.2, VRS 2.0)
3. STORE: Write to storage backend (TileDB-SOMA, TileDB-VCF)
4. LINK: Generate KG edges connecting observations to semantic entities
5. REGISTER: Add Dataset node to Catalog Graph with FAIR metadata
```
