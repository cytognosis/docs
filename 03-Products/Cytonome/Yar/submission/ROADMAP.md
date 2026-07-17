# Roadmap

## Phase 1 (near-term, post-YC)

- Move the device-side store from JSONL to SQLite + FTS5, keeping JSONL as
  the export format.
- Adopt the `any-sync` transport for sync (assessed and recommended; not yet
  integrated into the shipped build).
- Bundle on-device AI runtime seams (STT/LLM/TTS sidecars) so capability
  tiers work fully offline, not just through the LAN-laptop or server tier.
- Harden the assistant's grounded-chat quality with a real embedding model
  behind the `EmbeddingProvider` seam.
- Dark mode, native "Save as" export, ESLint enforced in CI.

## Phase 2

- Replace the in-memory server knowledge graph with FalkorDB per the
  data-fabric benchmarks.
- Build a custom Loro+Iroh sync layer for direct device-to-device sync
  without the relay, replacing the FNV projection hash with a real Merkle
  head for anti-entropy.
- Live, low-latency, bidirectional voice conversation loop (today's voice
  path is server-side STT plus read-aloud only).
- Conversational thought-map growth: a placer/reviser/side-thread agent loop
  over the map, once the on-device AI runtime lands.

## Phase 3

- Resolve the long-term cross-platform framework decision (mobile + desktop,
  on-device AI, low-latency voice) and build the real mobile shell; Tauri is
  the interim desktop-only build used for this submission, not assumed to be
  the long-term answer.
- Full CAP crisis-detection module, clinical-advisor-reviewed, with
  launch-market hotline routing (CAP-Lite today is a minimal, non-clinical
  keyword gate).
- End-to-end encrypted sync payloads; blob sync for voice notes across
  devices.
- Universal sensor protocol (Cytonome Sensor Protocol) integration, once
  Cytoscope's sensor science is ready to plug in as a consumed capability.

Yar stays fully free, with no subscription, throughout every phase above;
none of this roadmap is gated behind a paid tier.
