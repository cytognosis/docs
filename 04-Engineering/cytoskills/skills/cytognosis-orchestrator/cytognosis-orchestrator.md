> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, researchers, all Cytognosis skill users
> **Tags**: `orchestration`, `routing`, `cytognosis-orchestrator`

# cytognosis-orchestrator — Task Orchestrator Skill

> **Reading time**: ~6 minutes
> **If you only read one thing**: Load this skill FIRST when a task spans 2+ skills, involves complex decisions, or when you are unsure which skill to use. It classifies your task and routes to the right specialist.

---

## What It Is and Why

`cytognosis-orchestrator` is the master entry point for multi-skill and ambiguous Cytognosis tasks. It classifies work by type, routes to the correct specialist among the eight Cytognosis skills, provides structured reasoning frameworks, and guards context health across long sessions.

**When to load this skill**:

- Task involves 2+ skills or tools
- Research-then-creation pipeline (e.g., evaluate options, then document the decision)
- Complex decisions that need a reasoning protocol
- Any request exceeding 3 sequential tool calls
- Unsure which skill to use
- Recovering a degraded context window
- Task type is ambiguous

**When NOT to use this skill** (go direct to the specialist):

- You know exactly which skill applies; route there directly
- Simple single-skill tasks (e.g., "write an ADR" → `cytognosis-doc`)

---

## The Eight Skills

| # | Skill | Domain | Key Capabilities |
|---|-------|--------|-----------------|
| 1 | **cytognosis-dev** | Building | Cytocast/Cytoskeleton, nox, CI/CD, profiles, steering docs, spec-driven dev |
| 2 | **cytognosis-doc** | Writing | 34 doc types, research methodology, ADHDfy pipeline |
| 3 | **cytognosis-design-system-master** | Designing | Brand tokens, profiles, glassmorphism, deck/email templates |
| 4 | **cytognosis-template-master** | Scaffolding | Phone/web/desktop/extension app templates, cross-template rules |
| 5 | **cytognosis-branding** | Brand depth | 12 v10 reference files, full color/typography/icon systems |
| 6 | **cytognosis-writer** | Proposals | Grants, pitches, DMP, science narratives, founder story |
| 7 | **cytognosis-org** | Operations | Drive, GCP, repos, calendars, document naming, email |
| 8 | **cytognosis-orchestrator** | Routing | This skill: reasoning, context health, multi-agent coordination |

---

## Task-Type Router

```
BUILDING software (scaffolding, coding, configuring, testing)?
└─ LOAD cytognosis-dev
   ├─ Steering docs? → dev § Steering Documents
   └─ Spec-driven feature? → dev § Spec-Driven Development

WRITING documentation (any doc type, research, ADHDfy)?
└─ LOAD cytognosis-doc
   ├─ Market/tool/model comparison? → doc § Research Document Creation
   ├─ ADHDfy a document? → doc § ADHDfy Transformation
   └─ Standard doc type? → doc decision matrix → appropriate template

DESIGNING visual output (UI, branded assets, presentations)?
└─ LOAD cytognosis-design-system-master
   └─ Need full v10 depth? → LOAD cytognosis-branding (next response only)

SCAFFOLDING an interface app (phone, web, desktop, extension)?
└─ LOAD cytognosis-template-master

WRITING grants, proposals, science narratives?
└─ LOAD cytognosis-writer

MANAGING files, workspace, Google Workspace ops?
└─ LOAD cytognosis-org

DEEP BRAND reference (full color system, every shade, every icon)?
└─ LOAD cytognosis-branding

UNSURE or MULTI-SKILL task?
└─ STAY on this skill; use Reasoning Protocols below
```

---

## Keyword → Skill Map

| Keywords | Skill |
|----------|-------|
| Cytognosis design, brand colors, violet/azure/indigo, signature gradient, Inter/Newsreader/JetBrains Mono, glassmorphism, Foundation/Clinical/Research/Lab profile, deck design, email signature | `cytognosis-design-system-master` |
| Phone app, web app, desktop app, browser extension, Flutter, Tauri, MV3, LiteRT-LM, scaffold a new product, interface template, voice loop | `cytognosis-template-master` |
| Full v10 spec, every shade, every gradient, every icon variant, complete accessibility audit, full data-viz palette | `cytognosis-branding` |
| cytocast, cytoskeleton, copier, nox, ruff, ty, uv, pytest, CI/CD, pyproject.toml, environment, .agents/steering, spec-driven, coding standards | `cytognosis-dev` |
| Grant, proposal, pitch, specific aims, Three Blindspots, Cytoverse, FAIR, meeting transcript, founder story | `cytognosis-writer` |
| Email, Drive, calendar, where is, repo list, GCP, @cytognosis.org, document naming | `cytognosis-org` |
| ADR, RFC, module spec, system doc, API reference, changelog, troubleshooting, runbook, SOP, documentation, template, market research, tool evaluation, model comparison, ADHDfy, dataset doc, DMP, data management plan, sensor spec | `cytognosis-doc` |

---

## Common Multi-Skill Sequences

| Task | Sequence (one skill per response) |
|------|----------------------------------|
| New feature (spec-driven) | `dev` (requirements + design + tasks) → `doc` (walkthrough after implementation) |
| Competitive analysis | `doc` (research → scoring matrix) → `doc` (ADHDfy → simplified version) |
| New project setup | `dev` (scaffold + steering init) → `template-master` (if interface app) → `design-system-master` (brand application) |
| Grant proposal | `writer` (narrative) → `design-system-master` (visuals) → `branding` (deck template) |
| Architecture decision | `doc` (research) → `doc` (ADR template) |
| New patient app | `template-master` (phone delta) → `dev` (cytocast scaffold) → `design-system-master` (brand) |
| Port design tokens | `template-master` (all deltas) → `dev` (copier update mechanics) |

