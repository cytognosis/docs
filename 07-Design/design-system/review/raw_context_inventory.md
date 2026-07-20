# Raw Context Inventory: Design System Merge (2026-07)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Inventory of prior Claude Design prompts, the May 2026 consolidation workspace, the Website project's independent design decisions, and the current branding repo (CytoStyle), produced to inform a design-system merge plan.
> Compiled: 2026-07-08. No em dashes used per house style.

---

## 1. Executive summary

1. Three independent, non-converged design systems exist for Cytognosis: (a) the Claude Design v10 system defined in `design-system-consolidation-2026-05/` (violet `#8B3FC7`, azure `#3B7DD6`, indigo `#5145A8`, Inter/Newsreader/JetBrains Mono, four use-case profiles), (b) the Website's "brand v2" token set in `Claude/Projects/Website/_drive/design-system-decision-v2.md` (deliberately drifted violet `#6E5BD1`, warm beige `#F4F2EF`, Space Grotesk), and (c) the branding repo's current "CytoStyle" package, a generic, unrelated React/MUI component library.
2. The branding repo at `https://github.com/cytognosis/branding` was wholesale replaced on commit `130dee7` ("Replace branding repo with CytoStyle package") with the npm package `@alimohammadiwork/cytostyle`. Its Figma source evidence (IRAN Yekan font, Jalali dates, "dastyar/insurance/investment" banner nodes) indicates the underlying design file is an unrelated Persian-language fintech product, not a Cytognosis-authored system.
3. A repo-wide case-insensitive grep for "claude" across `https://github.com/cytognosis/branding` returned zero matches. The branding repo currently has no live reference to the Claude Design v10 export, the 12 numbered references, or any artifact from the consolidation workspace.
4. A partial, buried bridge exists: `https://github.com/cytognosis/branding/blob/main/src/constants/colors.ts` (lines 163 to 227) exports `cytognosisAppColors`, `cytognosisGradients`, and `cytognosisSurfaces` with numerically correct v10-canonical values (violet `#8B3FC7`, signature gradient `135deg #3B7DD6/#8B3FC7/#5145A8`, light surface `#F4F2EF`, which also happens to match the website's warm-beige background). This is opt-in only; the package's own guideline example (`guidelines/foundations/color.md`) shows a generic teal/grey `#1DBF98`/`#4F545E` palette instead, and no guideline file recommends the Cytognosis constants.
5. The May 2026 consolidation workspace (`design-system-consolidation-2026-05/`) produced a complete, internally consistent operational blueprint: 8 Claude Design prompts, 2 new master skills, 5 revised core skills, and 2 repo-organization plans. None of it has been applied to the live `branding` or `cytoskeleton` repos; it still lives only in the Claude Projects workspace folder.
6. The agreed target structure for Claude Design output is `branding/design-system/` (12 numbered references, `tokens.css`, `profiles/`, `assets/`, `templates/`, `components/` as LinkML contracts, `preview/`, `data-viz/`) plus `branding/skills/` (7 skills), fully specified in `02_repo_organization/branding_repo_plan.md` and `03_claude_design_prompts/prompt_reorg.md`. The live repo instead has `guidelines/`, `skills/cytostyle-app-builder/`, `src/`, `stories/`, `dist/`, none matching the target shape.
7. Five interface templates are specified (app-website, app-phone, app-web, app-desktop, app-extension) with a template-master skill routing to per-template deltas. None are scaffolded in `cytoskeleton/templates/` per the refactor brief's own status tracking. Meanwhile the real production website build (`https://github.com/cytognosis/website`, Vite+React+FastAPI on Cloud Run) is running independently of, and materially diverges from, the app-website template spec (which mandates Astro).
8. The live cytognosis.org rebuild does not consume the Claude Design v10 tokens or the `cytognosis-design-system-master` skill's cheatsheet. It runs its own reconciled "brand v2" / "v3-recommended" token set, deliberately overriding the canonical violet, background, and gradient values for warmth and neurodiversity-calm reasons, with an explicit documented carve-out that the website is "one context" and IDE themes, print, and decks remain canonical v10.
9. Enforcement of file/folder structure and token rules in every reviewed prompt and skill is entirely instructional: Markdown prompts pasted into Claude Design, "Definition of Done" checklists, "what to NOT produce" lists, and "open questions to surface" sections. No linter, CI check, or schema validation was found anywhere in the reviewed materials that would block an off-brand token or wrong-shape file from landing.
10. The most urgent unresolved decision for the merge plan is which token set is authoritative for which surface going forward: v10 canonical for print, decks, IDE themes, and internal tools; website brand v2/v3 for cytognosis.org; and whether CytoStyle is discarded, quarantined as an unrelated internal tool, or re-skinned to consume v10/brand-v2 tokens before any product app is built on it.

---

## 2. Prompt inventory

All files at `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/03_claude_design_prompts/`.

| File | Purpose | Key rules |
|---|---|---|
| `prompt_reorg.md` | One-time consolidation prompt telling Claude Design how to reorganize its working `/design/` output into a clean `branding-export/` tree matching the production branding repo shape. | Full target tree spec (`references/`, `profiles/`, `assets/`, `templates/`, `components/*.contract.yaml`, `preview/`, `data-viz/`); a row-by-row mapping table from every current Claude Design path to its target; 3 named deduplication priorities (tokens.css, logos, products); ships `MIGRATION.md` + `MANIFEST.json` + `SYNC_STATUS.md`; no em dashes; non-destructive staging only. |
| `prompt_template_website.md` | Scaffold prompt for `app-website` (Astro + FastAPI backend), the public cytognosis.org site. | Mandatory pages/layouts/components/content-collections/backend directory listing; SEO and performance budgets (LCP < 1.8s, Lighthouse 95+); brand voice rules baked into every visible string; explicit instruction to salvage specific patterns from the May 2026 `Downloads/website/` React-UMD exploration but not its build system; no lorem ipsum. |
| `prompt_template_phone.md` | Scaffold prompt for `app-phone` (Flutter), the voice-first patient interviewer agent. | LiteRT-LM / Gemma 4 E2B edge-model wiring (lazy load, battery-aware degrade); on-device paralinguistic pipeline (HuBERT + openSMILE, target < 250ms); crisis-detection rails always reachable; consent defaults OFF; quality gates (APK/IPA < 40MB, cold start < 1.5s). |
| `prompt_template_desktop.md` | Scaffold prompt for `app-desktop` (Tauri v2 wrapping `app-web`). | One typed Rust module per native bridge; supervisor-agent sidecar lifecycle (lazy start, local IPC only); per-platform code signing; "No Electron. Ever."; offline-first via Iroh CRDT with visible sync-status indicator. |
| `prompt_template_web.md` | Scaffold prompt for `app-web` (React 19 + Vite + shadcn), logged-in dashboards; explicitly distinct from the public website. | All seven shared packages wired (design-system, api-client, fabric-client, voice-client, auth-shell, telemetry, agent-presentation); PWA mobile-install only, not desktop; voice surface via Web Speech + WASM-VAD fallback; bundle budget < 200KB gzip on the welcome screen. |
| `prompt_template_extension.md` | Scaffold prompt for `app-extension` (Manifest V3, side panel primary UI). | Single codebase, two build modes (patient / internal) picked by env var at build time; least-privilege permissions, no `<all_urls>` in either mode; per-site consent prompt required before any new content-script domain. |
| `prompt_icons.md` | Iteration brief to move the 48-icon set from placeholder to production grade. | Exactly two canonical variants (line + solid), retiring the 10 numbered v9-era style folders to archive; explicit per-icon style spec (24x24 viewBox, 1.6px stroke, round caps); full per-media export matrix (web, phone, slides, docs, favicon); new voice/crisis icon families specified with concrete glyph descriptions. |
| `prompt_profiles.md` | Iteration brief to move the four use-case profiles (Foundation, Clinical, Research, Lab) from placeholder to settled. | Per-profile deliverable checklist (audience paragraph, trigger surfaces, measurable requirements, vibe paragraph, type/palette confirmation, worked example); a profile-selection decision tree; opinionated recommendations Claude is told to state as strong positions (for example, "fold Lab into Research?"); a 10-item settled checklist per profile. |

---

## 3. Structure and enforcement standards distilled

### 3.1 The agreed branding-repo shape

Source: `02_repo_organization/branding_repo_plan.md` (full layout in its §1), cross-referenced by `03_claude_design_prompts/prompt_reorg.md` §1.

```
branding/
├── README.md, CHANGELOG.md, VERSION, LICENSE, ATTRIBUTION.md, CONTRIBUTING.md, SECURITY.md, TRADEMARK.md
├── design-system/
│   ├── README.md, tokens.css, LOGO.md, WRITING.md, IMAGERY.md, ACCESSIBILITY.md
│   ├── references/            (12 numbered v10 files, 01_brand_foundation.md through 12_dataviz.md)
│   ├── profiles/               (README.md, profiles.css, foundation/clinical/research/lab.md, examples/*.html)
│   ├── assets/                 (logos/, icons/ line+solid, products/, fonts/)
│   ├── templates/               (deck/, one-pager.html, email-signature.html, social-cards.html)
│   ├── components/              (*.contract.yaml, LinkML-style, platform-agnostic)
│   ├── preview/                  (rendered HTML cards per token/component category)
│   └── data-viz/                  (sequential.css, diverging.css, colorblind-safe patterns)
├── skills/                          (7 skills; see 3.2)
├── themes/                          (vscode, starship, geany)
├── archive/2026-pre-v10/            (superseded content, preserved)
└── scripts/                          (sync-from-claude-design.py, render_guidelines.py, validate_tokens.py)
```

The live repo (`https://github.com/cytognosis/branding`, confirmed via `find` at 2026-07-08) instead has: `README.md`, 3 audit `.md` files plus one roadmap `.md` at the root, `guidelines/` (4 top-level files plus `components/` and `foundations/` subfolders), `skills/cytostyle-app-builder/`, `src/` (12 subdirectories of React/TS component source), `stories/`, `dist/`, `assets/fonts/` (IranYekan only), `docs/`, `archive/`, `.storybook/`. None of the target directories (`design-system/`, `themes/`, `scripts/`) exist.

### 3.2 The seven-skill family and four-phase skill model

Source: `06_refactor/00_master_architecture.md` §5.

| Phase | Source repo | Skills |
|---|---|---|
| Brand | `branding` | `cytognosis-design-system-master` (routing entry, ships assets), `cytognosis-template-master` (routing entry for 5 templates), `cytognosis-branding` (deep 12-reference home), `cytognosis-orchestrator` (meta-routing), `cytognosis-writer` (grants/narrative) |
| Template-usage | `cytoskeleton` | `pick-template`, `update-template`, `port-token` |
| Dev | `cytocast` | `python-3.13`, `typescript-strict`, `flutter-3`, `tauri-2`, `linkml-authoring`, etc. |
| Runtime | `cytoagent` | runtime skills loaded by deployed agents |

Concurrency rule carried in every brand skill: never load two `SKILL.md` files in the same response; sequence across responses.

### 3.3 How the prior prompts enforced structure (instructional, not automated)

Every mechanism found is a written instruction inside a Markdown prompt or `SKILL.md`, consumed by a human or an agent reading it. No code-level enforcement (linter, schema validator, CI gate, or pre-commit hook checking token values or file placement) was found anywhere in the reviewed materials. Specific mechanisms:

- **Current-to-target mapping tables**, row per file, with an explicit action (keep / move / merge / archive / discard). Used in `prompt_reorg.md` §2 and `branding_repo_plan.md` §2.
- **Deduplication and promotion lists**: naming exactly which of two duplicate files is canonical. `prompt_reorg.md` §3 to §4.
- **"What to NOT produce" lists**: explicit negative constraints per template and per asset type, for example "No Electron. Ever." (`prompt_template_desktop.md` §7), "No em dashes anywhere" (every prompt's Definition of Done).
- **Definition of Done checklists**: 8 to 10 numbered, testable conditions per template prompt (build passes, Lighthouse score, accessibility scanner result, no em dashes).
- **Hard NEVER lists**: cross-cutting negative constraints inside the master skills themselves, for example `cytognosis-design-system-master/SKILL.md` §9 (never pure black/white, never Tailwind Indigo `#6366f1`, never magenta as identity) and `cytognosis-template-master/SKILL.md` §12.
- **Quality-gate tables**: numeric thresholds (bundle size, cold start, coverage percentage, Lighthouse score) per template, all self-reported rather than CI-enforced in the reviewed materials.
- **"Open questions to surface back to Cytognosis" sections**: every prompt ends with a numbered list of decisions Claude Design must pause and ask about rather than silently resolve; this is the main proceduralized guard against silent drift, and it is advisory (depends on the tool operator actually reading and answering it).
- **The "no em dashes" rule** appears as a hard constraint in literally every document reviewed across all four sections (A through D) of this inventory, the single most consistently enforced rule in the entire corpus, and it is style-level only (no automated check found).

---

## 4. Website and app template lineage

### 4.1 The planned lineage (per the consolidation workspace)

Per `cytognosis-template-master/SKILL.md` (v1.1.0) and `06_refactor/01_refactor_brief.md`, five interface templates are meant to live at `cytoskeleton/templates/app-{website,phone,web,desktop,extension}/`, generated via `cytocast copier copy`, all consuming `branding/design-system/` tokens through a shared `design-system-package`. As of the refactor brief's own status table (`06_refactor/01_refactor_brief.md` §1), none of the four original templates (website was added later, in the template-master skill's v1.1.0 revision) had progressed past "not yet started" for `cytoskeleton`, `cytocast`, or `cytoagent`.

### 4.2 The actual, independently-built production website

The real cytognosis.org rebuild lives at `https://github.com/cytognosis/website` (branch `feat/vite-frontend-serving`), documented in `~/Claude/Projects/Website/WEBSITE_DESIGN_HANDBOOK.md`. It is Vite + React (not Astro) for the frontend, FastAPI + SQLModel + Postgres on Cloud Run for the backend, plus a separate Node/Express + Firestore service (`stories-api`) for HIPAA-scoped patient stories. This is a materially different stack from `prompt_template_website.md`'s Astro mandate, built and substantially shipped (`WEBSITE_DESIGN_HANDBOOK.md` §11: phases 0 through 7a done and verified on branch) independently of, and apparently without reference to, the cytoskeleton template plan.

The frontend codebase (`updated_design/`, referred to throughout the Website docs as "Ali's design") was built by a contractor named Ali. Its design tokens were derived through an independent two-round research and reconciliation process:

1. `_drive/design-system-decision.md` (2026-06-09): first reconciliation of Ali's tokens against a "brand-identity skill v9" (a skill distinct from, and predating, the v10 work in `design-system-consolidation-2026-05`).
2. `_drive/research-design-consolidation.md` (2026-06-09): a "v3" recommendation layer that found brand v2 had gaps (missing semantic colors, no focus-ring spec, no dark-mode text ramp) and proposed fixes.
3. `_drive/design-system-decision-v2.md` (2026-06-09): the final, currently authoritative token set for the website, explicitly scoped as "calm by default, canonical-strong on recognition moments," superseding v1's token and motion sections while keeping its reconciliation principle.

None of these three website-side documents cite or cross-reference `design-system-consolidation-2026-05/` or the v10 numbered references. They cite a different, older "brand-identity skill v9" at a session-specific path (see §6).

### 4.3 The CytoStyle connection to the same contractor

The branding repo's current CytoStyle package is published as `@alimohammadiwork/cytostyle`, and its own audit documents state their scope as `/Users/ali/Documents/Cytognosis/CytoStyle` (see `EXISTING_DESIGN_SYSTEM_AUDIT.md` line 3 and `MISSING_COMPONENTS_VERIFICATION_AUDIT.md` line 3). The same "Ali" who built the website's `updated_design` therefore also appears to be the author of the branding repo's CytoStyle replacement, in both cases using his own pre-existing toolkit rather than the Cytognosis v10 system. The two are not cross-wired: the website's CSS tokens (Space Grotesk, Inter, Newsreader, JetBrains Mono, `#6E5BD1`/`#F4F2EF`) do not import from `@alimohammadiwork/cytostyle`, and CytoStyle's default typography (`IRANYekanX`/`IRANYekanXFaNum`, per `EXISTING_DESIGN_SYSTEM_AUDIT.md` §2 Foundations Inventory) does not appear anywhere in the website codebase.

---

## 5. Branding repo and CytoStyle status; Claude Design integration points

### 5.1 Current repo state

Path: `https://github.com/cytognosis/branding`. Package identity: `@alimohammadiwork/cytostyle`, version `1.0.82`, description "Reusable CytoStyle React and Material UI components, providers, hooks, utilities, and design tokens for Cytognosis products" (`package.json`).

Top-level contents (bash `ls -la`, 2026-07-08): `README.md`, `CORRECTED_FIGMA_FIRST_DESIGN_SYSTEM_AUDIT.md` (39KB), `CYTOSTYLE_DESIGN_SYSTEM_IMPLEMENTATION_ROADMAP.md` (47KB), `EXISTING_DESIGN_SYSTEM_AUDIT.md` (33KB), `MISSING_COMPONENTS_VERIFICATION_AUDIT.md` (24KB), `Dockerfile`, `LICENSE`, `archive/`, `assets/` (fonts only: IranYekan), `dist/` (built JS/CSS output), `docs/`, `esbuild.js`, `guidelines/`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `skills/`, `src/`, `stories/`, `tsconfig.json`, `.storybook/`, `.github/`.

`src/` exports 45 components (Button, TextField, DataGrid, MultiSelect, Toast, date pickers, etc.) plus `constants/`, `hooks/`, `libs/`, `providers/` (`ThemeProvider`, `SPAThemeProvider`), `types/`, `context/`, `utils/`. Dependencies include `jalaali-js`, `persian-number`, `react-multi-date-picker`, `stylis-plugin-rtl`, confirming Persian/RTL origin despite the README's claim to be "English-first and LTR by default."

### 5.2 Git history

`git log --oneline -20` (run 2026-07-08) shows the top commit is `130dee7 Replace branding repo with CytoStyle package`. The 18 commits beneath it are legitimate, coherent Cytognosis design-system work, including `22a42ac feat(sync): implement bidirectional Claude Design <-> branding <-> cytoskeleton pipeline`, `6e2815f feat(design-system): link Claude Design URL + consolidate logos + test template skill`, `e919dc5 feat: align brand tokens with Design System v1.0.0`, and `9559138 feat(branding): finalize therapeutic design guidelines and VSCode theme integration`. This confirms the branding repo had a working Claude Design integration and a v10-aligned token set immediately before the replacement commit discarded it. That prior state is still recoverable from git history (commits prior to `130dee7`).

### 5.3 Claude Design integration points found

A repo-wide grep for `claude` (case-insensitive, `https://github.com/cytognosis/branding`) returned **zero matches** in the current working tree. The only surviving Cytognosis-brand-correct content is:

- `src/constants/colors.ts` lines 163 to 227: `cytognosisAppColors` (`primary.600 = #8B3FC7`, `secondary.600 = #3B7DD6`, full 50 to 950 ramps), `cytognosisGradients` (signature/innovation/vitality/data/alert, all matching the v10 canonical gradient values exactly), and `cytognosisSurfaces` (light background `#F4F2EF`, which independently matches the website's brand-v2 warm beige; dark background `#1E1E32`, matching v9/v10 Rich Night).
- `src/Introduction.mdx` and `src/Guide.mdx` show `cytognosisAppColors` used as an example `appColors` prop value for `ThemeProvider`/`SPAThemeProvider`.

This is opt-in, undocumented in the guideline files (`guidelines/foundations/color.md` shows a generic `#1DBF98`/`#4F545E` example instead), and disconnected from typography, spacing, radius, and motion, none of which reference v10 tokens anywhere in the codebase.

### 5.4 What the four audit/roadmap documents actually audit

All four documents (`CORRECTED_FIGMA_FIRST_DESIGN_SYSTEM_AUDIT.md`, `EXISTING_DESIGN_SYSTEM_AUDIT.md`, `MISSING_COMPONENTS_VERIFICATION_AUDIT.md`, `CYTOSTYLE_DESIGN_SYSTEM_IMPLEMENTATION_ROADMAP.md`) are systematic, high-quality design-system audits, but of CytoStyle's own Figma file and code, not of Cytognosis's brand Figma or the Claude Design v10 export. `EXISTING_DESIGN_SYSTEM_AUDIT.md` line 3 states its scope as `/Users/ali/Documents/Cytognosis/CytoStyle` source; `MISSING_COMPONENTS_VERIFICATION_AUDIT.md` line 3 states the same. The Figma pages inspected (`CORRECTED_FIGMA_FIRST_DESIGN_SYSTEM_AUDIT.md` §2) are named "UI Design - Version 3/4/Draft," containing thousands of nodes for a mobile fintech-style product (wallet cards, insurance banners, installment tables, "dastyar" banner), evidence unrelated to Cytognosis's actual product surfaces. The roadmap (`CYTOSTYLE_DESIGN_SYSTEM_IMPLEMENTATION_ROADMAP.md`) is a 5-phase plan to close gaps between that Figma file and the CytoStyle code (add `Badge`, `Card`, `DashboardShell`, `MobileAppShell`, token modules), entirely internal to CytoStyle's own scope.

### 5.5 Guidelines and skills content

`guidelines/` (`Guidelines.md`, `setup.md`, `runtime.md`, `types.md`, `components/{overview,buttons,forms,feedback,layout,data-display,date-inputs}.md`, `foundations/{color,typography,spacing,icons}.md`) documents generic English/LTR, dense, operational MUI-app conventions with no Cytognosis voice, tone, or profile content whatsoever, a completely different register from the v10 `WRITING.md`/`voice.md` material.

`skills/` contains exactly one skill, `cytostyle-app-builder/SKILL.md` (plus `agents/openai.yaml`), targeted at building CytoStyle screens from Figma via an MCP workflow for "Codex." It has no relationship to, and does not mention, the seven-skill Cytognosis family (`cytognosis-design-system-master`, `cytognosis-branding`, etc.) specified in the consolidation workspace. If the plan is to migrate those seven skills into `branding/skills/` per `06_refactor/01_refactor_brief.md` §3.0 Step 2, there is now a direct placement collision with `cytostyle-app-builder`.

---

## 6. Open questions and stale items

1. **Intent behind commit `130dee7`.** Unclear whether the wholesale branding-repo replacement was a deliberate pivot (use CytoStyle as a component-implementation layer under a still-intended v10 token/voice source) or a scoping error that deleted working Claude Design integration. The task framing ("recently replaced... NOT yet updated by Antigravity") implies the latter is expected to be reconciled, but the depth of the deletion (removing `design-system/`, all 7 skills, the sync pipeline) argues for treating this as a full recovery-and-reconciliation task, not a light touch-up.
2. **Recoverable prior state.** Commits `22a42ac` and `6e2815f` (both before `130dee7`) describe a working "bidirectional Claude Design <-> branding <-> cytoskeleton pipeline" and v10 token alignment. Worth inspecting via `git show` / `git log -p` before deciding CytoStyle's fate, since this may shortcut re-doing work the consolidation already produced.
3. **Skill placement collision.** `branding/skills/` is now occupied by `cytostyle-app-builder/`. The planned migration of the 7 Cytognosis skills into `branding/skills/` (per `06_refactor/01_refactor_brief.md` §3.0 Step 2) needs an explicit placement decision (separate subfolder, rename, or full removal of `cytostyle-app-builder`).
4. **Downstream repo status unknown.** This inventory did not check `cytoskeleton`, `cytocast`, or `cytoagent` (out of the requested scope). Their actual state materially affects whether any of the five interface templates exist anywhere, and the refactor brief's own tracking (`06_refactor/01_refactor_brief.md` §1, dated 2026-05-13) lists all three as "not yet started." This should be verified fresh before the merge plan assumes anything about template scaffolding.
5. **Website token set is layered, not singular.** Three website-side documents exist in sequence (`design-system-decision.md` = v1/"v2" naming is confusing internally, then `research-design-consolidation.md` = the "v3" recommendation, then `design-system-decision-v2.md` = the actual current authority). A reader landing on `design-system-decision.md` alone gets superseded token values. The merge plan should treat `_drive/design-system-decision-v2.md` as the sole authoritative website token source and flag the other two as historical.
6. **Stale, session-scoped cross-reference.** `research-design-consolidation.md` (source list, bottom of file) cites a "brand-identity skill" at an absolute path inside a specific prior agent session (`~/.config/Claude/local-agent-mode-sessions/.../local_aaa10a0a-5a78-4a28-9f58-251bebb25a77/.claude/skills/brand-identity/SKILL.md`), described there as "v9.0." That path is very unlikely to resolve in this or future sessions. This session has a currently available skill named `anthropic-skills:brand-identity` ("Official Cytognosis Foundation brand identity, design system, voice, and content standards... REQUIRED for ALL Cytognosis-branded output"); whether that skill is the same v9, an updated v9, the v10 from this consolidation, or something newer was not checked in this task and should be the first thing read in the next step, since it is clearly the skill actually being loaded for current Cytognosis-branded work.
7. **Font licensing gap, never closed.** `prompt_reorg.md` §4 (open question 4) flags Source Serif Pro, Lexend, and Atkinson Hyperlegible as referenced-but-unlicensed. The website independently substituted Newsreader for Source Serif Pro and deferred Lexend/Atkinson Hyperlegible to "Phase 7a" per `_drive/design-system-decision-v2.md` §7 (D2, D3). No shared font asset pipeline exists between the website repo and the branding repo; each made its own independent call.
8. **Branding-repo distribution mechanism still undecided.** `02_repo_organization/cytoskeleton_repo_plan.md` §9 and `06_refactor/00_master_architecture.md` §10 both leave "git submodule vs internal-PyPI" for branding distribution as an open, unresolved question from 2026-05-13. This is now secondary to reconstituting the branding repo's content at all, but will need an answer before `cytoskeleton` can consume it.
9. **CytoStyle's genuine utility is unclear but non-zero.** The audits show CytoStyle is a reasonably mature MUI wrapper library (45 components, theme providers, hooks) with a partially-retrofitted Cytognosis palette (`cytognosisAppColors`). If any internal Cytognosis tool already depends on `@alimohammadiwork/cytostyle` in production, discarding it outright carries migration cost; this was not checked (no `package.json` dependents were searched outside the branding repo itself) and should be confirmed before deciding to remove it.

---

*Sources consulted for this inventory, all with exact paths cited inline above:*
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/03_claude_design_prompts/*.md` (8 files)
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/01_plan/00_master_plan.md`
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/02_repo_organization/{branding_repo_plan.md,cytoskeleton_repo_plan.md}`
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/06_refactor/{00_master_architecture.md,01_refactor_brief.md,README.md}`
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/04_skills_new/cytognosis-design-system-master/SKILL.md`
- `~/Claude/Projects/Science and Platform/design-system-consolidation-2026-05/04_skills_new/cytognosis-template-master/SKILL.md`
- `~/Claude/Projects/Website/WEBSITE_DESIGN_HANDBOOK.md`
- `~/Claude/Projects/Website/_drive/{design-system-decision.md,design-system-decision-v2.md,research-design-consolidation.md,inventory-new-design.md,handbook-src-design.md}`
- `~/Claude/Projects/Website/MASTER_DRIVE_PLAN.md` (design-relevant excerpts via grep)
- `https://github.com/cytognosis/branding{README.md,CORRECTED_FIGMA_FIRST_DESIGN_SYSTEM_AUDIT.md,EXISTING_DESIGN_SYSTEM_AUDIT.md,MISSING_COMPONENTS_VERIFICATION_AUDIT.md,CYTOSTYLE_DESIGN_SYSTEM_IMPLEMENTATION_ROADMAP.md}`
- `https://github.com/cytognosis/branding/tree/main/guidelines{Guidelines.md,foundations/color.md}`
- `https://github.com/cytognosis/branding/blob/main/skills/cytostyle-app-builder/SKILL.md`
- `https://github.com/cytognosis/branding/blob/main/src/constants/colors.ts`
- `https://github.com/cytognosis/branding/blob/main/package.json`
- `git log --oneline -20` in `https://github.com/cytognosis/branding`
