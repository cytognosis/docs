# SSSOM Cross-Ontology Mapping

> Cross-ontology mapping at Cytognosis lives as data, not as bespoke code. We use the Simple Standard for Sharing Ontology Mappings (SSSOM) to round-trip between UMLS, MONDO, HP, CL, CHEBI, NCBITaxon, SNOMED CT and the Cytognosis [scholarly knowledge graph](scholarly-knowledge-graph.md), and we hand SSSOM tables to downstream consumers (NCATS Translator, CELLxGENE, internal LLMs) without rewriting them.

The full hands-on writeup with worked examples (download SNOMED CT exports, validate, convert to RDF, apply SNOMED → MONDO mappings before CELLxGENE schema validation) was migrated into this repo on 2026-07-02 and lives at:

- [`sssom-tooling-handbook.md`](sssom-tooling-handbook.md) (this repo)

This document captures the architectural decision and serves as the canonical pointer.

## Why SSSOM

A normalized mapping table that anyone in the ecosystem can validate and reload is preferable to:

- Bespoke Python dictionaries scattered across notebooks.
- Vendor-specific crosswalks that don't survive a tooling upgrade.
- Free-text mapping tables that drift silently.

SSSOM gives us:

- **A LinkML schema** (`sssom-schema`) for mapping records — compatible with the Cytognosis scholarly KG schema by construction.
- **A canonical TSV serialization** with prefixes / metadata in a YAML preamble.
- **First-class provenance** — match type, confidence, justification, mapping author, mapping tool, mapping date.
- **Round-trippability** to RDF, JSON, and (via Koza) Biolink-compliant KGX.

## Chosen tooling stack

| Component | Role |
| --- | --- |
| `sssom-schema` | LinkML source of truth. Imported into the Cytognosis schema rather than redefined. |
| `sssom` (sssom-py) | I/O, validation, `MappingSetDataFrame`, set algebra (intersect / union / difference), format conversion. |
| `oaklib` (`runoak`) | Ontology access. `runoak lexmatch`, `runoak mappings`, `runoak diff` — bridges OLS / BioPortal / UMLS / SNOMED. |
| `curies` + `prefixmaps` | CURIE expansion / contraction, driven from `bioregistry`. |
| `koza` | LinkML-native ETL. Consumes SSSOM for normalization. Emits Biolink-compliant KGX. |
| `linkml` | Codegen — Pydantic, JSON Schema, OWL, SHACL, SQL DDL from the unified schema. |
| `boomer` *(optional)* | Probabilistic refinement of candidate mappings. |
| `biomappings` *(optional)* | Community-curated mappings, useful as a seed. |

## Single-cell integration (hybrid pattern)

Single-cell datasets need both **structural** validation (does this AnnData have `X`, `var`, `obsm`?) and **semantic** validation (does `obs.disease_ontology_term_id` use the MONDO IDs that CELLxGENE expects?). We split that responsibility:

- **Structural** — CZI's `cellxgene-schema validate` is the right tool; no custom code competes with it.
- **Semantic** — LinkML + OAK + SSSOM. Source vocabularies in `obs` (e.g. SNOMED CT codes from a clinical site) are mapped through SSSOM to the CL / MONDO / NCBITaxon IDs that CELLxGENE requires.

The worked SNOMED CT example in [`sssom-tooling-handbook.md`](sssom-tooling-handbook.md) demonstrates this end-to-end.

## OLS4 SSSOM endpoint

EBI's OLS4 publishes SSSOM exports for its hosted ontologies at:

```text
https://www.ebi.ac.uk/ols4/api/v2/ontologies/{ontology}/exports/sssom
```

For SNOMED CT specifically, pin the OLS4 release tag in CI rather than fetching `latest`, because SNOMED's IDs are stable but mapping coverage is not. The TSV exports we keep on hand should live under `Infrastructure and Tooling/sssom/` in the workspace folder.

> **Verification note** — verify the OLS4 URL pattern resolves the specific ontology you intend to fetch before automating a pipeline against it. Coverage varies per ontology (some have full SSSOM exports, some do not).

## Integration with the scholarly KG

When extending the [scholarly KG schema](scholarly-knowledge-graph.md):

- Import `sssom_schema` directly in the YAML.
- Add an `EntityMapping` subclass of the SSSOM `Mapping` class that links each mapping back to a `ResearchObject` for provenance — i.e. *who produced this mapping, in what release, against which source corpus*.
- Treat SSSOM TSVs in `Infrastructure and Tooling/sssom/` as build-time inputs to ingestion.

## Open follow-ups

- Pin OLS4 SNOMED CT release slug in CI.
- Store curated SSSOM TSVs at `Infrastructure and Tooling/sssom/`.
- Wire `sssom validate` into CI alongside `linkml validate`.
- Decide which mappings publish externally (under permissive license) vs. which stay internal.

## Cross-references

- [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md) — the LinkML schema that imports SSSOM.
- [`paper-library-architecture.md`](paper-library-architecture.md) — the corpus the mappings are applied to during enrichment.
- [`linkml-kg-playbook.md`](linkml-kg-playbook.md) — chapter 14 covers the full SSSOM workflow with OLS4 SNOMED CT; chapter 18 covers AnnData harmonization.

---
**Document Owner**: Chief Data Officer, Cytognosis Foundation
**Last Updated**: May 2026
**Status**: Stack chosen and documented; CI integration outstanding
**Classification**: Internal Use Only
