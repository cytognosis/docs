# Organization OPA/Cedar Policy Deployment Guide

This guide prepares organizations to replace the repository's deterministic OPA-shaped and Cedar-shaped policy scaffolds with owned policy runtimes, policy bundles, promotion controls, and operational evidence. It does not deploy production OPA or Cedar, and it does not close the organization-specific policy deployment gate in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md).

The checked-in policies and adapter tests are local scaffold evidence. They are not production policy, not a regulated-profile approval, and not a substitute for organization-owned policy review.

## Scope

This guide covers:

- policy ownership and approval responsibilities;
- OPA/Rego and Cedar deployment choices;
- CAP PDP adapter request/decision contracts;
- Policy Registry and signed policy-bundle promotion;
- environment separation;
- rollout, rollback, hot update, emergency override, and exception handling;
- test promotion and evidence needed before a deployment can claim organization-specific policy readiness.

It does not define the organization's policy semantics, legal obligations, clinical/domain rules, cloud IAM, or runtime hosting platform.

## Existing CAP Policy Interfaces

| Surface | Current repo hook | Production expectation |
|---|---|---|
| CAP request shape | `CAPPolicyRequest` in `cap_protocol.runtime.pdp_adapters` | Organization-owned adapters should preserve subject, action, resource, context, constraints, evidence refs, policy refs, privacy boundary, and profile namespace. |
| OPA-shaped input | `opa_input(request)` | Real OPA/Rego policies should consume the same content-minimized input shape or a versioned superset. |
| Cedar-shaped request | `cedar_authorization_request(request)` | Real Cedar policies should preserve CAP principal/action/resource/context mapping and avoid raw evidence contents. |
| PDP decision shape | `PDPDecision` | Real adapters must return allow/deny/human-review decisions, reasons, constraints deltas, policy ids, runtime metadata, and fail-closed runtime availability. |
| Policy bundles | `PolicyBundle`, `OfflinePolicyBundleCache`, `ReferencePolicyRegistryService` in `cap_protocol.runtime.local_pep` | Production deployments must distribute signed bundles through an authenticated Policy Registry with session pinning, expiry, revocation, and audited hot-update behavior. |
| Guard conversion | gRPC `evaluate_policy_to_guard(...)` and HTTP `opa_policy_to_guard(...)` | Real policy decisions must still become CAP `GuardDecision` objects and must not bypass Local PEP or Edge PEP checks. |

## Ownership Model

Every production policy set should have named owners:

| Role | Responsibility |
|---|---|
| Policy owner | Owns policy intent, risk appetite, profile constraints, and approval to promote. |
| Domain reviewer | Reviews domain-specific behavior, for example CAP-Med non-diagnostic or CAP-SWE repository-write constraints. |
| Security reviewer | Reviews authority, privacy, data access, policy update, and emergency override impact. |
| Runtime owner | Operates OPA/Cedar services, adapters, registry clients, and availability monitoring. |
| Release owner | Signs and promotes bundles, manages staged rollout, and coordinates rollback. |
| Audit owner | Verifies policy evaluation, promotion, hot update, emergency override, and exception records. |

No single person or service should be able to write policy, approve it, sign the bundle, deploy it, and approve emergency override for high-risk profiles.

## Environment Separation

Use separate policy assets, signing keys, registries, and PDP endpoints per environment:

| Environment | Purpose | Requirements |
|---|---|---|
| `dev` | Policy authoring and adapter development. | Synthetic data only; no production signer; deterministic fixtures allowed. |
| `test` | Automated parity and negative tests. | Signed test bundles; production-like CAP input shapes; no production data. |
| `staging` | Deployment rehearsal and canary validation. | Staging KMS/HSM keys, staging Policy Registry, staged revocation source, production-like OPA/Cedar runtime. |
| `prod` | Organization-approved enforcement. | Production signer, production Policy Registry, monitored PDP runtime, live revocation, audit export, rollback path. |

Policy IDs, bundle IDs, digest refs, and PDP endpoints should include environment or trust-domain metadata so a non-production bundle cannot be silently used in production.

## Sample Layout

A non-production sample layout is checked in under [policies/organization_template](../../policies/organization_template/):

```text
policies/organization_template/
  README.md
  bundles/policy-bundle.manifest.example.json
  cedar/cap_policy.cedar
  opa/cap_policy.rego
  tests/policy_cases.example.jsonl
```

Organizations should copy the shape into their own repository or controlled policy workspace. Do not edit the template into production policy in this repository.

