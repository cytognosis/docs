# Pre-Execution Audit: Answers & Task Plan

> Generated: 2026-05-12 | Answers to all outstanding questions

---

## 1. Provisional Schemas Needing Revision

These are the v0.4.0 resource schemas that exist as design documents but have NOT been validated against live data:

| Schema | File | Status | Revision Needed |
|--------|------|--------|-----------------|
| **Papers** | [papers.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/papers.yaml) | Draft | Integrate `niaid:ScholarlyArticle` (doi/pmid/pmcid), `nde:Dataset` citation refs, PKG2.0 field mapping |
| **Datasets** | [datasets.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/datasets.yaml) | Draft | Integrate `niaid:Dataset` (infectiousAgent, healthCondition, spatialCoverage, temporalCoverage), `nde:Dataset`, `creid:Dataset`, `bts:BioMedicalDataset` |
| **Models** | [models.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/models.yaml) | Draft | Integrate **m4ml** classes: `MLModel` (deployedAt, evaluationMetricValue, fineTunedBy, generatedBy, optimizedFor), `MLModelValidationAction`, `MLModelOptimizationAction`, `MLSoftwareSourceCode`, `MLSoftwareApplication` |
| **Code** | [code.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/code.yaml) | Draft | Integrate `m4ml:MLSoftwareSourceCode` (evaluationMetric, hyperparameter, mlAlgorithm, mlTask), `niaid:ComputationalTool` (applicationCategory, featureList, softwareHelp), `nde:ComputationalTool` |
| **Protocols** | [protocols.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/protocols.yaml) | Draft | Integrate `bioschemastypesdrafts:LabProtocol` (bioSampleUsed, reagentUsed, labEquipmentUsed), ISA model (Investigation → Study → Assay) |
| **Workflows** | [workflows.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/workflows.yaml) | Draft | No major DDE additions needed; validate against CWL/WDL instances |
| **Research Objects** | [research_objects.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/research_objects.yaml) | Draft | Validate against RO-Crate 1.2 spec |
| **Relationships** | [relationships.yaml](file:///home/mohammadi/Documents/Sorted/infra/schemas/resource_schemas/relationships.yaml) | Draft | Add SEPIO evidence/assertion predicates |
| **Bio Entities** | v0.4.0 lines 1221-1340 | Draft | Add `nde:Sample`, `nde:SampleCollection`, `nde:ResourceCatalog`, `nde:DataCollection` |
| **Clinical** | v0.4.0 lines 1335-1395 | Draft | Add GA4GH Pedigree classes |
| **License** | v0.4.0 lines 839-857 | Stable | No revision needed (already comprehensive) |

---

## 2. NamedThing Nodes: 707,133 Under-Typed Nodes

These nodes have `category = biolink:NamedThing` because our OWL parser or UMLS ingestion couldn't map them to a more specific BioLink category.

| Prefix | Count | Correct Category | Action |
|--------|------:|-----------------|--------|
| **MESH** | 355,283 | Mixed (use MeSH tree numbers to reclassify) | Re-map using MeSH tree: C=Disease, D=Chemical, A=Anatomy, etc. |
| **NCIT** | 202,053 | Mixed (NCI has own hierarchy) | Re-map using NCIT semantic types |
| **CHV** | 57,795 | Consumer health terms → map to parent ontology | Link to UMLS CUI → inherit category |
| **FOODON** | 30,103 | biolink:ChemicalEntity or biolink:EnvironmentalFeature | Re-classify as food/chemical |
| **NCBITaxon** | 15,773 | biolink:OrganismTaxon | Fix: should be OrganismTaxon |
| **UMLS** | 15,178 | Mixed (use semantic type) | Re-map using MRSTY |
| **http** | 11,819 | Mixed (IRI-based nodes) | Resolve IRIs → assign by source |
| **ENVO** | 4,894 | biolink:EnvironmentalFeature | Fix: should be EnvironmentalFeature |
| **FIDEO** | 2,676 | biolink:ChemicalEntity + interactions | Reclassify |
| **Other** | 11,669 | Various (PO, CDNO, SYMP, etc.) | Map per ontology |

**Action plan**: Write a `reclassify_named_things.py` script that uses MRSTY semantic types, MeSH tree numbers, and OWL ontology class hierarchy to promote these to specific BioLink categories.

---

## 3. OrganismTaxon: 1,592,901 → ~5,000 (pruning plan)

Currently 1.59M NCBITaxon nodes. Keep only:

| Criteria | Estimated Count | Source |
|----------|---------------:|--------|
| Model organisms (CXG schema) | ~15 | Homo sapiens, Mus musculus, Rattus norvegicus, Danio rerio, Drosophila melanogaster, C. elegans, S. cerevisiae, etc. |
| scPRINT-2 species | ~10 | Human, mouse, rat, zebrafish, fly, worm + any additional |
| Pets / companion animals | ~20 | Canis lupus familiaris, Felis catus, Equus caballus, + breeds |
| CellxGene Census species | **TBD** | Query `obs.organism_ontology_term_id` unique values |
| Species with KG edges | **TBD** | Any NCBITaxon node with ≥1 non-taxonomy edge |
| Key pathogens/viruses | ~200 | SARS-CoV-2, HIV, Influenza, etc. + linked to Disease nodes |
| **Total keep** | **~5,000** | |
| **Nodes to prune** | **~1,587,000** | |

**Next step**: Query CellxGene Census for species list, then filter.

---

## 4. Cross-Ontology / Annotation Mappings Status

### ✅ Added (Present in KG)

| Mapping Source | Edges | Type |
|---------------|------:|------|
| OLS4 SSSOM (45 files) | 1,273,903 | Cross-ontology (skos:exactMatch, closeMatch, etc.) |
| UMLS MRREL | ~4.3M | Vocabulary cross-references |
| UMLS MRCONSO xrefs | ~1.4M | Concept-to-concept |
| UMLS MRMAP (SNOMEDCT_US) | 772,866 + 314,179 | Clinical coding maps |
| UMLS MRMAP (CCSR_ICD10CM) | 474,280 + 237,140 | Clinical classification |
| SNOMED simple maps | 1,108,246 | SNOMED → ICD-10 etc. |
| SNOMED ext maps | 314,179 | Extended mappings |
| bero | 481,785 | Biomedical entity resolution |
| UPHENO | 320,349 | Phenotype cross-species |
| Ensembl xrefs | ~600K | Via EnsemblOntologyResolver |

### ❌ Missing / Must Add

| Mapping | Priority | Source | Why Needed |
|---------|----------|--------|-----------|
| **MONDO → DOID → OMIM** disease mappings | P1 | MONDO SSSOM | Unify disease identifiers |
| **Gene → Protein** (UniProt xrefs) | P1 | UniProt XML | Gene-protein linking |
| **Drug → Target** (DrugBank) | P1 | DrugBank/ChEMBL | Drug mechanism edges |
| **HPO → MONDO** (disease-phenotype) | P1 | HPO annotations | Phenotype-disease links |
| **GO annotations** (gene → GO term) | P1 | GOA file | Gene function edges |
| **ClinVar** (variant → disease) | P2 | ClinVar VCF/XML | Variant pathogenicity |
| **Reactome** (gene → pathway) | P2 | Reactome SBML/BioPAX | Pathway membership |
| **OMIM → Gene** | P2 | OMIM genemap2 | Mendelian disease-gene |
| **ChEBI → DrugBank** chemical xrefs | P2 | ChEBI xrefs | Chemical identity |

---

## 5. Zero-Edge Ontologies: Root Cause & Fix

### Actual edge counts from KG:

| Ontology | Nodes | Edges | Expected | Root Cause |
|----------|------:|------:|----------|-----------|
| DOID | 19,493 | 26,983 | ~35K+ | **Partial** — many DOID→external edges lost because imported terms (from CHEBI, UBERON, etc.) were deduplicated |
| DPO | 1,552 | 2,977 | ~3K | OK — small ontology |
| **BAO** | **1,534** | **0** | ~2K+ | **BUG** — OWL parser missed BAO rdfs:subClassOf edges |
| **ICO** | **1,558** | **0** | ~1.5K | **BUG** — same issue, OWL parser missed hierarchy |
| OPMI | 3,153 | 4,178 | ~4K | OK |
| FIDEO | 3,543 | 2,542 | ~3K | OK |
| ONS | 4,834 | 5,230 | ~5K | OK |
| NMDCO | 13,682 | 29,726 | ~30K | OK |
| HHEAR | 4,010 | 4,184 | ~4K | OK |
| MAXO | 7,120 | 15,276 | ~15K | OK |
| OBI | 5,178 | 7,545 | ~8K | OK |

### Why DOID has fewer edges than expected

DOID imports terms from CHEBI, UBERON, CL, HP, SYMP, etc. Our parser:
1. Extracted DOID-native terms correctly (19K nodes)
2. Extracted DOID-native `subClassOf` edges (27K)
3. **But**: edges from DOID terms to imported terms (e.g., `DOID:123 → has_material_basis_in CHEBI:456`) were stored with the imported term's prefix, NOT `owl:doid`
4. These cross-ontology edges exist but are attributed to CHEBI/UBERON/etc.

**Fix**: Re-parse DOID/BAO/ICO with edge attribution to the source ontology file, not the target term's prefix.

### Why BAO and ICO have ZERO edges

The OWL parser (`ontology_owl.py`) uses `pronto` which sometimes fails to extract `rdfs:subClassOf` from OWL files that use complex OWL axioms (restrictions, intersections). BAO and ICO use these heavily.

**Fix**: Use `owlready2` or `rdflib` as fallback parser for BAO and ICO to extract all axioms.

---

## 6. Embedded Ontology Deduplication

Several ontologies import terms from others:

| Ontology | Imports From | Risk |
|----------|-------------|------|
| DOID | CHEBI, UBERON, CL, HP, SYMP, NCBITaxon, SO | Node duplication |
| MONDO | DOID, OMIM, ORDO, NCBITaxon, HP | Node duplication |
| EFO | CHEBI, UBERON, CL, HP, MONDO, DOID, GO | Node duplication |
| OBA | PATO, UBERON, CL, GO, CHEBI | Node duplication |
| ECTO | CHEBI, ENVO, ExO, UBERON, NCBITaxon | Node duplication |
| CLO | CL, UBERON, NCBITaxon | Node duplication |

**Current approach**: Our parser creates nodes with the imported term's original CURIE (e.g., `CHEBI:12345`), so they merge with existing CHEBI nodes. This is correct for nodes.

**Problem**: Edges may be duplicated if both the source ontology and the importing ontology declare the same `subClassOf` relationship.

**Fix**: Deduplicate edges by `(subject, predicate, object)` triple, keeping the most specific `provided_by` attribution.

---

## 7. DDE Schema Integration Matrix

### Fetched and Analyzed

| Namespace | Classes | Key Properties to Integrate |
|-----------|---------|---------------------------|
| **m4ml** (5 classes) | MLSoftwareSourceCode, MLSoftwareApplication, MLModel, MLModelOptimizationAction, MLModelValidationAction | `evaluationMetric`, `hyperparameter`, `mlAlgorithm`, `mlTask`, `deployedAt`, `evaluationMetricValue`, `fineTunedBy`, `generatedBy`, `optimizedFor`, `retrainedBy`, `ethicalLegalSocial`, `intendedUse` + codemeta: contIntegration, buildInstructions, developmentStatus, embargoDate, issueTracker, referencePublication, readme |
| **niaid** (8 classes) | Dataset, ComputationalTool, ScholarlyArticle, MonetaryGrant, Organization, DataDownload, TemporalInterval, AdministrativeArea | `infectiousAgent`, `healthCondition`, `species`, `funding`, `spatialCoverage`, `temporalCoverage`, doi/pmid/pmcid, `locationType`, `temporalType` |
| **nde** (6 classes) | Dataset, ComputationalTool, Sample, SampleCollection, ResourceCatalog, DataCollection | `sample` (new!), `sampleCollection`, `resourceCatalog` |
| **creid** | Dataset | Extends niaid:Dataset with CREID-specific fields |
| **bts** | BioMedicalDataset | Biomedical-specific dataset extensions |
| **m4mlProfiles** | MLModel (profile) | Simplified m4ml for submission profiles |
| **bioschemastypesdrafts** | LabProtocol | `bioSampleUsed`, `reagentUsed`, `labEquipmentUsed`, `protocolPurpose`, `protocolOutcome` |

### Integration Plan: What goes into our schemas

| Our Schema | DDE Properties to Add | Source |
|-----------|----------------------|--------|
| **models.yaml** | `evaluation_metric`, `hyperparameter`, `ml_algorithm`, `ml_task`, `deployed_at`, `evaluation_metric_value`, `fine_tuned_by`, `generated_by`, `optimized_for`, `retrained_by`, `ethical_legal_social`, `intended_use` | m4ml |
| **models.yaml** | `MLModelValidationAction` class, `MLModelOptimizationAction` class | m4ml |
| **code.yaml** | `cont_integration`, `build_instructions`, `development_status`, `embargo_date`, `issue_tracker`, `reference_publication`, `readme_url` | m4ml/codemeta |
| **datasets.yaml** | `infectious_agent`, `health_condition`, `spatial_coverage`, `temporal_coverage`, `measurement_technique` (EDAM/NCIT terms) | niaid |
| **datasets.yaml** | `Sample`, `SampleCollection`, `ResourceCatalog`, `DataCollection` classes | nde |
| **papers.yaml** | `doi`, `pmid`, `pmcid` as first-class slots (not just in external_ids) | niaid |
| **protocols.yaml** | `bio_sample_used`, `reagent_used`, `lab_equipment_used`, `protocol_purpose`, `protocol_outcome` | bioschemastypesdrafts |
| **scholarly_base.yaml** | `TemporalInterval` class, `AdministrativeArea` class | niaid |
| **agents.yaml** | `MonetaryGrant` enhancement (funder + parentOrganization) | niaid |

---

## 8. New Ontologies to Add

| Ontology | Source | Expected Terms | Priority |
|----------|--------|---------------|----------|
| **SOHO** (Social Determinants of Health) | [BioPortal](https://bioportal.bioontology.org/ontologies/SOHO) | ~500 | P1 |
| **ACESO** (Adverse Childhood Experiences) | [BioPortal](https://bioportal.bioontology.org/ontologies/ACESO) | ~200 | P1 |
| **GO-Plus** (Gene Ontology with cross-refs) | [OBO](http://purl.obolibrary.org/obo/go/extensions/go-plus.owl) | ~50K (extends existing GO) | P1 |
| **OBI** (already partially in: 5,178 nodes) | Already ingested | Need edge re-parse | P1 (fix edges) |
| **GO** (already in: 51,937 nodes) | Already ingested | Verify completeness | ✅ Done |

---

## 9. Schema/Ontology Imports to Add

| Source | Type | Classes/Terms | Action |
|--------|------|--------------|--------|
| **HED** (Hierarchical Event Descriptors) | Schema + controlled vocab | ~1,200 tags in 8 groups | Parse HED schema XML → LinkML classes + controlled vocabulary terms → KG nodes |
| **ISA** (Investigation-Study-Assay) | Schema | Investigation, Study, Assay, Protocol, Source, Sample, Factor, etc. | Parse ISA-JSON spec → LinkML classes (aligns with our protocols.yaml) |
| **SEPIO** (sepio-linkml) | LinkML schema | Assertion, Evidence, EvidenceLine, Proposition, Statement | Clone repo → import directly as LinkML dependency; adds evidence/assertion layer |
| **GA4GH Pedigree** | JSON Schema | Pedigree, Individual, Relationship, Condition, Pregnancy | Clone repo → convert JSON Schema → LinkML; test with sample pedigree |
| **UniProt** (sprot XML) | Data | ~570K protein entries | Parse XML → Protein nodes + Gene xrefs + function annotations + disease associations |

### UniProt XML (`uniprot_sprot.xml.gz`, ~800MB compressed)

Fields to extract per entry:
- `accession` → Protein node ID (UniProt:P04637)
- `protein/recommendedName` → name
- `gene/name[@type='primary']` → gene cross-ref
- `organism/dbReference[@type='NCBI Taxonomy']` → taxon link
- `dbReference` → cross-refs (PDB, Ensembl, HGNC, GO, Reactome, etc.)
- `comment[@type='function']` → function annotation
- `comment[@type='disease']` → disease association
- `feature` → domains, variants, modifications
- `keyword` → keyword annotations

---

## 10. Execution Order for This Batch

```
1. Fix zero-edge ontologies (BAO, ICO) - re-parse with rdflib fallback
2. Add SOHO + ACESO ontologies
3. Add GO-Plus (extends existing GO with cross-ontology axioms)
4. Reclassify NamedThing nodes (707K → specific categories)
5. Prune OrganismTaxon (1.59M → ~5K) via CXG Census species query
6. Deduplicate embedded ontology edges
7. Parse UniProt XML → protein nodes + edges
8. Import SEPIO-LinkML + GA4GH Pedigree
9. Parse HED schema + ISA model → LinkML
10. Integrate DDE schemas into our resource YAMLs
11. Re-export KG (nodes.tsv, edges.tsv, parquet, Neo4j)
```
