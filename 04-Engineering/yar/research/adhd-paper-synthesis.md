# ADHD Task Management Paper Synthesis — Mapping Chen, Meng & Nie (2026) to Yar

> **Paper**: "Not Just Me and My To-Do List: Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds"
> **Authors**: Jingruo Chen, Yibo Meng, Kexin Nie
> **Source**: arXiv:2603.17258v2, April 2026
> **Date**: 2026-05-31
> **Status**: Living synthesis document

---

## 1. Executive Summary

This paper presents the strongest empirical foundation to date for exactly the kind of cognitive companion Yar aims to be. Through 22 semi-structured interviews and 20 speed-dating sessions with ADHD-identifying adults, Chen et al. demonstrate that task management for adults with ADHD is relationally and affectively co-constructed, not an isolated act of individual willpower. The paper's core argument — that productivity tools designed around neurotypical assumptions (stable attention, linear time, individual self-regulation) actively harm ADHD users — validates Yar's foundational design principles.

The study surfaces three major insight clusters. First, ADHD task management challenges span internal cognitive-emotional barriers, relational-sociocultural misrecognition, and systemic-structural misalignments. Second, participants compensate through social dynamics (body doubling, peer communities) and technological tools used as externalized cognition. Third, speed-dating evaluation of 13 speculative AI concepts reveals that adults with ADHD most value emotional understanding (Concept 8: Brain Weather Dashboard, M=5), supportive presence (Concept 6: Social Presence AI, M=4.5), adaptive rest (Concept 11: Emotionally Aware Pause Days, M=4.5), and flexible planning (Concept 3: Flexible Planning and Gentle Streaks, M=5).

The paper generates five design implications that map directly to Yar's architecture: relational accountability over solo optimization, time as rhythm rather than grid, mood-adaptive interfaces, affirming neurodivergent cognition, and co-regulation as core infrastructure. Every one of these aligns with Yar's existing design principles and fills specific feature gaps in the current roadmap.

---

## 2. The 13 Design Concepts — Evaluation and Yar Mapping

The speed-dating study evaluated 13 speculative concepts across four task management phases: planning, execution, adaptation, and post-task reflection. Twenty participants rated each on a 1-5 Likert scale. The following analysis integrates ratings, qualitative feedback, and Yar feature mapping.

### 2.1 Planning Phase Concepts

#### Concept 1: Private Emotional Notes Before Planning

| Attribute | Detail |
|---|---|
| **Description** | A private text box appears when users begin planning. Users jot mood notes or emotional reflections. Notes are not used for scheduling suggestions — they serve purely for emotional self-awareness. |
| **Median Rating** | M=3 |
| **Key Quotes** | Perceived as "useful for emotional expression but unnecessary within task-focused workflows." |
| **Design Implication** | Mood-adaptive interfaces; emotional self-awareness |
| **Yar Mapping** | Maps to Yar's existing **reflection prompting** capability (Tier 2, Skill Building). Implement as an optional pre-planning check-in within the gentle planning flow. |
| **Priority** | Low — integrate into broader mood-adaptive system rather than as standalone feature |

#### Concept 2: Mood-Aware Daily Companion

| Attribute | Detail |
|---|---|
| **Description** | An AI checks in each morning with a friendly greeting, asks how the user is feeling, and provides personalized daily suggestions balanced between ambition and realism. |
| **Median Rating** | M=3 |
| **Key Quotes** | Participants valued the relational tone but worried about it becoming "another notification to dismiss." |
| **Design Implication** | Relational accountability; mood-adaptive interfaces |
| **Yar Mapping** | Maps directly to Yar's **gentle planning** capability ("What should I focus on today?"). Enhance with mood-aware input: Yar's morning prompt adapts based on detected vocal biomarkers and user self-report. |
| **Priority** | High — core differentiator, already partially implemented |

#### Concept 3: Flexible Planning and Gentle Streaks

| Attribute | Detail |
|---|---|
| **Description** | Users set "ideal" (ambitious) and "baseline" (minimum effort) plans. When energy dips, the system shifts to baseline without resetting progress streaks. Streaks are preserved even on skip days. |
| **Median Rating** | **M=5** (highest co-rated) |
| **Key Quotes** | S14: "This stopped me from hating myself for not completing everything." S19: flexibility made attention "feel developable over time." Some cautioned excessive flexibility could become demotivating. |
| **Design Implication** | Time as rhythm; affirming neurodivergent cognition |
| **Yar Mapping** | Maps to Yar's **"No shame, ever"** design principle. Yar already rejects streaks, red overdue tasks, and productivity language. This concept validates that approach AND provides a constructive alternative: dual-track goals that normalize partial completion. |
| **Priority** | **Critical** — implement dual-track planning as core gentle planning UX |

#### Concept 4: Emotional Inventory Before New Commitments

| Attribute | Detail |
|---|---|
| **Description** | Reflective prompts appear when users accept new tasks: "Do you have the energy for this right now?" "Would you like to schedule this for a time that suits your brain better?" |
| **Median Rating** | **M=2** (among lowest) |
| **Key Quotes** | Mixed: some valued it as a private outlet, others felt it "introduced friction during moments of high motivation or impulsive task acceptance." Appeared in least-preferred lists of 10 participants. |
| **Design Implication** | Mood-adaptive interfaces |
| **Yar Mapping** | Implement as a **configurable Just-In-Time Adaptive Intervention (JITAI)**, not a mandatory gate. Yar surfaces the prompt only when patterns suggest overcommitment (e.g., three new tasks added in rapid succession). |
| **Priority** | Low — optional, pattern-triggered only |

