> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `steering`, `structure`

---
inclusion: always
version: 1.0.0
category: structure
description: Directory layout and module boundaries for Cytoplex (CAP)
last_updated: 2026-05-29
---

# Structure Steering: Cytoplex (CAP)

## Directory Layout

```
CAP/
├── pyproject.toml                      # Project metadata, deps, ruff/pytest config
├── README.md
├── CHANGELOG.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                             # Apache 2.0
├── .pre-commit-config.yaml
├── .env.example                        # Environment variable template
│
├── src/
│   └── cytoplex/                       # Main package
│       ├── __init__.py                 # Package version and public API
│       ├── paths.py                    # Path resolution utilities
│       ├── benchmarks.py              # Performance benchmark suite
│       │
│       ├── runtime/                    # Core protocol runtime
│       │   ├── __init__.py             # Runtime public API
│       │   ├── registry.py             # Authority and capability registry
│       │   ├── controller.py           # Protocol controller / orchestrator
│       │   ├── lifecycle.py            # Agent lifecycle management
│       │   ├── authority.py            # Authority level definitions
│       │   ├── local_pep.py            # Local Policy Enforcement Point
│       │   ├── edge_pep.py             # Edge/lightweight PEP
│       │   ├── attested_local_pep.py   # Hardware-attested PEP
│       │   ├── mobile_local_pep.py     # Mobile on-device PEP
│       │   ├── privacy_pdp.py          # Privacy Policy Decision Point
│       │   ├── pdp_adapters.py         # PDP adapter implementations
│       │   ├── supervisor_gateway.py   # Supervisor agent gateway
│       │   ├── session_router.py       # Session routing and management
│       │   ├── workflow_engine.py      # Multi-step workflow execution
│       │   ├── service_mesh.py         # Service mesh integration
│       │   ├── substrate_interop.py    # Cross-substrate interoperability
│       │   ├── observability.py        # Metrics, logging, tracing
│       │   ├── human_review.py         # Human-in-the-loop review flows
│       │   ├── interrupts.py           # Interrupt handling
│       │   ├── ui_abort.py             # UI-initiated abort flows
│       │   ├── ui_correction.py        # UI-initiated correction flows
│       │   ├── warrants.py             # Authorization warrant management
│       │   ├── workload_identity.py    # Workload identity resolution
│       │   ├── embeddings.py           # Semantic embedding operations
│       │   ├── live_model_streaming.py # Live model streaming protocol
│       │   ├── slow_path_classifier.py # Slow-path classification logic
│       │   ├── redaction.py            # PII/PHI redaction engine
│       │   ├── retention.py            # Data retention policies
│       │   └── temporal.py             # Temporal consistency checks
│       │
│       ├── schema/                     # Schema definitions
│       │   ├── __init__.py             # Schema public API
│       │   └── linkml.py              # LinkML schema definitions for CAP types
│       │
│       ├── security/                   # Security and cryptography
│       │   ├── __init__.py
│       │   ├── cap_crypto.py           # Cryptographic operations (signing, verify)
│       │   ├── cert_manager.py         # Certificate lifecycle management
│       │   └── transparency.py         # Transparency log implementation
│       │
│       ├── profiles/                   # Domain-specific profiles
│       │   ├── __init__.py             # Profile registration and lookup
│       │   ├── cap_med.py              # Medical/clinical domain profile
│       │   ├── cap_swe.py              # Software engineering domain profile
│       │   └── inheritance.py          # Profile inheritance system
│       │
│       ├── conformance/                # Conformance testing
│       │   ├── __init__.py
│       │   ├── runner.py               # Lightweight conformance runner
│       │   ├── v1_runner.py            # Full v1 conformance test suite
│       │   └── fixtures/               # Test fixture data (JSONL)
│       │
│       ├── bindings/                   # Transport bindings
│       │   ├── __init__.py
│       │   ├── edge_pep_bridge.py      # Edge PEP transport bridge
│       │   ├── grpc_reference/         # gRPC reference implementation
│       │   │   └── *.proto             # Protocol Buffer definitions
│       │   └── http_json/              # HTTP JSON binding
│       │
│       ├── scenarios/                  # Reference deployment scenarios
│       │   ├── __init__.py
│       │   └── therapist_supervisor/   # Therapist-supervisor demo scenario
│       │
│       ├── evaluation/                 # Quality evaluation
│       │   ├── __init__.py
│       │   └── semantic_quality.py     # Semantic quality metrics
│       │
│       ├── hardening/                  # Production hardening
│       │   ├── __init__.py
│       │   ├── audit_store.py          # Persistent audit trail storage
│       │   └── policy_engine.py        # Runtime policy evaluation engine
│       │
│       └── cli/                        # CLI entry points
│           ├── run_final.py            # Final integration runner
│           ├── run_hardening.py        # Hardening test runner
│           ├── run_benchmarks.py       # Benchmark runner
│           ├── verify_package.py       # Package verification
│           ├── verify_release_baseline.py  # Release baseline check
│           └── check_v1_schema_drift.py    # Schema drift detector
│
├── schemas/                            # Top-level schema definitions
│   ├── cap.yaml                        # CAP protocol schema
│   ├── core.yaml                       # Core data type schemas
│   ├── cap-core/                       # Core schema module
│   ├── cap-med/                        # Medical domain schemas
│   └── domains/                        # Domain-specific schema extensions
│
├── config/                             # Configuration files
├── docs/                               # Documentation (7-spec suite + API docs)
│   ├── CAP_00_README.md                # Protocol overview
│   ├── CAP_01_foundations.md           # Spec 1: Foundations
│   ├── CAP_02_core_model.md            # Spec 2: Core model
│   ├── CAP_03_primitives.md            # Spec 3: Primitives
│   ├── CAP_04_security_trust_evidence.md  # Spec 4: Security and trust
│   ├── CAP_05_integrations.md          # Spec 5: Integrations
│   ├── CAP_06_conformance.md           # Spec 6: Conformance
│   ├── CAP_07_profiles_roadmap.md      # Spec 7: Profiles and roadmap
│   ├── api.md                          # API reference
│   ├── development.md                  # Development guide
│   └── testing.md                      # Testing guide
│
├── tests/                              # Test suite
├── examples/                           # Usage examples
├── scripts/                            # Development and CI utilities
├── policies/                           # Policy definition files
├── reference_grpc/                     # gRPC reference server
├── second_http/                        # Second HTTP binding implementation
├── third_impl/                         # Third implementation variant
├── runs/                               # Test/benchmark run outputs
└── dist/                               # Build distribution artifacts
```

