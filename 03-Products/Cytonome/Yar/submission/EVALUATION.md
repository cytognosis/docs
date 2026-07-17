# Evaluation

## A. Current Automated Test Status

- Frontend: `tsc --noEmit` clean, `vite build` clean.
- Backend: `python3 manage.py test` -- 41/41 passing (includes the CAP-Lite
  gate: crisis-language detection in English and Persian, diagnosis and
  treatment refusal, and benign-message pass-through).
- E2E (Playwright, Chromium, real Django + built frontend): 29/29 passing --
  desktop shell/accessibility, offline flows, device <-> server sync loop
  with projection-hash convergence, the grounded assistant, transcription ->
  task extraction, mobile-viewport shell/touch targets, and AI-runtime-tier
  scenarios (defaults, laptop persistence, graceful degradation, honest
  device-STT placeholder).
- Desktop shell: `npm run tauri dev` builds and runs; `deb` and `rpm`
  installer bundles build green. AppImage packaging is blocked on a
  linuxdeploy tooling issue and is parked, not required for this submission.

## B. Evaluation Dimensions

- Deterministic op-log replay and projection-hash convergence (device <-> server).
- CAP-Lite pre-response gate: refusal correctness and non-refusal of benign messages.
- Sync protocol correctness: idempotent import, actor/version heads, tie-break ordering, tombstone-wins fold.
- GraphRAG retrieval grounding: answers only cite the person's own captured graph.
- Voice pipeline: transcription -> content-addressed blob archive -> task extraction.
- Accessibility: single `h1` per screen, `aria-current` navigation, ≥44px touch targets, no color-only information, `prefers-reduced-motion` honored.
- No external dependency required for the core, offline-first demo path.

## C. Suggested Manual Checklist

- Run `npm run dev` or `npm run tauri dev`.
- Capture a thought; turn it into a task; see it in Plan.
- Check in on Mood & Energy; run a Focus session.
- Place and link thoughts on the Map.
- Connect the optional server; sync; confirm "Projections match" in Settings.
- Ask the Assistant a grounded question; confirm cited sources.
- Submit a crisis/diagnosis message; confirm the CAP-Lite refusal and real-support message.

## D. Known Limitations

- The device-side store is JSONL, not SQLite yet; the server's knowledge graph is in-memory, not FalkorDB yet -- both are documented next projections of the same op-log, not architectural gaps.
- Voice today is server-side STT plus read-aloud; there is no live, low-latency, bidirectional voice loop yet.
- CAP-Lite is a deterministic term gate, not a clinically reviewed crisis-detection system.
- No mobile build ships in this submission.

## Reproducibility Notes

The core demo (`npm run dev` or `npm run tauri dev`) requires no network access, no accounts, and no external credentials. The optional server's default providers (transcription mock, assistant rule-based floor) are deterministic, so tests do not depend on a model download.
