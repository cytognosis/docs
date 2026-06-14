# Molecular/Clinical KG: Entity & Relationship Audit

> **Date**: 2026-05-12 | **KG Scale**: 10.7M nodes, 118.5M edges, 4 molecular sources

## 1. Entity Types (Node Categories)

### Schema Maturity Legend

| Rating | Meaning | Criteria |
|--------|---------|----------|
| 🟢 **Stable** | Community-backed, well-defined | Has LinkML schema, validated by 2+ sources, aligns to community standard |
| 🟡 **Provisional** | Functional but needs refinement | Has basic schema, sourced from 1 KG, fields may change |
| 🔴 **Missing** | No dedicated schema | Catch-all category or untyped, needs reclassification |

### Tier 1: Core Biomedical Entities (>100K nodes, stable schemas)

| Entity Type | Node Count | Sources | Schema | Community Standard | Maturity |
|-------------|----------:|---------|--------|-------------------|----------|
| `biolink:Disease` | 1,093,827 | Monarch, PrimeKG, OT, Core | `disease.yaml` | MONDO, DOID, OMIM | 🟢 Stable |
| `biolink:Protein` | 894,830 | Monarch, Core | `gene.yaml` | UniProt, PR ontology | 🟢 Stable |
| `biolink:Gene` | 846,437 | Monarch, PrimeKG, OT, Core | `gene.yaml` | HGNC, Ensembl, NCBI Gene | 🟢 Stable |
| `biolink:ChemicalEntity` | 630,302 | Monarch, Core | `drug.yaml` | CHEBI, PubChem | 🟢 Stable |
| `biolink:Drug` | 592,753 | PrimeKG, OT, Core | `drug.yaml` | DrugBank, ChEMBL | 🟢 Stable |
| `biolink:AnatomicalEntity` | 485,242 | Monarch, PrimeKG, Core | `anatomy.yaml` | UBERON, HRA | 🟢 Stable |
| `biolink:PhenotypicFeature` | 427,704 | Monarch, PrimeKG, Core | `disease.yaml` | HP, MP | 🟢 Stable |
| `biolink:BiologicalProcess` | 292,043 | Monarch, PrimeKG, Core | `pathway.yaml` | GO (BP) | 🟢 Stable |
| `biolink:SequenceVariant` | 218,546 | Monarch | `variant.yaml` | VRS 2.0, ClinVar, dbSNP | 🟢 Stable |
| `biolink:Genotype` | 139,197 | Monarch | `variant.yaml` | VRS 2.0 | 🟢 Stable |
| `biolink:Cell` | 99,472 | Monarch, Core | `anatomy.yaml` | CL | 🟢 Stable |

### Tier 2: Clinical/Regulatory Entities (>50K nodes, provisional schemas)

| Entity Type | Node Count | Sources | Schema | Community Standard | Maturity |
|-------------|----------:|---------|--------|-------------------|----------|
| `biolink:ClinicalFinding` | 1,393,204 | Core (UMLS) | `clinical.yaml` | SNOMED CT findings | 🟡 Provisional |
| `biolink:ClinicalAttribute` | 732,925 | Core (UMLS) | `clinical.yaml` | SNOMED, LOINC | 🟡 Provisional |
| `biolink:Procedure` | 707,855 | Core (UMLS) | `clinical.yaml` | SNOMED, CPT, MAXO | 🟡 Provisional |
| `biolink:EnvironmentalFeature` | 363,661 | Core | `environment.yaml` | ENVO, ECTO | 🟡 Provisional |
| `biolink:OrganismTaxon` | 184,325 | Monarch, Core | `taxonomy.yaml` | NCBITaxon | 🟡 Provisional |
| `biolink:CellLine` | 167,186 | Core | `environment.yaml` | CLO, Cellosaurus | 🟡 Provisional |
| `biolink:ExperimentalFactor` | 96,973 | Core | `environment.yaml` | EFO | 🟡 Provisional |
| `biolink:Device` | 74,912 | Core | `sensor.yaml` | SNOMED, GMDN | 🟡 Provisional |
| `biolink:MolecularActivity` | 51,924 | Monarch, PrimeKG, Core | `pathway.yaml` | GO (MF) | 🟢 Stable |

### Tier 3: Specialized Entities (<50K nodes)

