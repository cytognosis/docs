# Coding-Agent Productivity Multipliers for Yar Timeline Planning

Prepared: 2026-07-19. Purpose: give Yar (Tauri v2 + TypeScript + Rust + Django, mixed greenfield/brownfield) a defensible, cited productivity multiplier for timeline scenarios. Read-only research; this is the only file written.

**If you only read one thing:** recommended multiplier for **1 FTE + coding agent is 1.5x to 2.0x** project-level throughput vs. an unaided FTE (mid case 1.7x), not 10x. The evidence supports large multiplier on toy/greenfield tasks (up to 1.5-2x on isolated, well-specified work) but shows a net *slowdown* on mature-codebase debugging in the closest real-world analog (METR 2025). Reading time: about 9 minutes.

---

## 1. Evidence summary

- **GitHub Copilot RCT (Peng et al. 2023, Microsoft/GitHub/MIT)**: developers implementing an HTTP server in JavaScript with Copilot finished in 71 minutes vs. 160 minutes without it, a **55% reduction in completion time** (95% CI: 21%-89%), plus a higher completion rate (78% vs. 70%). Less experienced and older developers benefited more. Caveat: single, narrow, well-specified greenfield task, novice-friendly language, no existing codebase, no code review or integration step, short session. This is a **task-level ceiling**, not a project-level number.
  Source: https://arxiv.org/pdf/2302.06590 ; https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/

- **METR RCT, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (July 2025)**: 16 experienced developers (avg. 5 years on their own mature repos, avg. 22,000+ stars / 1M+ LOC) completed 246 real issues/PRs. When allowed to use AI tools (Cursor Pro, Claude 3.5/3.7 Sonnet), they took **19% longer**, not shorter. Developers had *forecast* a 24% speedup beforehand and *believed after the fact* they'd been sped up ~20%; both were wrong in direction. This is the closest published analog to Yar's brownfield-fix, senior-dev-on-familiar-codebase situation. Caveat: n=16, agentic tooling has improved since early 2025, and METR itself later revised its experiment design (see below), but it is the only RCT measuring real repo work with experienced maintainers, and it directly contradicts naive "always faster" assumptions.
  Source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; https://arxiv.org/pdf/2507.09089 ; METR's own follow-up acknowledging design limits: https://metr.org/blog/2026-02-24-uplift-update/

