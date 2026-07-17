---
spec_id: SPEC-sync-protocol
version: "0.1"
status: draft
domain: storage-sync
owner: Shahin Mohammadi
created: 2026-06-21
last_updated: 2026-06-22
depends_on: [SPEC-storage-engine]
implements: []
---

> **Related:** [storage-engine spec](./SPEC-storage-engine.md)

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `sync`, `crdt`, `loro`, `iroh`, `any-sync`, `solid`, `identity`, `hipaa`

> **Implementation status**: The CRDT op-log architecture, L0 transport choices (mDNS, Tailscale), and L1 identity decisions (WebID, Solid-OIDC, did:web) are **design decided** but not yet implemented in Yar. The sync benchmark harness (`yar_supervisor_reproducible_benchmark_package/sync_benchmark/yar_sync_edge_bench.py`) is **implemented** and has verified 12/12 edge cases against the Yar sync contract. No real Iroh, Loro, or Automerge adapter is wired to Yar's storage layer yet. The sync protocol choice (O-1) is **open**.

# SPEC: Yar Sync Protocol

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-sync-protocol_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

**BLUF:** Cross-node sync is built on a CRDT op-log at L2. The protocol that replicates that log is open; the leaning is Loro + Iroh (score 36/45) over any-sync (35/45). Neither is committed. Solid is the portability and consent layer at L6, not the hot-path runtime.

---

## 1. Cross-Node Sync Model (Decided in Principle)

The L2 layer replicates the CRDT op-log across devices and nodes. Two properties are architectural requirements:

1. **Convergence is mathematical, not operational.** Any device that receives the full op-log history converges to identical state. There is no primary node, no write lock, and no "last write wins" conflict resolution.
2. **The engine at L4 is a derived view.** Sync operates on the op-log. The graph index at L4 is rebuilt from it. See `SPEC-storage-engine.md` for L4 details.

### 1.1 Eight-Layer Data Fabric (Summary)

| Layer | Label | Status |
|---|---|---|
| L7 | Agents and UI (Gemma, Dapr + NATS, Flutter + Rive, Tauri + React) | Decided |
| L6 | Consent and Access (privacy-boundary schema, WAC now, ACP at ~6 months, Solid pods as portability mirror) | Core decided; ACP scheduled |
| L5 | Vectors and GraphRAG (HNSW; native if SurrealDB, else sqlite-vec) | Follows L4 engine choice |
| **L4** | Graph index and query (SurrealDB, LadybugDB, or SQLite stack) | Open; see SPEC-storage-engine.md |
| **L3** | Storage (local store per engine; encrypted blob store: iroh-blobs or any-sync-filenode) | Tied to sync choice |
| **L2** | Replication and Convergence (CRDT op-log = source of truth; sync protocol open) | Decided in principle; protocol open |
| **L1** | Identity and Keys (WebID, Solid-OIDC, did:web, per-space keys) | Core decided |
| **L0** | Transport and Discovery (mDNS, Tailscale, Iroh) | mDNS + Tailscale decided; Iroh explored |

This spec covers L0 through L3 and the L6 consent integration.

---

## 2. Sync Candidates

### 2.1 Scoring Summary

Scored on nine criteria, 1 to 5 each, maximum 45. Scores are within one point; the decision is about preferred risk profile and language ecosystem, not raw capability.

| Option | Mobile | P2P/CRDT | E2E | Self-host | License | Maturity | Composability | Effort | Stack-fit | Total |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Loro + Iroh (Option B)** | 4 | 4 | 3 | 4 | 5 | 3 | 5 | 3 | 5 | **36** |
| **any-sync (Option A)** | 3 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | **35** |
| Automerge 3.0 | 4 | 4 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | **36** |
| Yjs / yrs | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 3 | 3 | **34** |

### 2.2 Option A: any-sync (Adopt a Stack)

