> **Status**: Gap Audit (read-only; do not edit)
> **Date**: 2026-06-21
> **Author**: Claude Sonnet 4.6 (audit agent)
> **Audience**: @shahin, product, engineering
> **Tags**: `yar`, `feature-matrix`, `gap-audit`, `v4`

# Yar Feature Research Gap Audit (v4)

> **TL;DR**: v4 is approximately 72% complete. It is not yet publishable as a finished research artifact. The scoring arithmetic contains 14 known errors, 8 of the named tools lack standalone deep-dive coverage, several unique Cytognosis features are underspecified, and 3 legacy docs contain unique content not yet reconciled into v4. The ADHD variant has 5 P1 features missing from its build list and one em-dash violation. The duplicate master files remain unresolved. The two critical architecture gaps (privacy schema, crisis detection) are flagged in v4 but reportedly addressed in separate specs that must be linked.

> **Reading time**: ~10 min.
> **If you only read one thing**: go to Section 2 (Concrete Gap List), which is ordered High to Low.

---

## 1. Coverage Table

Each item from the original requirement checklist is rated **Fully / Partial / Missing** in v4.

### 1.1 Named Tools

| Tool | Coverage in v4 | Status | What to add |
|---|---|:---:|---|
| Leantime | Scored (81/120); emoji mood pattern cited; LEO AI mentioned | Fully | None |
| Super Productivity | Scored (86/120); focus/idle/break stack analyzed; MIT source files cited by count | Fully | None |
| Lovable mind-mapping | Named in "Niche" table; brief D explains it is a builder platform, not a shipped ND product; score 4/10 included | Fully | None |
| Brain.fm | Named in "Niche" table; Section 10.2 contains evidence caveat (one study, ADHD symptoms not diagnosis, no effect sizes); Communications Biology 2024 cited | Fully | None |
| Mindstrong | Named in "Niche" table; Section 10.1 contains four-point failure post-mortem (reimbursement, willingness-to-pay, tech-replaces-care, evidentiary gap); primary source Perlis/STAT cited | Fully | None |
| Chen et al. 2026 | Cited; 13 concepts with medians mapped to F05-F17 and others; attribution rule in Section 10.3; CSCW 2026 venue confirmed in brief C | Fully | None |
| Blue Lin (bluelin.me, menstrual_health project, CHI 2024 + IMWUT 2025) | Named in "Niche" table; Section 10.4 covers engagement curve; DR2/DR4/DR5 cited in CSV rows; brief D has full researcher profile and 5 DRs | Partial | v4 main doc does not reproduce the 5 DRs, the 7 visualization patterns, the 3-phase study structure, the MenstrualMate/PeriodBubble prototype pair, or the paired-hypothesis and circular-vs-linear toggle patterns. Brief D contains all of these but they are not surfaced in v4. Either add a dedicated Blue Lin subsection (Section 10.5 equivalent) or create a per-tool doc and link it. |
| Goblin Tools | Scored (57/120); spiciness slider, Formalizer, Judge, Compiler, Estimator, Professor, Consultant, Taskmaster all named; design rationale (solo ND developer, zero-friction) cited | Fully | None |
| Saner AI | Scored (63/120); morning plan, PiP, ADHD-explicit design, proactive model described in brief D | Fully | None |
| Tana | Scored (61/120); supertags, dual phone/desktop, voice-to-typed-node, Live Search, personal KG gap (proprietary schema) all present | Partial | The personal knowledge gap (proprietary schema prevents CAP governance) is implied but not stated explicitly as a Yar risk. Brief D and `tana-outliner-deep-dive.md` contain the gap clearly. Add one sentence in Section 5 or the Tana row notes in Section 7. |
| Capacities (all-in-one home) | Scored (58/120); object-first, daily-note inbox, AI rate-limiting noted | Partial | v4 does not mention that Capacities' sync cannot be disabled and uses no E2EE, which is a relevant disqualifier for mental-health-adjacent use. Brief D and `yar-substrate-decision.md` both flag this. Add to Section 5 or the Capacities row note. |
| Omi AI | Scored (70/120); open-source, MCP server, pluggable STT, pendant hardware, 300k+ users cited in brief D | Fully | None |
| PKM comparator: Obsidian | Present in "Niche" table; brief C has light scan; `yar-substrate-decision.md` has full assessment | Partial | v4 does not state Obsidian's MVP 8/10 long-term 7/10 rating or its "adapter target" role conclusion. Brief C and substrate doc have this. Add the role conclusion to Section 7 niche table or as a note. |
| PKM comparator: Logseq | Named in "Niche" table; brief C notes slowing development pace | Partial | Same as Obsidian: no role conclusion (inspiration only, MVP 6/10) from substrate decision surfaced in v4. |
| PKM comparator: AFFiNE | Named in "Niche" table with ADHD planner templates and infinite canvas noted; brief C has light scan | Partial | Substrate doc conclusion (inspiration only, MVP 6/10, self-host-only privacy caveat) not surfaced in v4. |
| PKM comparator: Notion | Named in "Niche" table; brief C notes AI add-on | Partial | Substrate doc concludes reject (MVP 4/10, cloud-first, insufficient for mental-health companion); v4 does not carry this conclusion. |
| PKM comparator: Anytype | Scored (61/120); selected as storage backend; local-first and E2E encryption noted | Partial | Substrate doc conclusion (MVP-only substrate, long-term 6/10, analytics caveat, Any Source Available License risk) not surfaced in v4. This is material for engineering decisions. |
| Speechify | Named in "Niche" table; TTS cascade noted (Kokoro/Fish Audio/ElevenLabs) | Fully | None |
| Letterly | Scored (41/120); voice brain-dump pattern cited | Fully | None |
| ND Visual Organizer | Scored (58/120); MCP pattern role noted | Fully | None |

