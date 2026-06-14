# Claude Design Prompt: Profile System Refinement

> Paste this prompt into Claude Design when you want to iterate the six use-case profiles (Foundation, Clinical, Research, Lab, Companion, Crisis) from their current preliminary form to a settled production specification.
> Cytognosis context: see the cytognosis-branding skill, `references/profiles.md`. The six profiles exist in CSS overlay form at `org/design/profiles/profiles.css` plus JSX example surfaces; this revision moves them to production grade.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_profiles.md`
> **Changes**: expanded from 4 to 6 profiles (added Companion and Crisis), replaced `cytognosis-design-system-master` with `cytognosis-branding`, replaced `cytognosis-template-master` with `cytognosis-branding`, removed em dashes, added ADHD/ND-specific instructions.

---

## Brief

Refine the six Cytognosis use-case profiles from their current placeholder form into a settled, production-ready specification. Each profile gets: a confirmed audience, the trigger surfaces, the requirements (density, contrast budget, motion budget), the vibe (one-paragraph emotional register), the typography stack confirmation, the palette emphasis confirmation, and a worked example. Plus a profile-selection decision tree and worked side-by-side examples so the six read as distinct registers.

## 1. The six profiles (current state)

| Profile | Surface (current) | Type stack (current) | Palette emphasis (current) | Voice (current) |
|---|---|---|---|---|
| Foundation | cytognosis.org, decks, social, press | Inter · Newsreader · JetBrains Mono | Signature triad gradient | visionary, hopeful |
| Clinical | patient / consumer app (clinical contexts) | Inter · Source Serif Pro · JetBrains Mono | muted 300-shade pastels | calm, reassuring |
| Research | Cytoverse workbench, dashboards | IBM Plex Sans + Plex Mono | Indigo + magenta alert | precise, neutral |
| Lab | CLI, editor, dev docs, terminal | Recursive (one variable family) | Violet-300 on ink | technical, playful |
| Companion | Yar mobile, daily ND use, gamification | Lexend · Atkinson Hyperlegible · JetBrains Mono | muted 300-shade pastels, cognitive-signal colors | warm, encouraging, grounding |
| Crisis | health alerts, safety surfaces, emergency overlays | Inter at 18px+ minimum | high contrast, coral urgency, severity levels | direct, calm, single-action |

These are placeholders. The audiences, requirements, vibes, and worked examples all need iteration. The mechanism (`[data-profile="<name>"]` overlays in CSS) is settled.

## 2. What this revision must produce per profile

For each of Foundation / Clinical / Research / Lab / Companion / Crisis, ship:

### 2.1 Audience (one paragraph)

Who is in front of this surface? What is their state of mind? What did they just do, and what are they about to do?

Worked example for Clinical (use as a template; revise as needed):

> "A patient who just opened the Cytognosis app on their phone. They may have just received a biomarker reading that drifted, or they may be about to record a voice check-in with the interviewer agent. They are not technical. They are anxious or uncertain. They may be reading the screen with reduced mental bandwidth because of distress. Their primary goal is to feel oriented and informed without being overwhelmed."

Worked example for Companion:

> "A neurodivergent individual using the Cytognosis companion app as part of their daily routine. They may have ADHD, autism, or another neurodevelopmental condition. Their attention is variable. They may be fatigued, hyperfocused, or transitioning between tasks. They need clear visual hierarchy, predictable navigation, and gentle reinforcement. Cognitive load must stay low. The interface should feel like a supportive daily tool, not a clinical instrument."

Worked example for Crisis:

> "A person experiencing a health alert or safety event. They may be in physical distress, emotional crisis, or responding to an urgent biomarker reading. Cognitive bandwidth is severely limited. They need exactly one clear action per screen, with no distractions, no animations, and maximum contrast. The interface must feel immediately understandable even under stress."

### 2.2 Trigger surfaces (concrete list)

Which products / pages / screens default to this profile? Examples for each:

- **Foundation**: cytognosis.org logged-out pages, investor decks, press releases, social cards, conference talks.
- **Clinical**: app-phone interviewer agent (clinical context), app-phone asset hub (patient mode), the patient-facing extension build, any web logged-in view aimed at a patient in clinical workflows.
- **Research**: app-desktop internal hub, app-web logged-in dashboards for researchers / clinicians, Cytoverse workbench, the internal extension build.
- **Lab**: cytoctl CLI, cytognosis-dusk terminal theme, dev docs site, log streams, IDE themes.
- **Companion**: Yar mobile app (default profile), daily health tracking surfaces, gamification screens, habit-tracking dashboards, neurodivergent-focused onboarding flows, any surface marked for ND daily use.
- **Crisis**: health alert dialogs, crisis-safety surfaces, emergency banners, biomarker-drift urgency overlays, any surface triggered by `CrisisDetected` events.

### 2.3 Requirements (measurable)

- **Density**: words per square inch, table rows per page, allowable nesting depth.
- **Contrast budget**: minimum WCAG ratio required (AA, AAA where).
- **Motion budget**: how much animation is welcome.
- **Reading-level budget**: target Flesch-Kincaid (if applicable).
- **Touch target minimum**: per the profile's surface.
- **Cognitive load ceiling** (Companion and Crisis only): maximum number of actions per screen, maximum information density score.

Profile-specific requirements to confirm:

| Requirement | Foundation | Clinical | Research | Lab | Companion | Crisis |
|---|---|---|---|---|---|---|
| Contrast | AA body, AAA hero | AAA all | AA all | AA all | AAA body, AA decorative | AAA all, 7:1 minimum |
| Motion | generous | conservative | moderate | generous | disabled by default, opt-in | none, zero animations |
| Touch target | 44px | 44px | 44px | 44px | 48px | 56px minimum |
| Max actions/screen | n/a | 3-5 | n/a | n/a | 3 primary | 1 primary |
| Line height | 1.5 | 1.6 | 1.4 | 1.3 | 1.7 | 1.6 |
| Max line width | 75ch | 65ch | 80ch | 90ch | 65ch | 480px card width |
| Paragraph gap | 1em | 1.25em | 0.75em | 0.5em | 1.5em | 1.5em |

### 2.4 Vibe (one-paragraph emotional register)

How does the profile feel? Like talking to whom? What music plays in the background?

Worked example for Foundation (use as a template):

> "Like listening to a thoughtful TED talk by a clinician-scientist. Warm but not saccharine. Confident but never arrogant. Aspirational without overpromising. Slow tempo, clear melody. Reads like the New York Times Sunday Review on a healthcare topic, not a tech magazine on a healthcare topic."

Worked example for Companion:

> "Like a supportive friend who understands that your brain works differently and celebrates it. Gentle without being condescending. Encouraging without pressure. The visual space feels open, uncluttered, and breathable. Like a well-organized desk in a quiet room with warm lighting and a plant. Progress is visible, streaks are celebrated, and there is always an easy way to pause."

Worked example for Crisis:

> "Like a calm, trained first responder who speaks in short, clear sentences. No decoration, no personality, no warmth beyond clarity. Every word earns its place. The visual space is stripped to essentials: one action, one message, maximum contrast. Like a well-designed emergency exit sign."

### 2.5 Typography stack (confirmation + alternates)

Confirm the default and the alternates. State **why** each alternate is the alternate.

Companion typography:

| Role | Font | Rationale |
|---|---|---|
| Body | Lexend | Designed for reading fluency; reduces visual crowding for neurodivergent readers |
| Code / data | Atkinson Hyperlegible Mono | Maximum character distinguishability; designed for low-vision but benefits ND readers |
| Headings | Inter | Consistent with Foundation; familiarity across profiles |
| Alternate body | OpenDyslexic | Available as user-selectable toggle for dyslexic users |

Crisis typography:

| Role | Font | Rationale |
|---|---|---|
| Body | Inter at 18px+ minimum | Maximum clarity at stress-level reading; no decorative fonts |
| Headings | Inter Bold at 24px+ | Clear hierarchy without visual complexity |

### 2.6 Palette emphasis (confirmation + the why)

Confirm which colors carry the emphasis. State which colors are forbidden in this profile.

Companion palette:

| Role | Color | Token |
|---|---|---|
| Focus signal | Azure 300 | `--cg-companion-focus` |
| Energy signal | Magenta 300 | `--cg-companion-energy` |
| Mood signal | Violet 300 | `--cg-companion-mood` |
| Sleep signal | Teal 300 | `--cg-companion-sleep` |
| Stress signal | Coral 300 | `--cg-companion-stress` |
| Backgrounds | muted 300-shade pastels | Reduced saturation defaults |
| Forbidden | any 600+ shade as background | Too visually intense for sustained ND use |

Crisis palette:

| Role | Color | Token |
|---|---|---|
| Urgency | Coral 600 | `--cg-crisis-urgency` |
| Action | Azure 600 on white | `--cg-crisis-action` |
| Severity low | Teal 600 | `--cg-crisis-severity-low` |
| Severity medium | Violet 600 | `--cg-crisis-severity-medium` |
| Severity high | Coral 600 | `--cg-crisis-severity-high` |
| Severity critical | Magenta 600 on dark | `--cg-crisis-severity-critical` |
| Forbidden | gradients, decorative color | Distracting under stress |

### 2.7 Worked example (a paragraph of copy)

Same topic in each of the six profile voices. Pick one topic and write six versions. Suggested topic: explaining a recent biomarker drift to the relevant audience.

## 3. Profile selection decision tree

A clear flow for picking a profile when context is unclear:

```
1. Is this a crisis or safety surface?
   └─ Yes → Crisis

