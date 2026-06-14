> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `architecture`, `cytonome`, `mvp`, `yar`

# 07 — Architecture Design Prompt

Copy and use this prompt to generate a detailed implementation architecture.

## Current status note — 2026-05-17

This prompt is preserved as the original architecture-generation prompt. The implemented system has now advanced beyond the prompt in these areas:

- `mobile/` Flutter app exists.
- `/voice/*` endpoints exist.
- Edge `VoiceIntent` routing is formalized.
- Central Ollama-compatible routing exists and was smoke-tested locally with `gemma4:e4b`.
- Anytype confirmed write execution path exists, guarded by CAP-Lite.

Use `PRODUCT_MILESTONE_1_MOBILE_VOICE.md` for the current implemented architecture and setup details.

```text
You are an expert local-first systems architect, AI product engineer, MCP integration engineer, LinkML schema designer, knowledge-graph engineer, and privacy/safety reviewer.

We are building Yar, a local-first cognitive companion and research capture system for the Gemma 4 Good hackathon.

Important correction:
Do not focus first on the full feature set. The immediate MVP is a skeleton-first system. The goal is to prove that phone capture can reach a desktop/local coordinator, which can connect to Anytype through MCP, map LinkML schemas to Anytype object Types/Properties, and create/read/update/link typed entities.

Product references:
- Tana-like capture and structured outliner UX.
- Anytype-like local-first object graph backend.
- Anytype MCP as preferred integration path.
- Local SQLite/JSON graph as required fallback.
- LinkML as canonical schema layer.
- W3C Web Annotation Data Model as annotation model.
- Hypothesis and Memex as browser/web annotation reference patterns.

Current user context:
The user already has a Research space/channel in Anytype mobile with Types like Dataset, Code, Method, Author, and Paper. The skeleton should reuse this direction.

Core system loop:
phone voice/text capture → desktop/local coordinator → Gemma 4 structured router → CAP-Lite guard → LinkML schema registry → Anytype MCP adapter or local fallback graph → typed object creation/read/link.

Two graph layers:
1. Domain/entity graph: Paper, Author, Dataset, Code, Method, Model, Project, Task, Annotation, Collection.
2. Personalization/memory graph: UserCapture, UserInterest, UserPriority, UserAnnotation, Session, provenance, temporal context.

The personalization layer references domain entities instead of duplicating them.

AI role:
Gemma 4 is used as the semantic router. It receives raw capture and produces strict JSON object proposals with:
- object type,
- title,
- summary,
- properties,
- proposed links,
- confidence,
- whether user confirmation is needed.

CAP-Lite role:
Use a lightweight CAP-inspired guard layer, not full CAP.
It should enforce:
- allowed operations only,
- no external writes without confirmation,
- raw captures stay local by default,
- model output must validate against schema,
- low-confidence links are suggestions, not facts,
- diagnostic or clinical claims are refused if they appear.

Minimum entity types:
- Paper
- Author
- Dataset
- Code
- Method
- Annotation
- Project
- Task

Optional entity types:
- Model
- Collection
- Concept
- Webpage
- Organization

Required architecture output:
1. Describe the final architecture in layers.
2. Provide a Mermaid diagram.
3. Define the phone capture app responsibilities.
4. Define the desktop/local coordinator responsibilities.
5. Define API endpoints.
6. Define the Gemma 4 structured-output prompts.
7. Define JSON schemas for Capture, ObjectProposal, LinkProposal, GuardDecision, ExecutionReport, and YarObject.
8. Define LinkML-to-Anytype mapping rules.
9. Define the Anytype MCP adapter interface.
10. Define the local SQLite/JSON fallback graph store.
11. Define how W3C Web Annotation objects are represented and linked.
12. Define read/write/link operation flows.
13. Define error handling and fallback behavior.
14. Define privacy and consent model.
15. Define implementation order for a 48-hour hackathon build.
16. Define what is explicitly out of scope.
17. Define acceptance tests.

Constraints:
- Keep it minimal and demoable.
- The demo must work even if Anytype MCP fails.
- Do not over-engineer CAP.
- Do not make this a therapy chatbot or clinical system.
- Keep raw captures local by default.
- User confirmation is required before external writes.
- Use exportable JSON/Markdown.
- Prefer explicit schemas and typed execution over free-form agent behavior.

Demo scenario:
A phone-side capture says:
"I found HCA Pilot Dataset and scvi-tools. It looks like scvi-tools might implement the method we need for single-cell modeling. Add it to the Research space and remind me to review the method later."

Expected behavior:
- Create or propose Dataset object: HCA Pilot Dataset.
- Create or propose Code object: scvi-tools.
- Create or propose Method placeholder: single-cell modeling method.
- Create Task: Review scvi-tools for the method.
- Link Code → may_implement → Method.
- Link Task → references → Code.
- Add all objects to Research space or fallback graph.
- Return execution report.

Now design the complete architecture and implementation plan.
```
