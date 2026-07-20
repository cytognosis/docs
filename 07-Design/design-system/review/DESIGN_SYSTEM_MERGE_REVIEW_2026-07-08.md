# Design System Merge Review

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-08. **Reading time:** about 8 minutes.
**If you only read one thing:** read Section 8 (the decision box). Everything else proceeds without input.

---

## 0. BLUF

- **Ali's latest export is the right structural base** for the merged system: modular tokens, typed components with usage docs, working AI-adherence rules, and a full provenance trail. **Your system supplies the governance and brand-depth layer** it lacks: accessibility, writing, imagery, and logo standards, the four-profile system, deliverable templates, branded icons, and versioning discipline.
- **The brand itself never forked.** Every primitive color scale, gradient, font choice, radius, and shadow is byte-identical between your system and Ali's latest. The conflicts live in one thin layer: **semantic aliases** (`--bg-*`, `--fg-*`, `--border-1`), one spacing step, and two easing curves. All are resolvable with a short table (Section 4).
- **Ali_old is not a Cytognosis asset.** It is Ali's personal brand system (built from his CV and work manual, zero Cytognosis mentions). Nothing merges from it; it stays archived as process reference.
- **The branding repo needs attention.** Commit `130dee7` replaced the entire repo with CytoStyle, Ali's pre-existing Persian/RTL fintech MUI library. It contains zero references to Claude Design or the v10 system. The prior working state (v10 tokens, 7 skills, bidirectional sync pipeline) is fully recoverable from git history.

---

## 1. What each package actually is

| Package | Files | Identity | Verdict |
|---|---|---|---|
| `mine` | 457 | Cytognosis, v9/v10 era (three conflicting version claims) | **Governance donor.** Broadest scope, weakest internal consistency |
| `ali_old` | 83 | **Ali's personal brand** (monochrome + blue, fintech/executive) | **Out of scope.** Archive as reference; confirms shared platform scaffolding (`deck-stage.js` identical to yours) |
| `ali_latest` | 129 | Cytognosis, self-declared v10.1.0, June 2026 | **Structural base.** Best machine-readability of the three; missing governance |

One scope surprise inside `ali_latest`: it bundles **Yar**, a separate AI-companion product (11 files: `yar-app/`, three HTML prototypes, `Yar Handoff.md`). Yar reuses Cytognosis tokens but is not one of the four documented platform products. It needs an explicit in/out call (Section 8, D1).

---

## 2. What is good (keep)

**From `ali_latest` (the base):**

- **Modular `tokens/`** (7 files, one concern each) instead of one flat CSS file. Adopt as-is.
- **Typed components**: `components/core/{Badge,Button,Card,Input,Tag}` and `components/data/{DataBar,MetricTile}`, each with `.jsx` + `.d.ts`, most with `.prompt.md`. The only system whose adherence config can actually catch an invalid prop (19 validation rules).
- **`guidelines/`**: 16 `@dsCard`-tagged specimen cards, individually addressable.
- **Landing-light palette** (`--cg-lp-*`, 14 tokens) with a formal `[data-theme="light"]` block.
- **Provenance**: the 12 literal source documents in `uploads/`, the canonical token JSON, and the CEO-approved reference HTML.
- **Non-diagnostic safety rules** as a first-class readme section.

**From `mine` (the grafts):**

- **Governance suite**: `CONTRIBUTING.md` (ownership matrix), `CHANGELOG.md`, `VERSION`.
- **Standards docs**: `ACCESSIBILITY.md` (WCAG 2.2 contrast audit per profile), `WRITING.md`, `IMAGERY.md`, `LOGO.md`. Nothing comparable exists in either Ali system.
- **The four-profile system** (`profiles/`: Foundation, Clinical, Research, Lab) with CSS-scoped re-theming. Unique and strategically important for a clinical-adjacent brand.
- **Deliverable templates**: `templates/deck.html`, `one-pager.html`, `email-signature.html`, `social-cards.html`.
- **Branded icons**: `assets/icons/violet/` sprite sheets. Directly fills `ali_latest`'s acknowledged icon gap (its readme notes it ships no bundled SVGs).
- **The 12-file `branding/references/`** set (granular brand guide), after fixing its routing bugs.
- **Lumen dark variant**: your Lumen proposal includes a dark-mode landing palette; `ali_latest` has none.

