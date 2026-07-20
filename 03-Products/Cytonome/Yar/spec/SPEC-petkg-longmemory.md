---
spec_id: SPEC-petkg-longmemory
version: "1.0"
status: active
domain: memory-knowledge-graph
owner: Shahin Mohammadi
created: 2026-07-19
last_updated: 2026-07-19
depends_on:
  - SPEC-storage-engine
  - SPEC-sync-protocol
  - SPEC-multi-agent
implements:
  - F67 (long-term personal memory graph)
  - F66 (ask & summarize your captures)
---

> **Status**: Active (founder-approved 2026-07-19)
> **Date**: 2026-07-19
> **Author**: @shahin (agent-drafted, founder review pending)
> **Audience**: engineers
> **Tags**: `yar`, `spec`, `petkg`, `memory`

# SPEC: Yar Personal Temporal Knowledge Graph (PeT)

**Reading time:** about 16 minutes. **If you only read one thing:** Section 4 (Data model) and Section 6 (Substrate choice), which together fix what PeT is made of and where it lives. Everything else follows from those two decisions.

---

## BLUF

**PeT (Personal Temporal knowledge graph) is the long-term memory layer that lets Yar remember a person's own facts, terms, and projects across weeks and months, not just the current session.** It layers bitemporal fact tables on the already-decided SQLite plus FTS5 plus sqlite-vec device store, with FalkorDB as the optional server-tier graph projection; no new database is introduced. PeT facts are CRDT ops on the same op-log as every other Yar write, and cytomem (today Neo4j-based, org-wide) converges with PeT at the schema and API layer now, with a shared graph engine deferred until an embeddable option matures.

---

## 1. Problem

Yar's agents forget. Every conversation, capture, and brainmap session today starts from a near-blank context window. The Proofreading agent cannot recognize a person's own vocabulary across sessions. The mind-mapping agents (Placer, Reviser) cannot place a new thought next to a related one from three weeks ago. The planned ask-and-summarize feature (F66) has nothing longitudinal to search.

`FEATURE-VERIFICATION.md` confirms this gap directly: F52 (private local knowledge store) covers *where* notes live, F58 and F33 cover *recognizing* names and terms in the moment, but nothing covers the retrieval-augmented, longitudinal recall act itself. `SPEC-storage-engine.md` already flags SurrealDB's Spectron layer as a relevant future building block, which shows the project is infra-aware of this gap without having named or designed the feature. This spec closes that gap.

A neurodivergent adult's working memory is often the exact place that struggles most with holding threads across time. A cognitive companion that also forgets does not reduce that tax; it adds to it. PeT is the mechanism by which Yar keeps its side of the relationship: remembering what the person said, changed their mind about, or asked not to be reminded of, without asking them to repeat themselves.

---

## 2. Definition and scope

**PeT (Personal Temporal knowledge graph)** is a per-person, on-device-first knowledge graph that stores facts about the person's world (people, terms, projects, preferences, events, and free-form facts) along with when each fact was true and when Yar learned it. Facts are asserted, superseded, or retracted over time; nothing is silently overwritten.

**In scope:**
- Node and edge schema for personal facts, typed and free-form.
- Bitemporal fact representation (event time and record time), confidence, and provenance.
- A recall API consumed by the Proofreading agent and the mind-mapping agents (Placer, Reviser), per `SPEC-multi-agent.md`.
- The substrate PeT runs on, chosen from the already-benchmarked options in `SPEC-storage-engine.md`.
- A convergence plan with cytomem, the Cytognosis Foundation's existing Neo4j-based artifact memory system.
- The coupling contract that keeps PeT ops on the same CRDT op-log the sync and storage specs already govern.

**Out of scope:**
- The op-log CRDT library choice itself (Loro vs any-sync vs Automerge); PeT inherits whatever `SPEC-sync-protocol.md` O-1 resolves.
- The L4 graph engine choice for non-PeT data; PeT inherits `SPEC-storage-engine.md`'s decided SQLite-plus-FalkorDB architecture and does not reopen O-1 there.
- Sensor-derived facts (voice, physiological, menstrual, social); those belong to the Cytoscope project and the CSP (Cytonome Sensor Protocol) schema. PeT may store a *derived* fact that a sensor signal produced, once it has crossed the privacy boundary as a permitted signal type, but PeT does not define sensor schemas.
- Model choice or prompting strategy for the agents that write to PeT; that is `SPEC-multi-agent.md`'s territory.

---

## 3. Research landscape (July 2026)

The founder's brief named six systems to check. All six were verified directly; none of the modern ones except HippoRAG were referenced anywhere in the Yar docs before this pass, confirming this is genuinely new engineering ground for Yar, not a rediscovery of an existing decision.

