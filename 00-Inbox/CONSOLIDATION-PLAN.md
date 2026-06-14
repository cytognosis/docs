---
title: "Yar/Cytonome Doc Consolidation Plan"
date: 2026-06-14
author: Shahin Mohammadi
status: draft
---

> **Status**: Draft | **Date**: 2026-06-14 | **Author**: Shahin Mohammadi | **Audience**: Internal | **Tags**: meta, consolidation, yar, cytoplex, docs

# Yar/Cytonome Doc Consolidation Plan

**Reading time**: ~5 min. **If you read one thing**: Section 3 (Redundancy Clusters) and Section 5 (Target Canonical Set).

---

## 1. Total Doc Inventory

**Total tracked files**: 444

| Layer | Count | Notes |
|-------|-------|-------|
| `00-Inbox` | 5 | Needs triage |
| `01-Strategy` | 10 | Clean |
| `02-Funding` | 16 | Clean |
| `03-Products` | 86 | Yar: 46, Cytoplex: 29, other: 11 |
| `04-Engineering` | 250 | yar: 37, cytoplex: 25, cytos: 78, other: 110 |
| `05-Research` | 5 | Clean |
| `06-Operations` | 27 | Clean |
| `07-Design` | 3 | Clean |
| `_templates` | 2 | Clean |

