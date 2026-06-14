> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `dev-setup`

# Development

## Environment

Use the existing Python environment:

```bash
cd cap_protocol
source venv/bin/activate
python -m pip install -e ".[dev]"
```

If the environment does not exist, create it from the repository root:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

## Source Layout

Implementation code lives under `src/cap_protocol`. Top-level scripts and `reference_grpc/` / `second_http/` contain compatibility wrappers only. Keep new implementation work inside the package.

Use `cap_protocol.paths` for repository paths such as schemas, policies, binding roots, and output folders. Do not add new `sys.path` mutations inside implementation modules.

## Schema Authoring

CAP v1 schema authoring follows the Cytos LinkML structure:

- `schemas/cap.yaml` is the umbrella schema.
- `schemas/core.yaml` holds shared types, enums, and reusable classes.
- `schemas/domains/*.yaml` contains domain modules for authority, evidence, privacy, capability, constraints, control objects, and non-Core profile/scenario contracts.

The current executable schema artifacts remain reviewed JSON Schema Draft 2020-12 files under `schemas/cap-core/`. They are not generated into the runtime validation path yet. LinkML and JSON Schema drift is checked by comparing essential fields, required fields, enums, cardinalities, and numeric minima between the v1 LinkML authoring schema and the checked-in v1 JSON Schema artifacts.

Validate the authored LinkML structure with:

```bash
pytest tests/test_cap_v1_linkml.py
```

Run the standalone v1 drift check with:

```bash
python scripts/check_v1_schema_drift.py
```

After reinstalling the editable package, the same check is also available as `cap-check-v1-schema-drift`. The same drift check is covered by `tests/test_cap_v1_linkml.py`, so CI can include either the script command or the pytest suite.

## Test Baseline and Localhost Proxy Caveat

Use the repo-local virtual environment and bypass system proxies for localhost HTTP smoke tests:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

The `NO_PROXY` setting is local testing guidance, not a CAP protocol requirement. Plain `pytest` can fail in proxy-configured environments because localhost HTTP traffic may be routed through system proxy software such as Privoxy.

## Protobuf

Generated protobuf modules are checked in for deterministic runs. Regenerate only when `src/cap_protocol/bindings/grpc_reference/cap.proto` changes:

```bash
python scripts/generate_proto.py
```

The script normalizes generated imports to package-relative imports.

## Runtime Output

Generated files belong in ignored locations:

- `final_output/`
- `runtime_data/`
- `*/runtime_data/`
- `certs/`
- runtime key folders

Clean them with:

```bash
rm -rf final_output runtime_data reference_grpc/runtime_data second_http/runtime_data
rm -rf src/cap_protocol/bindings/grpc_reference/runtime_data src/cap_protocol/bindings/http_json/runtime_data
find . -name __pycache__ -type d -prune -exec rm -rf {} +
```

## Production Key Custody

Local runtime keys, deterministic attestation keys, fixture signing keys, and in-memory signer callbacks are non-production. Do not reuse them for deployed CAP authority, policy, audit, transparency, evidence, release, or envelope signing.

Production deployments should follow `docs/kms_hsm/README.md` and keep real KMS/HSM provider references, credentials, tokens, private keys, account identifiers, and signer endpoints outside this repository. `config/kms_hsm.example.yaml` is a non-secret placeholder shape only.

## Organization Policy Deployment

The repository's OPA-shaped and Cedar-shaped adapters are deterministic scaffolds. Organization-owned policy deployment should follow `docs/policy_deployment/README.md`, use `config/policy_deployment.example.yaml` only as a non-secret placeholder, and treat `policies/organization_template/` as a layout template rather than production policy.

## Real-Model Mode

Runtime code no longer installs model dependencies automatically. Install optional model packages manually, then run:

```bash
export HF_TOKEN=your_huggingface_token
python run_final_cap.py --target both --use-real-separate-e2b --require-real-model
```

## Live Model Streaming

`cap_protocol.runtime.live_model_streaming` keeps the default live stream path dependency-free. Use `ScriptedModelStream` for deterministic local streaming tests, or `OllamaModelStream` when a caller provides an available Ollama service. Both paths feed chunks through `LocalPEP.open_stream_gate(...)`; do not send model chunks directly to user-visible output in new demos.

## Benchmarks

Run the local deterministic latency and mobile-resource benchmark harness with:

```bash
source venv/bin/activate
python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10
```

The command writes `docs/benchmarks/cap_v1_latency_mobile_budget.json` and `docs/benchmarks/cap_v1_latency_mobile_budget.md`. These artifacts measure local Python p50/p95 latency, CPU-time proxy units, tracemalloc peak memory, streaming delay, and Android/iOS proxy scaffold paths. They do not measure native device battery drain, production model-provider latency, service-mesh latency, or networked registry/PDP latency.

