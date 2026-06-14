> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, researchers, technical writers
> **Tags**: `quick-reference`, `cytognosis-doc`

# cytognosis-doc — Quick Reference

> **One line**: Load this skill for any documentation task; it owns all 34 doc types, templates, research methodology, and the ADHDfy transformation pipeline.
> **Full doc**: [cytognosis-doc.md](cytognosis-doc.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Diataxis** | Documentation framework dividing content into tutorials, how-to guides, reference, and explanation. This skill covers reference and explanation doc types. |
| **ADHDfy** | 11-step transformation that converts a technical doc into a neurodivergent-friendly variant with BLUF, alerts, 101 sidebars, and bullet structure. |
| **EARS notation** | Requirements syntax: WHEN/WHILE/IF/THE SYSTEM SHALL patterns that eliminate ambiguity. |
| **Metadata header** | Required blockquote at the top of every doc: Status, Date, Author, Audience, Tags. |
| **Two-variant pattern** | High-stakes docs ship in a technical version (`_technical.md`) and an ADHD-friendly version (`_adhd.md`). |
| **Docs-as-code** | All docs live in Git, treated as part of the PR process, written in Markdown with Mermaid. |

---

## Document Type by Stage

| Stage | Doc Type | Template |
|-------|----------|----------|
| Research | Market Research | `references/market-research-template.md` |
| Research | Evaluation | `references/evaluation-template.md` |
| Research | Model Research | `references/model-research-template.md` |
| Research | Requirements | `references/requirements-template.md` |
| Development | ADR | `references/adr-template.md` |
| Development | Module Spec | `references/module-spec-template.md` |
| Development | RFC | `references/rfc-template.md` |
| Development | System Doc | `references/system-doc-template.md` |
| Development | Standards Inventory | `references/standards-inventory-template.md` |
| Development | Architecture Overview | `references/architecture-overview-template.md` |
| Post-Dev | Changelog | `references/changelog-template.md` |
| Post-Dev | Troubleshooting | `references/troubleshooting-template.md` |
| Post-Dev | API Reference | `references/api-reference-template.md` |
| Post-Dev | Deployment Runbook | `references/deployment-runbook-template.md` |
| Post-Dev | Operational SOP | `references/operational-sop-template.md` |
| Post-Dev | Walkthrough | `references/walkthrough-template.md` |
| Post-Dev | Tutorial | `references/tutorial-template.md` |
| Cross-cutting | ADHD-Friendly Variant | `references/adhd-friendly-template.md` |
| Cross-cutting | Agent Prompt | `references/agent-prompt-template.md` |
| Cross-cutting | Action Tracker | `references/action-tracker-template.md` |
| Domain | Dataset Doc | `references/dataset-doc-template.md` |
| Domain | DMP | `references/dmp-template.md` |
| Domain | Measurement Spec | `references/sensor-spec-template.md` |
| Domain | Protocol Implementation | `references/protocol-impl-template.md` |
| Domain | Platform Design | `references/platform-design-template.md` |
| Domain | Grant / Proposal Section | `references/grant-section-template.md` |
| Publication | CITATION.cff | `references/citation-cff-template.md` |
| Publication | Croissant Data Card | `references/croissant-data-card-template.md` |
| Publication | HF Model Card | `references/hf-model-card-template.md` |
| Publication | README | `references/readme-template.md` |
| Operational | Meeting Notes | `references/meeting-notes-template.md` |
| Operational | Decision Log | `references/decision-log-template.md` |
| Operational | Quick Reference | `references/quick-reference-template.md` |

---

## Commands

| Command | What It Does |
|---------|-------------|
| `cyto doc adhdfy <path>` | Transform one document to ADHD-friendly format |
| `cyto doc validate --adhd <path>` | Validate an ADHD variant |
| `cyto doc identify <path>` | Auto-classify a document type |
| `cyto doc standardize <path>` | Standardize to matching template |
| `cyto doc adhdfy-repo <repo>` | Batch transform all docs in a repo |
| `cyto doc ingest <path>` | Register in knowledge graph |
| `cyto research market "<topic>"` | Market/feature landscape research |
| `cyto research tool "<category>"` | Tool/library evaluation |
| `cyto research model "<task>"` | ML model comparison |
| `cyto research arch "<decision>"` | Architecture research |

---

## Options / Parameters

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--dry-run` | `bool` | `false` | Preview what would be changed without writing files. |
| `--prompt-only` | `bool` | `false` | Return the transformation prompt without executing it. |
| `--adhd` | `bool` | `false` | Target ADHD variant for validate command. |

---

## Common Patterns

```bash
# Transform a doc to ADHD-friendly variant (dry run first)
cyto doc adhdfy design/system_docs/SYSTEM-platform.md --dry-run
cyto doc adhdfy design/system_docs/SYSTEM-platform.md

# Classify an unknown document
cyto doc identify path/to/unknown-doc.md

# Standardize a doc to its template
cyto doc standardize path/to/existing-doc.md

# Register a new doc in the knowledge graph
cyto doc ingest docs/adrs/ADR-001-use-linkml-for-schemas.md

# Run technology evaluation research
cyto research tool "vector database"
```

---

## Naming Conventions (Most Common)

| Type | Pattern | Example |
|------|---------|---------|
| ADR | `ADR-NNN-kebab-title.md` | `ADR-001-use-linkml.md` |
| RFC | `RFC-NNN-kebab-title.md` | `RFC-001-identity-pipeline.md` |
| Module Spec | `MODULE-name.md` | `MODULE-semantic-scholar.md` |
| Evaluation | `EVAL-topic.md` | `EVAL-scholarly-access.md` |
| Meeting Notes | `MEETING-YYYY-MM-DD-topic.md` | `MEETING-2026-06-14-review.md` |
| Quick Reference | `QUICKREF-topic.md` | `QUICKREF-cyto-doc.md` |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| `cyto doc adhdfy` produces no output | Check `--dry-run` flag was removed; verify path exists |
| Metadata header missing on validate | Add the required blockquote block (Status/Date/Author/Audience/Tags) |
| ADR edit rejected | Do not edit existing ADRs; create a new ADR that supersedes the old one and link it |
| Wrong template used | Run `cyto doc identify <path>` to auto-classify, then check the matrix for the correct template |

---

## See Also

- [Full documentation](cytognosis-doc.md) — comprehensive reference + explanation
- `doc-type-guide.md` — detailed "when to create" for all 34 types (see cytoskills repo)
- `command-reference.md` — full command specs with all flags (see cytoskills repo)
- `adhdfy-pipeline.md` — 11-step transformation pipeline (see cytoskills repo)
- [cytognosis-dev](../cytognosis-dev/cytognosis-dev.md) — coding standards (not documentation)
- [cytognosis-writer](../cytognosis-writer/cytognosis-writer.md) — grant narrative strategy
