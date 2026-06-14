> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, researchers, technical writers
> **Tags**: `documentation`, `cytognosis-doc`, `diataxis`, `reference`

# cytognosis-doc — Technical Documentation Skill

> **Reading time**: ~10 minutes
> **If you only read one thing**: Load this skill for any documentation task. Use the document type matrix to pick the right template. Never write a doc without a template.

---

## What It Is and Why

`cytognosis-doc` is the **authoritative single source of truth** for Cytognosis Foundation documentation standards. It defines 34 document types across 6 lifecycle stages, provides templates for all of them, and includes tooling for ADHD-friendly transformation and research methodology.

The skill exists to prevent documentation being written ad-hoc, inconsistently, or without proper metadata. All documentation at Cytognosis follows docs-as-code principles: Markdown in Git, treated as a first-class part of the PR process.

**When to load this skill**:

- Creating any new document (ADR, RFC, spec, runbook, data card, grant section, README)
- Transforming an existing document to be ADHD-friendly (`cyto doc adhdfy`)
- Conducting research (market analysis, tool evaluation, model comparison)
- Standardizing a document to a template (`cyto doc standardize`)
- Registering a document in the knowledge graph (`cyto doc ingest`)

**When NOT to use this skill**:

- Coding standards and tooling norms live in `cytognosis-dev`
- Visual design and brand tokens live in `cytognosis-design-system-master`
- Grant narrative strategy lives in `cytognosis-writer`

---

## Core Principles

1. **Docs-as-code**: All documentation lives in Git alongside code. Doc updates are part of the PR process. Use Markdown with Mermaid diagrams.
2. **Living documents**: Update docs when code changes, not after. Stale docs are worse than no docs.
3. **Audience-aware**: State the intended reader at the top of each document.
4. **Metadata header required**: Every document starts with a blockquote header (Status / Date / Author / Audience / Tags).
5. **Active voice**: Present tense, active voice. Authoritative but approachable.
6. **Never create without a template**: Every doc type has a template in `references/`.

---

## Document Type Matrix

### Research Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Analyzing a market, competitors, or feature landscape | Market Research | `references/market-research-template.md` |
| Evaluated libraries, APIs, or tools for adoption | Evaluation | `references/evaluation-template.md` |
| Comparing ML/AI models for a specific application | Model Research | `references/model-research-template.md` |
| Defining requirements using EARS notation | Requirements | `references/requirements-template.md` |

### Development Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Made a significant technical choice | ADR | `references/adr-template.md` |
| Building or refactoring a module | Module Spec | `references/module-spec-template.md` |
| Proposing a new feature or change | RFC | `references/rfc-template.md` |
| Producing a comprehensive system overview | System Doc | `references/system-doc-template.md` |
| Inventorying a system's standards usage | Standards Inventory | `references/standards-inventory-template.md` |
| Describing cross-system architecture | Architecture Overview | `references/architecture-overview-template.md` |

### Post-Development Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Recording what changed in a release | Changelog | `references/changelog-template.md` |
| Documenting common errors and fixes | Troubleshooting | `references/troubleshooting-template.md` |
| Authoring an API reference | API Reference | `references/api-reference-template.md` |
| Writing a production deployment guide | Deployment Runbook | `references/deployment-runbook-template.md` |
| Writing an operational SOP | Operational SOP | `references/operational-sop-template.md` |
| Creating a post-implementation demonstration | Walkthrough | `references/walkthrough-template.md` |
| Creating a hands-on learning guide | Tutorial | `references/tutorial-template.md` |

### Cross-Cutting

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Explaining a complex topic for ADHD-friendly readability | ADHD-Friendly Variant | `references/adhd-friendly-template.md` |
| Writing an agent execution plan or prompt | Agent Prompt | `references/agent-prompt-template.md` |
| Tracking task progress with ADHD-friendly done-lists | Action Tracker | `references/action-tracker-template.md` |

### Domain-Specific Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Documenting a curated dataset | Dataset Documentation | `references/dataset-doc-template.md` |
| Writing a data management plan for a grant | DMP | `references/dmp-template.md` |
| Specifying a sensor, assay, or measurement system | Measurement Spec | `references/sensor-spec-template.md` |
| Documenting a protocol implementation | Protocol Implementation | `references/protocol-impl-template.md` |
| Designing platform-level architecture | Platform Design | `references/platform-design-template.md` |
| Writing a grant narrative | Grant / Proposal Section | `references/grant-section-template.md` |

