# Cytos KG Schema Design

> Last updated: 2026-05-12 | Categories: **53 → 42 canonical** | Predicates: **702**

## 1. Three Constituent Graphs

The Cytos KG is composed of three constituent graphs, each with a distinct role:

| Constituent Graph | Content | Mnemonic |
|------------------|---------|----------|
| **Ontology Graph** | Definitions, hierarchies, identifiers, vocabularies, mappings | What things ARE |
| **Catalog Graph** | Papers, datasets, models, software, protocols, trials, organizations | What has been CREATED |
| **Observation Graph** | Measured associations, interactions, annotations, clinical findings | What has been OBSERVED |

Plus an orthogonal **Classification Layer** (UMLS Semantic Network, BioLink categories, MeSH tree numbers, AIO, CSO) that tags/clusters nodes across all three graphs.

## 2. Ontology Graph Entity Types

Entities that define what things ARE. The coordinate system of the KG.

### Tier 1: Stable (community-backed, validated by 2+ sources)

| Entity Type | Count | Key Ontologies | Schema |
|-------------|------:|---------------|--------|
| `biolink:Disease` | 1,093,827 | MONDO, DOID, OMIM | `disease.yaml` |
| `biolink:Protein` | 894,830 | UniProt, PR | `gene.yaml` |
| `biolink:Gene` | 846,437 | HGNC, Ensembl, NCBI Gene | `gene.yaml` |
| `biolink:ChemicalEntity` | 630,302 | CHEBI, PubChem | `drug.yaml` |
| `biolink:Drug` | 592,753 | DrugBank, ChEMBL | `drug.yaml` |
| `biolink:AnatomicalEntity` | 485,242 | UBERON, HRA (CCF) | `anatomy.yaml` |
| `biolink:PhenotypicFeature` | 427,704 | HP, MP, PATO | `disease.yaml` |
| `biolink:BiologicalProcess` | 292,043 | GO (BP) | `pathway.yaml` |
| `biolink:SequenceVariant` | 218,546 | VRS 2.0, dbSNP, ClinVar | `variant.yaml` |
| `biolink:OrganismTaxon` | 184,325 | NCBITaxon | `taxonomy.yaml` |
| `biolink:CellLine` | 167,186 | CLO, Cellosaurus, DepMap | `cellline.yaml` |
| `biolink:Genotype` | 139,197 | VRS 2.0 | `variant.yaml` |
| `biolink:Cell` | 99,472 | CL | `anatomy.yaml` |
| `biolink:Device` | 74,912 | SNOMED devices, GMDN | `device.yaml` |
| `biolink:MolecularActivity` | 51,924 | GO (MF) | `pathway.yaml` |
| `biolink:Pathway` | 27,889 | Reactome, KEGG, WikiPathways | `pathway.yaml` |
| `biolink:CellularComponent` | 18,497 | GO (CC) | `pathway.yaml` |
| `biolink:GeographicLocation` | 5,046 | GAZ, ISO 3166, GeoNames | `geography.yaml` |
| `biolink:MeasurementUnit` | 5,981 | UO, QUDT | `measurement.yaml` |
| `biolink:LifeStage` | 2,354 | HsapDv, MmusDv | `anatomy.yaml` |

### Tier 2: Provisional (functional, needs refinement)

| Entity Type | Count | Key Ontologies | Schema | Action |
|-------------|------:|---------------|--------|--------|
| `biolink:ClinicalAttribute` | 732,925 | SNOMED, LOINC | `clinical.yaml` | Align to OMOP Measurement |
| `biolink:Procedure` | 707,855 | SNOMED, CPT, MAXO | `clinical.yaml` | Align to OMOP Procedure |
| `biolink:EnvironmentalFeature` | 363,661 | ENVO, ECTO | `environment.yaml` | Merge with Exposure hierarchy |
| `biolink:ExperimentalFactor` | 96,973 | EFO | `environment.yaml` | — |
| `cytos:ExposureEntity` | 22K | ECTO, ExO, ENVO, SDOH | `exposure.yaml` | New: parent of 9 exposure subtypes |
| `biolink:NucleicAcidEntity` | 16,792 | SO | `information.yaml` | — |
| `cytos:NeurobehavioralPhenotype` | ~3K | NBO, DSM-5 criteria | `behavior.yaml` | New: split from Behavior |
| `cytos:PopulationGroup` | 12,109 | OMB, GAZ | `population.yaml` | Renamed from PopulationOfIndividualOrganisms |
| `cytos:OccupationalRole` | 7,829 | SNOMED, ISCO-08 | `agent.yaml` | Renamed from IndividualOrganism |
| `cytos:PhenotypicAttribute` | 5,647 | FBcv | → merge into `disease.yaml` | Merge into PhenotypicFeature |

