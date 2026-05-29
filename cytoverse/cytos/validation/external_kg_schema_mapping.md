# External KG Schema Mapping

> Generated: 2026-05-12 | Status: Mapped, NOT imported

Each KG is mapped to our Cytos BioLink schema. They remain independent artifacts
until we finalize schema compatibility and decide which to import.

---

## 1. PrimeKG (Harvard/Zitnik Lab)

**Size**: 8.1M edges | **Format**: CSV (kg.csv)

### Entity Types → Cytos Mapping

| PrimeKG Type | Cytos BioLink | ID System |
|-------------|---------------|-----------|
| gene/protein | biolink:Gene + biolink:Protein | NCBI Gene |
| disease | biolink:Disease | MONDO |
| drug | biolink:Drug | DrugBank |
| anatomy | biolink:AnatomicalEntity | UBERON |
| biological_process | biolink:BiologicalProcess | GO |
| cellular_component | biolink:CellularComponent | GO |
| molecular_function | biolink:MolecularActivity | GO |
| pathway | biolink:Pathway | Reactome |
| effect/phenotype | biolink:PhenotypicFeature | HPO |
| exposure | biolink:EnvironmentalExposure | CTD |

### Relationship Types (30)

| PrimeKG Relation | Cytos Predicate |
|-----------------|-----------------|
| protein_protein | biolink:interacts_with |
| drug_protein | biolink:interacts_with |
| disease_protein | biolink:gene_associated_with_condition |
| disease_phenotype_positive | biolink:has_phenotype |
| disease_phenotype_negative | biolink:has_phenotype (negated) |
| indication | biolink:treats |
| contraindication | biolink:contraindicated_for |
| off-label use | biolink:treats (off_label qualifier) |
| drug_effect | biolink:has_adverse_event |
| drug_drug | biolink:interacts_with |
| exposure_disease | biolink:contributes_to |
| exposure_protein | biolink:affects |
| bioprocess_protein | biolink:has_participant |
| molfunc_protein | biolink:enables |
| cellcomp_protein | biolink:located_in |
| pathway_protein | biolink:participates_in |
| *_* (same type) | biolink:related_to |

**Compatibility: HIGH** — all types map cleanly to BioLink.

---

## 2. Monarch Initiative KG

**Size**: 1.38M nodes, 15.36M edges | **Format**: DuckDB (KGX-native)

### Schema
Already in KGX/BioLink format. Direct import possible.

**Key columns**: id, category, name, description, full_name, in_taxon, symbol

### Cross-ontology Mappings
1.26M SSSOM mappings included in the DuckDB.

**Compatibility: PERFECT** — native BioLink/KGX format.

---

## 3. PheKnowLator (Callahan Lab)

**Size**: ~156GB (includes OWL, build data) | **Format**: RDF/OWL + processed edge lists

### Processed Data Files
- `CLINVAR_VARIANT_GENE_DISEASE_PHENOTYPE_EDGES.txt`
- `HPA_GTEX_RNA_GENE_PROTEIN_EDGES.txt`
- `REACTOME_PW_GO_MAPPINGS.txt`
- `ENTREZ_GENE_PRO_ONTOLOGY_MAP.txt`
- `SO_GENE_TRANSCRIPT_VARIANT_TYPE_MAPPING.txt`
- `GENE_SYMBOL_ENSEMBL_TRANSCRIPT_MAP.txt`
- `MESH_CHEBI_MAP.txt`

### Entity Types
| PheKnowLator Type | Cytos BioLink |
|-------------------|---------------|
| Gene (Entrez) | biolink:Gene |
| Protein (PRO) | biolink:Protein |
| Disease (DOID/MONDO) | biolink:Disease |
| Phenotype (HPO) | biolink:PhenotypicFeature |
| Chemical (CHEBI) | biolink:ChemicalEntity |
| Anatomy (UBERON) | biolink:AnatomicalEntity |
| Pathway (PW/Reactome) | biolink:Pathway |
| Variant (ClinVar) | biolink:SequenceVariant |