**Convergence insight (the quiet good news):** your Lumen glass proposal, Ali's `--cg-lp-*` landing palette, and the website's "brand v2" warm palette are the **same palette**. Eight of nine shared hex values are identical across Lumen and `ali_latest`; the beige `#F4F2EF` also survives inside CytoStyle's `cytognosisSurfaces`. The only straggler is the landing violet: Lumen `#7159A7` vs `#6E5BD1` everywhere else. The three-way drift already converged on its own; the merge just formalizes it.

---

## 3. What is broken or stale (fix during merge)

| # | Defect | Where | Severity |
|---|---|---|---|
| 1 | Root `SKILL.md` indexes almost none of the system's best content (`profiles/`, `branding/`, `templates/`, governance docs invisible to an agent) | `mine/SKILL.md` | High |
| 2 | `branding/SKILL.md` routing table points to wrong filenames (02/03 swapped) | `mine/branding/SKILL.md` | High |
| 3 | Three conflicting version claims (9.0, 10.0, 1.0.0) and three divergent SKILL.md entry points | `mine` root | Medium |
| 4 | CHANGELOG describes fonts and folders that never shipped (Geist, Fraunces, `motion/`, `a11y/`); Fraunces is banned elsewhere | `mine/CHANGELOG.md` | Medium |
| 5 | Adherence config registers zero components (293 tokens tracked, nothing prop-checked) | `mine/_adherence.oxlintrc.json` | Medium |
| 6 | `Button.jsx` violates the system's own 44px touch-target rule (sm 32px, md 40px) | `ali_latest/components/core/Button.jsx` | Medium |
| 7 | `DataBar.prompt.md` and `Tag.prompt.md` missing (5 of 7 components documented) | `ali_latest/components/` | Low |
| 8 | No CHANGELOG, VERSION, or CONTRIBUTING anywhere | `ali_latest` | Medium |
| 9 | Yar product unreferenced by the system's own scope docs | `ali_latest` | Medium |
| 10 | WRITING.md examples use retired placeholder product names (Signal, Cohort, Trace) | `mine/WRITING.md` | Low |

---

## 4. Token reconciliation (the complete conflict list)

Primitives need **no work**: all six hue scales (violet `#8B3FC7`, azure `#3B7DD6`, indigo `#5145A8`, teal `#14A3A3`, coral `#F26355`, magenta `#E0309E`, every shade step), all five gradients, fonts (Inter, Newsreader, JetBrains Mono), radii, and shadows match exactly.

Resolutions below adopt **`ali_latest` as canonical** (it is the declared new standard) unless noted:

| Token | Yours | Ali latest | Resolution |
|---|---|---|---|
| `--fg-1/2/3` | Brighter ramp | Softer ramp | **Adopt Ali's values.** Slightly lower contrast; ACCESSIBILITY.md re-audit required (backlog item 4) |
| `--bg-1` through `--bg-4` | `bg-1` = darkest | `bg-1` = mid-dark, `bg-4` = darkest (**inverted semantics**) | **Adopt Ali's mapping.** Ship a migration table in the changelog; any artifact ported from your system must remap, or it renders wrong silently |
| `--border-1` | White-based | Violet-tinted | **Adopt Ali's** (on-brand hue) |
| `--space-4xl` | 96px | 80px (+ new `--space-5xl` 120px) | **Adopt Ali's** |
| `--ease-out`, `--ease-in-out` | Material-style curves | More expressive curves | **Adopt Ali's** |
| Light neutrals | `--cg-neutral-400..50` | Renamed `--cg-day-400..50` (same hex) | **Adopt `--cg-day-*`** (mechanical rename) |
| Landing violet | Lumen `#7159A7` | `--cg-lp-violet: #6E5BD1` | **Adopt `#6E5BD1`** (already live on the website and in CytoStyle's surviving constants) |
| Alternate font stacks | 3-deep per role | Single alt (Space Grotesk) | Keep Ali's single alt as the token; record your 3-deep stack in the typography reference as documented optionality |

---

## 5. Merge plan: Design System v11

**Base:** a copy of Ali's latest Claude Design project. **Version:** reset to a single semver track, `11.0.0`, with a fresh CHANGELOG whose first entry documents this merge (retires the 9.0/10.0/1.0.0 confusion).

**Graft from your system (in order):**

1. Governance: `CONTRIBUTING.md`, `CHANGELOG.md` (rewritten, truthful), `VERSION`.
2. Standards: `ACCESSIBILITY.md`, `WRITING.md` (fix product names), `IMAGERY.md`, `LOGO.md`.
3. `profiles/` (all five CSS files, README, examples), pending the profiles settlement pass (backlog).
4. `templates/` (deck, one-pager, email-signature, social-cards).
5. `assets/icons/violet/` sprite sheets, plus logo set reconciliation.
6. `branding/references/01..12` as the deep reference layer, with the 02/03 routing fix.
7. Lumen dark-variant tokens, renamed into the `--cg-lp-*` family as its `[data-theme="dark"]` block.

**Fixes during merge:** Button touch targets (44px minimum for all sizes), write the two missing `.prompt.md` files, register every component (old and grafted) in `_adherence.oxlintrc.json`, and produce **one** root `SKILL.md` that indexes everything (profiles, references, templates, governance) with correct filenames. Delete the two stray SKILL.md variants.

**Out:** Yar files (11) leave the design system (Section 8, D1). Ali_old contributes nothing.

**Target structure** (matches the agreed May standard, updated with Ali's proven patterns):

```
design-system/
├── SKILL.md, README.md, VERSION, CHANGELOG.md, CONTRIBUTING.md
├── ACCESSIBILITY.md, WRITING.md, IMAGERY.md, LOGO.md
├── tokens/            (base, colors, fonts, motion, shadows, spacing, typography)
├── styles.css         (import-only aggregate)
├── components/        (core/, data/: .jsx + .d.ts + .prompt.md per component)
├── guidelines/        (@dsCard specimen cards)
├── profiles/          (foundation, clinical, research, lab)
├── references/        (01_brand_foundation .. 12_dataviz)
├── templates/         (deck/, one-pager, email-signature, social-cards)
├── assets/            (logos/, icons/ line+solid, products/, fonts/)
├── uploads/           (provenance, kept)
└── _adherence.oxlintrc.json, _ds_manifest.json
```

One deliberate standards update: the May plan specified LinkML `*.contract.yaml` component contracts. Ali's `.d.ts` + `.prompt.md` + oxlint pattern is running and enforcing today inside Claude Design, so **v11 keeps `.d.ts` + `.prompt.md` as the source of truth**; LinkML contracts become a generated, repo-side artifact later if cytoskeleton needs platform-agnostic contracts.

---

## 6. Claude Design execution and enforcement

**How to run the merge:** duplicate Ali's latest project in Claude Design (name it "Cytognosis Design System v11"), upload the graft files from `01_extracted/mine/` listed above, then paste `03_next_prompts/prompt_merge_v11.md`. The prompt carries the full mapping table, token resolutions, fix list, structure tree, Definition of Done, and the open questions Claude Design must surface rather than resolve silently.

**Enforcement stance (unchanged philosophy, sharper teeth):** every prior prompt enforced structure instructionally (mapping tables, Definition-of-Done checklists, hard NEVER lists, open-questions sections). That stays, because it is what Claude Design can consume. Two upgrades: (1) the adherence config now validates component props for the **whole** merged library, not 7 components; (2) once the export syncs to the branding repo, repo-side automated checks (`validate_tokens.py`, CI token diff against `uploads/11_cytognosis_design_tokens.json`) close the gap the review found: **no automated enforcement existed anywhere**. The "no em dashes" rule remains in every prompt.

**Templates:** the five interface-template prompts (website, phone, web, desktop, extension) remain valid but must be re-pointed at v11 token names (notably `--cg-day-*`, `--space-5xl`, and the lp palette) before reuse. The production website keeps its documented carve-out (brand v2 tokens for cytognosis.org); v11's lp palette now matches it, so the carve-out shrinks to naming differences.

---

## 7. Branding repo (CytoStyle) assessment

**Status:** the repo is currently `@alimohammadiwork/cytostyle` v1.0.82, a 45-component React/MUI library with Persian/RTL fintech origins (IranYekan fonts, Jalali date handling, Figma evidence from an unrelated product). Repo-wide grep finds **zero** references to Claude Design. The four audit documents at its root audit CytoStyle against its own Figma file, not against the Cytognosis brand.

**What survives:** one buried bridge, `src/constants/colors.ts`, exports `cytognosisAppColors`, `cytognosisGradients`, and `cytognosisSurfaces` with numerically correct v10 values. It is opt-in and undocumented; the package's own color guideline shows a generic teal/grey palette instead.

**What was lost, and is recoverable:** commits before `130dee7` contain the v10-aligned token set, the design-system tree, and a working bidirectional Claude Design <-> branding <-> cytoskeleton sync pipeline (`22a42ac`, `6e2815f`). Recovery is a git operation, not a rebuild.

**Recommended disposition (D2 in the decision box):** restore the pre-`130dee7` branding content as the repo's core, move CytoStyle out to its own repo (it is already namespaced under Ali's personal npm scope), keep the `cytognosisAppColors` bridge by regenerating it from v11 tokens, and resolve the `skills/` collision (CytoStyle's `cytostyle-app-builder` currently occupies the folder planned for the seven Cytognosis skills). Before anything moves: check whether any internal tool depends on `@alimohammadiwork/cytostyle` in production, and have the conversation with Ali, since this rolls back his replacement commit. The Antigravity prompt in `03_next_prompts/` does the read-only investigation and prepares the PR plan; nothing force-pushes.

---

## 8. Decision box (flagged; I proceed on the recommendations unless you say otherwise)

| # | Decision | Recommendation | Why |
|---|---|---|---|
| D1 | Yar in or out of the design system? | **Out.** Yar becomes its own Claude Design project consuming v11 tokens; files stay archived in `01_extracted/` meanwhile | Separate product, separate voice register; keeps the design system's scope clean |
| D2 | CytoStyle disposition | **Quarantine to its own repo; restore branding repo from git history** | The org's branding repo should hold the org's brand; requires the Ali conversation and a dependency check first |
| D3 | Semantic token conflicts | **Adopt Ali's values wholesale** (with changelog migration table and a11y re-audit) | He built them for the current website/app direction; halving the diff beats litigating each alias |
| D4 | Version | **v11.0.0, single semver track** | Clean break from the 9.0/10.0/1.0.0 confusion |

D2 is the only one needing outside action (Ali). D1, D3, and D4 are already baked into the merge prompt as defaults.

---

## 9. What remains after the merge (ordered, do-now first)

1. **Run the merge** in Claude Design with `prompt_merge_v11.md`. No outreach needed.
2. **Icons production pass**: rerun `prompt_icons.md` against v11 (48-icon target, two variants); your 20 branded SVGs seed it. No outreach needed.
3. **Profiles settlement**: rerun `prompt_profiles.md` (includes the fold-Lab-into-Research question). No outreach needed.
4. **Accessibility re-audit** of the adopted `--fg-*` ramp against WCAG 2.2, updating ACCESSIBILITY.md. No outreach needed.
5. **Branding repo recovery** via the Antigravity prompt (read-only investigation first, then PR). Parked until D2 is confirmed with Ali.
6. **Font licensing and self-hosting** (Lexend, Atkinson Hyperlegible, Newsreader): the one open question every prior effort deferred.
7. **Yar spin-out** as its own Claude Design project (after D1 confirmation).
8. **Verify downstream repos** (cytoskeleton, cytocast, cytoagent): the refactor brief's "not yet started" status is from May and needs a fresh look before template work resumes.
9. **Website naming alignment**: document the now-tiny brand-v2 vs `--cg-lp-*` mapping in the website handbook.

---

## 10. Sources

- `02_review/raw_comparison_designsystems.md` (full three-way inventory, token tables, component matrix, 15 conflicts, quality scores)
- `02_review/raw_context_inventory.md` (8 prompts, structure standards, website lineage, CytoStyle audit)
- Extracted systems under `01_extracted/`; May workstream under `Science and Platform/design-system-consolidation-2026-05/`; website docs under `Website/`; branding repo at `https://github.com/cytognosis/branding`