The problem is concentrated in **03-Products/Cytonome/** and **04-Engineering/yar/cytoplex/**. Together they hold 162 files (36% of total), with significant overlap.

---

## 2. How Redundancy Happened

Three sources fed into the repo in separate passes:

1. **Yar repo** (`~/repos/cytognosis/Yar`) had research files under `docs/research/`
2. **Claude Projects** had a second copy of many of the same research evaluations, named with the EVAL-topic.md convention
3. **Drafts folder** had additional versions of CAP/Cytoplex architecture docs

Result: most Yar research evaluations appear in **both** `03-Products/Cytonome/Yar/research/` (EVAL-naming) and `04-Engineering/yar/research/` (original-naming). The taxonomy says research evals belong in `04-Engineering`. The `03-Products` copies are misplaced.

---

## 3. Redundancy Clusters (Priority Order)

### Cluster A: EVAL files in wrong layer (HIGH, ~15 files to delete)

15 tool/service evaluations live in `03-Products/Cytonome/Yar/research/` but have near-identical counterparts in `04-Engineering/yar/research/`.

| `03-Products` (to delete) | `04-Engineering` (canonical) |
|--------------------------|------------------------------|
| `EVAL-bio-model-zoos.md` | `bio-model-zoos-research.md` |
| `EVAL-blue-lin-projects.md` | `blue-lin-projects-deep-dive.md` |
| `EVAL-capacities.md` | `capacities-deep-dive.md` |
| `EVAL-elevenlabs.md` | `elevenlabs_evaluation.md` |
| `EVAL-lamindb.md` | `lamindb-deep-analysis.md` |
| `EVAL-leantime-vs-super-productivity.md` | `feature_comparison_leantime_vs_sp.md` |
| `EVAL-letterly.md` | `letterly-deep-dive.md` |
| `EVAL-omi-ai.md` | `omi-ai-deep-dive.md` |
| `EVAL-tana.md` | `tana-outliner-deep-dive.md` |
| `EVAL-tiledb.md` | `tiledb-cloud-analysis.md` |
| `EVAL-voice-models.md` | `voice_model_deep_evaluation.md` |
| `adhd-paper-synthesis.md` | `adhd-paper-synthesis.md` |
| `cap-yar-comprehensive-reference.md` | `cap_yar_comprehensive_reference.md` |
| `codebase-analysis.md` | `codebase-analysis.md` |
| `solid-pods-comprehensive.md` | `solid-pods-comprehensive.md` |

**Action**: Rename `04-Engineering` versions to EVAL-topic.md convention, then `git rm` all 15 from `03-Products`.

### Cluster B: Yar feature/requirements proliferation (HIGH, 3-4 files to consolidate)

8 overlapping docs all describe Yar's features/requirements:

| File | Content | Action |
|------|---------|--------|
| `yar-product-feature-master.md` | Full PRD-style feature list | **Merge into canonical PRD** |
| `yar-master-features-requirements.md` | Requirements format | **Merge into canonical PRD** |
| `cytonome-master-reference.md` | Master reference | **Merge into canonical PRD** |
| `feature-comparison.md` | Competitive comparison intro | Archive or merge into comparison |
| `yar-product-implementation.md` | Implementation guide | **Keep as-is** |
| `yar-feature-prioritization.csv` | Prioritization matrix | **Keep as-is** |
| `research/yar-unified-feature-comparison.md` | v1 comparison | Delete, superseded by v3 |
| `research/yar-unified-feature-comparison-v3.md` | v3 comparison | **Keep as canonical comparison** |
| `04-Engineering/yar/research/yar-unified-feature-comparison.md` | v1 duplicate | Delete |
| `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md` | v3 duplicate | Delete (03-Products version is canonical) |
| `04-Engineering/yar/research/yar-unified-feature-comparison-adhd.md` | ADHD variant | Merge into v3 or delete |

**Target**: 3 canonical docs (see Section 5).

### Cluster C: Cytoplex README/overview proliferation (MEDIUM, 4 files to delete)

6 files all describe what Cytoplex/CAP is:

| File | Keep? | Action |
|------|-------|--------|
| `03-Products/Cytoplex/cytoplex-readme.md` | Yes | **Canonical product overview** |
| `03-Products/Cytoplex/README.md` | No | Redundant with cytoplex-readme; delete |
| `03-Products/Cytoplex/overview.md` | No | Redundant; delete |
| `03-Products/Cytoplex/cap-readme.md` | Yes | **Canonical CAP protocol intro** |
| `03-Products/Cytoplex/cap-comprehensive.md` | No | Duplicate of `04-Engineering/cytoplex/research/cap-comprehensive.md`; delete from 03-Products |
| `03-Products/Cytoplex/cap-protocol-assessment.md` | No | Duplicate of `04-Engineering/cytoplex/research/cap-protocol-assessment.md`; delete from 03-Products |

### Cluster D: Supervisor reports (LOW, 1 file to archive)

| File | Lines | Action |
|------|-------|--------|
| `04-Engineering/cytoplex/reports/cap-v0.1-supervisor-report-full.md` | 429 | **Keep as canonical** |
| `04-Engineering/cytoplex/reports/cap-v0.1-supervisor-report.md` | shorter | Archive (move to `reports/archive/`) |

### Cluster E: 00-Inbox triage (LOW, 5 files to move)

| File | Target |
|------|--------|
| `00-Inbox/analysis/infra-scaling-analysis.md` | `04-Engineering/architecture/` |
| `00-Inbox/architecture-index.md` | `04-Engineering/architecture/` |
| `00-Inbox/product-implementation.md` | Review: may duplicate `03-Products/Cytonome/Yar/yar-product-implementation.md` |
| `00-Inbox/refactor-overview.md` | `04-Engineering/yar/refactor/` |
| `00-Inbox/yar_revision_plan.md` | `04-Engineering/yar/` |

---

## 4. Consolidation Math

| Action | Files removed | Files created | Net |
|--------|--------------|--------------|-----|
| Cluster A: delete 03-Products EVAL duplicates | -15 | 0 | -15 |
| Cluster B: merge Yar feature docs into PRD | -4 | +1 (yar-product-spec.md) | -3 |
| Cluster B: remove duplicate feature comparisons | -3 | 0 | -3 |
| Cluster C: Cytoplex README cleanup | -4 | 0 | -4 |
| Cluster D: archive short supervisor report | -1 | 0 | -1 |
| Cluster E: triage Inbox | -0 | 0 | 0 (moves only) |
| Rename 04-Engineering EVALs to EVAL-naming | 0 | 0 | 0 (renames only) |
| **Total** | **-27** | **+1** | **-26** |

Post-consolidation target: **~418 files**, with no redundancy in Yar/Cytoplex area.

---

## 5. Canonical Output Set (Target State)

### Yar (03-Products/Cytonome/Yar/)

| Canonical file | Status | Source |
|---------------|--------|--------|
| `yar-product-spec.md` | **To create** | Merge of feature-master + master-features-requirements + cytonome-master-reference |
| `yar-product-implementation.md` | Exists, keep | As-is |
| `yar-feature-prioritization.csv` | Exists, keep | As-is |
| `sensor-architecture.md` | Exists, keep | As-is |
| `sensor-ecosystem.md` | Exists, keep | As-is |
| `steering/yar-product.md` | Exists, keep | As-is |
| `steering/yar-tech.md` | Exists, keep | As-is |
| `steering/yar-structure.md` | Exists, keep | As-is |

### Yar Research (04-Engineering/yar/research/)

| Canonical file | Status | Notes |
|---------------|--------|-------|
| `EVAL-adhd-task-management-paper.md` | Exists | New full synthesis; `adhd-paper-synthesis.md` can be archived |
| `EVAL-{tool}.md` (11 files) | Rename needed | Standardize all to EVAL-topic.md convention |
| `yar-unified-feature-comparison-v3.md` | Keep v3 only | Delete v1 and adhd-variant |
| `yar-substrate-decision.md` | Keep | Architecture decision record |

### Cytoplex (03-Products/Cytonome/Cytoplex/)

| Canonical file | Status | Notes |
|---------------|--------|-------|
| `cytoplex-readme.md` | Keep | Product overview |
| `cap-readme.md` | Keep | Protocol intro |
| `spec/` (11 files) | Keep as-is | Structured spec chapters |
| `steering/` (3 files) | Keep as-is | Agent context |

### Cytoplex Engineering (04-Engineering/cytoplex/)

| Canonical file | Status | Notes |
|---------------|--------|-------|
| `cap-system-doc.md` | Keep | Technical reference |
| `api.md`, `development.md`, `testing.md` | Keep | Dev docs |
| `reports/cap-v0.1-supervisor-report-full.md` | Keep | Full report is canonical |
| `research/cap-comprehensive.md` | Keep | Detailed protocol analysis |
| `research/cap-protocol-assessment.md` | Keep | Assessment |
| `security/`, `compliance/`, `quality/`, `interop/` | Keep | Structured subdirs |

---

## 6. Standardized Doc Templates Per Type

These are the canonical formats all future docs in this area should follow:

| Doc type | Template | Required sections |
|----------|----------|-------------------|
| **Product spec (PRD)** | `_templates/product-spec.md` | Overview, users, features (by category), non-goals, open questions |
| **Architecture doc** | `_templates/architecture.md` | System context, components, data flows, decisions, open issues |
| **EVAL file** | `EVAL-{tool}.md` | BLUF, what it is, fit for Yar, verdict (adopt/watch/skip), links |
| **Feature comparison** | `yar-unified-feature-comparison-v3.md` pattern | Feature matrix, scoring rubric, synthesis |
| **Steering file** | `.agents/steering/` pattern | Already standardized |
| **Protocol spec** | Cytoplex `spec/` pattern | Numbered chapters, references, changelog |

---

## 7. Execution Order (Next Steps)

1. **Step 1 (automated, ~1 session)**: Rename 04-Engineering EVALs to EVAL-naming; delete 15 from 03-Products/Yar/research. No content changes, just `git mv` and `git rm`.

2. **Step 2 (content synthesis, ~2 sessions)**: Create `yar-product-spec.md` by merging feature-master + master-features-requirements + cytonome-master-reference into one canonical PRD-format doc.

3. **Step 3 (cleanup, ~1 session)**: Cytoplex README consolidation, supervisor report archive, Inbox triage.

4. **Step 4 (optional, future)**: Expand metadata headers to remaining ~350 docs outside Yar/Cytoplex area (04-Engineering/cytos has 78 files; 06-Operations has 27; most lack cytognosis-doc headers).

---

## 8. What NOT to Consolidate

- `04-Engineering/cytoplex/spec/` (11 files): structured spec chapters, keep as individual files by chapter
- `04-Engineering/yar/sensors/` (8 files): each is distinct implementation content
- `04-Engineering/yar/refactor/` (4 files): checklist, plan, verification, open-questions are distinct artifacts
- `03-Products/Cytonome/Yar/mvp/` (14 files): numbered session context; consolidation would lose traceability
- `04-Engineering/yar/reports/` (3 files): timestamped audit reports; should not merge
