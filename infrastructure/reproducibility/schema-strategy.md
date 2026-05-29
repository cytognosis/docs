<!-- Last updated: 2026-05-22 | Source: Plans/design/11_reproducibility_strategy/ -->
**← [Back to Reproducibility Index](README.md)**

# 01 — Schema Strategy

**Reading order**: read `00_master_strategy.md` §4 first; this file expands that section.

This document defines: where every schema lives, which standards each schema profiles, how LinkML compiles into the formats consumers need, and how the FAIRDOM / ISA / RO-Crate / Bioschemas ecosystem snaps in as profiles rather than parallel schemas.

---

## 1. The hub: cytoskeleton/schemas/

Schemas were authored in cytos (`cytos/schemas/`) but the master plan moves them upstream to `cytoskeleton/schemas/` in Phase 1. The post-move layout is:

```
cytoskeleton/schemas/
├── core/
│   ├── core.yaml                   # shared LinkML types + mixins
│   ├── prefixes.yaml               # bioregistry-aligned CURIE prefixes
│   └── ro_crate_mixin.yaml         # HasROCrateMetadata mixin (conforms_to, sd_publisher, cite_as, …)
├── domains/                        # the existing Cytos LinkML domain files
│   ├── anatomy.yaml · disease.yaml · gene.yaml · variant.yaml · drug.yaml · phenotype.yaml
│   ├── expression.yaml · pathway.yaml · publication.yaml · clinical.yaml · taxonomy.yaml
│   ├── environment.yaml · evidence.yaml · scholarly.yaml · genomics.yaml · person.yaml
│   ├── sensor.yaml (legacy) · sensor/ (universal sensor submodule)
│   ├── nwb.yaml · ga4gh.yaml · biothings.yaml · annotation.yaml
│   ├── cellline.yaml · device.yaml · behavior.yaml · exposure.yaml · geography.yaml
│   └── measurement.yaml · population.yaml · agent.yaml · dataset.yaml · topic.yaml
├── profiles/                       # NEW: schema profiles for external standards
│   ├── isa.yaml                    # ISA Abstract Model (Investigation/Study/Assay/Process/Material/Data)
│   ├── ro_crate.yaml               # RO-Crate 1.2 root + metadata descriptor
│   ├── workflow_ro_crate.yaml      # Workflow RO-Crate 1.0
│   ├── workflow_run_crate.yaml     # Workflow Run Crate + Provenance Run Crate
│   ├── process_run_crate.yaml      # Process Run Crate
│   ├── five_safes_crate.yaml       # Five Safes RO-Crate (TRE-FX)
│   ├── bioschemas/
│   │   ├── computational_workflow.yaml
│   │   ├── formal_parameter.yaml
│   │   ├── dataset.yaml
│   │   └── tool.yaml
│   ├── sosa_ssn.yaml               # W3C SOSA/SSN
│   ├── fhir_r5.yaml                # FHIR R5 subset (Observation, Device, DeviceMetric, DeviceUsage)
│   ├── ga4gh/
│   │   ├── phenopackets.yaml
│   │   ├── vrs.yaml                # Variant Representation
│   │   ├── drs.yaml                # Data Repository Service
│   │   └── trs.yaml                # Tool Registry Service
│   ├── codemeta.yaml               # CodeMeta + CITATION.cff
│   ├── datasheet.yaml              # Datasheets for Datasets (Gebru et al.)
│   ├── model_card.yaml             # Model Card (Mitchell et al.)
│   └── dmp.yaml                    # NIH/NSF/Horizon Europe DMP common core
├── enums/                          # validation enums backed by ontology codes
│   ├── mondo.yaml · hp.yaml · cl.yaml · uberon.yaml · efo.yaml
│   ├── hancestro.yaml · pato.yaml · go.yaml · chebi.yaml
│   └── spdx_licenses.yaml
├── mappings/
│   ├── sssom/                      # SSSOM mapping tables
│   └── _provenance/                # mapping provenance sidecars
├── codegen/                        # cached generated outputs (gitignored except .gitkeep)
│   ├── pydantic/
│   ├── jsonschema/
│   ├── owl/
│   ├── shacl/
│   ├── graphql/
│   ├── sql/
│   ├── markdown/
│   └── typescript/
└── README.md
```

Cytos and other consumers reference these as `external/cytoskeleton/schemas/...` via submodule (per Phase 6 of the master plan).

---

## 2. ISA Abstract Model as a LinkML profile

