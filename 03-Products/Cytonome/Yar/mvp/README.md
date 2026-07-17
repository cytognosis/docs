> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytonome`, `mvp`, `yar`

# Yar Gemma 4 Good MVP Docs — Current Scope

> **SUPERSEDED (2026-07-16):** This document is superseded. See `yar-product-spec.md` (product/spec canonical, this repo) and `yar-code-20260705-2354/ARCHITECTURE.md` (engineering canonical, in the code repo) for current state. Retained here for historical reference; not archived.

This package updates the previous Yar Gemma 4 Good hackathon scope based on the latest product/architecture feedback.

The original correction was that the immediate build should **not** focus on a broad feature set. It should first prove the technical skeleton:

1. Phone-side voice/text capture sends a message to a desktop/local coordinator.
2. The desktop coordinator establishes an MCP connection to Anytype.
3. The coordinator can register or map LinkML schemas into Anytype Types / Properties / Relations.
4. The coordinator can create, read, update, and link typed entities in Anytype.
5. The system supports research-domain entity types such as Paper, Author, Dataset, Code, Method, Model, Project, Task, Annotation, and Collection.
6. W3C Web Annotation Data Model / LinkML annotation schemas are treated as a reusable standard for browser/page/paper annotations.
7. Hypothesis and Memex are reference implementations/patterns for web annotation and browser capture.

## Current implementation status — 2026-05-17

The skeleton is now implemented and Product Milestone 1 adds the first real mobile voice vertical slice.

Implemented:

- FastAPI coordinator with `POST /capture` and the voice-specific `/voice/*` APIs.
- Flutter app under `mobile/` with status, voice, objects, Anytype plan, and settings screens.
- Platform speech-to-text with editable transcript fallback.
- On-device Gemma E2B intent-routing interface in Flutter using `flutter_gemma` and the LiteRT `.litertlm` model.
- Central Gemma E4B-compatible path through Ollama/local model server; this desktop uses `YAR_CENTRAL_MODEL_NAME=gemma4:e4b`.
- Deterministic stub providers remain the default for tests and reproducible demos.
- CAP-Lite blocks diagnosis, treatment, health-risk scoring, raw sharing without consent, and unconfirmed external writes.
- SQLite stores captures, objects, links, execution reports, schema metadata, Anytype write plans, and voice conversation turns.
- Anytype MCP status/tool discovery/search/read and guarded confirmed write execution path.
- Automated tests: `84 passed`; mobile API client tests pass; `flutter analyze` passes.

Still incomplete:

- Full Anytype type/property/schema synchronization.
- Browser extension, Hypothesis/Memex import/export, rich retrieval, personalization, planning, and production mobile release packaging.

## Files

- `00_CONTEXT_UPDATE.md` — what changed based on the latest feedback and screenshot.
- `01_UPDATED_MVP_SCOPE.md` — final skeleton-first MVP scope.
- `02_ARCHITECTURE_SCOPE.md` — detailed architecture boundary and system layers.
- `03_LINKML_ANYTYPE_MAPPING.md` — mapping LinkML classes/slots to Anytype Types/Properties/Relations.
- `04_ENTITY_MODEL.md` — initial research/personalization entity model.
- `05_TASK_LIST.md` — prioritized build task list.
- `06_WADM_ANNOTATION_INTEGRATION.md` — W3C Web Annotation / LinkML / AnnotationStore integration plan.
- `07_ARCHITECTURE_DESIGN_PROMPT.md` — copy-paste prompt for generating the detailed architecture.
- `08_DEMO_FLOW.md` — skeleton-first demo script.
- `09_RISKS_AND_ACCEPTANCE_CRITERIA.md` — risks, fallback paths, and pass/fail criteria.
- `11_SETUP_CENTRAL_AND_MOBILE.md` — macOS/Ubuntu central model setup and iOS/Android install scripts.
- `PRODUCT_MILESTONE_1_MOBILE_VOICE.md` — implemented mobile voice architecture, setup, demo script, limitations, and next steps.