## Change Control

Minimum change-control fields:

- policy id, owner, profile namespace, engine, and entry point;
- reason for change and risk classification;
- affected CAP roles, actions, resources, PrivacyBoundary dimensions, and PolicyRefs;
- test evidence and reviewer approvals;
- signed bundle id, version, digest, expiry, and revocation ref;
- rollout plan, rollback plan, and monitoring checks;
- exception or emergency override criteria.

Policy changes should be reviewed as code and promoted only after deterministic CAP tests, engine-specific tests, negative/adversarial cases, and signature verification pass.

## Test Promotion

Before promotion from one environment to the next, run at least:

```bash
source venv/bin/activate
pytest tests/test_pdp_adapters.py tests/test_policy_registry_service.py tests/test_policy_hot_update.py
cap-check-v1-conformance
```

Deployment-owned policy repositories should add:

- OPA unit tests for Rego packages and entrypoints.
- Cedar schema validation and authorization tests.
- CAP parity fixtures proving equivalent allow/deny/human-review behavior where both OPA and Cedar are claimed.
- Negative tests for forbidden tools, raw-data egress, stale policy, unknown policy id, digest mismatch, expired bundle, revoked bundle, and runtime unavailable.
- Profile-specific tests for CAP-Med, CAP-SWE, or organization-owned profiles.
- Canary tests against staging PDP endpoints and staging Policy Registry.

Promotion should fail closed if an external runtime is required but unavailable, mirroring `CedarPolicyAdapter(require_external_runtime=True)`.

## Rollout

Recommended rollout:

1. Publish the signed bundle as `candidate` in the target environment Policy Registry.
2. Run staging/canary CAP traces using the exact `policy_id`, `version`, and `digest`.
3. Activate the bundle for new sessions only.
4. Keep existing sessions pinned to their current bundle unless the profile explicitly allows hot update.
5. Monitor refusals, `stale_policy`, `require_policy_update`, `privacy_denied`, PDP latency, runtime unavailability, and emergency override counters.
6. Expand rollout by trust domain, profile, service, or user cohort.
7. Record rollout evidence in audit/provenance and release notes.

## Rollback

Rollback must be preplanned before promotion:

- keep the last known-good bundle active and verifiable;
- disable new sessions from receiving the bad bundle;
- revoke the bad bundle in the Policy Registry;
- force hot update only when the profile and incident response approve it;
- record affected sessions and policy refs;
- add regression tests for the failure before re-promoting.

Existing sessions should remain pinned unless the risk of staying pinned is higher than the risk of forced update.

## Hot Updates

CAP treats hot update as explicit. A Local PEP or Executor must not silently authorize a directive when its `PolicyRef.version` or `PolicyRef.digest` disagrees with the active signed bundle.

Production hot update requires:

- profile-level permission for hot update;
- signed target bundle with valid expiry and revocation state;
- Policy Registry audit event;
- session pin update record;
- reason code and approval ref;
- verifier behavior for stale in-flight directives.

If the hot update cannot be proven, return `stale_policy` or the Guard/PDP equivalent `require_policy_update`.

## Emergency Override And Exceptions

Emergency override must be narrower than ordinary policy relaxation:

- dual approval for high-risk profiles;
- signed emergency bundle with short expiry;
- clear scope, affected identities, and affected actions;
- mandatory audit and post-incident review;
- automatic rollback or expiry;
- refusal if signature, digest, expiry, or revocation metadata is invalid.

Exceptions should be modeled as policy data with owner, expiry, reason, scope, and audit refs, not as code paths that bypass PDP, Local PEP, Edge PEP, or Policy Registry checks.

## Deployment Evidence Checklist

The organization-specific OPA/Cedar deployment gate remains open until a deployment organization supplies:

- policy ownership matrix and approval workflow;
- environment topology and endpoint separation;
- OPA/Rego and/or Cedar policy repository with tests;
- CAP adapter mapping and versioned request schemas;
- signed policy-bundle generation and verification evidence;
- Policy Registry publication, revocation, session pinning, hot-update, and rollback evidence;
- emergency override process and last drill or tabletop evidence;
- PDP runtime monitoring, latency, availability, and fail-closed behavior;
- audit export showing policy evaluation and promotion events without raw sensitive evidence;
- evidence that sample policies in this repository are not used as production policy.

## External Gate Status

This guide is preparation evidence only. The external gate remains open until a real organization supplies owned policies, real OPA/Cedar runtime deployment evidence, signed bundle operations, and operational review artifacts.
