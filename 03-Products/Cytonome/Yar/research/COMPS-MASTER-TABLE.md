# Yar Comps Master Table and Feature-Coverage Map

> Every reference product used while researching Yar, gathered with full attributes and mapped to the universal feature hierarchy (`features.json` / `FEATURE-HIERARCHY.md`). Section 3 proves that every distinct capability seen across comps is either captured by a universal feature, a flagged gap, or a deliberate exclusion. Full narrative detail per comp: `01_comps-inventory.md`.

**Reading time:** about 10 minutes. **If you only read one thing:** Section 3, the capability coverage matrix, and its verdict.

## 1. How to read this

- **Score** is the 0-120 unified score from `yar-unified-feature-comparison-v4.md` where one exists; blank means it was not run through that pass.
- **Mapped features** are the universal feature IDs (F01-F62) whose scope covers that comp's capabilities. Cross-cutting foundations are tagged **[Voice]** (voice/AI pipeline), **[Store]** (local-first storage/sync), **[CAP]** (safety/consent); these foundations are realized through the enabling features listed.
- **Disposition:** `primary comp` (deep-dived anchor), `adopt pattern`, `substrate (MVP)`, `substrate (rejected)`, `adapter`, `inspiration`, `reference`, `cautionary`, `model (adopted/rejected)`.

## 2. Master comps table

### 2.1 Task / project management / ADHD-native

| # | Name | Category | What it is | License / Price | Platform | Local-first | Standout capabilities | Score | Mapped features | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Super Productivity** | Task/focus manager | Deep-work task manager for individuals | MIT; free | Electron, Capacitor, PWA, Docker | Yes (IndexedDB; opt sync) | Focus mode, Pomodoro, idle detection, break/tracking reminders, day planner, worklog, CalDAV, plugin API, op-log CRDT sync | 86 | F06, F20, F21, F22, F24, F26, F44, F16 [Store] | primary comp; adopt pattern |
| 2 | **Leantime** | Project management | PM "for non-project managers"; ADHD/dyslexia/autism framing | AGPLv3; free self-host | Docker web (PHP/MySQL) | No (server-first) | Kanban/gantt/table/calendar, sprints, milestones, Lean Canvas, retrospectives, idea boards, wiki, mood emoji, LEO AI | 81 | F02, F03, F08, F49; reframes → gap "personal compass" | primary comp; adopt (reframed) |
| 3 | **Goblin Tools** | ND micro-utilities | Magic ToDo, Formalizer, Judge, Estimator, Compiler | Free (license not stated) | Web | No (stateless) | Spiciness slider (granularity); Judge (tone/social check) | 57 | F04, F25, F56 | adopt pattern |
| 4 | **Saner AI** | ADHD AI assistant | Proactive unified capture+notes+tasks+calendar+chat | Not stated | Web/app | Cloud-first | Proactive, system-initiated check-ins; distributed nudges | 63 | F24, F01, F02, F39; lacks ERM/SMI (Yar moat) | reference (closest) |
| 5 | **ND Visual Organizer** | ND visual task tool | Board/visual ND organizer (not deep-dived) | Not stated | Not stated | Not stated | Visual/board organization (inferred) | 58 | F15 | reference |
| 6 | **Todoist / Things / Asana** | Mainstream task apps | Cited as negative comparison | Not stated | Multi | No | (Cited for the gap, not depth) | - | F53, F54 (negative ref) | reference |
| 7 | **Limitless** | AI meeting pendant | Wearable AI meeting/note assistant | Proprietary; $99 + $0-19/mo | Pendant + app | No (cloud) | Always-on capture, AI summaries | - | F01, F59 [Voice] | reference |
| 8 | **Plaud NotePin** | Recorder pendant | Hi-fi recorder/pendant | Proprietary; $169 + $0-7.99/mo | Pendant + app | No (cloud) | High transcription fidelity, mind-map summaries | - | F01 [Voice] | reference |
| 9 | **Otter.ai** | Meeting transcription | Voice-to-meeting-notes | Freemium | Not stated | No (cloud) | Action items + summary from meetings | - | F01, F02; gap: diarization | reference |

### 2.2 Voice / TTS / STT / underlying AI models