- **SWE-bench Verified**: a 500-task, human-vetted subset of real GitHub issues, used as the standard benchmark for autonomous agent coding capability. Top models (Claude Opus 4.5/4.6-class) now solve roughly **80%** of tasks autonomously as of early-to-mid 2026, up from the 50-70% range in 2024. Caveat: SWE-bench measures **whether** an agent can produce a merged-equivalent patch for a pre-selected, bounded, single-repo issue with a defined test oracle, under no wall-clock or cost pressure, and with no human review/iteration loop. It is a capability proxy, not a speed or throughput measure, and it systematically excludes the ambiguous, multi-system, "figure out what to build" work that dominates real feature delivery (e.g., Yar's Tauri-to-Rust-to-Django integration surfaces).
  Source: https://llm-stats.com/benchmarks/swe-bench-verified ; https://www.mindstudio.ai/blog/claude-mythos-benchmark-results-swe-bench-agentic-coding

- **DORA 2025 (State of AI-assisted Software Development, Google Cloud/DORA)**: for the first time, AI adoption shows a **positive relationship with software delivery throughput** (reversing a negative finding in the 2024 report), but AI adoption continues to show a **negative relationship with delivery stability**, i.e., faster shipping with more downstream breakage. DORA introduced a new **Rework Rate** metric specifically because AI-accelerated teams are producing more unplanned/rework deployments. Headline framing: "AI amplifies what's already there" — high-performing teams get faster and better, dysfunctional teams get faster and more broken. Caveat: this is large-n survey/perception data across many orgs and tools, not a controlled experiment, so it cannot isolate a clean multiplier, and it doesn't separate greenfield from brownfield work.
  Source: https://dora.dev/dora-report-2025/ ; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

- **Brooks's Law and empirical team-size studies**: adding people to a project increases communication paths combinatorially and imposes ramp-up cost (NASA Software Engineering Laboratory documented 3-6 month ramp-up for new engineers on existing codebases), so headcount does not scale linearly with output. A 117-project empirical study in Finland found maximum team size negatively correlated with development productivity. Caveat: these are pre-AI-agent studies of human coordination overhead; they establish the *shape* of the problem (sublinear scaling for both human-only and human+agent teams) but don't quantify an AI-era correction factor.
  Source: https://effectiviology.com/brooks-law/ ; https://www.researchgate.net/publication/228233532_Brooks'_Law_Revisited_Improving_Software_Productivity_by_Managing_Complexity

- **Synthesis point (not a single citation, drawn from all of the above)**: the gap between the Copilot RCT (+55% on a 90-minute greenfield toy task) and the METR RCT (-19% on real fixes in mature repos by experienced owners) is best explained by task type and context load. Agents shine on boilerplate, scaffolding, test-writing, and well-specified isolated greenfield work; they cost time on deep-context brownfield debugging because of review overhead, hallucinated fixes, wrong-context edits, and the time senior developers spend verifying agent output against tacit codebase knowledge the agent doesn't have. This context-dependence is the central variable for Yar's multiplier, since Yar is explicitly a mix of both.

---

## 2. Recommended multipliers (vs. 1 FTE, no agent, baseline = 1.0x)

| Scenario | Realistic multiplier (low-mid-high) | Rationale | Key caveats |
|---|---|---|---|
| **1 FTE, no agent** | 1.0x (fixed baseline) | Reference point. | N/A |
| **1 FTE + coding agent** | **1.3x - 1.7x - 2.2x** | Mid case reflects that Yar's mix of greenfield UI/boilerplate/tests (agent-favorable, Copilot-RCT-like) and brownfield Rust/Tauri/Django debugging (METR-like, can be neutral-to-negative) roughly offsets. High end applies only when the FTE is senior, single-threaded, and working on greenfield/boilerplate-heavy sprints; low end applies during deep debugging weeks. | Review overhead is real: a senior dev must read and verify every agent diff, which eats into the raw generation speedup. METR shows this can flip net-negative on unfamiliar-to-the-agent, high-context code. |
| **3 FTE, no agent** | **2.2x - 2.5x - 2.7x** (vs. 1 FTE) | Sublinear per Brooks's Law: coordination, code review among humans, merge conflicts, and onboarding/context-sharing overhead mean 3 people rarely deliver 3x. | Assumes the 3 are already ramped on Yar; a fresh hire's 3-6 month ramp (NASA SEL finding) would depress this further in year one. |
| **3 FTE + coding agents** | **3.0x - 3.8x - 4.7x** | Agent uplift applies per-developer (roughly the 1.3-2.2x band above) but the human-coordination ceiling from Brooks's Law still caps overall scaling; agents do not remove the need for humans to review each other's (and the agent's) code, so overhead does not vanish, and in fact PR/review volume rises, adding a further coordination tax DORA's "rework rate" flags. | High end assumes strong existing test coverage and modular boundaries so agents in parallel do not collide; low end assumes current Yar test/coverage maturity, which is likely partial. |

**Do not use 10x, or even parallel-scenario numbers like "3 FTE = 6-9x," for planning.** No cited source, including the vendor-friendliest one (Copilot RCT), supports a project-level multiplier above roughly 2x for a single senior developer on mixed work, and the one RCT closest to Yar's actual conditions (mature repo, experienced owner, real fixes) found a net slowdown.

---

## 3. Grounded assessment of "1 FTE + coding agent > 2 FTE, maybe up to 10x"

**Where this is plausible:**
- Pure greenfield, boilerplate-heavy work (new UI screens, CRUD scaffolding, test-writing, config, migrations, repetitive API wiring) with a single expert driver who has full context and can review fast. This is exactly the Copilot RCT's regime (+55% on an isolated, well-specified task), and it is where a single strong engineer plus an agent can plausibly outproduce two mid-level engineers, since there is no second person's context, review, or coordination cost to pay. In short bursts of this kind of work, multipliers toward the high end of 2x, and in the best-case narrow task, momentarily higher, are defensible.
- Cytognosis-relevant analogy: Yar's Tauri v2 shell UI, TypeScript frontend scaffolding, Django CRUD/admin surfaces, and test suites are the parts of the stack where this dynamic should hold.

**Where this is not plausible, and the 10x framing should be retired:**
- **Deep brownfield debugging** (existing Rust/Tauri IPC bugs, race conditions, state sync issues): this is the METR study's exact regime, and it found experienced developers were 19% *slower* with AI tools on real fixes in mature repos, not faster. Yar's brownfield work sits here.
- **Novel algorithmic/research components** described in the planning docs, specifically the **PeT knowledge-graph construction, sync logic, and mind-mapping structure-revision system**: these require design judgment, correctness reasoning about non-obvious data structures, and iterative research thinking that SWE-bench-style benchmarks explicitly do not test (SWE-bench tasks are pre-scoped, single-repo, test-oracle-defined; these components are the opposite: ill-defined, cross-cutting, and validated by domain judgment, not a test suite that already exists). Coding agents are good scaffolders for such code once the design is fixed, but the design work itself is agent-resistant, and a wrong agent-generated structural choice here is expensive to unwind later, which is the same "review/verification tax" mechanism DORA's rework-rate finding and the METR result both point to.
- **The "2 FTE" comparison specifically**: two competent engineers bring parallel throughput on independent workstreams (one can do PeT/KG design while the other does Tauri UI) in a way a single agent-assisted engineer cannot, no matter how fast the agent is, because the single engineer is still serial on judgment calls. Coding agents amplify an individual's typing/scaffolding speed; they do not add a second independent brain for architecture decisions or parallel-track ownership.

**Recommendation:** treat "1 FTE + agent beats 2 FTE" as true for greenfield/boilerplate sprints only, and false (likely net negative or flat) for PeT/KG, sync, and structure-revision work. Do not plan the KG/sync/mind-mapping timeline assuming any agent multiplier above roughly 1.0x-1.3x; plan the UI/CRUD/test-writing timeline assuming 1.5x-2.2x.

---

## 4. Effective engineer-weeks per 13-week quarter

Baseline: **1 FTE, no agent = 10 effective engineer-weeks per 13-week quarter** (per the parameters given; implies roughly 77% utilization after meetings, review, context switching, and non-coding overhead, which is a standard planning haircut and not itself a new claim).

| Scenario | Multiplier (mid case used) | Effective eng-weeks / 13-wk quarter |
|---|---|---|
| 1 FTE, no agent | 1.0x | **10** |
| 1 FTE + coding agent | 1.7x (range 1.3x-2.2x) | **17** (range 13-22) |
| 3 FTE, no agent | 2.5x (range 2.2x-2.7x) | **25** (range 22-27) |
| 3 FTE + coding agents | 3.8x (range 3.0x-4.7x) | **38** (range 30-47) |

Use the low end of each range for any quarter that is debugging-heavy or touches PeT/KG/sync/structure-revision work; use the high end only for quarters that are predominantly greenfield UI, scaffolding, or test-writing.

---

## Sources (all cited above, consolidated)

- Peng et al. 2023, GitHub Copilot RCT: https://arxiv.org/pdf/2302.06590
- Microsoft Research summary: https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity": https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ and https://arxiv.org/pdf/2507.09089
- METR experiment-design update: https://metr.org/blog/2026-02-24-uplift-update/
- SWE-bench Verified leaderboard: https://llm-stats.com/benchmarks/swe-bench-verified
- SWE-bench Verified / Claude results context: https://www.mindstudio.ai/blog/claude-mythos-benchmark-results-swe-bench-agentic-coding
- DORA 2025 report: https://dora.dev/dora-report-2025/
- Google Cloud announcement of 2025 DORA report: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- DORA 2025 takeaways (rework rate, amplifier framing): https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025
- Brooks's Law overview and empirical grounding: https://effectiviology.com/brooks-law/
- Brooks's Law Revisited (117-project Finnish study): https://www.researchgate.net/publication/228233532_Brooks'_Law_Revisited_Improving_Software_Productivity_by_Managing_Complexity

**Where evidence is thin:** there is no published controlled study of multi-developer teams paired with coding agents on mixed greenfield/brownfield codebases at Yar's scale. The "3 FTE + agents" row above is an extrapolation (per-developer agent uplift applied within a Brooks's-Law-capped team-scaling model), not a directly cited effect size, and should be treated as the most uncertain number in this document. Re-check against DORA's 2026 report and any updated METR uplift study before locking a multi-quarter roadmap.
