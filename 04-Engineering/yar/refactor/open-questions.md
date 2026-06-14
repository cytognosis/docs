> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `refactor`, `architecture`

# 07 — Yar + CAP — Open Questions

## Blocking

### Q1. CAP TS or CAP Rust?

Plan defaults to TypeScript (per cyto-skills addendum Q10). 

If Rust:
- Highest performance, smallest deploy footprint
- More complex toolchain
- Slower iteration on policy changes
- Aligns with Tauri (already Rust)

If TS (default):
- Co-located with cyto-skills (workspace package)
- MCP SDK JS first-class
- Easier policy iteration
- Possibly higher latency (still well under 50ms target for guard eval)

**Recommendation**: TS for v1.0; revisit Rust if benchmarks show > 100ms guard latency.

### Q2. Yar repo rename?

Shahin's update mentions "the name of the last two is subject to change" (referring to CAP and Yar). Renaming possibilities:
- Yar → `cytocapture` or `cyto-edge` (more descriptive)
- Yar → `cyto-yar` (consistent namespacing)
- Yar → keep (recognizable; pre-existing)

**Recommendation**: keep Yar for v1; track rename as separate refactor.

### Q3. CAP repo: standalone or in cyto-skills?

Plan puts CAP in `cyto-skills/cap/` as a workspace package. 

Alternative: `github.com/cytognosis/cap` standalone repo.

**Pros of in-workspace**:
- Co-located with skill runtime
- Single CI
- Single dependency story for Yar

**Pros of standalone**:
- CAP can release independently
- External consumers (non-Cytognosis projects) can adopt CAP without pulling cyto-skills runtime
- Cleaner if CAP becomes a community standard

**Recommendation**: in-workspace for v1; carve out if/when external adopters arrive.

## Modifying

### Q4. Mobile schema codegen path

Flutter doesn't consume Python Pydantic. We need Dart codegen from LinkML.

Options:
- (A) LinkML's gen-dart (experimental?). 
- (B) Hand-author Dart equivalents in apps/mobile/lib/schemas/.
- (C) Use JSON Schema codegen from LinkML, then `json_serializable` in Dart.

**Recommendation**: (C). LinkML → JSON Schema (existing codegen) → Dart `json_serializable` via standard tooling.

### Q5. CAP performance benchmarks

Once TS impl is done, run benchmarks: latency per Directive→Guard→Decision cycle. Target: < 50ms p95.

If targets miss: optimize hot paths (Zod parsing → custom parsers; jose JWS → noble-jwt-ed25519; etc.).

### Q6. Yar mobile Gemma 4 packaging

flutter_gemma 0.13.6 bundles the model? Or is it expected from device?

Current: `flutter_gemma` package supports both. Yar mobile would download model on first run if not bundled.

**Action**: configure per-app (bundled for premium tier; download for free tier).

### Q7. CAP-Med profile content authoring

cap-med.json policy in cyto-skills/cap/src/policies/. Who authors content?

The canonical CAP-Med profile is in the Python ref impl. We copy it verbatim. Future refinements per Cytognosis clinical advisory.

### Q8. Multi-tenant CAP

Currently single-tenant (one CAP server per Cytognosis instance). Multi-tenant requires:
- Per-tenant policy isolation
- Per-tenant audit log
- Per-tenant KMS keys

Deferred to v2.

## Resolved

- CAP source of truth: `/Infra and design/CAP/cytognosis_cap_v01_production_candidate/` (Python ref impl).
- CAP TS port preserves Python ref as docs/reference-python/ (not deleted, read-only).
- Yar schemas migrate to cytoskeleton/schemas/domains/yar/.
- Yar uses CAP TS server as sidecar via HTTP/JSON binding.
- Yar is a true multi-app monorepo with UV + Melos + pnpm + cargo via mise.
- Per-branch config drives env/skill/template selection.
