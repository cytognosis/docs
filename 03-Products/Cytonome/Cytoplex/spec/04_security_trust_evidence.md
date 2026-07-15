> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP_04 — Security, Trust, and Evidence

## 1. Security posture

CAP assumes that individual components can be compromised, evidence can be prompt-injected, tools can be malicious, and policies can become stale. CAP therefore focuses on **structural controls**:

- bounded Directives;
- explicit Guard decisions;
- typed refusal;
- authority-chain verification;
- evidence freshness and integrity;
- telemetry/provenance for review.

CAP does not claim that a model is safe, truthful, or immune to jailbreaks.

CAP v1 adds a stronger deployment assumption: enforcement must be placed where bypass can be controlled. For the Therapist/Supervisor scenario, the Local PEP must be the only path from the local Therapist/interviewer agent to user-visible output and to raw local evidence. A central Supervisor cannot bypass Local PEP privacy, non-diagnostic, non-prescriptive, jurisdiction, or safety vetoes.

## 2. Identity and transport security

CAP does not issue identities or certificates. Deployments SHOULD use established identity/authentication systems such as SPIFFE/SPIRE, DID, X.509, OAuth/OIDC, or mTLS.

A CAP implementation SHOULD expose stable workload identities in `sender_id`, `receiver_id`, `guard_identity`, and `agent_id`. These identities are inputs to policy evaluation; they are not policy decisions by themselves.

CAP v1 treats service meshes, mTLS, SPIFFE/SPIRE, and OIDC as substrates. When a mesh is present, CAP should consume mesh-provided identity and transport security instead of reimplementing them. CAP enforcement remains at the application-semantic layer: envelopes, directives, evidence references, privacy boundaries, and streaming output.

The current Python v1 scaffold consumes normalized SPIFFE SVID identities through `cap_protocol.runtime.workload_identity`. Deployments can provide `CAP_SPIFFE_ID`/`SPIFFE_ID` for deterministic tests or a mounted X.509 SVID via `CAP_SPIFFE_X509_SVID_PATH`; production deployments should source the same SPIFFE ID from SPIRE Workload API or a service mesh. Edge PEP can require `sender_id` and `receiver_id` to be valid SPIFFE IDs in the expected trust domain, and AuthorityChain verification now refuses missing, malformed, mismatched, or cross-domain SPIFFE SVID bindings. Runtime-generated localhost mTLS certificates remain only a non-production transport fallback for the gRPC demo and are not accepted as primary CAP v1 workload identity material.

The service-mesh composition scaffold in `cap_protocol.runtime.service_mesh` documents the local integration shape for Istio/Linkerd-style deployments. A workload pod declares the application container and a CAP Edge PEP application sidecar; the mesh sidecar is injected by labels/annotations such as `sidecar.istio.io/inject=true` or `linkerd.io/inject=enabled`. The mesh owns mTLS and SVID-backed workload identity. CAP consumes the expected SPIFFE ID and continues to validate detached CAPEnvelope signatures, timestamp/TTL, PolicyRefs, PrivacyBoundary decisions, AuthorityChain holder binding, and payload privacy. The generated manifest intentionally does not set `CAP_SPIFFE_ID` for mesh mode, so CAP does not mint or duplicate the mesh identity; deterministic local fallback remains available through an explicit `local-fallback` topology.

## 3. Attestations and signatures

The current package demonstrates detached-JWS, DSSE, and in-toto-style attestations. CAP v1 uses established signature envelope formats rather than custom cryptographic primitives.

Canonicalization decision:

- JSON encodings for production CAP v1 signatures MUST use RFC 8785 JSON Canonicalization Scheme (JCS), or a standards-based JOSE/COSE/DSSE library profile that defines equivalent deterministic payload bytes.
- Non-JSON encodings MUST use the canonicalization rules of their selected envelope or serialization standard, not an ad hoc CAP-specific byte format.
- The checked-in Python helper exposes both canonicalization modes. Helper-generated v1 signatures use and label `rfc8785-jcs`; archived v0.1 compatibility signatures keep the deterministic JSON encoder (`sort_keys=True`, compact separators, UTF-8) and label `json-deterministic-sort-keys-v0.1`. The local Go third-implementation adapter independently verifies the shared v1 JCS/detached Ed25519 fixture suite. Verifiers select the canonical payload bytes from explicit signature metadata without invalidating archived v0.1 samples.

