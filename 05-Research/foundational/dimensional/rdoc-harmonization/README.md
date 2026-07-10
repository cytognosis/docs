# RDoC Units of Analysis — Extraction & Harmonization

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `dimensional`, `rdoc`, `harmonization`, `data-index`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Source: NIMH Research Domain Criteria (RDoC) matrix, https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc
Extracted 2026-05-26. Scope: six units of analysis (Molecules, Cells, Circuits, Physiology, Behavior, Self-Report). Genes and Paradigms excluded per request.

## What's here

```
reference_tables/   harmonization of each distinct unit to external ontologies/DBs
matrices/           binary construct × unit association matrices
```

### Coverage
58 construct/subconstruct pages parsed → 922 association rows. Distinct units used in associations:
molecules 64 · cells 51 · circuits 178 · physiology 134 · behavior 159 · self-report 82.
Join key throughout is the NIMH numeric element id (stable across construct pages and unit pages).

## reference_tables/ (Phase 1)

- **reference_molecules.csv** — RDoC molecule → PubChem. Columns: official_name, pubchem_cid, molecular_formula, smiles, entity_type, confidence, notes. CIDs assigned only to discrete compounds/peptides (33); receptors/proteins/families (31) intentionally left without a CID. The NMDA-agonist (CID 22880) vs NMDA-receptor (protein) distinction is preserved.
- **reference_cells.csv** — Cell Ontology (CL CURIE, live OLS4) + Brain Cell Atlas major-class annotation; flag_poor_map marks the 38 that are brain regions mislabeled as cells, functional/marker types (place/mirror/face-selective cells), or valid CL types outside the BCA brain taxonomy.
- **reference_circuits.csv** — Allen Human Brain Reference Atlas (graph_id=16, Ding et al. 2016 nomenclature; parent ontology of the 2020 3D 141-region atlas). is_network flags entries that are networks/pathways/connections rather than single regions (~71 of 178). match_quality + flag_poor_map included.
- **reference_physiology.csv** — closest SNOMED CT concept (conceptId, FSN, semantic tag) via authoritative terminology server. 88 flagged — mostly research-specific ERP/EEG/TMS signals genuinely absent from SNOMED.
- **reference_behavior.csv** — dual Entity/Quality decomposition per the Cytognosis dimension–direction model:
  closest HPO / SNOMED / NBO matches **plus** an ENTITY (dimension) CURIE (source priority NBO → OBA → ICF b-codes → Cognitive Atlas → MF/MFOEM) and a QUALITY CURIE from PATO, with direction_type drawn from the 8-type deviation typology (deficit/excess/absence/distortion/release/dysregulation/mistiming/context-decoupling, or "neutral_measure").
- **reference_self_report.csv** — instrument full name, most reputable source URL, copyright_status, n_items, and ordered_questions.
  **Copyright handling:** verbatim ordered items are recorded ONLY for public-domain / open-license instruments (7 of 82). Copyrighted/unknown instruments (75) carry the source link, publisher, and item count but no reproduced item text.

## matrices/ (Phase 2)

`matrix_<unit>.csv` — one per unit type. First three columns are **Domain, Construct, Subconstruct** (subconstruct blank where not applicable). Each remaining column is a distinct unit (header = canonical label; element id appended in brackets only to disambiguate duplicate labels). Cell value = 1 if that unit is associated with that construct/subconstruct on NIMH, else 0.

- 58 rows each (full construct + subconstruct hierarchy; parent/container pages that list only subconstructs or paradigms appear as all-zero rows).
- Associations are taken **individually** per page (no roll-up from subconstruct to parent).
- Verified: matrix 1-counts equal the raw association pair counts exactly (molecules 178, cells 64, circuits 247, physiology 163, behavior 178, self-report 92).

## RDoC → HiTOP crosswalk (signed)

