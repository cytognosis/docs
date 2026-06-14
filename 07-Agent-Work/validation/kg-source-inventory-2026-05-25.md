# Phase E: Knowledge Graph Construction Report

> **Date**: 2026-05-25  
> **Scripts**: [E1](file:///home/mohammadi/repos/cytognosis/scratch/test_kg_inventory.py) | [E2](file:///home/mohammadi/repos/cytognosis/scratch/test_opentargets_ingest.py) | [E3](file:///home/mohammadi/repos/cytognosis/scratch/test_monarch_ingest.py) | [E4](file:///home/mohammadi/repos/cytognosis/scratch/test_primekg_ingest.py) | [E5](file:///home/mohammadi/repos/cytognosis/scratch/test_stringdb_stitch_ingest.py)  
> **KG Builder**: [builder.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/kg/builder.py)  
> **OT Ingest**: [opentargets.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/ingest/linkmlize/opentargets.py)

---

## Executive Summary

| Source | Nodes/Entities | Edges/Interactions | Disk Size |
|--------|---------------:|-------------------:|----------:|
| Open Targets 26.03 | 148,932 (targets+diseases+drugs) | 4,508,002 associations + 14.6M interactions | Multi-GB Parquet |
| Monarch KG | 1,379,605 | 15,356,321 | 7.0 GB DuckDB |
| PrimeKG | 129,375 | 8,100,498 | 3.9 GB CSV |
| PharmaProjects | 209,753 (drugs+programs+diseases+genes) | 57,658 drug-gene links | 134.9 MB JSON |
| StringDB v12.0 | 19,699 proteins | 13,715,404 total; 473,860 high-conf (≥700) | 374.6 MB |
| STITCH v5.0 | — | 15.5M chem-prot + 17.7M chem-chem + 21.8M actions | 36.4 GB |
| **TOTALS** | **~1.89M unique entities** | **~95M edges/interactions** | **~48 GB** |

---

## E.1 KG Source Inventory

### 1. Open Targets 26.03

- **Path**: `/home/mohammadi/datasets/03-knowledge-graphs/open-targets-latest/26.03/output/`
- **55 subdirectories** covering targets, diseases, drugs, evidence, associations, interactions, and more

| Dataset | Files | Size | Rows | Key Columns |
|---------|------:|-----:|-----:|-------------|
| `target` | 10 parquet | ~130 MB | 62,768 | id, approvedSymbol, approvedName, biotype, chromosome |
| `disease` | 1 parquet | ~6 MB | 25,166 | id, name, description, therapeuticAreas, parents |
| `drug_molecule` | 5 parquet | 2.6 MB | 22,230 | id, name, drugType, canonicalSmiles, maximumClinicalStage |
| `association_overall_direct` | 43 parquet | 604 MB | 4,508,002 | diseaseId, targetId, associationScore, evidenceCount |
| `interaction` | 8 parquet | 86.8 MB | 14,618,053 | sourceDatabase, targetA, targetB, scoring |
| `drug_mechanism_of_action` | 2 parquet | 566 KB | 6,505 | actionType, mechanismOfAction, targets |
| `disease_phenotype` | 1 parquet | 7.6 MB | 180,981 | disease, phenotype, evidence |

### 2. Monarch KG

- **Path**: `/home/mohammadi/datasets/03-knowledge-graphs/monarch/kg/`
- **DuckDB**: `monarch-kg.duckdb` — 7.0 GB, 16 tables

**Nodes by Category (1,379,605 total)**:

| Category | Count |
|----------|------:|
| biolink:Gene | 585,115 |
| biolink:SequenceVariant | 218,546 |
| biolink:PhenotypicFeature | 171,728 |
| biolink:Genotype | 139,197 |
| biolink:AnatomicalEntity | 66,147 |
| biolink:NamedThing | 34,060 |
| biolink:BiologicalProcess | 30,817 |
| biolink:Disease | 30,553 |
| biolink:Protein | 26,643 |
| biolink:Pathway | 22,627 |
| biolink:ChemicalEntity | 22,273 |
| biolink:MolecularActivity | 12,805 |
| biolink:Case | 8,207 |
| biolink:CellularComponent | 4,574 |
| biolink:Cell | 3,449 |
| biolink:OrganismTaxon | 2,021 |
| biolink:MolecularEntity | 529 |
| biolink:LifeStage | 314 |

**Edges by Predicate (15,356,321 total)**:

| Predicate | Count |
|-----------|------:|
| biolink:interacts_with | 2,758,065 |
| biolink:expressed_in | 2,443,986 |
| biolink:has_phenotype | 2,141,321 |
| biolink:orthologous_to | 1,729,200 |
| biolink:enables | 1,305,485 |
| biolink:actively_involved_in | 1,133,499 |
| biolink:related_to | 1,053,168 |
| biolink:located_in | 774,267 |
| biolink:subclass_of | 632,420 |
| biolink:participates_in | 346,478 |
| biolink:acts_upstream_of_or_within | 234,963 |
| biolink:is_sequence_variant_of | 190,074 |
| biolink:is_active_in | 177,016 |
| biolink:has_sequence_variant | 159,036 |
| biolink:part_of | 144,317 |

**Additional**: 1,262,397 cross-ontology mappings, 20,563,398 closure entries.

**16 Association Files** (gzipped TSV, KGX-compatible):

| Association Type | Rows |
|------------------|-----:|
| pairwise_gene_to_gene_interaction | 2,758,065 |
| gene_to_expression_site | 2,443,986 |
| gene_to_gene_homology | 1,729,200 |
| macromolecular_machine_to_biological_process | 1,374,572 |
| macromolecular_machine_to_molecular_activity | 1,315,292 |
| variant_to_phenotypic_feature | 320,880 |
| disease_to_phenotypic_feature | 256,073 |
| gene_to_pathway | 239,528 |
| variant_to_gene | 190,074 |
| variant_to_disease | 21,091 |
| genotype_to_disease | 10,271 |
| correlated_gene_to_disease | 8,735 |
| disease_to_genetic_inheritance | 8,820 |
| causal_gene_to_disease | 7,048 |
| disease_to_location | 1,018 |
| chemical_to_disease_or_phenotype | 951 |

### 3. PrimeKG

- **Path**: `/home/mohammadi/datasets/03-knowledge-graphs/primekg/`
- **Total size**: 3.9 GB across 12 files

**Nodes (129,375)** by type:

| Node Type | Count |
|-----------|------:|
| biological_process | 28,642 |
| gene/protein | 27,671 |
| disease | 17,080 |
| effect/phenotype | 15,311 |
| anatomy | 14,035 |
| molecular_function | 11,169 |
| drug | 7,957 |
| cellular_component | 4,176 |
| pathway | 2,516 |
| exposure | 818 |

**Edges (8,100,498)** — 30 unique relation types:

| Relation | Count |
|----------|------:|
| anatomy_protein_present | 3,036,406 |
| drug_drug | 2,672,628 |
| protein_protein | 642,150 |
| disease_phenotype_positive | 300,634 |
| bioprocess_protein | 289,610 |
| cellcomp_protein | 166,804 |
| disease_protein | 160,822 |
| molfunc_protein | 139,060 |
| drug_effect | 129,568 |
| bioprocess_bioprocess | 105,772 |
| pathway_protein | 85,292 |
| disease_disease | 64,388 |
| contraindication | 61,350 |
| drug_protein | 51,306 |
| anatomy_protein_absent | 39,774 |
| phenotype_phenotype | 37,472 |
| anatomy_anatomy | 28,064 |
| molfunc_molfunc | 27,148 |
| indication | 18,776 |
| cellcomp_cellcomp | 9,690 |
| phenotype_protein | 6,660 |
| off-label use | 5,136 |
| pathway_pathway | 5,070 |
| exposure_disease | 4,608 |
| exposure_exposure | 4,140 |
| exposure_bioprocess | 3,250 |
| exposure_protein | 2,424 |
| disease_phenotype_negative | 2,386 |
| exposure_molfunc | 90 |
| exposure_cellcomp | 20 |

Schema: `relation, display_relation, x_index, x_id, x_type, x_name, x_source, y_index, y_id, y_type, y_name, y_source`

### 4. PharmaProjects

- **Path**: `/home/mohammadi/datasets/12-network/public/clinical/Pharmaprojects/`
- **Total size**: 134.9 MB

| File | Records | Key Fields |
|------|--------:|------------|
| pharmaprojects_drugs.json | 43,455 | id, generic_name, global_status, mechanisms_of_action, therapeutic_classes |
| pharmaprojects_programs.json | 104,392 | id, drug_id, disease_id, company_name, target_status, highest_status_reached |
| pharmaprojects_diseases.json | 1,411 | id, name, disease_type, omim_mim_number, mesh_terms, ICD10_terms, is_rare_disease |
| pharmaprojects_genes.json | 2,837 | entrez_id, target_name, target_families, target_synonyms |
| pharmaprojects_drug_to_entrez_id.json | 57,658 | pharmaprojects_drug_id, entrez_id |

### 5. StringDB v12.0

- **Path**: `/home/mohammadi/datasets/12-network/public/clinical/STRING/`
- **Total size**: 374.6 MB (human 9606 only)

| Dataset | Rows | Key Columns |
|---------|-----:|-------------|
| protein.links.detailed (gz) | 13,715,404 | protein1, protein2, neighborhood, fusion, cooccurence, coexpression, experimental, database, textmining, combined_score |
| protein.links.full (gz) | 13,715,404 | Same as above + transferred channels (16 cols) |
| protein.info (gz) | 19,699 | string_protein_id, preferred_name, protein_size, annotation |
| protein.aliases (gz) | — | Protein aliases |
| protein.network.embeddings (h5) | — | Network embeddings |
| protein.sequence.embeddings (h5) | — | Sequence embeddings |

**Interaction Confidence Thresholds**:

| Threshold | Count |
|-----------|------:|
| ≥ 400 (medium) | 1,858,944 |
| ≥ 700 (high) | 473,860 |
| ≥ 900 (highest) | 201,712 |

### 6. STITCH v5.0

- **Path**: `/home/mohammadi/datasets/12-network/public/clinical/STITCH/`
- **Total size**: 36.4 GB (human 9606 + global chemical data)

| Dataset | Rows | Key Columns |
|---------|-----:|-------------|
| Chemical-Protein Detailed | 15,473,939 | chemical, protein, experimental, prediction, database, textmining, combined_score |
| Actions (gz) | 21,773,491 | item_id_a, item_id_b, mode, action, a_is_acting, score |
| Chemical-Chemical Detailed | 17,705,818 | chemical1, chemical2, similarity, experimental, database, textmining, combined_score |
| Chemical-Protein Transfer | — | Transfer scores |

**Chemical-Protein Confidence Thresholds**:

| Threshold | Count |
|-----------|------:|
| ≥ 400 (medium) | 1,545,933 |
| ≥ 700 (high) | 466,669 |
| ≥ 900 (highest) | 150,645 |

**STITCH Action Modes** (21.8M total):

| Mode | Count |
|------|------:|
| binding | 17,763,861 |
| pred_bind | 2,483,728 |
| expression | 544,510 |
| inhibition | 309,827 |
| activation | 266,420 |
| reaction | 220,800 |
| catalysis | 184,345 |

---

## E.2 Open Targets Ingestion Test

All 7 OT datasets loaded via DuckDB Parquet reader:

| Dataset | Rows | Status |
|---------|-----:|--------|
| targets | 62,768 | ✅ Loaded |
| diseases | 25,166 | ✅ Loaded |
| drugs | 22,230 | ✅ Loaded |
| association_overall_direct | 4,508,002 | ✅ Loaded |
| interaction | 14,618,053 | ✅ Loaded |
| drug_mechanism_of_action | 6,505 | ✅ Loaded |
| disease_phenotype | 180,981 | ✅ Loaded |
| **Total entities** | **19,461,492** | |

The existing `OpenTargetsLinkMLizer` in [opentargets.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/ingest/linkmlize/opentargets.py) maps:
- `target/` → Gene (ensembl_gene_id, symbol, name, biotype, chromosome)
- `disease/` → Disease (mondo_id, name, description)
- `molecule/` → Drug (drugbank_id, name, drug_type, max_phase)

Note: OT 26.03 renamed the `molecule` directory to `drug_molecule`, and `maximumClinicalTrialPhase` to `maximumClinicalStage`. The existing linkmlizer references `molecule/` and the old column name. Both need updating for 26.03 compatibility.

---

## E.3 Monarch KG Ingestion Test

- **DuckDB size**: 7.0 GB, 16 tables
- **Total nodes**: 1,379,605 across 18 BioLink categories
- **Total edges**: 15,356,321 across 30 predicates
- **Closure table**: 20,563,398 entries (transitive closure)
- **Mappings**: 1,262,397 cross-ontology mappings
- **16 association TSV files** with standardized KGX schema

All data loaded and categorized. Monarch is already in BioLink-compatible KGX format, making integration straightforward.

---

## E.4 PrimeKG Ingestion Test

- **Nodes**: 129,375 across 10 entity types
- **Edges**: 8,100,498 across 30 relation types
- **Schema**: `kg.csv` (12 columns), `edges.csv` (4 columns), `nodes.csv` (5 columns)

> [!NOTE]
> PrimeKG's CSV uses embedded commas in drug names (e.g., `"6,4'-Dihydroxy-3-Methyl-3',5'-Dibromoflavone"`). DuckDB requires `quote='"'` and `ignore_errors=true` to parse correctly. The 8.1M edges span gene-protein, drug, disease, phenotype, anatomy, pathway, exposure, and molecular function interactions.

---

## E.5 StringDB + STITCH Ingestion Test

### STRING v12.0 (Human)
- **Total interactions**: 13,715,404
- **High-confidence (≥700)**: 473,860
- **Highest-confidence (≥900)**: 201,712
- **Unique proteins**: 19,699

### STITCH v5.0 (Human)
- **Chemical-Protein**: 15,473,939 total; 466,669 high-conf (≥700)
- **Actions**: 21,773,491 (binding: 17.8M, pred_bind: 2.5M)
- **Chemical-Chemical**: 17,705,818

---

## KG Builder Architecture

The existing [builder.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/kg/builder.py) (1,008 lines) assembles KGX-format nodes and edges from:
1. Ontology term Parquet (Phase C output)
2. UMLS normalized Parquet (Phase D output)
3. SNOMED concept/relationship Parquet
4. Cross-ontology SSSOM mappings
5. HRA (Human Reference Atlas) OWL

It produces `nodes.tsv` and `edges.tsv` in KGX format with BioLink categories. The builder does NOT yet integrate the sources tested here (OT, Monarch, PrimeKG, STRING, STITCH). Extension points exist via the `_merge_nodes` and `_merge_edges` methods.

---

## Script Outputs

| Script | Log File |
|--------|----------|
| E.1 Inventory | [E1_inventory.log](file:///home/mohammadi/repos/cytognosis/scratch/E1_inventory.log) |
| E.2 Open Targets | [E2_opentargets.log](file:///home/mohammadi/repos/cytognosis/scratch/E2_opentargets.log) |
| E.3 Monarch | [E3_monarch.log](file:///home/mohammadi/repos/cytognosis/scratch/E3_monarch.log) |
| E.4 PrimeKG | [E4_primekg.log](file:///home/mohammadi/repos/cytognosis/scratch/E4_primekg.log) |
| E.5 STRING/STITCH | [E5_string_stitch.log](file:///home/mohammadi/repos/cytognosis/scratch/E5_string_stitch.log) |
