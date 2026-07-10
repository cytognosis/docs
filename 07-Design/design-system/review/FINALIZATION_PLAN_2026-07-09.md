# Design System Finalization Plan

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-09. **Reading time:** about 6 minutes.
**If you only read one thing:** the design system is structurally done but has a content problem (Helix shipped as a fake fourth product, 23 times) and a calm problem (live parallax, unbounded loops, cool-dark default). Both get fixed in one big revision run, in a **fresh** Claude Design chat, using `03_next_prompts/prompt_v11_revision_3_content_and_calm.md`. Then a separate run makes the artifact pack (VS Code theme, meeting and social backgrounds).

---

## 0. BLUF

- **Where we are:** the merge and asset generation are solid and verified. What remains is not plumbing, it is substance: the content is off-vocabulary, and the design is not yet living up to your own neurodiverse and therapeutic research.
- **Three problem clusters, one revision:** (1) content and vocabulary, (2) neurodiverse and calm, (3) profiles and platform fit. All fixable in one structured pass.
- **Do it in a new chat.** Claude Design is at 566k tokens and its self-reports have already drifted once. A fresh chat with the export re-uploaded is more reliable, and the revision prompt re-checks the earlier mechanical fixes so nothing regresses.
- **Two decisions for you** (both have a recommended default; I proceed unless you say otherwise): profile lineup (fold Lab into Research), and default surface (warm paper, not dark).

---

## 1. What is DONE (verified across exports)

- Structure, tokens, components, single SKILL.md, Yar removal: all correct and byte-stable.
- Logo corrected exactly as approved; full family, favicons, app icons, social assets all present at exact dimensions.
- 48 line + 48 solid icons, uniform 1.6px, token colors only.
- No em dashes or banned words in authored copy (the two historical slips were fixed).

## 2. What NEEDS REVISION (the substance)

### 2a. Content and vocabulary (the biggest issue)

**"Helix" ships as a fake fourth public product, 23 times across 14 files**, including its own icon, sprite entries, and a landing-page card. Per your note, Helix is an internal org-structure draft, not a product. The canonical architecture is **three products: Cytoverse (map), Cytoscope (sensor), Cytonome (navigator)**, together "GPS for Human Health," with **Neuroverse** as the public brain-health flagship deployment. The landing page even contradicts itself (its own heading says "Three systems," then a block below adds Helix as a fourth).

Also: stale v10.1.0 version header, a generic founder story instead of your approved public-safe variant, no "three blindspots" framing anywhere, no Neuroverse on the landing page, and copy that drifts toward implying diagnosis (against your non-diagnostic rule). Full file-by-file replacement copy is written and ready in `raw_vocabulary_alignment.md` Section 4.

### 2b. Neurodiverse and calm (your own research, not yet applied)

Ran your 45-item research checklist against the system: **21 pass, 16 fail, mostly in motion and layout**, the two areas your own prior research named highest-risk. Live violations that exist today, not hypothetically:

- Scroll-coupled parallax and 5+ unbounded looping animations in `landing/animations.js` and `profiles/motion.css`.
- Body-text floor conflicts three ways (14px vs 16px vs 17pt). Recommend 16px.
- The system reverts to a dark violet-gradient "AI SaaS" look outside the hero, instead of your warm calm-by-default surface.
- Reduced-motion handling incomplete; duplicate motion tokens mean a single "calm mode" switch would miss most surfaces.

Recovered bonus: your **therapeutic design guidelines with citations** (NIH, chromotherapy, dyslexia research) exist in branding git history (commit 9559138, since overwritten). Worth restoring as the evidence layer under ACCESSIBILITY.md.

### 2c. Profiles and platform fit

- **Fold Lab into Research** (as a density toggle). That gives a clean three-profile lineup (Foundation, Clinical, Research) and resolves the extension template's own indecision. Decision D5 below.
- **Clinical profile does not yet implement the calm rules** and has an internal contradiction (docs say no magenta, the alert example uses magenta). Re-point Clinical to the warm palette.
- **Missing safety components** block the patient phone app: no `CrisisBanner`, no `ConsentPrompt`. These are required by your own phone template spec.
- **Platform gaps:** no mobile type ramp confirmed, touch tokens exist but are not enforced, no density mode for dashboards, extension side-panel constraints unaddressed.

### 2d. Color uniqueness

The six-hue fluorophore palette and DAPI-violet story are genuinely ownable, but the system collapses into generic violet-on-dark gradients on most surfaces and never surfaces its own best assets (the fluorophore naming story, the logo's ring/orb/node geometry). Five distinctiveness moves are specced in `raw_profiles_usecases_critique.md` Section C; the top one is making warm paper the default surface.

## 3. What is YET TO BE DONE (sequence)

1. **Revision 3 (content + calm + profiles + platform), fresh chat.** The prompt below. Targets v11.2.0.
2. **Audit the v11.2.0 export** (same rigor; trust nothing self-reported).
3. **Publish** in Claude Design.
4. **Regenerate the brand-identity skill** from v11.2.0 (the live skill still carries an outdated gradient and, now confirmed, the same stale vocabulary risks).
5. **Artifact pack run** (separate, after finalization): `raw_artifact_pack_spec.md` covers all 17 missing artifacts. Order: VS Code theme family, meeting backgrounds, LinkedIn, other social, Slack, letterhead.
6. **Profiles settlement + accessibility re-audit** (values reconciliation and WCAG re-check of the adopted `--fg-*` ramp).
7. **Branding repo recovery** (gated on the Ali conversation; Antigravity prompt ready).
8. **Interface templates** re-pointed to v11.2.0, then built.

## 4. Decisions (recommended defaults; I proceed unless you redirect)

| # | Decision | Recommendation | Rationale |
|---|---|---|---|
| D5 | Profile lineup | **Foundation, Clinical, Research** (fold Lab into Research as a density toggle) | Removes redundancy, resolves the extension template's open question |
| D6 | Default surface | **Warm paper (`--cg-lp-*`) as the default**, dark as an explicit theme | Your calm research names this the highest-leverage distinctiveness and calm move at once |
| D7 | Body text floor | **16px** system-wide | Matches your prior research; resolves the three-way conflict |
| D8 | "GPS for Human Health" vs "GPS for Health" | **Standardize on "GPS for Human Health"** | Majority usage; one string everywhere |
| D9 | Therapeutic citations | **Restore from git as an evidence appendix to ACCESSIBILITY.md** | Puts the science back under the calm rules |

## 5. Sources

`raw_vocabulary_alignment.md`, `raw_neurodiverse_research_inventory.md`, `raw_profiles_usecases_critique.md`, `raw_artifact_pack_spec.md` (all in `02_review/`); prior evaluations `V11_EXPORT_EVALUATION` and `V11.1_EXPORT_EVALUATION`.
