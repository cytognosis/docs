# Claude Design Prompt: Design System Reorganization

> Paste this prompt into Claude Design when you want it to reorganize the current `/design/` output into the production-ready shape expected by the Cytognosis branding repo. This is a one-time consolidation pass.
> Cytognosis context: target shape lives at `design-system-consolidation-2026-05/02_repo_organization/branding_repo_plan.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_reorg.md`
> **Changes**: updated mapping table to reflect current branding repo structure, noted `design-system/` now populated with profiles, tokens, components, preview, and data-viz content. Replaced `cytognosis-design-system-master` with `cytognosis-branding`. Updated profile references from 4 to 6 profiles (added Companion, Crisis). Removed em dashes.

---

## Brief

The current Claude Design output has accreted three overlapping versions of the same content: (1) the top-level Design System at `/design/`, (2) a `branding/` subfolder that mirrors much of it for the production branding skill, (3) an `uploads/brand/` carrying earlier-version drafts. This needs to consolidate into one canonical shape that the Cytognosis branding repo expects.

Reorganize, deduplicate, and ship a single tree under `/design/branding-export/` matching the target layout below. After this lands, the existing `/design/branding/`, `/design/uploads/`, and the duplicated top-level files can be retired.

**Note**: The `design-system/` directory is now populated with profiles, tokens, components, preview cards, and data-viz content. The mapping below reflects this current state.

## 1. Target layout (matches the Cytognosis production `branding/design-system/`)