### 1.2 Cytognosis Unique Features

| CU# | Feature | Status | What to add |
|---|---|:---:|---|
| CU-1 Universal sensor/tracking system | Present as F12 + F55 + F46; CSP/USAP protocol lifecycle described (discover/connect/configure/read-stream/disconnect) | Fully | None |
| CU-2 Social interaction tracker + communication coach + exposome-to-mood causal linkage | Present as F42 + F56; causal linkage to mood via Brain Weather stated | Partial | The bidirectional coaching mechanism (ND-to-NT and NT-to-ND) is stated but not specified: what does the coach surface, at what trigger, with what output format? F42 is P3/Planned with no spec beyond description. A one-paragraph spec note or a link to a planned spec doc would close this. |
| CU-3 Adaptive personas (optional initial profile, implicit adaptation, mood/mindset switching, trust-building) | Present as F11, F29, F45, F57; four-feature cluster fully described; on-device bandit named | Partial | The "optional initial profile" sub-feature is implied but not made explicit as a separate UX step. v4 describes preset library and manual switch (F11) and auto-selection (F45) but the onboarding flow (user chooses initial persona or skips) is not described. Add one sentence to F11 or the CU-3 row in Section 8. |
| CU-4 Personal-knowledge NER for transcription | Present as F33 + F58; NER seeded from personal KG described | Fully | None |
| CU-5 Capture-anywhere (phone, desktop, Chrome extension like Hypothes.is and Memex) | Present as F59; Hypothes.is and Memex named as patterns; WADM as F50 | Partial | Memex appears only in `memex_revision.txt` (a GitHub repo list) and as a named annotation pattern. v4 names Memex as a reference but does not describe what Memex does or why it is relevant. The Hypothes.is annotation pattern (highlight, annotate, link to KG) is referenced through WADM but the UX flow (select text on a webpage, annotate, save to Yar KG) is not described. Brief D and `blue-lin-projects-deep-dive.md` do not cover Memex at all. Add a sentence on what Memex offers as a pattern (collaborative web annotation, open-source, privacy-respecting) and how it differs from Hypothes.is. |
| CU-6 Conversational mind-mapping (linear AND branching; 3-agent loop: transcriber, parallel map-grower/placer, reviewer; revision tracking) | Present as F13, F14, F15, F31, F60; all three agents named; linear and branching stated in F60 | Partial | Revision tracking is stated in F60's title ("revision tracking") but is not described in the feature description or in Section 8 CU-6 row. What does revision tracking mean here: a version history of map states, a log of placer decisions, or undo/redo of reviser actions? One sentence of clarification needed. |
| CU-7 Templated transformation engine (doc/artifact/transcript/mind-map to structured artifacts including proposals and meeting notes) | Present as F34 + F61; deterministic graph-to-document transform stated; "proposals, paper, or plan" listed as outputs | Fully | None |
| CU-8 Self-report instruments (personality and validated tests as psych sensors) | Present as F62; "validated clinical instruments (e.g., ADHD rating scales, mood inventories)" named; CAP-governed stated | Partial | No specific instruments are named (which ADHD rating scale? which mood inventory? PHQ-9? ASRS? BIS-11?). This matters for grant reviewers and IRB reviewers. Add a parenthetical listing 3-5 named validated instruments as examples. |