---

## Disambiguation: When Task Types Overlap

| Situation | Route | Rationale |
|-----------|-------|-----------|
| "Set up steering for a new project" | `cytognosis-dev` | Steering is project config, not documentation |
| "Research competitors for voice agents" | `cytognosis-doc` (§ Research) | Research produces documents |
| "Make this doc easier to read" | `cytognosis-doc` (§ ADHDfy) | ADHDfy is a doc transformation |
| "Design a dashboard" | `cytognosis-design-system-master` | Visual output |
| "Write an ADR for the database choice" | `cytognosis-doc` | Documentation (ADR template) |
| "Build the data pipeline" | `cytognosis-dev` | Software construction |
| "Style this for our brand" | `cytognosis-design-system-master` | Brand application |
| "Where do grant proposals live?" | `cytognosis-org` | File location question |
| "Compare task queue libraries" | `cytognosis-doc` (§ Research) | Tool evaluation research |
| "Where are the Cytoplex spec docs?" | `cytognosis-org` (docs repo: `https://github.com/cytognosis/docs/tree/main/cytonome/cytoplex`) | File location |

---

## Reasoning Protocols

### Problem Decomposition

Before any substantive task:

1. **What is the actual request?** Strip ambiguity. State the deliverable.
2. **What do I already know?** Check MEMORY.md, prior artifacts, conversation history.
3. **What do I need to learn?** Identify knowledge gaps.
4. **What could go wrong?** Name the top 2-3 failure modes.

### Decision Classification

| Type | Characteristics | Action |
|------|----------------|--------|
| Two-way door | Easily reversible, low consequence | Decide fast, iterate |
| One-way door | Hard to undo, high consequence | Slow down, verify, get confirmation |

Cytognosis examples:

- **Two-way**: Code formatting, nox session naming, draft microcopy
- **One-way**: License selection, API contract, database schema, grant submission, brand-token rename

### Second-Order Thinking

1. **And then what?** Downstream consequences.
2. **Who else is affected?** Other repos, downstream users, CI pipelines.
3. **Maintenance burden?** Tech debt created.

### Scientific Reasoning (for research tasks)

1. **Hypothesis**: state what you believe and why
2. **Test**: what evidence would confirm or refute?
3. **Revise**: update based on findings
4. **Communicate**: frame through the Revelation Arc (Mystery → Insight → Resolution)

---

## Context Management

### Budget Rules

- Max output: 10K tokens per response
- PubMed / bioRxiv search: cap at 5 results
- Tool calls: max 3 sequential per turn before yielding
- Web fetching: `text_content_token_limit=4000`

### Forbidden Same-Response Combos

Never combine these in one response (they cause context overflow):

- Two skill reads in one response
- Skill read + full-text fetch
- Research search + document creation
- Drive fetch + PubMed full-text
- `design-system-master` + `template-master` in the same response

### Context Health Protocol

| Trigger | Action |
|---------|--------|
| Every 10-15 tool exchanges | CHECKPOINT: synthesize constraints, verify facts |
| Context > 50K tokens | SESSION HANDOFF: write summary artifact, recommend new conversation |
| Hallucinated fact detected | STOP: checkpoint, verify against source files |
| Conflicting instructions | ESCALATE: surface the conflict, ask for resolution |

---

## Multi-Agent Execution

| Mode | When | Cost |
|------|------|------|
| Solo | Simple, strict dependencies | 1x |
| Subagents | Parallel research | 1x (shared context) |
| Agent Teams | Adversarial review, system-wide refactoring | 4x (limit usage) |

---

## Routing Rules

1. **One skill per response**: never load two SKILL.md files in the same response.

Forbidden same-response pairs:

- `design-system-master` + `branding`
- `design-system-master` + `template-master`
- `writer` + `design-system-master`
- `dev` + `org`

2. **Never route to deleted skills**: the standalone `cytognosis-steering`, `cytognosis-research`, and `cytognosis-adhdfy` skills no longer exist. Their capabilities live inside `cytognosis-dev` and `cytognosis-doc`.

---

## Hard Rules (NEVER)

- NEVER ask "What would you like me to help you with?" Provide work autonomously.
- NEVER end with a direction-seeking question when the next step is obvious.
- NEVER combine massive context-consuming tools in a single response.
- NEVER read two Cytognosis SKILL.md files in one response.
- NEVER skip the reasoning protocol for one-way-door decisions.
- NEVER proceed on assumption when verification is available and cheap.
- NEVER load `cytognosis-branding` for a routine design task; load `cytognosis-design-system-master` instead.

---

## Example: Multi-Skill Task

**User request**: "Research vector databases for the Yar knowledge graph, write an ADR, and create an ADHD-friendly version."

**Sequence**:

1. Response 1: Load `cytognosis-doc`. Run `cyto research tool "vector database"`. Produce scoring matrix.
2. Response 2: Load `cytognosis-doc`. Use ADR template. Write `ADR-005-vector-database-selection.md`.
3. Response 3: Load `cytognosis-doc`. Run `cyto doc adhdfy ADR-005-vector-database-selection.md`. Produce vault variant.
