# Schemas for Models, Sensors, Data, and the Human Body: Survey and Recommended Stack

**Date:** 2026-05-07 (updated)
**Audience:** Cytognosis Foundation platform/architecture
**Goal:** Identify best-of-breed schemas, frameworks, and ontologies for representing, validating, and matching the four coupled entities Cytognosis cares about, and propose a primary stack.

## Start here

The consolidated master document is **[unified-report.md](unified-report.md)**. It is the primary reference and supersedes the per-entity files for day-to-day use. The per-entity files (`models.md`, `sensors.md`, `data.md`, `interop.md`, `human-body.md`) are retained as deeper references and full source citations.

## The four entities

Cytognosis collects **data** from the **human body** using **sensors**, and uses dedicated **models** to analyze and embed them. The four are linked in one chain that maps onto the SOSA observation grammar: a `Sensor` makes an `Observation` of a `FeatureOfInterest` (the human body) via a `Procedure`, producing a `Result` (the data) which is then consumed by a `Model` (itself another `Procedure`) that emits further `Observation`s like embeddings or predictions.

1. **Human Body** (the FeatureOfInterest). Anchored in the [Human Reference Atlas](https://humanatlas.io/) (HRA / HuBMAP), with CCF coordinates, ASCT+B tables, RUI registration, VCCF distances, OMAP-validated panels.
2. **Sensors and assays.** Anything that produces phenotypic measurement: scRNA-seq, EEG/fMRI, bloodwork, CGM, wearables, imaging. Modality-spanning grammar via SOSA/SSN; bio-specific class via EFO/OBI/BAO; value semantics via UCUM/LOINC; events via HED.
3. **Data.** The artifacts: where they live, in what format (AnnData, MuData, SpatialData, Zarr/OME-NGFF, TileDB-SOMA, Parquet, FHIR, OMOP, BIDS), how dimensions map to metadata, and what units/types the values carry.
4. **Models.** ML models (encoders, generators, predictors, variational models). Their I/O contracts (MLflow signatures, ONNX), feature manifests, distributional outputs, training distributions, and provenance.

These four must compose into a matchable system. The match question: given a model, can it consume a given dataset? Are the cells in the dataset compatible with the model's training distribution (organism, tissue, cell type)? Is the feature axis identical (Ensembl version, canonical ordering)? Can the result be projected back into the donor's longitudinal record? Across modalities, can the same donor's scRNA-seq biopsy and CGM stream be co-embedded?

## Files in this folder

- **[unified-report.md](unified-report.md)**: the consolidated master report. Start here. Body, sensors, data, models in one coherent thread; HRA + SOSA + ISA + bio-noun ontologies + LinkML + RO-Crate; the recommended stack, the match function, gaps, and a step-wise adoption plan.
- [human-body.md](human-body.md): Human Reference Atlas (HRA) and HuBMAP in depth. ASCT+B tables, CCF Ontology, RUI, VCCF, OMAPs, the HuBMAP Data Portal, and how HRA scaffolds sensor data across micro/meso/macro scales.
- [models.md](models.md): Model representation and validation. ONNX, MLflow, Croissant, HuggingFace Model Cards, DOME-ML, scvi-hub, BioModels/SBML, EDAM Operation, distributional outputs (TFP/Pyro/NumPyro), feature ontologies.
- [sensors.md](sensors.md): Phenotypic assay and sensor representation. **SOSA/SSN as the unifying observation grammar**, plus OBI, BAO, EFO, ISA-Tab, BIDS+HED, OME-NGFF, DICOM waveforms, FHIR Observation+UCUM, Open mHealth, OMOP, CDISC SDTM, SensorML/SensorThings as the bio/clinical/IoT slot fillers.
- [data.md](data.md): Data storage, format, and metadata mapping. AnnData, MuData, SpatialData, TileDB-SOMA, OME-Zarr, Parquet/Arrow, LinkML, DCAT, Frictionless, RO-Crate, PROV-O, Bioregistry.
- [interop.md](interop.md): How the entities compose. Two-tier ontology backbone (SOSA/SSN over OBO Foundry), bridge schemas (LinkML, Croissant, RO-Crate), join keys (feature IDs, sample IDs, assay IDs), and the recommended stack with gaps called out explicitly.

## TL;DR recommended stack

For Cytognosis specifically, given the scverse-aligned single-cell + multimodal + longitudinal sensor scope:

| Layer | Recommendation | Why |
|---|---|---|
| Spatial scaffold for the body | **HRA / CCF Ontology + ASCT+B + RUI + VCCF + OMAP** (HuBMAP) | The only existing system that gives spatial coordinates plus part-of nesting plus cell-type-to-biomarker linking at the resolution required to register sensors across scales. 71 organs, 5,800 anatomical structures, 2,268 cell types, 2,531 biomarkers in HRA KG v2.2 |
| Experimental hierarchy | **ISA Abstract Model** (Investigation/Study/Assay/Material/Process), serialized as **ISA-JSON** | The right container for "an investigation produced these studies, each with these assays applied to these samples". Composes natively with SOSA |
| Generic observation grammar (upper) | **SOSA / SSN** (W3C/OGC, 2023 ed.) for `Sensor`, `Observation`, `Sample`, `Actuator`, `FeatureOfInterest`, `ObservableProperty`, `Procedure`, `Result`, with **SSN-Ext** for time-series collections, validated by **SOSA-SHACL** | One modality-independent grammar that unifies omics assays, neuroimaging, clinical labs, wearables, and closed-loop interventions. ISO 19156:2023 aligned via SOSA-OMS. Maps cleanly to FHIR, OMOP, SensorThings at the boundaries |
| Identifier backbone (bio nouns) | **Bioregistry** for CURIE resolution, **OBO Foundry ontologies** (CL, UBERON, FMA, NCBITaxon, MONDO, HP, GO, ChEBI, SO, HGNC, NCBIGene, Ensembl, UniProt, PATO, DUO) for semantic anchors, **EFO** as the application-ontology consolidator, **OBI** for investigation/process/device, **BAO** for 5-axis assay decomposition (perturbation), **HED** for events, **EDAM** for operations/data/format/topic, **UCUM/UO** for units, **LOINC** for clinical readouts | Already standard across scverse, cellxgene, EBI, HRA; populates SOSA's slots |
| Schema description language | **LinkML** as the meta-schema for everything Cytognosis-internal, with classes subclassing the SOSA upper-grammar | Generates JSON Schema, OWL, SHACL, Pydantic, Python classes, SQL DDL from one source. Used by Biolink, NMDC, Translator, Monarch |
| Dataset metadata | **Croissant** (MLCommons) extended with the **single-cell-curation schema** profile for omics, **BIDS** for neuroimaging, **FHIR/OMOP** for clinical | Croissant's ML semantics layer is what makes datasets directly model-ready; the bio profiles preserve domain rigor |
| In-memory data | **AnnData / MuData / SpatialData** (scverse) | Already the lingua franca for single-cell; first-class obs/var/obsm/uns slots map onto sensor metadata cleanly |
| On-disk data | **Zarr / OME-NGFF + AnnData-Zarr + Parquet** (the SpatialData layout), with **TileDB-SOMA** for census-scale tabular | Cloud-native, chunked, NGFF 1.0 stable in 2025, SOMA proven on the 44M-cell CZ census |
| Model artifact | **ONNX** for runtime portability, **MLflow** signatures for the IO contract, **HuggingFace Hub** for distribution, **scvi-hub Model Cards** for scverse-native generative models | ONNX gives the runtime, MLflow gives the typed contract, HF hosts. scvi-hub already does this for SCVI/SCANVI/totalVI |
| Distributional outputs | **TensorFlow Probability** or **Pyro/NumPyro distributions API** with reparameterized sampling, exposed as MLflow `params` plus a custom Croissant ML field for `output_distribution` | No mature standard exists for serializing a parameterized distribution as a model output type; this is one of the gaps |
| Sensor description | **SOSA/SSN as the upper grammar**, with **OBI + BAO** for assay class (Procedure), **EFO** for experimental factors, **UCUM** for units (Result.unit), **HED** for events in time-series, **single-cell-curation 7.x assay_ontology_term_id** for omics | The upper grammar unifies modalities; each bio ontology has a clear scope; combined coverage spans micro/meso/macro |
| Sampling regime | **OMOP CDM** + **FHIR Observation/Specimen** for snapshot/periodic clinical, **SensorThings API + Open mHealth** for ongoing continuous, **BIDS events.tsv + HED** for bounded continuous neuro, all projected into **SOSA Observations / ObservationCollections** | No single standard handles all four regimes; SOSA gives a single upper-layer view |
| Closed-loop / interventions | **SOSA Actuator / Actuation / ActuatableProperty** | First-class support for the dual to observation. Critical for CGM+pump, CRISPR perturbation, optogenetics, etc. |
| Provenance and packaging | **RO-Crate** + **Workflow Run RO-Crate** + **PROV-O** | Bundles models, data, sensors, code, and lineage as one archive |
| Identity and joining | Hash-stable feature manifests (Ensembl gene IDs in canonical order), CL/UBERON-resolved sample annotations, OBI/BAO-resolved assay class | The trick is making the model's expected feature manifest a content-addressable artifact pinned in the model card |

The rest of this folder explains why each choice, what alternatives were considered, where the gaps are, and how to close them.

## Method

Survey performed via web search across MLCommons, W3C, OBO Foundry, scverse, EBI, MLCommons, MLflow, ONNX, Hugging Face, OHDSI, CDISC, OGC, HL7, BIDS Standard, hed-standard, DOME-ML, NGFF, and primary literature (2023 to 2026). All sources cited in the per-entity files.

Sources consolidated in [interop.md](interop.md) Sources section.
