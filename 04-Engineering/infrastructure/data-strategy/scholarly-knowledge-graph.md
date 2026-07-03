# Scholarly Knowledge Graph Schema

> Cytognosis maintains a single LinkML schema that unifies bibliographic metadata, scholarly graph data, biomedical entities, research artifacts (code, data, models, workflows, protocols), licenses, and personal annotations — and is interoperable with SemOpenAlex SPARQL, the UMLS Metathesaurus, the NCATS Translator ecosystem, and RO-Crate packaging.

The canonical schema YAML was migrated into this repo on 2026-07-02 (Infrastructure consolidation) and lives under [`schemas/`](schemas/). Codegen outputs (Pydantic, JSON Schema, OWL, SHACL, SQL DDL) are large and stay out of git; regenerate them on demand. This document is the authoritative description of what the schema is for, where to find it, and how it is structured.

## Where to find the schema

| Artifact | Location |
| --- | --- |
| Current schema (v0.4.0) | [`schemas/cytognosis_scholarly_kg_v0.4.0.yaml`](schemas/cytognosis_scholarly_kg_v0.4.0.yaml) |
| Previous schema (v0.3.0) | [`schemas/cytognosis_scholarly_kg.yaml`](schemas/cytognosis_scholarly_kg.yaml) — retained for reference |
| Resource sub-schemas | [`schemas/`](schemas/) — code, datasets, models, papers, protocols, relationships, research_objects, workflows |
| Codegen outputs | regenerated on demand (Pydantic, JSON Schema, SHACL, OWL, SQL DDL); not tracked in git |

When the schema is promoted to a public release we will publish it under `cytognosis/scholarly-kg-schema` with a SPDX license, FAIR identifier (DOI via Zenodo), and a Hugging Face `data-card` mirror.

## Why a single schema

Several existing schemas overlap, none cover everything we need, and stitching them in code is brittle:

- **BibTeX / CSL-JSON** — covers paper metadata, weak on artifacts.
- **OpenAlex / SemOpenAlex** — covers scholarly graph + author graph, weak on artifact relationships.
- **Biolink / PubMed-KG** — strong on biomedical entities, weak on bibliographic detail.
- **UMLS** — strong on terminology mapping, not a content model.
- **NCATS Translator** — defines a Knowledge Provider (KP) interface, not the data model itself.
- **W3C Web Annotation** — strong on annotations, not on the corpus they annotate.
- **RO-Crate** — strong on packaging research outputs, not on internal cross-artifact relationships.

A LinkML schema lets us import all of the above as YAML modules and add typed Cytognosis-specific extensions on top, while emitting Pydantic / JSON Schema / OWL / SHACL / SQL DDL automatically.

## What v0.4.0 adds over v0.3.0

The 2026-04-11 v0.4.0 release added typed artifact relationship edges, RO-Crate alignment, computational workflows, formal parameters, instruments, protocols, presentations, and several enums.

### Typed artifact relationship edges

Three enums encode the relations we care about between papers and the artifacts they cite, produce, or extend.

```text
PaperCodeRelationType
    implements          (schema:isBasedOn)
    supplements         (schema:hasPart)
    depends_on          (prov:used)
    extends             (pav:previousVersion)
    documents           (codemeta:referencePublication)
    reproduces          (cito:replicates)

PaperModelRelationType
    proposes            (prov:wasGeneratedBy)
    uses                (prov:used)
    fine_tunes          (prov:wasDerivedFrom)
    evaluates           (cito:citesAsAuthority)
    distills            (prov:wasDerivedFrom)
    extends_architecture (pav:previousVersion)

PaperDatasetRelationType
    creates             (prov:wasGeneratedBy)
    uses                (cito:usesDataFrom)
    uses_for_training
    uses_for_testing    (cito:citesAsDataSource)
    uses_for_validation
    uses_as_benchmark   (cito:citesAsAuthority)
    augments            (prov:wasDerivedFrom)
    curates             (prov:wasDerivedFrom)
```

Each relation is captured as a concrete subclass of an abstract `ArtifactRelationship`:

- `PaperCodeRelationship`
- `PaperModelRelationship`
- `PaperDatasetRelationship`

