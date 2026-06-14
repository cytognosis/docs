> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `steering`, `tech`

---
inclusion: always
version: 1.0.0
category: tech
description: Technology stack and architecture patterns for Cytoplex (CAP)
last_updated: 2026-05-29
---

# Tech Steering: Cytoplex (CAP)

## Stack

| Layer | Technology | Version / Variant | Notes |
|-------|-----------|-------------------|-------|
| Language | Python | 3.12+ | Minimum runtime version |
| Build System | setuptools | >=69 | Legacy build backend (migration to hatchling planned) |
| Auth Tokens | biscuit-python | >=0.4, <0.5 | Decentralized authorization tokens |
| Cryptography | cryptography | >=42.0.0 | Certificate management, signing, verification |
| gRPC | grpcio | ==1.71.2 | gRPC transport binding (exact pin for proto compat) |
| Schema Validation | jsonschema | >=4.22.0 | JSON Schema validation for CAP messages |
| Protobuf | protobuf | ==5.29.5 | Protocol Buffers serialization (exact pin) |
| Schema DSL | LinkML | >=1.11 | Schema definitions for CAP message types (dev) |
| Linter/Formatter | ruff | >=0.4.4 | Python linting and formatting |
| Testing | pytest | >=8.3 | Test runner with integration/real_model markers |
| Pre-commit | pre-commit | >=3.7 | Git hook management |

## Architecture Patterns

### Protocol Enforcement Architecture (PEP/PDP)

Cytoplex follows a Policy Enforcement Point / Policy Decision Point architecture:

```
Agent Request
     ↓
┌─────────────────────┐
│  Policy Enforcement  │  ← PEP (edge_pep, local_pep, attested_local_pep)
│  Point (PEP)        │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│  Policy Decision     │  ← PDP (privacy_pdp, pdp_adapters)
│  Point (PDP)        │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│  Authority Registry  │  ← Central authority and capability registry
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│  Audit / Observability│ ← Transparency logs, retention, observability
└─────────────────────┘
```

### Module Architecture

```
src/cytoplex/
├── runtime/            # Core protocol runtime (PEP, PDP, registry, lifecycle)
├── schema/             # LinkML schema definitions
├── security/           # Cryptography, certificates, transparency logs
├── profiles/           # Domain profiles (cap_med, cap_swe, inheritance)
├── conformance/        # Conformance test suites and v1 runner
├── bindings/           # Transport bindings (gRPC, HTTP JSON, edge PEP bridge)
├── scenarios/          # Reference deployment scenarios
├── evaluation/         # Semantic quality evaluation
├── hardening/          # Production hardening (audit store, policy engine)
├── benchmarks.py       # Performance benchmark suite
└── cli/                # CLI entry points
```

### Key Design Decisions

- **Biscuit tokens**: Authority tokens use the Biscuit format for decentralized, attenuable authorization (no central auth server required)
- **Exact gRPC/protobuf pins**: Both `grpcio` and `protobuf` are pinned to exact versions to guarantee proto wire compatibility across all consumers
- **PEP layering**: Three PEP implementations for different deployment contexts: `local_pep` (full), `edge_pep` (lightweight), `attested_local_pep` (hardware-attested)
- **Mobile PEP**: Dedicated `mobile_local_pep` for on-device enforcement with constrained resources
- **Profile inheritance**: Domain profiles (medical, SWE) extend the base CAP profile through a formal inheritance system
- **Conformance-driven development**: The v1 conformance runner (`v1_runner.py`) is the canonical test of protocol compliance

### Transport Bindings

| Transport | Module | Status |
|-----------|--------|--------|
| HTTP JSON | `bindings/http_json/` | Production |
| gRPC | `bindings/grpc_reference/` | Reference implementation |
| Edge PEP Bridge | `bindings/edge_pep_bridge.py` | Production |

## Dependency Policy

### Adding Dependencies

1. Core protocol deps in `[project.dependencies]` — absolute minimum for runtime
2. Dev and tooling deps in `[project.optional-dependencies.dev]`
3. gRPC and protobuf pins are exact (`==`) to prevent wire format drift
4. Schema tooling (LinkML) is dev-only; runtime uses pre-generated validators

### Prohibited Patterns

- No `requirements.txt` for dependency management (keep `requirements.txt` only for legacy CI compatibility)
- No relaxation of gRPC/protobuf version pins without full cross-consumer testing
- No direct cryptographic operations outside `security/` module
- No runtime dependency on LinkML (schemas are compiled, not interpreted at runtime)
- No blocking I/O in PEP enforcement paths (latency-critical)
