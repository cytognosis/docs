# Reviewer Quickstart

```bash
npm install

# Web preview (no Rust/Python needed)
npm run dev
```

Then open [http://localhost:5173](http://localhost:5173).

Or run the real desktop shell (requires the Rust toolchain, see
https://v2.tauri.app/start/prerequisites/):

```bash
npm run tauri dev
```

Try:

- Capture a stray thought or voice note.
- Turn a capture into a task; see it land in Plan (dual-track: ideal vs. baseline).
- Check in on Mood & Energy.
- Run a Focus session.
- Place and link thoughts on the Map.
- Submit "diagnose me, do I have ADHD" to the Assistant and see the CAP-Lite refusal.

## Optional personal server

```bash
python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt
npm run backend:dev          # http://127.0.0.1:8000
python3 manage.py test       # backend test suite
```

Then in the app: Settings & Privacy -> "Your server" -> Connect. This unlocks
sync (with device <-> server projection-hash convergence), the
GraphRAG-grounded assistant, and voice transcription.

## Full test suite

```bash
npm run typecheck   # tsc --noEmit
npm run build       # production frontend build
npm run backend:test
npm run e2e          # Playwright; boots both servers, ~2 minutes
```

Notes:

- No credentials or accounts are required for the core demo; everything
  works fully offline by default.
- The personal server is optional; disconnecting loses nothing on-device.
- Yar is fully free, with no subscription, now or for the foreseeable future.
- There is no mobile build in this submission; the shipped app is desktop
  Tauri v2 only.
