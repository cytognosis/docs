# Revised A-to-Z Execution Plan

> Updated: 2026-05-12 | 666 predicates audited, 39 node categories analyzed

## KG Stats Before Fixes

| Metric | Value |
|--------|-------|
| Nodes | 9,673,136 |
| Edges | 60,111,215 |
| Distinct predicates | 666 |
| Standard biolink predicates | 53.18M edges (88.5%), 378 distinct |
| SKOS mapping predicates | 6.71M edges (11.2%), 3 distinct |
| **Non-standard (need resolution)** | **222K edges (0.3%), 285 distinct** |
| NamedThing nodes (under-typed) | 707,133 |
| OrganismTaxon (over-populated) | 1,592,901 |

---

## Phase A: KG Quality Fixes

### A1: Fix Zero-Edge Ontologies ⬅ START HERE

| Ontology | Nodes | Edges Now | Expected | Fix |
|----------|------:|----------:|----------|-----|
| BAO | 1,534 | 0 | ~2K | Re-parse with rdflib (pronto misses complex OWL axioms) |
| ICO | 1,558 | 0 | ~1.5K | Same fix |

### A2: Resolve Non-Standard Predicates (285 distinct, 222K edges)

**Categories of non-standard predicates:**

| Category | Distinct | Edges | Action |
|----------|--------:|------:|--------|
| `biolink:RO:*` (Relation Ontology CURIEs) | 202 | 117K | Map to human-readable BioLink labels using RO OWL |
| `biolink:BFO:*` (Basic Formal Ontology) | 14 | 61K | Map to readable labels |
| `biolink:http://...` (full URIs leaked) | 69 | 24K | Resolve to CURIEs, then map |
| `biolink:CLO:*`, `OPMI:*`, `OBI:*`, etc. | varies | 21K | Map to nearest BioLink predicate |

**Top non-standard predicates to map:**

| Raw Predicate | Edges | Correct BioLink Label |
|--------------|------:|----------------------|
| `biolink:BFO:0000050` | 53,615 | `biolink:part_of` |
| `biolink:RO:0002314` | 9,464 | `biolink:inheres_in_part_of` |
| `biolink:CLO:0000179` | 8,580 | `biolink:cell_derives_from` |
| `biolink:RO:0002162` | 7,897 | `biolink:in_taxon` |
| `biolink:RO:0002353` | 6,467 | `biolink:output_of` |
| `biolink:RO:0002211` | 6,141 | `biolink:regulates` |
| `biolink:RO:0002202` | 5,905 | `biolink:develops_from` |
| `biolink:BFO:0000051` | 5,810 | `biolink:has_part` |
| `biolink:RO:0002213` | 5,282 | `biolink:positively_regulates` |
| `biolink:RO:0002212` | 5,276 | `biolink:negatively_regulates` |

**Also fix clinical SNOMED predicates:**

| Current | Edges | Better Label |
|---------|------:|-------------|
| `biolink:has_finding_site` | 221,566 | Keep (SNOMED standard) |
| `biolink:has_associated_morphology` | 166,132 | Keep (SNOMED standard) |
| `biolink:has_default_outpatient_classification` | 150,230 | Keep (CCS standard) |
| `biolink:has_default_inpatient_classification` | 150,230 | Keep (CCS standard) |
| `biolink:method_of` | 199,734 | Keep (SNOMED standard) |
| `biolink:carries_out` | 80,966 | Keep (SNOMED standard) |
| `biolink:classified_as` | 378,930 | Keep (UMLS standard) |

### A3: Reclassify NamedThing Nodes (707K → specific types)

Reclassification strategy by prefix:

| Prefix | Nodes | Strategy |
|--------|------:|---------|
| MESH | 355K | MeSH tree: A→Anatomy, B→Organism, C→Disease, D→Chemical, E→Procedure, etc. |
| NCIT | 202K | NCIT semantic types → BioLink mapping |
| CHV | 58K | Map via UMLS CUI → inherit parent category |
| FOODON | 30K | → biolink:ChemicalEntity (food substances) |
| NCBITaxon | 16K | → biolink:OrganismTaxon |
| UMLS | 15K | Use MRSTY semantic type → BioLink |
| http/https | 15K | Resolve IRI → determine ontology |
| ENVO | 5K | → biolink:EnvironmentalFeature |
| FIDEO | 3K | → biolink:ChemicalEntity |
| Others | 8K | Per-ontology mapping |