`matrices/matrix_hitop.csv` and `reference_tables/reference_hitop_associations.csv`.
Source: Michelini, Palumbo, DeYoung, Latzman & Kotov (2021), "Linking RDoC and HiTOP: A new interface for advancing psychiatric nosology and neuroscience," *Clinical Psychology Review* (main paper + 5-figure supplement). Extracted from the paper's prose (direction of association) cross-checked against the supplementary figures (red arrow = positive, blue arrow = negative).

- **matrix_hitop.csv** — rows are the same 58 RDoC construct/subconstruct triplets (Domain, Construct, Subconstruct as the first three columns). The HiTOP columns use a **two-row hierarchical header**: row 1 = HiTOP Spectrum, row 2 = HiTOP Subfactor (blank where the association is at spectrum level). Values: **+1 positive association, −1 negative association, 0 none.** 9 HiTOP columns: Internalizing/Fear, Internalizing/Distress, Disinhibited Externalizing/Substance Abuse, Disinhibited Externalizing/Antisocial Behavior, Disinhibited Externalizing/(spectrum), Antagonistic Externalizing/Antisocial Behavior, Antagonistic Externalizing/(spectrum), Thought Disorder/(spectrum), Detachment/(spectrum).
- **reference_hitop_associations.csv** — the 88 underlying associations in long form with `confidence` (high/medium/low: figure-confirmed = high; text-only "emerging" links = medium/low) and `source_evidence` (figure + page).
- 88 signed cells (15 positive, 73 negative — the skew reflects that most cognitive/social deficits and reward hypofunction map to *higher* psychopathology). 35 of 58 rows carry ≥1 association.
- **Coverage caveat:** the paper predates RDoC's Sensorimotor Systems domain, so all Sensorimotor rows are 0. Reward Satiation ("not reliably linked") and Circadian Rhythms (only a tentative link to the general p-factor, out of scope) are intentionally all-zero per the paper.

## RDoC → HiTOP crosswalk — EXTENDED (literature-augmented + verified)

`matrices/matrix_hitop_extended.csv` and `reference_tables/reference_hitop_associations_extended.csv`.
This extends the base crosswalk above by (a) filling the gaps Michelini et al. left empty using other peer-reviewed literature and (b) verifying the base associations against independent sources.

- **Same structure** as the base matrix (two-row Spectrum/Subfactor header; rows = 58 RDoC triplets; values +1/−1/0), and it is a **strict superset** — every base association is preserved unchanged. One column added: **Somatoform** (spectrum-level), warranted by functional/conversion motor evidence.
- **109 signed cells** (17 positive, 92 negative), 46 of 58 rows populated (was 35).
- **Newly filled (literature-sourced, with PMIDs/DOIs in the reference file):**
  - *Sensorimotor Systems* (all 9 rows): motor abnormalities/neurological soft signs/psychomotor signs → Thought Disorder (−1) for Motor Actions and its subconstructs; Inhibition and Termination → Disinhibited Externalizing (−1, impulsivity); Agency and Ownership → Thought Disorder, Detachment, Somatoform (−1; passivity/anomalous agency, conversion); Habit-Sensorimotor → Substance Abuse / Disinhibited Externalizing (+1, overactive habit learning); Innate Motor Patterns → Thought Disorder (−1).
  - *Reward Satiation* → Internalizing/Distress (−1, anhedonic/hedonic decline) and Disinhibited Externalizing/Substance Abuse (−1, impaired satiation ↔ overconsumption/addiction).
  - *Circadian Rhythms* → Internalizing/Distress, Thought Disorder, Disinhibited Externalizing/Substance Abuse (all −1; transdiagnostic circadian disruption). Bipolar/mania circadian ties are noted but mania is not a clean in-scope HiTOP column.
- **Verification of the base 88:** every base association was checked against independent literature. Result — **0 contradicted**, 29 corroborated (direct meta-analysis/review), 43 consistent-indirect, 16 not-found (concentrated in the original low-confidence "emerging" links). The `reference_..._extended.csv` carries, per association: `origin` (base vs. extended), `confidence`, `source`, `verification_status`, and `verification_citation`.

