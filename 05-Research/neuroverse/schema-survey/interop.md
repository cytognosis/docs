# Interop: How Models, Sensors, and Data Compose into a Matchable System

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

The previous three documents survey each entity in isolation. This one is about the join: given a model card, a dataset manifest, and an assay manifest, how do you decide they fit, and what is the minimum machinery required to enforce that fit at runtime?

## The matching problem stated formally

A *match* across the three entities holds when:

1. **Modality match**: the dataset's nature (`edam_data`, `conforms_to`) and the assay's `assay_class` are in the set of modalities the model declares as acceptable inputs.
2. **Sample compatibility**: the dataset's sample-level annotations (organism, tissue, cell_type, disease, development_stage) intersect non-trivially with the model's training distribution as declared in the model card.
3. **Feature compatibility**: the dataset's feature axis matches the model's expected feature manifest. For genes: same identifier scheme, same annotation version, same canonical ordering, with a documented intersection rule for the missing-feature case.
4. **Value compatibility**: the dataset's `value_semantics` (type, unit, transformation, range) match what the model expects. For example, if the model expects `int` raw counts at `X` and the dataset has only `log1p_cp10k` at `X`, the match fails or invokes a recorded transformation.
5. **Sampling regime compatibility**: the dataset's sampling regime is one the model can consume. A model trained on snapshot scRNA-seq cannot directly score a CGM stream without an explicit aggregation step.
6. **Provenance compatibility (optional but recommended)**: the dataset's lineage is acceptable for the intended use. PHI-derived data cannot feed a public benchmark; consented data with a `DUO:0000004` (no restriction) tag can.

A *match* is more than a Boolean: it is a *mapping* that tells the platform how to wire the data into the model, plus a *manifest of any transforms* that must run between source and model.

## What the join keys actually look like

| Join | Key in model card | Key in dataset manifest | Key in assay manifest |
|---|---|---|---|
| Modality | `accepted_modalities[]` | `edam_data`, `edam_format`, `conforms_to` | `assay_class` (OBI/EFO) |
| Sample (organism) | `training_distribution.organism[]` | `obs.organism_ontology_term_id` | `sample.organism` (NCBITaxon) |
| Sample (tissue/cell) | `training_distribution.tissue[]`, `cell_type[]` | `obs.tissue_ontology_term_id`, `obs.cell_type_ontology_term_id` | `sample.tissue`, `sample.cell_type` |
| Feature axis | `feature_manifest_uri` (Croissant) | `var.identifier_scheme`, `annotation_version`, `canonical_order_sha256` | n/a (assay informs feature axis) |
| Value semantics | `expected_input_value_spec` | `value_semantics.X`, `value_semantics.layers.*` | `measurement.{value_type,unit,transformation}` |
| Sampling regime | `accepted_sampling_regimes[]` | (carried forward from assay) | `sampling.regime` |
| Provenance | (constraints if any) | `provenance.*`, `access.duo_codes` | `provenance.*` |

The *names* of these keys do not matter as long as they are consistent across the three manifests. What matters is that the keys reference shared CURIEs from a small set of authoritative ontologies.

## The shared ontology backbone

The ontology stack is now two-tiered: a **generic upper grammar** (SOSA/SSN) that gives modality-independent verbs (observe, sample, actuate), and a **domain noun layer** (OBO Foundry + EDAM + UCUM/LOINC + HED) that fills SOSA's slots with bio-specific terms.

### Upper-layer grammar (modality-independent)

| Ontology / standard | Role |
|---|---|
| **SOSA** (W3C/OGC) | Lightweight core: Sensor, Observation, Sample, Actuator, FeatureOfInterest, ObservableProperty, Procedure, Result. The unifying grammar for any phenotypic measurement |
| **SSN** (W3C/OGC, 2023 ed.) | Richer extension: System, Deployment, Platform, Device. Aligned to ISO 19156:2023 OMS via the SOSA-OMS module |
| **SSN-Ext** | ObservationCollection, ActuationCollection, SamplingCollection. The right home for time-series aggregation |
| **PROV-O** (W3C) | Provenance: Entity, Activity, Agent (composes with SOSA, RO-Crate) |

### Bio noun layer (the slot fillers)

This is the irreducible core every entity references at the bio level. SOSA's slots are populated with these CURIEs:

| Ontology | Role | SOSA slot it most often fills |
|---|---|---|
| **NCBITaxon** | Species | FeatureOfInterest |
| **CL** (Cell Ontology) | Cell type | FeatureOfInterest, Sample |
| **UBERON** | Tissue, organ, anatomy | FeatureOfInterest, Sample |
| **EFO** | Experimental factor (assay class, sample condition) | Procedure, FeatureOfInterest |
| **OBI** | Investigation, study, planned process, assay | Procedure |
| **BAO** | Bioassay decomposition (perturbagen / format / detection / signal / target) | Procedure (5-axis decomposition) |
| **MONDO** | Disease | FeatureOfInterest |
| **HP** | Phenotype | FeatureOfInterest, ObservableProperty |
| **ChEBI** | Chemical entity (drugs, metabolites, compounds) | ObservableProperty, ActuatableProperty |
| **SO** | Sequence Ontology (genomic features, variants) | ObservableProperty |
| **HGNC, NCBIGene, Ensembl** | Gene identifiers | ObservableProperty (the gene axis) |
| **GO** | Gene Ontology (biological processes, molecular functions, cellular components) | ObservableProperty |
| **EDAM** | Operation, Topic, Data, Format (workflow-level semantics) | Procedure (computational), Result (Data/Format) |
| **PATO** | Phenotypic and qualitative attributes (sex, color, shape) | FeatureOfInterest |
| **DUO** | Data use ontology (consent, restrictions) | (governance metadata, not a SOSA slot) |
| **HED** | Hierarchical Event Descriptors (events in time-series) | context.events around an Observation |
| **UCUM** | Units of measure | Result.unit |
| **LOINC** | Clinical observation codes | ObservableProperty (clinical) |
| **schema.org / Bioschemas** | Generic web-discoverable typing | (descriptive metadata) |

**Bioregistry** is the prefix resolver and validator across all of them.

The mental model: SOSA is the *grammar*, OBO is the *vocabulary*. SOSA gives you sentences ("Sensor X observed Property Y of FeatureOfInterest Z via Procedure P, producing Result R"). The OBO ontologies populate X, Y, Z, P, R with terms anyone can dereference and align to. The two together give you a graph that scales from a single CGM reading to a CELLxGENE Census slice without changing model.

## The bridge schemas: how the manifests compose

There are three credible candidates for the meta-schema that holds models, sensors, and data together. They are not mutually exclusive; the recommended stack uses each at the layer it is best at.

### LinkML as the authoring layer

