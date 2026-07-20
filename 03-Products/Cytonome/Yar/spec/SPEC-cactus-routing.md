---
spec_id: SPEC-cactus-routing
version: "0.2"
status: active
domain: edge-ai-routing
owner: Shahin Mohammadi
created: 2026-07-19
last_updated: 2026-07-19
depends_on: [SPEC-multi-agent, SPEC-edge-ai-hybrid, SPEC-privacy-boundary]
implements: [CAP RoutingPolicy concept, cap-comprehensive.md §5]
---

> **Status**: active (founder-decided 2026-07-19)
> **Date**: 2026-07-19
> **Author**: @shahin (agent-drafted, founder-decided)
> **Audience**: engineers, founder
> **Tags**: `yar`, `routing`, `edge-ai`, `cap`, `license`, `local-vs-cloud`
> **Depends on**: `SPEC-multi-agent.md`, `SPEC-edge-ai-hybrid.md`, `SPEC-privacy-boundary.md` (privacy-boundary-spec)

# SPEC: Model Routing (local vs cloud selection)

**Formerly the Cactus routing spec; Cactus removed per founder decision 2026-07-19; filename kept for link stability.**

**Reading time**: ~9 minutes.

**BLUF**: Cactus is **removed entirely** as a candidate dependency; nonprofit status and a fully-free product do not durably fix its license risk, so there is no scenario worth building around it. Sophisticated confidence-gated routing is not a critical feature for v1; it is replaced by a **simple, user-and-policy-driven local-vs-cloud selector** with a plain fallback ladder, built on Gemma 4 (Apache-2.0) and license-clean runtimes. Effort drops from the original 5-10 eng-week estimate to roughly **2-4 eng-weeks**.

**If you only read one thing**: Section 2 (does nonprofit/free change the license analysis: no) and Section 4 (the simplified selector design that replaces confidence-gated routing).

---

## 1. Problem, Revised Scope

The original draft of this spec formalized a confidence-gated `RoutingPolicy` inspired by the Cactus framework's edge-to-cloud handoff pattern, and separately flagged Cactus's license as a risk to verify. The founder's 2026-07-19 decision changes the scope on both fronts:

1. **Cactus is out, full stop.** Not "borrow the concept, skip the binary": Cactus is no longer a reference architecture, a benchmark, or a future revisit candidate. See Section 2 and Section 3 for why nonprofit and fully-free framing do not change this.
2. **Learned or confidence-gated routing is not a critical feature for v1.** It is real engineering effort (the original estimate was 5-10 eng-weeks) for a decision that a simple, transparent, user-controlled setting can make instead. The routing problem is descoped to: **which agents run locally by default, and when, if ever, does a Directive go to a local supervisor or the cloud, gated by a plain user setting and by consent.**

This spec still closes `cap-v0.2-revision-plan.md` open gap #6 (edge-cloud routing policy), but with a smaller answer than originally planned. It still formalizes the layer `SPEC-edge-ai-hybrid.md` left as a placeholder (`SPEC-multi-agent.md` §7.3: "treat the edge vs supervisor boundary as a runtime configuration, not a hardcoded topology"), and it still leaves the model inventory and inference contract to `SPEC-edge-ai-hybrid.md`.

---

## 2. Does Nonprofit Status or Fully-Free Change the Cactus License Position?

**Short answer: no.** Working it through honestly, because the founder decision explicitly asked for this check:

**What is true today.** The Cactus license (quoted in full in Section 3.2) grants free use unconditionally to 501(c)(3) nonprofits under §2(d), with no funding or revenue ceiling in that clause. Cytognosis Foundation is a registered 501(c)(3) (EIN 39-4383634). If Yar shipped only from the Foundation, indefinitely, as a nonprofit product, the Cactus license would, in fact, permit free use today.

**Why that finding does not resolve anything, in three parts:**

- **(a) The org's own plan contradicts the premise.** `CLAUDE.md` and `README.md` both describe a Summer 2026 YC for-profit consumer (PBC) arm for Yar, with the Foundation as the upstream nonprofit science platform. A spec cannot recommend a dependency whose safety depends on an entity structure the org has already decided to leave.
- **(b) "Fully free to users" is not the same axis as "commercial use by the licensor."** The Cactus license gates on the *organization's* funding and revenue, not on whether the organization charges its own users. A nonprofit or a for-profit giving Yar away at no charge could still exceed the $2,000,000 funding-or-revenue threshold through grants, investment, or donations, none of which is "revenue from users." Free-to-user pricing has zero bearing on this clause.
- **(c) Even the Foundation alone could trip the clause eventually.** Re-reading the license text quoted in Section 3.2: §2(b)'s $2,000,000 ceiling applies to organizations *other than* 501(c)(3)s, so the Foundation's §2(d) grant does not carry that specific cap. But §2(d) protects only the nonprofit entity itself; the moment any part of Yar ships through the for-profit PBC (the entity the org has already committed to for Summer 2026), that entity qualifies, if at all, only under §2(b), and typical YC funding exceeds $2,000,000 within weeks of a batch. There is no restructuring of "nonprofit" or "free" that keeps the for-profit arm under the (b) threshold once it takes YC-scale funding.

