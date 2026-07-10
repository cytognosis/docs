# Yar Revision Plan — Status Tracker

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: stakeholders
> **Tags**: `inbox`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Updated**: 2026-05-17
> **Scope**: Yar as an independent repo/package. Schema/CAP/interface modularization into separate repos is a future phase.

## Phase Completion Summary

| Phase | Name | Status | Progress |
|---|---|---|---|
| 0 | Audit & Cleanup Foundation | 🟡 Partial | 5/7 done |
| 1 | Anytype Submodule | 🟢 Complete | Refactored + REST client + 35 tests |
| 2 | CAP Integration Cleanup | 🟢 Complete | Consolidated subpackage + 81 tests |
| 3 | Code Quality & Structure | 🟡 Partial | Ruff done; type hints, docstrings, error hierarchy pending |
| 4 | Interface Organization | 🔲 Not started | 0/5 |
| 5 | Documentation | 🟢 Complete | 34 docs consolidated in `docs/` |
| 6 | Publishing Readiness | 🟡 Partial | CHANGELOG exists; LICENSE, CI, nox pending |

---

## Phase 0: Audit & Cleanup

| Task | Status | Notes |
|---|---|---|
| 0.1 Migrate to hatchling | ✅ Done | `pyproject.toml` uses hatchling |
| 0.2 Add Ruff config | ✅ Done | Configured in `pyproject.toml` |
| 0.3 Ruff autofix | ✅ Done | Clean: `ruff check --fix` + `ruff format` |
| 0.4 `__all__` exports | ✅ Done | All `__init__.py` have explicit exports |
| 0.5 `py.typed` marker | ✅ Done | `src/yar/py.typed` created |
| 0.6 Centralized `YarSettings` | 🔲 TODO | Env vars scattered across 5+ modules |
| 0.7 Remove dead code | 🔲 TODO | Old monolith deleted; check for `.bak` files |

## Phase 1: Anytype Submodule ✅

| Task | Status | Notes |
|---|---|---|
| 1.1 Create subpackage | ✅ Done | `src/yar/integrations/anytype/` (10 modules) |
| 1.2 Port monolith | ✅ Done | 1,283 → 558 lines in adapter |
| 1.3 Direct REST client | ✅ Done | `client.py`: 36 endpoints, rate-limited |
| 1.4 Schema bridge | ✅ Done | `_schema_mapper.py` + `_payload_mapper.py` |
| 1.5 Push/pull + CAP guard | ✅ Done | Write guard via `cap_lite_guard.py` |
| 1.6 Update routes | ✅ Done | All imports redirected |
| 1.7 Port auto-discovery | ✅ Done | `_config.py` discovers Anytype API port |
| 1.8 Comprehensive tests | ✅ Done | 35 new + 127 existing = 162 total |
| **Remaining** | | |
| Wire REST client into routes | 🔲 TODO | Dual-mode: prefer REST, fallback to MCP |
| Extract business logic | 🔲 TODO | `_apply_cap_lite_to_plan()` → `anytype_service.py` |
| Split models | 🔲 TODO | `anytype.py` → status/search/write sub-files |
| Live integration tests | 🔲 TODO | API key available, ready to test |

## Phase 2: CAP Integration Cleanup ✅

| Task | Status | Notes |
|---|---|---|
| 2.1 Consolidate to `src/yar/cap/` | ✅ Done | 6 modules: constants, primitives, guard, models, policies, `__init__` |
| 2.2 Delete legacy files | ✅ Done | `cap_profile.py`, `core/cap_lite_guard.py`, `models/guard.py` deleted; all 10 consumers updated |
| 2.3 Models in `cap/models.py` | ✅ Done | `GuardDecision`, `GuardDecisionValue` with docstrings |
| 2.4 Policies to data files | ✅ Done | `cap/data/` + `importlib.resources` loader (cached) |
| 2.5 Comprehensive tests | ✅ Done | 81 tests in `test_cap_subpackage.py` |
| 2.6 Lazy import for circular deps | ✅ Done | `__getattr__` + `importlib.import_module` in `cap/__init__.py` |

## Phase 3: Code Quality & Structure

| Task | Status | Notes |
|---|---|---|
| 3.1 Reduce module sizes | 🟢 Done | Anytype decomposed; CAP decomposed; `model_router.py` (620 lines) remaining |
| 3.2 Type hints | 🔲 TODO | |
| 3.3 Google-style docstrings | 🔲 TODO | |
| 3.4 Error hierarchy | 🔲 TODO | Create `src/yar/errors.py` |
| 3.5 Structured logging | 🔲 TODO | Replace raw `print()` |

## Phase 4: Interface Organization

| Task | Status | Notes |
|---|---|---|
| 4.1 Evaluate layout | 🔲 TODO | Mobile (Flutter), Web shell, Desktop (planned), Extension (planned) |
| 4.2 Create `interfaces/` | 🔲 TODO | |
| 4.3 Update static serving | 🔲 TODO | |
| 4.4 API client spec | 🔲 TODO | |
| 4.5 Modularization plan | 🔲 TODO | |

## Phase 5: Documentation ✅

| Task | Status | Notes |
|---|---|---|
| 5.1 Rewrite README.md | 🔲 TODO | Current README needs trimming; API docs → `docs/` |
| 5.2 `docs/` structure | ✅ Done | 23 docs across 4 categories |
| 5.3 Module docstrings | 🔲 TODO | |
| 5.4 OpenAPI spec export | 🔲 TODO | |
| 5.5 CHANGELOG.md | ✅ Done | Exists at root |

## Phase 6: Publishing Readiness

| Task | Status | Notes |
|---|---|---|
| 6.1 LICENSE | 🔲 TODO | Apache 2.0 |
| 6.2 GitHub CI | 🔲 TODO | `.github/workflows/` |
| 6.3 noxfile.py | 🔲 TODO | |
| 6.4 `.cytognosis-config.yaml` | 🔲 TODO | |
| 6.5 Full `pyproject.toml` metadata | 🟡 Partial | Has basics; needs classifiers, URLs |
| 6.6 Final verification | 🔲 TODO | |

---

## Priority Queue (Next Actions)

Ordered by impact and dependency:

| Priority | Task | Phase | Est. Time | Dependency |
|---|---|---|---|---|
| **P0** | Wire REST client into routes (dual-mode) | 1 | 45 min | None |
| **P0** | Extract `anytype_service.py` | 1 | 30 min | None |
| **P1** | Centralized `YarSettings` (Pydantic) | 0 | 60 min | None |
| **P1** | Error hierarchy (`errors.py`) | 3 | 30 min | None |
| **P1** | Split `models/anytype.py` | 1 | 20 min | None |
| **P1** | `_ensure_connected()` decorator | 1 | 15 min | None |
| **P2** | CAP consolidation → `src/yar/cap/` | 2 | 2 hrs | None |
| **P2** | Split `model_router.py` into providers | 3 | 1 hr | `YarSettings` |
| **P2** | README rewrite | 5 | 30 min | None |
| **P3** | Live Anytype integration tests | 1 | 1 hr | Anytype API key |
| **P3** | `py.typed` + type hints | 0/3 | 2 hrs | None |
| **P3** | Interface reorganization | 4 | 2 hrs | None |
| **P3** | LICENSE + CI + nox | 6 | 1 hr | None |