### HRA Spatial Entities (Ontology Graph)

HRA provides the spatial scaffold for the entire KG. All measurement data maps onto this coordinate system.

| Entity | Count | Schema | Spatial Data |
|--------|------:|--------|-------------|
| `ccf:AnatomicalStructure` | 4,496 | `hra.yaml` | UBERON + HRA ASCT+B |
| `ccf:CellType` | 1,195 | `hra.yaml` | CL + ccf_located_in edges |
| `ccf:Biomarker` | 2,084 | `hra.yaml` | HGNC genes + UniProt proteins |
| `ccf:SpatialEntity` | 1,713 | `hra.yaml` | 3D reference organ meshes |
| `ccf:SpatialPlacement` | 3,481 | `hra.yaml` | x/y/z translation + rotation + scaling |

HRA integration points:

```
Sensor → measures_at → HRA/UBERON location (via ccf_located_in)
CellType → ccf_located_in → AnatomicalStructure
AnatomicalStructure → ccf_part_of → AnatomicalStructure (hierarchy)
Biomarker → ccf_characterizes → CellType (ASCT+B)
SpatialPlacement → ccf_placement_for → SpatialEntity (3D coordinates)
```

### Device Hierarchy (Ontology Graph)

```
cytos:Device (parent)
├── cytos:MedicalDevice      # Therapeutic/assistive (prosthetics, implants)
├── cytos:DiagnosticDevice   # In-clinic measurement (MRI, lab analyzers)
└── cytos:Sensor             # Continuous/portable (Cytoscope backbone)
    ├── MolecularSensor      # Sequencers, mass spec
    ├── CellularSensor       # Flow cytometers, 10x Chromium
    ├── NeuroimagingSensor    # EEG caps, MEG, fNIRS
    └── PhysiologicalSensor  # CGM, PPG, accelerometer
```

### Sensor Triple (Ontology Graph)

Every measurement is described by three dimensions:

| Dimension | Question | Ontology | Example |
|-----------|----------|----------|---------|
| Assay (WHAT) | What is measured? | OBI, NCIT, EFO | `OBI:0002631` (RNA-seq) |
| Location (WHERE) | Where on/in body? | HRA, UBERON, CCF | `UBERON:0000955` (brain) |
| Schema (HOW) | How is data structured? | CellxGene, VRS, NWB | CellxGene v5.2 schema |

Schemas attach to assay ontology nodes and inherit downward:

| Assay | Schema | Specializations |
|-------|--------|----------------|
| `OBI:0002631` RNA-seq | CellxGene | scRNA-seq adds cell_type; spatial adds coords |
| `OBI:0000626` DNA-seq | VRS 2.0 | WGS adds coverage; WES adds capture_kit |
| `NCIT:C17958` fMRI | NWB/BIDS | rs-fMRI adds TR; task-fMRI adds events |
| `NCIT:C45259` EMR | OMOP CDM | — |
| `NCIT:C185651` CGM | `cytos:WearableTimeSeries` | — |

## 3. Catalog Graph Entity Types

Entities that represent human-created artifacts.

