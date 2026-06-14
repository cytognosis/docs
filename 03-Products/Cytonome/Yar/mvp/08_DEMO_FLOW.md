> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `mvp`, `implementation`

# 08 — Skeleton-First Demo Flow

## Demo title

**From phone capture to Anytype research graph**

## Demo goal

Show that Yar can take a messy phone capture and turn it into typed research objects in a local-first knowledge graph.

## Demo setup

Open three windows:

1. Flutter mobile app or browser mobile web shell.
2. Desktop coordinator logs or dashboard.
3. Anytype Research space or fallback graph viewer.

## Current Product Milestone 1 demo

The strongest current demo is the mobile voice loop:

1. Run backend on LAN:

```bash
source venv/bin/activate
YAR_CENTRAL_MODEL_PROVIDER=ollama \
YAR_CENTRAL_MODEL_ENDPOINT=http://127.0.0.1:11434 \
YAR_CENTRAL_MODEL_NAME=gemma4:e4b \
uvicorn yar.main:app --host 0.0.0.0 --port 8000 --reload
```

2. Open `mobile/` on a physical device:

```bash
cd mobile
flutter run --release -d <device-id>
```

3. Configure backend URL to `http://YOUR_MAC_IP:8000`.
4. Record or type:

```text
Save this: this paper introduces a Gemma method for annotation of research datasets and the code is on GitHub.
```

5. Verify:

- `/voice/turn` returns assistant text and created local objects.
- Model report shows either real central Ollama routing or explicit stub fallback.
- Objects can be selected in the mobile Objects screen.
- Anytype Plan screen shows the exact planned payload.
- Confirming write requires the explicit button and still gracefully refuses when Anytype MCP is unavailable.

6. Submit:

```text
Diagnose me from my captures.
```

Expected: CAP-Lite refuses before model routing.

## Demo script

### Step 1 — Show existing Research space

Show the Anytype Research space/channel.

Current types visible:

- Dataset
- Code
- Method
- Author
- Paper

Say:

> We are not starting from a blank chatbot. Yar writes into a typed local-first research graph. These are the entity types we want to reuse and extend.

### Step 2 — Submit phone capture

Input:

```text
I found HCA Pilot Dataset and scvi-tools. It looks like scvi-tools might implement the method we need for single-cell modeling. Add it to the Research space and remind me to review the method later.
```

Say:

> The user does not need to decide where this belongs. They just capture it from the phone.

### Step 3 — Coordinator receives capture

Show payload:

```json
{
  "source": "phone",
  "capture_type": "voice_transcript",
  "raw_local_only": true
}
```

Say:

> The raw capture stays local by default. The coordinator now asks Gemma to produce structured object proposals.

### Step 4 — Gemma structured output

Show objects:

- Dataset: HCA Pilot Dataset
- Code: scvi-tools
- Method: single-cell modeling method
- Task: Review scvi-tools for the method

Show links:

- Code may_implement Method
- Task references Code
- Dataset related_to Method

### Step 5 — CAP-Lite guard

Show guard decision:

```json
{
  "guard_decision": "allow_with_constraints",
  "constraints": [
    "user_confirmation_required_before_anytype_write",
    "low_confidence_links_marked_as_suggestions",
    "raw_capture_not_written_to_public_properties"
  ]
}
```

Say:

> Yar does not let the model directly mutate the graph. The guard checks permissions, confidence, privacy, and schema validity first.

### Step 6 — Write to graph

Show either:

- Anytype object creation, or
- fallback graph viewer.

Objects created:

- HCA Pilot Dataset
- scvi-tools
- Review scvi-tools for the method

### Step 7 — Read back

Ask:

```text
What did I capture about scvi-tools?
```

Expected answer:

```text
You captured scvi-tools as a Code object. It may implement a single-cell modeling method, but that link is marked as a suggestion because confidence is moderate. You also created a task to review whether it fits the Research project.
```

### Step 8 — Show schema mapping

Show a small table:

| LinkML class | Anytype Type | Status |
|---|---|---|
| Dataset | Dataset | mapped |
| Code | Code | mapped |
| Method | Method | mapped |
| Task | Task | fallback or mapped |
| Annotation | Annotation | planned |

### Step 9 — Close with value proposition

Say:

> This skeleton proves Yar's core loop: phone capture, local AI structuring, schema-based object creation, local-first graph storage, and safe controlled execution. Once this skeleton works, planning, browser annotation, communication support, and personalization can be layered on top.

## Optional second demo — Annotation

Input:

```text
Highlight: "single-cell variational inference enables scalable latent representation learning." Note: connect this to scvi-tools and our Method object.
```

Expected objects:

- Annotation object
- Method or Concept object
- Link Annotation targets Code/Method
- Task to review citation

## Demo pass criteria

- Capture submitted from Flutter app or phone/mobile shell.
- Coordinator receives it.
- Structured JSON is generated.
- Guard decision is shown.
- Objects are written to graph.
- Links are visible.
- Local search works.
- Anytype write planning and confirmation boundary are visible.
- Fallback works if Anytype MCP is unavailable.
