---
title: "Yar Storage and Sync Architecture: Consolidation Digest"
date: "2026-06-21"
author: "consolidation agent"
status: "synthesis (all open decisions remain open)"
tags: [yar, storage, sync, crdt, cytoplex, graph-db, surrealdb, loro, iroh, any-sync, solid]
sources:
  - "~/Downloads/Yar-Graph-DB-Picker-Visual-Guide.md"
  - "~/Downloads/yar_db_simplified.md (identical to above)"
  - "~/Downloads/Yar-SingleEngine-AnySync-Solid-Addendum.md"
  - "~/Downloads/Yar-Data-Fabric-Simple-Visual-Guide.md"
  - "~/Downloads/Yar-Sync-Architecture-anysync-vs-loro-iroh.md"
  - "consolidation_2026-06-21/_research/E_storage_sync_ingestion.md (prior ingestion pass)"
  - "consolidation_2026-06-21/_research/F_db_benchmark_ingestion.md (Ali's benchmark)"
existing_specs_reconciled:
  - "04-Engineering/yar/research/yar-substrate-decision.md"
  - "04-Engineering/yar/research/solid-pods-comprehensive.md"
  - "03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md"
  - "03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md"
---

# Yar Storage and Sync Architecture: Consolidation Digest

**BLUF:** The architectural keystone is decided: a CRDT op-log is the single source of truth, and the graph engine is a derived, swappable index rebuilt by replaying it. Everything below that keystone is under evaluation. The two live decisions are (1) which graph/storage engine to use at L4 and (2) which sync protocol to use at L2. Both have a recommended front-runner; neither is committed.

---

## 1. Database and Storage Options

### 1.1 Decision Criteria

Six criteria are make-or-break for a health companion:

| Criterion | Implication |
|---|---|
| Embeds on iOS + Android | Disqualifies 6 of 9 candidates evaluated |
| Single-engine everywhere | Narrows field to SurrealDB or SQLite stack under strict reading |
| CRDT / offline-first convergence | Required; no candidate ships it out of the box |
| 2-year vendor survival | Weighted as heavily as benchmarks for a healthcare product |
| HIPAA pathway (encryption, BAA) | Mandatory; shapes blob and pod hosting |
| License for commercial PBC | Must be MIT, Apache, or source-available with clear embed terms |

### 1.2 Candidate Profiles (storage / graph engine, L4)

**Neo4j**
- Labeled property graph, Cypher, JVM, server-only.
- Best GraphRAG tooling; $581M raised, IPO-prep, lowest vendor risk of the nine.
- Cannot embed on a phone. Disqualified as primary store under the single-engine rule.
- Role: cloud GraphRAG / supervisor tier only (Architecture C).

**SQLite stack** (SQLite + sqlite-vec + optional Cypher extensions)
- Ships on every phone, public domain, SQLCipher for HIPAA, PowerSync or CR-SQLite for sync.
- Graph semantics assembled from extensions; no off-the-shelf Cypher on device; slower traversals at scale.
- Survives both interpretations of the single-engine rule by sheer ubiquity.
- Role: device tier front-runner, Architecture C, safest fallback.
- Benchmark result (Ali, 2026-06-21): validated as the default for phone and laptop MVP. SQLite + FTS5 + sqlite-vec wins across phone and laptop tiers.

**FalkorDB**
- Labeled property graph on Redis, Cypher, vectors-on-edges, ex-Redis team, funded.
- Server-only (Redis module), no phone embedding.
- Disqualified as primary under single-engine rule.
- Benchmark result: wins on personal-server graph workloads.
- Role: cloud GraphRAG option alongside Neo4j.