Signing envelope expectations:

- Detached JWS-style signatures sign the exact canonical payload bytes and carry `protected`, `signature`, `payload_hash`, `payload_included`, `payload_type`, and `canonicalization` metadata. For the current unencoded detached payload form, the protected header uses `alg=EdDSA`, a `kid`, `typ`, critical `b64=false`, and a `canon` value matching the signature metadata for newly generated signatures.
- DSSE and in-toto-style attestations carry the canonical payload in the envelope, bind it with DSSE pre-authentication encoding, and include `payloadType`, `payload`, `signatures`, `payload_hash`, and canonicalization metadata where the profile permits extension fields.
- Verifiers MUST recompute the canonical payload hash before signature verification and MUST refuse on hash mismatch, malformed envelope metadata, unknown or revoked key id, unsupported algorithm, or invalid signature.
- Signature verification MUST NOT log hidden chain-of-thought, raw transcript/audio, or raw sensitive evidence; refusals should identify object refs and digest metadata only.

Required signing targets:

- `AuthorityChainStep`
- `GuardDecision`
- high-stakes `Directive`
- evidence snapshots
- signed audit operations when an audit sink is configured as durable evidence or as a user-visible delivery precondition
- compensation/rollback attestations
- `CAPEnvelope` whenever it crosses a trust boundary

Exact signed payloads:

- `AuthorityChainStep`: sign every step field except the embedded `signature` object. When `warrant_format=biscuit-v2`, the Biscuit warrant signs a canonical claim payload for the step and the readable `signature` object records the warrant payload hash. `previous_step_hash`, revocation metadata, scope, capability, identity binding, and expiry are inside the signed or warranted payload when present.
- `GuardDecision`: sign every decision field except `signature`, including `subject_ref`, policy refs, reasons, issuer, issue/expiry times, and any constraints delta.
- High-stakes `Directive`: sign every directive field except `signature`, including action, target, constraints refs or inline constraints, authority chain refs, policy refs, evidence refs, reversibility, expiry, and idempotency key.
- Evidence snapshots: sign or attest the immutable snapshot bytes or their content-addressed digest plus media type, confidentiality label, producer identity, freshness metadata, and access policy ref. Do not embed raw sensitive evidence in logs or telemetry.
- Signed audit operations: sign the event type, content-minimized audit event, next hash-chain sequence, previous-chain hash, retention/access policy metadata, key-custody descriptor, and replication/export policy. The current reference sink verifies these detached-JWS payloads against the durable hash chain and can fail closed before user-visible delivery when a profile requires audit confirmation.
- Compensation/rollback attestations: sign a DSSE or in-toto-style statement whose subject is the side-effect or execution-report digest and whose predicate records the compensation action, result, actor, timestamps, and residual manual-review requirements.
- Cross-boundary `CAPEnvelope`: sign the unsigned envelope object after removing only `signature`; the signed payload includes `cap_version`, envelope/session/trace ids, sender, receiver, message kind, exactly one of `payload` or `payload_ref`, authority chain ref, policy refs, privacy boundary ref, timestamp, ttl, and profile extensions.

CAP messages MAY also rely on transport authentication inside a single trust boundary, but profiles SHOULD explicitly state when message-level attestations are relaxed.

CAP v1 authority chains should be backed by cryptographic capability warrants: attenuating, holder-bound, offline-verifiable tokens with monotonic narrowing semantics. Profiles may use Biscuit, Tenuo, Macaroons, or an equivalent primitive, but must state how warrant steps bind to workload identities, signatures, revocation metadata, policy references, and delegation constraints. CAP Core requires the binding fields; it does not mandate one warrant primitive.