## Source Modules

| Module | Responsibility | Key Exports |
|--------|---------------|-------------|
| `runtime` | Core protocol enforcement | `Registry`, `Controller`, `LocalPEP`, `EdgePEP`, `SupervisorGateway`, `WorkflowEngine` |
| `schema` | Protocol message schemas | LinkML-based CAP type definitions |
| `security` | Cryptographic operations | `CAPCrypto`, `CertManager`, `TransparencyLog` |
| `profiles` | Domain profile system | `CAPMed`, `CAPSWE`, profile inheritance |
| `conformance` | Protocol compliance testing | `ConformanceRunner`, `V1Runner` |
| `bindings` | Transport layer adapters | gRPC binding, HTTP JSON binding, edge PEP bridge |
| `scenarios` | Reference deployments | `TherapistSupervisor` scenario runner |
| `evaluation` | Quality metrics | `SemanticQuality` evaluator |
| `hardening` | Production readiness | `AuditStore`, `PolicyEngine` |
| `cli` | Command-line tools | CLI entry points for all `plex-*` commands |

## Module Boundaries

### Import Rules

- `cli` imports from any module (top-level entry points)
- `runtime` imports from `schema`, `security`, `profiles`
- `conformance` imports from `runtime`, `schema` (testing the protocol)
- `bindings` imports from `runtime`, `schema` (transport adaptation)
- `scenarios` imports from `runtime`, `profiles` (reference deployments)
- `hardening` imports from `runtime` only
- `evaluation` imports from `runtime`, `schema`
- `security` imports from `schema` only (no runtime dependency)
- `profiles` imports from `schema` only (no runtime dependency)
- `schema` has no internal imports (leaf module)
- No circular imports between `runtime` submodules

### Test Structure

- Test files in `tests/` mirror source module structure
- Markers: `@pytest.mark.integration` (full runtime tests), `@pytest.mark.real_model` (GPU/model required)
- Conformance fixtures in `conformance/fixtures/*.jsonl`
- CI gates: `plex-check-v1-schema-drift` and `plex-check-v1-conformance`

## Naming Conventions

| Entity | Convention | Example |
|--------|-----------|---------|
| Package | `snake_case` | `cytoplex` |
| Runtime modules | `snake_case` | `local_pep.py`, `supervisor_gateway.py` |
| Classes | `PascalCase` | `LocalPEP`, `SupervisorGateway` |
| CLI commands | `plex-<verb>-<noun>` | `plex-run-final`, `plex-check-v1-conformance` |
| Schema files | `snake_case.yaml` | `cap.yaml`, `core.yaml` |
| Proto files | `snake_case.proto` | `cap_service.proto` |
| Profile classes | `CAP` + `PascalCase` | `CAPMed`, `CAPSWE` |
| Test files | `test_<module>.py` | `test_local_pep.py` |
| Fixture files | `<name>.jsonl` | `conformance_cases.jsonl` |
| Spec documents | `CAP_<NN>_<topic>.md` | `CAP_04_security_trust_evidence.md` |
