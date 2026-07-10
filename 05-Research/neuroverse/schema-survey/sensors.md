# Sensors and Phenotypic Assays: Schemas, Frameworks, and Ontologies

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Scope: how to describe a phenotypic measurement (the assay or sensor) so that another system can match it to a model input, a downstream analysis, or co-register it with another modality. Six sub-questions:

0. What is the *generic grammar* of "a sensor made an observation about a feature of interest using a procedure and produced a result", before any biomedical specifics?
1. How is the assay class (the "type of measurement") declared?
2. How is the entity being measured (cells from organ X of organism Y) declared?
3. How are the value semantics (unit, range, scale, type) declared?
4. How is the sampling regime (snapshot, periodic, bounded continuous, ongoing) declared?
5. How is the experimental and event context (what happened during/before measurement) declared?

The phenotypic scope spans micro (single-cell omics, microscopy), meso (EEG/fMRI, bloodwork), and macro (wearables, CGM, physiological telemetry). No single standard covers all three. The right answer is the **SOSA/SSN observation grammar as the unifying upper layer**, with the bio-specific ontologies (OBI, BAO, EFO, UCUM, LOINC, MONDO, CL, UBERON) bound into SOSA's slots, plus modality-specific data structures (BIDS, OME-NGFF, FHIR, OMOP, SDTM, SensorML) as the on-disk profiles.

## 0. The unifying observation grammar: SOSA / SSN

The single biggest gap in the original survey was the absence of a *generic, modality-independent* vocabulary for observation. SOSA fills that gap. It lets a 10x scRNA-seq run, an EEG session, a CGM stream, and an MRI scan all be described with the same six core relations, with the bio-specific ontologies (OBI/BAO/EFO/UBERON/CL/...) plugged into the slots.

### What SOSA/SSN is

