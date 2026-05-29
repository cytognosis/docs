# Production KMS/HSM Operations Plan

This plan defines the deployment-facing responsibilities for CAP production signing keys. It does not implement a production KMS/HSM integration, and it does not close the production KMS/HSM release gate in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md).

The current repository uses deterministic or caller-supplied signing material for local tests, scaffolds, and compatibility evidence. Runtime-generated keys from `generate_runtime_keyset(...)`, deterministic attestation providers, local Biscuit warrant keys, and in-memory or test callbacks are non-production material. They must not be reused as production authority, policy, audit, transparency, evidence, or release-signing keys.

## Scope

This plan covers production custody for keys used to sign or verify CAP security evidence:

- `CAPEnvelope` signatures that cross trust boundaries.
- `AuthorityChainStep` signatures and Biscuit/Tenuo/Macaroon-equivalent warrant root keys.
- `GuardDecision` signatures.
- High-stakes `Directive` signatures.
- Signed policy bundles and emergency override bundles.
- Evidence snapshot attestations.
- Signed audit operations.
- DSSE/in-toto release and compensation attestations.
- Sigstore/Rekor publication keys or identities where a deployment controls them.

Out of scope for CAP itself: issuing workload identities, operating KMS/HSM products, storing secrets in this repository, defining cloud IAM policy, or replacing SPIFFE/SPIRE, OIDC, mTLS, Sigstore, or an organization-owned PKI.

## Existing Signer Interfaces

| Surface | Current repo hook | Production expectation |
|---|---|---|
| Detached JWS and DSSE payloads | `cap_protocol.security.cap_crypto.DetachedJWS`, `DSSE`, `KeyMaterial`, `KeyRegistry` | Replace direct private-key access with an external signer that returns equivalent signature metadata over the exact canonical payload bytes. Publish public keys through an organization-controlled key registry with revocation state. |
| Audit signing | `AuditSigningKeyProvider`, `ExternalAuditSigningKeyProvider`, `ExternalKMSHSMAuditSigningKeyProvider`, `SignedAuditSink` in `cap_protocol.runtime.observability` | Use a KMS/HSM signer behind `AuditSigningKeyProvider.sign(...)`. The sink must never persist private key material. Audit key custody metadata must identify provider, key id/version, custody mode, and access policy. |
| Authority warrants | `cap_protocol.runtime.warrants.encode_biscuit_authority_step(...)`, `verify_biscuit_authority_step(...)`, and `ServiceBackedKeyRegistry` | Use HSM-backed or KMS-backed root/signing keys for warrant issuance. Publish active public keys and revocation metadata through the Capability Registry or deployment key directory. |
| Authority-chain verification | `cap_protocol.runtime.authority.verify_authority_chain(...)` | Require fresh revocation checks for high-risk profiles and fail closed when production revocation status is unavailable. |
| Transparency bundles | `cap_protocol.security.transparency` local Rekor-compatible scaffold | Use external Sigstore/Rekor or equivalent transparency service, with monitored inclusion, checkpoint, and outage policy. |

## Key Roles

| Key role | Signs | Typical custody | Rotation trigger | Revocation source |
|---|---|---|---|---|
| Envelope signing key | Cross-boundary `CAPEnvelope` objects | Workload-bound KMS key, HSM key, or SPIFFE/JWT-bound signing service | Workload compromise, service owner change, scheduled rotation, algorithm migration | Key registry and workload identity status |
| Authority/warrant root key | `AuthorityChainStep` warrants or root delegation tokens | HSM or high-assurance KMS with dual control | Delegation-policy change, suspected compromise, trust-domain migration, scheduled ceremony | Capability Registry warrant-key directory and revocation service |
| Guard decision key | `GuardDecision` payloads | Guard/PDP-owned KMS key or signing service | Policy owner change, PDP compromise, scheduled rotation | Policy Registry and key registry |
| Policy bundle key | Signed policy bundles and emergency override bundles | Policy-owner HSM/KMS key with change-control approval | Policy release cadence, emergency rollback, compromise | Policy Registry signed-bundle revocation |
| Audit operation key | Signed audit operations | Dedicated audit KMS/HSM key with restricted signer role | Audit service migration, retention-policy change, compromise, scheduled rotation | Audit key registry and incident record |
| Evidence attestation key | Evidence snapshots and registry attestations | Evidence-service KMS/HSM key | Producer compromise, registry migration, scheduled rotation | Evidence Registry and attestation transparency records |
| Release/compensation attestation key | DSSE/in-toto release or rollback attestations | Release engineering HSM/KMS key or Sigstore identity | Release owner change, CI compromise, scheduled rotation | Release transparency log and key registry |
| Transparency publication identity | Rekor or equivalent entries | OIDC/Sigstore identity or HSM-backed signing key | Issuer migration, identity compromise | Transparency log monitor and issuer revocation |

## Custody Requirements

Deployment organizations must provide:

- A KMS/HSM or signing service for every production signing role.
- A public-key discovery path for verifiers, including key id, version, algorithm, validity window, owner, trust domain, and status.
- Revocation and suspension records that verifiers can query with bounded freshness.
- Separation of duties for key creation, activation, rotation, emergency override, and deletion.
- Access-control policy for signer use, with least privilege per CAP role.
- Audit logging of every signing request, denial, key state change, export attempt, policy change, and break-glass action.
- Incident-response procedures for key compromise and signer outage.
- Backup, escrow, and disaster-recovery rules that do not permit unauthorized private-key export.
- Regionality and compliance controls required by the deployment domain.

