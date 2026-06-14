> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `substrate`, `research`, `decision`

# Yar substrate decision report

## Executive verdict

If you force the decision to a **single existing PKM platform**, the strongest off-the-shelf match for Yar today is **Anytype**. It is local-first, encrypted, object-based, schema-oriented, cross-platform, supports local-only and self-hosted modes, and now exposes a localhost **Local API** with official developer docs, object/type/property CRUD, and an official MCP server. That combination makes it the closest existing product to the substrate you described. citeturn26view4turn26view3turn26view0turn27search4turn27search2turn27search6turn27search7turn5search2

That said, **Anytype is not my actual recommendation** for Yar as a company/product architecture. My recommendation is a **hybrid MVP** in which **Yar owns the canonical local object runtime from day one**, while **Obsidian serves as the temporary shell/capture surface and interoperability layer**. Obsidian gives you local Markdown files, no app telemetry for the core apps, official desktop/mobile apps, an official web clipper, a mature plugin API, structured properties, and Bases for database-like views. Those qualities make it much easier to move fast without handing your long-term authority model to a third-party product. citeturn6search0turn6search1turn7search3turn7search5turn29search0turn30search0turn30search8

So the decisive answer is:

**Best immediate MVP path:** a **hybrid** architecture with a **Yar-owned local runtime** plus an **Obsidian shell/plugin** for capture, browsing, and rapid iteration.

**Best long-term architecture:** a **Yar-native local-first object runtime** with **CAP as the sole execution authority**, a custom cross-platform UI, optional sync, and existing PKM tools treated as import/export or adapter targets, not as the system of record. The local-first database/sync ecosystem strongly supports this direction: Replicache focuses on optimistic local mutators, ElectricSQL syncs scoped subsets of Postgres into local apps, RxDB is explicitly local-first/offline-first with replication, and SurrealDB supports both schemafull and graph-style relationship modeling. These are useful building blocks, but not complete product substrates by themselves. citeturn47search4turn47search1turn47search2turn47search14turn47search3turn47search19turn47search23

A practical corollary follows from that verdict: **do not make Anytype, Obsidian, Logseq, Tana, Capacities, Notion, or any other PKM app the canonical source of truth for Yar**. CAP needs to govern every AI read, write, suggestion, refusal, audit record, and consent boundary. That requirement is easier to satisfy cleanly when Yar owns the runtime and treats outside tools as shells or adapters. citeturn27search9turn16search16turn16search17turn45view1

## What Yar actually needs from a substrate

Yar is not “a notes app with AI.” Your requirements imply a product that needs **typed long-lived entities**, **governed AI operations**, **privacy-preserving defaults**, **frictionless capture**, and a **companion-like interaction model**. In practical architectural terms, that means the substrate must do more than store blocks or pages. It must support a stable canonical schema for objects like `Task`, `Project`, `Person`, `Source`, `Decision`, `Reflection`, `CommunicationInsight`, `DailyPlan`, and `StateObservation`, while also preserving provenance and links between them. Platforms that only offer pages plus ad-hoc tags or lightweight properties usually distort this model over time. Platforms with real object typing do much better. Anytype, Capacities, and Tana are strongest on the “typed object” dimension among existing products; Obsidian and Joplin are much stronger on portability and controllability; custom runtimes are best overall because the schema belongs to Yar rather than to a vendor. citeturn27search6turn27search7turn15search2turn15search6turn14search0turn31search4turn29search0turn30search0turn44search0

The **CAP requirement** sharply changes the ranking. Many tools let an integration read and write content. Far fewer let you model **least privilege**, **object- or property-level consent**, **staged writes**, **typed execution reports**, and **refusal records** in a first-class way. Notion has explicit integration capabilities and page/database permissions, but it is still cloud-first and the trust boundary sits with Notion, not with Yar. Capacities’ MCP is promising but currently exposes a narrow tool set and is still beta. Anytype’s Local API is a stronger fit because it runs on localhost and supports object/type/property operations, but it still does not natively make CAP the authority layer; CAP would need to sit in front of it. Obsidian’s plugin model is less object-native, but it gives Yar the cleanest opportunity to mediate all AI operations locally through a plugin and sidecar runtime. citeturn16search16turn16search9turn16search17turn45view1turn26view0turn27search2turn27search6turn27search7turn7search3turn7search0

