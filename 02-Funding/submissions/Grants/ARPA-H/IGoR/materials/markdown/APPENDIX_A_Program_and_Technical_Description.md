# Appendix A: Program and Technical Description

> [!NOTE]
> **Type:** PDF · **Source file:** `materials/APPENDIX+A_Program+and+Technical+Description_IGoR.pdf` · **Extracted text:** `materials/extracted-text/AppA_Program_Technical.txt`
> **Governs:** Full technical requirements, four Technical Areas, phase structure, milestone/metric tables, IV&V roles, and management expectations for IGoR performers.

## At a glance (BLUF)

Appendix A defines the complete scientific and technical scope of the IGoR program. It specifies four Technical Areas (TAs), a 5-year/3-phase program structure with quantitative milestones and metrics, and the roles of Independent Verification and Validation (IV&V) partners. Any proposal that does not address all four TAs "will not be reviewed."

## Key facts

| Item | Value |
|---|---|
| **Agency / Office** | Advanced Research Projects Agency for Health (ARPA-H), Proactive Health Office |
| **Program name** | Intelligent Generator of Research (IGoR) |
| **Instrument** | Other Transaction (OT) Agreement |
| **Anticipated awards** | Approximately 3 multidisciplinary teams |
| **Program duration** | 5 years, 3 phases |
| **Phase I** | 18 months, Concept and Component Development |
| **Phase II** | 18 months, Integration and Interoperability |
| **Phase III** | 24 months, Scaling, Generalization, and Transition |
| **Budget ceiling** | None stated in Appendix A |
| **Disease areas** | 1 primary (Phase I/II); 1 additional related area required by Phase III |
| **Minimum TA4 laboratories** | At least 2 per team |
| **Required key personnel** | PI, Project Manager (named), Software Architect (named, distinct from PI/PM) |
| **IV&V cost** | Not budgeted by performers; collaboration effort must be budgeted |
| **Vertebrate animal experiments** | Limited; allowed only for testing strong predictions; must be directed by human researcher |
| **Human clinical trials** | Out of scope |
| **Page limits** | Not stated in Appendix A (see Appendix B/C) |

## Structure / contents

1. **Program Overview**, Four-component vision; 10x cycle-time target
2. **Background**, Reproducibility crisis; fragmented mechanistic knowledge; gap in existing AI-to-lab systems
3. **Program Description**
   - Core design principles (high cohesion, low coupling; human augmentation not replacement)
   - National health impact
   - Disease focus guidance and justification requirements
   - Experiment scope (cell/tissue, lower invertebrates in scope; vertebrates limited; clinical trials out)
4. **IGoR Technical Areas**
   - **TA1: Comprehensive Disease Models**, Digital twins; modular, mechanistic, multiscale, verifiable; 2 objectives
   - **TA2: New Science Engine**, AI orchestration; hypothesis generation; explainability/human interface; 2 objectives
   - **TA3: Interoperable Experimental Procedures**, Layered protocol stack (Intent / Protocols / Calibration / Hardware); standards development; 2 objectives
   - **TA4: Experiment Marketplace**, Validated laboratory network; reproducible experimentation; marketplace operations; 2 objectives
5. **Program Structure**
   - 5.1 Proposal Scope, All 4 TAs required; 1 PI/prime performer; sub-performer overlap rules
   - 5.2 Phases, Phase I (18 mo), Phase II (18 mo), Phase III (24 mo)
   - 5.3 Program Milestones and Metrics, Table 1 (milestones by TA/phase); Table 2 (quantitative metrics)
   - 5.4 IV&V, Mechanistic Model IV&V (TA1); Experimental Infrastructure IV&V (TA3/TA4); Expert Panel
   - 5.5 Project Management, Integration, and Collaboration, PM role, Software Architect role, cross-team APA obligations
   - 5.6 Commercial Transition, Partnership models; open data layer as sustainability foundation

## What it requires of a proposer

