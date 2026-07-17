# Yar: A Cognitive Companion Built by and for Neurodivergent Minds

Yar helps people capture scattered thoughts and voice notes, then turns them into a private, local-first personal knowledge graph, with planning, focus, and mood tools built around how neurodivergent attention actually works.

Yar is fully free, with no subscription, indefinitely. The userbase itself is the strategic asset: it is the community Yar will serve when its companion sensor (Cytoscope) is ready. There is no freemium tier and no paid tier today.

## What the Demo Proves

The demo proves the core loop, running today as a Tauri v2 desktop app (React/TypeScript frontend, Rust shell):

```text
capture (voice/text) -> task/thought structuring -> CAP-Lite safety gate -> local op-log store -> plan/focus/mood -> optional sync -> grounded assistant (GraphRAG, with sources)
```

It does this without requiring an account, cloud storage, or a network connection. Everything works on-device by default: no accounts, no analytics, no cloud. An optional personal Django server adds sync, transcription, and a grounded chat assistant, connected only if the person opts in from Settings.

Voice today is server-side speech-to-text plus read-aloud (Kokoro-class TTS on the server tier, OS voices on-device). A live, low-latency, bidirectional voice conversation loop is on the roadmap, not shipped yet.

## How to Run

```bash
npm install

# Web preview (no Rust/Python needed)
npm run dev

# Desktop app
npm run tauri dev

# Optional personal server
python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt
npm run backend:dev
# then: Settings & Privacy -> "Your server" -> Connect
```

Open the desktop app (`npm run tauri dev`) or the web preview at `http://localhost:5173`.

## Main Demo Flow

1. Capture a stray thought or a voice note (private space, nothing auto-promotes).
2. Turn a capture into a task; see it land on the Plan screen in a dual-track lane (ideal vs. baseline).
3. Check in on the Mood & Energy screen; see the rolling texture timeline.
4. Run a Focus session (body-doubling companion, no penalty for stopping early).
5. Place a thought on the map; create a link between two thoughts.
6. Ask the assistant a question grounded in what was just captured; see cited sources.
7. Connect the optional personal server in Settings; watch the two devices converge on the same projection hash.
8. Submit a message with crisis or diagnosis language; see the CAP-Lite safety gate refuse and redirect to real human support.

## What Remains Stubbed or Future

- On-device AI runtime (local STT/LLM/TTS sidecars) is a documented seam, not bundled yet; today's STT/LLM/TTS run through the optional server tier or OS voices.
- The device-side store is append-only JSONL; SQLite + FTS5 + sqlite-vec is the next projection, not yet shipped.
- The server-side knowledge graph is in-memory; FalkorDB is the planned graph engine.
- Sync today is a single-tenant personal relay (device-token auth, one person's own devices). Adopting the `any-sync` transport has been assessed as the near-term upgrade; a custom Loro+Iroh sync layer is planned after this YC round.
- Mobile is not shipped. Tauri is the interim desktop build used for this submission; the long-term cross-platform framework (evaluated separately, not assumed to be Tauri) is still under founder review.
- CAP-Lite is a deterministic keyword/term gate, not a clinically reviewed crisis-detection system; full CAP crisis tooling is scoped for after this beta.
