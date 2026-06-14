# External Tool Evaluation & Bioentity Landscape

> Created: 2026-05-12 08:12 UTC | Step 1 of BioAtlas Plan

## 1. Repos Cloned

| Repo | Path | Purpose |
|------|------|---------|
| laminlabs/bionty | `third_party/bionty` | Ontology + bioentity tables |
| biothings/biothings_client.py | `third_party/client.py` | REST API client (gene/variant/chem/disease/taxon) |
| biothings/biothings_schema.py | `third_party/schema.py` | JSON Schema validation |
| biothings/mygene.info | `third_party/mygene.info` | Gene annotation API source |
| chanzuckerberg/single-cell-curation | `third_party/chanzuckerberg_single-cell-curation` | CXG schema validation |
| biopragmatics/bioregistry | `third_party/biopragmatics_bioregistry` | Prefix registry (2,713 prefixes) |

## 2. Entity Type Classification

> [!IMPORTANT]
> Two fundamentally different kinds of biological entities:
> - **Semantic entities** = ontology terms (cell types, diseases, tissues). Already in our KG.
> - **Biomolecular entities** = individual genes, proteins, variants, chemicals. NOT in our KG as first-class instances (only as ontology classes).

### What's Already in Our KG (Semantic Entities)

| Entity Type | In KG? | Sources | Prefix(es) | Count |
|------------|--------|---------|-----------|-------|
| Cell Type | ✅ | CL, HRA ASCT+B | CL: | ~2,600 |
| Anatomical Structure | ✅ | UBERON, FMA, HRA | UBERON:, FMA: | ~15,000 |
| Disease | ✅ | MONDO, DOID, SNOMED | MONDO:, DOID:, SCTID: | ~30,000+ |
| Phenotype | ✅ | HP, PATO | HP:, PATO: | ~20,000+ |
| Chemical (class-level) | ✅ | ChEBI | CHEBI: | ~100,000 |
| Drug (class-level) | ✅ | RxNorm | RXNORM: | ontology terms |
| Experimental Factor | ✅ | EFO | EFO: | ~25,000 |
| Developmental Stage | ❌ | HsapDv, MmusDv | — | need to add |
| Pathway | ❌ | GO, PW | — | need to add |
| Gene (ontology class) | ✅ partial | HGNC (via HRA BM) | HGNC: | ~1,900 (only biomarkers) |

### What's NOT in Our KG (Biomolecular Entities)

| Entity Type | Primary DB | Identifiers | Bionty? | BioThings? | Record Count |
|------------|-----------|-------------|---------|-----------|-------------|
| **Gene** | Ensembl | ensembl_gene_id, symbol, ncbi_gene_id, HGNC | ✅ | ✅ (mygene.info) | ~60K (human) |
| **Protein** | UniProt | uniprot_id, gene_name | ✅ | ❌ (via mychem) | ~20K (human reviewed) |
| **Variant** | dbSNP/ClinVar | HGVS, rs_id, chrom:pos | ❌ | ✅ (myvariant.info) | millions |
| **Chemical/Drug** (instance) | DrugBank/ChEBI | drugbank_id, chebi_id, inchikey | ❌ | ✅ (mychem.info) | ~14K (DrugBank) |
| **Gene Set** | MSigDB/GO | geneset_id | ❌ | ✅ (mygeneset.info) | ~30K |
| **Cell Line** | Cellosaurus/DepMap | cellosaurus_id, depmap_id | ✅ | ❌ | ~130K |
| **Cell Marker** | CellMarker 2.0 | marker_id | ✅ | ❌ | ~10K |
| **Taxon** | NCBI Taxonomy | ncbi_taxon_id | ✅ | ✅ (mytaxon.info) | ~2.5M |

## 3. Bionty Evaluation

### Entity Model
Bionty has **two distinct entity backends**:

1. **Ontology-backed** (semantic): CellType (CL), Tissue (UBERON), Disease (MONDO/DOID), Phenotype (HP/PATO), ExperimentalFactor (EFO), Ethnicity (HANCESTRO), DevelopmentalStage (HsapDv), Drug (DRON/ChEBI), Pathway (GO/PW)
   - These download OWL files and parse them
   - We already have ALL of these in our KG via the 21 ontologies

2. **Table-backed** (biomolecular): Gene (Ensembl), Protein (UniProt), CellLine (Cellosaurus/DepMap), CellMarker, BFXPipeline, BioSample
   - These download pre-built Parquet tables from `s3://bionty-assets/`
   - Each table has columns: `[primary_id, symbol, name, synonyms, ...]`
   - **These are what we need to catalog/map, NOT ingest wholesale**

### Key Patterns to Adopt
- `validate(values, field)` — check if values are valid for an entity type
- `map_legacy_ids()` — convert old Ensembl IDs to current
- `lookup()` — fuzzy search + synonym matching
- `inspect(values)` → categorize as mapped/unmapped
- Per-organism versioning of tables (human, mouse, etc.)

### Gene Table Schema (Ensembl via bionty)

| Column | Description | Example |
|--------|-------------|---------|
| `ensembl_gene_id` | Primary identifier | ENSG00000141510 |
| `symbol` | Gene symbol (HGNC) | TP53 |
| `ncbi_gene_id` | Entrez Gene ID | 7157 |
| `biotype` | Gene biotype | protein_coding |
| `description` | Gene description | tumor protein p53 |
| `synonyms` | Pipe-delimited synonyms | p53\|LFS1 |

### Protein Table Schema (UniProt via bionty)