#### Concept 5: Shared Planning with a Trusted Person

| Attribute | Detail |
|---|---|
| **Description** | Users share daily plans with a trusted friend, coach, or partner. That person can see the plan, send brief encouragements, or simply acknowledge intentions without acting as a supervisor. |
| **Median Rating** | M=3 |
| **Key Quotes** | S9 valued gentle accountability. S4 questioned "whether supportive relationships between family or friends should require AI mediation." Some found it intrusive or emotionally demanding. |
| **Design Implication** | Co-regulation as core; relational accountability |
| **Yar Mapping** | Maps to Yar's **persistent relational context** (Tier 3). Design as opt-in shared visibility with granular controls: what to share, with whom, and what kind of response is welcome. Never default to sharing. |
| **Priority** | Medium — implement after core companion features are solid |

### 2.2 Execution Phase Concepts

#### Concept 6: Social Presence AI During Work

| Attribute | Detail |
|---|---|
| **Description** | An AI companion simulates body doubling: staying present through animated timers, gentle prompts, or silent visual presence. Users toggle between active support (encouraging messages) and silent companionship. |
| **Median Rating** | **M=4.5** (second highest) |
| **Key Quotes** | S2: "a partner who understands and supports and doesn't judge." S6: useful when human companionship is unavailable. S7: compared AI to the rose in *The Little Prince*, valuing emotional reassurance over productivity gains. Appeared in top-3 of 12 participants. |
| **Design Implication** | Co-regulation as core; relational accountability |
| **Yar Mapping** | Maps directly to Yar's **Rive persona animation** (idle → listening → thinking → speaking → empathic states). This concept validates Yar's animated companion as a body-doubling proxy. Implement as a **focus companion mode**: Yar's avatar remains visible during work, providing ambient presence without interruption. |
| **Priority** | **Critical** — core persona/companionship feature, partially designed |

#### Concept 7: Ambient Transition Cues

| Attribute | Detail |
|---|---|
| **Description** | Gentle, non-verbal signals (calming soundscapes, color shifts, soft chimes) indicate focus periods, task transitions, or breaks. Replaces standard notifications. |
| **Median Rating** | **M=2** (lowest co-rated) |
| **Key Quotes** | "Too subtle to notice during focused work." Several participants reported they would "miss them entirely." Appeared in least-preferred lists of 11 participants. |
| **Design Implication** | Mood-adaptive interfaces; affirming neurodivergent cognition |
| **Yar Mapping** | Keep as **supplementary**, not primary. Offer ambient cues as a customizable layer within Yar's notification system. Primary transitions should use multimodal cues (voice + visual + haptic) as participants requested. |
| **Priority** | Low — customization option, not default behavior |

#### Concept 8: Brain Weather Visualization Dashboard

| Attribute | Detail |
|---|---|
| **Description** | A dynamic, metaphorical display of cognitive states using weather metaphors: "light fog with patches of clarity," "clear skies," "scattered showers." Helps users understand fluctuating mental conditions and encourages self-compassion. |
| **Median Rating** | **M=5** (highest co-rated) |
| **Key Quotes** | S5: "I hope my emotions are seen, I hope I am seen and understood." S9: described "mild haze" as "more comforting than red overdue tasks — poetic and calming." Appeared in top-3 of 13 participants (most frequent). |
| **Design Implication** | Affirming neurodivergent cognition; time as rhythm |
| **Yar Mapping** | Maps to Yar's **paralinguistic sensing** (Layer 2.4: emotion sensing via HuBERT, openSMILE) and **longitudinal vocal biomarker tracking** (Tier 3). Implement as Yar's primary self-awareness interface: a brain weather metaphor replaces conventional productivity dashboards. Vocal biomarkers, self-reported mood, and activity patterns feed the weather model. |
| **Priority** | **Critical** — highest-rated concept; defines Yar's unique visual language |

### 2.3 Adaptation Phase Concepts

#### Concept 9: Adaptive Planning Undo Button

| Attribute | Detail |
|---|---|
| **Description** | Users withdraw tasks from their schedule without penalty when plans change. A "soft reset" without judging missed tasks. |
| **Median Rating** | M=2.5 |
| **Key Quotes** | S11: reduced anxiety about committing to plans. Others raised concerns about "enabling procrastination." |
| **Design Implication** | Time as rhythm; mood-adaptive interfaces |
| **Yar Mapping** | Implement as a natural extension of **dual-track planning** (Concept 3). Tasks are never "overdue" in Yar — they are rescheduled, descoped, or released. No language of failure. |
| **Priority** | Medium — embedded in planning system design |

#### Concept 10: Pattern-Based Gentle Nudges

| Attribute | Detail |
|---|---|
| **Description** | The system detects recurring friction points (e.g., always missing morning writing sessions) and offers context-sensitive suggestions like "Would you like to move this task to tomorrow afternoon?" |
| **Median Rating** | M=3 |
| **Key Quotes** | S2: felt the system "acknowledged emotions without materially helping." S14: "Even if I know it's trying to help, it feels like it's watching me." Others appreciated alignment with personal rhythms. |
| **Design Implication** | Time as rhythm; mood-adaptive interfaces |
| **Yar Mapping** | Maps to Yar's **pattern surfacing** capability (Tier 2). Critical design constraint: frame as insight rather than instruction. "You've been more productive in afternoons this week" vs. "Move your task to the afternoon." User controls nudge frequency, tone, and content. |
| **Priority** | Medium — requires longitudinal data collection first |

