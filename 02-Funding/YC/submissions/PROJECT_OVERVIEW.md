# Project Overview

Yar is a local-first capture and graph-coordination prototype for people who collect ideas across notes, webpages, papers, datasets, and conversations.

The problem is not a lack of note apps. The problem is that scattered captures often remain unstructured, hard to retrieve, and risky to send to external systems by default. Yar accepts messy input, proposes typed graph objects, validates them against local schema metadata, applies CAP-Lite guardrails, and stores the result in a local SQLite graph store.

## Why It Matters

- Capture should be fast enough for fragmented attention.
- Raw private context should stay local by default.
- Structured knowledge should be reviewable and editable.
- External writes should be planned before they execute.
- Safety boundaries should block diagnosis, treatment, unsupported mind-reading, and unconfirmed data sharing.

## Demo Scope

The demo shows a working local coordinator, mobile-first web UI, Flutter mobile voice slice, deterministic model-router stub, optional Ollama-compatible central model routing, schema-aware validation, WADM annotation capture, local graph editing, and guarded Anytype write planning/execution.

It intentionally does not claim clinical use, production Anytype synchronization, or production-grade mobile release readiness.

## Product Milestone 1 Additions

- Flutter app in `mobile/` with Status, Voice, Objects, Anytype Plan, and Settings screens.
- Platform speech-to-text plus editable transcript fallback.
- On-device Gemma E2B `VoiceIntent` routing interface through `flutter_gemma`.
- Backend `/voice/*` APIs for voice turns, Anytype plan creation, confirmed write execution, and conversation history.
- Central Ollama-compatible route tested locally with `gemma4:e4b`.
- CAP-Lite remains the boundary before model routing and before external writes.