The **privacy and mental-health-adjacent** requirement also eliminates several otherwise attractive tools. Capacities openly says sync to servers cannot be disabled and explains that it intentionally does not use E2EE because strong APIs, AI, and current integrations depend on server access. Notion is fundamentally cloud-based and its offline mode is a controlled local cache rather than a local-first ownership model. Tana has made real progress with offline desktop support and a Local API/MCP endpoint, but it remains a proprietary cloud-centered system with an increasingly agentic product direction. Those tools may be excellent for general productivity knowledge work, but they push too much trust outside Yar for the kind of companion you are describing. citeturn45view0turn46search0turn45view3turn33search1turn16search1turn31search2turn14search3turn31search16

Finally, Yar’s **non-shaming, neurodivergent-friendly** UX goal matters. Tana and Capacities feel closer than most tools to “structured, living knowledge” for non-technical users, but both compromise the privacy boundary. Obsidian, Logseq, SiYuan, and Trilium give you more control but tend to feel more tool-like and more demanding. Anytype has one of the best UX balances among local-first object systems, which is why it remains the best off-the-shelf fallback even though it is not the best architectural destination. citeturn14search2turn15search2turn15search9turn26view4turn39search6turn43search0

## Candidate-by-candidate assessment

**Anytype** — Short description: a local-first, encrypted, object-based knowledge system with custom types, relations, peer-to-peer sync, local-only mode, and now a localhost Local API plus official MCP tooling. Strengths for Yar: this is the best existing match for typed PKG requirements; its data model is genuinely object/type-centric rather than file-centric, and the new Local API makes AI read/write automation much more realistic than it used to be. Weaknesses for Yar: the desktop client code is source-available rather than permissively open source; the API is still young; mobile still lacks some views/features; and Anytype still reports app-usage analytics unless you block hosts or rebuild. AI/CAP feasibility is **good but not native**: Yar can sit in front of the Local API and wrap every call in CAP, but least privilege and consent are still your responsibility, not the platform’s. Privacy/local-first is **excellent in storage and sync model**, but the analytics caveat matters for sensitive reflection. Licensing/strategic risk is **material** because the desktop app uses the Any Source Available License, not MIT/Apache. **MVP 8/10. Long-term 6/10. Role: MVP-only substrate.** citeturn26view4turn26view3turn26view0turn26view1turn26view2turn27search4turn27search2turn27search6turn27search7turn5search16

**Obsidian** — Short description: a local Markdown vault app with desktop/mobile clients, official web clipping, local properties, Bases views, and an unusually mature plugin ecosystem. Strengths for Yar: maximum data ownership, no required account, no app telemetry, official clipper, strong developer ergonomics, and very low migration risk because the data stays in local files. Weaknesses for Yar: the data model is file-centric, not object-native; typed objects are emulated through frontmatter/templates/Bases; and a companion-like experience requires you to build it yourself through plugins and custom views. AI/CAP feasibility is **very strong** because a Yar plugin plus local sidecar can intercept reads/writes and stage proposed changes before they touch the vault. Privacy/local-first is **excellent**, with optional E2EE only if you opt into Sync; the main privacy risk comes from plugins and any model provider you wire in. Licensing/strategic risk is moderate: the app is proprietary, but the data format is durable and portable. **MVP 8/10. Long-term 7/10. Role: adapter target.** citeturn6search0turn6search1turn7search3turn7search5turn29search0turn30search0turn30search8turn30search6

**Logseq** — Short description: an open-source, privacy-first outliner/graph tool with file-based graphs and an evolving DB mode. Strengths for Yar: strong block graph semantics, Datalog-style querying, plugin APIs, and open-source control. Weaknesses for Yar: the product is in a transitional period between file graphs and DB graphs; the DB version uses SQLite; the sync story is split between open-source MD sync and a newer non-open-source RTC path for DB sync; and the DB mobile story is still catching up. AI/CAP feasibility is **possible but unstable** because plugin and DB APIs are evolving, and the architectural transition increases integration risk. Privacy/local-first is strong in principle, but the fast-moving storage/sync model increases operational risk for a production companion. **MVP 6/10. Long-term 5/10. Role: inspiration only.** citeturn8search0turn12search0turn11search2turn11search7turn11search9

