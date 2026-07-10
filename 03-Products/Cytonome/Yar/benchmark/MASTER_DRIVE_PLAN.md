# Yar Feature Consolidation — Master Drive Plan

**Owner:** Shahin Mohammadi · **Started:** 2026-06-21 · **Status:** ACTIVE
**Reading time:** ~4 min · **If you only read one thing:** the Phase Plan table and the Decisions Log.

---

## BLUF

This program finds, ingests, and harmonizes every prior Cytonome, Yar, and Cytoplex doc, deeply
researches each competitor tool, then produces **two master deliverables**: a formal Yar feature
master and an ADHD-friendly companion. Features are aligned to one vocabulary, grouped by
neurodiversity domain using clinically accurate language, scored for AI fit and prior-AI maturity,
and prioritized. Cytognosis's own unique features are folded into the same matrix.

---

## Done-list (progress you can see)

- [x] Recon: mapped all Yar/Cytoplex/Cytonome docs across repos, vault, home dir, and projects
- [x] Confirmed write access to canonical docs repo
- [x] Read orchestration framework (`task-orchestrator`)
- [x] Created this Master Drive Plan
- [x] Phase 2: ingested existing docs (digests in `_ingestion/`)
- [x] Phase 3: researched competitors + papers (briefs in `_research/`)
- [x] Phase 4: synthesized unified scored matrix (`_synthesis/yar-feature-matrix-v4.csv`)
- [x] Phase 5: produced formal master + ADHD master (in `research/`)
- [x] QA pass: fixed AI-Fit arithmetic, prior-AI, em dash, ADHD P1 list (`_synthesis/QA_REPORT.md`)

**PROGRAM COMPLETE 2026-06-21.** Deliverables: `research/yar-unified-feature-comparison-v4.md`, `research/yar-unified-feature-comparison-v4-adhd.md`, `consolidation_2026-06-21/_synthesis/yar-feature-matrix-v4.csv`.

---

## Phase Plan

| Phase | Goal | Engine | Output |
|---|---|---|---|
| 1. Recon | Map all source docs + tools | main | this plan |
| 2. Ingest | Extract every prior feature, score scheme, naming, gaps | Sonnet subagents (2 at a time) | `_ingestion/*.md` structured digests |
| 3. Research | Deep-dive each competitor tool + key papers | Sonnet subagents (2 at a time) | `_research/*.md` per-tool briefs |
| 4. Synthesize | One aligned, grouped, scored, prioritized matrix | Opus (main) | `yar-feature-matrix-v4.csv` + narrative |
| 5. Produce | Formal master + ADHD-friendly master | Opus (main) | `yar-unified-feature-comparison-v4.md` + `...-v4-adhd.md` |

**Model routing:** Sonnet for all reading, search, and extraction; Opus for synthesis and final writing.
**Parallelism cap:** 2 subagents per batch. **Checkpoint:** every 10-15 tool exchanges; recommend a
fresh session if context degrades.

---

## Source Inventory (Phase 2 ingestion targets)

### A. Canonical product docs — `repos/cytognosis/docs/03-Products/Cytonome/`
- `cytonome-track.md`, `cytonome-track-simplified.md`
- `Cytoplex/cytoplex-readme.md`, `Cytoplex/steering/{cytoplex-tech,cytoplex-product,cytoplex-structure}.md`
- `Yar/yar-product-feature-master.md` (CANONICAL), `Yar/yar-master-features-requirements.md` (CANONICAL)
- `Yar/yar-product-implementation.md`, `Yar/cytonome-master-reference.md`, `Yar/yar-feature-prioritization.csv`
- `Yar/steering/{yar-tech,yar-structure,yar-product}.md`

### B. Feature research (reconcile duplicates) — `.../Yar/research/` + `04-Engineering/yar/research/`
- `yar-unified-feature-comparison-v3.md` (BACKBONE — current scoring scheme lives here)
- `yar-unified-feature-comparison.md` (older), `yar-unified-feature-comparison-adhd.md` (existing ADHD version)
- `cap-yar-comprehensive-reference.md` / `cap_yar_comprehensive_reference.md`
- `yar-substrate-decision.md` (NAMING: reword "Substrate" to layer/foundation)
- `04-Engineering/yar/yar-system-doc.md`

### C. Site + funding + architecture
- `docs/site_docs/explanation/{cytoplex-overview,cytoplex-foundations,cytoplex-core-model}.md`
- `docs/02-Funding/foresight/foresight-cytonome-2026-submit.md`
- `org/plans/phase3b-cytonome-yar-architecture.md`, `docs/00-Inbox/yar_revision_plan.md`

### D. Code repo — `repos/cytognosis/Yar/`
- `docs/architecture/*`, `docs/research/*`, `docs/planning/*`, `src/yar/` schema, `apps/mobile/` (Flutter)

### E. Un-ported / loose — `/home/mohammadi/`
- `02_cap_comprehensive.md`, `03_yar_product_and_implementation.md`, `04_voice_model_deep_evaluation.md`
- `Collaborative Intelligence and Meeting Document Synthesis...md` (transcription + synthesis eval)
- `memex_revision.txt`
- Other Claude Projects to scan: `Cytognosis`, `Science and Platform`, `Strategic Planning`

### F. Cloned reference tools — `repos/cytognosis/infrastructure/third_party/`
- `hypothesis-extension`, `memex`, `affine` (ground truth for annotation + PKM features)

