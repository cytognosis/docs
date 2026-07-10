# ADHD and Neurodiversity Design Research

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Cytognosis Foundation Design System Reference
> **Version:** 1.0 · **Date:** 2026-05-31 · **Status:** Canonical reference
> **Maintainer:** Cytognosis Design System Team

## TL;DR

Neurodivergent users (ADHD, autism, dyslexia, anxiety/depression) require design systems that reduce cognitive load, eliminate shame, and adapt to fluctuating cognitive states. This document synthesizes primary research from Chen, Meng & Nie (2026, 42 participants), Blue Lin (CHI 2024), evidence-based color and typography studies, and the Cytognosis design system into actionable guidelines. Every recommendation maps to empirical evidence, a WCAG criterion, or a validated design concept.

---

## 1. Research Foundation

### 1.1 Primary Research: Chen, Meng & Nie (2026)

**Citation:** Chen, J., Meng, Y., & Nie, K. (2026). "Not Just Me and My To-Do List: Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds." arXiv:2603.17258v2.

**Study design:** Two-phase mixed-methods study with ADHD-identifying adults. Phase 1 conducted 22 semi-structured interviews (P1-P22; 16 clinically diagnosed, 6 strongly self-identified; ages 18-55; diverse occupations). Phase 2 ran 20 speed-dating sessions (S1-S20) evaluating 13 speculative AI design concepts on a 1-5 Likert scale.

**Core finding:** Task management for adults with ADHD is relationally and affectively co-constructed, not an isolated act of individual willpower. Productivity tools built on neurotypical assumptions (stable attention, linear time, individual self-regulation) actively harm ADHD users.

#### Barrier Taxonomy

The study identifies 14 barriers across three categories:

| Category | Barrier | Key Quote |
|---|---|---|
| **Internal (8)** | Task initiation paralysis | "I obviously want to brush my teeth and wash my face, but I stay in bed all the time." (P17) |
| | Hyperfocus/flow states | "When it's something I really like, I can write for ten hours straight, and it feels effortless." (P13) |
| | Time perception disorders | "Unless I pay special attention, my perception of time is as if I want to deliberately forget it." (P5) |
| | Deadline addiction | "I feel that I have formed a kind of satisfaction [from] this kind of dependence on pressure." (P1) |
| | Emotional avoidance of low-meaning tasks | Tasks without personal relevance become "emotionally aversive" (P4, P8, P12) |
| | Emotional fluctuations and self-blame | "I often blame myself for a moment of distraction." (P17) |
| | Fear of sustainability | "If I really succeed, it will be very hard to maintain. I might as well smash this possibility with my own hands." (P1) |
| | Planning anxiety | "Every time I write a plan, I get anxious because I know I won't follow it." (P10) |
| **Relational (4)** | Social misrecognition | "When I told my sister I had ADHD, she said, 'Then just correct it.'" (P6) |
| | Internalized inadequacy | "I know it's ADHD, but I still feel like I should just try harder." (P10) |
| | Resistance and reframing | "It's not that I can't focus; it's that I focus differently." (P7) |
| | Unequal access to social scaffolding | Those living alone described "emotional burden of self-management in isolation." (P8, P14) |
| **Systemic (2)** | Institutional misalignment | Open-office sensory overload, notification clutter, rigid administrative systems |
| | Over-reliance and avoidance | "I sometimes spend more time organizing the to-do app than doing the task." (P9) |

#### Top-Rated Design Concepts

Speed-dating evaluation ranked 13 concepts. The top four, which directly inform Cytognosis design patterns:

| Concept | Phase | Median | Top-3 Count | Design Implication |
|---|---|---|---|---|
| **C8: Brain Weather Dashboard** | Execution | **5.0** | 13 | Affirming ND cognition; metaphorical visualization reduces shame |
| **C3: Flexible Planning + Gentle Streaks** | Planning | **5.0** | 10 | Time as rhythm; dual-track goals normalize partial completion |
| **C6: Social Presence AI** | Execution | **4.5** | 12 | Co-regulation; digital body-doubling reduces initiation barrier |
| **C11: Emotionally Aware Pause Days** | Adaptation | **4.5** | 12 | Mood-adaptive; proactive rest prevents burnout |

The lowest-rated concepts (C4: Emotional Inventory, M=2; C7: Ambient Transition Cues, M=2) reveal that ADHD users reject features that add friction during high-motivation moments or produce cues too subtle to notice during focus.

#### Five Design Implications

1. **Relational accountability over solo optimization.** Simulate relational presence through conversational check-ins, progress co-tracking, and dynamic emotional acknowledgment.
2. **Time as rhythm, not grid.** Structure tasks against energy flows. Support "ideal vs. baseline" plans. Preserve streaks on skip days.
3. **Mood-adaptive interfaces.** Integrate mood-awareness into every interaction. A user feeling overwhelmed should see only manageable goals with affirming language.
4. **Affirming neurodivergent cognition.** Allow users to select representations that align with their cognitive orientation. Cognitive heterogeneity requires multiple engagement modes.
5. **Co-regulation as core infrastructure.** Build social scaffolding into the architecture: focus rooms, journaling dashboards with peer check-ins, shared timelines with mutual nudging.

### 1.2 CHI 2024 Design Principles (Blue Lin)

Blue Lin's health-data-visualization research at CHI 2024 establishes six principles for presenting complex health data to neurodivergent users:

1. **Sensemaking over prediction.** Help users understand cognitive patterns rather than simply scheduling tasks.
2. **User agency primary.** The system illuminates; the user decides. No automated actions without explicit consent.
3. **Progressive disclosure.** Show a composite "How am I doing?" summary first, then signal groups, then raw data on demand.
4. **Longitudinal context.** Multi-week overlays reveal cognitive signatures that single-day snapshots miss.
5. **Inclusive, neurotype-neutral, culturally responsive.** No deficit framing. Language and visualizations respect diverse cognitive profiles.
6. **No shame, ever.** "Your focus was lower today" replaces "You had a bad day." Gentle streaks. Pause days. No red overdue tasks.

### 1.3 Industry Best Practices (2024-2026)

Recent research and industry practice converge on five pillars for neurodivergent-accessible design:

**Cognitive load reduction.** Progressive disclosure keeps working memory demands below Miller's Law threshold (7±2 chunks). Simplified navigation with step-by-step wizards reduces decision fatigue. Sweller's Cognitive Load Theory (1988) establishes that extraneous load from poor design directly competes with germane load needed for learning and task execution.

**Sensory environment control.** No autoplay media. Subtle, purposeful animations only. Clean grid layouts with ample whitespace. All motion must respect `prefers-reduced-motion`. Squirrelsong research confirms pastels reduce sensory overload compared to saturated palettes.

**Predictability and consistency.** Standardized UI patterns across all views. Consistent button placements. Clear, immediate feedback for every action. WCAG 2.2 criterion 3.2.3 (Consistent Navigation) codifies this principle.

**User autonomy and flexibility.** User control over font size, spacing, color themes, information density, and notification frequency. Multiple input modalities (voice, text, touch). Customizable dashboard layouts.

**Gamification done right.** Immediate feedback loops with gentle animations. Flexible streaks that survive skip days. Low-stakes challenges that build momentum. Novelty and progression to sustain engagement without shame.

**Applicable WCAG 2.2 criteria:**

| Criterion | Requirement | ND Relevance |
|---|---|---|
| 2.2.2 Pause, Stop, Hide | User can pause, stop, or hide moving content | Reduces distraction for ADHD users |
| 2.4.6 Headings and Labels | Headings and labels describe topic or purpose | Supports scanning behavior |
| 3.2.3 Consistent Navigation | Navigation mechanisms occur in same relative order | Reduces cognitive load from reorientation |
| 3.3.2 Labels or Instructions | Labels or instructions provided for user input | Prevents form anxiety and errors |

---

## 2. Design Principles

### 2.1 Cognitive Load Reduction

**Evidence:** Miller's Law (7±2 items in working memory); Sweller's Cognitive Load Theory (1988); Chen et al. (2026) over-reliance barrier.

Design to keep working memory demands minimal at every interaction point:

- **Progressive disclosure.** Present the most important information first. Hide details in expandable sections (`<details>` elements). Cap nesting at three levels maximum.
- **Chunked information.** Break content into scannable units of 3-4 sentences. Use tables for 3+ comparable items (Paivio's Dual Coding Theory, 1986).
- **One primary action per screen.** Each view should have one clear call to action. Secondary actions use reduced visual weight.
- **Smart defaults.** Pre-fill forms with intelligent defaults. Reduce the number of decisions the user must make.
- **Step-by-step wizards.** Complex workflows become sequential steps with progress indicators. Each step fits on one screen without scrolling.

```css
/* Progressive disclosure pattern */
.disclosure-panel {
  max-height: 0;
  overflow: hidden;
  transition: max-height 300ms ease-out;
}

.disclosure-panel[open] {
  max-height: var(--panel-max-height, 500px);
}

/* Reduce decisions: single primary action */
.action-bar .primary {
  background: var(--color-azure-500);
  font-weight: 600;
}

.action-bar .secondary {
  background: transparent;
  color: var(--color-text-muted);
  font-weight: 400;
}
```

### 2.2 Sensory Environment Control

**Evidence:** NIH/iMotions cool-colors-reduce-anxiety research; Squirrelsong pastel research; Chen et al. (2026) C7 low rating (ambient cues too subtle).

Control the sensory environment to prevent overwhelm without understimulating:

- **No autoplay.** All media requires explicit user action to start. This includes videos, animations, and audio.
- **Purposeful motion only.** Animations serve a function (state transitions, feedback, spatial orientation). Decorative animation is off by default.
- **Whitespace as structure.** Generous padding and margins create visual breathing room. Minimum 16px padding on content blocks; 24px between sections.
- **Clean grid layouts.** Predictable alignment reduces visual scanning effort. Use consistent 8px grid.
- **Muted palette defaults.** Daily-use colors use shade-300 tokens (desaturated pastels). Full-saturation brand colors appear in accents, illustrations, and CTAs only.
- **Dark mode as default.** Cytognosis dark theme (#0A0A14 to #13131F backgrounds) reduces eye strain and sensory load during extended use.

### 2.3 Predictability and Consistency

**Evidence:** WCAG 2.2 criterion 3.2.3; autism spectrum research on predictable layouts; Chen et al. (2026) planning anxiety barrier.

Predictable interfaces reduce the cognitive cost of orientation:

- **Consistent navigation.** Navigation elements appear in the same position on every screen, in the same order.
- **Standardized component behavior.** Buttons, inputs, and interactive elements behave identically across all contexts. A toggle always toggles. A swipe always swipes the same direction.
- **Immediate feedback.** Every user action produces a visible response within 100ms. Loading states appear for operations exceeding 300ms.
- **Clear labels.** All interactive elements have descriptive labels. No icon-only buttons without accessible text. WCAG 2.2 criterion 3.3.2 applies.
- **Predictable content structure.** Pages follow a consistent template per type. Users learn the layout once and navigate by muscle memory.

### 2.4 User Autonomy and Customization

**Evidence:** Chen et al. (2026) DI4 (affirming ND cognition requires multiple engagement modes); Lin (2024) DR2 (user agency primary).

Users control their own experience:

- **Font selection.** Offer Lexend (default), Inter, Atkinson Hyperlegible, and OpenDyslexic as options.
- **Size and spacing controls.** Font size, line height, and letter spacing adjustable via settings. Minimum 16px body text; users can increase without layout breakage.
- **Information density.** Compact, comfortable, and spacious layout modes. Default to comfortable.
- **Notification preferences.** Per-category notification controls: frequency, tone, delivery mode (visual, audio, haptic). Gentle, non-punitive defaults.
- **Color theme options.** Dark (default), light, high-contrast, and custom theme support. All themes meet WCAG AAA contrast.
- **Dashboard customization.** Users choose which widgets appear, their order, and their size. No forced information.

### 2.5 Relational and Social Support

**Evidence:** Chen et al. (2026) DI1, DI5; C6 Social Presence AI (M=4.5); C3 Flexible Planning (M=5).

Design for co-regulation rather than isolated self-management:

- **Companion presence.** Animated companion (Rive avatar) provides ambient body-doubling during work sessions. Toggleable between active support (encouraging messages) and silent presence.
- **Gentle accountability.** Check-ins use warm, non-evaluative language. "You captured three things today" rather than "You completed 3 of 7 tasks."
- **Shared visibility (opt-in).** Users choose what to share, with whom, and what response they welcome. Sharing never defaults to on. Granular per-person controls.
- **No shame language.** Tasks are never "overdue." They are rescheduled, descoped, or released. No red warning indicators on missed items. No productivity metrics that invite comparison.
- **Flexible streaks.** Streaks survive skip days. A gentle streak counts consistency over time, not consecutive days. "You've been consistent 4 of the last 7 days" rather than "Streak: 0."

---

## 3. Color System for Neurodivergent Users

### 3.1 Evidence-Based Color Choices

Research from multiple sources converges on specific color guidelines for neurodivergent users:

| Principle | Evidence Source | Cytognosis Application |
|---|---|---|
| Cool colors reduce anxiety | NIH; iMotions research | Entire palette anchored in cool family (violet, azure, teal, indigo) |
| Pastels reduce sensory overload | Squirrelsong research | Daily-use shade-300 tokens for backgrounds and subtle elements |
| Pure black (#000) causes halation | Coding Horror; accessibility research | Indigo-tinted darks only: #0A0A14 to #1E1E32 |
| Pure white (#FFF) causes glare | Low-vision research | Off-whites with indigo undertone: #E0E0ED to #F8F8FC |
| Muted, desaturated tones reduce cognitive load | ADHD reading research | Core palette uses muted versions for daily interaction |
| Warm colors trigger arousal | Color psychology research | Coral (#F26355) and Magenta (#E0309E) used sparingly as accents |
| Violet aids emotional regulation | Chromotherapy evidence | Violet (#8B3FC7) as signature brand color |
| Strategic color coding reduces processing effort | UX research; dual coding theory | Consistent cognitive-signal color mapping across all surfaces |

### 3.2 Cytognosis Cognitive-Signal Color Mapping

The Yar cognitive companion maps five cognitive signals to Cytognosis brand colors (derived from fluorescent dye wavelengths, reinforcing the biomedical identity):

| Cognitive Signal | Color | Hex | Fluorophore Origin | Usage |
|---|---|---|---|---|
| **Focus** | Azure | `#3B7DD6` | Alexa Fluor 488 | Focus timers, attention metrics, work sessions |
| **Energy** | Magenta | `#E0309E` | Rhodamine | Energy level indicators, activity bursts (use sparingly) |
| **Mood** | Violet | `#8B3FC7` | DAPI | Mood tracking, emotional state, Brain Weather primary |
| **Sleep/Recovery** | Teal | `#14A3A3` | GFP (Green Fluorescent Protein) | Sleep quality, recovery metrics, rest suggestions |
| **Stress/Load** | Coral | `#F26355` | MitoTracker Red | Cognitive load alerts, stress indicators (use sparingly) |

This mapping creates a learnable visual vocabulary. Users internalize the association (blue = focus, purple = mood) and can scan dashboards without reading labels. The mapping remains stable across all Cytognosis products and profiles.

### 3.3 Therapeutic Color Theory

The Cytognosis accessibility reference (Section 11) establishes therapeutic principles that govern color usage across all neurodivergent-facing surfaces:

| Principle | Evidence | Application |
|---|---|---|
| Cool colors reduce anxiety | NIH, iMotions | Entire palette stays in the cool family |
| Pastels reduce sensory overload | Squirrelsong | Daily-use shade-300 tokens for backgrounds, cards, subtle UI |
| Pure black causes halation | Coding Horror | Indigo-tinted darks only (#0A0A14, never #000000) |
| Violet aids emotional regulation | Chromotherapy | Signature brand color, mood-state visualizations |
| Warm accents prevent flatness | UX research | Coral and Magenta in measured doses for energy and emphasis |

**The therapeutic color hierarchy for daily use:**

1. **Base layer (80% of surface area):** Indigo-tinted darks (#0A0A14 to #13131F) or light off-whites (#F0F0F7 to #F8F8FC)
2. **Card/container layer (15%):** Elevated surfaces (#25253D dark, #FFFFFF light) with glassmorphism (rgba(30,41,59,0.5) + blur(12px))
3. **Accent layer (5%):** Brand colors at shade-300 for daily use, shade-500/600 for interactive elements

### 3.4 Profile-Specific Color Adaptations

Cytognosis operates three user profiles, each requiring specific color adaptations for neurodivergent users:

**Companion Profile (ND-First):** The primary neurodivergent-optimized profile. Uses the full cognitive-signal color mapping. Brain Weather Dashboard as the default home view. Muted shade-300 palette for daily interaction. Full-saturation colors appear only in data visualizations and CTAs.

**Crisis Profile (Urgent States):** Simplified color palette with maximum contrast. Reduces to three colors: primary action (Azure), warning (Coral), and neutral (base). Removes all decorative color. Increases text contrast to maximum AAA levels. Simplifies the UI to essential actions only.

**Clinical Profile (ND Adaptations):** Professional clinical interface with ND accommodations. Uses the cognitive-signal mapping but with clinical labeling. Supports high-contrast mode. All data visualizations include redundant coding (color + shape + label) for colorblind safety.

### 3.5 Color Tokens Reference Table

```css
/* ==========================================================
   Cytognosis ND Color Tokens
   All neutrals carry hue ~240 (indigo undertone), never cold gray.
   ========================================================== */

:root {
  /* --- Base Surfaces --- */
  --surface-base:        #0A0A14;  /* Primary dark background */
  --surface-elevated:    #13131F;  /* Secondary dark background */
  --surface-card:        #25253D;  /* Card / container background */
  --surface-overlay:     rgba(30, 41, 59, 0.5);  /* Glassmorphism base */

  /* --- Text --- */
  --text-primary:        #F8F8FC;  /* Primary text on dark (AAA 16.2:1) */
  --text-secondary:      #E0E0ED;  /* Secondary text on dark (AAA 14.6:1) */
  --text-muted:          #9090B0;  /* Muted text, captions (AA 5.8:1) */
  --text-on-light:       #1C1C2E;  /* Body text on light backgrounds */

  /* --- Cognitive Signal Colors (shade-500, interactive) --- */
  --color-focus:         #3B7DD6;  /* Azure, focus/attention */
  --color-energy:        #E0309E;  /* Magenta, energy/vitality */
  --color-mood:          #8B3FC7;  /* Violet, mood/emotional state */
  --color-sleep:         #14A3A3;  /* Teal, sleep/recovery */
  --color-stress:        #F26355;  /* Coral, stress/cognitive load */

  /* --- Daily-Use Pastels (shade-300, reduced saturation) --- */
  --color-focus-muted:   #7BAAE6;  /* Azure-300, daily-use focus */
  --color-energy-muted:  #F080C4;  /* Magenta-300, daily-use energy */
  --color-mood-muted:    #B17FDB;  /* Violet-300, daily-use mood */
  --color-sleep-muted:   #5CC5C5;  /* Teal-300, daily-use sleep */
  --color-stress-muted:  #F5998F;  /* Coral-300, daily-use stress */

  /* --- Semantic --- */
  --color-success:       #14A3A3;  /* Teal, reuses sleep/recovery */
  --color-warning:       #F5998F;  /* Coral-300, non-alarming */
  --color-error:         #F26355;  /* Coral-500, always with icon+label */
  --color-info:          #5145A8;  /* Indigo, calm informational */

  /* --- Interactive --- */
  --color-interactive:   #3B7DD6;  /* Azure, primary actions */
  --color-interactive-hover: #5A95E8;  /* Azure-400, hover state */
  --color-focus-ring:    #7BAAE6;  /* Azure-300, 3px, 2px offset */

  /* --- Gradient (signature) --- */
  --gradient-brand: linear-gradient(135deg, #8B3FC7, #5A95E8, #E0309E);

  /* --- Light Theme Overrides --- */
  --surface-base-light:      #F8F8FC;
  --surface-elevated-light:  #F0F0F7;
  --surface-card-light:      #FFFFFF;
  --text-primary-light:      #1C1C2E;
  --text-secondary-light:    #3A3A5C;
}

/* Glassmorphism for elevated cards */
.glass-card {
  background: var(--surface-overlay);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(139, 63, 199, 0.15);
  border-radius: 12px;
}
```

---

## 4. Typography for Neurodivergent Users

### 4.1 Font Recommendations

Evidence-based font selection, ordered by primary use case:

| Font | Primary Use | Evidence | Strengths |
|---|---|---|---|
| **Lexend** (Variable) | Body text (default) | Bonnie Shaver-Troup's reading-fluency research; controlled experiments show significantly higher WCPM vs Times New Roman | Reduces visual crowding via hyper-expansion spacing. Variable weight allows fine-tuned density control. Best overall choice for ADHD users. |
| **Atkinson Hyperlegible** | Low-vision contexts, instructions, clinical forms | Braille Institute; designed to maximize character distinction | Distinct b/d, p/q, I/l/1, O/0 letterforms. Excellent for users with dyslexia or low vision. |
| **Inter** | UI chrome, navigation, secondary text | Industry standard; optimized for screen legibility | Clean, open letterforms. Extensive glyph coverage. Cytognosis brand font. |
| **OpenDyslexic** | User-selectable option for dyslexic users | Weighted letter bottoms reduce reversal; subjective user preference | Some dyslexic users strongly prefer it. Always offer as an option; never force. |
| **JetBrains Mono** | Code blocks, monospace contexts | Designed for code readability; distinct similar characters | Clear distinction between similar characters (0/O, 1/l/I). Cytognosis terminal font. |

**Font stack implementation:**

```css
:root {
  --font-body:    'Lexend', 'Inter', system-ui, sans-serif;
  --font-ui:      'Inter', system-ui, sans-serif;
  --font-a11y:    'Atkinson Hyperlegible', 'Inter', sans-serif;
  --font-dyslexic: 'OpenDyslexic', 'Lexend', sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;
}

/* User font preference override */
[data-font-preference="atkinson"] body {
  font-family: var(--font-a11y);
}

[data-font-preference="dyslexic"] body {
  font-family: var(--font-dyslexic);
}
```

### 4.2 Spacing and Sizing Requirements

| Property | Minimum | Recommended | Maximum | Evidence |
|---|---|---|---|---|
| **Body font size** | 16px | 18px (patient-facing) | User-controlled | 12-14pt minimum; 16pt+ preferred for accessibility |
| **Line height** | 1.5x font size | 1.6x-1.8x | 2.0x | 1.5x reduces crowding; 2.0x max before text feels disconnected |
| **Letter spacing** | 0 | 0.01em-0.02em | 0.05em | Slight expansion aids character distinction |
| **Word spacing** | Normal | 0.05em-0.1em | 0.16em | Wider word spacing aids word boundary detection |
| **Line length** | 45 characters | 65-75 characters | 80 characters | Prevents eye fatigue and tracking loss |
| **Paragraph spacing** | 1.0em | 1.5em | 2.0em | Creates visual breathing room between blocks |
| **Heading spacing** | 1.5em above | 2.0em above, 0.5em below | 2.5em above | Clear hierarchy with ample separation |

```css
/* ND-optimized typography scale */
:root {
  --text-xs:    0.75rem;   /* 12px, captions only */
  --text-sm:    0.875rem;  /* 14px, secondary labels */
  --text-base:  1rem;      /* 16px, minimum body */
  --text-lg:    1.125rem;  /* 18px, patient-facing body */
  --text-xl:    1.25rem;   /* 20px, section headers */
  --text-2xl:   1.5rem;    /* 24px, page headers */
  --text-3xl:   1.875rem;  /* 30px, hero headers */

  --leading-tight:   1.4;
  --leading-normal:  1.6;
  --leading-relaxed: 1.8;
  --leading-loose:   2.0;

  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;
}

body {
  font-family: var(--font-body);
  font-size: var(--text-lg);      /* 18px default for health app */
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
  text-align: left;               /* NEVER justified */
  max-width: 72ch;                /* ~72 characters per line */
}

/* Paragraph constraints */
p {
  margin-bottom: 1.5em;
  /* Content rule: max 4 sentences per paragraph (enforced editorially) */
}

/* Heading hierarchy with generous spacing */
h1, h2, h3, h4 {
  margin-top: 2em;
  margin-bottom: 0.5em;
  font-weight: 600;
}
```

### 4.3 Content Formatting Rules

These rules apply to all Cytognosis content targeting neurodivergent users:

| Rule | Rationale | Evidence |
|---|---|---|
| **Left-aligned always** | Justified text creates "rivers" of whitespace that distract dyslexic readers | Dyslexia research; ADHD visual processing studies |
| **Bold for emphasis, never italics** | Italics merge letterforms for dyslexic readers. Underlines suggest hyperlinks. | Dyslexia typography research; web conventions |
| **Max 4 sentences per paragraph** | Reduces visual overwhelm. Creates natural scanning points. | ADHD reading research; ADHDfy pipeline principle #4 |
| **Max 80 characters per line** | Prevents eye fatigue and tracking loss during line returns | Typography best practices; reading fluency research |
| **Tables over lists for 3+ items** | Tables create spatial structure that supports visual scanning | Paivio's Dual Coding Theory (1986) |
| **Concrete examples before abstractions** | ADHD learners process concrete-to-abstract more effectively | Concrete-first learning preference research |
| **BLUF (Bottom Line Up Front)** | Key information appears first; supports scanning and task initiation | Military communications research; Miller's Law |
| **Define acronyms on first use** | Reduces working memory burden from tracking unfamiliar terms | Autism-friendly explicitness; cognitive load reduction |
| **Descriptive link text** | "View your sleep data" not "click here." Supports screen readers and scanning. | WCAG 2.2; accessibility best practices |
| **Emoji section markers** | Visual anchors aid rapid section identification: 🔬 Research, ⚡ Quick Start, ➡️ Next Steps | ADHDfy pipeline; visual scanning support |

### 4.4 The ADHDfy Pipeline

The ADHDfy pipeline transforms complex documents into neurodivergent-accessible formats using an 11-step evidence-based process. Apply this pipeline to any document exceeding 200 lines or targeting non-specialist readers.

**Pipeline steps:**

| Step | Action | Evidence |
|---|---|---|
| 1 | **BLUF extraction.** Generate a 3-sentence TL;DR in a callout at the top. | Miller's Law; cognitive load reduction |
| 2 | **Paragraph chunking.** Break paragraphs exceeding 4 sentences into bullet points with bold key terms. | ADHD reading research |
| 3 | **Table conversion.** Convert lists of 3+ comparable items into tables with clear column headers. | Dual Coding Theory (Paivio, 1986) |
| 4 | **Diagram injection.** Add Mermaid diagrams for any process, flow, or relationship described in prose. | Dual Coding Theory |
| 5 | **Section summaries.** Add one-sentence summary callouts at each major section. | Cognitive Load Theory (Sweller, 1988) |
| 6 | **Progressive disclosure.** Wrap deep-dive content in `<details><summary>` tags, collapsed by default. | Nielsen Norman Group; CLT |
| 7 | **Action anchors.** Add "What's Next?" sections at decision points with concrete next steps. | Executive function support |
| 8 | **101 sidebars.** Add "What is X?" explanations for non-obvious technical terms. | Autism-friendly explicitness |
| 9 | **Emoji markers.** Add section-type markers (🔬 Research, 🏗️ Build, ✅ Done, ⚠️ Warning, 💡 Tip, ⚡ Quick Start). | Visual scanning support |
| 10 | **Source link.** Add a prominent link to the original full-spec document. | Traceability |
| 11 | **Glossary.** Append an expandable terminology glossary at the end. | Working memory burden reduction |

**NEVER list (from ADHDfy pipeline):**

- NEVER remove content from the original. ADHDfying reorganizes and simplifies; it never deletes.
- NEVER use justified text alignment.
- NEVER use pure black (#000000) on pure white (#FFFFFF).
- NEVER use italics for emphasis. Use bold.
- NEVER use red for errors without a companion icon or label.
- NEVER nest more than 3 levels deep.
- NEVER write paragraphs exceeding 4 sentences.
- NEVER skip the BLUF.
- NEVER leave jargon unexplained.
- NEVER use "click here" link text.

---

## 5. Motion and Animation

### 5.1 Reduce-Motion Defaults

**Cytognosis accessibility mandate:** Always honor `prefers-reduced-motion: reduce`. This is not optional.

```css
/* Respect user motion preferences globally */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Default: subtle transitions only */
:root {
  --transition-fast:    150ms ease-out;
  --transition-normal:  300ms ease-out;
  --transition-slow:    500ms ease-out;
}

/* Motion must be purposeful, never decorative */
.state-transition {
  transition: opacity var(--transition-fast),
              transform var(--transition-fast);
}
```

### 5.2 Purposeful Animation Guidelines

Chen et al. (2026) C7 (Ambient Transition Cues) rated lowest (M=2) because participants reported cues were "too subtle to notice during focused work." This reveals a key tension: animations must be noticeable enough to serve their purpose but restrained enough to avoid sensory overwhelm.

**Animation purpose hierarchy:**

| Purpose | Example | Duration | Allowed with Reduced Motion? |
|---|---|---|---|
| **Feedback** | Button press confirmation, save indicator | 100-200ms | Yes (instant state change only) |
| **State transition** | Panel opening, view switching | 200-300ms | No (instant cut) |
| **Spatial orientation** | Navigation transition, scroll position | 300-500ms | No (instant cut) |
| **Companion expression** | Rive avatar idle, listening, empathic states | Continuous loop | No (static pose) |
| **Celebration** | Streak milestone, goal completion | 500-800ms | No (static badge) |
| **Decorative** | Background particles, ambient effects | N/A | Never (off by default even without reduced-motion) |

**Rules for purposeful animation:**

1. Every animation must answer: "What does the user learn from this movement?" If nothing, remove it.
2. All continuous animations must pause when the browser tab loses focus.
3. No animation should block user interaction. Users can always click/tap during transitions.
4. Maximum three simultaneous animated elements on screen.
5. Looping animations require a visible pause/stop control (WCAG 2.2.2).

### 5.3 Gamification Tokens

Gamification elements support engagement without shame. These tokens define the visual language for achievements, streaks, and progress.

```css
/* Gamification tokens */
:root {
  /* Streak indicators: gentle, never punitive */
  --streak-active:      var(--color-mood-muted);    /* Violet-300 */
  --streak-skip:        var(--surface-card);          /* Neutral, no red */
  --streak-milestone:   var(--gradient-brand);        /* Brand gradient */

  /* Progress: always forward, never backward */
  --progress-fill:      var(--color-focus);           /* Azure */
  --progress-track:     var(--surface-card);          /* Subtle background */
  --progress-milestone: var(--color-mood);            /* Violet pulse */

  /* Achievement badges */
  --badge-earned:       var(--color-sleep);           /* Teal, calm success */
  --badge-locked:       var(--surface-card);          /* Neutral, not grayed-out */
  --badge-glow:         0 0 12px rgba(20, 163, 163, 0.3); /* Soft teal glow */
}

/* Gentle streak visualization */
.streak-day {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--streak-skip);       /* Default: neutral */
}

.streak-day[data-active="true"] {
  background: var(--streak-active);     /* Violet-300 when active */
}

/* NEVER: .streak-day[data-missed] { background: red; } */
/* Skip days are neutral, never punished visually */
```

---

## 6. Component Patterns

### 6.1 Forms and Inputs

**Evidence:** Chen et al. (2026) planning anxiety barrier; WCAG 3.3.2 (Labels); executive function support research.

Forms represent a high-friction interaction for ADHD users. Every form element should reduce the distance between intention and completion.

**Design rules:**

- **One-tap actions wherever possible.** Medication logging, mood check-ins, and quick captures should require a single tap.
- **Visible labels always.** Placeholder text is not a label. Labels remain visible above the input at all times.
- **Inline validation.** Validate as the user types, with gentle correction language. "Looks like an email address is needed here" not "Invalid email."
- **Progress saving.** Auto-save form state every 5 seconds. Users should never lose work due to distraction or context-switching.
- **Forgiving inputs.** Accept multiple date formats, phone number formats, and name formats. Parse generously; confirm explicitly.
- **Maximum 5 fields visible at once.** Group longer forms into steps with clear progress indicators.
- **Quick mood journaling.** Mood check-ins complete in under 3 minutes. Use emoji scales, slider controls, or single-tap selections rather than free-text fields.

```css
/* Form input styling for ND users */
.form-input {
  font-family: var(--font-body);
  font-size: var(--text-lg);           /* 18px minimum */
  padding: 12px 16px;
  border: 2px solid var(--surface-card);
  border-radius: 8px;
  background: var(--surface-elevated);
  color: var(--text-primary);
  transition: border-color var(--transition-fast);
  min-height: 48px;                    /* Touch target: 48px > 44px min */
}

.form-input:focus {
  border-color: var(--color-interactive);
  outline: 3px solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* Labels: always visible, always above */
.form-label {
  display: block;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

/* Inline validation: gentle language */
.form-hint {
  font-size: var(--text-sm);
  color: var(--text-muted);
  margin-top: 4px;
}

.form-error {
  font-size: var(--text-sm);
  color: var(--color-stress-muted);    /* Coral-300, not pure red */
  margin-top: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.form-error::before {
  content: "⚠️";                      /* Icon + text, never color alone */
}
```

### 6.2 Navigation

**Evidence:** WCAG 3.2.3 (Consistent Navigation); autism predictable-layout research; ADHD scanning behavior studies.

- **Persistent global navigation.** Main navigation remains visible (or one tap away) on every screen. Tab order follows visual layout.
- **Maximum 5-7 top-level items.** Miller's Law applies directly. Group secondary items in clearly labeled submenus.
- **Current location always visible.** Active nav item uses distinct visual treatment (bold + color indicator + background change). Breadcrumbs appear on nested pages.
- **Skip-to-content link.** Every page includes a skip-to-content link as the first focusable element.
- **Keyboard navigation.** All interactive elements reachable by Tab in logical order. Visible focus indicator: 3px Azure-300, 2px offset.
- **Consistent ordering.** Navigation items maintain the same order across all views, all sessions, all devices. No dynamic reordering based on "intelligence."

### 6.3 Notifications and Alerts

**Evidence:** Chen et al. (2026) C7 (ambient cues too subtle, M=2); relational accountability design implication; ADHD health app patterns.

Notifications represent a critical design tension: ADHD users need reminders but experience notification overload as a major stressor.

**Notification hierarchy:**

| Level | Purpose | Delivery | Visual Treatment |
|---|---|---|---|
| **Gentle nudge** | Pattern-based suggestion | In-app only, user-scheduled times | Muted card, dismissable, no sound default |
| **Check-in** | Daily planning prompt, mood check | User-chosen time + modality | Companion avatar animation, warm tone |
| **Alert** | Time-sensitive reminder | Push notification (if enabled) | Azure accent, brief vibration |
| **Urgent** | Safety-related, crisis resource | Prominent in-app + optional push | Coral accent with icon, non-dismissable until acknowledged |

**Rules:**

- Default to the gentlest notification level. Users opt into more prominent notifications.
- Never use red badges with counts. Replace with subtle dots.
- All notifications include a "Not now" action that reschedules rather than dismisses.
- Batch non-urgent notifications into a single daily summary rather than individual interruptions.
- Notification language is warm and non-punitive. "Ready to check in?" not "You haven't logged today."
- Multimodal delivery: users choose from visual, audio, haptic, or any combination per notification type.

### 6.4 Data Visualization

**Evidence:** Blue Lin (CHI 2024) progressive disclosure; Chen et al. (2026) Brain Weather Dashboard (M=5, highest rated); Paivio's Dual Coding Theory.

Data visualization for neurodivergent users follows Lin's progressive disclosure model:

**Layer 1: Metaphorical overview.** The Brain Weather Dashboard presents cognitive state as weather: "light fog with patches of clarity," "clear skies," "scattered showers." This metaphor externalizes cognitive state as environment rather than character, directly addressing Chen et al.'s finding that ADHD users internalize fluctuations as personal failure.

**Layer 2: Signal groups.** Individual cognitive signals (focus, energy, mood, sleep, stress) displayed as color-coded trend lines or simple gauges. Each signal uses its assigned color token.

**Layer 3: Raw data.** Detailed metrics available on demand via progressive disclosure. Expandable panels show timestamps, sensor sources, and numerical values.

**Visualization rules:**

- Always pair color with shape. Colorblind users must distinguish data by form, not color alone.
- Use the cognitive-signal color mapping consistently. Focus is always Azure. Mood is always Violet.
- Prefer simple visualizations (bar charts, trend lines, gauges) over complex ones (radar charts, heat maps, scatter plots).
- Label all axes, data points, and legends clearly. No jargon in visualization labels.
- Include a "What does this mean?" link on every chart that explains the data in plain language.
- Time axes should show relative time ("3 days ago") alongside absolute dates.
- Pattern recognition visualizations should highlight trends with narrative descriptions: "Your focus tends to peak in the afternoon" alongside the visual.

### 6.5 Progress and Achievement

**Evidence:** Chen et al. (2026) C3 Flexible Planning (M=5); gentle streaks principle; no-shame design.

Progress tracking must celebrate consistency without punishing gaps:

- **Dual-track goals.** Users set "ideal" (ambitious) and "baseline" (minimum effort) plans. Completing baseline counts as success. This directly implements Chen et al. C3, the co-highest-rated concept.
- **Gentle streaks.** Streaks count active days over a window, not consecutive days. "4 of 7 days this week" rather than "Streak: 4" (which implies day 5 resets to 0).
- **Forward-only progress.** Progress bars only grow; they never shrink. A missed day does not reduce progress.
- **Narrative reflection.** Weekly summaries use narrative form: "You captured 12 thoughts this week, mostly about [topic]. Your focus was strongest on Wednesday afternoon." This implements Chen et al. C13 (Weekly Narrative Reflection).
- **No comparison metrics.** Never show averages, percentiles, or peer comparisons. The only comparison is the user with their own historical pattern.
- **Celebration without pressure.** Milestone celebrations use the brand gradient and a brief, warm message. "Nice consistency this week" rather than "Keep your streak alive!"

---

## 7. Cytognosis Profile Integration

### 7.1 Companion Profile (ND-First)

The Companion profile is the primary neurodivergent-optimized experience. It serves as the default for Yar and all Cytognosis consumer-facing products.

**Core features:**

- **Brain Weather Dashboard** as the home view. Cognitive state displayed as weather metaphors with the Violet-anchored palette.
- **Gentle planning** with dual-track (ideal/baseline) goals and rhythm-based scheduling.
- **Companion presence** via Rive avatar with idle, listening, thinking, speaking, and empathic animation states.
- **Voice-first capture** with frictionless "brain dump" mode that structures messy input after capture, not during.
- **Flexible streaks** and forward-only progress tracking.

**ND design adaptations:**

| Element | Standard UI | Companion Profile Adaptation |
|---|---|---|
| Task status | "Overdue" in red | "Needs attention" in neutral tone, or silently rescheduled |
| Empty states | "You have no tasks" | "All clear for now. What's on your mind?" |
| Errors | "Error: invalid input" | "That didn't quite work. Here's what to try:" with specific guidance |
| Streaks | "Streak: 0 days" | "You've been active 4 of the last 7 days" |
| Reminders | "You missed your 2pm reminder" | "Still interested in [task]? No pressure." |
| Onboarding | 10-step setup wizard | 3-step essentials, everything else discoverable later |

### 7.2 Crisis Profile (Urgent States)

The Crisis profile activates during detected or user-declared emotional crisis states. It strips the interface to essential safety resources.

**Design principles:**

- Reduce to a single-column layout with maximum 3 visible actions.
- Increase font size by 25% and contrast to maximum AAA levels.
- Remove all decorative elements, animations, and non-essential information.
- Surface crisis resources (hotlines, grounding exercises, trusted contacts) prominently.
- Use Azure for primary actions, Coral for urgent/safety items only, neutral for everything else.
- Allow one-tap return to normal profile when the user is ready.

### 7.3 Clinical Profile (ND Adaptations)

The Clinical profile serves healthcare providers viewing patient-consented data. It maintains professional conventions while incorporating ND accessibility.

**ND adaptations for clinical view:**

- Support high-contrast mode for clinical environments with variable lighting.
- All data visualizations include redundant encoding (color + shape + label) for colorblind safety.
- Use the cognitive-signal color mapping with clinical labels (e.g., "Attention Index" alongside "Focus").
- Provide exportable summaries in both narrative and tabular formats.
- Respect the same typography standards (Lexend/Inter, 16px minimum, left-aligned).

### 7.4 Cross-Profile Accessibility

These accessibility features apply across all profiles without exception:

| Feature | Implementation | Standard |
|---|---|---|
| **Contrast** | Body text: 7:1 (AAA). Large text 18pt+: 4.5:1 (AAA). UI components: 4.5:1. | WCAG 2.1 AAA |
| **Text scaling** | Supports 200% browser zoom without layout breakage. | WCAG 1.4.4 |
| **Touch targets** | Minimum 44x44px (Cytognosis targets 48x48px). | WCAG 2.5.5 |
| **Focus indicators** | 3px Azure-300, 2px offset, visible on all interactive elements. | WCAG 2.4.7 |
| **Reduced motion** | Honors `prefers-reduced-motion: reduce`. All motion stops. | WCAG 2.3.3 |
| **Screen reader** | Semantic HTML, ARIA landmarks, heading order, alt text on all meaningful images. | WCAG 4.1.2 |
| **Keyboard access** | All interactive elements reachable by Tab in logical order. Skip-to-content link. | WCAG 2.1.1 |
| **Color independence** | Color never used as the sole conveyor of information. Always paired with icon, label, or pattern. | WCAG 1.4.1 |
| **Font selection** | User choice of Lexend, Inter, Atkinson Hyperlegible, or OpenDyslexic. | Beyond WCAG |
| **Spacing control** | User-adjustable line height, letter spacing, and paragraph spacing. | WCAG 1.4.12 |

---

## 8. Testing Checklist

### 8.1 Automated Checks

Run these automated checks on every pull request:

| Check | Tool | Threshold | Blocks PR? |
|---|---|---|---|
| Color contrast (all text) | axe-core or Lighthouse | WCAG AAA (7:1 body, 4.5:1 large) | Yes |
| Touch target size | axe-core | 44x44px minimum | Yes |
| Focus indicator presence | axe-core | All interactive elements | Yes |
| Heading hierarchy | axe-core | Sequential, no skips | Yes |
| Alt text coverage | axe-core | 100% meaningful images | Yes |
| ARIA landmark structure | axe-core | Main, nav, banner, contentinfo | Yes |
| `prefers-reduced-motion` support | Custom CSS lint | All animation declarations guarded | Yes |
| Paragraph length | Custom lint | Max 4 sentences | No (warning) |
| Line length | Custom lint | Max 80 characters | No (warning) |
| Font size minimum | Custom CSS lint | 16px body minimum | Yes |
| Color-alone information | Manual + axe-core | No color-only indicators | Yes |

### 8.2 Manual ND Testing Protocol

Conduct manual ND-focused testing quarterly and before major releases:

**Cognitive load assessment:**

- [ ] Complete the primary user flow (capture, plan, check-in) without referencing documentation.
- [ ] Count the number of decisions required per task. Target: fewer than 3 decisions for core flows.
- [ ] Verify that progressive disclosure works: collapsed content is non-essential; expanded content adds value.
- [ ] Test after a 10-minute distraction break: can you resume without reorientation?

**Sensory environment:**

- [ ] Enable `prefers-reduced-motion: reduce` and verify all animations stop.
- [ ] Test in a dark room and a bright room. Verify no glare or halation.
- [ ] Play all audio elements at default volume. Verify none are startling.
- [ ] Count animated elements visible simultaneously. Target: 3 or fewer.

**Predictability:**

- [ ] Navigate to every primary view. Verify navigation position and order remain consistent.
- [ ] Perform the same action (save, delete, create) in 3 different contexts. Verify identical behavior.
- [ ] Verify every interactive element has a visible label (not placeholder-only).
- [ ] Verify every action produces visible feedback within 100ms.

**Emotional safety:**

- [ ] Search all user-facing text for: "overdue," "missed," "failed," "behind," "you didn't." Zero tolerance.
- [ ] Verify streak displays use window-based counting ("4 of 7 days"), not consecutive.
- [ ] Verify empty states use warm, inviting language.
- [ ] Verify error messages include specific guidance and gentle tone.
- [ ] Verify no comparison metrics (averages, percentiles, rankings) appear anywhere.

**Customization:**

- [ ] Switch between all available fonts. Verify layout integrity with each.
- [ ] Increase font size to 200%. Verify no content overflow or truncation.
- [ ] Switch between dark, light, and high-contrast themes. Verify all content remains readable.
- [ ] Adjust notification preferences. Verify changes take effect immediately.

### 8.3 User Research Criteria

When recruiting neurodivergent participants for usability testing:

**Participant diversity requirements:**

- Include ADHD (inattentive, hyperactive-impulsive, and combined presentations), autism, dyslexia, and anxiety/depression profiles.
- Include both clinically diagnosed and self-identified participants (following Chen et al. methodology).
- Include a range of ages, occupations, and technology comfort levels.
- Minimum 5 participants per neurodivergent profile for qualitative insights (Nielsen's recommendation adapted for ND variability).

**Session accommodations:**

- Schedule sessions at participant-preferred times (respect circadian rhythm differences).
- Offer breaks every 20-25 minutes (Chen et al. included a 5-minute break in sessions exceeding 25 minutes).
- Provide tasks in written and verbal form simultaneously.
- Allow fidget tools and sensory comfort items.
- Use semi-structured interview format (rigid scripts increase anxiety).
- Compensate participants fairly ($40+ for 30-minute sessions, matching Chen et al.).

**Evaluation metrics:**

- **Task completion with minimal friction:** Can the user complete core flows without confusion or frustration?
- **Emotional response:** Does the interface feel safe, supportive, and non-judgmental? (Self-report on 5-point scale)
- **Cognitive load (subjective):** NASA-TLX adapted for ND users (simplified to 3 dimensions: mental demand, frustration, effort).
- **Return intention:** "Would you use this again tomorrow?" (Binary yes/no, the strongest predictor of ND app retention).

---

## 9. References

### Primary Research

1. Chen, J., Meng, Y., & Nie, K. (2026). "Not Just Me and My To-Do List: Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds." arXiv:2603.17258v2.
2. Lin, B. (2024). Health Data Visualization Design Principles for Neurodivergent Users. CHI 2024. [Blue Lin research]
3. Shaver-Troup, B. (2017). Lexend Font Reading Fluency Research. [Lexend typography evidence]
4. Braille Institute. (2020). Atkinson Hyperlegible Font. [Low-vision typography]

### Cognitive Science

5. Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two." Psychological Review, 63(2), 81-97. [Working memory limits]
6. Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning." Cognitive Science, 12(2), 257-285. [Cognitive Load Theory]
7. Paivio, A. (1986). Mental Representations: A Dual Coding Approach. Oxford University Press. [Dual Coding Theory]

### Color and Sensory Research

8. NIH / iMotions. Cool Colors and Anxiety Reduction. [Therapeutic color evidence]
9. Squirrelsong. Pastel Color Palettes for Reduced Sensory Overload. [Desaturated palette research]
10. Coding Horror. (2012). "Why You Should Never Use Pure Black for Text." [Halation evidence]
11. Chromotherapy research. Violet and emotional regulation. [Therapeutic wavelength evidence]

### Accessibility Standards

12. W3C. (2023). Web Content Accessibility Guidelines (WCAG) 2.2. [Accessibility criteria]
13. W3C. (2017). Web Content Accessibility Guidelines (WCAG) 2.1 Level AA/AAA. [Contrast, text scaling, touch targets]

### ADHD and Neurodiversity Design

14. Mostert, J. C., et al. (2018). Cognitive heterogeneity in adult ADHD. [Individual variation evidence]
15. Steel, P. (2007). Temporal Motivation Theory. [Procrastination and ADHD]
16. Stefanidi, E., et al. MoodGems: modular display for emotional expression in children with ADHD. [Co-design evidence]
17. Pulatova, I. & Kim, S. Customizable tabletop robots for sensory regulation. [ND-specific interaction design]

### Cytognosis Internal References

18. Cytognosis Design System. Section 11: Accessibility. Version 10.0. [Internal accessibility reference]
19. Cytognosis ADHDfy Pipeline. [Internal document transformation reference]
20. Yar Master Features and Requirements. (2026). [Product feature reference]
21. ADHD Paper Synthesis for Yar. (2026). [Internal research mapping]
