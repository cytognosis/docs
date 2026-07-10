# Unified Schema Architecture for Cytognosis: Body, Sensors, Data, Models

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Version:** 2026-05-07 (consolidated)
**Supersedes:** the per-entity files in this folder, which are retained as deeper references.
**Audience:** Cytognosis Foundation platform/architecture and grant-writing teams.

## The unified frame

Cytognosis collects **data** from the **human body** using **sensors**, and uses dedicated **models** to analyze and embed them. Those four entities are not parallel. They are linked in one directed chain, and the chain corresponds exactly to the SOSA observation grammar:

```
HUMAN BODY  ← FeatureOfInterest of →  OBSERVATION  ← made by →  SENSOR
                                            │
                                       hasResult
                                            ↓
                                          DATA  ← consumed by →  MODEL
                                                                    │
                                                              also a Procedure
                                                                    │
                                                            produces another
                                                              OBSERVATION
                                                            (e.g. embedding)
```

Reading the chain right-to-left gives the operational view: a Cytognosis pipeline registers a sensor in the platform (a `sosa:Sensor` linked to an OBI/BAO/EFO assay class), describes the procedure it uses (a `sosa:Procedure` with EDAM Operation tags and ISA Study/Assay context), points at the human body region it observes (a `sosa:FeatureOfInterest` annotated with HRA/CCF coordinates and UBERON/CL terms), runs it to produce data (a `sosa:Result` stored as AnnData/Zarr/Parquet/FHIR), and then feeds that data to one or more models (each a `sosa:Procedure` of its own that produces further `sosa:Observation`s such as embeddings, predictions, or sampled distributions). Provenance across the whole chain is packaged as a Workflow Run RO-Crate.

This document is the master architectural reference for that chain. It is organized in three parts:

- **Part I (Foundations)** establishes the four anchors: SOSA/SSN as the upper grammar, HRA as the spatial scaffold for the body, ISA as the experimental hierarchy, and the OBO/EDAM/UCUM/HED bio-noun layer.
- **Part II (Entities)** walks through Body, Sensor, Data, Model with the same scaffold applied uniformly.
- **Part III (Composition)** covers RO-Crate / Croissant / LinkML / FHIR projections, the recommended stack, the matching function, gaps, and the next-step sequence.

Deeper references live in the companion files: [models.md](models.md), [sensors.md](sensors.md), [data.md](data.md), [interop.md](interop.md), [human-body.md](human-body.md).

---

# Part I: Foundations

## 1. SOSA / SSN: the modality-independent grammar

A 10x scRNA-seq run, an EEG session, a CGM stream, an MRI scan, an scVI inference, and a CRISPR knockdown all share the same six relations: a sensor (or actuator) acts on a feature of interest via a procedure, observing (or actuating) some property and producing a result, at a point in time. SOSA names those six relations precisely. SSN extends them with system, deployment, and platform abstractions; SSN-Ext adds collections for time series; SOSA-OMS aligns to ISO 19156:2023.

Core classes (full table in [sensors.md, section 0](sensors.md)):

| Class | What | Cytognosis example |
|---|---|---|
| `sosa:FeatureOfInterest` | The thing measurements are about | A patient (donor), a tissue, a single cell, an organoid, a cohort |
| `sosa:Sample` | A representative subset of an FOI | A biopsy block, a blood tube, a 50 µL aliquot |
| `sosa:Sensor` | The agent doing the observing | A NovaSeq, a Dexcom G7, an scVI service |
| `sosa:Actuator` | The agent doing the changing (closed-loop, perturbation) | An insulin pump, a CRISPR delivery system |
| `sosa:Observation` | One observational act | One sequenced library, one 5-minute glucose window |
| `sosa:Actuation` | One actuation act | One insulin bolus, one CRISPR knockdown |
| `sosa:ObservableProperty` | What is being observed | "gene expression", "interstitial glucose", "BOLD signal" |
| `sosa:Procedure` | The protocol or algorithm | "10x 3' v3 with Ensembl 111", "scVI training recipe" |
| `sosa:Result` | The output | A count matrix, a value, an embedding |
| `sosa:Platform` / `ssn:System` | Hosts/composites | A patient's wrist; a sequencing facility |

