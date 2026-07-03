# Yar and Cytoplex Spec Consolidation Plan

> ## ✅ EXECUTION STATUS — 2026-06-22 (updated)
> **All batches complete.** Batch 0 (headers + cross-links) applied to 5 specs; Batches 1-5 produced 9 specs. Verification verdict: **PASS-WITH-FIXES** (1 auto-fix, 3 flags).
> **Done-list:** Batch 0 ✅ · Batch 1 (CSP, multi-agent) ✅ · Batch 2 (physiological, speech) ✅ · Batch 3 (menstrual, social) ✅ · Batch 4 (personas-voice, edge-ai) ✅ · Batch 5 (neurobehavioral-axes) ✅
> **Open for human review:** (1) canonical CAP expansion to standardize across specs; (2) v0.2 hygiene patch to deprecate `yar.aware.call_duration_daily` in the physiological spec (already routed to the social-interaction canonical axis); (3) keep SPEC-storage-engine `draft` with open decisions until SurrealDB retest.
> Verification report: `_synthesis/SPEC_VERIFICATION_REPORT.md`.


**Owner:** Shahin Mohammadi · **Date:** 2026-06-21 · **Status:** PLANNING ONLY (no rewrites yet)
**Reading time:** ~8 min · **If you only read one thing:** Section 2 (target spec set) and Section 5 (batches).

---

## BLUF

We have 40+ spec-class docs split across Cytoplex/spec/, Cytoplex/steering/, 04-Engineering/cytoplex/, 04-Engineering/yar/sensors/, and newly written Yar/spec/. The Cytoplex core spec (01-07 series) is solid and essentially done. The Yar data-layer specs (storage engine, sync protocol, benchmark tracker, SurrealDB guide, privacy-boundary) are newly written and need only minor header harmonization. Seven domains have no spec at all and need net-new writing: personas/voice, multi-agent discovery, universal sensor (CSP), three sensor modalities, neurobehavioral axes, and edge-AI/hybrid supervisor.

---

## 1. Inventory Table

### 1a. Cytoplex Core Spec (03-Products/Cytonome/Cytoplex/spec/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| 01_foundations.md | safety-governance | CAP positioning, novelty, paper framing | solid | keep as-is |
| 02_core_model.md | safety-governance | Roles, CAPEnvelope FSM, constraint merge, runtime lanes | solid | keep as-is |
| 03_primitives.md | safety-governance | All message primitives and support structures | solid | keep as-is |
| 04_security_trust_evidence.md | safety-governance | Signing, authority chains, prompt-injection mitigation | solid | keep as-is |
| 05_integrations.md | multi-agent | CAP composition with A2A, MCP, OPA, OpenTelemetry | solid | keep as-is |
| 06_conformance.md | safety-governance | 28 core + 15 V1 conformance tests with owners | solid | keep as-is |
| 07_profiles_roadmap.md | safety-governance | Profile inheritance, extensions, roadmap, paper-readiness | solid | keep as-is |
| architecture.md | multi-agent | Three Mermaid diagrams of planes, enforcement points, control plane | solid | keep as-is |
| cap-examples.md | safety-governance | Annotated JSON for all primitives, CAP-Med and CAP-SWE scenarios | solid | keep as-is |
| appendix_schemas.md | safety-governance | JSON/LinkML schema layers with v0.1-to-v1 migration notes | draft | extend: add Yar-specific profiles once CAP-Yar profile is defined |
| claims.md | safety-governance | What v0.1 supports vs claims, paper-safe wording | reference-only | keep (living doc, no change) |
| supervisor_brief.md | safety-governance | External-reviewer explainer: novelty, evaluation, next steps | solid | keep as-is |
| supervisor_brief_final.md | safety-governance | Condensed one-page version of supervisor_brief | solid | keep as-is |
| references.md | safety-governance | External standards (MCP, A2A, policy, identity) | reference-only | keep as-is |
| changelog.md | safety-governance | Architectural pivot record | draft | keep, add entry when Yar profile added |
| implementation_alignment.md | engineering-research | Implementation vs spec checklist | reference-only | keep (living tracker) |
| final_status.md | engineering-research | Production-candidate status, gate list | reference-only | keep (living tracker) |
| release_gates.md | engineering-research | Gate taxonomy with per-gate evidence requirements | reference-only | keep as-is |
| v1_tasks.md | engineering-research | Full v1 backlog, all P1-P4 logged as done | reference-only | keep (historical) |
| privacy-boundary-spec.md | safety-governance | Privacy boundary schema v0, CrossBoundarySignal, 10 EARS req | draft | extend: add standard header, link to CAP 03_primitives.md |