**Extension caveats:** the new rows are *inferences from adjacent literature*, not from a dedicated RDoC–HiTOP crosswalk; most are medium/low confidence (see the reference file). HiTOP Eating Pathology (the most direct target for satiation/binge) is out of scope, so satiation rests on the food-addiction framing. Sign convention matches the base matrix (sign = direction of association between the RDoC function and the psychopathology dimension; deficit patterns = −1).

## RDoC → HiTOP crosswalk — WEIGHTED ([-1, +1])

`matrices/matrix_hitop_weighted.csv` and `reference_tables/reference_hitop_associations_weighted.csv`.
Continuous-valued version of the extended matrix: each cell carries **weight = sign × P(interaction)** in [−1, +1] (effectively [−0.94, +0.94] given the cap), with the probability of interaction built from three multiplicative evidence factors.

**Scoring scheme** (transparent and conservative — even fully-corroborated links top out near ±0.94 because real psychiatric effect sizes rarely exceed that):

| Factor | Levels | Multiplier |
|---|---|---|
| `base_score` (prior from confidence) | high / medium / low | 0.85 / 0.60 / 0.35 |
| `verification_factor` (independent-literature check, base rows) | corroborated / consistent_indirect / not_found / contradicted | 1.10 / 1.00 / 0.85 / 0.40 |
| `origin_factor` | base (Michelini 2021 peer-reviewed crosswalk) / extended (literature-inferred) | 1.00 / 0.85 |
| | cap | 0.95 |

`p_interaction = min(0.95, base_score × verification_factor × origin_factor)`; `weight = sign × p_interaction`.

**What the regimes look like:**
- Strongest (~±0.94): high-confidence + corroborated + base — e.g., Reward Anticipation→Distress/Substance Abuse, Working Memory→Thought Disorder, Performance Monitoring (ERN)→Fear.
- Mid (~±0.51–0.60): medium-confidence base, or medium-confidence extended.
- Weakest (~±0.30): low-confidence with no independent corroboration, or low-confidence inferred-extension (e.g., Habit-Sensorimotor→Disinhibited Externalizing spectrum, Innate Motor Patterns→Thought Disorder).

The companion `reference_..._weighted.csv` exposes every factor (`base_score`, `verification_factor`, `origin_factor`, `p_interaction`, `weight`) per association alongside the original `confidence`, `verification_status`, `origin`, and `source`/`citation` — so the weighting is fully auditable and re-tunable. The discrete +1/−1/0 matrix (`matrix_hitop_extended.csv`) and the binary base matrix (`matrix_hitop.csv`) remain alongside it, so all three resolutions of the crosswalk are available.

## Disease layer — RDoC×Disease and HiTOP×Disease (signed-weighted, Jacksonian convention)

`matrices/matrix_rdoc_disease.csv`, `matrices/matrix_hitop_disease.csv`, and `reference_tables/reference_disease_associations.csv`. Disorders are anchored in **MONDO** (Monarch Disease Ontology) per the methodology in our cdisc-qrs reference doc.

**Sign convention (different from the HiTOP crosswalk):** sign is the **Jacksonian positive/negative direction** of the disorder's phenotype on that RDoC/HiTOP dimension relative to neurotypical baseline:
- **+1** = primarily a **GAIN / RELEASE / EXCESS** (positive-symptom direction: hallucinations, mania, intrusions, hyperactivity, tremor, chorea, dysphoria-gained, paranoia, tics, agitation).
- **−1** = primarily a **LOSS / DEFICIT / ABSENCE** (negative-symptom direction: anhedonia, avolition, akinesia, memory loss, attention loss, social withdrawal).
- **0** = no association or truly balanced bidirectional. Magnitude in (0, 1] = literature reproducibility (≥0.85 meta-analyzed; 0.65–0.80 multi-study; 0.40–0.60 mixed; 0.20–0.35 emerging). `weight = sign × magnitude`; per cell, signed weights add and clamp to [−0.95, +0.95].