Private keys must not be checked into this repository, embedded in examples, written to test snapshots, exported into telemetry, or logged in audit/provenance records.

## Required Signing Request Shape

Production signers should accept a narrow request envelope:

| Field | Requirement |
|---|---|
| `key_role` | One of the key roles above. |
| `key_id` and `key_version` | Exact KMS/HSM key reference, not an alias that can silently move mid-session. |
| `payload_type` | CAP payload media type, for example `application/cap.signed-audit-operation+json`. |
| `canonicalization` | `rfc8785-jcs` for CAP v1 JSON payloads, or the selected DSSE/COSE/JOSE profile canonicalization. |
| `payload_hash` | Hash over the exact canonical payload bytes. |
| `signing_context` | Session, trace, issuer, workload identity, policy refs, authority refs, reason code, and ticket/change id when applicable. |
| `approval_context` | Required approval id for high-risk authority, policy, emergency override, or break-glass signing. |

The signer response should include:

- signature bytes or envelope metadata;
- key id and immutable key version;
- algorithm and canonicalization;
- payload hash;
- issued-at timestamp;
- signer service identity;
- signing audit ref;
- approval or change-control ref when required.

## Rotation Plan

Minimum production rotation requirements:

1. Create a new disabled key version under the same role, owner, and trust domain.
2. Publish the new public key as `pending` with a not-before time.
3. Run verifier compatibility checks against staged signatures and negative fixtures.
4. Activate the new key version and pin new sessions or bundles to it.
5. Keep old public keys available for verification until all signed objects expire or archival verification policy says otherwise.
6. Mark old signing versions disabled for new signatures.
7. Publish rotation evidence to audit/provenance and, where applicable, a transparency log.

High-risk roles should use shorter validity windows and explicit session or policy-bundle pinning. Emergency key rotation must fail closed for signatures that cannot be verified against a currently trusted or archival verification key.

## Revocation Plan

Production deployments must define revocation semantics for:

- key compromise;
- signer service compromise;
- workload identity compromise;
- policy owner compromise;
- delegated authority overreach;
- erroneous policy bundle or emergency override;
- audit signer misuse;
- transparency publication failure or log inconsistency.

For high-risk profiles, CAP verifiers should require live revocation freshness and return typed refusal when freshness cannot be established. The existing AuthorityChain verifier already supports a `revocation_provider` and `require_live_revocation_freshness`; production deployments must supply the provider and freshness SLA.

Revocation records should include key id, key version, trust domain, reason, actor, approval/change id, effective time, publication time, replacement key if any, and affected sessions or policy bundles.

## Incident Response

Each deployment must maintain a runbook for at least these incidents:

| Incident | Required response |
|---|---|
| Authority/warrant key compromise | Disable signing, publish revocation, rotate root or issuing key, refuse affected authority chains, identify delegated scopes, reissue valid delegations, and preserve incident audit. |
| Policy bundle key compromise | Revoke affected bundles, force policy refresh, pin safe replacement bundle, block emergency override signing until dual approval is restored. |
| Audit signing key compromise | Stop accepting signatures from the affected key version, preserve hash-chain records, rotate audit signer, verify replica integrity, and mark affected audit records for review. |
| Evidence attestation key compromise | Revalidate evidence snapshots where possible, revoke affected attestations, require fresh evidence for sensitive directives. |
| KMS/HSM outage | Fail closed for signing that grants new authority or updates policy. Continue verification from cached trusted public keys only inside documented freshness windows. |
| Unauthorized signing request | Deny request, alert owner, retain signer audit record, check workload identity and approval controls, and consider key suspension. |

Incident reports should feed back into [docs/security_review/findings_tracker_template.md](../security_review/findings_tracker_template.md) when the event affects the external security-review gate.

## Auditability

Production signer audit must be durable, content-minimized, and independently reviewable. At minimum, record:

- key role, key id, key version, algorithm, and custody provider;
- payload type and payload hash, not raw sensitive payloads;
- caller workload identity and authorization decision;
- approval/change-control reference;
- timestamp, region, signer service instance, and request id;
- result status and refusal reason;
- downstream CAP audit/provenance ref when a CAP object was emitted;
- rotation, revocation, deletion, and break-glass events.

Audit logs for signer operations should be protected separately from CAP telemetry. Telemetry delivery failure must not cause audit loss, and audit sink failure should block user-visible delivery when a profile requires audit-as-precondition.

## Deployment Evidence Checklist

The production KMS/HSM release gate remains open until the deployment organization supplies evidence for every item below:

- KMS/HSM architecture and ownership diagram.
- Key inventory for all CAP key roles, with owner, trust domain, algorithm, version, validity, and custody mode.
- Access-control policy and least-privilege signer IAM/ACLs.
- Rotation runbook and last successful rotation evidence.
- Revocation API or registry evidence with freshness SLA and failure behavior.
- Incident-response runbooks for the incidents above.
- Signer audit export evidence and access policy.
- Break-glass approval workflow and post-incident review requirement.
- Backup, disaster recovery, and key deletion policy.
- Proof that local ephemeral/demo/test keys are blocked from production configuration.
- Evidence that verifiers fail closed for unknown, revoked, expired, stale, or wrong-holder key material.
- External-review sign-off if KMS/HSM behavior is part of the independent security review scope.

## Configuration Placeholder

A non-secret placeholder config is provided at [config/kms_hsm.example.yaml](../../config/kms_hsm.example.yaml). It documents expected deployment-supplied values only. Do not put real provider URIs, credentials, tokens, private keys, or production account identifiers in that file.