| # | Name | Category | What it is | License / Price | Platform | Local-first | Standout capabilities | Score | Mapped features | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | **ElevenLabs** | Voice AI platform | TTS/STT, voice cloning, Voice Design, agents | Proprietary; custom | Cloud + on-device (early) | Partial | On-device TTS, Voice Design, 70+ langs, HIPAA/SOC2 | - | F11 [Voice]; F19 (partial) | adopt (voice out) |
| 11 | **Kokoro (82M)** | On-device TTS | Small open TTS model | Apache 2.0; free | On-device (ONNX) | Yes | Multiple voices, 24kHz, ~20 langs, tiny footprint | - | F11 [Voice] | model (adopted, v1.0 TTS) |
| 12 | **Moshi (+MoshiRAG)** | Full-duplex speech | Native full-duplex model | CC-BY (research); free | Edge/research | Yes | Best supervisor-interrupt (no audible gap) | - | [Voice] → F06, F60, F11 | model (monitor; EN-only, license) |
| 13 | **Gemma 4 (E4B + 26B MoE)** | Speech understanding + reasoning | Google open-weight audio+reasoning | Apache 2.0; free | On-device + supervisor | Yes | 35+ langs, native function-calling supervisor | - | [Voice], [CAP] → F18, F19 | model (adopted, core) |
| 14 | **Qwen3.5-Omni** | Omni-modal model | Audio/text/image reasoning | Not stated | Not stated | Not stated | Best raw nonverbal cue reading | - | [Voice] → F40, F54 | model (rejected alt) |
| 15 | **LFM2.5-Audio** | Audio-native model | Liquid-style audio model | Not stated | Not stated | Not stated | Some interleaved overlap | - | [Voice] | model (rejected) |
| 16 | **Whisper** | Speech-to-text | Industry-standard ASR | MIT; free | On-device/cloud | Yes | Widely deployed; strips nonverbal | - | [Voice] → F01 | model (baseline, deprioritized) |
| 17 | **HuBERT + openSMILE** | Paralinguistic sensor | SSL speech rep + acoustic features | OSS (research) | On-device | Yes | Quantified pitch/jitter/shimmer/HNR/rate, valence-arousal-dominance; language-independent | - | F40, F54, F05 | adopted (non-negotiable) |
| 18 | **Deepgram / Speechmatics / Soniox** | Cloud STT | Multi-provider transcription | Proprietary; per-min | Cloud | No | Speed / multi-lang / low-latency streaming | - | [Voice] → F28 | reference (pluggable) |
| 19 | **Speechify** | TTS / reading | Read-aloud app | Proprietary; ~$139/yr | iOS offline, else cloud | Partial | Best read-aloud with highlight sync | 46 | F23 [Voice] | adopt pattern |
| 20 | **Letterly** | Voice-to-text content | Rambling speech → polished content | Proprietary; ~$9/mo | iOS/Android/mac/Win/Web | No (cloud) | Offline record, one-tap widget, filler removal, 25+ rewrite styles, 90+ langs | 41 | F01, F02, F03, F59; anti-patterns flagged | adopt pattern |

### 2.3 Notes / PKM / knowledge-graph

