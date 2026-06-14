# CAP V1 Baseline: Done Prompt Archive

**Generated:** 2026-05-25T06:54:46+00:00
**Document set:** CAP V1 baseline consolidated Markdown set
**Repository status:** V1 architecture documented and V1 runtime scaffold present; current executable package remains `v0.1-production-candidate` and is not a complete stable V1 runtime.

This archive preserves the implementation prompt documents under the 20-document cap for the baseline V1 folder.

## Source Map

- `docs/task_prompts/cap_v1/Done/DOC-FIX-01_operationalconstraints_human_confirmation_placement.md`
- `docs/task_prompts/cap_v1/Done/DOC-FIX-02_privacyboundary_dimension_count_alignment.md`
- `docs/task_prompts/cap_v1/Done/DOC-FIX-03_streaming_buffer_default_and_diagram_alignment.md`
- `docs/task_prompts/cap_v1/Done/DOC-FIX-04_capability_shape_inline_documentation.md`
- `docs/task_prompts/cap_v1/Done/DOC-FIX-05_legacy_interrupt_vocabulary_rewrite.md`
- `docs/task_prompts/cap_v1/Done/DOC-FIX-06_normative_streaming_terminology.md`
- `docs/task_prompts/cap_v1/Done/P0-DOC-01_reframe_public_docs.md`
- `docs/task_prompts/cap_v1/Done/P0-DOC-02_two_tier_three_plane_architecture.md`
- `docs/task_prompts/cap_v1/Done/P0-DOC-03_therapist_supervisor_scenario.md`
- `docs/task_prompts/cap_v1/Done/P0-DOC-04_current_vs_target_alignment.md`
- `docs/task_prompts/cap_v1/Done/P0-DOC-05_localhost_proxy_testing_caveat.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-01_replay_idempotency.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-02_clock_skew_expiry.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-03_stale_policy_hot_update.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-04_evidence_tamper.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-05_offline_fallback.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-06_sidecar_bypass.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-07_streaming_correction.md`
- `docs/task_prompts/cap_v1/Done/P1-CONF-08_supervisor_overreach.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-01_cap_envelope.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-02_interrupt_decision.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-03_privacy_boundary.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-04_operational_constraints.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-05_capability.md`
- `docs/task_prompts/cap_v1/Done/P1-SCHEMA-06_linkml_json_schema_generation.md`
- `docs/task_prompts/cap_v1/Done/P1-SEC-01_canonicalization_signing.md`
- `docs/task_prompts/cap_v1/Done/P1-SEC-02_cap_warrant_authority_chain.md`
- `docs/task_prompts/cap_v1/Done/P1-T10_make_v1_c01_through_v1_c15_release_blocking.md`
- `docs/task_prompts/cap_v1/Done/P1-T1_migrate_grpc_reference_binding_to_capenvelope.md`
- `docs/task_prompts/cap_v1/Done/P1-T2_migrate_http_json_binding_to_capenvelope.md`
- `docs/task_prompts/cap_v1/Done/P1-T3_implement_rfc_8785_jcs_for_v1_signatures.md`
- `docs/task_prompts/cap_v1/Done/P1-T4_wire_local_pep_onto_agent_to_user_and_local_tool_paths.md`
- `docs/task_prompts/cap_v1/Done/P1-T5_wire_edge_pep_onto_cross_boundary_paths.md`
- `docs/task_prompts/cap_v1/Done/P1-T6_implement_runtime_interruptdecision_and_composition_rules.md`
- `docs/task_prompts/cap_v1/Done/P1-T7_implement_structured_privacyboundary_pdp_evaluation.md`
- `docs/task_prompts/cap_v1/Done/P1-T8_apply_clock_skew_and_expiry_uniformly.md`
- `docs/task_prompts/cap_v1/Done/P1-T9_use_capability_as_unified_registration_object.md`
- `docs/task_prompts/cap_v1/Done/P2-DOC-01_architecture_diagrams.md`
- `docs/task_prompts/cap_v1/Done/P2-DOC-02_therapist_supervisor_sequences.md`
- `docs/task_prompts/cap_v1/Done/P2-DOC-03_schema_appendix_migration.md`
- `docs/task_prompts/cap_v1/Done/P2-DOC-04_v1_release_gates.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-01_local_pep.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-02_edge_pep.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-03_streaming_lookahead_buffer.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-04_offline_policy_bundle_cache.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-05_supervisor_gateway_stub.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-06_federated_registry_stubs.md`
- `docs/task_prompts/cap_v1/Done/P2-RUNTIME-07_observability_plane_sinks.md`
- `docs/task_prompts/cap_v1/Done/P2-T10_implement_human_review_integration.md`
- `docs/task_prompts/cap_v1/Done/P2-T11_wire_opentelemetry_collector_and_attribute_coverage.md`
- `docs/task_prompts/cap_v1/Done/P2-T12_implement_signed_audit_operations.md`
- `docs/task_prompts/cap_v1/Done/P2-T13_wire_w3c_prov_store.md`
- `docs/task_prompts/cap_v1/Done/P2-T14_implement_service_mesh_composition_test.md`
- `docs/task_prompts/cap_v1/Done/P2-T15_implement_workflow_engine_composition_sample.md`
- `docs/task_prompts/cap_v1/Done/P2-T16_integrate_sigstore_and_rekor_transparency.md`
- `docs/task_prompts/cap_v1/Done/P2-T17_implement_live_mcp_and_a2a_substrate_interop.md`
- `docs/task_prompts/cap_v1/Done/P2-T18_split_controller_into_distinct_deployable.md`
- `docs/task_prompts/cap_v1/Done/P2-T1_deploy_capability_registry_service.md`
- `docs/task_prompts/cap_v1/Done/P2-T2_deploy_policy_registry_and_signed_bundle_distribution.md`
- `docs/task_prompts/cap_v1/Done/P2-T3_deploy_agent_and_tool_registry_services.md`
- `docs/task_prompts/cap_v1/Done/P2-T4_deploy_evidence_registry.md`
- `docs/task_prompts/cap_v1/Done/P2-T5_implement_cedar_pdp_adapter.md`
- `docs/task_prompts/cap_v1/Done/P2-T6_integrate_biscuit_or_tenuo_warrant_primitive.md`
- `docs/task_prompts/cap_v1/Done/P2-T7_integrate_spiffe_spire_workload_identity.md`
- `docs/task_prompts/cap_v1/Done/P2-T8_deploy_supervisor_gateway_service.md`
- `docs/task_prompts/cap_v1/Done/P2-T9_implement_session_router.md`
- `docs/task_prompts/cap_v1/Done/P3-T10_build_cap_swe_non_medical_reference_profile.md`
- `docs/task_prompts/cap_v1/Done/P3-T11_benchmark_latency_and_mobile_resource_budget.md`
- `docs/task_prompts/cap_v1/Done/P3-T12_build_third_implementation_interop.md`
- `docs/task_prompts/cap_v1/Done/P3-T13_formalize_lifecycle_fsm_and_profile_inheritance.md`
- `docs/task_prompts/cap_v1/Done/P3-T14_migrate_cap_med_v1_profile_end_to_end.md`
- `docs/task_prompts/cap_v1/Done/P3-T1_integrate_live_model_streaming.md`
- `docs/task_prompts/cap_v1/Done/P3-T2_implement_slow_path_classifier.md`
- `docs/task_prompts/cap_v1/Done/P3-T3_implement_ui_abort_propagation_per_platform.md`
- `docs/task_prompts/cap_v1/Done/P3-T4_design_and_implement_correction_frame_ux.md`
- `docs/task_prompts/cap_v1/Done/P3-T5_implement_mobile_separately_privileged_proxy_local_pep.md`
- `docs/task_prompts/cap_v1/Done/P3-T6_implement_attested_isolated_local_pep.md`
- `docs/task_prompts/cap_v1/Done/P3-T7_implement_local_ner_redaction_pipeline.md`
- `docs/task_prompts/cap_v1/Done/P3-T8_implement_embedding_only_egress.md`
- `docs/task_prompts/cap_v1/Done/P3-T9_implement_retention_timers_and_ttl_deletion.md`
- `docs/task_prompts/cap_v1/Done/P4-T1_prepare_independent_security_review_package.md`
- `docs/task_prompts/cap_v1/Done/P4-T2_prepare_production_kms_hsm_operations_plan.md`
- `docs/task_prompts/cap_v1/Done/P4-T3_prepare_organization_specific_opa_cedar_deployment_guide.md`
- `docs/task_prompts/cap_v1/Done/P4-T4_prepare_multi_organization_mcp_a2a_interop_plan.md`
- `docs/task_prompts/cap_v1/Done/P4-T5_prepare_domain_semantic_quality_evaluation_harness.md`
- `docs/task_prompts/cap_v1/Done/P4-T6_prepare_regulated_profile_review_packet.md`

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-01_operationalconstraints_human_confirmation_placement.md`

## Task Prompt: DOC-FIX-01 OperationalConstraints Human Confirmation Placement

### Implementation Status

Completed as documentation, schema metadata, example, and validation-test alignment work.

Placement decision:

- v0.1 `ConstraintSet.requires_human_confirmation` remains a compatibility field for the current v0.1 demo shape.
- CAP v1 Core `OperationalConstraints` does not include top-level `requires_human_confirmation`.
- In CAP v1, profile-specific confirmation obligations belong under a namespaced `profile_constraints` entry; policy-driven human review is represented by `GuardDecision.require_human_review` and the resulting authority or policy decision.

Updated files:

- `docs/CAP_02_core_model.md`
- `docs/CAP_03_primitives.md`
- `docs/CAP_appendix_schemas.md`
- `schemas/domains/constraints.yaml`
- `schemas/cap-core/v1/operational-constraints.schema.json`
- `examples/cap-core/v1/operational-constraints.json`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_schemas.py tests/test_cap_v1_linkml.py
python scripts/check_v1_schema_drift.py
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: targeted v1 schema tests passed, no CAP v1 LinkML/JSON Schema drift was detected, and the full test suite passed.

Status update after P1-T2: active gRPC and HTTP/JSON hot paths now use v1 objects, but this task itself only aligned documentation and v1 schema artifacts. Human review integration and full end-to-end profile runtime migration remain separate production gaps.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-01`.

Objective: resolve the documentation inconsistency between v0.1 `ConstraintSet.requires_human_confirmation` and v1 closed `OperationalConstraints`.

Inspect: `docs/CAP_03_primitives.md`, `docs/CAP_appendix_schemas.md`, `schemas/domains/control.yaml`, `schemas/cap-core/v1/operational-constraints.schema.json`, examples under `examples/cap-core/v1/`, and any tests that validate `OperationalConstraints`.

Required work: decide whether `requires_human_confirmation` belongs in Core `OperationalConstraints` or under profile constraints; apply the decision consistently to docs, schemas, examples, and tests; preserve backward-compatibility notes for v0.1 `ConstraintSet`; avoid profile-specific CAP-Med fields in Core.

Acceptance: docs state one clear placement rule; schema and examples match that rule; tests reject the outdated placement when appropriate; release claims remain conservative.

Verification: run schema and docs-related tests, then run the default test command if the change touches runtime validation.

Final response: summarize the placement decision and list changed files.

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-02_privacyboundary_dimension_count_alignment.md`

## Task Prompt: DOC-FIX-02 PrivacyBoundary Dimension Count Alignment

### Implementation Status

Completed as documentation, schema-description, claim-language, and validation-test alignment work.

Placement decision:

- CAP v1 `PrivacyBoundary` uses nine first-class privacy dimensions.
- The dimensions are classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw-data egress, and minimization.
- `boundary_id` is an identifier and `policy_refs` is supporting metadata; neither is counted as a privacy dimension.
- Recipients, raw-data egress, and minimization are required first-class dimensions, not optional refinements.

Updated files:

- `docs/CAP_03_primitives.md`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_examples.md`
- `docs/CAP_appendix_schemas.md`
- `docs/CAP_CLAIMS.md`
- `docs/CAP_v1_TASKS.md`
- `schemas/domains/privacy.yaml`
- `schemas/cap-core/v1/privacy-boundary.schema.json`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_schemas.py tests/test_cap_v1_linkml.py
python scripts/check_v1_schema_drift.py
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: targeted v1 schema tests passed, no CAP v1 LinkML/JSON Schema drift was detected, and the full test suite passed.

Schema compatibility impact: no field was removed or renamed. The JSON Schema still requires the same `PrivacyBoundary` fields and still requires explicit `raw_data_egress.raw_transcript` and `raw_data_egress.raw_audio` booleans.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-02`.

Objective: align the v1 `PrivacyBoundary` dimensional model across docs and schema.

Inspect: `docs/CAP_03_primitives.md`, `docs/CAP_04_security_trust_evidence.md`, `docs/CAP_examples.md`, `docs/CAP_appendix_schemas.md`, `schemas/domains/privacy.yaml`, `schemas/cap-core/v1/privacy-boundary.schema.json`, and privacy-boundary examples.

Required work: choose the normative wording: either six core dimensions with recipients, raw-data egress, and minimization as refinements, or nine first-class dimensions. Update all docs, examples, schema descriptions, and claim language to use one model consistently. Do not weaken the existing recipient, raw-egress, or minimization controls.

Acceptance: no doc says six while another says nine without explaining the relationship; examples validate; CAP-Med raw transcript/audio egress constraints remain explicit.

Verification: run v1 schema tests and any privacy-boundary tests.

Final response: state the chosen dimensional model and any schema compatibility impact.

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-03_streaming_buffer_default_and_diagram_alignment.md`

## Task Prompt: DOC-FIX-03 Streaming Buffer Default And Diagram Alignment

### Implementation Status

Completed as documentation, architecture-diagram, scaffold-comment, and streaming-test alignment work.

Default decision:

- The CAP v1 target sliding lookahead buffer default is the smaller of 250 ms of speech-equivalent text or 50 tokens unless a profile overrides it.
- The buffer sits inside the Local PEP on the path from local agent/model output to user-visible delivery.
- Updated by P3-T1: the current Python scaffold implements reference live wall-clock streaming and pull-side backpressure around the 250 ms and 50-token defaults. UI routing remains follow-up work.

Updated files:

- `docs/CAP_03_primitives.md`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/architecture.md`
- `docs/CAP_examples.md`
- `docs/CAP_06_conformance.md`
- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_pep.py -k "stream or lookahead"
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: streaming-focused tests passed and the full test suite passed. No dedicated markdown/link-check command was found in the local project configuration; targeted text scans were used to check default wording.

Updated production gap: P3-T1 integrates reference live local/optional Ollama streaming, wall-clock timers, backpressure, and abort propagation. UI/client routing and production provider rollout remain separate runtime tasks.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-03`.

Objective: make the sliding lookahead buffer default and architecture diagrams consistent.

Inspect: `docs/CAP_03_primitives.md`, `docs/CAP_04_security_trust_evidence.md`, `docs/architecture.md`, `docs/CAP_examples.md`, `src/cap_protocol/runtime/streaming.py` or equivalent streaming scaffold, and streaming tests.

Required work: document the default as the smaller of 250 ms speech-equivalent text or 50 tokens unless a profile overrides it; update architecture diagram captions or surrounding text to show where the buffer sits; ensure scaffold names and config comments match the normative wording.

Acceptance: all docs use one default; diagrams identify Local PEP streaming interception; tests or comments make clear that deterministic scaffolds do not implement live wall-clock streaming yet.

Verification: run streaming-related tests and markdown/link checks if available.

Final response: summarize docs and code comments updated.

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-04_capability_shape_inline_documentation.md`

## Task Prompt: DOC-FIX-04 Capability Shape Inline Documentation

### Implementation Status

Completed as documentation-only capability shape alignment work.

Inline shape decision:

- CAP v1 uses one `Capability` shape for agents, tools, services, humans, and policy subjects.
- Required fields are `capability_id`, `kind`, `subject_id`, and non-empty `operations`.
- Optional fields are `endpoint`, `risk_level`, `policy_refs`, and `profile_extensions`.
- A2A AgentCard pointers and MCP server/tool/input-schema metadata live under `profile_extensions`; no top-level A2A or MCP fields are promoted into CAP Core.
- Capability Registry semantics remain aligned: registries resolve by `capability_id`, check freshness/version/digest metadata, and authorize requested operations against `operations`.

Updated files:

- `docs/CAP_02_core_model.md`
- `docs/CAP_03_primitives.md`
- `docs/CAP_05_integrations.md`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_schemas.py -k capability tests/test_cap_v1_linkml.py -k capability tests/test_federated_registry.py
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: targeted capability/schema/registry tests passed and the full test suite passed.

Repository note: the prompt referenced `schemas/domains/registry.yaml`, but this repository currently has `schemas/domains/capability.yaml` plus deterministic registry runtime stubs. No registry domain schema file exists.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-04`.

Objective: document the required `Capability` fields inline so readers do not need to open JSON Schema artifacts.

Inspect: `docs/CAP_02_core_model.md`, `docs/CAP_03_primitives.md`, `docs/CAP_05_integrations.md`, `schemas/domains/registry.yaml`, `schemas/cap-core/v1/capability.schema.json`, and capability examples.

Required work: add a concise normative `Capability` field list covering `kind`, `subject_id`, `operations`, `endpoint`, `risk_level`, `policy_refs`, and `profile_extensions`; state that A2A AgentCard and MCP server metadata live in `profile_extensions`; keep registry semantics aligned.

Acceptance: docs expose the shape inline; schema and examples already match or are updated to match; no new profile-specific fields are made Core.

Verification: run v1 schema tests if examples or schemas change.

Final response: identify where the inline shape now appears.

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-05_legacy_interrupt_vocabulary_rewrite.md`

## Task Prompt: DOC-FIX-05 Legacy Interrupt Vocabulary Rewrite

### Implementation Status

Completed as documentation and example vocabulary alignment work.

Legacy interrupt vocabulary resolved:

- "downgrade language" and "downgraded language" are profile shorthand for a Core `transform`.
- "revise output", "revised output", and "revise question" are profile shorthand for a profile `Directive` plus `transform` or `constrain`.
- "local fallback" and offline fallback are deployment-mode shorthand for cached-policy `allow`, `deny`, or `constrain`.
- "deferred analysis" is scheduling or routing behavior represented by `pause`, `escalate`, or `reroute`.
- Streaming correction frames are linked outcomes of `transform` interruptions and execution reports, not `InterruptDecision.action` values.

Updated files:

- `docs/CAP_03_primitives.md`
- `docs/CAP_05_integrations.md`
- `docs/CAP_examples.md`
- `docs/CAP_06_conformance.md`
- `examples/cap-core/v1/interrupt-decision.json`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
rg -n "revise output|revised output|revise question|downgrade language|downgraded language|local fallback|deferred analysis|safe replacement|Safe replacement|safe-replacement|\"decision\"\\s*:\\s*\"refuse\"" docs/CAP_03_primitives.md docs/CAP_05_integrations.md docs/CAP_examples.md docs/CAP_06_conformance.md examples/cap-core/v1/interrupt-decision.json schemas/cap-core/v1/interrupt-decision.schema.json tests/test_cap_v1_schemas.py tests/test_cap_v1_linkml.py
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_schemas.py -k interrupt tests/test_cap_v1_linkml.py -k interrupt tests/test_conformance.py
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: the docs grep returns only explanatory shorthand notes, targeted interrupt/conformance tests passed, and the full test suite passed with `109 passed`.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-05`.

Objective: remove or clarify legacy v0.2 interrupt vocabulary that sounds like extra Core actions.

Inspect: `docs/CAP_03_primitives.md`, `docs/CAP_05_integrations.md`, `docs/CAP_examples.md`, `docs/CAP_06_conformance.md`, and `schemas/cap-core/v1/interrupt-decision.schema.json`.

Required work: find phrases such as "revise output", "downgrade language", or similar profile behaviors; rewrite them as compositions of `allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, and `reroute`; add a short note where narrative names remain profile shorthand.

Acceptance: docs preserve exactly seven Core primitives; profile-specific labels are explicitly compositions, not enum extensions.

Verification: run docs grep for legacy phrases and run interrupt schema/conformance tests if touched.

Final response: list the legacy terms resolved.

## Source: `docs/task_prompts/cap_v1/Done/DOC-FIX-06_normative_streaming_terminology.md`

## Task Prompt: DOC-FIX-06 Normative Streaming Terminology

### Implementation Status

Completed as documentation and scaffold-comment terminology alignment work.

Terminology defined once in `docs/CAP_03_primitives.md`:

- `lookahead buffer`: Local PEP-held stream content not yet delivered to a user surface.
- `sliding lookahead buffer`: a lookahead buffer that releases safe prefixes while retaining a bounded suffix for continued evaluation.
- `configurable lookahead`: a profile/deployment-selected token, character, or time window; the CAP v1 target default remains the smaller of 250 ms of speech-equivalent text or 50 tokens unless a profile overrides it.
- `buffered transform`: a `transform` `InterruptDecision` applied before user-visible delivery while unsafe candidate content is still buffered.
- `abort`: stopping further delivery or execution after a blocking decision while preserving audit/report linkage for any started work.
- `correction frame`: a safe linked user-visible correction after partial emission, not an `InterruptDecision.action`.

Updated files:

- `docs/CAP_03_primitives.md`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_examples.md`
- `docs/architecture.md`
- `src/cap_protocol/runtime/local_pep.py`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`
- `docs/task_prompts/cap_v1/Open/README.md`

Verification:

```bash
rg -n "smaller of 250|lookahead boundary|streaming lookahead|lookahead buffer|configurable lookahead|buffered transform|correction frame|correction-frame|abort|live model-stream|wall-clock" docs/CAP_03_primitives.md docs/CAP_04_security_trust_evidence.md docs/CAP_examples.md docs/architecture.md src/cap_protocol/runtime/local_pep.py tests/test_cap_v1_pep.py
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_cap_v1_pep.py -k "streaming or lookahead or correction"
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Results: terminology grep showed the canonical definition plus references to it, targeted streaming/lookahead/correction tests passed, and the full test suite passed with `109 passed`.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `DOC-FIX-06`.

Objective: define streaming and chunking terminology once and reuse it consistently.

Inspect: `docs/CAP_03_primitives.md`, `docs/CAP_04_security_trust_evidence.md`, `docs/CAP_examples.md`, `docs/architecture.md`, and streaming scaffold/test names.

Required work: add a normative paragraph defining lookahead buffer, sliding lookahead buffer, configurable lookahead, buffered transform, abort, and correction frame; update nearby text to refer back to that definition; avoid changing runtime behavior unless names or comments are misleading.

Acceptance: readers can distinguish pre-display transform from late correction; docs explain deterministic scaffold versus live stream integration.

Verification: docs-only unless code comments changed.

Final response: summarize the terminology definition and locations updated.

### Phase 1 Prompts: v1 Hot-Path Foundation

## Source: `docs/task_prompts/cap_v1/Done/P0-DOC-01_reframe_public_docs.md`

## Task Prompt: P0-DOC-01 Reframe Public Docs

You are an implementation agent working in `/Users/ali/Documents/cap_protocol` as a senior protocol maintainer. Complete task `P0-DOC-01` from `docs/CAP_v1_TASKS.md`.

### Source Priority

1. `/Users/ali/Downloads/cap_v1_final.md`
2. `/Users/ali/Downloads/CAP_Architecture_Critical_Review.md`
3. Other supplied files only as fallback context.

### Current Repo Status

The repository contains a v0.1 production-candidate implementation plus CAP v1 architecture documentation and scaffolding. Do not claim full v1 runtime implementation.

### Objective

Reframe high-level docs from only "Control Authority Profile" to CAP v1 "Control Authority Protocol" and "supervisory control plane", while preserving the current v0.1 implementation status.

### Files To Inspect

- `README.md`
- `docs/CAP_00_README.md`
- `docs/architecture.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_CLAIMS.md`
- `docs/CAP_RELEASE_GATES.md`

### Required Work

1. Search for stale or ambiguous wording around "Control Authority Profile".
2. Keep "Control Authority Profile" only where it describes the v0.1 subset or historical wording.
3. Make the public claim consistent: "CAP v1 architecture is documented and partially scaffolded; the current implementation is a v0.1 production-candidate subset with a v1 migration backlog."
4. Ensure high-level docs describe CAP as a runtime governance protocol and semantic enforcement layer above existing transports and frameworks.
5. Ensure docs do not claim CAP is a transport, policy language, identity system, audit database, workflow engine, or clinical correctness guarantee.

