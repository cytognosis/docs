# Cytognosis Tools Catalog

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, researchers
> **Tags**: `tools`, `catalog`, `infrastructure`

> *Cytognosis exists so no one else waits decades for answers.*

Single source of truth for the **911 unique tools** evaluated, adopted, deferred, or rejected across the Cytognosis Foundation infrastructure stack. Consolidated from six research archives plus the May 2026 connectomics review.

## Documents in this directory

| Document | Lines | Purpose |
| --- | ---: | --- |
| [`tools-master-catalog.md`](tools-master-catalog.md) | 2 022 | Full per-layer breakdown of all 911 tools with status, license, surface, org, and rejection rationale |
| [`tools-infrastructure-stack.md`](tools-infrastructure-stack.md) | 624 | Deep-dive on the infrastructure layers: storage → repos → meta → FAIR → provenance → workflow → KG, with Mermaid data-flow diagrams |
| [`tools-master-catalog.xlsx`](tools-master-catalog.xlsx) | — | Filterable spreadsheet with views by Layer, Surface, Status, Organization, plus Tag Glossary and Stats |

## Quick orientation

### Three product surfaces, one infrastructure spine

| Surface | Tool count | Description |
| --- | ---: | --- |
| 🌸 **Cytonome** | 200 | On-device navigator + empathic voice interviewer |
| 🟢 **Cytoverse** | 308 | AI map: knowledge graph + foundation-model platform + multi-omic data lake |
| 🟡 **Spine** | 396 | FAIR-compliant foundations: standards, repositories, lineage, reproducibility |

### 16-layer stack summary

| # | Layer | Tools | Headline picks |
| --- | --- | ---: | --- |
| L1 | Storage | 81 | TileDB, Zarr v3, Parquet, Safetensors, GGUF |
| L2 | Preprocessing | 146 | fMRIPrep, Docling, GROBID, PLINK2, ComBat |
| L3 | Repositories | 69 | GitHub, HuggingFace, Zenodo, OpenNeuro, DANDI |
| L4 | Meta layer | 109 | Bioregistry, Hypothes.is, Zoekt, GitNexus, OAK |
| L5 | Zoos | — | HuggingFace Hub, MLflow Registry, WorkflowHub |
| L6 | FAIR packaging | 26 | RO-Crate, FAIRSCAPE, Zenodo, Model Cards |
| L7 | Provenance | 35 | LaminDB, redun, DVC, DataLad, MLflow, Aim |
| L8 | Workflow | 38 | Nextflow, Snakemake, redun, Nipype, Docker |
| L9 | Standards | 211 | LinkML, GA4GH, BIDS, NWB, HED, OBO, MCP |
| L10 | Knowledge graphs | 69 | BioCypher, Neo4j, KuzuDB, SemOpenAlex |
| L11 | UI / Frontend | 101 | Flutter, React 19, Tauri v2, Rive, Mermaid |
| L12 | AI / Models | 278 | Gemma 4, OLMo, BrainGFM, LangGraph, PyTorch |
| L13 | Networking | 21 | mDNS, NATS, Tailscale, Iroh CRDT, WireGuard |
| L14 | Scholarly | 59 | Zotero, OpenAlex, GROBID, CiteAs, arXiv |
| L15 | KM | 22 | Anytype, Mermaid, Excalidraw, tldraw |
| L16 | Cloud | — | Cloud Run, Vertex AI, GCS, GitHub Actions |

### Adoption status

| Status | Count | Meaning |
| --- | ---: | --- |
| ✅ primary | 518 | Recommended pick, adopted in the stack |
| 🟡 alternative | 110 | Strong alternative, kept on radar |
| ⏸️ deferred | 16 | Revisit later (license, maturity) |
| ❌ rejected | 80 | Explicitly ruled out (rationale preserved) |
| • mentioned | 187 | Named but not actionable |

### Seven cross-cutting invariants

1. **Open by default** — every primary pick is permissively licensed (Apache 2.0 / MIT / BSD-3 / CC0)
2. **Schema is the hub** — LinkML compiles to Pydantic, JSON-Schema, GraphQL, OWL, ShEx, SHACL, SQL DDL, TypeScript
3. **Local-first and privacy-preserving** — edge inference, on-device persona, CRDT state, PHI never leaves phone
4. **Interoperability through MCP** — Model Context Protocol is the de-facto agent-to-tool standard
5. **FAIR is operational, not aspirational** — RO-Crate auto-emits from every workflow run; tri-identifier coverage
6. **Dual-tier S2S, never single-process** — phone (Tier 1, 90%) + supervisor (Tier 2, 8%) + cloud (Tier 3, 2%)
7. **Reproducibility as system property** — AST + data hashing via redun; provenance binds code, data, model, paper

## Cross-references

This catalog informs and is referenced by several other infrastructure documents:

- [Master Data Strategy](../data-strategy/master-data-strategy.md) — data governance vision referencing storage and FAIR tools
- [Data Management Plan Template](../../../_templates/data-management-plan-template.md) — DMP sections reference specific tools for storage, versioning, FAIR packaging, and repositories
- [Technical Data Infrastructure](../data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md) — GCP project taxonomy and HIPAA controls using tools from L1, L7, L8
- [Scholarly Knowledge Graph](../data-strategy/scholarly-knowledge-graph.md) — LinkML schema referencing L9, L10 tools
- [Sovereign Paper Library Architecture](../data-strategy/paper-library-architecture.md) — Zotero + Drive + Hypothes.is from L14, L4
- [Self-Hosted Services](../self_hosted/README.md) — container framework using L8 workflow tools

## Source provenance

This catalog is the union of 6 sources, deduplicated by canonical tool name:

| Source | Tools | Description |
| --- | ---: | --- |
| `master_unsorted.md` | 508 | Unsorted union of all 19 research tabs |
| `research_outline.md` | 494 | April 2026 outline with rejection rationale |
| `consolidated.md` | 439 | May 2026 harmonised 11-component architecture |
| `repos.md` | 194 | 16 catalogued GitHub org directories |
| `zotero-setup-guide.md` | 60 | Reference manager + PDF annotation pipeline |
| `connectomics/*.md` | 148 | BIDS / HED / NWB triad + fMRI foundation-model review |
