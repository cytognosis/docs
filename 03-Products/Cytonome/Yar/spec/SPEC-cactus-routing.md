---
spec_id: SPEC-cactus-routing
version: "0.1"
status: draft
domain: edge-ai-routing
owner: Shahin Mohammadi
created: 2026-07-19
last_updated: 2026-07-19
depends_on: [SPEC-multi-agent, SPEC-edge-ai-hybrid, SPEC-privacy-boundary]
implements: [CAP RoutingPolicy concept, cap-comprehensive.md §5]
---

> **Status**: Draft v1
> **Date**: 2026-07-19
> **Author**: @shahin (agent-drafted, founder review pending)
> **Audience**: engineers, founder
> **Tags**: `yar`, `cactus`, `routing`, `edge-ai`, `cap`, `license`
> **Depends on**: `SPEC-multi-agent.md`, `SPEC-edge-ai-hybrid.md`, `SPEC-privacy-boundary.md` (privacy-boundary-spec)

# SPEC: Yar Cactus-Pattern Edge/Cloud Routing Policy

**Reading time**: ~12 minutes.

**BLUF**: Yar adopts the **routing-decision pattern** popularized by the Cactus framework (confidence-gated edge-to-cloud handoff) but does **not** adopt the Cactus binary itself, because its license is a non-SPDX, revenue-and-funding-threshold source-available license that would very likely terminate the moment Yar's YC-backed for-profit consumer entity takes funding. Gemma 4, by contrast, is confirmed Apache-2.0 as of July 2026, so the on-device and local-supervisor models Yar already depends on carry no license risk. This spec formalizes the `RoutingPolicy` that governs every edge-versus-local-supervisor decision in Yar, extending the sketch in `cap-comprehensive.md` §5 with battery, thermal, connectivity, and consent-tier inputs, while leaving the model inventory and inference contract to `SPEC-edge-ai-hybrid.md`.

**If you only read one thing**: Section 2 (the license findings, with the actual quoted Cactus license text) and Section 4 (the adopt-vs-borrow recommendation). The short version: **borrow the routing concept, do not ship the Cactus framework as a dependency.**

---

## 1. Problem

`cap-comprehensive.md` §5 sketched a `RoutingPolicy` for edge-cloud decisions but never resolved two open questions: what concrete engine implements the routing decision, and whether the Cactus framework (a YC S25 on-device AI startup) is a safe dependency for a **fully free, no-subscription, local-first** consumer product owned by a 501(c)(3) foundation today and likely by a YC for-profit spinout tomorrow. `cap-v0.2-revision-plan.md` lists this as open gap #6 (Edge-cloud routing policy), MEDIUM priority. `SPECS-INVENTORY.md` and `EFFORT-ESTIMATES.md` both flag the Cactus license as **unverified** and call for direct confirmation before any adoption decision. This spec closes that gap: it verifies both licenses against source, and it formalizes the routing decision layer that `SPEC-edge-ai-hybrid.md` explicitly left as a placeholder (SPEC-multi-agent.md §7.3: "the split described in this section is a placeholder... treat the edge vs supervisor boundary as a runtime configuration, not a hardcoded topology").

Without a formalized routing policy, every agent improvises its own edge/cloud threshold, the CAP-Lite gate has no single contract to validate against, and the org cannot answer a basic diligence question: is Yar's core routing pattern licensed in a way compatible with a free consumer product built by a nonprofit and, later, spun into a for-profit?

---

## 2. Research and License Findings

### 2.1 Cactus framework: what it is

Cactus (`github.com/cactus-compute/cactus`, ~5.5k stars, 446 forks as of this research pass) is a hybrid edge-cloud AI inference engine for mobile devices and wearables, built by Cactus Compute, Inc., a YC S25-backed startup. Its stack is `Cactus Engine` (C, OpenAI-compatible chat/vision/transcription APIs) over `Cactus Graph` (C++ zero-copy compute graph) over `Cactus Kernels` (ARM NEON SIMD) over a custom rotation-based quantization scheme (`Cactus Quants`), with a `Cactus Transpiler` that converts PyTorch models into the Cactus runtime graph. It ships Swift, Kotlin, Flutter, React Native, Python, and Rust bindings, and its own `Cactus Hybrid` module explicitly implements "route hard queries to the cloud automatically based on local model confidence," including a `--confidence-threshold` CLI flag and a `confidence_threshold: 0.7` field in its own example output. This is the origin of the routing pattern this spec formalizes.

