# Sovereign Paper Library Architecture

> Cytognosis treats its scholarly corpus the same way it treats clinical data: every canonical artifact lives on Cytognosis-controlled infrastructure, with third-party SaaS tolerated only as a synchronization layer when the canonical copy already lives in our own storage.

This document specifies the four-layer architecture that replaces the previous ReadCube Papers / generic Zotero-cloud workflow with a sovereign, FAIR-aligned paper library.

## Why this architecture exists

- **Data sovereignty** — Cytognosis will not store PDFs, annotations, or organizational reading history on a vendor's cloud. Loss of vendor access (acquisition, pricing change, account suspension) must not threaten access to the corpus.
- **FAIR + open standards** — Every layer uses an open, well-specified standard (W3C Web Annotation, BibTeX/CSL-JSON, LinkML, Cypher) so that future tooling can ingest the same data without bespoke adapters.
- **Knowledge graph future-proofing** — Annotations, papers, code, models, and datasets are already first-class entities in the [scholarly knowledge graph](scholarly-knowledge-graph.md). The library is the operational front-end of that graph.
- **Research workflow continuity** — Researchers continue to use a familiar reference manager (Zotero) and editor (Google Docs) without losing access to citations, browser capture, or shared collections.

## Layered architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│  Layer 3 (planned): Neo4j Two-Layer Knowledge Graph              │
│    Objective layer: LinkML schema (papers, authors, code,        │
│        models, datasets, ontologies)                             │
│    Personalization layer: W3C Web Annotation nodes from          │
│        Hypothes.is (per-user / per-team filtered queries)        │
└────────────────────────────┬─────────────────────────────────────┘
                             ▲
                             │ ETL: Zotero API · OpenAlex · GitHub · HF
                             │ Annotation API (W3C)
┌────────────────────────────┴─────────────────────────────────────┐
│  Layer 2: Self-hosted Hypothes.is on `cytognosis-infrastructure` │
│    W3C Web Annotation Data Model · own PostgreSQL                │
│    Annotates ANY URI-addressable KG object (papers, code repos,  │
│    models, datasets, ontology terms)                             │
└────────────────────────────┬─────────────────────────────────────┘
                             ▲
                             │ URI-addressable references
                             │
┌────────────────────────────┴─────────────────────────────────────┐
│  Layer 1: Zotero Group Library (metadata-only sync)              │
│    Free, unlimited (no PDFs on Zotero servers)                   │
│    Linked URL attachments → Drive PDFs                           │
│    Extra field: structured links (drive-pdf, code-original,      │
│       code-internal, dataset-original, dataset-internal,         │
│       model-original, model-internal)                            │
└────────────────────────────┬─────────────────────────────────────┘
                             ▲
                             │ pyzotero · Connector
                             │
