# Deep-Dive Tool Research: Six ND-Relevant Apps
**Date:** 2026-06-21
**Analyst:** Claude Sonnet 4.6 (subagent)
**Purpose:** Depth pass on six known tools for the Yar feature matrix. Each section covers feature detail, ND domain mapping, AI usage, standout pattern, sourced evidence, and refined score.

**ND domain key**
- AE = Attention regulation and executive function
- ER = Emotional regulation and mood
- SC = Social communication and interaction
- SP = Sensory processing and regulation
- CT = Cognitive style and thought organization
- SI = Self-monitoring and interoception

---

## 1. Tana

**Product:** Tana Outliner (web, macOS, iOS, Android)
**Sources:** https://outliner.tana.inc/tana-mobile · https://outliner.tana.inc/supertags · https://aiproductivity.ai/tools/tana/ · https://outliner.tana.inc/articles/talk-through-your-ideas-with-tana-ai-voice-chat-for-ios

### Feature detail

**Supertags** are the structural primitive. A supertag is both a label and a schema: it defines typed fields (text, date, dropdown, reference to another node). Any outline node can carry multiple supertags. The user defines the schema once; the AI and search system treat it as a queryable type. Example: a #mood_log supertag could carry fields for energy (1-5), affect label, and a note, then surface in a saved search view filtering all #mood_log entries for the past week.

**Personal knowledge graph:** Every node is an addressable object in a single graph. Linking a voice memo to an existing person or project node creates a persistent bidirectional reference. Search nodes (saved, dynamic queries) function like live database views across the graph.

**Voice capture to structured nodes:** Lock-screen and home-screen widgets on iOS and Android allow one-tap voice memo start with no app navigation. Transcription supports 60+ languages with auto-detect. When a voice memo is tagged with a supertag, Tana AI autofills the supertag's fields from the transcript (e.g., "Review the proposal John sent for Scalegate" links to existing John and Scalegate nodes). AI instructions on voice memo supertags are user-editable.

**Tana AI Voice Chat (iOS):** A separate interactive voice conversation mode, not just dictation. The user speaks; the AI responds with awareness of the user's graph context. Custom supertags can shape what the conversation captures.

**Dual phone/desktop integration:** Captures on mobile join the same graph seen on desktop. Supertags, fields, and links are available immediately on return to desktop. No separate inbox to process.

**AI model choice (Dec 2025/2026):** Tana now supports GPT, Claude, and Gemini per agent, with surrounding graph as context.

### ND domains served
- **AE (primary):** Lock-screen widget reduces activation energy to near zero; supertag autofill eliminates the "what folder?" decision at capture time.
- **CT (primary):** Graph structure externalizes associative thinking; saved search views replace folder hierarchies.
- **SI (secondary):** Voice memo supertags can encode physiological or mood fields; the graph then makes these queryable over time.

### AI usage
- Transcription (60+ languages)
- Field autofill from voice (NLU + graph entity linking)
- AI agents with multi-model support (GPT/Claude/Gemini), graph context injection
- Voice chat (iOS): conversational AI that reads and writes graph nodes

