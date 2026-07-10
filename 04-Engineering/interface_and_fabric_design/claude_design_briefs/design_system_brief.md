# Claude Design Brief: Cytognosis Design System

> Read this brief end-to-end before producing or revising the Cytognosis Design System.
> The Cytognosis Design System lives authoritatively in Claude Design. Cytognosis backs it up in `branding` for offline use, human-readable browsing, and consumption by repos that cannot reach Claude Design (CI, downstream apps at build time).

## 1. Context

Cytognosis is a nonprofit foundation building a cellular-intelligence platform for disease interception. The Design System dresses every Cytognosis surface: phone apps (interviewer agent), web dashboards, desktop tools, browser extensions, slide decks, grant submissions, internal documentation. Every artifact you produce here is consumed by at least two distinct contexts (often more), so portability and discipline matter more than visual flourish.

Tone the design system should embody: **clinical, calm, respectful, alive**. Not corporate. Not aggressively medical. Not playful. Read like a thoughtful clinician who happens to be a designer.

The Design System should reflect that Cytognosis serves patients, clinicians, and researchers in equal measure. A patient encountering it should feel safe; a clinician should trust it; a researcher should find it precise. Avoid anything that prioritizes one of those three at the expense of the others.

## 2. Mandatory artifacts

Every revision of the Design System must include all of the following. If an artifact already exists, update it; do not skip.

### 2.1 Tokens (DTCG format)