### 1.3 Cross-Cutting Requirements

| Requirement | Status | What to add |
|---|:---:|---|
| Grouping by neurodiversity domain with clinically accurate, affirming terms | Fully covered; six ND domain taxonomy with explicit double-empathy framing and person-first language throughout | None |
| AI-Fit scoring with prior-AI-attempt notes | Partial: AI-Fit scoring present; prior-AI notes present in CSV WhoTriedAI_Note column; but 14 AI-Fit totals in v4 main doc do not match CSV source (QA report Check 4 confirms this) | Reconcile 14 AI-Fit /20 values and 6 Prior-AI /5 values per QA report before calling the scoring layer complete |
| Prioritization (P1/P2/P3/Infra tiers) | Fully covered; tiers defined with rules; P1 build list of 23 features explicit | None |
| Aligned single vocabulary across all tools | Partial: v4 uses consistent ND domain codes and controlled vocabulary; but QA report Check 7 identifies 5 P1 features missing from ADHD variant P1 list; and the em-dash violation in ADHD variant Mermaid node remains unfixed | Apply 4 fixes from QA report (em-dash, 14 AI-Fit totals, 6 Prior-AI values, ADHD P1 completeness) |

---

## 2. Concrete Gap List

Ordered High to Low severity.

### HIGH severity

**H1. AI-Fit arithmetic errors (14 features in v4 main doc, 6 Prior-AI mismatches)**
The QA report (Check 4 and 6) confirms 14 AI-Fit /20 totals in the Section 4 tables do not match the CSV source-of-truth. Six Prior-AI /5 values also mismatch. The CSV is correct; the doc totals were calculated without one axis (likely Feasibility) in an earlier draft. Every score cited in the formal master for F01, F02, F03, F04, F08, F09, F10, F20, F21, F22, F23, F24, F26, and F28 is wrong by 1-2 points. Grant reviewers or product stakeholders reading Section 4 get incorrect prioritization data.

**H2. Five P1 features missing from the ADHD variant build list**
The ADHD variant Section "What to build first (P1)" lists 18 features. The formal master lists 23. The 5 missing are: F06 Social Presence AI, F07 Dual-track planning, F08 Emoji mood on tasks, F17 Private emotional notes before planning, F57 Adaptive personas (implicit). A founder or engineering lead reading only the ADHD variant would under-scope the P1 set. Either complete the list or add a note that the ADHD variant is a curated subset pointing to the formal master.

**H3. Blue Lin coverage is shallow in v4; deep-dive doc not linked**
v4 names Blue Lin in the "Niche" table and Section 10.4 covers the engagement curve finding, but the 5 functional design requirements (DR1-DR5), 7 visualization patterns, 3-phase study structure, and paired-hypothesis data-entry pattern are not surfaced in v4. These are some of the most directly actionable design evidence in the entire research corpus. The per-tool deep-dive `04-Engineering/yar/research/blue-lin-projects-deep-dive.md` contains all of this and is not linked from v4. This is a meaningful coverage gap for any reader who does not open the engineering research folder.