| Entity Type | Count | Schema | Key Standards |
|-------------|------:|--------|--------------|
| `biolink:Publication` | 1,000,000 | `publication.yaml` | DataCite, CiTO, OpenAlex |
| `biolink:ClinicalTrial` (metadata) | 480,795 | `publication.yaml` | ClinicalTrials.gov, WHO ICTRP |
| `cytos:Dataset` | — (future) | `dataset.yaml` | DCAT, Croissant, RO-Crate |
| `cytos:MLModel` | — (future) | `model.yaml` | HuggingFace model cards |
| `biolink:SoftwareOrTool` | 1,120 | `software.yaml` | CodeMeta, CITATION.cff |
| `cytos:Workflow` | — (future) | `workflow.yaml` | CWL, Nextflow, Bioschemas |
| `cytos:Protocol` | — (future) | `protocol.yaml` | protocols.io |
| `cytos:Organization` | 3,480 | `agent.yaml` | ROR, Schema.org |
| `cytos:BehavioralAssessment` | — (subset) | `behavior.yaml` | NCIT instruments, PHQ-9, GAD-7 |

### FAIR Fields on Dataset Nodes

Dataset nodes are catalog entries (metadata), NOT actual data. FAIR fields link to data lake:

| FAIR | Fields | Ontology |
|------|--------|----------|
| **F**indable | identifier, repository, landing_page | DataCite, DCAT |
| **A**ccessible | access_url, protocol, auth, restrictions | DCAT, `cytos:` |
| **I**nteroperable | data_format (EDAM), conforms_to_schema, vocabulary_encodings | EDAM, DCAT |
| **R**eusable | license, provenance, quality_metrics, checksum | PROV, BAO |

## 4. Observation Graph Entity Types

Entities that capture measured/observed findings. Note: the Observation Graph is primarily EDGES between Ontology Graph nodes, with few exclusive node types.

| Entity Type | Count | Schema | Key Standards |
|-------------|------:|--------|--------------|
| `biolink:ClinicalFinding` | 1,393,204 | `clinical.yaml` | SNOMED findings → OMOP Condition |
| `cytos:ClinicalCase` | 8,207 | `clinical.yaml` | GA4GH Phenopackets v2 |

## 5. Edge Types (Interaction Taxonomy)

### Intra-Graph Edges

| Graph | Edge Types | Key Predicates |
|-------|-----------|---------------|
| **Ontology** | Ontology structure + SSSOM mappings | subclass_of, part_of, exactMatch, closeMatch |
| **Catalog** | Citations (CiTO subtypes), co-authorship, artifact provenance | cites, trained_on, develops_software |
| **Observation** | Molecular interactions (MI ontology: functional, experimental, predicted, genetic), gene-disease, drug mechanisms, expression, clinical trial observations | interacts_with, expressed_in, gene_associated_with_condition, treats, eligibility_inclusion |

### Inter-Graph Edges

| From → To | Predicate Pattern | Example |
|-----------|------------------|---------|
| Observation → Ontology | Annotation edges | Gene → enables → GO:0006281 |
| Catalog → Ontology | NER/entity linking | Paper → mentions_entity → HGNC:11998 |
| Catalog → Observation | Evidence provenance | Paper → provides_evidence_for → (TP53, cancer) |

## 6. Classification Layer (orthogonal)

| Network | Terms | Coverage | Edge Predicate |
|---------|------:|----------|---------------|
| UMLS Semantic Network | 127 types | ~80% biomedical | `cytos:has_semantic_type` |
| BioLink categories | 53 types | 100% | `rdf:type` (implicit) |
| MeSH Tree Numbers | ~29K | ~60% disease/drug/anatomy | `cytos:has_mesh_heading` |
| AIO | 442 | LOW (AI/ML only) | `cytos:has_topic` |
| CSO | 14,736 | LOW (CS only) | `cytos:has_topic` |

## 7. Reclassification Queue

| Current Category | Count | Resolution |
|-----------------|------:|-----------|
| `biolink:NamedThing` | 296,570 | PlaNet (185K) → Disease/Drug/Condition via MeSH/CUI; Core/Monarch (112K) → individual triage |
| `biolink:InformationContentEntity` | 597,848 | Many are Disease, Procedure, or ClinicalFinding; reclassify via UMLS semantic type |

## 8. Schema Evolution Strategy

1. **Stable**: community-backed, 2+ source validation. Breaking changes require LinkML version bump.
2. **Provisional**: functional, single source. Promoted to stable after 3+ source validation.
3. **Missing**: create schema, assign ontology source, validate against existing data.
4. All schemas reference the Ontology Graph for controlled vocabularies (enums validated against OWL).
