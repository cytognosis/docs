# Yar Client Evaluation — yar-code-20260705-2354

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-06
**Evaluator:** Cytognosis Foundation
**Subject:** Ali's new Yar client (Tauri + TypeScript/React + Django backend)
**Source:** `https://github.com/cytognosis/yar_revisions/yar-code-20260705-2354/`

---

## BLUF

Ali's new Yar client is **the most architecturally complete implementation to date**. It implements the op-log-first, CRDT-compatible architecture from the Data Fabric report, covers 22 of the 62-feature catalog items (many more as groundwork), ships a working server-side sync protocol with projection-hash convergence verification, and includes a real GraphRAG retrieval pipeline. The storage engine choice is correctly deferred; databases are projections of the op-log, never the source of truth. **This codebase should be adopted as the Yar Wave 1 reference implementation.**

---

## 1. Assessment Against 3-Agent Design

Yar specifies three parallel agents: (1) transcription, (2) revision/tagging, and (3) organization into a personal knowledge graph.

| Agent | Status | Implementation |
|---|---|---|
| **Transcription** | ✅ Shipped (server-tier), groundwork (device-tier) | `backend/transcribe/` — mock and faster-whisper providers; audio archived by content hash in blob store. Device-tier whisper.cpp/WhisperKit seam documented but not bundled. |
| **Revision/Tagging** | ✅ Shipped | `backend/assistant/extraction.py` — transcript-to-task extraction; `backend/assistant/providers.py` — grounded chat with rule-based floor + OpenAI-compatible upgrade path; personal NER via gazetteer. |
| **Organization/KG** | ✅ Shipped (MVP) | `backend/knowledge/` — BM25 + hashing embedder + RRF hybrid retrieval + n-hop graph expansion; `GraphEngine` seam for FalkorDB; `EmbeddingProvider` seam for real embedder. Thought map (spatial canvas) in frontend. |

**Verdict:** All three agents have working implementations. The device-tier AI sidecars (whisper.cpp, llama.cpp) are honest placeholders with documented seams. The server-tier agents are fully functional and e2e-tested.

---

## 2. Storage Engine Assessment

| Criterion | Assessment |
|---|---|
| **Op-log as source of truth** | ✅ Structural. `src/domain/operations.ts` defines the op vocabulary. `src/domain/store.ts` only exposes `dispatch(body)` — no direct state mutation. |
| **Databases are projections** | ✅ Structural. `ARCHITECTURE.md` line 60-64: "The future local index (SQLite + FTS5 + sqlite-vec) and any server graph projection are *additional projections of the same log*." No UI module imports a database name. |
| **Current persistence** | JSONL on disk (Tauri: `oplog.jsonl`), localStorage (web preview). Append-only, corrupt-line-tolerant. |
| **SQLite migration planned** | ✅ Documented in `NEXT_STEPS.md` §2: rusqlite + FTS5 + projection cache table + sqlite-vec. |
| **SurrealDB integration** | Not present. No SurrealDB import anywhere in the codebase. Correct — SurrealDB is a future GraphRAG projection candidate, not the MVP store. |
| **Engine lock-in risk** | ✅ Zero. The `YarOpRepository` interface (`loadAll / append / appendMany / clear`) is 4 methods. Any backend can implement it. |

---

## 3. Local-First Behavior

| Requirement | Status |
|---|---|
| **Works offline** | ✅ All features work without a server. Web preview uses localStorage; Tauri uses filesystem. |
| **Server is optional** | ✅ Settings → "Connect to your Yar server" is explicitly opt-in. Disconnecting loses nothing. |
| **Sync exchanges ops, never DB files** | ✅ `backend/sync/views.py` implements `push/pull` of operations. No database file sync. |
| **Projection-hash convergence** | ✅ FNV-1a/imul hash computed identically in TS and Python. `sync/tests.py` verifies cross-language convergence. |
| **Deterministic reducer** | ✅ `core/reducer.py` is the bit-for-bit twin of `projections.ts`. Same total order (lamport, actorId, opId). |

---

## 4. Encryption and Data Sovereignty

| Requirement | Status | Details |
|---|---|---|
| **Data stays on device by default** | ✅ | `PrivacyPrefs.local_only = true` (Rust default). Privacy prefs mirrored to `privacy.json` for Rust-side boot-time enforcement. |
| **On-device AI only by default** | ✅ | `PrivacyPrefs.on_device_ai_only = true`. |
| **Encryption at rest** | ⚠️ Not yet | JSONL op-log is plaintext. `NEXT_STEPS.md` §0: "End-to-end encrypt op payloads before they leave the device." The Tauri CSP blocks external connections, but the file itself is unencrypted. |
| **Encryption in transit** | ⚠️ Partial | Server sync uses HTTPS (assumed) but ops are plaintext in the relay database. The relay should hold ciphertext per the architecture. |
| **HIPAA pathway** | ⚠️ Gated | Requires SQLCipher for at-rest encryption and E2E encryption of sync payloads. Architecture supports it; implementation pending. |
| **Privacy boundary UI** | ✅ | Settings screen with toggles for local-only, on-device AI, voice mood awareness (opt-in, "never a diagnosis"), and diagnostics. |
| **Data export/deletion** | ✅ | `export_data` (JSON/Markdown) and `clear_local_data` commands. UI warns about irreversibility and suggests export first. |

---

## 5. Crisis Detection and Safety