**SurrealDB**
- Multi-model (graph, relational, document, KV, time-series), SurrealQL, native HNSW, VERSION time-travel, Spectron agent-memory layer, Surrealism WASM extensions, native file support. Rust core.
- Funding: ~$44M total; $23M Series A extension Feb 2026 (FirstMark, Georgian, Chalfen, Begin Capital); Forbes AI 50 2026.
- Architecture 3.0: released Feb 2026 as a correctness-motivated rewrite. Synced writes by default, redesigned on-disk representation. Short production track record on current architecture.
- Single-engine pitch: "embedded, at the edge, or as a highly-scalable cluster, same engine everywhere." Mobile FFI path (Flutter/iOS/Android) is thin and early-adopter territory.
- Benchmark result (Ali, 2026-06-21): completed all runs but full-text index creation failed (fell back to CONTAINS); task-lookup and cold-open latency are almost certainly configuration artifacts, not a ceiling. A targeted retest is required before ruling out or committing.
- De-risking requirements: (a) CRDT log behind it; (b) own soak test of mobile path; (c) MVP avoids Spectron, Surrealism, and native file features; (d) confirm BSL license for commercial PBC before launch.
- Status: co-front-runner with SQLite stack under single-engine rule. Under evaluation.

**LadybugDB** (Kuzu fork)
- Kuzu was the ideal embedded graph DB for on-device GraphRAG. Apple acquired it October 9, 2025 and archived the repo the next day.
- LadybugDB is the best active fork. iOS embedding works. Android binding is DIY (weeks of work). No cloud clustering.
- The entire "embedded graph DB for on-device AI" category is unsettled for 12-24 months.
- Status: viable if the team is willing to own a small fork of an archived upstream. If not, Architecture C is the fallback.

**Anytype** (design reference only, not an engine)
- Perfect sync model (any-sync), CRDT/DAG-based, self-hostable, time-travel. Not embeddable as a backend; no Cypher/SQL/graph-walk traversal API.
- ASAL-licensed clients cannot be used in a commercial product.
- Role: steal the design; do not adopt the app or engine.

**Kuzu** - Dead. Apple acquired and archived the repo. See LadybugDB above.

**Memgraph** - C++ in-memory graph, vectors in 3.8. No Series A in 8 years, ~25 people. Server-only. Cloud maybe; disqualified as primary.

**Dgraph** - Two acquisitions in 24 months (Hypermode then Istari), founder left. Skip.

**JanusGraph** - JVM, 2-person commit base, stagnating, no vectors. Skip.

**`any-store`** (anyproto, MIT)
- Embedded SQLite-backed document store, Mongo-like API, used inside anytype-heart.
- Pre-1.0, "APIs may change." Adoptable as a local store supporting component.

### 1.3 The Three Architecture Patterns

| Pattern | Engine stack | Wins | Costs |
|---|---|---|---|
| A: "Best Tech" | LadybugDB on device + Loro CRDT + Iroh | Fastest on-device graph, native vectors, MIT throughout, matches existing L0 stack | LadybugDB = small fork, Android binding DIY, CRDT-to-graph reducer = custom code |
| B: "Elegant Bet" | SurrealDB everywhere + CRDT log | One engine, one query language, best native time-travel (VERSION), graph+vector+text+time in one query | Mobile FFI unofficial, 3.0 correctness rewrite is months old, sync still custom |
| C: "Safest" | SQLite + sqlite-vec on device + Neo4j/FalkorDB in cloud | Lowest risk, SQLite everywhere, HIPAA via SQLCipher, best GraphRAG in cloud, swap any layer | No off-the-shelf Cypher on device, two engines to maintain, slower traversals |

Under the strict single-engine rule, only Architecture B (SurrealDB) and Architecture C (SQLite stack as the single tier, server-only DB demoted to optional read index) survive. Under the preferred interpretation (CRDT log is the single source, engine is a swappable read index), all three survive.

---

## 2. The Single-Engine Decision and AnySync / Solid (from the Addendum)

### 2.1 Two Interpretations of "No Drift"

The addendum establishes that "no drift" can be read two ways, and they lead to different answers:

1. **Literal one-engine binary on every tier.** Surviving candidates: SurrealDB (by design) and SQLite stack (by ubiquity). All hybrid architectures (A and C) are eliminated.
2. **One logical source of truth; read-index may differ per tier.** The CRDT log is the single source; any engine is a materialized view. Convergence is guaranteed mathematically rather than hoped for operationally. This is the stronger engineering answer.

Interpretation 2 is recommended. It also makes the engine choice lower-stakes and reversible.

### 2.2 SurrealDB as Co-Front-Runner

Under interpretation 2, SurrealDB is the recommended front-runner because it is the only candidate whose roadmap matches every Yar axis simultaneously: one engine everywhere, native knowledge graph, bi-temporal data, multimodal (native file support), vectors, and an agent-memory layer (Spectron). The risk is concentration: betting the whole platform on a single young vendor's recently-rewritten engine, plus headline AI features that shipped within the last few months.

Adoption path if SurrealDB is chosen: maintain the CRDT log as the true source, pin a version, run a multi-week iOS and Android crash/restore/corruption soak before committing, and treat Spectron/Surrealism/native files as upside only, not MVP foundation.

### 2.3 any-sync Adoptability

The addendum establishes that any-sync is adoptable, not just inspirational. The MIT-licensed protocol and self-hostable node set give you Anytype's exact local-first E2E P2P design legally. Only the ASAL-licensed client/middleware and the object model must be reimplemented.

Component verdict:
- **Adopt as-is (MIT):** `any-sync` (protocol), `any-sync-node`, `any-sync-filenode`, `any-sync-coordinator`, `any-sync-consensusnode`, optionally `any-store`.
- **Adopt the design, reimplement:** object/type/space/relation model, key-custody specifics, ACL semantics mapped to privacy-boundary schema.
- **Do not adopt:** `anytype-ts`/`-swift`/`-kotlin` (ASAL), `anytype-mcp` (desktop bridge), the Anytype query surface as the graph API.

This makes any-sync a direct competitor to the Loro+Iroh stack, not just a design reference.

### 2.4 Solid Protocol Prioritization

Solid's role is framing-settled: it is the patient-ownership and portability layer, not the runtime database. The hot path stays the CRDT log + graph engine. Solid pods are the user-controlled, standards-based home that lets a patient take their data elsewhere and grant/revoke app access.

No public pod provider offers a HIPAA Business Associate Agreement. For PHI, enterprise-hosted Cytognosis-operated pods are required.

| Horizon | Implement |
|---|---|
| Now (stable + implemented) | Core Solid Protocol resource model (export/portability, not hot path), WebID, Solid-OIDC, WAC, self-hosted pod (CSS for prototype) |
| ~6 months (near-stable, worth waiting) | ACP (v0.9.0, primarily ESS), Solid Notifications (WebSocket/Webhook), Type Indexes |
| Wait / do not build | SAI v0.1.0 (too complex, too early), Shape Trees (sparse impls), Solid DID Method (unofficial draft, use `did:web` instead), HTTPSig, Solid-PREP/Chat/ERP |

---

## 3. The Data Fabric Concept

The data fabric is the complete layered substrate under the Cytonome agents. It is described as an 8-layer stack. The key insight: Layer 2 (sync/CRDT) is the subject of the sync decisions; Layer 4 (graph engine) is the subject of the DB-picker decisions. The fabric integrates both.

| Layer | Label | Decided / Open |
|---|---|---|
| L7 | Agents (Gemma E2B + 26B MoE, Dapr+NATS, MCP surface) and UI (Flutter+Rive, Tauri+React) | Decided |
| L6 | Consent and Access (privacy-boundary schema, WAC now / ACP ~6mo, Solid pods as portability mirror) | Core decided; ACP scheduled |
| L5 | Vectors and GraphRAG (HNSW; native if SurrealDB, else sqlite-vec) | Follows engine choice |
| L4 | Graph index and query (SurrealDB, LadybugDB, or SQLite stack; materialized from op-log) | Open; SurrealDB is front-runner |
| L3 | Storage (local store per engine; encrypted blob store TBD: iroh-blobs or any-sync-filenode) | Tied to sync choice |
| L2 | Replication and Convergence / Cytoplex core (CRDT op-log = source of truth; engine TBD) | Decided in principle; engine open |
| L1 | Identity and Keys (WebID, Solid-OIDC, did:web, per-space keys) | Core decided |
| L0 | Transport and Discovery (mDNS/DNS-SD, Tailscale, Iroh) | mDNS + Tailscale decided; Iroh explored |