The current repository chooses Biscuit for the v1 warrant scaffold because Biscuit is an attenuating capability-token primitive with native offline verification and caveat checks. `warrant_format=biscuit-v2` steps carry a `warrant_token` object with the Biscuit token, root key id, signed CAP-claims hash, canonicalization, and payload type. The token caveats bind the runtime holder identity, required capability, and requested scope; the CAP verifier then checks policy refs, expiry, revocation freshness, holder binding, and cross-step scope attenuation. Detached-JWS authority steps remain supported as compatibility/scaffold coverage.

### Production KMS/HSM custody

Production deployments must supply their own KMS/HSM or equivalent signing service for CAP signing roles. The deployment-facing plan is [docs/kms_hsm/README.md](../../../../04-Engineering/cytoplex/security/kms_hsm.md), and the non-secret placeholder shape is [config/kms_hsm.example.yaml](../config/kms_hsm.example.yaml). That plan covers key roles, custody, rotation, revocation, incident response, auditability, signer request/response metadata, and deployment evidence.

The current `KeyMaterial`, runtime-generated keyset, deterministic Biscuit warrant keys, and test signing callbacks are local scaffold material. They are not production key custody and must not be treated as deployment evidence. The `ExternalKMSHSMAuditSigningKeyProvider` interface is a fail-closed hook for deployments to bind an external signer; a deployment must still provide the actual signer, access policy, public-key discovery, revocation source, audit trail, and runbooks.

### Sigstore/Rekor transparency

CAP does not define a transparency-log protocol. Deployments SHOULD use Sigstore Rekor or an equivalent append-only transparency service when publishing release attestations, authority-step attestations, compensation attestations, or other cross-organization evidence that must be discoverable after issuance.

The current repository includes a deterministic local Rekor-compatible scaffold in `cap_protocol.security.transparency`. It logs two artifact classes:

- release attestations: DSSE-wrapped in-toto statements whose subject is a release or verification artifact digest;
- AuthorityChainStep attestations: DSSE-wrapped in-toto statements whose subject is the canonical unsigned authority-step digest and whose predicate records delegatee, capability, scope, policy digest, and signature payload hash.

The local scaffold produces a Rekor-style bundle with a hashedrekord-like entry body, signed entry timestamp, Merkle inclusion proof, checkpoint metadata, and the DSSE attestation envelope. Verifiers can check the attestation signature, signed entry timestamp, entry-body digest, and inclusion proof offline from the bundle. Local tests and hardening checks use this deterministic fixture; production publication still depends on external Sigstore/Rekor service availability, key custody, log monitoring, and operational policy for when publication is unavailable.

## 3.1 Clock skew and expiry

Profiles SHOULD define a clock-skew tolerance for signed CAP objects. The current v1 temporal scaffold defaults to 30 seconds.

Envelope verifiers first validate the detached signature over the exact unsigned `CAPEnvelope`, then apply temporal checks before payload dereference or privacy-boundary payload inspection:

1. If `timestamp` is later than verifier time plus profile skew tolerance, refuse with `RefusalMessage.reason_code = clock_skew_exceeded`.
2. If `timestamp + ttl_ms` is not later than verifier time, refuse with `RefusalMessage.reason_code = expired`.
3. Only then may the verifier inspect or dereference payload content.

Directive execution paths MUST also refuse a Directive whose `expires_at` or legacy `expiry` is not later than verifier time. That refusal uses `expired` and occurs before executor side effects.

The current Python v1 scaffold centralizes these checks in `cap_protocol.runtime.temporal`. Edge PEP envelope verification, AuthorityChain `issued_at`/`not_before`/`expires_at` checks, Local PEP directive and policy-bundle expiry, Supervisor Gateway authority expiry, registry metadata freshness, EvidenceRef freshness, and the gRPC/HTTP v1 binding validators reuse the shared helper. This keeps refusal codes consistent across deterministic tests: future timestamps beyond the default skew use `clock_skew_exceeded`, expired envelopes/directives/authority steps use `expired`, stale policy material uses `stale_policy`, and stale EvidenceRefs use `stale_evidence`.

## 3.2 Policy freshness and hot updates

