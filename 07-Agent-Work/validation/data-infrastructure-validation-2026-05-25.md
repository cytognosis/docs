# Data Infrastructure Validation Report

> **Date**: 2026-05-25 · **Author**: AI Agent (Antigravity)
> **Purpose**: Comprehensive validation of all data infrastructure components

---

## 1. Virtual File System (VFS)

### Test: Full Lifecycle (Put → Exist → Stat → Get → Verify → Delete)

| Operation | Input | Output | Status |
|-----------|-------|--------|--------|
| `LocalVFS(root=...)` | Test store path | VFS instance | ✅ |
| `vfs.put(source, uri, provenance)` | PrimeKG nodes.csv (7.87M) | URI string | ✅ |
| `vfs.exists(uri)` | URI | `True` | ✅ |
| `vfs.stat(uri)` | URI | size=7,869,553, prov_uri present | ✅ |
| `vfs.get(uri, target)` | URI + target path | File pulled | ✅ |
| SHA-256 verify | source vs pulled | Exact match | ✅ |
| Provenance sidecar | `.prov.json` | W3C PROV-J compliant | ✅ |
| `vfs.ls('')` | Store root | 1 asset (sidecars excluded) | ✅ |
| `vfs.delete(uri)` | URI | File removed | ✅ |

**Script**: `/home/mohammadi/repos/cytognosis/scratch/test_vfs_lifecycle.py`

> [!NOTE]
> API notes: URIs must be relative paths (no `cytognosis://` scheme). `put()`/`get()` take `Path` objects. `put()` returns a `str` URI.

---

## 2. RO-Crate Experiments

### Tracked (Formal) Experiment
- **Location**: `/home/mohammadi/repos/cytognosis/scratch/rocrate_experiments/formal_experiment`
- **Metadata**: 2,637 bytes, 6 graph entities
- **Entities**: Dataset, CreativeWork, Person, File, SoftwareApplication, CreateAction
- **Provenance**: Author, license (Apache-2.0), dateCreated, action/instrument chain
- **WRROC Profile**: ✅ Compliant

### Untracked (Sandbox) Experiment
- **Location**: `/home/mohammadi/repos/cytognosis/scratch/rocrate_experiments/sandbox_experiment`
- **Entities**: 3 (Dataset, CreativeWork, File)
- **Type**: `additionalType: https://w3id.org/cytognosis/SandboxExperiment`
- **Tracking**: `isPartOf: None` (explicitly untracked)

**Script**: `/home/mohammadi/repos/cytognosis/scratch/test_rocrate_experiment.py`

---

## 3. Provenance Verification

### UMLS 2026AA Parquet Provenance Coverage

| Metric | Value |
|--------|-------|
| Total Parquet files | 60 |
| With `.provenance.yaml` | 56 |
| Without provenance | 4 |
| **Coverage** | **93.3%** |
| SHA-256 correct | 56/56 (100%) |
| Attribution complete | 56/56 (100%) |
| Transform chain documented | 56/56 (100%) |
| Elapsed time | 4.7s (6.8 GB verified) |

**4 uncovered files** (supplementary tables in subdirectories):
1. `CHANGE/DELETEDCUI.parquet` (36 KB)
2. `CHANGE/MERGEDCUI.parquet` (11 KB)
3. `SemanticNetwork/SRDEF.parquet` (25 KB)
4. `SemanticNetwork/SRSTR.parquet` (7 KB)

**Script**: `/home/mohammadi/repos/cytognosis/scratch/test_provenance_verify.py`

---

## 4. UMLS/SnomedCT Reprocessing Validation

### 4.1 Dataset Registration

| Dataset | Version | Files | Size | Registration |
|---------|---------|-------|------|-------------|
| UMLS Metathesaurus | 2026AA | 56 RRF | 30.6 GB | `cytos/data/registrations/umls_2026AA_registration.yaml` |
| SnomedCT International | 20260501 | 46 RF2 | 3.6 GB | `cytos/data/registrations/snomedct_international_20260501_registration.yaml` |