### Standout pattern for Cytognosis
**Schema-governed capture.** The user defines a supertag schema (e.g., #symptom_log with fields: domain, severity, context), and every future capture of that type lands pre-structured, searchable, and linkable. Yar could adopt this as its data model: each check-in is a typed node, not a freeform log entry. This eliminates post-hoc tagging friction and makes longitudinal pattern queries trivial.

### Score sketch
**8/10.** Best-in-class for structured personal knowledge capture and graph querying. Loses 2 points for steep learning curve (supertag schema design requires upfront cognitive effort), limited native analytics/visualization, and no ND-explicit framing. Does not surface patterns proactively; user must construct views.

---

## 2. Capacities

**Product:** Capacities (web, macOS, Windows, Linux, iOS, Android)
**Sources:** https://capacities.io/ · https://www.atlasworkspace.ai/blog/obsidian-vs-capacities · https://blog.saner.ai/capacities-review/ · https://play.google.com/store/apps/details?id=io.capacities.mobile

### Feature detail

**Object-based PKM:** Everything is an object with a type (Person, Book, Meeting, Project, or user-defined). Objects have typed properties. This is the key UX distinction from page-and-folder PKM: there is no "where does this go?" decision, only "what is this?" The graph view shows typed, color-coded nodes with named relation types (unlike Obsidian, which treats all links as equal).

**Daily notes as pressure-free inbox:** The daily note is the default entry point. Users write anything; objects are linked or created inline as needed. The daily note auto-populates with incomplete tasks, calendar events, and journal prompts (in Pro). There is no mandatory structure.

**Linking and backlinks:** Any object can reference any other. Backlinks surface automatically. "Related Content" is an AI-assisted feature that scans notes to surface conceptual connections not explicitly linked.

**AI features (Pro, $8-10/mo):** AI chat over the workspace, AI tagging, automated note organization, Related Content discovery. AI is rate-limited on Pro; heavy AI users report frustration. No voice capture or mobile audio at present.

**ND-adjacent user feedback:** Direct testimonial on Capacities.io from a user with ADHD: "My ADHD brain thanks the founders. I do normally make a mess in my notes, so it is super helpful with not having 9 levels of folders." Object-based organization eliminates the "which folder?" decision at the root.

**Limitations:** Mobile app is cited as weaker than desktop; import friction; AI daily-limit complaints. Funded by users, not VCs; EU-hosted; GDPR compliant; full export always available.

### ND domains served
- **CT (primary):** Object types externalize categorical thinking; no folder hierarchy to maintain.
- **AE (secondary):** Daily note as low-friction inbox reduces task-initiation barrier; no setup required.

### AI usage
- Related Content: unsupervised similarity scan to surface latent connections
- AI tagging and categorization
- AI chat over personal knowledge base (Pro)

### Standout pattern for Cytognosis
**Object-first, daily note as inbox.** The combination of typed objects (structured) with a daily note inbox (unstructured entry point) is the key UX pattern. Yar should adopt this: a frictionless daily check-in generates raw entries that the system resolves into typed objects (mood event, symptom, win, concern) without the user needing to file anything. The user writes freely; the structure is imposed post-capture.

### Score sketch
**6/10.** Strong concept and clean execution. Loses points for immature mobile, AI rate-limiting, and absence of any ND-explicit features or proactive surfacing. The object model is highly relevant to Yar's data architecture but Capacities does not close the loop to insight or action.

---

## 3. Omi AI

**Product:** Omi wearable ($89 device) plus iOS/Android/macOS/web app
**Sources:** https://www.omi.me/pages/product · https://github.com/BasedHardware/omi · https://grokipedia.com/page/Omi_wearable_AI · https://pyshine.com/Omi-AI-Powered-Wearable-Assistant/

### Feature detail

**Hardware:** 2.5 cm diameter pendant, 150 mAh battery (10-14 hours), 2 microphones, offline recording, Bluetooth 5.1, 2.4/5 GHz Wi-Fi. Worn as pendant or attached to forehead. Not water-resistant.

**Real-time transcription:** Captures everything the user says and hears. 25+ languages, single/multi-speaker, live translation. Speech profiles improve per-speaker accuracy. Latency 500-2000 ms (live) or 10-20 seconds (offline batch). Offline recording to device with cloud sync when reconnected.

**Automatic summaries, tasks, memories:** AI post-processes each conversation segment into summary, action items extracted as tasks, and persistent memories. "Memories" are stored in a searchable Brain Map. Evening Daily Recaps synthesize the day.

**Recall and query:** "Ask Omi" is an AI chat that has full access to the user's memory store plus web search. "Tap and Talk" sends a quick question and gets an answer grounded in personal context.

**App ecosystem:** Omi App Store lists 1,000+ integrations. Custom summary templates. Task sync to external managers. Folders and starred items for organization.

**Open source:** Full stack is open source under BasedHardware on GitHub. Hardware design is open. Users can choose their own STT provider, run locally, and ship apps to the Omi store (paid or free). MCP server and REST API are published. SOC 2 and HIPAA compliance. TLS in transit, AES-256-GCM at rest.

**Brain interface:** A separate brain-interface module is planned for 2026-2027; current device is audio-only.

**Scale:** 300,000+ users; 9,000+ Discord community; 500+ verified reviews. Press coverage in TechCrunch, The Verge, Wired, WSJ, Forbes.

### ND domains served
- **AE (primary):** Ambient capture eliminates all capture friction; the user never has to initiate a logging action. Auto-task extraction offloads the "what do I need to do?" synthesis step.
- **CT (secondary):** Brain Map externalizes working memory; the user's history is queryable rather than needing to be remembered.
- **SI (secondary):** Daily Recaps create a forced reflection loop on what was said and done. Could surface mood/energy patterns if combined with symptom prompts.

### AI usage
- STT transcription (user-selectable model/provider)
- LLM summarization and task extraction
- Semantic memory store and retrieval (Brain Map)
- AI chat grounded in personal history + web search
- Custom template logic for summary formatting

### Open standards / protocols published
- REST API (documented at h.omi.me/apps)
- MCP server (mentioned on product page)
- Open hardware schematics (BasedHardware GitHub)
- Pluggable STT: user can supply Deepgram, Whisper, or other provider

### Standout pattern for Cytognosis
**Passive ambient capture as the zero-effort logging baseline.** Omi demonstrates that the capture friction for a wearable can be zero: the device records; the AI does all structuring. For Yar, this is a reference point for the "soft sensor" layer: a future Yar wearable (or phone-based always-listen mode) could passively capture speech and extract mood-relevant content, diarization, and task commitments without any user-initiated log. The open MCP server and pluggable STT also model how Yar should expose its data layer for third-party integration.

### Score sketch
**7/10.** Best-in-class for passive ambient capture and open architecture. Loses points for hardware dependency ($89 + $16/mo), no native ND-explicit framing, no visualization of longitudinal patterns, and no symptom-domain structure (captures conversation, not internal state). Highly relevant as a future layer, not a daily-habit app wedge. Score revised up from any prior estimate that treated it as peripheral: the open MCP + pluggable STT is more mature than expected.

---

## 4. Goblin Tools

**Product:** Goblin Tools (web free, iOS/Android $2.99 one-time)
**Sources:** https://goblin.tools/ · https://psychelicht.com/en/goblin-tools-review-magic-todo/ · https://www.focushack.io/reviews/goblin-tools-adhd-review/ · https://forum.asana.com/t/free-handy-ai-assisted-goblin-tools/868466

### Feature detail

**Current tools (v3.3.2):**
- **Magic ToDo:** Enter any task; AI breaks it into subtasks. "Spiciness" slider (1-5) controls granularity. At max spiciness, a vague task like "prepare for doctor appointment" becomes 15+ discrete micro-steps. No account required. Unlimited free use on web.
- **Formalizer:** Paste text in any register (casual, anxious, blunt); select a target tone (professional, empathetic, assertive, etc.); AI rewrites. Designed to help ND users who struggle to calibrate formality in written communication.
- **Judge:** Paste a message; AI identifies emotional tone (as received by a neurotypical reader). Helps ND users who may misread implied emotional content in written messages.
- **Estimator:** Enter a task; AI guesses realistic time. Addresses time blindness.
- **Compiler:** Free-form brain dump; AI organizes into an actionable list.
- **Professor:** Explain anything at a chosen complexity level.
- **Consultant:** Decision support.
- **Taskmaster (new):** Focus on one task at a time; progressive disclosure of the full list to avoid overwhelm.
- **Chef:** Generate recipes from available ingredients.

**Design rationale (explicit):** Goblin Tools was built by a solo developer who is neurodivergent. The design philosophy is: zero setup, zero account, zero friction. The site loads and the tool is immediately usable. Every additional step between intent and action is a potential ADHD dropout point. The "spiciness" metaphor is deliberately non-clinical and approachable. Viral on TikTok and Reddit in 2023-2024 specifically in ND communities.

**AI approach:** GPT-4 class LLM behind all tools. No local processing, no memory, no persistent state. Each request is stateless. Sponsored by community donors (Ko-Fi, Patreon) to remain free.

### ND domains served
- **AE (primary):** Magic ToDo and Taskmaster directly target task initiation and executive planning. The spiciness slider allows users to control decomposition depth based on current executive capacity (which varies day to day).
- **SC (primary):** Formalizer and Judge are the only tools in this landscape explicitly designed for social communication support. Judge is particularly novel: it lets users check their own emotional calibration before sending.
- **CT (secondary):** Compiler converts undifferentiated brain-dump to structured action list.
- **ER (secondary):** Judge provides a form of external emotional validation; knowing how a message reads can reduce anxiety before sending.

### AI usage
- LLM (GPT-4 class) for all tool functions
- No memory, no fine-tuning, no user model
- Stateless: each request is independent

### Standout pattern for Cytognosis
**Spiciness slider as adaptive granularity control.** This is the single most transferable UX primitive in this landscape. The insight: the appropriate level of task decomposition is not fixed; it depends on the user's current executive state. A user in crisis needs 15 micro-steps; a user in flow needs 3. Yar should expose a similar "support level" control on any task or plan view, scaling decomposition to declared capacity rather than assuming a fixed level. Also: the Judge tool's "how does this read emotionally?" function could be directly adapted to help Yar users calibrate mood self-reports ("does this description match how you're feeling, or is there more?").

### Score sketch
**8/10** for ND-specific UX design purity. Loses points for statelessness (no memory, no longitudinal data, no personalization), no integration with other systems, and no proactive nudging. The spiciness slider and Judge pattern are best-in-class for the domains they address.

---

## 5. Blue Lin (Georgianna Lin)

**Primary:** https://bluelin.me/projects/menstrual_health · https://dl.acm.org/doi/10.1145/3613904.3642282

**Note:** Blue Lin is a researcher/designer (Postdoctoral Research Fellow, Columbia University), not a commercial product. This entry covers design patterns and published findings applicable to Yar's symptom-tracking UX.

### Research overview

Three-phase mixed-methods project using menstrual health as a lens for multimodal health sensemaking. Total: 100 participants, 190+ days of longitudinal data, 3 research phases.

**Phase 1 (50 participants, 3 months):** Contextual inquiry. Participants used Mira (hormones: E3G, LH), Fitbit Sense (sleep, HR, stress), Dexcom G6 (continuous glucose), and a custom app (mood, flow, pain, notes) simultaneously, but in native siloed apps. Key finding: fragmented apps produce fragmented thinking. Users toggled between 3-4 apps to correlate signals; cognitive load caused "data fatigue," leading to default to familiar data types and abandonment of novel signals.

**Phase 2 (30 participants):** Co-design of two proof-of-concept interfaces and derivation of five functional design requirements (DRs). Published at CHI 2024 (https://dl.acm.org/doi/10.1145/3613904.3642282).

The five DRs:
- **DR1 Predict symptoms/events:** Help users anticipate upcoming phases. Both linear and circular visualizations needed for planning vs. cycle-awareness.
- **DR2 Multivariate unified view:** Display multiple data types (hormones, sleep, mood) in one view, sorted by personal relevance.
- **DR3 Inspect individual signals:** Allow drill-down on a single metric with clinical context.
- **DR4 Compare across signals:** Show relationships between symptoms and physiological data on aligned timescales.
- **DR5 Compare across cycles:** Support time-based reflection with historical, current, predicted, and peer-aggregate context.

**Phase 3 (20 participants, 100 days):** Longitudinal field study of a working prototype (React Native, Fitbit API, Mira API, Node.js + PostgreSQL backend). Published in IMWUT 2025. Key findings: (a) integrated multimodal view enabled "big picture" health understanding, moving users from logging to connecting; (b) engagement followed a learning-curve pattern (high early, sharp mid-study decline as patterns internalized, late resurgence for new insights); (c) users developed lasting internalized models even after stopping active tracking.

**Two prototype concepts evaluated:**
- **MenstrualMate:** Human-avatar interface, body-centric symptom mapping on a figure over linear timeline. Phase-specific stats. Cycle comparison with historical and peer data.
- **PeriodBubble:** Node-link graph, signals as nodes orbiting a cycle hub. Circular timeline. Drag-and-drop comparison. Summary popups.

**Cognitive strategies identified (IMWUT 2025):** Users aligned health goals with each device's perceived scope and approached multimodal data with paired hypotheses ("when my LH spikes, does my sleep degrade?"). Confidence in one's own sensemaking process mediates engagement with multimodality. Design recommendation: scaffold trust, not just information.

### ND domain applicability
- **SI (primary):** The entire research program is a self-monitoring and interoception design project. Key finding that users need tools to build trust between body signals and digital representations is directly applicable to Yar's mood and symptom tracking.
- **CT (secondary):** DR2 and DR4 (unified multivariate view, cross-signal comparison) address cognitive load in pattern recognition.
- **AE (secondary):** DR1 (predictive) addresses proactive planning; cycle-aware planning is directly analogous to Yar's future energy/capacity prediction.

### Design patterns for Cytognosis

| Pattern | Source | Application to Yar |
|---|---|---|
| Unified multimodal view (DR2) | CHI 2024 | Yar should show mood, energy, sleep, and cognitive state in one timeline view, not separate logs |
| Paired-hypothesis data entry | IMWUT 2025 | Prompt users: "You logged low energy; how was your sleep last night?" rather than separate logging |
| Circular vs. linear toggle | CHI 2024 | Offer both views: linear for week planning, circular for pattern recognition across cycles |
| Progressive trust-scaffolding | IMWUT 2025 | Introduce data streams gradually; do not overwhelm with all signals on day one |
| "Data fatigue" as dropout signal | IMWUT 2025 | Monitor engagement curve; if mid-study decline occurs (as in Phase 3), trigger a "simplify view" suggestion |
| Body-centric visualization | CHI 2024 | Embodied self-report (MenstrualMate avatar) reduced abstraction; Yar could use body-region taps for sensory/somatic symptoms |
| Peer-aggregate context | CHI 2024 | Anonymized community distributions reduce self-pathologizing by showing what is typical |

### Score sketch
**N/A (researcher, not product).** Relevance score for Yar design: **9/10.** The five DRs and the cognitive strategy findings are the most directly applicable design evidence in this landscape. The IMWUT 2025 paper should be cited in Yar's design rationale.

---

## 6. Saner AI

**Product:** Saner.AI (iOS, Android, web, Chrome extension)
**Sources:** https://www.saner.ai/ · https://www.primeproductiv4.com/apps-tools/saner-ai-review · https://easyai.indevs.in/saner-ai/ · https://opentools.ai/tools/sanerai

### Feature detail

**Core identity:** Explicitly positions as "the first ADHD-friendly AI personal assistant for notes, email, and calendar." The team interviewed 200+ ADHDers during development. This is the only tool in this set with ADHD as its stated primary design target.

**Capture:** Voice notes, quick capture via Chrome extension, bulk import from Google Drive, PDFs, YouTube links. All inputs are processed by Skai (the AI assistant) and auto-organized with AI tagging and categorization. Voice is optimized for quick brain-dump.

**Skai (AI assistant):** Has simultaneous access to notes, tasks, emails, and calendar. Semantic search allows natural language queries across all content ("what did I say about the Cellanome meeting last week?"). Skai also performs proactive morning planning: it reviews the inbox and calendar, builds a prioritized action plan, and presents it at day-start. Throughout the day, Skai does check-ins that surface forgotten tasks.

**Notes-tasks-calendar integration:** Unlike Capacities or Tana (which are note-focused), Saner integrates the full productivity triad. Email is connected; Skai can extract tasks from email threads. Calendar is connected; Skai can schedule directly and build time-blocked day plans. This is the closest in this set to an end-to-end ADHD productivity assistant.

**Task breakdown:** Skai breaks intimidating projects into bite-sized milestones, paralleling Goblin's Magic ToDo but with persistent memory and calendar context.

**ADHD-specific design decisions:**
- No folder hierarchy (flat + AI-organized)
- Morning proactive plan (removes the "where do I start?" paralysis)
- Proactive check-ins throughout day (external reminder as prosthetic working memory)
- Semantic search over freeform capture (no need to organize before retrieval)
- Prioritized action plan removes decision paralysis

**Limitations:** No voice chat or wearable. No longitudinal mood/symptom tracking. No ND domain beyond AE/CT. AI is strong but calendar integration still reported as less polished than dedicated calendar apps. Pricing: free plan; Starter $8-12/mo; Standard $16-20/mo.

### ND domains served
- **AE (primary):** Proactive morning plan, check-ins, task breakdown directly target dysexecutive patterns.
- **CT (primary):** Semantic search and AI organization remove the cognitive overhead of filing and retrieval.

### AI usage
- Skai: LLM with simultaneous access to notes, tasks, emails, calendar
- Auto-tagging and categorization of all captured content
- Semantic (vector) search over personal corpus
- Proactive scheduling and check-in generation
- Task decomposition from project descriptions

### Standout pattern for Cytognosis
**Proactive morning briefing + distributed check-ins.** Saner demonstrates a viable pattern for ADHD support that Yar should adopt: the AI does not wait for the user to initiate. It surfaces a daily plan at a consistent time and periodically re-surfaces forgotten items. For Yar, this maps to: morning mood check-in + energy forecast + top-3 intentions, then a mid-day and evening micro-check-in, all initiated by Yar, not the user. The key insight from Saner: the AI should be the agent that initiates; the user responds. This is the inverse of most productivity apps.

### Score sketch
**7/10.** Best-in-class for proactive ADHD-specific design pattern (morning plan + check-ins) and notes-tasks-calendar integration. Loses points for no mood/symptom tracking, no longitudinal visualization, no wearable/ambient layer, and immature calendar integration. Closer to the right framing for Yar's core UX than any other tool in this set.

---

## Cross-Tool Synthesis

### Score summary table

| Tool | ND Relevance Score | Primary Domain | Key Differentiator |
|---|---|---|---|
| Tana | 8/10 | AE, CT | Schema-governed capture; graph as memory layer |
| Capacities | 6/10 | CT, AE | Object-first; daily note inbox; no ND framing |
| Omi AI | 7/10 | AE, CT | Zero-friction ambient capture; open MCP + pluggable STT |
| Goblin Tools | 8/10 | AE, SC | Adaptive granularity (spiciness); Judge for social calibration |
| Blue Lin (research) | 9/10 relevance | SI, CT | 5 design requirements; multimodal sensemaking evidence base |
| Saner AI | 7/10 | AE, CT | Proactive AI-initiated check-ins; ADHD-explicit design |

### Patterns to adopt in Yar (priority order)

1. **Proactive AI-initiated check-ins (Saner):** Yar initiates; user responds. Morning plan + 2-3 micro-check-ins daily.
2. **Adaptive granularity / support-level slider (Goblin):** Task and plan detail scales to declared capacity.
3. **Unified multimodal timeline (Blue Lin DR2/DR4):** One view shows mood, energy, sleep, cognitive state; not separate logs.
4. **Schema-governed typed capture (Tana):** Each check-in resolves to a typed node with structured fields.
5. **Object-first, frictionless entry (Capacities):** Daily note as unstructured inbox that the system resolves to objects.
6. **Ambient capture as baseline (Omi):** Future layer; expose MCP/API from day one for integration readiness.
7. **Social communication calibration (Goblin Judge):** Optional "how does this read?" for externalized messages.

### Findings that change a prior assumption

- **Omi open architecture is more mature than expected.** MCP server and pluggable STT mean Omi is integration-ready today, not "future hardware play." Score revised up to 7 (from any prior estimate treating it as peripheral).
- **Goblin's Judge tool is unique in this landscape** for social communication support (SC domain). No other tool addresses this. Yar should have a version for mood-report calibration.
- **Blue Lin's IMWUT 2025 finding on the engagement learning curve** (sharp mid-study drop, late resurgence) is directly predictive of Yar user churn risk. Design must account for the "patterns internalized" phase by shifting from daily data entry to periodic confirmation and exception flagging.
- **Saner is the closest existing product to Yar's core UX framing**, but it lacks the symptom/mood/SI layer entirely. Yar's differentiation is adding SI and ER domains to Saner's AE/CT foundation.

---

## References

- Tana mobile: https://outliner.tana.inc/tana-mobile
- Tana supertags: https://outliner.tana.inc/supertags
- Tana review 2026: https://aiproductivity.ai/tools/tana/
- Tana voice chat: https://outliner.tana.inc/articles/talk-through-your-ideas-with-tana-ai-voice-chat-for-ios
- Capacities home: https://capacities.io/
- Capacities vs Obsidian: https://www.atlasworkspace.ai/blog/obsidian-vs-capacities
- Capacities review (Saner blog): https://blog.saner.ai/capacities-review/
- Omi product page: https://www.omi.me/pages/product
- Omi GitHub: https://github.com/BasedHardware/omi
- Omi overview: https://grokipedia.com/page/Omi_wearable_AI
- Goblin Tools home: https://goblin.tools/
- Goblin Tools ADHD review: https://www.focushack.io/reviews/goblin-tools-adhd-review/
- Goblin Tools review 2026: https://psychelicht.com/en/goblin-tools-review-magic-todo/
- Blue Lin project: https://bluelin.me/projects/menstrual_health
- Blue Lin CHI 2024: https://dl.acm.org/doi/10.1145/3613904.3642282
- Blue Lin IMWUT 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC11687174/ (related PMDS/JMIR paper; IMWUT paper PDF at bluelin.me)
- Saner AI home: https://www.saner.ai/
- Saner AI review: https://www.primeproductiv4.com/apps-tools/saner-ai-review
- Saner AI review 2026: https://easyai.indevs.in/saner-ai/