[LinkML](https://linkml.io/) is the right place to author Cytognosis-internal schemas. One source emits:

- JSON Schema (runtime validation in Python/JS)
- SHACL (graph validation against an ontology)
- OWL (formal subsumption reasoning)
- Pydantic v2 models (runtime parsing)
- SQL DDL (warehouse tables)
- Python dataclasses (typed Python)
- GraphQL (API typing)
- ShEx (RDF shape expressions)

The Biolink Model, NMDC, NCATS Translator, Monarch, Center for Cancer Data Harmonization, and Alliance of Genome Resources all use it. [LinkML, GigaScience 2025](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082).

For Cytognosis, the recommendation is to author three top-level LinkML classes (`ModelManifest`, `AssayManifest`, `DatasetManifest`), with ontology slot bindings, and let the LinkML toolchain emit everything else.

### Croissant as the ML-facing exchange

[Croissant](https://docs.mlcommons.org/croissant/) is what makes a dataset directly model-ready. It is JSON-LD over schema.org, so it composes with Bioschemas and DCAT naturally. The ML semantics layer names which fields are inputs, labels, weights. Croissant 1.1 in development adds provenance/lineage/versioning. [Life sciences extension is in the working group's scope](https://docs.mlcommons.org/croissant/).

For Cytognosis, the recommendation is to emit a Croissant document for every published dataset, generated from the LinkML `DatasetManifest`. The Croissant `RecordSet` carries the in-memory schema; the model card cites the Croissant document by URI; the platform's match function reads both.

The gap: Croissant does not yet have a standardized way to declare that a dataset *produces a typed distribution* as a model output. This is one place where Cytognosis would either:
- Add an internal LinkML extension and propose it upstream as a Croissant-ML draft.
- Encode it in a LinkML `ModelManifest.output_distribution_class` field and accept that match logic cannot reason about it without Cytognosis-specific code today.

### RO-Crate as the wrapper for runs and releases

[RO-Crate](https://www.researchobject.org/ro-crate/) and [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) wrap a complete run: model + data + code + provenance + environment. PROV-O aligned. Already supported by Nextflow (nf-prov), Snakemake, Galaxy, WfExs.

For Cytognosis, the recommendation is to package every "model-applied-to-dataset" run as a Workflow Run RO-Crate, archived alongside the resulting dataset version. The RO-Crate is the unit of reproducibility.

## Layered architecture for matching

Building from the inside out, now with SOSA/SSN as the upper-grammar tier:

```
Layer 5: Provenance + reproducibility       → Workflow Run RO-Crate, PROV-O
Layer 4: Ecosystem-facing exchange          → Croissant (datasets), HuggingFace Model Card YAML, DCAT (catalog),
                                               FHIR projection at clinical boundary, SensorThings at IoT boundary
Layer 3: Cytognosis-internal manifests      → LinkML classes: ModelManifest, ObservationManifest,
                                               ActuationManifest, DatasetManifest, SubjectManifest
Layer 2: Domain profile bindings            → single-cell-curation 7.x, BIDS+HED, FHIR/OMOP, OME-NGFF,
                                               Open mHealth, OGC SensorThings/SensorML, DICOM, NWB
Layer 1b: Generic observation grammar       → SOSA / SSN / SSN-Ext (ISO 19156:2023 aligned via SOSA-OMS),
                                               PROV-O for provenance abstraction
Layer 1a: Identifier and bio noun backbone  → Bioregistry + OBO Foundry (CL, UBERON, NCBITaxon, EFO, OBI,
                                               BAO, MONDO, HP, ChEBI, SO, GO, PATO, DUO) + EDAM + UCUM + LOINC + HED
```

Layer 1a (bio nouns) and Layer 1b (generic observation grammar) compose: every Cytognosis observation is a `sosa:Observation` whose slots are populated with Layer 1a CURIEs.

Layer 2 is whatever profile the modality requires; each Layer 2 profile maps deterministically into Layer 1b (SOSA) so heterogeneous modalities can be matched against one another.

Layer 3 is Cytognosis-authored LinkML. Each LinkML class subclasses (or projects to) the appropriate Layer 1b class. `ObservationManifest`, `ActuationManifest`, `SubjectManifest` are the new ones; `ModelManifest` and `DatasetManifest` carry forward from the pre-SOSA design.

Layers 4 and 5 are emitted from Layer 3 deterministically.

The match function lives at Layer 3: given a `ModelManifest`, an `ObservationManifest` (or collection thereof), and a `DatasetManifest`, all validated against Layer 1b SOSA-SHACL plus Layer 1a Cytognosis-LinkML-emitted SHACL, return a typed `MatchResult` with `compatible: bool`, `mapping: {...}`, `transforms: [...]`, `warnings: [...]`, and `errors: [...]`. Because SOSA-SHACL handles the grammar-level validation for free, Cytognosis-authored SHACL only has to enforce the bio-specific constraints (correct ontology branches, right Ensembl version, allowed UCUM units for the Property class, etc.).

## Where each existing standard fits in this picture

| Standard | Layer | Role |
|---|---|---|
| **SOSA** (W3C/OGC) | 1b (generic observation grammar) | Modality-independent vocabulary for Sensor/Observation/Sample/Actuator/FOI/ObservableProperty/Procedure/Result. The unifying upper layer |
| **SSN** (W3C/OGC, 2023) | 1b | Richer extension over SOSA: System, Deployment, Platform, Device. ISO 19156:2023 aligned via SOSA-OMS module |
| **SSN-Ext** | 1b | ObservationCollection/ActuationCollection/SamplingCollection for time series and grouped observations |
| **SOSA-SHACL** | 3 (validation) | W3C SHACL shapes that validate any SOSA graph; Cytognosis-emitted SHACL layers on top for bio-specific constraints |
| ONNX | 3 (model artifact runtime) | Portable runtime weights and IO |
| MLflow signature | 3 (model contract) | Authored typed IO contract |
| HuggingFace Model Card | 4 (model exchange) | Public-facing card emitted from LinkML |
| DOME-ML | 4 (publication checklist) | Review-time annotation |
| Croissant | 4 (dataset exchange) | ML-aware dataset description |
| scvi-hub | 4 (specialized hub) | scverse-native model+data registry on HF |
| BioModels / SBML / CellML | 4 (mechanistic comparators) | Reference mechanistic models |
| AnnData / MuData / SpatialData | 2 (omics in-memory) | Domain profile for omics data |
| TileDB-SOMA | 1 (storage) | Cloud-native scale storage |
| OME-NGFF / OME-Zarr | 2 (imaging on-disk) | Domain profile for bioimaging |
| BIDS + HED | 2 (neuro on-disk) | Domain profile for neuroimaging + events |
| FHIR Observation + UCUM + LOINC | 2 (clinical) | Domain profile for clinical observations |
| OMOP CDM | 2 (observational research) | Domain profile for retrospective EHR |
| CDISC SDTM/ADaM | 2 (clinical trials) | Domain profile for regulated trials |
| Open mHealth | 2 (wearables) | Domain profile for wearable streams |
| OGC SensorThings / SensorML | 2 (IoT sensors) | Domain profile for environmental and IoT sensors. SensorThings is the REST/JSON projection of SOSA-aligned data; SensorML carries internal sensor process structure |
| **ISO 19156:2023 OMS** | 1b (semantics) | The conceptual model SOSA-OMS conforms to. The standard for "observation about a feature" beyond just sensor IoT |
| DICOM (incl. Sup 30 waveforms) | 2 (clinical imaging and waveforms) | Domain profile when interoperating with hospitals |
| EDAM | 1 (semantic) | Operation/Topic/Data/Format ontology |
| OBI, BAO, EFO | 1 (semantic) | Investigation/assay/factor ontology |
| CL, UBERON, NCBITaxon, MONDO, HP, ChEBI, SO | 1 (semantic) | Domain ontology backbone |
| HED | 1 (events) | Event vocabulary, schema-extensible |
| Bioregistry | 1 (resolver) | CURIE prefix registry and validator |
| LinkML | 3 (authoring) | Meta-schema for all Cytognosis-internal manifests |
| RO-Crate / Workflow Run RO-Crate | 5 (packaging) | Run-level provenance and reproducibility |
| PROV-O | 5 (provenance) | W3C provenance model (RO-Crate aligned) |
| DCAT v3 | 4 (catalog) | Public dataset catalog |
| DataCite | 4 (citation) | DOI-level citation |
| BioCompute Object | 5 (regulatory) | FDA-aligned provenance for regulated work |

## Where the gaps are

Even with all of the above adopted, there are real gaps:

### 1. Distributional outputs lack a standard type

ONNX, MLflow, and Croissant treat a model output as a tensor or a nested structure. None has first-class "the output is a parameterized distribution from this class with these natural parameters". Pyro/NumPyro/TFP have the runtime registry; nothing has the spec. Workaround: a LinkML extension carrying `output_distribution_class` plus the natural-parameter tensor names. Watch Croissant ML for upstream resolution.

### 2. Mixing sampling regimes inside one dataset

A patient might contribute (snapshot scRNA-seq from a biopsy) + (periodic bloodwork) + (continuous CGM) + (continuous EEG during a stress test). No single standard handles all four under one manifest. The current pragmatic answer is a top-level `Subject` linked to multiple `Dataset`s under one `Investigation`, ISA-Tab style, with each dataset using its own domain profile. A unified Cytognosis `SubjectManifest` LinkML class is what closes this.

### 3. Architectural type vs. operational effect

EDAM Operation captures the operational effect well (dimensionality reduction, regression, generation). It does not cleanly carry "encoder vs. decoder vs. autoencoder vs. diffusion vs. transformer". Workaround: a Cytognosis-internal LinkML enumeration for architectural pattern, plus EDAM Operation for effect. Propose upstream once the enumeration stabilizes.

### 4. Feature manifest as a content-addressed object

The model says "I expect 38244 genes in this exact order from Ensembl 111". In practice, this is a sorted list of 38244 strings. Today nobody has a clean standard for "feature manifest as a content-addressable artifact". The right move is to ship the manifest as a JSON file with a SHA256, expose the SHA256 in both the model card and the dataset manifest's `var` annotation, and verify equality at match time. Treat this as a Cytognosis-authored convention; it is mechanically simple but has no industry standard.

### 5. Continuous-stream-to-snapshot bridges

A model trained on biopsy snapshots cannot directly score a CGM stream. The platform needs a documented set of *bridge transforms*: aggregation windows, change-point segmentation, FFT/wavelet feature extraction, embedding-time-series. These transforms are themselves models, with their own manifests. The recursion is fine, but no current standard treats it as such. Cytognosis-authored convention: every continuous-to-snapshot bridge is itself a `ModelManifest` with `accepted_modalities: [continuous]` and `output_modality: [snapshot_features]`.

### 6. Data Use Ontology compliance at match time

DUO covers consent and use restrictions. The match function needs to check that a model's `intended_use` is permitted given a dataset's `duo_codes`. Implementing this correctly requires a small policy engine. Existing tools (REMS, DUO Beacon) handle pieces; nothing offers a turnkey "given (DUO codes, model intended use), allow or deny" resolver. Cytognosis-authored is fine; this is governance, not science.

## Concrete next steps for Cytognosis

If the goal is to operationalize this in the platform, the minimum sequence:

1. **Adopt the two-tier ontology backbone.** Pin the SOSA/SSN 2023 edition + SSN-Ext as the upper grammar; pin the OBO Foundry release date (e.g., monthly Cytognosis ontology snapshot) for the bio noun layer; validate every CURIE through Bioregistry; codify in a `cytognosis-ontologies` Python package.
2. **Author the LinkML class set** with SOSA as the explicit upper-class:
   - `ObservationManifest` subclasses `sosa:Observation` (or `sosa:ObservationCollection` for series)
   - `ActuationManifest` subclasses `sosa:Actuation` (closed-loop / perturbation experiments)
   - `SubjectManifest` subclasses `sosa:FeatureOfInterest` (the unified longitudinal subject record across modalities)
   - `SampleManifest` subclasses `sosa:Sample`
   - `SensorManifest` subclasses `sosa:Sensor`
   - `ProcedureManifest` subclasses `sosa:Procedure`
   - `ModelManifest` (carries `sosa:Procedure` URI when the model is invoked as a Procedure; otherwise standalone)
   - `DatasetManifest` (carries pointers to one or more Observations)

   Emit JSON Schema, Pydantic, and SHACL. Compose Cytognosis-LinkML SHACL with stock SOSA-SHACL.
3. **Mirror the single-cell-curation 7.x conventions** for any omics dataset; mirror BIDS+HED for neuroimaging; mirror FHIR+OMOP for clinical; mirror Open mHealth + OGC SensorThings for wearables/IoT. Each Layer 2 profile gets a deterministic projection into the Layer 3 SOSA-aligned manifests.
4. **Implement the match function** as a typed Python service: in: three manifests, out: `MatchResult`. Start with strict equality on the irreducibles (organism, feature manifest hash, value semantics), tolerant on the rest. Because the manifests are SOSA-aligned, the match function gets the modality-independent checks for free (every observation has a FOI, an ObservableProperty, a Procedure, a Result) and only needs Cytognosis logic for the bio-specific compatibility checks.
5. **Emit Croissant + HuggingFace Model Card + Workflow Run RO-Crate + FHIR Bundle + SensorThings entities** automatically from the LinkML manifests at the publication step. The internal SOSA-aligned manifest is the source of truth; the public formats are derived.
6. **Pick the first end-to-end demo**: scVI checkpoint + CELLxGENE Census slice + an in-house biopsy AnnData. Each piece becomes one or more `sosa:Observation` records. Run the full match pipeline, check the result, iterate. This is the use case where every standard mentioned in this document already has working tooling.
7. **Pick the first cross-modality demo**: a longitudinal subject record combining a snapshot scRNA-seq biopsy, periodic bloodwork (FHIR Observation), and a 14-day CGM stream (Open mHealth + SensorThings). All three become `sosa:Observation` instances on the same `sosa:FeatureOfInterest` (the patient). This is the test of whether the unified upper grammar actually pays off.
8. **Identify the first Cytognosis-specific extension to upstream**: the `output_distribution_class` field is the obvious candidate, since it has clear cross-org demand and is squarely within Croissant ML's scope. A second candidate is a Bio-HED library schema for cellular perturbations and assay events; a third is a SOSA profile for biomedical sensors (a "Bio-SOSA" extension), if upstream W3C/OGC interest exists.

## A note on scope

Most of the rigor in this document is targeted at the omics and clinical settings, because that is where the standards are densest. For phenotypic measurement modalities outside that core (continuous physiological telemetry, ambient sensors, behavioral logs), the standards are thinner and the right move is to lean on FHIR + UCUM + Open mHealth where possible and accept that some Cytognosis-authored LinkML classes will be needed. The key is to author them in LinkML so they can be evolved into upstream proposals later, rather than living as ad-hoc JSON shapes in a service somewhere.

## Master sources index

### Models
- [ONNX](https://onnx.ai/), [ONNX IR spec](https://onnx.ai/onnx/repo-docs/IR.html)
- [MLflow signatures](https://mlflow.org/docs/latest/ml/model/signatures/)
- [Croissant](https://docs.mlcommons.org/croissant/), [Croissant arXiv](https://arxiv.org/pdf/2403.19546)
- [DOME](https://www.nature.com/articles/s41592-021-01205-4), [DOME Registry](https://registry.dome-ml.org/intro)
- [Hugging Face Model Cards](https://huggingface.co/docs/hub/en/model-cards)
- [scvi-tools](https://docs.scvi-tools.org/), [scvi-hub on HF](https://huggingface.co/scvi-tools)
- [BioModels](https://www.ebi.ac.uk/biomodels/), [SBML](https://sbml.org/)
- [NumPyro](https://num.pyro.ai/), [Pyro](https://pyro.ai/)

### Generic observation grammar (upper layer)
- [SOSA / SSN W3C Recommendation](https://www.w3.org/TR/vocab-ssn/), [SSN 2023 Edition](https://www.w3.org/TR/vocab-ssn-2023/)
- [SSN-Ext](https://www.w3.org/TR/vocab-ssn-ext/), [SDW-SOSA-SSN repo](https://github.com/w3c/sdw-sosa-ssn/)
- [SOSA arXiv 1805.09979](https://arxiv.org/abs/1805.09979), [SOSA/SSN, Semantic Web J.](https://www.semantic-web-journal.net/system/files/swj1804.pdf)
- [Alignment to O&M / ISO 19156](https://www.w3.org/2015/spatial/wiki/Alignment_to_O&M), [ISO 19156:2023](https://www.iso.org/standard/82463.html)
- [SOSA-SHACL, IJCKG 2021](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235)
- [SSN + FHIR mobile health, BMC 2019](https://link.springer.com/article/10.1186/s12911-019-0806-z), [SSN + IoMT, SAGE 2020](https://journals.sagepub.com/doi/full/10.1177/1550147719889591)

### Sensors and assays
- [OBI](https://obi-ontology.org/), [BAO](https://bioregistry.io/bao), [EFO](https://www.ebi.ac.uk/efo/)
- [BIDS](https://bids-specification.readthedocs.io/), [HED](https://www.hedtags.org/)
- [ISA Tools](https://isa-tools.org/), [MIxS](https://genomicsstandardsconsortium.github.io/mixs/)
- [FHIR Observation](https://hl7.org/fhir/observation.html), [UCUM in FHIR](https://www.hl7.org/fhir/valueset-ucum-units.html), [LOINC](https://loinc.org/)
- [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html), [OHDSI](https://www.ohdsi.org/)
- [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm), [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam)
- [Open mHealth](https://www.openmhealth.org/), [OpenmHealthtoFHIR](https://healthedata1.github.io/mFHIR/)
- [OGC SensorML](https://www.ogc.org/standards/sensorml/), [OGC SensorThings](https://www.ogc.org/standards/sensorthings/)
- [DICOM](https://www.dicomstandard.org/), [DICOM Sup 30](https://dicom.nema.org/dicom/supps/sup30_lb.pdf)

### Data
- [AnnData](https://anndata.readthedocs.io/), [MuData](https://github.com/scverse/mudata), [SpatialData](https://spatialdata.scverse.org/)
- [TileDB-SOMA](https://github.com/single-cell-data/TileDB-SOMA)
- [OME-NGFF / OME-Zarr](https://ngff.openmicroscopy.org/)
- [Apache Arrow](https://arrow.apache.org/), [Parquet](https://parquet.apache.org/)
- [LinkML](https://linkml.io/), [LinkML GigaScience 2025](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082)
- [Frictionless](https://framework.frictionlessdata.io/)
- [DCAT v3](https://www.w3.org/TR/vocab-dcat-3/)

### Identifiers and provenance
- [Bioregistry](https://bioregistry.io/), [OBO Foundry](http://obofoundry.org/)
- [PROV-O](https://www.w3.org/TR/prov-o/)
- [RO-Crate](https://www.researchobject.org/ro-crate/), [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)
- [DataCite](https://datacite.org/)
- [single-cell-curation 7.x](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html)
- [BioCompute Object IEEE 2791](https://www.biocomputeobject.org/)

### Other relevant references
- [Virtual Cell Challenge 2025](https://virtualcellchallenge.org/), [Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)
- [FAIR Genomes Sci Data 2022](https://www.nature.com/articles/s41597-022-01265-x)
- [Schema Playground PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10116472/)
