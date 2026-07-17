# Safety and Trust

## Defaults

- Yar is local-first by default: no accounts, no analytics, no cloud.
  Everything works fully offline.
- The optional personal server is a relay and projection host, never the
  source of truth; the frontend never talks to it unless the person connects
  it explicitly in Settings, and disconnecting loses nothing on-device.
- Sync exchanges operations, never database files; a device and the server
  verify convergence by comparing a deterministic projection hash, surfaced
  in Settings as "Projections match."
- Auth for the personal server is device-token based: a personal relay,
  where the only principals are the person's own devices.
- The assistant only ever answers from the person's own captured graph
  (GraphRAG, with cited sources) and never diagnoses.

## CAP-Lite Boundaries

`CapLiteGuard` (`backend/cap/guard.py`) is a deterministic, non-ML
term-matching gate that runs before any model call. It refuses:

- crisis language (English and Persian),
- diagnosis or clinical-conclusion requests ("do I have ADHD", "diagnose
  me"),
- treatment or medication-recommendation requests,
- health-risk scoring,
- unsupported certainty about another person's true intent or emotion,
- raw data sharing without consent,
- unconfirmed external writes.

It is wired as a pre-response gate on the assistant's chat and
task-extraction endpoints (`ChatView`, `ExtractTasksView`); on a match, the
message never reaches the model provider. Crisis-language refusals return a
real-support message rather than a generic error, including a launch-market
crisis line reference and findahelpline.com as an international fallback.

Yar is not a clinical product, a diagnostic product, a treatment
recommender, or a mental-health chatbot.

## Examples

**Person:** "Diagnose me, do I have ADHD"
**Yar:** Refuses diagnostic conclusions; suggests real human support.

**Person:** "What treatment do I need?"
**Yar:** Refuses treatment recommendation.

**Person:** "Why did they message me that way?"
**Yar:** Can help preserve context or draft uncertainty-aware language, but
must not claim to know another person's real intent.

## What CAP-Lite Is Not

CAP-Lite is a minimal, deterministic beta safety net, not a clinically
reviewed crisis-detection system. It blocks known high-risk phrasing but
does not prove comprehensive safety coverage. The full CAP protocol
(Controller-Authority Protocol), including a clinical-advisor-reviewed
crisis module and launch-market hotline routing, lives separately under
Cytoplex and is explicitly scoped for after this beta, once a functioning
beta exists and a clinical advisor is contracted.

## Data and Privacy

- Raw captures stay local by default; the person chooses, per capability
  (STT/LLM/TTS), whether to route through this device, a LAN laptop, or the
  optional personal server, in Settings -> AI runtimes.
- Voice notes are archived by content hash (sha256) in a content-addressed
  blob store when the optional server is connected; nothing is uploaded
  otherwise.
- Yar is fully free, with no subscription; there is no commercial incentive
  to retain or monetize captured data beyond the person's own use of the
  product.
