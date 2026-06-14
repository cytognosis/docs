# Architectural Decision Log

This document consolidates the differences between v1/v2 architecture and the current data-only focus + SurrealDB adoption.

## 1. Modeling Arc (features, models, train, evaluate, infer)

* **v1 State**: Deeply integrated first-class modules within `cytos`.
* **v2 State**: Proposed to be removed entirely, shifting to a "data-only" direction.
* **Current Decision (v3)**: We are removing the stub modeling directories (`features/`, `models/`, `train/`, `evaluate/`, `rag/`) from `src/cytos/` to enforce the data-only architecture. Machine learning pipelines will consume the exported graphs via external repositories or pipeline steps, ensuring `cytos` remains strictly a Knowledge Graph construction, harmonization, and provisioning layer.

## 2. Database Backend Strategy

* **Previous State**: Neo4j was the primary graph database backend alongside DuckDB for local build orchestration.
* **Current Decision**: Adopting SurrealDB as the primary backend to leverage its combined document-graph capabilities. 
    * Neo4j integration remains but is moved under a unified `src/cytos/db/` namespace.
    * A new, fully-featured `src/cytos/db/surrealdb/` module is introduced to handle schema generation from LinkML, data conversion, and complex graph querying.
    * Benchmarking will dictate the final transition timeline from Neo4j to SurrealDB for production environments.

## 3. Schemas Migration

* **Previous State**: Schemas lived inside `cytos/schemas/`.
* **Current Decision**: Schemas have been migrated to the `cytoskeleton` repository. A symlink (or Git submodule reference) will be maintained to allow tooling to access them transparently while avoiding duplication.

## 4. Pipeline Stages

* **Decision**: We maintain the 14 execution stages defined in `PIPELINE.md`, but modeling stages are treated as external downstream consumers rather than built-in steps of the `cytos` ingest orchestrator.
