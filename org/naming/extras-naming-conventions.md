---
title: "Extras & Naming Conventions Research"
date: "2026-05-25"
source: "migrated from org/plans"
category: "operations"
status: "current"
tags:
  - cytognosis
  - operations
---

# Extras & Naming Conventions Research

> For cytoskeleton, cytos, and all downstream packages

---

## Best Practices (from PEP 621, PEP 735, community)

| Rule | Rationale |
|------|-----------|
| **Feature-centric names** | Name by what it enables, not the library it installs (`aws` not `boto3`) |
| **Hyphens over underscores** | Normalized by PEP 508; `my-feature` preferred over `my_feature` |
| **Lowercase** | Standard normalization |
| **Short ≤12 chars** | Our own convention for consistency |
| **Single-word when possible** | Easier to type and remember |
| **`all` meta-extra** | Installs everything; standard pattern |
| **Separate `dev` from extras** | Use `[dependency-groups]` for dev tools, not extras |

---

## Current State

### cytoskeleton extras

| Current | Proposed | Change? | Rationale |
|---------|----------|---------|-----------|
| `gcs` | `gcs` | ✅ Keep | Feature-centric, short |
| `s3` | `s3` | ✅ Keep | Feature-centric, short |
| `cytognosis` | (disabled) | — | Not yet published |
| `linkml` | **Move to core** | ⚠️ | Per user decision: schemas are foundational |
| `swhid` | `swhid` | ✅ Keep | Feature-centric |
| `docker` | `docker` | ✅ Keep | Feature-centric |
| `workflows` | `workflows` | ✅ Keep | Already renamed from `experiments` |
| `compute` | `compute` | ✅ Keep | Already renamed |
| `catalog` | `catalog` | ✅ Keep | Already added |
| `observe` | `observe` | ✅ Keep | Already added |
| `full` | `full` | ✅ Keep | Standard pattern (without `cytognosis`, `swhid` for now) |

### cytos extras (proposed)

| Extra | What It Enables | Heavy Deps? |
|-------|----------------|-------------|
| `schemas` | Full LinkML codegen (OWL, SHACL, GraphQL, Pydantic gen) | Yes (linkml-owl, linkml-renderer) |
| `kg` | KG assembly (BioCypher, Koza, DuckDB) | Yes |
| `genomics` | VCF, TileDB-SOMA, pysam | Yes |
| `scholarly` | OpenAlex, PubMed, bibliometric + NLP (medspaCy, scispaCy) | Yes |
| `clinical` | FHIR R5, OMOP CDM adapters | Medium |
| `causal` | DoWhy, SCM, normalizing flows | Yes |
| `sensor` | Sensor data processing, AWARE adapters | Medium |
| `grants` | Grant parsing, extraction, harmonization, generation | Medium |
| `all` | Everything | Massive |

> [!NOTE]
> `nlp` merged into `scholarly` per user directive. Grants stays in cytos for now (decision pending neuros separation research).

### neuros extras (proposed)

| Extra | What It Enables |
|-------|----------------|
| `nwb` | NWB data handling, pynwb |
| `bids` | BIDS data handling |
| `connectome` | Brain connectivity processing |
| `psych` | Psychiatric instruments, PGC data |
| `nbb` | NeuroBioBank data (migrated from cytos) |
| `all` | Everything |

---

## Central Repository Naming

Following the same principles, the central `cytognosis://` URI scheme asset types should use consistent naming:

| Asset Type | URI Segment | Convention |
|-----------|-------------|------------|
| Python packages | `pkg/pypi:` | Standard PyPI naming |
| Container images | `image/` | OCI digest-based |
| Conda packages | `pkg/conda:` | conda-forge naming |
| npm packages | `pkg/npm:` | npmjs naming |
| Schemas/ontologies | `schema/` | LinkML URI |
| Datasets | `data/` | Content-addressed |
| ML models | `model/` | HF org/repo format |
| Workflows | `workflow/` | TRS ID |
| RO-Crates | `crate/` | DOI |
| Source code | `code/` | SWHID |
| Skills | `skill/` | Name@version |
| Locked envs | `env/` | Name@version |
| Dockerfiles | `docker/` | Name@version |
| Components | `component/` | Name@version |

### Zoekt Deployment

Per user comment: **`code.cytognosis.org`** (not `search.cytognosis.org`)