### 2.2 Cactus license: verbatim text and finding

**This is the critical deliverable.** The repository's `LICENSE` file (fetched directly from `github.com/cactus-compute/cactus/main/LICENSE`) reads, in full:

> Copyright (c) 2025 Cactus Compute, Inc. All Rights Reserved.
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, and distribute the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> 1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> 2. This grant of permission applies only to:
>    (a) Individual persons using the Software for personal, educational, research, or non-commercial purposes;
>    (b) Organizations (including their parent companies and subsidiaries) with both:
>        (i) Less than $2,000,000 USD in total funding (including but not limited to equity investments, debt financing, grants, and loans); AND
>        (ii) Less than $2,000,000 USD in gross annual revenue;
>    (c) Educational institutions and students;
>    (d) Non-profit organizations registered under section 501(c)(3) of the United States Internal Revenue Code or equivalent in other jurisdictions.
>
> 3. Any person or organization not meeting the criteria in Section 2 must obtain a separate commercial license from Cactus Compute, Inc. Contact founders@cactuscompute.com for licensing terms.
>
> 4. If an organization qualifying under Section 2(b) subsequently exceeds either threshold, this permission automatically terminates and a commercial license must be obtained within thirty (30) days. For purposes of this license, "gross annual revenue" means total revenue in the preceding 12 months.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...

**Finding**: this is **not** an OSI-approved license and **has no SPDX identifier**. It reads like MIT boilerplate but is a bespoke source-available, revenue-and-funding-threshold license, closest in spirit to "Fair Source" or a PolyForm-Noncommercial-style gate, except the free tier is defined by funding and revenue ceilings rather than a flat non-commercial restriction. It is closer to a **BUSL-pattern commercial-conversion license** than to any permissive OSS license.

**Practical read for Cytognosis**:

