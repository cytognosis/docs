# Multi-Organization MCP/A2A Interop Plan

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This package prepares the external live MCP/A2A interoperability gate. It is a runbook and evidence format for partner organizations. It does not close the gate by itself: local simulation and repository-maintainer-only execution remain local evidence.

The release-gate status is tracked in CAP_RELEASE_GATES.md (target archived/removed). Integration mappings are described in CAP_05_integrations.md (target archived/removed).

## Objective

Demonstrate that CAPEnvelope authority, policy, privacy, evidence, and refusal semantics survive real cross-organization MCP and A2A operation.

The minimum run uses two separately controlled organizations:

| Role | Responsibility | Required owner |
|---|---|---|
| Organization A controller | Issues signed CAPEnvelope directives and publishes controller identity metadata. | Partner A security or platform owner |
| Organization A registries | Provides policy, capability, evidence, revocation, and warrant-key references used by A. | Partner A registry owner |
| Organization B MCP server | Hosts at least one allowed MCP `tools/call`, one allowed MCP `resources/read`, and one forbidden tool target. | Partner B agent/tool owner |
| Organization B A2A agent | Publishes AgentCard CAP extension metadata and receives CAPEnvelope-wrapped A2A messages. | Partner B agent/tool owner |
| Independent observer | Records transcript hashes, decision results, log extracts, and report sign-off. | Jointly agreed reviewer |

Optional third or fourth organizations can add another controller, another MCP server, or an A2A peer with a different trust root. More organizations strengthen the evidence, but two independent owners are the minimum external run.

## Existing Local Harness

The repository already has a deterministic local harness:

- [substrate_interop.py](../../src/cap_protocol/runtime/substrate_interop.py) builds in-process MCP and A2A peers.
- [test_live_substrate_interop.py](../../tests/test_live_substrate_interop.py) checks MCP `tools/call`, MCP `resources/read`, forbidden-tool refusal before handler execution, A2A CAPEnvelope carriage, AgentCard CAP extension metadata, and tampered-envelope refusal.
- [go_cap_adapter](../../third_impl/go_cap_adapter) validates shared CAPEnvelope/JCS/signature fixtures in Go, but it does not host MCP or A2A services.