## Go Third Implementation Interop Adapter

The local third implementation adapter lives under `third_impl/go_cap_adapter` as a separate Go module with standard-library dependencies only. Run it from its module directory:

```bash
cd third_impl/go_cap_adapter
go test ./...
go run . --fixtures testdata/cap_v1_interop.json --json
```

The adapter validates shared CAP v1 CAPEnvelope/JCS/signature fixtures and reports fixture IDs for pass/fail traceability. Keep it scoped to cross-implementation fixture validation; it is not the place for production registries, PEP services, policy engines, or key-custody code.

## MCP/A2A Interop Simulation

The local MCP/A2A substrate harness lives in `cap_protocol.runtime.substrate_interop` and is covered by `tests/test_live_substrate_interop.py`. Run it before inviting external partners:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py tests/test_go_interop_adapter.py
```

Use `docs/mcp_a2a_interop/README.md`, `config/mcp_a2a_interop.example.yaml`, and `docs/mcp_a2a_interop/report_template.md` for partner planning. Local simulation output is onboarding evidence only; external multi-organization evidence remains required.

## Domain Semantic-Quality Evaluation

Domain semantic-quality evaluation is separate from CAP structural conformance. Run the synthetic onboarding fixture with:

```bash
source venv/bin/activate
python -m cap_protocol.evaluation.semantic_quality --cases examples/domain_semantic_quality/cap_med_synthetic_cases.jsonl --scores examples/domain_semantic_quality/synthetic_reviewer_scores.jsonl
pytest tests/test_semantic_quality_evaluation.py
```

Use `docs/domain_semantic_quality/README.md`, `docs/domain_semantic_quality/reviewer_rubric.md`, and `config/domain_semantic_quality.example.yaml` to plan external expert review. Synthetic fixture scores are smoke evidence only.

## Regulated-Profile Review Packet

Regulated-profile review is separate from structural CAP conformance, security review, and semantic-quality scoring. Use `docs/regulated_profile_review/README.md`, `docs/regulated_profile_review/reviewer_checklist.md`, `docs/regulated_profile_review/open_questions.md`, `docs/regulated_profile_review/report_template.md`, and `config/regulated_profile_review.example.yaml` to prepare CAP-Med or similar profile review.

Run the local packet evidence checks with:

```bash
source venv/bin/activate
pytest tests/test_cap_med_v1_profile.py tests/test_supervisor_gateway_service.py tests/test_human_review_integration.py tests/test_semantic_quality_evaluation.py
python scripts/check_doc_links.py
python scripts/check_claim_language.py
```

Do not store raw participant data, raw transcript/audio, credentials, clinical records, or partner-confidential review material in the packet or config placeholder.

## Slow-Path Classifier

`LocalPEP` runs fast regex checks and a semantic slow-path classifier before user-visible output is released. The default `DeterministicCapMedSlowPathClassifier` is CI-safe and catches curated non-regex CAP-Med drift fixtures. Optional model-as-judge deployments can instantiate `OllamaSemanticClassifier` with a caller-managed Ollama service and quantized local model; this adds latency to stream buffers and should be benchmarked for the deployment profile.

## Local NER Redaction

`LocalPEP.prepare_supervisor_context(...)` runs local-only NER redaction after raw transcript/audio substitution and before Supervisor Gateway backend access. The default `DeterministicLocalNERRedactor` is dependency-free for CI and offline fallback, replacing sensitive spans with category tags such as `[PERSON]`, `[LOCATION]`, `[DATE]`, `[EMAIL]`, `[PHONE]`, `[SSN]`, `[MEDICAL_ID]`, `[FINANCIAL_ID]`, `[CREDIT_CARD]`, and `[IP_ADDRESS]`. Deployments can pass `LocalModelNERRedactor` with a caller-managed local NER provider for additional categories, for example `[ORGANIZATION]`; remote NER providers are intentionally rejected because redaction must happen before cross-boundary egress.

Redaction audit events must record field paths, category counts, hashes, redaction refs, and `raw_content_logged=false`; do not add raw source text or matched span text to audit, telemetry, provenance, or test snapshots. Preserve `evidence_refs`, `policy_refs`, signatures, authority refs, privacy refs, and routing metadata when adding new payload fields.

## Embedding-Only Egress

`LocalPEP.prepare_supervisor_context(...)` can project Supervisor consultation payloads marked with `embedding_only` into local text/voice embeddings plus aggregate dimensions, safety flags, evidence refs, provenance refs, and minimization metadata. The default `DeterministicTextEmbeddingEncoder` and `DeterministicVoiceEmbeddingEncoder` are dependency-free CI fallbacks; production deployments can pass caller-managed local encoders through the Local PEP constructor, but remote encoders are rejected because raw transcript/audio must not leave the local boundary before embedding.

Embedding-only payloads must not contain `raw_transcript`, `raw_audio`, or `redacted_context`. Keep provenance to hashes, encoder ids, model refs, local evidence refs, modality, vector dimensions, and recipient-binding metadata. The active `PrivacyBoundary.allowed_recipients` list still gates the recipient identity, and untrusted recipients must receive a typed `privacy_denied` refusal without raw source text or audio bytes.

## Retention TTL Deletion

`PrivacyBoundary.retention.raw_local_ttl_seconds` now drives Local PEP raw backing storage for substituted `local-evidence://` refs. `LocalPEP.collect_retention_garbage(...)` deletes expired raw local transcript/audio backing content and emits `RetentionDeletion` audit/provenance metadata with hashes, refs, expiry time, deletion time, and `raw_content_logged=false`.

