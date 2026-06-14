> **Status**: Active
> **Date**: 2026-05-29
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `steering`, `agents`

---
inclusion: always
version: 1.0.0
category: structure
description: Directory layout and module boundaries for Yar
last_updated: 2026-05-29
---

# Structure Steering: Yar

## Directory Layout

```
Yar/
├── pyproject.toml                  # Project metadata, deps, ruff/pytest config
├── README.md
├── CHANGELOG.md
├── .env.example                    # Environment variable template
│
├── src/
│   ├── yar/                        # Main application package
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app factory
│   │   ├── main_dependencies.py    # Dependency injection setup
│   │   ├── cli.py                  # CLI entry point (yar command)
│   │   ├── logging_config.py       # Structured logging configuration
│   │   ├── py.typed                # PEP 561 marker
│   │   │
│   │   ├── api/                    # FastAPI route handlers
│   │   │   ├── routes_voice.py     # Voice capture and STT endpoints
│   │   │   ├── routes_tts.py       # Text-to-speech synthesis
│   │   │   ├── routes_affect.py    # Emotional affect detection
│   │   │   ├── routes_capture.py   # Knowledge capture endpoints
│   │   │   ├── routes_retrieval.py # Semantic search and retrieval
│   │   │   ├── routes_communication.py  # Conversational AI endpoints
│   │   │   ├── routes_objects.py   # Knowledge object CRUD
│   │   │   ├── routes_schemas.py   # Schema registry endpoints
│   │   │   ├── routes_planning.py  # Task planning and proposals
│   │   │   ├── routes_anytype.py   # Anytype integration endpoints
│   │   │   ├── routes_export.py    # Data export endpoints
│   │   │   ├── routes_annotations.py  # Annotation endpoints
│   │   │   ├── routes_persona.py   # Persona management
│   │   │   ├── routes_model.py     # Model management endpoints
│   │   │   ├── routes_cap.py       # CAP protocol endpoints
│   │   │   └── routes_health.py    # Health check
│   │   │
│   │   ├── core/                   # Business logic
│   │   │   ├── voice_service.py    # Voice processing pipeline
│   │   │   ├── model_router.py     # LLM dispatch (Gemma/cloud)
│   │   │   ├── coordinator.py      # Multi-step workflow coordination
│   │   │   ├── interactive_assistant.py  # Conversational assistant logic
│   │   │   ├── proposal_validator.py    # Knowledge proposal validation
│   │   │   ├── annotation_service.py    # Annotation processing
│   │   │   ├── anytype_write_planner.py # Anytype sync planning
│   │   │   ├── object_router.py    # Knowledge object routing
│   │   │   ├── json_utils.py       # JSON parsing utilities
│   │   │   ├── gemma_router_stub.py # On-device Gemma stub
│   │   │   ├── affect/             # Emotional affect analysis
│   │   │   └── tts/                # TTS engine abstraction
│   │   │
│   │   ├── models/                 # Pydantic data models
│   │   │   ├── voice.py            # Voice/audio request/response models
│   │   │   ├── voice_affect.py     # Affect detection models
│   │   │   ├── tts.py              # TTS configuration models
│   │   │   ├── capture.py          # Capture event models
│   │   │   ├── communication.py    # Conversation models
│   │   │   ├── planning.py         # Planning/proposal models
│   │   │   ├── yar_object.py       # Knowledge object models
│   │   │   ├── schema_registry.py  # Schema type registry
│   │   │   ├── anytype.py          # Anytype sync models
│   │   │   ├── link.py             # Graph link/edge models
│   │   │   ├── model_router.py     # Model routing config models
│   │   │   ├── guard.py            # Safety guard models
│   │   │   ├── wadm.py             # WADM deployment models
│   │   │   └── proposal_validation.py  # Proposal validation schemas
│   │   │
│   │   ├── storage/                # Persistence layer
│   │   │   ├── sqlite_store.py     # SQLite-backed object/metadata store
│   │   │   ├── graph_store.py      # Neo4j graph operations
│   │   │   └── voice_stores.py     # Voice recording file storage
│   │   │
│   │   ├── integrations/           # External service adapters
│   │   │   ├── anytype/            # Anytype MCP integration
│   │   │   ├── linkml_loader.py    # LinkML schema loader
│   │   │   └── wadm_adapter.py     # wasmCloud deployment adapter
│   │   │
│   │   ├── data/                   # Static data and resources
│   │   │   ├── prompts/            # LLM prompt templates
│   │   │   └── schemas/            # LinkML schema definitions
│   │   │
│   │   └── web/                    # Static web assets
│   │       └── static/             # Frontend static files
│   │
│   └── cap/                        # Cytoplex protocol (peer subpackage)
│       ├── __init__.py             # CAP public API
│       ├── guard.py                # Authority guard enforcement
│       ├── primitives.py           # CAP message primitives
│       ├── models.py               # CAP data models
│       ├── policies.py             # Policy definitions
│       ├── protocols.py            # Protocol interfaces
│       ├── constants.py            # CAP constants
│       └── data/                   # CAP static data
│
├── apps/
│   └── mobile/                     # Flutter mobile application
│
├── tests/                          # Test suite
├── docs/                           # Documentation
├── scripts/                        # Development utilities
├── data/                           # Runtime data directory
├── logs/                           # Application logs
├── assets/                         # Static assets (icons, etc.)
├── examples/                       # Usage examples
├── third_party/                    # Third-party submodules
└── build/                          # Build artifacts
```