Policy references are part of the authority surface. A Local PEP or Executor MUST NOT silently authorize a Directive when its `PolicyRef.version` or `PolicyRef.digest` disagrees with the active signed policy bundle. The safe result is `RefusalMessage.reason_code = stale_policy` or a GuardDecision equivalent such as `require_policy_update`.

The current Local PEP can compare Directive `policy_refs` against the active `PolicyBundle.policy_refs`. When configured with `ReferencePolicyRegistryService`, it fetches verified signed bundles from the service, pins one bundle version/digest per session by default, refuses directives that require an unapproved hot update, and only rotates a pinned session when explicit hot-update or emergency-override mode is enabled. Emergency override bundles are audited and still must pass signature, digest, and expiry checks.

Organization-specific OPA/Cedar deployment guidance is in [docs/policy_deployment/README.md](../../../../04-Engineering/infrastructure/policy-deployment/README.md), with a non-production sample layout under [policies/organization_template](../policies/organization_template/). That guide covers ownership, environment separation, policy promotion, rollback, hot updates, exception handling, and test evidence. The checked-in deterministic policy adapters and sample policies are not production policy deployment evidence.

Stale policy is distinct from stale evidence: policy version/digest mismatches use `stale_policy`, while expired or freshness-failed EvidenceRefs use `stale_evidence`.

### Offline policy-bundle fallback

When the central Control Plane or PDP is unreachable, a Local PEP MAY continue only from a cached signed policy bundle whose version, digest, expiry, and signature metadata are valid under the active profile. Missing, expired, malformed, or unverifiable policy material MUST fail closed for sensitive local turns.

For the Therapist/Supervisor scenario, offline fallback permits only profile-safe supportive local output. Raw transcript/audio upload, external messaging, new high-risk tool use, irreversible side effects, and other sensitive actions must be denied unless a fresh policy bundle authorizes a narrower behavior. Offline mode does not let a central Supervisor bypass the Local PEP.

The current Python Local PEP checks bundle id, version, digest shape, expiry, signature metadata, and optional signed-payload verification through the existing detached-JWS helper. The reference Policy Registry service requires verified signed payloads by default, records fetch/refusal/override audit events, and rejects revoked bundles while the service is reachable. The local `OfflinePolicyBundleCache` remains the fallback when the Control Plane is unreachable; it validates cached signed bundles but cannot observe fresh service-side revocation while offline. This is still not a production Policy Registry deployment or KMS/HSM signing-custody implementation.

## 3.3 Local PEP trust modes

CAP v1 defines three Local PEP deployment modes:

| Mode | Use case | Trust property |
|---|---|---|
| Trusted in-process library | First-party trusted agents in controlled infrastructure. | Bypass resistance is a development and code-review concern. |
| Separately privileged proxy | Mobile, desktop, or server deployments where the agent should not directly reach user, network, or tools. | OS or platform routing prevents bypass. |
| Attested isolated process | High-assurance profiles. | Control Plane registration requires platform attestation. |

The Therapist/Supervisor scenario should default to separately privileged proxy for implementation planning and move to attested isolated mode for high-assurance mobile deployments.

The current repository includes a deterministic Android/iOS separately privileged proxy scaffold in `cap_protocol.runtime.mobile_local_pep`. It declares Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, manifest-shaped route-control metadata, and smoke checks that refuse direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts.

The current repository also includes deterministic attested isolated Local PEP registration in `cap_protocol.runtime.attested_local_pep`. The Control Plane registrar issues challenge/nonce payloads, verifies detached-JWS responses from the deterministic test provider, requires provider-specific verifier hooks for production attestation contracts, binds the evidence to SPIFFE workload identity and Local PEP version, refuses missing, expired, replayed, mismatched, untrusted, or production-verifier-missing attestations, and publishes Local PEP capability metadata only after verification. The built-in provider is a deterministic test double; Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote contracts are declared but need production verifier integrations.

These scaffolds are not native mobile or attestation certification: platform entitlements, native project wiring, device or emulator instrumentation, app-store/notarization review evidence, hardware-backed production verifiers, native/mobile performance telemetry, measured battery drain, and operational rollout remain external work.

