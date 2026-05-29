# 05 — Task List: Skeleton-First Build

## Current completed status — 2026-05-17

The original skeleton task list has largely been completed, plus Product Milestone 1 has been added.

Completed:

- FastAPI backend and local coordinator.
- `POST /capture` plus `/voice/*` mobile voice endpoints.
- LinkML-like schema registry and demo research schema.
- CAP-Lite guard and execution reports.
- SQLite graph store for objects, links, captures, schemas, Anytype plans, and voice turns.
- Anytype MCP status/tool discovery/search/read and guarded confirmed write path.
- WADM-compatible annotation capture.
- Mobile-first web shell.
- Flutter mobile app for voice, status, object review, Anytype write plan, and confirmation.
- Configurable model router with deterministic stub, HTTP JSON, and Ollama-compatible central provider.
- Automated tests: `84 passed`; mobile API client tests pass; Flutter analyzer passes.

Remaining:

- Full Anytype type/property/schema sync.
- Browser extension and Hypothesis/Memex import/export.
- Rich retrieval/query endpoint.
- Personalization, planning, and production mobile packaging.

## P0 — Absolute must-build skeleton

### 1. Repository and environment

- [ ] Create repo structure.
- [ ] Add README with setup instructions.
- [ ] Add `.env.example` for model and Anytype settings.
- [ ] Add `docker-compose.yml` or simple local run instructions.
- [ ] Add sample captures and expected outputs.

Acceptance criteria:

- A new developer can run the local demo from README.

---

### 2. Phone capture shell

- [x] Build a minimal mobile web page and Flutter shell.
- [x] Add text input field.
- [x] Add voice transcript input field.
- [x] Add submit button.
- [x] Send payload to desktop/local coordinator.
- [x] Show processing status and result.

Acceptance criteria:

- A capture can be submitted from phone/browser to coordinator.

---

### 3. Capture API

- [x] Implement `POST /capture`.
- [x] Store capture metadata.
- [x] Mark raw capture as local-only by default.
- [x] Add voice conversation history through `/voice/conversations/{conversation_id}`.

Acceptance criteria:

- Capture is received, assigned ID, and persisted locally.

---

### 4. Gemma structured router

- [x] Write `object_router.md` prompt.
- [x] Define strict JSON output schema.
- [x] Implement model call interface.
- [x] Add deterministic stub router mode for offline demo/tests.
- [x] Validate output against schema.
- [x] Parse/repair JSON where possible.
- [x] Add HTTP JSON and Ollama-compatible provider paths.

Acceptance criteria:

- Raw capture becomes valid structured object proposal.

---

### 5. CAP-Lite guard

- [ ] Implement guard rules.
- [ ] Define allowed operations.
- [ ] Define forbidden operations.
- [ ] Add guard decision object.
- [ ] Add execution report object.
- [ ] Block unsafe/unsupported outputs.

Acceptance criteria:

- Guard can allow, allow_with_constraints, or refuse operation.

---

### 6. LinkML-style schema registry

- [ ] Define local schema registry format.
- [ ] Add classes: Paper, Author, Dataset, Code, Method, Annotation, Project, Task.
- [ ] Add slot definitions.
- [ ] Add relationship definitions.
- [ ] Add validation function.

Acceptance criteria:

- Object proposals are validated before writing.

---

### 7. Graph adapter interface

- [ ] Define `GraphAdapter` abstract interface.
- [ ] Implement `create_object`.
- [ ] Implement `read_object`.
- [ ] Implement `search_objects`.
- [ ] Implement `update_object`.
- [ ] Implement `create_link`.
- [ ] Implement `export_graph`.

Acceptance criteria:

- The coordinator can call one adapter interface regardless of backend.

---

### 8. Local fallback graph store

- [ ] Implement SQLite or JSON graph store.
- [ ] Store objects.
- [ ] Store links.
- [ ] Store captures.
- [ ] Store execution reports.
- [ ] Support export to JSON.

Acceptance criteria:

- Full demo works without Anytype.

---

### 9. Anytype MCP adapter

- [ ] Add adapter stub.
- [ ] Connect to Anytype MCP if available.
- [ ] Implement list spaces/types if available.
- [ ] Implement search/read objects.
- [ ] Implement create object if available.
- [ ] Implement property update if available.
- [ ] Add graceful fallback if MCP fails.

Acceptance criteria:

- Anytype integration path exists, but demo does not break if Anytype MCP is unavailable.

---

### 10. Read/write/link demo

- [ ] Create a Paper object.
- [ ] Create a Dataset object.
- [ ] Create a Code object.
- [ ] Create a Method object.
- [ ] Link Code → implements → Method.
- [ ] Link Paper → uses_dataset → Dataset.
- [ ] Read back objects and links.

Acceptance criteria:

- Terminal/UI shows successful object creation and graph retrieval.

---

## P1 — Strong demo improvements

### 11. Anytype type mapping UI/report

- [ ] Show LinkML class to Anytype Type mapping.
- [ ] Show missing types/properties.
- [ ] Show schema drift report.

### 12. WADM annotation object

- [ ] Add Annotation schema.
- [ ] Add target/body/motivation/selector fields.
- [ ] Create annotation from webpage/paper capture.
- [ ] Link annotation to Paper or Webpage.

### 13. Browser capture mock

- [ ] Accept URL/title/selected text.
- [ ] Convert to Webpage or Annotation object.
- [ ] Link to Project/Task.

### 14. Graph visualization

- [ ] Show objects and links in a simple graph or table.
- [ ] Filter by type.
- [ ] Click object to see source capture and properties.

### 15. Retrieval query

- [ ] Implement `POST /query`.
- [ ] Search graph.
- [ ] Return relevant objects.
- [ ] Summarize with citations to object IDs.

---

## P2 — Stretch

- [x] Real voice-to-text through Flutter platform STT.
- [x] Flutter mobile app.
- [ ] Real browser extension.
- [ ] Full Anytype schema registration.
- [ ] LinkML YAML import from Cytognosis repository.
- [ ] Hypothesis import/export compatibility.
- [ ] Memex-style browser capture flow.
- [ ] CAP trace viewer.
- [ ] Temporal memory timeline.
- [ ] Persona/personalization layer.

## 48-hour implementation order

1. Local fallback graph store.
2. Schema registry.
3. Capture API.
4. Gemma/mock structured router.
5. CAP-Lite guard.
6. Read/write/link demo.
7. Phone/mobile web capture shell.
8. Anytype MCP adapter stub.
9. WADM Annotation object.
10. Demo script and README.
