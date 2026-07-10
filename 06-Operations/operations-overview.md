# Operations (06-Operations) — Layer Overview (Technical)

> **Status:** Active · **Date:** 2026-07-01 · **Author:** Operations consolidation · **Pillar:** Operational (org/business ops)
> **Variants**: Technical (this doc) - Readable (operations-overview.md in Obsidian vault: 06-Operations/) - Agent (operations-overview_prompt.md)
> **Reading time:** ~6 minutes

**If you only read one thing:** `06-Operations` is the canonical home for Cytognosis **org and business operations**: HIPAA and NIH GDS compliance, data-access policy and governance, operational audits, org communications and workspace, and org naming and governance records. The compliance program is **pre-operational** (no PHI ingested), tracking **32 of 38** HIPAA controls complete (see `data-strategy/compliance/HIPAA-STATUS.md`).

## Scope and boundary

| Owner | Scope | Layer |
|---|---|---|
| **Operations** (this layer) | Compliance, audits, communications, data-access policies, org governance | `06-Operations` |
| **Infrastructure** | Technical infra, CI/CD, technical data infrastructure | `04-Engineering/infrastructure` |
| **Cytognosis** | Mission, general org context | `00-Inbox`, `06-Operations/org` (mission context) |

**Tiebreak** when a doc straddles Operations and Infrastructure: if the document's purpose is a **compliance or governance obligation**, it is Operations even when its implementation touches GCP; if the purpose is **running the technical platform**, it is Infrastructure. Straddling items are flagged for Wave 2 (see "Boundary flags").

## Directory map

| Path | Purpose | Docs |
|---|---|---|
| `data-strategy/compliance/` | HIPAA and NIH GDS control SOPs, templates, trackers | 14 |
| `data-strategy/policies/` | Formal data-access and governance policies | 3 |
| `communications/` | Workspace and AI-enablement operational guides | 1 (+ root `COMMUNICATIONS_AND_WORKSPACE.md`) |
| `audits/` | Operational audit index; technical audits point to Infrastructure | pointer `README.md` |
| `org/compliance/` | Org-level HIPAA quick-reference and infra-compliance synthesis | 2 |
| `org/naming/` | Naming conventions and ADRs (boundary: see flags) | 3 |
| `policy-deployment/` | OPA/Cedar policy deployment guide (boundary: see flags) | `README.md` |
| `_archive/` | Superseded originals kept for provenance, badged and forward-linked | 1 |

## Document index (canonical)

### Compliance controls, `data-strategy/compliance/`

| Doc | Role | Status |
|---|---|---|
| `HIPAA-STATUS.md` | Live control tracker, 32/38 done, next review 2026-08-26 | Active |
| `hipaa-compliance-framework.md` | Authoritative HIPAA narrative (Privacy, Security, Breach, HITECH) | Active |
| `phi-security-controls-checklist.md` | Quarterly runnable checklist companion to the framework | Active |
| `deferred-controls.md` | Catalog of deferred HIPAA/NIH controls; CMEK done 2026-06-14, VPC-SC pending | Active |
| `baa-inventory.md` | Signed BAA inventory and vendors-without-BAA list | Active |
| `nih-gds-requirements.md` | NIH GDS 2025 operational requirements for Neuroverse DUCs | Active |
| `incident-response-runbook.md` | HIPAA incident-response SOP, P0 to P3 severity playbooks | Active |
| `member-inference-eval.md` | Membership-inference evaluation SOP before controlled-access model release | Active |
| `audit-log-retention.md` | 7-year audit-log retention SOP (GCS retention lock) | Active, infra-flavored |
| `contingency-plan.md` | HIPAA 164.308(a)(7) disaster-recovery SOP with RTO/RPO | Active, infra-flavored |
| `duc-iam-pattern.md` | Per-DUC GCP IAM provisioning pattern | Active, infra-flavored |
| `confidential-compute-rollout.md` | AMD SEV-SNP Confidential VM rollout SOP | Deferred, infra-flavored |
| `pia-template.md` | Blank Privacy Impact Assessment template | Template |
| `risk-assessment-template.md` | Blank HIPAA risk-assessment template | Template |