**Tana** — Short description: a highly structured knowledge graph workspace built around nodes, fields, supertags, mobile capture, and increasingly agentic AI behavior. Strengths for Yar: superb typed-structure UX, strong mobile capture, voice memo workflows, JSON/Markdown export, and now a desktop Local API/MCP endpoint. Weaknesses for Yar: proprietary control, cloud-centered trust, and a product trajectory that is increasingly about Tana’s own agentic system rather than CAP-as-external-governor. AI/CAP feasibility is **medium** because the Local API/MCP helps, but the authority model is not really yours. Privacy/local-first is the deal-breaker: desktop offline mode exists, but the product is not local-first in the Yar sense. **MVP 6/10. Long-term 3/10. Role: reject.** citeturn14search0turn14search2turn14search3turn14search4turn31search3turn31search16

**Capacities** — Short description: an object-type-based knowledge workspace with polished UX, offline-first behavior, local caching, object properties, graph views, REST API, and MCP support. Strengths for Yar: strong object model, very good non-technical usability, export to Markdown/frontmatter/CSV, and emerging AI/MCP integration. Weaknesses for Yar: it is explicitly cloud-based, sync cannot be disabled, it intentionally does not use E2EE, local data is not encrypted on-device, and the current MCP surface is still narrow. AI/CAP feasibility is **promising but incomplete**: the beta MCP supports search, content retrieval, object links, and writing to the daily note, but not the full object-runtime governance Yar needs. Privacy/local-first is **not sufficient** for a mental-health-adjacent companion because the authoritative data path is server-based and non-E2EE by design. **MVP 5/10. Long-term 3/10. Role: reject.** citeturn45view0turn15search2turn15search6turn15search12turn45view1turn45view2turn45view3turn46search0

**Notion** — Short description: a polished cloud workspace with databases, properties, collaboration, offline caching, and a mature public REST API. Strengths for Yar: excellent API, page/database schema support, scoped integration capabilities, and broad user familiarity. Weaknesses for Yar: it is the opposite of local-first ownership, and the offline story is cached-page access inside a cloud product rather than local-first authority. AI/CAP feasibility is **mechanically good but strategically wrong**: the API can read, create, update, and search, but CAP would be layered on top of a cloud workspace whose permission model is not designed around sensitive personal reflection. Privacy/local-first is insufficient for Yar’s core promise. **MVP 4/10. Long-term 2/10. Role: reject.** citeturn16search16turn16search9turn16search17turn16search18turn33search1turn33search2turn33search3turn33search8

**AppFlowy** — Short description: an AGPL open-source Notion alternative built with Flutter/Rust, with local control, self-hosting options, collaborative data-layer crates, and local AI plugin work. Strengths for Yar: open-source control, local/native clients, self-hosting, an extensible collaboration/data layer based on `yrs`, and a local AI plugin system with an Ollama plugin. Weaknesses for Yar: its core model is still primarily docs + databases rather than a semantically typed object graph; backlink/relationship knowledge behavior is weaker than Anytype/Tana/Logseq; and official documentation reads more like a contributor architecture map than a stable app-extension surface. AI/CAP feasibility is **better than many people assume** because the codebase is open and LAI/Collab are real; but you may end up forking rather than integrating. Privacy/local-first is good, but AppFlowy staff have explicitly said they do **not** provide end-to-end encryption. **MVP 7/10. Long-term 6/10. Role: adapter target.** citeturn35search1turn35search2turn18search2turn18search4turn17search6turn34search7

**AFFiNE** — Short description: a local-first, MIT-licensed open-source workspace blending docs, whiteboards, and databases, with self-hosting and AI features. Strengths for Yar: open source, local-first positioning, self-hosting, and a modern docs/canvas/database blend that is appealing for planning and organization. Weaknesses for Yar: the model is still block/doc/collection oriented rather than strongly typed object-runtime oriented; plugin/community block extensibility is still “coming soon” in the repo language; and the hosted privacy policy clearly covers usage/device/location/AI input data collection for the service. AI/CAP feasibility is currently weaker than Obsidian or Anytype because extension points are less mature. Privacy/local-first is acceptable only if you self-host and control the stack closely. **MVP 6/10. Long-term 5/10. Role: inspiration only.** citeturn19search1turn36search3turn36search8turn36search0turn38search0turn38search2