**Naming note:** The sync architecture docs used "Cytoplex" as the data fabric label and "CAP" as the consent layer. Both are inferred mappings that need confirmation from Shahin. The technical content is unaffected by naming.

---

## 4. Cross-Node Sync: any-sync vs Loro vs Iroh

### 4.1 Scoring (1-5 on nine criteria, /45)

| Engine | Mobile | P2P/CRDT | E2E | Self-host | License | Maturity | Composability | Effort | Stack-fit | Total |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **any-sync** | 3 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | **35** |
| **Loro** | 4 | 4 | 3 | 4 | 5 | 3 | 5 | 3 | 5 | **36** |
| Automerge 3.0 | 4 | 4 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | **36** |
| Yjs/yrs | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 3 | 3 | **34** |

The scores are within one point. The decision is about preferred risk profile and language, not raw capability.

### 4.2 any-sync (Option A: adopt a stack)

- **What it is:** Anytype's complete local-first P2P E2E protocol plus four self-hostable Go server nodes.
- **CRDT model:** Merkle-DAG of operations per object (change-DAG). Content-addressed; peers exchange missing nodes and converge. Proven convergence; tamper-evident; opinionated object/space model.
- **Components:** coordinator node (membership/directory), sync node (relays encrypted change-DAG), file node (encrypted blobs, IPLD/IPFS-derived), consensus node (ACL log head/ordering), optional any-sync-bundle for self-hosting.
- **Identity/keys:** per-space symmetric keys wrapped to member identities; no central account registry; servers see ciphertext only. True E2E, server-blind storage. Key custody, recovery, and break-glass are the adopter's responsibility.
- **Transport:** QUIC + Yamux; TLS identities.
- **Maturity:** production-proven at Anytype's full userbase. Most mature option.
- **Tradeoffs:** turnkey, complete, proven; Go-centric (heavier mobile path); 4-node topology; opinionated object model must be reimplemented to avoid ASAL entanglement.
- **Fallback trigger:** if building ACL + key custody + relay from parts (Option B) proves too costly in engineering time, adopt the any-sync node set wholesale rather than half-building it.

### 4.3 Loro (core of Option B)

- **What it is:** A Rust CRDT library with first-class mobile bindings (Swift + `flutter_rust_bridge`).
- **CRDT algorithm:** Fugue for text; movable Tree CRDT for hierarchical/graph data; Eg-walker-style event graph; built-in version DAG with time-travel.
- **Container types:** Text, List, MovableList, Map, Tree, Counter.
- **Why Tree matters:** maps naturally to graph adjacency (nodes as Tree entries, edges as Map entries); time-travel built in for longitudinal health data.
- **vs Automerge 3.0:** both score 36/45. Loro wins on movable-Tree CRDT and built-in time-travel. Automerge wins on maturity and memory efficiency (~10x memory reduction in 3.0). Prototype Loro first; Automerge is the drop-in fallback within Option B.
- **vs CR-SQLite:** CR-SQLite is stalled; avoid.
- **Stated leaning:** Loro is recommended first; prototype it. Switch to Automerge 3.0 if Loro integration proves too costly.

### 4.4 Iroh (P2P transport, Option B)