---

## Research Targets (Phase 3)

| # | Tool | URL | ND angle to extract |
|---|---|---|---|
| 1 | Leantime | leantime.io | ADHD-friendly project management |
| 2 | Super Productivity | super-productivity.com | OSS time-tracking + task focus |
| 3 | Lovable mind-mapping | lovable.dev/solutions/use-case/mind-mapping-tools | AI mind-map generation patterns |
| 4 | Brain.fm | brain.fm | functional music for attention; cite their studies |
| 5 | Mindstrong (defunct) | statnews.com/2023/02/06/mindstrong-demise... | failure lessons (digital phenotyping) |
| 6 | ADHD task-mgmt paper | arxiv.org/pdf/2603.17258 | AI-augmented social scaffolds; find our prior summary |
| 7 | Blue Lin designs | bluelin.me + /projects/menstrual_health | tracking UX, self-report design, her papers |
| 8 | Goblin Tools | goblin.tools | task breakdown, tone, formalizer (ND-native) |
| 9 | Saner AI | saner.ai | ADHD AI assistant patterns |
| 10 | Tana | outliner.tana.inc | supertags, dual phone/desktop, personal knowledge graph |
| 11 | Capacities | capacities.io | object-based all-in-one PKM home |
| 12 | Omi AI | omi.me/pages/product | OSS AI note-taker, summaries, auto-tasks, memories, standards |

---

## Cytognosis Unique Features to fold into the matrix

1. **Universal sensor/tracking system** — user-extensible health and mental-health axes.
2. **Social interaction tracker** — communication coach for neurodivergent-to-neurotypical exchange,
   plus causal linkage of exposome (social interactions) to mental-health shifts.
3. **Adaptive personas** — optional initial profile, implicit adaptation to build trust, persona
   switching matched to the user's current mood and mindset.
4. **Personal knowledge + NER** — understands the user's domains (code, papers, models, fashion,
   shopping) for accurate transcription without manual correction.
5. **Capture anywhere** — phone, desktop, and a Chrome extension for on-page annotation and comments
   (Hypothes.is plus Memex patterns).
6. **Conversational mind-mapping** — supports linear and branching cognition; a 3-agent loop: main
   transcriber, parallel mind-map grower, and a reviewer that rescans for terminology and NER
   correction and auto-reorganizes the map, with full revision tracking.
7. **Templated transformation engine** — turns any doc, artifact, transcript, or mind-map into
   structured artifacts (proposals, meeting notes, and similar).
8. **Self-report instruments** — personality and validated common tests as opt-in psych "sensors."

---

## Neurodiversity Grouping (clinically accurate, affirming language)

Group features by functional domain, not by diagnosis label:

- **Attention regulation and executive function** (relevant to ADHD): task initiation, working memory,
  time perception, task switching, prospective memory, planning and sequencing.
- **Emotional regulation and mood** (relevant to depression, anxiety, bipolar): mood tracking,
  rumination, motivation and anhedonia, distress tolerance.
- **Social communication and interaction** (relevant to autism): social reciprocity, perspective
  exchange, communication-style mismatch (frame via the double-empathy problem, not deficit-only).
- **Sensory processing and regulation**: sensory load, overstimulation, environment and sound.
- **Cognitive style and thought organization**: nonlinear and associative ideation.
- **Self-monitoring and interoception**: symptom tracking and self-report instruments.

---

## Scoring Rubric (reconcile with v3 after ingestion)

Each feature scored 1-5 on: **AI leverage**, **prior-AI maturity** (has anyone shipped AI here),
**Cytognosis differentiation**, **ND impact**, **build feasibility**. Priority is a weighted blend,
favoring high AI leverage + high ND impact + high differentiation. Final scheme locks after Phase 2
confirms the existing v3 rubric, so we extend rather than replace it.

---

## Output Spec

- **Location:** `docs/03-Products/Cytonome/Yar/research/` (canonical), built here first.
- **Formal master:** `yar-unified-feature-comparison-v4.md` (supersedes v3; archive v3).
- **ADHD-friendly master:** `yar-unified-feature-comparison-v4-adhd.md`.
- **Data:** `yar-feature-matrix-v4.csv` (the scored, grouped, prioritized matrix).
- Read `cytognosis-doc` skill before drafting finals (research templates + ADHD guidelines).

---

## Decisions Log

- 2026-06-21: Build in canonical docs repo (Git-tracked), present copies to user via Cowork.
- 2026-06-21: Extend the existing v3 comparison into v4; do not start from scratch.
- 2026-06-21: Reword retired "Substrate" term to layer/foundation in all carried-forward content.
- 2026-06-21: Group by functional ND domain, not diagnosis; affirming + clinically precise terms.

## Open Flags (acting unless told otherwise)

- Reconciling duplicate v3 copies into one source of truth under `research/`.
- Treating home-dir loose files as possibly-newer un-ported content; subagent C checks for unique ideas.

## Checkpoint / Handoff

CHECKPOINT (2026-06-21, post-recon): Goal = two consolidated Yar masters. Done = recon, plan.
Next = dispatch Phase 2 ingestion subagents (A: canonical product; B: feature research + ADHD format).
Active constraints = Sonnet for research, Opus for synthesis, 2 subagents/batch, no em dashes,
affirming clinical language, no "Substrate".
