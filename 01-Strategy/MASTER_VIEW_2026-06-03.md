# Cytognosis Master View

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 · The consolidation program's capstone: per-track top priorities, one unified timeline, the cross-track spine, and links to every canonical track doc. Built on the cytomem corpus (10,006 artifacts / 27 sources) and the frozen taxonomy. Reading time ~8 min.

## BLUF

The full consolidation program is complete: the archive is audited and ingested, the taxonomy is frozen, and all six tracks are consolidated into full and ADHD docs. The near-term picture is dominated by a funding sprint stacked against the Oct 1 runway cliff, with three external deadlines in the next six weeks (AWS Jun 5, IGoR Jun 25, NSF Jul 13). The single most leveraged move this week is messaging Patty, because she gates both the Duane contract path and the Jordan/HSF path.

## Program status (done)

- ✅ **Stage 0–1:** Archive audit and selective ingest closed; corpus at 10,006 artifacts / 27 sources; nothing deleted
- ✅ **Stage 4:** Taxonomy frozen (6 pillars + 3 overlays), value-streams × lifecycle grid, canonical-home rule
- ✅ **Stage 5:** All six tracks consolidated (full + ADHD): Funding/IGoR, People, Cytoverse, Cytonome, Cytoscope, Toolchain/Operational
- ✅ **Stage 6:** This master view

## Per-track top priorities

| Track | #1 priority | #2 | #3 |
|---|---|---|---|
| **Funding / IGoR** | Restructure IGoR Summary to IPAI-prime / Cytognosis-sub; submit Jun 25 | Close survival tier (~$615K, drafted, no outreach) before Oct 1 | Activate NSF X-Labs Phase 0 with Hervé before Jul 13 |
| **People** | Message Patty today (gates Duane + Jordan) | Get Ananth's answer Jun 4 on which IPAI grant funds ~50% effort | Send NSF citizenship query this week |
| **Cytoverse** | Submit the bipolar paper (McLean + MtSinai OOD) | Run stratified-LDSC (cheapest de-risk) | Load biomolecular entities as first-class KG nodes |
| **Cytonome** | Ship Yar TestFlight beta (243 tests pass, zero users) | Submit YC Summer 2026 (needs 60s demo video) | Yar entity + IP license with Duane (gated on YC) |
| **Cytoscope** | Resolve citizenship + designate PI of record before Jun 30 | Finalize and submit Phase 0 (Jul 13) | Build Psychoverse coordinate model now (no blockers) |
| **Toolchain / Operational** | Graph hygiene + Graphiti embedding fix | Phase 0 infra execution (7 tasks) | Registry convergence + missing asset types |

## Unified timeline

| Date | Milestone | Track |
|---|---|---|
| Jun 4 | Ananth answer: which IPAI grant funds ~50% effort | People / Funding |
| **Jun 5** | AWS Imagine Round 1 | Funding |
| **Jun 9** | IGoR Proposer Day | Funding |
| Jun 20 | Confirm Hervé citizenship eligibility (written) | Cytoscope |
| **Jun 25** | IGoR Solution Summary due, 12:00 PM ET | Funding |
| Jun 30 | NSF PI-of-record designation | Cytoscope |
| **Jul 13** | NSF X-Labs Phase 0 due, 5:00 PM ET | Cytoscope / Funding |
| Aug 6 | IGoR full proposal (internally documented; verify on SAM.gov) | Funding |
| **Oct 1** | Runway cliff | Funding / People |
| Oct 6 | NIH TMM RFA-DA-27-004 R01 | Funding |
| 2027 | NIH / HSF / One Mind | Funding |

## Cross-track spine (interconnections)

- **Cellular micro-to-meso causal bridge** is the keystone thesis. It feeds **IGoR TA1** (mechanistic heterogeneity, not symptom clustering), **HSF/EVIDENT** (predict neuroplastogen response from molecular biotype), and the **Cytoscope** biotype layer (the theory of what the sensor reads). It is the differentiator vs HSF, which is genomic+connectomic only.
- **Cytoscope** is funded by **NSF X-Labs** and commercializes **through the Cytonome/Yar PBC arm** (soft sensors → MH sensors → wearable).
- **Toolchain LinkML schemas/standards** provide the ontology grounding that **IGoR TA1** requires for phenotype standardization.
- **Funding splits by horizon:** bridge/small grants = survival to Oct 1; IGoR/HSF/NIH = 2027 money.
- The **factorized PRS** is confidential platform IP across all tracks: kept off the bipolar paper and out of external text.

## Canonical track docs

| Track | Full | ADHD |
|---|---|---|
| Funding / IGoR | `tracks/FUNDING_IGOR_TRACK_2026-06-03.md` | `tracks/FUNDING_IGOR_TRACK_ADHD_2026-06-03.md` |
| People | `tracks/PEOPLE_TRACK_2026-06-03.md` | `tracks/PEOPLE_TRACK_ADHD_2026-06-03.md` |
| Cytoverse | `tracks/CYTOVERSE_TRACK_2026-06-03.md` | `tracks/CYTOVERSE_TRACK_ADHD_2026-06-03.md` |
| Cytonome | `tracks/CYTONOME_TRACK_2026-06-03.md` | `tracks/CYTONOME_TRACK_ADHD_2026-06-03.md` |
| Cytoscope | `tracks/CYTOSCOPE_TRACK_2026-06-03.md` | `tracks/CYTOSCOPE_TRACK_ADHD_2026-06-03.md` |
| Toolchain / Operational | `tracks/TOOLCHAIN_OPERATIONAL_TRACK_2026-06-03.md` | `tracks/TOOLCHAIN_OPERATIONAL_TRACK_ADHD_2026-06-03.md` |

Supporting: `MASTER_PLAN_AND_CONSOLIDATION_PROGRAM_2026-06-03.md`, `STAGE4_META_STRATEGY_TAXONOMY_2026-06-03.md`, `STAGE1_ARCHIVE_TRIAGE_2026-06-03.md`.

## Canonical-home reconciliation rollup

Duplicates surfaced across tracks; canonical assignments (others kept indexed, not edited):

| Cluster | Canonical home |
|---|---|
| Helix org strategy, 15-Year Roadmap | `cowork-strategic-planning/master_plan/` |
| `22_people_and_consultants.md` | `X-Labs/01-strategy/master-plan-v2.0/` |
| `B_patty_meeting_synthesis.md` | `master-plan-v2.0/appendix/` |
| `01_plan_prose.md` and platform plans | `docs/cytoverse/cytos/` |
| YC applications | `X-Labs/02-applications/yc/` |
| Cytoplex implementation alignment | `docs/cytonome/yar/cytoplex/v1-baseline/` |
| Sensor docs (`13_sensor_ecosystem`, `sensors.md`) | `docs` / `master-plan-v2.0` |
| Infra docs (DNS, hosting, gcp-setup, deployment, sssom, scholarly-kg) | `docs` repo |
| Branding templates `08` vs `10` | Compare content before merge |

## Remaining follow-ups (not yet done)

1. **Graph hygiene:** the repo scanner does not read a per-repo `exclude` key, so removing `.dvc/tmp`, `.github`, and lockfile noise needs a small `scanner.py` change plus re-ingest. Tracked separately (see `task-65fec913` Graphiti embedding fix).
2. **Formalize canonical-home moves:** the reconciliation rollup above is assignment-only; the physical reorg (or redirect stubs) is a cleanup pass.
3. **Verify Aug 6 IGoR full-proposal date on SAM.gov** before committing resources.
