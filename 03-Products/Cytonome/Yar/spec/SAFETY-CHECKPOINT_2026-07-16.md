---
spec_id: SAFETY-CHECKPOINT-2026-07-16
version: "1.0"
status: design-final
implementation_status: deferred-post-yc
domain: safety-governance
owner: Shahin Mohammadi
created: 2026-07-16
last_updated: 2026-07-16
depends_on: [SPEC-privacy-boundary, MODULE-crisis-detection]
implements: []
---

> **Purpose of this document:** this is the resume-from-zero-context checkpoint for the Yar safety/crisis workstream. It exists so that in October (or whenever this workstream is picked back up), whoever opens it — including a future Shahin who has forgotten all of this — can resume without re-deriving any of the reasoning below. It does not replace `spec/privacy-boundary-spec.md` or `spec/MODULE-crisis-detection.md`; it is the map that sits on top of them.

# Safety/Crisis Workstream Checkpoint — 2026-07-16

## BLUF

Decision D5: build the full CAP privacy-boundary and crisis-detection modules **post-YC**. For the beta, ship only the lightweight `CapLiteGuard` keyword gate — already done. Both governing specs (`privacy-boundary-spec.md`, `MODULE-crisis-detection.md`) are now finalized designs with implementation deferred; 41 backend tests confirm the shipped gate works today. Nothing further needs to happen on this workstream until post-YC engineering resumes, except two founder decisions that can be made any time before then (clinical advisor contracting, launch-market hotline choice).

## 1. Current Shipped State (as of 2026-07-16)

### 1.1 What is live

- **`CapLiteGuard`**: a deterministic, 22-term English/Farsi keyword-match gate. Ported today from the legacy Yar repo (`https://github.com/cytognosis/Yar/tree/main/src/cap`) into the YC Tauri base at `https://github.com/cytognosis/yar_revisions/yar-code-20260705-2354/backend/cap/`, commit `068b10d` ("feat(safety): port CapLiteGuard pre-response gate from legacy Yar repo").
- **Wiring**: `backend/assistant/safety.py` wraps `CapLiteGuard` behind `evaluate_message()`, `is_denied()`, `gate_reason()`, `gate_message()`. `backend/assistant/views.py` calls this as a **pre-response gate** in both `ChatView.post()` and `ExtractTasksView.post()`, before any provider/LLM call. On a `deny` decision, the view short-circuits and returns the guard's own refusal message; `get_provider()` is never invoked.
- **Crisis message content**: on a crisis-term match, the guard's refusal text points to **1480 (Iran Social Emergency)** and **findahelpline.com**. This is a live, shipped product decision, not a proposal.

### 1.2 Test coverage

41 backend tests, all green (`.venv/bin/python manage.py test` in the Tauri base, run 2026-07-16). Of specific relevance, `SafetyGateTests` in `backend/assistant/tests.py` covers:

- `test_crisis_phrase_english_is_gated_and_skips_provider`
- `test_crisis_phrase_persian_is_gated_and_skips_provider`
- `test_diagnosis_request_is_gated`
- `test_benign_message_passes_through_to_provider`
- `test_extract_tasks_gates_crisis_message`
- `test_extract_tasks_gates_diagnosis_request`
- `test_extract_tasks_allows_benign_text`

In short: crisis (English + Farsi), diagnosis requests, and benign pass-through are all covered on both gated endpoints.

### 1.3 What is explicitly NOT built

- The full `CrossBoundarySignal` schema-validated privacy boundary (privacy-boundary-spec Sections 3-6): data-class enforcement beyond the keyword gate, consent-ref checking, retention TTL enforcement.
- The full crisis-detection module (MODULE-crisis-detection Sections 3-10): tiered scoring (`none`/`elevated`/`acute`), the `CrisisDecision` struct, negation/context handling, the elevated (non-acute) supportive response, and a real resource registry beyond the hardcoded Iran/findahelpline pair.
- The PAP (Policy Administration Point) — does not exist in any form, anywhere, in Cytoplex or Yar.