| # | Name | Category | What it is | License / Price | Platform | Local-first | Standout capabilities | Score | Mapped features | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| 21 | **Tana** | AI graph outliner | "Everything is a node," supertags | Proprietary; free/$10/$18 mo | Desktop/mobile/web | No | Supertags w/ inheritance, live searches as nodes, command nodes, botless transcription | 61 | F09, F10, F58, F13, F14, F15 | substrate (rejected); adopt pattern |
| 22 | **Capacities** | Object PKM | "Everything is a typed thing" | Proprietary, not E2EE; free/$10/$12 mo | Multi + web | No (sync forced) | Object Studio, two-way linking, composable views | 58 | F09, F14 [Store] | substrate (rejected) |
| 23 | **Anytype** | Local-first object PKM | Encrypted object system, P2P, MCP | Source-available; free tier | Desktop/mobile/web | Yes | 36 REST endpoints, MCP server, local encrypted store, type inheritance | 61 | F52, F09, F28 [Store] | substrate (MVP, not long-term) |
| 24 | **Obsidian** | Local markdown PKM | Markdown vault + plugins | Proprietary app, open data; free personal | Desktop/mobile | Yes | Official clipper, plugin API, Bases views, properties | - | F16, F52 [Store] | adapter (recommended shell) |
| 25 | **Logseq** | Block-graph outliner | Privacy-first outliner → SQLite DB mode | OSS; free | Desktop/mobile | Yes | Block-graph, Datalog queries, plugin API | - | F13, F09 | inspiration |
| 26 | **Notion** | Cloud workspace | Databases/pages + API | Proprietary; freemium | Multi + web | No | Excellent API, schema, integrations | - | F09, F16 | substrate (rejected) |
| 27 | **AppFlowy** | OSS Notion alt | Docs+DB, Flutter/Rust, local AI | AGPL; free self-host | Desktop/self-host | Partial | Local AI (Ollama) plugin, extensible data layer | - | F52, F19 [Store] | adapter target |
| 28 | **AFFiNE** | Canvas+docs workspace | Docs/whiteboard/DB blend | MIT; free self-host | Desktop/web/self-host | Yes (self-host) | Infinite canvas, ADHD planner templates | - | F13, F15 | inspiration |
| 29 | **SiYuan** | Self-hosted PKM | Block refs, SQL embeds, E2EE sync | OSS; free | Desktop/mobile/self-host | Yes | Block/query model, E2EE sync | - | F09, F52 | inspiration (security caveat) |
| 30 | **Trilium Notes** | Scriptable PKM | Notes/attributes/relations + ETAPI | OSS; free | Desktop | Yes (protected notes) | ETAPI, custom handlers, relation maps | - | F09, F51 | inspiration |
| 31 | **Joplin** | Privacy note app | Markdown, offline-first, E2EE | OSS; free | Desktop/mobile | Yes (E2EE) | Offline sync, APIs, clipper | - | F52, F59 | adapter target |
| 32 | **Athens / Roam** | Block-graph notes | Athens (dead OSS) / Roam (cloud) | Athens OSS dead; Roam paid | Web | Athens local-ish; Roam no | Block-reference model | - | F13 | reject |
| 33 | **Memex (WorldBrain)** | Web annotation | Local-first, account-free annotation | OSS; free | Browser ext | Yes | Local annotation, no central server | - | F50, F59 | adopt pattern (Cytomark) |
| 34 | **Hypothes.is** | Web annotation | Account-based annotation | Not stated | Browser/web | No | Annotation standard | - | F50 | reference (contrast) |
| 35 | **Lovable.dev** | AI app builder | Prompt-to-app generator | Not stated | Web | Not stated | Prompt-to-mind-map pattern | - | F13, F60 | reference (UX only) |

### 2.4 Local-first / storage / sync / protocol

| # | Name | Category | What it is | License / Price | Platform | Local-first | Standout capabilities | Mapped features | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| 36 | **Solid (Pods / W3C)** | Decentralized data protocol | Data decoupled from apps in user Pods | Open W3C; free | Any (server+SDKs) | Yes | LDP CRUD, WAC/ACP access control, Solid-OIDC+DPoP, Shape Trees; apps: HealthPod, VitalStats, Portable LibreChat | F52, F18, F16, F30 [Store][CAP] | phased target |
| 37 | **Replicache** | Local-first sync toolkit | Optimistic local mutators | Not stated | SDK | Yes | Offline optimistic mutation | F52 [Store] | building block |
| 38 | **ElectricSQL** | Local-first sync engine | Scoped Postgres→local via Shapes | OSS | SDK | Yes | Postgres-to-local scoped sync | F52 [Store] | building block |
| 39 | **RxDB** | Local-first DB | Offline-first JS DB w/ replication | Open-core | SDK (JS) | Yes | Offline-first replication | F52 [Store] | building block |
| 40 | **SurrealDB** | Multi-model DB | Document+relational+graph | Not stated | Embed/server | Yes (embed) | Graph RELATE, schemafull | F52, F13, F15 [Store] | benchmark (demoted) |
| 41 | **Automerge / Yjs** | CRDT libraries | Conflict-free replication primitives | OSS (MIT-family) | SDK | Yes | Concurrent conflict-free editing | F52 [Store] | building block |
| 42 | **FalkorDB** | Graph database | Server graph engine | Not stated | Server | - | Server-side graph projection | F52, F13, F15, F60 [Store] | adopted (server graph) |
| 43 | **LadybugDB (Kuzu fork)** | Embedded graph DB | On-device graph alt | Not stated | Embedded | Yes | On-device graph queries | F52 [Store] | candidate (blocked) |
| 44 | **Neo4j** | Graph database | Mature graph DB (Cytognosis cytomem, not Yar) | Dual license | Server | No | Mature graph ecosystem, GraphRAG | (out of scope for Yar) | reference |