- **What it is:** Anytype's complete local-first P2P end-to-end protocol plus four self-hostable Go server nodes.
- **CRDT model:** Merkle-DAG of operations per object (change-DAG). Content-addressed; peers exchange missing nodes and converge. Proven convergence; tamper-evident; opinionated object-and-space model.
- **Components to adopt (all MIT):** `any-sync` protocol, `any-sync-node` (relay), `any-sync-filenode` (encrypted blobs, IPLD-derived), `any-sync-coordinator` (membership and directory), `any-sync-consensusnode` (ACL log head and ordering), optionally `any-store` (embedded SQLite-backed document store, pre-1.0).
- **Components to reimplement (to avoid ASAL entanglement):** object/type/space/relation model; key-custody specifics; ACL semantics mapped to Yar's privacy-boundary schema.
- **Do not adopt:** `anytype-ts`, `anytype-swift`, `anytype-kotlin` (all ASAL-licensed; cannot be used in a commercial product). Do not adopt `anytype-mcp` (desktop bridge) or the Anytype query surface as the graph API.
- **Identity and keys:** per-space symmetric keys wrapped to member identities; servers see ciphertext only. Key custody, recovery, and break-glass are the adopter's responsibility.
- **Transport:** QUIC + Yamux; TLS identities.
- **Maturity:** production-proven at Anytype's full userbase. Most mature option of the four.
- **Tradeoffs:** turnkey, complete, proven; Go-centric backend is a heavier mobile path; four-node topology is required infrastructure; opinionated object model must be reimplemented.
- **Role in current plan:** fallback if building ACL + key custody + relay from parts (Option B) proves too costly; or adopt wholesale as an escape hatch.

### 2.3 Option B: Loro + Iroh (Current Leaning)

**2.3.1 Loro (CRDT library)**

- Rust crate with first-class mobile bindings (Swift and `flutter_rust_bridge`).
- CRDT algorithms: Fugue for text; movable Tree CRDT for hierarchical and graph data; Eg-walker-style event graph; built-in version DAG with time-travel.
- Container types: Text, List, MovableList, Map, Tree, Counter.
- The movable Tree CRDT maps naturally to graph adjacency (nodes as Tree entries, edges as Map entries). Built-in time-travel is directly useful for longitudinal health data.
- All MIT licensed.

**2.3.2 Loro vs Automerge 3.0**

Both score 36/45. The decision between them is low-stakes and is resolved by prototyping.

| Dimension | Loro | Automerge 3.0 |
|---|---|---|
| Distinguishing feature | Movable-Tree CRDT + built-in time-travel | Memory efficiency (~10x reduction in 3.0) |
| Maturity | Newer, less battle-tested | More mature |
| Language | Rust with Flutter/Swift bindings | Rust with broad WASM support |
| Fallback role | Prototype first | Drop-in fallback within Option B |

Recommendation: prototype Loro. Switch to Automerge 3.0 if Loro integration proves too costly. This is an operational decision, not a strategic one.

**2.3.3 Iroh (P2P Transport)**

- Modular Rust networking stack. "Dial keys, not IP addresses." v0.95 (November 2025), actively developed.
- Modules: `iroh` core (QUIC by public key, hole-punching, relay fallback), `iroh-blobs` (BLAKE3-verified content-addressed blob transfer, pre-1.0), `iroh-gossip` (epidemic broadcast, eventual and unordered), `iroh-docs` (de-emphasized by n0; budget to write your own reconciliation if needed).
- mDNS and Tailscale are already adopted at L0. Iroh was already explored for distributed session state.
- Stack-fit advantage: Option B reuses three already-decided L0 components.

**2.3.4 Encrypted Blob Store**

Under Option B, `iroh-blobs` serves the role that `any-sync-filenode` serves under Option A: BLAKE3-verified content-addressed encrypted blob transfer. Pre-1.0; requires own soak test.

### 2.4 Yjs / yrs (Deprioritized)

- Scores 34/45; lowest stack-fit.
- Mature, widely used, WASM-ready. Rust port is `yrs`.
- Deprioritized because it does not add capabilities over Loro or Automerge 3.0 and scores lower on stack-fit.
- Not ruled out; could be reconsidered if Loro and Automerge 3.0 both fail in prototyping.

