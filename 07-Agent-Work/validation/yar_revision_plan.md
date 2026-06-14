# Yar Repository Revision Plan — Complete Step-by-Step

> **Status**: Draft (pending review)
> **Date**: 2026-05-17
> **Scope**: Yar as an independent repo/package. Modularization of schemas, CAP, and interfaces into individual repos is a separate future phase.

---

## Executive Summary

This plan revises Yar from its current hackathon-MVP state into a publishable, well-documented, clean Python package. It covers 6 phases across ~25 work items, addressing: project structure, code quality, Anytype submodule, CAP integration, interface organization, documentation, and publishing readiness.

---

## Phase 0: Audit & Cleanup Foundation (Days 1-2)

### 0.1 Migrate build system to hatchling

**Current**: `setuptools` in `pyproject.toml`. **Target**: `hatchling` (Cytognosis standard per cytognosis-dev skill).

```diff
-[build-system]
-requires = ["setuptools>=69.0"]
-build-backend = "setuptools.build_meta"
-[tool.setuptools.packages.find]
-where = ["src"]
+[build-system]
+requires = ["hatchling"]
+build-backend = "hatchling.build"
+[tool.hatch.build.targets.wheel]
+packages = ["src/yar"]
```

### 0.2 Add Ruff + ty configuration

Add to `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py312"
src = ["src"]

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM", "RUF"]

[tool.ruff.lint.isort]
known-first-party = ["yar"]
```

### 0.3 Run Ruff autofix across entire codebase

```bash
ruff check --fix src/ tests/
ruff format src/ tests/
```

### 0.4 Add missing `__all__` exports to all `__init__.py`

Audit each package init and declare explicit public API.

### 0.5 Add `py.typed` marker

Create `src/yar/py.typed` (empty file) for PEP 561 compliance.

### 0.6 Consolidate environment variables

**Current**: env vars scattered across `cap_lite_guard.py`, `model_router.py`, `voice_service.py`, `anytype_mcp_adapter.py`, `logging_config.py`.
**Target**: Single `src/yar/config.py` using Pydantic `BaseSettings`:

```python
from pydantic_settings import BaseSettings

class YarSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="YAR_")
    router_provider: str = "ollama_cli"
    model_name: str = "gemma4:e4b"
    model_fallback_to_stub: bool = False
    model_timeout_seconds: int = 180
    log_level: str = "INFO"
    cap_http_url: str = "http://localhost:7100"
    cap_timeout_secs: float = 10.0
    anytype_mcp_enabled: bool = False
    # ... all other env vars
```

### 0.7 Remove dead code and backup files

- Remove `*.bak`, `*.pre-phase1.bak` files
- Remove any `__pycache__` directories from version control
- Audit for unused imports across all modules

---

## Phase 1: Anytype Submodule (Days 2-4)

### 1.1 Create `src/yar/anytype/` subpackage (NOT `packages/yar-anytype/`)

> [!IMPORTANT]
> Per the user's request, the Anytype submodule lives INSIDE `src/yar/anytype/` as part of the Yar package, not as a separate package. This keeps Yar self-contained as a single publishable package.

```
src/yar/anytype/
├── __init__.py          # Public API exports
├── client.py            # AnytypeMCPClient (connection, lifecycle, health)
├── discovery.py         # Tool discovery (search/read/write tool name resolution)
├── push.py              # Write operations (create, update, delete objects/links/relations)
├── pull.py              # Read operations (search, get object, list types, read links)
├── schema_bridge.py     # LinkML ↔ Anytype type/property mapping
├── guard.py             # CAP-Lite guard integration for write operations
├── models.py            # Pydantic models for Anytype payloads
└── errors.py            # Typed error hierarchy
```

### 1.2 Port `anytype_mcp_adapter.py` (48 KB) into subpackage

Split the monolithic adapter into focused modules:

| Target Module | Source Functions to Port |
|---|---|
| `client.py` | `AnytypeMCPAdapter.__init__`, `_start_mcp`, `_stop_mcp`, `status`, `health` |
| `discovery.py` | `_discover_tools`, `_find_search_tool`, `_find_read_tool`, `_find_write_tool` |
| `push.py` | `write_object`, `write_link`, `execute_write_plan`, `bulk_push` (new) |
| `pull.py` | `search`, `read_object`, `read_links`, `list_types` |
| `schema_bridge.py` | `_map_yar_type_to_anytype`, `linkml_to_anytype_payload`, type mapping dicts |
| `guard.py` | Write guard checks (extract from `anytype_write_planner.py` + `cap_lite_guard.py`) |
| `models.py` | `AnytypeWritePlan`, `AnytypeWriteResult`, `AnytypeSearchResult` (extract from `models/anytype.py`) |
| `errors.py` | `AnytypeError`, `AnytypeConnectionError`, `AnytypeWriteRefused`, etc. |

### 1.3 Implement full `AnytypeMCPClient`

```python
class AnytypeMCPClient:
    """Persistent MCP client with connection pooling and retry."""
    
    def __init__(self, settings: AnytypeSettings):
        self._settings = settings
        self._process: subprocess.Popen | None = None
        self._tools: dict[str, Any] = {}
    
    async def connect(self) -> None: ...
    async def disconnect(self) -> None: ...
    async def health(self) -> bool: ...
    async def discover_tools(self) -> dict[str, Any]: ...
    async def call_tool(self, tool_name: str, args: dict) -> Any: ...
```

### 1.4 Implement schema bridge with full LinkML support

```python
# Schema bridge maps between Yar's LinkML types and Anytype object types
YAR_TO_ANYTYPE_TYPE = {
    "Note": "ot-note", "Task": "ot-task", "Idea": "ot-idea",
    "Project": "ot-project", "Person": "ot-human", "Paper": "ot-note",
    "Webpage": "ot-bookmark", "Decision": "ot-note", "Reflection": "ot-note",
    "MessageDraft": "ot-note",
}

YAR_TO_ANYTYPE_RELATION = {
    "related_to": "rel-related", "authored_by": "rel-author",
    "annotates": "rel-linked", "uses_dataset": "rel-linked",
}

def yar_object_to_anytype_payload(obj: YarObject) -> dict[str, Any]:
    """Convert a validated YarObject to an Anytype create-object payload."""
    ...

def anytype_object_to_yar(raw: dict[str, Any]) -> YarObject:
    """Convert an Anytype object response to a YarObject."""
    ...
```

### 1.5 Implement push/pull with CAP guard integration

Every write operation flows through:
```
push.write_object() → guard.check_write_permission() → client.call_tool()
```

Every pull operation is unguarded (read-only).

### 1.6 Update routes to use new subpackage

Replace `from yar.integrations.anytype_mcp_adapter import ...` with `from yar.anytype import ...` across all route modules.

### 1.7 Deprecate old adapter

Mark `src/yar/integrations/anytype_mcp_adapter.py` as deprecated with a module-level warning. Keep for one release cycle, then remove.

### 1.8 Add comprehensive tests

```
tests/anytype/
├── test_client.py
├── test_discovery.py
├── test_push.py
├── test_pull.py
├── test_schema_bridge.py
├── test_guard.py
└── conftest.py          # Shared fixtures (mock MCP subprocess)
```

---

## Phase 2: CAP Integration Cleanup (Days 4-5)

### 2.1 Consolidate CAP code locations

**Current state**: CAP code is split across 3 locations:
1. `src/yar/cap_profile.py` (12 KB) — primitives factory
2. `src/yar/core/cap_lite_guard.py` (21.6 KB) — in-process guard
3. `CAP/` directory at root — integration shims, policies, schemas

**Target**: Single `src/yar/cap/` subpackage:

