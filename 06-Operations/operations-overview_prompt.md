# Operations (06-Operations) — Fresh-Agent Brief

> **Variants**: Agent seed (this doc) - Technical (operations-overview.md) - Readable (operations-overview.md in Obsidian vault: 06-Operations/)

> **Status:** Active · **Date:** 2026-07-01 · Self-contained brief for an agent picking up this layer cold.
> Companions: [technical](operations-overview.md) · [readable](operations-overview.md)

## Goal

Keep `06-Operations` the single canonical home for Cytognosis org and business operations (compliance, data policy, audits, communications, org governance), with one home per artifact and no dangling cross-references.

## Scope (and what is out)

- **In:** HIPAA and NIH GDS compliance SOPs and templates, data-access and governance policies, operational audits index, workspace and comms guides, org naming and governance records.
- **Out:** technical infrastructure and CI/CD (that is `04-Engineering/infrastructure`, the Infrastructure agent); mission and general org context (that is the Cytognosis project).

## Decided and done (2026-07-01)

- Operations stays a **standalone** project; content is thick enough (27 canonical docs), not merged into Cytognosis.
- Archived the stale raw `gcp-infrastructure-audit-2026-05-25.md` to `_archive/audits/` with a `SUPERSEDED` badge; canonical is the annotated copy in `04-Engineering/infrastructure/audits/`.
- Repaired four broken absolute links in `org/compliance/hipaa-overview.md`.
- Confirmed `06-Operations/data-strategy/` and `04-Engineering/infrastructure/data-strategy/` are disjoint (no duplication).
- Authored this three-variant overview and the layer `README.md`.

## Open questions (recommendations in the project OPEN_QUESTIONS.md)

1. Route four boundary docs to their true owners in Wave 2: `org/compliance/neuroverse-infrastructure-compliance.md` and `policy-deployment/README.md` to Infrastructure/Engineering; the three `org/naming/*` ADRs to `04-Engineering/decisions`. Kept in place until Wave 2 (cross-layer moves are not a Wave 1 action).
2. Disposition of the legacy `~/repos/cytognosis/org` repo (a 227 MB grab-bag; content mostly superseded or owned by other pillars). Recommendation: archive or split by pillar in Wave 2; do not bulk-import into `06-Operations`.

## Prioritized pending tasks

1. Wave 2: execute the four boundary routings above once Infrastructure and Engineering agents confirm.
2. Full cross-reference audit across the 14 compliance SOPs (only `hipaa-overview.md` has been link-checked so far).
3. Decide the `org` repo disposition with the owner.

## Source-of-truth files

- Live compliance status: `data-strategy/compliance/HIPAA-STATUS.md`.
- Authoritative HIPAA narrative: `data-strategy/compliance/hipaa-compliance-framework.md`.
- Governance policy: `data-strategy/policies/data-governance-policy.md`.
- Consolidation state and manifests: `~/Claude/Projects/Operations/00-CONSOLIDATION/` (`STATE.md`, `OPEN_QUESTIONS.md`, `NEXT_STEPS.md`, `CLASSIFICATION.tsv`, `DATA-MANIFEST.md`, `CONFLICTS.md`).

## Start commands

```bash
# See the layer
ls -R ~/repos/cytognosis/docs/06-Operations
# Current branch (consolidation work)
git -C ~/repos/cytognosis/docs branch --show-current   # reorg/operations-2026-07-01
# Live compliance status
sed -n '1,40p' ~/repos/cytognosis/docs/06-Operations/data-strategy/compliance/HIPAA-STATUS.md
```

## Success criteria

Every doc has one home; cross-references resolve; boundary items are flagged not misfiled; the layer `README.md` and this brief let a fresh agent orient in 5 minutes, find current work in 10, and act in 15.