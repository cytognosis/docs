---
doc_id: ANYSYNC-FIT-ASSESSMENT
version: "1.0"
status: assessment
domain: storage-sync
owner: Shahin Mohammadi
created: 2026-07-16
related: [SPEC-sync-protocol.md, SPEC-storage-engine.md]
decision_ref: "D3 (YAR-MASTER-PLAN_2026-07-16.md, Section 10)"
---

# Assessment: Anytype `any-sync` as Yar's Near-Term Sync Layer

**Read this first (BLUF).** Adopt `any-sync` now, but scoped narrowly to transport, relay, and blob duties. Every Go server-node repo Yar would touch (`any-sync`, `any-sync-node`, `any-sync-filenode`, `any-sync-coordinator`, `any-sync-consensusnode`, `any-store`) is MIT licensed today, confirmed 2026-07-16, with no CLA burden found. The ASAL-licensed client (`anytype-heart` and the official apps) is correctly excluded and not needed for this plan. Do not let any-sync's object/ACL/space model become Yar's source of truth in phase 1; keep Yar's own tested reducer authoritative and treat any-sync purely as the pipe. That preserves the op-log contract and the post-YC Loro+Iroh swap path. Estimated cost: 4 to 6 engineer-weeks for a 2-person team, not YC-blocking.

---

## 1. Licensing (verified 2026-07-16)

Confirmed directly against each repository's GitHub license metadata and license file text.

| Repo | Role | License (today) | Commercially self-hostable, free of charge? |
|---|---|---|---|
| `any-sync` | Core protocol: commonspace, ACL, consensus, coordinator client, net, protobuf | MIT | Yes |
| `any-sync-node` | Sync/relay node (stores spaces and objects) | MIT | Yes |
| `any-sync-filenode` | File node (encrypted, content-addressed blobs) | MIT | Yes |
| `any-sync-coordinator` | Membership and network directory | MIT | Yes |
| `any-sync-consensusnode` | ACL log ordering and consensus | MIT | Yes |
| `any-store` | Embedded SQLite-backed doc store (pre-1.0) | MIT | Yes, optional, not load-bearing |
| `any-sync-tools` | Node config builder | MIT | Yes |
| `any-sync-dockercompose` | Reference self-host deployment | MIT | Yes, personal-scale reference only |
| `anytype-heart` | Client middleware: object/type/space/relation model, embeds any-sync client-side | Any Source Available License (ASAL) 1.0 | **No.** Commercial use restricted to Any Association-approved "Allowed Networks" |
| `anytype-ts` / `anytype-swift` / `anytype-kotlin` | Official Anytype apps | ASAL 1.0 family (GitHub reports `spdx_id: NOASSERTION`, custom license) | **No.** Do not adopt |

**Key finding:** the license boundary in the anyproto org runs exactly where Yar's own `SPEC-sync-protocol.md` already drew it. The four server-node repos plus the protocol repo are unrestricted MIT. The restriction lives entirely in the client middleware (`anytype-heart`) and the three official apps built on it. D3's plan to take the Go server nodes and avoid the ASAL client is licensing-clean.

**ASAL 1.0 terms, for the record:** it permits Non-Commercial Use freely, and Commercial Use only inside Any Association's published "Allowed Networks" list (`networks.any.coop`). Yar would never touch this license under the D3 plan, since anytype-heart is out of scope.

**CLA / trademark:** no contributor license agreement was found gating contributions to the MIT server-node repos; standard GitHub contribution guidelines apply. No separate trademark policy document was found in this research pass. As a standard-practice flag, not a verified legal fact: do not use the "Anytype" name, logo, or branding in Yar-branded builds or marketing; this costs nothing to honor and removes any ambiguity.