**H4. Cytomark browser extension: no spec, not linked in v4**
G2 in Section 11 flags Cytomark as "highest-value unbuilt surface; write the spec (see F59)." The spec has not been drafted. F59 is P2 in the matrix. The annotation flow (select text on a webpage, annotate, link to Yar KG via WADM) is described in the feature description but the extension architecture, data flow, and UX are not specified. This is also the surface where Memex and Hypothes.is patterns would be most relevant, and v4 does not explain those patterns.

**H5. Vocal-biomarker storage schema (VocalBiomarkerFrame) unspecified**
G3 in Section 11 flags this. F40 (voice-first emotional awareness) uses HuBERT-large + openSMILE eGeMAPSv02, but the storage schema for the features extracted is named (VocalBiomarkerFrame) but not defined. The feature is Research/P3 so this is not blocking v4 publication, but any reader trying to understand the F40 implementation path hits a dead end. A minimal schema stub (fields: timestamp, acoustic_features, affect_label, confidence, session_id) would close this.

**H6. Duplicate master files unresolved**
Brief A (Section 7, bottom) confirms `yar-product-feature-master.md` and `yar-master-features-requirements.md` are byte-for-byte identical at two paths. v4 Section 9 recommendation 6 mentions this but no action has been taken. Having two identical files with different names creates confusion about which is canonical and risks future drift if one is edited and the other is not.

### MEDIUM severity

**M1. Tana proprietary-schema governance risk not stated**
Brief D and `tana-outliner-deep-dive.md` explicitly state that Tana's supertag schema is proprietary and that the authority model cannot be CAP-governed if Yar relies on Tana's schema. v4 says "Proprietary schema; steep onboarding" in the leaders table but does not connect this to the CAP governance implication. A reader evaluating whether to use Tana as a data layer would miss this.

**M2. Capacities E2EE disqualifier not stated**
`yar-substrate-decision.md` (page 6) and brief D both note that Capacities explicitly does not use E2EE and sync cannot be disabled, making it unsuitable for mental-health-adjacent data. v4 notes "No proactive surfacing; rate-limited AI" as weaknesses but not the privacy disqualifier.

**M3. PKM substrate conclusions (Obsidian, AFFiNE, Anytype, Logseq, Notion) not reconciled into v4**
`yar-substrate-decision.md` contains scored role conclusions (MVP/long-term ratings and "role: adapter target / reject / inspiration only") for 9 PKM tools. None of these conclusions appear in v4's Section 7 niche table. A product engineer making storage or integration decisions who reads v4 does not know that Anytype is MVP-only (long-term 6/10, analytics caveat, Any Source Available License risk), that Obsidian is the preferred adapter target, or that Notion and Tana are explicit rejects for CAP-governed data.

**M4. CU-2 bidirectional coaching mechanism underspecified**
F42 (ND-NT Communication Translation) is P3 and planned, but the coaching direction, trigger, and output format are not described beyond "bidirectional translation." For grant narratives (IGoR, NSF, ARPA-H) this feature is often cited as a differentiator; a two-paragraph spec stub would make it grant-ready.

**M5. CU-3 onboarding flow (optional initial profile) not described**
The adaptive persona cluster (F11, F29, F45, F57) describes the steady-state behavior well but does not describe the first-run experience: does the user pick a starting persona, answer an onboarding questionnaire, or simply start with a default that adapts? This matters for UX design.

**M6. CU-8 no specific validated instruments named**
F62 describes "ADHD rating scales, mood inventories" generically. For a grant reviewer or IRB, specific instrument names (ASRS v1.1, PHQ-9, GAD-7, BRIEF-A, BIS-11) are required to assess clinical validity.