### 1b. Cytoplex Steering (03-Products/Cytonome/Cytoplex/steering/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| cytoplex-product.md | safety-governance | Product vision, personas, success metrics | solid | keep as-is (steering, not spec) |
| cytoplex-tech.md | engineering-research | Python stack, dependency pins, architecture patterns | solid | keep as-is (steering, not spec) |
| cytoplex-structure.md | engineering-research | Directory layout and module boundary map | solid | keep as-is (steering, not spec) |

### 1c. Cytoplex Engineering (04-Engineering/cytoplex/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| cap-system-doc.md | safety-governance | v0.1 overview, roles, canonical implementation paths | solid | keep as-is (companion to spec) |
| api.md | engineering-research | CLI entry points for running and verifying CAP | solid | keep as-is |
| research/cap-protocol-assessment.md | safety-governance | Gap and rebuild assessment for CAP repo and Yar integration | solid | supersede: content absorbed into 01_foundations + architecture; archive |
| research/cap-comprehensive.md | multi-agent | Draft revision plan for CAP communication and coordination | draft | supersede: absorbed into 05_integrations + architecture; archive |
| reports/multi-agent-architecture-report.md | multi-agent | Validated edge-interviewer + center-supervisor with Level 12 Gemma test | solid | keep as research evidence; referenced from new SPEC-multi-agent.md |
| reports/cap-v0.1-supervisor-report.md | safety-governance | v0.1 artifact inventory: roles, core types, CAP-Med constraints | solid | keep as historical report |
| security/threat_model.md | safety-governance | Threat model for CAP | solid | keep (security sub-domain) |
| security/security_review.md | safety-governance | Security review findings | solid | keep (security sub-domain) |
| security/kms_hsm.md | safety-governance | KMS/HSM key management patterns | solid | keep (security sub-domain) |
| benchmarks/cap_v1_latency_mobile_budget.md | edge-AI-hybrid | Mobile latency budget for CAP v1 on-device | solid | keep; reference from SPEC-edge-ai-hybrid.md |

### 1d. Yar Spec (03-Products/Cytonome/Yar/spec/) -- NEW, 2026-06-21

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| SPEC-storage-engine.md | storage-sync | CRDT op-log source of truth, three architecture patterns, open decisions | draft | extend: add standard header; resolve open decisions after SurrealDB retest |
| SPEC-sync-protocol.md | storage-sync | Eight-layer sync, Loro+Iroh vs any-sync scoring, Solid portability, HIPAA | draft | extend: add standard header |
| STORAGE_BENCHMARK_TRACKER.md | storage-sync | Ali's results; SQLite validated; SurrealDB last-place flagged for retest | draft | keep as living tracker; add header |
| SurrealDB-tuning-and-graphrag-guide.md | storage-sync | SurrealDB 3.1 tuning, schemafull, FTS/HNSW/DISKANN config, GraphRAG, Flutter | solid | keep as-is; reference from SPEC-storage-engine.md |
| MODULE-crisis-detection.md | safety-governance | On-device crisis-detection: signal tiers, API contract, safety principles, EARS | draft | extend: add standard header, link to privacy-boundary-spec.md |

### 1e. Yar Steering (03-Products/Cytonome/Yar/steering/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| yar-product.md | engineering-research | Vision, four user personas, success metrics, roadmap | reference-only | keep (steering); note stack choices are partially stale (Anytype removed, DB TBD) |
| yar-tech.md | engineering-research | Stack table (Python/FastAPI/Neo4j/Flutter/Gemma), arch patterns | reference-only | keep; annotate that Neo4j is cloud-only and DB engine is pending retest |
| yar-structure.md | engineering-research | Monorepo directory layout, module boundaries, naming conventions | reference-only | keep as-is |

