# Grant & Funding Opportunity Pipeline — Documentation Hub

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This folder is the single documentation hub for all grant-related infrastructure in Cytos. It covers the canonical template system, the extraction/harmonization pipeline, testing strategy, and roadmap.

## Contents

| Document | Path | Purpose |
|---|---|---|
| **Deep Research Report** | [architecture/deep_research_report.md](architecture/deep_research_report.md) | Comprehensive findings, schema analysis, convergence status, and gap analysis |
| **Architecture Diagram** | [architecture/pipeline_architecture.md](architecture/pipeline_architecture.md) | End-to-end pipeline flow with component relationships |
| **Status Matrix** | [status/component_status.md](status/component_status.md) | Per-component implementation status (done/WIP/missing) |
| **Implementation Plan** | [plans/implementation_plan.md](plans/implementation_plan.md) | Phased plan to complete, test, and ship the pipeline |
| **Testing Strategy** | [testing/testing_strategy.md](testing/testing_strategy.md) | Unit, integration, and pressure-test plan |

## Quick Links to Source Code

| Module | Path | Status |
|---|---|---|
| Parser | [parser.py](../../src/cytos/scholarly/grants/parser.py) | ✅ Production |
| Extractor | [extractor.py](../../src/cytos/scholarly/grants/extractor.py) | ✅ Production (Llama 3.1; Nemotron pending) |
| Registry | [registry.py](../../src/cytos/scholarly/grants/registry.py) | ✅ Production |
| Harmonizer | [harmonizer.py](../../src/cytos/scholarly/grants/harmonizer.py) | ⚠️ Scaffolded (placeholder slot mapping) |
| Generator | [generator.py](../../src/cytos/scholarly/grants/generator.py) | ⚠️ Scaffolded (LLM-based, needs templates) |
| Renderer | [render.py](../../src/cytos/scholarly/grants/render.py) | ⚠️ Scaffolded (Jinja2 only, no Pandoc/Quarto wiring) |

## Quick Links to Schemas

| Asset | Path | Status |
|---|---|---|
| Manifest (v1.2) | [manifest.yaml](reusable-blocks/slot-library/manifest.yaml) | ✅ Authoritative |
| Groups & Presets | [groups.yaml](reusable-blocks/slot-library/groups.yaml) | ✅ Complete |
| Opportunity Mappings | [opportunity_mapping.yaml](reusable-blocks/slot-library/opportunity_mapping.yaml) | ✅ 71 opportunities mapped |
| Funder Profiles | [funders/](reusable-blocks/slot-library/funders) | ⚠️ 10 files / ~25 needed |
| Slot Files | [slots/](../../src/cytos/scholarly/grants/schemas/slots/) | ⚠️ 27 files; 4 authored, 23 stubs |

## Consolidation 2026-07-16

See `_consolidation-2026-07-16/CONSOLIDATION_LOG.md` for the grants and applications consolidation (plan, asset inventory, rebuilt registry, standardization sizes and values, EU/UK and entity memo, precision-psychiatry 1-pager).
