# API Walkthrough

Yar's core experience needs no server. This walkthrough covers the optional
Django personal server, which adds sync, transcription, and a
GraphRAG-grounded assistant. Connect it from Settings & Privacy -> "Your
server", or run these directly.

Start the server:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8000
```

Health check (anonymous):

```bash
curl http://127.0.0.1:8000/api/health
```

## Sync (op-log relay, never database files)

Register a device (personal relay; re-registering an actorId rotates its token):

```bash
curl -X POST http://127.0.0.1:8000/api/sync/register \
  -H "Content-Type: application/json" \
  -d '{"actorId":"device-demo-1","deviceName":"Demo Laptop"}'
```

Current heads (actor heads + server sequence):

```bash
curl http://127.0.0.1:8000/api/sync/heads
```

Push operations (idempotent by `opId`):

```bash
curl -X POST http://127.0.0.1:8000/api/sync/push \
  -H "Content-Type: application/json" \
  -d '{"ops":[{"opId":"...","actorId":"device-demo-1","lamport":1,"type":"capture.created","objectId":"cap_1","payload":{}}]}'
```

Pull operations since a cursor:

```bash
curl -X POST http://127.0.0.1:8000/api/sync/pull \
  -H "Content-Type: application/json" \
  -d '{"sinceSeq":0}'
```

Acknowledge a sync round:

```bash
curl -X POST http://127.0.0.1:8000/api/sync/ack -H "Content-Type: application/json" -d '{}'
```

Canonical projection hash (used to verify device <-> server convergence; the app surfaces this as "Projections match" in Settings):

```bash
curl http://127.0.0.1:8000/api/sync/projection
```

Upload / download a content-addressed blob (voice notes, archived by sha256):

```bash
curl -X POST http://127.0.0.1:8000/api/sync/blobs -F "file=@note.webm"
curl http://127.0.0.1:8000/api/sync/blobs/{sha256} -o note.webm
```

## Knowledge (GraphRAG projection)

Query (hybrid BM25 + deterministic hashing-embedding, RRF-fused, n-hop expansion):

```bash
curl -X POST http://127.0.0.1:8000/api/knowledge/query \
  -H "Content-Type: application/json" \
  -d '{"question":"what did I capture about the focus companion","k":6,"hops":1}'
```

Full graph projection (map viz / debugging):

```bash
curl http://127.0.0.1:8000/api/knowledge/graph
```

## Assistant (grounded chat + task extraction)

Chat, grounded only in what the person themselves captured, gated by CAP-Lite before any provider call:

```bash
curl -X POST http://127.0.0.1:8000/api/assistant/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What should I focus on today?","tone":"gentle"}'
```

Extract tasks from raw text (used by "turn into task" in Capture), same CAP-Lite gate:

```bash
curl -X POST http://127.0.0.1:8000/api/assistant/extract-tasks \
  -H "Content-Type: application/json" \
  -d '{"text":"Remind me to email the landlord and follow up with Sam about the grant."}'
```

Safety refusal example (crisis/diagnosis language never reaches the provider):

```bash
curl -X POST http://127.0.0.1:8000/api/assistant/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Do I have ADHD, diagnose me"}'
```

## Transcribe + TTS

Transcribe a voice note (multipart upload; archived by content hash; `mock` or `faster-whisper` provider):

```bash
curl -X POST http://127.0.0.1:8000/api/transcribe -F "audio=@note.webm"
```

Read text aloud (server TTS tier; `mock` WAV or an OpenAI-compatible endpoint such as Kokoro-FastAPI):

```bash
curl -X POST http://127.0.0.1:8000/api/tts \
  -H "Content-Type: application/json" \
  -d '{"text":"Here is your plan for today.","voice":"default"}' \
  -o reply.wav
```
