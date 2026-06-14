# Claude Design Prompt: Neurodiversity Testing Protocol

> Paste this prompt into Claude Design when you want to audit ND accessibility.
> Cytognosis context: nd-design-guide.md, 11_accessibility.md, companion-profile.md

---

## Brief

Build a comprehensive neurodiversity accessibility testing protocol for Cytognosis surfaces. This covers automated checks, manual testing with ND participants, heuristic evaluation, and WCAG 2.2 criteria mapping.

## 1. Automated Checks (CI-Blocking)

Run these checks on every PR that touches CSS, HTML, or JSX:

| Check | Tool | Threshold |
|-------|------|-----------|
| Text contrast ratio | axe-core | 7:1 body, 4.5:1 heading (WCAG AAA) |
| Touch target size | axe-core | 48px Companion, 56px Crisis |
| Font size minimum | stylelint | 17px body Companion, 18px Crisis |
| Line height minimum | stylelint | 1.5 general, 1.7 Companion |
| No pure black/white | stylelint | Reject `#000`, `#fff`, `#000000`, `#ffffff` |
| No italic emphasis | stylelint | `em { font-style: normal }` enforced |
| No justified text | stylelint | Reject `text-align: justify` |
| Animation duration | custom | 0ms when `[data-motion]` absent or `disabled` |
| No autoplay | custom | Reject `autoplay` attribute on media elements |
| Focus visible | axe-core | All interactive elements have visible focus |

## 2. Manual ND Testing Protocol

### 2.1 Participant Criteria
- Minimum 5 participants with self-identified neurodivergent conditions
- Mix: ADHD (2+), dyslexia (1+), autism spectrum (1+), anxiety/depression (1+)
- Ages 18-65, varying tech literacy
- Compensate fairly ($75/hour minimum)

### 2.2 Session Design
- Maximum 45 minutes (cognitive fatigue boundary)
- Breaks every 15 minutes (offer, do not require)
- Quiet, low-stimulation environment
- Screen recording with consent; no live observers behind glass
- Provide task list in writing before session starts
- Allow participants to skip any task without explanation

### 2.3 Task Categories

#### A. First Impressions (5 minutes)
- Show the main screen for 10 seconds, then ask: "What do you notice first?"
- "Does anything feel overwhelming or calming?"
- "Can you find the main action?"

#### B. Core Flow (15 minutes)
- Complete the primary task (e.g., log mood, review biomarker)
- Note: time to first action, errors, hesitations, re-reads
- Ask: "Was anything confusing?" after each step

#### C. Customization (10 minutes)
- Find and use the font toggle
- Find and use the density control
- Find and use the motion toggle
- Ask: "Which settings feel most comfortable?"

#### D. Notification Response (5 minutes)
- Trigger a test notification
- Measure: time to notice, time to act, emotional response
- Ask: "How did that feel? Too much? Too little?"

#### E. Recovery (5 minutes)
- Present an error state
- Can the participant recover without help?
- Is the next action clear?

## 3. Heuristic Evaluation Checklist

### 3.1 Cognitive Load
- [ ] Can the user complete the primary task without reading instructions?
- [ ] Is there only one primary CTA visible at a time?
- [ ] Are paragraphs 4 sentences or fewer?
- [ ] Is content width 65ch or less?
- [ ] Are form fields shown one at a time (wizard pattern)?
- [ ] Is progress visible (step indicators, progress bars)?

### 3.2 Distraction Audit
- [ ] Is there any moving element not initiated by the user?
- [ ] Are there any auto-playing media elements?
- [ ] Is the notification count 1 or fewer at a time?
- [ ] Are decorative elements minimal and non-distracting?
- [ ] Is the color palette muted (300-shade scale)?

### 3.3 Navigation Predictability
- [ ] Is the nav structure identical on every page?
- [ ] Are buttons in consistent positions across screens?
- [ ] Does every action produce immediate visual feedback?
- [ ] Are state indicators always visible (where am I, what is happening)?

### 3.4 Typography Comfort
- [ ] Can the user read for 10 minutes without eye strain?
- [ ] Is bold the only emphasis method (no italic, no underline)?
- [ ] Is text left-aligned (never justified)?
- [ ] Is the default font reading-fluency optimized (Lexend)?

### 3.5 Error Recovery
- [ ] Does every error state offer a clear next action?
- [ ] Are error messages non-punitive and specific?
- [ ] Can the user undo any destructive action?
- [ ] Is data auto-saved so nothing is lost?

## 4. WCAG 2.2 Criteria Mapping

| Criterion | Description | Target | Profile |
|-----------|------------|--------|---------|
| 1.4.3 | Contrast (minimum) | 4.5:1 text | All |
| 1.4.6 | Contrast (enhanced) | 7:1 body text | Companion, Crisis |
| 1.4.12 | Text Spacing adjustable | User density control | Companion |
| 2.2.2 | Pause, Stop, Hide | All motion user-controlled | Companion |
| 2.4.6 | Headings and Labels | Descriptive headings | All |
| 2.5.5 | Target Size (enhanced) | 44px+ (48px Companion, 56px Crisis) | Companion, Crisis |
| 3.2.3 | Consistent Navigation | Nav identical across pages | All |
| 3.3.2 | Labels or Instructions | Visible label on every field | All |
| 3.3.7 | Redundant Entry | No re-entering previously provided info | Companion |
| 3.3.8 | Accessible Authentication | No cognitive function tests | All |

## 5. Reporting Template

After testing, produce a report with:

1. **Summary**: pass/fail counts by category
2. **Critical findings**: any issue that blocks task completion
3. **Comfort findings**: issues that cause discomfort but not failure
4. **Participant quotes**: direct feedback (anonymized)
5. **Recommendations**: prioritized fix list with effort estimates
6. **Before/after screenshots**: for each recommended fix
7. **Retest plan**: timeline for verifying fixes

## 6. Frequency

| Trigger | Test Type |
|---------|-----------|
| Every PR (CSS/HTML/JSX) | Automated checks (CI) |
| Monthly | Heuristic evaluation (internal) |
| Quarterly | Manual ND testing (external participants) |
| Major release | Full protocol (automated + heuristic + manual) |
| New profile or component | Manual ND testing for that surface |