#### Concept 11: Emotionally Aware Pause Days

| Attribute | Detail |
|---|---|
| **Description** | The system proactively suggests a pause day when it detects signs of burnout. Offers self-care options like journaling or low-pressure creative tasks. |
| **Median Rating** | **M=4.5** (second highest) |
| **Key Quotes** | S1: sadness "often became apparent only when overwhelming." S17: "earlier intervention might have prevented burnout." Some raised concerns about misinterpretation. |
| **Design Implication** | Time as rhythm; mood-adaptive interfaces |
| **Yar Mapping** | Maps to Yar's **vocal biomarker tracking** and **emotional aftercare**. Implement as a JITAI triggered by converging signals: declining vocal energy, reduced capture frequency, self-reported low mood. Frame rest as care, not failure. |
| **Priority** | **High** — directly addresses burnout prevention, a core Yar value proposition |

### 2.4 Post-Task Reflection Concepts

#### Concept 12: Emotional Debrief After Task Collapse

| Attribute | Detail |
|---|---|
| **Description** | When users abandon a task, the system offers a non-judgmental reflection space. Asks gentle questions like "Want to reflect on what got in the way?" |
| **Median Rating** | M=3 |
| **Key Quotes** | S16 and S5 valued reflection. Others worried about "revisiting failure too directly." |
| **Design Implication** | Relational accountability; mood-adaptive interfaces |
| **Yar Mapping** | Maps to Yar's **emotional aftercare** and **replay loop interruption** capabilities. Implement with opt-in framing: "Would you like to think about this?" not "Let's debrief what happened." Structured reflection helps break rumination cycles. |
| **Priority** | Medium — important but requires careful tone calibration |

#### Concept 13: Weekly Narrative Reflection Instead of Analytics

| Attribute | Detail |
|---|---|
| **Description** | Users narrate their week in their own words instead of viewing quantitative analytics. Asks: "What surprised you? What felt unexpectedly hard?" |
| **Median Rating** | M=3 |
| **Key Quotes** | "Generally useful for sensemaking but not distinctive." Narrative alone may be "insufficient without additional scaffolding." |
| **Design Implication** | Affirming neurodivergent cognition |
| **Yar Mapping** | Maps to Yar's **reflection without judgment** (Tier 3). Combine with Brain Weather historical view: users narrate while viewing their cognitive weather patterns over the week. The narrative adds meaning to the data; the data adds grounding to the narrative. |
| **Priority** | Medium — implement alongside Brain Weather Dashboard |

### 2.5 Concept Ratings Summary

| Concept | Phase | Median | Top-3 Count | Least-3 Count | Yar Priority |
|---|---|---|---|---|---|
| C8: Brain Weather Dashboard | Execution | **5** | **13** | 0 | **Critical** |
| C3: Flexible Planning + Gentle Streaks | Planning | **5** | 10 | 1 | **Critical** |
| C6: Social Presence AI | Execution | **4.5** | **12** | 1 | **Critical** |
| C11: Emotionally Aware Pause Days | Adaptation | **4.5** | **12** | 0 | **High** |
| C2: Mood-Aware Daily Companion | Planning | 3 | 0 | 2 | High |
| C12: Emotional Debrief After Collapse | Reflection | 3 | 3 | 4 | Medium |
| C5: Shared Planning w/ Trusted Person | Planning | 3 | 4 | 5 | Medium |
| C13: Weekly Narrative Reflection | Reflection | 3 | 0 | 3 | Medium |
| C10: Pattern-Based Gentle Nudges | Adaptation | 3 | 0 | 3 | Medium |
| C1: Private Emotional Notes | Planning | 3 | 2 | 2 | Low |
| C9: Adaptive Planning Undo | Adaptation | 2.5 | 1 | 5 | Medium |
| C4: Emotional Inventory Before Commitments | Planning | **2** | 0 | **10** | Low |
| C7: Ambient Transition Cues | Execution | **2** | 1 | **11** | Low |

---

## 3. Challenge Framework — Mapped to Yar Features

### 3.1 Internal Cognitive and Emotional Barriers (Section 4.1)

| Challenge | Paper Evidence | Yar Feature Response |
|---|---|---|
| **Task initiation paralysis** | "I obviously want to brush my teeth and wash my face, but I stay in bed all the time; there will be a big start-up difficulty." (P17) | **Voice capture** (frictionless start: "Hey Yar" begins interaction), **Social Presence AI** (body-doubling reduces initiation barrier), **Spiciness slider** (micro-step decomposition from Goblin Tools pattern) |
| **Hyperfocus and flow states** | "When it's something I really like, I can write for ten hours straight, and it feels effortless." (P13) | **Break reminders** (from Super Productivity pattern), **Emotionally Aware Pause Days** (burnout prevention), **Brain Weather Dashboard** (awareness of state transitions) |
| **Time perception disorders** | "Unless I pay special attention, my perception of time is as if I want to deliberately forget it." (P5) | **Time estimation** (Goblin Tools pattern), **Flexible Planning** (dual-track ideal/baseline), **Rhythm-based scheduling** (energy flows, not hourly grids) |
| **Deadline addiction** | "I feel that I have formed a kind of satisfaction [from] this kind of dependence on pressure." (P1) | **Gentle planning** (proactive structure without crisis dependency), **Pattern surfacing** ("You tend to finish things 2 days before deadline — what if we started the ramp earlier?") |
| **Emotional avoidance of low-meaning tasks** | Tasks without personal relevance become "emotionally aversive" (P4, P8, P12) | **Communication Coach** (reframe task purpose), **Mood-aware planning** (sequence aversive tasks strategically), **Spiciness slider** (make aversive tasks feel smaller) |
| **Emotional fluctuations and self-blame** | "I often blame myself for a moment of distraction and the originally thought-out plan keeps getting tangled in my brain." (P17) | **Brain Weather Dashboard** (normalize fluctuations as weather, not failure), **Emotional aftercare** (structured debrief after setbacks), **No shame design principle** |
| **Fear of sustainability** | "If I really succeed, it will be very hard to maintain. I might as well smash this possibility with my own hands." (P1) | **Gentle streaks** (celebrate consistency without pressure), **Reflection prompting** (explore success anxiety patterns), **Persistent relational context** (Yar remembers and normalizes the pattern) |
| **Planning anxiety** | "Every time I write a plan, I get anxious because I know I won't follow it." (P10) | **Adaptive Planning Undo** (plans are revocable), **Dual-track planning** (baseline is always achievable), **Brain Weather** (plan only what the weather allows) |

