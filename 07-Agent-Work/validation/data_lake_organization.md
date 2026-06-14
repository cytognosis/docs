# Data Lake Organization Proposal

> **Current total**: ~1.5TB across `/home/mohammadi/datasets/`

## Proposed Structure

```
/home/mohammadi/datasets/
├── 01-ontologies/                    # OWL/OBO ontology files (69GB)
│   ├── biomedical/                   # HP, MONDO, DOID, GO, CL, UBERON, etc.
│   ├── clinical/                     # ICD, SNOMED, LOINC (from ontologies/clinical/)
│   ├── environmental/                # ECTO, FOODON, HHEAR, NMDCO
│   ├── experimental/                 # OBI, BAO, ICO, EFO (from ontologies/experiments/)
│   ├── neuro/                        # NIFSTD, BIDS terms (from ontologies/neuro/)
│   └── singlecell/                   # CL, HANCESTRO, UniProt XML (from ontologies/singlecell/)
│
├── 02-vocabularies/                  # UMLS + SNOMED + structured vocabs (136GB)
│   ├── UMLS/                         # from latest/UMLS/
│   ├── SnomedCT/                     # from latest/SnomedCT/
│   ├── biothings_schemas/            # from latest/biothings_schemas/
│   └── schemas/                      # from latest/schemas/
│
├── 03-knowledge-graphs/              # External KGs (393GB)
│   ├── monarch/                      # 114GB, DuckDB + neo4j dump
│   ├── pheknowlator/                 # 156GB, RDF/OWL + processed edges
│   ├── primekg/                      # 3.9GB, CSV
│   ├── planet/                       # 25GB, pickle + TSV triples
│   ├── open-targets/                 # 23GB, Parquet
│   ├── petagraph/                    # 24GB
│   ├── pkg2.0/                       # 51GB, TSV (from KGs/PMK/)
│   ├── ckg/                          # TBD (GitHub clone)
│   ├── openalex/                     # from KGs/openalex/
│   └── neuro-kg/                     # from KGs/NeuroKG/
│
├── 04-identifiers/                   # Cross-reference databases (171GB)
│   ├── ensembl/                      # from latest/Ensembl/
│   ├── unichem/                      # from identifiers/databases/UniChem/
│   ├── ols4-sssom/                   # from latest/ols4/sssom/
│   ├── umls-sssom/                   # from latest/mappings/
│   ├── curated/                      # from identifiers/curated/
│   └── databases/                    # from identifiers/databases/ (minus UniChem)
│
├── 05-annotations/                   # Annotations + topic areas (14GB)
│   ├── topic-areas/                  # from FAIR/organizational/topic_areas/
│   │   ├── aio/                      # AI Ontology (for ML model annotation)
│   │   ├── cso/                      # Computer Science Ontology (paper topics)
│   │   ├── roadmap/                  # Research topic roadmap
│   │   └── ncit/                     # NCI Thesaurus (already via UMLS)
│   ├── cellxgene/                    # from latest/cellxgene/
│   ├── hra/                          # from latest/HRA/
│   └── nbb/                         # from latest/NBB/
│
├── 06-genotype/                      # Genomic data (103GB)
│   ├── personal/                     # WGS/WES data (temporary, do not track)
│   └── reference/                    # Reference panels, annotations
│
├── 07-single-cell/                   # scRNA-seq datasets (separate)
│
├── 08-neuroimaging/                  # BIDS/NWB datasets (319GB)
│   └── (from neuro/)
│
├── 09-literature/                    # Papers, BibTeX (5MB+)
│   └── (from papers/)
│
├── 10-embeddings/                    # Pre-computed embeddings (34GB)
│
├── 11-benchmarks/                    # Benchmark datasets (23GB)
│
├── 12-network/                       # Network data (200GB)
│
└── 13-cell-lines/                    # Cell line data (2.8GB)
```

## Migration Map

| Current Path | Proposed Path | Size |
|-------------|---------------|------|
| `ontologies/` | `01-ontologies/` | 69GB |
| `latest/UMLS/` | `02-vocabularies/UMLS/` | ~80GB |
| `latest/SnomedCT/` | `02-vocabularies/SnomedCT/` | ~50GB |
| `KGs/monarchinitiative/` | `03-knowledge-graphs/monarch/` | 114GB |
| `KGs/pheknowlator/` | `03-knowledge-graphs/pheknowlator/` | 156GB |
| `KGs/PrimeKG/` | `03-knowledge-graphs/primekg/` | 3.9GB |
| `KGs/PlaNet/` | `03-knowledge-graphs/planet/` | 25GB |
| `KGs/open_targets/` | `03-knowledge-graphs/open-targets/` | 23GB |
| `KGs/PMK/` | `03-knowledge-graphs/pkg2.0/` | 51GB |
| `identifiers/` | `04-identifiers/` | 171GB |
| `FAIR/` + `latest/cellxgene` | `05-annotations/` | 14GB |
| `genotype/` | `06-genotype/` | 103GB |
| `neuro/` | `08-neuroimaging/` | 319GB |
| `embeddings/` | `10-embeddings/` | 34GB |
| `benchmark/` | `11-benchmarks/` | 23GB |

## DVC Tracking Strategy

### Tracked by DVC (large, versioned)
- `03-knowledge-graphs/*/` — KG downloads and builds
- `04-identifiers/*/` — identifier mapping databases
- `01-ontologies/*/` — ontology files

### NOT tracked by DVC
- `06-genotype/personal/` — ephemeral test data
- `08-neuroimaging/` — too large, tracked separately
- `12-network/` — too large, tracked separately

### DVC Remote
Configure a GCS remote for `dvc push/pull`:
```bash
dvc remote add gcs gs://cytognosis-data-lake/
dvc remote modify gcs projectname cytognosis-infrastructure
```

## Phased Migration

> [!IMPORTANT]
> Migration should use `mv` (rename) not `cp` to preserve disk space.
> Create symlinks at old paths for backward compatibility.

### Phase 1: Create structure + symlinks (immediate)
```bash
mkdir -p /home/mohammadi/datasets/{01-ontologies,02-vocabularies,03-knowledge-graphs,...}
# Rename directories
mv KGs/monarchinitiative 03-knowledge-graphs/monarch
ln -s ../03-knowledge-graphs/monarch KGs/monarchinitiative
```

### Phase 2: Update all code references (after migration)
- `cytos/params.yaml` — update all source paths
- `cytos/dvc.yaml` — update pipeline source paths
- `cytos/src/cytos/pipelines/` — update hardcoded paths

### Phase 3: DVC tracking (after references updated)
```bash
cd /home/mohammadi/datasets
dvc init
dvc add 01-ontologies/ 03-knowledge-graphs/ 04-identifiers/
```