### Publication / Release Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Releasing software publicly | CITATION.cff | `references/citation-cff-template.md` |
| Releasing a public dataset | Croissant Data Card | `references/croissant-data-card-template.md` |
| Releasing a model publicly | HF Model Card | `references/hf-model-card-template.md` |
| Creating or standardizing a repo README | README | `references/readme-template.md` |

### Operational Stage

| Situation | Document Type | Template |
|-----------|--------------|----------|
| Capturing decisions, actions, and parking lot from a meeting | Meeting Notes | `references/meeting-notes-template.md` |
| Running scannable index of all project decisions | Decision Log | `references/decision-log-template.md` |
| Producing a scannable cheat sheet for a tool, API, or system | Quick Reference | `references/quick-reference-template.md` |

---

## Naming Conventions

| Document Type | Pattern | Example |
|---------------|---------|---------|
| ADR | `ADR-NNN-kebab-case-title.md` | `ADR-001-use-linkml-for-schemas.md` |
| Module Spec | `MODULE-module-name.md` | `MODULE-semantic-scholar.md` |
| RFC | `RFC-NNN-kebab-case-title.md` | `RFC-001-person-identity-pipeline.md` |
| Evaluation | `EVAL-kebab-case-topic.md` | `EVAL-scholarly-access-strategy.md` |
| Troubleshooting | `TROUBLESHOOT-area.md` | `TROUBLESHOOT-auth-service.md` |
| System Doc | `SYSTEM-system-name.md` | `SYSTEM-platform.md` |
| Standards Inventory | `STANDARDS-<scope>.md` | `STANDARDS-global.md` |
| Architecture Overview | `ARCHITECTURE-<scope>.md` | `ARCHITECTURE-global.md` |
| API Reference | `API-package.md` | `API-core-client.md` |
| Deployment Runbook | `DEPLOY-<system>.md` | `DEPLOY-api-service.md` |
| Operational SOP | `SOP-<procedure>.md` | `SOP-credential-rotation.md` |
| ADHD-Friendly | `<topic>_adhd.md` | `cap_adhd.md` |
| Agent Prompt | `<topic>_prompt.md` | `phase1_prompt.md` |
| Meeting Notes | `MEETING-YYYY-MM-DD-<kebab-topic>.md` | `MEETING-2026-06-14-design-review.md` |
| Decision Log | `DECISIONS-<project>.md` | `DECISIONS-platform.md` |
| Grant Section | `GRANT-<agency>-<mechanism>-<year>.md` | `GRANT-NIH-R01-2026.md` |
| CITATION.cff | `CITATION.cff` (always at repo root) | `CITATION.cff` |
| HF Model Card | `MODEL-CARD-<model-name>.md` | `MODEL-CARD-mymodel-v1.md` |
| README | `README.md` (always at repo root) | `README.md` |
| Quick Reference | `QUICKREF-<kebab-topic>.md` | `QUICKREF-cyto-doc.md` |

---

## Metadata Header (Required on Every Document)

Every document starts with this block:

```markdown
> **Status**: Draft | Active | Accepted | Deprecated | Superseded
> **Date**: YYYY-MM-DD
> **Author**: @handle
> **Audience**: engineers | stakeholders | operators | reviewers
> **Tags**: `tag1`, `tag2`
```

---

## cyto doc Commands

All commands follow the Command Execution Contract (see the cytoskills repo). Every command supports `--dry-run`, `--prompt-only`, and ends with a validation step.

| Command | Purpose |
|---------|---------|
| `cyto doc adhdfy <path>` | Transform one document to ADHD-friendly format |
| `cyto doc validate --adhd <path>` | Validate an ADHD variant |
| `cyto doc identify <path>` | Auto-classify a document type |
| `cyto doc standardize <path>` | Standardize to the matching template |
| `cyto doc adhdfy-repo <repo>` | Batch transform all docs in a repo |
| `cyto doc ingest <path>` | Register a document in the knowledge graph |

Research commands:

| Command | Purpose |
|---------|---------|
| `cyto research market "<topic>"` | Market/feature landscape research |
| `cyto research tool "<category>"` | Tool/library evaluation |
| `cyto research model "<task>"` | ML model comparison |
| `cyto research arch "<decision>"` | Architecture research |

---

## Research Methodology

All research documents follow the 5-phase workflow:

1. **Scope**: define the research question and evaluation criteria
2. **Search**: gather candidates from primary sources
3. **Score**: apply 0-10 scoring against each criterion
4. **Compare**: build the scoring matrix
5. **Recommend**: state the recommendation with rationale