## 4. Authority-chain verification algorithm

Before accepting a Directive or cross-boundary CAPEnvelope, a PEP or Executor MUST resolve `authority_chain_ref` to an `AuthorityChain` or use the embedded `Directive.authority_chain`, then perform the following checks before payload use or side effects:

1. Parse and validate the enclosing object and the resolved AuthorityChain schema.
2. Confirm the Directive or envelope timestamp/expiry is valid under the active profile.
3. Confirm the requested action kind is supported.
4. Resolve the effective policy set from `policy_refs`; each authority step also carries the policy reference under which the delegation is valid.
5. Verify every required `AuthorityChainStep`:
   - `delegator`, `delegatee`, `identity_binding`, and trust domain match an accepted identity substrate such as SPIFFE, X.509, OIDC, DID, or a profile-selected equivalent;
   - holder binding proves that the step's token or attestation is usable by the `delegatee`, not merely by whoever possesses the bytes;
   - `capability` is supported and authorizes the requested operation class;
   - `scope` includes the action/tool/resource target;
   - each delegated step monotonically attenuates previous scope and constraints rather than expanding them;
   - `issued_at`, `not_before` when present, and `expires_at` are valid under profile clock-skew rules;
   - `revocation_ref` is checked against the deployment's revocation source, or fails closed when the active profile requires online revocation freshness;
   - `delegation_constraints` are present and compatible with the requested action and privacy boundary;
   - `previous_step_hash` matches the prior step when ordered chaining is used;
   - signature, DSSE, COSE, JOSE, in-toto, or profile-selected warrant verification succeeds over the exact unsigned or warranted step payload.
6. Refuse missing chains or invalid identity/scope/capability with `unauthorized`.
7. Refuse unsupported local executor capability with `insufficient_capability`.
8. Refuse expired steps with `expired`.
9. Refuse malformed or unverifiable attestations with `invalid_signature`.
10. Verify required GuardDecision objects are present and unexpired.
11. Merge Guard constraints with Controller constraints.
12. Resolve EvidenceRefs, if required.
13. Verify evidence hash, freshness protocol, access policy, confidentiality constraints, and media type.
14. Verify the applicable PrivacyBoundary before payload dereference or outbound delivery.
15. Refuse if any required check fails.

The current Python v1 runtime includes a `verify_authority_chain` reference verifier for signed JSON and Biscuit-backed AuthorityChain steps. It verifies required binding fields, SPIFFE SVID holder identity when the binding type is `spiffe`, capability, scope, policy ref shape, `issued_at`/`not_before` skew, expiry, revocation markers supplied by the caller, optional live service-backed revocation freshness, attenuation by scope subset, previous-step hashes, detached Ed25519 signatures, and `biscuit-v2` warrant tokens. `ServiceBackedKeyRegistry` can resolve active warrant-signing keys from the Capability Registry reference service and fails closed for rotated or revoked keys. This is still a reference integration: production deployments still need SPIRE/service-mesh rollout, KMS/HSM signing custody, operational key ceremonies, and external interoperability evidence for their selected warrant profile.

## 5. Evidence integrity and freshness

Evidence is always treated as untrusted until verified.

### Requirements

- Evidence SHOULD be content-addressed where possible.
- Mutable external state MUST be snapshotted or attested before being used as evidence.
- EvidenceRef MUST include a hash when integrity matters.
- EvidenceRef SHOULD include `created_at`, `expires_at`, `freshness_policy`, `producer_identity`, and `access_policy_ref`.
- Stale evidence MUST result in `RefusalMessage.reason_code = stale_evidence` or a GuardDecision requiring fresh evidence.
- Evidence access denial MUST result in `evidence_access_denied`.
- Hash mismatch MUST result in `evidence_hash_mismatch`.
- When backing evidence content is dereferenced, implementations SHOULD re-hash the retrieved content and compare it with the EvidenceRef hash before using it. Refusals should identify the EvidenceRef URI, not log raw evidence content.