### Acceptance Criteria

- `README.md`, `docs/CAP_00_README.md`, and `docs/architecture.md` distinguish v1 target architecture from v0.1 implementation evidence.
- The phrase "implementation-ready architecture baseline" is not interpreted as "fully implemented runtime."
- All docs consistently call the v1 system "Control Authority Protocol" and "supervisory control plane."

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize files changed, wording decisions, tests run, and any remaining documentation gaps.

## Source: `docs/task_prompts/cap_v1/Done/P0-DOC-02_two_tier_three_plane_architecture.md`

## Task Prompt: P0-DOC-02 Two-Tier Three-Plane Architecture

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P0-DOC-02`.

### Objective

Document CAP v1 as a hybrid two-tier, three-plane supervisory control-plane architecture.

### Source Priority

Use `/Users/ali/Downloads/cap_v1_final.md` first, then `/Users/ali/Downloads/CAP_Architecture_Critical_Review.md`, then fallback files only if needed.

### Required Architecture Terms

- Local tier: Local PEPs near agents, tools, and user surfaces.
- Federated tier: decomposed central Control Plane and registries.
- Data plane: A2A, MCP, HTTP, gRPC, WebSocket, local IPC traffic.
- Control plane: `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`.
- Observability plane: signed audit records, OpenTelemetry telemetry, W3C PROV graphs.
- Control Plane components: Controller, Supervisor Gateway, Session Router, logical Interrupt Manager, PDP adapters, Human Review integration.
- Registries: Agent, Tool, Capability, Policy, Evidence.

### Files To Inspect

- `docs/architecture.md`
- `docs/CAP_01_foundations.md`
- `docs/CAP_02_core_model.md`
- `docs/CAP_03_primitives.md`
- `docs/CAP_05_integrations.md`
- `README.md`

### Required Work

1. Add or refine architecture prose so the two tiers and three planes are explicit.
2. State that v0.1 Center/Edge demos are simplified demonstrations, not the full decomposed v1 Control Plane.
3. Keep observability independent from hot-path control logic.
4. Ensure CAP is described as transport-independent and framework-independent.
5. Link unresolved runtime work to `docs/CAP_v1_TASKS.md`.

### Acceptance Criteria

- Docs name Local PEP, Edge PEP, decomposed Control Plane, PDP, federated registries, and independent observability plane.
- No doc claims Local PEP, streaming lookahead, offline policy bundle, or federated registries are fully implemented unless code and tests prove it.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

List changed docs, the architecture claims clarified, and any open implementation gaps left in the backlog.

## Source: `docs/task_prompts/cap_v1/Done/P0-DOC-03_therapist_supervisor_scenario.md`

## Task Prompt: P0-DOC-03 Therapist/Supervisor Scenario

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P0-DOC-03`.

### Objective

Document the Therapist/Supervisor scenario as an example profile/scenario, not CAP Core.

### Required Semantics

- Therapist is a local interviewer persona.
- Therapist must remain non-diagnostic and non-prescriptive.
- Supervisor is not a single CAP component.
- Separate the Supervisor authority role, Supervisor Gateway endpoint, and model/human/rule engine behind the gateway.
- Supervisor cannot bypass Local PEP privacy, non-diagnostic, jurisdiction, or safety vetoes.

### Files To Inspect

- `README.md`
- `docs/CAP_00_README.md`
- `docs/CAP_02_core_model.md`
- `docs/CAP_07_profiles_roadmap.md`
- `docs/CAP_v1_TASKS.md`
- `schemas/domains/profiles.yaml`
- `tests/test_cap_v1_linkml.py`

### Required Work

1. Search for "Therapist", "interviewer", "Supervisor", "Center", and "CAP-Med".
2. Normalize scenario wording across docs.
3. Ensure profile-specific non-diagnostic language is not placed in CAP Core.
4. If schema/docs drift exists, update the LinkML profile schema or tests carefully.
5. Add examples only if they are redacted and do not include hidden chain-of-thought.

### Acceptance Criteria

- Docs state Therapist is a non-diagnostic local interviewer persona.
- Docs state Supervisor is a central/main authority participant behind a gateway.
- Docs state Local PEP can veto unsafe Supervisor directives.
- CAP Core docs do not define medical or psychometric semantics as universal Core behavior.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize exact scenario changes, tests run, and any profile/runtime gaps.

## Source: `docs/task_prompts/cap_v1/Done/P0-DOC-04_current_vs_target_alignment.md`

## Task Prompt: P0-DOC-04 Current vs Target Alignment

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P0-DOC-04`.

### Objective

Update `docs/CAP_IMPLEMENTATION_ALIGNMENT.md` so it clearly separates implemented v0.1 behavior, documented v1 target behavior, partially implemented v1 behavior, and missing v1 behavior.

### Files To Inspect

- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_v1_TASKS.md`
- `README.md`
- `docs/architecture.md`
- `src/cap_protocol/runtime/`
- `schemas/cap.yaml`
- `schemas/cap-core/v1/`
- `tests/`

### Required Work

1. Audit current implementation evidence in code and tests.
2. Place every claim into one of four buckets: implemented v0.1, documented v1 target, partially implemented v1, missing v1.
3. Mention v1 LinkML authoring schemas and JSON Schema artifacts without calling the runtime migrated.
4. Preserve exact public claim: CAP v1 architecture is documented and partially scaffolded; current implementation is v0.1 production-candidate subset.

### Acceptance Criteria

- `CAP_IMPLEMENTATION_ALIGNMENT.md` lists v0.1 evidence and v1 gaps without overclaiming.
- The docs do not confuse schema scaffolding with full runtime conformance.
- Therapist/Supervisor is identified as a profile/scenario.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Report what moved between status buckets and any uncertain claims left for review.

## Source: `docs/task_prompts/cap_v1/Done/P0-DOC-05_localhost_proxy_testing_caveat.md`

## Task Prompt: P0-DOC-05 Localhost Proxy Testing Caveat

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P0-DOC-05`.

### Objective

Ensure the repo consistently documents that tests should be run with localhost proxy bypass in this environment.

### Files To Inspect

- `README.md`
- `docs/testing.md`
- `docs/development.md`
- `docs/CAP_v1_TASKS.md`
- any CI or test guidance files if present

### Required Work

1. Confirm the documented command uses:

   ```bash
   source venv/bin/activate
   NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
   ```

2. Explain that plain `pytest` can fail in proxy-configured environments because localhost HTTP traffic may be routed through system proxy software such as Privoxy.
3. Keep the caveat local/environmental, not a CAP protocol requirement.
4. Update baseline test count if the current suite count has changed.

### Acceptance Criteria

- Backlog or alignment docs mention the localhost proxy caveat.
- The standard test command is consistent across docs.
- Current observed baseline is accurate after running the suite.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

State the observed test count and the files where the command was updated.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-01_replay_idempotency.md`

## Task Prompt: P1-CONF-01 Replay And Idempotency

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-01`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_replay_idempotency.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Remaining production gap: replay protection is process-local and in-memory. Durable per-session replay caches or nonce stores shared across executor replicas remain future runtime work.

### Objective

Add adversarial tests proving replayed directives cannot trigger duplicate execution.

### Files To Inspect

- `src/cap_protocol/conformance/runner.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_conformance.py`
- existing tests under `tests/`
- v1 Directive and CAPEnvelope schemas/examples

### Required Work

1. Identify current idempotency handling in v0.1 and v1 scaffolding.
2. Add a deterministic replay fixture or pytest case.
3. Ensure duplicate directive delivery returns the previous terminal result or a typed refusal, not a second side effect.
4. If runtime state is needed, keep it small and test-local.
5. Document remaining limitations if replay protection is only scaffolded.

### Acceptance Criteria

- A replayed directive with the same directive id or idempotency key cannot execute twice.
- Expected refusal or replay result is explicit.
- Existing v0.1 tests still pass.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize tests added, runtime behavior touched, and remaining replay gaps.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-02_clock_skew_expiry.md`

## Task Prompt: P1-CONF-02 Clock Skew And Expiry

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-02`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Remaining production gap: profile-specific timestamp policy, external cross-implementation JCS fixtures, and deployment clock-synchronization requirements remain broader security/runtime work.

### Objective

Add tests proving signed objects outside profile clock-skew and expiry tolerance are refused.

### Files To Inspect

- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/security/cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_conformance.py`
- `docs/CAP_04_security_trust_evidence.md`

### Required Work

1. Identify existing TTL and expiry checks.
2. Add deterministic tests for expired `CAPEnvelope`, expired `Directive`, and excessive future timestamp if supported.
3. Return or assert typed refusal such as `expired` or `clock_skew_exceeded`.
4. Keep system clock use injectable or deterministic in tests.

### Acceptance Criteria

- Objects outside profile skew tolerance are refused.
- Expired envelopes/directives are refused before payload use.
- Docs describe clock-skew behavior if runtime semantics are added.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize skew/expiry tests and any remaining timestamp policy decisions.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-03_stale_policy_hot_update.md`

## Task Prompt: P1-CONF-03 Stale Policy And Hot Update

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-03`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_policy_hot_update.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Remaining production gap: full Policy Registry distribution, session pinning policy, emergency override behavior, and registry freshness remain future runtime work.

### Objective

Add tests for stale policy and hot policy update behavior.

### Files To Inspect

- `policies/*.json`
- `src/cap_protocol/hardening/policy_engine.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `tests/test_hardening.py`
- `tests/test_cap_v1_pep.py`
- `schemas/cap-core/v1/policy-ref.schema.json`
- `schemas/domains/authority.yaml`

### Required Work

1. Define a minimal policy version/digest mismatch fixture.
2. Test that stale policy produces `stale_policy`, `require_policy_update`, or a safe refusal.
3. If session pinning is implemented, test that policy version changes are pinned per session.
4. Keep policy registry behavior as future work unless this task explicitly implements it.

### Acceptance Criteria

- Stale or mismatched policy metadata cannot silently authorize execution.
- Tests distinguish stale policy from stale evidence.
- Backlog remains explicit about full Policy Registry work.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize policy fixtures/tests and any deferred registry work.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-04_evidence_tamper.md`

## Task Prompt: P1-CONF-04 Evidence Tamper

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-04`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_evidence_tamper.py`
- `src/cap_protocol/bindings/grpc_reference/cap_core.py`
- `src/cap_protocol/bindings/http_json/validators.py`

Remaining production gap: evidence tamper checks re-hash optional local backing content only. Registry-backed dereference, snapshot attestation, and access-policy enforcement remain future runtime work.

### Objective

Add evidence tamper tests proving changed backing content produces `evidence_hash_mismatch`.

### Files To Inspect

- `schemas/domains/evidence.yaml`
- `schemas/cap-core/v1/evidence-ref.schema.json`
- `examples/cap-core/v1/evidence-ref.json`
- `src/cap_protocol/conformance/runner.py`
- `src/cap_protocol/hardening/`
- `tests/test_conformance.py`
- `tests/test_hardening.py`

### Required Work

1. Locate existing evidence hash/freshness/access tests.
2. Add or strengthen a deterministic hash-mismatch test.
3. Ensure evidence content cannot alter allowed tools, forbidden tools, budgets, authority, or data scope.
4. Do not log raw sensitive evidence or hidden chain-of-thought.

### Acceptance Criteria

- Hash mismatch produces `evidence_hash_mismatch`.
- Prompt injection inside evidence cannot change constraints.
- Test data is minimized and redacted.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize evidence tamper tests and any evidence-store limitations.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-05_offline_fallback.md`

## Task Prompt: P1-CONF-05 Offline Fallback Tests

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-05`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Updated by `P2-RUNTIME-04`: cached policy bundles now validate expiry, digest shape, signature metadata, and optional detached-JWS signed payloads through existing crypto helpers.

Updated by `P2-T2`: `ReferencePolicyRegistryService` now models service-backed signed-bundle distribution, per-session pinning, explicit hot update, online revoked-bundle refusal, and audited emergency override. Production network deployment, service authentication, HA replication, monitoring, organization rollout controls, and KMS/HSM signing custody remain open.

### Objective

Add or strengthen tests for Local PEP offline fallback with cached signed policy bundles.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_06_conformance.md`
- `docs/CAP_v1_TASKS.md`

### Required Work

1. Test central Control Plane unreachable plus valid cached policy bundle.
2. Test central unreachable plus expired or missing policy bundle.
3. Confirm sensitive turns fail closed when policy material is invalid.
4. For Therapist persona, allow only profile-safe supportive behavior in offline mode.
5. Record signature limitations explicitly; `P2-RUNTIME-04` updates this scaffold with optional detached-JWS signed-payload verification.

### Acceptance Criteria

- Valid cached policy permits only safe offline behavior.
- Expired or missing policy fails closed for sensitive output.
- Tests avoid clinical or treatment claims.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize offline cases and remaining signed-bundle work.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-06_sidecar_bypass.md`

## Task Prompt: P1-CONF-06 Sidecar Bypass

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-06`.

### Implementation Status

Completed as deterministic scaffold coverage. Status update after P1-T4: the gRPC and HTTP/JSON binding smoke reports also assert direct user-output and direct local-tool bypass refusals while routing selected mediated paths through Local PEP.

Executable evidence:

- `tests/test_cap_v1_pep.py`
- `tests/test_grpc_reference_v1_binding.py`
- `tests/test_http_binding.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Remaining production gap: bypass checks are deterministic Local PEP scaffold checks. Production bypass resistance still requires separately privileged proxies or attested isolation with OS/platform routing, network controls, and mediated local-tool access.

### Objective

Add sidecar-bypass tests for high-assurance profiles so agents cannot reach user, network, or tools outside Local PEP.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_threat_model.md`
- `docs/CAP_06_conformance.md`

### Required Work

1. Identify existing high-assurance bypass scaffold.
2. Add tests for direct user-visible output bypass, direct raw-data egress, and direct tool/network path if supported.
3. Assert typed refusal such as `sidecar_bypass_attempt` or equivalent.
4. Do not implement broad sandboxing beyond a minimal deterministic test scaffold unless explicitly needed.

### Acceptance Criteria

- Agent cannot bypass Local PEP in high-assurance test mode.
- Refusal is typed and auditable.
- Docs clarify that production sandboxing remains deployment-specific if not fully implemented.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize bypass paths covered and residual production risks.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-07_streaming_correction.md`

## Task Prompt: P1-CONF-07 Streaming Correction Tests

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-07`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Updated by P3-T1/P3-T3/P3-T4: deterministic configurable lookahead exists under `P2-RUNTIME-03`, and reference live local/optional Ollama streaming now covers wall-clock release, backpressure, abort propagation, CLI/WebSocket-style abort replacement contracts, and CLI/WebSocket-style correction-frame replacement/annotation contracts. Shipping native UI wrappers and production provider rollout remain future runtime work.

### Objective

Add tests for buffered unsafe streaming content and late correction frames.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `schemas/cap-core/v1/interrupt-decision.schema.json`
- `schemas/cap-core/v1/execution-report.schema.json`
- `docs/CAP_06_conformance.md`

### Required Work

1. Test diagnostic wording detected before emission is transformed or denied.
2. Test late detection after partial emission emits a correction frame.
3. Ensure `ExecutionReport` or equivalent test record links original stream id, partial emission, `InterruptDecision`, correction frame, and audit/provenance refs if scaffolded.
4. Ensure unsafe diagnostic/treatment content does not reach the user in buffered cases.

### Acceptance Criteria

- Buffered diagnostic wording is blocked or transformed before display.
- Late detection creates a correction frame.
- Supervisor directives cannot force unsafe stream output.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize streaming cases and whether live token/time buffering remains open.

## Source: `docs/task_prompts/cap_v1/Done/P1-CONF-08_supervisor_overreach.md`

## Task Prompt: P1-CONF-08 Supervisor Overreach

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-CONF-08`.

### Implementation Status

Completed as deterministic scaffold coverage.

Executable evidence:

- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`

Updated by `P2-RUNTIME-05`: a deterministic Supervisor Gateway stub now privacy-filters, authority-checks, and mediates structured supervisor output before Local PEP veto. A deployed gateway service with backend integration remains future runtime work.

### Objective

Add tests proving Supervisor requests for raw transcripts, raw audio, diagnosis, or treatment advice are vetoed by Local PEP policy.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `schemas/domains/profiles.yaml`
- `schemas/domains/privacy.yaml`
- `docs/CAP_07_profiles_roadmap.md`
- `docs/CAP_threat_model.md`

### Required Work

1. Add Supervisor directive/request fixtures for raw transcript egress, raw audio egress, diagnosis, and treatment advice.
2. Assert Local PEP typed refusal.
3. Assert redacted context or EvidenceRefs remain allowed where appropriate.
4. Keep scenario as profile-specific and non-diagnostic.

### Acceptance Criteria

- Local PEP vetoes unsafe Supervisor directives.
- Refusals are typed and do not leak raw data.
- Tests preserve the three Supervisor meanings: authority role, gateway endpoint, and backend engine.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize overreach cases and any remaining deployed Supervisor Gateway work.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-01_cap_envelope.md`

## Task Prompt: P1-SCHEMA-01 CAPEnvelope

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-01`.

### Implementation Status

Completed as v1 schema, example, test, and runtime-scaffold coverage.

Executable evidence:

- `schemas/domains/control.yaml`
- `schemas/cap-core/v1/cap-envelope.schema.json`
- `examples/cap-core/v1/cap-envelope.json`
- `src/cap_protocol/runtime/edge_pep.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_pep.py`

Status update after P1-T10: the gRPC reference demo and independent HTTP/JSON demo now use v1 `CAPEnvelope` objects on their active hot paths, helper-generated v1 signatures use RFC 8785/JCS, demo cross-boundary CAP envelopes pass Edge PEP verification before payload use, and V1-C01 through V1-C15 have release-blocking deterministic scaffold conformance coverage. Remaining production gaps include production PEP deployment, registry-backed dereference, external cross-implementation JCS fixtures, and key infrastructure.

### Objective

Define and validate the CAP v1 `CAPEnvelope` object across LinkML, JSON Schema, examples, docs, and tests.

### Required Fields

`envelope_id`, `session_id`, `trace_id`, `sender_id`, `receiver_id`, `message_kind`, `payload` or `payload_ref`, `authority_chain_ref`, `policy_refs`, `privacy_boundary_ref`, `timestamp`, `ttl_ms`, and `signature`.

### Verification Semantics To Document

- Sender signature must be verified before cross-trust-boundary processing.
- Privacy boundary must be checked before payload dereference or user-visible delivery.
- Canonicalization rules are documented in `CAP_04_security_trust_evidence.md` and trace to completed `P1-SEC-01`.

### Files To Inspect

- `schemas/domains/control.yaml`
- `schemas/cap-core/v1/cap-envelope.schema.json`
- `examples/cap-core/v1/cap-envelope.json`
- `src/cap_protocol/runtime/edge_pep.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_02_core_model.md`

### Required Work

1. Confirm LinkML and JSON Schema agree on field names and required fields.
2. Confirm example payload validates under JSON Schema.
3. Add or update tests for missing signature, missing privacy boundary, and either `payload` or `payload_ref`.
4. Ensure runtime checks in Edge PEP are compatible with the schema.
5. Do not migrate v0.1 demos unless the task explicitly expands to runtime migration.

### Acceptance Criteria

- Schema includes every required field.
- Examples validate.
- Tests reject missing required fields and invalid message kind.
- Docs state CAPEnvelope is v1 target scaffolding unless the runtime is fully migrated.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize schema/test/doc changes and note whether runtime migration remains open.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-02_interrupt_decision.md`

## Task Prompt: P1-SCHEMA-02 InterruptDecision

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-02`.

### Implementation Status

Completed as v1 schema, example, reduced-enum, documentation, Local PEP scaffold coverage, and P1-T6 deterministic runtime composition coverage.

Executable evidence:

- `schemas/core.yaml`
- `schemas/domains/control.yaml`
- `schemas/cap-core/v1/interrupt-decision.schema.json`
- `examples/cap-core/v1/interrupt-decision.json`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/interrupts.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_interrupt_runtime.py`

Status update after P1-T6: the runtime helper builds all seven primitives, composes conflicts with `deny > pause/escalate > transform > constrain > allow`, maps CAP-Med profile shorthand to Core actions, and the gRPC/HTTP demos link applied interrupt refs from execution reports.

Remaining production gap: deterministic configurable streaming lookahead scaffolding exists under `P2-RUNTIME-03`, but a deployed logical Interrupt Manager plus live model-stream, UI, human-review, and cross-service conflict integration remain future runtime work.

### Objective

Define and validate the CAP v1 `InterruptDecision` object using the reduced Core primitive action set.

### Core Action Set

Only these actions are CAP Core primitives:

- `allow`
- `deny`
- `transform`
- `constrain`
- `pause`
- `escalate`
- `reroute`

Do not add `revise`, `replace`, `downgrade_language`, `local_fallback`, or `defer_async_analysis` as Core actions. Represent them as compositions, profile policy, deployment mode, or scheduling behavior.

### Files To Inspect

- `schemas/core.yaml`
- `schemas/domains/control.yaml`
- `schemas/cap-core/v1/interrupt-decision.schema.json`
- `examples/cap-core/v1/interrupt-decision.json`
- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_03_primitives.md`
- `docs/CAP_06_conformance.md`

### Required Work

1. Confirm LinkML enum and JSON Schema enum match exactly.
2. Add or update tests that reject older bloated taxonomy actions.
3. Document how profile-specific transforms map to the reduced primitives.
4. If runtime behavior is touched, keep it minimal and deterministic.

### Acceptance Criteria

- Schema and fixtures cover the seven reduced primitives.
- Older action names are absent from Core schemas and tests.
- Streaming and Therapist/Supervisor docs refer to transform/correction behavior without expanding Core actions.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

List enum/schema/test changes and any runtime gaps left for `P2-RUNTIME-03`.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-03_privacy_boundary.md`

## Task Prompt: P1-SCHEMA-03 PrivacyBoundary

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-03`.

### Implementation Status

Completed as structured v1 schema, example, structured privacy PDP scaffold, Local PEP, and Therapist/Supervisor privacy test coverage.

Executable evidence:

- `schemas/domains/privacy.yaml`
- `schemas/cap-core/v1/privacy-boundary.schema.json`
- `examples/cap-core/v1/privacy-boundary.json`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/privacy_pdp.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_privacy_pdp.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_threat_model.md`

Remaining production gap: the deterministic Supervisor Gateway stub and in-process privacy PDP helper now cover basic structured privacy filtering; a deployed gateway service, deployed local/central PDP service, Policy Registry distribution, and production privacy-filtering integration remain future runtime work.

### Objective

Define structured CAP v1 `PrivacyBoundary` semantics and tests. Do not model privacy as a flat enum.

### Required Dimensions

- classification
- movement
- transformation
- retention
- logging
- audit visibility
- allowed recipients
- raw-data egress rules
- redaction/minimization requirements

The Therapist/Supervisor fixtures must block raw transcript and raw audio egress by default.

### Files To Inspect

- `schemas/domains/privacy.yaml`
- `schemas/cap-core/v1/privacy-boundary.schema.json`
- `examples/cap-core/v1/privacy-boundary.json`
- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_threat_model.md`

### Required Work

1. Ensure LinkML and JSON Schema model structured dimensions.
2. Ensure `raw_transcript` and `raw_audio` are explicit booleans.
3. Add tests rejecting flat privacy enum usage if needed.
4. Add or update Therapist/Supervisor tests proving raw transcript/audio egress is blocked by default.
5. Keep raw sensitive content out of examples and logs.

### Acceptance Criteria

- Boundary supports all required dimensions.
- Therapist/Supervisor fixtures block raw transcript/audio egress.
- Local PEP can refuse Supervisor requests that violate the boundary.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize schema, fixture, and Local PEP coverage changes.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-04_operational_constraints.md`