## 2. What Full Implementation Requires

### 2.1 Components to build (from MODULE-crisis-detection.md)

| Component | Spec section | Notes |
|---|---|---|
| `CrisisDecision` struct + `evaluate()` API | §4 | Stateless, synchronous, target < 10ms, no network dependency |
| Tiered signal taxonomy (`elevated`/`acute`) | §5 | Requires clinical-advisor-owned lexicon with negation/context handling; current 22-term list is `acute`-only |
| Response actions (elevated-tier supportive flow, optional clinician alert) | §6 | Clinician alert depends on privacy-boundary consent-ref plumbing |
| Verified resource registry (data-driven, localized) | §7 | Must replace the hardcoded Iran/findahelpline pair with a verified, updatable registry |
| Threshold/evaluation harness | §8 | Needs a labeled, privacy-safe evaluation set; clinical-advisor task |

### 2.2 Components to build (from privacy-boundary-spec.md)

| Component | Spec section | Notes |
|---|---|---|
| `CrossBoundarySignal` schema (LinkML + generated JSON Schema) | §5 | Canonical schema language already chosen (LinkML); implementation not started |
| Full PEP enforcement of the schema | §4, §5 | See Cytoplex reuse map below — do not rebuild |
| PDP evaluation wired to the above | §4 | See Cytoplex reuse map below — do not rebuild |
| PAP for updatable policy | §2, §8 (Decision #3) | **Net-new, no existing code anywhere, no owner assigned** |
| Consent-ref checking + retention TTL enforcement | §6 | Legal-decision-dependent (Section 8, Decision #2) |

### 2.3 Cytoplex reuse map (do not rebuild these)

Four **Production** files already exist in `https://github.com/cytognosis/cytoplex/tree/main/src/cytoplex/runtime` and must be reused by the full implementation:

| File | Role |
|---|---|
| `local_pep.py` | Local Policy Enforcement Point — capture-level guard evaluating operational constraints and privacy boundary |
| `edge_pep.py` | Edge/boundary PEP — validates CAP envelope structure, authority chains, privacy boundary at the network edge |
| `privacy_pdp.py` | Privacy Policy Decision Point — evaluates the privacy-boundary dimensions (classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw-data egress, minimization) |
| `pdp_adapters.py` | Adapters bridging directive envelopes (`CAPPolicyRequest`) into PDP calls |

**The PAP is the one gap with no existing component.** It is net-new work with no assigned owner as of 2026-07-16. Before any PAP work starts, someone (likely Shahin or whoever leads Architecture post-YC) must be assigned as owner — see Open Decision #3 in privacy-boundary-spec.md §8.

### 2.4 Non-engineering dependencies

| Dependency | Status |
|---|---|
| Contracted clinical advisor | **None yet.** Blocks: crisis lexicon beyond 22 keywords, tier thresholds, negation/context handling rules, evaluation set construction, sensitivity/specificity targets. |
| Launch-market hotline decision | **Open founder decision.** Option A: 1480 Iran Social Emergency + findahelpline.com (already shipped in code today). Option B: 988 US Suicide & Crisis Lifeline + Crisis Text Line (text HOME to 741741) (the spec's proposed US default, not yet verified or shipped). Whichever market Yar launches in first should drive this; both may be needed for a simultaneous US+Iran launch. |
| Counsel review (Duane Valz) | Retention TTLs, clinician-path HIPAA posture, clinician-alert opt-in mechanics, crisis-log retention under HIPAA/state law, formal PHI definition — all still open per both specs' Open Decisions sections. |

### 2.5 Safety-gated features (do not build until the above is resolved)

Per the Yar feature catalog, the following features are gated on this workstream and must not ship ahead of it: **F27, F36, F42, F48, F56, F62, F40, F28.**

## 3. Exact Resume Steps, In Order

1. **Re-read this checkpoint doc in full**, then `spec/privacy-boundary-spec.md` (Section 0) and `spec/MODULE-crisis-detection.md` (Section 0) for the authoritative implementation-status snapshot.
2. **Confirm the shipped gate still works.** Run `.venv/bin/python manage.py test` from `yar_revisions/yar-code-20260705-2354/backend/` (or whatever the current Tauri base directory is by then) and confirm the `SafetyGateTests` still pass. If the Tauri base has moved or been renamed, locate it via `INTEGRATION_PLAN.md` in this project directory.
3. **Make the two open founder decisions** (can happen before or in parallel with step 4):
   - Contract a clinical advisor, or explicitly decide to proceed without one for a defined interim period.
   - Decide the launch-market hotline set (1480+findahelpline vs. 988+Crisis Text Line vs. both), informed by which market(s) Yar is launching in.
   - Input docs: `spec/MODULE-crisis-detection.md` §0, §7, §11 (Decisions #1, #3, #6).
4. **Assign a PAP owner** if runtime-updatable policy is confirmed as a v1 requirement (this itself is Open Decision #3 in `privacy-boundary-spec.md` §8 and needs an Architecture decision first).
   - Input docs: `spec/privacy-boundary-spec.md` §0, §2, §8 (Decision #3).
5. **Scope the `CrossBoundarySignal` schema implementation** against the four existing Cytoplex Production files (Section 2.3 above), confirming the reuse plan still holds (check whether Cytoplex's `runtime/` module has changed since 2026-07-16).
   - Input docs: `spec/privacy-boundary-spec.md` §3, §5, Section 0 reuse table; `cytoplex/src/cytoplex/runtime/{local_pep,edge_pep,privacy_pdp,pdp_adapters}.py`.
6. **Build the crisis-detection module** (`CrisisDecision`, tiered scoring, resource registry) once the clinical advisor is engaged and has supplied the lexicon, tiers, and evaluation set.
   - Input docs: `spec/MODULE-crisis-detection.md` §3-§10; clinical advisor's deliverables (lexicon, thresholds, evaluation set — none exist yet).
7. **Wire the crisis-detection module and full privacy-boundary PEP/PDP into the same pre-response gate point** currently occupied by `CapLiteGuard` (`backend/assistant/safety.py` / `backend/assistant/views.py`), replacing or augmenting the keyword gate without regressing the 41 existing tests.
   - Input docs: `backend/assistant/safety.py`, `backend/assistant/views.py`, `backend/assistant/tests.py` (as they exist at resume time).
8. **Re-verify acceptance criteria** in both specs (`privacy-boundary-spec.md` §7, `MODULE-crisis-detection.md` fail-safe requirements §9-10) before any user-facing release, and get clinical-advisor and counsel sign-off per each spec's Open Decisions.

## 4. Pointers

- Full specs: `spec/privacy-boundary-spec.md`, `spec/MODULE-crisis-detection.md`
- Shipped code: `yar_revisions/yar-code-20260705-2354/backend/cap/`, `backend/assistant/safety.py`, `backend/assistant/views.py`, `backend/assistant/tests.py`
- Legacy source of the port: `Yar/src/cap/`
- Cytoplex reusable components: `cytoplex/src/cytoplex/runtime/{local_pep,edge_pep,privacy_pdp,pdp_adapters}.py`
- Feature catalog (safety-gated features): `feature-research/yar-unified-feature-comparison-v4.md` (F27, F36, F42, F48, F56, F62, F40, F28)

---

## Related documents

- [`privacy-boundary-spec.md`](./privacy-boundary-spec.md), [`MODULE-crisis-detection.md`](./MODULE-crisis-detection.md) -- the two specs this checkpoint closes out; depends_on both.
- CAP code path: `https://github.com/cytognosis/yar_revisions/yar-code-20260705-2354/backend/cap/` (CapLiteGuard implementation this checkpoint governs).
- [`../research/yar-feature-research-FINAL-simplified_2026-07-16.md`](../research/yar-feature-research-FINAL-simplified_2026-07-16.md) -- notes the 8 features gated on this checkpoint's two dependencies.
