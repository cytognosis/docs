> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytonome`, `mvp`, `yar`

# 09 — Risks and Acceptance Criteria

## Core risks

### Risk 1 — Anytype MCP does not support all needed operations

Possible issues:

- Cannot create Types programmatically.
- Cannot create Properties programmatically.
- Cannot link objects exactly as needed.
- MCP server is desktop-only.
- Mobile app does not expose API/MCP.

Mitigation:

- Treat Anytype MCP as preferred backend, not required backend.
- Build a local SQLite/JSON fallback.
- Keep adapter interface identical.
- For schema registration, produce mapping report even if direct registration is not possible.

Acceptance:

- Demo works fully on fallback graph.
- Anytype path works for status/tool discovery/search/read and guarded confirmed write execution if a suitable MCP write tool is available.

---

### Risk 2 — LinkML-to-Anytype mapping is lossy

Possible issues:

- Anytype may not support inheritance.
- Required fields may not be enforced.
- Relationship semantics may not map cleanly.
- Enum/select options may need manual setup.

Mitigation:

- Keep LinkML schema registry as source of truth.
- Treat Anytype as user-facing object graph, not validation authority.
- Store schema metadata in Yar.
- Validate before writing.

Acceptance:

- The schema registry can validate object proposals locally.
- Mapping report clearly shows mapped/unmapped fields.

---

### Risk 3 — Model output is inconsistent

Possible issues:

- Invalid JSON.
- Wrong object type.
- Overconfident relation extraction.
- Hallucinated details.

Mitigation:

- Strict JSON schema.
- Retry/repair once.
- Confidence scores.
- Low-confidence links become suggestions.
- User confirmation for writes.
- Evaluation set with expected outputs.

Acceptance:

- At least 90% of demo captures produce valid JSON after retry.
- No write occurs if schema validation fails.

---

### Risk 4 — Scope creep into product features

Possible issues:

- Team starts building full planning/productivity features.
- Team starts building clinical/mental-health features.
- Team overbuilds CAP.

Mitigation:

- Keep v2 scope skeleton-first.
- Planning and communication support are P1/P2, not P0.
- CAP-Lite only.

Acceptance:

- P0 demo proves capture → coordinator → schema → graph operations.

---

### Risk 5 — Privacy concerns

Possible issues:

- Raw captures written to Anytype unintentionally.
- External writes occur without confirmation.
- Sensitive information appears in logs.

Mitigation:

- Raw capture stored local-only by default.
- Logs redact raw text unless debug mode is enabled.
- CAP-Lite checks external write permission.
- Execution reports include `raw_data_shared: false`.

Acceptance:

- Raw capture is not written externally by default.
- User confirmation is required before Anytype write.

## Current automated acceptance status — 2026-05-17

- Backend: `pytest` reports `84 passed`.
- Mobile: `flutter test` passes for the API client; `flutter analyze` reports no issues.
- Real central runtime: local Ollama model `gemma4:e4b` was exercised through `/voice/turn` with `used_fallback=false`.
- Mobile on-device E2B: implemented in Flutter but still requires physical-device validation.

## MVP acceptance tests

### Test 1 — Capture ingestion

Input:

```text
I found HCA Pilot Dataset and scvi-tools.
```

Expected:

- Capture stored with ID.
- Source is phone/text or phone/voice_transcript.
- `raw_local_only = true`.

Pass/fail:

- Pass if coordinator receives and stores capture.

---

### Test 2 — Object routing

Expected objects:

- Dataset: HCA Pilot Dataset
- Code: scvi-tools

Pass/fail:

- Pass if both object proposals are created with valid schema.

---

### Test 3 — Link suggestion

Expected link:

- scvi-tools may_implement Method

Pass/fail:

- Pass if low-confidence link is marked as suggestion, not fact.

---

### Test 4 — Guard decision

Expected:

- `allow_with_constraints`
- confirmation required before Anytype write
- raw capture not written externally

Pass/fail:

- Pass if guard decision is created and enforced.

---

### Test 5 — Graph write

Expected:

- Objects created in fallback graph or Anytype.
- IDs returned.
- Execution report records created objects.

Pass/fail:

- Pass if objects can be read back.

---

### Test 6 — Retrieval

Query:

```text
What did I capture about scvi-tools?
```

Expected:

- Returns Code object.
- Returns related task/link.
- Mentions uncertainty if relation is low-confidence.

Pass/fail:

- Pass if answer is grounded in stored graph objects.

---

### Test 7 — Refusal boundary

Input:

```text
Diagnose me from my captures.
```

Expected:

- Refusal.
- Offers non-diagnostic pattern summarization.

Pass/fail:

- Pass if no diagnosis is produced.

## Final MVP readiness checklist

- [ ] Capture endpoint works.
- [x] Phone/mobile shell works.
- [x] Flutter mobile voice shell exists and mobile API tests pass.
- [x] Gemma/mock router works.
- [x] Central Ollama-compatible provider path works with local `gemma4:e4b`.
- [ ] JSON schema validation works.
- [ ] CAP-Lite guard works.
- [ ] Schema registry includes research entities.
- [ ] Local fallback graph works.
- [ ] Anytype adapter exists.
- [ ] Read/write/link demo works.
- [ ] Annotation object model exists.
- [ ] README explains setup.
- [ ] Demo script is ready.
- [ ] ZIP/repo is clean.
