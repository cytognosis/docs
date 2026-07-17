# Project Overview

Yar is a local-first cognitive companion for people who think in fragments: a voice note while walking, a task that needs breaking down, a thought that does not fit a to-do list, a mood that needs naming before it can be planned around.

The problem is not a lack of task apps. The problem is that neurodivergent attention, planning, and mood do not fit the rigid, shame-adjacent defaults most productivity tools ship with. Yar accepts messy input, structures it into typed objects in a personal knowledge graph (an append-only op-log, replayed deterministically), and keeps raw data on-device by default.

## Why It Matters

- Capture should be fast enough for fragmented attention: no forced sorting, no forced categorization.
- Raw private context should stay local by default; sync is opt-in and personal.
- Plans should have a built-in lighter version, not just a single track that becomes a source of shame when missed.
- Rest should count. Streaks that honor rest days, gaps that "pause" rather than reset.
- A hard safety boundary should block diagnosis, treatment claims, and unconfirmed data sharing, structurally, before any model call.

## Demo Scope

The demo shows a working Tauri v2 desktop app (React/TypeScript UI, Rust shell) with capture, planning (dual-track: ideal vs. baseline), a focus companion, a mood and energy map, a spatial thought map, local graph editing and linking, JSON/Markdown export, and an optional personal Django server for sync, transcription, and a GraphRAG-grounded assistant.

It intentionally does not claim clinical use, a finished mobile app, or a live bidirectional voice loop. About 22 of the 62 features in Yar's canonical feature catalog are shipped and tested today; the rest are groundwork or honest, labeled placeholders.

## Milestone Additions (this submission)

- CAP-Lite safety gate (`CapLiteGuard`) ported into the Django backend and wired as a pre-response gate on the assistant's chat and task-extraction endpoints; refuses crisis language (English and Persian), diagnosis requests, and treatment requests before any model call.
- Sync protocol (`central_oplog_pull_since_seq`) implemented and tested end to end, including idempotent replay, tie-break ordering, and tombstone handling.
- Deterministic reducer parity between the TypeScript frontend and the Python backend, verified bit-for-bit on the same op-log.
- GraphRAG-grounded assistant: retrieval over the person's own captures only, with cited sources, never external data.

Yar is fully free, with no subscription, now or planned for the near term. The founder is building this solo, for the neurodivergent community they are already embedded in.
