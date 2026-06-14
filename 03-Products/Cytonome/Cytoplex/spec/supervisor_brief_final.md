> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP v0.1 Supervisor Brief — Final Production-Candidate Package

## One-paragraph summary

CAP v1 is a **Control Authority Protocol** for agentic systems: a supervisory control plane and semantic enforcement layer above existing transports, policy engines, identity systems, observability stacks, and workflow engines. The current package implements a narrower v0.1 Control Authority Profile subset and a deterministic v1 runtime scaffold. It is no longer only a conceptual draft: it includes a gRPC/protobuf reference binding, an independently structured HTTP/JSON binding, shared conformance checks, CAP-Med v1 runtime-profile evidence for non-diagnostic constraints and raw-data minimization, local live MCP/A2A substrate interop plus OPA/OpenTelemetry/W3C PROV demos or adapters, and a production-hardening layer with detached signatures, DSSE, in-toto-style attestations, adversarial fixtures, package-private-key scanning, and hash-chain audit validation.

## What is novel

The novelty is not a new transport or universal agent protocol. The novelty is a compact authority semantics layer for agentic actions:

1. Explicit `AuthorityChain` rather than implicit prompt authority.
2. `GuardDecision` objects that can allow, deny, narrow, or escalate proposed action.
3. Typed `RefusalMessage` objects instead of unstructured error strings.
4. `EvidenceRef` objects that bind execution to integrity, freshness, provenance, and access-policy constraints.
5. `ExecutionReport` objects that make side effects, produced evidence, and policy references auditable.
6. A CAP-Med v1 runtime-profile fixture that enforces non-diagnostic boundaries and raw-data minimization structurally, without claiming clinical validation.

## Current implementation status

The package contains:

- reference implementation: `src/cap_protocol/bindings/grpc_reference/` (`reference_grpc/` remains a compatibility wrapper)
- second independent implementation: `src/cap_protocol/bindings/http_json/` (`second_http/` remains a compatibility wrapper)
- shared conformance: `src/cap_protocol/conformance/`
- security/hardening: `src/cap_protocol/security/`, `src/cap_protocol/hardening/`, `policies/`
- final runner: `run_final_cap.py`
- hardening runner: `run_production_hardening.py`

The latest local deterministic run produced passing output for both executable implementations and the production-hardening layer. This is local structural/conformance evidence, not external audit evidence.

## What should not be overstated

CAP does not prove clinical safety, clinical utility, diagnosis quality, or LLM truthfulness. It provides structural control, bounded authority, evidence linkage, typed refusal, policy traceability, and provenance. The current package is production-candidate and research-grade, not yet an externally audited public standard.

## Remaining before stable release

- independent third-party security review;
- production KMS/HSM integration;
- organization-specific OPA/Cedar deployment;
- external MCP server and live multi-organization MCP/A2A interoperability testing;
- empirical semantic-quality evaluation for the intended domain. A synthetic onboarding harness exists, but qualified expert review remains required;
- CAP-Med or other regulated-profile review. A packet exists under `docs/regulated_profile_review/`, but qualified external profile review remains required.

## Remaining before stronger systems paper

- latency and overhead benchmark;
- non-medical profile example;
- third minimal implementation or external adapter;
- externally reviewed lifecycle FSM/profile-inheritance behavior beyond the current deterministic scaffold;
- qualified expert semantic-quality evaluation beyond the synthetic onboarding fixtures;
- broader empirical distinction between structural conformance and semantic-quality evaluation.

## Recommended supervisor ask

Please review whether the v1 framing as a supervisory Control Authority Protocol is academically defensible, whether the current v0.1 Profile subset is clearly scoped, and whether the implementation evidence is sufficient for an architecture/systems workshop paper before external security review.
