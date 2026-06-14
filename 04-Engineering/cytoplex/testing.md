> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `testing`

# Testing

## Standard Test Run

```bash
source venv/bin/activate
python -m pip install -e ".[dev]"
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

The explicit `NO_PROXY` setting prevents localhost HTTP smoke-test traffic from being routed through system proxy software on machines where that is configured.
This is a local test-environment caveat, not a CAP protocol requirement. Plain `pytest` can fail in proxy-configured environments because the HTTP/JSON smoke test uses localhost URLs and system proxy software such as Privoxy may intercept them.

The pytest suite covers:

- shared conformance fixture pass/fail behavior
- CAP message schema validation
- hardening runner output with a temporary runtime directory
- deterministic HTTP/JSON v1 CAPEnvelope smoke execution
- deterministic gRPC v1 CAPEnvelope smoke execution
- legacy CLI wrapper resolution
- CAP v1 LinkML schema structure and object-model checks
- CAP v1 schema/example validation
- CAP v1 Local PEP, local NER redaction, embedding-only egress, retention TTL deletion, mobile proxy Local PEP, attested Local PEP registration, and Edge PEP smoke behavior
- CAP v1 live model-stream adapter behavior, including wall-clock release, unsafe pre-display transform, semantic slow-path drift interception, backpressure, abort propagation, CLI/WebSocket abort UX, and CLI/WebSocket correction-frame UX
- Android/iOS separately privileged proxy Local PEP scaffold behavior for direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts
- attested Local PEP registration behavior for missing, expired, replayed, mismatched, untrusted, debuggable, production-verifier-missing, and valid deterministic test-double attestations
- local NER redaction, embedding-only egress, and retention TTL behavior for names, locations, dates, contact info, medical/financial identifiers, Supervisor Gateway context minimization, evidence-ref preservation, deterministic text/voice vectors, recipient binding, expired local memory deletion, Evidence Registry backing-content deletion, and audit records that exclude raw source text/audio/evidence
- separate v0.1 fixture conformance and v1 release-blocking deterministic scaffold conformance runners
- machine-checkable lifecycle FSM validation for envelope, directive, interrupt, execution, evidence, audit, and provenance traces, plus deterministic profile-inheritance composition and conflict-refusal behavior
- local deterministic benchmark harness execution and artifact generation for latency, streaming delay, CPU-time, memory, and mobile proxy-path measurements
- local Go third-implementation CAPEnvelope/JCS fixture validation and fixture-ID failure traceability

## CAP v1 Conformance Gate

```bash
source venv/bin/activate
cap-check-v1-conformance
```

This runs `V1-C01` through `V1-C15` as required deterministic scaffold cases. It is release-blocking for the current repository package, but it is not full CAP v1 runtime certification; full production/runtime evidence remains tracked in `docs/CAP_RELEASE_GATES.md`.

## Third Implementation Interop Adapter

```bash
cd third_impl/go_cap_adapter
go run . --fixtures testdata/cap_v1_interop.json --json
```

This runs the local standard-library Go adapter against shared CAP v1 CAPEnvelope/JCS/signature fixtures. The default pytest suite also covers it through `tests/test_go_interop_adapter.py` when the Go toolchain is available. This is local third-implementation fixture evidence, not external multi-organization interoperability certification.

## Benchmark Harness

```bash
source venv/bin/activate
python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10
```

This writes the published local artifacts under `docs/benchmarks/`. The reported p50/p95 latency, CPU-time, memory, streaming delay, and mobile proxy-path values are local microbenchmark evidence only; production device telemetry, measured battery drain, native mobile wrappers, model-provider latency, service-mesh latency, and networked registry/PDP latency remain separate release-gate evidence.

## Package Verification

```bash
python VERIFY_RELEASE_BASELINE.py
```

This checks required package files, stale forbidden labels, packaged private key material, and the release-blocking CAP v1 deterministic scaffold conformance gate. Generated runtime folders are ignored.

## Therapist/Supervisor Scenario

```bash
python -m cap_protocol.scenarios.therapist_supervisor.runner --case all
```

The deterministic scenario writes CAPEnvelope traces, Supervisor decisions, tool-call traces, privacy-boundary evaluations, capability evaluations, final responses, an `ExecutionReport`, and a summary under `runs/cap_therapist_supervisor_demo/<timestamp>/`.

## Integration Checks

```bash
python second_http/run_demo.py
python run_production_hardening.py
python run_final_cap.py --target both
```

The gRPC check uses checked-in generated protobuf modules and runtime-generated local mTLS certificates under `runtime_data/certs/` as non-production localhost transport fallback material. CAP v1 workload identity in both demos is the SPIFFE SVID carried by `CAPEnvelope.sender_id`/`receiver_id` and AuthorityChain `identity_binding`; Edge PEP and the authority verifier reject missing or mismatched SPIFFE SVID bindings. The HTTP/JSON check posts v1 `EvidenceRef` and `Directive` envelopes across localhost and receives v1 `ExecutionReport` acknowledgment envelopes. Do not run protobuf generation unless `cap.proto` changes.

## Real-Model Checks

Real-model tests are not run by default. They require optional dependencies, sufficient hardware, and model access:

```bash
export HF_TOKEN=your_huggingface_token
python -m pip install --upgrade torch torchvision accelerate safetensors pillow librosa
python -m pip install --upgrade "git+https://github.com/huggingface/transformers.git"
python run_final_cap.py --target both --use-real-separate-e2b --require-real-model
```

## Live Stream Checks

The default pytest suite includes `tests/test_live_model_streaming.py`, which uses `ScriptedModelStream` as a deterministic pull-based local stream. The runtime also exposes `OllamaModelStream` for callers that have a local or remote Ollama service available; the default tests do not require Ollama.

`tests/test_slow_path_classifier.py` covers the deterministic CAP-Med slow-path classifier, including subtle non-regex diagnostic and treatment drift fixtures, streaming integration, and fail-closed behavior when a configured classifier raises. Optional model-judge checks are not part of default CI.

`tests/test_ui_abort_propagation.py` covers per-platform stream-abort presentation. CLI and WebSocket-style adapters replace the visible stream region with safe text and avoid surfacing raw transport failures; Android and iOS checks verify the native `CapStreamAbort` API contracts because native wrappers are not checked in.

`tests/test_correction_frame_ux.py` covers late correction-frame presentation. CLI and WebSocket-style adapters replace the partial stream region and annotate the correction with safe copy; tests also verify Android/iOS `CapStreamCorrection` contracts, audit/provenance link preservation, and sanitization of unsafe correction text.

`tests/test_local_ner_redaction.py` covers the deterministic local redactor, Local PEP Supervisor-context preparation, Supervisor Gateway backend minimization, and the optional local-model NER adapter. The default suite does not require model downloads or a remote NER service.

`tests/test_embedding_only_egress.py` covers deterministic local text/voice embedding vectors, Local PEP embedding-only Supervisor projection, raw transcript/audio non-egress, Supervisor Gateway backend minimization, and recipient-bound privacy refusals. The default suite does not require model downloads or remote embedding services.

`tests/test_retention_ttl_deletion.py` covers `PrivacyBoundary.retention` TTL deletion for Local PEP raw backing storage and Evidence Registry backing blobs. It verifies that expired content is deleted, evidence resolvers refuse expired backing content, deletion audit/provenance records are preserved, and raw evidence does not leak into audit records.

`tests/test_cap_med_v1_profile.py` covers the CAP-Med v1 runtime-profile fixture. It validates the fixture against existing Core schemas, checks that CAP-Med constraints and metadata are namespaced under `cap-med/v1`, verifies unified `Capability` records and `InterruptDecision` mappings, and runs the signed hot-path smoke through Edge PEP, Local PEP, and Supervisor Gateway overreach refusal.
