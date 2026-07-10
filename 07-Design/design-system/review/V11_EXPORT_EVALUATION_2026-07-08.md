# v11 Export Evaluation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-08. **Reading time:** about 4 minutes. **Raw evidence:** `raw_v11_export_audit.md`.
**If you only read one thing:** the merge itself worked; one more Claude Design run (`03_next_prompts/prompt_v11_revision_1.md`) closes the 5 remaining defects and executes all of Phase 2.

---

## 0. BLUF

- **Phase 1 (the merge) is substantially done and structurally correct:** 5 clean passes, 3 partials, 1 fail across 9 gating checks. Tokens, governance, components, references, profiles, templates, SKILL.md, and the Yar removal are all verified right.
- **Claude Design correctly stopped before Phase 2** because its own checklist had failures. Zero asset generation exists yet (no logo family, favicons, app icons, social, slides, or icon completion).
- **Five defects need Revision 1;** all are small and mechanical. The revision prompt also pre-answers the two Phase 2 approval questions with my recommendations, so the next run finishes everything.

## 1. What is done (verified, not claimed)

| Area | Evidence |
|---|---|
| Version discipline | `VERSION` = 11.0.0; changelog has the migration table, Yar list, and 9.0/10.0/1.0.0 retirement |
| Tokens | Every reconciled value exact (spacing, easings, day scale, semantic aliases, `--cg-lp-violet`); primitives byte-identical to the base; **new dark landing theme** added (`--cg-lp-bg: #15131C`) |
| Components | All 7 have `.jsx` + `.d.ts` + `.prompt.md` (the 2 missing docs were written); **Button now meets 44px on all four sizes**; all 7 registered in the adherence config |
| Grafts | Governance suite, ACCESSIBILITY (with re-audit flags), WRITING (real product names, merged banned list), IMAGERY, LOGO, profiles (all 12 files carry the settlement note), templates (old token names cleaned), 12 references with the 02/03 routing fixed and documented |
| Single entry point | Exactly one SKILL.md, comprehensive index, read order, hard NEVER list |
| Scope | Yar fully removed; uploads provenance untouched; zero unexplained files |

## 2. What needs revision (Revision 1, in the prompt)

| # | Defect | Severity |
|---|---|---|
| 1 | "breakthrough" used as live copy in 2 places (`guidelines/colors-gradients.card.html:27`, `references/01_brand_foundation.md:36`) | High |
| 2 | Em dashes: 2 authored (`_adherence.oxlintrc.json` lint messages), 33 in tool-generated manifest/bundle (waive with changelog note if not editable) | High |
| 3 | Font allowlist never extended for the 4 profile fonts; the changelog claims it was, and every profile font declaration would trip the linter | High |
| 4 | Hardcoded off-token hexes: 14 in `templates/` (includes near-miss drift like `#1E1E2E` vs token `#1E1E32`), 48 in `profiles/` (old per-profile palette as bare literals; convert to named profile tokens now, reconcile values in the settlement pass) | Medium |
| 5 | Icon README claims 1.6px strokes; actual sprites use 1.5/1.75/2 (fix the claim now; Phase 2 redraws at 1.6) | Low, plus `readme.md` -> `README.md` casing |

## 3. What remains to be done

1. **Phase 2, all of it** (next Claude Design run): corrected master mark (3 real fixes; the `#d1d1d1` item turned out to be editor metadata, not a visible color), wordmark lockups, mono + reversed + simplified small variants, favicon set, app icons, social assets, deck cover/dividers, template re-pointing, 48-icon production set, ICONOGRAPHY.md, version bump to 11.1.0. The two approval gates (logo color corrections; retiring the old flat marks to archive) are pre-answered YES in the revision prompt; say so now if you want either reversed.
2. **After the export passes:** publish the design system in Claude Design (the Published checkbox), regenerate the brand-identity skill from v11, profiles settlement pass, accessibility re-audit, then the branding repo recovery (still gated on the Ali conversation) and the downstream template updates.

## 4. Judgment call worth knowing

The merge converted em dashes inside token-file comments (values untouched). Technically it edited files it was told not to restyle, but the em-dash rule is absolute and only comments changed. I scored this acceptable, not a defect.