## Task Prompt: P1-SCHEMA-04 OperationalConstraints

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-04`.

### Implementation Status

Completed as v1 `OperationalConstraints` schema, example, tests, and migration documentation.

Executable evidence:

- `schemas/domains/constraints.yaml`
- `schemas/cap-core/v1/operational-constraints.schema.json`
- `examples/cap-core/v1/operational-constraints.json`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `docs/CAP_02_core_model.md`
- `docs/CAP_03_primitives.md`
- `docs/CAP_07_profiles_roadmap.md`

Status update after P1-T2: the active gRPC and HTTP/JSON hot paths now use v1 `OperationalConstraints`; retained v0.1 helpers and fixtures still carry the legacy `ConstraintSet` shape for compatibility. Remaining production gaps include full profile end-to-end migration and production PEP/registry integration.

### Objective

Split legacy `ConstraintSet` semantics into CAP Core `OperationalConstraints` plus profile-specific constraints.

### Core Constraint Fields

Core may include allowed tools, forbidden tools, max wall time, max tool calls, budget, data access scope, reversibility, side-effect limits, network egress, and freshness limits.

Profile-specific constraints such as non-diagnostic style, psychometric scoring, medical thresholds, or escalation thresholds must live under profile extensions/profile constraints.

### Files To Inspect

- `schemas/domains/constraints.yaml`
- `schemas/cap-core/v1/operational-constraints.schema.json`
- `examples/cap-core/v1/operational-constraints.json`
- v0.1 schemas under `schemas/cap-core/v0.1/`
- `docs/CAP_02_core_model.md`
- `docs/CAP_07_profiles_roadmap.md`
- tests covering schema validation

### Required Work

1. Confirm Core constraints are generic and profile constraints are separated.
2. Preserve v0.1 compatibility notes for `ConstraintSet`.
3. Update examples to keep Therapist non-diagnostic requirements in profile extension fields.
4. Add tests rejecting invalid Core values, such as invalid reversibility or negative budgets.

### Acceptance Criteria

- Generic constraints remain Core.
- Profile-specific constraints do not become CAP Core fields.
- Examples validate.
- Docs explain the migration from `ConstraintSet` to `OperationalConstraints`.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize schema alignment, profile separation, and tests.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-05_capability.md`

## Task Prompt: P1-SCHEMA-05 Capability

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-05`.

### Implementation Status

Completed as unified v1 `Capability` schema, agent/tool examples, tests, and integration documentation.

Executable evidence:

- `schemas/domains/capability.yaml`
- `schemas/cap-core/v1/capability.schema.json`
- `examples/cap-core/v1/capability.json`
- `examples/cap-core/v1/capability-tool.json`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `docs/CAP_02_core_model.md`
- `docs/CAP_05_integrations.md`

Updated by `P2-RUNTIME-06`: deterministic federated registry stubs now cover capability cache/version/revocation behavior. Deployed capability registry services remain future runtime work.

### Objective

Unify agent and tool capability metadata into a CAP v1 `Capability` object with a `kind` discriminator.

### Required Semantics

- `kind` distinguishes agent, tool, service, human, and policy subjects.
- A2A and MCP endpoint metadata must be preserved through extension fields, not owned by CAP Core.
- Capability metadata must support policy references.

### Files To Inspect

- `schemas/domains/capability.yaml`
- `schemas/cap-core/v1/capability.schema.json`
- `examples/cap-core/v1/capability.json`
- `docs/CAP_02_core_model.md`
- `docs/CAP_05_integrations.md`
- tests for LinkML and JSON Schema validation

### Required Work

1. Confirm LinkML and JSON Schema capability fields align.
2. Add examples for at least one agent and one tool capability if missing.
3. Make sure A2A/MCP fields are extension metadata and do not imply CAP replaces A2A or MCP.
4. Add tests for valid and invalid `kind` values.

### Acceptance Criteria

- Agent and tool capability examples share one structure.
- `kind` discriminator is required.
- A2A/MCP-specific metadata is preserved without redefining those protocols.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize schema/test/doc updates and any deployed registry service work still deferred.

## Source: `docs/task_prompts/cap_v1/Done/P1-SCHEMA-06_linkml_json_schema_generation.md`

## Task Prompt: P1-SCHEMA-06 LinkML-to-JSON-Schema Generation

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SCHEMA-06`.

### Implementation Status

Completed as CI-friendly LinkML/JSON Schema drift checking rather than generated-artifact replacement.

Executable evidence:

- `src/cap_protocol/schema/linkml.py`
- `src/cap_protocol/cli/check_v1_schema_drift.py`
- `scripts/check_v1_schema_drift.py`
- `tests/test_cap_v1_linkml.py`
- `pyproject.toml`
- `docs/development.md`
- `docs/CAP_appendix_schemas.md`

Remaining production gap: deterministic generated JSON Schema replacement is deferred until generated output is reviewed and can replace the checked-in artifacts without changing the runtime validation path.

### Objective

Automate or scaffold LinkML-to-JSON-Schema generation and drift checking between the CAP v1 LinkML authoring schemas and JSON Schema artifacts.

### Current Status

LinkML authoring schemas exist under `schemas/cap.yaml`, `schemas/core.yaml`, and `schemas/domains/*.yaml`. JSON Schema artifacts exist under `schemas/cap-core/v1/`. Drift checking is automated by `python scripts/check_v1_schema_drift.py`, by `python -m cap_protocol.cli.check_v1_schema_drift`, and by `tests/test_cap_v1_linkml.py`; the `cap-check-v1-schema-drift` entry point is available after reinstalling the editable package.

### Files To Inspect

- `schemas/cap.yaml`
- `schemas/core.yaml`
- `schemas/domains/*.yaml`
- `schemas/cap-core/v1/*.schema.json`
- `src/cap_protocol/schema/linkml.py`
- `tests/test_cap_v1_linkml.py`
- `tests/test_cap_v1_schemas.py`
- `pyproject.toml`
- `requirements-dev.txt`

### Required Work

1. Prefer a lightweight script or test that uses LinkML tooling already in dev dependencies.
2. Do not add heavy dependencies unless necessary.
3. Either generate JSON Schema into a deterministic generated-artifact location or compare essential fields/enums between LinkML and existing JSON Schema.
4. Make CI failure messages clear when drift exists.
5. Do not replace the current JSON Schema validation path until generated artifacts are deterministic and reviewed.

### Acceptance Criteria

- A developer can run one command to detect LinkML/JSON Schema drift.
- CI can include the drift check.
- Existing JSON Schema example tests continue to pass.
- Docs state whether JSON Schemas are generated or manually aligned.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
python VERIFY_FINAL_PACKAGE.py
```

### Final Response

Report the generation/checking approach, commands added, and any remaining manual alignment limitations.

## Source: `docs/task_prompts/cap_v1/Done/P1-SEC-01_canonicalization_signing.md`

## Task Prompt: P1-SEC-01 Canonicalization And Signing

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SEC-01`.

### Implementation Status

Completed as documentation plus deterministic security coverage.

Executable evidence:

- `tests/test_cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_cap_v1_schemas.py`
- `src/cap_protocol/security/cap_crypto.py`
- `docs/CAP_04_security_trust_evidence.md`

Standards decision:

- CAP v1 production JSON signatures use RFC 8785/JCS canonicalization or an equivalent standards-based envelope/library profile.
- Existing v0.1 helper signatures remain compatible with the repository's deterministic sorted-key JSON encoder and label that mode as `json-deterministic-sort-keys-v0.1`.

Status update after P1-T3: helper-generated v1 detached-JWS and DSSE signatures now use RFC 8785/JCS and label `rfc8785-jcs`; v0.1 compatibility verification remains available under `json-deterministic-sort-keys-v0.1`.

Remaining production gap: the runtime still uses local Ed25519 helper keys. Production deployments still need KMS/HSM or workload-key integration, registry-backed key discovery/revocation, and external cross-implementation JCS fixtures.

### Objective

Specify and test canonicalization and signing rules for signed CAP Core objects without implementing custom cryptography.

### Required Signing Targets

- `AuthorityChainStep`
- `GuardDecision`
- high-stakes `Directive`
- evidence snapshots
- compensation/rollback attestations
- `CAPEnvelope` across trust boundaries

### Required Constraints

- Prefer established formats/libraries.
- RFC 8785 JSON canonicalization is acceptable for JSON encodings if no better project standard exists.
- DSSE, COSE, JOSE, in-toto-style attestations may be used.
- Do not log hidden chain-of-thought or raw sensitive evidence.

### Files To Inspect

- `src/cap_protocol/security/cap_crypto.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/hardening/`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_threat_model.md`
- `tests/test_hardening.py`
- `tests/test_cap_v1_pep.py`

### Required Work

1. Document canonicalization decision and signing envelope expectations.
2. Add or update tests for invalid signature and payload tamper.
3. Ensure high-risk signed objects identify the exact signed payload.
4. Keep existing v0.1 signatures compatible unless a migration note explains the difference.

### Acceptance Criteria

- Security docs explain signing targets and canonicalization.
- Tests cover invalid signature and tampered payload.
- No custom cryptographic primitive is introduced.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
python VERIFY_FINAL_PACKAGE.py
```

### Final Response

Summarize security behavior, tests added, and any standards decisions left open.

## Source: `docs/task_prompts/cap_v1/Done/P1-SEC-02_cap_warrant_authority_chain.md`

## Task Prompt: P1-SEC-02 CAP Warrant And Authority Chain

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-SEC-02`.

### Implementation Status

Completed as documentation, schema tightening, and deterministic runtime scaffold coverage.

Executable evidence:

- `src/cap_protocol/runtime/authority.py`
- `tests/test_authority_chain.py`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`
- `schemas/domains/authority.yaml`
- `schemas/cap-core/v1/authority-chain.schema.json`
- `docs/CAP_02_core_model.md`
- `docs/CAP_03_primitives.md`
- `docs/CAP_04_security_trust_evidence.md`

Updated by P2-T6: this repository now includes a Biscuit-backed `biscuit-v2` AuthorityChainStep warrant reference integration with registry-backed revocation freshness checks. Remaining production gaps are KMS/HSM-backed key management, deployed revocation operations, and external interoperability evidence for selected warrant profiles.

### Objective

Define CAP Warrant / authority-chain binding so authority is more than `sender_id`.

### Required Semantics

Authority requires identity, capability, scope, policy, time, expiry, revocation metadata, delegation constraints, and attestation. Authority chains should support attenuating, holder-bound, offline-verifiable capability tokens. Profiles may use Biscuit, Tenuo, Macaroons, or equivalent primitives.

### Files To Inspect

- `schemas/domains/authority.yaml`
- `schemas/cap-core/v1/authority-chain.schema.json`
- `examples/cap-core/v1/authority-chain.json`
- `docs/CAP_02_core_model.md`
- `docs/CAP_04_security_trust_evidence.md`
- `src/cap_protocol/runtime/edge_pep.py`
- v0.1 authority-chain-step schema and tests

### Required Work

1. Document the verification algorithm for PEPs and Executors.
2. Ensure schema fields cover expiry, scope, policy ref, identity binding, revocation ref, delegation constraints, and signature.
3. Add tests for missing authority, expired authority, unsupported capability, and invalid signature where practical.
4. Keep production Warrant implementation as a backlog item if only documented.

### Acceptance Criteria

- Authority-chain docs bind identity, capability, scope, expiry, revocation, and attenuation.
- Tests cover at least one invalid authority path.
- Docs allow profile-selected warrant primitives without mandating one in Core.

### Verification

Run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize schema/doc/test coverage and note what remains a production warrant backlog.

## Source: `docs/task_prompts/cap_v1/Done/P1-T10_make_v1_c01_through_v1_c15_release_blocking.md`

## Task Prompt: P1-T10 Make V1-C01 Through V1-C15 Release Blocking

### Implementation Status

Completed in this repository:

- `src/cap_protocol/conformance/v1_runner.py` now exposes `run_v1_conformance_release_gate`, which maps V1-C01 through V1-C15 to executable required deterministic scaffold cases.
- Every case carries owner, status, coverage level, evidence links, and an explicit full-runtime external-gate reason.
- `cap-check-v1-conformance`, `tests/test_conformance.py`, and `python VERIFY_FINAL_PACKAGE.py` fail when any required case fails.
- `docs/CAP_06_conformance.md`, `docs/CAP_RELEASE_GATES.md`, `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`, `docs/testing.md`, and `docs/CAP_v1_TASKS.md` distinguish release-blocking deterministic scaffold conformance from full CAP v1 runtime certification.