**SiYuan** — Short description: a privacy-first, self-hosted, fully open-source PKM with block references, custom attributes, SQL query embeds, web clipping, offline usage, and E2EE sync. Strengths for Yar: very strong privacy/story for local usage, solid block/query model, custom attributes, official desktop/mobile projects, and multiple sync options through official or third-party services. Weaknesses for Yar: UX is more technical, API documentation remains sparse, and the Bazaar/plugin ecosystem had serious recent security advisories including remote code execution vectors from malicious marketplace content. AI/CAP feasibility is **possible but less comfortable**: the platform is powerful, but the integration/documentation experience is rougher than Obsidian/Joplin/Anytype. Privacy/local-first is strong if you avoid unsafe marketplace behavior and keep integrations tightly controlled. **MVP 6/10. Long-term 6/10. Role: inspiration only.** citeturn21search3turn39search6turn39search5turn39search1turn40search0turn21search2turn39search0turn39search3

**Trilium Notes** — Short description: a scriptable hierarchical PKM that uses notes, attributes, relations, promoted attributes, relation maps, and an external REST API. Strengths for Yar: robust ETAPI, scripting, custom request handlers, relations, promoted attributes, protected notes encryption, and active maintenance in the current TriliumNext/Trilium repo. Weaknesses for Yar: the UX is better for power users than mainstream companion use, mobile is still a known gap, and its modeling style is flexible but not as cleanly object-typed as Anytype or Tana. AI/CAP feasibility is good because ETAPI is comprehensive and scripting is strong. Privacy/local-first is good, especially with protected notes and self-hosted sync, but note metadata and attributes are not all encrypted in protected notes. **MVP 5/10. Long-term 5/10. Role: inspiration only.** citeturn43search0turn43search1turn42search0turn22search1turn22search11turn42search9turn43search20

**Joplin** — Short description: a privacy-focused note app with Markdown storage, offline-first sync, E2EE, data API, plugin API, mobile support, scan workflows, and browser clipper. Strengths for Yar: highly reliable local/offline behavior, good cross-platform support, explicit E2EE, and mature programmatic APIs. Weaknesses for Yar: the knowledge model is notes/notebooks/tags rather than typed first-class objects and relations, so Yar’s canonical schema gets flattened. AI/CAP feasibility is good for note operations, but the shape of the data will fight you on relationship memory and typed cognitive objects. Joplin is excellent as a capture or archival adapter, not as Yar’s substrate. **MVP 6/10. Long-term 4/10. Role: adapter target.** citeturn44search0turn23search0turn23search4turn23search7turn23search11turn23search2

**Athens Research and Roam-like systems** — Short description: Athens was an open-source/local-first-style Roam alternative, but the official repo now says it is no longer maintained; Roam remains primarily a cloud-first networked-thought app. Strengths for Yar: the block-graph/block-ref mental model remains influential and conceptually important. Weaknesses for Yar: Athens is effectively dead as a strategic base, and Roam-like systems generally put you back into a block-graph world without strong local-first guarantees or a stable, open, typed runtime. **MVP 2/10. Long-term 1/10. Role: reject.** citeturn24search0turn24search1turn24search3turn24search5

**Custom local-first stack using SQLite/DuckDB plus sync plus React Native or Flutter** — Short description: a Yar-native runtime with a local relational/object core, append-only event log, blob store, optional sync, and your own UI. Strengths for Yar: perfect CAP compatibility, clean typed schema mapping, real least-privilege enforcement, per-object local-only flags, exportability, exact UX control, and no forced vendor semantics. Weaknesses for Yar: more up-front engineering and product work. AI/CAP feasibility is the best of all candidates because CAP becomes a first-class runtime primitive, not a wrapper. Privacy/local-first is the strongest possible outcome if you keep cloud optional. **MVP 7/10. Long-term 10/10. Role: primary substrate.** citeturn47search2turn47search14turn47search4turn47search1turn47search3turn47search19

