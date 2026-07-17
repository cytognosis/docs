# Limitations

## Intentionally Stubbed or Limited

- The device-side op-log store is append-only JSONL; SQLite + FTS5 +
  sqlite-vec is the planned next projection, not yet shipped.
- The server-side knowledge graph is in-memory; FalkorDB is the planned
  graph engine per the data-fabric benchmarks.
- On-device AI runtime (local STT/LLM/TTS sidecars, e.g. whisper.cpp,
  llama.cpp, Piper) is a documented seam in `src/lib/runtimes.ts`, not
  bundled yet. Today's STT/LLM/TTS run through the optional LAN-laptop or
  server tier, or OS voices.
- Voice today is server-side speech-to-text plus read-aloud; a live,
  low-latency, bidirectional voice conversation loop is roadmap, not shipped.
- Sync today is a single-tenant personal relay (one person's own devices,
  device-token auth). Adopting the `any-sync` transport has been assessed as
  the near-term upgrade path; a custom Loro+Iroh sync layer is planned after
  this YC round, not built yet.

## Production Hardening Needed

- End-to-end encryption of sync payloads (the relay currently holds
  plaintext operations; Settings copy already promises encryption).
- Background/opportunistic sync (currently a manual "Sync now").
- Real embedding model behind the `EmbeddingProvider` seam, replacing the
  deterministic hashing embedder used for retrieval today.
- Continuous integration: typecheck + build + backend tests are run
  manually; ESLint is written to but not yet enforced in CI.

## Safety and Trust Limitations

- CAP-Lite (`CapLiteGuard`) is a deterministic, non-ML term-matching gate.
  It is not a clinically reviewed crisis-detection system and should not be
  represented as one. It blocks known high-risk phrasing (crisis language in
  English and Persian, diagnosis and treatment requests) but does not prove
  comprehensive safety coverage.
- Full CAP crisis tooling (clinical-advisor-reviewed crisis module, launch-
  market hotline routing) is explicitly deferred to after this beta; a
  contracted clinical advisor and launch-market hotline decision are still
  open founder items.
- The personal server holds a replica of the op-log; it is optional, and
  disconnecting it loses nothing on-device.

## Mobile and Platform Limitations

- No mobile build ships in this submission. Tauri v2 desktop is the interim
  build used for YC; the long-term cross-platform framework (assessed
  separately, not assumed to be Tauri) is still a pending founder decision.
- AppImage packaging is blocked on a linuxdeploy tooling issue and is
  parked; `deb` and `rpm` installer bundles build green.
- Dark mode is not implemented; the app ships light-theme only at this
  stage (a provider flag away, per the engineering roadmap).

## Feature Coverage

- About 22 of the 62 features in Yar's canonical feature catalog are
  shipped and tested. The remainder are groundwork (the seam or data model
  exists, the feature completes when its dependency lands) or honest,
  labeled in-UI placeholders (for example, voice mood awareness is marked
  experimental, off by default, and explicitly not a diagnosis).
- Cytoscope-owned sensor science (voice-emotion modeling, physiological and
  wearable signals) is out of scope for Yar; Yar consumes sensing, it does
  not own the sensing science.