**Mandatory.** Output design tokens following the [W3C Design Tokens Community Group](https://design-tokens.github.io/community-group/format/) specification in JSON. Tokens are the single source of truth that every template and every brand-aligned asset references.

Required token categories:

- `color/` (palette + semantic aliases)
- `typography/` (font families, scales, weights, line-heights, letter-spacing)
- `spacing/` (4px-based scale: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96)
- `radius/` (corner radii: 0, 2, 4, 8, 12, 16, 24, full)
- `motion/` (durations + easing curves)
- `elevation/` (shadow tokens for depth)
- `border/` (border weights + styles)
- `breakpoint/` (responsive breakpoints for the web template)

Token naming **must be semantic first, physical second**. Semantic tokens reference physical tokens. Example:

```json
{
  "color": {
    "physical": {
      "indigo": { "500": { "$value": "#5B6CFF", "$type": "color" } }
    },
    "semantic": {
      "surface": {
        "empathic": {
          "calm":   { "$value": "{color.physical.indigo.100}", "$type": "color" },
          "active": { "$value": "{color.physical.indigo.500}", "$type": "color" }
        }
      }
    }
  }
}
```

Naming rules:

- Lowercase, dot-namespaced.
- Semantic tokens use role names: `surface`, `text`, `action`, `feedback`, `state`, `border`.
- Components do not introduce new tokens; they consume semantic tokens.
- Brand-specific tokens live under `color.physical.cytognosis.*`.
- Crisis or safety-related colors live under `color.semantic.feedback.crisis.*` and are subject to a stricter contrast budget.

### 2.2 Typography system

**Mandatory.** A complete typography scale aligned to the spacing grid.

Output:

```
design-system/typography/
├── families.json          (Sans, Mono, optional Display)
├── scale.json             (XS, SM, BASE, LG, XL, 2XL, 3XL, 4XL, 5XL, 6XL with size + line-height + tracking)
├── weights.json           (300, 400, 500, 600, 700; usage guidance for each)
└── pairings.md            (which size pairs with which on each surface)
```

Font choice constraint: **at most one paid foundry license**. Open-source fonts (Inter, Source Sans, Atkinson Hyperlegible) are strongly preferred because Cytognosis is open-source and grant-funded. If a paid family is recommended, justify it in `pairings.md` and propose an open-source fallback.

Body text minimum size: 16px on web/desktop, 17pt on phone, never smaller. Patient-facing surfaces use 18px / 18pt minimum.

### 2.3 Color system

**Mandatory.** A palette plus semantic aliases that satisfies WCAG 2.1 AA for normal text (4.5:1) and AAA for body text on patient-facing surfaces (7:1).

Output:

```
design-system/color/
├── palette.json           (physical tokens, 10-step scale per hue)
├── semantic.json          (semantic aliases for surface/text/action/feedback/state/border)
├── crisis.json            (crisis-state colors with stricter contrast budget)
├── contrast-matrix.json   (computed contrast ratio for every text/surface combination)
└── usage.md               (when to use each semantic role; what NOT to do)
```

Special requirements:

- Every semantic surface token must have a paired text token, and the pair must meet the contrast budget. If it does not, the pair is invalid and must not be exported.
- Crisis colors must be perceptible to deuteranopes and protanopes; include a colorblind-simulation grid in `crisis.json` documentation.
- Brand color is anchored but not dominant. Patient-facing surfaces lean cooler and quieter than brand-marketing surfaces. Produce two palette modes: `clinical` (default) and `marketing` (for slides and website).

### 2.4 Iconography

**Mandatory.** A consistent icon set, SVG-first, organized by domain.

Output:

```
design-system/iconography/
├── voice/                 (vad-active, listening, speaking, repair, paused, ...)
├── hub/                   (asset, document, note, citation, ...)
├── agent/                 (agent-thinking, tool-use, escalation, ...)
├── data/                  (chart, metric, alert, normal, ...)
├── status/                (success, warning, error, info, crisis, ...)
├── nav/                   (home, back, settings, search, ...)
├── index.json             (manifest of every icon with metadata)
└── guidelines.md          (sizing, alignment, color-from-tokens rules)
```

Per-icon constraints:

- Stroke-based, 1.5px stroke at 24px viewbox.
- 24px and 16px sizes shipped per icon (16px optimized for clarity at small size).
- Color via `currentColor` so consumers can paint with a semantic token.
- Filenames kebab-case: `voice-active.svg`, not `voiceActive.svg`.
- No raster icons. No flat-color overlays. No drop shadows.

### 2.5 Motion

**Mandatory.** Duration and easing tokens, plus motion patterns for the recurring interactions.

Output:

```
design-system/motion/
├── durations.json         (instant 0ms, micro 80ms, fast 160ms, base 240ms, slow 320ms, deliberate 480ms)
├── easings.json           (standard, decelerate, accelerate, emphasized; cubic-bezier values)
├── patterns/
│   ├── enter-exit.md
│   ├── focus.md
│   ├── voice-listening.md (the "calm pulse" pattern for the listening state)
│   ├── voice-speaking.md
│   ├── crisis-attention.md
│   └── reduced-motion.md  (mandatory: what every pattern degrades to under prefers-reduced-motion)
```

Reduced-motion is non-negotiable: every motion pattern documents its reduced-motion variant, which must convey the same information through change-of-state rather than animation.

### 2.6 Voice and tone

**Mandatory.** Rules for the language Cytognosis surfaces use.

Output:

```
design-system/voice-and-tone/
├── voice.md               (the core voice attributes; 5 to 7 attributes max)
├── tone-by-context.md     (calm/clinical for routine; warm/anchored for crisis; precise for research)
├── microcopy-patterns/
│   ├── empty-states.md
│   ├── errors.md
│   ├── confirmations.md
│   ├── consent.md         (mandatory; consent text is high-stakes)
│   ├── crisis-rails.md    (mandatory; crisis copy is highest-stakes)
│   └── voice-agent-turns.md (turn-taking cues, repair, backchanneling)
└── lexicon.md             (preferred / avoided terms; e.g., "patient" preferred over "user")
```

Voice rules that must appear in `voice.md` (you may add more, but these are required):

1. Cytognosis does not say "user". It says "patient", "clinician", "researcher", "you", or a specific role.
2. Cytognosis does not promise. It commits or it abstains.
3. Cytognosis does not infantilize. Plain language, not childlike language.
4. Cytognosis names crisis directly when present. It does not euphemize.
5. Cytognosis is honest about uncertainty. Confidence words match the underlying probability.
6. No em dashes anywhere.

### 2.7 Accessibility budget

**Mandatory.** A document that any consumer can run a design against.

Output:

```
design-system/accessibility-budget.md
```

Required sections:

- Contrast minimums per surface category.
- Touch / pointer target sizes (44pt phone, 24px web standard, 32px patient-facing).
- Keyboard navigation expectations (focus order, focus styles, skip links).
- Screen reader expectations (semantic HTML, aria-* annotations, live regions).
- Motion: prefers-reduced-motion handling.
- Color independence: no information conveyed by color alone.
- Time independence: no forced timeouts on patient-facing flows; explicit extend or pause controls.
- Reading level: target 8th-grade reading level for patient-facing copy; flesch-kincaid target ≤ 70.

### 2.8 Component contracts (not implementations)

**Mandatory.** Platform-agnostic *contracts* for every recurring component. The contracts define props, states, events, accessibility expectations; the template repos implement them in their own framework.

Output:

```
design-system/components/
├── button.contract.yaml
├── input.contract.yaml
├── toggle.contract.yaml
├── modal.contract.yaml
├── toast.contract.yaml
├── card.contract.yaml
├── nav.contract.yaml
├── voice-affordance.contract.yaml  (the listen/talk/repair surface for voice agents)
├── crisis-banner.contract.yaml     (high-stakes; tighter contract)
├── consent-prompt.contract.yaml    (high-stakes; tighter contract)
└── README.md
```

Contract schema (LinkML-style YAML, one file per component):

```yaml
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

### 2.9 Human-readable docs (rendered)

**Mandatory.** Render the entire Design System as a navigable Markdown / HTML doc for the branding backup. This is what readers without Claude Design access see.

Output:

```
design-system/_rendered/
├── index.html
├── tokens.html
├── typography.html
├── color.html
├── iconography.html
├── motion.html
├── voice-and-tone.html
├── accessibility.html
├── components.html
└── assets/                (icon SVGs, font samples, palette swatches inlined)
```

The rendered docs are self-contained (single-folder, no external CDN dependencies). Use system fonts as fallbacks. Make them printable at A4 / Letter without page-break disasters.

### 2.10 Skill manifest

**Mandatory.** The Design System ships a `skills/manifest.yaml` describing the Cytognosis-wide skills that anyone (humans or agents) can invoke. These are the brand-phase skills referenced by the four-phase skill model.

Required skill entries:

- `brand-review` (review any output against the voice and tone rules; flag deviations)
- `tone-check` (validate tone of a draft against the target tone-by-context)
- `accessibility-audit` (run the accessibility budget against a draft)
- `contrast-check` (validate any text/surface color combination)
- `microcopy-validate` (validate microcopy against the relevant pattern)
- `reading-level-check` (compute reading level against the target)

Each skill is a directory under `skills/` with a `SKILL.md` describing inputs, outputs, and behavior.

## 3. Optional artifacts

Include where they add real value, omit if they would dilute.

- **Brand mark variations** beyond the primary logo (monochrome, single-color, social avatar). Only if Cytognosis has commissioned the logomark; do not invent.
- **Illustration system** (custom illustrations for empty states, onboarding, education). Only if the budget justifies; default is photography-free abstraction using tokens.
- **Photography guidelines** (when photography is permitted, what kinds, where it appears).
- **Sound design tokens** (UI sound effects, voice-agent earcons). Probably out of scope for first revision; add later when voice UX matures.
- **Slide-deck template** that consumes the tokens. High value for grants; add as a separate "marketing" track.
- **Email template** that consumes the tokens. Useful for transactional and newsletter mail; add when communications grow.

## 4. Folder layout (top of design-system/)

```
design-system/
├── README.md                       (one-page overview; entry point)
├── tokens/                         (DTCG JSON; mandatory)
│   ├── color/
│   ├── typography/
│   ├── spacing.json
│   ├── radius.json
│   ├── motion/
│   ├── elevation.json
│   ├── border.json
│   └── breakpoint.json
├── color/                          (mandatory; documentation + matrix)
├── typography/                     (mandatory)
├── iconography/                    (mandatory)
├── motion/                         (mandatory)
├── voice-and-tone/                 (mandatory)
├── accessibility-budget.md         (mandatory)
├── components/                     (mandatory; contracts only)
├── _rendered/                      (mandatory; HTML output)
├── skills/                         (mandatory; skill manifest + skills)
├── _illustrations/                 (optional)
├── _photography/                   (optional)
├── _slides/                        (optional)
└── _email/                         (optional)
```

## 5. Naming and styling conventions for output files

### 5.1 Filenames

- Lowercase, kebab-case: `voice-active.svg`, `crisis-attention.md`.
- Singular when describing a thing (`button.contract.yaml`); plural only when describing a collection (`microcopy-patterns/`).
- Use the `.contract.yaml` suffix for component contracts.
- Use the `.md` suffix for human-readable docs; the `.html` outputs go under `_rendered/`.
- Underscore-prefixed folders are optional or rendered-output (`_rendered/`, `_illustrations/`).

### 5.2 Token names

- Dot-namespaced semantic path: `color.semantic.surface.empathic.calm`.
- Lowercase only. No camelCase. No PascalCase.
- Numbers permitted only inside scale steps (`color.physical.indigo.500`).
- Variants in curly braces are placeholders documenting the schema (e.g., `color.semantic.action.{variant}.surface`); concrete tokens substitute the variant.

### 5.3 Document styling

- Plain Markdown with a small allowance for HTML where Markdown cannot express layout (color swatches, contrast tables).
- Every Markdown file starts with a one-sentence summary on the first line, blank line, then a one-paragraph "what's in here" before the first H2.
- Code blocks fenced with the language tag (` ```json `, ` ```yaml `, ` ```md `).
- Tables for matrices; lists for rules; prose for the why.
- No em dashes anywhere.