**Custom graph/object DB layer using SurrealDB, RxDB, ElectricSQL, Replicache, Automerge, Yjs, or similar** — Short description: infrastructure rather than a product substrate. Strengths for Yar: these tools solve critical pieces of the problem. Replicache gives you optimistic local mutators; ElectricSQL gives you scoped sync from Postgres into local apps via Shapes; RxDB gives you an in-app local-first DB with replication; SurrealDB supports schemafull and graph-style relationships. Weaknesses for Yar: none of them by itself gives you typed cognitive objects, CAP directives, consent semantics, audit records, or companion UX. My recommendation is to treat this candidate as a **toolbox**, not as a singular answer. **MVP 6/10. Long-term 9/10. Role: primary substrate.** citeturn47search4turn47search1turn47search2turn47search14turn47search3turn47search19turn47search23

**Hybrid architecture with an existing PKM interface for MVP and a Yar runtime later** — Short description: start with an adapter/shell on top of a Yar-owned local runtime, then phase out dependence on third-party UX. Strengths for Yar: best speed-to-learning without surrendering long-term control. Weaknesses for Yar: you must be disciplined about keeping the external PKM layer non-canonical. This is the highest-scoring practical option because it optimizes both MVP learning speed and long-term architectural integrity. **MVP 9/10. Long-term 10/10. Role: primary substrate.** citeturn6search0turn7search3turn7search5turn26view0turn27search4turn47search2turn47search4

## Comparison table and ranked shortlist

The table below is a synthesis of the evidence above. The scores are judgment calls, not vendor-provided claims.

| Candidate | MVP suitability | Long-term suitability | Recommended role | Bottom-line judgment |
|---|---:|---:|---|---|
| Hybrid: Yar runtime + external shell | 9 | 10 | Primary substrate | Best overall path |
| Custom local-first stack | 7 | 10 | Primary substrate | Best long-term foundation |
| Custom graph/object DB layer toolbox | 6 | 9 | Primary substrate | Best infra family, not a full product |
| Anytype | 8 | 6 | MVP-only substrate | Best existing off-the-shelf substrate |
| Obsidian | 8 | 7 | Adapter target | Best shell/interoperability layer |
| AppFlowy | 7 | 6 | Adapter target | Good open-source alternative, weaker graph semantics |
| SiYuan | 6 | 6 | Inspiration only | Strong privacy, rougher integration/security ergonomics |
| Logseq | 6 | 5 | Inspiration only | Great ideas, too much platform transition risk |
| Joplin | 6 | 4 | Adapter target | Excellent capture/archive adapter, weak typed graph |
| Trilium Notes | 5 | 5 | Inspiration only | Powerful for power users, weak mainstream companion fit |
| Tana | 6 | 3 | Reject | Great schema UX, wrong trust boundary |
| Capacities | 5 | 3 | Reject | Lovely object UX, not local-first enough |
| AFFiNE | 6 | 5 | Inspiration only | Promising local-first workspace, not yet the right runtime |
| Notion | 4 | 2 | Reject | Great API, fundamentally wrong architecture for Yar |
| Athens / Roam-like systems | 2 | 1 | Reject | Historically important, strategically unsuitable |

The **ranked shortlist** is:

**Hybrid Yar runtime + Obsidian shell**, **custom local-first Yar runtime**, **Anytype**, **Obsidian**, **AppFlowy**. The reason AppFlowy makes the top five instead of Tana or Capacities is not that it has a better end-user UX today; it is that it keeps more architectural control in your hands and is materially safer for a local-first companion product. citeturn35search1turn18search2turn18search4turn14search4turn45view1

If you absolutely refuse to build a Yar-owned runtime in the MVP, then the recommendation changes slightly:

**Best off-the-shelf MVP-only substrate:** **Anytype**.  
**Best open data / plugin shell:** **Obsidian**.  
**Best open-source forkable workspace alternative:** **AppFlowy**. citeturn26view0turn27search4turn7search3turn7search5turn35search1turn18search2

## Recommended architecture and migration path

**Best immediate MVP choice:** **Hybrid architecture with Yar’s own local runtime and Obsidian as the temporary shell.** This is the recommendation because it preserves your most important invariant: **CAP remains the authority and control layer**. Obsidian offers the easiest route to quick capture, browser clipping, mobile/desktop use, local files, and plugin-side AI orchestration, while Yar keeps the canonical schema, authority logic, evidence model, and audit trail in its own runtime. citeturn6search0turn7search5turn29search0turn30search8turn47search2turn47search4