- **What it is:** Modular Rust networking stack. "Dial keys, not IP addresses." v0.95 (November 2025), actively developed.
- **Modules:** `iroh` core (QUIC by public key, hole-punching, relay fallback), `iroh-blobs` (BLAKE3-verified content-addressed blob transfer, pre-1.0), `iroh-gossip` (epidemic broadcast, eventual + unordered), `iroh-docs` (de-emphasized by n0; budget to write your own reconciliation if needed).
- **Integration with existing stack:** mDNS and Tailscale are already adopted at L0. Iroh was already explored for distributed session state. Option B reuses three existing L0 decisions; this gives it a head start on stack-fit.
- **Stated leaning:** Iroh is the recommended P2P transport for Option B, with mDNS (LAN) and Tailscale (overlay) already decided alongside it.

### 4.5 Leaning Summary (not a final decision)

The source documents state a leaning toward Option B (Loro + Iroh) by a margin of 36 vs 35, driven primarily by:
- Best mobile path (Rust + Flutter + Swift bindings).
- All-MIT/Apache throughout; no ASAL entanglement.
- Composability: engine-agnostic op-log, swap L4 freely.
- Stack-fit: Iroh, mDNS, and Tailscale already in the stack.

The recommendation is to build on Loro + Iroh and borrow any-sync's design for the parts that must be built from scratch: per-space key wrapping, ACL head-sync, content-addressed encrypted blob store (iroh-blobs in the filenode role). If building those proves too costly, adopt any-sync wholesale.

**This leaning is documented in the source materials but is not a committed decision.**

---

## 5. Decision State

### Decided / Locked In

| Component | Status |
|---|---|
| CRDT op-log = single source of truth | Decided (all source docs agree) |
| L4 graph engine = derived swappable index, rebuilt by replaying op-log | Decided as architectural principle |
| L0: mDNS/DNS-SD (LAN discovery) | Decided |
| L0: Tailscale overlay | Decided |
| L0: Iroh (explored, tentatively in stack) | Explored; in stack for session state |
| L7: Gemma 4 E2B (interviewer), Gemma 4 26B MoE (supervisor), Dapr+NATS | Decided |
| L7 UI: Flutter+Rive (mobile), Tauri+React (desktop) | Decided |
| L1: WebID + Solid-OIDC + did:web | Core decided |
| L6: WAC now, ACP at ~6 months, enterprise-hosted Solid pods for PHI | Core decided; ACP scheduled |
| Solid = portability layer, not hot-path database | Decided |
| No public HIPAA-compliant pod provider; must self-host pods | Decided |
| Use `did:web`, not Solid DID Method | Decided |
| SOSA/SSN for sensor data vocabulary | Decided |
| Kuzu is dead; LadybugDB is the fork; embedded-graph-DB category unsettled 12-24 months | Fact |
| Do not adopt anytype-ts/swift/kotlin (ASAL) in a commercial product | Decided |
| any-store is a supporting local-store component, not a primary graph engine | Decided |

### Open / Under Evaluation

| # | Decision | Current leaning (not committed) | Key constraint or blocker |
|---|---|---|---|
| 1 | L4 graph engine: SurrealDB vs SQLite stack vs LadybugDB | SurrealDB front-runner (single-engine rule + feature fit); SQLite stack = safest fallback | SurrealDB 3.0 mobile soak test (iOS + Android, multi-week) required before committing; benchmark retest needed (FTS config artifact) |
| 2 | L2 sync engine: any-sync (Option A) vs Loro+Iroh (Option B) | Lean Option B (Loro+Iroh); any-sync is the fallback/escape hatch | Backend language preference (Go vs Rust); appetite for building ACL/key custody from parts vs adopting 4-node topology |
| 3 | CRDT library within Option B: Loro vs Automerge 3.0 | Prototype Loro first (movable-Tree + time-travel); Automerge 3.0 is the drop-in fallback | Both score 36/45; decision is operationally low-stakes; prototype resolves it |
| 4 | Key custody + ACL design | Borrow any-sync's per-space key wrapping and ACL head-sync design; reimplement against privacy-boundary schema | Healthcare break-glass and runtime-updatable policy (PAP) are load-bearing sub-problems |
| 5 | LadybugDB fork ownership | Team must decide: willing to own a small fork of archived upstream? If no, Architecture C | Kuzu upstream archived; Android binding DIY |
| 6 | SurrealDB BSL license for commercial PBC | Confirm text before launch | Not yet checked against PBC structure |
| 7 | Cytoplex / CAP naming in layer diagram | Needs correction from Shahin | Sync-architecture docs used inferred mappings; technical content unaffected |
| 8 | Benchmark retest: SurrealDB | Ali's run had FTS config artifact; retest with correct full-text index config before ruling in or out | Required before commitment |