Remaining production gaps: deployed Local/Edge PEP trust modes, production registries, live stream integration, deployed Supervisor Gateway service integration, production observability operations, production warrant/key infrastructure, external interoperability, and full CAP v1 runtime certification remain future tasks.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T10`.

Objective: promote the v1 conformance backlog from smoke coverage to release-blocking status.

Inspect: `docs/CAP_06_conformance.md`, `src/cap_protocol/conformance/`, CI scripts, `pyproject.toml`, tests for v1 smoke coverage, and release gates.

Required work: define V1-C01 through V1-C15 as executable cases; mark deterministic scaffold cases versus full runtime cases; wire CI or a release command to fail on required cases; document skipped or external-gate cases with explicit reason and owner.

Acceptance: CI/release verification fails on any required v1 conformance failure; docs no longer imply smoke tests equal certification; every V1 case has owner, status, and evidence link.

Verification: run the v1 conformance command and the default test command.

Final response: summarize conformance status and any intentionally deferred cases.

### Phase 2 Prompts: Services, Registries, And Substrate Integration

## Source: `docs/task_prompts/cap_v1/Done/P1-T1_migrate_grpc_reference_binding_to_capenvelope.md`

## Task Prompt: P1-T1 Migrate gRPC Reference Binding To CAPEnvelope

Status: Complete for the gRPC reference binding hot path.

Implementation evidence:

- `src/cap_protocol/bindings/grpc_reference/cap_v1_core.py` builds signed v1 `CAPEnvelope` objects and signed v1 payload objects.
- `src/cap_protocol/bindings/grpc_reference/center_server.py` and `edge_client.py` now exchange v1 `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` envelopes over the existing gRPC JSON payload field.
- `src/cap_protocol/bindings/grpc_reference/schema_validation.py` validates gRPC trace messages against `schemas/cap-core/v1/cap-envelope.schema.json` plus the corresponding v1 payload schemas.
- `tests/test_grpc_reference_v1_binding.py` runs the deterministic gRPC demo and validates representative emitted envelopes against v1 schemas.
- v0.1 gRPC compatibility builders and conformance coverage remain available through `cap_core.py`, `conformance.py`, and `*_legacy.py` adapter modules.

Status update after P1-T10: the independent HTTP/JSON binding has also migrated to v1 `CAPEnvelope` objects, helper-generated v1 signatures use RFC 8785/JCS, both executable bindings route selected user-output/local-tool paths through the Local PEP scaffold, demo cross-boundary CAP envelopes pass Edge PEP verification before payload use, and V1-C01 through V1-C15 are release-blocking deterministic scaffold conformance cases. Remaining production gaps include production Edge PEP service-mesh deployment, registry-backed dereference, external cross-implementation JCS fixtures, production Local PEP trust modes, and production key management.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_grpc_reference_v1_binding.py tests/test_cap_v1_schemas.py tests/test_conformance.py
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Original Task

Objective: migrate the gRPC reference binding from the v0.1 message shape to v1 `CAPEnvelope` plus v1 payload objects.

Inspect: `reference_grpc/`, `src/cap_protocol/bindings/grpc_reference/`, protobuf definitions, gRPC runner tests, `schemas/cap-core/v1/cap-envelope.schema.json`, v1 examples, crypto helpers, and existing v0.1 compatibility tests.

Required work: emit and validate `CAPEnvelope`; use v1 `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` payloads; preserve v0.1 fixtures as compatibility or legacy tests; update docs and conformance fixtures to state which path is v1.

Acceptance: the gRPC demo validates against `cap-envelope.schema.json`; v0.1 envelope is no longer on the gRPC hot path; existing production-candidate evidence is preserved as v0.1 compatibility where needed.

## Source: `docs/task_prompts/cap_v1/Done/P1-T2_migrate_http_json_binding_to_capenvelope.md`

## Task Prompt: P1-T2 Migrate HTTP/JSON Binding To CAPEnvelope

Status: Complete for the independent HTTP/JSON binding hot path.

Implementation evidence:

- `src/cap_protocol/bindings/http_json/cap_v1_types.py` builds signed v1 `CAPEnvelope` objects and v1 payload objects for the HTTP path.
- `src/cap_protocol/bindings/http_json/http_runtime.py` now returns v1 `ExecutionReport` acknowledgment envelopes from `/edge/event` and `/center/response`.
- `src/cap_protocol/bindings/http_json/run_demo.py` now posts v1 `EvidenceRef` and `Directive` envelopes across HTTP and validates all boundary messages with v1 schemas.
- `src/cap_protocol/bindings/http_json/validators_v1.py`, `integrations_v1.py`, and `conformance_v1.py` provide HTTP-specific v1 schema validation, integrations, and C01-C28 smoke behavior.
- `tests/test_http_binding.py` validates representative HTTP emitted envelopes against `schemas/cap-core/v1/cap-envelope.schema.json` plus the matching payload schemas.
- Retained `cap_types.py`, `validators.py`, `integrations.py`, and `conformance.py` keep v0.1 HTTP compatibility coverage available.

Status update after P1-T5: helper-generated v1 signatures now use RFC 8785/JCS and label `rfc8785-jcs`, both executable bindings route selected user-output/local-tool paths through the Local PEP scaffold, and demo cross-boundary CAP envelopes pass Edge PEP verification before payload use.

Remaining production gaps: production Edge PEP service-mesh deployment, registry-backed dereference, external cross-implementation JCS fixtures, production Local PEP trust modes, and production key management remain separate tasks. V1-C01 through V1-C15 are now release-blocking deterministic scaffold conformance cases after P1-T10, but full production runtime certification remains separate.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost python -m cap_protocol.bindings.http_json.run_demo
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_http_binding.py tests/test_cap_v1_schemas.py tests/test_conformance.py tests/test_executor_validation.py tests/test_evidence_tamper.py
```

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T2`.

Objective: migrate the independent HTTP/JSON binding to v1 `CAPEnvelope` and v1 payload objects.

Inspect: `second_http/`, `src/cap_protocol/bindings/http_json/`, HTTP smoke tests, JSON Schema validation helpers, `schemas/cap-core/v1/`, and existing proxy caveat documentation.

Required work: make requests and responses use `CAPEnvelope`; validate all cross-boundary messages with v1 schema; keep payloads as v1 Core objects; update conformance fixtures; preserve legacy v0.1 compatibility tests if still needed.

Acceptance: HTTP/JSON demo validates against `cap-envelope.schema.json`; conformance suite remains green with `NO_PROXY` set; docs distinguish v1 HTTP path from any retained v0.1 examples.

Verification: run targeted HTTP tests with localhost proxy bypass, then the default test command.

Final response: summarize endpoint/message changes and test results.

## Source: `docs/task_prompts/cap_v1/Done/P1-T3_implement_rfc_8785_jcs_for_v1_signatures.md`

## Task Prompt: P1-T3 Implement RFC 8785 JCS For v1 Signatures

Status: Complete for helper-generated v1 signing surfaces.

Implementation evidence:

- `src/cap_protocol/security/cap_crypto.py` exposes `canonical_json_jcs`, `canonical_json_for`, `CAP_V1_JCS_CANONICALIZATION`, and `sign_v1` helpers for detached-JWS and DSSE signatures.
- v1 runtime, binding, and smoke-conformance signing surfaces now use `sign_v1` and metadata label `rfc8785-jcs`.
- v0.1 compatibility signing and verification remain available under `json-deterministic-sort-keys-v0.1`, including verification for legacy detached signatures without a `canon` protected-header field.
- `tests/test_cap_crypto.py` covers JCS ordering, Unicode, numeric rendering, v1 detached-JWS member reordering, DSSE canonicalization mismatch, and v0.1 compatibility.
- `tests/test_cap_v1_pep.py`, `tests/test_authority_chain.py`, `tests/test_cap_v1_schemas.py`, `tests/test_grpc_reference_v1_binding.py`, and `tests/test_http_binding.py` assert v1 signature metadata and JCS payload hashes on implemented v1 paths.
- `examples/cap-core/v1/*.json` and `docs/CAP_examples.md` now label signed v1 examples as `rfc8785-jcs`.

Remaining production gaps: production KMS/HSM or workload-key integration, registry-backed key discovery/revocation, audited external JOSE/DSSE/COSE profile integration, and third-party cross-implementation JCS fixtures remain separate tasks.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T3`.

Objective: implement RFC 8785 JSON Canonicalization Scheme for v1 signing surfaces while retaining v0.1 deterministic JSON compatibility.

Inspect: `src/cap_protocol/security/cap_crypto.py`, signing tests, docs in `docs/CAP_04_security_trust_evidence.md`, v1 envelope verification, DSSE/in-toto helpers, and current metadata labels for `json-deterministic-sort-keys-v0.1`.

Required work: add a v1 JCS canonicalization path; mark v1 signatures as using RFC 8785/JCS; preserve v0.1 signature verification under the old algorithm label; add cross-ordering, unicode, numeric, and tamper fixtures where practical.

Acceptance: all v1 signatures use JCS; v0.1 signed fixtures remain valid; signature metadata clearly identifies the algorithm; tests fail on canonicalization mismatch.

Verification: run security/signing tests and the default test command.

Final response: summarize algorithm split and compatibility behavior.

## Source: `docs/task_prompts/cap_v1/Done/P1-T4_wire_local_pep_onto_agent_to_user_and_local_tool_paths.md`

## Task Prompt: P1-T4 Wire Local PEP Onto Agent-To-User And Local-Tool Paths

Status: Complete for deterministic executable-binding Local PEP mediation.

Implementation evidence:

- `src/cap_protocol/runtime/local_pep.py` now exposes explicit `deliver_user_output(...)` and `authorize_local_tool_call(...)` boundary APIs that keep lower-level output gating reusable while returning audit and provenance refs for mediated decisions.
- `src/cap_protocol/bindings/grpc_reference/edge_client.py` routes selected user-visible question delivery and raw local observation handling through Local PEP; `mcp_adapter.py` routes MCP-style local-tool simulation through Local PEP.
- `src/cap_protocol/bindings/http_json/run_demo.py` routes selected user-visible question delivery and raw local observation handling through Local PEP; `integrations_v1.py` routes MCP-style local-tool simulation through Local PEP.
- gRPC and HTTP execution reports now include `local_pep_decision_ref` and Local PEP provenance refs before signing the report payload.
- `tests/test_cap_v1_pep.py` covers the new boundary APIs, mediated local-tool allows, forbidden local-tool refusal, and direct user-output/tool bypass refusal.
- `tests/test_grpc_reference_v1_binding.py` and `tests/test_http_binding.py` assert Local PEP mediation flags, direct bypass refusal flags, and audit/provenance links in executable binding reports.
- `src/cap_protocol/conformance/v1_runner.py` includes release-gated deterministic checks for mediated user output, mediated local tool access, and direct bypass refusals.

Remaining production gaps: this is deterministic in-process scaffold wiring. It does not provide OS/platform-enforced isolation, separately privileged proxy deployment, attested Local PEP deployment, live model-stream interception, production local-tool clients, or production registry/PDP distribution.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T4`.

Objective: make the reusable Local PEP the enforced path from agent to user-visible output and local tools in both executable bindings.

Inspect: Local PEP scaffold, gRPC and HTTP binding flow, agent output code, local tool invocation paths, CAP-Med profile constraints, bypass tests, and `docs/CAP_RELEASE_GATES.md`.

Required work: route user-visible output, local tool calls, local memory/raw data movement, privacy vetoes, typed refusals, and streaming gate calls through Local PEP; remove or guard direct bypass paths; add adversarial tests that attempt direct output and direct local-tool access.

Acceptance: direct agent-to-user output is structurally impossible in migrated paths; bypass tests fail closed; Local PEP decisions are linked to audit/provenance where scaffolds exist.

Verification: run Local PEP tests, binding tests, and the default test command.

Final response: summarize enforced paths and any remaining deployment trust-mode limitations.

## Source: `docs/task_prompts/cap_v1/Done/P1-T5_wire_edge_pep_onto_cross_boundary_paths.md`

## Task Prompt: P1-T5 Wire Edge PEP Onto Cross-Boundary Paths

### Implementation Status

Completed for the gRPC and HTTP/JSON demo bindings.

Executable evidence:

- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/bindings/edge_pep_bridge.py`
- `src/cap_protocol/bindings/grpc_reference/center_server.py`
- `src/cap_protocol/bindings/grpc_reference/edge_client.py`
- `src/cap_protocol/bindings/grpc_reference/cap_v1_core.py`
- `src/cap_protocol/bindings/http_json/http_runtime.py`
- `src/cap_protocol/bindings/http_json/run_demo.py`
- `src/cap_protocol/bindings/http_json/cap_v1_types.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_grpc_reference_v1_binding.py`
- `tests/test_http_binding.py`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_v1_TASKS.md`

Covered behavior:

- gRPC center-to-edge `GuardDecision`, `Directive`, and `InterruptDecision` envelopes are verified through Edge PEP before edge payload use;
- gRPC edge-to-center `ExecutionReport` envelopes are verified through Edge PEP before center payload use;
- HTTP/JSON outbound requests, inbound acknowledgments, server-received envelopes, and center-to-edge directive handoff pass Edge PEP checks;
- binding reports expose the verification order and prove invalid signature, expired envelope, unknown boundary, revoked authority, and payload-ref dereference refusal cases;
- Edge PEP supports receiver-delegatee authority validation for boundary directives while keeping the default sender-delegatee behavior for existing unit tests.

Remaining production gaps: key lookup, PolicyRef resolution, PrivacyBoundary lookup, AuthorityChain revocation freshness, payload dereference, and PDP decisions are still in-process mappings/callbacks. This is not a deployed Edge PEP sidecar/service mesh, production registry integration, or release-blocking CAP v1 certification.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T5`.

Objective: make Edge PEP the enforced path for cross-boundary gRPC and HTTP/JSON traffic.

Inspect: Edge PEP scaffold, gRPC/HTTP clients and servers, signature helpers, authority-chain verifier, policy and privacy-boundary resolution stubs, and payload dereference code.

Required work: route every network-bound `CAPEnvelope` through Edge PEP before payload use; validate signature, timestamp, TTL, clock skew, privacy boundary, policy refs, and authority chain in the documented order; add tests for invalid signature, expired envelope, unknown boundary, revoked authority, and payload-ref dereference refusal.

Acceptance: cross-boundary envelopes are verified before payload dereference; bypass around Edge PEP is covered by tests; errors are typed refusals.

Verification: run Edge PEP tests, binding tests, and the default test command.

Final response: summarize verification order and unresolved registry/PDP dependencies.

## Source: `docs/task_prompts/cap_v1/Done/P1-T6_implement_runtime_interruptdecision_and_composition_rules.md`

## Task Prompt: P1-T6 Implement Runtime InterruptDecision And Composition Rules

### Implementation Status

Completed for deterministic runtime composition and demo binding linkage.

Executable evidence:

- `src/cap_protocol/runtime/interrupts.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/supervisor_gateway.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `src/cap_protocol/bindings/grpc_reference/cap_v1_core.py`
- `src/cap_protocol/bindings/grpc_reference/center_server.py`
- `src/cap_protocol/bindings/grpc_reference/edge_client.py`
- `src/cap_protocol/bindings/grpc_reference/conformance_v1.py`
- `src/cap_protocol/bindings/http_json/cap_v1_types.py`
- `src/cap_protocol/bindings/http_json/run_demo.py`
- `src/cap_protocol/bindings/http_json/conformance_v1.py`
- `tests/test_interrupt_runtime.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_grpc_reference_v1_binding.py`
- `tests/test_http_binding.py`
- `tests/test_conformance.py`
- `docs/CAP_03_primitives.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_v1_TASKS.md`

Covered behavior:

- all seven Core actions (`allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, `reroute`) can be emitted as schema-shaped `InterruptDecision` payloads;
- deterministic composition implements `deny > pause/escalate > transform > constrain > allow`;
- conflicting transforms compose to bounded `pause`;
- compatible `constrain` decisions merge by narrowing constraints and contradictory constraint intersections compose to `deny`;
- CAP-Med profile shorthand maps to Core primitive actions through `cap_med_profile_interrupts(...)` and `compose_cap_med_interrupts(...)`;
- Local PEP and Supervisor Gateway interrupt payloads use the shared runtime builder;
- gRPC and HTTP/JSON demos emit explicit applied `InterruptDecision` envelopes and execution reports link to applied interrupt refs.

Remaining production gaps: this is an in-process deterministic runtime helper, not a deployed logical Interrupt Manager. Production live model-stream routing, native/browser UI abort/correction rollout, production human-review workflow integration, durable cross-service conflict state, and production Control Plane deployment remain open.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T6`.

Objective: use `InterruptDecision` as the runtime control object with the seven primitives and deterministic composition rules.

Inspect: `schemas/cap-core/v1/interrupt-decision.schema.json`, current guard/refusal code, Local PEP, Edge PEP, Supervisor Gateway stub, conformance runner, CAP-Med examples, and `docs/CAP_03_primitives.md`.

Required work: implement the seven actions `allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, and `reroute`; implement conflict resolution `deny > pause/escalate > transform > constrain > allow`; add a profile-composition library for CAP-Med behaviors; emit explicit `InterruptDecision` objects instead of implicit guard side effects.

Acceptance: V1 interrupt conformance covers all primitives; conflicting decisions resolve predictably; execution reports link to the applied interrupt decision.

Verification: run interrupt/conformance tests and the default test command.

Final response: summarize primitives, conflict handling, and profile-composition API.

## Source: `docs/task_prompts/cap_v1/Done/P1-T7_implement_structured_privacyboundary_pdp_evaluation.md`

## Task Prompt: P1-T7 Implement Structured PrivacyBoundary PDP Evaluation

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T7`.

Objective: evaluate `PrivacyBoundary` and closed `OperationalConstraints` through the PDP instead of profile-string checks.

Inspect: privacy and constraints schemas, Local PEP checks, OPA-style adapter, profile constraints, CAP-Med fixtures, and existing privacy tests.

Required work: represent Core operational constraints as a closed shape; move CAP-Med fields such as `non_diagnostic_required` into `profile_constraints`; implement structured boundary evaluation over classification, movement, transformation, retention, logging, audit visibility, recipients, raw-data egress, and minimization according to the chosen doc model; add tests for new profiles without code changes.

Acceptance: V1 privacy conformance passes; Core/profile mixing is eliminated; PEP refusals cite the failing boundary dimension.

Verification: run PDP/privacy tests, schema tests, and the default test command.

Final response: summarize the policy model and compatibility changes.

### Implementation Status

Status: Completed as deterministic in-process v1 privacy PDP scaffold and runtime wiring. This does not claim a deployed local/central PDP service, production Policy Registry distribution, policy-language portability, or full CAP v1 runtime certification.

Implemented evidence:

- Added `src/cap_protocol/runtime/privacy_pdp.py` with `evaluate_privacy_boundary(...)`, `normalize_operational_constraints(...)`, the nine first-class privacy dimensions, closed Core `OperationalConstraints` fields, and known profile-only constraint migration into `profile_constraints`.
- Wired Local PEP, Edge PEP, and v1 OPA-style adapter paths through the structured privacy PDP for PrivacyBoundary decisions.
- Privacy refusals now cite the failing boundary dimension, such as `raw_data_egress.raw_transcript`, `movement.local_only`, `allowed_recipients`, or `minimization.allowed_summary_fields`.
- Added `tests/test_privacy_pdp.py` for all nine PrivacyBoundary dimensions, Core/profile constraint normalization, profile portability without code-branch changes, and PEP refusal detail checks.
- Extended the v1 conformance runner with structured privacy PDP checks; after P1-T10 these checks are part of the release-blocking deterministic scaffold gate.

Verification evidence:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_privacy_pdp.py tests/test_cap_v1_pep.py tests/test_cap_v1_schemas.py tests/test_cap_v1_linkml.py tests/test_conformance.py -q

source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_grpc_reference_v1_binding.py tests/test_http_binding.py tests/test_replay_idempotency.py -q
```

Remaining production gaps:

- The PDP is an in-process deterministic helper, not a deployed local/central PDP service.
- Policy Registry distribution, session pinning, emergency overrides, production policy-language adapters, and release-blocking v1 privacy conformance remain open.

## Source: `docs/task_prompts/cap_v1/Done/P1-T8_apply_clock_skew_and_expiry_uniformly.md`

## Task Prompt: P1-T8 Apply Clock Skew And Expiry Uniformly

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T8`.

Objective: apply default 30 second clock-skew tolerance and TTL/expiry checks uniformly across all v1 envelope verification paths.

Inspect: Edge PEP, Local PEP, signing helpers, authority-chain verifier, policy bundle cache, registry stubs, conformance tests, and docs.

Required work: centralize or consistently reuse time validation; cover envelope `timestamp` and `ttl_ms`, authority step expiry, policy bundle expiry, registry metadata freshness, and evidence freshness where documented; add boundary tests for just-inside and just-outside skew.

Acceptance: V1 clock-skew conformance passes; all refusal codes are consistent; no runtime path uses payload content before expiry checks.

Verification: run expiry/skew tests and the default test command.

Final response: summarize shared validation behavior and default tolerance.

### Implementation Status

Completed in this repository as deterministic scaffold/runtime coverage.

Implemented evidence:

- `src/cap_protocol/runtime/temporal.py` centralizes CAP v1 temporal checks with a default 30 second skew tolerance, RFC3339 parsing, envelope `timestamp` plus `ttl_ms` validation, future/not-before skew checks, and exact expiry checks.
- Edge PEP envelope verification, AuthorityChain verification, Local PEP directive and policy-bundle expiry, Supervisor Gateway authority expiry, federated registry metadata freshness, EvidenceRef freshness, and the gRPC/HTTP v1 binding validators reuse the shared temporal helpers.
- Expired envelopes and directives are refused before payload dereference, privacy payload inspection, evidence hash checks, or executor side effects in the covered v1 scaffolds.
- Boundary coverage was added for exactly-inside and just-outside the default 30 second skew, exact expiry boundaries, authority `issued_at`/`not_before`, registry metadata expiry, EvidenceRef `expires_at`, and future `created_at`.
- The v1 conformance runner now includes default-skew boundary and expired payload-ref non-dereference checks; after P1-T10 these checks are part of the release-blocking deterministic scaffold gate.

Verification evidence:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_temporal_validation.py tests/test_authority_chain.py tests/test_federated_registry.py tests/test_cap_v1_pep.py tests/test_grpc_reference_v1_binding.py tests/test_http_binding.py tests/test_conformance.py -q
```

Remaining gaps:

- This is still deterministic in-process scaffold behavior. Production registry services, deployed PEPs, distributed clock source policy, revocation freshness, and release-blocking CAP v1 certification remain separate backlog work.

## Source: `docs/task_prompts/cap_v1/Done/P1-T9_use_capability_as_unified_registration_object.md`

## Task Prompt: P1-T9 Use Capability As Unified Registration Object

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P1-T9`.

Objective: use v1 `Capability` as the unified registration object for agents, tools, services, humans, and policy subjects.

Inspect: registry stubs, capability schema, A2A and MCP metadata examples, Agent/Tool capability code, docs in `CAP_02`, `CAP_03`, and `CAP_05`, and tests.

Required work: migrate informal `AgentCapability` and `ToolCapability` shapes to unified `Capability`; use `kind` as the discriminator; put A2A AgentCard and MCP server details in `profile_extensions`; update registry APIs and examples; add backward-compatibility adapters only where needed.

Acceptance: all capability metadata uses one shape; registry tests cover agent, tool, service, human, and policy subjects; docs explain extension metadata.

Verification: run registry/capability/schema tests and the default test command.

Final response: summarize unified shape and migration impact.

### Implementation Status

Completed in this repository as deterministic scaffold/runtime coverage.

Implemented evidence:

- `CapabilityRegistry` now validates and stores one closed CAP v1 `Capability` metadata shape for `agent`, `tool`, `service`, `human`, and `policy` subjects.
- Kind-specific registry views (`AgentRegistry`, `ToolRegistry`, `ServiceRegistry`, `HumanRegistry`, and `PolicySubjectRegistry`) normalize to the same `Capability` shape and are compatibility views, not separate Core metadata shapes.
- A small legacy adapter can ingest older `agent_id`/`tool_id` style metadata when needed, preserving non-Core fields under `profile_extensions.legacy`.
- V1 examples now cover all five `Capability.kind` values, with A2A, MCP, service, human-review, and policy details under `profile_extensions`.
- Registry and v1 release-gated deterministic conformance tests cover authorization and metadata freshness for unified Capability subject kinds.

Verification evidence:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_federated_registry.py tests/test_cap_v1_schemas.py tests/test_cap_v1_linkml.py tests/test_conformance.py -q
```

Remaining gaps:

- This is still an in-memory deterministic registry scaffold. Production Capability Registry service deployment, signed distribution, federation, revocation propagation, and operational monitoring remain open backlog work.

## Source: `docs/task_prompts/cap_v1/Done/P2-DOC-01_architecture_diagrams.md`

## Task Prompt: P2-DOC-01 Architecture Diagrams

### Implementation Status

Completed as documentation-only architecture diagram work.

Documentation updated:

- `docs/architecture.md`
- `docs/CAP_00_README.md`
- `docs/CAP_02_core_model.md`
- `docs/CAP_05_integrations.md`
- `README.md`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`

Remaining production gaps: the diagrams describe the CAP v1 target topology. The current package still remains a v0.1 production-candidate subset with initial v1 schemas plus Local PEP, Edge PEP, Supervisor Gateway, federated registry, and observability sink scaffolding. Deployed Supervisor Gateway service integration, Session Router, federated registry services, production observability exporter/collector integration, live streaming lookahead integration, and full runtime adoption remain separate runtime tasks.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-DOC-01`.

### Objective

Add CAP v1 architecture diagrams to docs.

### Required Diagram Content

- Local PEP
- Edge PEP
- decomposed Control Plane
- Supervisor Gateway
- Session Router
- logical Interrupt Manager
- local and central PDPs
- federated registries
- independent observability plane
- data, control, and observability planes

### Files To Inspect

- `docs/architecture.md`
- `docs/CAP_00_README.md`
- `docs/CAP_02_core_model.md`
- `docs/CAP_05_integrations.md`

### Required Work

1. Add Mermaid diagrams in Markdown.
2. Keep diagrams simple enough to render reliably.
3. Make v0.1 vs v1 status clear in captions.
4. Do not imply full v1 runtime implementation.

### Acceptance Criteria

- Diagrams show all required components and planes.
- The implementer reading path is clearer.
- No runtime code changes are required unless tests need doc path updates.

### Verification

Run tests if any docs tooling exists; otherwise run:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize diagrams added and status caveats.

## Source: `docs/task_prompts/cap_v1/Done/P2-DOC-02_therapist_supervisor_sequences.md`

## Task Prompt: P2-DOC-02 Therapist/Supervisor Sequence Examples

### Implementation Status

Completed as documentation-only sequence example work.

Documentation updated:

- `docs/CAP_examples.md`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`

Examples added:

- safe pass-through;
- diagnostic transform;
- supervisor pause with Local PEP overreach veto;
- self-harm escalation;
- offline fallback.

Remaining runtime gaps: these examples document the CAP v1 target behavior and align with existing deterministic Local PEP and Supervisor Gateway scaffolding. A deployed Supervisor Gateway service, live stream lookahead integration, Human Review service, production signed policy-bundle distribution, and federated registry-backed runtime remain separate runtime tasks.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-DOC-02`.

### Objective

Add Therapist/Supervisor sequence examples for the CAP v1 profile scenario.

### Required Examples

- safe pass-through
- diagnostic transform
- supervisor pause
- self-harm escalation
- offline fallback

### Files To Inspect

- `docs/CAP_examples.md`
- `docs/CAP_07_profiles_roadmap.md`
- `docs/CAP_06_conformance.md`
- `examples/cap-core/v1/`
- `schemas/domains/profiles.yaml`

### Required Work

1. Add redacted JSON or sequence examples.
2. Keep Therapist supportive, non-diagnostic, and non-prescriptive.
3. Show Supervisor receives redacted context, EvidenceRefs, dimension vectors, and safety flags by default.
4. Show Local PEP veto where Supervisor overreaches.
5. Do not include hidden chain-of-thought or raw sensitive evidence.

### Acceptance Criteria

- Examples cover all required scenarios.
- Examples are schema-valid where they are JSON artifacts.
- Sensitive examples are minimized/redacted.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize examples added, validation status, and remaining runtime gaps.

## Source: `docs/task_prompts/cap_v1/Done/P2-DOC-03_schema_appendix_migration.md`

## Task Prompt: P2-DOC-03 Schema Appendix Migration

### Implementation Status

Completed as documentation-only schema appendix migration work.

Documentation updated:

- `docs/CAP_appendix_schemas.md`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`

Appendix changes:

- Preserves v0.1 inline JSON Schema skeletons as current-runtime compatibility documentation.
- Adds CAP v1 LinkML reading path.
- Adds v1 domain map and v1 JSON Schema/example map.
- Explains that LinkML is the authoring layout while checked-in JSON Schema artifacts are executable validation artifacts until deterministic generation is reviewed.
- Keeps the runtime caveat explicit: after P1-T2 the gRPC and HTTP/JSON demos use v1 `CAPEnvelope` hot paths, while compatibility fixtures still preserve the v0.1 subset and the full runtime has not migrated to the complete v1 object model.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-DOC-03`.

### Objective

Update the schema appendix after v1 schema migration while preserving v0.1 compatibility notes.

### Files To Inspect

- `docs/CAP_appendix_schemas.md`
- `schemas/cap.yaml`
- `schemas/core.yaml`
- `schemas/domains/*.yaml`
- `schemas/cap-core/v0.1/*.schema.json`
- `schemas/cap-core/v1/*.schema.json`
- `examples/cap-core/v1/*.json`
- `tests/test_cap_v1_schemas.py`
- `tests/test_cap_v1_linkml.py`

### Required Work

1. Keep v0.1 appendix content clearly labeled as current implementation where appropriate.
2. Add v1 LinkML and JSON Schema reading paths.
3. Explain that LinkML is the authoring layout and JSON Schema artifacts are executable validation artifacts until generation is automated.
4. Avoid duplicating giant schemas in markdown if links to files are clearer.

### Acceptance Criteria

- Appendix reflects v1 object names.
- v0.1 compatibility notes remain.
- Docs do not imply runtime migration is complete.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize appendix changes and schema status.

## Source: `docs/task_prompts/cap_v1/Done/P2-DOC-04_v1_release_gates.md`

## Task Prompt: P2-DOC-04 v1 Release Gates

### Implementation Status

Completed as documentation-only release gate work.

Documentation updated:

- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_FINAL_STATUS.md`
- `docs/CAP_CLAIMS.md`
- `README.md`
- `docs/CAP_v1_TASKS.md`
- `docs/task_prompts/cap_v1/README.md`

Gate updates:

- Separates `v0.1-production-candidate`, `v1-architecture-documented`, `v1-runtime-scaffold`, `v1-implemented-runtime`, and stable-release labels.
- Adds v1 implemented-runtime gates for LinkML/JSON drift, v1 runtime schema adoption, Local PEP, Edge PEP, Supervisor Gateway, Session Router, Interrupt Manager, streaming lookahead, offline signed policy bundles, PDP/Policy Registry separation, federated registries, authority warrants, observability-plane split, and conformance backlog.
- Preserves external stable-release gates for security review, KMS/HSM, organization policy deployment, live interoperability, production observability/audit, domain semantic-quality evaluation, regulated-profile review, and performance/mobile budgets.
- Keeps the public claim conservative: current status supports v0.1 production candidate and v1 documented architecture, not v1 implemented runtime or stable standard.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-DOC-04`.

### Objective

Update release gates for CAP v1 so they distinguish v0.1 candidate, v1 documented architecture, and v1 implemented runtime.

### Files To Inspect

- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_FINAL_STATUS.md`
- `docs/CAP_CLAIMS.md`
- `docs/CAP_v1_TASKS.md`
- `README.md`

### Required Work

1. Keep v0.1 production-candidate gates separate from v1 gates.
2. Add v1 release gates for LinkML/JSON schema drift, Local PEP, Edge PEP, Supervisor Gateway, streaming, offline policy bundles, registries, observability plane split, and conformance backlog.
3. Do not call v1 stable or implemented until gates pass.
4. Include external gates such as security review, KMS/HSM, live interoperability, and domain semantic-quality evaluation.

### Acceptance Criteria

- Release docs distinguish v0.1 candidate, v1 documented architecture, and v1 implemented runtime.
- CAP claims remain conservative and test-backed.
- Unresolved gaps are not deleted.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize gate updates and remaining blockers to v1 implementation status.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-01_local_pep.md`

## Task Prompt: P2-RUNTIME-01 Local PEP

### Implementation Status

Completed as a deterministic reusable Local PEP scaffold. Status update after P1-T4: both executable v1 bindings now call the scaffold for selected user-visible output, local memory/raw-observation handling, and MCP-style local-tool access.

Executable evidence:

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_replay_idempotency.py`
- `tests/test_policy_hot_update.py`
- `tests/test_grpc_reference_v1_binding.py`
- `tests/test_http_binding.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`

Covered behavior:

- local privacy boundary enforcement for Therapist/Supervisor raw transcript and raw audio defaults;
- raw evidence-reference substitution before Supervisor consultation;
- deterministic typed `RefusalMessage` generation through the reusable Local PEP API;
- output gating before user-visible delivery for diagnostic or treatment language;
- mediated user-output and local-tool boundary APIs that return audit/provenance refs;
- gRPC and HTTP/JSON demo wiring for selected user-visible output, raw local observation minimization, and MCP-style local-tool simulation;
- local guard rules for unsafe Supervisor directives and offline-sensitive output;
- Supervisor overreach veto for raw data, diagnosis, and treatment advice;
- offline fallback fail-closed behavior using cached policy-bundle metadata, with `P2-RUNTIME-04` adding optional detached-JWS signed-payload verification;
- deterministic streaming transform/correction scaffolding when unsafe output is detected before or after emission.

Remaining production gaps: this is still a Python scaffold, not a production sandbox or complete CAP v1 runtime. Durable replay stores, production signed-policy distribution, rotation, revocation freshness, production key management, separately privileged or attested Local PEP deployment, production model-provider rollout, shipping native UI wrappers around the P3-T1/P3-T4 reference adapters, deployed Supervisor Gateway service integration, and registry integration remain separate runtime work.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-01`.

### Objective

Extract or strengthen a reusable Local PEP component for CAP v1.

### Required Local PEP Enforcement

- local privacy boundaries
- raw evidence locality
- evidence-reference substitution
- local typed refusal
- output gating before user-visible delivery
- local guard rules
- Supervisor overreach veto
- offline fallback behavior
- streaming interruption when implemented

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_cap_v1_pep.py`
- `schemas/domains/privacy.yaml`
- `schemas/domains/profiles.yaml`
- `docs/architecture.md`

### Required Work

1. Keep Local PEP reusable and independent of v0.1 demo internals.
2. For Therapist/Supervisor, enforce raw transcript/audio locality by default.
3. Make typed refusals deterministic.
4. Add tests for privacy boundary, output gate, and Supervisor veto.
5. Do not claim full production sandboxing unless implemented.

### Acceptance Criteria

- Minimal reusable Local PEP exists.
- Tests show Local PEP enforces privacy and local output gating.
- Existing demos are either kept as v0.1 examples or carefully migrated.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize Local PEP API, tests, and remaining production hardening gaps.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-02_edge_pep.md`

## Task Prompt: P2-RUNTIME-02 Edge PEP

### Implementation Status

Completed as a deterministic reusable Edge PEP scaffold, with P1-T5 wiring into the gRPC and HTTP/JSON demo cross-boundary `CAPEnvelope` paths.

Executable evidence:

- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/bindings/edge_pep_bridge.py`
- `src/cap_protocol/bindings/grpc_reference/center_server.py`
- `src/cap_protocol/bindings/grpc_reference/edge_client.py`
- `src/cap_protocol/bindings/http_json/http_runtime.py`
- `src/cap_protocol/bindings/http_json/run_demo.py`
- `src/cap_protocol/runtime/__init__.py`
- `src/cap_protocol/runtime/authority.py`
- `src/cap_protocol/security/cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_grpc_reference_v1_binding.py`
- `tests/test_http_binding.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`

Covered behavior:

- cross-trust-boundary `CAPEnvelope` missing or invalid signatures are refused before payload use;
- detached signature verification covers tampered signed envelope fields;
- signed-envelope shape, timestamp, TTL, and clock-skew checks run before privacy or payload-ref dereference;
- configured boundary `PolicyRef` version/digest checks refuse stale or mismatched policy metadata;
- resolved `AuthorityChain` verification can be required before forwarding, using the deterministic signed-chain verifier;
- gRPC and HTTP/JSON demo boundary paths require Edge PEP allow decisions before payload use and expose report evidence for verification order plus refusal cases;
- unknown privacy boundary refs fail closed before payload-ref dereference;
- embedded payloads and resolved payload refs are checked for raw transcript/audio before forwarding.

Remaining production gaps: authority chains, policy refs, privacy boundaries, and payload refs are resolved through injected local mappings/callbacks only. This is not a production PDP, Policy Registry, Evidence Registry, key-discovery service, service mesh/sidecar integration, or full v1 cross-boundary runtime.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-02`.

### Objective

Add or strengthen a reusable Edge PEP for CAPEnvelope validation at network/message boundaries.

### Required Edge PEP Enforcement

- CAPEnvelope signature validation
- policy checks at boundaries
- authority-chain verification before forwarding
- privacy boundary checks before payload dereference or egress
- refusal on invalid or missing signatures for cross-trust-boundary envelopes

### Files To Inspect

- `src/cap_protocol/runtime/edge_pep.py`
- `src/cap_protocol/security/cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `schemas/cap-core/v1/cap-envelope.schema.json`
- `schemas/domains/control.yaml`

### Required Work

1. Validate signatures before payload use.
2. Validate TTL/expiry and privacy boundary references.
3. Add tests for missing signature, invalid signature, expired envelope, and privacy-before-dereference.
4. Keep policy/authority verification minimal if registries are not implemented; document stubs clearly.

### Acceptance Criteria

- Minimal Edge PEP exists or is clearly stubbed with tests.
- Cross-trust-boundary invalid/missing signature is refused.
- Existing tests pass.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize Edge PEP behavior and remaining registry/PDP dependencies.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-03_streaming_lookahead_buffer.md`

## Task Prompt: P2-RUNTIME-03 Streaming Lookahead Buffer

### Implementation Status

Completed as a deterministic, unit-testable Local PEP streaming lookahead scaffold.

Executable evidence:

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`

Covered behavior:

- `LocalPEP.open_stream_gate(...)` creates a reusable `StreamingLookaheadBuffer`;
- `StreamingLookaheadConfig` supports configurable token, character, and profile time-budget metadata;
- safe chunks are held until flush or released only after the configured lookahead window is exceeded;
- unsafe diagnostic/treatment wording fully inside the buffer is transformed before user-visible delivery;
- late detection after partial release emits a correction frame and linked execution report;
- Supervisor directives still cannot force unsafe content through the stream gate.

Updated by P3-T1/P3-T3/P3-T4/P3-T11: the runtime now includes a reference live local/optional Ollama stream adapter, wall-clock `tick()` release, pull-side backpressure, abort propagation, CLI/WebSocket-style abort replacement contracts, CLI/WebSocket-style correction-frame replacement/annotation contracts, and a local deterministic streaming benchmark artifact. Remaining gaps are production model-provider rollout, shipping native UI wrappers, production Local PEP trust modes, deployment-representative latency/resource evaluation, and a deployed Interrupt Manager.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-03`.

### Objective

Implement or scaffold a Local PEP streaming lookahead buffer.

### Required Behavior

1. Streaming output passes through Local PEP before user-visible delivery.
2. Local PEP supports configurable lookahead buffer.
3. Unsafe buffered content is blocked or transformed before display.
4. Late detection after partial emission emits a correction frame.
5. Report links original stream id, partial emission, `InterruptDecision`, correction frame, and audit/provenance references where available.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `tests/test_cap_v1_pep.py`
- `schemas/domains/control.yaml`
- `schemas/cap-core/v1/interrupt-decision.schema.json`
- `schemas/cap-core/v1/execution-report.schema.json`

### Required Work

1. Keep the buffer deterministic and unit-testable.
2. Avoid introducing model streaming dependencies.
3. Add tests for diagnostic wording in buffer and late correction.
4. Ensure no unsafe diagnostic/treatment content reaches the user in buffered cases.

### Acceptance Criteria

- Local PEP supports configurable buffer behavior.
- Streaming tests cover transform and correction.
- Supervisor cannot force unsafe output through the stream.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize streaming API, tests, and live integration gaps.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-04_offline_policy_bundle_cache.md`

## Task Prompt: P2-RUNTIME-04 Offline Policy Bundle Cache

### Implementation Status

Completed as a deterministic Local PEP offline policy-bundle cache scaffold.

Executable evidence:

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/__init__.py`
- `src/cap_protocol/security/cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_policy_hot_update.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`

Covered behavior:

- `PolicyBundle` carries bundle id, version, digest, expiry, signature metadata, policy refs, and optional signed payload;
- `PolicyBundle.validation_status(...)` fails closed on malformed digest, invalid expiry, expiry, missing signature metadata, signed-payload signature failure, or digest mismatch;
- signed payload verification uses existing `DetachedJWS` and `KeyRegistry` helpers, not custom cryptography;
- `OfflinePolicyBundleCache` models a cached bundle plus central Control Plane reachability;
- Local PEP treats explicit offline mode or unreachable Control Plane as offline fallback mode;
- valid cached policy permits only profile-safe supportive output;
- missing, expired, malformed, or tampered cached policy fails closed;
- Therapist offline mode blocks raw-data upload, external messaging, diagnosis, treatment advice, prescription, and sensitive/irreversible side-effect language.

Updated by `P2-T2`: a local `ReferencePolicyRegistryService` now covers service-backed signed-bundle fetch, per-session pinning, explicit hot update, online revoked-bundle refusal, and audited emergency override.

Remaining production gaps: this is not a production network Policy Registry, central PDP deployment, or KMS/HSM-backed signing system. Production deployments still need service authentication, HA replication, monitoring, organization rollout controls, and KMS/HSM signing custody.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-04`.

### Objective

Implement or scaffold offline behavior for Local PEP using cached signed policy bundles.

### Required Behavior

- Local PEP can operate when central Control Plane is unreachable.
- Cached policy bundles have expiry and version/digest.
- Sensitive turns fail closed when policy bundle is missing or expired.
- Therapist offline mode permits only profile-safe supportive behavior.
- Offline mode blocks diagnosis, treatment advice, prescription, raw-data upload, new high-risk tool access, and irreversible external side effects.

### Files To Inspect

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/security/cap_crypto.py`
- `tests/test_cap_v1_pep.py`
- `docs/CAP_04_security_trust_evidence.md`

### Required Work

1. Represent a policy bundle with version, digest, expiry, and signature status.
2. Add tests for central unreachable plus valid cached policy.
3. Add tests for expired and missing policy.
4. Make failure closed behavior explicit.
5. Do not implement custom cryptography.

### Acceptance Criteria

- Offline valid cache allows safe supportive behavior only.
- Offline expired/missing cache blocks sensitive behavior.
- Docs say whether this is scaffold or production-grade signed-bundle support.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize offline behavior, signature assumptions, and tests.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-05_supervisor_gateway_stub.md`

## Task Prompt: P2-RUNTIME-05 Supervisor Gateway Stub

### Implementation Status

Completed as a deterministic Supervisor Gateway runtime scaffold.

Executable evidence:

- `src/cap_protocol/runtime/supervisor_gateway.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_06_conformance.md`

Covered behavior:

- separates Supervisor authority role, Supervisor Gateway endpoint, and backend engine reference;
- prepares Supervisor consultation requests from Local PEP-minimized context, replacing raw transcript/audio with local EvidenceRefs by default;
- validates authority scope through existing `AuthorityChain` verification helpers when a `KeyRegistry` is supplied;
- translates structured safe strategy output into a v1-shaped `Directive`;
- translates `pause` and `escalate` Supervisor output into v1-shaped `InterruptDecision` objects;
- uses existing detached-JWS helpers for gateway signatures when a signing key is supplied;
- preserves Local PEP as the final veto for raw transcript/audio requests, diagnosis, treatment advice, and other local policy violations.

Remaining production gaps: this is not a deployed Supervisor Gateway service, backend model/human/rule-engine integration, Session Router, production Interrupt Manager, Policy Registry/PDP integration, service discovery, scaling, or operational monitoring implementation.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-05`.

### Objective

Add a minimal Supervisor Gateway stub that separates Supervisor authority role, gateway endpoint, and backend engine.

### Required Behavior

- Supervisor output is structured.
- Supervisor consultation receives redacted context and EvidenceRefs by default.
- Gateway validates authority scope and privacy boundary.
- Gateway translates safe supervisor output into `Directive` or `InterruptDecision`.
- Local PEP can veto unsafe supervisor output.

### Files To Inspect

- `src/cap_protocol/runtime/`
- `schemas/domains/profiles.yaml`
- `schemas/domains/control.yaml`
- `tests/test_cap_v1_pep.py`
- `docs/architecture.md`
- `docs/CAP_02_core_model.md`

### Required Work

1. Add a small runtime module only if it improves clarity.
2. Model the gateway separately from backend model/human/rule engine.
3. Add tests for safe strategy, raw transcript request, diagnosis request, and pause/escalate output.
4. Do not make Supervisor a monolithic Control Plane.

### Acceptance Criteria

- Supervisor Gateway stub exists or docs clearly explain why deferred.
- Tests show privacy-filtered structured supervisor output.
- Local PEP remains final local veto.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize gateway API, tests, and deferred production integration.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-06_federated_registry_stubs.md`

## Task Prompt: P2-RUNTIME-06 Federated Registry Stubs

### Implementation Status

Completed as deterministic federated registry runtime scaffolding.

Executable evidence:

- `src/cap_protocol/runtime/registry.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_federated_registry.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_06_conformance.md`

Covered behavior:

- Agent, Tool, Capability, Policy, and Evidence registry stubs exist through `FederatedRegistrySet`;
- registry records carry version, digest, expiry, trust domain, optional source URI, cached timestamp, and revocation state;
- cache miss/fill and cache-hit behavior is deterministic and observable;
- stale version, digest drift, expiry, trust-domain mismatch, malformed digest, and revoked metadata fail closed;
- revoked capabilities cannot authorize operations;
- Policy Registry detects `PolicyRef` digest drift;
- Evidence Registry detects EvidenceRef metadata drift and backing-content hash mismatch.

Remaining production gaps: these are in-memory stubs, not deployed registry services. Production deployments still need signed distribution, cross-organization federation, durable cache invalidation, revocation propagation, service authentication, high-availability replication, and operational monitoring.

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-06`.

### Objective

Add deterministic stubs for federated CAP registries with cache/version semantics.

### Registries

- Agent Registry
- Tool Registry
- Capability Registry
- Policy Registry
- Evidence Registry

### Files To Inspect

- `schemas/domains/capability.yaml`
- `schemas/domains/authority.yaml`
- `schemas/domains/evidence.yaml`
- `src/cap_protocol/runtime/`
- `tests/`
- `docs/architecture.md`

### Required Work

1. Add minimal registry interfaces or data classes if useful.
2. Include version, digest, expiry, trust domain, and stale metadata behavior.
3. Add tests for stale metadata, revoked capability, and cache hit/miss if implemented.
4. Do not create real network services unless explicitly needed.

### Acceptance Criteria

- Registry APIs exist as deterministic stubs with cache/version semantics.
- Stale or revoked metadata cannot silently authorize execution.
- Docs distinguish stubs from production federated services.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize registry stubs, tests, and service work still open.

## Source: `docs/task_prompts/cap_v1/Done/P2-RUNTIME-07_observability_plane_sinks.md`

## Task Prompt: P2-RUNTIME-07 Observability Plane Sinks

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-RUNTIME-07`.

### Implementation Status

Completed as deterministic observability-plane sink scaffolding.

Executable evidence:

- `src/cap_protocol/runtime/observability.py`
- `src/cap_protocol/runtime/__init__.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `tests/test_observability_plane.py`
- `docs/CAP_05_integrations.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_06_conformance.md`

Covered behavior:

- Audit sink wraps the hash-chain audit store and is durable, tamper-evident, and retention-oriented.
- Telemetry sink can fail or sample out without breaking audit integrity.
- Provenance sink preserves structural lineage independently of telemetry delivery.
- `ObservabilityPlane` isolates sink exceptions and reports per-sink delivery results without changing hot-path PEP behavior.

Updated by P2-T12 and P2-T13: signed audit-operation scaffolding and local W3C PROV-JSONLD store/query coverage now exist. Remaining production gaps: deployed audit transparency/replication services, production KMS/HSM custody, OpenTelemetry collector/exporter wiring, production PROV graph/document store deployment, access-control integration, recovery, and main-runtime/demo wiring.

### Objective

Split observability plane sinks so audit, telemetry, and provenance are not treated as one synchronous hot-path sink.

### Required Semantics

- Audit is durable, signed or tamper-evident, and retention-oriented.
- Telemetry may be sampled, lossy, and short retention.
- Provenance preserves structural lineage.
- Observability exporters are independent of hot-path control logic.

### Files To Inspect

- `src/cap_protocol/hardening/audit_store.py`
- `src/cap_protocol/bindings/*/telemetry_prov.py`
- `src/cap_protocol/bindings/http_json/`
- `tests/test_hardening.py`
- `docs/architecture.md`
- `docs/CAP_05_integrations.md`

### Required Work

1. Audit current audit, OTel, and PROV code paths.
2. Separate interfaces or docs where the code currently conflates sinks.
3. Add tests that audit integrity does not depend on telemetry delivery.
4. Avoid changing hot-path runtime behavior without focused tests.

### Acceptance Criteria

- Docs and code names reflect separate observability responsibilities.
- Audit, telemetry, and provenance assumptions are distinct.
- Existing conformance tests still pass.

### Verification

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Final Response

Summarize sink separation, tests, and remaining exporter work.

## Source: `docs/task_prompts/cap_v1/Done/P2-T10_implement_human_review_integration.md`

## Task Prompt: P2-T10 Implement Human Review Integration

Completed as a CAP v1 Human Review reference integration.

Implementation evidence:

- `src/cap_protocol/runtime/human_review.py`
- `tests/test_human_review_integration.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_v1_TASKS.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_06_conformance.md`

What changed:

- added `HumanReviewService`, `HumanReviewPortal`, `ScriptedHumanReviewPortal`, and `LocalHumanReviewClient`;
- made `escalate` `InterruptDecision` payloads create Local PEP-minimized `HumanReviewRequest` tasks;
- added optional `SessionRouter` routing for review tasks without router payload ownership;
- added structured approve, deny, transform, and pause review decisions;
- blocked portal requests for raw transcript/audio unless the active privacy policy permits them;
- emitted review audit/provenance refs and linked `ExecutionReport` objects to the interrupt and review result;
- added v1 conformance smoke checks for end-to-end escalation, raw-request refusal, structured review decisions, and report linkage.

Remaining production gaps:

- this is a reference integration, not production certification;
- reviewer authentication, production portal UI, durable queues, workflow-engine/SLA handling, reviewer roster management, operational monitoring, and organization-owned review policy remain future work.

### Original Prompt

Objective: make `escalate` usable end to end through a Human Review integration.

Inspect: interrupt schema, Supervisor Gateway, HumanReviewRequest or EscalationRequest docs, workflow handoff docs, audit/provenance, and CAP-Med escalation examples.

Required work: define service/portal stub API; create and route human review requests; enforce privacy-minimized context; return structured approval, denial, transform, or pause decisions; link review events to audit and provenance.

Acceptance: `escalate` primitive is exercised end to end; human review cannot request raw transcripts/audio unless policy allows; execution reports link to the review result.

Verification: run human-review/interruption tests and the default test command.

Final response: summarize escalation flow and portal limitations.

## Source: `docs/task_prompts/cap_v1/Done/P2-T11_wire_opentelemetry_collector_and_attribute_coverage.md`

## Task Prompt: P2-T11 Wire OpenTelemetry Collector And Attribute Coverage

Completed as a reference OpenTelemetry collector configuration and deterministic `cap.*` attribute coverage scaffold.

Implementation evidence:

- `config/otel/collector-cap.yaml`
- `src/cap_protocol/runtime/observability.py`
- `tests/test_observability_plane.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_v1_TASKS.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/CAP_06_conformance.md`

What changed:

- added a reference OTLP collector/processor/exporter config at `config/otel/collector-cap.yaml`;
- added OpenTelemetry `cap.*` attribute normalization helpers in `cap_protocol.runtime.observability`;
- added lifecycle fixture coverage for envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal events;
- added validation that fails on missing required lifecycle attributes;
- kept telemetry lossy and independent from durable audit and provenance sinks;
- extended V1-C15 conformance checks for collector config presence, lifecycle attribute coverage, and missing-attribute detection.

Remaining production gaps:

- this is a reference fixture/scaffold, not production collector deployment;
- exporter credentials, deployed collector operations, retention, backpressure/retry, access control, recovery, and full runtime rollout remain future work.

### Original Prompt

Objective: wire production-like OpenTelemetry collector/exporter configuration and verify `cap.*` attribute coverage at lifecycle states.

Inspect: observability scaffolds, OTel docs in `CAP_05`, lifecycle events, binding flow, conformance runner, and existing telemetry tests.

Required work: add collector/exporter config or test fixture; emit required `cap.*` attributes across envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal events; add coverage tests that fail on missing required attributes.

Acceptance: traces show the full CAP lifecycle; telemetry remains independent from audit and provenance; lossy telemetry failure does not break durable audit unless a profile explicitly requires it.

Verification: run observability/OTel tests and the default test command.

Final response: summarize attribute coverage and collector path.

## Source: `docs/task_prompts/cap_v1/Done/P2-T12_implement_signed_audit_operations.md`

## Task Prompt: P2-T12 Implement Signed Audit Operations

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T12`.