| Entity Type | Node Count | Sources | Schema | Community Standard | Maturity |
|-------------|----------:|---------|--------|-------------------|----------|
| `biolink:Pathway` | 27,889 | Monarch, PrimeKG, Core | `pathway.yaml` | Reactome, KEGG, WikiPathways | 🟢 Stable |
| `biolink:ExposureEvent` | 21,161 | Core | `environment.yaml` | ECTO | 🟡 Provisional |
| `biolink:CellularComponent` | 18,497 | Monarch, PrimeKG, Core | `pathway.yaml` | GO (CC) | 🟢 Stable |
| `biolink:NucleicAcidEntity` | 16,792 | Core | `information.yaml` | SO | 🟡 Provisional |
| `biolink:Activity` | 12,644 | Core | `information.yaml` | — | 🟡 Provisional |
| `biolink:PopulationOfIndividualOrganisms` | 12,109 | Core | — | GAZ | 🔴 Missing |
| `biolink:Case` | 8,207 | Monarch | — | Phenopackets | 🔴 Missing |
| `biolink:IndividualOrganism` | 7,829 | Core | — | ORCID (for humans) | 🔴 Missing |
| `biolink:PhenotypicQuality` | 7,746 | Core | `disease.yaml` | PATO | 🟡 Provisional |
| `biolink:QuantityValue` | 5,981 | Core | — | QUDT, UO | 🔴 Missing |
| `biolink:Attribute` | 5,647 | Core | — | — | 🔴 Missing |
| `biolink:GeographicLocation` | 5,046 | Core | — | GAZ | 🔴 Missing |
| `biolink:Behavior` | 5,003 | Core | — | NBO | 🔴 Missing |
| `biolink:Agent` | 3,480 | Core | — | FOAF, ORCID | 🔴 Missing |
| `biolink:LifeStage` | 2,354 | Monarch, Core | `anatomy.yaml` | HsapDv, MmusDv | 🟡 Provisional |
| `biolink:EnvironmentalExposure` | 818 | PrimeKG | `environment.yaml` | ECTO | 🟡 Provisional |

### Tier 4: Reclassification Needed

| Entity Type | Node Count | Sources | Issue |
|-------------|----------:|---------|-------|
| `biolink:NamedThing` | 296,570 | Monarch (34K), PlaNet (185K), Core (78K) | Generic catch-all. PlaNet nodes are mostly Disease/Drug/Condition (resolvable via MeSH/CUI mapping). Core/Monarch nodes need individual triage. |
| `biolink:InformationContentEntity` | 597,848 | Core | Overly broad. Contains UMLS concepts that could be reclassified to Disease, Procedure, or Finding. |

---

## 2. Relationship Types (Predicates)

### Molecular/Clinical Predicates by Category

#### Gene-Disease Associations

| Predicate | Count | Sources | MI Alignment | Notes |
|-----------|------:|---------|-------------|-------|
| `biolink:gene_associated_with_condition` | 652,863 | Monarch, PrimeKG, OT, PlaNet | — | Primary gene-disease link |
| `biolink:causes` | 19,337 | Monarch | — | Causal gene-disease |
| `biolink:contributes_to` | 15,207 | Monarch, PrimeKG | — | Contributing factor |
| `biolink:associated_with_increased_likelihood_of` | 5,008 | Monarch | — | Risk factor |
| `biolink:has_mode_of_inheritance` | 8,820 | Monarch | — | AR, AD, XL, etc. |
| `biolink:model_of` | 10,271 | Monarch | — | Animal model of disease |
| `biolink:has_disease` | 8,183 | Monarch | — | Phenotype→disease |

#### Protein-Protein / Molecular Interactions

| Predicate | Count | Sources | MI Alignment | Notes |
|-----------|------:|---------|-------------|-------|
| `biolink:interacts_with` | 6,124,149 | Monarch, PrimeKG | `MI:0190` (interaction type) | **NEEDS SUBTYPING**: lumps all PPI, genetic, predicted. Per your report, should split into Functional/Molecular/Predicted/Phenotypic |
| `biolink:colocalizes_with` | 4,596 | Monarch | `MI:0403` (colocalization) | Subcellular co-occurrence |

> [!WARNING]
> `interacts_with` (6.1M edges) is our biggest unresolved predicate. It merges direct biophysical (Y2H, co-IP), indirect (co-expression), and predicted (STRING) interactions with no evidence typing. The MI ontology classification from your Harmonizing report should be applied retroactively.

