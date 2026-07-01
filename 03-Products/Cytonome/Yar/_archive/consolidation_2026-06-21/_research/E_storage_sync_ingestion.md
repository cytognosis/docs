> **Status**: SUPERSEDED -- see `spec/STORAGE_BENCHMARK_TRACKER.md`, `spec/SPEC-storage-engine.md`, and `spec/SPEC-sync-protocol.md` for the authoritative synthesis. Retained for audit trail only.
> **Date**: 2026-06-21
> **Author**: ingestion agent
> **Audience**: Opus synthesis pass
> **Tags**: `yar`, `storage`, `sync`, `crdt`, `cytoplex`, `ingestion`
> **Sources ingested**:
> - `~/Downloads/Yar-Graph-DB-Picker-Visual-Guide.md` (identical to `yar_db_simplified.md`)
> - `~/Downloads/Yar-SingleEngine-AnySync-Solid-Addendum.md`
> - `~/Downloads/Yar-Data-Fabric-Simple-Visual-Guide.md`
> - `~/Downloads/Yar-Sync-Architecture-anysync-vs-loro-iroh.md`
> **Existing docs scanned**: `yar-substrate-decision.md`, `privacy-boundary-spec.md`, `cap-yar-comprehensive-reference.md`

# E: Storage and Sync Architecture Ingestion Digest

---

## 1. Database and Storage Options

### 1.1 Decision Criteria (explicit in source docs)

The evaluation matrix scores each candidate against nine axes:

| Criterion | Weight signal |
|---|---|
| Embeds on iOS + Android (phone-first) | Make-or-break; disqualifies 6 of 9 |
| Company / project survival (2-year horizon) | Weighted as heavily as benchmarks for healthcare |
| CRDT / sync story native | Required; none ship it out of the box |
| GraphRAG / vector support | Required for on-device Gemma agents |
| Time-travel / temporal queries | Required for longitudinal health data |
| Offline-first convergence | Required; no cloud-dependent hot path |
| License (commercial PBC pathway) | Must be MIT/Apache or source-available with clear embed terms |
| Healthcare fit (HIPAA, PHI) | Mandatory |
| Single-engine everywhere (added by addendum) | Narrows field dramatically |

### 1.2 Candidate Profiles

**Neo4j**
- Data model: labeled property graph (LPG), Cypher query language.
- Pros: deepest GraphRAG tooling (LangGraph, Knowledge Graph Builder), $581M raised, IPO-prep, $200M+ ARR, safest vendor survival.
- Cons: JVM, server-only, no phone embedding, no native CRDT/sync.
- Score: Cloud tier only. Under the single-engine rule, disqualified as primary store.

**SQLite stack** (SQLite + sqlite-vec + optional Cypher extensions)
- Data model: relational core; graph semantics assembled from extensions.
- Pros: ships on every phone, public domain (bulletproof survival), SQLCipher for HIPAA, PowerSync or CR-SQLite for sync.
- Cons: no off-the-shelf Cypher on device, graph traversals slower at high end, you assemble the graph and sync layers from parts.
- Score: Device tier, Architecture C front-runner. Survives the single-engine rule as a literal everywhere option.

**FalkorDB**
- Data model: labeled property graph on Redis; Cypher; vectors-on-edges.
- Pros: GraphRAG-focused, ex-Redis team, healthy ($funded), fast, vectors on edges useful for relationship-typed retrieval.
- Cons: Redis module only, no phone embedding.
- Score: Cloud option only; disqualified as primary under single-engine rule.

**SurrealDB**
- Data model: multi-model (graph, relational, document, KV, time-series) with SurrealQL; native HNSW vectors; VERSION clause for time-travel; Spectron agent-memory layer; Surrealism WASM extension system; native file support (3.0).
- Funding: ~$44M total; $38M Series A (FirstMark, Georgian, Chalfen Ventures, Begin Capital); February 2026 extension; Forbes AI 50 2026; ~32k GitHub stars.
- Architecture 3.0 specifics: correctness-motivated rewrite released February 2026; synced writes by default; redesigned on-disk document representation; separated values from expressions; ID-based metadata storage.
- Pros: only candidate whose roadmap matches every Yar axis at once (one engine everywhere, KG, bi-temporal, multimodal, vectors, agent-memory via Spectron); explicit "runs embedded, at the edge, or as a highly-scalable cluster, same engine everywhere" positioning; Rust core matches Flutter/LadybugDB.
- Cons: 3.0 is a months-old correctness rewrite with short production track record on current architecture; mobile FFI (Flutter/iOS/Android) path thin and early-adopter territory; Spectron, Surrealism, and native files shipped in the last few months and are unproven; BSL-style source-available license (confirm for commercial PBC).
- Score: Co-front-runner under single-engine rule. Recommended only with: (a) CRDT log behind it, (b) own soak test of mobile path, (c) MVP avoids Spectron/Surrealism/native files.