2. Is this surface designed for daily neurodivergent use?
   └─ Yes → Companion

3. Who is the primary reader?
   ├─ A potential investor, partner, or member of the press → Foundation
   ├─ A patient or a clinician acting in clinical mode → Clinical
   ├─ A scientist (researcher) or a clinician acting in analyst mode → Research
   └─ A developer of Cytognosis tools or someone using the CLI → Lab

4. If the surface mixes audiences, which audience is highest-stakes?
   ├─ Patient-facing copy on a marketing page → still Foundation for the page;
   │  isolate the patient-facing card in [data-profile="clinical"]
   └─ Research surface inside a patient app → reserve Research for the secondary view;
      patient-facing primary view stays Clinical

5. If still unclear:
   ├─ Public-facing default: Foundation
   └─ Internal default: Research
```

## 4. Side-by-side comparison

Produce a 6-up comparison page (`branding/design-system/profiles/_comparison.html`) showing:

- The same paragraph in each profile's voice.
- The same data point in each profile's visual style.
- A representative button in each profile.
- A representative heading in each profile.

This is the single page a reviewer can scan to feel the difference between the six registers.

## 5. Cross-link to interface templates

Each of the interface templates has a default profile. Confirm or revise:

| Template | Default profile (proposed) |
|---|---|
| app-phone (clinical context) | Clinical |
| app-phone (Yar daily use) | Companion |
| app-phone (health alerts) | Crisis |
| app-web (logged-out) | Foundation |
| app-web (logged-in) | Research |
| app-desktop | Research |
| app-extension (patient mode) | Companion |
| app-extension (internal mode) | Research or Lab |

If any of these is wrong, surface it. The cytognosis-branding skill's per-template references inherit these defaults.

## 6. Recommendations to lock in (Claude as opinionated collaborator)

For each profile, take a position. State the position as a strong recommendation; Cytognosis confirms or overrides.

Sample recommendations to weigh:

1. **Clinical is the most-mentioned but the most-placeholder.** Treat it as the priority. The patient-app interviewer agent is the headline product, and Clinical defines what it feels like. Spend the most time here.
2. **Lab might be over-engineered.** Recursive is a beautiful idea, but does Cytognosis ship enough developer tooling to justify a profile distinct from Research? If not, fold Lab into Research with a single CSS toggle for "terminal density" rather than a separate profile.
3. **Research has the right type stack but the wrong palette.** Indigo-as-default may read too cool; consider adding violet-300 as a secondary so the workbench feels brand-continuous with Foundation.
4. **Foundation's default headings are too large.** 40-52px at hero is fine; 28-32px for in-page headings is more in line with the brand's restraint.
5. **Companion is the ND-first profile and must be tested with ND users.** Do not ship without at least one round of usability testing with ADHD and autistic participants. The cognitive-signal color mapping needs validation.
6. **Crisis must be clinically reviewed.** The single-action focus and severity levels need sign-off from a clinical safety team before shipping.

## 7. Status (preliminary to settled checklist)

For each profile, work through:

- [ ] Audience paragraph written and reviewed.
- [ ] Trigger surfaces enumerated.
- [ ] Requirements measured (density, contrast, motion, cognitive load).
- [ ] Vibe paragraph written.
- [ ] Type stack confirmed; alternates justified.
- [ ] Palette emphasis confirmed; forbidden colors listed.
- [ ] Worked example written (one paragraph in this profile's voice).
- [ ] Cross-link to templates confirmed.
- [ ] Side-by-side comparison row populated.
- [ ] CSS overlay tokens reviewed against the audience requirements.
- [ ] ND-specific requirements validated (Companion and Crisis only).

When all six profiles have all 11 boxes ticked, the profile system moves from preliminary to settled.

## 8. Deliverables to ship back

1. Refreshed `branding/design-system/profiles/README.md` reflecting the production spec (carries the matrix + decision tree).
2. Per-profile detail docs: `branding/design-system/profiles/foundation.md`, `clinical.md`, `research.md`, `lab.md`, `companion.md`, `crisis.md`. Each contains the audience, trigger surfaces, requirements, vibe, type/palette confirmation, and worked example.
3. The side-by-side comparison page at `branding/design-system/profiles/_comparison.html`.
4. Updated `branding/design-system/profiles/profiles.css` with any token revisions surfaced during the audience requirements review, including Companion and Crisis overlay tokens.
5. Six rendered example pages at `branding/design-system/profiles/examples/{foundation,clinical,research,lab,companion,crisis}.html`.

## 9. Open questions to surface back to Cytognosis

When you hit any of these, pause and ask:

1. Is the "Clinical patient" and "Clinical clinician" distinction needed? Or does Clinical cover both, with Companion handling the daily-use patient surface?
2. Is the Lab profile worth its own register, or should it fold into Research?
3. The Foundation profile's hero headings: 40-52px (current) vs 28-32px (recommendation for restraint)?
4. The Research profile uses indigo-as-default. Should violet-300 be the secondary emphasis so the workbench feels brand-continuous with Foundation?
5. Companion's cognitive-signal color mapping (Focus=Azure, Energy=Magenta, Mood=Violet, Sleep=Teal, Stress=Coral): does this need clinical/psychological validation?
6. Crisis severity levels: three tiers (low/medium/high) or four tiers (low/medium/high/critical)?
7. Should Companion support a "body doubling" mode where the interface stays visible but dims non-essential elements during focus sessions?

## 10. Voice-rules consistency

All six profiles still inherit the hard voice rules from `branding/design-system/WRITING.md`:

- No em dashes.
- No "patients" outside clinical context.
- No hype words.
- Active present tense.
- Oxford comma always.
- Title Case headings; sentence case for UI labels.

Profile-specific dials (warmth, precision, length) modulate within these rules, not against them.

Companion adds: use encouraging language, celebrate progress, avoid urgency language for non-urgent contexts, prefer "you" over "the user."

Crisis adds: use imperative mood, one sentence per instruction, no decorative language, action verb first.
