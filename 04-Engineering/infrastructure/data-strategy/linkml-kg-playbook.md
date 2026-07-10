# LinkML + Knowledge Graph Playbook

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> A 22-chapter, group-organized, hands-on playbook covering everything from "what is LinkML" to "how do I run an LLM RAG agent over the Cytognosis KG". This is the standard reference for any new schema, ontology mapping, or KG ingestion task at Cytognosis.

The playbook itself is a directory of markdown chapters and supporting code, not a single document. The full playbook was migrated into this repo on 2026-07-02 (Infrastructure consolidation) and now lives alongside this pointer document.

- **Location** — [`linkml-kg-playbook/`](linkml-kg-playbook/) (this repo)

This pointer document captures the structure and the decisions that came out of the playbook, so the operational docs in this repo (the [scholarly KG schema](scholarly-knowledge-graph.md), [SSSOM stack](sssom-cross-ontology-mapping.md), [paper library](paper-library-architecture.md)) can reference specific chapters reliably.

## Structure (8 groups, 22 chapters)

### 1. Foundations (chapters 00–02)

| Chapter | Topic |
| --- | --- |
| 00 | Setup |
| 01 | LinkML in an Hour |
| 02 | Schema Landscape (BibTeX, OpenAlex, Biolink, GA4GH, etc.) |

### 2. Pull canonical schemas (chapters 03–10)

| Chapter | Topic |
| --- | --- |
| 03 | schema.org + Bioschemas |
| 04 | Biolink + core LinkML schemas |
| 05 | UMLS + SNOMED CT — RF2 / RRF coverage; key components; OLS4 release; `snomed-owl-toolkit` vs. `umls2rdf` adapter comparison |
| 06 | BioThings + DDE |
| 07 | GA4GH (VRS, VA, Phenopackets, Pedigree, Beacon; `cmungall/linkml-phenopackets`) |
| 08 | SOSA / SSN |
| 09 | CELLxGENE |
| 10 | HDMF + NWB |

### 3. Pull domain data (chapters 11–12)

| Chapter | Topic |
| --- | --- |
| 11 | Open Targets |
| 12 | OpenAlex + BibTeX |

### 4. Organize (chapter 13)

| Chapter | Topic |
| --- | --- |
| 13 | Hybrid-layout pattern; v0.5.0 refactor target for `cytognosis_scholarly_kg.yaml` |

### 5. Map terms (chapter 14)

| Chapter | Topic |
| --- | --- |
| 14 | Full SSSOM workflow with OLS4 SnomedCT (download, parse, validate, RDF, SNOMED → MONDO) |

### 6. Ingest (chapters 15–17)

| Chapter | Topic |
| --- | --- |
| 15 | BioCypher — architecture, ontologies, schema-config philosophy, adapters with Biolink / MONDO / SNOMED examples + Open Targets case study |
| 16 | Koza + Monarch ecosystem — Koza vs. Monarch distinction, `monarch-ingest` deep dive, Monarch KG dedicated subsection (about, build, schemas, hands-on download / Neo4j / OAK), `phenopacket-ingest` with Protobuf and LinkML transform variants |
| 17 | BioCypher vs. Monarch — side-by-side architecture, inputs (schema / ontology + identifier resolution), outputs (formats + automation), use cases (Open Targets — BioCypher; STRING / PPI — both with CROssBARv2 vs. `string-ingest`), Cytognosis decision matrix |

### 7. Apply (chapters 18–20)

| Chapter | Topic |
| --- | --- |
| 18 | AnnData harmonization — 5-tier OAK → SSSOM → SapBERT → LLM → curator pipeline |
| 19 | LLM / RAG over the KG — biochatter, phenomics-assistant, graph-agent-devops, LangChain / LangGraph patterns (text-to-Cypher, agentic), end-to-end Cytognosis bio-agent example |
| 20 | Structured extraction — OntoGPT (LinkML-templated, OAK-grounded), Instructor (Pydantic + LLM), PydanticAI; hands-on LinkML → Pydantic → Instructor pipeline; spaCy / scispaCy hybrid pattern; tier comparison |

### 8. Reference (chapter 21)

| Chapter | Topic |
| --- | --- |
| 21 | Appendix — quick-references, prefix tables, troubleshooting |

## Operational decisions that came out of the playbook

- **BioCypher vs. Koza/Monarch** (chapter 17 decision matrix):
  - **BioCypher** — direct-to-Neo4j, used for Cytognosis-internal KG construction where we control the ingest end-to-end.
  - **Koza / Monarch** — used for any source that already has, or should have, per-source CI in the Monarch ingest pattern, or where we want Monarch KG reuse downstream.
  - Both are layered with `biochatter` / `phenomics-assistant` for LLM access (chapter 19).
- **v0.5.0 schema refactor** — driven by the hybrid-layout pattern in chapter 13. Targeted for the next minor release of `cytognosis_scholarly_kg.yaml`.
- **AnnData ingest** — chapter 18's 5-tier OAK → SSSOM → SapBERT → LLM → curator pipeline is the default ordering.

## Caveats and follow-ups

- **UMLS / SNOMED CT data folders** — chapter 05 assumes read-only mirrors at `_data/umls/` and `_data/snomed/` (local checkout subfolders). At the time the chapter was written those folders were not present; once they are, the chapter's hands-on commands run as-written.
- **No unverified URLs** — when chapters reference external endpoints (OLS4 SSSOM exports, OpenAlex API), the playbook is explicit about which URLs have been tested. New chapters or revisions should keep that discipline; if a URL has not been verified, phrase it as a hypothesis rather than an instruction.

## Cross-references

- [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md) — the schema the playbook revolves around.
- [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md) — chapter 14 is the worked SSSOM example.
- [`paper-library-architecture.md`](paper-library-architecture.md) — the sovereign library that feeds the OpenAlex + Zotero ingest in chapter 12.
- [`monday-resource-boards.md`](monday-resource-boards.md) — the boards the playbook's ingest pipelines populate.

---
**Document Owner**: Chief Data Officer, Cytognosis Foundation
**Playbook location**: [`linkml-kg-playbook/`](linkml-kg-playbook/) (this repo)
**Last Updated**: May 2026
**Status**: 22 chapters in 8 groups; living document
**Classification**: Internal Use Only