```
src/yar/cap/
├── __init__.py          # Public API: evaluate, is_allowed, refuse, report
├── profile.py           # Moved from cap_profile.py (directive/refusal/report factories)
├── guard.py             # CAP-Lite guard logic (in-process + optional sidecar client)
├── policies.py          # Policy definitions (extracted from CAP/policies/*.json)
├── models.py            # CAP Pydantic models (Directive, GuardDecision, RefusalMessage, etc.)
└── sidecar.py           # HTTP client for external CAP sidecar (optional)
```

### 2.2 Make sidecar optional with graceful fallback

```python
# cap/__init__.py
async def evaluate(directive: Directive) -> GuardDecision:
    """Evaluate via sidecar if available, else use in-process guard."""
    if settings.cap_sidecar_enabled:
        return await sidecar.evaluate_directive(directive.model_dump())
    return guard.evaluate_local(directive)
```

### 2.3 Type CAP models with Pydantic

Replace raw dict factories in `cap_profile.py` with proper Pydantic models:

```python
class Directive(BaseModel):
    directive_id: str = Field(default_factory=lambda: f"yar-dir-{uuid4()}")
    directive_type: Literal["execute", "observe", "compensate", "wait"] = "execute"
    action: DirectiveAction
    constraints: ConstraintSet
    authority_chain: list[AuthorityChainStep]
    policy_refs: list[PolicyRef]
    expiry: datetime
    reversibility: Literal["reversible", "partial", "irreversible"]
```

### 2.4 Move policies to data files

Move `CAP/policies/cap_core_policy.json` and `cap_med_policy.json` to `src/yar/cap/data/` and load via `importlib.resources`.

### 2.5 Clean up root `CAP/` directory

After consolidation, the root `CAP/` directory retains only:
- `README.md` (pointer to `src/yar/cap/` and external CAP repo)
- `schemas/` (JSON Schemas for reference, not runtime)

---

## Phase 3: Code Quality & Structure (Days 5-7)

### 3.1 Reduce module sizes

Split oversized modules:

| Module | Current Size | Action |
|---|---|---|
| `model_router.py` | 23.6 KB | Extract `OllamaProvider`, `HttpJsonProvider`, `DisabledProvider` into `core/providers/` |
| `voice_service.py` | 19 KB | Extract edge/central routing into `core/voice/edge.py` and `core/voice/central.py` |
| `routes_anytype.py` | 15.3 KB | Will naturally shrink after anytype subpackage migration |
| `routes_retrieval.py` | 12.8 KB | Extract retrieval logic into `core/retrieval.py`; routes become thin |
| `routes_communication.py` | 11.1 KB | Extract translation logic into `core/communication.py` |

### 3.2 Add type hints to all function signatures

Run `ty` (Astral type checker) and fix all errors:

```bash
ty check src/yar/
```

### 3.3 Add Google-style docstrings to all public functions

Every public function and class gets a docstring with Args, Returns, and Raises sections.

### 3.4 Standardize error handling

Create `src/yar/errors.py` with typed exception hierarchy:

```python
class YarError(Exception): ...
class CaptureError(YarError): ...
class GuardRefusalError(YarError): ...
class ModelRoutingError(YarError): ...
class AnytypeError(YarError): ...
class SchemaValidationError(YarError): ...
```

### 3.5 Add structured logging throughout

Replace raw `print()` and inconsistent `logger` usage with structured logging using the existing `logging_config.py` foundation.

---

## Phase 4: Interface Organization (Days 7-9)

### 4.1 Evaluate current interface layout

| Interface | Current Location | Status | Tech |
|---|---|---|---|
| Mobile | `mobile/` | Functional MVP | Flutter/Dart |
| Web Shell | `src/yar/web/static/` | Functional, basic | HTML/CSS/JS |
| Desktop | — | Not started | Planned: Tauri |
| Extension | — | Not started | Planned: MV3 |

### 4.2 Restructure into `interfaces/` directory

```
interfaces/
├── README.md                    # Interface overview + how to add new ones
├── mobile/                      # Move from mobile/ (Flutter)
│   ├── lib/
│   ├── pubspec.yaml
│   ├── android/
│   ├── ios/
│   └── macos/
├── web/                         # Move from src/yar/web/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── desktop/                     # Scaffold (Tauri)
│   ├── README.md
│   └── .gitkeep
└── extension/                   # Scaffold (MV3)
    ├── README.md
    └── .gitkeep
```

