# Self-Hosted Core Services Infrastructure

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This directory is the **single source of truth** for self-hosted Cytognosis services and the architectural / evaluation reports behind them. All services are orchestrated via the [Container Framework](../../container_framework/README.md) using a modular Docker / Podman composition.

The services here support both day-to-day team operations (scheduling, whiteboarding, knowledge management) and the research stack (Neo4j, Jupyter, MLflow). The research stack interlocks tightly with the [Data Strategy & Compliance](../data-strategy/README.md) hub — see in particular the [sovereign paper library architecture](../data-strategy/paper-library-architecture.md) and the [scholarly knowledge graph schema](../data-strategy/scholarly-knowledge-graph.md).

## Architectural evaluations and planning

These documents formally evaluate platforms before they were standardized on.

- **[Cal.com Architecture](calcom_architecture.md)** — HIPAA-aware scheduling at `cal.cytognosis.org`.
- **[Logseq & Knowledge Platform](logseq_knowledge_architecture.md)** — researcher-facing knowledge stack: Zotero (metadata only) + Logseq + Excalidraw + Hypothes.is (W3C Web Annotation) + Neo4j (KG). Updated to align with the sovereign paper library architecture.
- **[Excalidraw & Mermaid](whiteboard_mermaid_architecture.md)** — real-time collaboration and diagram tooling. Note: the original Zotero self-hosting plan in this doc is superseded; see the doc itself for context.
- **[MLflow Architecture](mlflow_architecture.md)** — experiment tracking and model registry for the MLOps pipelines.
- **[Bundled Master Plan](bundled_master_plan.md)** — the historical strategy that produced the unified `core` and `research` stacks. Now operational; refer to the Container Framework for runtime detail.
- **[Deployment Walkthrough](deployment_walkthrough.md)** — snapshot of the live deployment (containers, hosts, DNS).

## Operational matrix

For runtime configuration of these services, see [`container_framework/configs/`](../../container_framework/configs/) — `services/*.yaml` for individual service definitions and `stacks/*.yaml` for the composed stacks (`core`, `research`, `neo4j-only`).