Why SOSA matters most: validation (SOSA-SHACL gives modality-independent shape checks for free), match logic (the platform's match function works at the SOSA level then drops into bio-specific checks), projections (SOSA → FHIR Observation, → SensorThings, → SensorML are all worked out in literature). Sources: [SOSA / SSN W3C Rec](https://www.w3.org/TR/vocab-ssn/), [SSN 2023 Edition](https://www.w3.org/TR/vocab-ssn-2023/), [SOSA arXiv 1805.09979](https://arxiv.org/abs/1805.09979), [SOSA-SHACL IJCKG 2021](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235).

## 2. HRA / HuBMAP: the spatial scaffold for the body

SOSA tells you that a measurement has a `FeatureOfInterest`. The HRA tells you *what specific structure in the body* that FeatureOfInterest is, with coordinates, anatomical labels, and cell-type and biomarker context, all linked to canonical ontologies. This is the missing scaffold the previous documents lacked.

What HRA gives you (full detail in [human-body.md](human-body.md)):

- **ASCT+B tables** (Anatomical Structures + Cell Types + Biomarkers) for 71 organs, 5,800 anatomical structures, 2,268 cell types, 2,531 biomarkers as of HRA KG v2.2 (May 2025). Linked to UBERON, FMA, CL, HGNC.
- **CCF Ontology** for specimens, biological structures, and spatial positions. Latitude-longitude analog for the body.
- **3D Reference Organs**: meshes for >50 organs; the registration substrate for tissue blocks.
- **RUI** (Registration User Interface): tool for placing a tissue block in 3D against a reference organ, with auto-assignment of anatomical-structure annotations via mesh collision.
- **Vasculature CCF (VCCF)**: distance-to-vessel as an additional coordinate axis, captured in the [HRA-VCCF repo](https://github.com/hubmapconsortium/hra-vccf).
- **OMAPs** (Organ Mapping Antibody Panels): community-curated, validated antibody panels for multiplex spatial proteomics, tied to specific organs and ASCT+B-listed structures and cell types.
- **HuBMAP Data Portal**: 5,032 datasets across 22 data types, 27 organ classes, 310 donors (Oct 2025), with provenance graphs from donor → sample → assay → dataset.

Why HRA matters: it is the **only existing system that gives you spatial coordinates plus part-of nesting plus cell-type-to-biomarker linking** at the resolution and curation depth required to register sensor outputs across scales. Every Cytognosis sensor reading whose FeatureOfInterest is a human body region can carry CCF coordinates plus UBERON/FMA intersection lists plus VCCF distances, all dereferenceable. HRA is what makes "match across scales" a tractable spatial join. Sources: [HuBMAP HRA Nature Methods 2024](https://www.nature.com/articles/s41592-024-02563-5), [HRA KG Sci Data 2025](https://www.nature.com/articles/s41597-025-05183-6), [HRA portal humanatlas.io](https://humanatlas.io/), [CCF Ontology](https://humanatlas.io/ccf-ontology).

## 3. ISA: the experimental hierarchy

Where SOSA gives the per-observation grammar, the [ISA Abstract Model](https://isa-specs.readthedocs.io/en/latest/isamodel.html) gives the surrounding *experimental design* hierarchy: who set up the study, what samples were collected under what protocol, which assays were applied to which samples, and how they all relate. ISA fills the gap between "an investigation existed" and "an observation happened".

Core ISA structure:

```
Investigation
└── Study (1..N)
    ├── Source (initial biological material)
    ├── Sample (derived from Source via Process)
    ├── Process nodes (apply a Protocol to inputs producing outputs)
    └── Assay (1..N per Study)
        └── more Process nodes producing measurement output
```

Key components:

- **Investigation**: the project context. Title, description, people, scholarly publications, ontology sources used.
- **Study**: subject(s) under study, characteristics, treatments, and the entire material/process DAG that leads to assay outputs.
- **Assay**: a specific test producing measurements. Each Assay has its own measurement type (e.g., "transcription profiling"), technology type (e.g., "RNA sequencing"), and platform (e.g., "Illumina NovaSeq 6000").
- **Source / Sample / Material**: nodes in the experimental DAG. Source = starting biological material; Sample = derived by a Process; Material = consumable.
- **Process**: an application of a Protocol with parameter values to inputs, producing outputs. The DAG edge.
- **Protocol**: the documented procedure. Has parameters and components.
- **Factor / FactorValue**: experimental variables (independent factors that vary across the study, with values per Sample).
- **OntologySource**: declares the ontologies referenced (URI, version, description).
- **OntologyAnnotation**: a typed annotation referencing a term in an OntologySource.

ISA-Tab serializes this as a tab-delimited multi-file format (`i_*.txt` for Investigation, `s_*.txt` for Study, `a_*.txt` for Assay). ISA-JSON is the machine-readable JSON serialization. The [ISA API](https://pmc.ncbi.nlm.nih.gov/articles/PMC8444265/) is the Python toolchain.

How ISA composes with SOSA: an ISA `Process` is a `sosa:Procedure` instance; an ISA `Sample` is a `sosa:Sample`; an ISA `Assay` produces one or more `sosa:Observation`s; an ISA `Study` corresponds to a `ssn:Deployment` of one or more sensors over a defined time period. The mapping is mechanical, and treating SOSA as the upper grammar with ISA as the surrounding study container is exactly the integration pattern the Cytognosis platform should adopt. Sources: [ISA Abstract Model](https://isa-specs.readthedocs.io/en/latest/isamodel.html), [ISA-Tab](https://isa-specs.readthedocs.io/en/latest/isatab.html), [ISA-JSON](https://isa-specs.readthedocs.io/en/latest/isajson.html), [ISA API paper, PMC 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8444265/).

## 4. The bio-noun layer: BAO, OBI, EFO, EDAM, plus the OBO core

SOSA gives the verbs; the body atlas gives the spatial scaffold; ISA gives the study hierarchy. The OBO/EDAM bio-noun layer is what fills the slots with terms.

### OBI: Ontology for Biomedical Investigations

OBI organizes terms into four top-level domains. This decomposition is the right mental model for any Cytognosis assay registration:

| OBI domain | Examples | SOSA slot it most often fills |
|---|---|---|
| **Material entities** | Organism, specimen, device, processed material, reagent | FeatureOfInterest, Sample, Sensor (when Sensor is a device) |
| **Observable qualities** | Concentration, intensity, expression level, cell count | ObservableProperty, Result.value_type |
| **Planned processes** | Assay, study design execution, specimen collection, data acquisition, data analysis | Procedure, Actuation |
| **Information artifacts** | Dataset, model, document, plan specification, conclusion | Result (when the result is data), `cytognosis:ModelManifest` reference |

OBI defines >2,500 terms covering all phases of an investigation: planning, execution, reporting. Crucial subclasses:

- `OBI:0000070` assay
- `OBI:0000272` protocol
- `OBI:0000094` material processing
- `OBI:0000245` planned process
- `OBI:0100051` specimen
- `OBI:0000968` device
- `OBI:0000893` data set
- `OBI:0001271` RNA-seq via Illumina (example concrete assay)

Source: [OBI ontology](https://obi-ontology.org/), [OBI PLOS One 2016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154556).

### BAO: BioAssay Ontology

BAO 2.0 organizes the assay description problem along **six components**, each its own subsumption tree. This is the most disciplined assay decomposition in any standard, and it generalizes beyond high-throughput screening into perturbation biology, pharmacology, and any "we did X to a system and read out Y" experiment.

| BAO component | What it answers | Cytognosis use |
|---|---|---|
| **Bioassay** | The integrative top-level class that ties the others together | The umbrella for one Cytognosis assay registration |
| **Assay biology** | What biological process or target the assay reports on (proximal vs. meta target) | Useful when an assay reports on a downstream proxy of the real target |
| **Assay method** | How the assay is performed (including computational method, instrument, reagents) | Maps to `sosa:Procedure` |
| **Assay format** | The biological/chemical experimental system (cell-based, biochemical, organism-based, in vivo) | A natural place to declare in vitro vs. in vivo vs. in silico |
| **Assay endpoint** | The result quantity, with units (imported from UO, the Units Ontology) | Maps to `sosa:Result` value type and unit |
| **Assay screened entity** | The perturbagen (small molecule, siRNA, CRISPR guide, antibody, environmental factor) | Critical for perturbation experiments |

Crucial subclasses: `BAO:0002854` perturbagen, `BAO:0000179` assay format, `BAO:0000074` assay method, `BAO:0000179` assay format, `BAO:0000540` detection method, `BAO:0000026` assay endpoint. The 2025 PK/PD extension paper [J Biomed Semantics 2025](https://link.springer.com/article/10.1186/s13326-025-00342-5) brought BAO into translational pharmacology in addition to drug-discovery HTS.

Source: [BAO Evolving paper, J Biomed Semantics 2014](https://jbiomedsem.biomedcentral.com/articles/10.1186/2041-1480-5-S1-S5), [BAO PK/PD extension 2025](https://link.springer.com/article/10.1186/s13326-025-00342-5).

### EFO: Experimental Factor Ontology

EFO is the **application ontology** that consolidates UBERON (anatomy), ChEBI (chemicals), CL (cell types), MONDO (diseases), and others into one practical vocabulary, used by the EBI BioSamples database, Expression Atlas, ArrayExpress, the GWAS Catalog, and Open Targets. EFO's main branches are:

| EFO branch | Coverage | Example terms |
|---|---|---|
| **Diseases, traits, phenotypes** | Disease classification (aligned with MONDO since EFO3) | `EFO:0000400` (diabetes mellitus), `EFO:0000305` (breast carcinoma) |
| **Anatomy, development, cells** | UBERON + CL coverage | `EFO:0000940` (lymph node), `CL:0000236` (B cell) |
| **Assays, measurements, compounds** | Assay class + measurement endpoints + compounds | `EFO:0009922` (10x 3' v3), `EFO:0008914` (Smart-seq2), `EFO:0007936` (single-cell RNA sequencing) |

For Cytognosis, EFO is the **right primary ontology for `assay_class`** because (a) the single-cell-curation 7.x schema requires EFO `assay_ontology_term_id`, (b) most omics assays already have EFO terms, (c) it auto-imports the bio-anatomy and cell-type concepts you also need. Use EFO first, fall back to OBI when EFO has no matching term, fall back to BAO when the 5-axis decomposition matters.

Source: [EFO at EBI](https://www.ebi.ac.uk/efo/), [EFO repo](https://github.com/EBISPOT/efo), [EFO Wikipedia](https://en.wikipedia.org/wiki/Experimental_factor_ontology).

### EDAM: Ontology of bioinformatics operations, data, formats, topics

EDAM is structured in **four parallel hierarchies**: Topic, Operation, Data (incl. Identifier), Format. It is the only ontology in the survey that names *computational* concepts at the right granularity for the Models layer.

| EDAM section | What | Examples |
|---|---|---|
| **Topic** | Application domain or subject area | `topic:3308` Transcriptomics, `topic:3170` (RNA-Seq), `topic:3474` Machine learning, `topic:3577` Personalised medicine, `topic:3489` Database management, `topic:3382` Imaging |
| **Operation** | Function with typed inputs and outputs (the *what does this do*) | `operation:3937` Feature extraction, `operation:3935` Dimensionality reduction, `operation:3659` Regression, `operation:2426` Modelling and simulation, `operation:2238` Statistical calculation, `operation:0226` Annotation |
| **Data** | Data types and Identifiers | `data:0918` Gene expression matrix, `data:2295` Gene ID, `data:2810` Ensembl gene ID, `data:1027` Gene ID (NCBI), `data:1772` Score, `data:2884` Plot |
| **Format** | Data formats and standards | `format:3590` h5ad, `format:3727` Zarr, `format:1929` FASTQ, `format:2330` Textual format, `format:3464` JSON, `format:3550` MTX |

For Cytognosis, EDAM is the right ontology for tagging `sosa:Procedure` at the high-level effect (Operation), the dataset's nature (Topic + Data + Format), and a model's effect on data (Operation, e.g., a VAE encoder is `operation:3935` Dimensionality reduction). EDAM does not natively distinguish architectural patterns (encoder vs. decoder vs. diffusion); a Cytognosis-internal LinkML enumeration covers that gap.

Source: [EDAM site](https://edamontology.org), [EDAM repo](https://github.com/edamontology/edamontology), [EDAM on BioPortal](https://bioportal.bioontology.org/ontologies/EDAM).

### The OBO core that fills FeatureOfInterest, Sample, ObservableProperty

| Ontology | Role | SOSA slot it fills |
|---|---|---|
| **NCBITaxon** | Species | FeatureOfInterest, Sample |
| **CL** Cell Ontology | Cell types | FeatureOfInterest, Sample |
| **UBERON** | Tissues, organs, anatomy | FeatureOfInterest, Sample (combined with HRA CCF coords) |
| **FMA** Foundational Model of Anatomy | Detailed anatomy (cross-walks with UBERON) | Spatial registration |
| **MONDO** | Disease | FeatureOfInterest |
| **HP** Human Phenotype Ontology | Phenotypes | FeatureOfInterest, ObservableProperty |
| **GO** Gene Ontology | Biological processes, molecular functions, cellular components | ObservableProperty |
| **ChEBI** | Chemical entities | ObservableProperty, ActuatableProperty (drugs/perturbagens) |
| **SO** Sequence Ontology | Sequence features and variants | ObservableProperty |
| **HGNC, NCBIGene, Ensembl** | Gene identifiers | ObservableProperty (the gene axis) |
| **UniProt** | Proteins | ObservableProperty (proteomics axis) |
| **PATO** | Phenotypic and qualitative attributes (sex, color, shape) | FeatureOfInterest |
| **DUO** Data Use Ontology | Consent, restrictions | governance metadata |
| **HED** Hierarchical Event Descriptors | Event descriptors in time-series | Context.events around an Observation |
| **UO** Units Ontology / **UCUM** | Units of measurement | Result.unit |
| **LOINC** | Clinical observation codes | ObservableProperty (clinical) |
| **SNOMED CT** | Clinical findings, procedures, conditions | clinical-only context |
| **HRA / CCF** | Spatial coordinates of structures and cells | FeatureOfInterest, Sample (with `ccf:rui_location`) |
| **ASCT+B** | Anatomical structure / cell type / biomarker mappings per organ | constraint on FeatureOfInterest cell-type assignment |

[Bioregistry](https://bioregistry.io/) is the prefix resolver and validator across all of them.

The mental model: **SOSA is the grammar; HRA is the map; ISA is the experimental container; OBO + EDAM is the vocabulary**.

---

# Part II: The four entities

## 5. The Human Body (the FeatureOfInterest)

### What you need to declare

For any Cytognosis observation, the FOI annotation should answer:

1. **Species** (NCBITaxon)
2. **Donor identity** (opaque ID, with consent codes via DUO)
3. **Demographic context** (age range, sex via PATO, development stage, self-reported ethnicity)
4. **Disease/phenotype state** (MONDO, HP)
5. **Anatomical location** (UBERON + FMA cross-walks)
6. **Spatial registration in HRA-CCF** (where applicable: RUI block placement, intersected anatomical structures, VCCF distances)
7. **Cell-type context** (CL, constrained by the relevant ASCT+B table for the organ)
8. **Sub-cellular context** (when relevant: GO-CC, PATO)
9. **Sample provenance chain** (Source → Sample, ISA-style, with collection time, preservation, processing steps)

### Canonical record

A Cytognosis `SubjectManifest` (LinkML class subclassing `sosa:FeatureOfInterest` and `fhir:Patient`):

```yaml
id: cytognosis.subj:donor_038
type: [sosa:FeatureOfInterest, fhir:Patient, ccf:Donor]
species: NCBITaxon:9606
sex: PATO:0000383
development_stage: HsapDv:0000087
self_reported_ethnicity: HANCESTRO:0005
disease_state: [MONDO:0007254]                # zero or more
phenotypic_features: [HP:0001250]              # zero or more
consent: { duo_codes: [DUO:0000004] }
ccf_donor_id: 4f6a-...uuid                    # HuBMAP-style if applicable
provenance: { study: cytognosis.study:0042 }
```

A Cytognosis `SampleManifest` (subclasses `sosa:Sample` and `fhir:Specimen` and `ccf:TissueBlock` where applicable):

```yaml
id: cytognosis.samp:0001
type: [sosa:Sample, fhir:Specimen, ccf:TissueBlock]
is_sample_of: cytognosis.subj:donor_038
collected_at: 2026-04-03T14:22:00Z
collection_procedure: OBI:0000659              # specimen collection
preservation_method: snap_frozen
tissue: UBERON:0008952                         # lower lobe of left lung
ccf_rui_location:
  organ_iri: http://purl.obolibrary.org/obo/UBERON_0008952
  dimension_x_mm: 8.4
  dimension_y_mm: 6.1
  dimension_z_mm: 0.8
  placement_translation: [3.21, -2.05, 1.03]
  placement_rotation_quaternion: [...]
ccf_intersects:
  - UBERON:0002048   # lung
  - UBERON:0008952   # lower lobe
  - UBERON:0002187   # bronchiole
ccf_vccf_nearest_vessel: ...
```

This is the spatial-anatomical scaffold the rest of the chain hangs off. Detail in [human-body.md](human-body.md).

## 6. Sensor / Assay (the observing agent)

### What you need to declare

For any Cytognosis sensor/assay registration, the manifest should answer:

1. **Assay class** (EFO primary, OBI fallback, BAO 5-axis decomposition for perturbation work)
2. **Sensor instance and host platform** (the specific instrument + where it lives)
3. **Procedure** (the protocol, with EDAM Operation tags; can be a wet-lab protocol via OBI/EFO or a computational pipeline)
4. **ObservableProperty** (gene expression via GO, glucose via ChEBI/LOINC, BOLD signal, etc.)
5. **Sampling regime** (snapshot, periodic, bounded continuous, ongoing continuous)
6. **Result schema** (value type, unit via UCUM/UO, range, transformation, missing-value encoding)
7. **Context** (ISA Investigation/Study/Assay refs, HED tags for events, perturbations from ChEBI/genes/BAO)
8. **Modality-specific profile binding** (which Layer 2 profile applies: single-cell-curation 7.x, BIDS+HED, OME-NGFF, FHIR Observation, OMOP, Open mHealth, SensorThings)

### The four sampling regimes and where each profile lives

| Regime | Examples | Primary profile | SOSA shape |
|---|---|---|---|
| Snapshot | scRNA-seq biopsy, MRI scan, single blood draw | AnnData/MuData/SpatialData (omics), DICOM (clinical imaging), FHIR Observation (single labs) | `sosa:Observation` |
| Periodic | Annual labs, quarterly imaging | OMOP MEASUREMENT rows, FHIR ResearchStudy + Observation series | `sosa:ObservationCollection` (SSN-Ext) |
| Bounded continuous | EEG session, fMRI run, gait analysis | BIDS 1.11+ with modality extension, NWB, OME-NGFF (microscopy time series) | `sosa:ObservationCollection` |
| Ongoing continuous | CGM, wearables, ICU telemetry | Open mHealth + FHIR Observation, OGC SensorThings, DICOM Sup 30 (clinical waveforms) | `sosa:ObservationCollection` (rolling windows) |

Each profile maps deterministically into a SOSA-aligned `ObservationManifest` at Layer 3. Detail in [sensors.md](sensors.md).

### Canonical record

A Cytognosis `SensorManifest`:

```yaml
id: cytognosis.sensor:novaseq-x-#42
type: sosa:Sensor
device_class: EFO:0009922                      # or OBI/BAO when EFO does not have a term
instance_label: "NovaSeq X #42, Lab Genomics Core"
hosts_in_platform: cytognosis.platform:lab-genomics-core
observes:                                       # ObservableProperty class this sensor type can measure
  - GO:0010467                                  # gene expression
```

A Cytognosis `ProcedureManifest`:

```yaml
id: cytognosis.proc:proc_10x_3prime_v3_human_v1
type: [sosa:Procedure, OBI:0000272]            # OBI protocol
conforms_to: EFO:0009922                        # 10x 3' v3
edam_operation: [operation:3937, operation:0226]   # feature extraction, annotation
edam_topic: [topic:3170, topic:3308]            # RNA-Seq, Transcriptomics
bao_axes:
  perturbagen: null                             # snapshot, no perturbation
  format: BAO:0000179.cell_based
  detection_method: BAO:0000540.next_gen_sequencing
  endpoint: BAO:0000026.transcript_count
reference_genome: ensembl:111
feature_manifest_uri: cytognosis.feature_manifest:human-ensembl-111-canonical
feature_manifest_sha256: 0xdeadbeef...
isa_protocol_ref: cytognosis.isa_protocol:0010
documentation: ro-crate:.../protocol.md
```

## 7. Data (the artifact and its dimensions)

### What you need to declare

For any Cytognosis dataset registration, the manifest should answer:

1. **Storage** (URIs, replicas, format, size, chunking)
2. **In-memory format** (AnnData, MuData, SpatialData, FHIR Bundle, etc.)
3. **Domain typing** (EDAM Data + EDAM Format + `dct:conformsTo` to a domain profile)
4. **Per-axis annotation schemas** (the `obs` schema, the `var` schema, etc.; LinkML class refs)
5. **Feature-axis pinning** (identifier scheme + annotation version + canonical-order SHA256)
6. **Value semantics** (per-layer, with type, unit, range, transformation)
7. **Source observations** (links to one or more `ObservationManifest` records)
8. **Provenance** (PROV-O metadata; RO-Crate ref; generating workflow)
9. **Access** (license, DUO codes, controlled-access flag)
10. **Catalog refs** (DCAT entry, DataCite DOI when applicable)

### Storage tier choices

| Use case | Recommendation |
|---|---|
| Bulk omics, in development | AnnData h5ad on local disk |
| Bulk omics, shared at scale | AnnData-Zarr or TileDB-SOMA on S3/GCS |
| Imaging | OME-Zarr (NGFF 1.0 stable in 2025) on S3/GCS |
| Spatial omics | SpatialData on S3/GCS (Zarr + Parquet, OME-NGFF aligned) |
| Tabular/sensor time series | Parquet partitioned, queried via DuckDB/Arrow/Polars |
| Clinical | FHIR server (HAPI, Smile, Firely) or OMOP CDM in Postgres/BigQuery/Snowflake |

Detail in [data.md](data.md).

### Canonical record

```yaml
id: cytognosis.dataset:0001
type: [sosa:Result, schema:Dataset, dcat:Dataset]
classification:
  edam_data: data:0918                         # gene expression matrix
  edam_format: format:3590                     # h5ad
  edam_topic: topic:3170
  conforms_to: cellxgene-schema:7.1.0
storage:
  primary_uri: s3://cytognosis-data/.../obs1.zarr
  size_bytes: 142589321024
  chunks: { obs: 16384, var: 4096 }
in_memory:
  format: AnnData
  axes:
    obs:
      n: 1289341
      annotation_class: cytognosis:CellAnnotation
    var:
      n: 38244
      annotation_class: cytognosis:GeneAnnotation
      identifier_scheme: ensembl.gene
      annotation_version: ensembl:111
      canonical_order_sha256: 0xdeadbeef...
value_semantics:
  X: { value_type: int, unit: "1", transformation: identity }
  layers.normalized: { value_type: float, unit: "1", transformation: log1p_cp10k }
source_observations: [cytognosis.obs:0001, cytognosis.obs:0002, ...]
provenance:
  prov_o: ...
  ro_crate: s3://cytognosis-data/.../ro-crate-metadata.json
  generated_by_workflow: nf-core/scrnaseq:2.6.0
license: CC-BY-4.0
access: { duo_codes: [DUO:0000004], controlled: false }
catalog_refs:
  dcat_entry: cytognosis.catalog:0001
  doi: 10.0000/example
```

## 8. Model (the analytical procedure)

### What you need to declare

For any Cytognosis model release, the manifest should answer:

1. **Feature axis contract** (which feature manifest, which annotation version, which identifier scheme)
2. **Input/output tensor schema** (MLflow ColSpec/TensorSpec, with optional ONNX export)
3. **Output type semantics** (point estimate, embedding, classification probabilities, parameterized distribution; if distribution, the class name from Pyro/TFP plus the natural-parameter slots)
4. **Architectural pattern** (LinkML enumeration: encoder, vae, gan, diffusion, transformer, etc.)
5. **Operational effect** (EDAM Operation + HuggingFace `pipeline_tag`)
6. **Training distribution** (organism, tissue, cell type, disease, assay class)
7. **Inference parameters** (MLflow `params`)
8. **Provenance** (Workflow Run RO-Crate of the training run)
9. **Card / publication** (HuggingFace Model Card YAML, DOME-ML annotation at publication)

### Canonical record

```yaml
id: cytognosis.model:scvi_lung_v1
type: [sosa:Procedure, schema:SoftwareApplication, mlflow:Model]
architectural_pattern: variational_autoencoder
edam_operation: [operation:3935, operation:3937]   # dim reduction, feature extraction
hf_pipeline_tag: feature-extraction
training_distribution:
  organism: [NCBITaxon:9606]
  tissue: [UBERON:0002048, UBERON:0008952]
  cell_type_constraint: asct+b:lung
  assay_class: [EFO:0009922]
input:
  feature_manifest_uri: cytognosis.feature_manifest:human-ensembl-111-canonical
  feature_manifest_sha256: 0xdeadbeef...
  expected_value_spec:
    value_type: int                          # raw counts
    unit: "1"
    transformation: identity
mlflow_signature_uri: ...
output:
  - name: latent
    tensor: float32[batch, 30]
    semantics: embedding
  - name: nb_mean
    tensor: float32[batch, n_genes]
    semantics: NegativeBinomial.mean
  - name: nb_dispersion
    tensor: float32[n_genes]
    semantics: NegativeBinomial.dispersion
output_distribution_class: NegativeBinomial   # the distributional output extension
params:
  - { name: return_distribution, type: enum[mean, samples, parameters] }
  - { name: n_samples, type: int32 }
weights_uri: hf://cytognosis/scvi_lung_v1
training_run_ro_crate: s3://cytognosis-data/.../scvi_lung_v1_run.rocrate
hf_model_card: hf://cytognosis/scvi_lung_v1/README.md
dome_ml_score: ...
```

Detail in [models.md](models.md).

---

# Part III: Composition

## 9. The packaging layer: RO-Crate and PROV-O

The chain (Body → Sensor → Data → Model) is only useful if it is traceable. RO-Crate gives a single archive format that bundles all the manifests, the actual data, the code, and the provenance.

### RO-Crate basics

[RO-Crate](https://www.researchobject.org/ro-crate/) is a community-driven, lightweight packaging format. The "crate" is a directory (or zip) with:

- `ro-crate-metadata.json`: a JSON-LD file rooted in `schema.org` describing every file in the crate.
- The data files themselves.
- Optional: workflow definitions, environment specs, intermediate provenance.

[RO-Crate Spec 1.1.2](https://www.researchobject.org/ro-crate/specification/1.1/metadata.html) is the current stable. JSON-LD over schema.org is the encoding.

### Workflow Run RO-Crate

The [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) extension specializes RO-Crate for execution provenance:

- Records URLs used to fetch input data and workflows.
- Records SHA256 fingerprints of inputs, workflow files, container images.
- Records derived metadata about each step.
- Aligned to W3C PROV-O (`Entity`, `Activity`, `Agent`, `wasGeneratedBy`, `used`, `wasDerivedFrom`).
- Implemented by Nextflow (nf-prov), Snakemake, Galaxy, WfExs.

For Cytognosis, every "model applied to dataset" run becomes a Workflow Run RO-Crate. The crate contains:

- The `ModelManifest` and `DatasetManifest` and the relevant `ObservationManifest`(s) and `SubjectManifest`(s).
- The model weights (or a hash + URI to them).
- The output (new dataset, new observation, evaluation report).
- The PROV-O graph linking inputs to outputs.
- The ISA Investigation/Study/Assay context (if it was a study run rather than ad hoc inference).

### BioCompute Object

For regulatory work (NGS-based diagnostics, FDA submissions), [IEEE 2791 BioCompute Object](https://www.biocomputeobject.org/) is the regulator-facing standard. It can be embedded in an RO-Crate as a profile. Adopt only when filing.

Source: [RO-Crate Metadata Spec 1.1.2](https://www.researchobject.org/ro-crate/specification/1.1/metadata.html), [Workflow Run RO-Crate site](https://www.researchobject.org/workflow-run-crate/), [Workflow Run paper, PLOS One 2024](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309210), [PROV-O W3C](https://www.w3.org/TR/prov-o/).

## 10. The authoring layer: LinkML

[LinkML](https://linkml.io) is the right meta-schema. One source of truth, multiple emitted artifacts:

- JSON Schema (runtime validation)
- SHACL (graph validation against the SOSA + bio ontology backbone)
- OWL (subsumption reasoning)
- Pydantic v2 (Python parsing)
- SQL DDL (warehouse tables)
- GraphQL (API typing)

LinkML is used by Biolink, NMDC, NCATS Translator, Monarch, the Center for Cancer Data Harmonization, and the Alliance of Genome Resources.

The Cytognosis LinkML schema set:

| Class | Subclasses | Role |
|---|---|---|
| `cytognosis:SubjectManifest` | `sosa:FeatureOfInterest`, `fhir:Patient`, `ccf:Donor` | A donor / participant |
| `cytognosis:SampleManifest` | `sosa:Sample`, `fhir:Specimen`, `ccf:TissueBlock` | A specimen with optional CCF registration |
| `cytognosis:SensorManifest` | `sosa:Sensor` | A device/agent that observes |
| `cytognosis:ActuatorManifest` | `sosa:Actuator` | A device/agent that perturbs (closed-loop, CRISPR, drug dosing) |
| `cytognosis:ProcedureManifest` | `sosa:Procedure`, `obi:protocol` | A protocol (wet or dry) |
| `cytognosis:ObservationManifest` | `sosa:Observation` (or `sosa:ObservationCollection` for time series) | A single observation or collection |
| `cytognosis:ActuationManifest` | `sosa:Actuation` (or `sosa:ActuationCollection`) | A single actuation or collection |
| `cytognosis:DatasetManifest` | `sosa:Result`, `dcat:Dataset` | A storable artifact with axes, schemas, and provenance |
| `cytognosis:ModelManifest` | `sosa:Procedure`, `mlflow:Model` | A model (also a Procedure when invoked) |
| `cytognosis:StudyManifest` | `isa:Study`, `fhir:ResearchStudy`, `ssn:Deployment` | The experimental container |
| `cytognosis:InvestigationManifest` | `isa:Investigation`, `prov:Activity` | Top-level project context |

Each class binds its slots to ontology CURIEs (validated by Bioregistry). Cytognosis-emitted SHACL composes with stock SOSA-SHACL for two-layer validation.

## 11. The exchange layer: Croissant, FHIR projection, SensorThings, HuggingFace

Cytognosis-internal manifests are SOSA-aligned LinkML; outward-facing exchange formats are emitted automatically:

| Outward format | Trigger |
|---|---|
| HuggingFace Model Card YAML | Model publication |
| Croissant JSON-LD | Dataset publication |
| FHIR Bundle (Observation, Specimen, Patient, Procedure, Device, ResearchStudy) | Clinical-system handoff |
| OGC SensorThings Things/Datastreams/Observations entities | IoT/wearable system handoff |
| ISA-JSON | Cross-organization study handoff |
| DCAT v3 entry | Internal/external data catalog |
| DataCite DOI | Citation footprint |
| Workflow Run RO-Crate | Run-level archival, reproducibility, sharing |
| BioCompute Object | Regulatory submission |
| DOME-ML annotation | Model publication |

The internal manifest is the source of truth; every exchange format is a deterministic projection.

## 12. The recommended stack (consolidated TL;DR)

| Layer | Recommendation |
|---|---|
| **Spatial scaffold for the body** | **HRA / CCF Ontology v2.x + ASCT+B + RUI + VCCF + OMAP** |
| **Generic observation grammar** | **SOSA + SSN + SSN-Ext** (W3C/OGC, 2023 ed.); validate with **SOSA-SHACL** |
| **Experimental container** | **ISA Abstract Model** (Investigation/Study/Assay/Material/Process), serialized as **ISA-JSON** internally |
| **Authoring meta-schema** | **LinkML**; emit JSON Schema, SHACL, OWL, Pydantic, GraphQL, SQL DDL |
| **Identifier resolution** | **Bioregistry** for every CURIE |
| **Bio nouns** | **OBO Foundry**: NCBITaxon, CL, UBERON, FMA, MONDO, HP, GO, ChEBI, SO, HGNC, NCBIGene, Ensembl, UniProt, PATO, DUO. **EFO** for assay/sample/condition. **OBI** for investigation/process/device. **BAO** for 5-axis assay decomposition (perturbation). **HED** for events. **EDAM** for operations/topics/data/format. **UCUM/UO** for units. **LOINC** for clinical readouts. **SNOMED CT** for clinical findings (when needed). |
| **Domain profiles (per modality)** | **single-cell-curation 7.x** (omics), **BIDS+HED 1.11+** (neuro), **OME-NGFF/OME-Zarr** (imaging), **FHIR Observation+UCUM+LOINC** (clinical), **OMOP CDM v5.4** (observational), **CDISC SDTM/ADaM** (regulated trials), **Open mHealth + OGC SensorThings** (wearables/IoT), **DICOM Sup 30** (clinical waveforms), **NWB** (electrophysiology) |
| **In-memory data** | **scverse stack**: AnnData (single assay), MuData (multimodal), SpatialData (spatial omics) |
| **On-disk storage** | **AnnData-Zarr / TileDB-SOMA** (omics at scale), **OME-Zarr** (imaging), **Parquet** (tabular and sensor time series) |
| **Model artifact** | **MLflow signature** (typed contract) + **ONNX** (runtime portability) + **HuggingFace Hub** (distribution) + **scvi-hub conventions** for scverse-native generative models |
| **Distributional outputs** | **Pyro/NumPyro/TFP** distribution registry; declare class via Cytognosis LinkML extension `output_distribution_class` until Croissant ML adds it |
| **Dataset card / ML exchange** | **Croissant** (MLCommons, JSON-LD over schema.org) |
| **Catalog and citation** | **DCAT v3**, **DataCite DOI**, **schema.org / Bioschemas** for SEO |
| **Provenance + packaging** | **Workflow Run RO-Crate + PROV-O**; **BioCompute Object** when regulated |
| **Publication review** | **DOME-ML** annotations |

## 13. The match function (the operational payoff)

Given:

- one or more `cytognosis:SubjectManifest` (the FOIs)
- one or more `cytognosis:ObservationManifest` per Subject (with their associated `SensorManifest`, `ProcedureManifest`, `SampleManifest`, `DatasetManifest`)
- one or more `cytognosis:ModelManifest`

The platform's `match(model, dataset, observations) -> MatchResult` returns:

```yaml
match_result:
  compatible: true | false | partial
  mapping:
    feature_axis: { source: ..., model_expects: ..., transform: identity }
    sample_axis: { source: ..., model_expects: ..., transform: identity }
    value_semantics: { source: ..., model_expects: ..., transform: log1p_cp10k }
  spatial_compatibility:
    organ_overlap: [UBERON:0002048]
    asctb_table_used: HRA-v2.2-lung-v3
  warnings:
    - "Source dataset has 1043 genes outside model's training distribution; will be zero-imputed"
  errors: []
  required_transforms:
    - { type: log1p_cp10k, applied_to: layers.X }
  required_subsetting:
    - { axis: var, by: model.feature_manifest_sha256, drops: 1043 }
```

The match function uses:

- SOSA-SHACL for grammar-level validation (every input has the SOSA shape).
- Cytognosis-LinkML-emitted SHACL for bio-specific shape (correct ontology branches, valid feature manifest hash, allowed UCUM units for the property).
- HRA/CCF spatial join for cross-modality co-location.
- ASCT+B-aware constraints on cell-type compatibility.
- DUO-aware policy gating on intended-use vs. consent.

Because the upper grammar is shared (SOSA + HRA + ISA + LinkML), a single match function works across modalities. New modalities are added by writing the Layer 2 profile binding, not by adding new match-function code.

## 14. Gaps and Cytognosis-authored extensions

The following gaps remain after adopting the entire stack above. Each has a workaround, and several are candidates for upstream contribution.

| Gap | Workaround | Upstream candidate |
|---|---|---|
| Distributional outputs lack a standard type | LinkML `output_distribution_class` field with Pyro/TFP class names | Propose Croissant ML extension |
| No standard for content-addressed feature manifests | SHA256 of canonical-ordered ID list; verify equality at match | Cytognosis-authored convention (mechanically simple) |
| Architectural pattern (encoder/decoder/diffusion) not in any ontology | LinkML enumeration + EDAM Operation for effect | Propose to EDAM if it stabilizes |
| Cross-regime mixing per subject (snapshot + periodic + continuous) | Cytognosis `SubjectManifest` linking multiple `ObservationManifest`s, each with its own regime | None obvious; this is a Cytognosis platform pattern |
| Continuous-stream-to-snapshot bridge transforms are themselves models | Bridge transforms become `ModelManifest`s with regime translation declared | None obvious |
| DUO consent enforcement at match time | Small Cytognosis policy engine | DUO Beacon, REMS partial coverage |
| Disease-state and developmental atlases not unified under HRA CCF | Use HRA as healthy baseline; register disease atlases as CCF extension subgraphs | HRA roadmap will address |
| HRA does not cover dynamic state transitions | Captured in observation/study layer, not the spatial reference | None obvious |
| Bio-aware HED library for cellular perturbations and assay events | Author HED library extension | Submit to hed-standard |

## 15. Concrete next steps for Cytognosis

In rough dependency order:

1. **Pin the foundation versions.** SOSA/SSN 2023 edition + SSN-Ext; HRA KG v2.2 (or latest); a monthly Cytognosis OBO Foundry snapshot; Bioregistry latest. Codify as a `cytognosis-ontologies` Python package with version pins.

2. **Author the LinkML manifest set.** All 11 classes from §10. Bind slots to ontology CURIEs. Emit JSON Schema, Pydantic v2, SHACL. Compose SOSA-SHACL on top of the Cytognosis-emitted SHACL.

3. **Build the ingestion path.** Domain-specific adapters that convert (HuBMAP donor/sample/dataset records, single-cell-curation 7.x AnnData, BIDS folders, FHIR Bundles, Open mHealth JSON, OGC SensorThings entities) into the Cytognosis manifest set. Each adapter is a deterministic projection.

4. **Implement the match function.** Strict on irreducibles (organism, feature manifest hash, value semantics), tolerant elsewhere. Returns `MatchResult` with explicit transform list.

5. **First end-to-end demo (single modality).** scVI checkpoint + CELLxGENE Census slice + an in-house lung biopsy AnnData with RUI registration into HRA. Run the full pipeline. Confirm the spatial join works (lung-relevant cells from the Census align with lung-relevant cells from the biopsy).

6. **First cross-modality demo.** A single longitudinal donor with: snapshot scRNA-seq lung biopsy, periodic bloodwork (FHIR Observation), 14-day CGM stream (Open mHealth + SensorThings), 64-channel resting-state EEG session (BIDS+HED). All four become `ObservationManifest`s on the same `SubjectManifest`. Cross-modal query: predict CGM time-in-range over the next month from the donor's lung biopsy embedding and bloodwork features. This is the test of whether the unified upper grammar pays off.

7. **First closed-loop demo.** Subject + CGM + insulin pump as one `ssn:System` with one `SubjectManifest` (FOI), one `SensorManifest` (CGM), one `ActuatorManifest` (pump), and matched `ObservationManifest` / `ActuationManifest` streams over a defined `StudyManifest` (ISA Study). This exercises the actuator side of SOSA.

8. **Publish the first dataset and the first model.** Emit Croissant + Workflow Run RO-Crate + HuggingFace Model Card + DOME-ML annotation. Validate that an external collaborator can ingest the published artifacts using only standard tooling (no Cytognosis-specific code).

9. **Identify upstream contributions.** `output_distribution_class` for Croissant ML is the obvious first proposal. A bio-HED library extension is a second. A SOSA "biomedical investigations" profile (maybe "Bio-SOSA") is a possible third.

10. **Decide the long-tail standards.** OMOP / CDISC adoption for clinical interop, BCO for any regulatory pathway, NWB for any electrophysiology work, DICOM Sup 30 for any clinical waveform interop. None are urgent; all are well-mapped.

---

## Master sources index

### Spatial body scaffold
- [HRA portal](https://humanatlas.io/), [HRA About](https://humanatlas.io/about), [CCF Ontology](https://humanatlas.io/ccf-ontology), [HRA-VCCF GitHub](https://github.com/hubmapconsortium/hra-vccf), [HRA OMAP](https://humanatlas.io/omap), [HRA UI repo](https://github.com/hubmapconsortium/hra-ui)
- [HuBMAP Portal](https://portal.hubmapconsortium.org/), [HuBMAP Consortium](https://hubmapconsortium.org/), [NIH Common Fund HuBMAP](https://commonfund.nih.gov/HuBMAP)
- [HuBMAP HRA construction Nature Methods 2024](https://www.nature.com/articles/s41592-024-02563-5), [HRA Knowledge Graph Sci Data 2025](https://www.nature.com/articles/s41597-025-05183-6), [Specimen/biological/spatial Sci Data 2023](https://www.nature.com/articles/s41597-023-01993-8), [ASCT+B Nature Cell Biology 2021](https://www.nature.com/articles/s41556-021-00788-6), [3D Reference Organs PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10079270/), [RUI Comm Biology 2022](https://www.nature.com/articles/s42003-022-03644-x), [VCCF Sci Data 2023](https://www.nature.com/articles/s41597-023-02018-0), [OMAP Nature Methods 2023](https://www.nature.com/articles/s41592-023-01846-7), [HuBMAP Portal arXiv 2511.05708](https://arxiv.org/abs/2511.05708)

### Generic observation grammar
- [SOSA / SSN W3C Rec](https://www.w3.org/TR/vocab-ssn/), [SSN 2023 Edition](https://www.w3.org/TR/vocab-ssn-2023/), [SSN-Ext](https://www.w3.org/TR/vocab-ssn-ext/), [SDW-SOSA-SSN repo](https://github.com/w3c/sdw-sosa-ssn/)
- [SOSA paper arXiv 1805.09979](https://arxiv.org/abs/1805.09979), [SOSA/SSN Semantic Web J.](https://www.semantic-web-journal.net/system/files/swj1804.pdf)
- [Alignment to O&M / ISO 19156](https://www.w3.org/2015/spatial/wiki/Alignment_to_O&M), [ISO 19156:2023](https://www.iso.org/standard/82463.html)
- [SOSA-SHACL IJCKG 2021](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235)
- [SSN+FHIR mobile health BMC 2019](https://link.springer.com/article/10.1186/s12911-019-0806-z), [SSN+IoMT SAGE 2020](https://journals.sagepub.com/doi/full/10.1177/1550147719889591)

### Experimental hierarchy
- [ISA Abstract Model](https://isa-specs.readthedocs.io/en/latest/isamodel.html), [ISA-Tab](https://isa-specs.readthedocs.io/en/latest/isatab.html), [ISA-JSON](https://isa-specs.readthedocs.io/en/latest/isajson.html), [ISA Tools](https://isa-tools.org/), [ISA API paper PMC 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8444265/)

### Bio-noun ontologies
- [OBI](https://obi-ontology.org/), [OBI on OBO Foundry](http://obofoundry.org/ontology/obi.html), [OBI PLOS One 2016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154556)
- [BAO Bioregistry](https://bioregistry.io/bao), [BAO Evolving J Biomed Semantics 2014](https://jbiomedsem.biomedcentral.com/articles/10.1186/2041-1480-5-S1-S5), [BAO PK/PD 2025](https://link.springer.com/article/10.1186/s13326-025-00342-5), [BAO Assay Guidance Manual](https://www.ncbi.nlm.nih.gov/books/NBK92017/)
- [EFO at EBI](https://www.ebi.ac.uk/efo/), [EFO repo](https://github.com/EBISPOT/efo)
- [EDAM site](https://edamontology.org), [EDAM repo](https://github.com/edamontology/edamontology), [EDAM on BioPortal](https://bioportal.bioontology.org/ontologies/EDAM)
- [Bioregistry](https://bioregistry.io/), [OBO Foundry](http://obofoundry.org/), [Bioregistry Sci Data 2022](https://www.nature.com/articles/s41597-022-01807-3)
- [single-cell-curation latest](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html)

### Sensors and assays (modality-specific)
- [BIDS spec](https://bids-specification.readthedocs.io/en/stable/), [BIDS site](https://bids.neuroimaging.io/), [HED](https://www.hedtags.org/), [HED v5 schema 2025](https://zenodo.org/records/15571221)
- [FHIR Observation](https://hl7.org/fhir/observation.html), [UCUM in FHIR](https://www.hl7.org/fhir/valueset-ucum-units.html), [LOINC](https://loinc.org/)
- [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html), [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm), [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam)
- [Open mHealth](https://www.openmhealth.org/), [OpenmHealth on FHIR](https://healthedata1.github.io/mFHIR/), [OGC SensorML](https://www.ogc.org/standards/sensorml/), [OGC SensorThings](https://www.ogc.org/standards/sensorthings/)
- [DICOM](https://www.dicomstandard.org/), [DICOM Sup 30 Waveform](https://dicom.nema.org/dicom/supps/sup30_lb.pdf)

### Data formats and storage
- [AnnData docs](https://anndata.readthedocs.io/), [scverse](https://scverse.org/), [MuData](https://github.com/scverse/mudata), [SpatialData docs](https://spatialdata.scverse.org/), [SpatialData Nature Methods 2024](https://www.nature.com/articles/s41592-024-02212-x)
- [TileDB-SOMA](https://github.com/single-cell-data/TileDB-SOMA)
- [OME-NGFF](https://ngff.openmicroscopy.org/), [OME-Zarr Springer 2023](https://link.springer.com/article/10.1007/s00418-023-02209-1)
- [Apache Arrow](https://arrow.apache.org/), [Parquet](https://parquet.apache.org/)

### Models and ML
- [ONNX](https://onnx.ai/), [ONNX IR spec](https://onnx.ai/onnx/repo-docs/IR.html)
- [MLflow signatures](https://mlflow.org/docs/latest/ml/model/signatures/)
- [Croissant](https://docs.mlcommons.org/croissant/), [Croissant 1.x announce](https://mlcommons.org/2024/03/croissant_metadata_announce/), [Croissant + MCP 2025](https://mlcommons.org/2025/10/croissant-mcp/), [Croissant arXiv 2403.19546](https://arxiv.org/pdf/2403.19546)
- [DOME Nat Methods 2021](https://www.nature.com/articles/s41592-021-01205-4), [DOME Registry arXiv 2408.07721](https://arxiv.org/abs/2408.07721)
- [Hugging Face Model Cards](https://huggingface.co/docs/hub/en/model-cards)
- [scvi-tools docs](https://docs.scvi-tools.org/), [scvi-hub on HF](https://huggingface.co/scvi-tools)
- [BioModels](https://www.ebi.ac.uk/biomodels/), [SBML](https://sbml.org/)
- [NumPyro](https://num.pyro.ai/), [Pyro](https://pyro.ai/)
- [Virtual Cell Challenge 2025](https://virtualcellchallenge.org/), [VCC Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)

### Authoring, packaging, provenance
- [LinkML site](https://linkml.io/), [LinkML GigaScience 2025](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082)
- [DCAT v3](https://www.w3.org/TR/vocab-dcat-3/), [DCAT v3 W3C announce](https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/)
- [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/)
- [PROV-O W3C](https://www.w3.org/TR/prov-o/), [RO-Crate](https://www.researchobject.org/ro-crate/), [RO-Crate Spec 1.1.2](https://www.researchobject.org/ro-crate/specification/1.1/metadata.html), [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/), [Workflow Run paper PLOS One 2024](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309210)
- [DataCite](https://datacite.org/)
- [BioCompute Object IEEE 2791](https://www.biocomputeobject.org/)

### Other
- [FAIR Genomes Sci Data 2022](https://www.nature.com/articles/s41597-022-01265-x), [FAIR principles Sci Data 2016](https://www.nature.com/articles/sdata201618)
- [Schema Playground PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10116472/)