---

## 6. Reconciliation Map (Existing Repo Specs)

### `docs/04-Engineering/yar/research/yar-substrate-decision.md`
- **Date:** 2026-06-14
- **Covers:** PKM platform evaluation (Anytype, Obsidian, Tana, Logseq, Capacities, Notion, AppFlowy, SiYuan, Trilium, Joplin). Recommends hybrid Yar-owned runtime + Obsidian shell for MVP; Yar-native local-first object runtime long-term. Establishes SQLite as the MVP local object store.
- **Overlap:** Shares the conclusion that a custom local-first stack is the long-term path. Its mention of SurrealDB, RxDB, ElectricSQL, and Replicache is brief and predates the full nine-DB evaluation. Does not cover Loro, Iroh, any-sync, Solid, or the CRDT-log-as-source-of-truth architecture.
- **Action:** Do not merge. Keep as the product-level rationale for why a Yar-owned runtime is required. Cross-reference from the new storage/sync spec. Update or annotate the SQLite recommendation to note it is a subset of Architecture C and that a fuller DB/sync analysis now exists.

### `docs/04-Engineering/yar/research/solid-pods-comprehensive.md`
- **Date:** 2026-05-25
- **Covers:** Comprehensive Solid ecosystem research: protocol maturity, server implementations, health data architecture, FHIR integration, encryption, Cytognosis integration roadmap. Recommends CSS for prototype; Inrupt ESS for production; self-hosting for HIPAA.
- **Overlap:** Predates the addendum's Solid prioritization framework (now/6-months/wait-for-it). Core findings are consistent but do not include the ACP-vs-WAC sequencing or the HIPAA-BAA constraint. Does not address Solid's positioning within the 8-layer data fabric.
- **Action:** Do not merge. Keep as the detailed Solid ecosystem reference. Annotate with a forward-reference to the addendum's prioritization framework (ACP at ~6 months; SAI/ShapeTrees deferred). The new storage/sync spec supersedes the addendum table; the comprehensive doc is still useful for server comparison detail.

### `docs/03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md`
- **Date:** 2026-06-21
- **Covers:** Privacy boundary between Yar's on-device worker zone and external recipients (supervisor, clinician, services). CrossBoundarySignal schema, EARS requirements, data classification, retention and consent rules, CAP enforcement (PEP/PDP/PAP/PIP). Open decisions include PAP implementation, retention TTLs, and clinician-path HIPAA posture.
- **Overlap:** Directly implements the L6 consent layer in the data fabric. The phone-to-supervisor boundary maps to the L2/L6 ACL layer. The PAP open decision in this spec is the same open decision in the sync architecture (runtime-updatable policy).
- **Action:** Do not merge; scopes are complementary. Cross-reference both ways: storage/sync spec cites privacy-boundary-spec as the L6 data contract; privacy-boundary-spec references the sync architecture as its transport substrate. Consolidate the PAP tracking so it is resolved in one place and reflected in both.

### `docs/03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md`
- **Date:** 2026-05-29
- **Covers:** CAP protocol (Controller-Authority Protocol): four roles, seven primitives, 11 architectural layers, transport bindings (gRPC/protobuf + HTTP/JSON), integration with object graph (Anytype MCP, SQLite).
- **Overlap:** Layer 8 of CAP's 11-layer architecture currently references "Anytype MCP, SQLite." The storage/sync analysis supersedes this: the actual engine will be SurrealDB or SQLite stack (not Anytype as canonical store), and the CRDT op-log is the source of truth.
- **Action:** Do not merge. Make two targeted updates: (a) update Layer 8 to reference the storage/sync decision (SurrealDB or SQLite stack, with CRDT op-log as true source) once the engine is committed; (b) add cross-references to privacy-boundary-spec.md (L6 contract) and this digest (L0-L4 substrate). No other rewrites needed.