**Conclusion, stated plainly:** nonprofit framing and fully-free-to-users framing both look protective at first glance, and neither one durably fixes the license risk, because the license's gate is organizational funding and revenue, not user price and not tax status alone once a for-profit entity is in the picture. Combined with the effort question in Section 1, that closes the case: Cactus is removed, not deferred.

---

## 3. License Findings (Retained From v0.1 Research)

### 3.1 Cactus framework: what it is

Cactus (`github.com/cactus-compute/cactus`) is a hybrid edge-cloud AI inference engine for mobile devices, built by Cactus Compute, Inc., a YC S25-backed startup. It implements confidence-gated edge-to-cloud handoff (a `--confidence-threshold` CLI flag, `confidence_threshold: 0.7` in its own example output). That pattern was this spec's original inspiration; it is no longer referenced as prior art going forward, per Section 1.

### 3.2 Cactus license: verbatim text and finding

The repository's `LICENSE` file reads, in relevant part:

> Copyright (c) 2025 Cactus Compute, Inc. All Rights Reserved.
>
> Permission is hereby granted, free of charge... subject to the following conditions:
>
> 2. This grant of permission applies only to:
>    (a) Individual persons using the Software for personal, educational, research, or non-commercial purposes;
>    (b) Organizations (including their parent companies and subsidiaries) with both:
>        (i) Less than $2,000,000 USD in total funding; AND
>        (ii) Less than $2,000,000 USD in gross annual revenue;
>    (c) Educational institutions and students;
>    (d) Non-profit organizations registered under section 501(c)(3)...
>
> 3. Any person or organization not meeting the criteria in Section 2 must obtain a separate commercial license...
>
> 4. If an organization qualifying under Section 2(b) subsequently exceeds either threshold, this permission automatically terminates and a commercial license must be obtained within thirty (30) days.

**Finding**: this is **not** an OSI-approved license and has **no SPDX identifier**. It is a bespoke source-available, funding-and-revenue-threshold license, closer to a BUSL-style commercial-conversion license than to any permissive open-source license.

### 3.3 Gemma 4: confirmed Apache-2.0

The dedicated Gemma 4 license page (`ai.google.dev/gemma/apache_2`) is the plain, unmodified **Apache License 2.0**, in full, with no custom terms, no revenue gate, and no Prohibited Use Policy incorporated into the grant itself. This is directly verified against Google's own page and applies to both the edge tier (`gemma-4-E2B`/`E4B`) and the local-supervisor tier (`gemma-4-26B-MoE`) that Yar already depends on per `SPEC-edge-ai-hybrid.md`. Google separately publishes a Prohibited Use Policy as responsible-use guidance; Yar honors it given the mental-health-adjacent domain, but it is not a license condition.

### 3.4 License-clean runtime alternatives

None of these carries a funding cap, a revenue cap, or a commercial-license contingency. All are SPDX-registered, OSI-approved licenses, and none references Cactus in any way:

| Library | License (SPDX) | Maturity | Role |
|---|---|---|---|
| **Gemma 4** (E2B/E4B edge, 26B MoE local supervisor) | **Apache-2.0** (verified 3.3) | Google, already decided per `SPEC-edge-ai-hybrid.md` | Edge and local-supervisor inference model |
| **LiteRT** (google-ai-edge/LiteRT) | **Apache-2.0** | Mature, Google-maintained, already decided per `SPEC-edge-ai-hybrid.md` §5.2 | Edge inference runtime |
| **llama.cpp** (ggml-org/llama.cpp) | **MIT** | Mature, industry-standard on-device LLM runtime | Fallback edge runtime candidate |
| **MLC-LLM** (mlc-ai/mlc-llm) | **Apache-2.0** | Mature, TVM-based, cross-platform | Fallback edge runtime candidate; strongest for WebGPU/browser delivery |
| **ONNX Runtime** (microsoft/onnxruntime) | **MIT** | Mature, Microsoft-maintained | Fallback runtime for non-LLM edge models (for example, DistilHuBERT-SER) |

---

## 4. Simplified Design: Local-vs-Cloud Selection

