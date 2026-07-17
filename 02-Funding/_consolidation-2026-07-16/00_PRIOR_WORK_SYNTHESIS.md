# Prior Work Synthesis: Grants, Applications, Funding Standardization

**Built from:** 7 prior Cowork session transcripts on "consolidation" (2026-07-01 through 2026-07-16).
**Scope:** only content relevant to grants, applications, funder research, and standardization. Read-only; no changes made.
**Reading time:** about 8 minutes.

**If you only read one thing:** a real, working reusable-grant-template system exists (slots + funder configs + funder profiles) and is promoted into the docs repo at `02-Funding/reusable-blocks/slot-library/`. But the Grants project's own `README.md` is stale (dated 2026-06-12, pre-migration) and its `00-CONSOLIDATION/` tracking folder is gone from the working tree. Also: this program has a documented history of "claimed done but wasn't" (Antigravity restructures that silently dropped tracking folders and an application-templates merge that stalled once before it finally landed). Treat every "done" claim below as needing one live verification pass, not as ground truth.

---

## Sessions read

| # | Session ID | Title | Coverage | Grants relevance |
|---|---|---|---|---|
| 1 | `local_16ec7f6d-0e3a-4867-bf6f-5174bcb1a5e5` | Finalize the Consolidation Efforts | Full (470 lines; session still "running") | Low direct content; mostly mission-control tooling (AgentsRoom/OpenHands/Vibe Kanban) then a deep Yar pivot. Grants appears only as a priority-queue entry |
| 2 | `local_2aa3c74c-b219-4b37-9294-ae2df8add7b1` | Funding & Grants consolidation | Full | **Highest.** This is the actual per-project consolidation agent run for the Grants project |
| 3 | `local_3a22463d-903e-4ae6-8352-a8a3cb411e90` | Consolidation priorities and planning | Full (796 lines, read in 3 passes) | High. Funding tracker, UK/EU eligibility, a **16-block Heilmeier proposal library**, and the CEO-contract detour |
| 4 | `local_04160028-7532-4a52-8305-3fa3a33fdad6` | Cytognosis consolidation continuation | Full (single large capture; likely missing its true opening turns, which were cut by the transcript-length cap) | **Highest.** Contains the slot-library discovery/standardization and the full Grants-to-docs-repo migration |
| 5 | `local_72fe6fd8-aa72-409e-a711-c000229c65a6` | Claude projects consolidation | Full | **Highest.** This is where the whole control-tower (blueprint, registry, master plan) was built, and where the `application_templates` archive was discovered and routed to Grants |
| 6 | `local_debe1db8-04d3-4f21-8f97-1077d26c277d` | Consolidation updates | Full (via saved file; likely captures from its true start) | Medium. Org-wide dedup/promotion into docs repo (Grants promotion numbers), git-identity cleanup, mostly infra not grants-specific |
| 7 | `local_7b5bddeb-480f-4979-a3ce-3e4c7f50d684` | Consolidation Phase II | Full | Low-medium. Corrects stale wave-status claims; Zotero/Monday key setup; confirms Grants-adjacent facts but no new standardization content |

**None were empty or rate-limited.** No retry needed. Two caveats: session 1 is still marked "running" elsewhere, so newer turns may exist beyond what I captured; sessions 4 and 6 were recovered from size-overflow dumps and may not include their very earliest turns (the visible content starts mid-narrative in both cases).

---

## 1. Standardization work that already exists

- **The slot-library grant-template system** (the core artifact). Structure, per agent reports:
  - `slots/` — 27 reusable content blocks: universal **U01-U22** + org-specific **A01-A05**.
  - `funders/` — 10 YAML funder configs: `arpah`, `astera`, `brains`, `doe_genesis`, `foresight`, `google_impact`, `heilmeier`, `nih_r01`, `nsf_tech_labs`, `yc_nonprofit`.
  - `research/profiles/` — funder profiles, one per opportunity (ARPA-H, ARIA, Astera, Anthropic, RWJF, etc.), each with YAML frontmatter. Count **grew from 40 to 71** as later merges folded in more funders (session `local_72fe6fd8` found 40 in the original archive; session `local_04160028` standardized 71).
  - `proposals/` — assembled proposals (e.g., `astera_2026`).
  - A `README.md` inside slot-library is the **system of record**.
  - **Location:** docs repo, `02-Funding/reusable-blocks/slot-library/` (per `local_04160028`, `local_3a22463d`).
  - **State:** Canonical. 157 of 159 funding docs got standard headers (the other 2 have headers sitting below long YAML frontmatter, not truly missing) — session `local_04160028`.
  - **Origin:** discovered as an 88-file archive at `~/Documents/_archive/unsorted/application_templates` (universal template, 27 slots, 10 funder configs, 40 profiles, raw ARPA-H/DoE/NSF ISOs, a live Astera draft), flagged by you as unique and "stored nowhere else," and routed to Funding & Grants as the top integration priority — session `local_72fe6fd8`.
  - A `heilmeier.yaml` funder config exists inside this system, so Heilmeier-style structuring is present per-funder, but I found **no explicit doc mapping PsychIGoR Solution Summary sections to Heilmeier questions** in these 7 sessions (see Section 4).