Full workflow: `references/research-methodology.md`
Scoring matrix examples: `references/research-workflow.md`

---

## ADHDfy Transformation

The `cyto doc adhdfy` command transforms any technical document into a neurodivergent-friendly variant using an 11-step pipeline:

1. Add BLUF (3-sentence summary at top)
2. Add reading time and "if you only read one thing" anchor
3. Break paragraphs to 4 sentences maximum
4. Convert prose lists to bullet points
5. Add GitHub alert boxes (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`)
6. Add "101" sidebars for non-obvious terms
7. Bold key terms on first use
8. Replace walls of text with tables
9. Add Mermaid diagrams for flows
10. Sequence action lists: self-serve first, "needs outreach" last
11. Add done-list (check marks) at top of trackers

Full pipeline: `references/adhdfy-pipeline.md`
Before/after examples: `references/transformation-rules.md`

---

## Multi-Variant Patterns

### Two-Variant Pattern (high-stakes docs)

Critical docs ship in two variants:

1. **Technical** (`<topic>_technical.md`): rigorous, comprehensive, audience = engineers
2. **ADHD-friendly** (`<topic>_adhd.md`): diagrams, alerts, 101 sections; audience = stakeholders

The two variants must agree on content; they differ only in presentation.

### Three-Variant Pattern (hand-off docs)

When handing off to an agent for execution:

1. **Technical** (full reasoning and decisions)
2. **ADHD-friendly** (overview for human stakeholders)
3. **Agent Prompt** (executable plan with paths, commands, success criteria)

---

## Directory Structure

```
design/ (or docs/)
├── README.md              ← Documentation index
├── CITATION.cff           ← Software citation
├── CHANGELOG.md           ← Release history
├── adrs/
├── modules/
├── rfcs/
├── evaluations/
├── meetings/
├── runbooks/
├── sops/
├── system_docs/
├── ARCHITECTURE.md
├── ROADMAP.md
└── REQUIREMENTS.md
```

---

## Hard Rules

- **NEVER create documentation without a template.** Always start from a template in `references/`.
- **NEVER edit an existing ADR.** Supersede it with a new one and add a link.
- **NEVER skip the metadata header.** Every document must have the Status/Date/Author/Audience block.
- **Do not duplicate content** between repo docs and formal specs — link from one to the other.
- Spec and design docs live in the central `docs` repo. User-facing docs stay in source repos.
- ADHD-friendly variants live in the note-taking vault (not git-tracked).

---

## Examples

### Example 1: Creating an ADR

A team needs to document the decision to use LinkML for schemas.

1. Load `cytognosis-doc`.
2. Matrix row: "Made a significant technical choice" → **ADR** → `references/adr-template.md`.
3. Name the file: `ADR-001-use-linkml-for-schemas.md`.
4. Metadata header: Status = Draft, Date = today, Author = @handle, Audience = engineers.
5. Fill in template sections: Context, Decision Drivers, Considered Options, Decision Outcome, Consequences.
6. Commit alongside the code change that implements the decision.

### Example 2: ADHDfy an architecture doc

A comprehensive architecture doc needs to be shared with stakeholders.

1. Load `cytognosis-doc`.
2. Run: `cyto doc adhdfy design/system_docs/SYSTEM-platform.md`
3. The pipeline produces `SYSTEM-platform_adhd.md` in the vault (not git-tracked).
4. Validate: `cyto doc validate --adhd <path>`
5. Share the ADHD variant with stakeholders; the technical variant stays in the repo.

---

## Reference Index

### Core References

| File | Purpose |
|------|---------|
| `references/doc-type-guide.md` | Detailed "when to create" guide for all 34 types |
| `references/command-reference.md` | Full `cyto doc` command specs with all flags |
| `references/command-execution-contract.md` | Cross-agent command contract |
| `references/research-methodology.md` | Complete 5-phase research workflow |
| `references/research-workflow.md` | Populated scoring matrices and examples |
| `references/adhdfy-pipeline.md` | 11-step ADHDfy transformation pipeline |
| `references/transformation-rules.md` | Before/after examples for all 11 steps |
| `references/doc-infrastructure.md` | Three-source architecture (repo/specs/vault) |

### Examples

| File | Purpose |
|------|---------|
| `examples/adr-001-example.md` | Filled-in ADR |
| `examples/eval-scholarly-access-example.md` | Real technology evaluation |
