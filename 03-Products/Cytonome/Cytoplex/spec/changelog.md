# CAP Changelog from Previous Draft

This changelog records the architectural shift from the older protocol-shaped CAP draft to the v0.1-candidate Control Authority Profile.

## 1. Renamed and reframed

- **Old framing:** Cognitive Agent Protocol, an application-layer control protocol for hierarchical multi-agent systems.
- **New framing:** Control Authority Profile, a semantic authority profile that composes with A2A, MCP, policy engines, observability systems, identity systems, and workflow runtimes.

Reason: the older framing implied CAP owned transport, task lifecycle, audit, checkpointing, and governance. The new framing keeps CAP focused on Controller-to-Executor authority semantics.

## 2. Removed from Core

| Removed item | Replacement |
|---|---|
| Standalone wire-protocol claim | Semantic profile over existing protocols. |
| Mandatory gRPC conformance | Transport-independent semantic conformance. |
| Eleven hardcoded roles | Controller, Executor, Guard, Observer. |
| Role-transition matrix | Capability claims + policy evaluation + lifecycle invariants. |
| Seven hardcoded governance modes | PolicyRef + GuardDecision via OPA/Cedar/custom policy engines. |
| DelegationRequest | A2A Task. |
| HumanReviewRequest | Workflow engine or application-level human approval. |
| StateCheckpoint | Runtime checkpoint references, Temporal/LangGraph/database snapshots. |
| AuditEvent | OpenTelemetry span events + W3C PROV mapping. |
| Custom hash-chain audit | External transparency/Merkle/in-toto/DSSE mechanisms. |
| CAP capability descriptor | A2A AgentCard extension or deployment metadata. |
| Tool schemas/tool invocation | MCP. |

## 3. Added to Core

- Formal Directive lifecycle FSM, now backed by a machine-checkable lifecycle scaffold for envelope, directive, interrupt, execution, evidence, audit, and provenance domains.
- Effective constraint merge semantics.
- Guard conflict defaults.
- Stronger `GuardDecision` object.
- Typed `EvidenceRef` object.
- `PolicyRef` object.
- `AuthorityChainStep` verification model.
- `SideEffect` and compensation metadata.
- Transport-neutral Envelope.
- OpenTelemetry semantic attribute recommendations.
- W3C PROV mapping.
- Expanded conformance suite.
- Threat model and residual risk statement.

## 4. Moved to profiles

- CAP-Med clinical/non-diagnostic constraints.
- CAP-SWE code sandboxing and rollback specifics.
- Profile inheritance and override rules; Core refuses profile attempts to redefine lifecycle states or interrupt actions.
- CAP-Fin regulatory retention and funds-movement policy.
- CAP-Rob physical safety constraints.
- Domain-specific evidence schemas.
- Human review requirements.
- Retention/minimization rules.

## 5. Postponed to v0.2 or later

- Cross-organization trust federation beyond basic identity references.
- Formal TLA+ or Alloy machine-checkable model.
- Official profile registry.
- Canonical protobuf schemas.
- Standardized transparency-log anchoring.
- Threshold signatures or multi-party approval protocols.
- Confidential computing attestation profiles.

## 6. Main design principle retained

CAP still keeps the original insight:

> Do not let an agent that forms intent directly and opaquely act on the world. Intent should cross a typed, bounded, guardable, refusible, evidence-referenced boundary before execution.

The v0.1-candidate narrows that insight into an implementable interoperability profile.



## Supervisor-package additions

- Added `CAP_supervisor_brief.md` for a concise supervisor-facing summary, novelty framing, paper opportunity, and evaluation plan.
- Added `CAP_paper_positioning.md` to prevent overclaiming and frame CAP as a profile-based research contribution.
- Added `CAP_references.md` with verified standards links.
- Updated README reading order to include supervisor and paper-positioning documents.
- Updated foundations with explicit novelty and non-contribution statements.
- Updated roadmap with paper-readiness milestones.

## CAP v1 architecture alignment additions

- Reframed public docs toward CAP v1 as the Control Authority Protocol and supervisory control plane while preserving the current v0.1 production-candidate implementation claim.
- Added `CAP_v1_TASKS.md` with source priority, Therapist/Supervisor scenario contract, completed/partial/open migration status, and P0/P1/P2 backlog items.
- Added initial CAP v1 JSON Schemas under `schemas/cap-core/v1/` for `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`, `EvidenceRef`, `AuthorityChain`, `PolicyRef`, `PrivacyBoundary`, `Capability`, and `OperationalConstraints`.
- Added CAP v1 LinkML authoring schemas using the Cytos-style `schemas/cap.yaml`, `schemas/core.yaml`, and `schemas/domains/*.yaml` structure.
- Added matching CAP v1 examples under `examples/cap-core/v1/`.
- Added minimal `LocalPEP` and `EdgePEP` runtime scaffolds for privacy-boundary enforcement, Supervisor overreach refusal, offline policy-bundle behavior, streaming transform/correction scaffolding, high-assurance bypass refusal, and signed envelope checks.
- Added `cap_protocol.conformance.v1_runner.run_v1_conformance_smoke` to distinguish implemented v1 smoke coverage from the existing v0.1 fixture conformance runner.
- Added `cap_protocol.conformance.v1_runner.run_v1_conformance_release_gate` and `cap-check-v1-conformance` so V1-C01 through V1-C15 are release-blocking deterministic scaffold cases with full-runtime external gates documented separately.
- Updated testing guidance to use `venv` and `NO_PROXY=127.0.0.1,localhost` for localhost HTTP smoke tests in proxy-configured environments.
- Added `cap_protocol.benchmarks`, `cap-run-v1-benchmarks`, and `docs/benchmarks/` artifacts for local deterministic p50/p95 latency, CPU-time, memory, streaming-delay, and mobile proxy-path evidence, with production/device performance caveats.
- Added `third_impl/go_cap_adapter`, a standard-library Go adapter that validates shared CAP v1 CAPEnvelope/JCS/signature fixtures and reports failures by fixture ID as local third-implementation interop evidence.
- Added `cap_protocol.runtime.lifecycle` and `cap_protocol.profiles.inheritance` so lifecycle FSM behavior and profile inheritance/override rules are machine-checkable and covered by V1 conformance.