- **A second, separate Heilmeier artifact: 16 Heilmeier-keyed proposal blocks.** Session `local_3a22463d` (2026-07-06) built this via a subagent: *"Continuing the Cowork-doable lanes, now building the reusable Heilmeier proposal-block library (P4/L5)... P4 reusable-block library is built, 16 Heilmeier-keyed blocks ready to drop into any proposal."* Sources cited: "Projects-resident sources (biotypes, transdiagnostic, gaps, team bios)." The same session explicitly notes *"the external slot library folds in host-side"* — meaning the plan was to eventually merge this with the slot-library above. **I found no confirmation in later sessions that this merge happened.** Exact file location was not stated in the transcript (likely under a `00-CONSOLIDATION/` folder, dated 2026-07-06). **Flag: possible unreconciled duplicate reusable-block system; locate and check whether it was folded into the slot-library or still sits separately.**

- **cytognosis-doc skill v5.6.0**: two templates added, `literature-synthesis-template.md` and `funding-opportunity-profile-template.md`, at `~/repos/cytognosis/cytoskills/skills/cytognosis/cytognosis-doc/references/`. Bidirectional twin-linking required between variants (sessions `local_04160028`, `local_debe1db8`).

- **Three-variant doc pattern**: every substantive doc gets `<topic>.technical.md` / `<topic>.readable.md` (mirrored to Obsidian) / `<topic>.agent.md`. Applied to the grant-alignment map (session `local_2aa3c74c`).

- **Gap confirmed, not just assumed:** none of these 7 sessions mention a PsychIGoR Solution Summary-to-Heilmeier-question crosswalk or an ISO-mapping punch list. Per your own memory index, that content exists in a `proposal_craft_2026-06-23/` body of work, dated before this consolidation program and never mentioned as touched by it. Check that folder's current location directly.

## 2. "Values inference per funder" work