Objective: move signed audit from local hash-chain scaffold toward production operations with key custody hooks, retention, replication, retry, access control, and audit-as-precondition support.

Inspect: hash-chain audit store, observability sinks, signing helpers, KMS/HSM docs, profile gates, and delivery paths.

Required work: define audit signing key interface; integrate optional KMS/HSM provider hooks or deployment stubs; implement retention metadata, replication/export hooks, backpressure/retry behavior, and audit confirmation before delivery for profiles that require it.

Acceptance: audit-as-precondition can gate user-visible delivery; telemetry failure does not corrupt audit; key custody remains clearly external if no KMS/HSM is locally available.

Verification: run audit/observability/security tests and the default test command.

Final response: summarize audit durability and external key-custody assumptions.

### Implementation Status

Completed in this repository as deterministic scaffold coverage.

Implemented:

- `SignedAuditSink` signs audit operations with detached-JWS over content-minimized audit events, the next hash-chain sequence, previous-chain hash, retention/access metadata, key-custody descriptors, and replication policy.
- `AuditSigningKeyProvider` defines the signing interface; `ExternalAuditSigningKeyProvider` wraps caller-supplied key material without persisting private keys in the sink; `ExternalKMSHSMAuditSigningKeyProvider` is a fail-closed deployment hook for real KMS/HSM signers.
- `AuditRetentionPolicy`, read access checks, replication exporter hooks, retry state, and backpressure behavior are modeled in `cap_protocol.runtime.observability`.
- `ObservabilityPlane(audit_required_for_delivery=True)` can block user-visible delivery when durable signed audit confirmation fails or replication backpressure exceeds the configured threshold.
- Tests and V1-C15 conformance cover signed audit verification, tamper detection, KMS/HSM stub fail-closed behavior, replication retry/backpressure, telemetry failure isolation, and signed audit evidence in hardening checks.

Remaining production gaps:

- real deployed KMS/HSM custody and key ceremony;
- transparency-log or remote replication service deployment;
- production access-control integration and audit-reader identity enforcement;
- operational recovery/runbooks and main runtime rollout beyond deterministic scaffolds.

## Source: `docs/task_prompts/cap_v1/Done/P2-T13_wire_w3c_prov_store.md`

## Task Prompt: P2-T13 Wire W3C PROV Store

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T13`.

Objective: integrate a W3C PROV-compatible store with PROV-JSONLD ingestion and queryable lineage.

Inspect: provenance sink scaffold, PROV docs, EvidenceRef, ExecutionReport, audit links, and existing provenance tests.

Required work: select a local reference store or interface; ingest PROV-JSONLD events; support queries for session lineage, evidence lineage, authority lineage, and interrupt lineage; keep provenance independent from telemetry.

Acceptance: provenance graphs are queryable across sessions; evidence and execution events link correctly; store failure behavior is documented and tested.

Verification: run provenance tests and the default test command.

Final response: summarize store choice and query coverage.

### Implementation Status

Completed in this repository as deterministic scaffold coverage.

Implemented:

- `W3CProvenanceSink` converts CAP observability events into content-minimized PROV-JSONLD bundles with W3C `prov` context.
- `JsonlProvStore` is the local reference store: it ingests one PROV-JSONLD bundle per JSONL row and can reload/query persisted documents.
- Query helpers cover session lineage, evidence lineage, authority lineage, and interrupt lineage.
- Evidence-to-execution lineage is represented with `prov:wasDerivedFrom`; authority delegation uses `prov:actedOnBehalfOf`; execution/evidence/interrupt lifecycle facts use `prov:Entity`, `prov:Activity`, `prov:SoftwareAgent`, `prov:used`, `prov:wasGeneratedBy`, and `prov:wasAssociatedWith`.
- Store failure is isolated by `ObservabilityPlane`: provenance ingest failure does not invalidate audit or telemetry, and provenance remains outside the hot path by default.
- Tests and V1-C15 conformance cover cross-session queries, evidence/report links, authority and interrupt lookups, raw evidence/hidden chain-of-thought exclusion, and store failure isolation.

Remaining production gaps:

- deployed graph/document store with service authentication and access policy enforcement;
- backup/recovery and operational runbooks;
- production retention/deletion workflows for provenance;
- runtime rollout beyond deterministic scaffolds.

## Source: `docs/task_prompts/cap_v1/Done/P2-T14_implement_service_mesh_composition_test.md`

## Task Prompt: P2-T14 Implement Service Mesh Composition Test

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T14`.

Objective: demonstrate CAP running on a service mesh substrate such as Istio or Linkerd.

Inspect: Edge PEP, mTLS/SPIFFE integration, deployment manifests if any, architecture docs, and binding services.

Required work: add a local or documented integration path where Edge PEP runs as an application sidecar alongside the mesh sidecar; mesh handles mTLS; CAP still validates envelopes, policy, privacy, and authority; document required labels/manifests.

Acceptance: integration test or reproducible dev instructions show mesh composition; CAP does not duplicate mesh identity incorrectly; fallback local mode remains available.

Verification: run any available container/mesh smoke tests or document why they require an external cluster.

Final response: summarize mesh topology and what was verified locally.

### Implementation Status

Completed in this repository:

- Added `src/cap_protocol/runtime/service_mesh.py` with deterministic Istio/Linkerd topology helpers, Kubernetes Deployment manifest generation, mesh SPIFFE ID derivation, composition validation, an Edge PEP factory for mesh-sidecar deployments, and explicit local fallback topology.
- Added `tests/test_service_mesh_composition.py` covering:
  - Edge PEP as an application sidecar next to an injected mesh sidecar;
  - mesh-owned mTLS/SPIFFE identity with no `CAP_SPIFFE_ID` minting by CAP in mesh mode;
  - CAPEnvelope signature, PolicyRef, PrivacyBoundary, and AuthorityChain validation after the mesh transport layer;
  - runtime SPIFFE receiver mismatch refusal without CAP reterminating TLS;
  - deterministic local fallback mode.
- Added V1-C01 conformance checks for service-mesh topology, mesh identity consumption, CAP validation after mesh mTLS, and local fallback.
- Updated release/status/API docs and prompt indexes to record the scaffold and its remaining production gaps.

Verification run locally:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_service_mesh_composition.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_conformance.py -q
```

External cluster note: no live Istio/Linkerd smoke test was run in this task because the repository does not include a Kubernetes cluster, mesh control plane, or SPIRE deployment fixture. The checked-in evidence is a deterministic manifest/topology plus in-process Edge PEP verification scaffold.

## Source: `docs/task_prompts/cap_v1/Done/P2-T15_implement_workflow_engine_composition_sample.md`

## Task Prompt: P2-T15 Implement Workflow Engine Composition Sample

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T15`.

Objective: provide a Temporal or LangGraph sample showing CAP envelopes flowing through durable workflow orchestration.