┌────────────────────────────┴─────────────────────────────────────┐
│  Layer 0: Google Drive (canonical PDF & artifact store)          │
│    Library/Attachments/ — canonical PDFs                         │
│    Library/Intake/      — new papers awaiting metadata            │
│    Library/Papers/      — original ReadCube export (legacy)       │
└──────────────────────────────────────────────────────────────────┘
```

### Layer 0 — Google Drive

The canonical, append-only PDF store. Every PDF in the corpus is identified by its Drive object ID; every other layer references that ID rather than storing its own copy.

- **`Library/Attachments/`** — canonical PDFs. Filenames follow `{first-author}{year}_{short-title}.pdf` post-import.
- **`Library/Intake/`** — newly captured PDFs awaiting metadata extraction and migration into `Attachments/`.
- **`Library/Papers/`** — ReadCube export (legacy). Preserved unchanged so the migration is auditable and reversible.

In-PDF annotations follow ISO 32000 (the standard PDF annotation format). Drive sync handles propagation across devices. This is portable, inspectable, and survives any reader-software change.

### Layer 1 — Zotero (metadata-only)

Zotero is the team's reference manager. The Cytognosis Foundation Zotero **Group Library** holds metadata only — never PDFs.

- **Free tier, unlimited** — Zotero Group Libraries do not bill for metadata. We never exceed the cloud-storage quota because we never put files there.
- **Linked URL attachments** — each Zotero item carries a `linked URL` attachment pointing at the Drive PDF (the redirect to the actual `https://drive.google.com/file/d/{id}/view` is stored, not the PDF).
- **Extra field encodes structured cross-references** — the Zotero `Extra` field uses a small key-value vocabulary aligned with the [scholarly KG schema](scholarly-knowledge-graph.md):
  - `drive-pdf:` Drive file ID for the canonical PDF
  - `code-original:` upstream repository (e.g. authors' GitHub)
  - `code-internal:` Cytognosis-mirrored fork (when one exists)
  - `dataset-original:` upstream dataset URI (Zenodo, Figshare, etc.)
  - `dataset-internal:` Cytognosis-mirrored copy (when one exists)
  - `model-original:` upstream model card (HuggingFace, etc.)
  - `model-internal:` Cytognosis-mirrored copy (when one exists)
- **Tools** — Zotero 7 (open source, https://www.zotero.org/), Zotero Connector (Chrome / Firefox), pyzotero for programmatic enrichment.

> **Architectural decision: do NOT use Zotero's built-in PDF annotation engine.**
> Zotero's annotations live in a proprietary SQLite store that does not sync without Zotero's cloud storage subscription, and the export format is brittle. Use ISO 32000 in-PDF annotations (Drive-synced) for personal/portable annotations, and Hypothes.is (Layer 2) for threaded team discussion.

> **Architectural decision: Zotero plugins that need PDF content will not work.**
> ZotSeek, Beaver, full-text search, automatic tagging, etc., depend on Zotero having local PDF copies. We deliberately decline that path. Equivalent capabilities are built on our own infrastructure (full-text search via Elasticsearch / OpenSearch; auto-tagging via OpenAlex enrichment + LLM extraction).

### Layer 2 — W3C Web Annotation via self-hosted Hypothes.is

Hypothes.is is BSD-licensed and self-hostable. We run an instance in `cytognosis-infrastructure` against an own PostgreSQL database and serve it at an internal subdomain. The data model is the W3C Web Annotation Data Model (`https://www.w3.org/TR/annotation-model/`) — annotations have stable identifiers, structured selectors, and can target any URI.

This means Hypothes.is can annotate not only papers but **any URI-addressable KG object**: a GitHub repository, a HuggingFace model card, a dataset DOI, an ontology term in OLS4, a Cytognosis internal protocol page. Threaded discussion (replies) and group permissions are first-class.

Personal and team libraries are queries over the annotation graph rather than copies of the corpus:

- *Shahin's personal library* = annotations where `creator = mohammadi@cytognosis.org`.
- *Cellular Intelligence team library* = annotations where `audience ∈ {cellular-intelligence-team}`.
- *Internal review of paper X* = annotations where `target = drive://{paper-id}` and `motivation = reviewing`.

### Layer 3 (planned) — Neo4j two-layer knowledge graph

The future state lifts Layers 0–2 into a single graph database for cross-corpus query.

- **Objective layer** — LinkML-driven nodes for papers, authors, code, models, datasets, biological entities (Gene Ontology, Disease Ontology, Cell Ontology). Fed by the Zotero API, OpenAlex, GitHub API, and HuggingFace API. Schema is documented in [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md).
- **Personalization layer** — W3C Web Annotation nodes harvested from Hypothes.is. Personal libraries become filtered queries over annotations; the underlying corpus is not duplicated.

The Neo4j stack is already provisioned (see [`../self_hosted/logseq_knowledge_architecture.md`](../self_hosted/logseq_knowledge_architecture.md) and the [Container Framework](../../container_framework/README.md)).

## Reader and annotation tools

| Platform | Recommended reader | Annotation strategy |
| --- | --- | --- |
| Linux | Okular (annotates), Sioyek (read/navigate, has its own DB so do not annotate in Sioyek) | ISO 32000 in-PDF; Hypothes.is for team discussion |
| macOS | Preview, Skim | ISO 32000 in-PDF |
| iOS / iPadOS | GoodReader (one-time purchase, integrates with Drive) | ISO 32000 in-PDF |
| Windows | Foxit, Xodo | ISO 32000 in-PDF |
| Cross-platform premium | Xodo PDF Studio Pro (one-time purchase, native Linux available) | ISO 32000 in-PDF |

## Automation pipelines (current and planned)

| Pipeline | State | Description |
| --- | --- | --- |
| Intake watcher | planned | Watch `Library/Intake/` → DOI extract → CrossRef metadata lookup → create Zotero item → move PDF to `Library/Attachments/` |
| Drive ↔ Zotero link sync | planned | Reconcile Zotero linked URLs against Drive file IDs after any rename or move |
| Google Docs bibliography hyperlinker | planned | Apps Script that walks references in a Doc and replaces them with Drive links to the canonical PDF |
| Zotero Connector PDF redirect | planned | Custom variant of ZotMoov so capturing a paper from a publisher page deposits the PDF into `Library/Intake/` rather than a local Zotero attachment store |
| OpenAlex enrichment | planned | Periodic ETL that augments Zotero items with OpenAlex IDs, citation counts, and authorship graphs |
| Monday.com sync | active (manual) | Mirror Papers / Code / Models / Datasets / Workflows / Protocols into the Resources workspace ([`monday-resource-boards.md`](monday-resource-boards.md)) |

## Migration from ReadCube Papers

ReadCube Papers is being deprecated in favor of this stack. The migration baseline:

- All ReadCube PDFs have already been exported to `Library/Papers/` on Drive.
- An XLS workbook with paper-level metadata, filenames, and the original folder hierarchy was produced as part of the export.
- Zotero is installed locally; the `cytognosis` Zotero account exists but the Group Library is being seeded fresh.

Migration steps:

1. Convert the XLS export to RIS or BibTeX. Import into the Zotero Group Library so each paper has a metadata record.
2. Move PDFs from `Library/Papers/` to `Library/Attachments/` on Drive.
3. For each Zotero item, attach a linked URL pointing at the Drive PDF and populate the `Extra` field with the structured cross-references (`drive-pdf:`, `code-original:`, etc.).
4. Rebuild the ReadCube collection hierarchy as Zotero collections from the XLS.
5. Validate: every Zotero item resolves to a working Drive link; every paper in `Library/Papers/` has a corresponding Zotero record.

A step-by-step operational guide (`zotero-setup-guide.md`) lives in the **Infrastructure and Tooling** workspace folder rather than this repo, because it contains personal Drive paths and account specifics.

## Cross-references

- [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md) — the LinkML schema that all of the above feeds into.
- [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md) — how biological entities mentioned in the library are mapped across UMLS, MONDO, HP, CL, CHEBI, NCBITaxon, SNOMED CT.
- [`monday-resource-boards.md`](monday-resource-boards.md) — the registry boards that surface the corpus in Cytognosis's project-management workspace until the Neo4j stack is fully online.
- [`../self_hosted/logseq_knowledge_architecture.md`](../self_hosted/logseq_knowledge_architecture.md) — how Logseq plugs into Layer 1 / Layer 2 for note-taking workflows.
- [`linkml-kg-playbook.md`](linkml-kg-playbook.md) — pointer to the hands-on playbook (LinkML, Biolink, BioCypher, Koza/Monarch, OLS4 SSSOM) used to build the ETL pipelines above.

---
**Document Owner**: Chief Data Officer, Cytognosis Foundation
**Last Updated**: May 2026
**Status**: Layers 0–1 operational; Layer 2 in deployment; Layer 3 planned
**Classification**: Internal Use Only