**Kuzu / LadybugDB**
- Kuzu was the ideal embedded graph DB for on-device GraphRAG. Apple acquired it on October 9, 2025 and archived the repo the next day. The entire "embedded graph DB for on-device AI" category lost its only real player.
- LadybugDB is the best active fork but is a small community. iOS embedding works; Android binding is DIY (weeks of work). No cloud clustering.
- Score: Architecture A "best tech" option if team is willing to own the fork; otherwise Architecture C (skip). Treat category as unsettled for 12-24 months.

**SurrealDB Spectron** (agent-memory layer, not a standalone DB)
- Described as a separate layer atop SurrealDB that stores facts, preferences, episodes, and procedures as records with hybrid retrieval (vectors + graph + BM25 + keywords), provenance, and "corrections supersede, never overwrite" semantics. Also advertises bi-temporal and "tri-temporal" fact versioning.
- Status: brand new, unproven. Do not depend on for MVP.

**`any-store`** (anyproto, MIT)
- An embedded SQLite-backed document store with a Mongo-like API, used inside anytype-heart.
- Pre-1.0; "APIs may change." Adoptable as a local store component under either sync option.
- Score: usable supporting component, not a primary graph engine.

**Anytype** (as a substrate, not an engine)
- Perfect sync model (any-sync), CRDT/DAG-based, self-hostable, time-travel. But not embeddable as a backend; cannot be used as a graph engine with traversal APIs. No Cypher/SQL/graph-walk.
- Score: steal the design, do not adopt the app. ASAL-licensed clients cannot be used in a commercial product.

**Memgraph**
- C++ in-memory graph DB, MAGE algorithms, vectors in 3.8.
- No Series A in 8 years, ~25 people, small team risk.
- Score: cloud maybe; disqualified as primary under single-engine rule.

**Dgraph**
- Two acquisitions in 24 months (Hypermode then Istari), founder left. HIGH risk.
- Score: skip.

**JanusGraph**
- JVM, 2-person commit base, stagnating, no vectors.
- Score: skip.

### 1.3 The Three Architecture Options (pre-addendum)

**Architecture A: "Best Tech"** (LadybugDB on device + Loro CRDT + Iroh transport)
- Wins: fastest on-device graph queries, native vectors, MIT throughout, matches mDNS/Tailscale/Iroh stack.
- Costs: LadybugDB is a small fork of an archived upstream, Android binding DIY, CRDT-to-graph reducer is custom code, must own security.

**Architecture B: "Elegant Bet"** (SurrealDB everywhere + custom CRDT + cloud cluster)
- Wins: one engine, one query language, best native time-travel (VERSION), graph+vector+text+time in one query.
- Costs: mobile embedding unofficial, 3.0 is a correctness rewrite with short track record, still must build sync.

**Architecture C: "Safest"** (SQLite + sqlite-vec on device + Neo4j/FalkorDB in cloud)
- Wins: lowest risk, SQLite everywhere, HIPAA via SQLCipher, best GraphRAG tooling in cloud, swap any layer.
- Costs: no off-the-shelf Cypher on device, slower traversals, two engines to maintain.

### 1.4 How the Single-Engine Addendum Reshapes the Shortlist

The addendum establishes that the "no drift" constraint is best interpreted as either:
1. Literally one engine binary on every tier (strict): survives as SurrealDB or SQLite stack only.
2. One logical source of truth with swappable read-indexes (preferred interpretation): the CRDT log is the single source; any engine can be the materialized index as long as all devices converge on the same op-log.

Interpretation 2 is the stronger engineering answer because CRDT convergence is mathematically guaranteed rather than operationally hoped for. It also means the engine choice becomes lower-stakes and reversible.

