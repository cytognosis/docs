# YAR Architecture (v1.0)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: stakeholders
> **Tags**: `inbox`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

YAR (Your AI Representative) is a cognitive companion.

## System Overview
- **Privacy-First & On-Device**: Built for local execution using the Cytonome paradigm.
- **Component Map**:
  - API Layer (16 routers)
  - Core Logic (coordinator, model_router, voice, affect, TTS)
  - Storage Layer (SQLite + Graph representations)
  - CAP (Controller-Authority Protocol for safety and guardrails; spec in `cytoplex/`)
- **Universal Sensor Architecture**: Defined in `sensors/sensor-architecture.md` (CSP / USAP).
- **Sensor Roadmap**:
  - v0.1 Voice -> v0.2 Text -> v0.3 Facial -> v0.4 Multimodal -> v1.0 Wearables

## Dependencies
- FastAPI, Pydantic, httpx, MCP.
