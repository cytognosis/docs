# Cytoverse Track: Science Foundation (ADHD Edition)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 | **Reading time:** ~3 min

**BLUF:** The science foundation is real. The BDNF/TrkB axis paper has a clear, bounded scope with strong grant alignment (EVIDENT/HSF, IGoR TA1). The KG/cytos platform is production-ready. The cellular micro-to-meso causal bridge is the spine that connects all three funding tracks; it is the single most important concept to communicate in any grant narrative.

**If you only read one thing:** Section 2, "The three actions," tells you exactly what to do next.

---

## Done List (check marks = already complete)

- [x] Science keystone dossier written (BDNF/TrkB axes, publish vs platform boundary locked)
- [x] 14-disorder transdiagnostic syntheses complete (MICRO + MESO + MACRO scales)
- [x] KG platform production: 9.3M nodes, 53M edges, 200+ edge types
- [x] Data lake organized (~1.5TB, provenance 93.3%)
- [x] Validation infrastructure (VFS, RO-Crate) operational
- [x] Genomic atlas implemented (GWAS, eQTL, PRS, LDGM modules all production)
- [x] Publish-vs-platform boundary defined

---

## 1. Science snapshot

### The axes (publishable)

Three continuous, molecularly grounded axes defined by BDNF/TrkB downstream dysregulation:

| Axis | Molecular program | Grant hook |
|---|---|---|
| Mood | BDNF/TrkB to CREB, neuroplasticity, LTP | EVIDENT: this is the plasticity state neuroplastogens target |
| Thought | TrkB/PLCgamma to KCC2, E/I balance | IGoR TA1: circuit heterogeneity mechanism |
| Cognitive | BDNF-CREB learning/memory, hippocampal | HSF: cognitive endpoint stratification |

**Cohorts:** Discovery in McLean (published). Out-of-distribution validation in MtSinai (in progress, WGS must run inside MtSinai's environment with Panos's team).

### The platform (confidential)

There is a confidential genomic platform layer that reconstructs the axes from genotype alone (noninvasive, scalable). It is the moat. It stays off the paper and out of all external-facing content. Details are in the full track doc (Section 5) and the dossier (Section 5).

### The KG

| Layer | Size | Status |
|---|---|---|
| Ontology Graph | ~30K disease terms, ~15K anatomy terms, and more | Production |
| Catalog Graph | Publications, clinical trials | Production |
| Observation Graph | GWAS hits, Monarch/PrimeKG associations | Production |
| Genome KG | GENCODE, PGC, eQTL, LDGM | Production |
| **Total** | **9.3M nodes, 53M edges** | **Production** |

---

## 2. The three actions (no outreach required)

**Do now:**

1. **Draft the bipolar paper.** Scope: BDNF/TrkB Mood/Thought/Cognitive axes, McLean discovery, MtSinai OOD validation. This is P0. Without a preprint, IGoR credibility and EVIDENT anchor are both weak. Lock with Brad and Xikun. Keep the confidential platform layer off.

2. **Run stratified-LDSC for CREB/SREBP heritability enrichment.** This is the cheapest check on whether the confidential platform's biological premise holds before building the full pipeline. One analysis, publishable on its own. Do this before committing engineering time.

3. **Load biomolecular entities (genes, proteins, variants) as first-class KG nodes.** Currently the KG has gene ontology classes but not gene instances. The micro-to-meso bridge traversal (GWAS hit to eQTL to cell-type program) is blocked until this is done. Engineering sprint.

**Needs outreach (park for later):**

- Confirm MtSinai WGS DUA permits Cytognosis-relevant analysis.
- Coordinate with Panos's team on WGS environment access.

---

## 3. The cellular micro-to-meso causal bridge (the concept that connects everything)

This is the key concept to put in every grant narrative.

**The idea:** Psychiatric variation runs from genome to molecules to cells (micro) up to circuits and connectivity (meso). Most groups work at one scale. Cytognosis's differentiated position is the causal link between scales.

| Scale | What we measure | What it means |
|---|---|---|
| Micro | BDNF/TrkB cell-type programs in snRNA-seq | Who has impaired plasticity, E/I balance, or cognitive BDNF signaling |
| Bridge | Cell-type specific heritability, eQTL-to-program traversal | Why the circuit looks the way it does |
| Meso | dlPFC-sgACC connectivity, gamma oscillations, aperiodic slope | What Cytoscope sensors will read |

**Funding connection:**

| Track | What the bridge delivers |
|---|---|
| IGoR TA1 | Mechanistic heterogeneity explanation (not just symptom clustering) |
| HSF / EVIDENT | Predicts who responds to which neuroplastogen from molecular biotype |
| NSF X-Labs / Cytoscope | Theory of what the sensor is reading |

---

## 4. Gaps to be aware of

| Gap | Urgency |
|---|---|
| Bipolar paper not submitted | Blocking |
| Stratified-LDSC not run | High |
| Biomolecular KG nodes missing | High |
| Cognitive-axis pathway set not finalized | High (blocks paper) |
| MtSinai WGS DUA not confirmed | High |
| SurrealDB async bug | Medium |

---

## 5. Duplicate docs needing canonical-home assignment (flag only, do not edit)

| File | Current location | Canonical home |
|---|---|---|
| `01_plan_prose.md` (cytos platform design) | `docs/cytoverse/cytos/historical/historical/` | `docs/cytoverse/cytos/` engineering canonical |
| `neurobehavioral-dimension-direction-model.md` | `personal-drafts/Science/psych/` | Superseded by BDNF dossier |

---

**Full doc:** `/home/mohammadi/Claude/Projects/X-Labs/01-strategy/tracks/CYTOVERSE_TRACK_2026-06-03.md`
**Science keystone:** `/home/mohammadi/Claude/Projects/X-Labs/04-research/BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md`