### 2.5 AI assistants / wearables / functional audio / research

| # | Name | Category | What it is | License / Price | Platform | Local-first | Standout capabilities | Score | Mapped features | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| 45 | **OMI (Friend)** | OSS AI wearable | Always-on ambient pendant, "second brain" | MIT full stack; $89 + free/$19 | iOS/Android/mac/web | Partial | Full OSS stack, MCP server, 2000+ integrations, Silero VAD | 70 | F01, F59, F28, F12, F30 [Voice] | reference architecture |
| 46 | **Brain.fm** | Functional audio | Focus-engineered audio | Proprietary | App | Not stated | One peer-reviewed ADHD study | - | F23 (SPR) | reference (evidence-caveated) |
| 47 | **Mindstrong (defunct)** | Digital phenotyping | Failed passive-sensing mental-health co | Defunct | - | - | Cautionary: failed on economics/positioning, not science | - | [CAP], ERM → F18 | cautionary |
| R1 | **Chen, Meng & Nie (2026)** | Research (CSCW) | 42 ADHD adults; 13 AI design concepts | Paper (arXiv 2603.17258) | - | - | Empirical basis: body-doubling, mood-adaptive, dual-plan, social scaffolding | - | F06, F36, F53, F07 | research grounding |
| R2 | **Blue (Georgianna) Lin** | Research (HCI) | Menstrual-health data-sensemaking | Papers/dataset | - | - | Progressive disclosure, phase-coded viz, personal-baseline comparison | - | F43, F05, F55 | research grounding |

## 3. Capability coverage matrix (the verification)

Each distinct capability observed across all comps, mapped to the universal feature(s) that capture it. **Verdict** is `covered`, `gap` (recommend a new feature), or `excluded` (deliberately out of scope).

### Capture / tasks

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Voice brain-dump (one-tap, background, offline-sync) | F01, F59 | covered |
| Task CRUD w/ subtasks/dependencies | F02, F03, F04 | covered |
| Auto-tagging / AI classification | F03, F08 | covered |
| Task breakdown, adjustable granularity | F04 | covered |
| Tone / social calibration before send | F25 | covered |
| Kanban/gantt/table/calendar views | - | excluded (enterprise PM) |
| Sprint / milestone tracking | - | excluded (enterprise PM) |
| Account-free local web annotation/clipping | F50, F59 | covered |
| Multi-source capture unification | F59 | covered |
| Meeting transcription w/ speaker diarization | F01 (+diarization) | gap (diarization explicit) |
| Action-item / commitment extraction | F02, F03 | covered |
| Filler-word removal | F02 | covered |
| Home-screen widget / hotkey capture | F59, F26 | covered |

### Planning / time

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Pomodoro / focus-session timers | F20, F06 | covered |
| Idle / AFK detection | F21 | covered |
| Take-a-break reminders | F22 | covered |
| Full-screen single-task focus | F20 | covered |
| Day planner / AI daily plan | F24 | covered |
| Dual plan modes (ideal vs baseline) | F07 | covered |
| Worklog / time reports | F49, F05 (reframed) | covered (anti-surveillance reframe) |
| Calendar integration (CalDAV/iCal) | F28 | covered |
| Goal / OKR tracking as gentle "compass" | (F07/F24/F49 implied) | gap (explicit "personal compass") |

### Notes / knowledge management

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Typed objects / "everything is a thing" | F09 | covered |
| Two-way linked properties / backlinks | F09, F14 | covered |
| Schema inheritance (supertag-of-supertag) | F09, F51 | covered |
| Composable views (Board + Group By) | F10, F15 | covered |
| Live / saved queries as first-class objects | F10 | covered |
| Force-directed graph visualization | F15 | covered |
| Daily notes as temporal capture | F32, F53 | covered |
| Block/outliner nesting + transclusion | F09, F13 | covered |
| Command nodes / template bundles | F61 | covered |
| Media as first-class typed objects (OCR, audio analysis) | F09 (partial) | gap (rich media objects) |
| Export to Markdown/JSON/CSV | F16 | covered |

