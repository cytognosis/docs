> **Status**: Active
> **Date**: 2026-07-19
> **Author**: research agent (subagent, Cowork session)
> **Audience**: whoever sequences and staffs Wave 0
> **Tags**: `yar`, `effort-estimate`, `wave-0`, `planning`

# Yar Wave 0: Implementation Effort Estimates

**BLUF:** Wave 0's 12 components need an estimated **174 to 318 engineer-weeks** of net-new implementation (roughly 3.5 to 7 engineer-years at typical productive-week assumptions), on top of substantial, well-licensed open-source reuse. The three highest-effort components, **PeT knowledge graph** (35 to 65 weeks), **cross-node sync** (28 to 48 weeks), and **mind-mapping's structure-inference engine** (24 to 40 weeks), together account for roughly half the total. Two components (**F65 focus guardian**, **F69 diarization**) carry non-technical gates (privacy-boundary schema, counsel review) that can block shipping even after the engineering is done.

**Reading time:** about 14 minutes. **If you only read one thing:** Section 3 (Totals) for the number, and the risk-driver column for the three highest-effort rows in Section 2.

---

## 1. Methodology

**LOC-to-weeks assumption.** I use **350 effective net-new LOC per engineer-week** as the point estimate (range 300 to 500, per the task's own anchor), covering implementation, tests, and review, for typical integration and application code atop mature libraries. This sits at the higher, glue-code end of standard software-estimation heuristics (roughly 50 to 250 LOC/week for complex from-scratch work, higher for integration work), which fits Wave 0 since most components adopt a mature library rather than inventing an algorithm from zero.

For components where the underlying work is genuinely novel or experimental (new clustering algorithms, protocol design, retrieval-quality tuning, cross-platform native permission plumbing), raw LOC undercounts effort because time goes to research, evaluation harnesses, and tuning rather than net-new lines. I apply a **research/novelty multiplier of 1.1x to 1.8x** on top of the raw LOC/350 calculation for those rows, stated per row below. As a worked example: cross-node sync's 7,000 to 12,000 net-new LOC divided by 350 gives a raw 20 to 34 weeks; applying a 1.5x multiplier for protocol-design uncertainty yields the stated 28 to 48 weeks. The same logic applies silently to the other flagged rows.

**Adopt-vs-build philosophy.** For each component, I searched for the best-maintained, most permissively licensed existing implementation and estimated how much of the target capability it covers out of the box versus how much is genuinely new integration or algorithm work. "Build-vs-adopt split" is a rough percentage of the total capability, not of the LOC (a 70/30 split can still carry a large LOC count if the remaining 30 percent is a big surface).

**Confidence caveats.**
- These are **engineering-judgment, order-of-magnitude ranges** built from public repo signals (stars, forks, release cadence, license, last-release date) and the org's own existing gap analysis, not a bottom-up task breakdown against a written spec. Seven of Wave 0's ten spec areas are explicitly **missing** per `SPECS-INVENTORY.md`; expect these ranges to tighten once each spec lands, in the build order that document already sets.
- LOC figures count **Yar's own net-new glue and business logic only**, not the internals of adopted libraries (spaCy, whisper.cpp, Loro, and so on).
- Effort excludes spec-writing time (already tracked separately in `SPECS-INVENTORY.md`'s build list) and excludes DevOps/infra provisioning beyond what is folded into a component's own integration work.
- Confidence is **medium** for adopt-heavy components (proofreading, personas, Cactus routing) since license and maturity data are well established. Confidence is **low-to-medium** for research-heavy components (mind-mapping, PeT KG, sync, F65, F69) since they depend on decisions the org has not yet made (the open O-1 sync decision, the undefined term "PeT," legal clearance for F69); their ranges are deliberately wide.
- Two library-fact gaps are flagged explicitly in Section 2 rather than guessed at: Cactus's exact SPDX license identifier (a `LICENSE` file exists in its repo but its text was not independently confirmed in this pass) and "ReMem," which turned out to be a name shared by at least two unrelated research artifacts with no single confirmed, maintained, permissively licensed public repo.
- Not independently deep-researched in this pass (flagged, not fabricated): diarization-specific libraries such as pyannote.audio or WhisperX (not on the task's named list; needed for F69, called out as a fast-follow item), streaming/incremental clustering libraries for mind-mapping (also not named; candidates like online HDBSCAN exist but were not verified here), and Ollama/Dapr/NATS/OntoGPT, which the org's own docs already treat as decided or as an existing canonical pattern.

---

## 2. Per-Component Table

| Component / feature (+F-id) | Adoptable libraries (license, maturity) | Build-vs-adopt | Net-new LOC (low-high) | Effort (eng-weeks, low-high) | Risk | Main risk driver |
|---|---|---|---|---|---|---|
| **1. Transcriber agent** (real-time STT + dialogue, local/edge + cloud) | whisper.cpp (MIT; mature C/C++ on-device port); faster-whisper (MIT; CTranslate2, ~12.9x realtime); OpenAI Whisper (MIT; ~72k★, source of the weights); Gemma 4 (Apache-2.0 per Google's Apr 2026 release per secondary source, verify against `ai.google.dev/gemma/terms` directly before relying on it); Cactus (see row 8) for on-device routing and native STT; OMI/BasedHardware (MIT; full-stack open capture-to-action loop, already flagged in org docs as a P0 adoption target) | ~40% / 60% | 4,000-7,000 | 15-25 | Medium-High | Real-time on-device latency budget across low-end phones; the "Interviewer" conversational/mood-inference role does not exist in shipped code yet, only the "Transcriber" ASR role does |
| **2. Proofreading agent** (NER + personal-term mapping + structured output) | spaCy (MIT; used in 139k+ public repos, most mature tool here); sciSpacy (Apache-2.0, AllenAI); medSpacy (MIT); Instructor (MIT; ~11-12k★, 3M+ monthly downloads); DSPy (MIT; 36k★, 5.9M+ monthly downloads); OntoGPT (already an internal canonical pattern per org docs, not re-researched here) | ~70% / 30% | 2,000-4,000 | 6-12 | Low-Medium | "Maps to prior conversations" is blocked on F67 landing; medSpacy/DSPy evaluation for this specific domain has not been done yet |
| **3. Mind-mapping agent** (evolving heterogeneous graph, iterative) | No proven library for the core structure-inference step; existing shipped BM25 + hashing-embedder + RRF hybrid retrieval is already Yar code, not a new adopt; Tana is proprietary with no export API, so it is UX-pattern inspiration only, not adoptable code | ~25% / 75% | 6,000-10,000 | 24-40 | High | No adoptable library exists for structure-preserving incremental clustering that respects the user's existing spatial layout; the org's own docs call this "new research" |
| **4. Multi-platform app** (Tauri phone + desktop + web; browser extension later) | Tauri v2 (dual MIT/Apache-2.0; ~85k★, official iOS 13+/Android 7+ support); existing org-wide interface templates (Flutter phone, React 19 + Vite + Tailwind + shadcn web, MV3 extension) already locked at the org level; W3C WADM (free open standard); Memex/WorldBrain (MIT; ~4.5-4.7k★, actively developed since ~2015) | ~55% / 45% | 5,000-9,000 | 16-30 | Medium | Mobile app-store review, code signing, and native background-mic permission plumbing are process risks that engineering time alone cannot fully compress |
| **5. Cross-node sync** (F68) | Loro (MIT; 5.7k★, 130+ releases, latest Jun 2026) plus Iroh (dual MIT/Apache-2.0; 8.7k★, just reached v1.0 in May 2026, 563 dependents); OR any-sync server nodes (MIT; 1.6k★, 295 tags) - note Anytype's own client app is separately licensed ASAL-1.0 (source-available, non-commercial-leaning), which is irrelevant since Yar would reuse only the MIT server/protocol code, not that client; Automerge (MIT) as the org's documented fallback | ~35% / 65% | 7,000-12,000 | 28-48 | High | The org's own O-1 decision (any-sync vs. Loro+Iroh) is still open; whichever wins, distributed-systems correctness (conflict resolution, partial connectivity, key/identity management) is inherently hard to bound and this blocks everything downstream |
| **6. PeT knowledge graph + long-term memory** (F67) | HippoRAG 2 (MIT; 3.6k★, OSU NLP Group, NeurIPS'24 + ICML'25) needs real adaptation from its static-corpus design to Yar's incrementally-updated personal memory; "ReMem" is a name shared by at least two unrelated works (an OpenReview paper with no confirmed public repo, and a Dec-2025 DeepMind-associated Evo-Memory pattern with an unofficial-looking repo), treat as inspiration only, not a dependency; SurrealDB Spectron is an invite-only cloud preview, not adoptable today (SurrealDB core itself is BSL 1.1, converting to Apache 2.0 four years after each release); FalkorDB (SSPL v1, already decided server-side, ~4.7k★) | ~20% / 80% | 8,000-14,000 | 35-65 | High | "PeT" itself is undefined anywhere in the org's docs (zero grep hits); HippoRAG's design target (static document corpora, heavy server-side embedding models) differs meaningfully from Yar's continuously-updated, on-device-first personal memory; likely the single largest, riskiest Wave 0 component |
| **7. Personas** | Kokoro TTS (Apache-2.0; 82M params, already implemented); ElevenLabs (proprietary paid API, planned; a vendor-cost risk, not an LOC risk) | ~80% / 20% | 500-1,500 | 2-5 | Low | Scope creep if "does each worker agent need its own persona" becomes a design exploration rather than a config toggle |
| **8. Cactus model-routing** | Cactus (a `LICENSE` file exists in the repo but its exact terms were not independently confirmed in this pass, verify before adoption; ~5.3k★, 420 forks, v1.14 released Apr 2026, backed by a funded YC S25 startup); an internal `RoutingPolicy` sketch already exists in `cap-comprehensive.md` §5, must be reconciled with the already-decided Gemma-edge + Ollama-cloud split | ~50% / 50% | 2,000-4,000 | 7-13 | Medium | Cactus is a young (sub-2-year), VC-funded startup project; API-stability and long-term maintenance are vendor-continuity risks more than difficulty risks |
| **9. F65 focus/adherence guardian** | No direct library; needs OS-level monitoring/blocking APIs per platform (iOS Screen Time/Family Controls, Android Usage Stats/Accessibility Service, desktop window-focus APIs); existing shipped F06 and F39 provide a partial base to extend | ~15% / 85% | 5,000-9,000 | 18-34 | High | Gated behind the not-yet-built privacy-boundary schema **and** dependent on OS vendor entitlements (especially Apple's) that can be restricted or rejected at app-review time; a policy/platform-approval risk layered on top of the engineering risk |
| **10. F24 interactive daily-plan refinement** | Reuses F60's already-shipped conversational-iteration pattern plus Instructor/DSPy (already adopted in row 2) | ~50% / 50% | 1,500-3,000 | 4-8 | Low-Medium | Mostly a UX-tuning risk (how many refinement turns feel helpful versus annoying to an ADHD user), not a technical risk |
| **11. F66 ask & summarize** | Existing F52/F19/F10 building blocks plus the shipped BM25 + RRF hybrid retrieval stack (already Yar code); Instructor/DSPy for grounded-answer formatting; usable against F52 on day one, upgrades once F67 lands | ~45% / 55% | 3,000-5,500 | 9-18 | Medium | Grounding and hallucination-mitigation (answer only from the user's own notes) is a genuine trust-and-safety tuning problem, plus a two-phase dependency on F67 for full quality |
| **12. F69 meeting diarization** | whisper.cpp/faster-whisper (already adopted in row 1) plus a dedicated speaker-diarization library (for example pyannote.audio or WhisperX bundles; not on this task's named list, license and maturity not verified here, flagged as a fast-follow research item) | ~35% / 65% | 3,000-6,000 | 10-20 | High (legally gated) | Multi-party recording consent law varies by U.S. state; the org's own docs flag this as needing counsel review before formalizing, separate from the usual privacy/crisis gate. Engineering can finish and still be blocked from shipping pending legal clearance |

---

## 3. Totals and Two Paths

**Total net-new LOC:** approximately **47,000 to 85,000 lines** (Yar-specific glue and business logic only, excludes the internals of every adopted library).

**Total effort:** approximately **174 to 318 engineer-weeks**, roughly 3.5 to 7 engineer-years at typical productive-week assumptions (46 to 50 weeks/year after PTO and holidays). This is a headcount-agnostic total; converting it into a calendar timeline under specific team-size scenarios is the next task in the queue (#30), not this one.

**Three highest-effort components** (by the high end of each range):
1. **PeT knowledge graph + long-term memory** (F67): 35-65 eng-weeks
2. **Cross-node sync** (F68): 28-48 eng-weeks
3. **Mind-mapping agent**: 24-40 eng-weeks

Together these three account for roughly **87 to 153 of the 174 to 318 total**, close to half. All three share the same underlying reason: the org's own docs already flag them as genuinely new engineering ground, not library-integration work.

### Cheapest path (max reuse), approximately 174 eng-weeks

Take the low end of every row. This assumes: the more turnkey sync option is chosen (whichever of any-sync or Loro+Iroh needs less custom protocol work once prototyped) rather than building the most defensible option; HippoRAG is adopted with light adaptation rather than a deep re-architecture; Cactus and Kokoro are adopted as-is; and **F65 and F69 are deferred to a later wave**, since both are gated on non-engineering work (the privacy-boundary schema and counsel review, respectively) that this estimate cannot shorten with more engineers. Deferring those two alone removes 28 to 54 eng-weeks of gated, legally-encumbered work from the near-term critical path without losing any core Wave 0 functionality.

### Robust path (durable, fully hardened), approximately 318 eng-weeks

Take the high end of every row. This assumes: a fully custom wire protocol is built regardless of which sync library wins the O-1 decision; PeT KG gets a full re-architecture and a proper retrieval-quality eval harness rather than a light adaptation of HippoRAG; F65 gets full native permission integration across all three platforms; F69's diarization and consent-flow are built in parallel with legal review rather than waiting on it; and medSpacy/DSPy get full evaluation passes rather than shipping on defaults.

**Recommendation:** plan around the cheapest path for the Wave 0 commit, but budget the delta as a known follow-up, not a surprise. Defer F65 and F69 explicitly (both already carry an internal gate independent of this estimate); do not defer PeT KG or sync, since every other Wave 0 and Wave 1 component depends on them per the org's own build order in `SPECS-INVENTORY.md`.

---

## Notes on Specific Uncertainties

- **"PeT" is undefined.** Confirmed zero grep hits across the docs tree for the literal term, per `SPECS-INVENTORY.md`. This estimate treats it as "the long-term personal/temporal memory graph," matching the F67 description in `FEATURE-VERIFICATION.md`, but the term itself needs a definition before the spec is written.
- **Cactus's license was not fully confirmed.** Its GitHub repo shows a `LICENSE` file and a generic "License" link, but the specific terms were not independently readable in this pass. Verify the SPDX identifier directly before committing to it for a commercial product.
- **Gemma 4's Apache-2.0 licensing claim came from a secondary summary**, not a direct read of Google's own terms page. Verify against `https://ai.google.dev/gemma/terms` directly before relying on it for any compliance sign-off; earlier Gemma versions used a more restrictive custom usage license.
- **"ReMem" is not one thing.** At least two unrelated research artifacts share the name (an OpenReview paper on episodic memory, and a Google DeepMind-associated Evo-Memory/ReMem pattern from December 2025), and neither has a single confirmed, actively maintained, clearly licensed public repository. Treat "ReMem" as a research pattern to read, not a dependency to install.
- **SurrealDB Spectron is not adoptable today.** It is an invite-only, cloud-hosted preview product, which conflicts with Yar's device-first, privacy-first architecture. The org's own `SPEC-storage-engine.md` already reached this conclusion ("upside only, not MVP foundation"); this research confirms it independently.
- **FalkorDB and SurrealDB core are both source-available, not pure OSI open source** (SSPL v1 and BSL 1.1, respectively). Neither restriction blocks Yar from using them as embedded/internal infrastructure, but both are worth a compliance-check pass before any future Yar-as-a-hosted-service business model, since both licenses specifically target cloud-service resale.
- **F69 (diarization) carries a legal gate, not just a technical one.** Multi-party recording consent law varies by U.S. state, and the org's own `FEATURE-VERIFICATION.md` already recommends counsel review before formalizing this feature. This estimate treats that as unresolved; do not schedule F69's ship date assuming only engineering time.

---

## Sources

**Sync / CRDT:** [any-sync](https://github.com/anyproto/any-sync), [anytype-ts client](https://github.com/anyproto/anytype-ts), [ASAL license discussion](https://toscalix.com/2025/12/02/choosing-anytype-a-platform-for-scalable-secure-governance/), [Loro](https://github.com/loro-dev/loro), [Iroh](https://github.com/n0-computer/iroh), [Iroh 1.0 announcement](https://www.techtimes.com/articles/318490/20260616/peer-peer-library-iroh-10-ships-dial-devices-key-not-ip-address.htm), [Automerge](https://github.com/automerge/automerge)

**Memory / KG:** [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG), [HippoRAG paper](https://arxiv.org/abs/2405.14831), [HippoRAG 2 paper](https://arxiv.org/abs/2502.14802), [REMem (OpenReview)](https://openreview.net/forum?id=fugnQxbvMm), [DeepMind Evo-Memory/ReMem coverage](https://www.marktechpost.com/2025/12/02/google-deepmind-researchers-introduce-evo-memory-benchmark-and-remem-framework-for-experience-reuse-in-llm-agents/), [evo_mem repo](https://github.com/zhaosnw/evo_mem), [SurrealDB Spectron](https://surrealdb.com/platform/spectron), [SurrealDB license FAQ](https://surrealdb.com/license), [SurrealDB core license](https://github.com/surrealdb/surrealdb/blob/main/LICENSE), [FalkorDB](https://github.com/FalkorDB/FalkorDB)

**NLP / structured output:** [spaCy](https://github.com/explosion/spaCy), [sciSpacy](https://github.com/allenai/scispacy), [medSpacy](https://github.com/medspacy/medspacy), [Instructor](https://github.com/567-labs/instructor), [DSPy](https://github.com/stanfordnlp/dspy)

**Transcription / models:** [whisper.cpp](https://github.com/ggml-org/whisper.cpp), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [Gemma overview](https://ai.google.dev/gemma/docs/core), [Gemma terms](https://ai.google.dev/gemma/terms), [Gemma Wikipedia summary](https://en.wikipedia.org/wiki/Gemma_(language_model)), [OMI](https://github.com/BasedHardware/omi), [Kokoro TTS](https://github.com/hexgrad/kokoro)

**Platform / routing:** [Tauri v2](https://github.com/tauri-apps/tauri), [Cactus](https://github.com/cactus-compute/cactus), [Cactus on Y Combinator](https://www.ycombinator.com/companies/cactus), [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), [Memex](https://github.com/WorldBrain/Memex), [Tana Input API docs](https://tana.inc/docs/input-api), [Tana lock-in critique](https://www.dsebastien.net/the-reasons-ill-never-switch-from-obsidian-to-tana/)

**Internal sources cross-referenced:** `FEATURE-VERIFICATION.md`, `SPECS-INVENTORY.md`, `docs/03-Products/Cytonome/Yar/research/features.json`