**Compatibility: HIGH** — uses OBO ontology identifiers. Needs conversion from RDF/OWL.

---

## 4. PlaNet (Clinical Trial KG)

**Size**: ~240M edges (train.tsv) | **Format**: TSV triples + entity/relation dicts

### Relations (26 types)

| Source | Relation | Cytos Predicate |
|--------|----------|-----------------|
| MESH | has_parent | biolink:subclass_of |
| UMLS | PAR | biolink:subclass_of |
| DISGENET | dis-gene | biolink:gene_associated_with_condition |
| GO | is_a | biolink:subclass_of |
| GO | part_of | biolink:part_of |
| GO | regulates | biolink:regulates |
| GO | negatively_regulates | biolink:negatively_regulates |
| GO | positively_regulates | biolink:positively_regulates |
| CLASSYFIRE | is_a | biolink:subclass_of |
| DRUGBANK | inhibitor | biolink:inhibits |
| DRUGBANK | antagonist | biolink:antagonist_of |
| DRUGBANK | agonist | biolink:agonist_of |
| DRUGBANK | inducer | biolink:induces |
| DRUGBANK | substrate | biolink:substrate_of |
| CTD | affects | biolink:affects |
| CTD | increases | biolink:increases |
| CTD | decreases | biolink:decreases |
| CLINICAL_TRIAL | study-disease | biolink:studies |
| CLINICAL_TRIAL | arm_tests_drug | biolink:has_active_ingredient |
| CLINICAL_TRIAL | primary_outcome | biolink:has_output |

**Compatibility: MEDIUM** — needs entity dictionary resolution (UMLS CUIs, MeSH, etc.).

---

## 5. Monarch Associations

15.36M edges with KGX-native BioLink categories and predicates.
Includes knowledge_level and agent_type metadata per edge.
486 information resources tracked.

---

## 6. Clinical Knowledge Graph (CKG)

**Status**: Schema mapped from BioCypher adapter | GitHub repos:
- Main: `github.com/MannLabs/CKG`
- BioCypher adapter: `github.com/biocypher/clinical-knowledge-graph`

### Node Types (BioCypher full_schema_config.yaml)

| CKG Type | BioLink is_a | Preferred ID | Cytos Mapping |
|----------|-------------|-------------|---------------|
| amino acid sequence | polypeptide | UniProt | biolink:Polypeptide |
| analytical sample | material sample | - | biolink:MaterialSample |
| biological sample | material sample | - | biolink:MaterialSample |
| biological process | biological process | GO | biolink:BiologicalProcess |
| cellular component | cellular component | GO | biolink:CellularComponent |
| chromosome | nucleic acid entity | chr | biolink:NucleicAcidEntity |
| phenotypic feature | phenotypic feature | SNOMEDCT | biolink:PhenotypicFeature |
| disease | disease | MONDO/DOID | biolink:Disease |
| drug | drug | DrugBank | biolink:Drug |
| clinical finding | clinical finding | EFO | biolink:ClinicalFinding |
| food | food | FOBI | biolink:ChemicalEntity |
| gene | gene | HGNC | biolink:Gene |
| GWAS study | study | - | biolink:Study |
| metabolite | small molecule | HMDB | biolink:SmallMolecule |
| modified protein | polypeptide | UniProt | biolink:Protein |
| molecular function | molecular activity | GO | biolink:MolecularActivity |
| pathway | pathway | Reactome | biolink:Pathway |
| peptide | polypeptide | - | biolink:Polypeptide |
| protein | protein | UniProt | biolink:Protein |
| protein domain | protein domain | Pfam | biolink:ProteinDomain |
| macromolecular complex | complex | CORUM | biolink:MacromolecularComplex |
| publication | publication | PMID | biolink:Publication |
| tissue | anatomical entity | UBERON/BTO | biolink:AnatomicalEntity |
| transcript | transcript | Ensembl | biolink:Transcript |
| known variant | sequence variant | dbSNP | biolink:SequenceVariant |
| somatic mutation | sequence variant | COSMIC | biolink:SequenceVariant |