```
branding-export/
├── README.md                   (one entry-point; tagline; promise; product map)
├── CHANGELOG.md
├── VERSION                     (string, e.g. "10.0.0")
├── LOGO.md                     (canonical logo guide)
├── WRITING.md                  (voice and tone; per-profile dials)
├── IMAGERY.md                  (photography + illustration tone)
├── ACCESSIBILITY.md            (WCAG audit)
├── CONTRIBUTING.md             (how to contribute changes)
│
├── tokens.css                  (the single canonical CSS variables file; merged from colors_and_type.css)
│
├── references/                 (the 12 v10 numbered references; deep content)
│   ├── 01_brand_foundation.md
│   ├── 02_voice_and_tone.md
│   ├── 03_logo.md
│   ├── 04_color_system.md
│   ├── 05_typography.md
│   ├── 06_iconography.md
│   ├── 07_imagery.md
│   ├── 08_motion.md
│   ├── 09_layout.md
│   ├── 10_templates.md
│   ├── 11_accessibility.md
│   └── 12_dataviz.md
│
├── profiles/
│   ├── README.md
│   ├── profiles.css            (the six-profile overlay tokens)
│   ├── foundation.md
│   ├── clinical.md
│   ├── research.md
│   ├── lab.md
│   ├── companion.md            (NEW: ND-first daily use profile)
│   ├── crisis.md               (NEW: emergency/safety profile)
│   ├── a11y.css
│   ├── motion.css
│   ├── states.css
│   ├── dataviz.css
│   ├── _comparison.html        (the 6-up side-by-side; per prompt_profiles)
│   └── examples/
│       ├── foundation.html
│       ├── clinical.html
│       ├── research.html
│       ├── lab.html
│       ├── companion.html
│       └── crisis.html
│
├── assets/
│   ├── logos/
│   │   ├── cytognosis-light.svg
│   │   ├── cytognosis-light.png
│   │   ├── cytognosis-dark.svg
│   │   ├── cytognosis-dark.png
│   │   ├── cytognosis-mark.svg
│   │   ├── cytognosis-mark.png
│   │   └── cytognosis-mark-square.svg
│   ├── icons/
│   │   ├── line/<icon-id>.svg              (one file per icon)
│   │   ├── solid/<icon-id>.svg             (one file per icon)
│   │   ├── _bundle-line.svg                (consolidated sprite)
│   │   ├── _bundle-solid.svg               (consolidated sprite)
│   │   ├── index.json                      (manifest of every icon)
│   │   └── _gallery.html                   (rendered visual review)
│   ├── products/
│   │   ├── cytoverse.png
│   │   ├── cytoscope.png
│   │   ├── cytonome.png
│   │   └── helix-model.png
│   └── fonts/
│       └── README.md                       (production stack; self-hosted files when licensed)
│
├── templates/
│   ├── deck/                               (12-layout deck template; light + dark)
│   │   ├── index.html
│   │   ├── theme.css
│   │   └── deck-stage.js
│   ├── one-pager.html                      (US Letter research brief, print-ready)
│   ├── email-signature.html                (full + compact)
│   ├── social-cards.html                   (Open Graph 1200×630 + square 1080×1080)
│   └── README.md
│
├── components/                             (platform-agnostic contracts; LinkML-style YAML)
│   ├── README.md
│   ├── button.contract.yaml
│   ├── input.contract.yaml
│   ├── toggle.contract.yaml
│   ├── modal.contract.yaml
│   ├── card.contract.yaml
│   ├── nav.contract.yaml
│   ├── voice-affordance.contract.yaml
│   ├── crisis-banner.contract.yaml
│   ├── consent-prompt.contract.yaml
│   ├── profile-switcher.contract.yaml      (NEW: data-profile toggling)
│   ├── density-control.contract.yaml       (NEW: compact/comfortable/spacious)
│   ├── font-toggle.contract.yaml           (NEW: Inter/Lexend/Atkinson/OpenDyslexic)
│   └── motion-toggle.contract.yaml         (NEW: motion preference control)
│
├── preview/                                (rendered design-system cards)
│   ├── index.html
│   ├── brand-hero.html
│   ├── brand-logos.html
│   ├── brand-icons.html
│   ├── brand-imagery.html
│   ├── brand-products.html
│   ├── colors-identity-triad.html
│   ├── colors-primary-scales.html
│   ├── colors-secondary.html
│   ├── colors-accent-scales.html
│   ├── colors-gradients.html
│   ├── colors-semantic.html
│   ├── colors-neutrals-light.html
│   ├── colors-neutrals-dark.html
│   ├── type-display.html
│   ├── type-body.html
│   ├── type-accent-code.html
│   ├── type-accessibility.html
│   ├── components-buttons.html
│   ├── components-badges.html
│   ├── components-cards.html
│   ├── components-forms.html
│   ├── spacing-scale.html
│   ├── spacing-radii.html
│   ├── spacing-shadows.html
│   ├── writing-kit.html
│   ├── logo-usage.html
│   ├── dataviz-kit.html
│   ├── ui-website.html
│   └── governance.html
│
└── data-viz/
    ├── README.md
    ├── sequential.css
    ├── diverging.css
    └── patterns/                           (colorblind-safe pattern fills)
        └── README.md
```

## 2. Mapping from current state to target

