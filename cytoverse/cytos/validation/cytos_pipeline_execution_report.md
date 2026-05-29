# Cytos Data Pipeline Execution Report

> **Date**: 2026-05-12  
> **Status**: Phases A, B, C (partial) complete. D, H, J code-ready.

---

## Pipeline Execution Results

### Phase B: Schema.org / Bioschemas / BioLink ✅

| Output | File | Rows |
|--------|------|------|
| BioLink Class Hierarchy | `normalized/biolink/4.x/BiolinkClassHierarchy.parquet` | 332 |
| Cytos-BioLink Alignment | `normalized/biolink/4.x/CytosBiolinkAlignment.parquet` | **28/28 aligned** |
| Schema.org Types | `schemas/schema_org_types.yaml` | 15 types |
| Bioschemas Profiles | `schemas/bioschemas_profiles.yaml` | 4 profiles |

**Runtime**: 0.4 seconds

### Phase C: Ontology Ingestion ✅ (13 of 27 ontologies)

| Ontology | Terms | Active | Target Class | Validation Enum |
|----------|-------|--------|--------------|-----------------|
| CL (Cell Ontology) | 19,150 | 18,862 | CellType | ✅ |
| UBERON | 27,295 | 25,905 | AnatomicalEntity | ✅ |
| MONDO | 58,940 | 54,305 | Disease | ✅ |
| HPO | 19,944 | 19,389 | Phenotype | - |
| DOID | 14,638 | 12,127 | Disease | - |
| HANCESTRO | 1,310 | 1,264 | Ancestry | ✅ |
| PATO | 8,625 | 7,643 | PhenotypicQuality | ✅ |
| HsapDv | 260 | 239 | DevelopmentStage | ✅ |
| MmusDv | 178 | 134 | DevelopmentStage | ✅ |
| MAXO | 7,120 | 7,045 | TreatmentAction | - |
| EDAM | 3,524 | 2,404 | DataFormat | - |
| SWO | 1,971 | 1,294 | Software | - |
| GENO | 589 | 541 | GenomicEntity | - |
| **Total** | **163,544** | **151,152** | | |

**Runtime**: 33.7 seconds

> [!NOTE]
> Remaining ontologies (ChEBI 775MB, EFO 332MB, NCBITaxon 1.9GB, clinical OWL vocabs) require longer processing and will run in batch mode.

---

## Code Inventory

### Linkmlize Transforms (16 modules, ~3,500 lines)

| Module | Lines | Purpose |
|--------|-------|---------|
| `base.py` | 143 | Abstract base class with Parquet/YAML writers |
| `biolink.py` | 197 | BioLink Model alignment validation |
| `biothings.py` | 83 | BioThings DDE schema conversion |
| `cellxgene.py` | 149 | CELLxGENE AnnData normalization |
| `ga4gh.py` | 184 | GA4GH VRS/Phenopackets conversion |
| `kg_align.py` | 400+ | PrimeKG, Monarch, PubMedKG, Petagraph alignment |
| `nwb.py` | 183 | NWB/HDMF schema conversion |
| `ontology.py` | 255 | Bulk ontology ingestion (27 catalogs) |
| `openalex.py` | 156 | OpenAlex publication normalization |
| `opentargets.py` | 148 | Open Targets platform ingestion |
| `schema_org.py` | 225 | Schema.org/Bioschemas JSON-LD conversion |
| `sosa.py` | 130 | W3C SOSA/SSN sensor ontology conversion |
| `umls.py` | 504 | UMLS/SNOMED clinical terminology (absorbs neuro-pheno) |

### Parsers (8 modules, ~1,250 lines)

| Parser | Lines | Formats |
|--------|-------|---------|
| `rrf.py` | 207 | UMLS RRF (pipe-delimited) |
| `owl.py` | 126 | OWL/OBO via pronto |
| `rdf.py` | 220 | RDF/Turtle/JSON-LD via rdflib |
| `jsonschema.py` | 169 | JSON Schema (VRS, Phenopackets) |
| `hdmf.py` | 226 | HDMF Schema Language YAML |
| `parquet.py` | 143 | Parquet via DuckDB/Polars |
| `bibtex.py` | 137 | BibTeX bibliography files |

### API Verification Clients (4 modules, ~670 lines)

| Client | Lines | Methods |
|--------|-------|---------|
| `ols4/client.py` | 167 | `get_term`, `search`, `verify_term` |
| `opentargets/client.py` | 186 | `get_target`, `get_disease`, `get_drug`, `verify_target` |
| `umls/client.py` | 169 | `get_concept`, `get_atoms`, `get_relations`, `verify_concept` |
| `monarch/client.py` | 148 | `get_entity`, `get_associations`, `verify_entity` |

### Infrastructure

| File | Lines | Purpose |
|------|-------|---------|
| `configs/prefixes/prefix_map.yaml` | 116 | 60+ CURIE prefix mappings |
| `data/provenance/registry.yaml` | 316 | 20 dataset provenance records |
| `schemas/core.yaml` | 199 | DatasetManifest, VerificationStatusEnum |
| `src/cytos/ingest/run.py` | 312 | Master CLI runner |

---

## Dependency Changes

### `pyproject.toml`
- Added core runtime deps: `pyyaml`, `polars`, `duckdb`, `pyarrow`, `rdflib`, `httpx`, `loguru`, `pronto`
- Fixed UV-incompatible optional extras (emptied groups with unresolvable packages)

### `cytoskeleton/configs/components/python/data/io.yaml`
- Added `httpx>=0.27` for API verification clients

---

## Next Steps (Priority Order)

1. **Phase C remainder**: Run ChEBI, EFO, NCBITaxon (selective), and clinical OWL ontologies
2. **Phase D execution**: Run `UMLSLinkMLizer` against UMLS Parquet data
3. **Phase H**: Run `OpenTargetsLinkMLizer` against 47GB Parquet corpus
4. **Phase J**: Run PrimeKG alignment (3.9GB CSV)
5. **Phase K**: Write integration tests using API clients
6. **Phase I**: BioCypher adapter for Neo4j ingestion
