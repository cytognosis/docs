> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `report`, `v0.1`

# CAP v0.1 Production-Candidate Supervisor Report

## Summary

CAP v0.1 is framed and implemented as a **Control Authority Profile** for agentic systems. It is not a standalone transport, tool-calling protocol, policy language, identity system, workflow runtime, clinical standard, or production security certification.

The canonical implementation lives under `src/cap_protocol/`. The top-level `reference_grpc/`, `second_http/`, `run_final_cap.py`, `run_production_hardening.py`, and `VERIFY_FINAL_PACKAGE.py` files are compatibility wrappers around package modules.

## Implemented Local Evidence

- Roles: Controller, Guard, Executor, and Observer.
- Core artifacts: `Directive`, `GuardDecision`, `RefusalMessage`, `ExecutionReport`, `DecisionRecord`, `EvidenceRef`, and `AuthorityChain`.
- CAP-Med v0.1 non-diagnostic profile constraints for clinical-output blocking and raw-transcript minimization.
- gRPC/protobuf reference binding at `src/cap_protocol/bindings/grpc_reference`.
- Independent HTTP/JSON binding at `src/cap_protocol/bindings/http_json`.
- Shared conformance runner and adversarial fixtures at `src/cap_protocol/conformance`.
- Local demos/adapters for MCP constrained invocation, A2A metadata carriage, OPA-style policy-as-data, OpenTelemetry attributes, and W3C PROV export.
- Deterministic v1 scaffolds for lifecycle FSM validation, profile inheritance/conflict resolution, CAP-SWE profile evidence, latency/mobile-resource benchmarking, and local Go CAPEnvelope/JCS fixture interop.
- Hardening checks for runtime-generated local mTLS certificates, Ed25519 detached-JWS verification, DSSE envelopes, in-toto-style statements, revoked-key refusal, tampered-payload rejection, JSON Schema validation, package-private-key scanning, and hash-chain audit validation.

## Latest Local Runner Outputs

A successful deterministic local run produces:

- `final_output/CAP_FINAL_SUMMARY.json`
- `final_output/production_hardening/CAP_PRODUCTION_HARDENING_REPORT.json`

The latest local run in this workspace was regenerated at `2026-05-22T12:53:22Z` and reported 28/28 implementation conformance checks per executable binding and 33/33 production-hardening/shared conformance checks. These are local deterministic structural results, not external verification or an independent security audit.

## Optional Real-Model Mode

Real-model execution is optional and not installed by default. It is requested with `--use-real-separate-e2b`, and `--require-real-model` makes model loading failure fatal. Without `--require-real-model`, failures fall back to deterministic local execution.

## Non-Claims

CAP v0.1 does not claim clinical validity, model truthfulness, stable-standard maturity, production deployment readiness, live multi-organization interoperability, or externally audited security completeness.

## Remaining Stable-Release Gates

- Independent third-party security review.
- Production KMS/HSM integration.
- Organization-specific OPA/Cedar policy deployment.
- Live multi-organization MCP/A2A interoperability tests.
- Domain semantic-quality evaluation.

## Research-Strengthening Gates

- Deployment-representative latency and overhead benchmark beyond the local deterministic artifact.
- Externally owned non-medical profile example beyond the local CAP-SWE scaffold.
- Third minimal implementation or external adapter beyond the local Go fixture adapter.
- External profile-owner review of lifecycle FSM and profile inheritance rules.
- Synthetic CAP-Med semantic-quality evaluation dataset.
- Broader empirical semantic-quality evaluation distinct from structural conformance.