| System | What it is | License | Maintenance signal (July 2026) | Relevance to PeT |
|---|---|---|---|---|
| **HippoRAG 2** | Non-parametric continual-learning memory framework using personalized PageRank over an LLM-extracted knowledge graph; successor to HippoRAG (NeurIPS 2024), itself published as "From RAG to Memory" (ICML 2025) | MIT per the repository's license badge; **confirm the exact `LICENSE` file text before adopting any code**, not just the algorithm pattern | Active OSU-NLP-Group repo, ongoing releases | The graph-plus-PageRank retrieval pattern is a strong reference for PeT's hybrid recall, not a library to embed directly |
| **Zep / Graphiti** | Temporal knowledge graph engine for agent memory; ingests conversational "episodes," extracts entities and relationships, stores them with explicit event-time and ingestion-time annotations | Apache-2.0 | Very actively maintained; 107 releases and 20,000-plus GitHub stars as of 2026, among the most maintained agent-memory engines available | **Closest architectural sibling to PeT.** Its bitemporal fact model (valid time plus system time) and its "old facts are invalidated, not deleted" rule are directly adopted as PeT's supersession semantics in Section 4 |
| **Letta (formerly MemGPT)** | Platform for stateful agents with self-managing memory, git-based context versioning planned | Apache-2.0 | Actively maintained; commercial managed tiers layered on top of the open core | Useful for the agent-side memory-management loop (what to keep in context vs recall on demand), less relevant to PeT's storage schema itself |
| **mem0** | Universal memory layer for AI agents/apps; extraction plus vector plus optional graph store | Apache-2.0 | Very active; 59,600-plus GitHub stars, v2.0 shipped June 2026 | Good reference for a simple extraction-and-recall API surface; its default backend is vector-first rather than temporal-graph-first, a weaker fit for PeT's bitemporal requirement |
| **cognee** | Self-hosted, graph-native "AI memory platform," ECL (extract, cognify, load) pipeline into a knowledge graph | Apache-2.0 (some secondary sources say MIT; Apache-2.0 is the more consistently cited figure and should be the one confirmed against the repo before any adoption) | Active; 12,000 to 27,700 GitHub stars depending on the 2026 snapshot cited, 80-plus contributors | Reference for the ECL pipeline shape (capture to structured graph); not adopted directly since it assumes a pluggable external graph database rather than an embedded on-device one |
| **SurrealDB Spectron** | "Tri-temporal" (a third dimension beyond bitemporal: transaction time, valid time, and decision time) agent-memory layer built directly on SurrealDB, one ACID transaction per memory write, background consolidation of fragmented knowledge | **Proprietary**; early preview, waitlist-gated as of July 2026, no public source or license terms yet | Pre-GA; SurrealDB itself carries the open BSL license question already flagged unresolved in `SPEC-storage-engine.md` O-4 | Confirms the market pattern PeT is built for, but is not adoptable today: no source, no confirmed license, and it sits on SurrealDB, which is already demoted to a candidate GraphRAG projection, not the MVP foundation, per the storage spec |

**Two systems share the name "REMem"; disambiguated per the founder's brief:**