The ISA Abstract Model (https://isa-specs.readthedocs.io/en/latest/isamodel.html) has 12 core entities. Here is each one as a LinkML class. The profile imports `core/core.yaml` and uses `class_uri` + `slot_uri` so a generated JSON serializer round-trips with ISA-JSON.

```yaml
# profiles/isa.yaml (excerpt — full schema is ~600 lines)
id: https://w3id.org/cytognosis/cytoskeleton/profiles/isa
name: cytognosis_isa
title: ISA Abstract Model as a LinkML profile
license: https://www.apache.org/licenses/LICENSE-2.0

imports:
  - linkml:types
  - ../core/core
  - ../core/ro_crate_mixin

prefixes:
  isa: https://w3id.org/cytognosis/isa/
  obo: http://purl.obolibrary.org/obo/
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#

default_prefix: isa

classes:
  Investigation:
    class_uri: schema:Project
    description: ISA top-level Investigation grouping multiple Studies.
    mixins:
      - HasROCrateMetadata
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      title:
        range: string
        required: true
      description:
        range: string
      submission_date:
        range: date
      public_release_date:
        range: date
      ontology_source_references:
        range: OntologySource
        multivalued: true
      publications:
        range: Publication
        multivalued: true
      contacts:
        range: Contact
        multivalued: true
      studies:
        range: Study
        multivalued: true
        required: true
        inlined_as_list: true

  Study:
    class_uri: schema:Dataset
    mixins:
      - HasROCrateMetadata
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      title:
        range: string
      description:
        range: string
      submission_date:
        range: date
      public_release_date:
        range: date
      design_descriptors:
        range: OntologyAnnotation
        multivalued: true
      factor_name:
        range: string
      factor_type:
        range: OntologyAnnotation
      publications:
        range: Publication
        multivalued: true
      contacts:
        range: Contact
        multivalued: true
      protocols:
        range: Protocol
        multivalued: true
      sources:
        range: Source
        multivalued: true
      samples:
        range: Sample
        multivalued: true
      processes:
        range: Process
        multivalued: true
      assays:
        range: Assay
        multivalued: true

  Assay:
    class_uri: schema:LabProtocol
    mixins:
      - HasROCrateMetadata
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      measurement_type:
        range: OntologyAnnotation
        required: true
      technology_type:
        range: OntologyAnnotation
        required: true
      technology_platform:
        range: string
      protocol_used:
        range: Protocol
      inputs:
        range: Material
        multivalued: true
        required: true
      outputs:
        range: Material
        multivalued: true
        required: true
      processes:
        range: Process
        multivalued: true
      data_files:
        range: Data
        multivalued: true

  Protocol:
    class_uri: schema:HowTo
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      name:
        range: string
        required: true
      protocol_type:
        range: OntologyAnnotation
      description:
        range: string
      uri:
        range: uri
      version:
        range: string
      parameters:
        range: ProtocolParameter
        multivalued: true

  Material:
    abstract: true
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      name:
        range: string
      characteristics:
        range: Characteristic
        multivalued: true
      material_type:
        range: OntologyAnnotation

  Source:
    is_a: Material
    description: Starting biological material; appears only in Study graphs.
    class_uri: obo:NCIT_C16631
    slot_usage:
      material_type:
        required: true

  Sample:
    is_a: Material
    description: Major output of a sampling Process.
    class_uri: obo:OBI_0000747

  Data:
    description: Output of a data-producing Process.
    class_uri: schema:DigitalDocument
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      file_name:
        range: string
        required: true
      encoding_format:
        range: string
      content_hash:
        range: string
        description: sha256 of the file content (hex)
      content_size_bytes:
        range: integer

  Process:
    description: Application of a protocol producing outputs from inputs (DAG node).
    class_uri: prov:Activity
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      protocol:
        range: Protocol
        required: true
      parameter_values:
        range: ParameterValue
        multivalued: true
      performer:
        range: string
      date:
        range: datetime
      inputs:
        range: Material
        multivalued: true
      outputs:
        range: Material
        multivalued: true
      previous_process:
        range: Process
      next_process:
        range: Process

  OntologyAnnotation:
    attributes:
      term:
        range: string
      term_source:
        range: OntologySource
      term_accession:
        range: uriorcurie

  OntologySource:
    attributes:
      name:
        range: string
        required: true
      file:
        range: uriorcurie
      version:
        range: string
      description:
        range: string

  Unit:
    is_a: OntologyAnnotation

  Publication:
    class_uri: schema:ScholarlyArticle
    attributes:
      pubmed_id:
        range: string
      doi:
        range: uri
      author_list:
        range: string
        multivalued: true
      title:
        range: string
      status:
        range: OntologyAnnotation

  Contact:
    class_uri: schema:Person
    attributes:
      name:
        range: string
        required: true
      email:
        range: string
      phone:
        range: string
      address:
        range: string
      affiliation:
        range: string
      orcid:
        range: uriorcurie
      roles:
        range: OntologyAnnotation
        multivalued: true

  # supporting types
  Characteristic:
    attributes:
      category:
        range: OntologyAnnotation
      value:
        range: string
      unit:
        range: Unit

  ProtocolParameter:
    attributes:
      parameter_name:
        range: OntologyAnnotation

  ParameterValue:
    attributes:
      category:
        range: ProtocolParameter
      value:
        range: string
      unit:
        range: Unit
```

### 2.1 Validators beyond LinkML

The Process graph must be a DAG (per ISA spec). LinkML's structural validation doesn't enforce acyclicity. We add a custom validator in `src/cytoskeleton/isa/validate.py` that:

1. Builds a graph from Process / Material / Data nodes.
2. Verifies all edges are typed (Process → Material/Data; Material/Data → Process).
3. Verifies no cycles (NetworkX `is_directed_acyclic_graph`).
4. Verifies Study graphs have Source → Process → Sample pattern (with split/pool tolerated).
5. Verifies Assay graphs have Sample → Process → (Material|Data)+ pattern.

This is invoked by `nox -s schemas_validate` and `cytoskeleton run` before any pipeline execution.

### 2.2 ISA-JSON round-trip

`cytoskeleton.isa.serialize.to_isa_json(investigation)` walks the LinkML instance and produces ISA-JSON conformant with the official schema at https://github.com/ISA-tools/isa-api/tree/develop/isatools/resources/schemas/isa_model_version_1_0_schemas.

`cytoskeleton.isa.parse.from_isa_json(json)` reverses the direction. Round-trip tests guarantee structural equality.

### 2.3 SEEK ISA-JSON-compliant Experiments

Per `docs.seek4science.org/help/user-guide/isa-json-compliant-experiment.html`, SEEK accepts ISA-JSON-compliant Investigations with structured Studies, Assay Streams, Assays, Sample Types, and Experiment Sample Templates. Our LinkML ISA profile produces exactly this shape, so `cytoskeleton publish --to seek` posts the ISA-JSON directly to a SEEK instance's REST endpoint.

---

## 3. RO-Crate family as LinkML profiles

RO-Crate is JSON-LD with a flat `@graph` and a metadata file descriptor. The four working profiles get LinkML mirrors.

### 3.1 RO-Crate root (1.2)

```yaml
# profiles/ro_crate.yaml (excerpt)
id: https://w3id.org/cytognosis/cytoskeleton/profiles/ro_crate
name: ro_crate_profile
prefixes:
  rocrate: https://w3id.org/ro/crate/1.2/
  schema: http://schema.org/

classes:
  ROCrate:
    description: RO-Crate root entity (./)
    class_uri: schema:Dataset
    mixins:
      - HasROCrateMetadata
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      name:
        range: string
        required: true
      description:
        range: string
      conforms_to:
        range: uriorcurie
        multivalued: true
        required: true
      date_published:
        range: date
      license:
        range: License
        required: true
      creator:
        range: AgentEntity
        multivalued: true
      has_part:
        range: FileEntity
        multivalued: true
        inlined_as_list: true
      main_entity:
        range: FileEntity
      version:
        range: string
      cite_as:
        range: string

  ROCrateMetadataFile:
    description: ro-crate-metadata.json descriptor
    class_uri: schema:CreativeWork
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
        ifabsent: "ro-crate-metadata.json"
      about:
        range: ROCrate
        required: true
      conforms_to:
        range: uriorcurie
        required: true
        multivalued: true
```

### 3.2 Workflow RO-Crate (1.0)

The Workflow RO-Crate profile mandates a `mainEntity` of type `["File", "SoftwareSourceCode", "ComputationalWorkflow"]` with a `programmingLanguage` from a controlled list (CWL / Galaxy / KNIME / Nextflow / Snakemake). The Crate MUST specify a `license`, SHOULD contain `README.md`, MAY contain `test/` and `examples/` directories.

```yaml
# profiles/workflow_ro_crate.yaml (excerpt)
id: https://w3id.org/cytognosis/cytoskeleton/profiles/workflow_ro_crate
name: workflow_ro_crate

imports:
  - ./ro_crate

classes:
  WorkflowROCrate:
    is_a: ROCrate
    slot_usage:
      conforms_to:
        equals_string_in:
          - https://w3id.org/ro/crate/1.2
          - https://w3id.org/workflowhub/workflow-ro-crate/1.0
        required: true
      main_entity:
        range: ComputationalWorkflow
        required: true

  ComputationalWorkflow:
    is_a: FileEntity
    class_uri: schema:SoftwareSourceCode
    mixins:
      - bioschemas:ComputationalWorkflow
    attributes:
      programming_language:
        range: ComputerLanguage
        required: true
      image:
        range: ImageObject
      subject_of:
        range: FileEntity
        description: Optional CWL description of the main workflow.
      input:
        range: FormalParameter
        multivalued: true
      output:
        range: FormalParameter
        multivalued: true

  ComputerLanguage:
    class_uri: schema:ComputerLanguage
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      name:
        range: string
      alternate_name:
        range: string
      url:
        range: uri

enums:
  WorkflowLanguageEnum:
    permissible_values:
      cwl:
        meaning: https://w3id.org/workflowhub/workflow-ro-crate#cwl
      galaxy:
        meaning: https://w3id.org/workflowhub/workflow-ro-crate#galaxy
      knime:
        meaning: https://w3id.org/workflowhub/workflow-ro-crate#knime
      nextflow:
        meaning: https://w3id.org/workflowhub/workflow-ro-crate#nextflow
      snakemake:
        meaning: https://w3id.org/workflowhub/workflow-ro-crate#snakemake
      redun:
        meaning: https://w3id.org/cytognosis/workflow-ro-crate#redun
      kedro:
        meaning: https://w3id.org/cytognosis/workflow-ro-crate#kedro
```

Note: `redun` and `kedro` aren't yet officially supported `programmingLanguage` values at workflowhub.eu. We define them under our own w3id namespace, but a workflow that needs to publish to public workflowhub.eu must use one of CWL/Galaxy/KNIME/Nextflow/Snakemake. Recommended path: wrap any redun workflow in a thin Snakefile or CWL CommandLineTool for external publication; for internal publication to `workflows.cytognosis.org`, redun-native is fine.

### 3.3 Workflow Run Crate

The Workflow Run Crate extends Workflow RO-Crate with execution provenance: a `CreateAction` whose `instrument` is the workflow, `result` is the output files, `agent` is the runner, plus start/end times.

```yaml
# profiles/workflow_run_crate.yaml (excerpt)
id: https://w3id.org/cytognosis/cytoskeleton/profiles/workflow_run_crate
imports:
  - ./workflow_ro_crate

classes:
  WorkflowRunCrate:
    is_a: WorkflowROCrate
    slot_usage:
      conforms_to:
        equals_string_in:
          - https://w3id.org/ro/crate/1.2
          - https://w3id.org/workflowhub/workflow-ro-crate/1.0
          - https://w3id.org/ro/wfrun/process/0.5
          - https://w3id.org/ro/wfrun/workflow/0.5
        required: true
      has_part:
        required: true

  WorkflowRunAction:
    class_uri: schema:CreateAction
    mixins:
      - prov:Activity
    attributes:
      identifier:
        identifier: true
        range: uriorcurie
      name:
        range: string
      instrument:
        range: ComputationalWorkflow
        required: true
      object:
        range: FileEntity
        multivalued: true
      result:
        range: FileEntity
        multivalued: true
      agent:
        range: AgentEntity
        multivalued: true
      start_time:
        range: datetime
        required: true
      end_time:
        range: datetime
        required: true
      status:
        range: RunStatusEnum
      container_image:
        range: ContainerImage
      parameter_values:
        range: ControlAction
        multivalued: true
      attestation:
        range: InTotoAttestation
        description: DSSE-wrapped in-toto attestation chain.
```

The `InTotoAttestation` class wraps a base64-encoded DSSE envelope; the `ContainerImage` class records OCI registry + digest.

### 3.4 Five Safes RO-Crate

Five Safes RO-Crate is for TRE-FX (Trusted Research Environment) workflows over sensitive data. It adds: governance metadata (which Safes were applied: Safe people, projects, settings, data, outputs), DUC reference, PIA reference, de-id audit trail.

```yaml
# profiles/five_safes_crate.yaml (excerpt — Cytognosis-extended)
id: https://w3id.org/cytognosis/cytoskeleton/profiles/five_safes_crate
imports:
  - ./workflow_run_crate

classes:
  FiveSafesCrate:
    is_a: WorkflowRunCrate
    slot_usage:
      conforms_to:
        equals_string_in:
          - https://w3id.org/5s-crate/0.4
        required: true
    attributes:
      safe_projects:
        range: ProjectGovernance
        multivalued: true
        required: true
      safe_people:
        range: AgentEntity
        multivalued: true
        required: true
      safe_settings:
        range: TREEnvironment
        required: true
      safe_data:
        range: DataGovernance
        required: true
      safe_outputs:
        range: OutputDisclosure
        multivalued: true
      duc_reference:
        range: uriorcurie
        description: Per-cohort Data Use Certification (NIH GDS).
      pia_reference:
        range: uriorcurie
        description: Privacy Impact Assessment for this cohort.
```

### 3.5 Process Run Crate

For one-off scripts (no workflow), Process Run Crate is the lightweight option. It's identical to Workflow Run Crate except the `instrument` is a plain `SoftwareSourceCode` not a `ComputationalWorkflow`.

---

## 4. Bioschemas, SOSA/SSN, FHIR, GA4GH

### 4.1 Bioschemas ComputationalWorkflow

Used by WorkflowHub for indexing. Bakes into `workflow_ro_crate.yaml` via the `bioschemas:ComputationalWorkflow` mixin. The mixin requires `name`, `description`, `url`, `creator`, `dateCreated`, `dateModified`, `keywords`, `license`, `version`, `producer`, `featureList`, `programmingLanguage`. We auto-populate from cytoskeleton's repository metadata.

### 4.2 SOSA/SSN profile

The Cytos sensor universal schema already drafts `profile_sosa.yaml` aligning SOSA Sensor / Observation / FeatureOfInterest / Procedure / Platform / Sample / Result / ObservationCollection / Deployment / System / SystemCapability. The schema is at `cytos/schemas/domains/sensor/profiles/profile_sosa.yaml`; we move it to `cytoskeleton/schemas/profiles/sosa_ssn.yaml`.

### 4.3 FHIR R5 profile

`profile_fhir.yaml` from the sensor universal schema covers FHIR Observation, Device, DeviceMetric, DeviceUsage. We move it to `cytoskeleton/schemas/profiles/fhir_r5.yaml`. Round-trip to FHIR JSON is via `cytoskeleton.fhir.serialize`.

### 4.4 GA4GH

Four GA4GH profiles:

- **Phenopackets** — phenotype + disease bundles (mirroring `cmungall/linkml-phenopackets`).
- **VRS** — variant identity via cryptographic hashes.
- **DRS** — Data Repository Service URIs (the VFS exposes a DRS adapter).
- **TRS** — Tool Registry Service (the WorkflowHub instance exposes a TRS endpoint).

Phenopackets and VRS are LinkML profiles we import; DRS and TRS are wire protocols implemented in cytoskeleton.

---

## 5. Mappings (SSSOM)

Per `project_sssom_tooling.md` and the v0.4.0 scholarly KG schema, SSSOM is a first-class concern. The schema layer is:

```yaml
# mappings/sssom/mondo_to_omim.sssom.tsv
# subject_id  predicate_id  object_id  mapping_justification  ...
MONDO:0007103 skos:exactMatch OMIM:603467 semapv:LexicalMatching ...
```

Plus a `_provenance/mondo_to_omim.sssom.tsv.provenance.yaml` sidecar with: source vocab, target vocab, ontology versions, generation tool, agent, datetime, sha256.

A mapping set is an `EntityMapping` subclass in the scholarly schema linked to a `ResearchObject` for provenance, and emits its own RO-Crate (a `Dataset` containing the TSV + sidecar).

---

## 6. Codegen pipeline

LinkML compiles to many targets. The cytoskeleton `nox -s schemas_codegen` session runs:

```
linkml-validate schemas/ → 0 errors
gen-pydantic schemas/cytos.yaml → codegen/pydantic/cytos.py
gen-pydantic schemas/profiles/isa.yaml → codegen/pydantic/isa.py
gen-pydantic schemas/profiles/workflow_run_crate.yaml → codegen/pydantic/wfrun.py
gen-json-schema schemas/profiles/workflow_run_crate.yaml → codegen/jsonschema/wfrun.schema.json
gen-owl schemas/cytos.yaml → codegen/owl/cytos.ttl
gen-shacl schemas/cytos.yaml → codegen/shacl/cytos.shapes.ttl
gen-graphql schemas/cytos.yaml → codegen/graphql/cytos.graphql
gen-sqltables schemas/cytos.yaml → codegen/sql/cytos.ddl
gen-markdown schemas/cytos.yaml → codegen/markdown/
gen-typescript schemas/cytos.yaml → codegen/typescript/cytos.ts
```

These caches are gitignored by default; CI rebuilds and uploads to GCS for downstream consumers that don't run LinkML locally. The TypeScript bindings ship in the cytocast `templates/shared/api-client/` package.

---

## 7. Validation engines

Cytoskeleton provides a single validation entry point:

```bash
$ cytoskeleton validate <file> --schema <schema> --profile <profile>
```

Under the hood, this composes:

1. **LinkML structural validation** (`linkml-validate`).
2. **JSON Schema validation** (against codegen JSON Schema, useful for ISA-JSON / RO-Crate metadata).
3. **SHACL shape validation** (for RDF outputs).
4. **Custom validators** (DAG check for ISA Process graphs; URL liveness check for `cite_as`; sha256 verification for RO-Crate File entities; in-toto chain check for WorkflowRunCrate).
5. **Standards round-trip** (for ISA-JSON, FHIR JSON, RO-Crate JSON-LD: serialize → re-parse → structural equality).

A pre-commit hook + CI gate ensures every schema commit, every Crate emission, and every config change passes validation.

---

## 8. Backward compatibility with cytos.yaml

Cytos currently has `cytos/schemas/cytos.yaml` as the umbrella schema importing 21 domain files. The migration (Phase 6 of master plan) is:

1. Copy `cytos/schemas/*` to `cytoskeleton/schemas/domains/`.
2. Rewrite `cytos/schemas/cytos.yaml`'s `imports:` to point at `external/cytoskeleton/schemas/domains/...`.
3. Add a symlink `cytos/schemas → external/cytoskeleton/schemas` to preserve any tooling that hard-codes the path.
4. Add the new profiles (ISA, RO-Crate, etc.) in `cytoskeleton/schemas/profiles/` without touching cytos.

The PredicateEnum bug in cytos core (per the sensor schema design doc §7 open question 2) is fixed during the move: convert it from a `class` definition to a proper `enum` with `permissible_values`.

---

## 9. Versioning and release

- **Schema versions** follow SemVer at the umbrella `cytos.yaml` and profile-level. Breaking changes require major bump + ADR.
- **Profile versions** track upstream where applicable (Workflow RO-Crate 1.0.x, ISA Abstract Model 1.0, RO-Crate 1.2). When upstream releases a new minor, we re-profile in a feature branch, run round-trip tests, and ship.
- **Mapping sets** versioned per release date; SHA-256 of the TSV is in the provenance sidecar.
- **Generated codegen artifacts** versioned with the schema release; CI publishes a wheel `cytognosis-schemas==X.Y.Z` to internal PyPI containing the Pydantic + JSON Schema codegen for that release.

---

## 10. Open questions specific to schemas

1. **Phenopackets v2 vs v3**: do we pin v2 (current production) or chase v3 (under active development)? Recommendation: pin v2 in `profiles/ga4gh/phenopackets.yaml`; track v3 in a `phenopackets_v3.yaml` draft, switch on stability.

2. **Bioschemas ComputationalWorkflow 1.0 vs 0.5**: WorkflowHub example metadata still cites 0.5-DRAFT in some pages; the profile says 1.0-RELEASE in others. Recommendation: target 1.0-RELEASE; downgrade gracefully if WorkflowHub rejects.

3. **SSSOM schema import**: import the upstream `sssom-schema` LinkML directly (`imports: sssom-schema:sssom_schema`), or fork? Recommendation: import upstream; pin to a specific tag.

4. **CodeMeta + CITATION.cff alignment**: CodeMeta is JSON-LD, CITATION.cff is YAML. Both describe software. Our `profiles/codemeta.yaml` covers both — generate both formats from one LinkML instance.

5. **Five Safes profile location**: official location is `https://w3id.org/5s-crate/`; we mirror the schema, but should we contribute upstream? Recommendation: yes, after we have a working internal implementation.
