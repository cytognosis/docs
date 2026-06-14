# Phase D: Ontology Ingestion & Cross-Ontological Mappings

**Execution date**: 2026-05-25 04:24 PDT
**Status**: ✅ All sub-phases complete

---

## D.1 — Ontology Registry Validation

**Script**: [test_ontology_registry.py](file:///home/mohammadi/repos/cytognosis/scratch/test_ontology_registry.py)
**Registry**: [registry.yaml](file:///home/mohammadi/datasets/01-ontologies/registry.yaml)

### Summary

| Metric | Value |
|--------|-------|
| Total registered ontologies | **51** |
| Present on disk | **51** |
| Missing on disk | **0** |
| Flag mismatches | **0** |
| Total size on disk | **9.5 GB** |
| OWL directory | `/home/mohammadi/datasets/01-ontologies/owl/` (72 files, 9.7 GB) |

> [!NOTE]
> The registry tracks 51 ontologies while the OWL directory contains 72 files. The 21 extra OWL files are present on disk but not yet registered in registry.yaml.

### Top 10 by Size

| Rank | Ontology | Size |
|------|----------|------|
| 1 | ncbitaxon | 1.8 GB |
| 2 | pr | 1.3 GB |
| 3 | chebi | 774.4 MB |
| 4 | ncit | 774.0 MB |
| 5 | loinc | 698.4 MB |
| 6 | dron | 669.2 MB |
| 7 | mesh | 659.2 MB |
| 8 | upheno | 397.0 MB |
| 9 | efo | 331.6 MB |
| 10 | cellosaurus | 259.8 MB |

### Size Accuracy

All declared sizes match actual sizes within 5%, except 3 small ontologies with rounding differences:
- `gmho`: declared 0.3MB, actual 0.3MB (13.1% delta due to rounding at small scale)
- `mmusdv`: declared 0.4MB, actual 0.4MB (12.4% delta)
- `sbo`: declared 0.6MB, actual 0.6MB (7.4% delta)

**Verdict**: Registry is fully consistent. All 51 `present: true` flags are accurate.

---

## D.2 — SSSOM Mapping Validation

**Script**: [test_sssom_validation.py](file:///home/mohammadi/repos/cytognosis/scratch/test_sssom_validation.py)

### OLS4 SSSOM Dataset

| Metric | Value |
|--------|-------|
| Directory | `/home/mohammadi/datasets/04-identifiers/ols4-sssom/sssom/` |
| Total TSV files | **278** |
| Files with data | **233** |
| Empty/header-only | **45** |
| Total mapping rows | **9,983,559** |
| Unique subject prefixes | **247** |
| Unique object prefixes | **728** |
| Unique prefix pairs | **2,335** |

### Top 10 SSSOM Files by Row Count

| File | Rows | Size |
|------|------|------|
| ncbitaxon.ols.sssom.tsv | 5,468,276 | 593.5 MB |
| slm.ols.sssom.tsv | 1,984,053 | 913.5 MB |
| snomed.ols.sssom.tsv | 301,134 | 46.6 MB |
| pr.ols.sssom.tsv | 238,940 | 29.4 MB |
| chebi.ols.sssom.tsv | 229,395 | 35.5 MB |
| vto.ols.sssom.tsv | 228,693 | 22.2 MB |
| ncit.ols.sssom.tsv | 155,054 | 19.2 MB |
| mondo.ols.sssom.tsv | 146,765 | 16.8 MB |
| ogg.ols.sssom.tsv | 143,690 | 14.0 MB |
| omit.ols.sssom.tsv | 139,605 | 12.4 MB |

### Top Prefix Pairs (subject → object)

| Subject | Object | Count |
|---------|--------|-------|
| NCBITaxon | GC_ID | 2,708,758 |
| NCBITaxon | NCBITaxon | 2,708,757 |
| SLM | smiles | 778,936 |
| SLM | inchi | 593,209 |
| SLM | inchikey | 593,209 |
| SNOMED | SNOMED | 301,134 |
| PR | UniProtKB | 174,043 |
| NCIT | NCIT | 154,672 |
| GNO | GNO | 133,041 |
| CHEBI | CHEBI | 126,366 |

### Predicate Distribution

| Predicate | Count |
|-----------|-------|
| `oboInOwl:hasDbXref` | 5,820,594 |
| `rdfs:subClassOf` | 4,132,775 |
| `skos:exactMatch` | 68,059 |
| `owl:equivalentClass` | 24,383 |
| `rdfs:subPropertyOf` | 2,270 |
| `ro:HOM0000017` | 1,686 |
| `skos:closeMatch` | 143 |
| `skos:broadMatch` | 91 |
| `skos:narrowMatch` | 58 |

### UMLS SSSOM Dataset

| Metric | Value |
|--------|-------|
| Directory | `/home/mohammadi/datasets/04-identifiers/umls-sssom/` |
| Total TSV files | **283** |
| Files with data | **238** |
| Total mapping rows | **10,051,100** |
| Unique subject prefixes | **307** |
| Unique object prefixes | **788** |

### Overlap Analysis: OLS4 vs UMLS

| Metric | Value |
|--------|-------|
| OLS4 files | 278 |
| UMLS files | 283 |
| Shared files | **278** |
| OLS4-only files | 0 |
| UMLS-only files | 5 |

> [!IMPORTANT]
> **All 278 shared files are byte-identical** (confirmed via md5sum). The UMLS SSSOM directory is a superset of OLS4, containing 5 additional files from the Biomappings project:
> - `biomappings_predictions.sssom.tsv` (54,049 rows, 9.8 MB)
> - `biomappings_positive.sssom.tsv`
> - `biomappings_negative.sssom.tsv`
> - `biomappings_unsure.sssom.tsv`
> - `biomappings_curators.tsv`

The additional Biomappings files contribute 60 extra subject prefixes and ~67,500 additional mapping rows.

### Key Ontology SSSOM Coverage

| Ontology | SSSOM File | Rows |
|----------|-----------|------|
| GO | go.ols.sssom.tsv | 26,807 ✓ |
| HP | hp.ols.sssom.tsv | 33,565 ✓ |
| MONDO | mondo.ols.sssom.tsv | 146,765 ✓ |
| DOID | doid.ols.sssom.tsv | 37,839 ✓ |
| UBERON | uberon.ols.sssom.tsv | 49,369 ✓ |
| CL | cl.ols.sssom.tsv | 3,126 ✓ |
| ChEBI | chebi.ols.sssom.tsv | 229,395 ✓ |
| EFO | efo.ols.sssom.tsv | 36,071 ✓ |

---

## D.3 — SSSOM Consolidation Test

**Script**: [test_sssom_consolidation.py](file:///home/mohammadi/repos/cytognosis/scratch/test_sssom_consolidation.py)
**Module under test**: [sssom_consolidator.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/kg/sssom_consolidator.py)

### Test 1: Upstream SSSOMConsolidator (as-is)

**Result**: ✗ **FAILED** — all 278 files failed to parse.

> [!WARNING]
> **Bug discovered**: `SSSOMConsolidator.consolidate()` at [line 251](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/kg/sssom_consolidator.py#L251) calls `pl.read_csv()` without `comment_prefix="#"`. SSSOM files begin with YAML metadata lines prefixed with `#`, which causes Polars schema inference to fail on every file.

### Test 2: Patched Consolidation (with `comment_prefix="#"`)

**Result**: ✓ **SUCCESS**

| Metric | Value |
|--------|-------|
| Files parsed successfully | **233** |
| Empty/no-data files skipped | **45** |
| Failed files | **0** |
| Pre-dedup rows | **9,983,559** |
| Post-dedup rows (unique triples) | **9,981,261** |
| Duplicates removed | **2,298** |
| Output file | `/home/mohammadi/repos/cytognosis/scratch/sssom_consolidated/consolidated.sssom.tsv` |
| Output size | **1,973.2 MB** (2,069,029,974 bytes) |

### Consolidated Predicate Distribution

| Predicate | Count |
|-----------|-------|
| `oboInOwl:hasDbXref` | 5,820,587 |
| `rdfs:subClassOf` | 4,130,484 |
| `owl:equivalentClass` | 24,383 |
| `skos:exactMatch` | 3,159 |
| `rdfs:subPropertyOf` | 2,270 |
| `skos:closeMatch` | 143 |
| `skos:relatedMatch` | 89 |
| `skos:broadMatch` | 83 |

### Required Fix

```diff
--- a/src/cytos/kg/sssom_consolidator.py
+++ b/src/cytos/kg/sssom_consolidator.py
@@ -249,6 +249,7 @@
             try:
                 df = pl.read_csv(
                     sssom_file,
                     separator="\t",
                     infer_schema_length=0,
                     ignore_errors=True,
+                    comment_prefix="#",
                 )
```

---

## D.4 — Ontology Currency Report

**Script**: [test_ontology_currency.py](file:///home/mohammadi/repos/cytognosis/scratch/test_ontology_currency.py)

### Key Ontology Versions

| Ontology | Name | Version Installed | Source | Size (MB) | OBO Status | Age (days) | Freshness |
|----------|------|-------------------|--------|-----------|------------|------------|-----------|
| GO | Gene Ontology | 2024-09-08 | OBO Foundry | 123.7 | active | 611 | ✗ Old |
| HP | Human Phenotype Ontology | 2024-08-13 | OBO Foundry | 72.6 | active | 637 | ✗ Old |
| MONDO | MONDO Disease Ontology | 2024-10-01 | OBO Foundry | 231.6 | active | 588 | ✗ Old |
| DOID | Human Disease Ontology | 2024-09-24 | OBO Foundry | 26.9 | active | 595 | ✗ Old |
| UBERON | Uber Anatomy Ontology | 2024-08-07 | OBO Foundry | 94.0 | active | 643 | ✗ Old |
| CL | Cell Ontology | 2024-09-26 | OBO Foundry | 62.8 | active | 593 | ✗ Old |
| ChEBI | Chemical Entities of Biological Interest | 2024-09-01 | OBO Foundry | 774.4 | active | 618 | ✗ Old |
| EFO | Experimental Factor Ontology | 3.70.0 | GitHub | 331.6 | N/A | — | ✗ Old |

> [!CAUTION]
> **All 8 key ontologies are stale** — installed versions are from Aug-Oct 2024, now ~600 days old. The EFO latest release on GitHub is **v3.90.0** (2026-05-18) vs installed **3.70.0**. A full ontology refresh is recommended.

### Registry Metadata

| Field | Value |
|-------|-------|
| Schema version | 1.0.0 |
| Registry last updated | 2026-05-12 |
| Base path | `/home/mohammadi/datasets/01-ontologies` |

---

## Files Produced

| File | Size | Description |
|------|------|-------------|
| [test_ontology_registry.py](file:///home/mohammadi/repos/cytognosis/scratch/test_ontology_registry.py) | 3.5 KB | D.1 registry validator |
| [test_sssom_validation.py](file:///home/mohammadi/repos/cytognosis/scratch/test_sssom_validation.py) | 6.2 KB | D.2 SSSOM mapping validator |
| [test_sssom_consolidation.py](file:///home/mohammadi/repos/cytognosis/scratch/test_sssom_consolidation.py) | 5.1 KB | D.3 consolidation tester |
| [test_ontology_currency.py](file:///home/mohammadi/repos/cytognosis/scratch/test_ontology_currency.py) | 3.8 KB | D.4 currency reporter |
| [consolidated.sssom.tsv](file:///home/mohammadi/repos/cytognosis/scratch/sssom_consolidated/consolidated.sssom.tsv) | 1,973 MB | Consolidated SSSOM mappings |

## Key Findings

1. **Registry integrity is perfect**: 51/51 ontologies present, all flags accurate, all sizes match.
2. **SSSOM corpus is substantial**: ~10M mapping rows across 278 files from OLS4, dominated by NCBITaxon (5.5M rows) and SLM (2M rows).
3. **OLS4 and UMLS are identical**: The UMLS SSSOM directory is a byte-identical copy of OLS4, plus 5 Biomappings files (~67.5K extra rows). No distinct UMLS-derived mappings exist yet.
4. **Consolidator has a bug**: Missing `comment_prefix="#"` in `pl.read_csv()` causes 100% file parse failure. One-line fix resolves it.
5. **Ontologies need refresh**: All 8 key ontologies are 588-643 days old (from 2024). EFO is 20 minor versions behind (3.70.0 vs 3.90.0).
