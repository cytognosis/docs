# MCP/A2A Interop Evidence Report Template

Use this template for live external MCP/A2A interoperability runs. Local simulation output can be attached, but it does not close the external gate.

## Run Metadata

| Field | Value |
|---|---|
| Report id |  |
| Run date |  |
| CAP version/profile |  |
| Repository commit or package version |  |
| Environment | local simulation / single-organization external stack / multi-organization external run |
| Gate conclusion | external_evidence_required / ready_for_gate_review / blocked |
| Report owner |  |

## Partner Organizations

| Organization | Role | Trust domain | Runtime stack | Sign-off owner |
|---|---|---|---|---|
|  | Controller / registry / MCP server / A2A agent / observer |  |  |  |

## Trust Roots

| Trust item | Reference | Digest or key id | Validity window | Owner |
|---|---|---|---|---|
| Workload identity root |  |  |  |  |
| CAP signing public key |  |  |  |  |
| Authority/warrant root |  |  |  |  |
| Policy root |  |  |  |  |
| Capability root |  |  |  |  |
| Evidence root |  |  |  |  |
| Time source |  |  |  |  |

## Registry Records

| Registry | Record id | Version | Digest | Status |
|---|---|---|---|---|
| Capability |  |  |  |  |
| Policy |  |  |  |  |
| Evidence |  |  |  |  |
| Warrant/key |  |  |  |  |

## Fixture Manifest

| Fixture | Location or reference | Digest | Notes |
|---|---|---|---|
| CAPEnvelope directive bundle |  |  |  |
| MCP tool descriptor |  |  |  |
| MCP resource descriptor |  |  |  |
| A2A AgentCard |  |  |  |
| EvidenceRef set |  |  |  |
| PolicyRef set |  |  |  |
| PrivacyBoundary |  |  |  |

## Test Matrix

| ID | Flow | Expected result | Actual result | Evidence refs | Status |
|---|---|---|---|---|---|
| INT-MCP-01 | Allowed MCP `tools/call` | Handler executes and report is emitted. |  |  |  |
| INT-MCP-02 | Allowed MCP `resources/read` | Handler executes and EvidenceRefs are returned. |  |  |  |
| INT-MCP-03 | Forbidden MCP tool target | Refused before handler execution. |  |  |  |
| INT-MCP-04 | Tampered CAPEnvelope signature | Refused before payload use. |  |  |  |
| INT-MCP-05 | PolicyRef mismatch | Refused before handler execution. |  |  |  |
| INT-MCP-06 | EvidenceRef mismatch or expiry | Refused before evidence use. |  |  |  |
| INT-A2A-01 | A2A message carries CAPEnvelope part | Receiver accepts after Edge PEP verification. |  |  |  |
| INT-A2A-02 | AgentCard CAP extension advertised | Extension resolves and matches fixture. |  |  |  |
| INT-A2A-03 | Receiver or trust-domain mismatch | Refused before delivery. |  |  |  |
| INT-A2A-04 | Missing CAPEnvelope carriage | Refused or not accepted as CAP-governed traffic. |  |  |  |
| INT-PRIV-01 | Raw data egress attempt | Refused or transformed; raw content absent from shared logs. |  |  |  |
| INT-REPLAY-01 | Replay duplicate directive | Duplicate side effect prevented. |  |  |  |
| INT-OBS-01 | Observability sink coverage | Content-minimized audit, telemetry, and provenance refs recorded. |  |  |  |

## Log and Privacy Review

| Check | Result | Evidence |
|---|---|---|
| Shared logs contain no raw transcript/audio or raw sensitive evidence. |  |  |
| Shared logs contain no credentials, bearer headers, tokens, or private keys. |  |  |
| Refusals include reason codes without leaking protected content. |  |  |
| Audit/provenance refs are content-minimized. |  |  |
| Handler-executed flags are recorded for all refusal paths. |  |  |

## Findings

| Finding id | Severity | Description | Owner | Status | Retest evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Gate Conclusion

State exactly one conclusion:

- `external_evidence_required`: local simulation only, or no two-organization live run.
- `blocked`: external run completed but a required case failed or privacy/logging review found a blocking issue.
- `ready_for_gate_review`: two or more independent organizations completed the required cases with acceptable evidence and no blocking findings.

Sign-off:

| Organization | Sign-off owner | Date | Notes |
|---|---|---|---|
|  |  |  |  |