### A4: Prune OrganismTaxon (1.59M → ~5K)

Steps:
1. Query CellxGene Census for unique species
2. Get scPRINT-2 species list
3. Compile model organisms + pets + pathogens whitelist
4. Keep NCBITaxon nodes that match whitelist OR have non-taxonomy edges
5. Remove remaining ~1.58M nodes and their taxonomy-only edges

### A5: Deduplicate Embedded Ontology Edges

1. Sort edges by `(subject, predicate, object)`
2. Remove exact duplicates, keeping the most specific `provided_by`
3. Verify edge counts post-dedup

---

## Phase B: New Ontology & Data Ingestion

### B1: Add SOHO + ACESO Ontologies
- Download OWL from BioPortal
- Parse with ontology_owl.py (with rdflib fallback)
- Add OLS4 SSSOM cross-mappings if available

### B2: Add GO-Plus
- Download go-plus.owl from OBO
- Parse → adds cross-ontology axioms (GO→CHEBI, GO→CL, etc.)
- Merge with existing GO nodes (no duplication)

### B3: Parse UniProt XML
- Parse uniprot_sprot.xml.gz (570K SwissProt entries)
- Extract: Protein nodes, Gene xrefs, GO annotations, disease associations
- Create edges: protein→gene, protein→taxon, protein→GO, protein→disease

---

## Phase C: Schema Integration

### C1: Integrate DDE Schemas
- m4ml → models.yaml (ML-specific properties)
- niaid → datasets.yaml, papers.yaml, agents.yaml (infectious disease metadata)
- nde → datasets.yaml (Sample, SampleCollection, ResourceCatalog)
- bioschemastypesdrafts → protocols.yaml (LabProtocol properties)

### C2: Import SEPIO-LinkML
- Clone sepio-framework/sepio-linkml
- Import as LinkML dependency (Assertion, Evidence, EvidenceLine)

### C3: Import GA4GH Pedigree
- Clone ga4gh/pedigree
- Convert JSON Schema → LinkML
- Test with sample pedigree data

### C4: Parse HED Schema
- Download HED schema XML
- Convert to LinkML controlled vocabulary + hierarchy

### C5: Parse ISA Model
- Parse ISA-JSON spec
- Convert to LinkML (Investigation→Study→Assay hierarchy)

### C6: Revise All Provisional Resource Schemas
- Merge DDE properties into existing YAML schemas
- Validate against live data
- Promote from draft to stable

---

## Phase D+: Remaining (unchanged from previous plan)

| Phase | Tasks |
|-------|-------|
| D | Scholarly KG (PKG2.0, BibTeX, OpenAlex) |
| E | Variant pipeline (VRS, GWAS, test datasets) |
| F | Phenopackets + Open Targets bulk |
| G | BioCypher + Koza automation |
| H | External KGs (Monarch, PrimeKG, NeuroKG, PheKnowLator, Petagraph) |
| I | Schema validation iteration loop |
| J | DVC + RO-Crate infrastructure |
| K | Neuro-specific tasks |

---

## Execution Checklist

- [ ] A1: Fix BAO/ICO zero-edge ontologies
- [ ] A2: Resolve 285 non-standard predicates
- [ ] A3: Reclassify 707K NamedThing nodes
- [ ] A4: Prune OrganismTaxon to ~5K
- [ ] A5: Deduplicate embedded ontology edges
- [ ] B1: Add SOHO + ACESO
- [ ] B2: Add GO-Plus
- [ ] B3: Parse UniProt XML
- [ ] C1: Integrate DDE schemas
- [ ] C2: Import SEPIO-LinkML
- [ ] C3: Import GA4GH Pedigree
- [ ] C4: Parse HED schema
- [ ] C5: Parse ISA model
- [ ] C6: Revise provisional schemas
- [ ] Re-export KG