### `consolidation_2026-06-21/_research/E_storage_sync_ingestion.md` (same session)
- **Date:** 2026-06-21
- **Covers:** Prior ingestion pass synthesizing the five source docs. Includes decision-state table, consolidation map for three existing specs, and feature impact analysis.
- **Overlap:** This digest supersedes E_storage_sync_ingestion.md as the authoritative synthesis. The prior ingestion pass is factually accurate and consistent with this document; there are no contradictions.
- **Action:** Mark E_storage_sync_ingestion.md as superseded; retain for audit trail. Forward all future updates to this digest.

### `consolidation_2026-06-21/_research/F_db_benchmark_ingestion.md` (same session)
- **Date:** 2026-06-21
- **Covers:** Ali's benchmark results (SQLite, Kuzu, FalkorDB, Neo4j, SurrealDB) on Yar-relevant workloads at 3k/10k/100k records.
- **Key findings incorporated here:** SQLite + FTS5 + sqlite-vec validated as default for phone and laptop MVP. FalkorDB wins personal-server graph. SurrealDB results invalid for FTS/hybrid (config artifact); task-lookup and cold-open latency are likely configuration artifacts; retest required.
- **Action:** Retain as the benchmark reference. Add a note that a SurrealDB retest (correct FTS index config, correct schema settings) is required and is open decision #8 above.

---

## 7. Six-Bullet Summary

1. **Keystone decided, engine open.** The CRDT op-log as single source of truth and the graph engine as a derived swappable index are architectural principles agreed across all source documents. Which engine (SurrealDB vs SQLite stack vs LadybugDB) and which sync protocol (any-sync vs Loro+Iroh) are both open and under evaluation.

2. **SurrealDB is the storage front-runner with genuine risk.** It is the only candidate whose roadmap matches every Yar axis at once: one engine everywhere, knowledge graph, bi-temporal, multimodal, vectors, agent memory. The risk is concentration on a vendor whose correctness-rewrite (3.0) shipped in February 2026, with mobile FFI still thin. A multi-week iOS/Android soak test and a SurrealDB FTS benchmark retest are required before commitment.

3. **SQLite stack is the safe fallback, validated by benchmark.** Ali's benchmark confirms SQLite + FTS5 + sqlite-vec as the MVP default for phone and laptop. It survives both interpretations of the single-engine rule and carries the lowest vendor risk of any option.

4. **Loro+Iroh is the recommended sync path; any-sync is the escape hatch.** Loro+Iroh scores one point higher (36 vs 35) and reuses three already-adopted L0 components (Iroh, mDNS, Tailscale). The recommendation is to build on Loro+Iroh and borrow any-sync's design for the hard parts (per-space keys, ACL head-sync, blob store). If building those components proves too costly, adopt the any-sync node set wholesale.

5. **Solid is portability, not runtime.** Its role is patient data ownership and export, not the hot-path store. The stable core (Protocol, WebID, Solid-OIDC, WAC) is usable now; ACP and Notifications are on the ~6-month horizon; SAI, Shape Trees, and Solid DID Method are explicitly deferred. No public provider offers a HIPAA BAA; pods must be self-hosted.

6. **Four existing specs need cross-references, not rewrites.** `yar-substrate-decision.md` needs an annotation pointing to the fuller DB analysis. `solid-pods-comprehensive.md` needs a forward-reference to the addendum prioritization table. `cap-yar-comprehensive-reference.md` needs two targeted updates to Layer 8 once the engine is committed. `privacy-boundary-spec.md` needs a substrate cross-reference and shared PAP tracking with this spec. The `E_storage_sync_ingestion.md` in this session is superseded by this digest.