**Best long-term architecture:** **Yar-native local object runtime with custom cross-platform UI.** The canonical source of truth should not be a third-party vault, graph, or cloud workspace. It should be a **local SQLite-based typed object store** with: a schema registry; append-only event/audit log; content/blob store; vector/FTS indexing; per-object/local-only flags; CAP directives for every action; and an adapter layer for import/export with Markdown vaults, Anytype objects, Joplin notes, and optionally Notion/Tana/Capacities export feeds. DuckDB can be added later for reflective analytics and longitudinal pattern work, but it should not be the primary transactional store. citeturn47search2turn47search14turn47search3turn47search23

A good text-form architecture looks like this:

```text
[Yar UI]
  ├─ Mobile/Desktop surface
  ├─ Capture inbox
  ├─ Daily planning view
  ├─ Relationship memory view
  └─ Review / approve AI changes

        ↓

[CAP Gateway]
  ├─ Read policy enforcement
  ├─ Write policy enforcement
  ├─ Consent checks
  ├─ Sensitive-scope blocking
  ├─ Staging / review queue
  ├─ Execution reports
  └─ Audit / refusal log

        ↓

[Yar Runtime]
  ├─ Typed object schema registry
  ├─ Local SQLite object store
  ├─ Append-only event log
  ├─ Full-text + semantic index
  ├─ Blob store for sources/media
  ├─ Link / evidence engine
  └─ Adapter framework

        ↓
   ┌───────────────┬────────────────┬────────────────┐
   │               │                │                │
[Local models] [Capture adapters] [PKM adapters] [Optional sync]
 Gemma/Ollama   Browser clipper     Obsidian         User-controlled
 Embeddings     Email/share sheet   Anytype import   E2EE later
 Rewriters      OCR/transcript      Joplin import
```

The migration strategy, if the MVP shell differs from the long-term UI, should be **non-destructive and adapter-based**. In the MVP, Obsidian can receive mirrored Markdown projections of Yar objects for searchability and familiar browsing. Over time, the Yar UI replaces more of the interaction surface, while Obsidian becomes optional. If you choose Anytype instead of Obsidian for an off-the-shelf MVP, the same rule applies even more strongly: treat Anytype as a consumable shell, not as the canonical runtime, because export/migration friction and strategic control risk are substantially higher. citeturn15search12turn5search0turn6search1turn44search0

## Risk register, decision memo, and prototype plan

**Risk register**

| Risk | Likelihood | Impact | Why it matters | Mitigation |
|---|---:|---:|---|---|
| Third-party substrate becomes de facto authority | High | High | CAP gets weakened if platform semantics govern reads/writes | Keep Yar runtime canonical from day one |
| Typed schema distortion in file/block products | High | High | `Person`, `Decision`, `Reflection`, `StateObservation` collapse into generic notes | Use strict Yar schemas and projections |
| Privacy leakage through hosted AI or telemetry | Medium | High | Especially bad for reflection / mental-health-adjacent features | Default to local models, opt-in external providers, disable/avoid telemetry-heavy shells |
| Plugin / extension attack surface | Medium | High | Obsidian plugins, SiYuan Bazaar, browser capture surfaces all expand risk | Signed allowlist, minimal plugin set, sandbox sidecar, CAP-mediated writes |
| Vendor lock-in / license change | Medium | High | Anytype source-available risk, Tana/Capacities/Notion cloud lock-in | Prefer open formats and adapter-driven migration |
| Local-first sync complexity | High | Medium | Conflict handling and cross-device merge logic are deceptively hard | Start single-device-first; add sync after CAP/event model stabilizes |
| Model overreach in sensitive cognition features | Medium | High | A generic chatbot feel would betray Yar’s brief | Use structured tools and constrained action plans, not open-ended agent autonomy |
| Overbuilding in the first month | High | High | You can lose the MVP by chasing infra perfection | Build only the typed runtime slice needed for capture, structuring, planning, and rewrite workflows |

**Final decision memo for a technical supervisor**