### 3.2 Relational and Sociocultural Misrecognition (Section 4.2)

| Challenge | Paper Evidence | Yar Feature Response |
|---|---|---|
| **Social misrecognition and family invalidation** | "When I told my sister I had ADHD, she said, 'Then just correct it.'" (P6) "Everyone thinks ADHD is only about 'hyperactivity' and can't sit still." (P10) | **Communication Coach** (bidirectional ND↔NT bridging), **Affirming language** (Yar never uses deficit framing), **Persistent relational context** (understands per-person communication needs) |
| **Internalized inadequacy** | "I know it's ADHD, but I still feel like I should just try harder. Other people manage; why can't I?" (P10) | **Brain Weather Dashboard** (externalizes cognitive state as weather, not character flaw), **Weekly Narrative Reflection** (reframes week through accomplishment, not deficit), **Identity-safe design** |
| **Resistance and reframing** | "It's not that I can't focus; it's that I focus differently. The problem is the world doesn't allow for that." (P7) | **Affirming neurodivergent cognition** (Yar's entire persona is built on this), **Cognitive scaffolding** (builds on strengths), **Pattern surfacing** (shows what works, not just what fails) |
| **Unequal access to social scaffolding** | Those living alone described "emotional burden of self-management in isolation" (P8, P14) | **Social Presence AI** (always-available body double), **AI co-regulation** (Yar fills the gap when human support is unavailable), **Community features** (future: shared focus rooms) |

### 3.3 Systemic and Structural Misalignments (Section 4.3)

| Challenge | Paper Evidence | Yar Feature Response |
|---|---|---|
| **Institutional and environmental misalignment** | P4 left job due to open-office sensory overload. P4: "Why didn't you just remind me once that I didn't have enough credits?" | **Proactive AI** (surfaces overlooked obligations from connected sources), **Ambient cues** (customizable sensory environment), **Context-sensitive notifications** |
| **Over-reliance and avoidance** | "I sometimes spend more time organizing the to-do app than doing the task." (P9) | **Friction reduction** (Yar captures without elaborate setup), **Auto task extraction** (Saner AI pattern — AI finds tasks, user doesn't organize them), **JITAI delivery** (support at moment of need, not as ongoing system to maintain) |

---

## 4. Strategy Framework — Mapped to Yar Implementation

### 4.1 Social Dynamics as Executive Function Prosthetics (Section 4.4)

| Strategy | Paper Evidence | Yar Implementation Pattern |
|---|---|---|
| **Co-regulation and borrowed structure** | "My friend calls me to remind me to get up and do things. Without that, I might just stay in bed all day." (P17) P1 maintains "replacement" friends to avoid relational dependence. | Yar's **Social Presence AI** provides reliable, non-fragile co-regulation. Unlike human body doubles, Yar is always available and never judges. Implement as persistent ambient companion during work. Key design constraint: supplement human relationships, never replace them. |
| **Peer communities and recognition** | "Only in the ADHD group do I feel that I can tell the truth." (P13) | Future feature: **shared focus rooms** where Yar mediates peer co-working sessions. Privacy-preserving: share presence, not content. Map to Yar's distributed runtime (Dapr + NATS, Phase future). |

### 4.2 Technological Tools as Externalized Cognition (Section 4.5)

| Strategy | Paper Evidence | Yar Implementation Pattern |
|---|---|---|
| **Digital tools and scaffolded memory** | "If it's only me reminding myself, it just becomes invisible after a few days." (P11) | Yar's **graph RAG** and **semantic retrieval** make captures permanently findable. Social layer (shared calendars, accountability) keeps information salient. Key insight: tools only work when embedded in relationships — Yar IS the relationship. |
| **Emotional symbolism of tools** | "The bullet journal is the only paper tool I can stick to. It gives me peace of mind." (P15) "Writing a to-do list is a pleasure in itself." (P1) | Design Yar's capture experience to be **intrinsically rewarding**: satisfying animations, warm confirmation tones, Rive avatar reactions. The act of capturing should feel good independent of follow-through. Brain Weather Dashboard serves the same symbolic function as a bullet journal. |
| **Simulated companionship and AI co-regulation** | "Reporting progress to AI was helpful." (P9) "If a friend or even the app tells me to go to the library, I can start." (P3) | This IS Yar's core value proposition. Participants already use AI chatbots for task accountability (P3, P6, P9). Yar formalizes this pattern with structured capture, persona consistency, longitudinal memory, and safety guardrails (CAP). |

---

## 5. Design Implications — Integration with Yar Architecture

### DI1: Relational Accountability Rather Than Solo Optimization

**Paper says**: Future systems should simulate relational accountability through conversational check-ins, progress co-tracking, and dynamic emotional acknowledgment. AI should adopt the role of attentive companion.

**Yar alignment**: Direct match to Yar's persona design (warmth=0.85, patience=0.95, shame_avoidance=true). Yar's Rive animation states (idle → listening → thinking → speaking → empathic) implement visual relational presence. The "companion, not therapist" framing aligns exactly.

**Implementation gap**: Yar lacks **progress co-tracking UI**. Add a lightweight "check-in" flow where Yar acknowledges what the user captured/completed today in warm, non-evaluative language.

### DI2: Time as Rhythm Rather Than Grid

**Paper says**: Structure tasks against energy flows that fluctuate naturally. Support "ideal vs. baseline" plans. Preserve streaks even on skip days. Temporal flexibility is a basic accessibility requirement.

**Yar alignment**: Yar's design principles already reject streaks and productivity language. The paper provides the constructive alternative: rhythm-based planning with dual-track goals.

**Implementation gap**: Yar's gentle planning currently lacks **energy-state-aware scheduling**. Integrate vocal biomarker data (Layer 2.4: HuBERT emotion sensing, openSMILE prosodic features) to estimate energy state and suggest appropriate plan tier (ideal vs. baseline).

### DI3: Mood-Adaptive Interfaces

**Paper says**: Systems should integrate mood-adaptive mechanisms. A user feeling overwhelmed should be encouraged to complete only a small, manageable goal with affirming messages. Simple acknowledgments prevent emotional spirals.

**Yar alignment**: Maps to Yar's Brain Weather concept and emotional aftercare module. The paper validates that mood-awareness is the single most valued feature category across all 13 concepts.

**Implementation gap**: Yar needs a **mood-state inference pipeline** that combines self-report, vocal biomarkers, and behavioral signals (capture frequency, interaction patterns) into a unified cognitive weather model. This feeds the Brain Weather Dashboard and drives adaptive planning.

### DI4: Affirming Neurodivergent Cognition

**Paper says**: Mainstream tools pathologize divergence by enforcing uniform norms. Future systems should allow users to select representations that align with their cognitive orientation. Cognitive heterogeneity requires multiple modes of engagement.

**Yar alignment**: Yar is identity-safe by design. Communication Coach preserves intent. The paper reinforces that ADHD cognitive profiles are heterogeneous (Mostert et al., 2018), and not every ADHD user needs the same interface.

**Implementation gap**: Yar needs **customizable cognitive metaphors**. Some users prefer Brain Weather; others prefer analytical dashboards. Some want micro-step decomposition; others prefer high-level overviews. Build a preference system that adapts the interface to the user's cognitive style.

### DI5: Co-Regulation as Core Infrastructure

**Paper says**: Co-regulation should be built into the core architecture. Platforms should offer live focus rooms, journaling dashboards with peer check-ins, and shared task timelines with mutual nudging. Cognitive processes span multiple actors and artifacts.

**Yar alignment**: Yar's distributed runtime (Dapr + NATS, LiveKit) is designed for exactly this kind of multi-actor cognitive infrastructure. The phone-laptop-cloud tiered architecture supports co-regulation across devices.

**Implementation gap**: No social/peer features exist in current Yar. Phase this carefully: **Phase 1** = AI-as-co-regulator (Social Presence AI), **Phase 2** = trusted-person sharing (Concept 5), **Phase 3** = peer focus rooms (requires distributed runtime).

---

## 6. ADHD Apps Research Doc Integration

The ADHD apps research document evaluates an Android-to-Linux productivity ecosystem through the lens of "friction-to-action" ratio reduction for the neurodivergent professional. Cross-referencing its tool categories with the paper's validated concepts reveals strong alignment.

### 6.1 Voice-to-Structure Intelligence

| Apps Research Finding | Paper Validation | Yar Integration |
|---|---|---|
| **Tana** voice memos → supertag pipeline provides structured capture from speech; Tana's mobile voice agent enables remote information capture and on-the-go task entry, a key competitive feature for distributed cognition | Paper's Concept 2 (Mood-Aware Daily Companion) validates that voice-first interaction reduces friction for ADHD users | Yar's voice capture pipeline (Gemma 4 E2B/E4B via LiteRT-LM) combines ASR + understanding. Enhance with Tana-style supertag routing: voice input auto-classified into typed objects. Mobile voice agent pattern validates Yar's always-available voice companion design. |
| **Letterly** transforms "rambling" into polished summaries | Paper's emphasis on reducing cognitive burden aligns: P4 said "Many apps are too complicated to set up" | Yar's brain dump compiler (from Goblin Tools pattern) serves this function. Add AI summarization as a post-capture step. |
| **Voicenotes.com** enables "Universal Recall" across all voice history | Paper's P11: "If it's only me reminding myself, it just becomes invisible after a few days." | Yar's semantic retrieval across all captures implements this. Graph RAG (planned) makes voice history queryable. |

### 6.2 Vision-to-Data Architecture

| Apps Research Finding | Paper Validation | Yar Integration |
|---|---|---|
| **Mathpix** provides zero-friction STEM diagram-to-LaTeX conversion | Paper does not address STEM-specific capture. This is additive to the paper's scope. | Integrate Mathpix-style OCR as a Yar plugin for scientific users (target audience: ND researchers & students). |
| **Nebo** interactive ink for diagram beautification | Paper's emphasis on multiple modes of engagement (DI4) supports offering handwriting as an input modality | Future feature: handwriting capture via mobile stylus → Yar routes to knowledge graph. |

### 6.3 Knowledge Workspace

| Apps Research Finding | Paper Validation | Yar Integration |
|---|---|---|
| **Obsidian** local-first Markdown vault with 1500+ plugins | Paper's privacy emphasis aligns: participants wanted AI that doesn't impose expectations or surveil | Yar already uses Anytype as local-first KG. Obsidian MCP integration provides alternative storage backend for developer-oriented users. |
| **Heptabase** infinite canvas for visual synthesis | Paper's Concept 8 (Brain Weather Dashboard) validates visual metaphors for cognitive states | Yar's Brain Weather Dashboard serves a similar spatial-visual function. Consider canvas view for knowledge exploration. |

### 6.4 Proactive AI for Executive Function

| Apps Research Finding | Paper Validation | Yar Integration |
|---|---|---|
| **Saner.ai** "morning brief" scans all connected tools for daily plan | Paper's Concept 2 (Mood-Aware Daily Companion) validates morning check-ins. P14: "I hope the system comes to me instead of me opening it." | Yar's gentle planning implements proactive daily planning. Enhance with Saner-style multi-source scanning (captures, calendar, pending tasks). |
| **Recallify** extracts tasks from unstructured recordings | Paper's over-reliance concern (Section 4.3): "I sometimes spend more time organizing the to-do app than doing the task." | Yar's auto task extraction (from Saner AI pattern) addresses this: AI organizes, user acts. No organizing required. |

### 6.5 Clipboard and Cross-Device Flow

| Apps Research Finding | Paper Validation | Yar Integration |
|---|---|---|
| **ClipZ** AI-powered clipboard with OCR and summarization | Paper does not directly address clipboard workflows, but the "capture tax" concept aligns | Yar's browser extension (Cytomark) handles contextual capture. ClipZ-style AI clipboard complements as mobile capture layer. |
| **KDE Connect** shared clipboard between phone and laptop | Paper's co-regulation emphasis spans devices: support should be available wherever the user is | Yar's distributed runtime (NATS JetStream, Iroh Documents) provides cross-device sync. KDE Connect complements for non-Yar clipboard needs. |

---

## 7. ADHD Apps Prompt Doc Integration

The prompt document specifies target feature requirements across four categories. Each requirement maps to paper-validated concepts.

### 7.1 Voice Assistant/Transcriber Requirements

| Prompt Requirement | Paper Validation | Implementation Priority |
|---|---|---|
| Real-time, no-delay conversational interface | Validated by participant expectations for "low-friction and proactive interaction" (Section 4.6) | **Critical** — Yar voice pipeline (Phase 5) |
| Turn scattered voice into structured docs | Validated by Concept 3 (Flexible Planning) and strategy of tools as externalized cognition | **Critical** — brain dump compiler + typed object routing |
| Understanding equations and math (LaTeX) | Not directly validated by paper (STEM-specific). Validated by apps research (Mathpix). | **Medium** — plugin for scientific users |
| AI summarization of transcribed content | Validated by participant desire for reduced cognitive burden | **High** — post-capture AI processing |
| Integration with personal knowledge bases | Validated by strategies section: tools work when embedded in context | **High** — Anytype MCP, Graph RAG |
| Privacy and open-source availability | Validated by ethical concerns (Section 7.3): participants prefer AI that doesn't surveil | **Critical** — on-device AI, local-first storage |

### 7.2 Unstructured Content Transformation Requirements

| Prompt Requirement | Paper Validation | Implementation Priority |
|---|---|---|
| OCR for handwriting to editable text | Supports DI4 (affirming neurodivergent cognition through multiple input modes) | **Medium** — Mathpix plugin |
| Structure Recognition (notes → lists, tasks, mind maps) | Directly validated by Concept 3, auto task extraction patterns | **High** — core routing engine |
| Visual-to-digital transformation (photo clean/straighten) | Not directly validated; additive convenience feature | **Low** |
| Ability to edit scanned doc regions | Not validated by paper | **Low** |

### 7.3 Note-Taking App Requirements

| Prompt Requirement | Paper Validation | Implementation Priority |
|---|---|---|
| Seamless cross-device sync (Android + Ubuntu Linux) | Validated by co-regulation as core infrastructure (DI5): support spans devices | **High** — distributed runtime |
| Online and offline functionality | Validated by on-device AI emphasis and privacy concerns | **Critical** — local-first architecture |

### 7.4 Clipboard Manager Requirements

| Prompt Requirement | Paper Validation | Implementation Priority |
|---|---|---|
| Copy as AI-friendly formats (Markdown) | Not directly validated; developer-oriented feature | **Medium** |
| Cross-device sharing | Same as cross-device sync validation | **Medium** |
| AI-powered complex screen capture | Supports frictionless capture principle | **Medium** |

---

## 8. Master Feature Requirements

This unified list de-duplicates features from all three sources, grouped by the executive function they support.

### 8.1 Task Initiation (Overcoming Paralysis)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 1 | **Voice-first capture** ("Hey Yar" → brain dump → typed object) | Apps Research, Prompt Doc, Product Impl | DI1: relational accountability reduces initiation barrier | **Critical** |
| 2 | **Spiciness slider for task decomposition** | ADHD Feature Comparison (Goblin Tools) | Challenge: task initiation paralysis; Strategy: task breakdown | **Critical** |
| 3 | **Social Presence AI / body doubling** | Paper C6 (M=4.5, top-3 by 12 participants) | DI5: co-regulation as core infrastructure | **Critical** |
| 4 | **Auto task extraction from captures** | Apps Research (Saner AI), Feature Comparison | Challenge: over-reliance on organizing tools | **High** |
| 5 | **Mood-Aware Daily Companion** (morning check-in) | Paper C2, Apps Research (Saner.ai morning brief) | DI1 + DI3: relational + mood-adaptive | **High** |

### 8.2 Sustained Attention (Managing Focus and Hyperfocus)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 6 | **Focus companion mode** (Rive avatar as ambient presence) | Paper C6, Product Impl (Rive persona) | DI5: co-regulation | **Critical** |
| 7 | **Break reminders during hyperfocus** | Feature Comparison (Super Productivity) | Challenge: hyperfocus exhaustion | **High** |
| 8 | **Idle detection with graceful pause** | Feature Comparison (Super Productivity) | Challenge: time perception disorders | **Medium** |
| 9 | **PiP Focus Window** (floating current-task reminder) | Apps Research (Saner AI) | Challenge: distraction management | **Medium** |

### 8.3 Time Management (Overcoming Time Blindness)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 10 | **Dual-track planning** (ideal vs. baseline goals) | Paper C3 (M=5, highest rated) | DI2: time as rhythm | **Critical** |
| 11 | **Time estimation for tasks** | Feature Comparison (Goblin Tools) | Challenge: time perception disorders | **High** |
| 12 | **Rhythm-based scheduling** (energy flows, not hourly grids) | Paper DI2 | Challenge: planning anxiety | **High** |
| 13 | **Gentle streaks** (preserved on skip days, no resets) | Paper C3 | DI4: affirming neurodivergent cognition | **High** |
| 14 | **Proactive daily planning** (AI suggests based on captures, energy, pending) | Apps Research (Saner.ai), Paper C2 | DI1: relational accountability | **High** |

### 8.4 Emotional Regulation (Preventing Shame Spirals)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 15 | **Brain Weather Dashboard** (cognitive state visualization) | Paper C8 (M=5, highest rated, top-3 by 13) | DI4: affirming neurodivergent cognition | **Critical** |
| 16 | **Emotionally Aware Pause Days** (proactive rest suggestion) | Paper C11 (M=4.5, top-3 by 12) | DI3: mood-adaptive interfaces | **High** |
| 17 | **Emotional aftercare** (post-difficult-interaction processing) | Product Impl (Tier 2), Paper C12 | DI3: mood-adaptive | **High** |
| 18 | **Emoji mood tracking on tasks** | Feature Comparison (Leantime) | DI3: mood-adaptive interfaces | **Medium** |
| 19 | **Emotional debrief after task collapse** | Paper C12 (M=3) | DI1 + DI3: relational + mood-adaptive | **Medium** |
| 20 | **Replay loop interruption** | Product Impl (persona behavior) | Challenge: emotional fluctuations and self-blame | **Medium** |

### 8.5 Working Memory (Externalized Cognition)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 21 | **Brain dump compiler** (chaos → structure) | Feature Comparison (Goblin Tools), Prompt Doc | Strategy: tools as externalized cognition | **Critical** |
| 22 | **Semantic retrieval** ("What was that thing about...") | Product Impl (Tier 1), Apps Research (Voicenotes) | Challenge: scaffolded memory fails without reinforcement | **High** |
| 23 | **Smart note types / supertags** | Feature Comparison (Tana), Apps Research (Tana) | Strategy: typed object routing | **High** |
| 24 | **Browser-aware contextual capture** (Cytomark extension) | Product Impl (Tier 1) | Strategy: capture where cognition already happens | **High** |
| 25 | **Cross-device clipboard sync** | Apps Research (KDE Connect, ClipZ), Prompt Doc | DI5: support spans devices | **Medium** |
| 26 | **OCR for handwriting/whiteboard** | Apps Research (Mathpix, Nebo), Prompt Doc | DI4: multiple input modalities | **Medium** |
| 27 | **LaTeX/math equation support** | Apps Research (Mathpix), Prompt Doc | Additive for STEM users | **Medium** |

### 8.6 Social Cognition (Communication and Relationships)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 28 | **Communication Coach** (ND↔NT bidirectional) | Product Impl (Tier 2) | Challenge: social misrecognition; DI4: affirming cognition | **Critical** |
| 29 | **Tone analysis** ("Was that email rude or am I overthinking?") | Feature Comparison (Goblin Tools Judge) | Challenge: internalized inadequacy | **High** |
| 30 | **Persistent relational context** (per-person communication models) | Product Impl (Tier 3) | Challenge: unequal access to social scaffolding | **Medium** |
| 31 | **Shared planning with trusted person** (opt-in) | Paper C5 (M=3, mixed response) | DI5: co-regulation | **Medium** |

### 8.6b Persona and Adaptation (Relational Depth)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 40 | **Adaptive Multi-Persona System** (coach, buddy, guardian, mom, partner) | Product Impl (Phase 6 expanded) | DI1: relational accountability; C6: Social Presence AI | **Critical** |
| 41 | **Mood-context persona switching** (learns which persona fits which state) | Product Impl (Phase 6 expanded) | DI3: mood-adaptive interfaces; C8: Brain Weather feeds persona selection | **Critical** |
| 42 | **ElevenLabs persona voices** (distinct voice per relationship type) | Product Impl (Phase 6 expanded), ElevenLabs evaluation | DI4: affirming cognition through relational depth | **High** |
| 43 | **Interaction-driven persona refinement** (no manual config tax) | Product Impl (Phase 6 expanded) | DI4: heterogeneous cognitive profiles require adaptive, not configured, interfaces | **Critical** |

### 8.7 Self-Awareness (Longitudinal Understanding)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 32 | **Vocal biomarker tracking** (energy, stress, medication effects) | Product Impl (Tier 3), Master Ref (Layer 2.4) | DI3: mood-adaptive (feeds Brain Weather) | **High** |
| 33 | **Pattern surfacing** ("You've been capturing a lot about X this week") | Product Impl (Tier 2), Paper C10 | DI2: time as rhythm | **Medium** |
| 34 | **Weekly Narrative Reflection** | Paper C13 (M=3) | DI4: affirming cognition | **Medium** |
| 35 | **Longitudinal cognitive weather history** | Paper C8 extrapolation | DI4: self-compassion through data | **Medium** |

### 8.8 Privacy and Autonomy

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 36 | **On-device AI** (local-first inference) | Product Impl, Master Ref, Apps Research | Ethical considerations (Section 7.3): non-judgmental, no surveillance | **Critical** |
| 37 | **CAP safety guardrails** | Product Impl, Master Ref | Paper's tension: autonomy vs. guidance; users want suggestions not directives | **Critical** |
| 38 | **User-controlled nudge configuration** | Paper speed-dating findings | "Adaptive support was most welcome when users could configure nudges" | **High** |
| 39 | **Open-source availability** | Prompt Doc, Feature Comparison | Aligns with Cytognosis mission | **Critical** |

### 8.9 Sensor Integration (Physiological Context)

| # | Feature | Source(s) | Paper Validation | Priority |
|---|---|---|---|---|
| 44 | **Universal Sensor Adapter Protocol (USAP)** (MCP for sensors) | Product Impl (Phase 7), Blue Lin DR3 | DI3: mood-adaptive (physiological signals feed Brain Weather) | **Critical** |
| 45 | **Wearable integration** (Oura, Apple Watch, Garmin) | Product Impl (Phase 7) | C8: Brain Weather needs physiological ground truth | **High** |
| 46 | **Brain connectomic integration** (future EEG/neural trackers) | Product Impl (Phase 7), Cytonome vision | DI3 + DR1 (Lin): predicted cognitive states with confidence | **Medium** |
| 47 | **Environmental context** (light, noise, air quality) | Product Impl (Phase 7) | Challenge: institutional misalignment (P4 open-office sensory overload) | **Medium** |

---

## 9. Implementation Roadmap Alignment

The paper's validated concepts map to Yar's existing implementation phases:

| Yar Phase | Paper Concepts to Integrate | New Requirements from Paper |
|---|---|---|
| **Phase 1: CAP Integration** | No change | CAP must support mood-adaptive policy adjustments |
| **Phase 2: Anytype Submodule** | No change | Schema needs "cognitive weather" object type |
| **Phase 3: Mobile Interface** | C6 (Social Presence AI), C3 (Flexible Planning), C8 (Brain Weather) | Rive persona must support focus companion mode; gentle planning UI needs dual-track goals |
| **Phase 4: Desktop & Web** | C8 (Brain Weather Dashboard), C13 (Weekly Narrative) | Desktop dashboard becomes Brain Weather primary interface |
| **Phase 5: Voice Pipeline** | C2 (Mood-Aware Companion) | Vocal biomarkers feed Brain Weather model; morning check-in flow |
| **Phase 6: Persona System** | C6 (Social Presence AI), C11 (Pause Days) | Persona must detect burnout signals and proactively suggest rest |
| **Phase 7: Universal Sensor Adapter** | C8 (Brain Weather needs physiological ground truth) | USAP protocol, Oura/watch adapters, CAP privacy gates for sensor data |

> [!IMPORTANT]
> The paper's highest-rated concepts (C8, C3, C6, C11) concentrate in Phases 3-5. This validates Yar's current phase ordering: CAP and infrastructure first, then the features that matter most to users.

---

## 10. Key Design Tensions

The speed-dating findings surface four tensions that Yar must navigate:

| Tension | Paper Finding | Yar Design Response |
|---|---|---|
| **Autonomy vs. Guidance** | "I want it to suggest, not decide." Users fear excessive AI intervention. | Yar operates at "companion" authority level. CAP enforces boundaries. All suggestions are inspectable, adjustable, and overridable. |
| **Emotional Support vs. Efficiency** | Emotional journaling seen as extra cognitive burden when it disrupts workflow. | Embed emotional awareness seamlessly: vocal biomarkers detect mood without explicit journaling. Brain Weather updates passively. |
| **Privacy vs. Social Connection** | Social Presence AI (C6) highly valued; Shared Planning (C5) divisive. | Default to AI-mediated social presence. Human sharing is always opt-in with granular controls. |
| **Adaptive Nudges vs. Surveillance** | "Even if I know it's trying to help, it feels like it's watching me." (S14) | All nudges are user-configured: frequency, tone, content, and delivery mode. Pattern detection happens on-device; no data leaves. |