### 1f. Yar Engineering (04-Engineering/yar/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| yar-system-doc.md | engineering-research | MVP architecture: local graph, CAP-Lite, SQLite, multi-platform surfaces | solid | keep (companion system doc, not a spec) |
| sensors/README.md | universal-sensor-CSP | Index for USAP/CSP sensor documentation suite | solid | keep; reference from SPEC-CSP.md |
| sensors/unified-sensor-report.md (at 04-Engineering/cytos/) | universal-sensor-CSP | Authoritative consolidated sensor architecture and schema reference | solid | merge into SPEC-CSP.md as the schema foundation |
| sensors/implementing-wearables.md | sensor-physiological | Oura Ring and Fitbit API integration, FHIR mapping, ND features | solid | merge into SPEC-sensor-physiological.md |
| sensors/implementing-aware.md | sensor-physiological | AWARE passive sensing adapter, Python, ADHD phenotyping | solid | merge into SPEC-sensor-physiological.md |
| sensors/implementing-health-instruments.md | sensor-physiological | Clinical questionnaires and EMA instruments as Cytonome sensors | draft | merge into SPEC-sensor-physiological.md |
| sensors/ml-models.md | engineering-research | Survey of ML model IO schemas and ontologies | draft | keep as supporting research reference |
| research/elevenlabs_evaluation.md | personas-voice | ElevenLabs TTS, STT, and agent products evaluation | draft | extract into SPEC-personas-voice.md as vendor section |
| research/voice_model_deep_evaluation.md | personas-voice | Voice model eval: interrupt control, prosody, longitudinal tracking | draft | extract into SPEC-personas-voice.md as model-selection section |
| research/cap_yar_comprehensive_reference.md | safety-governance | Comprehensive technical reference for CAP and Yar multi-agent arch | solid | keep; supersede with SPEC-multi-agent.md once written |
| research/yar-substrate-decision.md | storage-sync | Decision: Yar-owned local runtime over third-party PKM substrates | solid | keep; reference from SPEC-storage-engine.md as decision record |
| reports/03_cap_consolidation.md | safety-governance | CAP consolidation report from engineering sprint | reference-only | keep as historical record |

### 1g. Yar Consolidation Digests (Yar/consolidation_2026-06-21/_storage/)

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| _storage/BENCHMARK_DIGEST.md | storage-sync | Ali's benchmark results: SQLite, Kuzu, FalkorDB, Neo4j, SurrealDB | solid | reference from SPEC-storage-engine.md; do not move |
| _storage/STORAGE_SYNC_DIGEST.md | storage-sync | CRDT op-log architecture with open decisions on graph engine and sync | solid | key input for resolving open decisions in SPEC-storage-engine.md |
| _synthesis/SPEC_INPUT_PACK.md | safety-governance | Source pack for privacy-boundary and crisis-detection spec drafting | solid | keep as provenance record |

### 1h. Org-level Assessment

| Path | Domain | Summary | Quality | Action |
|---|---|---|---|---|
| org/plans/research/cap-protocol-assessment.md | safety-governance | Earlier org-level CAP assessment (predates docs-repo copy) | superseded | supersede: docs-repo copy at 04-Engineering/cytoplex/research/ is authoritative |

---

## 2. Target Harmonized Spec Set

The final set we should end with. Specs marked DONE exist and need only a standard header pass. Specs marked EXTEND need substantive additions. Specs marked NEW require net-new writing.

### Group A: Safety and Governance Layer (CAP/Cytoplex)

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Cytoplex/spec/01_foundations.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/02_core_model.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/03_primitives.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/04_security_trust_evidence.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/05_integrations.md` | safety-governance + multi-agent | DONE | existing |
| `Cytoplex/spec/06_conformance.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/07_profiles_roadmap.md` | safety-governance | DONE | existing |
| `Cytoplex/spec/privacy-boundary-spec.md` | safety-governance | EXTEND | add header, link to 03_primitives |
| `Yar/spec/MODULE-crisis-detection.md` | safety-governance | EXTEND | add header, link to privacy-boundary-spec |

### Group B: Data Layer (Storage and Sync)

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-storage-engine.md` | storage-sync | EXTEND | resolve open decisions post-retest |
| `Yar/spec/SPEC-sync-protocol.md` | storage-sync | EXTEND | add header |
| `Yar/spec/STORAGE_BENCHMARK_TRACKER.md` | storage-sync | EXTEND | add header; living tracker |
| `Yar/spec/SurrealDB-tuning-and-graphrag-guide.md` | storage-sync | DONE | existing |