#### Gene Expression & Function

| Predicate | Count | Sources | MI Alignment | Notes |
|-----------|------:|---------|-------------|-------|
| `biolink:expressed_in` | 5,480,392 | Monarch, PrimeKG | — | Gene/protein→tissue/cell |
| `biolink:not_expressed_in` | 39,774 | PrimeKG | — | Negative expression |
| `biolink:enables` | 1,444,545 | Monarch, PrimeKG | — | Gene→MolecularFunction (GO MF) |
| `biolink:actively_involved_in` | 1,133,499 | Monarch | — | Gene→BiologicalProcess (GO BP) |
| `biolink:located_in` | 940,071 | Monarch, PrimeKG | — | Gene→CellularComponent (GO CC) |
| `biolink:is_active_in` | 177,016 | Monarch | — | Gene active in cellular component |
| `biolink:participates_in` | 431,770 | Monarch, PrimeKG | — | Entity→Pathway |
| `biolink:acts_upstream_of_or_within` | 234,963 | Monarch | — | Causal GO annotation |
| `biolink:acts_upstream_of` | 4,038 | Monarch | — | Upstream regulator |

#### Drug Mechanisms

| Predicate | Count | Sources | MI Alignment | Notes |
|-----------|------:|---------|-------------|-------|
| `biolink:treats` | 23,912 | PrimeKG | — | Drug→Disease (approved) |
| `biolink:inhibitor` / `biolink:inhibits` | 10,727 | OT, PlaNet | — | Drug→Target (inhibition) |
| `biolink:antagonist` / `biolink:antagonist_of` | 3,983 | OT, PlaNet | — | Receptor antagonism |
| `biolink:agonist` / `biolink:agonist_of` | 3,067 | OT, PlaNet | — | Receptor agonism |
| `biolink:blocker` | 1,657 | OT | — | Channel/receptor blocker |
| `biolink:has_active_ingredient` | 131,908 | PlaNet | — | Drug→compound |
| `biolink:has_adverse_event` | 129,568 | PrimeKG | — | Drug→side effect |
| `biolink:contraindicated_for` | 61,350 | PrimeKG | — | Drug→condition (contra) |
| `biolink:positive_allosteric_modulator` | 1,055 | OT | — | Fine-grained drug mechanism |
| `biolink:modulator` | 446 | OT | — | Generic modulation |
| *(15+ more OT drug mechanism subtypes)* | ~1,500 | OT | — | Very fine-grained |

#### Variant & Genotype

| Predicate | Count | Sources | Notes |
|-----------|------:|---------|-------|
| `biolink:is_sequence_variant_of` | 190,074 | Monarch | Variant→Gene |
| `biolink:has_sequence_variant` | 159,036 | Monarch | Gene→Variant (reverse) |
| `biolink:has_gene` | 8,138 | Monarch | Genotype→Gene component |

#### Phenotype & Orthology

| Predicate | Count | Sources | Notes |
|-----------|------:|---------|-------|
| `biolink:has_phenotype` | 2,444,342 | Monarch, PrimeKG | Gene/Disease→Phenotype |
| `biolink:orthologous_to` | 1,729,212 | Monarch | Cross-species gene mapping |
| `biolink:homologous_to` | 14,036 | Monarch | Broader homology |

#### Clinical Trial Observations (PlaNet)

| Predicate | Count | Source | Notes |
|-----------|------:|--------|-------|
| `biolink:eligibility_exclusion` | 1,544,284 | PlaNet | Trial→Condition (exclusion criteria) |
| `biolink:eligibility_inclusion` | 813,029 | PlaNet | Trial→Condition (inclusion criteria) |
| `biolink:affects` | 432,821 | PlaNet | Drug/intervention→Condition |
| `biolink:has_output` | 354,518 | PlaNet | Trial→Outcome measure |
| `biolink:studies` | 112,889 | PlaNet | Trial→Entity under investigation |
| `biolink:increases_expression_of` | 10,960 | PlaNet | Drug→Gene (expression effect) |
| `biolink:decreases_expression_of` | 9,592 | PlaNet | Drug→Gene (expression effect) |
| `biolink:regulates` | 3,216 | PlaNet | Generic regulation |
| `biolink:positively_regulates` | 2,756 | PlaNet | Activation |
| `biolink:negatively_regulates` | 2,767 | PlaNet | Inhibition |
| `biolink:induces` | 875 | PlaNet | Drug→Effect |

