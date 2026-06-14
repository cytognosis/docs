# 03 — LinkML to Anytype Mapping

## Goal

Yar should reuse existing structured schemas instead of inventing ad hoc object models. LinkML is the canonical schema authoring layer. Anytype is the user-facing local-first object graph layer.

The mapping layer should translate LinkML classes and slots into Anytype Types, Properties, Relations, and Templates.

## Current implementation status — 2026-05-17

Implemented:

- `examples/demo_research_schema.yaml` registers a LinkML-like research schema.
- `scripts/register_demo_schema.py` loads and reports the normalized schema and Anytype mapping.
- SQLite stores normalized schema metadata and Anytype mapping reports.
- Anytype write planning can build object/type/property/relation plans from the local registry and local objects.
- CAP-Lite checks every Anytype write plan/execution path and blocks raw capture fields, unsupported actions, deletes without external IDs, diagnosis/treatment/health-risk content, and unconfirmed external writes.

Not yet implemented:

- Full LinkML runtime validation.
- Automatic Anytype type/property/schema registration with stable production semantics.
- Schema drift repair against a live Anytype space.

The current safe rule is: Yar treats the local schema registry as source of truth, creates dry-run Anytype plans, and executes only confirmed plans through discovered MCP tools.

## Conceptual mapping

| LinkML | Anytype | Notes |
|---|---|---|
| Schema | Space-level schema package | Stored as metadata in Yar registry; optionally mirrored in Anytype. |
| Class | Type | Example: `Paper` → Anytype Type `Paper`. |
| Slot | Property | Example: `title`, `abstract`, `doi`. |
| Slot with class range | Relation | Example: `authored_by` range `Author`. |
| Multivalued slot | Multi-select or relation list | Depends on range type. |
| Enum | Select/Tag options | Example: `publication_status`. |
| Required slot | Validation rule | Anytype may not enforce all required properties; Yar must. |
| Identifier | External ID / unique property | Example: DOI, ORCID, GitHub URL. |
| Inheritance | Type template metadata | Anytype may not support inheritance natively; preserve in Yar registry. |
| Description | Type/property description | Used in UI and LLM prompt context. |
| Aliases | Synonyms/search hints | Used by router and retrieval. |

## MVP schema registry

Use a local schema registry as source of truth.

```json
{
  "schema_name": "yar_research_schema",
  "version": "0.1",
  "classes": {
    "Paper": {
      "description": "A scholarly paper, preprint, article, or technical report.",
      "slots": {
        "title": {"range": "string", "required": true},
        "doi": {"range": "string", "required": false},
        "url": {"range": "uri", "required": false},
        "authors": {"range": "Author", "multivalued": true},
        "uses_dataset": {"range": "Dataset", "multivalued": true},
        "implements_method": {"range": "Method", "multivalued": true}
      }
    }
  }
}
```

## Minimum LinkML-inspired classes

### Paper

```yaml
Paper:
  description: A scholarly paper, preprint, article, or technical report.
  slots:
    - title
    - doi
    - url
    - abstract
    - authors
    - uses_dataset
    - uses_method
    - related_code
    - annotations
```

### Author

```yaml
Author:
  description: A person who authored or contributed to a research artifact.
  slots:
    - name
    - orcid
    - affiliation
    - homepage
    - authored_papers
```

### Dataset

```yaml
Dataset:
  description: A dataset used, cited, generated, or discussed in research work.
  slots:
    - name
    - url
    - license
    - domain
    - data_type
    - used_by_papers
    - related_code
```

### Code

```yaml
Code:
  description: A software package, repository, notebook, script, or code artifact.
  slots:
    - name
    - repository_url
    - language
    - license
    - implements_method
    - uses_dataset
    - related_paper
```

### Method

```yaml
Method:
  description: A scientific, computational, or analytical method.
  slots:
    - name
    - description
    - implemented_by_code
    - used_in_papers
    - applies_to_dataset
```

### Annotation

```yaml
Annotation:
  description: A W3C Web Annotation-style comment, highlight, or note targeting a paper, webpage, dataset, or code artifact.
  slots:
    - body
    - target
    - motivation
    - selector
    - creator
    - created_at
    - source_capture
```

## Anytype registration strategy

### Phase 1 — Local-only schema registry

- Keep LinkML schema in the coordinator.
- Use schema to validate model outputs.
- Create Anytype objects using existing manually created Types.
- If Type does not exist, fall back to generic `Note` plus `yar_type` property.

### Phase 2 — Anytype type/property mapping

- Discover existing Anytype Types.
- Map LinkML classes to existing Types when names match.
- Create missing Types manually or via MCP if supported.
- Create missing Properties manually or via MCP if supported.

### Phase 3 — Round-trip schema synchronization

- Read Anytype Types/Properties.
- Compare against LinkML schema.
- Produce schema drift report.
- Allow user-approved sync.

## Type mapping example

```json
{
  "linkml_class": "Dataset",
  "anytype_type_name": "Dataset",
  "properties": {
    "name": "Name",
    "url": "URL",
    "license": "License",
    "domain": "Domain",
    "data_type": "Data Type"
  },
  "relations": {
    "used_by_papers": {
      "target_type": "Paper",
      "relation_name": "Used by Paper"
    }
  }
}
```

## Validation rules

Before writing to Anytype:

1. Object type must exist in schema registry.
2. Required fields must be present or marked `needs_user_confirmation`.
3. Links must reference known object types.
4. Low-confidence links must be stored as suggestions, not facts.
5. Raw capture must not be written as a public object property unless the user explicitly confirms.