## Source Modules

| Module | Responsibility | Key Exports |
|--------|---------------|-------------|
| `api` | HTTP route handlers | FastAPI `APIRouter` instances per domain |
| `core` | Business logic and orchestration | `VoiceService`, `ModelRouter`, `Coordinator`, `InteractiveAssistant` |
| `models` | Pydantic request/response schemas | Domain-specific model classes shared across api and core |
| `storage` | Data persistence | `SQLiteStore`, `GraphStore`, `VoiceStores` |
| `integrations` | External service adapters | `LinkMLLoader`, `WADMAdapter`, Anytype client |
| `data` | Static resources | Prompt templates, LinkML schema YAML files |
| `web` | Static web frontend | HTML/CSS/JS served by FastAPI |
| `cap` (peer) | Authority protocol | `Guard`, `Primitives`, `Policies` — used by `api/routes_cap.py` |

## Module Boundaries

### Import Rules

- `api` imports from `core`, `models`, `storage`, and `cap`
- `core` imports from `models`, `storage`, and `integrations`
- `models` has no internal imports (leaf module)
- `storage` imports from `models` only
- `integrations` imports from `models` only
- `cap` is a standalone peer package; import as `from cap import ...`
- No direct imports from `api` into `core` or `storage`

### Test Structure

- Tests mirror source: `tests/test_routes_voice.py`, `tests/test_model_router.py`
- Fixtures in `tests/conftest.py` provide FastAPI test client and mock stores
- Integration tests marked with `@pytest.mark.live` require running Anytype instance
- Async tests use `pytest-asyncio` with `asyncio_mode = "auto"`

## Naming Conventions

| Entity | Convention | Example |
|--------|-----------|---------|
| Route files | `routes_<domain>.py` | `routes_voice.py` |
| Service classes | `PascalCase` + domain | `VoiceService` |
| Model classes | `PascalCase` | `CaptureRequest` |
| Store classes | `PascalCase` + Store | `SQLiteStore` |
| Integration adapters | `PascalCase` + Adapter/Loader | `LinkMLLoader` |
| Config constants | `UPPER_SNAKE` | `DEFAULT_SAMPLE_RATE` |
| Test files | `test_<module>.py` | `test_voice_service.py` |
| Prompt templates | `snake_case.txt` | `capture_prompt.txt` |