### 5.4 HTML render styling

- Single CSS file embedded in `<head>`, referencing nothing external.
- Use the Design System's own typography and color tokens to style the docs (the docs are the first product of the Design System).
- Tables with zebra striping. Code blocks monospace at 14px. Headings on the typography scale, not arbitrary sizes.
- A small TOC at the top of each page. No global navigation; pages link to each other inline.
- Print-friendly: page break before each H1; avoid orphans on H2.

## 6. Versioning and update protocol

Design System version follows semver:

- **Patch** (`v1.2.3 → v1.2.4`): no behavior change; typo fixes, doc refinements, additional optional artifacts. No downstream PRs are forced.
- **Minor** (`v1.2.3 → v1.3.0`): additive changes; new tokens, new components, new icons, new microcopy patterns. Downstream PRs are auto-opened but non-breaking.
- **Major** (`v1.2.3 → v2.0.0`): breaking changes; renamed tokens, removed components, altered semantic meanings, palette overhaul. Ship `MIGRATION.md` alongside the new export.

Every revision writes:

- `CHANGELOG.md` entry (top of file; Conventional-Commits style summary).
- A signed Git tag.
- The full export as a single tarball plus the per-folder structure above.

## 7. Sync to branding

The Cytognosis side runs `nox -s sync-from-claude-design` in `branding`. The expected sync inputs:

- The full `design-system/` folder (above).
- A `CHANGELOG.md` since the last sync.
- A `version` string (semver).

The sync writes:

- The full `design-system/` tree into `branding/design-system/`.
- The voice-and-tone tree into `branding/voice-and-tone/`.
- The skill manifest and skills into `branding/skills/`.
- A `SYNC_STATUS.md` recording the version and timestamp.

If the sync detects manual edits inside `branding/design-system/`, it surfaces them as a merge conflict rather than overwriting. branding's CI fails if a sync is overdue (configurable; default 14 days).

## 8. Definition of done for a Design System revision

Before declaring a revision complete:

1. All mandatory artifacts above are present and parseable.
2. Every contrast pair satisfies its budget; the matrix is regenerated.
3. The full Markdown / HTML render is produced and the `_rendered/index.html` opens with no broken links.
4. The skill manifest validates against `cytos.schema.SkillManifest`.
5. No em dashes anywhere in any output.
6. The `CHANGELOG.md` reflects the changes.
7. The version is bumped according to semver.

## 9. What to NOT produce

To keep the Design System lean:

- Do not produce mockups of specific products. That is the templates' job.
- Do not produce framework-specific implementations of components. The component contracts define the contract; the four templates implement them.
- Do not produce one-off illustrations for specific campaigns. Those live in the campaign's own folder.
- Do not introduce new tokens for one component. Components consume existing semantic tokens; if no semantic token fits, the answer is to add the semantic alias, not invent a component-local token.
- Do not include raw model outputs or research notes. The Design System is the polished surface; research lives elsewhere.

## 10. Open questions for the Cytognosis team

When you hit any of these, pause and ask before deciding:

1. Brand mark: does Cytognosis have a commissioned logomark we should incorporate, or do we operate without one until commissioned?
2. Display typeface: license budget and preference (open-source default vs licensed)?
3. Primary brand color in the `clinical` palette mode: is the current indigo-leaning anchor confirmed, or is the brand color being revisited?
4. Patient-facing minimum reading level: 8th-grade is the recommendation; confirm or override.
5. Sound: is voice-agent earcon design in scope for this revision?