### Group C: Multi-Agent System

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-multi-agent.md` | multi-agent | NEW | consolidate from: 05_integrations, architecture, multi-agent-architecture-report, cap_yar_comprehensive_reference; add discovery and orchestration layers |

### Group D: Personas, Voice, and Character

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-personas-voice.md` | personas-voice | NEW | from scratch with: elevenlabs_evaluation, voice_model_deep_evaluation, yar-product (persona section) as inputs |

### Group E: Universal Sensor Protocol (CSP)

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-CSP.md` | universal-sensor-CSP | NEW | consolidate from: sensors/unified-sensor-report, sensors/README, sensors/implementation-plan; define canonical CSP schema |

### Group F: Prioritized Sensor Modalities

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-sensor-physiological.md` | sensor-physiological | NEW (consolidation) | merge: implementing-wearables, implementing-aware, implementing-health-instruments |
| `Yar/spec/SPEC-sensor-speech-mentalstate.md` | sensor-speech-mentalstate | NEW | from scratch; inputs: voice_model_deep_evaluation (prosody section), elevenlabs_evaluation |
| `Yar/spec/SPEC-sensor-menstrual.md` | sensor-menstrual | NEW | from scratch; no existing docs |
| `Yar/spec/SPEC-sensor-social-interaction.md` | sensor-social-interaction | NEW | from scratch; no existing docs |