| Column | Description | Example |
|--------|-------------|---------|
| `uniprotkb_id` | UniProt accession | P04637 |
| `protein_name` | Protein name | Cellular tumor antigen p53 |
| `gene_symbol` | Corresponding gene | TP53 |
| `length` | Amino acid length | 393 |
| `organism_name` | Species | Homo sapiens |

## 4. BioThings Evaluation

### API Endpoints

| API | URL | Entity | Primary ID | Key Fields |
|-----|-----|--------|-----------|------------|
| MyGene.info | mygene.info/v3 | Gene | Entrez, Ensembl | symbol, name, taxid, entrezgene, ensembl.gene |
| MyVariant.info | myvariant.info/v1 | Variant | HGVS | chrom, pos, ref, alt, clinvar, dbsnp, cadd |
| MyChem.info | mychem.info/v1 | Chemical/Drug | InChIKey, DrugBank | drugbank, chebi, pharmgkb, aeolus |
| MyDisease.info | mydisease.info/v1 | Disease | MONDO, DOID | mondo, disgenet, ctd |
| MyTaxon.info | mytaxon.info/v1 | Taxon | NCBI Taxon | scientific_name, lineage |
| MyGeneset.info | mygeneset.info/v1 | Gene Set | various | genes, description |

### What BioThings Provides That We Don't
- **Variant annotations**: ClinVar significance, CADD scores, allele frequencies
- **Drug-target interactions**: DrugBank bindings, PharmGKB annotations
- **Disease-gene associations**: DisGeNET, CTD
- **Gene functional annotations**: GO terms, pathways, protein domains

### REST API Pattern
```python
# biothings_client usage
import biothings_client
mg = biothings_client.get_client("gene")
mg.getgene("1017")  # by Entrez
mg.query("symbol:CDK2")  # by query
mg.getgenes(["1017", "1018"])  # batch
```

## 5. Bioregistry (biopragmatics) Evaluation

### What It Provides
- **2,713 prefix registrations** with metadata (name, pattern, URI format, example, homepage)
- CURIE ↔ URI resolution
- Prefix normalization (e.g., "gene ontology" → "go", "GO")
- Alignment with Identifiers.org, OBO, OLS, N2T, etc.
- Domain classification (chemical, gene, tissue, etc.)

### What We Should Adopt
- Prefix metadata for CURIE expansion/validation
- URI format templates for link generation
- The `Domain` controlled vocabulary: chemical, tissue, reaction, gene, cell and cell line, lipid, morphology, disease, phenotype, anatomy, protein, organism, pathway, variant, etc.

## 6. Single-Cell-Curation Evaluation

### Validator Flow
```
AnnData → cellxgene_schema.validate() → {is_valid, errors, warnings}
```
- Checks obs column presence and ontology term validity
- Validates against CXG schema version (7.x)
- Checks CURIE prefixes match expected ontologies per column
- Validates var (gene) identifiers against Ensembl

## 7. Entity/Identifier Matrix (Decision Table)

> [!IMPORTANT]
> This matrix determines what we need before any biomolecular ingestion.

| Entity | In Semantic KG | Need Instance Table | Primary IDs | Cross-ref IDs | Source for Table |
|--------|:-:|:-:|---|---|---|
| Gene | ❌ (only ~1.9K biomarkers) | ✅ | Ensembl, HGNC | NCBI, UniProt, symbol | Ensembl (bionty) / mygene.info (REST) |
| Protein | ❌ (only ~200 biomarkers) | ✅ | UniProt | PDB, Gene, InterPro | UniProt (bionty) |
| Variant | ❌ | ✅ later | HGVS, rsID | ClinVar, gnomAD | myvariant.info (REST) |
| Chemical | ✅ (ChEBI classes) | ✅ later | InChIKey, ChEBI | DrugBank, PubChem | mychem.info (REST) |
| Cell Line | ❌ | ✅ later | Cellosaurus | DepMap, CLO | bionty |
| Cell Marker | ❌ | ✅ | CellMarker ID | Gene symbol | bionty |
| Pathway | ❌ | ✅ | GO, KEGG, Reactome | PW | GO OWL + Reactome |
| Developmental Stage | ❌ | ✅ | HsapDv, MmusDv | — | OWL (bionty source) |

### Priority for Bioentity Table Ingestion

1. **Gene** (P1) — needed for CXG var validation, ASCT+B biomarker enrichment
2. **Protein** (P1) — cross-ref from Gene, needed for drug target analysis
3. **Cell Marker** (P2) — links genes to cell types
4. **Pathway** (P2) — GO, Reactome for functional enrichment
5. **Developmental Stage** (P2) — needed for CXG schema compliance
6. **Variant** (P3) — future genomics integration
7. **Chemical/Drug instances** (P3) — future drug discovery
8. **Cell Line** (P3) — future experimental metadata

## 8. Architecture Decision

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Ontology-backed entities | Use our KG directly | We already have all 21 ontologies; bionty would be redundant |
| Gene/Protein tables | Build own from Ensembl/UniProt downloads | Bionty's tables are good reference but tightly coupled to lamindb |
| Variant/Chem queries | Wrap biothings_client REST API | Too large for local storage; query on demand |
| Prefix resolution | Adopt bioregistry data + our own expansion | 2,713 prefixes provides comprehensive CURIE support |
| CXG validation | Wrap single-cell-curation + our LinkML | Need both for cross-validation |
| Entity resolution | KG first, then REST fallback | KG has semantic context; REST fills gaps |