### Key Relationship Types (35+)

| CKG Relationship | Cytos Predicate |
|-----------------|-----------------|
| COMPILED_INTERACTS_WITH | biolink:interacts_with |
| CURATED_INTERACTS_WITH | biolink:interacts_with |
| TRANSLATED_INTO (Gene→Protein) | biolink:has_gene_product |
| TRANSCRIBED_INTO (Gene→Transcript) | biolink:transcribed_to |
| VARIANT_FOUND_IN_PROTEIN | biolink:is_sequence_variant_of |
| VARIANT_FOUND_IN_GENE | biolink:is_sequence_variant_of |
| ASSOCIATED_WITH_Disease | biolink:associated_with |
| IS_BIOMARKER_OF_DISEASE | biolink:biomarker_for |
| DETECTED_IN_PATHOLOGY_SAMPLE | biolink:expressed_in |
| ANNOTATED_IN_PATHWAY | biolink:participates_in |
| HAS_MODIFICATION (PTM) | biolink:has_attribute |
| HAS_QUANTIFIED_PROTEIN | biolink:has_output |
| STUDIES_TRAIT (GWAS) | biolink:studies |
| PUBLISHED_IN | biolink:published_in |
| IS_SUBUNIT_OF | biolink:part_of |
| HAS_CONTENT (food→metabolite) | biolink:has_part |

**Compatibility: HIGH** — BioCypher adapter provides complete BioLink mapping.
Proteomics-specific types (analytical sample, peptide, modified protein, PTMs) extend
our schema in a clinical proteomics direction.

---

## Topic Area Ontologies

### For Scholarly KG Annotation

| Ontology | Description | Size | Verdict |
|----------|-------------|------|---------|
| AIO (AI Ontology) | ML/DL layer types, architectures | ~300 terms | ✅ Import (ML model annotation) |
| CSO 3.5 (Computer Science) | CS research topics hierarchy | ~15K terms | ✅ Import (paper topics) |
| ROADMAP | Research topic roadmap | ~2K terms | ✅ Import (project topics) |
| NCIT (NCI Thesaurus) | Cancer/disease topics | ~180K terms | ⚠️ Already in KG via UMLS |
| Annett-O | Annotation ontology | ~1K terms | ❌ Skip (too narrow) |

### Recommended Imports
1. **AIO** → annotate MLModel nodes
2. **CSO 3.5** → annotate Paper.topics field
3. **ROADMAP** → annotate Project/Investigation nodes
4. **MeSH descriptors** (already in KG) → primary paper annotation

---

## Identifier Standards

### Primary IDs (Cytos canonical)

| Domain | Primary | Cross-ref via |
|--------|---------|---------------|
| Genes | Ensembl (ENSG) | HGNC, NCBI Gene, UniProt |
| RNA/Transcripts | Ensembl (ENST) | RefSeq, GENCODE |
| Proteins | UniProtKB | Ensembl (ENSP), PDB |
| Chemicals | PubChem CID | CHEBI, DrugBank, UniChem |
| Diseases | MONDO | OMIM, DOID, MeSH, ICD |
| Phenotypes | HPO | UMLS CUI, MP |
| Anatomy | UBERON | FMA, MeSH |
| Cell Types | CL | MeSH |

### UniChem Update Plan
- Current: `/home/mohammadi/datasets/identifiers/databases/UniChem/` (old)
- Download: `ftp://ftp.ebi.ac.uk/pub/databases/chembl/UniChem/data/table_dumps/`
- Tables: `reference.tsv`, `source.tsv`, `structure.tsv`
- Use: Map PubChem ↔ CHEBI ↔ DrugBank ↔ ChEMBL