### Data policies, `data-strategy/policies/`

| Doc | Role | Status |
|---|---|---|
| `data-governance-policy.md` | Formal governance policy covering all personnel, data, systems, committee | Active |
| `controlled-data-access.md` | Controlled-access dataset acquisition policy, dual-track IRB strategy | Active |
| `nih-nda-access-procedures.md` | NIH NDA eDAR submission procedures (FWA, IRB/IORG, eRA Commons) | Active |

### Communications

| Doc | Role | Status |
|---|---|---|
| `COMMUNICATIONS_AND_WORKSPACE.md` (layer root) | Workspace domain setup, email routing groups, noreply deprecation | Active |
| `communications/workspace-ai-setup.md` | Enabling Gemini Enterprise AI in Workspace Admin | Active |

### Org governance, `org/`

| Doc | Role | Status |
|---|---|---|
| `org/compliance/hipaa-overview.md` | ADHD-friendly HIPAA quick-reference with a GCP architecture diagram | Active (links repaired 2026-07-01) |
| `org/compliance/neuroverse-infrastructure-compliance.md` | NIST 800-66r2 / OCR / NIH GDS / FDA SaMD synthesis for GCP design | Active, route-to-Infra flag |
| `org/naming/naming-resolution.md` | ADR reversing ADR-005 (psych over neuro; CAP to Cytoplex) | Active, route-to-Eng flag |
| `org/naming/domain-vertical-naming.md` | Product naming analysis (Greek/Latin roots, PyPI audit) | Active, route-to-Eng flag |
| `org/naming/extras-naming-conventions.md` | Python package extras naming per PEP 621/735 | Active, route-to-Eng flag |

### Cross-cutting

| Doc | Role | Status |
|---|---|---|
| `gdrive-ops-legal-index.md` (layer root) | Index of legal and financial Drive docs (CEO contract, IRS filings, bank) | Active |
| `audits/README.md` | Audit index; technical audits canonical in Infrastructure | Active |
| `policy-deployment/README.md` | OPA/Cedar policy deployment guide for CAP runtimes | Active, route-to-Eng flag |

## Live status anchors

- **HIPAA program:** pre-operational, no PHI ingested; 32/38 controls complete; CMEK deployed on PHI buckets 2026-06-14; VPC Service Controls still planned.
- **Deferred work:** tracked in `data-strategy/compliance/deferred-controls.md`.

## Boundary flags (deferred to Wave 2 cross-layer dedup)

These docs currently live in `06-Operations` but their purpose is technical or product, not org governance. They are **kept in place** for now; moving them into another agent's layer is a Wave 2 action, not a unilateral Wave 1 edit. See `00-CONSOLIDATION/CONFLICTS.md`.

| Doc | Recommended target | Reason |
|---|---|---|
| `org/compliance/neuroverse-infrastructure-compliance.md` | `04-Engineering/infrastructure` | Technical security-architecture reference |
| `policy-deployment/README.md` | `04-Engineering` | OPA/Cedar deployment for the CAP codebase |
| `org/naming/*` (3) | `04-Engineering/decisions` | Product and architecture naming ADRs |
| `audit-log-retention.md`, `contingency-plan.md`, `duc-iam-pattern.md`, `confidential-compute-rollout.md` | Keep in Operations, cross-link from Infra | Compliance-owned SOPs whose implementation is infra |

## Resolved this consolidation (2026-07-01)

- **GCP audit deduplicated:** the raw `audits/gcp-infrastructure-audit-2026-05-25.md` was archived to `_archive/audits/` with a `SUPERSEDED` badge forward-linking to the annotated canonical copy in `04-Engineering/infrastructure/audits/`.
- **Broken links repaired:** four dead absolute links in `org/compliance/hipaa-overview.md` now use correct relative paths.
- **`data-strategy/` boundary confirmed disjoint:** the Operations compliance/policy set and the Infrastructure technical data-strategy set share no filenames; not a duplication.

## Resume kit

The consolidation state, open questions, next steps, and data manifest live in the Operations project at `~/Claude/Projects/Operations/00-CONSOLIDATION/`.