Yar should **not** be built on top of Anytype, Obsidian, Tana, Capacities, Notion, or any other PKM platform as its canonical substrate. The key architectural reason is CAP. Yar’s defining differentiator is not notes, graph views, or AI prompts. It is **governed cognition**: controlled reads, staged writes, consent boundaries, evidence-linked outputs, refusal semantics, and least-privilege execution. That is a runtime concern, not a note-app concern. Existing PKM tools can accelerate UI and capture, but they should not own the authority boundary. citeturn26view0turn16search16turn45view1turn7search3

The recommended approach is therefore a **hybrid MVP**. Implement a Yar-owned local runtime immediately, but keep the initial surface area intentionally narrow. Pair it with an Obsidian shell because Obsidian offers the fastest route to local capture, browser clipping, structured properties, database-like views, and plugin-side orchestration without forcing a cloud trust boundary or a proprietary object schema. This provides high learning velocity while protecting the long-term architecture. citeturn6search0turn7search5turn29search0turn30search0

Anytype should be regarded as the **best off-the-shelf fallback**, not the best architectural answer. It is much closer than most alternatives to the shape of Yar, especially after the addition of the Local API and MCP support. However, the source-available licensing posture, analytics caveat, younger developer surface, and higher risk of external schema dependence make it a weaker strategic foundation than a Yar-owned runtime. If the team wants to experiment quickly with a “native typed object” UX before building more of Yar’s own shell, Anytype is defensible as an MVP-only substrate. citeturn26view0turn26view1turn26view2turn27search4

**Concrete 30-day prototype plan**

**Exact architecture.** Build a desktop-first prototype with four components: a local **Yar Core** service; an **Obsidian plugin** as the shell; a **browser capture extension** that sends normalized captures into Yar Core; and a **local model service** running Gemma through Ollama or an equivalent local inference server. Yar Core should use **SQLite** for objects and event logs, **FTS** for retrieval, and a filesystem blob store for source artifacts and attachments. Every model request must run through the **CAP Gateway** before any read/write occurs. Obsidian is only a projection layer: it renders or mirrors specific Yar objects to Markdown for browsing, not the other way around unless explicitly imported under CAP rules. citeturn7search3turn7search5turn47search2turn47search14

**Required adapters.** Build only four adapters in the first month: an Obsidian projection adapter; a browser/web capture adapter; a plain-text/share-sheet import adapter; and a local model adapter. Do **not** build Anytype, Notion, Tana, or Capacities adapters in the first 30 days. Those are distractions until the CAP and schema core is stable. citeturn7search5turn23search11turn5search0turn33search2

| Adapter | Purpose | Direction |
|---|---|---|
| Obsidian plugin | Browse objects, review staged changes, quick capture from within shell | Yar ⇄ Obsidian |
| Browser capture extension | Save URLs, selected text, article extracts, metadata | Browser → Yar |
| Inbox/share adapter | Dump text/audio transcript snippets into Inbox/Reflection/Capture | External → Yar |
| Gemma local model adapter | Structuring, rewrite, summarization, classification | Yar ⇄ local model |

**Initial data schemas.** Keep the first schema set small and typed:

| Type | Minimum fields |
|---|---|
| `Capture` | `id`, `created_at`, `source_kind`, `raw_text`, `url`, `attachments[]`, `ingest_status`, `sensitivity`, `evidence_refs[]` |
| `Task` | `id`, `title`, `status`, `due_at`, `energy`, `project_ref`, `person_refs[]`, `source_refs[]`, `created_from_capture_ref`, `sensitivity` |
| `Project` | `id`, `title`, `state`, `goal`, `active`, `person_refs[]`, `source_refs[]`, `decision_refs[]` |
| `Person` | `id`, `name`, `relationship_type`, `communication_prefs`, `topics[]`, `last_contact_at`, `memory_confidence` |
| `Source` | `id`, `title`, `url`, `captured_at`, `source_type`, `content_hash`, `blob_ref`, `citation_data` |
| `Decision` | `id`, `title`, `summary`, `made_at`, `rationale`, `evidence_refs[]`, `project_ref`, `person_refs[]` |
| `Reflection` | `id`, `created_at`, `prompt_kind`, `text`, `mood_tags[]`, `sensitivity`, `visibility_scope`, `evidence_refs[]` |
| `DailyPlan` | `id`, `date`, `intent`, `top_tasks[]`, `constraints[]`, `gentle_notes`, `generated_by`, `approved_at` |
| `CommunicationInsight` | `id`, `created_at`, `message_ref`, `tone_summary`, `risk_flags[]`, `rewrite_options[]`, `person_ref`, `consent_scope` |
| `StateObservation` | `id`, `created_at`, `observation_kind`, `text`, `tags[]`, `confidence`, `sensitivity` |
| `CapDirective` | `id`, `scope`, `actor`, `allowed_reads[]`, `allowed_writes[]`, `requires_confirmation[]`, `forbidden_actions[]`, `expires_at` |
| `ExecutionReport` | `id`, `action_type`, `requested_by`, `directive_ref`, `inputs`, `reads`, `writes_staged`, `writes_committed`, `evidence_refs[]`, `status`, `refusal_reason` |