Inspect: workflow engine docs in `CAP_05`, binding examples, execution reports, evidence refs, interrupt decisions, and existing examples.

Required work: choose one workflow engine; implement or document a runnable sample activity that receives, verifies, routes, and emits CAP envelopes; preserve CAP as supervisory control, not the workflow engine itself; include failure and retry behavior.

Acceptance: sample runs locally or is clearly marked as requiring optional dependency; workflow history links to CAP trace/session IDs; interrupt and execution report behavior is shown.

Verification: run sample tests if available and the default test command.

Final response: summarize workflow engine choice and runnable command.

### Implementation Status

Completed in this repository as a local Temporal-style workflow composition sample, not a deployed Temporal or LangGraph worker.

Implementation evidence:

- `src/cap_protocol/runtime/workflow_engine.py` adds `TemporalCAPWorkflowSample` and `run_temporal_workflow_sample`.
- The sample receives a signed `Directive` CAPEnvelope, verifies it through Edge PEP, routes it through `SessionRouter`, records workflow history with `workflow_id`, `run_id`, `session_id`, and `trace_id`, emits a retry-triggered `pause` `InterruptDecision`, emits a final `ExecutionReport`, and refuses a tampered input envelope before activity execution.
- `tests/test_workflow_engine_composition.py` validates envelope schema shape, interrupt/report/refusal behavior, history links, retry behavior, raw-content minimization in history, and module runnability.
- `src/cap_protocol/conformance/v1_runner.py` adds workflow checks under V1-C13.
- The runnable command is:

```bash
source venv/bin/activate
python -m cap_protocol.runtime.workflow_engine
```

Remaining production gaps:

- Deployed Temporal or LangGraph worker integration.
- Durable external workflow queue/state store.
- Production human-review workflow wiring and SLA handling.
- Operational monitoring and organization-owned retry/compensation policy.

## Source: `docs/task_prompts/cap_v1/Done/P2-T16_integrate_sigstore_and_rekor_transparency.md`

## Task Prompt: P2-T16 Integrate Sigstore And Rekor Transparency

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T16`.

Objective: add Sigstore/Rekor transparency-log integration for authority-step or release attestations.

Inspect: DSSE/in-toto helpers, authority-chain signatures, release artifacts, security docs, and CI packaging scripts.

Required work: decide which artifacts are logged; add signing/logging hooks; verify inclusion proofs where practical; keep local/offline test fixtures deterministic; document dependency on external transparency service availability.

Acceptance: selected attestations can be published to or verified against a transparency log; tests cover local verification or mocked Rekor responses; docs explain operational use.

Verification: run security/attestation tests and the default test command.

Final response: summarize logged artifacts and offline behavior.

### Implementation Status

Completed in this repository as deterministic Sigstore/Rekor-style transparency scaffolding, not external Rekor publication.

Implementation evidence:

- `src/cap_protocol/security/transparency.py` adds `LocalRekorTransparencyLog`, release and AuthorityChainStep DSSE/in-toto attestation helpers, Rekor-compatible bundles, signed entry timestamps, Merkle inclusion proofs, and offline bundle verification.
- `tests/test_transparency_log.py` covers release attestation bundle verification, AuthorityChainStep attestation bundle verification, raw-content minimization metadata, inclusion-proof tamper detection, and signed-entry-timestamp failure.
- `src/cap_protocol/cli/run_hardening.py` logs release and AuthorityChainStep attestations into the local transparency log and records offline verification in the production-hardening report.
- `src/cap_protocol/conformance/v1_runner.py` adds V1-C15 transparency checks for release bundles, AuthorityChainStep bundles, and inclusion-proof tamper detection.
- Docs now explain that local tests do not require external Rekor availability.

Logged artifacts:

- Release attestations for package or verification artifacts.
- AuthorityChainStep attestations for signed authority-step digests.

Remaining production gaps:

- External Sigstore/Rekor publication and availability handling.
- Log monitoring and consistency verification.
- Production key custody for attestation and log signing.
- Release-blocking policy for missing transparency inclusion.
- Cross-organization transparency interoperability evidence.

## Source: `docs/task_prompts/cap_v1/Done/P2-T17_implement_live_mcp_and_a2a_substrate_interop.md`

## Task Prompt: P2-T17 Implement Live MCP And A2A Substrate Interop

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T17`.

Objective: replace metadata-only substrate demos with live MCP server and A2A message interop through CAP enforcement paths.

Inspect: `docs/CAP_05_integrations.md`, MCP constrained-invocation demo, A2A metadata demo, Edge PEP, Capability Registry, Tool Registry, and binding examples.

Required work: route MCP tools/call and resources/read through Edge PEP; wrap A2A messages with CAPEnvelope; advertise CAP support in AgentCard extension; test forbidden tool refusal, constrained invocation, evidence refs, and cross-boundary envelope validation.

Acceptance: at least one live MCP server path and one live A2A message path run through CAP checks; metadata-only demos are no longer the only evidence.

Verification: run MCP/A2A integration tests and the default test command.

Final response: summarize live substrate coverage and any external interoperability gap.

### Implementation Status

Completed as deterministic live local substrate interop scaffold.

Evidence:

- `src/cap_protocol/runtime/substrate_interop.py` adds `LiveMCPServer`, `LiveA2AAgent`, and `run_live_substrate_interop_sample`.
- MCP `tools/call` and `resources/read` requests now use signed CAPEnvelope `Directive` payloads and pass through Edge PEP signature, SPIFFE, PolicyRef, PrivacyBoundary, and AuthorityChain checks before handlers run.
- MCP descriptors are discovered from service-backed `Capability` records; forbidden tools are refused before handler side effects; successful calls emit `ExecutionReport` objects with EvidenceRefs.
- A2A messages now carry an `application/cap-envelope+json` part, with the CAPEnvelope wrapping the A2A message payload. The receiving A2A peer validates the envelope through Edge PEP before delivery and advertises CAP v1 support in its AgentCard extension.
- `tests/test_live_substrate_interop.py` covers allowed MCP tool invocation, MCP resource read with EvidenceRefs, forbidden-tool refusal before side effects, CAP-advertising AgentCard, CAPEnvelope-wrapped A2A delivery, and tampered cross-boundary A2A envelope refusal.
- `src/cap_protocol/conformance/v1_runner.py` adds release-blocking scaffold checks for the live local MCP/A2A substrate paths under V1-C14.

Remaining production gaps:

- No external MCP server, external A2A network, or multi-organization interoperability run is included.
- Production service authentication, network registry deployment, HA registry behavior, operational monitoring, KMS/HSM custody, and organization-owned substrate rollout remain external gates.

## Source: `docs/task_prompts/cap_v1/Done/P2-T18_split_controller_into_distinct_deployable.md`

## Task Prompt: P2-T18 Split Controller Into Distinct Deployable

### Implementation Status

Completed as a decomposed v1 Controller reference service boundary.

Evidence:

- `src/cap_protocol/runtime/controller.py` adds `ControllerService`, `ControllerIntent`, `LocalControllerClient`, `HTTPControllerClient`, `PDPGuardEvaluator`, and `ScriptedGuardEvaluator`.
- The Controller service owns intent formation/orchestration and signed `Directive` CAPEnvelope construction, while policy evaluation is delegated to a Guard/PDP interface, routing is delegated to `SessionRouter`, and audit/telemetry/provenance is delegated to optional `ObservabilityPlane` sinks.
- `legacy_center_compatibility_report()` preserves the combined gRPC `CAPCenter` path as explicit v0.1 legacy compatibility instead of making it the v1 default.
- `tests/test_controller_service.py` covers Guard substitution, PDP-backed Guard evaluation, plain versus signed audit sink substitution, telemetry failure isolation, HTTP/JSON service boundary behavior, operation without an observer sink, and no raw payload storage in Controller/Router audit metadata.
- `src/cap_protocol/conformance/v1_runner.py` adds V1-C12 checks for Controller boundary separation, Guard substitution, audit substitution, no-observer operation, and legacy Center compatibility.

Remaining production gaps:

- This is a reference service, not production deployment certification.
- Production service authentication, discovery, HA orchestration state, durable intent state, production Guard/PDP clients, deployed router/observer wiring, operational monitoring, and organization-owned rollout policy remain external deployment work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T18`.

Objective: separate the v1 Controller role from the combined v0.1 Center/Guard/Observer implementation.

Inspect: control-plane docs, v0.1 Center code, Guard/PDP code, Observer/audit code, Supervisor Gateway, Session Router, and binding demos.

Required work: define Controller responsibilities as intent formation and orchestration; move policy evaluation to PDP/Guard paths, routing to Session Router, and observability to sinks; provide a deployable process or service boundary; preserve v0.1 compatibility as a legacy mode.

Acceptance: v1 runtime can run Controller independently from Guard and Observer responsibilities; tests prove policy and audit can be substituted independently.

Verification: run control-plane integration tests and the default test command.

Final response: summarize component boundaries and legacy compatibility.

### Phase 3 Prompts: Streaming, Trust Modes, Profiles, And Evaluation

## Source: `docs/task_prompts/cap_v1/Done/P2-T1_deploy_capability_registry_service.md`

## Task Prompt: P2-T1 Deploy Capability Registry Service

### Implementation Status

Completed as a local reference-service implementation, not as a production network deployment.

Executable evidence:

- `src/cap_protocol/runtime/registry.py`
- `src/cap_protocol/runtime/authority.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `tests/test_capability_registry_service.py`
- `tests/test_federated_registry.py`
- `tests/test_authority_chain.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_RELEASE_GATES.md`

Covered behavior:

- SQLite-backed reference service persists registry records, revocation state, warrant-key directory entries, and audit events.
- `CapabilityRegistry` clients preserve cache hit/miss semantics while checking service-backed live revocation freshness before using cached metadata.
- trust-domain federation hooks can delegate lookups and propagate revocation markers.
- `ServiceBackedKeyRegistry` resolves Ed25519 warrant keys for AuthorityChain verification.
- tests cover persisted capability lookup, live cached-capability revocation, federated lookup/propagation, key rotation, and revoked AuthorityChain refs.

Updated by P2-T6: production warrant primitive integration now has Biscuit reference coverage. Remaining production gaps: this is not a production registry deployment. Production deployments still need network service packaging, service authentication, high-availability replication, signed distribution, operational monitoring, organization rollout controls, deployed revocation operations, and KMS/HSM key custody.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T1`.

Objective: replace deterministic Capability Registry stubs with a service interface and reference implementation suitable for warrant-key directory and revocation propagation.

Inspect: registry stubs, `Capability` schema, authority-chain verifier, revocation tests, runtime config, docs, and release gates.

Required work: design service API, persistence model, cache/freshness behavior, trust-domain federation hooks, audit events, key lookup, revocation status, and rotation tests; keep KMS/HSM production custody as an external deployment dependency if not available locally.

Acceptance: runtime can perform live revocation freshness checks against the service; key rotation and revoked capability tests pass; local stub remains only as a test fixture.

Verification: run registry/authority tests and the default test command.

Final response: summarize service behavior, deployment assumptions, and remaining KMS/HSM gap.

## Source: `docs/task_prompts/cap_v1/Done/P2-T2_deploy_policy_registry_and_signed_bundle_distribution.md`

## Task Prompt: P2-T2 Deploy Policy Registry And Signed Bundle Distribution

### Implementation Status

Completed as a local reference-service implementation, not as a production network deployment.

Executable evidence:

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `tests/test_policy_registry_service.py`
- `tests/test_cap_v1_pep.py`
- `tests/test_policy_hot_update.py`
- `docs/CAP_RELEASE_GATES.md`

Covered behavior:

- `ReferencePolicyRegistryService` persists signed policy bundles, session pins, revocation state, and audit events.
- Local PEP can fetch verified signed bundles from the service when the Control Plane is reachable.
- sessions pin bundle version/digest by default; explicit hot-update mode rotates the pin.
- revoked, expired, mismatched, malformed, or tampered bundles fail closed.
- emergency override bundles are audited and still require valid signature, digest, and expiry.
- offline fallback continues from the verified `OfflinePolicyBundleCache` and allows only profile-safe local support.

Remaining production gaps: this is not a production Policy Registry deployment. Production deployments still need network service packaging, service authentication, high-availability replication, operational monitoring, organization rollout controls, and KMS/HSM signing custody.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T2`.

Objective: implement Policy Registry service behavior for signed policy-bundle distribution, version pinning, rotation, revocation freshness, emergency override, and offline cache validation.

Inspect: offline policy bundle cache, policy refs, OPA adapter, Local PEP, Edge PEP, registry stubs, policy drift tests, and docs.

Required work: add API and reference service for policy bundle fetch; enforce digest/version/expiry; support per-session pinning and documented hot-update behavior; integrate signed bundle verification; model emergency override with audit evidence.

Acceptance: Local PEP fetches bundles from a service in integration tests; offline cache validates signed bundles; stale or mismatched bundles fail closed; docs state operational limits.

Verification: run policy cache/registry/PDP tests and the default test command.

Final response: summarize policy distribution and hot-update semantics.

## Source: `docs/task_prompts/cap_v1/Done/P2-T3_deploy_agent_and_tool_registry_services.md`

## Task Prompt: P2-T3 Deploy Agent And Tool Registry Services

Completed as service-backed Agent/Tool discovery for the deterministic v1 demos.

Implementation evidence:

- `src/cap_protocol/runtime/registry.py`
- `src/cap_protocol/bindings/http_json/integrations_v1.py`
- `src/cap_protocol/bindings/http_json/run_demo.py`
- `src/cap_protocol/bindings/grpc_reference/registry_discovery.py`
- `src/cap_protocol/bindings/grpc_reference/mcp_adapter.py`
- `src/cap_protocol/bindings/grpc_reference/a2a_adapter.py`
- `src/cap_protocol/bindings/grpc_reference/center_server.py`
- `tests/test_agent_tool_registry_service.py`
- `tests/test_http_binding.py`
- `tests/test_grpc_reference_v1_binding.py`
- `src/cap_protocol/conformance/v1_runner.py`

Status:

- `AgentToolDiscoveryService` provides service-backed `register_agent`, `register_tool`, `discover_agent`, `discover_tool`, `agent_card`, and `mcp_tool_descriptor` APIs with trust-domain and expected version/digest checks.
- Agent and Tool registrations remain closed CAP `Capability` objects; A2A AgentCard metadata and MCP tool descriptors are carried under `Capability.profile_extensions`.
- The HTTP/JSON and gRPC reference demos register deterministic A2A/MCP records into the service and discover them at runtime instead of relying only on local constants.
- Cache miss/fill, cache hit, stale metadata, unknown registration, revoked registration, and trust-domain mismatch paths are covered by tests and conformance metadata.

Remaining production gaps: this is still an in-process SQLite reference service and deterministic demo wiring. Production deployment still needs network service packaging, service authentication, HA replication, operational monitoring, organization rollout controls, and live multi-organization MCP/A2A interoperability evidence.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T3`.

Objective: turn Agent and Tool Registry stubs into service-backed discovery for cross-host demos.

Inspect: registry stubs, capability schema, A2A metadata, MCP tool metadata, binding demos, and docs.

Required work: implement API surfaces for registration, lookup, freshness, trust domain, and cache behavior; load demo registrations from the services instead of local files; preserve deterministic test fixtures; add stale/unknown/revoked registration tests.

Acceptance: demos discover agents and tools through services; registry cache hit/miss and stale metadata paths are tested; `Capability.profile_extensions` carries substrate-specific metadata.

Verification: run registry and demo tests, then the default test command.

Final response: summarize service APIs and demo wiring.

## Source: `docs/task_prompts/cap_v1/Done/P2-T4_deploy_evidence_registry.md`

## Task Prompt: P2-T4 Deploy Evidence Registry

Completed as a service-backed Evidence Registry reference implementation with content-addressed storage.

Implementation evidence:

- `src/cap_protocol/runtime/registry.py`
- `src/cap_protocol/runtime/edge_pep.py`
- `tests/test_evidence_registry_service.py`
- `tests/test_federated_registry.py`
- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_06_conformance.md`

Status:

- `ReferenceCapabilityRegistryService.put_evidence`, `get_evidence`, `verify_evidence_ref`, and `evidence_payload_resolver` provide content-addressed Evidence storage and lookup.
- Evidence storage computes `sha256:` content URIs, stores media type and size, publishes matching Evidence Registry metadata, and attaches reference attestation and provenance metadata to `EvidenceRef.attestation_ref` and `EvidenceRef.provenance_ref`.
- Evidence verification checks registry metadata freshness, content presence, and re-hashes stored bytes before returning decoded content.
- Edge PEP accepts typed Evidence dereference results from the registry resolver after signature/time/policy/authority/privacy-boundary checks and refuses missing or tampered evidence without logging raw content.
- Tests cover put/get/verify, missing content, storage tamper, Edge PEP privacy-before-dereference ordering, hash-mismatch refusal, and provenance projection for evidence storage events.

Remaining production gaps: this is an in-process SQLite reference service. Production use still needs network service packaging, service authentication, access-policy enforcement, retention/deletion controls, production attestation signing, HA replication, operational monitoring, and external deployment evidence.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T4`.

Objective: implement a service-backed Evidence Registry with content-addressed storage and attestation.

Inspect: `EvidenceRef` schema, evidence hash mismatch tests, audit/provenance sinks, registry stubs, execution reports, and docs.

Required work: add content-addressed put/get/verify operations; store hashes and media types; attach attestation metadata; integrate EvidenceRef dereference through Edge PEP privacy-before-dereference checks; add tamper and missing evidence tests.

Acceptance: V1 evidence conformance passes against the registry; hash mismatch refuses use; provenance can link evidence storage events.

Verification: run evidence/registry/provenance tests and the default test command.

Final response: summarize storage and verification behavior.

## Source: `docs/task_prompts/cap_v1/Done/P2-T5_implement_cedar_pdp_adapter.md`

## Task Prompt: P2-T5 Implement Cedar PDP Adapter

Completed as a deterministic Cedar PDP adapter scaffold behind the same CAP PDP interface as the OPA-shaped adapter.

Implementation evidence:

- `src/cap_protocol/runtime/pdp_adapters.py`
- `src/cap_protocol/runtime/__init__.py`
- `src/cap_protocol/bindings/grpc_reference/policy_adapter.py`
- `src/cap_protocol/bindings/http_json/integrations_v1.py`
- `tests/test_pdp_adapters.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_05_integrations.md`
- `docs/CAP_06_conformance.md`
- `docs/CAP_RELEASE_GATES.md`

Status:

- `CAPPolicyRequest`, `PDPDecision`, and `PDPAdapter` define the shared CAP-facing adapter interface.
- `OPAPolicyAdapter` and `CedarPolicyAdapter` evaluate the same deterministic scaffold policy rules for allow, deny, privacy-deny, and human-review decisions.
- Cedar request mapping is explicit: CAP subject maps to Cedar principal, action operation/kind maps to Cedar action, action target/resource maps to Cedar resource, and normalized constraints/evidence/policy refs map to Cedar context.
- gRPC and HTTP/JSON policy-guard adapters can select the Cedar adapter while preserving existing OPA defaults.
- Tests cover OPA/Cedar parity for conformance fixture decisions, Cedar mapping, guard-adapter wiring, unsupported engine refusal, and explicit fail-closed behavior when an external Cedar runtime is required but unavailable.

Remaining production gaps: this is a deterministic in-process scaffold. Production use still needs organization-owned Cedar policies, external Cedar runtime invocation, service deployment, rollout/rollback/change control, and profile-owner governance.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_pdp_adapters.py tests/test_conformance.py -q
## 12 passed, 1 skipped

source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
## 180 passed, 1 skipped
```

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T5`.

Objective: add a Cedar PDP adapter to demonstrate policy-engine portability alongside the existing OPA-style adapter.

Inspect: PDP adapter interfaces, OPA-style adapter, policy tests, structured PrivacyBoundary evaluation, docs mapping OPA/Cedar, and dependency constraints.

Required work: implement Cedar adapter behind the same interface; support equivalent decisions for the conformance fixtures; document how Cedar policies map to CAP subject/action/resource/context; skip or mark tests if Cedar runtime dependency is unavailable, but keep the interface explicit.

Acceptance: the same policy conformance suite passes with Cedar and OPA where both are available; docs state parity and limitations.

Verification: run PDP adapter tests and the default test command.

Final response: summarize adapter parity and any optional dependency requirement.

## Source: `docs/task_prompts/cap_v1/Done/P2-T6_integrate_biscuit_or_tenuo_warrant_primitive.md`

## Task Prompt: P2-T6 Integrate Biscuit Or Tenuo Warrant Primitive

Completed as a Biscuit-backed AuthorityChainStep warrant reference integration.

Primitive choice:

- Chosen primitive: Biscuit, via `biscuit-python`.
- Rationale: Biscuit is purpose-built for offline-verifiable, attenuating capability tokens with caveats. It fits CAP authority chains better than a generic signature envelope because the token itself can bind holder identity, requested capability, and requested scope before the CAP verifier applies expiry, policy-ref, revocation, and cross-step attenuation checks.

Implementation evidence:

- `pyproject.toml`
- `src/cap_protocol/runtime/warrants.py`
- `src/cap_protocol/runtime/authority.py`
- `src/cap_protocol/runtime/__init__.py`
- `schemas/domains/authority.yaml`
- `schemas/cap-core/v1/authority-chain.schema.json`
- `examples/cap-core/v1/authority-chain.json`
- `tests/test_warrant_primitives.py`
- `tests/test_authority_chain.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_06_conformance.md`

Status:

- `warrant_format=biscuit-v2` AuthorityChain steps carry a `warrant_token` object with the Biscuit token, root key id, signed CAP-claims hash, canonicalization, and payload type.
- `encode_biscuit_authority_step` signs canonical CAP AuthorityChainStep claims into a holder-bound Biscuit token.
- `verify_biscuit_authority_step` decodes the token, enforces runtime holder/capability/scope caveats, verifies the signed claims hash, and returns canonical step claims to `verify_authority_chain`.
- `verify_authority_chain` preserves detached-JWS compatibility while adding Biscuit warrant verification, policy-ref shape checks, scope attenuation, previous-step hash checks, expiry/skew checks, and live registry-backed revocation freshness.
- Tests cover authority-step round-trip, captured-token wrong-holder refusal, scope-expansion refusal, policy-ref shape verification, service-backed warrant-key lookup, key rotation, and registry-backed live revocation refusal.

Remaining production gaps: this is reference integration evidence, not production deployment certification. Production use still needs KMS/HSM signing custody, service authentication, deployed revocation services, HA replication, operational monitoring, and external interoperability evidence for selected warrant profiles.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_authority_chain.py tests/test_warrant_primitives.py tests/test_conformance.py tests/test_cap_v1_linkml.py tests/test_cap_v1_schemas.py -q
## 46 passed

source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
## 185 passed, 1 skipped
```

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T6`.

Objective: integrate a production-grade attenuating capability warrant primitive, preferably Biscuit or Tenuo, for v1 authority chains.

Inspect: authority-chain schema and verifier, capability registry service, signing helpers, SPIFFE/OIDC identity hooks, revocation tests, and docs.

Required work: choose a primitive with clear rationale; encode/decode `AuthorityChainStep` into the warrant; enforce holder binding against runtime identity; verify attenuating caveats, expiry, scope subset, policy refs, and revocation freshness; preserve deterministic detached-JWS tests as compatibility/scaffold coverage.

Acceptance: authority steps round-trip through the warrant primitive; captured tokens are refused for the wrong holder; scope expansion is impossible; revocation freshness is checked through registry integration.

Verification: run authority/warrant/security tests and the default test command.

Final response: summarize primitive choice, holder binding, and revocation behavior.

## Source: `docs/task_prompts/cap_v1/Done/P2-T7_integrate_spiffe_spire_workload_identity.md`

## Task Prompt: P2-T7 Integrate SPIFFE/SPIRE Workload Identity

Status: Completed as deterministic SPIFFE/SVID workload-identity scaffold and selected runtime wiring. `cap_protocol.runtime.workload_identity` parses normalized SPIFFE IDs and mounted X.509 SVIDs, Edge PEP can require SPIFFE sender/receiver/runtime identities, AuthorityChain and Biscuit-backed warrant verification reject missing or mismatched SPIFFE SVID holder bindings, and the gRPC/HTTP demos report SPIFFE SVIDs as primary CAP v1 workload identity.

Remaining production gaps: this is not a production SPIRE deployment or service-mesh integration. Runtime-generated gRPC mTLS certificates remain a non-production localhost transport fallback. Production use still needs SPIRE Workload API or service-mesh SVID sourcing, service authentication, registry/key infrastructure, KMS/HSM signing custody, deployed revocation operations, and external interoperability evidence.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P2-T7`.