Under interpretation 1, Architectures A and C are eliminated (both use two engines). Under interpretation 2, all three survive but the decoupled CRDT design is explicitly favored.

**Net post-addendum shortlist:** SurrealDB (with CRDT log behind it) or SQLite stack (assembled with CRDT log), with LadybugDB remaining viable if the fork risk is accepted.

---

## 2. The Data Fabric Concept

The data fabric is the complete layered substrate under the Cytonome agents. It is described as an 8-layer stack:

| Layer | Label | Contents |
|---|---|---|
| L7 | Application and Agents | Gemma interviewer (E2B, LiteRT-LM, Flutter), Supervisor (26B MoE, Tauri+React), Dapr Agents on NATS JetStream, MCP tool surface |
| L6 | Consent and Access (CAP/Cytoplex) | Privacy-boundary schema (phone-to-supervisor), WAC/ACP access control, Solid pods as portability mirror |
| L5 | Vectors and GraphRAG | HNSW vector index, hybrid retrieval (vector + graph + BM25) |
| L4 | Graph index and query (Yar PKG) | SurrealDB embedded, or LadybugDB, or SQLite+sqlite-vec; materialized from the op-log |
| L3 | Storage | Local store (any-store / SurrealKV / SQLite), encrypted blob store (filenode / iroh-blobs), self-hosted cloud relay node |
| L2 | Replication and Convergence (Cytoplex core) | CRDT op-log as source of truth, ACL head-sync / change-DAG |
| L1 | Identity and Keys | WebID / Solid-OIDC / did:web, per-space keys creator-held |
| L0 | Transport and Discovery | mDNS/DNS-SD (LAN), QUIC P2P + hole-punch + relay, Tailscale/WireGuard overlay |

**The architectural keystone:** The CRDT op-log at L2 is the single source of truth. The graph engine at L4 is a derived, swappable index rebuilt by replaying the log. Drift becomes mathematically impossible. If the graph engine dies (like Kuzu did), replay the log into a fresh engine. No lock-in.

**Layer 2 (sync) is the subject of the sync-architecture documents. Layer 4 (engine) is the subject of the DB-picker documents. The fabric concept integrates both.**

The fabric uses the term "Cytoplex" as the data fabric / sync + storage platform connecting Yar instances across devices and cloud. The naming needs confirmation: the Sync Architecture doc notes this is an inferred mapping and flags it for correction.

---

## 3. Sync Protocols and Strategies

### 3.1 any-sync (Option A: adopt a stack)

**What it is:** Anytype's complete local-first P2P E2E protocol plus a set of self-hostable Go server nodes. ~85-89 repos in the anyproto org; the protocol and infrastructure nodes are MIT.

**Components:**
- `any-sync-coordinator`: network membership, config, space registry; directory for peer discovery.
- `any-sync-node`: stores and relays the encrypted change-DAG (CRDT operations) for spaces; the always-on cloud relay.
- `any-sync-filenode`: encrypted large-object storage (IPLD/IPFS-derived content addressing); for blobs (sensor data, genome files, audio).
- `any-sync-consensusnode`: maintains the ACL log head and ordering per space; key rotations.
- `any-sync-bundle` (community, grishy): all four nodes prepackaged for one-command self-hosting; verify its own license.
- `any-store` (MIT): embedded SQLite document store with Mongo-like API used inside anytype-heart; pre-1.0.

**Internal mechanisms:**
- Change-DAG (CRDT): Merkle-DAG of operations per object; content-addressed; peers exchange missing nodes and converge. Proven convergence; tamper-evident; natural history. The object/space model is opinionated and not a generic CRDT.
- ACL head-sync: an access-control log per space, hash-linked; membership and key-rotation events ordered; revocation supported. Conceptually heavy; adopts Anytype's ACL semantics.
- Per-space keys / E2E: symmetric space keys wrapped to member identities; no central account registry; creator generates space keys; new members get keys wrapped to their identity; servers see ciphertext only. True E2E, server-blind storage, HIPAA-friendly; key custody, recovery, and break-glass are the adopter's responsibility.
- Transport: QUIC + Yamux; TLS identities between nodes/peers.
- IPLD-style content addressing: blobs chunked, hashed, stored by CID, encrypted; dedup and integrity; IPFS-derived complexity.