The current registry reference service persists registry metadata, content-addressed Evidence blobs, attestation metadata, and revocation state locally. Evidence put/get/verify operations compute `sha256:` URIs, store media type and size, attach a reference attestation object, validate EvidenceRef `expires_at` and future `created_at`, and re-hash dereferenced bytes before use. Expired backing blobs can be garbage-collected by TTL while registry/audit metadata stays content-minimized and available for accountability. Edge PEP payload-ref dereference can be backed by this service: signature, time, policy, authority, and privacy-boundary checks run before the Evidence Registry resolver is called; hash mismatch or expired/missing backing content returns a typed refusal without logging raw evidence content. Registry metadata expiry and service-backed revocation freshness are validated separately before cached registry records are treated as fresh.

## 6. Prompt injection through evidence

Evidence may contain malicious natural-language instructions. CAP's mitigation is a strict separation between evidence content and protocol constraints.

Executors MUST NOT treat instructions inside EvidenceRef payloads as CAP authority. Only `Directive`, `GuardDecision`, `ConstraintSet`, `PolicyRef`, and verified authority steps can authorize action.

Recommended implementation controls:

- parse CAP control objects outside the LLM context path;
- pass evidence to models as quoted/untrusted data;
- use structured extraction before model reasoning;
- sanitize tool results before feeding them to Controllers;
- use Guard policies for evidence origin and media type;
- never allow retrieved evidence to modify `allowed_tools`, `forbidden_tools`, budgets, or data access scopes.

## 7. Confused deputy mitigation

A confused deputy attack occurs when an Executor uses its own privilege to perform an action that the Controller was not authorized to request.

Mitigations:

- every Directive carries scoped authority;
- tools/resources are called under effective constraints;
- Executor policy checks both Controller authority and Executor capability;
- MCP servers or downstream services SHOULD enforce their own authorization;
- high-risk actions SHOULD use attenuated, per-Directive credentials where possible.

## 8. Replay semantics

CAP distinguishes two replay types.

### Structural replay

Structural replay verifies the trace without re-running model inference or external tools. It checks schemas, timestamps, lifecycle transitions, authority chains, policy refs, evidence hashes, and terminal states.

Structural replay is the primary CAP audit target.

### Semantic replay

Semantic replay re-executes models/tools using recorded inputs. Outputs may diverge because LLM sampling, model versions, external APIs, time-dependent data, and mutable environments can change.

CAP MUST NOT claim bit-exact semantic replay.

## 9. Privacy and minimization

CAP supports minimization by reference.

- Controllers SHOULD pass EvidenceRefs, not raw sensitive blobs, unless a profile requires inline data.
- EvidenceRef SHOULD include `confidentiality_label` and `access_policy_ref`.
- Redacted variants SHOULD use `redaction_ref` and provenance relations to the original.
- Observers MUST avoid exporting sensitive evidence contents into telemetry attributes.
- DecisionRecord MUST NOT include raw chain-of-thought or unnecessary personal data.

CAP v1 models privacy as a structured policy expression rather than a closed enum. A `PrivacyBoundary` carries nine first-class dimensions: classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw-data egress, and minimization. `boundary_id` is an identifier and `policy_refs` is supporting metadata, not an additional dimension. The PDP evaluates those dimensions; the Local PEP enforces redaction, evidence-reference substitution, recipient restrictions, raw-egress denial, embedding-only projection, retention TTL deletion, and outbound filtering. For the Therapist/Supervisor scenario, `raw_data_egress.raw_transcript` and `raw_data_egress.raw_audio` are explicit booleans and both are denied by default. Supervisor consultation receives locally redacted context and evidence references, or policy-allowed local embeddings plus aggregate dimensions, unless profile policy explicitly authorizes a narrower exception.

The current repository includes a deterministic in-process privacy PDP helper for this model. It returns typed denials with the failing boundary dimension, while deployed local/central PDP services and Policy Registry distribution remain v1 runtime backlog items.