`ReferenceCapabilityRegistryService.collect_retention_garbage(...)` deletes expired Evidence Registry backing blobs while preserving registry/audit metadata. Deletion audit events must stay content-minimized: include hashes, media type, size, trust domain, expiry, deletion time, and provenance refs, but never raw evidence bytes. Audit retention is governed separately by `audit_ttl_seconds` or the caller-supplied audit retention policy.

## Lifecycle FSM and Profile Inheritance

`cap_protocol.runtime.lifecycle` is the executable source for CAP lifecycle states and transitions across envelope, directive, interrupt, execution, evidence, audit, and provenance domains. Keep docs, tests, and V1 conformance checks aligned with that module when adding or changing lifecycle states; skipped preconditions and terminal-to-active resumes should fail validation.

`cap_protocol.profiles.inheritance` is the executable source for profile composition. New profile work should preserve monotonic narrowing: parents apply before children, allowed/resource lists intersect, forbidden lists union, numeric ceilings take the minimum, required booleans cannot be unset, risk levels can only move stricter, and profiles cannot redefine Core lifecycle states or interrupt actions.

## CAP-Med Runtime Profile

`cap_protocol.profiles.cap_med` is the CAP-Med v1 runtime-profile fixture. Keep CAP-Med-only fields under `profile_constraints.cap-med/v1` or `profile_extensions.cap-med/v1`; do not add non-diagnostic, non-prescriptive, human-confirmation, raw-transcript, or Supervisor metadata as top-level Core fields. The hot-path smoke should continue to verify signed `CAPEnvelope` handling through Edge PEP, Local PEP raw-transcript minimization, Supervisor Gateway strategy translation, and Local PEP veto of raw-data Supervisor overreach.

## UI Abort Propagation

`cap_protocol.runtime.ui_abort` maps terminal stream decisions to client surfaces. The repository implements deterministic CLI and WebSocket-style presentation adapters that replace the active stream region with safe text before closing or stopping the stream. Android and iOS native wrappers are not present in this repo; their contracts require a `CapStreamAbort` event with `reasonCode`, `replacementText`, `interruptRef`, and `reportRef`, and the native UI must replace the message bubble on the main UI thread before cancelling the transport.

## Correction Frame UX

`cap_protocol.runtime.ui_correction` maps late Local PEP correction frames to client surfaces. CLI and WebSocket-style adapters replace the partial stream region identified by `partial_emission_ref` and add a short safe correction notice; Android and iOS native wrappers are not present, but their contracts require a `CapStreamCorrection` event that carries replacement text, notice text, partial-emission, interrupt, report, audit, and provenance refs. Correction copy must not quote unsafe original stream text.

## Mobile Local PEP Proxy

`cap_protocol.runtime.mobile_local_pep` models the separately privileged proxy trust mode for Android and iOS. The scaffold declares Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, manifest-shaped route-control metadata, and deterministic smoke checks for user-output, network, raw-data egress, local-tool, and missing OS-route bypass attempts. It is a Python contract and test scaffold; native projects, platform entitlements, and device instrumentation are not checked in.

## Attested Local PEP Registration

`cap_protocol.runtime.attested_local_pep` models the attested isolated Local PEP trust mode before Capability Registry publication. Use `AttestedLocalPEPRegistrar.issue_challenge(...)` to bind a challenge to `pep_id`, SPIFFE workload identity, Local PEP version, profile, trust domain, and nonce, then submit a signed attestation response through `register(...)`. The default deterministic provider is a test double for CI and signs detached-JWS payloads. Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote contracts are declared as production-verifier requirements; `AttestedLocalPEPVerifier` refuses those providers unless a provider-specific platform verifier hook is supplied.