Sources: [any-sync](https://github.com/anyproto/any-sync), [any-sync-node](https://github.com/anyproto/any-sync-node), [any-sync-filenode license](https://api.github.com/repos/anyproto/any-sync-filenode/license), [any-sync-coordinator license](https://api.github.com/repos/anyproto/any-sync-coordinator/license), [any-sync-consensusnode license](https://api.github.com/repos/anyproto/any-sync-consensusnode/license), [any-store license](https://api.github.com/repos/anyproto/any-store/license), [anytype-heart LICENSE.md](https://github.com/anyproto/anytype-heart/blob/main/LICENSE.md), [anytype-heart license API](https://api.github.com/repos/anyproto/anytype-heart/license), [anytype-ts license API](https://api.github.com/repos/anyproto/anytype-ts/license).

---

## 2. Maturity and Operations

| Dimension | Finding | Source |
|---|---|---|
| Minimum node topology | 4 node types: sync node, filenode, coordinator, consensusnode | any-sync-dockercompose |
| Supporting infrastructure | MongoDB (state), Redis (indexing), MinIO/S3-compatible storage, netcheck | any-sync-dockercompose |
| Minimum resource footprint | Roughly 1 GB RAM for the full reference stack; per-service idle use around 8 to 13 MiB, Redis around 4 MiB | any-sync-dockercompose, community reports |
| Network ports | TCP 33010 (DRPC), UDP 33020 (QUIC), per the community single-binary bundle | grishy/any-sync-bundle |
| Official production guidance | Docker Compose is explicitly scoped to "personal self-hosted any-sync networks"; the maintainers point to Puppet/Ansible modules for production at scale | any-sync-dockercompose |
| Community lightweight alternative | `any-sync-bundle` merges all four node types into a single Go binary and swaps MinIO for lighter local storage | grishy/any-sync-bundle |
| Self-hosting guides in the wild | Multiple independent VPS guides exist (Safecast, Xylentis, YunoHost forum), evidence of a real self-hosting community, not just official docs | Safecast guide, Xylentis blog, YunoHost forum |
| Real-world reliability signal | General sentiment: fast, near-instant sync. One review noted multi-device sync lagging 30 to 90 seconds in testing, requiring manual refresh | synthesized from 2026 product reviews |
| Maintenance activity | Active commits across the any-sync repo family as of July 2026 | github.com/anyproto/any-sync/activity |

**Fit note:** the "personal self-hosted" ceiling that the official docs describe is not a weakness for Yar's current architecture. Yar's own Django relay is explicitly built as a single-tenant "personal relay" (see `RegisterView` docstring in `views.py`: *"Personal relay, MVP trust model."*). The scale any-sync is proven at for self-hosting matches the scale Yar needs today. There is no premature-scale mismatch.

Sources: [any-sync-dockercompose](https://github.com/anyproto/any-sync-dockercompose), [any-sync-bundle](https://github.com/grishy/any-sync-bundle), [Safecast self-hosting guide](https://github.com/Safecast/AnyType-VPS/blob/main/anytype-selfhosting-guide.md), [Xylentis VPS guide](https://xylentis.com/blog/self-hosting-anytype-sync-server-on-a-vps-complete-autonomy-over-your-end-to-end-encrypted-knowledge-base), [Anytype self-hosting docs](https://doc.anytype.io/anytype-docs/advanced/data-and-security/self-hosting).

---

## 3. Go Mobile Path

| Path | Mechanism | Fit for Yar | Cost / risk |
|---|---|---|---|
| `gomobile bind` to AAR / XCFramework | The pattern Anytype's own official apps use to embed the Go core into iOS and Android | Technically proven, but the artifact being embedded (`anytype-heart`) is ASAL. Yar would need to `gomobile`-bind its own MIT-only Go client built directly on `any-sync`, which does not exist yet and would be custom work | Real: cgo/gomobile toolchain, a second GC runtime alongside Rust/Dart in one process, binary size growth (roughly 5 to 10 MB per ABI), and a CI matrix that now includes Go, Rust, and Flutter toolchains together |
| Local Go sidecar process | The pattern Anytype's own desktop client uses: the Electron UI talks to a local Go binary over gRPC, not statically linked in | Strong fit for Yar's **current** desktop app (Tauri + Rust + React): spawn or connect to an any-sync client/relay binary over localhost gRPC or a Unix socket | Low bridging risk; matches a proven production pattern; does not work on mobile OSes because of background execution limits, which `SPEC-sync-protocol.md` already lists as an open conformance gap |
| Flutter + `flutter_rust_bridge` (Yar's actual planned mobile stack) | Yar's own L6 framework decision already picked Flutter with a Rust core bridged via `flutter_rust_bridge` | Any-sync's client is Go, not Rust. There is no Rust any-sync client. Embedding any-sync natively on mobile means running Go alongside Rust in one Flutter app | Adds a second native runtime and bridge layer that the mobile stack was not designed around. The cheaper near-term path is a thin HTTP/gRPC client on mobile talking to a self-hosted any-sync node fleet, not a fully embedded P2P peer |

**Recommendation embedded in this finding:** do not push any-sync client embedding onto mobile in this phase. Desktop gets the sidecar pattern now; mobile stays a thin remote client against the self-hosted node network until the founder decides whether true mobile P2P embedding is worth a second native runtime in the Flutter app.

Sources: [gomobile command docs](https://pkg.go.dev/golang.org/x/mobile/cmd/gomobile), [Go Mobile wiki](https://go.dev/wiki/Mobile), [anytype-heart repo structure](https://github.com/anyproto/anytype-heart).

---

## 4. Protocol Fit vs. Yar's Object Model

Read directly from `backend/sync/models.py`, `views.py`, and `tests.py` in `yar-code-20260705-2354`, and from `SPEC-sync-protocol.md`.

**Yar's actual contract today:** a single append-only `Operation` table keyed by a global `server_seq` pull cursor, with `op_id` uniqueness giving idempotent push, a Lamport clock plus deterministic `sort_key` tie-break giving total order, and a pure-function reducer (`core.reducer.project`, `sort_key`, `projection_hash`) that any device or the server can run to get a bit-identical projection. Blobs are a flat sha256 content-addressed store, decoupled from the op-log. All 12 sync edge cases pass against this contract, including `duplicate_replay`, `out_of_order_chunks`, `same_lamport_tie_break`, and `delete_update_race_delete_wins` (verified directly in `tests.py`).

**any-sync's actual model:** a Merkle-DAG of signed changes per object ("tree"), grouped under spaces, with a separate consensus-node-ordered ACL log per space, per-space symmetric keys wrapped to member identities, and convergence proven per object tree (Merkle-root equality), not via one whole-log hash.

| Yar concept | any-sync equivalent | Fit | Where it bites |
|---|---|---|---|
| Global `server_seq` pull cursor | Per-object-tree DAG heads; no single global sequence | Partial | Yar's "pull since seq N" has no direct any-sync equivalent. Needs an aggregation layer over per-space heads to reconstruct cursor semantics |
| `op_id` uniqueness for idempotent push | Content-addressed change hash | Good fit | None; arguably cleaner under any-sync |
| Lamport clock + `sort_key` total order + `projectionHash` | Causal parent-hash partial order per tree; convergence proven per-object | Partial mismatch | Yar's single whole-log `projectionHash` concept does not exist in any-sync. Yar's reducer must keep computing its own total order and hash on top of whatever any-sync delivers |
| `object.tombstoned` with deterministic tombstone-beats-update precedence | No built-in precedence rule; this logic lives in `anytype-heart`'s object/type model (ASAL, excluded) | Reimplement | Yar's own reducer (already tested 12/12) stays authoritative for this. Any-sync trees carry the same ops as opaque payloads; any-sync's own merge semantics must not be relied on here |
| Flat sha256 blob store, no encryption | `any-sync-filenode`: encrypted, key-wrapped, IPLD-derived content-addressed blobs bound to a space | Superset, not a mismatch | Requires the ACL/space/key layer to exist first. Yar has none of it: `Device` is a flat actor with a bearer token, and `Operation.payload` is a plaintext `JSONField` today |
| No account/space/ACL/encryption model | Space = mandatory unit of membership, ACL, and per-space keys | **Biggest gap** | This is the real cost of adopting any-sync, not the wire protocol. It is already tracked as open item O-3 (key custody + ACL design) in `SPEC-sync-protocol.md`, independent of which sync backend is chosen |

**Conclusion of this section:** the wire-protocol shape mismatch (global log vs. per-object DAG) is real but manageable, because Yar's reducer already isolates application logic behind pure functions that take a plain list of wire-format ops. The genuinely expensive gap is the ACL/key/space model any-sync requires as a package deal, which Yar would have had to build anyway for any production sync backend.

---

## 5. Verdict: Adopt Now, Narrowly Scoped

**Adopt any-sync now for transport, relay, and blob duties. Do not adopt its object/ACL/key model as Yar's source of truth in this phase.**

Reasoning:

1. **Licensing is clean and low-risk.** Every component Yar would touch is MIT, confirmed today, no CLA burden. The one real license boundary (ASAL on `anytype-heart` and the official clients) is already excluded by D3 and matches the exclusion `SPEC-sync-protocol.md` already recommended.
2. **Maturity matches Yar's actual deployment scale.** Any-sync is production-proven at Anytype's userbase, and its self-host docs are explicitly scoped to "personal" networks, which is exactly what Yar's current single-tenant Django relay already is.
3. **Yar's reducer contract is transport-agnostic by design.** `project()`, `sort_key()`, and `projection_hash()` operate on a plain list of wire-format ops; nothing in that code cares which transport delivered them. Any-sync can sit behind that contract as a pipe without displacing it.
4. **The expensive part (ACL/key custody/space model) was already coming.** It is open item O-3 in `SPEC-sync-protocol.md` regardless of sync backend. Borrowing any-sync's design for it, as the spec already suggests, is reuse, not new scope.
5. **Mobile is the one place to hold back.** Yar's own L6 decision already committed mobile to Flutter + `flutter_rust_bridge` (Rust core). Any-sync's client path is Go-only via `gomobile`. Running two native runtimes in one mobile app is avoidable complexity before YC. Mobile should stay a thin HTTP/gRPC client against the self-hosted node fleet for now.

### Minimum Integration Plan (2-person team)

| Phase | Work | Duration |
|---|---|---|
| 0 | Stand up the 4-node any-sync network locally via `any-sync-dockercompose` or the lighter `any-sync-bundle`; confirm the roughly 1 GB RAM footprint on Yar's existing target infra | 2 to 3 days |
| 1 | Write a minimal Go adapter that creates one space and pushes/pulls Yar's existing wire-format ops as opaque change payloads inside an any-sync tree; re-run the existing 12-case edge benchmark against this **real** backend instead of only the simulated harness | 1 to 2 weeks |
| 2 | Desktop-only integration: Tauri spawns or connects to the any-sync client as a local sidecar process (mirroring Anytype's own desktop architecture), taking over the relay role for desktop-to-desktop and desktop-to-self-hosted-node sync. Keep the existing Django push/pull/ack HTTP API alive in parallel as the mobile-facing thin-client surface | 1 to 2 weeks |
| 3 (deferred past YC) | Full ACL + per-space key wrapping + `any-sync-filenode` blob migration + true mobile P2P embedding | Not scoped here; matches already-open items O-3 and O-4 in `SPEC-sync-protocol.md` |

**Total estimate: 4 to 6 engineer-weeks for Phases 0 to 2**, consistent with the "not YC-blocking" framing already used for D3/D4 in `YAR-MASTER-PLAN_2026-07-16.md`.

**What stays untouched:** the op-log wire format (`opId`, `actorId`, `lamport`, `type`, `objectId`, `payload`), the reducer contract (`project`, `sort_key`, `projection_hash`), the 12-case edge benchmark, and the existing Django HTTP API surface (`push`, `pull`, `ack`, `heads`) all stay exactly as built. Any-sync sits behind them as a transport, never in front of them.

### Exit Strategy (Post-YC Swap to Loro + Iroh)

Because any-sync is scoped to transport/relay/blob duties only, and Yar's reducer stays authoritative, swapping to Loro + Iroh later is a transport-layer swap, not an application rewrite:

1. Write a new transport adapter that speaks the same pull/push/ack contract already exposed in `views.py` (already transport-agnostic).
2. Migrate content-addressed blobs from `any-sync-filenode` to `iroh-blobs`. Both are content-addressed, so this is a data copy and re-key job, not a schema rewrite.
3. Decommission the any-sync node fleet.

No application-level rewrite is required, because any-sync's object/ACL model was deliberately never allowed to become Yar's source of truth.

---

## Open Flag for the Founder

D3 as written in `YAR-MASTER-PLAN_2026-07-16.md` ("adopt any-sync protocol + Go server nodes now") could be read as adopting the full stack, ACL and key model included. This assessment recommends the narrower reading: transport, relay, and blob layer only, in phase 1. Recommend confirming that narrower scope explicitly as an addendum to D3, since it changes the effort estimate from "large, ACL-and-keys-included" to "4 to 6 weeks, transport-only."

---

## Related documents

- [`SPEC-sync-protocol.md`](./SPEC-sync-protocol.md) -- the protocol this assessment evaluates Any-Sync against.
- [`SPEC-storage-engine.md`](./SPEC-storage-engine.md) -- the storage-engine decision (D3/D4) this assessment's `decision_ref` points at.
- [`../research/yar-framework-assessment_2026-07-16.md`](../research/yar-framework-assessment_2026-07-16.md) -- companion app-framework call made in the same session.
- [`STORAGE_BENCHMARK_TRACKER.md`](./STORAGE_BENCHMARK_TRACKER.md) -- open decisions O-1 through O-8, including sync.
