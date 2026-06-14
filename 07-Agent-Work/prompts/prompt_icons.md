# Claude Design Prompt: Iconography Revision

> Paste this prompt into Claude Design when you want to iterate on the Cytognosis icon set. The current v10 set has 48 icons in 7 categories but only the categories are settled; many glyphs are placeholders that need targeted refinement.
> Cytognosis context: see the cytognosis-branding skill (this is upstream of that skill).

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_icons.md`
> **Changes**: replaced `cytognosis-design-system-master` with `cytognosis-branding`, added 8 new ND-specific icons (calm-mode, focus-timer, body-double, streak, mood-ring, pause-day, brain-weather, gentle-nudge), removed em dashes.

---

## Brief

Revise the Cytognosis icon set with concrete refinements per category, ship in the two canonical variants (line + solid), and ship per-media renditions (web, phone, slides, docs, favicon). The current set is preliminary; this revision moves it to production grade.

## 1. Scope

Produce a refreshed iconography bundle covering:

1. The 48 existing icons with refinements to the placeholders flagged below.
2. ~10 new icons in the voice / crisis / sensor categories where coverage is currently thin.
3. **8 new ND-specific icons** for the Companion profile and neurodivergent-facing surfaces (see §2.7).
4. Two canonical variants per icon: **line** (the v10 default) and **solid** (filled fluorophore duotone).
5. Per-media renditions for each variant (sizes optimized per surface).
6. Light-mode and dark-mode variants where relevant.
7. The consolidated `<symbol>` sprite bundles per variant.
8. An updated `branding/design-system/references/06_iconography.md` reflecting the final spec.

## 2. Categories with worked examples (priority order)

### 2.1 Voice and paralinguistic (NEW; ~6 icons)

These do not exist in v10 and are needed for the patient interviewer agent and any voice surface:

- `vad-active`: the small circular indicator showing voice activity detection is running.
- `listening`: the agent is listening for user speech. The calm-pulse companion glyph; use violet-300 stroke; the icon is the stationary mark and the pulse is in motion CSS, not in the SVG.
- `speaking`: the agent is speaking. A waveform-derived shape (not literal). 3-5 waveform peaks, asymmetric, sized within the 24×24 viewBox.
- `repair`: the agent is requesting clarification ("Sorry, can you say that again?"). A subtle circular-arrow + question-mark combination.
- `paused`: voice loop is paused (microphone off). Standard pause glyph but with the Cytognosis stroke weight + radius.
- `backchannel`: the agent's low-intrusion acknowledgment cue (a small dot or breath-like mark to signal the agent is tracking the user's turn).

### 2.2 Crisis and safety (NEW; ~4 icons)

The crisis rail is a first-class Cytognosis subsystem and needs its own glyph family:

- `alert-radar`: refresh of v10 radar with a clearer "incoming signal" feel. Use coral-600 stroke for line; coral-600 + magenta-300 fill for solid.
- `safety-resources`: an icon for the patient-facing safety-resources surface. Conveys "help available". Not a generic shield. Suggest: hands cupping a small light, or a phone with a lifeline.
- `escalation`: the visual for "this is being routed to a higher tier or a human". Two stepped arrows or a tier-handoff visual.
- `pause-mid-flow`: a glyph for "let us pause this and revisit later", used in patient flows under stress.

### 2.3 Sensing, GPS, radar (REFINE; existing 6 icons)

The current 6 (`sensor`, `radar`, `gps-marker`, `wave-signal`, `beacon`, `wearable`) need glyphs that read distinctly at 16px:

- `sensor`: currently generic; revise to imply biosensor specifically. Suggest: a microchip outline with a cellular nucleus inside.
- `wearable`: the watch glyph is fine; add a heart-pulse trace overlay to distinguish from a regular smartwatch.
- `beacon`: distinguish from `radar` by emphasizing emission outward (radiating dots).
- `gps-marker`: keep the pin shape but add a small cellular detail at the apex to land the Cytognosis identity.

### 2.4 Equity and people (REFINE; existing 4 icons)

The current 4 (`community`, `global-access`, `person-card`, `equity`) need richer representation across age, ability, ethnicity:

- `community`: a small cluster of figures, varied silhouettes (one with a walking aid, one shorter, one with hair texture indicating diversity, one in profile).
- `global-access`: a globe with a dotted-line pattern of access pathways (not all radiating from a single center).
- `person-card`: a profile card with the cellular-glyph identity element on the avatar.
- `equity`: scales of justice, but balanced (the current v10 may show imbalance which reads as inequity, not equity).

### 2.5 Cell and molecular biology (KEEP, with minor refinements; 10 icons)

These read well. Optional refinement:

- `genome` and `dna-strand` overlap visually; consider rendering `dna-strand` as a single strand (vs the double helix) so the pair distinguishes cleanly.

### 2.6 Healthcare and medicine, AI and ML, Networks and graph, Time and process

Keep the v10 versions. Re-render in the canonical pair (line + solid) and per-media if not already done.

### 2.7 Neurodivergent and companion (NEW; 8 icons)

These icons support the Companion profile and ND-facing surfaces. They use warm, approachable metaphors and avoid clinical or technical imagery:

- `calm-mode`: a soft wave or ripple pattern suggesting calm. Use teal-300 stroke. Conveys "entering a calmer state." Not a meditation symbol.
- `focus-timer`: a simplified clock face with a single wedge highlighted (not a full stopwatch). Suggests time-bounded focus without pressure. Use azure-300 stroke.
- `body-double`: two figures side by side, one slightly transparent or outlined, suggesting companionship during work. Use violet-300 stroke. Conveys "working alongside someone."
- `streak`: a small flame or sequential dots suggesting continuity. Use magenta-300 stroke. Conveys "you kept going." Not a fire emoji; stylized within the Cytognosis stroke language.
- `mood-ring`: a circular ring with a subtle gradient segment suggesting emotional state. Use violet-300 stroke with a teal-300 accent. Conveys "how you feel matters."
- `pause-day`: a soft pause symbol (two vertical bars) with a small leaf or breath mark. Use teal-300 stroke. Conveys "it is okay to rest."
- `brain-weather`: a simplified cloud or sun shape above a brain outline (abstracted, not anatomical). Use azure-300 stroke. Conveys "your cognitive weather today."
- `gentle-nudge`: a small hand with a soft touch gesture, or a subtle arrow with a rounded tip. Use coral-300 stroke. Conveys "a friendly reminder, not a demand."

Design principles for ND icons:

- Softer stroke weight where possible (1.4px instead of 1.6px) to reduce visual sharpness.
- Rounded, organic shapes preferred over angular geometry.
- Warm 300-shade strokes by default; 600-shade only for the solid variant.
- Each icon must read clearly at 24px and degrade gracefully at 16px.
- Avoid metaphors that imply deficit, disorder, or medical treatment.

## 3. Per-icon style spec (unchanged from v10)

| Property | Value |
|---|---|
| Format | SVG |
| ViewBox | 24 × 24 |
| Stroke (line variant) | 1.6px (1.4px for ND category) |
| Stroke caps and joins | round |
| Fill (line) | none |
| Fill (solid) | duotone (primary shape shade 600, accent detail shade 300) |
| Color via | `currentColor` (line); explicit fluorophore tokens (solid) |

## 4. Canonical variants per icon

Two canonical variants. Retire the 10 numbered style folders (`01_solid_violet`, etc.) from the v9-era; archive them under `branding/archive/2026-pre-v10/icons/` if they hold useful experiments.

| Variant | Use | Color rule |
|---|---|---|
| **Line** | UI dashboards, dense screens, documents, default | semantic stroke via `currentColor`; consumer sets `color:` on parent |
| **Solid** | marketing surfaces, hero compositions, slide covers | shade 600 primary fill + shade 300 accent detail; fluorophore-tinted |

## 5. Light-mode and dark-mode per icon

For each canonical variant, produce two stroke / fill versions where applicable:

- **Light mode** (use on light backgrounds): dark stroke / fill (indigo-700 or violet-700 for the line variant).
- **Dark mode** (use on dark backgrounds): light stroke / fill (violet-300 or white for the line variant).

For the solid variant: the fluorophore duotone reads on both light and dark backgrounds without re-coloring (validated case by case in `branding/design-system/preview/`).

## 6. Per-media renditions

Each icon ships in the right sizes / formats per surface:

| Surface | Sizes | Format | Notes |
|---|---|---|---|
| Web (dashboards, marketing) | 24px | SVG inline | color via `currentColor`; consumer sets color |
| Phone (Flutter) | 24pt @ 1x / 2x / 3x | PNG triplet | bundled in app assets at three densities |
| Slides | 48px | SVG | line for content; solid for cover slides |
| Docs (Word, PDF) | 16px and 24px | SVG | match body font size |
| Favicon | 16 / 32 / 64 | SVG + ICO | for the logo mark only, not the 48-set |
| Open Graph | (composition, not icon) | PNG | uses `templates/social-cards.html` |

## 7. The bundle sprites

Ship two consolidated `<symbol>` sprite SVGs:

- `assets/icons/_bundle-line.svg`: all 48+ icons as `<symbol>` elements, addressable via `<svg><use href="#icon-id"/></svg>`.
- `assets/icons/_bundle-solid.svg`: same structure, solid variant.

Sprite naming: `icon-<id>` where `<id>` is the kebab-case icon name. Example: `<symbol id="icon-cell-membrane" viewBox="0 0 24 24">…</symbol>`.

## 8. Color semantics (carry forward from v10)

| Color | Use |
|---|---|
| Violet 600 / 300 | innovation, AI, default |
| Azure 600 / 300 | data, the patient, input, focus (ND) |
| Indigo 600 / 300 | pioneer, output, foundation |
| Teal 600 / 300 | success, biology, harmony, calm (ND) |
| Coral 600 / 300 | warmth, human, hope, gentle-nudge (ND) |
| Magenta 600 | alerts only (never in the identity triad); streak (ND at 300) |

## 9. What to NOT produce

- No emoji.
- No filled-pictogram variants outside the canonical pair (no glyph styles, no isometric, no 3D, no skeuomorphic).
- No icons without `aria-label` planning (the bundle must include each icon's preferred screen-reader label in `icons/index.json`).
- No drop shadows on icons.
- No recoloring outside the six brand colors.
- No icons that overlap the logo glyph's identity (the cellular "C" glyph is the mark; icons must read distinctly).
- No ND icons that use clinical or pathologizing metaphors.

## 10. Deliverables to ship back

Hand back:

1. The refreshed `branding/design-system/references/06_iconography.md` reflecting the final spec.
2. Per-icon SVGs in `branding/design-system/assets/icons/line/<name>.svg` and `…/solid/<name>.svg`.
3. The consolidated sprite bundles `_bundle-line.svg` and `_bundle-solid.svg`.
4. A `branding/design-system/assets/icons/index.json` manifest listing every icon with: id, name, category, variants present, default `aria-label`, semantic color recommendation, status (production / placeholder).
5. A `branding/design-system/assets/icons/_gallery.html` rendering every icon in both variants on both light and dark backgrounds at 16 / 24 / 48 / 64px for visual review.
6. Per-media exports under `branding/design-system/assets/icons/_exports/`:
   - `web/` (SVG, 24px)
   - `phone/` (PNG @1x/2x/3x at 24pt)
   - `slides/` (SVG, 48px)
   - `docs/` (SVG, 16px + 24px)
   - `favicon/` (SVG + ICO at 16/32/64; mark only)

## 11. Process

Work in this order so the most consequential icons land first:

1. Voice and paralinguistic family (§2.1), needed for the interviewer agent.
2. Crisis and safety family (§2.2), needed for the crisis rail.
3. Neurodivergent and companion family (§2.7), needed for the Companion profile.
4. Refinements to sensing (§2.3) and equity/people (§2.4), current set is weakest here.
5. Re-render the existing 38 in the canonical pair (line + solid) per media.
6. Generate the sprite bundles and the gallery HTML.
7. Update the iconography reference doc.

## 12. Open questions to surface back to Cytognosis

When you hit any of these, pause and ask:

1. The voice-listening icon: pair with motion in CSS (the calm pulse) or include subtle radial-pulse rings inside the SVG itself? Recommendation: motion in CSS so the SVG stays consistent across reduced-motion users.
2. The crisis-safety icon: literal lifeline / hands-cupping-light, or abstract? Cytognosis should sign off on the specific metaphor before rendering.
3. The equity icon: balanced scales, or a different metaphor entirely (e.g., a footbridge across uneven terrain)? Worth a brief discussion.
4. Brand mark in icons: the cellular "C" glyph appears in some current icons (e.g., `cell`, `nucleus`). Should this propagate to product-identity icons in the 48-set, or stay reserved for the logo only? Recommendation: reserve for the logo; icons should not look like logo variants.
5. ND icon stroke weight: 1.4px (softer, recommended for Companion profile) or keep 1.6px for consistency across all categories? Recommendation: 1.4px for the ND category only.
6. The `body-double` icon: is the "two figures" metaphor clear enough, or does it need additional context (e.g., a shared workspace element)? Worth user testing with ND participants.
7. The `brain-weather` icon: is an abstract cloud-over-brain clear, or should it use a more universal metaphor like a weather vane? Recommendation: cloud-over-brain, but test for clarity.
