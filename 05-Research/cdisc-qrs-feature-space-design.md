# Cytognosis Neurobehavioral Phenotype Feature Space: Design Reference (Part 2)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Companion to `cdisc-qrs-comprehensive-reference.md`. Where Part 1 catalogued CDISC QRS instruments and external standards, this document tackles three design problems:

1. **Choose or construct a universal neurobehavioral phenotype feature set** (cognition, mood, attention, affect, perception, motor, sleep, social, personality, substance, eating, sexual, somatic, QoL), to which DSM/ICD diagnoses map cleanly and every major instrument projects.
2. **Map instruments and tests onto that feature set** (psychiatric, neurology, QoL, substance, sexual function, GU), with item-level granularity, so the same axes can be tracked continuously by a guardian-agent sensor.
3. **Map diagnoses (DSM-5-TR, ICD-10-CM, ICD-11) onto the same feature set**, so categorical labels can be reconstructed from feature signatures.

Plus operational appendices: a 40 row bulk-download inventory, exploratory Cypher queries for the existing UMLS + SNOMED + OLS4 Neo4j graph, and an honest gap list.

Author: Cytognosis Foundation, drafted 2026-05-13. Status: living design doc.

---

## 0. TL;DR

No single existing vocabulary supplies the universal feature space you need. Each candidate is strong on one axis and weak elsewhere:

- **HPO behavioral subtree (HP:0000708)** is monthly-refreshed, has good cross-vocabulary mapping infrastructure (SSSOM to SNOMED, UMLS, MONDO, ICD-10), but it has only ~235 descendants under HP:0000708 plus the cognitive sister branch HP:0100543. Its psychiatric depth lags behind clinical use, and its terms are framed as abnormalities rather than continuous features.
- **SNOMED CT mental state / behavior / disorder subtree (root 384821006, plus the disorder root 74732009)** has 6,000 to 8,000 concepts, the richest relationship model in any clinical terminology, and built-in severity and temporal context. It is the only candidate that natively supports post-coordination of severity into the term, and it is the de facto DSM bridge via ICD-10-CM. But it is enormous, post-coordination-heavy, and not a hierarchy of features per se.
- **UMLS Semantic Types** (T041 Mental Process, T048 Mental or Behavioral Dysfunction, T053 Behavior with sub T054/T055, T184 Sign or Symptom) give cross-vocabulary clustering and synonymy. UMLS is a hub, not a feature ontology.
- **Neuro Behavior Ontology (NBO)** is confirmed too limited for human psychiatry; it reflects rodent ethology (mating, grooming, locomotion) and has not had a meaningful release since July 2023.
- **Mental Functioning Ontology (MF) + MFOEM (Emotion)** together have ~1,024 terms across mental process, disposition, quality, mood, emotion. Small but the only candidate with proper philosophical typing. Best for an upper-level scaffold.
- **Cognitive Atlas + CogPO** give the deepest cognitive-construct and task-paradigm representation (~918 concepts and ~857 tasks). Cognitive-only.
- **ICF Body Functions Ch.1 (mental functions, b110 to b189) + Ch.2 (sensory)** plus Activities and Participation Ch.1 (learning and applying knowledge) and Ch.7 (interpersonal interactions) supply a WHO-blessed mid-grain scaffold of about 150 stable categories covering somatic + mental + social + environmental in one taxonomy. Useful as a backbone but not granular enough alone.
- **RDoC Matrix** has 6 domains and ~36 constructs across the units-of-analysis grid. Mechanistically grounded, neuroscience-anchored, designed for dimensions. Coarse hierarchy and no native somatic / QoL coverage.
- **HiTOP** has a deep 6 level hierarchy (super-spectra, spectra, sub-factors, syndromes, symptom components, items) covering psychopathology and personality. The best dimensional psychometric backbone. Weak on cognition, motor, sleep, sensory.
- **PROMIS + NIH Toolbox** give about 2,100 IRT-calibrated items across ~127 item banks. LOINC-coded, FHIR-ready, FDA-qualified for several domains. The right item-level operational layer.

**Recommendation: build the Cytognosis feature space as a six layer stack** that uses each candidate at its strength:

```
Layer 0 (metamodel)            : OGMS + IAO + BFO
Layer 1 (universal scaffold)   : ICF Body Functions Ch.1, 2 + Activities & Participation Ch.1, 7, plus selected GU/somatic chapters
Layer 2 (upper mental category): MF + MFOEM (process / disposition / quality / appraisal / mood / emotion)
Layer 3 (mid construct overlay):
    3a (mechanistic)           : RDoC + Cognitive Atlas + CogPO
    3b (psychometric)          : HiTOP spectra / sub-factors / syndromes / components
Layer 4 (clinical leaves)      : HPO behavioral + cognitive subtrees, SNOMED CT mental state + disorder subtree
Layer 5 (operational items)    : PROMIS item banks + NIH Toolbox measures + CDISC QSTESTCD items + PhenX protocols
```

Every Cytognosis feature carries a 5-tuple identifier `(ICF code, MF/MFOEM class, RDoC construct, HiTOP component, HPO + SNOMED + UMLS CUI bundle)` plus an operational binding to one or more PROMIS / NIH Toolbox / CDISC items. DSM-5-TR and ICD-11 diagnoses are then reconstructable as feature combinations at Layer 3b (HiTOP syndrome level) or as boolean conjunctions of Layer 4 clinical leaves.

This stack is not yet built anywhere in public form. Cytognosis can build it by ingesting the public components and curating the bridge tables. The bulk-download inventory in §6 enumerates every component.

---

## 1. Problem Framing

### 1.1 Why a feature space at all

The analogy to RNA-seq is exact and important. In transcriptomics, the feature axis (genes) is:
- Open, stable, and shared across cohorts and species (via orthology).
- Approximately 1D (each gene is a feature; gene families and pathways are derived, not primary).
- Quantitative (expression value per gene per sample).
- Hierarchical only in derived ontologies (GO, Reactome).

For neurobehavioral phenotype the right feature space is similar in spirit but differs in two ways:
- Features should be **hierarchically nested** (zoomable from coarse "negative affect" to fine "irritability evoked by minor frustration in social contexts"), so models can learn at the resolution the data supports.
- Features should carry **modality-agnostic operationalization**, so the same axis can be measured by a self-report item, a clinician rating, a performance task, or a language signal extracted by a continuous-monitoring agent.

The deliverable is a feature space that:
1. Covers cognition, mood, attention, affect, perception, motor, sleep, social, personality, substance, eating, sexual, somatic, QoL, and functioning.
2. Has at least 4 hierarchical depths so models can zoom.
3. Carries a stable identifier per node that maps to ICF, HiTOP, RDoC, HPO, SNOMED, UMLS, LOINC, and CDISC.
4. Lets us reconstruct DSM-5-TR and ICD-11 mental and behavioral disorder labels as feature combinations.

### 1.2 Why none of the existing vocabularies is sufficient alone

Each candidate fails at least one criterion:

| Criterion | HPO behavioral | SNOMED mental | UMLS | NBO | MF+MFOEM | CogAt | ICF | RDoC | HiTOP | PROMIS | NIH Tbx | CDISC QSTESTCD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hierarchical depth >= 4 | yes (5 to 8) | yes (12 to 14) | no | yes (6 to 7) | yes (5 to 6) | yes (5 to 7) | yes (4) | no (3) | yes (6) | no (3) | no (2 to 3) | no (2 to 3) |
| Somatic + mental | partial | yes | yes | weak | no | no | yes | no | weak | yes | partial | yes |
| Sleep specific | shallow | rich | n/a | shallow | weak | no | yes (b134) | only arousal | weak | yes (PROMIS Sleep) | no | yes (PSQI, ESS) |
| Sexual function | no | yes | yes | partial | no | no | yes (b640+d770) | no | partial | yes (SexFS) | no | yes |
| Substance use | weak | yes | yes | weak | no | no | weak (b1304) | partial | yes (Dis-Ext) | yes | no | yes (AUDIT, FTND) |
| Personality | weak | yes | yes | no | partial | weak | yes (b126) | weak | yes | no | no | no |
| Continuous quantification | no | partial (severity) | n/a | no | no | no | qualifier 0 to 4 | partial | partial | yes (IRT) | yes (T-score) | partial |
| DSM reconstruction | poor | good (via ICD) | indirect | none | poor | none | partial | poor | excellent | partial | partial | good |
| Instrument item map | none direct | via LOINC | via LOINC | none | none | partial | partial | none | yes (HiTOP-SR) | yes (LOINC) | yes (LOINC) | yes (native) |
| Bulk download | yes | yes (UMLS) | yes | yes | yes | yes | yes | weak (HTML) | partial | yes | partial | yes |

No row has yes everywhere. Stacking is the only path.

### 1.3 The three problems restated

- **Problem 1** (universal feature axes): pick a primary stack. Solved in §3 below.
- **Problem 2** (instruments and tests onto features): build the item-to-feature crosswalk by leveraging LOINC + SNOMED + HiTOP-SR mapping + PROMIS LOINC codes + CDISC supplements. Approach in §4.
- **Problem 3** (DSM and ICD onto features): leverage existing UMLS SNOMED ICD chains plus HiTOP DSM-5 mapping plus hand-curated criterion decomposition. Approach in §5.

---

## 2. Phenotype Ontology Assessment

### 2.1 HPO behavioral subtree

**Identity and size.** HPO v2026-02-16 has 32,085 terms and 373 object properties. The behavioral subtree root is **HP:0000708** (current label "Atypical behavior"; older "Behavioral abnormality" and "Psychiatric disturbances" retained as synonyms). The sister cognitive subtree is **HP:0100543 Cognitive impairment**. Their common parent is **HP:0000707 Abnormality of the nervous system**.

**Direct children of HP:0000708 (16 branches, confirmed via OLS4 API)**:

1. HP:0002193 Pseudobulbar affect
2. HP:0008768 Abnormal sexual behavior
3. HP:0012433 Abnormal social behavior
4. HP:0025783 Diagnostic behavioral phenotype
5. HP:0031466 Impairment in personality functioning
6. HP:0033051 Impaired executive functioning
7. HP:0033052 Non-epileptic seizure
8. HP:0100962 Excessive shyness
9. HP:4000068 Abnormal interest
10. HP:5200024 Abnormal relationship
11. HP:5200045 Reduced impulse control
12. HP:5200046 Sensory behavioral abnormality (24 descendants)
13. HP:5200104 Abnormal play (4 descendants)
14. HP:5200241 Recurrent maladaptive behavior (117 descendants, densest branch; covers self-injurious, stereotypic, compulsive, addictive behaviors)
15. HP:5200261 Abnormal demeanor (6 descendants)
16. HP:6000768 Echophenomenon (17 descendants; echolalia, echopraxia)

Total descendants of HP:0000708: **235**. Add HP:0100543 (cognitive impairment, several hundred more terms) and HP:0000709 (abnormality of higher mental function) to get the operational HPO behavioral / cognitive vocabulary, around 700 to 1,000 terms.

The HP:5200xxx and HP:6000xxx ID ranges show heavy 2024 to 2025 expansion driven by the Monarch Initiative and SNOMED International bidirectional mapping collaboration announced 2024. This is the most active near-term improvement vector for HPO psychiatric coverage.

**Coverage by life domain (0 = none, 5 = excellent)**: mood 4, anxiety 3, psychosis 3, cognition 4 (via HP:0100543), attention 3, executive 4, memory 4, language 3, motor 4, sleep 4, perception 3, social 4, personality 3, substance 3, impulse 4, eating 3, somatic 3. Max IS-A depth 7 to 8 from HP:0000118.

**Relationship richness.** HPO is a near-pure IS-A tree with selective `has_modifier`, `has_onset`, `has_clinical_course`, `has_frequency` on disease-association files. The `phenotype.hpoa` file ties HPO terms to OMIM and Orphanet diseases with frequency triples.

**Mappings.** Ships `hp.sssom.tsv` with SNOMED CT, UMLS, MONDO, ORDO, MeSH, MedDRA, and ICD-10 cross-mappings. ~30% of HPO classes have complete SNOMED CT equivalence; ~92% have at least partial mapping. DSM-5 itself is not directly cross-walked, but reach-via-SNOMED is improving fast under the Monarch x SNOMED collaboration.

