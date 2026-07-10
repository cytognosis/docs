# Cytognosis Foundation — Organizational Context (Technical)

> **Variants**: Technical (this doc) - Readable (org-context.md in Obsidian vault: 06-Operations/org/) - Agent (org-context_prompt.md)

> **Status:** Active · **Date:** 2026-07-01 · **Author:** Cytognosis (Org) consolidation agent · **Layer:** `06-Operations/org` · **Variants:** `org-context.md` (this) · `org-context.md` · `org-context_prompt.md`

**If you only read one thing:** This is the canonical, deliberately thin org-level context for Cytognosis Foundation: legal identity, mission framing, structure, voice, and openness posture, plus pointers to where domain content actually lives. It is a reference and routing doc, not a pitch or a platform description; the science and platform narrative is owned by the Neuroverse / science pillar, funding by Funding & Grants, and engineering by the product and toolchain pillars.

---

## 1. Legal identity

| Field | Value | Notes |
|---|---|---|
| Legal name | Cytognosis Foundation | |
| Tax status | 501(c)(3) nonprofit | |
| Incorporation | Delaware | |
| EIN | 39-4383634 | |
| Mailing address | 394 Innisfree Dr, Daly City, CA 94015 | Founder residence |
| HQ / registered | Listed as South San Francisco, CA in strategy docs | **Reconcile on official filings** |
| Founder and CEO | Shahin Mohammadi | 20 years computational biology; MIT, Broad, insitro, GenBio AI |

**Address invariant:** filings and external documents must match the address on the **IRS determination letter**. The mailing address and the strategy-doc HQ differ; treat the determination letter as authoritative wherever an address is required, and reconcile the two before any official use. This is tracked in `../../00-CONSOLIDATION/OPEN_QUESTIONS.md` (via the project resume kit).

**Commercial pathway:** a Public Benefit Corporation (PBC) subsidiary is **not yet formed**; formation is pending the Gate 1 / YC S26 outcome. Do not describe a PBC as existing. See the `openness` skill for the nonprofit-to-PBC commercial pathway and dual-licensing strategy.

## 2. Mission framing (voice-bound)

Cytognosis builds AI-native biomedical technology to **detect and intercept** disease **years before symptoms**. Framing rules are mandatory in all output and are enforced by the brand voice:

- Use **detect and intercept**, not "diagnose and treat".
- Use **years before symptoms**, not "early detection".
- Use **AI-native**, not "algorithm-based".
- Use **healthcare** (one word); use person-first language.
- **Forbidden words:** "revolutionary", "cure", "game-changing", "breakthrough".
- **Tone:** authoritative, compassionate, optimistic; never fear-based.

The full brand system (colors, typography, logos, messaging architecture) is owned by the `brand-identity` skill and the Branding pillar (`07-Design`). This doc carries only the org-level voice invariants.

## 3. Structure: six pillars, three overlays

Cytognosis organizes as **value-streams by lifecycle**: six pillars plus three cross-cutting overlays. This doc does not duplicate the mapping; the authoritative table (pillar, identity, repos, docs layers) lives in the blueprint and the registry.

| Element | Members | Source of truth |
|---|---|---|
| Pillars | Cytoverse, Cytonome, Cytoscope, Toolchain, Operational, Research | `Refactor/00-CONSOLIDATION/SHARED-BLUEPRINT.md` Section 2 |
| Overlays | Funding & Partnerships, People, Personal/Legal Ops | same |
| Project to folder to pillar to repo mapping | all keeper and pillar projects | `Refactor/00-CONSOLIDATION/PROJECT-REGISTRY.md` |
| Docs authoring taxonomy (8 layers) | `00-Inbox` through `07-Design` plus `_templates` | `SHARED-BLUEPRINT.md` Section 2a |

## 4. Canonical homes (no duplication)

Every artifact has exactly one canonical home. The org project is the **working area** for cross-org context only; finalized engineering docs do not live here.

| Home | Path | Canonical for |
|---|---|---|
| cytomem | `~/repos/cytognosis/cytomem` (Neo4j + Graphiti) | Cross-repo index, provenance, dedup oracle |
| docs repo | `~/repos/cytognosis/docs` | Engineering and platform docs (incl. this doc, under `06-Operations/org`) |
| Obsidian vault | `~/Documents/ObsidianVault` | Personal, ADHD-variant readable docs |
| Claude Projects | `~/Claude/Projects/<project>` | Working drafts, strategy, per-project sets |
| Data Hub | `gs://cytognosis-data-hub` (via DVC) | Datasets, large or versioned assets, pipeline outputs |

## 5. Openness posture

Defaults are **Apache 2.0** for code and **CC BY 4.0** for docs and data, with **FAIR** data principles. Licensing choices, controlled-access exceptions, model and data cards, and the nonprofit-to-PBC pathway are owned by the `openness` skill; consult it before choosing a license or writing open-science grant language.

## 6. Scope boundary for this project (what belongs here)

**Belongs here:** cross-org mission and identity, org-level operating context, and `org/` operations that do not fit a more specific pillar.

**Does not belong here (route to owner):**

| Content | Owner |
|---|---|
| Product framing, specs, features | Cytonome (Yar) / Cytoverse (Cytos) pillars, `03-Products` / `04-Engineering` |
| Funding, grants, IGoR, partner dossiers | Funding & Grants overlay, `02-Funding` |
| Research corpus, papers, science foundation | Research / Neuroverse pillars, `05-Research` |
| Technical infrastructure, CI/CD, DNS, GCP | Infrastructure (Operational), `04-Engineering/infrastructure` |
| Brand, website, design system | Branding (Operational), `07-Design` |
| Compliance, audits, org communications | Operations, `06-Operations` (this project owns only the `org/` sub-slice) |

## 7. Source-of-truth pointers

| Need | File / skill |
|---|---|
| Program rules every agent follows | `Refactor/00-CONSOLIDATION/SHARED-BLUEPRINT.md` |
| Project to folder to pillar mapping | `Refactor/00-CONSOLIDATION/PROJECT-REGISTRY.md` |
| Current consolidation plan and phase status | `Refactor/00-CONSOLIDATION/MASTER-CONSOLIDATION-PLAN.md` |
| Science and platform narrative | `science-platform` skill |
| Brand, voice, design system | `brand-identity` skill, `07-Design` |
| Openness and licensing | `openness` skill |
| This project's state and open items | `~/Claude/Projects/Cytognosis/00-CONSOLIDATION/` |