### Voice / AI

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| On-device TTS, multiple voices/speed | F11 [Voice] | covered |
| Voice Design persona from text | F11 | covered |
| Full-duplex supervisor-interrupt | F60, F11, F06 [Voice] | covered |
| Structured function-call supervisor | F18 [CAP] | covered |
| Quantified paralinguistic/emotion sensing | F40, F54, F05 | covered |
| Modular pluggable STT/LLM providers | F28, F19 | covered |
| Voice Activity Detection cost cut | F19 [Voice] | covered |
| Botless meeting transcription | F01 | covered |
| 25+ AI rewrite styles | F34, F61, F02 | covered |
| Multi-model AI provider selection | F28, F19 | covered |

### Sync / storage / local-first

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Local-only mode + optional P2P/server sync | F52 [Store] | covered |
| Op-log CRDT sync w/ vector clocks | F52 [Store] | covered |
| Encrypt-before-upload | F18, F52, F19 | covered |
| Granular, revocable per-agent access control | F18 [CAP] | covered |
| WebID/OIDC decentralized identity | F18, F52 | covered |
| Data-hierarchy / shape validation | F51 | covered |
| Real-time change notifications | F28 | covered |
| Self-hostable full stack | F52, F19 | covered |
| Localhost REST + MCP bridge | F28 | covered |
| Offline-first (local cache as source of truth) | F52, F19 | covered |

### ADHD / neurodivergent-support

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Non-shaming, non-streak progress framing | F38, F44, F27 | covered |
| Personal-baseline (not normative) comparison | F05, F43, F55 | covered |
| Body-doubling / simulated co-presence | F06 | covered |
| Proactive, system-initiated check-ins | F39, F53, F24 | covered |
| Mood-adaptive task load / morning check-in | F35, F53, F08 | covered |
| Burnout / pause-day detection | F27, F48 | covered |
| Non-judgmental abandonment recovery | F48, F38 | covered |
| Brain-weather metaphorical visualization | F05, F43 | covered |
| Progressive disclosure of multimodal data | F43 | covered |
| Shared co-planning with one trusted person | F36 | covered |
| Advocate for user during invisible-disability periods | (none) | gap (advocacy mode) |

### Collaboration (enterprise)

| Capability | Universal feature(s) | Verdict |
|---|---|---|
| Multi-user roles & permissions | - | excluded |
| Real-time co-editing | - | excluded |
| Comments / discussions on objects | - | excluded |
| Team dashboards / shared workspaces | - | excluded |
| Enterprise auth (LDAP/SSO/2FA) | - | excluded |

## 4. Coverage verdict

- **Captured:** 58 of the ~63 distinct capabilities map cleanly onto existing universal features. Yar's taxonomy absorbs the full competitive landscape's individual-user capability set.
- **Gaps (4), recommend adding:** (1) invisible-disability **advocacy mode** (SCI); (2) explicit **gentle goals / personal compass** (AEF or ERM); (3) **rich media as first-class objects** (CTO); (4) **meeting-mode diarization** (AEF/CTO, minor). These are the only comp capabilities not yet owned by a named feature.
- **Excluded (deliberate):** all enterprise/PM and multi-user collaboration capabilities, plus subscription gating. Document these as explicit non-goals so they are not mistaken for gaps.

**Conclusion:** with the 4 gap features added, the universal feature set fully captures every individual-user capability observed across all 47 comps. The gaps are additive, not structural; the 3-level hierarchy holds them without reorganization (advocacy → SCI/Communication coaching; personal compass → AEF/Day planning or ERM/Compassionate pacing; rich media → CTO/Notes; diarization → AEF/Capture).

## 5. Sources

Derived from `01_comps-inventory.md` (full per-comp detail and source paths) and `00_identity-and-feature-taxonomy.md`, which cite the underlying `docs/04-Engineering/yar/research/` EVAL files, `yar-unified-feature-comparison-v4.md`, `yar-substrate-decision.md`, `solid-pods-comprehensive.md`, and the vendored `third_party/` repos.
