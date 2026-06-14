> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, researchers, all Cytognosis skill users
> **Tags**: `quick-reference`, `cytognosis-orchestrator`

# cytognosis-orchestrator — Quick Reference

> **One line**: Load this skill first for any task spanning 2+ skills, complex decisions, or when unsure which skill to use; it classifies the task and routes to the right specialist.
> **Full doc**: [cytognosis-orchestrator.md](cytognosis-orchestrator.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Task-type router** | Decision tree that classifies a task as building, writing, designing, scaffolding, writing grants, operations, or ambiguous. |
| **One-way door** | A decision that is hard to reverse (license, API contract, schema). Requires slowdown and verification. |
| **Two-way door** | A decision that is easily reversible (formatting, draft copy). Decide fast and iterate. |
| **Revelation Arc** | Cytognosis narrative structure: Mystery → Insight → Resolution. |
| **Context health** | Protocol for managing context window size: checkpoint at 10-15 exchanges, handoff at 50K tokens. |
| **One skill per response** | Never load two Cytognosis SKILL.md files in the same response. |

---

## Task → Skill Router

| Task type | Load |
|-----------|------|
| Building software (scaffold, code, configure, test) | `cytognosis-dev` |
| Writing documentation (any doc type, research, ADHDfy) | `cytognosis-doc` |
| Designing visual output (UI, assets, presentations) | `cytognosis-design-system-master` |
| Scaffolding interface app (phone, web, desktop, extension) | `cytognosis-template-master` |
| Writing grants, proposals, science narratives | `cytognosis-writer` |
| Managing files, workspace, Google Workspace | `cytognosis-org` |
| Deep brand reference (full v10, every shade, all icons) | `cytognosis-branding` |
| Multi-skill or ambiguous task | Stay on this skill; use reasoning protocols |

---

## Keyword → Skill Map (abbreviated)

| Keywords | Skill |
|----------|-------|
| Brand colors, violet/azure/indigo, signature gradient, Inter, tokens.css, glassmorphism, deck design | `cytognosis-design-system-master` |
| Flutter, Tauri, MV3, phone app, web app, desktop app, browser extension, scaffold new product | `cytognosis-template-master` |
| Full v10 spec, every shade, every icon variant, complete accessibility audit | `cytognosis-branding` |
| cytocast, cytoskeleton, nox, ruff, uv, pyproject.toml, steering docs, spec-driven | `cytognosis-dev` |
| Grant, proposal, specific aims, pitch deck, Three Blindspots, founder story | `cytognosis-writer` |
| Drive, calendar, GCP, repo list, @cytognosis.org, document naming, where is | `cytognosis-org` |
| ADR, RFC, spec, runbook, SOP, ADHDfy, evaluation, model comparison, dataset doc, DMP | `cytognosis-doc` |

---

## Common Patterns (Multi-Skill Sequences)

```
# New feature (spec-driven)
dev (requirements + design + tasks) → doc (walkthrough)

# Competitive analysis
doc (research + scoring matrix) → doc (ADHDfy simplified version)

# Grant proposal
writer (narrative) → design-system-master (visuals) → branding (deck template)

# Architecture decision
doc (research) → doc (ADR template)

# New patient app
template-master (phone delta) → dev (cytocast scaffold) → design-system-master (brand)
```

---

## Forbidden Same-Response Pairs

| Pair | Reason |
|------|--------|
| `design-system-master` + `branding` | Context overflow; load sequentially |
| `design-system-master` + `template-master` | Load the one relevant to the task |
| `writer` + `design-system-master` | Sequence: writer for strategy, design-system for visual/voice |
| `dev` + `org` | Independent concerns; separate responses |

---

## Context Health Protocol

| Trigger | Action |
|---------|--------|
| Every 10-15 tool exchanges | CHECKPOINT: synthesize constraints, verify facts |
| Context > 50K tokens | SESSION HANDOFF: write summary artifact, recommend new conversation |
| Hallucinated fact detected | STOP: verify against source files |
| Conflicting instructions | ESCALATE: surface the conflict |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| Routed to `cytognosis-steering` | Skill no longer exists; route to `cytognosis-dev` (§ Steering Documents) |
| Routed to `cytognosis-research` | Skill no longer exists; route to `cytognosis-doc` (§ Research Document Creation) |
| Routed to `cytognosis-adhdfy` | Skill no longer exists; route to `cytognosis-doc` (§ ADHDfy Transformation) |
| Two skills loaded in same response | Stop; unload one; sequence across responses |
| Context degrading (rambling, repeating) | Trigger SESSION HANDOFF; write summary artifact |

---

## See Also

- [Full documentation](cytognosis-orchestrator.md) — comprehensive reference + explanation
- [cytognosis-dev](../cytognosis-dev/cytognosis-dev.md) — building software
- [cytognosis-doc](../cytognosis-doc/cytognosis-doc.md) — all documentation tasks
- [cytognosis-design-system-master](../cytognosis-design-system-master/cytognosis-design-system-master.md) — visual design
- [cytognosis-writer](../cytognosis-writer/cytognosis-writer.md) — grants and proposals