[SOSA](https://www.w3.org/TR/vocab-ssn/) (Sensor, Observation, Sample, and Actuator) is the lightweight core ontology. [SSN](https://www.w3.org/TR/vocab-ssn-2023/) (Semantic Sensor Network) is the richer extension. Joint W3C Recommendation and OGC implementation standard, originally 2017, [2023 edition](https://w3c.github.io/sdw-sosa-ssn/ssn/) aligns to ISO 19156:2023 (Geographic information: Observations, measurements and samples). [Spatial Data on the Web Working Group repo](https://github.com/w3c/sdw-sosa-ssn/).

The 2023 edition is modular:

| Module | Scope |
|---|---|
| **SOSA** | Lightweight core: 19 classes, ~30 properties. Self-contained. Targets Web developers, IoT, citizen science, lightweight Linked Data |
| **SSN** | The richer extension: System, Deployment, Platform, Device, ObservableProperty hierarchy. Adds OWL axiomatization |
| **SSN-Ext** | [Extensions](https://www.w3.org/TR/vocab-ssn-ext/): ObservationCollection, ActuationCollection, SamplingCollection. Aggregations of atomic observations sharing common FOI/property/procedure/sensor |
| **SOSA-OMS** (2023) | Adds classes/properties for full ISO 19156:2023 OMS conformance |

### Core classes you will use

| Class | What it is | Cytognosis example |
|---|---|---|
| `sosa:Sensor` | A device, agent, or computational procedure that observes | An Illumina NovaSeq, a Dexcom G7 CGM, a 64-channel EEG cap, an scVI inference service |
| `sosa:Observation` | An act that estimates the value of an `ObservableProperty` of a `FeatureOfInterest` | A single library sequenced; a single 5-minute glucose reading window; a single fMRI run |
| `sosa:Sample` | A subset of a FOI used as a representative; "samples are artifacts of an observational strategy and have no significant function outside their role in the observation process" | A tissue biopsy; a tube of blood; a 50 µL aliquot for proteomics |
| `sosa:Sampler` | The entity that produces Samples from a FOI | A biopsy needle, a flow cytometer pre-sort, a microdissection laser |
| `sosa:Actuator` | An entity that performs an `Actuation` to change the world | An insulin pump, a TMS coil, a CRISPR delivery system, a drug-dosing cabinet |
| `sosa:Actuation` | An act that changes the state of an `ActuatableProperty` of an FOI | An insulin bolus delivered, a CRISPR knockdown applied, a TMS pulse fired |
| `sosa:FeatureOfInterest` | The thing the world cares about, that observations are *about* | A patient, a tissue, a single cell, an organoid, a population |
| `sosa:ObservableProperty` | The property being observed | Interstitial glucose concentration, BOLD signal, gene expression of TP53, alpha-power in O1 |
| `sosa:Procedure` | A workflow/protocol/algorithm specifying how to set up an Observation, take a Sample, or perform an Actuation | A 10x Genomics 3' v3 protocol; a CGM device firmware spec; an scVI training recipe; a CRISPR guide design SOP |
| `sosa:Result` | The result of an Observation, Actuation, or Sampling | A FASTQ + count matrix; a glucose value 7.2 mmol/L; an embedding vector |
| `sosa:Platform` | An entity that hosts Sensors, Samplers, or Actuators | A patient's wrist (hosts a wearable); a sequencing facility; a clinical visit |
| `sosa:Deployment` | Process of placing a Platform/System for some Procedure | The deployment of a CGM for a 14-day study arm |
| `ssn:System` | A unit of abstraction for pieces of infrastructure that implement Procedures | A whole assay platform: instrument + reagents + analysis pipeline |

### Core relations

| Relation | Domain → Range | Example |
|---|---|---|
| `sosa:hasFeatureOfInterest` | Observation → FeatureOfInterest | An RNA-seq Observation has FOI = the tissue Sample (which `isSampleOf` the donor) |
| `sosa:observedProperty` | Observation → ObservableProperty | This Observation observed "glucose concentration" |
| `sosa:madeBySensor` | Observation → Sensor | This Observation was made by Sensor "Dexcom-G7-#834212" |
| `sosa:usedProcedure` | Observation → Procedure | Following Procedure "10x 3' v3.1 with Ensembl 111 reference" |
| `sosa:hasResult` | Observation → Result | The Result is a NegativeBinomial-distributed count vector |
| `sosa:hasSimpleResult` | Observation → literal | For value-only results: 7.2 |
| `sosa:phenomenonTime` | Observation → Time | When the thing was true in the world |
| `sosa:resultTime` | Observation → Time | When the Observation was recorded/computed |
| `sosa:isSampleOf` | Sample → FeatureOfInterest | A biopsy Sample isSampleOf a Patient |
| `sosa:hasSample` | FOI → Sample | Inverse |
| `sosa:isHostedBy` | Sensor/Sampler/Actuator → Platform | Sensor `isHostedBy` Platform |
| `sosa:observes` | Sensor → ObservableProperty | This Sensor type observes "interstitial glucose" |

### Why this matters for Cytognosis specifically

1. **Generic across modality.** A 10x Chromium run, a CGM stream, a CITE-seq experiment, an EEG session, a CRISPRi knockdown, and an scVI inference all fit under the same six relations. The bio ontologies (OBI/EFO for assay class, CL/UBERON for FOI, ChEBI/genes for ObservableProperty, UCUM/LOINC for Result type) populate the slots. This is exactly the unifying schema the matching problem needs.

2. **Sample is first-class and distinct from FOI.** A tissue biopsy is `sosa:Sample`, the patient is `sosa:FeatureOfInterest`, and `sosa:isSampleOf` makes the relationship explicit. This matches the omics workflow (donor → biopsy → dissociation → library → reads) precisely. The single-cell-curation `tissue_type` field collapses this into one slot; SOSA gives you the full chain when you need it.

3. **Actuator perspective is built in.** Cytognosis's longer-term GPS-for-Health vision implies interventions: closed-loop insulin pumps, optogenetic stimulation, scheduled drug dosing, CRISPR perturbations. SOSA's `Actuator`/`Actuation`/`ActuatableProperty` triad gives the dual to Sensor/Observation/ObservableProperty. A CGM + insulin pump system is one `ssn:System` with two co-located `sosa:Platform` instances on the same FOI. No other surveyed standard handles this as cleanly.

4. **Procedure is the bridge to ML.** A `sosa:Procedure` can be a wet-lab protocol (linked via OBI/EFO CURIE) or a computational method (linked to an EDAM Operation, an MLflow MLmodel, or an scVI checkpoint). The same predicate spans the wet-dry divide. This is where SOSA meets the Models layer of the survey.

5. **Time axis disambiguated.** `phenomenonTime` (when it was true) vs. `resultTime` (when it was recorded/derived) is exactly the longitudinal/event distinction the four sampling regimes need. ObservationCollection (SSN-Ext) groups dense series with shared FOI/Property/Procedure efficiently.

6. **W3C/OGC dual-blessed and aligned to ISO 19156:2023.** Long-term stable. Already mapped to FHIR Observation in published work (see "SOSA/SSN to FHIR" below) and to OGC O&M / OGC SensorThings API natively. The only generic observation ontology with this level of standardization.

### Validation: SOSA-SHACL

[SOSA-SHACL](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235) provides W3C SHACL shapes that validate whether a knowledge graph conforms to SOSA semantics. Sub-shapes for sensor, observation, sample, FOI, etc. Composes with LinkML-emitted SHACL for Cytognosis-specific constraints layered on top. This gives a clean two-layer validation story: SOSA-SHACL for "is this even a valid observation?", Cytognosis-SHACL for "is this a valid Cytognosis-specific observation in our profile?".

### SOSA/SSN ↔ FHIR alignment

A published [mobile health monitoring system, BMC Med Inform Decis Mak 2019](https://link.springer.com/article/10.1186/s12911-019-0806-z) and the [IoMT interoperability work, SAGE 2020](https://journals.sagepub.com/doi/full/10.1177/1550147719889591) both demonstrate the SOSA → FHIR mapping pattern:

| SOSA | FHIR |
|---|---|
| `sosa:Sensor` (when a physical device) | `Device` |
| `sosa:Observation` | `Observation` |
| `sosa:FeatureOfInterest` | `Patient`, `Specimen`, `BodyStructure` |
| `sosa:Sample` | `Specimen` |
| `sosa:Actuator` | `Device` (with role) |
| `sosa:Actuation` | `Procedure`, `MedicationAdministration` |
| `sosa:ObservableProperty` | `Observation.code` (LOINC) |
| `sosa:hasResult` | `Observation.value[x]` |
| `sosa:phenomenonTime` | `Observation.effective[x]` |
| `sosa:resultTime` | `Observation.issued` |
| `sosa:Procedure` (the protocol) | `PlanDefinition`, `ActivityDefinition`, `Procedure.basedOn` |
| `sosa:usedProcedure` | `Observation.method` |
| `sosa:Platform` (the patient's body) | `Patient` (when host is the patient) |
| `ssn:System` (the assay platform) | `DeviceDefinition` + `HealthcareService` |

The mapping is not bijective (FHIR carries clinical context SOSA does not, and SOSA carries provenance abstractions FHIR does not), but it is good enough for round-trip ingestion. For Cytognosis, the practical implication: **author Cytognosis observation manifests in SOSA**, and emit FHIR Observation resources at the boundary with clinical systems via deterministic projection.

### SOSA/SSN ↔ OGC O&M / SensorThings / SensorML

- [OGC SensorThings API](https://www.ogc.org/standards/sensorthings/) is the REST/JSON instantiation. Its data model is a simplification of O&M and aligns to SOSA via the [W3C alignment to O&M](https://www.w3.org/2015/spatial/wiki/Alignment_to_O&M) work. SensorThings is the right serving layer for ongoing-continuous IoT/wearable streams.
- [OGC SensorML](https://www.ogc.org/standards/sensorml/) describes the *internal process structure* of a sensor: input/output ports, processing chains, calibration. SOSA points at SensorML descriptions via custom URIs. SensorML is the right place to capture instrument-internal pipeline detail when it matters (e.g., for a custom electrode array).
- ISO 19156:2023 OMS is the underlying conceptual model SOSA-OMS conforms to.

### SOSA/SSN ↔ OBO Foundry bio ontologies

The principle is **SOSA gives the verbs, OBO gives the nouns**:

```turtle
:obs1 a sosa:Observation ;
  sosa:madeBySensor :illumina_novaseq_42 ;
  sosa:usedProcedure :proc_10x_3prime_v3 ;
  sosa:hasFeatureOfInterest :biopsy_2026_04_03_subj_038 ;
  sosa:observedProperty <http://purl.obolibrary.org/obo/GO_0010467> ;  # gene expression
  sosa:hasResult :result_count_matrix_x ;
  sosa:phenomenonTime :time_2026_04_03_14_22 ;
  sosa:resultTime :time_2026_04_05_09_18 .

:proc_10x_3prime_v3 a sosa:Procedure ;
  rdfs:label "10x Genomics Chromium 3' v3.1" ;
  dcterms:conformsTo <http://www.ebi.ac.uk/efo/EFO_0009922> ;  # 10x 3' v3 (EFO)
  cytognosis:referenceGenome "Ensembl 111" ;
  cytognosis:featureManifestSha256 "0xdeadbeef..." .

:biopsy_2026_04_03_subj_038 a sosa:Sample, fhir:Specimen ;
  sosa:isSampleOf :subj_038 ;
  obi:has_role <http://purl.obolibrary.org/obo/OBI_0100051> ;
  cytognosis:tissueOntologyTermId <http://purl.obolibrary.org/obo/UBERON_0002107> ;  # liver
  cytognosis:diseaseOntologyTermId <http://purl.obolibrary.org/obo/MONDO_0007254> .

:subj_038 a sosa:FeatureOfInterest, fhir:Patient ;
  cytognosis:organismOntologyTermId <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  cytognosis:developmentStage <http://purl.obolibrary.org/obo/HsapDv_0000087> .
```

That same template, with different OBO term bindings, describes a CGM reading, an EEG epoch, a fMRI run, or a scVI inference run.

### Recommendation

**Use SOSA/SSN as the upper-layer observation grammar for every Cytognosis sensor/assay registration.** Bind the bio-specific ontologies (OBI, BAO, EFO, CL, UBERON, NCBITaxon, MONDO, HP, ChEBI, SO, GO) into SOSA's `Procedure`, `FeatureOfInterest`, `Sample`, `ObservableProperty`, and `Result` slots via Bioregistry-validated CURIEs. Validate at ingestion with SOSA-SHACL plus a Cytognosis-LinkML-emitted SHACL profile. Project to FHIR/OMOP/CDISC at the boundary with clinical systems and to SensorThings/SensorML at the boundary with IoT/wearable telemetry.

The remaining sections of this document are the *bindings* into SOSA's slots: section 1 fills the Procedure/Assay axis, section 2 fills FeatureOfInterest and Sample, section 3 fills Result and ObservableProperty type, section 4 fills temporal regime, section 5 fills the contextual events around the Observation.

## 1. Assay class: what kind of measurement is this?

This populates `sosa:Procedure` (the protocol) and informs `sosa:madeBySensor` (the instrument class).

### OBI (Ontology for Biomedical Investigations)

[OBI](https://obi-ontology.org/) defines >2500 terms covering assays, devices, planned processes, study designs, and measurement objectives. It is OBO-Foundry compliant and is the upper-level reference for any biomedical investigation. OBI terms are the right anchor for "this is an assay measuring X with method Y". Examples: `OBI:0000895` (RNA-seq assay), `OBI:0001271` (RNA-seq via Illumina).

### BAO (BioAssay Ontology)

[BAO](https://bioregistry.io/bao) was originally built for high-throughput screening. Its five-axis decomposition is widely useful even outside HTS:

1. Perturbagen (small molecule, siRNA, CRISPR guide, antibody, environmental factor)
2. Format (cell-based, biochemical, organism-based, in vivo)
3. Detection method (fluorescence, luminescence, radiometric, label-free)
4. Physicochemical signal (absorbance, mass, electrical impedance, image)
5. Biological meta-target (the proximal vs. distal target the readout reports on)

This is a more disciplined decomposition than OBI offers and pairs well with it. [Recent 2025 work](https://link.springer.com/article/10.1186/s13326-025-00342-5) extended BAO into PK/PD and safety pharmacology, expanding its utility to translational settings.

### EFO (Experimental Factor Ontology)

[EFO](https://www.ebi.ac.uk/efo/) integrates UBERON, ChEBI, CL, and others into one application ontology used by EBI databases (Expression Atlas, GWAS catalog, Open Targets) and accepted as a source for MIxS standards. It is the right anchor for "experimental factors", i.e., the variables that change across conditions in a study (timepoint, dose, treatment, genotype).

### MIxS, MIAME, and the "Minimum Information" family

[MIxS](https://genomicsstandardsconsortium.github.io/mixs/) is the GSC's umbrella for "Minimum Information about any (X) Sequence", with checklists for human-associated, soil, marine, plant-associated, etc. MIAME (microarray), MINSEQE (sequencing), and MIRAGE (glycomics) follow the same pattern. These are reporting checklists (what *must* be present), not data structures. They feed into ISA-Tab and into EFO as field constraints.

### single-cell-curation 7.x assay_ontology_term_id

The CZ CELLxGENE [single-cell-curation schema](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html) requires `assay_ontology_term_id` populated with an EFO or OBI CURIE that resolves to a known assay class (e.g., `EFO:0009922` 10x 3' v3, `EFO:0030059` Slide-seqV2). This is the most pragmatic working example of "assay class as a typed field".

### Recommendation for assay class

For each Cytognosis assay registration:

- **Primary**: an EFO or OBI CURIE for the canonical assay class. EFO when an EFO term exists (covers most omics in practice); OBI otherwise.
- **Secondary** (when applicable, especially for screening/perturbational): BAO terms across the five axes.
- **Validate** at registration time against the [single-cell-curation accepted assay list](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html) for omics, and against custom Cytognosis enumerations for non-omics.

## 2. Entity being measured: FeatureOfInterest and Sample

In SOSA terms, this section fills `sosa:FeatureOfInterest` and `sosa:Sample`. The FOI is the entity the world cares about (a patient, a population, an organoid line); the Sample is the artifact the assay actually touches (a biopsy, a blood tube, a coverslip). For assays where the FOI *is* the assay target without intermediation (e.g., an EEG on a living person), there is no separate Sample.

The "what is the sample" question is where the OBO Foundry shines. Use the following stack:

| Question | Ontology | Example |
|---|---|---|
| Species | NCBITaxon | `NCBITaxon:9606` (human) |
| Tissue / organ | UBERON | `UBERON:0002107` (liver) |
| Cell type | CL (Cell Ontology) | `CL:0000236` (B cell) |
| Cell line | CLO (Cell Line Ontology) | `CLO:0009474` (HEK293T) |
| Disease / condition | MONDO | `MONDO:0007254` (breast cancer) |
| Phenotype | HP (Human Phenotype Ontology) | `HP:0001250` (seizure) |
| Sex / development | PATO + UBERON developmental stages | `PATO:0000383` (female) |
| Donor and consent | DUO (Data Use Ontology) | `DUO:0000004` (no restriction) |
| Anatomical context for spatial assays | UBERON + region-specific (DHBA, FMA fragments) | `UBERON:0002416` (integument) |

The single-cell-curation schema again is the live reference for combining these correctly: `tissue_type`, `tissue_ontology_term_id`, `cell_type_ontology_term_id`, `disease_ontology_term_id`, `organism_ontology_term_id`, `development_stage_ontology_term_id`, `self_reported_ethnicity_ontology_term_id`, `sex_ontology_term_id`. Replicate this list for any Cytognosis sample-level annotation.

For *non-cellular* sample types (a BOLD timecourse from a brain region, an ECG strip, a CGM trace), UBERON anchors anatomy and the modality-specific data structure (BIDS, FHIR Specimen, OMOP DEVICE) carries the rest.

## 3. Value semantics: unit, range, scale, type

### UCUM (Unified Code for Units of Measure)

[UCUM](https://www.hl7.org/fhir/valueset-ucum-units.html) is the canonical unit vocabulary, with formal syntactic rules (so `mg/dL`, `mmol/L`, `1/min` parse cleanly) and dimensional analysis. It is the unit system inside FHIR Observation, OMOP, and most clinical schemas. The FHIR value set contains >1000 codes from `unitsofmeasure.org`.

For non-clinical bio data (count matrices, fluorescence intensities, embedding coordinates), UCUM may be overkill but is rarely wrong. For arbitrary "model output" fields (a 50-D embedding) the unit is `1` (dimensionless) and the semantics live in the model card, not the unit field.

### LOINC

[LOINC](https://loinc.org/) gives the *what is being measured* code (e.g., `4548-4` Hemoglobin A1c). FHIR Observation pairs `code` (LOINC) with `valueQuantity.unit` (UCUM). For Cytognosis, LOINC is the right code for any clinical-style readout (lab panels, vitals).

### SNOMED CT

For findings, procedures, and conditions, SNOMED CT is the most expressive vocabulary, but heavyweight and licensed. Use when OMOP/FHIR pipelines require it; otherwise prefer MONDO + HP for diseases and phenotypes.

### Type, range, and scale

For non-clinical readouts, the LinkML pattern is:
- `value_type`: integer / float / boolean / categorical / ordinal / text
- `unit`: UCUM CURIE (or `1` for dimensionless)
- `range_min` / `range_max` / `precision`
- `transformation`: identity / log1p / clr / ilr / arcsinh
- `missing_value_encoding`: NaN / 0 / sentinel

This is straightforward but always custom; LinkML lets you author it once and emit JSON Schema, SHACL, and Python validators.

### Recommendation for value semantics

UCUM for unit, LOINC for the readout code where applicable, MONDO/HP for clinical phenotypes, plus a LinkML-authored `MeasurementValueSpec` class with `value_type`, `unit`, `range`, and `transformation`. Validate all four together at ingestion.

## 4. Sampling regime

The four regimes the user identified each have different best-fit standards.

### Snapshot (single point in time)

Most omics assays. The data structure is a single AnnData-style matrix or a single FHIR Observation with `effectiveDateTime`. ISA-Tab's Investigation/Study/Assay model captures the experimental hierarchy. OMOP captures it as MEASUREMENT or OBSERVATION rows with a `_datetime` column.

### Periodic (regular repeated snapshots)

Annual labs, quarterly clinical reviews, weekly imaging. FHIR Observation handles each instance; the *schedule* is encoded outside the observation (CarePlan, ResearchStudy). For research, ISA-Tab can encode multiple Studies under one Investigation. OMOP handles this naturally with multiple MEASUREMENT rows per person_id.

### Bounded continuous (a session of dense sampling)

EEG, fMRI, MEG, gait analysis, eye tracking, motion capture. This is BIDS territory.

[BIDS 1.11+](https://bids-specification.readthedocs.io/en/stable/) (the Brain Imaging Data Structure) is the dominant standard. It defines a directory layout, file naming, and JSON sidecars per modality. Modalities currently covered:
- MRI (anat, func, dwi, fmap, perf)
- EEG, MEG, iEEG
- PET
- Microscopy (Microscopy-BIDS, 2022)
- MRS (MRS-BIDS, 2025) [Sci Data 2025](https://www.nature.com/articles/s41597-025-05543-2)
- NIRS (NIRS-BIDS, 2025)
- Behavioral, Motion, Physio (cardiac/respiratory tied to neuroimaging runs)

Each modality's events are described in `*_events.tsv` files, with optional HED tags.

### Ongoing continuous (open-ended monitoring)

CGM, wearables, ambient sensors, ICU telemetry. BIDS does not cover this. The right standards are:

- **Open mHealth**: [openmhealth.org](https://www.openmhealth.org/) defines JSON schemas for heart rate, step count, sleep, blood glucose, etc., and is now an IEEE standard. Maps cleanly to FHIR Observation via [OpenmHealthtoFHIR](https://healthedata1.github.io/mFHIR/).
- **FHIR Observation** (with `effectivePeriod`, `Component`, `referenceRange`) for clinical-grade readouts. Use FHIR Specimen for biospecimens.
- **OGC SensorThings API** (REST/JSON, MQTT-friendly): [OGC SensorThings](https://www.ogc.org/standards/sensorthings/) for IoT/environmental telemetry.
- **OGC SensorML / O&M (Observations and Measurements)**: [SensorML](https://www.ogc.org/standards/sensorml/) for sensor system description, O&M for the observation payload. More prevalent in environmental and earth-observation work but cleanly applicable to biomedical IoT.
- **DICOM Supplement 30**: [DICOM Waveform](https://dicom.nema.org/dicom/supps/sup30_lb.pdf) for ECG, EEG, hemodynamics in clinical settings.
- **Apple HealthKit / Google Health Connect / Garmin FIT**: vendor formats; treat as raw inputs that get mapped into Open mHealth + FHIR.

### Recommendation for sampling regime

| Regime | Primary standard | Secondary |
|---|---|---|
| Snapshot omics | AnnData/MuData with single-cell-curation 7.x metadata | ISA-Tab for the surrounding study |
| Snapshot clinical | FHIR Observation | OMOP MEASUREMENT |
| Periodic | OMOP CDM v5.4 | FHIR ResearchStudy + Observation series |
| Bounded continuous neuro | BIDS 1.11+ with modality extension | NWB (Neurodata Without Borders) for electrophysiology |
| Bounded continuous imaging | OME-NGFF / OME-Zarr | DICOM for clinical |
| Ongoing continuous wearable | Open mHealth + FHIR Observation | Apple HealthKit/HealthConnect raw |
| Ongoing continuous IoT | OGC SensorThings | SensorML for the device, O&M for data |
| Continuous clinical waveform | DICOM Sup 30 | EDF+ for legacy ECG/EEG |

## 5. Event and context annotation

This is what HED solves for neuroimaging and what is largely an open problem elsewhere.

### HED (Hierarchical Event Descriptors)

[HED](https://www.hedtags.org/) is a controlled, hierarchical tag vocabulary for annotating events. The HED Standard Schema [v5 was released June 2025](https://zenodo.org/records/15571221), and HED is a [BIDS extension](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html). HED tags compose ("Action/Reach, Item/Object/Tool, Relation/Spatial-relation/Below"), validate against the schema, and support custom *library schemas* for domains. The [HED LANG library](https://www.nature.com/articles/s41597-024-04282-0) extends HED for language cognition; the [HED EEG library](https://www.nature.com/articles/s41597-025-05791-2) extends it for EEG-specific events. Library extensions are how you bring HED into a new domain (cellular perturbations, drug exposures, behavioral schedules).

### Alternatives outside neuroimaging

- **OBI Planned Process** + OBI study design terms: cleaner for "the experimental design", less rich for moment-to-moment events.
- **FHIR Encounter / Procedure / MedicationAdministration**: clinically standard, less expressive about timing and composition.
- **OMOP DRUG_EXPOSURE / PROCEDURE_OCCURRENCE**: same.
- **W3C Time Ontology**: the formal substrate for any of these, but rarely used directly.

### Recommendation for event/context

- **Bounded continuous neuro**: BIDS `events.tsv` with HED tags from the standard schema + a Cytognosis HED library extension when needed.
- **Cellular perturbation experiments**: OBI Planned Process + a LinkML `Perturbation` class referencing ChEBI (compounds), CHEBI/NCBIGENE (targets), `OGG` (genes), and BAO perturbagen taxonomy. Eventually consider proposing a HED-Bio library.
- **Clinical**: FHIR Encounter/Procedure tied to Observations.

## Combined: what an "observation manifest" looks like (SOSA-aligned)

A LinkML-authored `ObservationManifest`, modeling each entry as a `sosa:Observation` with bio-ontology CURIEs in the slots:

```yaml
# A single Observation (or ObservationCollection for series)
id: cytognosis.obs:0001
type: sosa:Observation                         # or sosa:ObservationCollection (SSN-Ext) for time series

# What was observed and about what
observed_property:                             # sosa:observedProperty
  curie: GO:0010467                            # gene expression (or LOINC for clinical)
  label: "gene expression"
feature_of_interest:                           # sosa:hasFeatureOfInterest
  type: sosa:FeatureOfInterest                 # also a fhir:Patient where applicable
  organism: NCBITaxon:9606                     # NCBITaxon
  tissue: UBERON:0002107                       # UBERON  (when FOI is the donor's tissue *in situ*)
  cell_type: CL:0000236                        # CL (only when FOI is a cell population)
  disease: MONDO:0007254                       # MONDO
  development_stage: HsapDv:0000087            # development stage
  sex: PATO:0000383
  donor_id: opaque
sample:                                        # sosa:hasSample / sosa:isSampleOf
  type: sosa:Sample                            # also fhir:Specimen where applicable
  is_sample_of: <feature_of_interest.id>
  obi_role: OBI:0100051                        # specimen role
  collected_at: 2026-04-03T14:22:00Z
  preservation: snap_frozen
  cell_type: CL:0000236                        # populated when sample is dissociated to specific cell pop

# How it was observed
sensor:                                        # sosa:madeBySensor
  type: sosa:Sensor
  device_class: EFO:0009922                    # 10x 3' v3 (EFO)
  instance: "novaseq-x-#42"                    # specific physical or logical sensor
  hosted_by_platform: "lab-genomics-core"      # sosa:isHostedBy → sosa:Platform
procedure:                                     # sosa:usedProcedure
  type: sosa:Procedure
  conforms_to: EFO:0009922                     # 10x 3' v3
  obi_assay: OBI:0001271                       # RNA-seq via Illumina
  bao_axes:                                    # only when relevant (HTS/perturbation work)
    perturbagen: BAO:...
    format: BAO:...
    detection_method: BAO:...
    signal: BAO:...
    meta_target: BAO:...
  reference_genome: ensembl:111
  feature_manifest_sha256: 0xdeadbeef...       # canonical feature axis pin
  protocol_doc: "ro-crate:.../protocol.md"

# What came out
result:                                        # sosa:hasResult
  type: cytognosis:CountMatrixResult           # subclasses sosa:Result
  storage_uri: s3://cytognosis-data/.../obs1.zarr
  in_memory_format: AnnData
  value_semantics:
    X:
      value_type: int                          # raw counts
      unit: "1"                                # UCUM dimensionless
      transformation: identity
      missing_value_encoding: null
    layers.normalized:
      value_type: float
      unit: "1"
      transformation: log1p_cp10k
  shape:
    n_obs: 4821
    n_vars: 38244
  output_distribution_class: NegativeBinomial   # when applicable (model-emitted observations)

# When
phenomenon_time:                               # sosa:phenomenonTime - when it was true
  start: 2026-04-03T14:22:00Z
  end: 2026-04-03T14:32:00Z
result_time: 2026-04-05T09:18:00Z              # sosa:resultTime - when recorded/derived
sampling_regime: snapshot                      # snapshot | periodic | bounded_continuous | ongoing_continuous
sampling_rate: null                            # for continuous regimes only
duration_seconds: 600

# Context
context:
  investigation: cytognosis.study:0042         # ISA Investigation or fhir:ResearchStudy ref
  study_arm: discovery_cohort
  events:                                      # BIDS events.tsv path or HED tag list or FHIR Encounter
    bids_events_tsv: null
    hed_tags: null
    fhir_encounter: ref
  actuations_co_observed:                      # for closed-loop or perturbation experiments
    - cytognosis.act:0123                      # links to a sosa:Actuation manifest (e.g., a CRISPR knockdown)

# Provenance
provenance:
  prov_o: ...                                  # W3C PROV
  ro_crate: s3://cytognosis-data/.../ro-crate-metadata.json
  generated_by_workflow: nf-core/scrnaseq:2.6.0
license: CC-BY-4.0
access:
  duo_codes: [DUO:0000004]
  controlled: false
```

For an Actuation (closed-loop or perturbation experiments), a parallel `ActuationManifest` mirrors the structure with `sosa:Actuator`, `sosa:actuatedProperty`, `sosa:hadActuator`, and `sosa:hasResult`. The platform's match function treats Observation manifests and Actuation manifests symmetrically.

This is the schema the model-input contract validates against at match time. The cleanest implementation: author this once in LinkML, generate JSON Schema for runtime validation, generate SHACL for graph-level validation, and inherit SOSA's own SHACL shapes ([SOSA-SHACL](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235)) for free at the upper layer. Project to FHIR Observation/Procedure resources at the clinical boundary, to SensorThings entities at the IoT boundary, and to a HuggingFace dataset card YAML for the ML boundary.

## Sources

- [SOSA / SSN W3C Recommendation](https://www.w3.org/TR/vocab-ssn/), [SSN 2023 Edition](https://www.w3.org/TR/vocab-ssn-2023/), [SSN-Ext (Extensions)](https://www.w3.org/TR/vocab-ssn-ext/), [SDW-SOSA-SSN repo](https://github.com/w3c/sdw-sosa-ssn/), [2023 Edition source](https://w3c.github.io/sdw-sosa-ssn/ssn/)
- [SOSA paper, J. Web Semantics 2018, arXiv 1805.09979](https://arxiv.org/abs/1805.09979), [SOSA/SSN Semantic Web J.](https://www.semantic-web-journal.net/system/files/swj1804.pdf)
- [SOSA at OGC](https://www.ogc.org/standards/semantic-sensor-network-ontology/), [Alignment to O&M (W3C)](https://www.w3.org/2015/spatial/wiki/Alignment_to_O&M), [ISO 19156:2023](https://www.iso.org/standard/82463.html)
- [SOSA-SHACL paper, IJCKG 2021](https://dl.acm.org/doi/fullHtml/10.1145/3502223.3502235)
- [SSN + FHIR mobile health, BMC Med Inform Decis Mak 2019](https://link.springer.com/article/10.1186/s12911-019-0806-z), [IoMT interoperability via SSN, SAGE 2020](https://journals.sagepub.com/doi/full/10.1177/1550147719889591)
- [OBI](https://obi-ontology.org/), [OBI on OBO Foundry](http://obofoundry.org/ontology/obi.html)
- [BAO paper](https://link.springer.com/article/10.1186/1471-2105-12-257), [BAO on Bioregistry](https://bioregistry.io/bao), [BAO PK/PD extension 2025](https://link.springer.com/article/10.1186/s13326-025-00342-5)
- [EFO](https://www.ebi.ac.uk/efo/), [EFO repo](https://github.com/EBISPOT/efo)
- [MIxS / GSC](https://genomicsstandardsconsortium.github.io/mixs/)
- [ISA Tools](https://isa-tools.org/), [ISA spec](https://isa-specs.readthedocs.io/en/latest/isamodel.html), [ISA API paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8444265/)
- [BIDS spec](https://bids-specification.readthedocs.io/en/stable/), [BIDS site](https://bids.neuroimaging.io/), [EEG-BIDS Sci Data 2019](https://www.nature.com/articles/s41597-019-0104-8), [iEEG-BIDS](https://www.nature.com/articles/s41597-019-0105-7), [MRS-BIDS 2025](https://www.nature.com/articles/s41597-025-05543-2)
- [HED site](https://www.hedtags.org/), [HED v5 schema 2025](https://zenodo.org/records/15571221), [HED in BIDS](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html), [HED EEG library 2025](https://www.nature.com/articles/s41597-025-05791-2), [HED LANG 2024](https://www.nature.com/articles/s41597-024-04282-0)
- [single-cell-curation latest](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html)
- [FHIR Observation](https://hl7.org/fhir/observation.html), [FHIR UCUM units value set](https://www.hl7.org/fhir/valueset-ucum-units.html)
- [Open mHealth](https://www.openmhealth.org/), [OpenmHealth on FHIR](https://healthedata1.github.io/mFHIR/), [Wearable mapping paper](https://pubmed.ncbi.nlm.nih.gov/37387034/)
- [OMOP CDM](https://ohdsi.github.io/CommonDataModel/), [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html)
- [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm), [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam)
- [OGC SensorML](https://www.ogc.org/standards/sensorml/), [OGC SensorThings](https://www.ogc.org/standards/sensorthings/), [OGC SWE overview](https://docs.ogc.org/wp/07-165r1/)
- [DICOM](https://www.dicomstandard.org/), [DICOM Sup 30 Waveform](https://dicom.nema.org/dicom/supps/sup30_lb.pdf)