**Tradeoffs:**
- Pros: complete turnkey system proven at Anytype's production userbase; all four nodes are MIT and self-hostable; gives Anytype's exact server-blind E2E P2P design, self-hosted for HIPAA, without touching ASAL client code.
- Cons: Go-centric (heavier on mobile vs. native Rust); 4-node topology to run; object model is opinionated and must be reimplemented to avoid ASAL entanglement; not a reusable SDK.

**Adoptability verdict:**
- Adopt as-is (MIT): `any-sync`, `any-sync-node`, `-filenode`, `-coordinator`, `-consensusnode`, optionally `any-store`.
- Adopt the design, reimplement: the object/type/space/relation model, the key-custody specifics, the ACL semantics mapped to the privacy-boundary schema.
- Do not adopt: `anytype-ts`/`-swift`/`-kotlin` (ASAL, full apps), `anytype-mcp` (desktop bridge), the Anytype query surface as the graph API.

**Maturity:** Production-proven at Anytype's userbase. The best "proven at scale" option.

### 3.2 Loro (core of Option B)

**What it is:** A Rust CRDT library with first-class mobile bindings (Swift + `flutter_rust_bridge`).

**CRDT type and algorithm:** Fugue algorithm for text; movable Tree CRDT for hierarchical/graph data; Eg-walker-style event graph; built-in version DAG with time-travel.

**Container types:** Text, List, MovableList, Map, Tree, Counter.

**Why Tree matters:** The movable-Tree CRDT maps naturally to graph adjacency (model nodes as Tree entries, edges as Map entries). Time-travel is built in, matching Yar's longitudinal health needs.

**Comparison to alternatives:**

| Library | Algorithm | Mobile bindings | Fit for Yar |
|---|---|---|---|
| Loro (recommended) | Fugue + movable Tree + built-in time-travel | Swift + flutter_rust_bridge | Best: Tree maps to graph; time-travel native |
| Automerge 3.0 | Columnar-compressed op-log, RGA-style text | C FFI / "Automerge Anywhere" | Mature, ~10x memory reduction in 3.0; more Flutter glue needed |
| Yjs / yrs | YATA algorithm | yffi C FFI | Best for text editors; less natural for graph data |
| Diamond Types | Research-grade text CRDT | Limited | Avoid; value has been absorbed into Loro |

**Pros:** mathematically guaranteed convergence, offline-first, engine-agnostic (swap L4 freely), pure Rust matches SurrealDB/LadybugDB and flutter_rust_bridge.

**Cons:** you build the relay, key custody, and ACL yourself; combined stack is less battle-tested as a product than any-sync.

**Scoring vs. any-sync:** Loro 36/45, any-sync 35/45, Automerge 3.0 36/45. The scores are within one point; the decision is about preferred risk profile and language, not raw capability.

### 3.3 Iroh (P2P transport, Option B)

**What it is:** A modular Rust networking stack; "dial keys, not IP addresses." Latest line v0.95 (November 2025), actively developed.

**Modules:**
- `iroh` (core): QUIC connections by public key, hole-punching, relay fallback; NAT traversal that "mostly just works"; n0 runs free relays, self-hostable.
- `iroh-blobs`: content-addressed blob transfer (BLAKE3-verified); replaces filenode role; integrity built in; pre-1.0 churn.
- `iroh-gossip`: epidemic broadcast for pub/sub; good for change notifications but eventual and unordered.
- `iroh-docs` (formerly): range-based reconciliation document sync; n0 has de-emphasized it; budget for writing your own reconciliation over blobs+gossip if needed.

**Integration with existing stack:** mDNS and Tailscale are already adopted at L0. Iroh was already explored for distributed session state. This gives Option B a head start on stack-fit.

### 3.4 Solid Protocol (portability and ownership layer)

**Framing:** Solid is the patient-ownership and portability layer, not the runtime database. The CRDT log + graph engine is the fast local system. Solid pods are the user-controlled, standards-based home for data portability and grant/revoke of app access.

**Self-hosting requirement:** No public pod provider offers a HIPAA BAA. For PHI, enterprise-hosted Cytognosis-operated pods are required. ACP (not WAC) is the access-control layer needed for app-binding and issuer restriction; ACP is v0.9.0 and primarily implemented in ESS (Inrupt).

**Prioritization by maturity tier:**