| Current path | Action | Target path |
|---|---|---|
| `/design/README.md` | merge | `branding-export/README.md` |
| `/design/CHANGELOG.md` | move | `branding-export/CHANGELOG.md` |
| `/design/VERSION` | move | `branding-export/VERSION` |
| `/design/LOGO.md` | move | `branding-export/LOGO.md` |
| `/design/WRITING.md` | move | `branding-export/WRITING.md` |
| `/design/IMAGERY.md` | move | `branding-export/IMAGERY.md` |
| `/design/ACCESSIBILITY.md` | move | `branding-export/ACCESSIBILITY.md` |
| `/design/CONTRIBUTING.md` | move | `branding-export/CONTRIBUTING.md` |
| `/design/SKILL.md` | discard | (skills live in the production branding repo, not in the design export) |
| `/design/colors_and_type.css` | rename + move | `branding-export/tokens.css` |
| `/design/branding/references/01_*.md` through `12_*.md` | move (12 files) | `branding-export/references/` |
| `/design/branding/assets/css/cytognosis-tokens.css` | discard | (duplicate of `/design/colors_and_type.css`) |
| `/design/branding/assets/logos/*` | merge | `branding-export/assets/logos/` (canonical set, deduplicated against `/design/assets/logos/`) |
| `/design/branding/assets/icons/{light,dark}/` | move + rename | `branding-export/assets/icons/{line,solid}/` (rename to canonical pair semantics) |
| `/design/branding/assets/products/*` | move | `branding-export/assets/products/` |
| `/design/branding/templates/deck/` | move | `branding-export/templates/deck/` |
| `/design/branding/templates/email-signature.html` | move | `branding-export/templates/email-signature.html` |
| `/design/branding/SKILL.md` | discard | (skills live in production branding repo) |
| `/design/profiles/profiles.css` | move + extend | `branding-export/profiles/profiles.css` (add Companion + Crisis overlay tokens) |
| `/design/profiles/README.md` | move + update | `branding-export/profiles/README.md` (update for 6 profiles) |
| `/design/profiles/{FoundationExample,...}.jsx` | export to static HTML | `branding-export/profiles/examples/{foundation,...,companion,crisis}.html` |
| `/design/profiles/{a11y,dataviz,motion,states}.css` | move | `branding-export/profiles/` |
| `/design/profiles/Profile explorations.html` | move | `branding-export/profiles/examples/_explorations.html` |
| `/design/profiles/{design-canvas.jsx,App.jsx}` | discard | (canvas runtime; not for distribution) |
| `/design/assets/icons/cytognosis-icons-{line,solid}.svg` | move | `branding-export/assets/icons/_bundle-line.svg`, `_bundle-solid.svg` |
| `/design/assets/logos/*` | merge | `branding-export/assets/logos/` (deduplicate) |
| `/design/assets/products/*` | merge | `branding-export/assets/products/` |
| `/design/assets/Helix_model_logo.png` | rename + move | `branding-export/assets/products/helix-model.png` |
| `/design/templates/*` | move | `branding-export/templates/` |
| `/design/components/Components.jsx` | export to LinkML contracts | `branding-export/components/*.contract.yaml` (component-by-component) |
| `/design/preview/*` | move | `branding-export/preview/` |
| `/design/ui_kits/website/*` | discard | (this lives in the website repo, not the design system) |
| `/design/uploads/*` | discard | (working artifacts) |
| `/design/_debug/` | discard | |
| `/design/.design-canvas.state.json` | discard | |
| `/design/index.html` | discard | (canvas state) |

## 3. Deduplication priorities

Three deduplications matter:

1. **Tokens**: `/design/colors_and_type.css` and `/design/branding/assets/css/cytognosis-tokens.css` are the same content. Keep the top-level one (more comprehensive), promote to `branding-export/tokens.css`, discard the other.
2. **Logos**: `/design/assets/logos/` and `/design/branding/assets/logos/` overlap heavily. The `branding/` subfolder is the cleaner set (with `cytognosis-mark-square.svg`); promote that to `branding-export/assets/logos/`, discard the top-level duplicates.
3. **Products**: same as logos. Use the `branding/` subfolder version.

## 4. Promotion list

Files that are currently in the `/design/branding/` subfolder but are **actually** the canonical version and should be promoted:

- The 12 numbered references (these are the v10 production references).
- `branding/templates/deck/` (the production deck template).
- `branding/templates/email-signature.html` (the production signature).
- `branding/assets/logos/cytognosis-mark-square.svg` (only exists in `branding/`; promote).
- `branding/assets/products/*.png` (cleaner cropping than the top-level versions).

Files that are currently at the top level of `/design/` but ARE the canonical version:

- `LOGO.md`, `WRITING.md`, `IMAGERY.md`, `ACCESSIBILITY.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `VERSION`. These are the production governance docs.
- `colors_and_type.css` (promote to `tokens.css`).
- `templates/{one-pager.html, social-cards.html}` (only at top level).
- `preview/*` (top level is the comprehensive set).

## 5. Component contracts (NEW; export from JSX)

The current `/design/components/Components.jsx` is a React component reference. The production Cytognosis Design System uses platform-agnostic **component contracts** authored as LinkML-style YAML so each interface template can implement them in its own framework.

For each component in `Components.jsx`, produce a `*.contract.yaml` at `branding-export/components/`:

```yaml
# branding-export/components/button.contract.yaml
component: button
states: [default, hover, focus, active, disabled, loading]
variants: [primary, secondary, ghost, danger, crisis]
props:
  - name: label
    type: string
    required: true
  - name: icon
    type: icon-id
    required: false
  - name: variant
    type: enum
    values: [primary, secondary, ghost, danger, crisis]
    default: primary
events: [press, longPress]
accessibility:
  role: button
  focusable: true
  keyboard: [Enter activates, Space activates]
  aria_label_required_when: icon-only
contrast_budget:
  text_on_surface: 4.5
size:
  min_target_pt: 44
tokens_consumed:
  - color.semantic.action.{variant}.surface
  - color.semantic.action.{variant}.text
  - radius.small
  - typography.scale.base
  - motion.duration.fast
  - motion.easing.standard
```

Produce contracts for the components in §6 of the brief, with the components already in `Components.jsx` covered first. Include the four new ND-specific contracts: profile-switcher, density-control, font-toggle, and motion-toggle.

## 6. What to NOT carry over

These should NOT be in the final export:

- The `/design/SKILL.md` and `/design/branding/SKILL.md` (skills are in the production branding repo, not in the design export).
- Any UI kit code (`/design/ui_kits/website/`).
- Working artifacts in `/design/uploads/` and `/design/_debug/`.
- Canvas state files (`.design-canvas.state.json`, `index.html` if it is just canvas state).
- Older versioned drafts in `/design/uploads/brand/references/0[12345678]_*.md`.

## 7. Voice rules during this reorganization

The reorganization is content-preserving. Do not rewrite copy during the move. Voice changes are a separate revision; this is a structural pass.

One exception: any em dashes encountered during the move get replaced with commas, semicolons, or restructured sentences. This is a hard Cytognosis rule and applies to every file shipped.

## 8. Deliverables to ship back

1. The complete `branding-export/` tree at the target layout above.
2. A `branding-export/MIGRATION.md` describing the changes for the Cytognosis team's review: what moved where, what was discarded, what was deduplicated.
3. A `branding-export/MANIFEST.json` listing every file in the export with its size, last-modified timestamp, and a one-line description.
4. A `branding-export/SYNC_STATUS.md` recording the version (10.0.0) and the export timestamp.

## 9. Process

1. Stage the new tree at `branding-export/` without modifying anything in `/design/` or `/design/branding/`. This is non-destructive.
2. For each file in the mapping (§2), copy / rename / merge into `branding-export/`.
3. For the JSX components, export each as a `.contract.yaml` per §5.
4. For the six profile examples, export the JSX as static HTML.
5. Write `MIGRATION.md`, `MANIFEST.json`, `SYNC_STATUS.md`.
6. Hand back the full export for Cytognosis team review before they merge into the production branding repo.

## 10. Open questions to surface back to Cytognosis

1. Should the existing `/design/branding/` subfolder be deleted from Claude Design after this consolidation, or kept as historical reference? Recommendation: keep until v10.1 lands.
2. Should `/design/uploads/brand/references/` (earlier-version drafts) be archived in Cytognosis's `branding/archive/` or fully discarded? Recommendation: archive; they have salvageable content.
3. The UI kit at `/design/ui_kits/website/` is a recreation of cytognosis.org. Should it stay in Claude Design as a working artifact, move to the website repo, or be discarded? Recommendation: move to the website repo as a reference build.
4. Are there licensed font files to be uploaded (Inter, Newsreader, JetBrains Mono, Atkinson Hyperlegible, Lexend, OpenDyslexic self-hosted)? Until they are, `branding-export/assets/fonts/README.md` documents the production stack but ships no files.
5. Should the four new component contracts (profile-switcher, density-control, font-toggle, motion-toggle) ship in this pass or in a separate ND-focused revision? Recommendation: ship in this pass so the structural reorganization is complete.