Every concrete relationship carries `source` / `target` references, the typed `predicate`, supporting `evidence_text`, and a `confidence` score.

### RO-Crate alignment

- `ResearchObject` (`schema:Dataset`) — the RO-Crate root entity, with typed `has_part` slots for papers, code, datasets, models, workflows, protocols, presentations, and instruments.
- `HasROCrateMetadata` mixin — `conforms_to`, `sd_publisher`, `sd_date_published`, `credit_text`, `cite_as`.
- `ResearchObjectProfile` enum — `base`, `workflow`, `workflow_run`, `process_run`, `provenance_run`, `workflow_testing`, `five_safes`, `arc`.

### New entity classes

- `ComputationalWorkflow` (`bioschemas:ComputationalWorkflow`) — workflow language, inputs / outputs as `FormalParameter`.
- `FormalParameter` (`bioschemas:FormalParameter`) — direction, type, default value.
- `Instrument` (`schema:Thing`) — manufacturer, model, serial number.
- `Protocol` (`schema:CreativeWork`) — protocol type, steps, reagents.
- `Presentation` (`schema:PresentationDigitalDocument`) — format, event name, slide count.

### New enums

`WorkflowStatus`, `WorkflowLanguage` (`cwl`, `wdl`, `nextflow`, `snakemake`, `galaxy`, …), `ParameterDirection`, `ProtocolType`, `ResearchObjectProfile`.

### New CURIE prefixes

| Prefix | Namespace |
| --- | --- |
| `pav:` | Provenance, Authoring, Versioning ontology |
| `bioschemas:` | bioschemas.org |
| `ro:` | Research Object Ontology |

### Schema statistics (v0.4.0)

- 38 enums
- ~95 classes (including 13 mixins)
- 250+ slots

## How the schema is used

| Surface | How it consumes the schema |
| --- | --- |
| Zotero / Drive integration | The `Extra` field on Zotero items uses keys aligned with the schema slots (`drive-pdf:`, `code-original:`, etc.). See [`paper-library-architecture.md`](paper-library-architecture.md). |
| Monday.com Resources workspace | Each entity board's columns map 1:1 to schema slots. Relationship boards instantiate the typed enums above. See [`monday-resource-boards.md`](monday-resource-boards.md). |
| Future Neo4j knowledge graph | Nodes and edges in the objective layer are produced by codegen against this schema. The personalization layer is W3C Web Annotation nodes layered on top. |
| NCATS Translator Knowledge Provider | The schema's Biolink-aligned classes let us register Cytognosis as a KP exposing typed paper / code / model / dataset / workflow / protocol relationships. |
| RO-Crate packaging | `ResearchObject` + `HasROCrateMetadata` mixin produce conformant RO-Crate metadata for any submitted release. |
| SSSOM cross-ontology mapping | The schema imports `sssom_schema`; an `EntityMapping` subclass of `Mapping` links to `ResearchObject` for provenance. See [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md). |

## Open follow-ups

- Promote the schema to its own public repo with a Zenodo DOI once v0.5.0 settles.
- Refactor v0.5.0 against the hybrid-layout pattern in chapter 13 of the [LinkML+KG playbook](linkml-kg-playbook.md).
- Wire `linkml validate` and `sssom validate` into CI for any PR that touches the schema or the SSSOM TSVs.

## Cross-references

- [`paper-library-architecture.md`](paper-library-architecture.md) — Layer 0–3 sovereign library that is the operational front end of this graph.
- [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md) — how biological entities are harmonized across vocabularies before ingest.
- [`monday-resource-boards.md`](monday-resource-boards.md) — Resources workspace that mirrors the schema's entity types.
- [`linkml-kg-playbook.md`](linkml-kg-playbook.md) — hands-on playbook covering LinkML, Biolink, BioCypher, Koza/Monarch, OLS4 SSSOM, CELLxGENE harmonization.

---
**Document Owner**: Chief Data Officer, Cytognosis Foundation
**Schema Version**: 0.4.0 (current); v0.5.0 in design
**Last Updated**: May 2026
**Classification**: Internal Use Only