Objective: integrate SPIFFE/SPIRE workload identity for demos and PEP verification paths.

Inspect: mTLS certificate generation, identity-binding code, Edge PEP, AuthorityChain verifier, service mesh docs, and runtime config.

Required work: consume SPIFFE SVIDs for workload identity; validate identity bindings in envelope and warrant verification; retire runtime-generated certs from the primary v1 path while keeping them as a local fallback; add docs and tests for missing or mismatched SVID.

Acceptance: demos can use SPIFFE SVIDs; identity-binding tests refuse mismatches; fallback cert behavior is clearly labeled non-production.

Verification: run identity/security tests and any SPIFFE integration tests available.

Final response: summarize SPIFFE wiring and fallback behavior.

## Source: `docs/task_prompts/cap_v1/Done/P2-T8_deploy_supervisor_gateway_service.md`

## Task Prompt: P2-T8 Deploy Supervisor Gateway Service

Completed as a CAP-facing Supervisor Gateway reference service boundary.

Implementation evidence:

- `src/cap_protocol/runtime/supervisor_gateway.py`
- `tests/test_supervisor_gateway_service.py`
- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_v1_TASKS.md`

What changed:

- added `SupervisorGatewayService` as the service boundary above the existing gateway enforcement core;
- added `HTTPSupervisorGatewayClient`, `LocalSupervisorGatewayClient`, and a standard-library HTTP/JSON reference service endpoint at `/cap/v1/supervisor/consultations`;
- added model, human-portal, and rule-engine backend adapters behind the same `SupervisorBackend` contract;
- routed v1 conformance Supervisor Gateway checks through the service contract instead of directly calling translation methods;
- preserved Local PEP minimization before backend access, raw-context refusal, AuthorityChain verification, policy/privacy/safety vetoes, and structured Directive/InterruptDecision translation;
- added audit and provenance references for each service consultation without logging raw content.

Remaining production gaps:

- this is a reference service and local HTTP/JSON deployable scaffold, not production certification;
- production service authentication, service discovery, scaling, operational monitoring, production KMS/HSM custody, production Policy/PDP rollout, organization-owned backend integrations, and external interoperability evidence remain future deployment work.

### Original Prompt

Objective: turn the deterministic Supervisor Gateway stub into a deployable CAP-facing service with real backend integration points.

Inspect: Supervisor Gateway stub, Local PEP veto logic, structured strategy-to-Directive translation, authority checks, privacy filters, CAP-Med examples, and docs.

Required work: define service API; route supervisor consultations through the service; support backend model, human portal stub, and rule-engine stub behind the same gateway; enforce redacted context and raw-data vetoes; integrate policy and authority verification; emit audit/provenance.

Acceptance: supervisor consultation goes through the service, not an in-process stub; unsafe supervisor output is vetoed; backend type is hidden behind the gateway contract.

Verification: run supervisor gateway tests, integration tests, and the default test command.

Final response: summarize service boundary and backend integration status.

## Source: `docs/task_prompts/cap_v1/Done/P2-T9_implement_session_router.md`

## Task Prompt: P2-T9 Implement Session Router

Completed as a CAP v1 Session Router reference component.

Implementation evidence:

- `src/cap_protocol/runtime/session_router.py`
- `tests/test_session_router.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/api.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_v1_TASKS.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`

What changed:

- added `SessionRouter` with per-session active participant registration;
- added sender/receiver membership checks before CAPEnvelope-like control-message delivery;
- added atomic same-session fanout and batch route helpers;
- added cross-session receiver refusal with typed `RefusalMessage` output;
- added route-history and audit/provenance metadata that records envelope ids, participants, payload refs, and payload presence without storing raw `payload` bodies;
- added v1 conformance smoke checks for session binding, cross-session refusal, same-session fanout, and raw-payload non-ownership.

Remaining production gaps:

- this is a reference component, not production certification;
- production service deployment, authentication, HA state management, queueing/backpressure, live Control Plane integration, operational monitoring, and external interoperability evidence remain future work.

### Original Prompt

Objective: implement the decomposed Control Plane Session Router.

Inspect: control-plane docs, session IDs in CAPEnvelope, binding flow, Supervisor Gateway, Interrupt Manager, registry stubs, and audit/provenance sinks.

Required work: track active session participants, route control messages without owning raw session content, enforce receiver/session binding, handle multi-session fanout safely, and emit routing audit events.

Acceptance: multi-session demo routes correctly; cross-session delivery attempts are refused; raw session payloads remain outside router ownership.

Verification: run session-routing tests and the default test command.

Final response: summarize routing model and privacy boundary.

## Source: `docs/task_prompts/cap_v1/Done/P3-T10_build_cap_swe_non_medical_reference_profile.md`

## Task Prompt: P3-T10 Build CAP-SWE Non-Medical Reference Profile

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T10`.

Objective: implement a non-medical CAP-SWE reference profile to defend CAP's generality claim.

Inspect: `docs/CAP_07_profiles_roadmap.md`, profile extension rules, CAP-Med examples, v1 Core schemas, conformance runner, and current developer tooling.

Required work: define CAP-SWE constraints for software engineering agents: diff evidence, sandbox constraints, test-result evidence, file-write authority, rollback/commit compensation, tool risk levels, and human escalation; add examples and conformance fixtures; keep all Core objects unchanged.

Acceptance: same Core plus different profile passes relevant conformance; docs explain how CAP-SWE differs from CAP-Med; generality claim has executable evidence.

Verification: run profile/conformance tests and the default test command.

Final response: summarize profile scope and examples.

### Implementation Status

Completed in this repository:

- Added `cap_protocol.profiles.cap_swe` with a deterministic CAP-SWE reference fixture using unchanged CAP Core v1 objects for `PrivacyBoundary`, `OperationalConstraints`, `EvidenceRef`, `Capability`, `Directive`, and `InterruptDecision`.
- Added CAP-SWE profile-owned constraints under `profile_constraints.cap-swe/v1` and `profile_extensions.cap-swe/v1` for diff evidence, test-result evidence, sandbox attestation, file-write authority, rollback/commit compensation, tool-risk levels, and code-owner escalation.
- Added `SoftwareEngineeringAgentProfile` to `schemas/domains/profiles.yaml` as a non-Core LinkML profile contract.
- Added `tests/test_cap_swe_profile.py` and V1-C05 conformance checks proving the same Core objects validate with CAP-SWE profile data and that production secrets remain local-only while minimized diff/test/evidence metadata may cross to authorized reviewers.
- Updated docs, release gates, examples, claims, and prompt indexes to describe CAP-SWE as deterministic generality evidence, not production SWE-agent certification.

Remaining production gaps: production SWE-agent sandboxing, real CI/repository integrations, external profile owners, cross-implementation profile conformance, and deployed policy/registry/PEP operations remain outside this deterministic reference profile.

## Source: `docs/task_prompts/cap_v1/Done/P3-T11_benchmark_latency_and_mobile_resource_budget.md`

## Task Prompt: P3-T11 Benchmark Latency And Mobile Resource Budget

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T11`.

Objective: measure CAP overhead versus direct execution, including Local PEP latency, streaming buffer overhead, and mobile/edge CPU, memory, and battery proxies.

Inspect: benchmark harnesses if any, binding demos, Local PEP, Edge PEP, streaming gate, release gates, and docs.

Required work: add reproducible benchmarks; measure direct MCP/tool path versus CAP-mediated path; report p50/p95 latency; measure streaming delay and resource usage; document hardware and environment; avoid overclaiming from local-only results.

Acceptance: benchmark numbers are published in docs or generated artifacts; tests verify benchmark harness runs; release gates link to results.

Verification: run benchmark command and the default test command.

Final response: summarize results and caveats.

### Implementation Status

Status: complete for local deterministic benchmark evidence.

Implemented:

- `cap_protocol.benchmarks` now provides a dependency-free CAP v1 microbenchmark harness for direct MCP tool handling, CAP-mediated MCP `tools/call`, Edge PEP envelope verification, direct user-output emission, Local PEP user-output gating, direct stream concatenation, Local PEP live-stream gating, and Android/iOS mobile proxy scaffold user-output paths.
- `cap-run-v1-benchmarks` writes reproducible JSON and Markdown artifacts under `docs/benchmarks/`, including p50/p95 latency, CPU-time per 1000 operations, tracemalloc peak memory, streaming delay, and explicit battery-proxy caveats.
- `docs/benchmarks/cap_v1_latency_mobile_budget.md` and `.json` publish the latest local run from this checkout with environment metadata.
- `tests/test_benchmark_harness.py` verifies the harness, artifact writer, and CLI output path.

Remaining production/external gaps:

- The artifact is a local Python microbenchmark, not native Android/iOS device telemetry, production model-provider latency, service-mesh latency, networked registry/PDP latency, measured battery drain, or production deployment certification.

## Source: `docs/task_prompts/cap_v1/Done/P3-T12_build_third_implementation_interop.md`

## Task Prompt: P3-T12 Build Third Implementation Interop

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T12`.

Objective: add a minimal third implementation or external adapter, preferably Rust or Go, that passes the v1 conformance suite.

Inspect: conformance fixtures, JSON Schemas, signing/canonicalization rules, envelope examples, and binding docs.

Required work: choose language/runtime; implement CAPEnvelope validation, JCS signing verification, basic payload handling, and conformance fixture runner; keep scope minimal; document build/run commands.

Acceptance: three independent implementations or runtime shapes can pass shared v1 conformance; failures are traceable to fixture IDs.

Verification: run third-implementation conformance command and Python default tests.

Final response: summarize language choice and conformance status.

### Implementation Status

Completed as local third implementation interoperability evidence.

Implemented:

- Added `third_impl/go_cap_adapter/`, a standard-library Go adapter that validates signed CAP v1 `CAPEnvelope` fixtures.
- The adapter verifies RFC 8785/JCS detached Ed25519 signatures on envelopes and signed payloads, checks required CAPEnvelope fields, validates timestamp/TTL expiry, and performs basic payload handling for supported v1 message kinds.
- Added `third_impl/go_cap_adapter/testdata/cap_v1_interop.json` as the shared third-implementation fixture suite with valid, tampered, missing-field, and expired-envelope cases.
- Added `tests/test_go_interop_adapter.py` to run the Go adapter from pytest, assert the static suite passes, and verify unexpected failures remain traceable to fixture IDs.
- Documented build/run commands in `third_impl/go_cap_adapter/README.md`.

Verification command:

```bash
cd third_impl/go_cap_adapter
go run . --fixtures testdata/cap_v1_interop.json --json
```

Remaining production gaps:

- This is a local third implementation shape, not a production CAP runtime.
- It does not implement gRPC/HTTP services, registries, Local PEP, Edge PEP, PDPs, policy distribution, or key custody.
- External multi-organization MCP/A2A interoperability and third-party certification remain separate Phase 4 gates.

## Source: `docs/task_prompts/cap_v1/Done/P3-T13_formalize_lifecycle_fsm_and_profile_inheritance.md`

## Task Prompt: P3-T13 Formalize Lifecycle FSM And Profile Inheritance

### Implementation Status

Completed in this repository. `cap_protocol.runtime.lifecycle` defines machine-checkable lifecycle FSMs for envelope, directive, interrupt, execution, evidence, audit, and provenance domains. `cap_protocol.profiles.inheritance` defines deterministic parent-before-child profile composition, monotonic narrowing, conflict refusal for widening overrides, risk-level strictness, and Core lifecycle/interrupt override refusal. `tests/test_lifecycle_profile_inheritance.py` covers illegal transitions and profile conflict resolution, and the V1-C05/V1-C15 conformance gate now calls the lifecycle/profile checks.

Remaining production work: external profile-owner governance, cross-implementation profile conformance, and deployed runtime enforcement remain outside this deterministic scaffold task.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T13`.

Objective: formalize CAP lifecycle state transitions and profile inheritance rules.

Inspect: `docs/CAP_06_conformance.md`, `docs/CAP_07_profiles_roadmap.md`, Core object docs, conformance runner, CAP-Med and CAP-SWE profile work.

Required work: define a machine-checkable lifecycle FSM for envelope, directive, interrupt, execution, evidence, audit, and provenance states; define profile inheritance and override rules; add validation tests for illegal transitions and profile conflict resolution.

Acceptance: conformance can validate lifecycle and profile inheritance; multi-profile composition behavior is deterministic; docs no longer rely on informal prose only.

Verification: run lifecycle/profile tests and the default test command.

Final response: summarize FSM states and inheritance rules.

## Source: `docs/task_prompts/cap_v1/Done/P3-T14_migrate_cap_med_v1_profile_end_to_end.md`

## Task Prompt: P3-T14 Migrate CAP-Med v1 Profile End To End

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T14`.

Objective: migrate CAP-Med from v0.1 executable behavior plus v1 examples to a true v1 runtime profile.

Inspect: CAP-Med docs/examples, v0.1 profile constraints, Local PEP, Supervisor Gateway, PrivacyBoundary, InterruptDecision, conformance cases, and release gates.

Required work: express CAP-Med constraints as profile extensions over v1 Core; use `CAPEnvelope`, structured PrivacyBoundary, `InterruptDecision`, unified `Capability`, and `OperationalConstraints`; keep non-diagnostic, non-prescriptive, raw-transcript minimization, and Supervisor overreach veto behavior; update examples and tests.

Acceptance: CAP-Med runs end to end on the v1 hot path; v0.1 compatibility is preserved as legacy evidence; profile conformance passes.

Verification: run CAP-Med profile tests, v1 conformance, and the default test command.

Final response: summarize migrated behavior and remaining regulated-profile review gap.

### Implementation Status

Completed in this repository:

- Added `cap_protocol.profiles.cap_med` as a CAP-Med v1 runtime-profile fixture over CAP Core v1 objects.
- Moved CAP-Med-owned runtime constraints and metadata under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1` for the profile fixture, Local PEP stream interrupts, Supervisor Gateway outputs, and Therapist scenario capability metadata.
- Added CAP-Med v1 tests and V1-C05 conformance checks for signed `CAPEnvelope` hot-path execution, structured `PrivacyBoundary`, closed `OperationalConstraints`, unified `Capability`, `Directive`, `EvidenceRef`, `InterruptDecision`, Local PEP raw-transcript minimization, and Supervisor Gateway overreach refusal.
- Preserved v0.1 CAP-Med constraints as legacy compatibility evidence.

Remaining external gap:

- Regulated CAP-Med profile review, clinical/domain semantic-quality evaluation, production Supervisor Gateway rollout, organization-owned backend integration, production Local PEP trust modes, and deployed policy/registry/audit operations remain out of scope for this deterministic scaffold.

### Phase 4 Prompts: External Gates And Evidence Packages

## Source: `docs/task_prompts/cap_v1/Done/P3-T1_integrate_live_model_streaming.md`

## Task Prompt: P3-T1 Integrate Live Model Streaming

### Implementation Status

Completed as reference live model-stream integration.

Executable evidence:

- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/live_model_streaming.py`
- `src/cap_protocol/runtime/__init__.py`
- `tests/test_live_model_streaming.py`
- `tests/test_cap_v1_pep.py`
- `src/cap_protocol/conformance/v1_runner.py`
- `docs/CAP_03_primitives.md`
- `docs/CAP_04_security_trust_evidence.md`
- `docs/CAP_06_conformance.md`
- `docs/CAP_RELEASE_GATES.md`
- `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`
- `docs/api.md`
- `docs/testing.md`
- `docs/development.md`

Covered behavior:

- `StreamingLookaheadBuffer.tick()` releases safe buffered text on the configured wall-clock window while preserving token/character lookahead behavior.
- `LiveModelStreamSession` feeds pull-based local scripted model chunks through the Local PEP before user-visible delivery.
- `OllamaModelStream` provides an optional stdlib HTTP streaming source for callers with an available Ollama service; default tests do not require Ollama.
- Unsafe CAP-Med diagnostic/treatment chunks are transformed before display using the pre-cached safe substitution and the source is aborted so later chunks are not pulled.
- Sink backpressure pauses model pulls deterministically until the user-visible sink is acknowledged.
- External abort signals propagate before source pull and produce linked `InterruptDecision`/`ExecutionReport` abort metadata.
- Emitted user-visible frames carry audit/provenance refs, source chunk hashes and lengths, lookahead metadata, and interrupt/report refs without logging raw unsafe chunks.
- V1-C03/V1-C04 conformance now cover live stream transform, wall-clock timer release, backpressure, and abort propagation.

Remaining production gaps:

- This is a reference local/optional-provider path, not production model-provider rollout.
- P3-T3/P3-T4 add CLI/WebSocket abort replacement UX, correction-frame replacement/annotation UX, and Android/iOS abort/correction contracts; shipping native SDK wrappers and browser deployment wiring remain P3 follow-up work.
- P3-T11 adds local deterministic streaming benchmark artifacts; deployed Local PEP trust modes, production observability sinks, deployment-representative latency/resource evaluation, and a durable cross-service Interrupt Manager remain external or later-phase work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T1`.

Objective: connect a live model output stream to the Local PEP sliding lookahead buffer with wall-clock timers, backpressure, and abort propagation.

Inspect: streaming scaffold, Local PEP, runtime demos, WebSocket or streaming transport code, CAP-Med transform tests, and observability sinks.

Required work: choose a local or optional remote streaming model path; feed tokens/chunks through the lookahead buffer; implement 250 ms or 50 token default, backpressure behavior, abort signal, pre-cached safe substitution, and audit/provenance links; avoid leaking unsafe partial chunks before PEP approval.

Acceptance: V1 streaming conformance passes against real model output; unsafe chunks transform before display or abort cleanly; under-load behavior is deterministic.

Verification: run streaming integration tests and the default test command.

Final response: summarize streaming source, latency behavior, and unsupported platforms.

## Source: `docs/task_prompts/cap_v1/Done/P3-T2_implement_slow_path_classifier.md`

## Task Prompt: P3-T2 Implement Slow-Path Classifier

### Implementation Status

Completed as deterministic semantic slow-path classifier integration.

Executable evidence:

- `src/cap_protocol/runtime/slow_path_classifier.py`
- `src/cap_protocol/runtime/local_pep.py`
- `src/cap_protocol/runtime/live_model_streaming.py`
- `tests/test_slow_path_classifier.py`
- `tests/test_live_model_streaming.py`
- `src/cap_protocol/conformance/v1_runner.py`

Implemented behavior:

- `SlowPathClassifier` protocol and `SemanticClassification` result type.
- `DeterministicCapMedSlowPathClassifier` for CI-safe non-regex CAP-Med diagnostic/treatment drift fixtures.
- Optional `OllamaSemanticClassifier` model-as-judge adapter using stdlib HTTP and caller-supplied local Ollama models.
- Local PEP combines fast regex and slow semantic decisions; either unsafe result transforms or corrects before further user-visible delivery.
- Streaming lookahead checks the slow path before safe-prefix, wall-clock, or final release.
- Classifier audit events store classification metadata and content hashes without raw text.

Remaining production gaps:

- Optional model-judge deployment is not enabled by default and requires organization-selected model/runtime setup.
- P3-T3/P3-T4 add CLI/WebSocket abort replacement UX, correction-frame replacement/annotation UX, and Android/iOS abort/correction contracts; P3-T11 adds local benchmark artifacts; shipping native SDK wrappers, browser deployment wiring, deployment-representative latency/resource evaluation, production provider rollout, and deployed Local PEP trust modes remain separate Phase 3 or external-gate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T2`.

Objective: add a parallel semantic slow-path classifier, such as a quantized 1B model-as-judge, beside fast regex checks.

Inspect: streaming gate, classifier interfaces, model dependency policy, CAP-Med semantic drift cases, and tests.

Required work: define classifier interface; provide local deterministic fallback for CI; integrate optional model runtime; combine fast and slow decisions safely; add subtle non-regex clinical drift fixtures.

Acceptance: semantic drift cases are intercepted; CI remains deterministic without downloading large models; docs explain optional model setup and latency tradeoffs.

Verification: run classifier/streaming tests and the default test command.

Final response: summarize classifier path and fallback behavior.

## Source: `docs/task_prompts/cap_v1/Done/P3-T3_implement_ui_abort_propagation_per_platform.md`

## Task Prompt: P3-T3 Implement UI Abort Propagation Per Platform

### Implementation Status

Completed in this repository as deterministic client-surface abort propagation scaffold:

- Added `cap_protocol.runtime.ui_abort` with per-platform abort mappings for CLI, web, Android, and iOS.
- Implemented available local CLI and WebSocket-style presentation adapters that replace the active stream region with safe text for terminal Local PEP stream decisions.
- Defined Android and iOS native `CapStreamAbort` contracts with `reasonCode`, `replacementText`, `interruptRef`, and `reportRef`; native wrappers are not present in this repository.
- Added UI abort tests covering CLI safe replacement, WebSocket replacement-before-close behavior, external stream abort UX, late correction replacement, and native contract precision.
- Added V1-C04 conformance smoke checks for CLI/WebSocket abort UX and Android/iOS contract declaration.
- Updated API, development, testing, conformance, examples, release gates, implementation-alignment docs, and prompt indexes.

Updated by P3-T4: late correction frames now have a dedicated `ui_correction` adapter with correction-specific replacement/annotation UX and Android/iOS `CapStreamCorrection` contracts. `ui_abort` remains responsible for terminal abort propagation.

Remaining production gaps: shipping native Android/iOS SDK wrappers, browser app deployment wiring, production model-provider rollout, deployment-representative latency/resource evaluation beyond the P3-T11 local benchmark artifact, deployed Local PEP trust modes, and deployed audit/provenance sinks remain separate runtime work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T3`.

Objective: define and implement abort propagation from Local PEP streaming decisions to Android, iOS, web, and CLI client surfaces.

Inspect: demos, client/UI code if any, streaming transport, protocol docs, correction-frame behavior, and CAP-Med examples.

Required work: specify per-platform abort signal mapping; implement available local clients; document unimplemented native clients with API contracts; make WebSocket close or stream abort show a safe user-visible replacement instead of raw failure.

Acceptance: CLI/web demos show clean abort UX; Android/iOS contracts are precise if native wrappers are not in repo; no unsafe partial output remains visible after abort.

Verification: run UI/client/streaming tests and any browser tests if web UI exists.

Final response: summarize each platform status.

## Source: `docs/task_prompts/cap_v1/Done/P3-T4_design_and_implement_correction_frame_ux.md`

## Task Prompt: P3-T4 Design And Implement Correction-Frame UX

### Implementation Status

Completed as correction-frame UX semantics and deterministic local client adapters.

Implemented evidence:

- Added `cap_protocol.runtime.ui_correction` with correction-frame semantics, CLI/WebSocket-style partial-region replacement plus safe annotation events, and Android/iOS `CapStreamCorrection` contracts.
- Extended Local PEP correction frames with safe notice/replacement text, display policy, correction audit refs, and an explicit `CorrectionFrame` audit event without logging unsafe original text.
- Preserved live-stream terminal correction payloads so client adapters can carry partial-emission, original-audit, correction-audit, interrupt, execution-report, and provenance refs.
- Added tests for correction UX contracts, CLI/WebSocket behavior, link preservation, and unsafe correction-copy sanitization.
- Updated V1-C04 conformance evidence and docs to distinguish abort replacement UX from correction-frame replacement/annotation UX.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_correction_frame_ux.py tests/test_ui_abort_propagation.py tests/test_live_model_streaming.py tests/test_cap_v1_pep.py tests/test_slow_path_classifier.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
cap-check-v1-conformance
```