### 4.3 Update backend to serve web from new location

```python
# main.py
WEB_STATIC_DIR = Path(__file__).parent.parent.parent.parent / "interfaces" / "web"
```

### 4.4 Add shared API client specification

Create `interfaces/shared/api_client_spec.md` documenting all backend endpoints with request/response shapes. Every interface implements against this spec.

### 4.5 Plan for next-phase modularization

Document in `interfaces/MODULARIZATION_PLAN.md`:
- Phase A: Mobile moves to `cytoskeleton/assets/templates/app-phone/` (Jinja2 template)
- Phase B: Desktop scaffold via cytocast `yar-desktop` profile
- Phase C: Extension scaffold via cytocast `yar-extension` profile
- Phase D: Web app migrates to Vite + framework (if needed)
- All interfaces consume the same backend API; no interface-specific backend code

---

## Phase 5: Documentation (Days 9-11)

### 5.1 Rewrite `README.md`

Replace the current 33 KB README (which is mostly API documentation) with a focused 3-5 KB README:

- What Yar is (2 paragraphs)
- Quickstart (5 commands)
- Architecture diagram (Mermaid)
- Link to full docs
- Built with / License / Acknowledgments

### 5.2 Create `docs/` directory structure

```
docs/
├── README.md                    # Docs index
├── architecture.md              # System architecture + diagrams
├── api-reference.md             # Full API documentation (moved from README)
├── cap-integration.md           # How CAP works in Yar
├── anytype-integration.md       # Anytype submodule documentation
├── schema-system.md             # Schema registration + validation
├── development.md               # Contributing + dev setup
├── deployment.md                # Running in production
├── adrs/                        # Architecture Decision Records
│   ├── ADR-001-local-first.md
│   ├── ADR-002-cap-as-sidecar.md
│   ├── ADR-003-gemma-on-device.md
│   └── ADR-004-anytype-optional.md
└── guides/
    ├── voice-capture.md
    ├── gentle-planning.md
    └── communication-translator.md
```

### 5.3 Add inline module docstrings

Every `__init__.py` gets a module-level docstring explaining the subpackage's purpose and public API.

### 5.4 Generate API reference

Use the existing route definitions to auto-generate OpenAPI spec:

```bash
python -c "from yar.main import app; import json; print(json.dumps(app.openapi(), indent=2))" > docs/openapi.json
```

### 5.5 Add CHANGELOG.md

Following Keep a Changelog format with Semantic Versioning.

---

## Phase 6: Publishing Readiness (Days 11-13)

### 6.1 Add LICENSE file

Apache 2.0 (per Cytognosis standard).

### 6.2 Add `.github/` CI scaffolds

```
.github/
├── workflows/
│   ├── ci.yml                   # Ruff + ty + pytest on PR
│   ├── release.yml              # Tag → PyPI publish
│   └── mobile.yml               # Flutter test (mobile/)
└── CODEOWNERS
```

### 6.3 Add `noxfile.py`

```python
import nox

@nox.session(python=["3.12", "3.13"])
def tests(session):
    session.install(".[dev]")
    session.run("pytest", "-v", "--tb=short")

@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "src/", "tests/")
    session.run("ruff", "format", "--check", "src/", "tests/")

@nox.session
def typecheck(session):
    session.install(".[dev]")
    session.run("ty", "check", "src/yar/")
```

### 6.4 Add `.cytognosis-config.yaml`

Per cytognosis-dev skill standard. Declares profile, cytoskeleton ref, skills, schemas, templates.

### 6.5 Update `pyproject.toml` with full metadata

```toml
[project]
name = "cytognosis-yar"
version = "0.2.0"
description = "Local-first cognitive companion for neurodivergent knowledge capture"
authors = [{name = "Cytognosis Foundation", email = "dev@cytognosis.org"}]
license = {text = "Apache-2.0"}
readme = "README.md"
requires-python = ">=3.12"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Framework :: FastAPI",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
```