---

## 3. Transport and Discovery (L0)

| Component | Status | Notes |
|---|---|---|
| **mDNS / DNS-SD** | Decided | LAN peer discovery; zero-config |
| **Tailscale** | Decided | Overlay network for routed sync between devices off-LAN |
| **Iroh** | In stack (explored) | QUIC by public key; hole-punching and relay fallback; already used for distributed session state |

Transport selection per context: mDNS for same-LAN sync; Tailscale for cross-network overlay; Iroh for hole-punching when Tailscale is unavailable or for ephemeral P2P sessions.

---

## 3.2 Sync Edge-Case Conformance (Minimum Bar)

The sync contract has been verified against a 12-case edge-case benchmark. Any sync adapter for Yar must pass all 12 cases before being considered for production. The benchmark harness is at `yar_supervisor_reproducible_benchmark_package/sync_benchmark/yar_sync_edge_bench.py`.

**Current result: 12/12 passed** (source: `yar_supervisor_reproducible_benchmark_package/sync_benchmark/EDGE_COVERAGE.md`).

| Category | Cases covered |
|---|---|
| Idempotency | `duplicate_replay`, `partial_crash_resume` |
| Delivery ordering | `out_of_order_chunks` |
| Chunking/backpressure | `chunk_limit_many_small_ops` |
| Crash/resume | `partial_crash_resume` |
| Device lifecycle | `new_device_bootstrap`, `device_reinstall_new_actor` |
| Conflict/tombstone | `delete_update_race_delete_wins`, `delete_update_race_update_wins` |
| Deterministic tie-breaking | `same_lamport_tie_break` |
| Partition healing | `network_partition_bridge` |
| Blob/encrypted DAG | `star_hub_blob_archive` |
| Anti-pattern guard | `snapshot_badness_guard` |

**Conformance gaps (not yet covered by an executable adapter):**

These require tool-specific integration, not just Yar sync contract simulation. Any real adapter must address all of them before being declared production-ready:

- Real any-sync cluster latency and failure under self-host deployment
- Real Iroh blob transfer over LAN, WAN, and NAT traversal
- Real Loro, Yjs, or Automerge document adapters against Yar object schema
- Mobile OS background execution limits on iOS and Android
- Encrypted key rotation and account recovery flows
- Malicious peer and Byzantine validation rules

---

## 4. Identity (L1)

| Component | Status | Notes |
|---|---|---|
| **WebID** | Decided | User identity anchor; dereferenceable URI |
| **Solid-OIDC** | Decided | OpenID Connect profile for Solid; issues DPoP-bound access tokens |
| **did:web** | Decided | DID method for machine-readable identity; preferred over Solid DID Method |
| **Solid DID Method** | Deferred | Unofficial draft; not yet implemented widely; use `did:web` instead |
| **Per-space symmetric keys** | Design adopted (from any-sync model) | Keys wrapped to member identities; servers see ciphertext only |

Key custody design (recovery, rotation, break-glass, enterprise escrow) is open. See Section 5, O-4.

---

## 5. Consent and Access (L6)

### 5.1 Access Control

| Horizon | Implement |
|---|---|
| **Now (stable)** | WAC (Web Access Control): simple owner/group/public ACLs; supported by all major Solid servers |
| **~6 months** | ACP (Access Control Policy) v0.9.0: fine-grained, contextual policies; primarily ESS; worth waiting for |
| **Defer** | SAI v0.1.0 (too complex, too early); Shape Trees (sparse implementations) |

The PAP (Policy Administration Point) sub-problem -- runtime-updatable access policy -- is shared with `privacy-boundary-spec.md`. It is tracked as an open decision in both specs; resolution in one place is required.

### 5.2 Solid Protocol Positioning

**Solid is the portability and patient-ownership layer, not the hot-path runtime.** The hot path is the CRDT op-log at L2 and the graph engine at L4. Solid pods are the user-controlled, standards-based store that lets a patient take their data to another app and grant or revoke access.