Confidence-gated, learned routing is removed from v1 scope (Section 5). In its place: a **plain, three-state user setting** plus a **fixed per-agent default**, both evaluated against hard privacy and consent gates that do not change from the original design.

### 4.1 User-visible setting

Every Yar session has exactly one active selection, visible and changeable in settings at any time:

| Setting | Meaning | Effect |
|---|---|---|
| **Local only** | Never leave the device | All Directives resolve to `edge_model`; `local_supervisor` and `cloud_supervisor` are disabled regardless of any other input |
| **Prefer local (default)** | Local first, escalate only when needed and allowed | Directives run on `edge_model`; escalation to `local_supervisor` is permitted when the fallback ladder (4.3) triggers and consent allows |
| **Allow cloud** | Local first, cloud permitted as a last resort | Same as "prefer local," plus `cloud_supervisor` becomes reachable if and when that tier exists, subject to the same consent and privacy gates |

The default is **prefer local** for every new session, consistent with Yar's local-first design (`yar-system-doc.md` §1) and with **fully free, no-subscription** positioning: nothing in this setting gates a feature behind payment.

### 4.2 Simplified RoutingPolicy schema

The `cap-comprehensive.md` §5 sketch is kept, trimmed to what a simple selector needs. The learned-routing fields (`complexity_threshold`, `battery_state`, `thermal_state`, `connectivity`, multi-tier `consent_tier` enum) are removed from the normative schema; connectivity and consent become simple gate checks (4.3), not weighted inputs to a confidence model.

```python
class RoutingPolicy(BaseModel):
    """Per-agent local-vs-cloud selection, evaluated by the routing decider."""
    policy_id: str
    agent_id: str                          # yar.<role>.<version>, per SPEC-multi-agent §8.3
    user_setting: Literal["local_only", "prefer_local", "allow_cloud"]
    privacy_level: Literal["device_only", "lan_ok", "cloud_ok"]   # hard constraint, unchanged
    consent_granted: bool                   # active consent_ref present for escalation scope
    fallback_on_unavailable: Literal["deny", "degrade", "queue"]
```

`RoutingDecision`, the output schema owned by `SPEC-edge-ai-hybrid.md` §3.2 (`decision_id`, `tier`, `trigger`, `privacy_gate`, `consent_ref`, `reasoning_code`, `timestamp`), is unchanged. The `confidence` field remains in that schema for forward compatibility but is not populated or evaluated by v1 (Section 5).

### 4.3 Hard constraints, retained unchanged

These are non-negotiable and identical to the prior design; simplifying the routing logic does not simplify governance:

- **`privacy_level` from `privacy-boundary-spec.md` §3.** Data classified `device_only` never resolves off-device, regardless of `user_setting`.
- **Consent gates from `privacy-boundary-spec.md` and CAP-Lite.** No escalation of any kind without an active, scope-matching `consent_ref`. `user_setting: allow_cloud` grants permission, not consent; both are required.
- **CAP-Lite gates every Directive**, on-device, before any inference, unchanged from `SPEC-edge-ai-hybrid.md` §2.

### 4.4 Fallback ladder (plain, not learned)

```
edge_model
   |  (edge cannot complete: capability gap, or latency budget exceeded, per SPEC-edge-ai-hybrid.md §5.1)
   v
local_supervisor (Ollama, laptop)      <- requires: user_setting != local_only, consent_granted = true
   |  (local_supervisor unreachable, or user_setting = local_only)
   v
fallback_on_unavailable:
   deny     -> Directive refused, RefusalMessage issued, no silent failure
   degrade  -> continue on edge with last-known guidance (SPEC-multi-agent.md §7.2 pattern)
   queue    -> buffer in outbox (SPEC-edge-ai-hybrid.md §4.4/§5.4), flush on reconnect
```

`cloud_supervisor` (hosted) is not built and does not appear in the v1 ladder. If it is ever built, it slots in after `local_supervisor` and is reachable only under `user_setting: allow_cloud`, plus the same consent and PEP gates as every other cross-boundary hop; this mirrors `SPEC-edge-ai-hybrid.md` §4.4 unchanged.

---

## 5. Explicitly Out of Scope Now

**Confidence-gated or learned routing** (a model-driven `complexity_threshold`, battery/thermal/connectivity-weighted decisions, per-dimension thresholds) is a **possible later enhancement**, not part of v1. It is removed from this spec's normative design, not merely deferred silently:

- If it returns, it reopens: the `complexity_threshold` default (previously 0.70, unvalidated), the `DeviceState` wire format (battery, thermal, connectivity), and the per-agent latency-budget cross-reference table that the original draft carried in full. None of that machinery is needed for the simple selector in Section 4.
- Any future proposal to reintroduce learned routing should re-run the license check in Section 2 against whatever reference implementation is proposed; the conclusion there is general (funding/revenue-gated licenses do not become safe because Yar is free or nonprofit-flagged) and applies to any future dependency with a similar clause, not only Cactus.

---

## 6. Per-Agent Defaults

Simplified from the original five-row routing table; agent names match the canonical set in `SPEC-multi-agent.md` (Transcriber, Proofreader, Mind-mapper, Interviewer, Supervisor).

| Agent | Default | Ever escalates? | Privacy level |
|---|---|---|---|
| **Transcriber** (STT) | Edge only | Never; raw audio is `device_only` | `device_only` |
| **Proofreader** (NER, structured output) | Edge, prefer local | Yes, on capability gap; structured signal only, never verbatim text | `boundary_derived` on escalation |
| **Mind-mapper** (placement + clustering) | Edge for placement; hybrid for clustering | Placement never escalates; clustering may, under `user_setting` and consent | `boundary_derived` for cross-session summaries only |
| **Interviewer** (conversational) | Edge, prefer local | Yes, non-blocking; guidance arrives asynchronously | `boundary_derived` |
| **Supervisor** | `local_supervisor` today | Is the escalation target, not an escalating agent | Full CAP, not CAP-Lite |

Crisis Guard sits in front of the Interviewer synchronously and is never subject to this or any routing setting; it is on-device, always, deny-wins, unchanged from `SPEC-edge-ai-hybrid.md` §1.3.

---

## 7. Boundary with SPEC-edge-ai-hybrid

| Owns | Spec |
|---|---|
| Model inventory, inference contract, `RoutingDecision`/`SemanticPacket`/`CenterDecision` schemas, latency budgets, interrupt protocol | `SPEC-edge-ai-hybrid.md` |
| `RoutingPolicy` input schema (Section 4.2) and the `user_setting` control | **This spec** |
| License posture of any third-party routing/inference framework | **This spec** |
| Per-agent default tier (Section 6) | **This spec** |

---

## 8. Risks

| Risk | Description | Mitigation |
|---|---|---|
| **A future dependency repeats the Cactus pattern** | A funding-or-revenue-gated license looks safe under the Foundation and gets vendored, then breaks when the for-profit PBC ships | Section 2's analysis is written to generalize: run it against any similarly-gated license before adoption, not just Cactus |
| **User setting is misunderstood as a privacy control** | A user on "allow cloud" might assume that alone sends data to the cloud, when `privacy_level` and consent still gate every hop | Settings copy states plainly that "allow cloud" permits escalation but does not override device-only data classes or consent |
| **Simplification removes a genuinely useful heuristic later** | If production data eventually shows confidence-gated routing would meaningfully improve quality, the simple ladder may look under-powered | Section 5 keeps the reopening path explicit and scoped, so this is a deliberate, revisitable tradeoff, not a dead end |
| **Two "cloud" meanings colliding** | `local_supervisor` (a laptop process) could be misread as internet cloud | Section 4.4 and Section 6 name the tiers explicitly (`edge_model`, `local_supervisor`, `cloud_supervisor`) |

---

## 9. Test Plan

**RT-1 (ubiquitous).** THE SYSTEM SHALL evaluate every Directive against its agent's `RoutingPolicy` before dispatch, and SHALL record the resulting `RoutingDecision` in the local audit log without PHI.

**RT-2 (unwanted, if-then).** IF a Directive's data classification is `device_only`, THEN THE SYSTEM SHALL resolve `tier: edge` regardless of `user_setting`.

**RT-3 (state-driven).** WHILE `user_setting: local_only` is active, THE SYSTEM SHALL resolve every routing decision to `edge_model` and SHALL NOT attempt `local_supervisor` or `cloud_supervisor` dispatch.

**RT-4 (event-driven).** WHEN `local_supervisor` is unreachable after dispatch, THE SYSTEM SHALL apply the `fallback_on_unavailable` value (`deny`, `degrade`, or `queue`) and SHALL NOT fail silently.

**RT-5 (event-driven).** WHEN `consent_granted: false`, THE SYSTEM SHALL NOT resolve any routing decision to `local_supervisor` or `cloud_supervisor`, regardless of `user_setting`.

**RT-6 (ubiquitous).** THE SYSTEM SHALL pass every Directive resolved to `local_supervisor` or `cloud_supervisor` through the CAP-Lite gate and the Privacy Boundary PEP before it leaves the device.

