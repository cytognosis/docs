# Cytognosis Documentation System

> Last updated: 2026-05-14 | Owner: @shmohammadi

## Template Catalog

All templates live in `design/templates/`. Use them as starting points for every new design doc, decision record, or module specification. Copy the template, fill in the sections, and commit alongside the code it describes.

| # | Template | Filename | When to Use |
|---|----------|----------|-------------|
| 1 | **Architecture Decision Record** | `ADR.md` | Any significant technical choice (library, pattern, schema, API design) |
| 2 | **Module Specification** | `MODULE_SPEC.md` | New module or major refactor of existing module |
| 3 | **Request for Comments** | `RFC.md` | Feature proposals requiring cross-module impact or team input |
| 4 | **Research Evaluation** | `EVALUATION.md` | Technology, library, or API evaluations before adoption |
| 5 | **Troubleshooting Guide** | `TROUBLESHOOTING.md` | Common errors, debugging procedures, environment issues |
| 6 | **Changelog** | `CHANGELOG.md` | Release notes, version history, migration guides |

## Naming Conventions

| Document Type | Naming Pattern | Example |
|---------------|---------------|---------|
| ADR | `ADR-NNN-short-title.md` | `ADR-001-use-linkml-for-schemas.md` |
| Module Spec | `MODULE-module-name.md` | `MODULE-semantic-scholar.md` |
| RFC | `RFC-NNN-short-title.md` | `RFC-001-person-identity-pipeline.md` |
| Evaluation | `EVAL-topic.md` | `EVAL-scholar-access-strategy.md` |
| Troubleshooting | `TROUBLESHOOT-area.md` | `TROUBLESHOOT-google-scholar.md` |

## Folder Structure

```
cytos/design/
├── README.md              ← This file (index)
├── templates/             ← Blank templates
│   ├── ADR.md
│   ├── MODULE_SPEC.md
│   ├── RFC.md
│   ├── EVALUATION.md
│   ├── TROUBLESHOOTING.md
│   └── CHANGELOG.md
├── adrs/                  ← Architecture Decision Records
├── modules/               ← Module specifications
├── rfcs/                  ← Requests for Comments
├── evaluations/           ← Technology evaluations
├── ARCHITECTURE.md        ← System-wide architecture overview
├── ROADMAP.md             ← Project roadmap
├── REQUIREMENTS.md        ← Functional and non-functional requirements
└── CHANGELOG.md           ← Project-level changelog
```

## Principles

1. **Docs-as-code**: All docs in Git, reviewed via PRs, versioned with the code
2. **Living documents**: Update docs when the code changes, not after
3. **Audience-aware**: State who the doc is for (developers, operators, users)
4. **Mermaid diagrams**: Use Mermaid for architecture, flow, and sequence diagrams
5. **Cytognosis voice**: Authoritative, compassionate, optimistic (see brand guidelines)
6. **Metadata header**: Every doc starts with title, date, status, and owner