- The **71 funder profiles** (`02-Funding/reusable-blocks/slot-library/research/profiles/`) are the closest match: one structured file per funder/opportunity, used (presumably) to decide which slots to pull when assembling a proposal for that funder.
- **`funder_crosswalk_matrix`** and **`funder_metadata`** sit as siblings to slot-library at `02-Funding/reusable-blocks/` (session `local_3a22463d`'s per-area inventory table). These are the closest thing to a formal cross-funder comparison, but I did not read their actual contents or columns, only agent-report descriptions of their existence.
- **No session describes a distinct "values inference method"** (an algorithm, prompt, or rubric that reads a funder's public materials and outputs inferred values/focus areas). If one exists, it is embedded inside the profile-authoring process itself, not a separate documented artifact. Verify by opening a profile file directly rather than trusting this transcript-level description.

## 3. Reusable proposal-building system

- Confirmed real and built: **universal slots** (funder-agnostic content, U01-U22) are separated from **funder-specific configs** (which slots to use, how to tailor them) and from **assembled proposals** (the final funder-facing document). This is a genuine reusable-vs-application-specific split, matching the goal.
- **Cytos tie-in, confirmed concretely:** `cytos funding parse --criticmarkup` is a real CLI command in the Cytos platform tooling repo (found alongside `cytos scholarly parse-papers` during a tooling-discovery pass, session `local_72fe6fd8`). This is the one direct link between "Cytos" and the grants/funding system: Cytos ships a command specifically for parsing funding documents with CriticMarkup annotations.
- **No session ties the slot-library to the earlier personal-app/Yar feature set** (e.g., Yar's persona slots, feature slots, or its "universal sensor" protocol). If a unified "slot" concept across Yar and Grants is wanted, that unification has not happened and would be new work, not a documented decision.

## 4. Section proportions/sizes (PsychIGoR Solution Summary page-budget)

- **Not found in any of the 7 sessions.** These sessions are entirely about file and folder consolidation, not proposal content, section budgets, or page limits.
- Per your memory index (outside these sessions), this work exists separately: `proposal_craft_2026-06-23/` (Heilmeier-to-healthcare guide, ARPA-H SS architecture/page-budget at 5.0pp, IGoR SS assessment/ISO-mapping punch list), dated **before** this July consolidation program started.
- **Action:** locate `proposal_craft_2026-06-23/` directly (it may have been promoted into docs `02-Funding`, archived, or left in a project folder) since none of these 7 sessions confirm what happened to it during the migration.

## 5. Per-application consolidation decisions

| Application | Status per these sessions | Doc location | Notes |
|---|---|---|---|
| **Astera Residency (Round 2)** | Denied (per your memory, not these sessions) | Versions v1-v19 collapsed into one canonical file + 19 dated git commits, at docs `02-Funding/submissions/` (exact leaf path not stated). Source copies confirmed on disk at `Grants/_archive/versions-collapsed-2026-07-10/Astera_Round2_Response/` | Version-as-git-history proven here first (session `local_04160028`) |
| **Google Impact / AI for Science** | Not stated in these sessions | Versions v2-v4 collapsed into one file + 3 commits, same docs pattern. Source at `Grants/_archive/versions-collapsed-2026-07-10/Google_Impact_Revised/` (confirmed on disk) | Second proof case for version-as-git |
| **Coefficient Giving** | **Rejected** | Marked in the P4 funding tracker | Session `local_3a22463d` |
| **Biswas Fast Grants** | **Rejected** | Marked in the same P4 tracker | Contradicts your memory's earlier framing of Biswas as "top pre-Oct-1 cash"; confirm which is current |
| **IGoR / ARPA-H** | Highest-value workstream | Canonical set assigned to `02-submissions/Grants/ARPA-H/IGoR/_consolidation_2026-06-19/` | Per your memory (not these sessions), a later Jun 21-24 cycle moved primary editing to Google Docs directly, with a **standing rule (2026-06-22)**: you hand-edit those docs now; agents must not push or edit them programmatically unless asked. None of these 7 sessions override that; carry it forward |
| **YC (nonprofit-era draft)** | Explicitly parked | Old draft at [Google Doc](https://docs.google.com/document/d/1XSazXPaI68hA5yPEfm96ELpVKr9Kolm7BQeCiLdTTCg/edit) | Decision: do not redraft until all Yar work is fully revised (session `local_3a22463d`). Deadline Jul 27. 7 YC-related files also sit under `02-Funding/*` |
| **ARPA-H ISO 1-2 pagers** (Coppersmith + Smoller) + **Convergent Research 1-pager** | In progress as of session `local_16ec7f6d` ("Now, highest priority, nothing blocking") | Filed under Grants | Not confirmed finished in any session read |
| **ARPA-H REST** | New opportunity surfaced | — | Due Aug 12 (session `local_3a22463d`) |
| **NSF X-Labs / Psychoscope** | Live | — | Phase 0 Topic 2 due Jul 13; dual-citizenship question added to the Duane meeting agenda |
| **GCP Research Credits** | Drafting | — | Cytognosis qualifies as Nonprofit Research Institution; needs a 250-word proposal, pricing estimate, and your billing-account ID (session `local_16ec7f6d`) |

## 6. Target folder taxonomy, naming, and archive rules

**Confirmed live on disk (checked directly, 2026-07-16):** the Grants project folder is now almost entirely `_archive/`, plus `README.md`, `CLAUDE.md`, and `_context/` (two live shortcuts only: `02-Funding -> docs/02-Funding`, `01-Strategy -> docs/01-Strategy`; no shortcut to `05-Research`).

- **`<funder>/<program>/` nesting confirmed** directly from the (stale but structurally accurate) local `README.md`: `02-submissions/Grants/ARPA-H/IGoR/INDEX.md`, with `Applications/` (credits, accelerators) kept separate from `Grants/` (large agency grants).
- **INDEX.md convention:** every area gets one, meant to pass a "5/10/15 test" (a fresh agent understands, locates, and starts work within 5, 10, 15 minutes).
- **Archive rule, confirmed on disk:** additive-only, archive-over-delete, dated subfolders, forward pointers. Live examples: `_archive/versions-collapsed-2026-07-10/`, `_archive/from-infrastructure-20260709-225245/`, `_archive/from-strategic-planning-20260709-225245/`, `_archive/grants-manifests-20260709-225245/`, `_archive/03-personal-leftover-20260709-224324/`.
- **"Version-as-git" rule:** multiple dated draft copies of the *same* submission collapse into one canonical file with sequential dated git commits replaying the history (proven on Astera Round-2 v1-v19 and Google Impact v2-v4). *Distinct* submissions (different YC cohorts, different funders, IGoR vs NSF X-Labs vs AWS) stay as separate files, each with its own history (session `local_04160028`).
- **"Simple twins in vault":** the readable variant of each three-variant doc set mirrors into the Obsidian vault.
- **Personal-vs-org split:** `03-personal/` (cv, biosketch, networking) moved out of Grants entirely into a new private "Personal" Claude project; contract and comp moved to Operations (`06-Operations/legal/`, `06-Operations/compensation/`), separate subsections.
- **Open gap found directly on disk:** Grants' top-level `README.md` is dated **2026-06-12** and still describes the *pre-migration* five-area structure (`01-strategy/`, `02-submissions/`, `03-personal/`, `04-research/`, `05-legal/`, `Yar/`). It does not mention `_context/`, the docs-repo migration, or anything from the July consolidation. **Needs a rewrite.**
- **Also missing on disk:** `Grants/00-CONSOLIDATION/` (the STATE.md / OPEN_QUESTIONS.md / NEXT_STEPS.md / DATA-MANIFEST.md / CONFLICTS.md resume-kit that session `local_2aa3c74c`'s agent created). Session `local_3a22463d` explains why: an Antigravity restructuring pass on/around 2026-07-06 **removed the `00-CONSOLIDATION` tracking folders from the working tree** project-wide (its own words: "that restructure also removed the `00-CONSOLIDATION` tracking folders and my planning docs from the working tree; they're in git history"). Recoverable from git history only, not the live tree.

## 7. Funding-opportunity research consolidation

- **UK/EU eligibility (sourced), session `local_3a22463d`:** ARIA and Wellcome Leap accept a US nonprofit as lead. Wellcome Trust, UKRI, and Horizon Europe require a UK/EU lead with Cytognosis as co-investigator. Recommendation given: **collaborate through a partner first; incorporate a UK/EU entity only if you must coordinate a Horizon Europe consortium.**
- **Nonprofit-vs-for-profit eligibility axis:** shows up adjacent, as the dual-entity discussion (Yar/for-profit PBC vs the Foundation). A 1-page dual-entity brief was drafted for counsel (Duane), covering for-profit-raised IP ownership and background/foreground IP splits (Herve/X-Labs). This gates which grants Cytognosis-the-nonprofit can lead versus must co-apply for, but it is org-structure content, not a funder database.
- **Madhvi-as-partner vs UK/EU branch: not found.** No session of the 7 mentions "Madhvi" at all. If this decision was made, it happened in a different session; search for it by name rather than assuming it is covered by the UK/EU research above.
- **Schema for funding opportunities:** the `funding-opportunity-profile` doc-skill template (v5.6.0) plus `funder_crosswalk_matrix` / `funder_metadata` are the closest things to a formal schema. A separate, **older** `Funding Opportunies_Schema.md` also exists but is archived/superseded, confirmed on disk at `Grants/_archive/from-infrastructure-20260709-225245/Funding/Funding Opportunies_Schema.md`. Treat as historical.
- **New/renewed opportunities surfaced in these sessions:** ARPA-H REST (Aug 12), NSF X-Labs Psychoscope (Jul 13), GCP Research Credits (nonprofit track).

## 8. Explicit open decisions and TODOs

**Needs your decision (no session resolved these):**
- Canonical pick between the **16 Heilmeier-keyed blocks** (2026-07-06) and the **slot-library's U01-U22/A01-A05 system** (from the application_templates archive). Are these merged, or do two reusable-block libraries exist in parallel?
- Whether the **86 files "deferred for a licensing caveat"** during the Grants docs-repo promotion (session `local_debe1db8`) are resolved, and what the caveat actually is (my best guess, unconfirmed: possibly the raw ARPA-H/DoE/NSF ISO template PDFs, which may not be Cytognosis's to redistribute; verify directly).
- Whether `proposal_craft_2026-06-23/` (Heilmeier guide, SS page-budget, ISO-mapping) survived the migration and where it lives now.

**Needs verification (claimed done, not independently confirmed by me):**
- Whether PR #9 (`cytognosis/docs`, opened in session `local_2aa3c74c` for the Funding & Grants Wave-1 work) actually merged. Later sessions (`local_2aa3c74c`'s successors) deliberately kept the docs repo **local-only** to shield newly-added comp/contract content, which raises the question of whether `02-Funding` content after that point is safely on the remote or sitting in unpushed local commits only.
- Landing primary tables (funding funnel, IGoR rosters, `ARPA-H_Awards.tsv`, RDoC/NbN) into `~/datasets/cytognosis/` — **blocked** as of session `local_2aa3c74c`, pending the datasets repo's `cytognosis/` taxonomy branch reaching `main`.
- Canonicalizing the opportunities index and runway synthesis into `02-Funding`, and wiring up `02-Funding/README.md` — queued, no blockers, but not confirmed done.
- This program has a **documented pattern of false "done" claims** (session `local_3a22463d` caught Antigravity claiming the 163-file application-templates merge was complete when it was not, and separately caught its own restructuring silently dropping `00-CONSOLIDATION` folders). Any status this document reports as "done" should get one live check before you rely on it.

**Not blocking, just noted:**
- Strategic Planning and Research were the last two Wave-1 agents still not run as of session `local_7b5bddeb`; this gates a broader "Wave 2" merge, not Grants specifically, but Strategic Planning owns the canonical strategy master that Grants hosts.

---

## DONE vs PENDING

| Status | Item |
|---|---|
| ✅ Done | `Grants and Applications` legacy folder merged (41 unique files routed, 5 duplicates left in place) and marked SUPERSEDED |
| ✅ Done | IGoR legacy stub archived; canonical IGoR tree preserved at `02-submissions/Grants/ARPA-H/IGoR/_consolidation_2026-06-19/` |
| ✅ Done | 65+ research papers evacuated from Grants to the Research project's paper inbox |
| ✅ Done | Grant-alignment map canonicalized into `02-Funding/strategy/` in technical/readable/agent variants; readable mirrored to Obsidian |
| ✅ Done | Slot-library grant-template system (27 slots, 10 funder configs, 71 profiles) discovered, standardized, promoted as system of record |
| ✅ Done | `funding-opportunity-profile` and `literature-synthesis` templates added to the cytognosis-doc skill (v5.6.0) |
| ✅ Done | Grants project fully emptied into the docs repo: submissions, research, funding, and strategy content routed to their docs-repo homes; personal content split to a new Personal project plus Operations |
| ✅ Done | Version-as-git-history policy proven on Astera Round-2 (v1-v19 to 1 file + 19 commits) and Google Impact (v2-v4 to 1 file + 3 commits) |
| ✅ Done | UK/EU funder eligibility researched with sourced recommendation (partner-first) |
| ✅ Done | Funding tracker updated marking Coefficient Giving and Biswas Fast Grants rejected |
| ✅ Done | Cross-project misfiles fixed (Yar research out of Grants; funding files out of Infrastructure) |
| ⏳ Pending, blocked | Primary tables (funding funnel, IGoR rosters, ARPA-H awards, RDoC/NbN) into `~/datasets/cytognosis/`, waiting on the datasets repo's taxonomy branch reaching `main` |
| ⏳ Pending, no blocker | Opportunities index + runway synthesis into `02-Funding`; `02-Funding/README.md` |
| ⏳ Pending, owner-gated | Grants-folder in-place moves committed to git; ~891 MB Projects-repo history rewrite |
| ❓ Unclear | 86 Grants files deferred for a "licensing caveat" during docs-repo promotion; reason not stated |
| ❓ Unclear | Whether the 16 Heilmeier-keyed blocks were folded into the slot-library, per the original plan |
| ❓ Unclear | Whether `proposal_craft_2026-06-23/` (Heilmeier/SS page-budget work) survived the migration |
| ❌ Not started / not found | Grants `README.md` rewrite (still describes the pre-migration structure) |
| ❌ Not found in these sessions | PsychIGoR SS section-to-question / page-budget mapping; Madhvi-as-partner decision |

---

## POINTERS

| Artifact | Path / URL | State |
|---|---|---|
| Slot-library grant-template system | docs repo, `02-Funding/reusable-blocks/slot-library/` (`slots/`, `funders/`, `research/profiles/`, `proposals/`) | Canonical, system of record |
| Funder crosswalk + metadata | docs repo, `02-Funding/reusable-blocks/funder_crosswalk_matrix`, `funder_metadata` | Canonical (per inventory report, not independently opened) |
| cytognosis-doc skill templates | `~/repos/cytognosis/cytoskills/skills/cytognosis/cytognosis-doc/references/{literature-synthesis,funding-opportunity-profile}-template.md` | Canonical, v5.6.0 |
| Grant-alignment map (3 variants) | docs repo, `02-Funding/strategy/` + Obsidian (readable twin) | Canonical |
| 16 Heilmeier-keyed proposal blocks | Not stated in transcript; likely a `00-CONSOLIDATION/` doc dated 2026-07-06 | **Location unconfirmed; may have been dropped by the Jul-6 Antigravity restructure** |
| Application-templates source archive | `~/Documents/_archive/unsorted/application_templates` (outside this agent's attached folders; not independently checked) | Source archive; routed/absorbed into slot-library per reports |
| Astera Round-2 Response, collapsed | docs repo `02-Funding/submissions/` (canonical); sources at `Grants/_archive/versions-collapsed-2026-07-10/Astera_Round2_Response/` | Canonical + archived source, both confirmed on disk |
| Google Impact Revised, collapsed | docs repo `02-Funding/submissions/` (canonical); sources at `Grants/_archive/versions-collapsed-2026-07-10/Google_Impact_Revised/` | Canonical + archived source, both confirmed on disk |
| Grants project `README.md` | `/home/mohammadi/Claude/Projects/Grants/README.md` | **Stale** (dated 2026-06-12; confirmed on disk 2026-07-16) |
| Grants project `_context/` | `/home/mohammadi/Claude/Projects/Grants/_context/README.md` | Live, confirmed on disk; only links `02-Funding` and `01-Strategy` (no `05-Research` link) |
| Grants `00-CONSOLIDATION/` resume kit | Not present in the working tree (confirmed via direct check) | **Removed by an Antigravity restructure per session `local_3a22463d`; recoverable from git history only** |
| Old `Funding Opportunies_Schema.md` | `Grants/_archive/from-infrastructure-20260709-225245/Funding/Funding Opportunies_Schema.md` | Superseded, confirmed on disk |
| Master consolidation control tower | `~/Claude/Projects/Refactor/00-CONSOLIDATION/` (`SHARED-BLUEPRINT.md`, `PROJECT-REGISTRY.md`, `MASTER-CONSOLIDATION-PLAN.md`, `CONSOLIDATION-INDEX.md`, `kickoff-prompts/`) | Canonical, actively maintained |
| Master Finish Plan | `Refactor/00-CONSOLIDATION/MASTER-FINISH-PLAN_2026-07-06.md` | Referenced; not independently opened |
| YC nonprofit-era draft | [Google Doc](https://docs.google.com/document/d/1XSazXPaI68hA5yPEfm96ELpVKr9Kolm7BQeCiLdTTCg/edit) | Old, parked (do not redraft until Yar is revised) |
| IGoR canonical set (per these sessions) | `02-submissions/Grants/ARPA-H/IGoR/_consolidation_2026-06-19/` | Per your memory (outside these sessions), superseded operationally by live Google Docs you now hand-edit directly (standing rule since 2026-06-22) |
| Docs repo remote-sync status | `cytognosis/docs` GitHub repo, PR #9 | **Ambiguous** — opened early; later sessions chose to keep the repo local-only to shield comp/contract content; unclear whether current `02-Funding` state is on the remote |

---

## Method notes

- Sessions 1, 3, 4, and 6 exceeded the direct transcript-read size limit and were recovered from their persisted dump files in full (no content lost from those calls), except that sessions 4 and 6 may not include their earliest turns since the underlying transcript read is capped and both dumps begin mid-narrative.
- I did not open the actual slot-library, funder-profile, or crosswalk files themselves (they live in the docs repo, which is outside this agent's attached folders). Everything about their content is as reported by the consolidation agents in these transcripts, not independently verified.
- I did directly verify, on disk, the current state of `/home/mohammadi/Claude/Projects/Grants` (its `README.md`, `_context/`, and `_archive/` contents), since that folder is attached to this session.