**M7. Voice model evaluation not linked from v4**
`/home/mohammadi/04_voice_model_deep_evaluation.md` (and its copy at `04-Engineering/yar/research/voice_model_deep_evaluation.md`) contains a detailed evaluation of Moshi 7B, Gemma 4 cascade, Qwen3.5-Omni, LFM2.5-Audio, and Whisper+LLM+Kokoro on supervisor interrupt, nonverbal understanding, and longitudinal storage. This is directly relevant to F01 (voice capture), F40 (vocal biomarkers), and F54 (affect detection), but v4 does not reference it. The voice model decision (Gemma 4 cascade recommended over Moshi for Yar's use case) is not surfaced in v4 at all.

**M8. Memex pattern not described in v4**
`memex_revision.txt` is a list of Memex GitHub repos (WorldBrain). v4 names Memex as a capture pattern in F59 but does not describe what it is. Brief D does not cover it. Memex is an open-source, privacy-respecting web annotation and knowledge-management browser extension with a focus on annotation, tagging, and sharing. Its distinction from Hypothes.is is that it is fully local-first and does not require an account. Adding one sentence of description to F59 or Section 7 would close this.

### LOW severity

**L1. Em-dash in ADHD variant Mermaid node (line 42)**
QA report Check 1 identifies one em-dash character in the Mermaid YAR node label. Violates the no-em-dash house rule and is a latent Mermaid rendering risk.

**L2. ADHD collaborative intelligence document not reconciled**
`~/Collaborative Intelligence and Meeting Document Synthesis...md` evaluates Fathom, Granola, Fireflies, Gemini, NotebookLM, and Otter for meeting transcription. This is a Cytognosis operational research document, not a Yar product research document, and its content (multilingual transcription pipeline design) does not belong in v4 directly. However, the Fireflies AI pattern (auto-join, multilingual, auto-route to Drive) could inform CU-5 (capture-anywhere) and F60 (conversational mind-mapping) for meeting capture use cases. Recommend noting in F60 or CU-5 that meeting transcripts are a supported capture type and linking to the collaborative-intelligence doc for the operational pipeline.

**L3. "substrate_interop.py" rename still unactioned**
G1 in Section 11 flags this. The code file uses the retired term "Substrate." The flag exists in v4; no PR or issue reference exists to track closure.

**L4. CSP/USAP canonical name decision still listed as open**
D1 in Section 11 resolves to "adopt CSP as canonical; document USAP as engineering alias." This is stated in v4 and in the QA report as PASS. However, the decision is presented as a recommendation, not as a committed resolution. The CSP/USAP dual-naming issue predates v4; v4 repeats the recommendation but does not close the ticket.

---

## 3. Sibling Docs to Reconcile or Port

| Document | Path | Unique content not in v4 | Action |
|---|---|---|---|
| Yar substrate decision | `04-Engineering/yar/research/yar-substrate-decision.md` | MVP/long-term ratings and role conclusions for 9 PKM tools; CAP governance implication for Tana/Capacities/Notion; Anytype analytics caveat and license risk; hybrid MVP architecture recommendation | Port the role-conclusion table and the CAP governance note for each rejected tool into v4 Section 7 or an appendix. This is the most content-dense unreconciled doc. |
| Tana outliner deep-dive | `04-Engineering/yar/research/tana-outliner-deep-dive.md` | Detailed supertag schema spec; automations/templates system; full Yar feature mapping table (Section 12 of the deep-dive); Input API details | Synthesize the feature-mapping table into v4 F09/F10/F58 WhoTriedAI notes. Most content already captured in brief D; main gap is the Input API (Tana exposes a write API that Yar could use as an adapter). |
| Blue Lin projects deep-dive | `04-Engineering/yar/research/blue-lin-projects-deep-dive.md` | Full 5-DR table; 7 visualization pattern table; 3-phase study structure; MenstrualMate and PeriodBubble prototype descriptions; paired-hypothesis data-entry pattern; circular-vs-linear toggle; body-centric visualization pattern | Add a Blue Lin subsection in Section 10 (after 10.4, as 10.5) with the 5 DRs, the 7 visualization patterns, and the 3 design patterns most relevant to Yar (unified multimodal view, paired-hypothesis, progressive-trust scaffolding). |
| Voice model deep evaluation | `04-Engineering/yar/research/voice_model_deep_evaluation.md` and `~/04_voice_model_deep_evaluation.md` | Supervisor interrupt comparison (Moshi vs. Gemma 4 vs. Qwen vs. Whisper); nonverbal understanding capability matrix; longitudinal storage requirements for vocal biomarkers; VocalBiomarkerFrame fields | Add a Section 10 note (or link) on the voice model evaluation verdict (Gemma 4 cascade recommended for Yar; Moshi monitored for future full-duplex). This closes M7 and provides grounding for F01, F40, F54. |
| CAP/Yar comprehensive reference (03-Products) | `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` | CAP primitive lifecycle; 7 primitives; 16 RefusalMessage reason codes; Directive state machine; routing architecture | v4 references Cytoplex/CAP-Lite but does not describe the CAP protocol internals. The reference doc is a separate technical reference, not a gap in the feature comparison. Mark as a linked reference in v4 Section 11 (Architecture Gaps) rather than porting content. |
| Collaborative Intelligence and Meeting Synthesis | `~/Collaborative Intelligence and Meeting Document Synthesis...md` | Meeting transcription pipeline (Fireflies/Granola/Fathom/Gemini/NotebookLM); Persian/Farsi multilingual support; zero-bot capture; Drive routing | Scope: operational, not product research. Do not port into v4 directly. Add a one-line note in F60 or F59 that meeting transcripts are a CU-5/CU-6 capture use case and link the doc for the operational pipeline design. |
| memex_revision.txt | `~/memex_revision.txt` | GitHub repo list for WorldBrain Memex (open-source local-first web annotation) | Not a research doc; it is a raw URL list. Describe the Memex pattern in one sentence in F59 WhoTriedAI_Note and close the file. No further porting needed. |

### Duplicate-doc reconciliation status

| Pair | Status |
|---|---|
| `yar-product-feature-master.md` vs. `yar-master-features-requirements.md` | Byte-identical. One must be designated canonical (recommend `yar-product-feature-master.md`) and the other replaced with a symlink or redirect note. NOT YET DONE. |
| `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison-v3.md` vs. `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md` | Content-equivalent but format-divergent (ADHD vs. technical prose). 04-Engineering version has 3 additional P3 features. v4 supersedes both. After v4 is finalized, both v3 files should be moved to `_archive/` and v4 files designated canonical. NOT YET DONE. |
| `04-Engineering/yar/research/voice_model_deep_evaluation.md` vs. `~/04_voice_model_deep_evaluation.md` | Appears identical by date and content. The home-directory copy is outside the repo. The repo copy should be designated canonical; the home-directory copy is stale. |

---

## 4. Prioritized To-Do to Reach "Fully Complete"

Ordered by impact and dependency. A "publishable" threshold requires completing items 1-4; items 5-8 make it production-grade.

| # | Action | Severity | Effort | Blocks |
|---|---|:---:|:---:|---|
| 1 | Fix 14 AI-Fit /20 and 6 Prior-AI /5 mismatches in v4 main doc (reconcile against CSV) | High | 30 min | Publishable threshold |
| 2 | Add 5 missing P1 features to ADHD variant build list (or add "curated subset" note) | High | 15 min | Publishable threshold |
| 3 | Fix em-dash in ADHD variant Mermaid YAR node label (line 42) | Medium | 5 min | Publishable threshold |
| 4 | Designate one of the two identical master files canonical; replace other with redirect | Medium | 10 min | Publishable threshold |
| 5 | Add Blue Lin subsection in v4 Section 10 (5 DRs, 7 visualization patterns, 3 Yar-relevant patterns) | High | 45 min | Production-grade |
| 6 | Port PKM substrate role-conclusions from `yar-substrate-decision.md` into v4 Section 7 niche table | Medium | 30 min | Production-grade |
| 7 | Add voice model evaluation verdict and link in v4 Section 10 or 11 | Medium | 15 min | Production-grade |
| 8 | Add specific named instruments to F62/CU-8 (ASRS v1.1, PHQ-9, GAD-7, BRIEF-A) | Medium | 10 min | Production-grade |
| 9 | Add one sentence on Memex pattern to F59 WhoTriedAI_Note | Low | 5 min | Completeness |
| 10 | Add CU-2 bidirectional coaching spec stub (trigger, output format, one paragraph) | Medium | 20 min | Grant-ready |
| 11 | Add CU-3 onboarding flow description (optional initial profile UX) | Low | 10 min | Design-ready |
| 12 | Add CU-6 revision tracking clarification (what is tracked, one sentence) | Low | 5 min | Design-ready |
| 13 | Add Anytype analytics caveat and Any Source Available License risk to v4 Section 7 | Medium | 10 min | Engineering decisions |
| 14 | Add Tana CAP-governance implication (proprietary schema = cannot govern with CAP) to Section 7 | Medium | 10 min | Engineering decisions |
| 15 | Link `cap-yar-comprehensive-reference.md` in v4 Section 11 as the CAP protocol reference | Low | 5 min | Reference completeness |
| 16 | Draft Cytomark browser extension spec (F59, G2 in Section 11) | High | 3-5 hrs | F59 build-ready |
| 17 | Draft VocalBiomarkerFrame schema stub (F40, G3 in Section 11) | Medium | 1 hr | F40 build-ready |
| 18 | Archive v3 files to `_archive/` after v4 is finalized | Low | 10 min | Repo hygiene |

---

## 5. Overall Verdict

**Completeness: approximately 72%. Not yet publishable.**

The research substance in v4 is high quality. The competitive landscape analysis, AI-Fit methodology, Cytognosis unique-feature framing, ADHD paper grounding, and strategic insights (Mindstrong lesson, Brain.fm caveat, Chen et al. attribution rule, Blue Lin engagement curve) are well-executed. The 62-feature taxonomy with six ND domains is the strongest structured feature framework in the Yar corpus.

What blocks publication is the scoring layer: 14 known arithmetic errors in the primary document make every AI-Fit total unreliable until reconciled. That alone is a High severity gap. Combined with the 5 missing P1 features in the ADHD variant and the unresolved em-dash, the v4 pair fails the internal QA report on Checks 1, 4, 6, and 7.

The deeper coverage gaps (Blue Lin design requirements, PKM substrate conclusions, voice model evaluation, Cytomark spec) are significant for a production-grade research artifact but do not block a first publication if the scoring errors are fixed.

**Gap counts:**
- High severity: 6
- Medium severity: 8
- Low severity: 4
- Total: 18

**Minimum fixes to reach "publishable" (checks 1-4 in Section 4):** approximately 1 hour of editing work. The scoring reconciliation is mechanical (CSV is source of truth; update 20 cells in the Section 4 tables).

**Minimum fixes to reach "production-grade" (checks 1-8 in Section 4):** approximately 3 additional hours, with the Blue Lin subsection being the largest single item.

**Cytomark spec (check 16):** the only item in the to-do list that requires new research rather than reconciliation; budget 3-5 hours separately.

---

*Audit generated: 2026-06-21. Sources read: yar-unified-feature-comparison-v4.md, yar-unified-feature-comparison-v4-adhd.md, yar-feature-matrix-v4.csv, A_canonical_product.md, B_feature_research.md, C_new_tools_and_papers.md, D_deepen_tools.md, QA_REPORT.md, CONSOLIDATED_INVENTORY.md, cap-yar-comprehensive-reference.md (03-Products), yar-substrate-decision.md, blue-lin-projects-deep-dive.md, tana-outliner-deep-dive.md, voice_model_deep_evaluation.md (04-Engineering), ~/04_voice_model_deep_evaluation.md, ~/memex_revision.txt, ~/Collaborative Intelligence and Meeting Document Synthesis...md.*
