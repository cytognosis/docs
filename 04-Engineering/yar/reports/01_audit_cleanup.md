# Phase 0: Audit & Cleanup Report

> **Status**: 5/7 complete
> **Scope**: Repository hygiene, packaging compliance, lint enforcement

## Completed Tasks

### 0.1 Migrate to Hatchling Build System

- `pyproject.toml` now uses `hatchling` as the build backend
- Proper `[project]` metadata including description, classifiers, Python requires
- `[tool.hatch.build.targets.wheel]` configured for `src/` layout

### 0.2 Ruff Configuration

Added comprehensive ruff config to `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py312"
line-length = 88
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "W", "F", "I", "UP", "B", "SIM", "RUF"]
ignore = [
    "E501",   # line too long (handled by formatter)
    "B008",   # do not perform function call in argument defaults (FastAPI Depends)
    "SIM108", # use ternary operator (readability)
    "RUF001", # ambiguous Unicode (false positive on Persian/Farsi safety terms)
]
```

**Design decision**: `RUF001` is suppressed globally because `CapLiteGuard` contains legitimate Persian/Farsi crisis detection terms (e.g., `خودکشی`, `می‌خوام بمیرم`) that ruff misidentifies as ambiguous Unicode.

### 0.3 Ruff Autofix

- Full pass: `ruff check --fix src/ tests/` + `ruff format src/ tests/`
- Zero remaining violations across 102 files

### 0.4 `__all__` Exports

- Every `__init__.py` now has explicit `__all__` lists
- Prevents accidental re-export of internal symbols
- Enables IDE autocompletion and static analysis

### 0.5 PEP 561 `py.typed` Marker

- Created `src/yar/py.typed` (empty file)
- Configured in `pyproject.toml` as shared-data package
- Enables type-checkers (mypy, pyright) to recognize Yar as a typed package

### Repository Cleanup

| Item | Action |
|---|---|
| `Yar.zip` | Deleted (root-level archive) |
| `logs/` | Deleted + gitignored |
| Legacy `Docs/` | Consolidated into `docs/` (lowercase) |
| `refactor/` | Gitignored as sandbox |
| Brand assets | Moved to `assets/brand/` |

## Remaining Tasks

| Task | Notes |
|---|---|
| 0.6 Centralized `YarSettings` | Env vars currently scattered across `_config.py`, `model_router.py`, `voice_service.py`, `logging_config.py`, `main.py`. Need a single Pydantic `Settings` class. |
| 0.7 Remove dead code | Check for any remaining `.bak` files or unused imports |