**Strengths.** Active maintenance (monthly), permissive license (HPO permissive, effectively CC-style), broad community use in rare-disease genomics, robust SSSOM cross-mappings, growing common-disease coverage.

**Limitations.** Mid-grained (not deeply granular for symptom-level psychiatric features), framed as abnormalities rather than continuous features, no built-in severity quantifier per term, psychiatric depth lags behind SNOMED.

**Bulk download.** `https://github.com/obophenotype/human-phenotype-ontology/releases`. Files: `hp-base.obo` ~10.7 MB, `hp-base.json` ~21 MB, `hp-full.json` ~41 MB, `hp-base.owl` ~46 MB, `hp.sssom.tsv` ~5 MB. License HPO permissive (free for commercial use with citation).

**Verdict.** Primary clinical leaf vocabulary in Layer 4 of the stack. Use HP:0000707 + HP:0000708 + HP:0000709 + HP:0100543 together. Not sufficient alone, but the best monthly-refreshed open-license clinical phenotype anchor.

### 2.2 SNOMED CT mental state / behavior / disorder subtree

**Identity and size.** SNOMED CT International Edition (March 2026 release) has ~360,000 active concepts. The relevant top-level roots:
- **384821006 Mental state, behavior and/or psychosocial function finding** (under 404684003 Clinical finding)
- **74732009 Mental disorder** (the operational DSM target subtree)
- **36456004 Mental state finding** (top-level psychological state)
- **247591002 Behavior finding**
- **248254009 Mood finding** (the user's earlier reference to 106131003 maps roughly here; verify in your local graph)
- **247806001 Thinking finding**
- **285852003 Anxiety**
- **191659001 Substance use / abuse findings**
- **284465006 Finding relating to psychosocial functioning**
- **718497002 Aggressive behavior**

Combined mental state + disorder coverage: approximately **6,000 to 8,000 concepts** in the International Edition; the US Edition adds ICD-O extensions and CDC additions. Max IS-A depth 12 to 14 from the top.

**Coverage**: mood 5, anxiety 5, psychosis 5, cognition 4, attention 4, executive 3, memory 4, language 4, motor 4, sleep 5, perception 4, social 4, personality 5, substance 5, impulse 4, eating 5, somatic 5.

**Relationship richness, the killer feature.** SNOMED is the only candidate with a built-in concept model that includes:
- IS-A (the backbone)
- `116676008 Associated morphology`
- `363698007 Finding site`
- `246075003 Causative agent`
- `246112005 Severity` (the only first-class severity relation in any candidate)
- `408729009 Finding context`
- `408731000 Temporal context`
- `408732007 Subject relationship context`
- `370135005 Pathological process`
- `47429007 Associated with`
- `255234002 After`

This makes SNOMED the **only candidate where severity and temporal context are first-class attributes**, not annotations. For continuous monitoring (your guardian-agent sensor), that is critical.

**DSM and ICD reach.** SNOMED CT to ICD-10-CM Map (the I-MAGIC map) is published by NLM, refreshed quarterly inside the SNOMED CT US Edition release file. UMLS Metathesaurus exposes it via `MRMAP.RRF`. SNOMED CT to ICD-11-MMS map pilot completed 2024; full chapter-by-chapter mapping is in progress (current coverage <30% of MMS as of May 2026).

**Bulk download.** SNOMED CT International Edition via SNOMED International Member Licensing Portal `https://mlds.ihtsdotools.org` (login). SNOMED CT US Edition via NLM `https://www.nlm.nih.gov/healthit/snomedct/us_edition.html`. RF2 format, ~600 MB compressed and ~5 to 6 GB uncompressed for the full International release. Monthly International releases since 2025. US Edition refreshed March and September. License: SNOMED Affiliate License, free for UMLS license holders.

**Verdict.** Primary deep clinical backbone in Layer 4. Use 384821006 plus 74732009 subtree extracts. Built-in severity and temporal context attributes are essential for the continuous-monitoring use case.

### 2.3 UMLS Semantic Network and Metathesaurus

**Identity.** UMLS 2025AB has ~3.49 M CUIs across 190 source vocabularies; 2026AA is the next semiannual release (May 2026). The Semantic Network has 127 Semantic Types organized as a DAG.

**Neurobehaviorally relevant Semantic Types (TUIs)**:
- **T053 Behavior** (parent; subsumes T054 Social Behavior and T055 Individual Behavior)
- **T041 Mental Process** (cognition, thinking, mood, memory; sub of T039 Physiologic Function)
- **T048 Mental or Behavioral Dysfunction** (clinical disorder; sub of T046 Pathologic Function)
- **T184 Sign or Symptom** (sub of T033 Finding)
- **T039 Physiologic Function** (parent of T041)
- **T046 Pathologic Function** (parent of T048, T047 Disease or Syndrome)
- **T040 Organism Function** (parent of T039)
- **T033 Finding** (broader umbrella)

Note that the earlier draft conflated T038 with Behavior; T038 is actually **Biologic Function**. The correct behavioral TUI is T053.

**Empirical CUI estimates** (UMLS does not publish per-TUI counts; values from prior community analyses):
- T048 Mental or Behavioral Dysfunction: ~20,000 to 25,000 CUIs
- T041 Mental Process: ~5,000 to 7,000 CUIs
- T053 Behavior: ~3,000 to 4,000 CUIs (T054 + T055 included)
- T184 Sign or Symptom: ~25,000 to 30,000 CUIs (broad, mixed)
- T039 Physiologic Function: ~5,000 to 6,000 CUIs
- T046 Pathologic Function: ~10,000 to 12,000 CUIs

**Relationship richness.** `MRREL.RRF` has 50+ relationship labels: `PAR/CHD` (parent/child IS-A within sources), `RB/RN` (broader/narrower), `RO` (other), `SY` (synonym), `RQ` (related qualifier), `SIB` (sibling). Source-specific `RELA` adds finer semantics like `clinically_associated_with`, `causative_agent_of`, `due_to`, `manifestation_of`.

**Role for Cytognosis.** UMLS is not a feature ontology but a **cross-vocabulary clustering and synonymy hub**. The CUI is the join key that ties together SNOMED, ICD, DSM-5, MeSH, MedDRA, LOINC, HPO, MONDO, NCIt mentions of the same concept. Your existing Neo4j graph already gives you this; UMLS provides the canonical CUI assignment.

**Bulk download.** `https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html`. Full release ~33.7 GB unpacked (2024AB), Metathesaurus subset 15 to 20 GB. Biannual (May AA, November AB). Files: MRCONSO.RRF (5 to 6 GB), MRSTY.RRF (~500 MB), MRREL.RRF (10 to 12 GB), MRDEF.RRF (~300 MB), MRHIER.RRF (~6 GB), MRMAP.RRF for mapping sets, MRSAB.RRF for source attribution. UMLS click-through license, free.

**Verdict.** Always-on cross-vocabulary hub in Layer 4. Use CUI bridge to align HPO, SNOMED, ICD, DSM, LOINC. Already in your Neo4j graph.

### 2.4 Neuro Behavior Ontology (NBO)

**Identity.** OBO Foundry. Version 2023-07-04, 4,546 terms, 326 object properties, license CC BY 3.0. Two top branches: `NBO:0000243 behavior process` and `NBO:0000313 behavior phenotype`.

**Coverage**: mood 1, anxiety 2, psychosis 0, cognition 1, attention 2, executive 1, memory 2, language 1, motor 4, sleep 3, perception 1, social 4, personality 0, substance 1, impulse 2, eating 4, somatic 1.

**Why it falls short.** NBO was built for **rodent and animal phenotyping** (integrates with MGI, ZFIN, MP). Categories are ethological (mating, grooming, locomotion, vocalization, parental behavior, exploration) and not aligned with human psychiatric phenomenology. Virtually no representation of psychosis, affect, or human cognition as a clinician would frame it. The GitHub repo (`obo-behavior/behavior-ontology`) shows light maintenance since 2023.

**Bulk download.** `http://purl.obolibrary.org/obo/nbo.owl`, ~6 MB.

**Verdict.** Confirmed too limited. Optional secondary use for cross-species translation (drug discovery animal model alignment); not a primary axis.

### 2.5 Mental Functioning Ontology (MF) + MFOEM

**Identity.** Janna Hastings et al. MF v2025-07-08, 400 terms, 90 properties. MFOEM (emotion module) v2025-07-31, 624 terms, 99 properties. Combined ~1,024 terms. Built on BFO. CC BY.

**Structure.** MF has three core branches: `mental process`, `mental disposition / trait`, `mental representation / quality`. MFOEM adds appraisal, subjective feeling, emotional disposition, mood, affect as first-class kinds. Cross-references Cognitive Atlas; aligned with OGMS for the disorder/dysfunction view.

**Strengths.** The only candidate with **philosophically-grounded type distinctions** between process, disposition, quality, representation, and emotional appraisal. Exactly what you want for a hierarchical feature space upper-level scaffold. Emotion appraisal theory (Scherer) is formally represented.

**Limitations.** Small (1,024 terms total). Limited disorder coverage. Sparse psychiatric symptoms. Not widely cross-referenced from external clinical sources.

**Bulk download.** `http://purl.obolibrary.org/obo/MF.owl` ~2 MB, `http://purl.obolibrary.org/obo/MFOEM.owl` ~3 MB. CC BY.

**Verdict.** Best upper-level scaffold for the feature space (Layer 2). Use as the "feature category" backbone, then populate leaf features from HPO and SNOMED in Layer 4.

### 2.6 Cognitive Atlas + CogPO

**Cognitive Atlas.** ~918 cognitive concepts in 9 categories (Learning and Memory 116, Perception 97, Language 96, Reasoning and Decision Making 65, Executive / Cognitive Control 43, Attention 37, Emotion 33, Motivation 13, Action 10) plus ~50 disorder tags and ~800 task paradigms with conditions, contrasts, measures. Python wrapper (PyPI `cognitiveatlas`) updated July 2024. OWL build at `github.com/CognitiveAtlas/cogat-ontology`. CC BY.

**CogPO** (Cognitive Paradigm Ontology). Last major release 2013, light maintenance. ~700 to 800 classes focused on task / paradigm / stimulus modality / response / cognitive paradigm class. Built on BFO; tightly integrated with BrainMap.org. CC BY.

**Coverage**: cognition 5, mood 2, attention 5, sleep 1, perception 5, motor 4, social 4, substance 1, eating 0, sexual 0, QoL 0, personality 1, somatic 0.

**Strengths.** Cognitive Atlas is the deepest cognitive-construct ontology that exists (max IS-A depth 5 to 7), used heavily in fMRI literature, complementary to RDoC.

**Limitations.** Cognitive-only. Weak on affect, psychiatric symptoms, QoL. CogAt's category-level depth is only 2 to 3 at the top, deeper at the leaf level.

**Bulk download.** `https://github.com/CognitiveAtlas/cogat-ontology/raw/master/cognitiveatlas.owl` ~2 MB. API at `https://www.cognitiveatlas.org/api/v-alpha/concept`. CogPO via `https://bioportal.bioontology.org/ontologies/COGPO/download`.

**Verdict.** Essential cognitive-construct overlay (Layer 3a). Pair with RDoC for mechanism layer. Especially valuable for mapping instrument items to underlying cognitive constructs (MoCA Trails B to "task switching"; MMSE serial 7s to "working memory / mental arithmetic").

### 2.7 NIFSTD, SYMP, OGMS, MONDO

**NIFSTD.** SciCrunch / NIF-Ontology. Last formal release 3.1, January 2018. CC BY 4.0. Strong for anatomy and cells; weak as a standalone behavioral source. Use only for anatomical / neural-circuit grounding when biomarker / imaging data arrive.

**SYMP (Symptom Ontology).** Disease Ontology family. 1,019 terms, version 2024-05-17, max depth 5. Useful as a lightweight crosswalk for layperson symptom labels; not a feature-space candidate.

**OGMS + IAO.** 186 terms, version 2021-08-19. CC BY. Defines the disease / disorder / disposition / pathological process / sign / symptom / clinical finding / patient role distinctions on top of BFO. Use as Layer 0 metamodel.

**MONDO (Monarch Disease Ontology).** Continues to absorb DSM, ICD, SNOMED, HPO disease equivalences. ~24,000 disease classes; the mental-disorder branch maps to DSM-5 codes. Use as the disorder-level unification anchor in Layer 4 alongside HPO and SNOMED.

### 2.8 Newer integrative behavioral / cognitive ontologies (2022 to 2026 scan)

- **CAOS** (Cognition And OntologieS) workshop series, edition 9 at FOIS 2025 (Catania). Active research community, no released integrative ontology yet.
- **"Human Ontology with Cognition and Ability Models"** (Springer 2026, digital-twin context). Academic, not yet released as a public OBO artifact.
- **BCO / Behavior and Cognition Ontology** and similar names: no concrete public release confirmed as of May 2026.

No 2022 to 2026 integrative ontology supersedes the HPO + SNOMED + MF/MFOEM + Cognitive Atlas combination. Monitor CAOS 2025 to 2026 outputs.

### 2.9 Comparative phenotype-ontology matrix

| Criterion | HPO behavioral | SNOMED mental | UMLS sem types | NBO | MF+MFOEM | CogAt+CogPO | NIFSTD | SYMP | OGMS |
|---|---|---|---|---|---|---|---|---|---|
| Behavioral term count | ~235 + ~500 cognitive | ~6,000 to 8,000 | n/a (clusters) | 4,546 | 1,024 | ~918 + ~800 | ~50 (behavior) | ~50 (mental) | 0 |
| Max IS-A depth | 7 to 8 | 12 to 14 | 3 (sem net) | 6 to 7 | 5 to 6 | 5 to 7 (concepts) | 4 to 5 | 4 to 5 | 4 |
| Mood | 4 | 5 | n/a | 1 | 4 | 3 | 1 | 3 | n/a |
| Anxiety | 3 | 5 | n/a | 2 | 3 | 2 | 1 | 4 | n/a |
| Psychosis | 3 | 5 | n/a | 0 | 2 | 1 | 0 | 2 | n/a |
| Cognition | 4 | 4 | n/a | 1 | 5 | 5 | 2 | 1 | n/a |
| Attention | 3 | 4 | n/a | 2 | 4 | 5 | 1 | 1 | n/a |
| Memory | 4 | 4 | n/a | 2 | 4 | 5 | 2 | 2 | n/a |
| Motor | 4 | 4 | n/a | 4 | 1 | 3 | 3 | 4 | n/a |
| Sleep | 4 | 5 | n/a | 3 | 1 | 1 | 1 | 3 | n/a |
| Social | 4 | 4 | n/a | 4 | 3 | 3 | 0 | 1 | n/a |
| Personality | 3 | 5 | n/a | 0 | 4 | 2 | 0 | 0 | n/a |
| Substance | 3 | 5 | n/a | 1 | 0 | 1 | 0 | 1 | n/a |
| Severity built-in | via HPOA | yes | via post-coord | no | no | no | no | no | no |
| DSM-5 mapping | via SSSOM | yes via ICD | yes via SAB | none | none | partial | none | indirect | none |
| CDISC QRS mapping | none direct | via LOINC | via LNC SAB | none | none | partial | none | none | none |
| License | HPO permissive | UMLS / Affiliate | UMLS | CC BY 3.0 | CC BY | CC BY | CC BY 4.0 | CC BY | CC BY |
| Refresh | monthly | monthly (US) | biannual | stale 2023 | annual | continuous (API) | stale 2018 | annual | stale 2021 |
| Recommended role | Layer 4 leaves | Layer 4 backbone | Layer 4 crosswalk hub | optional cross-species | Layer 2 scaffold | Layer 3a cognitive overlay | optional grounding | skip | Layer 0 metamodel |

---

## 3. Construct Framework Assessment and Featureset Recommendation

This section assesses the dimensional and construct frameworks (ICF, RDoC, HiTOP, PROMIS, NIH Toolbox, PhenX) and recommends the composite architecture.

### 3.1 ICF (International Classification of Functioning, Disability and Health)

**Structure.** 4 components; ~1,424 categories at 4 levels (component, chapter, 2nd level, 3rd/4th level).

**Body Functions Ch.1 Mental Functions, full b110 to b189 enumeration**:
- **Global mental functions (b110 to b139)**
  - b110 Consciousness functions
  - b114 Orientation functions (b1140 time, b1141 place, b1142 person/self, b1143 person/others, b1144 objects, b1148, b1149)
  - b117 Intellectual functions (including intellectual disability)
  - b122 Global psychosocial functions
  - b126 Temperament and personality functions (b1260 extraversion, b1261 agreeableness, b1262 conscientiousness, b1263 psychic stability, b1264 openness to experience, b1265 optimism, b1266 confidence, b1267 trustworthiness, b1268, b1269)
  - b130 Energy and drive functions (b1300 energy level, b1301 motivation, b1302 appetite, b1303 craving, b1304 impulse control, b1308, b1309)
  - b134 Sleep functions (b1340 amount, b1341 onset, b1342 maintenance, b1343 quality, b1344 sleep cycle, b1348, b1349)
  - b139 Global mental functions, other specified / unspecified
- **Specific mental functions (b140 to b189)**
  - b140 Attention functions (b1400 sustained, b1401 shifting, b1402 divided, b1403 shared, b1408, b1409)
  - b144 Memory functions (b1440 short-term, b1441 long-term, b1442 retrieval, b1448, b1449)
  - b147 Psychomotor functions (b1470 psychomotor control, b1471 quality, b1472 organization)
  - b152 Emotional functions (b1520 appropriateness, b1521 regulation, b1522 range, b1528, b1529)
  - b156 Perceptual functions (b1560 auditory, b1561 visual, b1562 olfactory, b1563 gustatory, b1564 tactile, b1565 visuospatial)
  - b160 Thought functions (b1600 pace, b1601 form, b1602 content, b1603 control, b1608, b1609)
  - b163 Basic cognitive functions
  - b164 Higher-level cognitive functions (b1640 abstraction, b1641 organization and planning, b1642 time management, b1643 cognitive flexibility, b1644 insight, b1645 judgment, b1646 problem-solving)
  - b167 Mental functions of language (b1670 reception of language, b1671 expression, b1672 integrative)
  - b172 Calculation (b1720 simple, b1721 complex)
  - b176 Mental function of sequencing complex movements
  - b180 Experience of self and time (b1800 experience of self, b1801 body image, b1802 experience of time)
  - b189 Specific mental functions, other

**Body Functions Ch.2 Sensory and pain (b2)**: b210 Seeing, b215 Functions of structures adjoining the eye, b220 Sensations associated with eye, b230 Hearing, b235 Vestibular, b240 Sensations associated with hearing/vestibular, b250 Taste, b255 Smell, b260 Proprioceptive, b265 Touch, b270 Sensory functions related to temperature/other stimuli, b280 Pain (b2800 generalized, b2801 localized, b2802 multiple body parts, b2803 radiating).

**Body Functions Ch.6 Genitourinary and reproductive (b6)**: b610 to b679 covering urinary, sexual (b640), menstruation, procreation, sensations associated.

**Body Functions Ch.7 Neuromusculoskeletal and movement-related (b7)**: b710 to b789 mobility of joint, muscle power, muscle tone, motor reflexes, control of voluntary movement, gait, etc.

**Activities and Participation Ch.1 (Learning and applying knowledge), full enumeration**:
- d110 Watching, d115 Listening, d120 Other purposeful sensing, d130 Copying, d135 Rehearsing, d140 Learning to read, d145 Learning to write, d150 Learning to calculate, d155 Acquiring skills, d160 Focusing attention, d163 Thinking, d166 Reading, d170 Writing, d172 Calculating, d175 Solving problems, d177 Making decisions.

**Activities and Participation Ch.7 (Interpersonal interactions and relationships)**: d710 basic interpersonal interactions, d720 complex interpersonal interactions, d730 relating with strangers, d740 formal relationships, d750 informal social relationships, d760 family relationships, d770 intimate relationships.

**Strengths.** WHO authority, universal, multi-component (impairment vs activity vs participation vs environment), bilingual, used in clinical practice globally, integrates somatic + mental + social + environmental. Maps to ICD-11. Native qualifier system (0 to 4 severity).

**Limitations for Cytognosis use.**
- Granularity ceiling at 4th level. No "verbal working memory span at 3-back >= 80% accuracy" level features.
- No biomarker / circuit / molecule layer.
- The 0 to 4 qualifier is designed for clinician judgment, not for continuous-measure binning.
- No psychiatric-specific elaboration; depression / anxiety / psychosis distinctions live below the b152 level and have to be inferred.
- Update lag (annual at best, mostly stable since 2001).
- WHO commercial license required for commercial productization.

**DSM and instrument mappability.**
- DSM-5 disorders reconstruct as ICF profile vectors but not as 1:1 mapping. Depression involves b152 + b130 + b134 + b144 + b1640 + d2 + d750. Schizophrenia involves b110 + b156 + b160 + b167. ADHD involves b140 + b1304 + b164 + b147.
- WHODAS 2.0 is an operationalized subset of ICF d-chapters; it is the gold-standard ICF-based disability instrument.
- PHQ-9 items map to b1300 / b1301 / b1302 / b134 / b144 / b180 + d2; GAD-7 to b152 / b1521 / b134; PANSS to b110 / b156 / b160 / b167; MMSE / MoCA cleanly map to b110 / b114 / b140 / b144 / b163 / b164 / b167 / b172 / b176.

**Bulk download.** WHO ICF / ICD-11 unified API `https://icd.who.int/icfapi/docs` (OAuth2 free registration). HL7 Terminology service: ICF CodeSystem `https://terminology.hl7.org/CodeSystem-ICF.html` (JSON / XML / TTL, version 1.0.0 active 2022-10-11). BioPortal `https://bioportal.bioontology.org/ontologies/ICF` (OWL / RDF / CSV). OLS4 `https://www.ebi.ac.uk/ols4/ontologies/icf`. License: WHO standard, free for non-commercial; commercial requires WHO license.

**Star rating (5 best in class).** Coverage 5, Hierarchy 4, DSM-map 3, Instrument-map 4, AI-granularity 3, Openness 4, Adoption 5. **Total 28 / 35.**

**Verdict.** Layer 1 universal scaffold. Use Body Functions Ch.1 to 8 (especially Ch.1, 2, 6, 7) + Activities and Participation Ch.1 to 9. Provides WHO-authoritative top-level domains that natively span somatic + mental + sensory + functional. Slot RDoC, HiTOP, MF, HPO, SNOMED below.

### 3.2 RDoC (Research Domain Criteria, NIMH)

**Complete enumeration (6 domains, ~36 constructs and subconstructs)**:

1. **Negative Valence Systems**: Acute Threat (Fear), Potential Threat (Anxiety), Sustained Threat, Loss, Frustrative Nonreward.
2. **Positive Valence Systems**: Reward Responsiveness (Reward Anticipation, Initial Response to Reward, Reward Satiation), Reward Learning (Probabilistic and Reinforcement Learning, Reward Prediction Error, Habit-PVS), Reward Valuation (Reward Probability, Delay, Effort).
3. **Cognitive Systems**: Attention, Perception (Visual, Auditory, Olfactory / Somatosensory / Multimodal), Declarative Memory, Language, Cognitive Control (Goal Selection / Updating / Representation / Maintenance, Response Selection / Inhibition / Suppression, Performance Monitoring), Working Memory (Active Maintenance, Flexible Updating, Limited Capacity, Interference Control).
4. **Social Processes**: Affiliation and Attachment, Social Communication (Reception/Production of Facial Communication, Reception/Production of Non-Facial Communication), Perception and Understanding of Self (Agency, Self-Knowledge), Perception and Understanding of Others (Animacy Perception, Action Perception, Understanding Mental States).
5. **Arousal and Regulatory Systems**: Arousal, Circadian Rhythms, Sleep-Wakefulness.
6. **Sensorimotor Systems**: Motor Actions (Action Planning and Selection, Sensorimotor Dynamics, Initiation, Execution, Inhibition and Termination), Agency and Ownership, Habit-Sensorimotor, Innate Motor Patterns.

**Units of analysis (cross-cutting)**: Genes, Molecules, Cells, Circuits, Physiology, Behavior, Self-Reports, Paradigms.

**Hierarchical depth.** 3 levels (Domain, Construct, Subconstruct) with an 8-unit analysis dimension giving an effective rank-3 tensor.

**Strengths.** Mechanistically grounded, neuroscience-anchored, designed for continuous dimensions, multi-scale (gene to self-report). Natively supports behavioral / self-report layers. Public domain (US government work).

**Limitations.** Coarse hierarchy (no specific symptoms enumerated). No coverage of somatic, QoL, sexual, eating as behavior. No standardized item bank. No DSM crosswalk (deliberately).

**Bulk download.** Construct definitions: HTML only at `https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc/constructs`. No CSV / JSON / OWL export from NIMH. Community OWL builds exist (Hastings, Larsen et al.) but not officially endorsed. NIMH Data Archive (NDA / former RDoCdb) at `https://nda.nih.gov` with Data Use Certification.

**Star rating.** Coverage 3, Hierarchy 3, DSM-map 2, Instrument-map 3, AI-granularity 4, Openness 5, Adoption 4. **Total 24 / 35.**

**Verdict.** Layer 3a mechanistic overlay. Use RDoC + Cognitive Atlas to attach mechanism-anchored construct labels to ICF / MF / HPO / SNOMED nodes. The mechanism layer makes biomarker grounding and translational work possible.

### 3.3 HiTOP (Hierarchical Taxonomy of Psychopathology)

**Complete 6-level hierarchy**:

- **Level 6 super-spectra**: General factor of psychopathology (p-factor), Emotional Dysfunction (= Internalizing + Somatoform), Psychosis (= Thought Disorder + Detachment), Externalizing (= Disinhibited + Antagonistic).
- **Level 5 six spectra**: Internalizing, Somatoform, Disinhibited Externalizing, Antagonistic Externalizing, Thought Disorder, Detachment.
- **Level 4 sub-factors**:
  - Internalizing: Distress, Fear, Eating Pathology, Sexual Problems, Mania (provisional cross-load with Thought Disorder).
  - Somatoform: mostly direct to syndromes.
  - Disinhibited Externalizing: Substance Abuse, Antisocial Behavior, Attentional Dysregulation.
  - Antagonistic Externalizing: Aggression, Manipulativeness.
  - Thought Disorder: Reality Distortion, Disorganization, Mania (provisional), Dissociation (provisional).
  - Detachment: Inexpressivity, Avolition, Social Anhedonia.
- **Level 3 syndromes / disorders (DSM-anchored, partial list)**: MDD, dysthymia, GAD, PTSD, panic, social anxiety, agoraphobia, specific phobia, OCD, anorexia, bulimia, BED, sexual dysfunctions, somatic symptom disorder, illness anxiety, conversion, AUD / SUD, ADHD, conduct disorder, ODD, IED, antisocial PD, histrionic PD, narcissistic PD, paranoid PD, borderline PD, schizophrenia, schizoaffective, schizotypal PD, schizoid PD, avoidant PD, bipolar I/II.
- **Level 2 symptom components and maladaptive traits**:
  - Internalizing traits: emotional lability, anxiousness, separation insecurity, submissiveness, perseveration, anhedonia.
  - Disinhibited Ext traits: impulsivity, irresponsibility, distractibility, disorganization, risk-taking, low perfectionism, low workaholism.
  - Antagonistic Ext traits: manipulativeness, deceitfulness, callousness, grandiosity, aggression, rudeness, domineering, suspiciousness.
  - Detachment traits: emotional detachment, anhedonia, social withdrawal, romantic disinterest.
  - Thought Disorder traits: peculiarity, unusual beliefs, unusual experiences, fantasy proneness.
- **Level 1 symptoms / signs**: HiTOP-SR self-report and HiTOP-CRT clinician-rated items (~400 items in HiTOP-SR full battery).

**Strengths.** Empirically derived (factor-analytic), 6 hierarchical levels by construction, DSM-bridging at the syndrome level, traits + symptoms unified, growing measure ecosystem (HiTOP-SR, HiTOP-CRT, HiTOP-PAQ, HiTOP-DAT). The HiTOP-DAT (Digital Assessment Tracker) operationalizes the mapping at the item level.

**Limitations.** No somatic functioning, sleep, sensorimotor, or QoL beyond illness impact. Not designed for biomarkers. Items not LOINC-coded. Some constituent scales (PID-5 facets, IDAS-II) carry author-level copyright.

**DSM mapping.** Kotov et al. 2017 (J Abnormal Psychology 126:454 to 477) Tables 1 to 2 plus supplements provide explicit DSM-5 disorder to HiTOP spectra / sub-factor / symptom-component mapping. The HiTOP R package on CRAN bundles scoring keys that implicitly encode component memberships per item.

**Bulk download.** Working model: OSF `https://osf.io/rscqf` and `https://osf.io/8h7m6`. Measures: `https://hitop-system.org/hitop-measures` (HiTOP-SR-pro, HiTOP-CRT, HiTOP-PAQ). Stony Brook manuscript PDF. R package on CRAN.

**Star rating.** Coverage 4, Hierarchy 5, DSM-map 5, Instrument-map 5, AI-granularity 5, Openness 4, Adoption 4. **Total 32 / 35.**

**Verdict.** Layer 3b psychometric overlay (primary backbone for psychopathology dimensions and DSM reconstruction). Use the full 6-level hierarchy as the psychopathology dimensional axes. Every DSM mental disorder collapses cleanly to a HiTOP node.

### 3.4 PROMIS

**Adult item-bank inventory (29 mental health banks plus physical, social)**:

- **Mental Health**: Cognitive Function (32 items), Cognitive Function-Abilities (31), Emotional Distress-Anxiety (29), Emotional Distress-Depression (28), Emotional Distress-Anger (22), Alcohol Use (37), Alcohol Negative Consequences (31), Alcohol Negative Expectancies (11), Alcohol Positive Consequences (20), Alcohol Positive Expectancies (9), General Life Satisfaction (10), Illness Burden (27), Meaning and Purpose (37), Positive Affect (34), Positive Outlook (27), Positive Treatment Expectations (27), Psychosocial Illness Impact-Negative (32), Psychosocial Illness Impact-Positive (39), Self-Efficacy-General (10), Self-Efficacy Manage Daily Activities (35), Self-Efficacy Manage Emotions (25), Self-Efficacy Manage Meds/Treatment (26), Self-Efficacy Manage Social Interactions (23), Self-Efficacy Manage Symptoms (28), Substance Use-Appeal (18), Prescription Pain Med Misuse (22), Substance Use-Severity (37), Spirituality (26), Healthcare Access Satisfaction (44).
- **Physical Health**: Fatigue (95), Pain Interference (20), Physical Function (173), Sleep Disturbance (27), Dyspnea-Functional Limitations (33), Dyspnea-Severity (33), Itch (multiple banks), Pain Behavior (20), Physical Function-Mobility (44), Physical Function-Upper Extremity (46), Physical Function for Mobility Aid Users (114), Sexual Function and Satisfaction-Factors Interfering (35), Sleep-Related Impairment (16). SexFS adds Interest, Lubrication, Vaginal Discomfort, Erectile Function, Orgasm, Therapeutic Aids. Plus Smell and Taste, GI Symptoms, Neuropathy.
- **Social Health**: Ability to Participate in Social Roles / Activities (35), Emotional Support (16), Informational Support (10), Instrumental Support (11), Satisfaction with Participation in Discretionary Social Activities (12), Satisfaction with Participation in Social Roles (14), Companionship, Social Isolation (14).
- **Pediatric / parent-proxy** banks across the same domains.

**Strengths.** IRT-calibrated continuous theta scores (ideal for ML), item-level granularity, LOINC-coded and FHIR-ready (HL7 PCO IG), FDA-qualified for several domains, multi-language, free for research and commercial use under HealthMeasures license.

**Limitations.** No personality framework, no psychosis bank, no eating-disorder bank, no autism-specific bank. Self-report only (objective performance is NIH Toolbox).

**Bulk download.** `https://www.healthmeasures.net/explore-measurement-systems/promis/intro-to-promis` (PDF item manuals plus scoring). LOINC contains PROMIS questions with full item parameters. HL7 PCO FHIR IG. Free with attribution; HealthMeasures account required for instrument-level downloads.

**Star rating.** Coverage 4, Hierarchy 3, DSM-map 4, Instrument-map 5, AI-granularity 5, Openness 5, Adoption 5. **Total 31 / 35.**

**Verdict.** Layer 5 operational item-level layer. Use PROMIS items as the IRT-calibrated continuous measurement substrate; bind each item to the appropriate Layer 1 to 4 nodes.

### 3.5 NIH Toolbox

**Complete structure (4 batteries, ~30 measures)**:
- **Cognition**: Dimensional Change Card Sort, Face Name Associative Memory, Flanker Inhibitory Control and Attention, List Sorting Working Memory, Oral Reading Recognition, Oral Symbol Digit, Pattern Comparison Processing Speed, Picture Sequence Memory, Picture Vocabulary, Rey Auditory Verbal Learning. Composites: Total Cognition, Fluid, Crystallized.
- **Emotion**: Negative Affect (Anger sub-banks for irritability, frustration, interpersonal sensitivity, envy, disagreeableness, anger control; Fear sub-banks Fear/Anxiety, Over-Anxious, Separation Anxiety; Sadness); Psychological Well-Being (Positive Affect, General Life Satisfaction, Meaning and Purpose); Social Relationships (Emotional Support, Friendship, Loneliness, Perceived Rejection, Perceived Hostility, Instrumental Support, Companionship, Social Distress); Stress and Self-Efficacy (Self-Efficacy, Perceived Stress).
- **Motor**: 2-Minute Walk Endurance, 4-Meter Walk Gait Speed, 9-Hole Pegboard Dexterity, Grip Strength, Standing Balance.
- **Sensation**: Hearing Threshold, Words-In-Noise, Visual Acuity (Near and Distance), Odor Identification, Pain Intensity, Pain Interference, Regional Taste Intensity.

**Strengths.** Objective performance measures (not just self-report), normed across ages 3 to 85+, used in HCP / ABCD, free for research.

**Limitations.** Not a featureset taxonomy. No psychiatric symptoms, no personality, no sleep, no eating.

**Star rating.** Coverage 3, Hierarchy 3, DSM-map 2, Instrument-map 3, AI-granularity 4, Openness 4, Adoption 4. **Total 23 / 35.**

**Verdict.** Layer 5 performance-based operational measures. Pair with PROMIS to cover self-report + performance. Especially critical for cognition where self-report is unreliable.

### 3.6 PhenX Toolkit Mental Health Research

**Structure.** MHR Core (Tier 1 + Tier 2) plus 4 specialty collections (Suicide, PTSD, Eating Disorders, Early Psychosis Clinical Services, Early Psychosis Translational Research). Approximately 25 to 40 protocols across Core and specialty.

**Strengths.** Designed for harmonization across NIH studies, dbGaP integration, every protocol has standard variable definitions, items mapped to LOINC by NCATS.

**Limitations.** A menu of validated instruments rather than a unified taxonomy.

**Bulk download.** `https://www.phenxtoolkit.org/` (CSV / XML per protocol, batch via dbGaP). Free, public domain.

**Star rating.** Coverage 3, Hierarchy 3, DSM-map 5, Instrument-map 5, AI-granularity 3, Openness 5, Adoption 4. **Total 28 / 35.**

**Verdict.** Layer 5 protocol-harmonization layer. Use to pick the canonical version of each instrument and inherit its data-dictionary mapping.

### 3.7 CDISC SDTM QRS QSTESTCD union

Estimated **~15,000 to 25,000 item codes** across the 500+ QRS supplements. Item-level union spans psychiatric, neuro, cognitive, pain, QoL, sleep, substance, function instruments. Could form a featureset baseline by union, but it is not a hierarchy; you would need a concept layer on top to make it usable.

**Star rating.** Coverage 4, Hierarchy 2, DSM-map 4, Instrument-map 5, AI-granularity 4, Openness 4, Adoption 5. **Total 28 / 35.**

**Verdict.** Layer 5 regulatory / legacy compatibility. CDISC items are the bridge from your feature space into clinical trial data and FDA submission datasets. Map each QSTESTCD to a Cytognosis leaf feature.

### 3.8 Construct-framework side-by-side

| Framework | Levels | Approx. leaf nodes | Cog | Aff | Sleep | Motor | Sens | Soc | Sub | Eat | Sex | QoL | Pers | DSM | Inst | AI | Open | Adopt | TOTAL/35 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ICF | 4 | ~1,424 | 5 | 4 | 5 | 5 | 5 | 4 | 2 | 3 | 4 | 5 | 3 | 3 | 4 | 3 | 4 | 5 | 28 |
| RDoC | 3 | ~60 | 5 | 4 | 3 | 5 | 5 | 5 | 4 | 3 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 4 | 24 |
| HiTOP | 6 | ~400 items | 2 | 5 | 1 | 1 | 3 | 3 | 5 | 5 | 4 | 1 | 5 | 5 | 5 | 5 | 4 | 4 | 32 |
| PROMIS | 3 | ~2,078 items | 4 | 5 | 5 | 4 | 3 | 5 | 5 | 1 | 5 | 5 | 0 | 4 | 5 | 5 | 5 | 5 | 31 |
| NIH Toolbox | 3 | ~30 measures | 5 | 4 | 0 | 5 | 4 | 4 | 0 | 0 | 0 | 3 | 0 | 2 | 3 | 4 | 4 | 4 | 23 |
| PhenX MHR | 3 | ~40 protocols | 3 | 5 | 2 | 2 | 1 | 4 | 5 | 5 | 1 | 4 | 1 | 5 | 5 | 3 | 5 | 4 | 28 |
| Cognitive Atlas | 5+ | 918 concepts | 5 | 2 | 1 | 4 | 5 | 4 | 1 | 0 | 0 | 0 | 1 | 2 | 2 | 5 | 5 | 3 | 24 |
| CDISC QRS | 2 to 3 | ~20k QSTESTCDs | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 3 | 1 | 5 | 0 | 4 | 5 | 4 | 4 | 5 | 28 |

HiTOP scores highest (32). PROMIS (31) and the ICF / PhenX / CDISC tier (28 each) are close. RDoC (24), NIH Toolbox (23), Cognitive Atlas (24) trail because they are not designed as universal feature spaces.

---

## 4. Recommended Cytognosis Feature Space Architecture

### 4.1 The six-layer stack

```
Layer 0 (metamodel)          : OGMS + IAO + BFO
                               Defines the kinds: process, disposition, quality,
                               finding, disorder, measurement, information artifact.

Layer 1 (universal scaffold) : ICF Body Functions Ch.1, 2, 6, 7 + Activities and
                               Participation Ch.1, 2, 3, 7, 8, 9.
                               WHO-authoritative top-level domains spanning somatic +
                               mental + sensory + functional in one taxonomy.
                               ~150 stable categories. Severity qualifier (0 to 4).

Layer 2 (upper mental scaffold): MF + MFOEM (process / disposition / quality /
                               appraisal / mood / emotion).
                               Philosophically-grounded type distinctions.
                               ~1,024 terms. Sits inside ICF mental and sensory chapters.

Layer 3 (mid construct overlay):
   3a Mechanistic            : RDoC + Cognitive Atlas + CogPO
                               ~36 RDoC constructs/subconstructs +
                               918 cognitive concepts + ~800 task paradigms.
                               Mechanism-anchored construct labels. Multi-scale
                               (Genes, Molecules, Cells, Circuits, Physiology,
                               Behavior, Self-Reports, Paradigms).
   3b Psychometric           : HiTOP (6 levels: super-spectra, spectra, sub-factors,
                               syndromes, symptom components/maladaptive traits,
                               items).
                               ~400 items in HiTOP-SR. Best DSM reconstruction.

Layer 4 (clinical leaves)    : HPO HP:0000707 + HP:0000708 + HP:0000709 + HP:0100543
                               (~700 to 1,000 terms; monthly refresh, SSSOM bridges)
                               + SNOMED CT 384821006 + 74732009 subtrees
                               (~6,000 to 8,000 concepts; first-class severity and
                               temporal context)
                               + MONDO disease anchors
                               + UMLS CUI bridge to ICD-10-CM, ICD-11, DSM-5, MeSH,
                               MedDRA, LOINC, RxNorm.

Layer 5 (operational items)  : PROMIS item banks (~2,078 IRT-calibrated items across
                               ~127 banks) + NIH Toolbox (~30 performance measures)
                               + CDISC QSTESTCD items (~20,000) + PhenX MHR protocols
                               + LOINC question codes + Answer Lists.
```

### 4.2 Per-feature identifier tuple

Every Cytognosis feature carries a five-tuple identifier:

```
{
  "cytognosis_id"   : "CYTO:0001234",                    # internal stable ID
  "label"           : "Anhedonia",
  "icf_code"        : "b1522",                            # ICF Specific mental functions / Range of emotion
  "mf_class"        : "MF:0000099",                       # Mental Functioning Ontology class
  "rdoc_construct"  : "Positive Valence / Reward Responsiveness / Initial Response to Reward (deficit)",
  "hitop_node"      : "Internalizing > Distress > Depression > Anhedonia (symptom component)",
  "hpo_id"          : "HP:0000718",                       # Anhedonia
  "snomed_id"       : "84379007",                          # Anhedonia (finding)
  "umls_cui"        : "C0392133",
  "mondo_xref"      : null,                                # phenotype, not a disease
  "operational_bindings": {
    "promis_item_id": "PROMIS-Depression-04",
    "loinc_panel"   : "44249-1",
    "loinc_item"    : "44250-9",
    "loinc_answers" : "LL358-3",
    "cdisc_qstestcd": "PHQ0101",
    "phenx_protocol": "PhenX:121601",
    "nih_toolbox"   : null,
    "hitop_sr_item" : "HiTOP-SR-DEP-04"
  },
  "parents"         : ["CYTO:0001000"],                    # zoomable hierarchy
  "depth"           : 5,
  "modality"        : ["self_report", "clinician_rated", "language_signal"],
  "severity_scale"  : "ordinal_0_4"
}
```

This tuple gives every feature:
- A WHO-authoritative scaffolding (ICF).
- A formal upper-level type (MF / MFOEM).
- A mechanistic anchor (RDoC, Cognitive Atlas).
- A psychometric anchor (HiTOP).
- A clinical anchor (HPO, SNOMED, MONDO, UMLS).
- Operational bindings to existing measurement instruments.
- A parent in the Cytognosis hierarchy so models can zoom.

### 4.3 Top-level domain proposal (16 domains plus 12 cross-cutting axes)

Top-level mental domains (organized by ICF):

1. **Consciousness and arousal** (ICF b110 + RDoC Arousal): vigilance, sustained attention to environment, dissociation.
2. **Orientation and insight** (ICF b114 + ICF b1644): time / place / person orientation, insight, judgment.
3. **Intellectual / general cognitive ability** (ICF b117 + Cognitive Atlas g-factor): crystallized vs fluid.
4. **Attention** (ICF b140 + RDoC Cognitive Systems / Attention): sustained, shifting, divided, selective. Operationalized by NIH Toolbox Flanker, DCCS, plus PROMIS Cognitive Function.
5. **Memory** (ICF b144 + RDoC Declarative + Working Memory): episodic, semantic, working, procedural.
6. **Executive function** (ICF b164 + RDoC Cognitive Control): planning, organization, cognitive flexibility, inhibition, problem-solving.
7. **Language** (ICF b167 + RDoC Cognitive Systems / Language): receptive, expressive, integrative, prosody, pragmatics.
8. **Perception** (ICF b156 + b2 + RDoC Perception + Sensorimotor): visual, auditory, olfactory, gustatory, somatosensory, multimodal; perceptual distortions (hallucinations).
9. **Thought** (ICF b160 + HiTOP Thought Disorder): pace, form (disorganization), content (delusions, obsessions), control (intrusions).
10. **Emotional functions** (ICF b152 + HiTOP Internalizing + RDoC NVS / PVS): appropriateness, regulation, range; specific affects: fear, anxiety, sadness, loss, anger, anhedonia, positive affect, irritability.
11. **Energy and drive** (ICF b130 + RDoC PVS): energy level, motivation, appetite, craving, impulse control.
12. **Sleep** (ICF b134 + RDoC Sleep-Wake / Circadian): amount, onset, maintenance, quality, cycle, sleep-related impairment.
13. **Psychomotor and motor** (ICF b147 + b7 + RDoC Sensorimotor): psychomotor agitation / retardation, motor planning, execution, gait, dexterity, strength, balance.
14. **Self and identity** (ICF b180 + RDoC Social Processes / Self): experience of self, body image, time, agency, dissociation.
15. **Social cognition and behavior** (ICF b122 + d7 + RDoC Social Processes + HiTOP Detachment / Antagonism): affiliation, theory of mind, social communication, interpersonal interactions, family / peer relationships.
16. **Personality traits** (ICF b126 + HiTOP traits): negative affectivity, detachment, antagonism, disinhibition, psychoticism, anankastia; plus normal-range Big Five.

Cross-cutting vertical axes (mapped to ICF d-component + PROMIS Social / Physical):

- A. Activities of daily living (ICF d4, d5, d6).
- B. Communication participation (ICF d3).
- C. Interpersonal and relational functioning (ICF d7).
- D. Work / education / economic participation (ICF d8).
- E. Community / civic participation (ICF d9).
- F. Quality of life and subjective well-being (PROMIS Meaning and Purpose, Positive Affect, Life Satisfaction).
- G. Substance use behavior (HiTOP Dis-Ext / Substance + PROMIS Substance Use).
- H. Eating behavior (HiTOP Internalizing / Eating Pathology + EDE-Q items).
- I. Sexual function and behavior (ICF b640 + PROMIS SexFS + ASEX).
- J. Suicidality (HiTOP cross-cut + C-SSRS).
- K. Aggression and antisocial (HiTOP Antagonistic / Disinhibited Ext).
- L. Somatic symptoms (HiTOP Somatoform + PROMIS Physical).

Feature space dimensionality: 16 mental domains x ~3 to 7 sub-constructs each x ~3 to 10 item-level features each = approximately **800 to 1,500 leaf features** at the most granular layer, organized into a 6-level hierarchy (super-domain, domain, sub-construct, facet, item-cluster, item).

### 4.4 Why not "union of CDISC QSTESTCDs" as the featureset

You floated this as a possibility. Honest take:
- The CDISC QSTESTCD union is rich (~20,000 items) and operational, but it is a **flat list** without a hierarchy.
- Items overlap heavily across instruments (PHQ-9 anhedonia ~ HiTOP-SR anhedonia ~ PROMIS-Depression anhedonia ~ BDI-II anhedonia ~ MADRS lassitude).
- Many items are copyrighted at the wording level, so the verbatim text is not always publicly reproducible.
- Without a concept layer above, you cannot do construct-level reasoning, severity calibration, or DSM reconstruction.

Therefore: use the CDISC QSTESTCD union as **Layer 5 operational bindings**, not as the feature space itself. The Cytognosis feature space sits above the items; many items bind to the same feature; that is the harmonization mechanism.

### 4.5 Architecture diagram

```
                 +-------------------------------------------+
                 |     Cytognosis feature ID (CYTO:xxxxx)     |
                 +-------------------------------------------+
                                     |
              +----------------------+----------------------+
              |                                             |
   +----------v---------+                       +-----------v-----------+
   | Layer 1 ICF code   |                       | Layer 2 MF / MFOEM    |
   +--------------------+                       +-----------------------+
              |                                             |
              v                                             v
   +-----------------------+                  +----------------------------+
   | Layer 3a RDoC + CogAt |  <-- cross-link  | Layer 3b HiTOP node        |
   +-----------------------+                  +----------------------------+
              |                                             |
              v                                             v
   +-----------------------+                  +----------------------------+
   | Layer 4 HPO+SNOMED+   |  <-- bridges --> | DSM-5-TR, ICD-10-CM,       |
   | UMLS+MONDO clinical   |                  | ICD-11 diagnostic codes    |
   +-----------------------+                  +----------------------------+
              |
              v
   +-----------------------------------------------+
   | Layer 5 Operational bindings                  |
   |  - PROMIS item ID  (IRT-calibrated)           |
   |  - NIH Toolbox measure                        |
   |  - CDISC QSTESTCD  (regulatory)               |
   |  - LOINC question + Answer List               |
   |  - PhenX protocol ID                          |
   |  - HiTOP-SR / HiTOP-CRT item                  |
   |  - Language-signal model (Cytoscope sensor)   |
   +-----------------------------------------------+
```

---

## 5. Instrument and Test to Feature Mapping (Problem 2)

### 5.1 Approach

Instead of starting from questions (which leads to a 20,000-item flat list), start from features and bind instruments to them. Algorithm:

1. For each Cytognosis feature, enumerate every operational binding that probes it.
2. For each operational binding, capture the item text (if licensed for use), the response options, the LOINC item code, and the QSTESTCD.
3. When a binding probes multiple features, list all features (most items probe more than one; that is fine).

This produces an inverted index: feature -> set of bindings, which is much more useful than the forward index instrument -> set of items.

### 5.2 Worked example: feature "anhedonia"

Cytognosis ID `CYTO:0001234`. ICF b1522 (range of emotion, with reduced positive emotion). MF "lack of positive appraisal". RDoC Positive Valence / Reward Responsiveness. HiTOP Internalizing / Distress / Depression / Anhedonia. HPO:0000718 Anhedonia. SNOMED 84379007 Anhedonia. UMLS C0392133. MONDO null (phenotype, not disorder).

Operational bindings:

| Binding | Item text (where public) | LOINC | QSTESTCD |
|---|---|---|---|
| PHQ-9 Q1 | "Little interest or pleasure in doing things" | 44250-9 | PHQ0101 |
| PHQ-2 Q1 | (same as PHQ-9 Q1) | 44250-9 | PHQ2-01 |
| HAM-D17 Q7 | "Work and activities" (loss of interest) | reg | HAMD1707 |
| MADRS Q8 | "Inability to feel" | reg | MADRS08 |
| BDI-II Q4 | Loss of pleasure (proprietary) | n/a | n/a |
| PROMIS Depression items | "I felt no interest in doing things I usually like to do", etc. | LOINC PROMIS items | n/a |
| HiTOP-SR Internalizing items | (anhedonia component) | n/a | n/a |
| SHAPS (Snaith-Hamilton Pleasure Scale) | full 14-item battery | reg | SHAPS-01 to 14 |
| PROMIS Positive Affect (reverse) | "I felt cheerful" (reverse-keyed) | LOINC PROMIS-PA | n/a |
| Cytoscope language signal | language model "anhedonia signal" classifier | n/a | n/a |

Severity calibration: PHQ-9 Q1 score 0 to 3, MADRS Q8 score 0 to 6, PROMIS theta IRT, SHAPS dichotomous. Use PROsetta Stone to anchor PHQ-9 to PROMIS T-score (free).

### 5.3 Bootstrapping the inverted index

You can build the initial inverted index by combining:
- HiTOP-SR-pro / HiTOP-CRT manuals (which already enumerate items per component).
- PROMIS LOINC bindings (each PROMIS item has a LOINC code).
- CDISC supplements (which provide QSTESTCD per item).
- LOINC SNOMED Cooperation expressions (which bridge LOINC items to SNOMED findings).
- HPO `hp.sssom.tsv` (which bridges HPO to SNOMED, UMLS, ICD-10).
- PROsetta Stone (which bridges legacy raw scores to PROMIS T-scores).

For instruments where no public crosswalk exists (BDI-II, BAI, PANSS, MoCA item text, MMSE item text), bind at the binding-level identifier only (instrument-item identifier) without verbatim text; the operational binding still works.

### 5.4 Instrument coverage plan

Tier 1 (deep mapping, public-domain core, public LOINC, machine-readable):
- PHQ-9 / 2 / 8 / 15, GAD-7, MADRS, HAM-D, HAM-A, YMRS, BPRS-18, AIMS, PCL-5, EPDS, ASRS, AUDIT, AUDIT-C, DUDIT, SNAP-IV, CGI-S, CGI-I, C-SSRS (free for non-commercial), ECOG, KPS, WHODAS 2.0, WHOQOL-BREF.

Tier 2 (licensed but trial-standard, structural-only mapping unless license obtained):
- PANSS, MoCA, MMSE, BDI-II, BAI, SF-36 / SF-12, EQ-5D-3L / 5L, Conners, ISI, PSQI, Y-BOCS, ESRS.

Tier 3 (PROMIS item banks as the IRT-calibrated substrate):
- All ~127 PROMIS adult and pediatric banks (full item text licensed under HealthMeasures).

Tier 4 (objective performance, paired with self-report):
- All NIH Toolbox Cognition, Emotion, Motor, Sensation measures.

Tier 5 (HiTOP-SR and HiTOP-CRT items):
- ~400 self-report items mapped to symptom components.

Tier 6 (PhenX harmonization layer):
- Adopt PhenX-recommended canonical version of each instrument; inherit data-dictionary mapping.

### 5.5 Continuous monitoring (Cytoscope guardian agent)

For language-based continuous tracking, the agent need not call legacy instruments. It can score utterances directly against the Cytognosis feature space using:

- **Zero-shot construct classifiers** anchored to HiTOP-SR item text plus PROMIS item text plus public-domain CDISC QSTEST labels (those that are public-domain). For each feature, the classifier prompt cites the HiTOP item, the PROMIS item, and the CDISC label as exemplars.
- **RDoC-paradigm-derived linguistic markers**, drawing on the published RDoC behavioral assessment methods compendium (NIMH 2016) which lists known behavioral indicators per construct.
- **ICF qualifier severity binning** (0 to 4) per feature per rolling time window. The qualifier scale gives a natural quantization (0 no problem, 1 mild, 2 moderate, 3 severe, 4 complete) usable as a categorical output even when the underlying signal is continuous.
- **Item-equivalent scoring**: when an utterance contains content equivalent to a PHQ-9 item, score the equivalent PROMIS theta and store as a passive observation.

This decouples the agent from depending on the user actually completing an instrument; the agent's output is a feature-vector time series.

---

## 6. Diagnostic Mapping (Problem 3): DSM-5-TR and ICD-11 onto Features

### 6.1 What UMLS already gives you

UMLS Metathesaurus (SAB `DSM5`) ingests **DSM-5 disorder labels and codes only**. It does **not** ingest:
- Criterion-level decomposition (A1, A2, B, etc.).
- Symptom / feature text from criteria.
- Specifier / severity modifiers as machine-readable concepts.
- Decision trees, inclusion / exclusion logic.

Term types you should expect for `SAB='DSM5'` are `PT` (preferred term, the disorder name) and `HT`/`HC` (hierarchy headings). The cross-walks to ICD-9-CM and ICD-10-CM that DSM-5 prints in its tables are reproduced via UMLS CUI co-occurrence (`MRREL.RRF`).

DSM-5-TR Update Supplement (September 2025 PDF, free from `https://www.psychiatry.org/getmedia/b68a5776-f88c-45c7-9535-fd219d7aa5cb/APA-DSM5TR-Update-September-2025.pdf`) is the only structured artifact APA distributes openly, and it is text and PDF only.

**Implication**: you must hand-curate the DSM-5 criterion-level decomposition. There is no canonical machine-readable source.

### 6.2 ICD-10-CM / ICD-11 mapping infrastructure

- **ICD-10-CM to SNOMED CT (I-MAGIC)**: maps ~95%+ of ICD-10-CM to SNOMED CT, distributed in the SNOMED CT US Edition RF2 reference set; exposed in UMLS via `MRMAP.RRF` with `MAPSETSAB='SNOMEDCT_US'`. Quarterly refresh.
- **ICD-11 MMS to ICD-10**: WHO publishes spreadsheet equivalence tables in the ICD-11 download area `https://icd.who.int/dev11/downloads`.
- **ICD-11 MMS to SNOMED CT**: no official map yet. SNOMED International has a partial reference set for a subset of MMS stem codes; coverage <30% of MMS as of May 2026.
- **Mental and behavioural chapter in ICD-11**: Chapter 06 at `https://icd.who.int/browse/2026-01/mms/en`.

### 6.3 DSM-5 to HiTOP (the cleanest published bridge)

Kotov et al. 2017 (J Abnormal Psychology 126:454 to 477), Tables 1 and 2 plus supplements, give explicit DSM-5 disorder to HiTOP spectra / sub-factor / symptom-component mapping. The HiTOP consortium maintains this via the HiTOP-DAT and the HiTOP R package.

This is the recommended primary bridge: **DSM-5-TR disorder -> HiTOP syndrome (Level 3) -> HiTOP symptom components (Level 2) -> HiTOP items (Level 1) -> Cytognosis features (via Layer 3b binding)**.

### 6.4 DSM-5 to RDoC

No canonical map. Closest authoritative sources:
- Cuthbert 2014 World Psychiatry 13:28 to 35 (conceptual transition framework).
- Clark, Cuthbert, Lewis-Fernandez, Narrow, Reed 2017 PSPI 18:72 to 145 (compares ICD-11, DSM-5, RDoC in prose).
- Lahey et al. 2022 (mini-RDoC quantitative confirmatory factor mapping on selected constructs).

Bridge construction: link each DSM criterion to a measure (PHQ-9 item, etc.), and link the measure to RDoC via published Behavioral Assessment Methods Reports plus HiTOP measure rosters.

### 6.5 DSM to HPO

`phenotype.hpoa` is rare-Mendelian-heavy. Coverage for DSM disorders:
- Schizophrenia (MONDO:0005090): ~5 to 10 HPO terms.
- Bipolar (MONDO:0004985): ~5 to 8.
- ASD (MONDO:0005258): dozens (genetic / syndromic overlap).
- MDD (MONDO:0002050): minimal.
- ADHD, OCD, PTSD: very thin.

Monarch and Charite flagged psychiatric phenotype coverage as a known gap since 2023.

### 6.6 DSM to SNOMED CT

No published DSM crosswalk per se. The SNOMED mental disorder hierarchy (74732009) and mental state finding hierarchy together approximately span DSM-5-TR. Bridge through UMLS CUI sharing: `DSM5` CUI <-> `SNOMEDCT_US` CUI.

### 6.7 OMOP CDM Survey domain

OHDSI Athena exposes psychiatric content through:
- `SNOMED` (primary Condition vocabulary, all mental disorders standard).
- `ICD10CM`, `ICD10`, `ICD9CM` (source, non-standard, with `concept_relationship` "Maps to" to SNOMED).
- `LOINC` (survey instruments and items; PHQ-9 total 44261-6, GAD-7 70274-6).
- `PPI` (All of Us Participant Provided Information; custom AoU survey codes including PHQ-9 / PHQ-2 variant).
- `Question` / `Answer` (generic OMOP survey).
- DSM-5 is **not** an OMOP standard vocabulary; psychiatric diagnoses live in SNOMED.

Athena distributes as CSV bundle (CONCEPT.csv, CONCEPT_RELATIONSHIP.csv, CONCEPT_ANCESTOR.csv, CONCEPT_SYNONYM.csv, VOCABULARY.csv, DOMAIN.csv, CONCEPT_CLASS.csv). Free with UMLS registration for SNOMED-containing bundles.

### 6.8 Recommended DSM and ICD bridge build

Construct a curated bridge table with the following columns:

```
diagnosis_code, system, label, hitop_node, rdoc_constructs[],
icf_codes[], cytognosis_features_required[], cytognosis_features_supportive[],
criterion_text_summary, criterion_decomposition[], snomed_id, mondo_id,
icd10cm_code, icd11_mms_code, dsm5tr_code, umls_cui
```

For each row:
- `hitop_node` from Kotov et al. 2017 tables.
- `rdoc_constructs[]` from hand curation (NIMH BAMM as source).
- `icf_codes[]` from hand curation.
- `cytognosis_features_required[]` lists feature IDs whose presence is needed for the diagnosis (e.g., for MDD: depressed_mood OR anhedonia plus >=4 supportive features per the A criterion).
- `criterion_decomposition[]` lists DSM criteria (A1, A2, B, etc.) and their text summary (not verbatim, to avoid APA copyright).
- The other identifiers anchor the row in existing graphs.

This table is the operational bridge for problem 3. It needs to be built once and curated as DSM-5-TR receives text revisions.

### 6.9 ICF in UMLS, coverage assessment

UMLS includes ICF with SAB `ICF`. ~1,400 to 1,500 CUIs reproduce the full ICF classification (chapters, blocks, categories, 2nd to 4th levels) but **not the qualifier system** (the 0 to 4 severity digits are not separate CUIs). The 2025AB release notes ICF as stable / unchanged.

UMLS ICF concepts share CUIs with SNOMED CT findings where overlap exists (ICF b110 Consciousness functions <-> SNOMED 311008 Consciousness).

UMLS ICF reproduces the 2001 published ICF + 2015 update + minor 2017 revisions. It does **not** include ICF-CY (Children and Youth, 2007 derivative) nor the qualifier system as structured values.

WHO is migrating ICF into ICD-11 Foundation; the Foundation-component ICF (`icd.who.int/dev11/l-icf`) has richer relationships than the UMLS snapshot.

Verdict: UMLS ICF is good for instrument-level mapping and as the LOINC / SNOMED bridge anchor. For richer relationship semantics, ingest the WHO Foundation ICF directly via ICD-11 API.

---

## 7. Bulk Download Inventory

All sizes and URLs reflect May 2026 state. UMLS license = NIH UMLS Metathesaurus License (free, registration via UTS). Public domain = US government work.

| # | Resource | Download URL | Format | License | Approx size | Cadence | Auth |
|---|---|---|---|---|---|---|---|
| 1 | UMLS Metathesaurus full (MRCONSO, MRSTY, MRREL, MRMAP, MRDEF, MRSAB, MRHIER) | `https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html` | RRF pipe-delim, SQL scripts | UMLS click-through | ~30 GB zip, ~80 GB unpacked | Biannual (May AA, Nov AB) | UTS account |
| 2 | UMLS Semantic Network | `https://www.nlm.nih.gov/research/umls/knowledge_sources/semantic_network/` | TXT, RDF | UMLS | <5 MB | Biannual | UTS |
| 3 | SNOMED CT International Edition | `https://mlds.ihtsdotools.org` | RF2 snapshot / delta / full | SNOMED Affiliate (free via UMLS for US) | ~3 GB zip | Monthly since 2025 | UMLS + MLDS |
| 3b | SNOMED CT US Edition | `https://www.nlm.nih.gov/healthit/snomedct/us_edition.html` | RF2 | UMLS | ~4 GB zip | March + September | UTS |
| 4 | ICD-10-CM FY2026 | `https://www.cms.gov/medicare/coding-billing/icd-10-codes` (and NBER mirror) | XML, fixed-width TXT, PDF | Public domain | ~25 MB | Annual (October) | None |
| 5 | ICD-11 MMS linearization spreadsheets | `https://icd.who.int/dev11/downloads` | XLSX, TSV, PDF | WHO (free non-commercial) | ~50 MB per linearization | Annual stable (Feb), continuous Foundation | None for files; OAuth for API |
| 5b | ICD-11 + ICF API + offline Docker | `https://icd.who.int/icdapi` | JSON, FHIR (prerelease) | WHO | Docker ~2 GB | Real-time | OAuth2 |
| 6 | ICF | `https://icd.who.int/dev11/downloads` (ICF linearization) and HL7 THO CodeSystem-ICF | XLSX, FHIR JSON/XML/TTL | WHO | ~5 MB | Annual | None |
| 7 | HPO releases | `https://github.com/obophenotype/human-phenotype-ontology/releases` | OBO, OWL, JSON, SSSOM TSV | CC BY 4.0 | hp.json ~70 MB, hp.owl ~120 MB | ~6 weeks | None |
| 8 | HPO phenotype.hpoa | `https://hpo.jax.org/data/annotations` | TSV 12-column | CC BY 4.0 | ~30 MB | Monthly | None for HPOA; OMIM key for mim2gene |
| 9 | MONDO | `https://github.com/monarch-initiative/mondo/releases` | OBO, OWL, JSON, SSSOM TSV | CC BY 4.0 | mondo.owl ~200 MB | Monthly | None |
| 10 | DOID | `https://github.com/DiseaseOntology/HumanDiseaseOntology/releases` | OBO, OWL, JSON, OBO-graph | CC0 | doid.owl ~25 MB | Monthly | None |
| 11 | LOINC | `https://loinc.org/downloads/` | CSV (Loinc.csv, LoincTableCore.csv, MapTo.csv), JSON/FHIR | LOINC license (CC BY style) | 85 MB main zip | Biannual (Feb, Aug) | Free LOINC account |
| 12 | LOINC FHIR terminology server | `https://fhir.loinc.org` | FHIR CodeSystem, ValueSet, ConceptMap | LOINC license | API | Continuous | LOINC account |
| 13 | RxNorm | `https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html` | RRF, Prescribable subset | UMLS | ~2 GB | Monthly (1st Mon), weekly delta | UTS |
| 14 | CDISC QRS Supplements | `https://www.cdisc.org/standards/foundational/qrs` and CDISC Library API | Define-XML, annotated CRF PDF, Excel | Free after registration; per-instrument copyright varies | <50 MB per instrument | When new instruments added | CDISC Library account (free for nonprofits) |
| 15 | CDISC Controlled Terminology | `https://evs.nci.nih.gov/ftp1/CDISC/` | Excel, txt, OWL, ODM | Public domain (US NCI distribution) | ~200 MB total | Quarterly | None |
| 16 | NCI Thesaurus (NCIt) | `https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/` | OWL, Flat TXT, OBO | NCI EVS Terms of Use | ~500 MB | Monthly | None |
| 17 | PROMIS item banks + calibrations | `https://www.healthmeasures.net` | PDF, Excel calibrations, scoring manuals | Free with attribution | per-bank 1 to 10 MB | When recalibrated | HealthMeasures account |
| 18 | PROsetta Stone crosswalks | `http://www.prosettastone.org` | PDF tables + Excel score conversions | Free, attribution | <50 MB | When new study completes | None |
| 19 | NIH Toolbox | `https://www.healthmeasures.net` (Toolbox section) + iPad app | PDF manuals, partial item-level via licensed API | Toolbox-specific (free for research, attribution) | varies | When recalibrated | HealthMeasures account |
| 20 | PhenX Toolkit | `https://www.phenxtoolkit.org/resources/download` | CSV data dictionary, RTF, REDCap zip, Excel | CC BY (NIH funding citation) | ~100 MB full bundle | Quarterly | None |
| 21 | NIH CDE Repository | `https://cde.nlm.nih.gov` | JSON via REST API, FHIR Questionnaire export, CSV bulk via search | Public domain (HHS) | per CDE; full >1 GB | Continuous | None for read |
| 22 | RDoC matrix + constructs | `https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc` | HTML only (no structured export from NIMH); third-party OWL via Hastings et al. | Public domain (US govt) | <1 MB | Sporadic | None |
| 23 | HiTOP measures and rubrics | `https://www.hitop-system.org/hitop-measures` + HiTOP R package on CRAN | PDF, R package with scoring keys | HiTOP consortium permits research use | <50 MB | When new measures field | None |
| 24 | DSM-5 / DSM-5-TR | `https://www.appi.org` and `https://www.psychiatry.org` | Print books; PsychiatryOnline subscription; only DSM-5-TR Update Supplement PDF free | APA copyright; no machine-readable dataset | n/a | Periodic | Paid subscription for full text |
| 25 | OHDSI Athena vocabularies | `https://athena.ohdsi.org` (bundle build) | CSV (CONCEPT, CONCEPT_RELATIONSHIP, CONCEPT_ANCESTOR, etc.) | Per source vocab (SNOMED needs UMLS) | ~3 to 8 GB | Semiannual | Free Athena account; UMLS for SNOMED |
| 26 | OBO Foundry full ontology archive | `https://obofoundry.org/registry/ontologies.yml` plus per-ontology PURLs | YAML + OWL/OBO/JSON | Per ontology (mostly CC BY 4.0 or CC0) | TB scale if exhaustive | Per ontology | None |
| 27 | OLS4 | `https://www.ebi.ac.uk/ols4/api` | OWL, OBO, JSON via API | Per ontology | API | Continuous | None |
| 28 | Wikidata psychiatric concepts | `https://query.wikidata.org/sparql` + dumps `https://dumps.wikimedia.org/wikidatawiki/entities/` | SPARQL, full JSON dump | CC0 | Full dump ~120 GB, psych subset <1 GB | Continuous; weekly dumps | None |
| 29 | NIDA CTN CDE | `https://cde.nida.nih.gov` and `https://ctnlibrary.org/ctn-cde/` | PDF, CSV listing, NIH CDE integration | Public domain | <100 MB | Quarterly | None |
| 30 | NIMH NDA (former RDoCdb) | `https://nda.nih.gov` | CSV, S3 after DUC | Data Use Certification required | Multi-TB | Continuous | NDA account + DUC |
| 31 | All of Us PRO instruments | `https://www.researchallofus.org/data-tools/survey-explorer/` | PDF codebooks, CSV PPI via Athena / Workbench | Public for codebooks | <50 MB codebooks | When new surveys field | Free for codebooks; Workbench for data |
| 32 | VSAC psychiatric value sets | `https://vsac.nlm.nih.gov` + FHIR `https://cts.nlm.nih.gov/fhir` | Excel, XML, SVS, FHIR JSON | UMLS | per value set; full ~500 MB | Continuous | UTS |
| 33 | HL7 FHIR Questionnaire IGs (PCO IG, US Core, eCR) | `https://build.fhir.org` + `http://hl7.org/fhir/us/pco` | FHIR JSON / XML / TTL | HL7 license (free) | per IG 10 to 100 MB | Continuous balloting | None |
| 34 | WHO QualityRights toolkit | `https://www.who.int/publications/i/item/9789241548410` | PDF | WHO (free with attribution) | ~20 MB | Sporadic | None |
| 35 | Cognitive Atlas | `http://www.cognitiveatlas.org/api/v-alpha` + Python wrapper `https://github.com/CognitiveAtlas/cogat-python` | JSON via REST, OWL/RDF dump | CC BY-SA | API; OWL ~10 MB | Continuous | None |
| 36 | MF / MFOEM | `http://purl.obolibrary.org/obo/MF.owl` and `https://github.com/jannahastings/mental-functioning-ontology` | OWL | CC BY 4.0 | <50 MB | Sporadic | None |
| 37 | NBO | `http://purl.obolibrary.org/obo/nbo.owl` and `https://github.com/obo-behavior/behavior-ontology` | OWL, OBO, JSON | CC BY 4.0 | <30 MB | ~Annual (last 2023) | None |
| 38 | OGMS + IAO + BFO | `http://purl.obolibrary.org/obo/ogms.owl`, `http://purl.obolibrary.org/obo/iao.owl`, `http://purl.obolibrary.org/obo/bfo.owl` | OWL | CC BY | <5 MB each | Sporadic | None |
| 39 | CogPO | `https://bioportal.bioontology.org/ontologies/COGPO/download` | OWL | CC BY | ~1 MB | Stale (2013 base) | BioPortal account |
| 40 | SYMP | `http://purl.obolibrary.org/obo/symp.owl` | OWL | CC BY | ~1 MB | Annual | None |

### Notes on bulk-download operations

- **One UTS account** suffices for UMLS, SNOMED CT US Edition, RxNorm, VSAC.
- **Stable canonical URLs**: HPO, MONDO, DOID, MF, MFOEM, NBO, OGMS, IAO, BFO, SYMP resolve at `http://purl.obolibrary.org/obo/<id>.owl` (PURL). Wire ingestion to PURLs; rebuilds happen via webhook.
- **Refresh automation**: HPO, MONDO, LOINC, SNOMED, RxNorm, NCIt all publish stable URL patterns that resolve to latest. UMLS follows a predictable AA (May) and AB (November) cycle.
- **Broken URLs as of May 2026**: NLM `/research/umls/sourcereleasedocs/current/DSM5/` and `/research/umls/mapping_projects/icd10cm_to_snomedct.html` return 404; content moved under `/healthit/snomedct/us_edition.html` and `/research/umls/knowledge_sources/metathesaurus/`. Add a weekly URL-canary check.

---

## 8. Cypher Query Templates for the Neo4j Graph

These templates assume the standard UMLS-style ingestion pattern where nodes are labelled `:Concept` carrying properties `cui`, `code`, `sab`, `tty`, `str`, with relationships `:PAR/:CHD` for UMLS hierarchy, `:RB/:RN` for broader/narrower, `:HAS_SEMANTIC_TYPE` to a `:SemanticType {tui}` node, and OLS4-imported OBO nodes carrying `obo_id`. Adjust label and property names to your actual schema.

### 8.1 Pull entire HPO behavioral subtree

```cypher
// All HPO descendants of HP:0000708 plus cognitive sister branch HP:0100543
MATCH (root:Concept {sab:'HPO'})
WHERE root.obo_id IN ['HP:0000707','HP:0000708','HP:0000709','HP:0100543']
MATCH (root)<-[:PAR*0..15]-(d:Concept {sab:'HPO'})
RETURN DISTINCT d.obo_id AS hpo_id, d.str AS label, d.cui AS cui,
       size((d)<-[:PAR]-()) AS num_children;
```

### 8.2 Pull SNOMED mental state and disorder subtrees

```cypher
// SNOMED Mental state, behavior, psychosocial subtree
MATCH (root:Concept {code:'384821006', sab:'SNOMEDCT_US'})
MATCH (root)<-[:PAR*0..20]-(d:Concept {sab:'SNOMEDCT_US'})
RETURN DISTINCT d.code AS sctid, d.str AS label, d.cui AS cui;

// SNOMED Mental disorder subtree
MATCH (root:Concept {code:'74732009', sab:'SNOMEDCT_US'})
MATCH (root)<-[:PAR*0..20]-(d:Concept {sab:'SNOMEDCT_US'})
RETURN DISTINCT d.code, d.str, d.cui;
```

### 8.3 All CUIs with neurobehavioral semantic types

```cypher
MATCH (c:Concept)-[:HAS_SEMANTIC_TYPE]->(st:SemanticType)
WHERE st.tui IN ['T041','T048','T053','T054','T055','T184']
RETURN DISTINCT c.cui, c.str, collect(DISTINCT st.tui) AS tuis,
       collect(DISTINCT c.sab) AS sources
LIMIT 50000;
```

### 8.4 Bridge SNOMED clinical leaves to HPO via CUI

```cypher
MATCH (sct:Concept {sab:'SNOMEDCT_US'})-[:PAR*0..20]->(:Concept {code:'384821006'})
MATCH (hp:Concept {sab:'HPO'})
WHERE hp.cui = sct.cui
MATCH (hp)-[:PAR*0..15]->(:Concept {obo_id:'HP:0000708'})
RETURN sct.code AS sctid, sct.str AS sct_label,
       hp.obo_id AS hpo_id, hp.str AS hpo_label, hp.cui AS shared_cui;
```

### 8.5 Depth-tagged HPO nodes (for hierarchical feature embedding)

```cypher
MATCH path = (root:Concept {obo_id:'HP:0000708'})<-[:PAR*0..15]-(d:Concept {sab:'HPO'})
RETURN d.obo_id AS hpo_id, d.str AS label, length(path) AS depth
ORDER BY depth, d.obo_id;
```

### 8.6 DSM-5-TR via ICD-10-CM to SNOMED then to HPO

```cypher
MATCH (icd:Concept {sab:'ICD10CM'})
WHERE icd.code STARTS WITH 'F'
OPTIONAL MATCH (icd)-[:CUI_OF]-(cui:CUI)
OPTIONAL MATCH (cui)-[:CUI_OF]-(sct:Concept {sab:'SNOMEDCT_US'})
OPTIONAL MATCH (cui)-[:CUI_OF]-(hp:Concept {sab:'HPO'})
RETURN icd.code AS icd10, icd.str AS dx,
       collect(DISTINCT sct.code) AS sct_codes,
       collect(DISTINCT hp.obo_id) AS hpo_ids;
```

(Adjust `:CUI_OF` to your actual cross-source linking. Canonical UMLS loads usually use CUI equality across `:Atom` or `:Concept` nodes rather than an explicit relationship.)

### 8.7 ICF mental functions (b1xx) extraction

```cypher
MATCH (icf:Concept {sab:'ICF'})
WHERE icf.code STARTS WITH 'b1'
RETURN icf.code AS icf_code, icf.str AS label, icf.cui AS cui
ORDER BY icf.code;
```

### 8.8 Find LOINC instrument panels and child items

```cypher
MATCH (panel:Concept {sab:'LNC'})
WHERE panel.str =~ '(?i).*(PHQ-9|GAD-7|PANSS|MMSE|MoCA|ADAS-Cog|YMRS|MADRS|HAM-D|HAM-A|C-SSRS).*'
OPTIONAL MATCH (panel)-[:HAS_PART*0..3]->(item:Concept {sab:'LNC'})
OPTIONAL MATCH (item)-[:RELATED|RO*0..2]-(sct:Concept {sab:'SNOMEDCT_US'})
RETURN panel.code AS loinc_panel, panel.str AS instrument,
       collect(DISTINCT {item:item.code, label:item.str}) AS items,
       collect(DISTINCT sct.code) AS related_sct;
```

### 8.9 Cytognosis universal feature pull

```cypher
CALL {
  MATCH (:Concept {obo_id:'HP:0000708'})<-[:PAR*0..15]-(d:Concept {sab:'HPO'})
  RETURN d.obo_id AS feature_id, d.str AS label, 'HPO' AS source, d.cui AS cui
  UNION
  MATCH (:Concept {obo_id:'HP:0100543'})<-[:PAR*0..15]-(d:Concept {sab:'HPO'})
  RETURN d.obo_id AS feature_id, d.str AS label, 'HPO_COG' AS source, d.cui AS cui
  UNION
  MATCH (:Concept {code:'384821006', sab:'SNOMEDCT_US'})<-[:PAR*0..20]-(d:Concept {sab:'SNOMEDCT_US'})
  RETURN d.code AS feature_id, d.str AS label, 'SCT_MENTAL' AS source, d.cui AS cui
  UNION
  MATCH (:Concept {code:'74732009', sab:'SNOMEDCT_US'})<-[:PAR*0..20]-(d:Concept {sab:'SNOMEDCT_US'})
  RETURN d.code AS feature_id, d.str AS label, 'SCT_DISORDER' AS source, d.cui AS cui
  UNION
  MATCH (icf:Concept {sab:'ICF'})
  WHERE icf.code STARTS WITH 'b1' OR icf.code STARTS WITH 'b2'
        OR icf.code STARTS WITH 'd1' OR icf.code STARTS WITH 'd7'
  RETURN icf.code AS feature_id, icf.str AS label, 'ICF' AS source, icf.cui AS cui
  UNION
  MATCH (c:Concept)-[:HAS_SEMANTIC_TYPE]->(st:SemanticType)
  WHERE st.tui IN ['T041','T048','T053'] AND c.sab IN ['COGAT','MF','MFOEM']
  RETURN c.code AS feature_id, c.str AS label, c.sab AS source, c.cui AS cui
}
RETURN source, count(*) AS n, collect(feature_id)[..5] AS sample_ids
ORDER BY n DESC;
```

### 8.10 Build the inverted index (feature -> bindings)

```cypher
// Start from a Cytognosis feature; collect all operational bindings via CUI
MATCH (feat:CytognosisFeature {id:'CYTO:0001234'})
OPTIONAL MATCH (feat)-[:HAS_HPO]->(hp:Concept {sab:'HPO'})
OPTIONAL MATCH (feat)-[:HAS_SNOMED]->(sct:Concept {sab:'SNOMEDCT_US'})
OPTIONAL MATCH (feat)-[:HAS_LOINC_PANEL]->(loinc:Concept {sab:'LNC'})
OPTIONAL MATCH (loinc)-[:HAS_PART*0..3]->(item:Concept {sab:'LNC'})
OPTIONAL MATCH (feat)-[:HAS_CDISC]->(cdisc:Concept {sab:'CDISC'})
RETURN feat.id, feat.label,
       collect(DISTINCT hp.obo_id) AS hpo_ids,
       collect(DISTINCT sct.code) AS snomed_ids,
       collect(DISTINCT item.code) AS loinc_items,
       collect(DISTINCT cdisc.code) AS cdisc_qstestcds;
```

`:CytognosisFeature` is your platform's local feature-node label, sitting on top of the ingested public vocabulary nodes.

---

## 9. Caveats, Gaps, and Open Questions

1. **There is no canonical machine-readable DSM-5-TR criterion decomposition.** APA does not publish one. You must hand-curate. Plan for a 2 to 4 month curation effort with two clinical reviewers per disorder.
2. **HPO psychiatric depth lags behind clinical use.** The Monarch x SNOMED collaboration is improving this; check `phenotype.hpoa` and `hp.sssom.tsv` every quarter for new additions.
3. **SNOMED licensing for the PBC pathway**: while Cytognosis Foundation is a US nonprofit and gets SNOMED free via NLM / UMLS, a future PBC commercial subsidiary will need a SNOMED International Affiliate License with revenue-based fees. Plan the architecture so SNOMED-derived content can be removed or replaced (with HPO + MONDO + ICD-11) in commercial outputs without breaking downstream models.
4. **DSM-5 text is proprietary.** APA does not offer a machine-readable license. Cytognosis can publish criterion identifiers (e.g., MDD-A1) without quoting criterion text; the disorder names and codes themselves are facts and not copyrightable.
5. **ICD-11 license**: WHO permits non-commercial use freely; commercial productization requires a licensing dialogue with WHO Geneva. Foundation work is free; PBC commercial work needs negotiation.
6. **HiTOP measures have heterogeneous copyright at the item level** (PID-5, IDAS-II). The HiTOP consortium has obtained author permissions for research use; commercial use sometimes requires direct author negotiation. The HiTOP R package on CRAN is safe.
7. **RDoC has no structured export** from NIMH. You must scrape HTML or use a third-party OWL representation (Hastings, Larsen et al.) and accept curation effort.
8. **HiTOP-DAT and PROMIS bridge**: HiTOP-DAT explicitly uses PROMIS short forms for many domains. If you ingest both, items appear twice under different parents. Use PROsetta Stone to dedupe at the item-equivalent level rather than at the instrument level.
9. **ICF granularity ceiling at 4th level** means it cannot operate as the sole featureset. Layer 4 (HPO + SNOMED) is required below.
10. **No 2022 to 2026 integrative behavioral / cognitive ontology** (BCO, COCO, etc.) supersedes the recommended stack. Monitor CAOS 2025 to 2026 outputs.
11. **NBO maintenance is slowing**; do not rely on new releases. Use as static input.
12. **PROMIS items are LOINC-coded but the item content is HealthMeasures-licensed**. The metadata is open; the verbatim text needs a HealthMeasures account for distribution.
13. **All of Us PPI** is the most psychiatry-relevant survey vocabulary built into OMOP-Athena. PPI codes are public; PPI answers require Researcher Workbench access (Registered or Controlled Tier) with a DUC. PPI is the right vocabulary to bind PHQ-9 items as canonical IDs in your KG.
14. **ICD-11 Foundation vs MMS**: MMS is the codable linearization (analog of ICD-10). Foundation is the underlying multidimensional graph. Foundation is much richer and the right ingest target for a knowledge graph; MMS is right for billing-style coding. The WHO API exposes both.
15. **Continuous monitoring privacy**: the Cytoscope guardian agent generates feature-vector time series that constitute PHI plus extended-sensitive psychiatric data. Plan for HIPAA-grade storage and explicit per-user consent flows. ICF qualifier binning gives a defensible aggregation level for non-clinical exports.

---

## 10. Recommended Next Steps

1. **Stand up a feature-curation team** of two clinical reviewers and one ontology engineer. Target: 1,000 to 1,500 Cytognosis features with full 5-tuple identifiers and operational bindings, in 4 to 6 months.
2. **Ingest the eight high-priority sources** into the Neo4j graph in this order: HPO + HPOA, MONDO, DOID, SNOMED CT US Edition (refresh), LOINC, ICF (HL7 THO + ICD-API), MF + MFOEM, Cognitive Atlas. UMLS Metathesaurus and OLS4 are already in place.
3. **Build the DSM-5-TR criterion decomposition** as a CSV maintained in a version-controlled repo. One row per criterion atom. Cross-walk to HiTOP, RDoC, ICF, HPO, SNOMED.
4. **Build the operational binding table** (feature -> PROMIS item, LOINC item, CDISC QSTESTCD, HiTOP-SR item, PhenX protocol). Bootstrap from PROMIS LOINC bindings, CDISC supplements, HiTOP manuals.
5. **Train zero-shot construct classifiers** for the Cytoscope guardian agent against the feature space, using HiTOP-SR + PROMIS + public CDISC item text as exemplars.
6. **Publish the Cytognosis feature space** under CC BY 4.0 plus Apache 2.0 once stable. The featureset itself (the 5-tuple coding scheme) is a contribution to open science; the underlying public vocabularies retain their original licenses.
7. **Negotiate licenses ahead of PBC spinout**: SNOMED International Affiliate, WHO ICD-11, APA DSM-5-TR. Lead time 6 to 12 months each.

---

*Document version 1.0, 2026-05-13. Companion to `cdisc-qrs-comprehensive-reference.md`.*