Implement now (stable design + working implementations):
- Core Solid Protocol resource model (LDP containers/resources) as the export/portability format; not the hot-path store.
- WebID + Solid-OIDC for identity.
- WAC for basic access control on day one.
- Self-hosted pod (Community Solid Server for prototype; plan enterprise-grade for PHI).

Implement at ~6 months (near-stable, worth waiting for):
- ACP for fine-grained, app-bound, time-bound consent (healthcare actually needs this; but v0.9.0, best in ESS).
- Solid Notifications (WebSocket/Webhook channels) for pod-to-device change feeds.
- Type Indexes for pod discoverability.

Wait / do not build yet (early drafts, sparse implementation):
- Solid Application Interoperability (SAI) v0.1.0: too early and complex.
- Shape Trees (Editor's Draft): sparse implementations.
- Solid DID Method (Unofficial Draft) and HTTPSig: speculative; use `did:web` instead.
- Solid-PREP, Chat, ERP: not relevant or not ready.

**Spec maturity reference:**

| Spec | Stage | Implemented? |
|---|---|---|
| Solid Protocol | CG-DRAFT v0.11.0 | Yes: CSS, NSS, ESS, TrinPod |
| WebID Profile | CG-DRAFT v1.0.0 | Yes, widely |
| Solid-OIDC | v0.1.0 | Yes (CSS, ESS, Inrupt libs) |
| WAC | CG-DRAFT v1.0.0 | Yes, default in most servers |
| ACP | v0.9.0 | Primarily ESS |
| Solid Notifications | CG-DRAFT v0.3.0 | Partial (WebSocket/Webhook) |
| SAI | CG-DRAFT v0.1.0 | Reference impls only |
| Shape Trees | Editor's Draft | Sparse |
| Solid DID Method | Unofficial Draft | Effectively none |

---

## 4. The Single-Engine + AnySync + Solid Addendum: How It Revises the Picture

The addendum answers four questions the DB-picker guide left open:

**1. How the single-engine constraint reshapes the shortlist.**
The strict interpretation eliminates all server-only DBs as primary stores (Neo4j, FalkorDB, Memgraph, Dgraph, JanusGraph). Architectures A and C from the prior report are eliminated under strict single-engine. The surviving literal single-engine candidates are SurrealDB (by design intent) and SQLite stack (by ubiquity). The addendum introduces a preferred looser interpretation: the CRDT log is the single source of truth, and the engine is a materialized read-index. This is a stronger guarantee against drift than trusting two engines to stay in lockstep.

**2. Focused SurrealDB assessment.**
The addendum adds funding details (Feb 2026 $23M Series A extension), confirms the 3.0 correctness-rewrite timeline, audits each Yar requirement against SurrealDB 3.0 status, and specifies four de-risking steps: (a) keep CRDT log behind it; (b) pin a version and run your own mobile soak test; (c) do not depend on Spectron/Surrealism/native files for MVP; (d) confirm BSL license for commercial PBC before launch.

**3. any-sync component adoptability.**
The addendum establishes that any-sync is "adoptable, not just inspirational." It provides a component-by-component verdict. The key finding is that the MIT-licensed protocol and self-hostable node set let you reuse Anytype's exact local-first E2E P2P design legally. Only the ASAL-licensed client/middleware and the object model must be reimplemented. This makes any-sync a direct competitor to Loro+Iroh (not just a design reference), with the language/topology tradeoff as the deciding factor.

**4. Solid prioritization.**
The addendum provides the now/6-months/wait-for-it breakdown described in Section 3.4 above. The strategic framing is confirmed: Solid is the patient-ownership and portability layer, not the runtime database. SOSA/SSN remains the sensor-data vocabulary regardless of Solid spec timing.

---

## 5. Decision State

### Decided / Locked In

| Component | Decision |
|---|---|
| CRDT op-log = single source of truth | Decided in principle across all documents |
| L4 graph engine = derived, swappable index (replay from log) | Decided as architectural principle |
| L0 transport: mDNS/DNS-SD (LAN) | Already adopted |
| L0 transport: Tailscale overlay | Already adopted |
| L0 transport: Iroh (explored, tentatively adopted) | Explored/adopted for session state |
| L7: Gemma 4 E2B (interviewer), Gemma 4 26B MoE (supervisor), Dapr+NATS | Decided |
| L7 UI: Flutter+Rive (mobile), Tauri+React (desktop) | Decided |
| L1 Identity: WebID + Solid-OIDC + did:web | Core decided |
| L6 Consent: WAC now, ACP at ~6 months, enterprise-hosted Solid pods for PHI | Core decided |
| Solid is the portability layer, not the hot-path database | Decided |
| No public pod provider gives a HIPAA BAA; must self-host pods | Decided |
| Kuzu is dead; LadybugDB is the fork; embedded-graph-DB category unsettled for 12-24 months | Fact |
| Do not adopt anytype-ts/swift/kotlin (ASAL) in a commercial product | Decided |
| Use `did:web`, not Solid DID Method | Decided |
| SOSA/SSN for sensor data vocabulary | Decided |

### Open Decisions

| # | Decision | Current leaning | Key constraint |
|---|---|---|---|
| 1 | L4 graph engine: SurrealDB vs SQLite stack vs LadybugDB | SurrealDB is front-runner under single-engine rule; SQLite is safest fallback | SurrealDB 3.0 mobile soak test required before committing |
| 2 | L2 sync engine: any-sync (Option A) vs Loro+Iroh (Option B) | Lean Option B (Loro+Iroh); any-sync is the escape hatch | Backend language (Go vs Rust); appetite for 4-node topology vs building ACL/key custody |
| 3 | Loro vs Automerge 3.0 within Option B | Loro first (movable-Tree CRDT + built-in time-travel map better to graphs) | Both score 36/45; prototype Loro first |
| 4 | Key custody + ACL design | Borrow any-sync's per-space key wrapping and ACL head-sync design | Healthcare break-glass and PAP (policy updatable at runtime) are sub-problems |
| 5 | LadybugDB fork ownership | Team must decide: willing to own a small fork of archived upstream? If no, Architecture C | Kuzu upstream archived by Apple; Android binding is DIY |
| 6 | SurrealDB BSL license for commercial PBC | Confirm before launch | License text must be checked |
| 7 | Cytoplex / CAP naming in the layer diagram | Needs correction from Shahin | Sync-architecture doc used inferred mappings |
| 8 | PAP implementation for runtime-updatable policy | Open per privacy-boundary-spec Section 8 | Required if policy must be updatable without app redeployment |

### Current Recommendations / Leanings

**Storage engine (L4):** SurrealDB is the recommended front-runner under the single-engine interpretation because it is the only candidate whose roadmap matches every Yar axis (KG, bi-temporal, multimodal, vectors, agent memory, one engine everywhere). It must be adopted with a CRDT log behind it and a mobile soak test before commitment. SQLite stack is the fallback if SurrealDB mobile FFI proves too thin.

**Sync protocol (L2):** Option B (Loro + Iroh) is recommended by a small margin (36 vs 35) and reuses existing L0 choices (Iroh, mDNS, Tailscale). The recommendation is to build on Loro+Iroh and borrow any-sync's design for the parts you must build (per-space keys, ACL head-sync, content-addressed encrypted blob store). Fallback trigger: if building ACL + key custody + relay proves too costly in engineering time, adopt the any-sync node set wholesale rather than half-building it.

**First actions (from source docs):**
1. Prototype the sync spine: Loro + Iroh, offline merge, relay node.
2. Spike two device engines: SQLite+sqlite-vec vs SurrealDB embedded, same CRDT log behind both.
3. Stand up Neo4j or FalkorDB in the cloud for heavy GraphRAG at the supervisor tier.
4. Write the reducer: Loro ops to graph-DB rows (~1,000-2,000 LOC).
5. Lift any-sync's per-space key wrapping and ACL head-sync design into a 1-page internal spec before coding.
6. Run SurrealDB 3.0 mobile soak: iOS and Android, realistic personal-KG workload, multi-week crash/restore/corruption test.

---

## 6. Consolidation Map

### `04-Engineering/yar/research/yar-substrate-decision.md` (2026-06-14)

**Coverage:** Evaluates off-the-shelf PKM platforms (Anytype, Obsidian, Tana, Logseq, Capacities, Notion, AppFlowy, SiYuan, Trilium, Joplin, Athens) as substrates for Yar. Recommends hybrid Yar-owned runtime + Obsidian shell for MVP; Yar-native local-first object runtime long-term. Establishes SQLite as the local object store; CAP as the authority layer; no third-party PKM as canonical truth.

**Overlap with ingested material:**
- Shares the conclusion that a custom local-first stack is the right long-term path.
- Its mention of SurrealDB, RxDB, ElectricSQL, and Replicache is brief (toolbox, not full assessment); the ingested docs supersede this with a full nine-DB evaluation + single-engine addendum.
- Its recommendation of SQLite for MVP is consistent with Architecture C in the ingested docs.
- Does not cover Loro, Iroh, any-sync, Solid, or the CRDT-log-as-source-of-truth architecture. Entirely predates the sync and data-fabric analysis.

**Action:** Do not merge; roles differ. The substrate-decision doc covers the PKM landscape and MVP-vs-long-term product question. The new storage/sync specs cover the technical data-fabric implementation. Cross-reference the substrate-decision doc from the new spec (it establishes why a Yar-owned runtime is required). The SQLite recommendation in substrate-decision is a subset of Architecture C; it should be updated or annotated to reflect the full DB/sync analysis.

**Content to migrate into new spec:** None; the substrate-decision doc is product-level reasoning, not an engineering spec. It belongs at the product strategy layer, not merged into a storage spec.

### `03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md` (2026-06-21)

**Coverage:** Defines the privacy boundary between Yar's on-device worker zone and external recipients (supervisor, clinician, services). Specifies the `CrossBoundarySignal` schema; EARS requirements; data classification (device-local vs. boundary-crossing); retention and consent rules; CAP enforcement (PEP/PDP/PAP/PIP). Recommends LinkML as canonical schema language. Open decisions include PAP implementation, retention TTLs, PHI definition, and clinician-path HIPAA posture.

**Overlap with ingested material:**
- Directly implements the L6 consent layer described in the data-fabric architecture.
- The "phone-to-supervisor boundary" in the privacy-boundary-spec maps to the L2/L6 ACL layer in the sync architecture docs.
- The CAP enforcement architecture (PEP blocks cross-boundary crossing) is the same "consent lives above the op-log" design described in Section 8.1 of the sync architecture doc.
- The privacy-boundary-spec's default-deny and local-only baseline are consistent with the local-first-first principle in all sync documents.

**Action:** Do not merge; scopes are complementary, not overlapping. The privacy-boundary-spec is the L6 schema/requirements document. The storage/sync spec is the L0-L4 architecture document. Cross-reference both ways: the storage/sync spec should cite the privacy-boundary-spec as the L6 data contract; the privacy-boundary-spec should reference the L2 sync architecture as its transport substrate. The open PAP decision in the privacy-boundary-spec is also an open decision in the sync architecture; consolidate that tracking.

**Content to migrate:** None; keep separate. Ensure the PAP open decision is tracked in both specs and resolved together.

### `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` (2026-05-29)

**Coverage:** Comprehensive reference for the CAP protocol (Controller-Authority Protocol): four roles (Controller, Guard, Executor, Observer), seven primitives (Directive, GuardDecision, RefusalMessage, ExecutionReport, DecisionRecord, EvidenceRef, AuthorityChain), 11 architectural layers, transport bindings (gRPC/protobuf + HTTP/JSON), and CAP's integration with the object graph (Anytype MCP, SQLite).

**Overlap with ingested material:**
- Layer 8 of CAP's 11-layer architecture mentions "Anytype MCP, SQLite" as the object graph integration surface. The ingested docs supersede this with the full storage/sync analysis; the actual engine will be SurrealDB or SQLite stack (not Anytype as the canonical store).
- The CAP reference predates the data-fabric layering. CAP governs L6 in the 8-layer fabric model; the fabric model clarifies what CAP sits on top of.
- The "governed AI operations" framing in cap-yar-comprehensive-reference aligns with the L7 agent architecture in the sync docs.

**Action:** Do not merge; roles are architecturally distinct. Update Layer 8 of the CAP architectural layers reference (currently "Anytype MCP, SQLite") to reflect the actual storage/sync decision once resolved (SurrealDB or SQLite stack). Add a note that CAP's L6 privacy boundary is specified in `privacy-boundary-spec.md` and that the L0-L4 substrate is specified in the new storage/sync spec. The cap-yar-comprehensive-reference does not need substantial rewrites; it needs two cross-reference additions.

---

## 7. Feature Impact

The features below are drawn from the v4 research matrix context (referenced in the privacy-boundary-spec and elsewhere). These features are directly affected by this storage/sync analysis.

| Feature | ID | Impact and recommended spec update |
|---|---|---|
| CSP (Consent Surface Protocol) / CAP | F12 | Status confirmed active. The L6 consent design is decided (WAC now, ACP at 6 months, enterprise-hosted Solid pods). The privacy-boundary-spec is the data contract. Cross-reference the sync architecture for the substrate CAP runs on top of. |
| Personal Knowledge Graph | F16 | The graph engine for the PKG is the open decision (SurrealDB vs SQLite stack vs LadybugDB). The CRDT log as source of truth is decided. Feature description should note: KG is a materialized derived index on the op-log, not the source of truth. |
| Local-first AI | F19 | Confirmed: Yar is local-first. CRDT log stays on device. Only derived signals cross the boundary (privacy-boundary-spec). No cloud dependency for core flows. Feature description is accurate; add: "CRDT op-log at L2 is the single source of truth; L4 graph engine is a derived local index." |
| Schema mapping | F51 | The sync architecture confirms LinkML/Biolink as the ONE foundation across layers (from the IGoR TA3 integrated design; applies here too). The CrossBoundarySignal schema uses LinkML per the privacy-boundary-spec. Feature description should add: schema mapping targets the L4 graph engine and uses LinkML as the canonical serialization. |
| Storage | F52 | Major update needed. Current description is likely SQLite-only from the substrate-decision era. Must be updated to reflect: (a) CRDT op-log at L2 (Loro or any-sync) is the true store; (b) L4 graph engine (SurrealDB front-runner, SQLite fallback, LadybugDB as alternative) is a materialized index; (c) L3 blob store (iroh-blobs or any-sync-filenode) for large objects; (d) Solid pods as portability/export format. Status: open decision, front-runner identified. |

Additional features likely affected (flag for synthesis pass review):

| Feature / area | Likely impact |
|---|---|
| Multi-device sync (any F referencing sync) | The entire L2 decision (any-sync vs Loro+Iroh) drives this; not yet decided |
| Time-travel / longitudinal history | Loro has built-in time-travel; SurrealDB has VERSION; both support this. Either engine option covers this feature. |
| Encrypted storage / E2E | any-sync: server-blind E2E by design; Loro+Iroh: self-managed key custody required. Both capable but at different engineering cost. Feature depends on sync choice. |
| Voice / audio storage (F50 WADM, wearables) | Large audio blobs go to L3 (iroh-blobs or any-sync-filenode), not the L4 graph. Feature spec should call out the blob tier explicitly. |
| Agent memory (Gemma, supervisor) | SurrealDB Spectron is the only candidate with a native agent-memory layer. If SurrealDB is chosen, Spectron is an upside; do not depend on it for MVP. If SQLite/LadybugDB, agent memory must be built separately. |

---

## Appendix: Standards Reference (L0-L6, from Sync Architecture doc Section 5)

| Standard | Layer | Purpose |
|---|---|---|
| CRDT (Fugue, YATA, RGA, movable-tree) | L2 | Conflict-free replicated data types |
| QUIC (RFC 9000) | L0 | Encrypted, multiplexed, NAT-friendly transport |
| mDNS / DNS-SD (RFC 6762/6763) | L0 | LAN service discovery (already adopted) |
| WireGuard | L0 | Modern VPN crypto; Tailscale overlay (already adopted) |
| WebID | L1 | HTTP URI identity; Solid core |
| Solid-OIDC | L1 | OIDC profile for Solid auth (v0.1.0, usable) |
| did:web | L1 | Decentralized identifier via HTTPS (prior decision) |
| WAC | L6 | Web Access Control, ACL-based (v1.0.0 CG-draft, stable) |
| ACP | L6 | Access Control Policy, app-bound (v0.9.0, ~6-month horizon) |
| Solid Notifications | L6 | Change channels (WebSocket/Webhook, ~6-month horizon) |
| SOSA / SSN | L4/L5 | W3C sensor/observation ontology (prior decision) |
| FHIR-RDF | L4/L5 | Health data as RDF |
| IPLD | L3 | Content-addressed linked data (any-sync filenode; iroh-blobs analog) |
| HNSW | L5 | Vector index for GraphRAG |
| LinkML / Biolink | L4/L6 | Schema language; ONE foundation across layers |
