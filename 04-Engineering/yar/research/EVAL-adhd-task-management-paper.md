> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `adhd`, `research`, `task-management`, `feature-prioritization`

# Research Synthesis: "Not Just Me and My To-Do List"

**Paper**: "Not Just Me and My To-Do List": Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds
**arXiv**: [2603.17258](https://arxiv.org/abs/2603.17258) — accepted to CSCW 2026
**Authors**: Jingruo Chen (Cornell), Yibo Meng (Tsinghua), Kexin Nie (University of Sydney)

---

## BLUF

Task management failure in adults with ADHD is fundamentally relational and affective, not cognitive or willpower-based; existing tools fail because they assume a neurotypical, solo, linear user. The strongest design signal from 42 participants across two studies is demand for **AI-augmented social scaffolding**: simulated co-presence, mood-adaptive planning, and co-regulation built into the core architecture. Yar's CSP (Cytonome Sensor Protocol; formerly USAP/UBAP) and CAP sensor-and-companion architecture directly instantiates what this paper calls for; this paper provides empirical grounding and grant-ready framing for that architecture.

---

## Paper Overview

| Field | Detail |
|---|---|
| **Venue** | CSCW 2026 (accepted) |
| **Submission date** | March 18, 2026 (revised April 20, 2026) |
| **Study 1** | 22 semi-structured interviews, ADHD-identifying adults (16 clinically diagnosed, 6 strongly self-identified), 25-35 min each, $40 compensation |
| **Study 2** | 20-participant speed-dating study with 13 speculative AI design concepts, 25-35 min each, separate cohort |
| **Total N** | 42 ADHD-identifying adults |
| **Age range** | 18-55 |
| **Occupations** | Students, office workers, teachers, doctors, farmers, delivery workers |
| **Methods** | Hybrid inductive thematic analysis (two-coder), Likert ratings (1-5) for speed-dating concepts |
| **Analysis** | Thematic coding; Davidoff et al. speed-dating protocol |

---

## Key Challenges Identified

| Challenge | ADHD Mechanism | Current Tool Failure | Yar Opportunity |
|---|---|---|---|
| **Task initiation paralysis** | Psychological inertia; executive dysfunction prevents transition to action even when intent is present | To-do lists assume initiation capacity; apps require the user to open them | Proactive sensor-triggered check-ins (CSP); CAP "comes to the user" |
| **Time perception disorders** | Chronic misestimation; planning calibrated to rare hyperfocus states, not average states | Calendars impose fixed grid time; no fallback plan | Dual "ideal/baseline" plan modes; rhythm-based scheduling |
| **Deadline addiction** | Crisis-driven dopamine spike needed to mobilize effort; adrenaline dependency | No graduated urgency system; binary "done/not done" | Pattern detection for recurring friction; gentle pre-deadline nudges |
| **Emotional dysregulation** | Rapid mood swings derail entire days; emotional avoidance of low-meaning tasks | No mood context in task presentation; rigid task ordering | Morning mood check-in; mood-adaptive task suggestion |
| **Planning anxiety** | Formalized plans trigger shame spirals because the user predicts their own non-compliance | Plans are all-or-nothing; missed tasks shown as failures | Non-penalizing "undo" and streak preservation through partial completion |
| **Social misrecognition** | Internalized stigma from years of being labeled "lazy"; distrust of own capacity | Tools don't validate or normalize ADHD patterns | Non-judgmental language; "brain weather" framing; narrative summaries |
| **Unequal social scaffolding access** | Efficacy depends on body-doubling and co-regulation; unavailable when living alone | Tools designed for solo use; no simulated co-presence | AI social presence ("body double") mode; shared planning with trusted person |
| **Tool over-reliance/avoidance** | Elaborate planning becomes procrastination when disconnected from social accountability | Planning affordances are separated from execution triggers | Social accountability tied directly to task activation |
| **Institutional misalignment** | Neurotypical workplaces (open offices, rigid deadlines) amplify cognitive load | Productivity tools reflect and reinforce neurotypical norms | Burnout detection; "pause day" suggestions; sensory accommodation framing |

---

## Feature Gaps: What No Current Tool Implements

Listed by priority relevance to Yar.

### Priority 1: Core Gaps (Yar must address)

1. **AI body doubling / social presence mode**: A simulated co-presence that provides quiet companionship during work without oversight. Rated highest or near-highest by most participants (Concept 6). No current mainstream productivity tool implements this.

2. **Mood-adaptive task load**: Morning check-in that dynamically adjusts the day's task presentation based on self-reported or inferred emotional state. Not implemented in any major task app (Todoist, Things, Notion, Asana).

3. **Dual plan mode (ideal + baseline)**: User sets an ambitious plan and a minimum viable plan; system shifts to baseline without shame signaling or streak loss when energy dips. Concept 3 was among the top 3 for 7 of 20 speed-dating participants.

4. **Non-judgmental task collapse recovery**: After abandoning a task, the system offers a gentle debrief rather than displaying it as an overdue failure. Distinct from simple task deletion; it is a reflective scaffold.

5. **Burnout / "pause day" detection**: System proactively suggests rest when behavioral patterns suggest overload. Currently absent from all surveyed tools.

### Priority 2: High Value, Differentiating

6. **Brain-weather cognitive state visualization**: Metaphorical, non-stigmatizing representation of cognitive states (e.g., "light fog," "clear skies") rather than productivity metrics. Concept 8 was the single most preferred concept overall.

7. **Pattern-based friction nudges**: Adaptive detection of recurring struggle points (e.g., "you always miss morning writing sessions") with context-sensitive schedule adjustment suggestions.

8. **Shared planning with trusted person**: Optional sharing of daily plan with one designated person for lightweight encouragement, not supervision. Distinct from social media sharing or team dashboards.

### Priority 3: Valuable But Context-Dependent

9. **Private emotional notes before planning**: A scratchpad for mood capture before task-setting; private, never used for scheduling. Low stakes, low cost to implement.

10. **Ambient transition cues**: Non-verbal, gentle sensory signals (soft sounds, color shifts) for focus/break transitions rather than alarm-style notifications.

11. **Narrative weekly summary**: User narrates their week in natural language rather than viewing analytics. Preferred by reflective users; not universally valued.

12. **Emotional inventory before new commitments**: Prompt asking "Do you have energy for this?" before the user accepts a new task. Mixed reception due to friction at high-motivation moments.

---

## Language and Framing

Terms and framings from this paper that are directly useful for describing Yar features in grants, proposals, and product copy.

| Term | Paper Definition | Yar Application |
|---|---|---|
| **Social scaffolding** | External relational supports (people, tools, shared presence) that compensate for executive function deficits | Describes Yar's co-presence and accountability features |
| **Body doubling** | The practice of working in the presence of another person (physically or virtually) to support task engagement | Direct name for Yar's AI social presence mode |
| **Co-regulation** | Emotional and behavioral regulation achieved through interaction with another person or system, not in isolation | Core design principle for CAP architecture |
| **Affective co-construction** | Task management as a jointly produced emotional and relational act, not a solo cognitive one | Frames why sensor data + social context = superior to to-do lists alone |
| **External accountability** | Borrowing structure from relationships to substitute for internally generated self-regulation | Names the mechanism behind shared planning and check-in features |
| **Nonlinear attention rhythms** | The oscillation between hyperfocus and inattention that characterizes ADHD time experience | Justifies rhythm-based (vs. grid-based) scheduling design |
| **Executive function prosthetics** | Technology or social arrangements that substitute for impaired self-regulation capacities | Positions Yar as prosthetic infrastructure, not lifestyle app |
| **Distributed regulation** | Regulatory capacity spread across people, tools, and environments rather than residing in the individual | Grounds the sensor-plus-companion architecture philosophically |
| **Neurotypical infrastructure** | Institutional and tool design built around assumptions of stable attention and linear time | Names what existing tools assume and what Yar rejects |
| **Psychological inertia** | The inability to transition into action despite cognitive intent; distinct from lack of motivation | Precisely names the initiation problem Yar's proactive triggers address |
| **Planning fallacy** | Systematic overestimation of task completion capacity based on rare peak states | Justifies dual plan mode and dynamic replanning |
| **Failure spirals** | Cascading shame from missed tasks that further reduces capacity to act | Names what Yar's non-judgmental design must interrupt |

---

## AI-Augmented Social Scaffolds: Paper Proposals and Yar Mapping

The paper argues that ADHD task management requires moving from "solo optimization" to "relational co-regulation." It proposes five design principles, each mapping to Yar architecture:

### 5.1 Relational Accountability (not solo optimization)
**Paper**: AI should simulate attentive companionship; check-ins that reproduce social pressure without surveillance or shame.
**Yar mapping**: CAP (Companion AI Platform) with proactive check-in cadence; CSP edge sensor detecting behavioral state transitions and triggering CAP prompts.

### 5.2 Time as Rhythm (not grid)
**Paper**: Replace fixed calendars with energy-flow framing; ideal/baseline dual plans; preserve streaks through partial completion.
**Yar mapping**: Rhythm-mode scheduling in Yar app; sensor-inferred energy state feeding into dynamic plan adjustment.

### 5.3 Mood-Adaptive Interfaces (prevent failure spirals)
**Paper**: Emotional state check-ins that alter task presentation; affirming messages when load is reduced; non-judgmental progress framing.
**Yar mapping**: Morning mood check-in (CAP); CSP physiological signals (HRV, movement, sleep) contributing to inferred readiness state; adaptive task queue.

### 5.4 Affirming Neurodivergent Cognition (not pathologizing)
**Paper**: Ambient metaphors (brain weather); non-judgmental indicators; task decomposition without overwhelm.
**Yar mapping**: Cytonome edge AI framing cognitive state as health coordinates, not deficits; language layer in CAP trained on affirming, non-deficit framing.

### 5.5 Co-Regulation as Core Infrastructure
**Paper**: Live focus rooms; shared timelines with AI or human partners; distributed accountability ecosystem.
**Yar mapping**: This is the architectural thesis of Yar. CSP provides the ambient sensing; CAP provides the relational layer; the combination enables co-regulation as infrastructure rather than an add-on.

---

## Direct Quotes

Selected for grant writing and feature justification. Max 10, with context.

1. **On initiation paralysis** (P17, 22-year-old office worker):
   > "I obviously want to brush my teeth and wash my face, but I stay in bed all the time; there will be a big start-up difficulty."
   *Context*: Illustrates that initiation failure extends beyond work tasks to basic daily function; not motivational.

2. **On time perception** (P5, 22-year-old student):
   > "Unless I pay special attention, my perception of time is as if I want to deliberately forget it."
   *Context*: Supports sensor-based time anchoring as an accessibility need, not a preference.

3. **On deadline dependency** (P1, 19-year-old student):
   > "I feel that I have formed a kind of satisfaction [from] this kind of dependence on pressure."
   *Context*: Names the crisis-productivity cycle; justifies graduated urgency features.

4. **On self-blame compounding failure** (P17):
   > "I often blame myself for a moment of distraction and the originally thought-out plan keeps getting tangled in my brain."
   *Context*: Failure spirals are the mechanism; non-judgmental design is the intervention.

5. **On planning anxiety** (P10, 33-year-old manager):
   > "Every time I write a plan, I get anxious because I know I won't follow it."
   *Context*: Rigid planning tools cause net harm for ADHD users; dual-mode and undo features are therapeutically motivated.

6. **On self-sabotage** (P1):
   > "If I really succeed, it will be very hard to maintain. I might as well smash this possibility with my own hands."
   *Context*: Fear of unsustainable success; Yar's rhythm-based sustainability framing directly addresses this.

7. **On social scaffolding fragility** (P11, 33-year-old teacher):
   > "If it's only me reminding myself, it just becomes invisible after a few days."
   *Context*: Justifies persistent, relational accountability over one-time tool setup.

8. **On borrowed executive function** (P17):
   > "My friend calls me to remind me to get up and do things. Without that, I might just stay in bed all day."
   *Context*: Human body doubling as current gold standard; Yar's AI social presence is a scalable substitute.

9. **On peer community as only safe space** (P13, 45-year-old office worker):
   > "Only in the ADHD group do I feel that I can tell the truth."
   *Context*: Non-ADHD environments require masking; Yar's design must be a safe, unmasked context.

10. **On feeling seen** (S5, speed-dating participant):
    > "I hope my emotions are seen, I hope I am seen and understood."
    *Context*: The emotional need driving demand for all top-rated design concepts; "being seen" is the core user need.

---

## Yar Feature Prioritization Implications

Based on the paper's empirical findings and speed-dating ratings. Listed in order of justification strength.

| Priority | Feature | Rationale from Paper |
|---|---|---|
| **P0** | Proactive AI check-in (CAP) that initiates contact without requiring user to open app | Initiation paralysis is the #1 barrier; "I hope the system comes to me instead of me opening it" (P14). Concept 2 directly addresses this. |
| **P0** | AI body doubling / social presence mode | Concept 6 was top-3 for 11/20 speed-dating participants; body doubling is the single most effective existing ADHD coping strategy per interviews. |
| **P0** | Morning mood check-in feeding adaptive task queue | Mood-adaptive task presentation is the most common unmet expectation from interview phase; P1: "ask me every day: How are you doing now?" |
| **P1** | Dual plan mode (ideal + baseline) with non-penalizing streak handling | Concept 3 top-3 for 7/20; directly addresses over-planning/shame cycle that causes tool abandonment. |
| **P1** | Brain-weather cognitive state visualization (non-metric) | Concept 8 was the single highest-rated concept across the full speed-dating study; metaphorical framing reduces stigma and shame. |
| **P1** | Burnout / pause day detection with proactive rest suggestion | Concept 11 was top-3 for 8/20 participants; early burnout intervention is clinically meaningful and currently absent from all tools. |
| **P2** | Non-judgmental task collapse recovery (debrief after abandonment) | Failure spirals are a key harm mechanism; gentle debrief after task abandonment breaks the cycle without requiring therapist involvement. |
| **P2** | Pattern-based nudges (detect recurring friction, suggest schedule adjustment) | Concept 10 valued by analytical users; sensor data from CSP makes this uniquely achievable for Yar vs. software-only competitors. |
| **P2** | Shared plan with trusted person (lightweight, non-supervisory) | Concept 5 valued by subset; bridges AI and human scaffolding; important for users whose human networks are strong but need a coordination layer. |
| **P3** | Ambient transition cues (non-alarm, sensory) | Concept 7 lowest-rated overall due to subtlety; implement as optional, highly configurable; may be high-value for specific sensory profiles. |
| **P3** | Adaptive "undo" button for task removal without shame | Concept 9 useful for anxiety reduction but raised procrastination concerns; implement with friction intentionally built in. |

### Architectural note for engineers

The paper's top-ranked concepts (8, 6, 11, 3) share a common architecture: they require **ambient state sensing**, **emotional state modeling**, and **proactive output**. This is not achievable in a software-only app. CSP's role as the sensing layer (physiological signals, movement, time-of-day) feeding CAP's relational output layer is the architectural requirement implied by this research. The paper's "design implication 5.5" (co-regulation as core infrastructure) is a direct description of the CSP-CAP integration pattern.

---

## See Also

- [sensor-architecture.md](../../../03-Products/Cytonome/Yar/sensor-architecture.md)
- [yar-product-feature-master.md](../../../03-Products/Cytonome/Yar/yar-product-spec.md)
- [yar-product-implementation.md](../../../03-Products/Cytonome/Yar/yar-product-spec.md)