1. **REMem (Reasoning with Episodic Memory in Language Agents)**, Yiheng Shu et al., accepted ICLR 2026 (arXiv 2602.13530). A two-phase framework: an indexing phase that turns utterances into time-scoped fact triples organized as a hybrid graph, and an agentic inference phase that retrieves via a combination of dense embeddings, graph exploration, and lexical search. This is the system PeT's retrieval design borrows from most directly (Section 5); the phrase "REMem-style" in this spec's brief refers to this work.
2. **ReMem (from the Evo-Memory benchmark)**, Google DeepMind and University of Illinois, published December 2025 (arXiv 2511.20857). A "think, act, memory-refine" control loop where an agent actively retrieves, prunes, and reorganizes its own memory mid-reasoning, rather than treating memory as a static store. This is a distinct piece of work; PeT borrows its *consolidation* idea (Section 9's compaction recommendation) but not its retrieval design.

Neither REMem/ReMem system ships a confirmed, permissively licensed, production-ready public repository as of this research pass; both are read as design patterns, not dependencies to install. This matches the caution already flagged in `EFFORT-ESTIMATES.md`.

**Newer or adjacent work surfaced but not adopted:** TOKI (a bitemporal operator algebra for contradiction resolution in agent memory, arXiv 2606.06240) and Memanto (typed semantic memory with information-theoretic retrieval, arXiv 2604.22085) are both 2026 research papers without production repositories; they are read-list items for the fact-consolidation design in Section 9, not build dependencies.

---

## 4. Data model

PeT nodes carry either a **predefined type** (structured, queryable fields) or are a **FreeFact** (a natural-language predicate that does not yet fit a typed schema). Both kinds of node share the same bitemporal, confidence, and provenance envelope.

### 4.1 Node types

| Node type | Purpose | Key fields |
|---|---|---|
| **Person** | Someone the user refers to: family, colleagues, clinicians, friends | `canonical_name`, `aliases[]`, `relationship_role` (free text, e.g. "manager", "sister") |
| **Term** | The user's own vocabulary; project jargon, nicknames, acronyms | `canonical_name`, `aliases[]`, `definition` (user-supplied or inferred) |
| **Project** | A named body of work or personal effort the user is tracking | `title`, `status` (active, paused, done), `thread_id` (link to a brainmap thread, per `SPEC-multi-agent.md` §6) |
| **Preference** | A stated like, dislike, or constraint | `subject_ref` (what the preference is about), `polarity` (prefers, avoids, requires), `text` |
| **Event** | Something that happened at a point or over an interval | `title`, `event_time` (point or interval), `participants[]` (Person refs) |
| **Organization** | A company, institution, or group the user references | `canonical_name`, `aliases[]` |
| **Thread** | A conversational or brainmap thread; a pointer into the CRDT tree, not a duplicate of it | `thread_id`, `title`, `active` |
| **FreeFact** | Anything that does not fit the above; a subject-predicate-object triple in natural language | `subject_ref` (optional; may be free text), `predicate`, `object_text` |

This list is deliberately open-ended. New typed node kinds are added by extending the schema, not by overloading FreeFact; FreeFact exists so that agents are never blocked from recording something true, but a fact that recurs in FreeFact form across sessions is a signal that it deserves a typed promotion (see Section 9, open question 2).

### 4.2 Edge types

| Edge type | From to To | Meaning |
|---|---|---|
| **ASSERTS** | Capture to Fact | Provenance: this capture is the source of this fact |
| **MENTIONS** | Fact to Entity (Person, Term, Project, Organization) | This fact references this entity |
| **SUPERSEDES** | Fact to Fact | The new fact replaces the prior one; the prior fact's validity interval closes, it is never deleted |
| **RETRACTS** | Fact to Fact | The user or an agent explicitly withdrew a prior fact; distinct from supersession because no replacement fact is asserted |
| **RELATES_TO** | Entity to Entity | A generic, typed or untyped relationship (e.g., `works_on`, `alias_of`, `participated_in`) |
| **PLACED_IN** | Fact or Entity to Thread | Links a fact into a brainmap thread, the placement context the Placer agent consumes |

### 4.3 Bitemporal fact envelope

Every fact, typed or FreeFact, carries the same envelope. This is the field set every PeT node instance actually stores:

```yaml
# Illustrative LinkML-style sketch; canonical schema lives in a shared
# cytoskeleton.schemas.petkg module per the cytomem convergence plan (Section 7).
PetFact:
  fact_id:        { range: string, required: true }   # UUID
  node_type:      { range: PetNodeTypeEnum, required: true }
  payload:        { range: JSON, required: true }      # typed fields or FreeFact triple
  event_time:     { range: TemporalInterval }          # when the fact was true in the world; open-ended if ongoing
  record_time:    { range: datetime, required: true }  # when Yar learned it; equals the CRDT op's HLC timestamp
  confidence:     { range: float, required: true }     # 0.0 to 1.0
  asserted_by:    { range: string, required: true }    # agent_id, or "user" for explicit statements
  source_capture_id: { range: string }                 # which capture or turn produced this fact
  status:         { range: PetFactStatusEnum, required: true }  # active | superseded | retracted
  supersedes_id:  { range: string }                    # set if this fact replaces a prior one
  retraction_reason: { range: string }                 # set only if status is retracted
```

**Event time vs record time, worked example.** The user says on 2026-07-19, "I switched teams last month." The **event time** for the fact `works_on: [new team]` is 2026-06-19 (approximately; the interval opens then). The **record time** is 2026-07-19, when Yar's op-log actually recorded it. If the user later says "actually it was two months ago," a new fact is asserted with a `SUPERSEDES` edge to the first; the first fact's `event_time` interval is corrected in the new fact, its own record remains untouched, and both are queryable: "what did Yar believe on 2026-07-19" versus "what actually happened."

**Confidence defaults by source**, until a learned scoring model exists (Section 9, open question 2):

| Source | Default confidence |
|---|---|
| Explicit first-person user statement | 1.0 |
| Proofreading agent NER match against an existing Term or Person | 0.8 |
| Placer or Reviser inference during brainmap placement | 0.6 |
| Derived signal crossing the privacy boundary (see Section 8) | per the signal's own confidence field, never upgraded by PeT |

---

## 5. Retrieval and agent integration

PeT is a **consumer-facing recall service**, not a raw database its callers query directly. Two agents from `SPEC-multi-agent.md` are the primary consumers today, and F66 (ask and summarize) is the third, user-facing consumer.

### 5.1 Recall API

```yaml
# Illustrative surface; final types land in the shared schema package (Section 7)
pet.recall(query: string, as_of: datetime | null, top_k: int) -> [RankedFact]
pet.resolve_entity(text_span: string, context: ThreadContext) -> [EntityMatch]
pet.get_placement_context(node_proposal: string, thread_id: string) -> PlacementContext
pet.assert_fact(fact: PetFact) -> fact_id           # writes a CRDT op; never a direct table write
pet.retract_fact(fact_id: string, reason: string) -> void
```

`as_of` makes every recall call bitemporal-aware: a caller can ask "what did Yar know as of last Tuesday," matching the point-in-time query pattern Graphiti and REMem both rely on.

### 5.2 Proofreading agent: personal-NER context

The Proofreading agent (named as a gap in `FEATURE-VERIFICATION.md` item 7; not yet in the `SPEC-multi-agent.md` agent inventory) calls `pet.resolve_entity` on each span it is uncertain about. Resolution runs a **hybrid match**: exact and fuzzy lexical match over `Term.canonical_name` and `aliases[]` via FTS5, combined with vector similarity over a small embedding of the span via sqlite-vec, fused by reciprocal rank fusion (RRF), the same technique already validated in the storage benchmark's `hybrid_rrf` operation. A match above a confidence threshold is surfaced as a suggested correction or auto-expansion (e.g., expanding a nickname to the `canonical_name`); a low-confidence match is surfaced as a soft suggestion, never a silent rewrite.

### 5.3 Mind-mapping agents: placement context

The Placer and Reviser agents (`SPEC-multi-agent.md` §6) call `pet.get_placement_context` with the current node proposal and thread ID. The call returns:

- Related entities and facts (2-hop graph neighborhood of the thread's existing nodes).
- Recent facts asserted in the same thread, ranked by recency and confidence.
- A short thread summary (node count, active sub-threads), reusing the shape of `BrainmapSessionState` already defined in `SPEC-multi-agent.md` §6.5.

This satisfies the Placer's existing constraint that it "must not make placement decisions that depend on the content of prior transcripts beyond the current session CRDT state": PeT's placement context is structured and derived, not raw transcript text, so consuming it does not violate that boundary.

### 5.4 F66 (ask and summarize): the retrieval consumer

F66 calls `pet.recall` directly, grounded only in the user's own captures and facts, matching its own one-line description in `FEATURE-VERIFICATION.md`: "grounded only in your own notes and highlights." F66 is usable against the existing local store (F52) on day one; PeT recall upgrades its quality once temporal, cross-session grounding is available, which is exactly the two-phase dependency `EFFORT-ESTIMATES.md` already flags for F66 row 11.

---

## 6. Substrate choice (from benchmarks)

**No new database is introduced for PeT.** The benchmarked and decided architecture in `SPEC-storage-engine.md` is reused directly.

| Tier | Engine | Role for PeT |
|---|---|---|
| **Device (primary)** | SQLite + FTS5 + sqlite-vec | `pet_facts` and `pet_edges` tables, layered onto the existing `objects`/`links` schema already implemented in `Yar/src/yar/storage/sqlite_store.py`. FTS5 virtual table over fact text fields; sqlite-vec table over fact embeddings for the hybrid recall in Section 5 |
| **Server (optional projection)** | FalkorDB | Cypher n-hop traversal for cross-session PeT queries at scale, matching the storage spec's decided server-tier role; rebuilt by replaying the op-log, never a second source of truth |
| **Future GraphRAG candidate, not MVP** | SurrealDB (Spectron or native) | Remains a priority future evaluation per the storage spec; PeT does not depend on it, and Spectron itself is proprietary and pre-GA (Section 3), so it is doubly excluded from MVP |

This is a direct extension of `STORAGE-ENGINE-RECOMMENDATION.md`'s architecture diagram: PeT's tables sit inside the existing "Device Projection: SQLite + FTS5 + sqlite-vec" box and the existing "Server Graph Projection: FalkorDB" box. Graph traversal at the device tier (2-hop placement context, Section 5.3) is done as an in-process adjacency-table walk over `pet_edges`, the same accommodation the storage spec already makes for SQLite's lack of native Cypher ("graph semantics require assembling extensions; traversal at scale is slower than a native graph engine," a cost accepted for the device tier and off-loaded to FalkorDB when a server projection exists).

**No LadybugDB dependency.** LadybugDB remains unbenchmarked and gated on a fork-ownership decision (`SPEC-storage-engine.md` O-2); PeT does not wait on it and is not blocked if the team declines fork ownership.

---

## 7. cytomem convergence plan

### 7.1 What cytomem is today

Per `cytomem-README.md` and `cytomem-steering.md`, cytomem is the Cytognosis Foundation's existing persistent memory layer: it tracks artifacts (code, docs, schemas, plans, decisions) across 19 organizational repositories, using **Neo4j** as its graph store, a local ONNX embedder for semantic search, and a schema of Artifact, Episode, Task, and Backlog nodes. It is org-wide and developer-facing, not per-person and not device-embedded. Its own steering doc states the constraint plainly: "zero internal deps... all Pydantic models mirror `cytoskeleton.schemas` for future v1 migration," and its own roadmap already names "Stage C: integrate with fixed cytoskeleton and cytos" as a future step.

### 7.2 Why the systems cannot share one binary today

Neo4j is disqualified as PeT's primary store under the same requirement that disqualified it for Yar's general storage: it is JVM-based, server-only, and does not embed on a phone (`SPEC-storage-engine.md` §3.4). PeT must run on-device first (Section 6); cytomem has no such constraint and gains real value from Neo4j's mature Cypher and GDS tooling for org-wide, developer-facing graph queries. A single shared binary is not currently possible without breaking one of the two systems' hard requirements.

### 7.3 The convergence path (concrete recommendation)

**Converge at the schema and API layer now; converge on one graph engine later, if and when an embeddable option reaches parity with Neo4j's tooling.**

1. **Shared schema package.** Define PeT's bitemporal fact envelope (Section 4.3) as a `cytoskeleton.schemas.petkg` module, following cytomem's own stated migration path ("mirror `cytoskeleton.schemas` for future v1 migration"). This is the single highest-leverage convergence step: it costs one schema definition and unlocks bidirectional borrowing without requiring either system to change its storage engine.
2. **Bidirectional borrowing, concretely:**
   - **cytomem to PeT:** adopt cytomem's proven `Episode` pattern (a snapshot created only when content actually changes, keyed by content hash) as the implementation pattern for PeT's `SUPERSEDES` mechanics; adopt cytomem's idempotent-ingest design (skip unchanged content) for PeT's capture-to-fact pipeline.
   - **PeT to cytomem:** cytomem's `Episode` model today only has record time (when the artifact changed), not valid time (when the fact was true in the world) or an explicit retraction concept. Backport PeT's bitemporal envelope and confidence/provenance fields into cytomem's schema; this gives cytomem a real answer to "when did this decision actually take effect," a question its current schema cannot answer.
   - **A shared recall API shape:** cytomem's `cytomem_recall` MCP tool and PeT's `pet.recall` (Section 5.1) should converge on the same request and response shape, differing only in which corpus (org artifacts vs personal facts) they query.
3. **One engine, deferred.** Revisit a single shared graph engine when either (a) LadybugDB or a similar embeddable graph database clears the benchmark and fork-ownership gate in `SPEC-storage-engine.md` O-2, making an embedded-plus-server topology plausible for both systems, or (b) cytomem's own roadmap moves it toward a device-embedded use case, which is not currently planned. Until then, two engines serving one shared schema is the correct trade, not a compromise to be apologized for.

### 7.4 What this unblocks

- PeT development can proceed immediately without waiting on a cytomem re-architecture.
- cytomem gains a bitemporal upgrade path it already listed as a future integration step.
- Neither team inherits the other's hard platform constraint (JVM server-only vs mobile-embedded).

---

## 8. Coupling contract (sync x storage x PeT)

A sibling agent is drafting `SPEC-sync-protocol.md` in parallel. This section is the explicit interface contract between that spec, `SPEC-storage-engine.md`, and this one.

**PeT fact assertions and retractions are ops on the same CRDT op-log as every other Yar write.** There is no separate PeT log. The op envelope:

```yaml
# Op envelope, shared across all Yar op types, PeT included
Op:
  id:          # UUID, idempotency key
  device:      # device_id that originated the op
  timestamp:   # Lamport or HLC (hybrid logical clock) timestamp; total order for replay
  actor:       # agent_id, or "user" for explicit user action
  entity_type: # "pet_fact" | "pet_edge" | "pet_retraction" | other existing types
  payload:     # the PetFact or edge body from Section 4
```

- **The Yar reducer stays authoritative.** PeT's `pet_facts` and `pet_edges` SQLite tables are, like `objects` and `links` before them, a **derived, rebuildable projection** of the op-log, not a second source of truth. `pet.assert_fact` and `pet.retract_fact` (Section 5.1) write an op; they never write the SQLite tables directly. This is the same principle `SPEC-storage-engine.md` §1 already establishes for the L4 engine generally, applied to PeT specifically.
- **PeT does not pick a CRDT container type independently.** Whichever library wins `SPEC-sync-protocol.md` O-1 (Loro plus Iroh is the current 36-vs-35 leaning; any-sync is the fallback) is what PeT's ops travel through. If Loro is adopted, `pet_edges` maps naturally onto Loro's `Map` container and `Thread` placement onto the same movable `Tree` container the brainmap already uses (`SPEC-multi-agent.md` §6.3); this is a reuse of an already-decided container pattern, not a new one.
- **PeT ops must pass the same 12-case sync conformance bar** `SPEC-sync-protocol.md` §3.2 already defines for every op type (idempotency, ordering, chunking, crash/resume, device lifecycle, conflict/tombstone, tie-breaking, partition healing, blob handling, anti-pattern guard). A `SUPERSEDES` or `RETRACTS` op is exactly the kind of "delete/update race" case that section's conformance suite already covers; no new test category is required, only new fixtures using PeT payloads.
- **Undo is inherited, not reinvented.** Because PeT facts are ops, the existing undo-by-replay guarantee (`SPEC-multi-agent.md` §6.4: "undo is always available... the CRDT op-log is the source of truth") applies to fact assertions and retractions with no additional engineering.

---

## 9. Privacy and CAP

**PeT never leaves the device unencrypted.** This follows directly from `SPEC-data-sovereignty.md` P1 (device-first) and P3 (zero-knowledge relay): the device op-log, PeT's tables included, is plaintext at rest only until the SQLCipher migration lands (already tracked as a gap in that spec's Section 4.1), after which PeT rows are encrypted exactly like every other row in the same tables.

**CAP governs any cross-boundary use of a PeT fact.** Concretely:

- A raw PeT fact (a `Person`, `Term`, `Preference`, or `FreeFact` row) is classified **Device-local** under `privacy-boundary-spec.md`'s trust-boundary taxonomy, the same classification the Transcriber's raw transcript buffer already carries. It MUST NOT appear in any `Directive` payload, `ExecutionReport`, or log entry that targets an external recipient.
- Only the Supervisor may emit a `CrossBoundarySignal`, and only one of the seven permitted derived-signal types (`privacy-boundary-spec.md` §3.1) may cross. A PeT fact is never itself one of those seven types; if a derived signal is built *from* PeT facts (for example, a mood-arc signal informed by a Preference node), the derivation happens on-device and only the derived, already-abstracted signal crosses the PEP gate, never the source fact.
- **CapLiteGuard's existing boundary categories extend naturally to PeT writes.** A fact that would encode a diagnosis, a treatment claim, or a health-risk score is blocked at assertion time by the same guard that already blocks those categories at conversation time (`SPEC-multi-agent.md` §5.4); PeT does not need a second safety gate, it sits behind the one that already exists.
- **Confidence and provenance are the CAP-relevant fields.** A low-confidence, agent-inferred fact (Section 4.3's 0.6 default for Placer/Reviser inference) must never be surfaced to the user or to another agent as if it were a confirmed statement; UI and agent-facing summaries hedge below a threshold (e.g., "Yar thinks you might mean..." rather than a flat assertion).
- **Retraction is a right, not a delete.** Consistent with `SPEC-data-sovereignty.md` P4 (export as a right) and P5 (no dark patterns), a user-initiated "forget this" action writes a `RETRACTS` op; it does not silently erase the op-log entry, preserving the audit trail `SPEC-data-sovereignty.md` §6 already requires, unless the user separately invokes full local data deletion (`SPEC-data-sovereignty.md` §5, "Data deletion" consent gate), which is a distinct, export-first, double-confirmed action.

---

## 10. Risks

| Risk | Description | Mitigation |
|---|---|---|
| **Fact pollution from low-confidence inference** | An agent asserts a plausible-sounding but wrong fact (a misheard name, a wrong project association), and it persists because nothing challenges it | Confidence scoring (Section 4.3) plus a UI surface for the user to correct or retract a fact on sight; agent-asserted facts below a threshold are never shown as settled |
| **Unbounded op-log growth from continuous inference** | Placer/Reviser and the Proofreading agent could assert facts on every turn, growing the log faster than the person's actual life changes | A periodic on-device consolidation pass (Section 9, open question 1) that merges near-duplicate FreeFacts and retires stale low-confidence facts, borrowing the "prune and reorganize" idea from the DeepMind ReMem pattern (Section 3) |
| **Cross-boundary leakage via agent context** | A Supervisor Directive to an external tool could accidentally include PeT fact text if a payload builder is careless | The CAP PEP gate (Section 9) is the enforcement point; a test asserting no raw PeT fact text ever appears in a `CrossBoundarySignal` payload is part of the test plan (Section 11) |
| **Sensitive inference without consent** | An agent could infer a health-adjacent fact (mood pattern, a disclosed diagnosis mentioned in passing) and store it as a durable FreeFact without the same scrutiny a live conversation gets | CapLiteGuard's existing health-risk-scoring and diagnosis-term categories (Section 9) apply at assertion time, not only at conversation time |
| **cytomem and PeT schema drift** | If the shared schema package (Section 7.3) is not adopted early, the two systems diverge and convergence becomes progressively more expensive | Land the `cytoskeleton.schemas.petkg` module before either system's schema is extended further; treat schema drift as a blocking review item, not a backlog item |
| **Vendor dependency on an unreleased product** | Building against SurrealDB Spectron speculatively, before it is GA or its license is public | Not adopted for MVP (Section 6); revisit only after GA and a confirmed, commercially usable license |
| **License risk on research-derived code** | Copying implementation details from a paper's reference code (HippoRAG, REMem, ReMem) without checking that specific repository's license | Every library and reference implementation in Section 3 carries an explicit license note; none are embedded as dependencies in this spec, only as design patterns |

---

## 11. Test plan

| Test | What it verifies |
|---|---|
| **Reducer conformance** | Replaying a sequence of `pet_fact` and `pet_edge` ops from a fresh op-log produces the correct `pet_facts` and `pet_edges` table state, matching the existing reducer test pattern for `objects`/`links` |
| **Bitemporal query correctness** | An `as_of` recall query returns the fact version that was true at that point in record time, not the latest version, across a scripted sequence of assertions and supersessions |
| **Supersession and retraction correctness** | A superseded fact's prior row is marked inactive, never deleted; a retracted fact carries a `retraction_reason` and is excluded from default recall but present in an explicit history query |
| **Recall precision and recall** | `pet.recall` against a synthetic personal-fact dataset meets a minimum precision and recall bar; benchmarked using the same harness pattern as the PATCH10 storage benchmark |
| **Proofreading resolution accuracy** | `pet.resolve_entity` correctly resolves a sample of aliases, nicknames, and typos against seeded Person and Term nodes, both exact and fuzzy match paths |
| **Placement context latency** | `pet.get_placement_context` returns within the on-device edge latency budget (under 200ms per `SPEC-multi-agent.md` §7.1) for a thread of representative size |
| **Privacy leakage test** | No raw PeT fact text appears in any `CrossBoundarySignal` payload, `Directive` payload, or `ExecutionReport` across a scripted multi-agent session |
| **cytomem schema conformance** | The shared `cytoskeleton.schemas.petkg` Pydantic models validate correctly against both the PeT SQLite projection and cytomem's Neo4j-backed model |
| **Sync conformance** | PeT-payload ops pass all 12 cases of the sync edge-case benchmark already defined in `SPEC-sync-protocol.md` §3.2, using PeT-specific fixtures for the conflict and tombstone cases |
| **Guard interception** | A scripted attempt to assert a diagnosis-shaped or health-risk-shaped FreeFact is blocked by `CapLiteGuard` at assertion time, not only at conversation time |

---

## 12. Open questions (each with a recommendation)

1. **How often should fact consolidation run, and what triggers it?**
   Recommendation: a background pass during device charging or app idle, not on every write; modeled on the DeepMind ReMem "prune and reorganize" loop (Section 3). Do not run consolidation synchronously in the write path.

2. **What confidence-scoring model should PeT use beyond the source-type defaults in Section 4.3?**
   Recommendation: ship the simple rule-based defaults for MVP; do not build a learned confidence model before real usage data exists to train or validate one. Revisit after Wave 0 ships.

3. **Should cytomem and PeT ever share one graph engine binary, not just a schema?**
   Recommendation: not for MVP. Converge at the schema and API layer now (Section 7.3); revisit a single engine only if an embeddable graph database clears `SPEC-storage-engine.md` O-2, or if cytomem's own scope moves toward device embedding, neither of which is currently planned.

4. **Should PeT build against SurrealDB Spectron given how directly it matches the founder's brief?**
   Recommendation: no, not yet. Spectron is proprietary, pre-GA, and waitlist-gated as of July 2026 (Section 3); it also inherits SurrealDB's own unresolved BSL license question (`SPEC-storage-engine.md` O-4). Revisit at GA with a confirmed license.

5. **Should retracted facts be visible to the user by default, or only on request?**
   Recommendation: hidden from default recall, visible through an explicit "memory history" view. This matches the export-as-a-right principle (`SPEC-data-sovereignty.md` P4) without cluttering everyday recall with stale facts.

6. **How should PeT resolve two devices asserting contradictory facts before sync completes?**
   Recommendation: last-assertion-wins by record time, with a surfaced conflict card the user can resolve manually, consistent with how `SPEC-sync-protocol.md`'s `delete_update_race` cases are already handled for other op types. Do not silently pick a winner without surfacing the conflict.

7. **What is the maximum retention depth for PeT's op-log specifically, separate from the general op-log?**
   Recommendation: no separate policy; defer to `SPEC-multi-agent.md` O-5's general op-log retention decision, which already flags HIPAA data-retention coordination with counsel as a prerequisite. Do not set a PeT-specific retention rule ahead of that decision.

---

## Cross-references

- `SPEC-storage-engine.md`, the decided SQLite plus FTS5 plus sqlite-vec device tier and FalkorDB server tier this spec builds on directly.
- `SPEC-sync-protocol.md`, the CRDT op-log and transport layer PeT ops travel through; the coupling contract in Section 8 is the explicit interface between the two specs.
- `SPEC-multi-agent.md`, the Proofreading and mind-mapping (Placer, Reviser) agents that consume PeT's recall API; the brainmap loop and `BrainmapSessionState` shape reused in Section 5.3.
- `SPEC-data-sovereignty.md`, the device-first trust boundary, encryption requirements, and export-as-a-right principle governing every PeT row.
- `cytomem-README.md`, `cytomem-AGENTS.md`, `cytomem-steering.md`, the existing Neo4j-based org memory system this spec's Section 7 proposes converging with.
- `FEATURE-VERIFICATION.md`, F67 (long-term personal memory graph) and F66 (ask and summarize your captures), the two feature anchors this spec implements.
- `EFFORT-ESTIMATES.md`, the PeT effort range (35 to 65 engineer-weeks, the highest of any Wave 0 component) and its explicit flag that "PeT" was undefined prior to this spec.
- `privacy-boundary-spec.md` (Cytoplex), the `CrossBoundarySignal` schema and PEP gate this spec's Section 9 relies on without redefining.

---

<details>
<summary><strong>Glossary</strong></summary>

- **PeT (Personal Temporal knowledge graph):** The long-term personal memory layer defined in this spec. Not to be confused with cytomem, which is the Foundation's org-wide, Neo4j-based artifact memory.
- **Bitemporal:** Tracking two independent timelines per fact: event time (when it was true in the world) and record time (when Yar learned it). A query can ask about either dimension independently.
- **Event time:** The validity interval of a fact in the world, open-ended if the fact is still true.
- **Record time:** The timestamp Yar's op-log actually recorded the fact; equals the CRDT op's HLC (hybrid logical clock) timestamp.
- **Supersession:** A new fact explicitly replacing an older one; the older fact's row is marked inactive, never deleted.
- **Retraction:** An explicit withdrawal of a fact with no replacement asserted; distinct from supersession and always reversible via the op-log.
- **FreeFact:** A catch-all node type for a natural-language subject-predicate-object triple that does not yet fit a typed schema entry.
- **RRF (reciprocal rank fusion):** The ranking method PeT uses to combine lexical (FTS5), vector (sqlite-vec), and graph-neighborhood results into one ranked list.
- **REMem (ICLR 2026):** Yiheng Shu et al.'s episodic-memory reasoning framework; the retrieval design this spec's Section 5 borrows from. Distinct from ReMem below.
- **ReMem (Evo-Memory, December 2025):** DeepMind and University of Illinois's self-evolving memory control loop; the consolidation pattern this spec's Section 9 borrows from. Distinct from REMem above.
- **Spectron:** SurrealDB's proprietary, pre-GA agent-memory layer; referenced as market context in Section 3, not adopted for MVP.
- **CAP (Cytognosis Authority Protocol):** The governance protocol that gates any cross-boundary use of a PeT fact, per Section 9.
- **CSP (Cytonome Sensor Protocol):** The universal sensor schema standard, owned by Cytoscope, not by this spec; referenced only to mark PeT's scope boundary in Section 2.

</details>