**RT-7 (unwanted, if-then).** IF a build configuration links any funding-or-revenue-gated-license dependency (including but not limited to the Cactus binary) into a distributable artifact, THEN CI SHALL fail the build and require a signed-off license exception referencing this spec's Section 2 and Section 3 findings.

Test matrix (unit/integration): policy evaluation across `{user_setting} x {privacy_level} x {consent_granted}` for each of the five agents in Section 6; a fallback-ladder test per `fallback_on_unavailable` value; a CI license-scan step (RT-7).

**Retired from the original test plan**: the cross-product test over `{battery_state} x {thermal_state} x {connectivity}`, which no longer exists as an input (Section 5). Confidence-threshold-specific assertions are retired with the same note.

---

## 10. Open Questions

Most routing open questions from the original draft close with the simplified scope. What remains:

| # | Question | Recommendation | Status |
|---|---|---|---|
| **OQ-1** | Adopt Cactus in any form? | No. Removed entirely per Section 2 and Section 5; not a "revisit later" item | **Closed** |
| **OQ-2** | 0.70 confidence threshold correct for Yar's population? | Not applicable; no confidence-gated routing in v1 | **Closed (would reopen only if Section 5's enhancement returns)** |
| **OQ-3** | Local-only supervisor (v1) vs optionally-hosted cloud supervisor (future)? | Shared with `SPEC-multi-agent.md` O-7; local-only for v1, unchanged | **Open**, tracked in `SPEC-multi-agent.md` |
| **OQ-4** | `DeviceState` wire format (battery/thermal/connectivity)? | Not applicable; these are not inputs to the simplified selector | **Closed (would reopen only if Section 5's enhancement returns)** |
| **OQ-5** | Should routing thresholds be runtime-updatable via a PAP? | Not applicable; there is no threshold to update, only the three-state `user_setting` | **Closed** |
| **OQ-6** | Proofreader/Mind-mapper naming vs Placer/Reviser? | Resolved: `SPEC-multi-agent.md` §12.3 already canonicalizes Transcriber, Proofreader, Mind-mapper and forbids reintroducing Placer/Reviser | **Closed** |

---

## 11. References

| Document | Relationship |
|---|---|
| `cap-comprehensive.md` §5 | Source of the original `RoutingPolicy` sketch; Section 4.2 trims it |
| `cap-v0.2-revision-plan.md` | Lists edge-cloud routing policy as open gap #6; this spec closes it with reduced scope |
| `SPEC-edge-ai-hybrid.md` | Owns model inventory, inference contract, `RoutingDecision`/`SemanticPacket`/`CenterDecision` schemas, latency budgets, interrupt protocol |
| `SPEC-multi-agent.md` | Agent inventory (canonical Transcriber/Proofreader/Mind-mapper naming, §12.3); O-7 (local vs hosted supervisor) |
| `SPEC-privacy-boundary.md` (privacy-boundary-spec) | Data classification, `CrossBoundarySignal` schema, consent rules |
| `SPEC-data-sovereignty.md` | `local_only: true` / `on_device_ai_only: true` defaults |
| `github.com/cactus-compute/cactus/LICENSE` | Source of the verbatim license text in Section 3.2 |
| `ai.google.dev/gemma/apache_2` | Source of the verbatim Gemma 4 Apache-2.0 finding in Section 3.3 |
| `EFFORT-ESTIMATES.md` (row 8) | Original 7-13 eng-week estimate for the confidence-gated design; superseded by this spec's 2-4 eng-week simplified estimate |

---

<details>
<summary><strong>Glossary</strong></summary>

- **Cactus**: A hybrid edge-cloud AI inference framework by Cactus Compute, Inc. (YC S25). Removed entirely as a dependency and as a design reference, per the founder decision in Section 2.
- **CAP-Lite**: Yar's on-device safety gate. Every routing decision that resolves off-device must still pass CAP-Lite, unchanged from `SPEC-edge-ai-hybrid.md`.
- **`user_setting`**: The three-state control (`local_only`, `prefer_local`, `allow_cloud`) that replaces confidence-gated routing as the primary decision input in this spec.
- **`local_supervisor`**: The Gemma 4 26B MoE agent running via Ollama on the user's own laptop. The de facto "cloud" tier for v1.
- **`cloud_supervisor`**: A future, optional, consent-gated, hosted tier. Not built.
- **RoutingPolicy**: The simplified per-agent configuration object in Section 4.2, evaluated by the on-device routing decider to produce a `RoutingDecision` (schema owned by `SPEC-edge-ai-hybrid.md`).
- **SPDX**: The Software Package Data Exchange license identifier standard. Cactus's license has none because it is not an open-source license under any OSI-approved definition.

</details>
