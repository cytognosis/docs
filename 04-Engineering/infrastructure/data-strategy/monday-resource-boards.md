# Monday.com Resource Boards

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> The Cytognosis Foundation Monday.com workspace mirrors the [scholarly knowledge graph schema](scholarly-knowledge-graph.md) at human-friendly resolution. Until the Neo4j stack is fully online, the Resources folder on Monday.com is the operational registry for papers, models, code, datasets, workflows, protocols, and the typed relationships between them.

## Workspace coordinates

- **Workspace**: Cytognosis Foundation (ID `1102588`)
- **Top-level folder**: Resources (ID `20138602`)

## Entity boards

Each entity type has its own sub-folder and its own board. Columns map 1:1 to slots in the v0.4.0 LinkML schema.

| Board | Board ID | Folder ID | Key columns |
| --- | --- | --- | --- |
| Papers Registry | `18408270634` | `20138603` | DOI, PMID, Year, Pub Date, Abstract, Journal, Authors, BibTeX Type, Open Access, URL, OpenAlex ID, ArXiv ID, Cited By Count, Keywords, Language, Volume, Issue, Pages, Is Retracted, Drive PDF, Code / Dataset / Model Links, License |
| Models Registry | `18408270635` | `20138604` | HuggingFace ID, DOI, ML Task, Framework, Base Model, Parameter Count, Precision, License, Repository URL, Downloads, Training Dataset, Description |
| Code Registry | `18408270636` | `20138605` | Repository URL, Programming Language, License, Stars, Forks, Last Commit, DOI, SWH ID, Description, Homepage, CI Status |
| Datasets Registry | `18408270637` | `20138606` | DOI, Repository URL, Access Level, Data Type, Size, Record Count, License, Format, Version, Publisher, Date Published, Description |
| Workflows Registry | `18408270638` | `20138607` | Workflow Language, Version, Status, Repository URL, License, DOI, Description |
| Protocols Registry | `18408270640` | `20138608` | Protocol Type, Version, URL, DOI, Description, License |

## Relationship boards

All three relationship boards live in the **Relationships** sub-folder (ID `20138609`). Each implements one of the typed enums from the [scholarly KG schema](scholarly-knowledge-graph.md).

| Board | Board ID | Relation type enum (Status column) | Source → Target |
| --- | --- | --- | --- |
| Paper-Code Relationships | `18408270641` | `implements`, `supplements`, `depends_on`, `extends`, `documents`, `reproduces` | Papers (`18408270634`) → Code (`18408270636`) via `board_relation` |
| Paper-Model Relationships | `18408270644` | `proposes`, `uses`, `fine_tunes`, `evaluates`, `distills`, `extends_architecture` | Papers (`18408270634`) → Models (`18408270635`) via `board_relation` |
| Paper-Dataset Relationships | `18408270645` | `creates`, `uses`, `uses_for_training`, `uses_for_testing`, `uses_for_validation`, `uses_as_benchmark`, `augments`, `curates` | Papers (`18408270634`) → Datasets (`18408270637`) via `board_relation` |

Every relationship board carries the same supporting columns:

- **Relation Type** — `status` column populated from the enum above.
- **Predicate URI** — `text` column with the canonical predicate (e.g. `cito:replicates`).
- **Evidence Text** — `long_text` column with the supporting passage from the paper.
- **Confidence** — `numbers` column (0.0–1.0).
- **Source Paper** — `board_relation` to Papers (`18408270634`).
- **Target entity** — `board_relation` to the appropriate entity board.

## Dashboards

A consolidated **Resources Overview** dashboard was attempted programmatically but Monday.com returned 403 — dashboard creation appears to require the Pro / Enterprise plan. The dashboard should be built manually in the Monday.com UI when the plan supports it. Until then, the entity boards are the operational view.

## How automation pipelines use these IDs

Use the board IDs above directly when wiring ETL pipelines:

- **Zotero → Papers Registry** — pyzotero pulls items, flattens BibTeX / OpenAlex fields, and `change_item_column_values` (or `create_item`) onto board `18408270634`. Drive PDF links populate the `Drive PDF` column.
- **GitHub API → Code Registry** — pull repository metadata (stars, forks, last commit, license, CI status) onto board `18408270636`. Software Heritage IDs (SWH) attach via the `SWH ID` column.
- **HuggingFace API → Models Registry** — pull `model_info` for each model card onto board `18408270635`. Base-model lineage flows into the `Base Model` column.
- **Workflow registries** — Snakemake / Nextflow / WDL workflow records flow onto board `18408270638`.
- **Relationship extraction** — paper-code / paper-model / paper-dataset relationships are extracted (today: manual + LLM-assisted; future: structured extraction via OntoGPT or similar — see the [LinkML+KG playbook](linkml-kg-playbook.md), chapter 20). Each extracted edge becomes a relationship board item with the typed predicate.

## Cross-references

- [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md) — the schema these boards instantiate.
- [`paper-library-architecture.md`](paper-library-architecture.md) — the sovereign library that feeds the Papers Registry.
- [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md) — used to harmonize ontology IDs that flow into entity board columns.

---
**Document Owner**: Chief Data Officer, Cytognosis Foundation
**Last Updated**: May 2026
**Status**: Boards instantiated; manual entry + partial automation; Neo4j replacement is the longer-term target
**Classification**: Internal Use Only
