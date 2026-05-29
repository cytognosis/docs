# Module Audit: Integrations & CAP

## Status Summary

| Module | Files | Tests | Docstring Coverage | Status |
|--------|-------|-------|--------------------|--------|
| `integrations/anytype/` | 12 | 8 test files (258 total pass) | **100%** | ✅ Done |
| `integrations/linkml_loader.py` | 1 | `test_linkml_loader.py` | **100%** | ✅ Done |
| `integrations/wadm_adapter.py` | 1 | `test_wadm_adapter.py` | **100%** | ✅ Done |
| `integrations/__init__.py` | 1 | — | **100%** | ✅ Fixed (added WADMAdapter export) |
| `cap/guard.py` | 1 | 3 test files | **100%** | ✅ Done |
| `cap/primitives.py` | 1 | covered by guard tests | **100%** | ✅ Done |
| `cap/models.py` | 1 | covered by guard tests | **100%** | ✅ Done |
| `cap/policies.py` | 1 | `test_cap_subpackage.py` | **100%** | ✅ Done |
| `cap/constants.py` | 1 | — | **100%** | ✅ Done |

> [!IMPORTANT]
> All 258 tests pass. Zero missing docstrings across both modules.

---

## Changes Made This Session

### Integrations Module
1. **`linkml_loader.py`** — Added comprehensive module docstring with usage example, class docstring with attributes, and Google-style docstrings to all 9 methods (public + private) with Args, Returns, Raises, and Examples.
2. **`wadm_adapter.py`** — Added module docstring with W3C WADM context, class docstring explaining 3 conversion pathways, and detailed docstrings to all 6 methods with examples.
3. **`__init__.py`** — Added module docstring; exported `WADMAdapter` (was missing from public API).
4. **`anytype/adapter.py`** — Added docstrings to all 20 methods (public + private).
5. **`anytype/client.py`** — Added docstrings to `__init__` (×2) and `_headers`.
6. **`anytype/_config.py`** — Added docstring to `configured` property.
7. **`anytype/_rate_limiter.py`** — Added docstrings to `__init__` and `_refill`.
8. **`anytype/_transport.py`** — Added docstrings to all 8 methods.
9. **`anytype/_payload_mapper.py`** — Added docstrings to `_schema_write_payload` and `_property_key`.

### CAP Module
1. **`guard.py`** — Added docstrings to all 11 private methods that were missing them.

---

## Communication Components → CAP Assessment

### Current Communication-Related Files

| File | Purpose | CAP Dependency? | CAP Candidate? |
|------|---------|-----------------|----------------|
| [routes_communication.py](file:///home/mohammadi/repos/cytognosis/refactor/Yar/src/yar/api/routes_communication.py) | Interpret/translate messages via Gemma | Yes (pre/post CAP guard checks) | **No** — belongs in `api/` as route layer |
| [communication.py](file:///home/mohammadi/repos/cytognosis/refactor/Yar/src/yar/models/communication.py) | Request/response models | References `GuardDecision` | **No** — belongs in `models/` |
| [test_communication_gemma.py](file:///home/mohammadi/repos/cytognosis/refactor/Yar/tests/test_communication_gemma.py) | Communication endpoint tests | — | — |

### What Belongs in CAP (Current + Future)

The CAP module is correctly scoped as a **deterministic policy gate**. It should remain focused on:

```
cap/
├── __init__.py          # Public API with lazy imports
├── constants.py         # Version, identities, profile namespace
├── guard.py             # CapLiteGuard (the runtime gate)
├── models.py            # GuardDecision, GuardDecisionValue
├── policies.py          # JSON policy loader
├── primitives.py        # CAP message factories
└── data/                # Bundled policy JSON files
```

### Future CAP Candidates (Priority Order)

| Priority | Component | Why |
|----------|-----------|-----|
| **P0** | **Sensor Data Policy Gate** | When the emotion sensor (HuBERT+openSMILE) ships, CAP must gate what biomarker observations can be stored, shared, or aggregated. Add `guard.validate_sensor_observation()`. |
| **P1** | **Auto-discovery Consent Flow** | mDNS/Zeroconf device pairing needs a CAP-level consent step: "Device X wants to connect. Allow?" This is a new `validate_peer_connection()` check. |
| **P2** | **Multi-device Sync Policy** | When Yar runs on phone + laptop, CAP gates what data can cross devices (structured observations only, never raw audio). |
| **P3** | **Communication Output Filter** | The `_post_check_response()` logic in `routes_communication.py` (mind-reading detection) could be extracted into a `guard.validate_communication_output()` method. |

---

## Auto-Discovery on Local Network

> [!TIP]
> This is the highest-priority new feature for reducing barriers for neurodiverse users.

### Recommended Approach: Zeroconf (mDNS/DNS-SD)

```
New module: src/yar/discovery/
├── __init__.py
├── announcer.py     # Publish Yar service via mDNS (_yar._tcp.local.)
├── scanner.py       # Discover other Yar instances on the network
├── models.py        # PeerInfo, PairingRequest, PairingConsent
└── pairing.py       # One-time pairing with QR code or 6-digit PIN
```

**How it works:**
1. Yar desktop starts → announces `_yar._tcp.local.` on port 8340 via Zeroconf
2. Yar mobile app scans for `_yar._tcp.local.` services
3. First connection: show a 6-digit PIN on desktop, user enters on mobile (one-time)
4. CAP validates the pairing request (`validate_peer_connection()`)
5. Subsequent launches: auto-connect with stored peer identity (zero friction)

**Key dependency:** `zeroconf` (pure Python, ~200KB, no native deps)

**UX for neurodiverse users:**
- Zero configuration after first pairing
- Visual feedback: pulsing connection indicator
- Graceful degradation: works offline, works without the other device
- No port numbers, no IP addresses, no manual setup

### Priority: **P1** (implement after sensor architecture, before multi-device sync)

---

## Next Steps

1. ~~Document integrations + CAP~~ ✅ Done
2. ~~Fix WADMAdapter export~~ ✅ Done
3. **Implement `src/yar/discovery/`** — Zeroconf announcer + scanner
4. **Extract communication output filter** from routes into CAP guard
5. **Add `validate_sensor_observation()`** to CAP guard (when emotion sensor ships)