### 6.6 Final verification

```bash
ruff check src/ tests/
ruff format --check src/ tests/
ty check src/yar/
pytest -v --tb=short
python -c "from yar.main import app; print('OK')"
```

---

## Summary: Target File Tree (Post-Revision)

```
Yar/
├── .cytognosis-config.yaml
├── .github/workflows/
├── CHANGELOG.md
├── LICENSE
├── README.md                        # Focused 3-5 KB
├── noxfile.py
├── pyproject.toml                   # hatchling + full metadata
├── docs/                            # Comprehensive documentation
│   ├── architecture.md
│   ├── api-reference.md
│   ├── cap-integration.md
│   ├── anytype-integration.md
│   ├── adrs/
│   └── guides/
├── interfaces/                      # All user-facing interfaces
│   ├── mobile/                      # Flutter (moved from mobile/)
│   ├── web/                         # Static shell (moved from src/yar/web/)
│   ├── desktop/                     # Scaffold
│   └── extension/                   # Scaffold
├── schemas/                         # JSON Schemas (kept for reference)
├── examples/                        # Demo data
├── scripts/                         # Setup + demo scripts
├── src/yar/                         # Python backend
│   ├── __init__.py
│   ├── config.py                    # Pydantic BaseSettings (centralized)
│   ├── errors.py                    # Typed exception hierarchy
│   ├── main.py                      # FastAPI app factory
│   ├── logging_config.py
│   ├── api/                         # Route modules (thin)
│   ├── core/                        # Business logic
│   │   ├── providers/               # Model providers (ollama, http, disabled)
│   │   ├── voice/                   # Voice pipeline (edge, central)
│   │   ├── retrieval.py
│   │   ├── communication.py
│   │   └── ...
│   ├── cap/                         # CAP integration subpackage
│   │   ├── profile.py
│   │   ├── guard.py
│   │   ├── models.py
│   │   ├── policies.py
│   │   ├── sidecar.py
│   │   └── data/                    # Policy JSON files
│   ├── anytype/                     # Anytype MCP subpackage
│   │   ├── client.py
│   │   ├── discovery.py
│   │   ├── push.py
│   │   ├── pull.py
│   │   ├── schema_bridge.py
│   │   ├── guard.py
│   │   ├── models.py
│   │   └── errors.py
│   ├── models/                      # Pydantic models
│   ├── storage/                     # SQLite + Graph
│   └── prompts/                     # LLM prompt templates
└── tests/
    ├── conftest.py
    ├── anytype/                      # Anytype subpackage tests
    ├── cap/                          # CAP subpackage tests
    └── ...                           # Existing tests (reorganized)
```

---

## Dependency on Future Phases

| Item | This Plan | Future Phase |
|---|---|---|
| CAP as repo | Stays as subpackage in Yar | Separate `github.com/cytognosis/cap` repo |
| Schemas | JSON Schemas in `schemas/` | Migrate to LinkML in `cytoskeleton` |
| Interfaces | Reorganized in `interfaces/` | Each becomes a cytocast-templated app |
| cyto-skills | Not integrated | JS/Node.js rewrite + Yar integration |
| Multi-tenant CAP | Not in scope | CAP v2 |
| Desktop/Extension | Scaffolded only | Full Tauri + MV3 implementations |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Anytype adapter refactor breaks existing tests | Medium | High | Run full test suite after each module port; keep old adapter until all tests pass |
| CAP sidecar unavailable during development | Low | Medium | In-process guard fallback always available |
| Interface reorganization breaks static file serving | Low | Low | Update path in `main.py`; test `/` route |
| Type checking reveals deep issues | Medium | Medium | Fix incrementally; allow `# type: ignore` for genuinely untyped third-party code |
| README reduction loses important information | Low | Medium | Move all API docs to `docs/api-reference.md` before trimming README |