Run the local simulation from the repository root:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py tests/test_go_interop_adapter.py
```

Local simulation is useful for partner onboarding and fixture debugging. It is not external multi-organization evidence.

## Partner Setup

Each organization should prepare a short environment sheet before the live run:

| Field | Required content |
|---|---|
| Organization id | Stable display name and trust-domain URI. |
| Contact owners | Security, registry, platform, and tool/agent owners. |
| Runtime stack | MCP server/runtime, A2A implementation, CAP adapter version, deployment environment. |
| CAP version | Supported CAP version and profile names. |
| Identity system | SPIFFE, OIDC, X.509, DID, or other identity used at the service boundary. |
| Network path | Ingress URL or service name, mTLS or token-auth shape, firewall allowlist owner. |
| Privacy boundary | Raw-data egress rules, logging policy, retention policy, allowed recipients. |
| Report owner | Person who can sign off that the run used organization-owned systems. |

Use [config/mcp_a2a_interop.example.yaml](../../config/mcp_a2a_interop.example.yaml) as a non-secret checklist. Do not store real tokens, private keys, credentials, account ids, or partner-confidential endpoints in the repository.

## Trust Roots

Before test execution, partners exchange or agree on these non-secret trust anchors:

| Trust item | Required evidence |
|---|---|
| Workload identity root | SPIFFE trust bundle, OIDC issuer/JWKS URL, X.509 CA bundle, or equivalent root reference. |
| CAP signing keys | Public key ids, algorithm, key-use metadata, rotation owner, and validity window. |
| Authority/warrant root | AuthorityChain root, warrant-key directory, revocation reference, and attenuation rules. |
| Policy root | Policy Registry base URL or bundle location, policy id, version, digest, and entry point. |
| Capability root | Capability Registry base URL or exported record set for AgentCard, MCP tools, and MCP resources. |
| Evidence root | Evidence Registry base URL or content-addressed storage root with hash verification. |
| Time source | NTP or equivalent clock source and allowed skew. |

The run should fail closed if any required trust root is missing, expired, revoked, or mismatched.

## Registry Setup

Each external run needs registry records for the exact live endpoints under test:

| Registry | Minimum records |
|---|---|
| Capability Registry | A2A agent capability, MCP tool capability, MCP resource capability, controller/service capability. |
| Policy Registry | Signed policy bundle or immutable policy record with digest, version, entry point, and environment. |
| Evidence Registry | Test EvidenceRefs with content hashes, freshness policy, media type, size, access policy ref, and expiry. |
| Warrant/key registry | CAP signing public keys, AuthorityChain or warrant keys, revocation state, and rotation metadata. |

Registry records should be exported as evidence refs or hashes in the final report. Raw evidence content should not be copied into the report.

## Fixtures

Create one fixture bundle per partner run. The fixture bundle should include:

| Fixture | Required fields |
|---|---|
| CAPEnvelope directive | `envelope_id`, `session_id`, `trace_id`, sender, receiver, message kind, policy refs, privacy boundary ref, authority chain ref, timestamp, TTL, and signature. |
| MCP tool descriptor | Server URI, tool URI/name, input schema hash, operation `tools/call`, risk level, and CAP constraints. |
| MCP resource descriptor | Server URI, resource URI/name, media type, operation `resources/read`, and CAP constraints. |
| A2A AgentCard | Agent URL, CAP extension URI, supported CAP version, supported message types, and envelope-required flag. |
| EvidenceRef set | URI, hash, media type, size, expiry, freshness policy, access policy ref, and provenance ref. |
| PolicyRef set | Policy id, engine, version, digest, URI, and entry point. |
| PrivacyBoundary | Classification, movement, transformation, retention, logging, audit visibility, raw-data egress, minimization, and allowed recipients. |

Use content-addressed references and hashes for fixtures whenever possible. Keep raw transcripts, raw audio, hidden reasoning, credentials, private keys, and sensitive partner data out of fixture files.

## Required Test Cases

The live run should include these pass and fail cases. Additional partner-specific cases can be appended.

| ID | Flow | Expected result |
|---|---|---|
| INT-MCP-01 | Org A sends signed CAPEnvelope directive to Org B MCP `tools/call` for an allowed tool. | Allowed; handler executes; ExecutionReport includes tool result refs and Edge PEP decision evidence. |
| INT-MCP-02 | Org A sends signed CAPEnvelope directive to Org B MCP `resources/read` for an allowed resource. | Allowed; resource handler executes; response returns EvidenceRefs, not raw sensitive content. |
| INT-MCP-03 | Org A requests a forbidden MCP tool target. | Refused before handler execution; refusal reason identifies forbidden target or policy denial. |
| INT-MCP-04 | CAPEnvelope signature is tampered after signing. | Refused before payload use or handler execution. |
| INT-MCP-05 | PolicyRef digest or version does not match the pinned registry record. | Refused before handler execution. |
| INT-MCP-06 | EvidenceRef hash mismatches backing content or evidence is expired. | Refused before evidence influences execution. |
| INT-A2A-01 | Org A sends an A2A message whose part carries `application/cap-envelope+json`. | Allowed; receiver verifies CAPEnvelope and records accepted message id. |
| INT-A2A-02 | Org B AgentCard advertises CAP v1 support and envelope-required metadata. | AgentCard metadata resolves through registry or live discovery and matches the report. |
| INT-A2A-03 | A2A receiver id or trust domain does not match the signed CAPEnvelope. | Refused before message delivery. |
| INT-A2A-04 | A2A message omits required CAPEnvelope carriage. | Refused or not accepted as CAP-governed traffic. |
| INT-PRIV-01 | Fixture attempts raw transcript, raw audio, or unrestricted result egress across the boundary. | Refused or transformed according to PrivacyBoundary; raw content is absent from logs. |
| INT-REPLAY-01 | A previously accepted directive is replayed with the same idempotency key. | Duplicate side effect is prevented and outcome is auditable. |
| INT-OBS-01 | Audit, telemetry, and provenance sinks receive content-minimized events for allowed and refused flows. | Report includes event ids or hashes without raw sensitive content. |

## Logging and Privacy Rules

Logs and reports should include:

- envelope ids, session ids, trace ids, partner ids, timestamps, and decision status;
- policy ids, policy digests, capability ids, evidence hashes, authority/warrant refs, and key ids;
- handler-executed booleans for every allow/refusal path;
- audit, telemetry, and provenance event ids or hashes;
- redaction/minimization metadata and `raw_content_logged=false` where applicable.

Logs and reports must not include:

- private keys, tokens, credentials, bearer headers, or partner secrets;
- raw transcript/audio, raw sensitive evidence, hidden reasoning, unsafe partial output, or matched redaction spans;
- unredacted endpoint internals that a partner marks confidential.

Partner organizations should retain their own raw operational logs under their governance controls. The shared report should contain hashes, ids, and summaries sufficient to reproduce the gate conclusion without leaking protected content.

## Report Format

Use [report_template.md](report_template.md) for the external evidence report. A valid report includes:

- partner organization identities and sign-off owners;
- trust roots and registry records used for the run;
- fixture manifest hashes;
- pass/fail matrix for every required test case;
- selected log/audit/provenance references;
- privacy review notes;
- open findings and retest status;
- explicit gate conclusion.

The conclusion must distinguish:

- local simulation only;
- live external-stack test by one organization;
- live multi-organization test by at least two independent organizations.

Only the third category can support closing the live multi-organization MCP/A2A gate.

## Local Simulation Mode

Use local simulation before inviting partners:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py
```

Optional companion check:

```bash
source venv/bin/activate
pytest tests/test_go_interop_adapter.py
```

Record local simulation output in the report only as onboarding evidence. Mark the gate conclusion as `external_evidence_required` unless two independent organizations ran live MCP/A2A endpoints or equivalent external stacks.

## Closure Rule

The live multi-organization MCP/A2A gate can close only when:

- at least two independent organizations execute the required MCP and A2A cases against live or deployment-representative endpoints;
- trust roots, registries, policies, warrants, and EvidenceRefs are organization-owned or organization-approved for the run;
- every required fail-closed case refuses before handler execution or message delivery;
- logs and reports are content-minimized and reviewed for privacy leakage;
- any blocking findings have fixes or documented mitigations and retest evidence;
- release docs are updated without claiming more than the evidence supports.
