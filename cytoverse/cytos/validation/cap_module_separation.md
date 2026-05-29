# CAP Module Separation & Prompts Relocation

## What Changed

### 1. Old `CAP/` Sandbox → `refactor/CAP/`
The project root `CAP/` directory contained development artifacts (notebooks, shell scripts, conformance tests, gRPC references, hardening scripts). Moved to `refactor/CAP/` since `refactor/` is the designated sandbox.

### 2. `src/yar/cap/` → `src/cap/` (Standalone Package)

**Before:** CAP was tightly coupled to Yar, importing `yar.models.Capture`, `yar.models.AnytypeWriteOperation`, etc.

**After:** CAP is a standalone package using Protocol types for structural subtyping.

```
src/cap/                          # ← Standalone, no yar imports
├── __init__.py                   #   Public API with lazy imports
├── constants.py                  #   CAP_VERSION, identity URIs
├── guard.py                      #   CapLiteGuard (uses Protocol types)
├── models.py                     #   GuardDecision, GuardDecisionValue
├── policies.py                   #   JSON policy loader (importlib.resources)
├── primitives.py                 #   CAP message factories
├── protocols.py                  #   CaptureProtocol, WriteOperationProtocol, etc.
└── data/
    ├── cap_core_policy.json
    └── cap_med_policy.json

src/yar/cap/                      # ← Thin bridge (re-exports from cap)
├── __init__.py                   #   from cap import *
├── guard.py                      #   from cap.guard import CapLiteGuard
├── models.py                     #   from cap.models import ...
├── constants.py                  #   from cap.constants import ...
└── policies.py                   #   from cap.policies import ...
```

### 3. Protocol Types (New: `src/cap/protocols.py`)

Three `@runtime_checkable` protocols decouple CAP from any specific host application:

| Protocol | Satisfying Yar Type | Purpose |
|----------|---------------------|---------|
| `CaptureProtocol` | `yar.models.Capture` | Input to `guard.evaluate()` |
| `WriteOperationProtocol` | `yar.models.AnytypeWriteOperation` | Input to `guard.validate_external_write()` |
| `WritePlanProtocol` | `yar.models.AnytypeWritePlan` | Batch of write operations |

Any project can integrate CAP by providing objects that satisfy these protocols.

### 4. Prompts Relocation

**Before:** `src/yar/prompts/*.md` — raw markdown files dumped in a package subdirectory, loaded via fragile `Path(__file__).resolve().parents[1]` traversal.

**After:** `src/yar/data/prompts/*.md` — proper data package with `__init__.py`, loaded via `importlib.resources.files("yar.data") / "prompts" / "..."`.

### 5. Build Configuration (`pyproject.toml`)

```diff
 [tool.hatch.build.targets.wheel]
-packages = ["src/yar"]
+packages = ["src/yar", "src/cap"]

 [tool.ruff.lint.isort]
-known-first-party = ["yar"]
+known-first-party = ["yar", "cap"]
```

## Files Modified

| File | Change |
|------|--------|
| `pyproject.toml` | Added `src/cap` to wheel packages and ruff isort |
| `src/cap/*` | New standalone CAP package (7 files + data/) |
| `src/yar/cap/*` | Replaced with thin bridge modules (5 files) |
| `src/yar/data/__init__.py` | New data package init |
| `src/yar/data/prompts/*.md` | Moved from `src/yar/prompts/` |
| `src/yar/core/model_router.py` | Updated to use `importlib.resources` |
| `refactor/CAP/` | Moved from project root `CAP/` |

## Zero Breakage Guarantee

- All 258 existing tests pass without modification
- All existing `from yar.cap import ...` imports work via the bridge
- Ruff checks pass clean
- Yar models satisfy CAP protocols (verified at runtime)