Remaining production gaps: native Android/iOS wrappers and production browser wiring are still not checked in; production model-provider rollout, deployed audit/provenance sinks, deployment-representative latency/resource evaluation beyond the P3-T11 local benchmark artifact, and deployed Local PEP trust modes remain separate Phase 3 or external-gate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T4`.

Objective: make late correction frames user-safe and non-jarring.

Inspect: streaming correction scaffold, CAP examples, UI/client code, audit/provenance linkage, and user-facing refusal messages.

Required work: define correction-frame semantics; implement UI/client handling for replacing or annotating partially emitted content; link correction to original output and audit event; avoid exposing diagnostic or unsafe text in correction copy.

Acceptance: late correction flow is visible, safe, and test-covered; user-facing text stays non-diagnostic for CAP-Med; audit/provenance linkage is preserved.

Verification: run streaming correction and UI tests.

Final response: summarize UX behavior and supported clients.

## Source: `docs/task_prompts/cap_v1/Done/P3-T5_implement_mobile_separately_privileged_proxy_local_pep.md`

## Task Prompt: P3-T5 Implement Mobile Separately Privileged Proxy Local PEP

### Implementation Status

Completed as deterministic Android/iOS separately privileged proxy Local PEP scaffold and release-gate smoke coverage.

Implemented evidence:

- Added `cap_protocol.runtime.mobile_local_pep` with Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, route-control metadata, topology validation, Android/iOS manifest-shaped helpers, and `MobileLocalPEPProxy`.
- Added smoke checks that refuse direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts with `sidecar_bypass_attempt`.
- Preserved Local PEP mediation for safe user output and allowed local tools, and preserved Local PEP privacy refusal for mediated raw-data egress.
- Extended V1-C11 conformance evidence with Android/iOS mobile proxy contract and bypass-smoke checks.
- Updated release gates, implementation alignment, API docs, testing docs, prompt indexes, and v1 baseline archives to distinguish deterministic scaffold coverage from native device certification.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_mobile_local_pep_proxy.py tests/test_cap_v1_pep.py tests/test_conformance.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
cap-check-v1-conformance
```

Remaining production gaps: native Android/iOS project wiring, platform entitlements, physical-device or emulator instrumentation, app-store/notarization review evidence, attested isolation, and production deployment controls remain separate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T5`.

Objective: implement or scaffold a platform-native separately privileged proxy Local PEP for Android and iOS with OS-level routing enforcement.

Inspect: Local PEP, trust-mode docs, mobile deployment notes if any, bypass tests, and CAP-Med profile defaults.

Required work: provide Android Service and iOS App Extension architecture or code where repo supports it; enforce direct user output, network, raw-data egress, and local-tool routing through the proxy; add platform attack/bypass tests or reproducible manual checks; document limitations.

Acceptance: high-assurance smoke checks cannot bypass Local PEP on supported platform; unsupported platform pieces have precise implementation contracts.

Verification: run Local PEP bypass tests and platform smoke tests where available.

Final response: summarize supported platform enforcement and gaps.

## Source: `docs/task_prompts/cap_v1/Done/P3-T6_implement_attested_isolated_local_pep.md`

## Task Prompt: P3-T6 Implement Attested Isolated Local PEP

### Implementation Status

Completed as deterministic attested isolated Local PEP registration scaffold and V1-C11 conformance coverage.

Implemented evidence:

- Added `cap_protocol.runtime.attested_local_pep` with challenge/response payloads, trusted provider contracts for deterministic TEE, Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote paths, and a Control Plane registrar that publishes Local PEP capability metadata only after attestation verification.
- Added `DeterministicAttestationProvider` as a CI-safe test double using detached-JWS payload signatures; production provider contracts require provider-specific platform verifier hooks and are not accepted implicitly.
- Bound attestations to challenge ID, challenge digest, nonce, SPIFFE workload identity, Local PEP ID, Local PEP version, profile ID, trust domain, provider, and measurement.
- Added refusal coverage for missing, unknown, expired, replayed, mismatched, untrusted, debuggable, production-verifier-missing, and invalid-trust-domain attestations.
- Extended V1-C11 conformance evidence with attested registration checks for missing attestation refusal, production-verifier-missing refusal, valid registration, replay refusal, and mismatched identity refusal.
- Updated release gates, implementation alignment, security/trust evidence, API docs, testing docs, prompt indexes, and v1 baseline archives to distinguish deterministic attested-registration coverage from production hardware-backed attestation verification.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_attested_local_pep.py tests/test_mobile_local_pep_proxy.py tests/test_cap_v1_pep.py tests/test_conformance.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
cap-check-v1-conformance
```

Remaining production gaps: real Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote verifier integrations, native mobile project wiring, platform entitlements, device/instrumented tests, app-store/notarization review evidence, deployment isolation, and production operations remain separate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T6`.

Objective: implement attested isolated Local PEP registration using TEE, Secure Enclave, TPM, Play Integrity, App Attest, or equivalent hooks.

Inspect: Local PEP trust modes, Capability Registry, authority identity binding, platform attestation docs, and registration flow.

Required work: define attestation challenge/response; verify attestation before Control Plane registration; bind attestation to workload identity and Local PEP version; add refusal path for missing, expired, or mismatched attestation; provide deterministic test doubles.

Acceptance: Control Plane refuses un-attested Local PEP registration for profiles requiring attested mode; tests cover replayed and mismatched attestations.

Verification: run trust-mode/attestation tests and the default test command.

Final response: summarize attestation providers and test-double behavior.

## Source: `docs/task_prompts/cap_v1/Done/P3-T7_implement_local_ner_redaction_pipeline.md`

## Task Prompt: P3-T7 Implement Local NER Redaction Pipeline

### Implementation Status

Completed as a deterministic local NER redaction pipeline with optional local-model adapter hooks and V1-C05 conformance coverage.

Implemented evidence:

- Added `cap_protocol.runtime.redaction` with a `LocalNERRedactor` protocol, deterministic CI-safe fallback, optional caller-supplied local model adapter, recursive Supervisor-payload redaction, and audit-safe redaction summaries.
- Redacts person names, locations and street addresses, dates, email addresses, phone numbers, SSNs, medical identifiers, financial identifiers, credit-card numbers, IP addresses, and local-model organization spans into category tags such as `[PERSON]`, `[EMAIL]`, and `[MEDICAL_ID]`.
- Wired `LocalPEP.prepare_supervisor_context(...)` to substitute raw transcript/audio into local EvidenceRefs first, then run local-only redaction over redacted context/text fields before Supervisor Gateway backend access.
- Preserved `evidence_refs`, policy refs, authority refs, privacy refs, hashes, signatures, and routing metadata while adding redaction metadata that records hashes, categories, counts, local-only status, and redaction refs without raw source text.
- Added `LocalNERRedaction` audit events with field paths, category counts, hashes, `local_only=true`, and `raw_content_logged=false`.
- Extended V1-C05 conformance evidence with checks that local NER redacts Supervisor context and that redaction audit excludes raw text.
- Updated API, development, testing, conformance, release-gate, implementation-alignment, roadmap, example, prompt-index, and v1 baseline docs to distinguish deterministic local redaction coverage from production NER model quality and deployment work.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_local_ner_redaction.py tests/test_cap_v1_pep.py tests/test_supervisor_gateway_service.py tests/test_conformance.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
cap-check-v1-conformance
```

Remaining production gaps: production-selected local NER model rollout, redaction-quality evaluation datasets, native/device enforcement around the Local PEP boundary, deployed audit/provenance sinks, and organization policy ownership remain separate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T7`.

Objective: implement local NER-based redaction for context-preserving privacy before supervisor or cross-boundary egress.

Inspect: PrivacyBoundary evaluation, Supervisor Gateway, Local PEP privacy gates, examples, and tests for raw transcript minimization.

Required work: add redaction interface with deterministic CI fallback and optional model-backed NER; replace sensitive spans with category tags; preserve evidence references; enforce local-only processing; add fixtures for names, locations, dates, contact info, and medical/financial identifiers where appropriate.

Acceptance: real text inputs are redacted before supervisor context; raw data never leaves when policy forbids it; redaction events are audited.

Verification: run privacy/redaction/supervisor tests and the default test command.

Final response: summarize redaction categories and model/fallback behavior.

## Source: `docs/task_prompts/cap_v1/Done/P3-T8_implement_embedding_only_egress.md`

## Task Prompt: P3-T8 Implement Embedding-Only Egress

### Implementation Status

Completed as deterministic local text and voice embedding-only egress for Supervisor consultation, with recipient-bound PrivacyBoundary checks and V1-C05 conformance coverage.

Implemented evidence:

- Added `cap_protocol.runtime.embeddings` with `LocalTextEmbeddingEncoder` and `LocalVoiceEmbeddingEncoder` protocols, deterministic CI-safe text/voice encoder fallbacks, embedding result metadata, source hashes, embedding hashes, provenance refs, and minimization summaries.
- Wired `LocalPEP.prepare_supervisor_context(...)` to support `embedding_only` Supervisor payloads after raw EvidenceRef substitution and local redaction, projecting cross-boundary context down to embeddings, aggregate dimensions, safety flags, evidence refs, provenance refs, and minimization metadata.
- Kept raw transcript/audio source material local: the Supervisor payload excludes `raw_transcript`, `raw_audio`, and `redacted_context`; audit and egress metadata use hashes, modality, encoder ids, provenance refs, and `raw_content_logged=false` rather than raw text or audio bytes.
- Bound embedding-only egress to the Supervisor Gateway recipient identity and the active PrivacyBoundary `allowed_recipients`; untrusted recipients receive a typed `privacy_denied` refusal without raw source leakage.
- Extended the default Therapist PrivacyBoundary to allow `text_embedding` and `voice_embedding` categories while continuing to deny raw transcript/audio egress.
- Added deterministic tests for fixed text/voice vectors, Local PEP embedding-only projection, Supervisor Gateway backend minimization, and recipient-bound refusal.
- Extended V1-C05 conformance with embedding-only Supervisor-context, audit non-leakage, and recipient-binding checks.

Verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_embedding_only_egress.py tests/test_local_ner_redaction.py tests/test_supervisor_gateway_service.py tests/test_conformance.py -q
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
cap-check-v1-conformance
```

Remaining production gaps: production local embedding model selection, embedding privacy/evaluation datasets, native/device enforcement around the Local PEP boundary, deployed audit/provenance sinks, and organization policy ownership remain separate work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T8`.

Objective: implement text and voice embedding-only egress on the supervisor channel.

Inspect: PrivacyBoundary raw-egress rules, Supervisor Gateway, local media handling, evidence refs, and CAP-Med examples.

Required work: add interfaces for local text and voice encoders; ensure raw transcripts/audio remain local; send only embeddings or aggregate dimensions when policy allows; attach provenance and minimization metadata; provide deterministic test vectors for CI.

Acceptance: supervisor consultation can run with embeddings only; tests prove raw transcript/audio do not leave the Local PEP boundary; recipients are identity-bound.

Verification: run privacy/egress/supervisor tests and the default test command.

Final response: summarize encoder interfaces and raw-data guarantees.

## Source: `docs/task_prompts/cap_v1/Done/P3-T9_implement_retention_timers_and_ttl_deletion.md`

## Task Prompt: P3-T9 Implement Retention Timers And TTL Deletion

Status: Completed as deterministic `PrivacyBoundary.retention` TTL enforcement for local raw evidence and Evidence Registry backing content.

Implemented evidence:

- Added `cap_protocol.runtime.retention` helpers for raw local TTL, audit-retention TTL, expiry checks, and content-minimized deletion records.
- Extended `LocalPEP.prepare_supervisor_context(...)` so raw transcript/audio substitutions include `expires_at`, raw local TTL metadata, and local-only backing storage; `LocalPEP.collect_retention_garbage(...)` deletes expired local backing content while preserving audit records.
- Extended `ReferenceCapabilityRegistryService` so Evidence blobs persist `expires_at`, expired direct reads fail closed, retention GC deletes expired backing content, and deletion audit/provenance records exclude raw evidence.
- Added focused retention tests for expired local memory, Evidence Registry TTL deletion, resolver refusal after expiry, audit preservation, and raw-content non-leakage.
- Extended V1-C05 and V1-C10 conformance with Local PEP retention GC and Evidence Registry deletion/audit checks.

Verification completed:

- `source venv/bin/activate && python -m compileall -q src/cap_protocol/runtime/retention.py src/cap_protocol/runtime/local_pep.py src/cap_protocol/runtime/registry.py src/cap_protocol/runtime/__init__.py src/cap_protocol/conformance/v1_runner.py tests/test_retention_ttl_deletion.py`
- `source venv/bin/activate && NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_retention_ttl_deletion.py tests/test_evidence_registry_service.py tests/test_privacy_pdp.py tests/test_cap_v1_pep.py tests/test_conformance.py -q`
- `source venv/bin/activate && cap-check-v1-conformance`

Remaining production gaps: durable distributed local stores, production registry authentication/authorization, deployed retention-job scheduling, legal/organizational retention policy mapping, production audit/provenance sinks, and operational deletion review remain external deployment work.

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P3-T9`.

Objective: enforce `PrivacyBoundary.retention` through timers and garbage collection.

Inspect: privacy schema, Local PEP storage, evidence registry, audit retention docs, profile policies, and tests.

Required work: map retention policy to local data TTL; delete stale local data; preserve audit records according to audit retention policy; handle evidence references whose backing content expires; emit deletion audit/provenance events.

Acceptance: stale local data is garbage-collected per policy; deletion does not break required audit integrity; tests cover expired local memory and evidence.

Verification: run retention/privacy/evidence tests and the default test command.

Final response: summarize deletion semantics and audit-retention split.

## Source: `docs/task_prompts/cap_v1/Done/P4-T1_prepare_independent_security_review_package.md`

## Task Prompt: P4-T1 Prepare Independent Security Review Package

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T1`.

Objective: prepare an evidence package for independent third-party security review without claiming the review is complete.

Inspect: release gates, threat model, authority/signing/privacy/PEP/policy/evidence/audit docs, conformance results, and security tests.

Required work: create or update a review packet listing architecture, trust boundaries, high-risk components, test commands, open gaps, expected reviewer focus, and evidence links; add a findings tracker template.

Acceptance: external reviewers can start from the packet; docs clearly say the gate remains open until external review is complete and critical findings are resolved.

Verification: docs-only unless links/scripts are added.

Final response: summarize packet location and open gate status.

### Implementation Status

Completed in this repository:

- Added `docs/security_review/README.md` as the independent security review starting packet.
- Added `docs/security_review/findings_tracker_template.md` as the findings tracker template for external reviewers.
- Linked the packet from `README.md`, `docs/CAP_00_README.md`, `docs/CAP_RELEASE_GATES.md`, `SECURITY.md`, and the CAP v1 task index.
- Kept the independent third-party security review gate open until external review completion and critical-finding remediation.

Remaining external gap:

- Qualified external reviewers still need to perform the review, record findings, verify fixes, and confirm there are no unresolved critical findings before the gate can close.

## Source: `docs/task_prompts/cap_v1/Done/P4-T2_prepare_production_kms_hsm_operations_plan.md`

## Task Prompt: P4-T2 Prepare Production KMS/HSM Operations Plan

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T2`.

Objective: prepare deployment-facing KMS/HSM custody and operations guidance for production keys.

Inspect: signing helpers, audit signing, warrant signing, release gates, security docs, and deployment notes.

Required work: document key roles, custody, rotation, revocation, incident response, auditability, signer interfaces, and what must be supplied by a deployment organization; add config placeholders only if useful.

Acceptance: production key management responsibilities are explicit; local ephemeral keys remain labeled as non-production; no stable-release claim is made.

Verification: docs-only unless config validation changes.

Final response: summarize guidance and external owner.

### Implementation Status

Completed in this repository:

- Added `docs/kms_hsm/README.md` as the production KMS/HSM custody and operations plan.
- Added `config/kms_hsm.example.yaml` as a non-secret placeholder shape for deployment-owned configuration.
- Documented CAP key roles, custody requirements, signing request metadata, rotation, revocation, incident response, auditability, signer interfaces, and deployment evidence.
- Linked the plan from release gates, security docs, development docs, security review packet, and CAP v1 task indexes.
- Preserved local runtime keys, deterministic signing keys, and test callbacks as non-production scaffold material.

Remaining external gap:

- A deployment organization must still supply real KMS/HSM services, signer access policies, public-key discovery, revocation freshness, key ceremonies, incident runbooks, signer audit evidence, and production verification before the production KMS/HSM gate can close.

## Source: `docs/task_prompts/cap_v1/Done/P4-T3_prepare_organization_specific_opa_cedar_deployment_guide.md`

## Task Prompt: P4-T3 Prepare Organization-Specific OPA/Cedar Deployment Guide

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T3`.

Objective: prepare guidance and harnesses for organization-owned OPA/Cedar policy deployment.

Inspect: PDP adapters, Policy Registry, policy bundle cache, release gates, and CAP-Med/CAP-SWE policies.

Required work: document ownership, change control, rollout, rollback, hot updates, exception handling, test promotion, and environment separation; provide sample policy deployment layout if absent.

Acceptance: an organization can plug in real policy ownership without confusing sample policies for production policy; external gate remains open.

Verification: run policy tests if sample layouts are added.

Final response: summarize guide location and deployment assumptions.

### Implementation Status

Completed in this repository:

- Added `docs/policy_deployment/README.md` as the organization-specific OPA/Cedar deployment guide.
- Added `config/policy_deployment.example.yaml` as a non-secret placeholder for deployment-owned policy configuration.
- Added `policies/organization_template/` with non-production OPA, Cedar, bundle-manifest, and fixture-layout examples.
- Documented ownership, environment separation, change control, rollout, rollback, hot updates, emergency overrides, exception handling, test promotion, and deployment evidence.
- Linked the guide from release gates, security docs, integration docs, development docs, security review packet, and CAP v1 task indexes.
- Preserved the current OPA/Cedar adapters and sample policies as deterministic scaffolding, not production policy.

Remaining external gap:

- A deployment organization must still supply real OPA/Cedar policies, policy-owner approvals, production PDP runtimes, signed policy bundles, Policy Registry rollout/rollback evidence, hot-update controls, exception records, and monitoring before the organization-specific policy deployment gate can close.

## Source: `docs/task_prompts/cap_v1/Done/P4-T4_prepare_multi_organization_mcp_a2a_interop_plan.md`

## Task Prompt: P4-T4 Prepare Multi-Organization MCP/A2A Interop Plan

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T4`.

Objective: prepare a test plan and harness for live multi-organization MCP/A2A interoperability.

Inspect: live MCP/A2A integration work, conformance suite, registry services, CAPEnvelope signing, and release gates.

Required work: define partner setup, trust roots, registries, test fixtures, expected pass/fail cases, logging, privacy constraints, and report format; include a local simulation mode if possible.

Acceptance: partner organizations can run the plan; local simulation does not count as closing the external gate.

Verification: run local simulation or docs validation if provided.

Final response: summarize plan and what evidence is still external.

### Implementation Status

Completed in this repository:

- Added `docs/mcp_a2a_interop/README.md` as the partner-facing multi-organization MCP/A2A interop runbook.
- Added `docs/mcp_a2a_interop/report_template.md` for external evidence reports.
- Added `config/mcp_a2a_interop.example.yaml` as a non-secret planning placeholder.
- Updated release/status/development/security docs and prompt indexes to separate local simulation from external partner evidence.
- Included the interop plan in the generated V1 baseline source map.

Local verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py tests/test_go_interop_adapter.py
python scripts/check_doc_links.py
python scripts/check_claim_language.py
```

Remaining external evidence:

- At least two independent organizations still need to run the required MCP and A2A cases against live or deployment-representative endpoints.
- Partner-owned trust roots, registries, policies, warrants, EvidenceRefs, log refs, privacy review, and sign-off evidence remain required before the live multi-organization MCP/A2A gate can close.

## Source: `docs/task_prompts/cap_v1/Done/P4-T5_prepare_domain_semantic_quality_evaluation_harness.md`

## Task Prompt: P4-T5 Prepare Domain Semantic-Quality Evaluation Harness

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T5`.

Objective: prepare a domain semantic-quality evaluation harness separate from structural CAP conformance.

Inspect: CAP-Med examples, CAP-SWE profile if present, conformance docs, release gates, and paper-positioning docs.

Required work: define datasets, reviewer criteria, scoring, privacy handling, output artifacts, and separation between protocol safety and model/domain quality; add synthetic fixtures only when clearly labeled.

Acceptance: evaluation can be run by domain experts; synthetic results are not misrepresented as expert validation; structural conformance remains separate.

Verification: run harness smoke tests if implemented.

Final response: summarize harness scope and external expert dependency.

### Implementation Status

Completed in this repository:

- Added `cap_protocol.evaluation.semantic_quality` as a standard-library JSONL aggregation harness for reviewer scores, blocking flags, and synthetic/expert evidence status.
- Added synthetic onboarding fixtures under `examples/domain_semantic_quality/` for CAP-Med and CAP-SWE.
- Added `tests/test_semantic_quality_evaluation.py` to smoke-test synthetic-only labeling, blocking flags, and reviewer-depth requirements.
- Added `docs/domain_semantic_quality/README.md`, `docs/domain_semantic_quality/reviewer_rubric.md`, and `docs/domain_semantic_quality/report_template.md`.
- Added `config/domain_semantic_quality.example.yaml` as a non-secret planning placeholder.
- Updated release/status/conformance/profile/research/development docs and prompt indexes to keep semantic-quality evaluation separate from CAP structural conformance.

Local verification:

```bash
source venv/bin/activate
pytest tests/test_semantic_quality_evaluation.py
python -m cap_protocol.evaluation.semantic_quality --cases examples/domain_semantic_quality/cap_med_synthetic_cases.jsonl --scores examples/domain_semantic_quality/synthetic_reviewer_scores.jsonl
python scripts/check_doc_links.py
python scripts/check_claim_language.py
```

Remaining external evidence:

- Qualified domain experts or profile owners still need to review non-synthetic or expert-authored datasets under the documented privacy rules.
- Synthetic fixture scores are onboarding and harness smoke evidence only.
- Structural CAP conformance remains a separate gate through `cap-check-v1-conformance`.

## Source: `docs/task_prompts/cap_v1/Done/P4-T6_prepare_regulated_profile_review_packet.md`

## Task Prompt: P4-T6 Prepare Regulated-Profile Review Packet

### Common Rules

1. Work in `/Users/ali/Documents/cap_protocol`.
2. Inspect existing code and docs before editing; preserve current patterns.
3. Preserve the v0.1 production-candidate path unless this task explicitly migrates it.
4. Do not claim CAP v1 is implemented, stable, production certified, externally reviewed, or deployment ready unless the task produces that evidence and `docs/CAP_RELEASE_GATES.md` allows the claim.
5. For Python commands, run `source venv/bin/activate` first.
6. Use `NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost` for tests that touch localhost.
7. Update docs, tests, schemas, examples, conformance runners, and release gates when behavior or claim status changes.

Default verification:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

### Task

You are an implementation agent working in `/Users/ali/Documents/cap_protocol`. Complete task `P4-T6`.

Objective: prepare a review packet for CAP-Med or another regulated profile without claiming regulatory or clinical approval.

Inspect: CAP-Med profile docs, non-diagnostic boundaries, escalation paths, privacy constraints, Supervisor Gateway behavior, Human Review integration, and release gates.

Required work: collect profile constraints, forbidden behaviors, escalation rules, privacy controls, user-facing refusals, evidence examples, test results, and known limitations; include reviewer checklist and open questions.

Acceptance: domain experts can review profile behavior; docs clearly state regulated-profile review is external and still open.

Verification: docs-only unless examples/tests are added.

Final response: summarize packet location and open review status.

### Implementation Status

Completed in this repository:

- Added `docs/regulated_profile_review/README.md` as the CAP-Med-oriented regulated-profile review packet.
- Added `docs/regulated_profile_review/reviewer_checklist.md`, `docs/regulated_profile_review/open_questions.md`, and `docs/regulated_profile_review/report_template.md` for external reviewer workflow.
- Added `config/regulated_profile_review.example.yaml` as a non-secret planning placeholder.
- Updated release/status/claim/profile/security/development/research docs and prompt indexes to state that regulated-profile review is prepared but still external and open.

Local verification:

```bash
source venv/bin/activate
pytest tests/test_cap_med_v1_profile.py tests/test_supervisor_gateway_service.py tests/test_human_review_integration.py tests/test_semantic_quality_evaluation.py
python scripts/check_doc_links.py
python scripts/check_claim_language.py
```

Remaining external evidence:

- Qualified external domain experts or profile owners still need to complete the regulated-profile review.
- The packet does not establish regulatory clearance, clinical approval, or CAP-Med deployment approval.
- Structural CAP conformance, semantic-quality scoring, security review, organization policy deployment, and production infrastructure evidence remain separately tracked.
