# Phase 2: CAP Consolidation Report

> **Status**: ✅ Complete
> **Scope**: Unify all CAP logic into `src/yar/cap/`, delete legacy files, comprehensive testing

## Problem

CAP (Communication Augmentation Protocol) logic was fragmented across three locations:

1. **`cap_profile.py`** (340 lines) — Constants (`CAP_VERSION`, identity URIs) and primitive factory functions (directives, refusals, execution reports, evidence refs, decision records, capabilities matrix).
2. **`core/cap_lite_guard.py`** (579 lines) — The `CapLiteGuard` class with all safety/privacy evaluation methods, crisis detection, Persian/Farsi term dictionaries, diagnostic/treatment boundary enforcement.
3. **`models/guard.py`** — Pydantic models `GuardDecision` and `GuardDecisionValue`.
4. **`CAP/policies/`** — Loose JSON policy files not importable via `importlib.resources`.

Consumers had to know which of these three files to import from, and there was no unified public API.

## Solution

### New Structure: `src/yar/cap/`

| Module | Lines | Source | Responsibility |
|---|---|---|---|
| `constants.py` | 13 | From `cap_profile.py` | `CAP_VERSION`, `PROFILE_NS`, SPIFFE identity URIs |
| `primitives.py` | 386 | From `cap_profile.py` | All CAP message factories: `directive()`, `refusal_message()`, `execution_report()`, `decision_record()`, `capabilities_matrix()`, evidence refs, constraints, hashing |
| `guard.py` | 654 | From `core/cap_lite_guard.py` | `CapLiteGuard` class with all evaluation methods |
| `models.py` | 44 | From `models/guard.py` | `GuardDecision`, `GuardDecisionValue` Pydantic models |
| `policies.py` | 42 | New | `importlib.resources` policy loader with `@lru_cache` |
| `__init__.py` | 73 | New | Public API with lazy imports |
| `data/*.json` | 2 files | From `CAP/policies/` | Bundled policy definitions |
| **Total** | **1,212** | | |

### Import Migration

Every consumer was updated to use the canonical location. No backward-compat shims:

| Consumer | Old Import | New Import |
|---|---|---|
| `models/communication.py` | `from yar.models.guard` | `from yar.cap.models` |
| `models/voice.py` | `from yar.models.guard` | `from yar.cap.models` |
| `models/__init__.py` | `from yar.models.guard` | `from yar.cap.models` |
| `core/coordinator.py` | `from yar import cap_profile` | `from yar.cap import primitives` |
| `core/coordinator.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `core/voice_service.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `api/routes_cap.py` | `from yar import cap_profile` | `from yar.cap import primitives` |
| `api/routes_cap.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `api/routes_voice.py` | `from yar import cap_profile` | `from yar.cap import CAP_VERSION, PROFILE_NS` |
| `api/routes_voice.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `api/routes_communication.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `api/routes_anytype.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `api/routes_objects.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |
| `tests/test_anytype_write_guard.py` | `from yar.core.cap_lite_guard` | `from yar.cap.guard` |

### Deleted Files

| File | Reason |
|---|---|
| `src/yar/cap_profile.py` | Logic moved to `cap/constants.py` + `cap/primitives.py` |
| `src/yar/core/cap_lite_guard.py` | Logic moved to `cap/guard.py` |
| `src/yar/models/guard.py` | Logic moved to `cap/models.py` |

### Circular Import Resolution

The dependency graph creates a cycle:

```
yar.models/__init__.py → imports GuardDecision from yar.cap.models
                          ↓ triggers yar.cap/__init__.py
yar.cap/__init__.py → wants to import guard.py and primitives.py
                          ↓ both import from yar.models
yar.models/__init__.py → still loading (circular!)
```

**Solution**: `cap/__init__.py` uses `importlib.import_module()` in `__getattr__` for lazy loading of `guard` and `primitives`. Constants, models, and policies (which have no `yar.models` dependency) load eagerly:

```python
# Safe eager imports (no yar.models dependency)
from yar.cap.constants import CAP_VERSION, ...
from yar.cap.models import GuardDecision, GuardDecisionValue
from yar.cap.policies import load_core_policy, ...

def __getattr__(name):
    if name == "CapLiteGuard":
        return importlib.import_module("yar.cap.guard").CapLiteGuard
    if name == "primitives":
        return importlib.import_module("yar.cap.primitives")
    raise AttributeError(...)
```

## Test Coverage

81 unit tests in `test_cap_subpackage.py` across 11 test classes:

| Test Class | Tests | Coverage |
|---|---|---|
| `TestConstants` | 3 | Version, namespace, SPIFFE URIs |
| `TestPrimitives` | 15 | All factory functions, constraints, evidence refs |
| `TestGuardCaptureEvaluate` | 14 | Safe capture, diagnosis, treatment, intent, raw sharing, risk scoring, confirmation |
| `TestGuardCrisis` | 4 | English crisis terms, Persian crisis terms, word boundaries, support message |
| `TestGuardPersianDiagnosis` | 1 | Persian/Farsi diagnosis term detection |
| `TestGuardExternalWrite` | 12 | Dry run, confirmed, unsupported (Pydantic-rejected), delete, raw content, health boundary, write plans |
| `TestGuardLocalObjectUpdate` | 6 | Safe update, diagnosis/treatment/risk/intent/diagnostic claim in fields |
| `TestGuardLocalLink` | 7 | Valid/invalid relations, self-links, bad relation names |
| `TestGuardReasonCodes` | 5 | privacy_denied, safety_denied, policy_denied reason code mapping |
| `TestModels` | 4 | Defaults, enum values, serialization, re-export from yar.models |
| `TestPolicies` | 4 | Core policy, med policy, not-found error, JSON round-trip |
| `TestPublicAPI` | 4 | Package-level guard, primitives, constants, policies access |

### Safety Term Coverage

The guard tests explicitly verify detection of:

**English terms**: diagnose, treatment, medication, prescribe, dosage, intent ("really feels"), raw sharing, health risk scoring, crisis ("kill myself", "suicidal", "self-harm", "want to die")

**Persian/Farsi terms**: تشخیص بده (diagnose me), آیا من اوتیسم (am I autistic), افسرده‌ام (I'm depressed), خودکشی (suicide), می‌خوام بمیرم (I want to die), کاش نبودم (I wish I wasn't here)

**Harmless context exclusion**: "treatment response prediction", "must not recommend treatment", "out-of-scope risk" are verified to NOT trigger false denials.

**Word boundary verification**: "suicidology" does NOT trigger "suicide" crisis detection.

## Design Decisions

1. **No backward compat shims**: This is v1.0. One canonical location, one import path.
2. **Policies as data files**: JSON policies ship inside the wheel via `importlib.resources`, no file-path fragility.
3. **`@lru_cache` on policy loading**: Policies are immutable at runtime; cache avoids repeated disk reads.
4. **`StrEnum` for `GuardDecisionValue`**: Enables both `decision.guard_decision == "deny"` and `decision.guard_decision == GuardDecisionValue.deny` comparison.
