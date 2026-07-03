# Research Brief C: New Tools and Papers
**Yar Feature Consolidation — 2026-06-21**
Reading time: ~6 min | If you read one thing: jump to "arXiv 2603.17258 Verification" and "Brain.fm Evidence Quality."

---

## Scoring Rubric
0 = absent, 3 = basic, 5 = adequate, 7 = strong, 10 = best-in-class.
Weight: neurodivergent-user relevance and real UX over marketing claims.

**ND Functional Domains (tags)**
- `ATT` — attention regulation and executive function
- `EMO` — emotional regulation and mood
- `SOC` — social communication and interaction
- `SEN` — sensory processing and regulation
- `COG` — cognitive style and thought organization
- `MON` — self-monitoring and interoception

---

## 1. Lovable.dev — AI Mind Mapping Use Case

**What it is:** Lovable is an AI-powered full-stack app builder (vibe coding), not a standalone mind mapping tool. Their mind mapping page describes what *you can build with Lovable*, not a shipped mind-mapping product. The page is a use-case marketing landing page.

**Key features described (platform capabilities, not shipped features):**
- Prompt-to-interactive-mind-map generation (nodes, connections, visual styles)
- Live rendering with instant undo
- Collaborative branching
- Image input handling
- One-click publish and share
- Select-and-edit for fine-grained UI tweaks without re-prompting

**ND domain alignment:**
- `COG` — nonlinear idea capture without forcing linear structure
- `ATT` — low-friction start (type a prompt, get a map) reduces initiation barriers

**AI use:** Core product is AI-driven code and UI generation. The mind-mapping use case inherits that: users describe what they want, the AI builds it. No specialized ND-tuned AI layer.

