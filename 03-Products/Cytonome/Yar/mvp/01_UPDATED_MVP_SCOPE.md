> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytonome`, `mvp`, `yar`

# 01 — Updated MVP Scope: Yar Skeleton-First Prototype

> **SUPERSEDED (2026-07-16):** This document is superseded. See `yar-product-spec.md` (product/spec canonical, this repo) and `yar-code-20260705-2354/ARCHITECTURE.md` (engineering canonical, in the code repo) for current state. Retained here for historical reference; not archived.

## Project title

**Yar: A Local-First Cognitive Companion for Research Capture and Personal Knowledge Graphs**

## One-line summary

Yar captures voice/text/web context from a phone, sends it to a local desktop coordinator, uses Gemma 4 to structure it into typed entities, and writes those entities into an Anytype-backed personal knowledge graph.

## MVP principle

Do **not** optimize the first build around the complete feature set.

Optimize for the skeleton:

```text
phone capture → desktop coordinator → Gemma structuring → CAP-Lite guard → Anytype MCP → LinkML-based typed objects → read/write/link operations
```

## MVP success definition

The MVP succeeds if it proves that Yar can act as a bridge between:

1. mobile/phone capture,
2. local AI coordination,
3. LinkML schema definitions,
4. Anytype Types/Objects/Properties,
5. typed research/personal memory graph operations.

The MVP does **not** need to prove full planning, full browser extension, full communication support, or full mental-health support.

## Implemented milestone status — 2026-05-17

The skeleton-first MVP is implemented, and Product Milestone 1 proves the first real mobile voice loop:

```text
Flutter mobile voice/text capture
→ on-device or backend edge VoiceIntent routing
→ CAP-Lite mobile directive
→ Yar central coordinator
→ central model router through stub/http_json/Ollama
→ SQLite graph
→ Anytype dry-run write plan
→ explicit user confirmation
→ guarded Anytype MCP write attempt
```

The default test path remains deterministic. Real central routing is opt-in through environment configuration, and this desktop has been smoke-tested with `YAR_CENTRAL_MODEL_NAME=gemma4:e4b`.

## In-scope for this MVP

### 1. Phone-side capture shell

The phone-side app was first allowed to be minimal. The current repository now includes:

- a Flutter mobile app under `mobile/`,
- the existing simple mobile web shell at `GET /`,
- voice transcript capture through platform STT,
- editable transcript fallback when STT/model runtime is unavailable.

It must support:

- text capture,
- voice transcript capture,
- sending capture payload to desktop/local coordinator.
- viewing backend/model/Anytype/CAP status.
- planning and confirming Anytype writes from selected local objects.

Real speech-to-text is implemented through the platform speech engine. The transcript field remains the reliable fallback.

### 2. Desktop/local coordinator

The desktop coordinator is the main MVP service.

Responsibilities:

- receive captures from phone,
- call Gemma 4 or a mock model interface,
- produce structured object proposals,
- run CAP-Lite guard checks,
- write/read/update/link objects via Anytype MCP or local fallback,
- return execution reports.

### 3. Anytype MCP connection

The coordinator must expose an adapter interface for Anytype MCP.

Required operations:

- list spaces,
- search objects,
- create object,
- read object,
- update object properties,
- create relation/link where supported,
- map object types and properties.

If real Anytype MCP write is unstable, the demo must fall back to local SQLite/JSON while keeping the adapter interface identical.

### 4. LinkML-to-Anytype schema mapping

The MVP must define how LinkML classes and slots map into Anytype constructs.

Minimum mapping:

| LinkML concept | Anytype concept |
|---|---|
| Class | Type |
| Slot | Property / Relation |
| Enum | Select / Tag options |
| Multivalued slot | Multi-select or relation list |
| Identifier | Object ID or external ID property |
| Required slot | Required property in validation layer |
| Class inheritance | Type template / schema metadata |

The first MVP can implement schema mapping as a local registry before pushing full schema definitions into Anytype.

### 5. Research entity types

Start with the research space shown in the screenshot.

Minimum entity types:

- Paper
- Author
- Dataset
- Code
- Method

Recommended additional types:

- Model
- Project
- Task
- Annotation
- Collection
- Concept

### 6. WADM annotation support

The MVP should include an annotation object model compatible with W3C Web Annotation Data Model patterns.

The goal is to support future browser/paper annotation flows such as:

- highlight webpage/paper,
- create Annotation object,
- link Annotation to target Paper/Webpage,
- link Annotation to user note/project/collection.

### 7. CAP-Lite safety and authority guard

CAP-Lite must be present as a small guard/execution boundary.

Minimum checks:

- only allowed object operations are executed,
- no external writes without user confirmation,
- raw captures stay local by default,
- model output must conform to schema,
- diagnostic/clinical claims are blocked,
- uncertain social interpretations must use uncertainty language if communication support is enabled later.

## Out of scope

The following are intentionally out of scope for the skeleton MVP:

- full mobile app polish,
- production mobile polish and device-farm CI,
- full browser extension,
- full Anytype schema synchronization if MCP does not support it cleanly,
- full CAP protocol implementation,
- health tracking,
- diagnosis,
- treatment advice,
- full communication coach,
- full planning engine,
- personalization model training,
- full Neuroverse phenotype stack.

## Demo objective

The demo should show:

1. A phone-side capture is submitted.
2. The desktop coordinator receives it.
3. Gemma structures it into Paper/Dataset/Code/Method/Author/Task/Annotation objects.
4. CAP-Lite approves or blocks the proposed operation.
5. The object is written to Anytype or the fallback graph.
6. The object is read back.
7. Links between objects are visible.
