# 00 — Context Update: Skeleton-First Direction

## Summary

The latest feedback changes the immediate implementation priority.

The MVP should **not** start by expanding the user-facing feature set. The immediate goal is to bring up the technical skeleton that proves the product can connect mobile capture, a desktop/local intelligence coordinator, Anytype MCP, LinkML schemas, and typed object operations.

## Current status — 2026-05-17

That skeleton is now present, and Product Milestone 1 has been implemented as a vertical slice:

- `mobile/` contains a Flutter app adapted from the LiteRT reference app.
- The app supports speech-to-text, editable transcript fallback, backend URL configuration, status display, local object review, Anytype write planning, and explicit write confirmation.
- The mobile app can load the public LiteRT Gemma E2B artifact through `flutter_gemma` for on-device `VoiceIntent` routing on a capable physical device.
- The backend exposes `/voice/turn`, `/voice/plan-anytype-write`, `/voice/confirm-anytype-write`, `/voice/conversations/{conversation_id}`, and `/product/status`.
- Central routing can use the deterministic stub, HTTP JSON, or Ollama-compatible provider. This desktop has the local Ollama model `gemma4:e4b`, and the real central-provider smoke test returned structured JSON with `used_fallback=false`.
- Anytype remains guarded: write planning is dry-run, and execution requires `user_confirmed_external_write=true` plus an available MCP write tool.

The current screenshot already shows a research-oriented Anytype space/channel with entity Types such as:

- Dataset
- Code
- Method
- Author
- Paper

This is exactly the right starting point. Yar should reuse this object-graph direction rather than inventing a separate database model first.

## Core correction

Previous scope:

```text
Build broad Yar features: capture, planning, communication support, KG, safety.
```

Updated scope:

```text
First build the skeleton:
phone capture → desktop/local coordinator → Anytype MCP connection → LinkML schema registration/mapping → create/read/update/link typed entities.
```

Feature richness comes later.

## Immediate technical goal

Build the smallest working system that can:

1. Receive a voice/text message from a phone-side app or mock endpoint.
2. Send it to a desktop/local coordinator service.
3. Connect from the coordinator to Anytype through MCP.
4. Register or map LinkML-style entity schemas into Anytype Types/Properties.
5. Create a typed entity instance such as Paper, Dataset, Code, Method, Author, Task, or Annotation.
6. Read back that entity from Anytype or the local fallback graph.
7. Link two entities, for example:
   - Paper → uses Dataset
   - Paper → authored_by Author
   - Code → implements Method
   - Annotation → targets Paper/Webpage
8. Preserve provenance from the original capture.

## Architectural implication

Yar has two graph layers:

### 1. Domain / entity knowledge graph

This contains reusable typed entities:

- Paper
- Dataset
- Code
- Method
- Model
- Author
- Organization
- Project
- Task
- Annotation
- Collection

### 2. Personalization / memory graph

This sits on top of the entity graph and stores user-specific context:

- what the user captured
- what the user cares about
- which papers/projects/tasks are important now
- user preferences
- user annotations
- temporal/provenance metadata
- retrieval and planning state

The personalization layer should reference domain entities rather than duplicating them.

## External reference standards and code paths

The following references should be treated as integration anchors:

- Anytype object graph and MCP adapter
- LinkML schemas for structured entity definitions
- W3C Web Annotation Data Model converted to LinkML
- Existing Cytognosis annotation schema:
  - `schemas/domains/annotation.yaml`
- Existing Cytognosis annotation code:
  - `src/cytos/scholarly/annotation.py`
- Existing AnnotationStore implementation
- Hypothesis as a web annotation reference pattern
- Memex as a browser capture/reference pattern

## What this means for the hackathon demo

The hackathon demo should show the skeleton working, not a fully polished product.

Best demo:

1. User speaks or types a research capture on the phone.
2. The phone sends it to the desktop coordinator.
3. Gemma structures it into typed entities.
4. CAP-Lite validates allowed actions.
5. The coordinator writes objects to Anytype or fallback graph.
6. The demo shows the created Types/Objects/Links.
7. The user asks for retrieval, and Yar reads back the graph.
