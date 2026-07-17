> **Status**: Active
> **Date**: 2026-05-29
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `steering`, `agents`

---
inclusion: always
version: 1.0.0
category: tech
description: Technology stack and architecture patterns for Yar
last_updated: 2026-05-29
---

# Tech Steering: Yar

> **SUPERSEDED (2026-07-16):** This document is superseded. See `yar-product-spec.md` (product/spec canonical, this repo) and `yar-code-20260705-2354/ARCHITECTURE.md` (engineering canonical, in the code repo) for current state. Retained here for historical reference; not archived.

## Stack

| Layer | Technology | Version / Variant | Notes |
|-------|-----------|-------------------|-------|
| Language | Python | 3.12+ | Backend runtime |
| Framework | FastAPI | >=0.111.0 | Async REST API with auto-generated OpenAPI |
| Graph DB | Neo4j | 5.x | Knowledge graph persistence (via `neo4j` driver) |
| Relational DB | SQLite | — | Local object/voice metadata storage |
| Mobile | Flutter | — | Cross-platform mobile app (`apps/mobile/`) |
| Desktop | Tauri | — | Lightweight desktop shell (planned) |
| Extension | Chrome MV3 | — | Browser extension for web capture (planned) |
| Voice STT | Whisper | — | Speech-to-text transcription |
| Voice TTS | Kokoro (on-device) | 82M | Text-to-speech synthesis with affect; ElevenLabs is design-time voice-design tooling only, not a runtime dependency (see `spec/SPEC-personas-voice.md`) |
| On-device LLM | Gemma | — | Local model routing for privacy-first inference |
| Validation | Pydantic | >=2.7.0 | Request/response model validation |
| HTTP Client | httpx | >=0.27.0 | Async HTTP for integrations |
| Build System | hatchling | >=1.21.0 | PEP 517 build backend |
| Dependency Mgr | uv | — | Fast dependency resolution and lockfiles |
| Linter/Formatter | ruff | >=0.11.0 | Unified Python linting and formatting |
| Testing | pytest | >=8.2.0 | Test runner with async support |
| Task Queue | Celery + Redis | — | Background task processing (planned) |
| Integration | Anytype | — | Bi-directional knowledge object sync via MCP |
| Protocol | CAP/Cytoplex | — | Agent authority protocol (bundled in `src/cap/`) |

## Architecture Patterns

### Multi-App Monorepo

Yar is a monorepo hosting the Python backend alongside client applications:

```
src/yar/          → FastAPI backend (importable package)
src/cap/          → Cytoplex protocol (bundled peer subpackage)
apps/mobile/      → Flutter mobile client
```

Both `yar` and `cap` are included in the wheel build (`tool.hatch.build.targets.wheel.packages`).

### Voice Pipeline Architecture

```
Microphone → Whisper STT → Intent Classification → Model Router
                                                      ↓
                                            ┌─────────┴──────────┐
                                            │ Local (Gemma)      │
                                            │ Cloud (API)        │
                                            └─────────┬──────────┘
                                                      ↓
                                            Response → Kokoro TTS (on-device) → Speaker
```

### Key Design Decisions

- **Voice-first**: All capture flows start from voice; text is secondary input
- **Model router**: Dispatches inference between on-device Gemma and cloud APIs based on complexity/privacy
- **CAP integration**: Agent communication follows the Cytognosis Authority Protocol for trust and authority levels
- **LinkML schemas**: Knowledge graph types defined in LinkML, loaded at runtime via `integrations/linkml_loader.py`
- **WADM adapter**: wasmCloud Application Deployment Manager adapter for distributed deployment

### API Conventions

- All routes live in `api/routes_*.py`, grouped by domain (voice, capture, retrieval, etc.)
- Route files export a `router = APIRouter(prefix="/api/v1/<domain>")`
- Core business logic lives in `core/`, routes are thin wrappers
- Models (Pydantic) in `models/` are shared across routes and core

## Dependency Policy

### Adding Dependencies

1. Core runtime deps in `[project.dependencies]` — keep minimal
2. Integration-specific deps in `[project.optional-dependencies]` (e.g., `anytype`, `dev`)
3. Dev tools in `[dependency-groups.dev]`
4. Pin minimum versions with `>=`; avoid exact pins

### Prohibited Patterns

- No `requirements.txt` as dependency source (use `pyproject.toml` exclusively)
- No direct import of `cap` from `yar.core`; use protocol interfaces
- No synchronous blocking calls in route handlers (use `async`/`await`)
- Do not store secrets in code; use `.env` with `python-dotenv`