### Group G: Neurobehavioral Axes

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-neurobehavioral-axes.md` | neurobehavioral-axes | NEW | from scratch; inputs: BDNF/TrkB axes memory note, adhd-paper-synthesis, Yar feature matrix mood/thought/cognitive axes |

### Group H: Edge-AI and Hybrid Supervisor

| Target File | Domain | Status | Source |
|---|---|---|---|
| `Yar/spec/SPEC-edge-ai-hybrid.md` | edge-AI-hybrid | NEW | from scratch; inputs: multi-agent-architecture-report (Level 12 Gemma), cap_v1_latency_mobile_budget, CAP-Lite in yar-system-doc |

**Total target spec files: 23**
- DONE (no writing needed): 8
- EXTEND (header plus targeted additions): 5
- NEW (net-new writing required): 10

---

## 3. Gap List: Domains Needing Net-New Specs

These domains have no meaningful existing spec coverage. Each requires a spec written from scratch or near-scratch.

| Domain | Gap Description | Primary Input Sources |
|---|---|---|
| Multi-agent system | Discovery, orchestration, and agent interaction contracts are scattered across reports; no unified spec | 05_integrations, architecture, multi-agent-architecture-report, cap_yar_comprehensive_reference |
| Personas, voice, and character | No spec exists; two research evals (ElevenLabs, voice models) remain un-synthesized; no dynamic discovery or ElevenLabs integration contract | elevenlabs_evaluation, voice_model_deep_evaluation |
| Universal sensor protocol (CSP) | The cytos sensing-schema docs define Cytoverse science sensors; a Yar-specific CSP binding them to the mobile/on-device context does not exist as a spec | unified-sensor-report, sensors/README |
| Speech-based mental-state sensing | No spec; voice model eval covers prosody and interrupt-control but does not define a sensing schema or inference pipeline | voice_model_deep_evaluation |
| Menstrual sensing | No prior doc of any kind | None; research required first |
| Temporal social-interaction sensing | No prior doc; AWARE integration covers passive sensing primitives but no social-interaction schema | implementing-aware (partial) |
| Neurobehavioral axes | BDNF/TrkB axes and Mood/Thought/Cognitive axes appear in science docs and the feature matrix but no engineering spec translates them to Yar sensor outputs | adhd-paper-synthesis, BDNF memory note, feature matrix |
| Edge-AI and hybrid supervisor | Level 12 Gemma test in multi-agent report and mobile latency budget doc exist; no spec defines the on-device vs cloud handoff protocol | multi-agent-architecture-report, cap_v1_latency_mobile_budget, yar-system-doc |

---

## 4. Cross-Cutting Standards

Apply these uniformly to every spec file on first pass or when extending.

### 4a. Standard Metadata Header

Every spec file must open with a YAML frontmatter block:

```yaml
---
spec_id: SPEC-<domain-code>   # e.g. SPEC-storage-engine, SPEC-CSP, MODULE-crisis-detection
version: "0.1"
status: draft | review | approved
domain: <one of the 8 canonical domains>
owner: Shahin Mohammadi
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
depends_on: []   # list spec_ids this spec depends on
implements: []   # list CAP sections or profile IDs this spec implements
---
```

### 4b. LinkML and Biolink Foundation

All data schema definitions inside specs must use LinkML syntax. Where biological or clinical entities appear, inherit from Biolink Model classes (e.g., `biolink:PhenotypicFeature`, `biolink:Disease`). Sensor signal schemas should extend the cytos sensing-schema LinkML classes defined in `04-Engineering/cytos/sensing-schema/`.

### 4c. CAP Governance Anchoring

Every spec that involves data leaving the device, agent decision-making, or user-facing actions must reference the relevant CAP primitive from `03_primitives.md`. Crisis-detection and privacy-boundary specs must cite the CAP conformance level they target (from `06_conformance.md`). Sensor specs that produce boundary-crossing signals must declare their `CrossBoundarySignal` classification per `privacy-boundary-spec.md`.

### 4d. CRDT Op-Log as Source of Truth

Any spec that touches persistent state must acknowledge the CRDT op-log architecture from `SPEC-storage-engine.md`. State mutations must be described as CRDT operations, not as direct database writes. This applies to: personas-voice (preference state), neurobehavioral-axes (longitudinal axis scores), and sensor specs (time-series observations).

### 4e. Naming Rules

- Never use "Substrate" as a noun for the data layer. Use "storage layer", "data layer", or "local runtime".
- The universal sensor protocol is canonically "CSP" (Cytonome Sensor Protocol). Do not use "USAP" in new spec writing.
- The governance/safety protocol is "CAP" (Control Authority Profile) or "Cytoplex". Do not use "Cognitive Agent Protocol".
- "Cytoplex" is the product name; "CAP" is the protocol name. Use them consistently: product docs say Cytoplex, protocol spec sections say CAP.

### 4f. Affirming Language

Any spec section with user-facing language (API response payloads, UI strings, notification content) must use affirming, non-stigmatizing framing. Do not use diagnostic labels as user-visible identifiers. Never use "normal" vs "abnormal" for sensor readings. Example: use "elevated distress signal" not "abnormal affective state".

---

## 5. Parallelization Plan

Dependencies flow: safety-governance core (Group A) is the foundation. Storage-sync (Group B) is independent and already in progress. Multi-agent (Group C) depends on Groups A and B. Sensor specs (Groups E and F) are mostly independent. Neurobehavioral axes (Group G) and edge-AI (Group H) depend on Group F (sensors) for their output types. Personas/voice (Group D) depends on Group E (CSP) for the sensor contract.

**Dependency order:**

```
Group A (done) + Group B (extend)
    -> Group C (multi-agent)
    -> Group E (CSP) -> Group F (sensor modalities) -> Group G (axes), Group H (edge-AI)
    -> Group D (personas) [depends on E]