**Evidence / claims:**
- Marketing page only; no published studies or UX research cited. [(Source)](https://lovable.dev/solutions/use-case/mind-mapping-tools)
- Company context: $330M Series B (Dec 2025), $6.6B valuation, $200M ARR. Well-funded but mind-mapping is one of hundreds of use cases.

**Score sketch:** 4/10 (as a mind-mapping tool for ND users).
*Justification: Low friction entry is ND-friendly, but this is a builder platform, not a purpose-built ND mind-mapping app; no ND UX validation, no offline support, collaboration is a dev workflow not an ND scaffold.*

---

## 2. Brain.fm — Functional Music for Attention and Focus

**What it is:** Subscription audio app using patented amplitude-modulated music designed to induce neural entrainment, marketed primarily for focus, sleep, and relaxation. Has dedicated ADHD track.

**Key features:**
- Functional music tracks (focus / sleep / relax modes)
- Patented rapid amplitude modulation (not binaural beats; company explicitly distinguishes these)
- ADHD-specific playlist category
- Mobile + desktop + web apps

**ND domain alignment:**
- `ATT` — primary claim: sustained attention and cognitive control enhancement
- `SEN` — auditory environment regulation (replaces distracting ambient noise)

**AI use:** AI-assisted music composition layer added on top of human-composed music to enforce amplitude modulation parameters. Not a generative conversational AI. Music is pre-composed and curated.

**Evidence and evidence quality — be precise:**

| Study | Authors | Journal | What was measured | Key finding |
|-------|---------|---------|------------------|-------------|
| Primary (2024) | Woods KJP, Sampaio G, James T, Przysinda E, Spencer A, Hewett A, Spencer A, Morillon B, Loui P | *Communications Biology* (Nature portfolio) | fMRI blood flow + behavioral attention tasks; ADHD-symptoms subgroup | Brain.fm modulated music produced significantly greater activation in attentional and cognitive control networks vs. unmodulated control music and pink noise; improved task performance in participants with ADHD symptoms |
| Secondary (2019) | Woods KJP, Hewett A, Spencer A, Morillon B, Loui P | arXiv preprint (not peer-reviewed) | Behavioral attention in online participants | Modulation in background music improved sustained attention vs. control |
| Supporting (2018) | Woods KJP et al. | *Attention, Perception, & Psychophysics* | Headphone screening methodology | Methods paper; not an efficacy study |

Sources: [(Brain.fm science page)](https://www.brain.fm/science) | [(Communications Biology 2024 paper)](https://www.nature.com/articles/s42003-024-07026-3) | [(2019 arXiv preprint)](https://arxiv.org/abs/1907.06909)

**Evidence quality assessment (critical):**
- The 2024 *Communications Biology* paper is real, peer-reviewed, and in a reputable Nature-portfolio journal. This is the only peer-reviewed efficacy study directly on Brain.fm music.
- Sample size not surfaced in search snippets; effect sizes not publicly reported in detail beyond "significantly greater activation."
- The ADHD finding is for participants with ADHD *symptoms* (likely screening-based), not clinically diagnosed ADHD in an RCT. The press release calls it "world's first science-backed, purpose-built focus music for ADHD" — this overstates what one neuroimaging study with self-reported symptoms demonstrates.
- The 2019 study is a preprint, not peer-reviewed.
- NSF funding acknowledged, which adds credibility to methodology but does not validate the marketing framing.
- **Counterintuitive finding:** Brain.fm has more peer-reviewed support than most attention-music apps, but it is still one study. Claims about ADHD specifically are ahead of the evidence.

**Score sketch:** 6/10 for ND users.
*Justification: Real neuroscience foundation and one peer-reviewed study distinguish it from most competitors; limited to auditory regulation only; no adaptive personalization or ND-specific coaching; overstated ADHD marketing.*

---

## 3. Mindstrong (defunct, shut down early 2023)

**What it was:** Digital mental health startup that began as a passive digital-phenotyping biomarker company (using smartphone interaction patterns — typing cadence, scrolling speed — as proxy mental health signals), then pivoted to providing app-based mental health care. Raised $160M total.

**Why it failed — primary sources:**

Roy Perlis (MGH/Harvard), writing in STAT News (2023-02-06):
1. **Reimbursement gap:** Insurance reimbursement for mental health care was structurally inadequate. The company could not make the unit economics work even with tech-enabled efficiencies.
2. **Willingness-to-pay mismatch:** "Americans value mental health extremely highly until they have to pay for it." Consumer willingness to pay did not match stated demand.
3. **Tech-replaces-care fallacy:** The assumption that digital tools could substitute for, rather than augment, clinical care was incorrect. "Technology can improve care, it just can't replace actual care."
4. **Evidentiary gap:** The pivot from biomarker company to care company happened before the passive sensing science was validated in real-world settings. Pilot studies did not translate to high-quality clinical validation.

Additional reporting (STAT, April 2023; MedTech Dive):
- SonderMind acquired Mindstrong's technology assets in early 2023.
- Pear Therapeutics failed around the same time for overlapping reasons.
- Common pattern: promising pilot studies, then insufficient investment in rigorous follow-on trials, then payer refusal to cover unvalidated DTx.

Sources: [(STAT — Perlis, Feb 2023)](https://www.statnews.com/2023/02/06/mindstrong-demise-future-mental-health-care/) | [(STAT — April 2023 analysis)](https://www.statnews.com/2023/04/18/mindstrong-pear-future-digital-mental-health/) | [(MedTech Dive — SonderMind acquisition)](https://www.medtechdive.com/news/sondermind-acquires-mindstrong-technology-digital-mental-health/645794/)

**ND domain relevance:**
- `MON` — the original passive sensing premise (self-monitoring via behavioral digital biomarkers) maps directly to the self-monitoring/interoception domain
- `EMO` — mood tracking was a core stated use case

**Lessons for Yar specifically:**
- Passive behavioral biomarkers are scientifically promising but not yet proven for clinical-grade monitoring at consumer scale.
- Consumer MH apps need a value proposition that does not depend on insurance reimbursement for early-stage survival.
- The care-replacement framing is a fatal positioning error; augmentation framing (tech + human care) is safer and more honest.
- Validate in real-world settings before scaling; pilot efficacy does not transfer automatically.

**Score sketch (as a model):** N/A (defunct). Lesson rating for Yar: High relevance — directly maps to the passive-sensor risk scenario.

---

## 4. arXiv 2603.17258 — ADHD Task Management Paper (Verification)

### VERIFIED: CONFIRMED

**Full citation:**
Chen, J., Meng, Y., & Nie, K. (2026). "Not Just Me and My To-Do List": Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds. *arXiv:2603.17258* [cs.HC]. Submitted March 18, 2026; revised April 20, 2026. Accepted to CSCW 2026.

Source: [(arXiv abstract page, fetched directly)](https://arxiv.org/abs/2603.17258)

**Authors confirmed:** Jingruo Chen (Cornell University), Yibo Meng (Tsinghua University), Kexin Nie (University of Sydney).

**Venue confirmed:** Accepted to CSCW 2026 (ACM Conference on Computer-Supported Cooperative Work and Social Computing). This is a leading peer-reviewed HCI venue, not just a preprint.

**Methodology:**
- 22 semi-structured interviews with ADHD-identifying adults (core challenge discovery)
- Speed dating study with 20 additional ADHD-identifying adults evaluating 13 speculative AI design concepts

**Core challenge categories identified:**
- Task management failure is *not* a willpower deficit; it is driven by emotional and relational misalignments between ADHD cognitive needs and tools designed for neurotypical linear self-regulation
- Existing productivity tools assume consistent self-regulation and linear time — both atypical in ADHD
- ADHD task management is *relationally and affectively co-constructed* (not an isolated individual act)

**"AI-Augmented Social Scaffolds" concept:**
- The core design implication: AI should act as a social co-regulator, not just a task organizer
- Design directions include: co-regulation (AI as accountability partner), nonlinear attention rhythm support, affectively-aware scaffolding, distributed task ownership (involving trusted others via AI mediation)

**Attribution check — does this source support "~30 ADHD-validated task-management sub-features"?**
- Partially. The paper evaluates 13 speculative design concepts (from the speed dating study) and derives qualitative design implications. It does not produce a numbered list of 30 validated sub-features as discrete items.
- The paper provides strong qualitative grounding for feature categories, but any specific "30 sub-features" count likely represents internal Yar elaboration or synthesis across multiple sources, not a direct count from this paper alone.
- Recommendation: cite Chen et al. (2026) as the foundational qualitative grounding for the social-scaffold and co-regulation feature cluster, but do not attribute a specific sub-feature count to this paper without also citing the internal synthesis process.

---

## 5. Light Scan — Note-Taking and Knowledge Tools

### Obsidian
**What it is:** Local-first, Markdown-based personal knowledge management app with a rich plugin ecosystem.
**Standout ND-relevant features:** Graph view (nonlinear navigation between notes, `COG`); community plugin ecosystem has dozens of AI plugins (GPT-4/Claude/Ollama backends via AI Assistant plugin, updated Jan 2026); Daily Notes for routine structuring (`ATT`); no internet required (reduces context-switching anxiety, `EMO`).
**AI:** Plugin-based, not native; requires user configuration.
**Score sketch:** 6/10 for ND users. Strong COG and ATT support via nonlinear structure; high setup friction is a real ND barrier.
Source: [(Storyflow 2026 comparison)](https://storyflow.so/blog/best-obsidian-alternatives-2026)

### Logseq
**What it is:** Open-source, local-first, outline-and-graph knowledge base. Block-based, bidirectional links.
**Standout ND-relevant features:** Block-level granularity supports nonlinear thought capture (`COG`); task tracking within notes reduces tool-switching (`ATT`); open-source = no subscription anxiety (`EMO`).
**AI:** Community plugins; no native AI as of mid-2026. Development pace has slowed.
**Score sketch:** 5/10 for ND users. Excellent COG fit; lower polish and slower development than competitors.

### AFFiNE
**What it is:** Open-source, local-first tool combining Markdown notes, infinite canvas (whiteboard), and database/Kanban in a single interface.
**Standout ND-relevant features:** Infinite canvas for spatial/visual thinking (`COG`); explicit ADHD-targeted daily planner templates (`ATT`); blends structured and unstructured modes in one tool (reduces app-switching overhead); free and open-source.
**AI:** AI writing and summarization features present (extent not fully detailed in 2026 sources).
**Score sketch:** 6/10 for ND users. Best multi-modal cognitive style support of the four; newer product with lower ecosystem maturity.
Source: [(AFFiNE blog)](https://affine.pro/blog)

### Notion
**What it is:** Cloud-based all-in-one workspace (notes, databases, wikis, tasks).
**Standout ND-relevant features:** Highly flexible structure (can be adapted for ND workflows, `COG`); Notion AI add-on (Q&A over notes, automated summaries, table-fill; $10/user/month since Oct 2025 v3.11, `ATT`).
**AI:** Native AI add-on, one of the more mature implementations in this category.
**Score sketch:** 5/10 for ND users. Powerful but high configurability creates setup paralysis, a known ADHD trap; requires sustained motivation to maintain; AI features are useful but not ND-specific.
Source: [(tech-insider.org 2026 comparison)](https://tech-insider.org/notion-vs-obsidian-2026/)

---

## Comparative Matrix

| Tool / Source | ND Domains | AI Present | Evidence Quality | Score |
|---------------|-----------|-----------|-----------------|-------|
| Lovable mind-mapping | COG, ATT | Yes (builder AI) | None (marketing) | 4/10 |
| Brain.fm | ATT, SEN | AI-assisted composition | 1 peer-reviewed study (Communications Biology 2024); 1 preprint | 6/10 |
| Mindstrong (defunct) | MON, EMO | Passive sensing + care delivery | Pilot only; not RCT-validated | N/A (lesson source) |
| Chen et al. 2026 (paper) | ATT, EMO, SOC | AI design concepts evaluated | CSCW 2026 (peer-reviewed HCI venue); qualitative | High relevance |
| Obsidian | COG, ATT | Plugin-based | None (tool, not a study) | 6/10 |
| Logseq | COG, ATT | Plugin-based | None | 5/10 |
| AFFiNE | COG, ATT | Native (partial) | None | 6/10 |
| Notion | COG, ATT | Native add-on | None | 5/10 |

---

## Key Assumptions Contradicted by Evidence

1. **Brain.fm has robust ADHD evidence — FALSE.** There is one peer-reviewed study (Communications Biology, 2024). It uses participants with ADHD *symptoms*, not clinical diagnosis, and no effect sizes are published in accessible summaries. The "world's first science-backed ADHD focus music" marketing is ahead of the data.

2. **Chen et al. (2026) validates ~30 discrete ADHD task-management sub-features — OVERSTATED.** The paper evaluates 13 speculative design concepts and provides qualitative design implications. A numbered sub-feature count is a downstream synthesis, not a direct paper output. The paper does provide strong grounding for the social-scaffold and co-regulation feature cluster.

3. **Lovable.dev offers a neurodiversity-relevant mind-mapping product — INCORRECT.** The mind-mapping page describes what builders can create on Lovable; it is not a shipped ND-focused mind-mapping app. No ND UX validation exists.

4. **Mindstrong failed because its technology was bad — INCORRECT.** The primary causes were structural insurance reimbursement inadequacy and the tech-replaces-care positioning error, not scientific invalidity of the digital phenotyping concept.

---

## Sources

- [Lovable mind-mapping use case page](https://lovable.dev/solutions/use-case/mind-mapping-tools)
- [Brain.fm science page](https://www.brain.fm/science)
- [Woods et al. 2024 — Communications Biology (primary Brain.fm study)](https://www.nature.com/articles/s42003-024-07026-3)
- [Woods et al. 2019 — arXiv preprint](https://arxiv.org/abs/1907.06909)
- [Brain.fm ADHD press release (Yahoo Finance / PRNewswire)](https://finance.yahoo.com/news/brain-fms-adhd-music-breakthrough-140100580.html)
- [Chen, Meng & Nie 2026 — arXiv:2603.17258 (CSCW 2026)](https://arxiv.org/abs/2603.17258)
- [STAT — Perlis, Mindstrong demise (Feb 2023)](https://www.statnews.com/2023/02/06/mindstrong-demise-future-mental-health-care/)
- [STAT — Mindstrong/Pear analysis (Apr 2023)](https://www.statnews.com/2023/04/18/mindstrong-pear-future-digital-mental-health/)
- [MedTech Dive — SonderMind acquires Mindstrong](https://www.medtechdive.com/news/sondermind-acquires-mindstrong-technology-digital-mental-health/645794/)
- [Storyflow — Obsidian alternatives 2026](https://storyflow.so/blog/best-obsidian-alternatives-2026)
- [AFFiNE blog](https://affine.pro/blog)
- [tech-insider.org — Notion vs Obsidian 2026](https://tech-insider.org/notion-vs-obsidian-2026/)