#### Ambiguous / Needs Resolution

| Predicate | Count | Sources | Issue |
|-----------|------:|---------|-------|
| `biolink:related_to` | 17,589,344 | Multiple | **BIGGEST PROBLEM**: Catch-all from UMLS MRREL. Mixes hierarchical (PAR/CHD), synonymy (SY), broader/narrower (RB/RN), and genuine "other" (RO). Needs decomposition. |
| `biolink:has_participant` | 289,610 | PrimeKG | Overly generic. Could be refined to has_substrate, has_product, has_enzyme. |
| `biolink:correlated_with` | 6,660 | PrimeKG | Statistical correlation, not causal. Needs evidence typing. |
| `biolink:other` | 9,948 | PlaNet, OT | Unclassified. Needs individual triage. |

---

## 3. Schema Maturity Summary

### Entity Schemas

| Maturity | Count | Categories | Total Nodes |
|----------|------:|-----------|------------:|
| 🟢 Stable | 15 | Gene, Protein, Disease, Drug, ChemicalEntity, AnatomicalEntity, PhenotypicFeature, BiologicalProcess, SequenceVariant, Genotype, Cell, MolecularActivity, Pathway, CellularComponent, MolecularActivity | 8,073,099 |
| 🟡 Provisional | 13 | ClinicalFinding, ClinicalAttribute, Procedure, EnvironmentalFeature, OrganismTaxon, CellLine, ExperimentalFactor, Device, NucleicAcidEntity, Activity, PhenotypicQuality, LifeStage, EnvironmentalExposure | 3,670,476 |
| 🔴 Missing | 8 | PopulationOfIndividualOrganisms, Case, IndividualOrganism, QuantityValue, Attribute, GeographicLocation, Behavior, Agent | 48,192 |
| ⚠️ Reclassify | 2 | NamedThing, InformationContentEntity | 894,418 |

### Relationship Schema Coverage

| Category | Predicates | Evidence Typing | MI Alignment | Status |
|----------|-----------|----------------|-------------|--------|
| Gene-Disease | 7 predicates | Partial (OT has evidence types) | Not applicable | 🟡 Needs unified evidence model |
| PPI/Interactions | 2 predicates | ❌ None | ❌ Not aligned | 🔴 Critical gap (6.1M edges untyped) |
| Expression | 6 predicates | ❌ None | Not applicable | 🟡 Functional but no source/confidence |
| Drug mechanisms | 20+ predicates | Partial (OT has mechanism of action) | Not applicable | 🟢 Well-typed (OT is granular) |
| Variant | 3 predicates | Partial (ClinVar significance) | Not applicable | 🟡 Needs VRS 2.0 alignment |
| Phenotype | 3 predicates | ❌ None | Not applicable | 🟡 Needs evidence source |
| Trial observations | 11 predicates | ❌ None | Not applicable | 🟡 PlaNet-specific, needs provenance |
| Ambiguous | 3 predicates | ❌ None | ❌ None | 🔴 17.6M edges need decomposition |

---

## 4. Priority Actions

### P0: Critical (blocks downstream analysis)

1. **Decompose `related_to`** (17.6M edges): Split UMLS MRREL into proper predicates (subclass_of, synonym_of, broader_than, narrower_than, other_related)
2. **Subtype `interacts_with`** (6.1M edges): Apply MI ontology classification (Functional/Molecular/Predicted/Phenotypic) with evidence metadata
3. **Reclassify `NamedThing`** (297K nodes): Assign proper BioLink categories via MeSH/CUI entity type resolution

### P1: Important (improves schema quality)

4. **Add evidence typing** to all molecular edges: `evidence_class`, `detection_method`, `confidence_score`, `source_database`
5. **Reclassify `InformationContentEntity`** (598K nodes): Many are actually Disease, Procedure, or Finding
6. **Formalize clinical schemas**: Promote ClinicalFinding, ClinicalAttribute, Procedure from provisional → stable with SNOMED/OMOP alignment

### P2: Enhancement (nice to have)

7. **Create missing schemas** for Case (Phenopackets), Agent (ORCID/FOAF), QuantityValue (QUDT/UO)
8. **Align drug mechanism predicates** across OT and PlaNet (currently use different predicate names for same concept)
9. **Add CiTO-style citation typing** to scholarly edges