**33 disorders** across 3 categories (each with MONDO ID, grouped into 6 clinical clusters as the second header row):
- *Psychotic:* Schizophrenia, Schizoaffective.
- *Mood:* Bipolar I, Bipolar II, MDD, Persistent depressive (dysthymia).
- *Anxiety/OCD/Stress:* GAD, Panic, Social anxiety, Specific phobia, PTSD, OCD.
- *Neurodev/SUD/PD/Tic:* ADHD, ASD, Anorexia, Bulimia, Alcohol UD, Opioid UD, Borderline PD, Antisocial PD, Tourette.
- *Neurodegenerative:* Alzheimer, Parkinson, Huntington, FTD, DLB, ALS, MS.
- *Epilepsy:* Epilepsy (general), TLE, Idiopathic generalized, JME, Dravet.

**matrix_rdoc_disease.csv** — three header rows: Cluster / Disease name / MONDO id; then Domain/Construct/Subconstruct as the first three data columns; then 58 RDoC rows × 33 disease columns of weighted values. 276 cells set (98 positive, 178 negative). Range [−0.95, +0.95]. Note: associations are recorded at the most granular available level (subconstruct when literature is subconstruct-specific), so for constructs with subconstructs the construct-level row may be 0 — read the subconstruct rows for the full disorder profile.

**matrix_hitop_disease.csv** — same three-row header (Cluster / Disease / MONDO); first two data columns Spectrum/Subfactor; 14 HiTOP rows × 33 disease cols. 97 cells set. HiTOP scores are themselves pathology-direction, so most disorder×spectrum cells are +1 by convention (elevated content = gain); the small number of −1 cells (e.g., Schizophrenia × Detachment, Frontotemporal dementia × Detachment) capture cases where the elevated spectrum reflects predominantly *lost* normal function (anhedonia, asociality, apathy) per Jacksonian framing.

**reference_disease_associations.csv** — long-format raw reference: 379 evidence rows across all 33 disorders, each with `target_table` (RDoC vs HiTOP), `sign`, `magnitude`, computed `weight`, `n_sources`, semicolon-separated PMIDs/DOIs, and `evidence_note` (including bipolar phase tags). Multi-source citations are the norm (most cells have ≥2 independent sources; the strongest cells rest on meta-analyses).

**Bipolar phase handling:** Bipolar I and II carry intentional dual entries for the same RDoC construct on opposite signs (manic vs depressive phase) — these are kept individually in the long reference and additively combined in the matrix cells, so the net weight reflects course-of-illness dominance (e.g., Bipolar I × Reward Anticipation net +0.15 = mania-phase elevation slightly exceeds depressive-phase blunting in evidence strength).

**Method note on extension research:** literature search was anchored to peer-reviewed meta-analyses and major reviews per cluster (e.g., Heinrichs & Zakzanis for schizophrenia neurocognition, Pizzagalli for reward in depression, Bora for cognition meta-analyses across disorders, McKeith consensus for DLB, Rascovsky consensus for bvFTD, Strong for ALS-FTD, Fiest for depression in epilepsy, Kahana Levy for TLE memory). The cdisc-qrs-comprehensive-reference doc's MONDO seed table was used as the disorder-MONDO anchor; additional MONDO IDs were resolved via OLS4. HiTOP placements followed Kotov 2017 / Conway 2021 / Michelini 2021.

## Caveats
- "High-rigor" mappings were verified against the live source for each term; confidence and flag columns mark weak/approximate matches — review flagged rows before downstream use.
- Allen 141-region 2020 subset is not exposed as a discrete API set; mapping used the parent Allen human structure ontology (graph_id=16), which contains that subset.
- Behavior Entity/Quality is a first verified pass; social-cognition, language-pragmatics, and sleep-umbrella terms have sparse ontology coverage and are flagged.

## Canonical synthesis

This harmonization backs the dimensional prose synthesis: [`../psych-axes-synthesis.md`](../psych-axes-synthesis.md).