| Criterion | Assessment |
|---|---|
| **Crisis module** | Out of scope per Wave 0 design decision. Correct for MVP. |
| **Non-clinical language** | ✅ Enforced. `src/lib/copy.ts` reviewed: no "failed", "behind", "broken", "missed". Mood vocabulary is feelings-words, never scores or clinical terms. |
| **Voice mood awareness** | ✅ Opt-in, off by default, explicitly "never a diagnosis", labeled experimental. |
| **Safety prompt** | ✅ Hard-coded in assistant provider. Grounded-only chat (retrieves from person's own graph, never generates unsourced claims). |
| **No dark patterns** | ✅ Private defaults, honest deletion dialogs, export-first prompts, no gamification pressure. |

---

## 6. Privacy Boundary Gating

| Gate | Status |
|---|---|
| **Tauri capability lockdown** | ✅ `capabilities/default.json`: only `core:default`. No fs/shell/http plugin permissions. |
| **CSP** | ✅ `default-src 'self'`; inline styles allowed for Emotion/MUI; IPC origins for Tauri. No external connections. |
| **Server connection consent** | ✅ Explicit user action required. Gentle disconnect confirmation dialog. |
| **Voice mood consent** | ✅ Off by default, separate toggle, experimental label. |
| **Diagnostics consent** | ✅ Off by default, separate opt-in toggle. |

---

## 7. Cytoplex Integration

| Integration Point | Status |
|---|---|
| **Direct cytoplex import** | ❌ Not present. No `cytoplex` import in the codebase. |
| **Privacy boundary spec** | Cross-referenced in `SPEC-storage-engine.md` §6. The PAP open decision is shared between Yar and Cytoplex. |
| **Shared op-vocabulary** | Possible. Yar's `OperationBody` type is extensible. Cytoplex ops could be added as new discriminated union members. |
| **Design system** | ✅ Both use Cytostyle. Yar imports exclusively through `src/lib/cytostyle.ts`. |

**Verdict:** Cytoplex integration is not yet implemented. This is correct for Wave 1 (Yar is the wedge product; Cytoplex is the scientific platform). The architecture supports future integration through the op-log extension pattern.

---

## 8. Feature Catalog Coverage (62 Features)

Based on `REQUIREMENTS_COVERAGE.md` and code inspection:

| Category | Shipped | Groundwork | Placeholder | Not Started |
|---|---|---|---|---|
| Wave 1 wedge features | 18 | 4 | 1 | 0 |
| Data-fabric requirements | 6 | 1 | 0 | 0 |
| ND/ADHD UX standards | All verified | — | — | — |
| AI runtime tiers | 2 shipped + 5 seams | — | 1 | — |

**Notable achievements:**
- 29/29 e2e tests passing (desktop shell, offline, sync convergence, grounded assistant, mobile)
- 34/34 backend tests (sync, GraphRAG, extraction, NER, TTS)
- `tsc --noEmit` clean, `vite build` clean
- Tauri config validated against official v2 schema

---

## 9. Build Feasibility

| Component | Buildable? | Notes |
|---|---|---|
| **Frontend (Vite)** | ✅ | `npm run build` confirmed clean |
| **Backend (Django)** | ✅ | `manage.py test` confirmed 34/34 |
| **Tauri shell (Rust)** | ⚠️ Untested | Requires Rust toolchain + webkit2gtk system libs. `cargo check` not verified in this eval. Sandbox lacked Rust. |
| **E2E (Playwright)** | ✅ | 29/29 on Chromium headless |

---

## 10. Risks and Gaps

| Risk | Severity | Mitigation |
|---|---|---|
| **No at-rest encryption** | High (HIPAA) | Migrate to SQLCipher when moving from JSONL to SQLite |
| **No E2E sync encryption** | High (HIPAA) | Implement before relay goes multi-user |
| **No dark mode** | Medium (ND UX) | `themeMode` flag in providers.tsx; listed in NEXT_STEPS |
| **JSONL not scalable** | Medium | SQLite migration planned; op-log grows linearly |
| **No ESLint/CI** | Low | Codebase written to rules but not enforced |
| **Cytoplex not integrated** | Low | Correct for Wave 1 scope |

---

## 11. Recommendation

**Adopt this codebase as the Yar Wave 1 reference implementation.** The architecture is sound, the op-log-first pattern is structural (not aspirational), and the feature coverage exceeds what was expected for a single development sprint. Immediate priorities:

1. **Run the Tauri shell** — `npm run tauri dev` on a machine with Rust toolchain
2. **Add SQLCipher** — Replace JSONL with SQLite + rusqlite + SQLCipher for at-rest encryption
3. **E2E encrypt sync payloads** — Before the relay handles real personal data
4. **Dark mode** — Flip `themeMode`, honor `prefers-color-scheme`
5. **Real embedder** — Replace hashing embedder with sentence-transformers or on-device model

---

## Cross-References

- Architecture: `yar-code-20260705-2354/ARCHITECTURE.md`
- Requirements: `yar-code-20260705-2354/REQUIREMENTS_COVERAGE.md`
- Implementation: `yar-code-20260705-2354/IMPLEMENTATION_NOTES.md`
- Next steps: `yar-code-20260705-2354/NEXT_STEPS.md`
- Data Fabric report: `yar_supervisor_reproducible_benchmark_package/reports/`
- Storage spec: `SPEC-storage-engine.md`