| Entity | Qualifies today under §2? | Why |
|---|---|---|
| Cytognosis Foundation (501(c)(3), EIN 39-4383634) | **Yes**, under §2(d) | Registered U.S. 501(c)(3); the license grants free use to nonprofits unconditionally, with no funding or revenue cap in that clause |
| A YC-backed for-profit Yar spinout (per CLAUDE.md's "Summer 2026 YC for-profit consumer positioning") | **No, almost certainly not for long** | YC's own standard deal plus a typical seed round puts most YC companies over $2,000,000 in total funding within weeks of the batch. Section 4's auto-termination clause then gives 30 days to obtain a commercial license from a single-vendor, sub-2-year-old startup |

This is exactly the license-compatibility risk the org's own `EFFORT-ESTIMATES.md` flagged as unverified ("Cactus's exact SPDX license identifier... was not independently confirmed in this pass. Verify the SPDX identifier directly before committing to it for a commercial product"). It is now verified: **there is no SPDX identifier because this is not an open-source license.**

### 2.3 Gemma license: verbatim text and finding

The general Gemma Terms of Use page (`ai.google.dev/gemma/terms`, last modified April 1, 2026) states plainly: **"The terms below apply to Gemma models listed in the Appendix at bottom of this page. For Gemma 4 terms, see the Gemma 4 license."** The Appendix covers Gemma 1, 1.1, 2, 3, 3n, FunctionGemma, EmbeddingGemma, PaliGemma, ShieldGemma, CodeGemma, and other variants under the custom Gemma Terms of Use, which incorporates a Prohibited Use Policy by reference and imposes redistribution notice conditions (Section 3.1) and use restrictions (Section 3.2).

**Gemma 4 is different.** The dedicated Gemma 4 license page (`ai.google.dev/gemma/apache_2`) is the **plain, unmodified Apache License 2.0** text, in full, starting:

> Apache License, Version 2.0, January 2004, http://www.apache.org/licenses/... Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

**Finding**: Gemma 4, the specific model family both `SPEC-edge-ai-hybrid.md`'s edge tier (`gemma-4-E2B`/`E4B`) and cloud tier (`gemma-4-26B-MoE`) depend on, is licensed **SPDX: Apache-2.0**, full stop, no custom terms, no revenue gate, no Prohibited Use Policy incorporated into the license grant itself. This resolves the uncertainty `EFFORT-ESTIMATES.md` flagged ("Gemma 4's Apache-2.0 licensing claim came from a secondary summary... verify against ai.google.dev/gemma/terms directly"). It is now directly verified against Google's own page. Google separately publishes a Prohibited Use Policy and an Intended Use Statement as responsible-use guidance; these are not license conditions for Gemma 4 specifically, but Yar should honor them anyway given the mental-health-adjacent domain.

### 2.4 Alternatives, all independently license-clean

| Library | License (SPDX) | Maturity | Role if adopted |
|---|---|---|---|
| **Gemma 4** (E2B/E4B edge, 26B MoE cloud) | **Apache-2.0** (verified 2.3) | Google, already the decided model per `SPEC-edge-ai-hybrid.md` | Edge and local-supervisor inference model, already decided |
| **LiteRT** (google-ai-edge/LiteRT, successor to TFLite) | **Apache-2.0** | Mature, Google-maintained, already the decided edge runtime per `SPEC-edge-ai-hybrid.md` §5.2 | Edge inference runtime, already decided |
| **llama.cpp** (ggml-org/llama.cpp) | **MIT** | Mature, ~90k+ stars, industry-standard on-device LLM runtime | Fallback edge runtime candidate if LiteRT proves insufficient on a target platform |
| **MLC-LLM** (mlc-ai/mlc-llm) | **Apache-2.0** | Mature, TVM-based, cross-platform (iOS/Android/WebGPU) LLM deployment | Fallback edge runtime candidate; strongest option if WebGPU/browser-extension delivery is prioritized |
| **ONNX Runtime** (microsoft/onnxruntime) | **MIT** | Mature, Microsoft-maintained, broad hardware acceleration support | Fallback runtime for non-LLM edge models (e.g., DistilHuBERT-SER, already implemented per `SPEC-edge-ai-hybrid.md`) |
| **whisper.cpp** / **faster-whisper** | **MIT** | Mature, already the Transcriber agent's evaluated adoption candidates per `EFFORT-ESTIMATES.md` row 1 | On-device ASR, independent of this spec's routing decision |

None of these five alternatives carries a funding cap, a revenue cap, or a commercial-license contingency. All are SPDX-registered, OSI-approved licenses. This is the practical case for the recommendation in Section 4.

---

## 3. RoutingPolicy Design

### 3.1 Adopt, do not re-derive, the CAP RoutingPolicy sketch

`cap-comprehensive.md` §5 already defines the base shape Yar's Guard evaluates:

```python
class RoutingPolicy(BaseModel):
    """Determines whether a Directive executes on-device or escalates to cloud."""
    privacy_level: Literal["device_only", "lan_ok", "cloud_ok"]
    complexity_threshold: float  # 0-1, above which escalate to cloud
    latency_budget_ms: int
    fallback_on_cloud_unavailable: Literal["deny", "degrade", "queue"]
```

This spec adopts that shape unchanged and extends it. It does not redefine `RoutingDecision`, the output schema already normative in `SPEC-edge-ai-hybrid.md` §3.2 (`decision_id`, `tier`, `trigger`, `confidence`, `privacy_gate`, `consent_ref`, `reasoning_code`, `timestamp`). `RoutingPolicy` is the input configuration the routing decider evaluates against; `RoutingDecision` remains the per-Directive output record.

### 3.2 Extended RoutingPolicy (v0.1, this spec)

```python
class RoutingPolicy(BaseModel):
    """Extends the cap-comprehensive.md §5 sketch with device-state and consent inputs."""
    policy_id: str
    agent_id: str                          # yar.<role>.<version>, per SPEC-multi-agent §8.3 naming rule
    privacy_level: Literal["device_only", "lan_ok", "cloud_ok"]
    complexity_threshold: float             # 0.0-1.0; default 0.70, see 3.3
    latency_budget_ms: int                  # per-agent, see Section 4
    battery_state: Literal["normal", "low_power", "critical"]
    thermal_state: Literal["nominal", "elevated", "throttled"]
    connectivity: Literal["offline", "lan_only", "online"]
    consent_tier: Literal[
        "device_only_mode",                 # no consent granted; SPEC-data-sovereignty default
        "cloud_supervisor_consented",       # consent_ref covers cloud_supervisor scope, per SPEC-edge-ai-hybrid §4.4
        "clinician_integration_consented",  # future; privacy-boundary-spec §3.1 PB-6 scope
    ]
    fallback_on_cloud_unavailable: Literal["deny", "degrade", "queue"]
```

**Decision inputs** (left column) map to **decision outputs** (right column) as follows:

| Input | Source of truth | Decision effect |
|---|---|---|
| `privacy_level` of the data | `privacy-boundary-spec.md` §3 data classification (`on_device_only` vs `boundary_derived`) | `device_only` data classes can never resolve to a cloud target, regardless of every other input |
| Task complexity | Edge model confidence score, same signal Cactus's own `--confidence-threshold` demonstrates is a workable pattern (its own example output showed `confidence: 0.8193` against `confidence_threshold: 0.7`) | Below `complexity_threshold`, stay on edge; at or above, evaluate escalation |
| Latency budget per agent | `SPEC-edge-ai-hybrid.md` §5.1 per-op-class table | Exceeding budget is itself a `RoutingTriggerEnum.latency_budget_exceeded` event |
| Battery/thermal state | Device OS APIs (iOS `ProcessInfo.thermalState`, Android `BatteryManager`); no Yar schema exists yet, open decision O-3 | `low_power` or `throttled` biases toward edge (cheaper) or toward local-supervisor offload (cooler), never toward a network-heavy path |
| Connectivity | Device network state | `offline` forces `tier: edge` regardless of every other input, consistent with `SPEC-edge-ai-hybrid.md` §5.4 device-only mode |
| User consent tier | `consent_ref` per `privacy-boundary-spec.md` §5 and `SPEC-data-sovereignty.md` §3 (`local_only: true` default) | No escalation of any kind without an active, scope-matching consent grant; this is non-negotiable |

**Decision outputs** are one of three targets, not two: this spec explicitly splits "cloud" into two operationally distinct tiers because `SPEC-multi-agent.md` open decision O-7 leans toward local-only supervisor for v1:

| Target | What it is today | What it may become |
|---|---|---|
| `edge_model` | Gemma 4 E2B/E4B via LiteRT, on-device | Unchanged; always available offline |
| `local_supervisor` | Gemma 4 26B MoE via Ollama on the user's own laptop, per `SPEC-multi-agent.md` §2.2 | The de facto "cloud" tier for v1 per O-7's current lean |
| `cloud_supervisor` (hosted) | Not yet built | Optional, consent-gated, must pass the identical Privacy Boundary PEP as any other external recipient (O-7's explicit condition) |

### 3.3 Confidence/complexity threshold: cross-check, not a new number

`SPEC-edge-ai-hybrid.md` §3.3 already sets the normative default `Confidence threshold for on-device execution: 0.70`, flagged as an unvalidated design heuristic (O-6). Cactus's own shipped example output independently uses `confidence_threshold: 0.7` as its default handoff point. This spec does not change Yar's 0.70 default; it notes the convergence as a mild external validation of the heuristic, not as evidence it is empirically correct for Yar's population. O-6 remains open.

### 3.4 Fallback ladder

```
edge_model
   |  (complexity_threshold exceeded, OR latency_budget_exceeded, OR capability_gap)
   v
local_supervisor (Ollama, laptop)      <- requires: connectivity != offline, consent_tier != device_only_mode
   |  (local_supervisor unreachable)
   v
fallback_on_cloud_unavailable:
   deny     -> Directive refused, RefusalMessage issued, no silent failure
   degrade  -> continue on edge with last-known guidance (SPEC-multi-agent.md §7.2 pattern)
   queue    -> buffer in outbox (SPEC-edge-ai-hybrid.md §4.4/§5.4), flush on reconnect
```

`cloud_supervisor` (hosted) does not appear in the v1 ladder. It is a future rung, gated behind the same three conditions `SPEC-edge-ai-hybrid.md` §4.4 already requires for any escalation (active consent, declared trigger, privacy gate pass), plus O-7's resolution.

### 3.5 The non-negotiable invariant

**CAP-Lite gates every cross-boundary hop.** No `RoutingDecision` output of `local_supervisor` or `cloud_supervisor` bypasses the CAP-Lite check (`CapLiteGuard`, `Yar/src/cap/guard.py`) or the Privacy Boundary PEP validation of the resulting `CrossBoundarySignal`. Routing determines *where compute happens*; it never determines *whether governance applies*. This mirrors `SPEC-edge-ai-hybrid.md` invariant 3 verbatim and is restated here because it is the single fact this spec cannot be allowed to weaken.

---

## 4. Per-Agent Routing Table

Latency budgets are drawn from `SPEC-edge-ai-hybrid.md` §5.1, not re-measured here. The five rows below use the pipeline-worker naming from `EFFORT-ESTIMATES.md` (Transcriber, Proofreader, Mind-mapper, Interviewer, Supervisor), which `SPECS-INVENTORY.md` flags as needing reconciliation with `SPEC-multi-agent.md`'s Placer/Reviser naming; this spec treats Proofreader and Mind-mapper as the structured-extraction and placement/clustering halves of that older Placer role, pending the Wave 2 `SPEC-multi-agent.md` update.

| Agent | Default tier | Escalation trigger | Latency budget | Privacy level | Notes |
|---|---|---|---|---|---|
| **Transcriber** (STT, latency-critical) | **Edge-first, never escalates** | None; raw audio is `device_only` per `privacy-boundary-spec.md` §3.2 | Full conversational turn ceiling: <200ms end-to-end (`SPEC-edge-ai-hybrid.md` §5.1); ASR segment itself must stay well under this | `device_only` | Raw audio and transcript text may never cross, at any confidence level; this is a hard rule, not a routing decision |
| **Proofreader** (NER + structured output) | **Edge-preferred** | `capability_gap` (cross-session personal-term lookup pending F67) or `confidence_low` on ambiguous entity resolution | Same op-class ceiling as brainmap node placement: <200ms (§5.1) | `boundary_derived` on escalation (structured signal only, never verbatim text) | Structured NER output crossing the boundary must still pass `PB-3`/`PB-5` opaque-reference rules from `privacy-boundary-spec.md` |
| **Mind-mapper** (placement + clustering) | **Hybrid** | Simple placement never escalates (§5.1: Placer never escalates, operates on local CRDT); clustering/restructure escalates on `cross_session` trigger when structure depends on state the local_supervisor holds | <200ms for placement ops (§5.1) | `boundary_derived` for cross-session structural summaries only | Matches `SPEC-multi-agent.md` §6 brainmap loop; CRDT op-log remains the sole write path regardless of tier |
| **Interviewer** (conversational) | **Hybrid** | `confidence_low` on mood-arc/dimensional inference; Interviewer never blocks on the escalation (§7.2 async guidance pattern) | <200ms edge conversational turn (§5.1); local_supervisor guidance is async, no hard ceiling | `boundary_derived` (`stress_signal`, `mood_arc`, `user_disengaged` only, per `SPEC-multi-agent.md` §5.3) | Crisis Guard sits in front of the Interviewer synchronously and is never subject to routing; it is on-device, always, deny-wins |
| **Supervisor** (cloud-optional) | **`local_supervisor` today; hosted `cloud_supervisor` is a future, consent-gated rung** | N/A; the Supervisor is itself the escalation target, not an escalating agent | No hard real-time constraint (§5.3) | Full CAP, not CAP-Lite | Per `SPEC-multi-agent.md` O-7, "cloud" in v1 means Ollama on the user's own laptop; any future hosted option must pass the identical PEP gate |

---

## 5. Boundary with SPEC-edge-ai-hybrid

To avoid two specs quietly drifting into overlapping or contradictory ownership:

| Owns | Spec |
|---|---|
| Model inventory (which model runs where: Gemma 4 E2B/E4B edge, Gemma 4 26B MoE local-supervisor, DistilHuBERT-SER edge) | `SPEC-edge-ai-hybrid.md` |
| Inference contract (temperature/topK/topP parameters, context window, runtime footprint) | `SPEC-edge-ai-hybrid.md` |
| `RoutingDecision` output schema, `SemanticPacket`/`CenterDecision` handoff schemas | `SPEC-edge-ai-hybrid.md` (unchanged, reused here) |
| Interrupt stream contract, crisis force-routing | `SPEC-edge-ai-hybrid.md` §6 (unchanged, reused here) |
| `RoutingPolicy` input schema (the configuration the decider evaluates) | **This spec** |
| Battery/thermal/connectivity/consent-tier inputs to the routing decision | **This spec** (new; not present in `SPEC-edge-ai-hybrid.md`) |
| License posture of any third-party routing/inference framework | **This spec** |
| Per-agent latency budget *values* | `SPEC-edge-ai-hybrid.md` §5.1 (this spec only references them) |
| Per-agent routing *table* (which trigger applies to which agent) | **This spec** (Section 4) |

If a future revision changes a latency budget number, it changes in `SPEC-edge-ai-hybrid.md` and this spec's Section 4 table is regenerated from it, not maintained independently.

---

## 6. Interfaces

### 6.1 Routing evaluation function (illustrative signature)

```python
def evaluate_routing_policy(
    directive: Directive,              # CAP primitive 1, per Cytoplex 03_primitives.md
    policy: RoutingPolicy,              # Section 3.2, per-agent
    device_state: DeviceState,          # battery_state, thermal_state, connectivity
    consent_ref: str | None,
) -> RoutingDecision:                   # unchanged schema, SPEC-edge-ai-hybrid.md §3.2
    ...
```

This function runs inside the on-device routing decider (`SPEC-edge-ai-hybrid.md` §1.2 architecture diagram, "Routing Decider" box), before the Directive reaches CAP-Lite for the boundary check. It never runs on the local_supervisor or cloud_supervisor side; those tiers only ever receive Directives that have already cleared this evaluation plus the CAP-Lite/PEP gate.

### 6.2 Configuration surface

`RoutingPolicy` instances are loaded per-agent at session init from a signed configuration bundle (same session-scoped lifecycle as the `YarAgentCard`, `SPEC-multi-agent.md` §3.2). Changing a policy value (for example, moving `complexity_threshold` off 0.70) requires a new `GuardDecision` record, per `cap-v0.2-revision-plan.md` §2.2's existing rule that policy changes are auditable events, not silent config edits.

### 6.3 What this spec does not define

This spec does not define: the wire format of `DeviceState` (battery/thermal/connectivity), which is left to the mobile app layer and flagged as Open Question OQ-4; the PAP (Policy Administration Point) that would let routing thresholds update at runtime, which `privacy-boundary-spec.md` §0 already flags as net-new and unowned; or any Cactus-specific API, since Section 4 recommends against adopting the Cactus binary.

---

## 7. Risks

| Risk | Description | Mitigation |
|---|---|---|
| **Cactus license termination on funding** | If a future engineering decision silently vendors the Cactus binary (not just its routing concept) into the YC for-profit build, the free-use grant terminates within 30 days of exceeding $2M in funding, and the code must either be removed or licensed commercially under time pressure | This spec's Section 4 recommendation: do not adopt the binary. If a future team overrides this, flag it as a legal/counsel review item before any funding round closes, not after |
| **Vendor continuity** | Cactus Compute, Inc. is a sub-2-year-old, single-vendor, VC-funded startup; its API, license terms, or continued existence are not guaranteed | Mitigated by not depending on it; if the routing-concept pattern needs a maintained reference implementation, LiteRT/llama.cpp/MLC-LLM communities are all larger and multi-vendor |
| **Confidence threshold not empirically validated** | The 0.70 default (shared with Cactus's own default) is a design heuristic on both sides, not validated against Yar's actual neurodivergent-adult user population | Open decision O-6 in `SPEC-edge-ai-hybrid.md` remains the tracking item; this spec does not close it |
| **Battery/thermal signal source undefined** | No Yar schema exists yet for `DeviceState`; without it, the extended `RoutingPolicy` fields (3.2) cannot be evaluated in production | Flagged as Open Question OQ-4; blocks full implementation of Section 3.2, not the license or routing-concept findings |
| **Two "cloud" meanings colliding** | `RoutingPolicy.privacy_level: cloud_ok` could be misread as meaning hosted internet cloud, when v1's actual target is a local-supervisor laptop process | Section 3.2 explicitly splits the output into three named targets (`edge_model`, `local_supervisor`, `cloud_supervisor`) to prevent this conflation in code and in documentation |
| **Naming drift between this spec and SPEC-multi-agent** | Proofreader/Mind-mapper (this spec, Section 4) vs Placer/Reviser (`SPEC-multi-agent.md` today) | Explicitly flagged in Section 4 header; resolves when the Wave 2 `SPEC-multi-agent.md` update lands, per the org's own build order in `SPECS-INVENTORY.md` |

---

## 8. Test Plan

EARS-style acceptance criteria, consistent with the sibling specs' conformance style:

**RT-1 (ubiquitous).** THE SYSTEM SHALL evaluate every Directive against its agent's `RoutingPolicy` before dispatch, and SHALL record the resulting `RoutingDecision` in the local audit log without PHI.

**RT-2 (unwanted, if-then).** IF a Directive's data classification is `device_only` per `privacy-boundary-spec.md` §3.2, THEN THE SYSTEM SHALL resolve `tier: edge` regardless of complexity, confidence, battery, thermal, or connectivity inputs.

**RT-3 (state-driven).** WHILE `connectivity: offline`, THE SYSTEM SHALL resolve every routing decision to `edge_model` and SHALL NOT attempt `local_supervisor` or `cloud_supervisor` dispatch.

**RT-4 (event-driven).** WHEN `local_supervisor` is unreachable after dispatch, THE SYSTEM SHALL apply the `fallback_on_cloud_unavailable` value from the active `RoutingPolicy` (`deny`, `degrade`, or `queue`) and SHALL NOT fail silently.

**RT-5 (event-driven).** WHEN `consent_tier: device_only_mode` is active, THE SYSTEM SHALL NOT resolve any routing decision to `local_supervisor` or `cloud_supervisor`, matching `SPEC-edge-ai-hybrid.md` §4.4.

**RT-6 (ubiquitous).** THE SYSTEM SHALL pass every Directive resolved to `local_supervisor` or `cloud_supervisor` through the CAP-Lite gate and the Privacy Boundary PEP before it leaves the device, with no code path that skips either check.

**RT-7 (unwanted, if-then).** IF a build configuration links the Cactus binary (not merely its documented routing pattern) into a distributable artifact, THEN CI SHALL fail the build and require a signed-off license exception referencing this spec's Section 2.2 finding.

**RT-8 (ubiquitous).** THE SYSTEM SHALL treat the per-agent latency budgets in Section 4 as sourced from `SPEC-edge-ai-hybrid.md` §5.1, and any test asserting a specific millisecond value SHALL cite that section, not a duplicated constant.

Test matrix (unit/integration level): policy evaluation across the full cross-product of `{battery_state} x {thermal_state} x {connectivity} x {consent_tier}` for each of the five agents in Section 4; a fallback-ladder test per `fallback_on_cloud_unavailable` value; a CI license-scan step (RT-7) that greps build manifests for Cactus binary artifacts and fails if found without an explicit exception file.

---

## 9. Open Questions (with recommendations)

| # | Question | Recommendation | Owner/blocker |
|---|---|---|---|
| **OQ-1** | Adopt the Cactus framework itself, or only its routing concept? | **Borrow the concept only.** The license is non-SPDX, funding/revenue-gated, and single-vendor. Yar already has license-clean alternatives (LiteRT, llama.cpp, MLC-LLM, ONNX Runtime) covering every runtime role Cactus would fill. Revisit only if Cytognosis Foundation remains the sole legal operator of Yar indefinitely (§2(d) nonprofit clause would keep it free), which conflicts with the org's own stated Summer 2026 YC for-profit plan | Founder decision; flag to counsel before any funding round if this is ever reconsidered |
| **OQ-2** | Is the 0.70 confidence/complexity threshold correct for Yar's population? | No change recommended here; this spec only notes Cactus's independent convergence on the same default as mild external validation. Empirical validation remains `SPEC-edge-ai-hybrid.md` O-6, unresolved | Requires production user sessions; not blocked on this spec |
| **OQ-3** | Local-only supervisor (v1) vs optionally-hosted cloud supervisor (future)? | Shared with `SPEC-multi-agent.md` O-7; this spec's three-target model (edge/local_supervisor/cloud_supervisor, Section 3.2) is built to support either answer without a schema change | Architecture decision; any hosted path must pass the identical PEP gate per O-7 |
| **OQ-4** | Wire format and OS-API source for `DeviceState` (battery/thermal/connectivity)? | Bind to `ProcessInfo.thermalState` (iOS) and `BatteryManager` (Android) at the mobile app layer; define a thin `DeviceState` LinkML schema alongside the next `SPEC-edge-ai-hybrid.md` revision rather than duplicating it here | No owner assigned yet; blocks full Section 3.2 implementation, not this spec's license findings |
| **OQ-5** | Should the PAP (Policy Administration Point) make `RoutingPolicy` thresholds runtime-updatable? | Defer. `privacy-boundary-spec.md` §0 already flags the PAP as net-new and unowned across all of CAP, not specific to routing. Do not build a routing-specific PAP ahead of the general one | Architecture (unassigned), shared with `privacy-boundary-spec.md` Open Decision #3 |
| **OQ-6** | Reconcile Proofreader/Mind-mapper naming (this spec) with Placer/Reviser naming (`SPEC-multi-agent.md` today)? | Land the Wave 2 `SPEC-multi-agent.md` update first (already queued per `SPECS-INVENTORY.md`'s build order); this spec's Section 4 table should be regenerated to match once that lands, not treated as the naming source of truth | Tracked in the org's own Wave 2 spec queue |

---

## 10. References

| Document | Relationship |
|---|---|
| `cap-comprehensive.md` §5 | Source of the original `RoutingPolicy` sketch, adopted unchanged in Section 3.1 |
| `cap-v0.2-revision-plan.md` | Lists edge-cloud routing policy as open gap #6, MEDIUM priority; this spec closes it |
| `SPEC-edge-ai-hybrid.md` | Owns model inventory, inference contract, `RoutingDecision`/`SemanticPacket`/`CenterDecision` schemas, latency budgets (§5.1), interrupt protocol; this spec's Section 5 states the boundary explicitly |
| `SPEC-multi-agent.md` | Agent inventory, supervisor-worker topology, O-7 (local vs hosted supervisor) |
| `SPEC-privacy-boundary.md` (privacy-boundary-spec) | Data classification (§3), `CrossBoundarySignal` schema, consent/retention rules, the unowned-PAP flag reused in OQ-5 |
| `SPEC-data-sovereignty.md` | `local_only: true` / `on_device_ai_only: true` defaults that this spec's `consent_tier: device_only_mode` maps onto |
| `github.com/cactus-compute/cactus/LICENSE` | Source of the verbatim license text quoted in Section 2.2 |
| `ai.google.dev/gemma/terms` and `ai.google.dev/gemma/apache_2` | Source of the verbatim Gemma license findings in Section 2.3 |
| `EFFORT-ESTIMATES.md` (row 8, "Cactus model-routing") | Prior effort estimate (7-13 eng-weeks, ~50%/50% build-vs-adopt) and the license-verification gap this spec closes |
| `SPECS-INVENTORY.md` | Places this spec in Tier 2 of the build order, after the `SPEC-multi-agent.md` update |

---

<details>
<summary><strong>Glossary</strong></summary>

- **Cactus**: A hybrid edge-cloud AI inference framework by Cactus Compute, Inc. (YC S25). Its routing-concept pattern is borrowed by this spec; its binary is not adopted, per the license finding in Section 2.2.
- **CAP-Lite**: Yar's on-device safety gate. Every routing decision that resolves off-device must still pass CAP-Lite before the Directive leaves the device, per the invariant in Section 3.5.
- **`consent_tier`**: The extended `RoutingPolicy` field mapping to the active `consent_ref` scope from `privacy-boundary-spec.md` and the `local_only`/`on_device_ai_only` defaults from `SPEC-data-sovereignty.md`.
- **`local_supervisor`**: The Gemma 4 26B MoE agent running via Ollama on the user's own laptop. The de facto "cloud" tier for v1, per `SPEC-multi-agent.md` O-7's current lean.
- **`cloud_supervisor`**: A future, optional, consent-gated, hosted tier. Not built. Must pass the same PEP gate as any other external recipient.
- **RoutingPolicy**: The per-agent configuration object this spec formalizes (Section 3.2), evaluated by the on-device routing decider to produce a `RoutingDecision` (schema owned by `SPEC-edge-ai-hybrid.md`).
- **SPDX**: The Software Package Data Exchange license identifier standard. The Cactus repository's license has no SPDX identifier because it is not an open-source license under any OSI-approved definition.

</details>