```

### Batch 0: Header Harmonization (no dependencies, parallelizable)

Run these two tasks simultaneously. They are pure add-header passes; no content rewriting.

| Task | Scope |
|---|---|
| 0a | Add standard YAML header to: privacy-boundary-spec.md, MODULE-crisis-detection.md, SPEC-storage-engine.md, SPEC-sync-protocol.md, STORAGE_BENCHMARK_TRACKER.md |
| 0b | Add cross-reference links in: privacy-boundary-spec.md (to 03_primitives), MODULE-crisis-detection.md (to privacy-boundary-spec), SPEC-storage-engine.md (to BENCHMARK_DIGEST and yar-substrate-decision) |

### Batch 1: Multi-Agent Spec + CSP Spec (independent of each other)

Both draw from different source pools. Run simultaneously.

| Task | Scope |
|---|---|
| 1a | Write SPEC-multi-agent.md: consolidate 05_integrations discovery sections, architecture.md orchestration diagrams, multi-agent-architecture-report Level-12 results, cap_yar_comprehensive_reference agent-interaction patterns; define discovery, routing, and interaction contracts |
| 1b | Write SPEC-CSP.md: consolidate unified-sensor-report schema, sensors/README index, sensors/implementation-plan; define canonical CSP schema structure, signal taxonomy, and LinkML class hierarchy for Yar on-device sensor context |

**Batch 1 depends on:** Batch 0 complete (headers needed before linking).

### Batch 2: Physiological Sensors + Speech Mental-State Sensor (independent)

Both draw from different source pools. Run simultaneously.

| Task | Scope |
|---|---|
| 2a | Write SPEC-sensor-physiological.md: merge implementing-wearables (Oura, Fitbit), implementing-aware (AWARE passive), implementing-health-instruments (EMA/questionnaires); unify under CSP schema from Batch 1b |
| 2b | Write SPEC-sensor-speech-mentalstate.md: extract prosody and mental-state inference pipeline from voice_model_deep_evaluation; define signal schema for real-time speech mental-state sensor under CSP |

**Batch 2 depends on:** Batch 1b (SPEC-CSP.md must exist before sensor modality specs can anchor to it).

### Batch 3: Menstrual Sensor + Social-Interaction Sensor (independent, research-heavy)

These are net-new with no existing internal docs. Both require external research before writing.

| Task | Scope |
|---|---|
| 3a | Research and write SPEC-sensor-menstrual.md: survey menstrual cycle tracking APIs (Apple Health CycleTracking, Fitbit female health), FHIR menstrual observations, ND-specific cycle-mood correlations; define CSP-compatible signal schema |
| 3b | Research and write SPEC-sensor-social-interaction.md: build on implementing-aware passive sensing primitives; define temporal social-interaction signal schema (call duration, proximity events, social rhythm metrics); anchor to CSP |

**Batch 3 depends on:** Batch 1b (SPEC-CSP.md), Batch 2a (can share AWARE primitives from physiological spec).

### Batch 4: Personas/Voice + Edge-AI/Hybrid (independent of each other)

| Task | Scope |
|---|---|
| 4a | Write SPEC-personas-voice.md: synthesize elevenlabs_evaluation (vendor contract), voice_model_deep_evaluation (model selection, prosody, interrupt control); add dynamic persona discovery spec; define ElevenLabs integration contract; CRDT state model for persona preferences; affirming-language section |
| 4b | Write SPEC-edge-ai-hybrid.md: define on-device vs cloud handoff protocol; anchor to multi-agent-architecture-report Level-12 test, cap_v1_latency_mobile_budget, CAP-Lite from yar-system-doc; specify supervisor interrupt behavior |

**Batch 4 depends on:** Batch 1a (SPEC-multi-agent.md for agent interaction contract), Batch 1b (SPEC-CSP.md for sensor signal types that trigger edge-AI).

### Batch 5: Neurobehavioral Axes (last; integrates everything)

| Task | Scope |
|---|---|
| 5a | Write SPEC-neurobehavioral-axes.md: translate BDNF/TrkB Mood/Thought/Cognitive axes into engineering spec; define axis schema as LinkML classes; specify how sensor outputs (from physiological, speech, social-interaction specs) feed axis score computation; CRDT state model for longitudinal axis tracks |

**Batch 5 depends on:** Batches 2 and 3 (sensor modality output types), Batch 1b (CSP), Batch 0 (headers/governance anchoring).

### Summary Table

| Batch | Tasks | Depends on | Outputs |
|---|---|---|---|
| 0 | 0a (headers), 0b (cross-links) | none | 5 existing specs harmonized |
| 1 | 1a (multi-agent), 1b (CSP) | Batch 0 | SPEC-multi-agent.md, SPEC-CSP.md |
| 2 | 2a (physiological), 2b (speech) | Batch 1b | SPEC-sensor-physiological.md, SPEC-sensor-speech-mentalstate.md |
| 3 | 3a (menstrual), 3b (social) | Batches 1b, 2a | SPEC-sensor-menstrual.md, SPEC-sensor-social-interaction.md |
| 4 | 4a (personas), 4b (edge-AI) | Batches 1a, 1b | SPEC-personas-voice.md, SPEC-edge-ai-hybrid.md |
| 5 | 5a (neuro-axes) | Batches 1b, 2, 3 | SPEC-neurobehavioral-axes.md |

**Total new files to write:** 8 net-new specs + 1 merged physiological spec = 9 write tasks across 5 batches.
**Total extend tasks:** 5 (headers + cross-links across Batch 0).
**Max parallel load:** 2 subagents per batch (rule compliant).