### 4.2 Parquet Conversion — 100% Match

| Table | Parquet Rows | Source Lines | Compression | Status |
|-------|-------------|-------------|-------------|--------|
| MRCONSO | 18,064,970 | 18,064,970 | 3.25x | ✅ |
| MRREL | 66,241,184 | 66,241,184 | 4.97x | ✅ |
| MRMAP | 886,538 | 886,538 | 4.52x | ✅ |
| MRSTY | 3,876,927 | 3,876,927 | 5.24x | ✅ |
| MRRANK | 947 | 947 | — | ✅ |
| SNOMED concepts | 531,997 | 531,997 | — | ✅ |
| SNOMED descriptions | 1,704,584 | 1,704,584 | — | ✅ |
| SNOMED relationships | 3,564,963 | 3,564,963 | — | ✅ |
| **TOTAL** | **94,872,110** | **94,872,110** | | **0 mismatches** |

### 4.3 KGX Extraction — Exact Reproducibility

| Metric | Fresh Run | Existing Output | Delta |
|--------|-----------|-----------------|-------|
| Nodes | 2,921,330 | 2,921,330 | +0 |
| Edges | 3,629,365 | 3,629,365 | +0 |
| Nodes file | 275.4 MB | 275.5 MB | -0.1 MB |
| Edges file | 249.6 MB | 249.6 MB | +0.0 MB |
| Elapsed | 25.1s | — | — |

**Top SABs**: NCBI Taxonomy (780,948), SNOMEDCT_US (386,110), MeSH (355,278), LOINC (301,558), NCIt (200,820)

**Scripts**: 
- `/home/mohammadi/repos/cytognosis/scratch/test_umls_registration.py`
- `/home/mohammadi/repos/cytognosis/scratch/test_umls_parquet_validation.py`
- `/home/mohammadi/repos/cytognosis/scratch/test_umls_kgx_extraction.py`

---

## 5. Ontology Validation

### 5.1 Registry — 51/51 Present

- All 51 registered ontologies exist on disk (9.5 GB total)
- Top 3 by size: ncbitaxon (1.8 GB), pr (1.3 GB), chebi (774 MB)
- 0 flag mismatches between registry and filesystem

### 5.2 SSSOM Mapping Consolidation

| Source | Files | Data Files | Mapping Rows |
|--------|-------|------------|-------------|
| OLS4 | 278 | 233 | 9,983,559 |
| UMLS | 283 | 233 + 5 Biomappings | 10,051,100 |
| **Consolidated** | — | — | **9,981,261 unique** |

- All 278 shared files are byte-identical (md5 confirmed)
- UMLS dir = OLS4 + 5 Biomappings files
- 2,298 duplicates removed during consolidation

### 5.3 Currency — All Stale

| Ontology | Installed | Days Stale |
|----------|-----------|-----------|
| GO | 2024-08-09 | ~643 |
| HP | 2024-09-20 | ~611 |
| MONDO | 2024-09-03 | ~628 |
| DOID | 2024-08-07 | ~645 |
| UBERON | 2024-09-09 | ~622 |
| CL | 2024-10-03 | ~598 |
| ChEBI | 2024-09-01 | ~630 |
| EFO | 3.70.0 | ~20 minor versions behind |

> [!WARNING]
> All key ontologies are 588-643 days stale. Full refresh recommended before production use.