- **Address all four TAs (TA1, TA2, TA3, TA4)** in a single proposal under a single prime performer and a single PI. Proposals missing any TA are not reviewed.
- **Justify disease focus**, demonstrate tractability through mechanistic/quantitative modeling, multifactorial or multiscale complexity, and feasibility within the program timeframe.
- **Plan interface definitions**, describe initial approach to TA-to-TA interfaces (information format and cadence); boundaries will evolve through Phase I Domain-Driven Design workshop.
- **Include at least two TA4 laboratories** with two-way capability communication established by end of Phase I.
- **Name a Project Manager** with project management expertise and sufficient level of effort for cross-TA coordination, delivery tracking, and reporting.
- **Name a Software Architect** (distinct from PI and PM) with demonstrated experience building interoperable, API-first systems; must exercise architectural authority over implementation decisions.
- **Containerize all TA1 models and software** so IV&V partner can build and execute them on an independent environment (100% of artifacts, Phase I milestone).
- **Plan for IV&V collaboration effort** (containerization, documentation, material transfer, biannual reviews), do not budget IV&V partner costs, but budget your own effort.
- **Participate in cross-team activities**: Domain-Driven Design workshop (Phase I kickoff), TA3 bake-offs and RFC process (Phases I-II), cross-team lab execution (Phases II-III), connect-a-thon (Phase III).
- **Propose additional quantitative metrics** beyond the program minimums, appropriate to the team's specific approach.
- **Extend disease model to a second related disease area** by Phase III.
- **Engage external standards bodies and equipment manufacturers** to ensure TA3 protocol standards have adoption potential beyond IGoR.
- **Deliver all computational artifacts to a public repository** with open-access certification by end of Phase III.
- **Establish at least one sustained partnership or adoption path** (e.g., NIH center, cloud lab provider, academic consortium) by Phase III.
- **Describe commercialization approach** for IGoR components throughout the program.

## Watch-outs

> [!IMPORTANT]
> **Hard gate, all four TAs required:** "Proposals not addressing all four TAs will not be reviewed." A proposal covering only TA1/TA2 or any subset is disqualified at intake.

> [!IMPORTANT]
> **Single prime, single PI:** Proposals must be submitted under one prime performer led by one PI covering all three phases. Multi-prime structures are not permitted.

> [!IMPORTANT]
> **Sub-performer overlap rule:** If ARPA-H selects two proposals using the same sub-performer in the same TA, ARPA-H may fund the overlapping work only once or require the sub-performer to elect one project. Plan sub-performer commitments accordingly.

> [!IMPORTANT]
> **Phase I walking skeleton milestone:** The system must demonstrate a closed-loop cycle (TA2 proposes experiment, TA3 generates protocol, TA4 executes, data returned to TA1) within Phase I. This is a continuation gate.

> [!WARNING]
> **Phase III second disease area:** By Phase III, teams "must extend their approach to a related disease area." This is mandatory, not optional, and affects TA1 model scope, TA2 experiment design, and TA4 laboratory coverage.

> [!WARNING]
> **TA2 is not an LLM wrapper:** "Systems that merely prompt an LLM to suggest experiments and route them to an automated laboratory do not meet the requirements of this program." The proposal must demonstrate mechanistic grounding, multi-modal design, and distributed execution across heterogeneous labs.

> [!WARNING]
> **Vertebrate animal experiments are limited:** They are allowed only for "testing strong predictions of a working system" and "must be directed solely by the human researcher." TA3 protocols focus on cell/tissue culture and lower invertebrates only.

> [!WARNING]
> **Software Architect role is mandatory and distinct:** The proposal "should name" (effectively must name) the individual responsible for interface design and architectural authority. This person is distinct from both the PI and the Project Manager.

> [!CAUTION]
> **TA1/TA2 boundary for knowledge gap identification is explicitly open:** ARPA-H states the optimal boundary "is an open question and expects that it will be refined during the program." Do not over-specify this in the proposal; describe your approach and justify your placement.

> [!CAUTION]
> **Phase II cross-team reproducibility threshold:** Concordance must be "≥85%" for cross-team laboratory execution (Table 1, TA4 Phase II). Phase III requires "≥90% concordance on standardized experiments" across all marketplace laboratories. These are hard numeric gates.

> [!CAUTION]
> **10x Experimental Cycle Time target:** The baseline is established in Phase I using conventional approaches. Phase II requires "≥4x improvement"; Phase III requires "≥10x improvement." Proposers must describe how they will establish and measure the baseline rigorously.

> [!CAUTION]
> **Model update latency metrics:** Phase II requires model update latency of "≤24 hours" from data receipt. Phase III tightens to "≤4 hours." Infrastructure and pipeline design must support these timelines.

## Cross-references

- [ISO, ARPA-H-SOL-26-155](ISO_ARPA-H-SOL-26-155.md), solicitation dates, eligibility, submission process
- [Comprehensive Reference](../IGoR_Comprehensive_Reference.md), full IGoR program reference
- [Appendix B, Solution Summary Format and Instructions](APPENDIX_B_Solution_Summary_Format_and_Instructions.md), Solution Summary format and instructions
- [Appendix C, Proposal Format and Instructions](APPENDIX_C_Proposal_Format_and_Instructions.md), full-proposal format, page limits, and evaluation criteria