| Horizon | Implement |
|---|---|
| **Now** | Core Solid Protocol (resource model, export and portability, not hot path), WebID, Solid-OIDC, WAC, self-hosted pod (Community Solid Server for prototype) |
| **~6 months** | ACP, Solid Notifications (WebSocket and Webhook), Type Indexes |
| **Wait / do not build** | SAI v0.1.0, Shape Trees, Solid DID Method, HTTPSig, Solid-PREP, Solid-Chat, Solid-ERP |

**HIPAA constraint (Decided):** No public pod provider offers a HIPAA Business Associate Agreement. For PHI, Cytognosis must operate enterprise-hosted pods. Self-hosting is required; public providers (Inrupt, SolidCommunity, others) are not viable for health data.

See `docs/04-Engineering/yar/research/solid-pods-comprehensive.md` (2026-05-25) for the detailed Solid server comparison (CSS vs Inrupt ESS vs others). That doc predates the ACP sequencing framework above; cross-reference both.

---

## 6. Decided vs Open

### Decided

| Component | Decision |
|---|---|
| CRDT op-log = single source of truth | Decided |
| L2 = CRDT op-log replication (not engine-internal sync) | Decided |
| L0: mDNS + Tailscale | Decided |
| L0: Iroh (in stack for session state) | Explored; in stack |
| L1: WebID + Solid-OIDC + did:web | Decided |
| Use `did:web`, not Solid DID Method | Decided |
| L6: WAC now; ACP at ~6 months | Decided sequence |
| Solid = portability layer, not hot-path runtime | Decided |
| No public HIPAA pod provider; self-host for PHI | Decided |
| Do not adopt ASAL-licensed Anytype clients in a commercial product | Decided |
| any-sync protocol components (MIT) are adoptable | Decided |
| any-store is a supporting local-store component (pre-1.0), not a primary engine | Decided |
| Yjs/yrs = deprioritized | Decided |
| SOSA / SSN for sensor data vocabulary | Decided |

### Open

| # | Decision | Current leaning | Blocker or gate |
|---|---|---|---|
| **O-1** | Sync protocol: any-sync vs Loro + Iroh | Lean Loro + Iroh (36 vs 35); any-sync is the fallback and escape hatch | Backend language preference (Go vs Rust); appetite for building ACL and key custody from parts vs adopting four-node topology |
| **O-2** | CRDT library within Option B: Loro vs Automerge 3.0 | Prototype Loro first | Both score 36/45; low-stakes; resolved by prototyping |
| **O-3** | Key custody + ACL design | Borrow any-sync's per-space key-wrapping and ACL head-sync design; reimplement against privacy-boundary schema | Healthcare break-glass (clinical emergency override) and runtime-updatable policy (PAP) are load-bearing sub-problems; PAP tracked jointly with privacy-boundary-spec.md |
| **O-4** | Encrypted blob store | iroh-blobs (Option B) or any-sync-filenode (Option A) | Follows O-1; both pre-1.0 and require own soak test |
| **O-5** | Enterprise pod hosting platform | Community Solid Server for prototype; Inrupt ESS or self-hosted CSS for production | BAA availability must be confirmed with any third-party hosting provider |

---

## 7. Cross-References

- `SPEC-storage-engine.md` -- L4 engine details; this spec is the source layer that L4 consumes.
- `STORAGE_BENCHMARK_TRACKER.md` -- living status table for all engine and sync options.
- `docs/03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md` (2026-06-21) -- L6 consent layer; PAP open decision is shared; resolve in one place and reflect in both.
- `docs/04-Engineering/yar/research/solid-pods-comprehensive.md` (2026-05-25) -- detailed Solid server comparison; predates ACP sequencing framework above; annotate with forward-reference to this spec.
- `docs/04-Engineering/yar/research/yar-substrate-decision.md` (2026-06-14) -- product-level rationale for a Yar-owned runtime; its brief mentions of RxDB, ElectricSQL, and SurrealDB are superseded by the fuller analysis in SPEC-storage-engine.md.