**CAP-controlled actions.** Limit the prototype to a very small action vocabulary. CAP should decide whether the model may: read specific object types; read specific fields inside sensitive types; propose object creation; propose updates; commit an approved update; create links between objects; produce a rewrite; or refuse the action. Hard-delete should not exist in the prototype. Sensitive reads from `Reflection`, `StateObservation`, or certain `Person` fields should require explicit confirmation unless the object already has an allowlisted directive. Every model action should produce an `ExecutionReport`, including refusals. citeturn27search9turn16search17turn45view1

**Gemma integration points.** Use Gemma locally for five bounded jobs only: capture classification, braindump structuring, daily-plan drafting, communication rewriting, and evidence-grounded summary generation. For all five jobs, Yar should first assemble an explicit context packet under CAP, then call the model with a structured output schema. The model should never receive the entire vault or entire runtime by default. It receives only the selected objects and fields authorized by the active `CapDirective`. That keeps the system from degrading into a generic “chat over everything” experience. citeturn47search4turn45view2

**Demo scenario.** The best 30-day demo is a single coherent workflow:
A user clips two articles from the browser, pastes a braindump about an overloaded week, and shares one tricky message from a colleague. Yar creates `Source` objects for the clips, converts the braindump into a `Capture`, proposes a `Project`, three `Task` objects, one `Decision`, and a `DailyPlan`, then produces two alternative rewrites for the colleague message and one `CommunicationInsight`. CAP allows reading the fresh captures and sources, but blocks access to older `Reflection` objects marked sensitive. The user reviews all proposed writes in a single “approve changes” view, accepts some, rejects some, and receives an `ExecutionReport` showing exactly what was read, proposed, refused, and committed.

**Success criteria.** After 30 days, the prototype succeeds if it demonstrates all of the following:
a local runtime that survives app restarts; typed object creation; CAP-mediated model reads/writes; browser semantic capture into typed objects; braindump-to-structure flow; a gentle daily plan flow; and communication rewrite with evidence-linked provenance. It also succeeds if the data can be exported cleanly to JSON plus Markdown projections without losing object identity. It does **not** need multi-device sync, collaboration, or autonomous agent loops to count as a success.

| Criterion | Pass condition |
|---|---|
| Frictionless capture | Browser clip or text dump lands in Yar in under 5 seconds |
| Typed PKG | At least 8 core object types implemented and linked |
| CAP enforcement | Every model read/write/refusal appears in an execution report |
| Gentle planning | User can approve a daily plan generated from captures/tasks |
| Communication help | User gets at least 2 rewrites plus a tone/risk explanation |
| Portability | Export to JSON + Markdown projection works |
| Privacy posture | No cloud dependency required for core flows |

**What should deliberately not be built yet.** Do not build multi-device sync, voice agents, full relationship CRM, generalized memory retrieval over everything, health scoring, wearable integrations, autonomous background agents, team collaboration, or a complicated CRDT layer in the first month. Those all become easier and safer after the CAP/event model, schema boundaries, and approval flow are proven on one local device.

**Open questions and limitations.** A few areas remain materially uncertain without deeper implementation testing: Anytype’s long-horizon API stability and commercial implications of the Any Source Available License in a shipped Yar product; the practical maturity of AppFlowy as an embeddable/extensible substrate without forking; and the ergonomic cost of using SiYuan or Trilium for non-technical companion UX. None of those uncertainties changes the recommendation. They only reinforce it: **own the Yar runtime, treat shells as replaceable, and keep CAP at the center.**