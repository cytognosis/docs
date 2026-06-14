# Yar CAP Usage and Capability Matrix

This document maps Yar's CAP usage to the Cytognosis CAP v0.1 production-candidate package supplied in:

- `/Users/ali/Downloads/Cytognosis_CAP_v01_Comprehensive_Implementation_and_Use_Cases.md`
- `/Users/ali/Downloads/CAP`

Yar uses CAP as a local control-authority profile for bounded, evidence-linked, guardable, refusable, and auditable memory actions. The implementation is intentionally HTTP/JSON and local-first; it does not claim the gRPC reference binding or cryptographic hardening pieces are complete.

## Runtime Placement

Yar maps the CAP roles as follows:

| CAP role | Yar component |
| --- | --- |
| Controller | FastAPI coordinator and voice routes |
| Guard | `CapLiteGuard` with CAP v0.1 metadata |
| Executor | Local graph store, Anytype MCP adapter, mobile UI render path |
| Observer | `/cap/audit`, SQLite execution reports, voice turn history |

## Implemented CAP Primitives

| Primitive | Yar support | Notes |
| --- | --- | --- |
| Directive | Implemented | Capture, voice, and Anytype write checks emit bounded local Directives with action, constraints, authority chain, evidence refs, policy refs, expiry, reversibility, and idempotency key. |
| GuardDecision | Implemented | Runtime guard decisions include CAP decision id, guarded message id, guard identity/capability, severity, constraints added, policy refs, and evidence required. |
| ExecutionReport | Implemented | Capture execution reports include CAP ExecutionReport payloads without raw transcript content. |
| RefusalMessage | Implemented | Safety/privacy/policy denials include typed reason codes such as `safety_denied`, `privacy_denied`, `unsupported_action`, and `policy_denied`. |
| DecisionRecord | Implemented | Audit-safe rationale summaries are emitted without hidden chain-of-thought or raw scratchpad text. |
| EvidenceRef | Implemented | Evidence refs point to local redacted/raw-local-only resources and include SHA-256 hash, media type, freshness, confidentiality, access policy, redaction ref, and provenance ref. |
| AuthorityChainStep | Implemented as local-dev attestation | Yar emits local authority scope and policy refs. Detached JWS/DSSE verification is not yet implemented. |
| ConstraintSet | Implemented | Constraints cover allowed/forbidden tools, data access, network egress, max tool calls/time, scope tags, and human confirmation requirements. |
| PolicyRef | Implemented | Yar emits `cap-core-policy-v0.1`, `cap-med-non-diagnostic-v0.1`, and `yar-local-memory-boundary-v0.1` refs with digests. |

## CAP-Med Profile Usage

Yar applies the non-diagnostic CAP profile to:

- `POST /capture`
- `POST /voice/turn`
- `POST /communication/translate`
- `POST /communication/interpret`
- local object updates
- Anytype write planning and execution

Enforced boundaries:

- Crisis language is denied for ordinary capture/rewrite and redirected to human support.
- Diagnosis, clinical conclusions, treatment/prescribing, health-risk scoring, and claims about another person's true intent/emotion are refused.
- Raw capture/transcript data stays local by default.
- External writes require explicit user confirmation.
- Anytype MCP calls are treated as constrained CAP tool invocations.

## API Surface

| Endpoint | Purpose |
| --- | --- |
| `GET /cap/capabilities` | Machine-readable matrix of CAP primitives implemented by Yar. |
| `GET /cap/rules` | Current local CAP policy terms, profile metadata, and policy refs. |
| `GET /cap/audit` | Exportable capture and voice CAP decisions/reports. |
| `GET /product/status` | Includes CAP version/profile and links to CAP endpoints. |

## Deliberate Limits

Yar does not yet implement:

- detached JWS/DSSE signature verification;
- OPA/Rego policy runtime;
- gRPC/protobuf CAP reference binding;
- OpenTelemetry `cap.*` emission;
- W3C PROV graph export;
- full evidence access control beyond local redacted pointers.

These are documented as explicit limits rather than hidden gaps. The implemented layer is still useful because all high-risk Yar actions now produce bounded CAP artifacts and audit records without exporting raw sensitive content.

## Acceptance Checks

Current automated checks cover:

- crisis/diagnosis/intent guard behavior;
- CAP rules/capabilities/audit endpoints;
- Anytype MCP constrained invocation and duplicate handling;
- mobile display of CAP refusal context;
- no raw API key leakage in Anytype status/write responses.