**Bug Fixed**: `SSSOMConsolidator.consolidate()` was missing `comment_prefix="#"` in `pl.read_csv()`, causing failures on all 278 SSSOM files with YAML metadata headers. Fixed in [PR #2](https://github.com/cytognosis/cytos/pull/2).

---

## 6. Knowledge Graph Sources

### Inventory: ~1.89M entities, ~95M edges, ~48 GB

| Source | Entities | Edges | Size | BioLink Native |
|--------|----------|-------|------|---------------|
| Open Targets 26.03 | 148,932 | 19.1M | Multi-GB | No (needs LinkMLizer) |
| Monarch KG | 1,379,605 | 15,356,321 | 7.0 GB | ✅ Yes |
| PrimeKG | 129,375 | 8,100,498 | 3.9 GB | No |
| PharmaProjects | 209,753 | 57,658 | 134.9 MB | No |
| StringDB v12.0 | 19,699 | 13,715,404 | 374.6 MB | No |
| STITCH v5.0 | — | 55.0M | 36.4 GB | No |

### Open Targets 26.03 — Schema Change Detected

> [!IMPORTANT]
> OT 26.03 renamed `molecule/` → `drug_molecule/` and `maximumClinicalTrialPhase` → `maximumClinicalStage`. The existing `OpenTargetsLinkMLizer` references the old names and needs updating.

---

## 7. Bioregistry

| Test | Input | Output | Status |
|------|-------|--------|--------|
| CURIE → URI | MONDO:0005090 | `http://purl.obolibrary.org/obo/MONDO_0005090` | ✅ |
| CURIE → URI | CHEBI:15422 | `http://purl.obolibrary.org/obo/CHEBI_15422` | ✅ |
| CURIE → URI | GO:0006915 | `http://purl.obolibrary.org/obo/GO_0006915` | ✅ |
| CURIE → URI | HP:0001250 | `http://purl.obolibrary.org/obo/HP_0001250` | ✅ |
| ID conversion | CHEBI → PubChem | Working | ✅ |
| ID conversion | UniProt → RefSeq | Working | ✅ |
| ID conversion | DrugBank → MeSH | Working | ✅ |
| Bulk performance | 100 IDs | 1.29s | ✅ |
| mygene | Gene lookup | Working | ✅ |
| mychem | Drug lookup | Working | ✅ |

---

## 8. GWAS Summary Statistics Pipeline

### Normalization (8/12 + 4 pending investigation)

| Trait | Variants | GW-Sig | Format | Parquet |
|-------|----------|--------|--------|---------|
| ADHD 2022 | 6,774,224 | 1,428 | classic | 171.4M |
| ASD 2019 | 9,112,386 | 93 | classic | 163.6M |
| BIP 2024 | 6,360,788 | 2,779 | classic | 341.8M |
| CDG 2025 | 2,846,564 | 605 | classic | 109.9M |
| PTSD 2024 | 11,713,632 | 0 | VCF | 237.2M |
| SCZ 2022 | 7,630,068 | 22,075 | classic | 379.7M |
| SUD CUD 2020 | 16,789,253 | 1 | classic | 358.2M |
| TS 2019 | 8,265,318 | 1 | classic | 164.6M |
| **TOTAL** | **69,492,233** | **26,982** | | **1,926M** |

### Multi-Trait Matrix
- **69.5M variant-trait rows** in long format (1.04 GB Parquet)
- **33.2M unique variants** across all traits
- **15.0M multi-trait variants** (45.3% shared between ≥2 traits)

---

## 9. Test Suites

### cytos (143 tests, 149.78s)
| Outcome | Count |
|---------|-------|
| Passed | 100 |
| Skipped | 33 |
| Failed | 6 (pre-existing: missing `rocrate`, `neo4j` modules) |
| Errors | 3 (pre-existing: Neo4j not installed) |

### cytoskeleton (869 tests, 46.60s)
| Outcome | Count |
|---------|-------|
| Passed | 869 |
| Skipped | 1 |

### cytoskills (141 tests, 724ms)
| Outcome | Count |
|---------|-------|
| Passed | 141 |

### cytoplex (292 tests)
| Outcome | Count |
|---------|-------|
| Passed | 292 |
| Skipped | 1 |

---

## 10. CLI Verification

| CLI | Command | Status |
|-----|---------|--------|
| cytos | `python -m cytos [compile\|schema\|ontology\|sources\|ingest\|funding\|scholarly]` | ✅ |
| cytoskeleton | `cytoskeleton [env\|deps\|lock\|pr]` | ✅ |
| cytoskills | `node packages/cli/dist/cyto-skills.js` (30+ commands) | ✅ |
| cytoplex | `plex-*` (8 commands) | ✅ |