The current Local PEP also includes a local-only NER redaction pipeline for Supervisor-context preparation. Raw transcript/audio fields are substituted into local EvidenceRefs first, then text-like context fields are redacted into category tags before Supervisor Gateway backend access. The deterministic fallback covers person names, locations and street addresses, dates, email addresses, phone numbers, SSNs, medical IDs, financial IDs, credit-card numbers, and IP addresses without downloading model weights. A caller can supply a local model adapter for additional entity spans, but remote NER is rejected because redaction must precede cross-boundary egress. Redaction events record field paths, hashes, categories, and counts with `raw_content_logged=false`; they must not log raw source text or matched span text.

The Local PEP can also run text and voice embedding encoders locally for Supervisor requests marked as embedding-only. Raw transcript/audio source material stays inside the Local PEP boundary; the cross-boundary payload carries embedding vectors, source/embedding hashes, encoder and model refs, provenance refs, evidence refs, aggregate dimensions, safety flags, recipient-binding metadata, and minimization metadata with `raw_content_logged=false`. The default deterministic encoders are CI fixtures, not production semantic or privacy-quality claims, and the active PrivacyBoundary still restricts embedding egress to identity-bound allowed recipients.

`PrivacyBoundary.retention.raw_local_ttl_seconds` maps to raw backing-content TTL for Local PEP `local-evidence://` refs and Evidence Registry backing blobs. Deletion events preserve hashes, refs, expiry/deletion timestamps, and provenance refs, but not raw transcript, raw audio, or raw evidence bytes. Audit retention is intentionally separate: audit records follow `audit_ttl_seconds` or the deployment audit-retention policy so deletion can prove what was removed without retaining the removed content itself.

## 10. Late veto and compensation

A Guard decision may arrive after execution begins. If the decision denies a still-running Directive, the Executor SHOULD abort if safe. If external side effects already occurred, compensation policy determines whether to compensate, alert, or preserve the state for manual review.

Irreversible actions SHOULD require stronger Guard policy and explicit human/workflow authority in profiles.

## 11. Streaming interruption and correction

CAP v1 requires streaming behavior to be explicit and uses the streaming terminology defined in `CAP_03_primitives.md#7-interruptdecision-target-primitive`. The target Local PEP applies configurable lookahead on outgoing streams before user-visible delivery. If unsafe diagnostic or treatment-advice content is detected while still buffered, the Local PEP applies a buffered transform or another pre-display interrupt. If unsafe content has already been partially emitted, the Local PEP emits a correction frame, preserves the original and correction in audit by reference, and reports `partially_emitted_then_corrected` or the profile-equivalent terminal status.

The current package includes Local PEP tests for chunk-level configurable lookahead, buffered transform, semantic slow-path classifier interception, late correction-frame linkage, wall-clock timer release, pull-side backpressure, abort propagation, CLI/WebSocket-style abort UX, CLI/WebSocket-style correction-frame replacement/annotation UX, and refusal of Supervisor attempts to force unsafe stream output. The reference live-stream adapter feeds local scripted model chunks, or optional Ollama chunks when a caller supplies an available service, through the Local PEP before user-visible delivery. The default slow path is deterministic for CI and catches curated non-regex CAP-Med clinical drift; deployments can opt into an Ollama model-as-judge with explicit latency and availability tradeoffs. `docs/benchmarks/cap_v1_latency_mobile_budget.md` records local deterministic stream-gate and timer-release benchmark evidence for the reference path. The scaffold links the stream id, partial-emission audit ref, InterruptDecision, correction frame, execution report, correction audit ref, frame audit refs, and provenance-style refs without storing unsafe diagnostic text in the user-visible correction. `cap_protocol.runtime.ui_abort` defines concrete CLI/WebSocket abort replacement behavior and Android/iOS `CapStreamAbort` contracts; `cap_protocol.runtime.ui_correction` defines concrete CLI/WebSocket correction-frame replacement/annotation behavior and Android/iOS `CapStreamCorrection` contracts. Native SDK wrappers are not checked in. Production model-provider rollout, shipping native UI wrappers, organization-selected model-judge rollout, native/device performance telemetry, measured battery drain, and deployed audit/provenance sinks remain future runtime work tracked in `CAP_v1_TASKS.md`.
