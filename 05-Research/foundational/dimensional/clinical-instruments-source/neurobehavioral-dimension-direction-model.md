# Separating Phenotype from Direction of Change: A Dimension–Deviation Model for the Cytognosis Neurobehavioral Feature Space (Part 3)

Companion to `cdisc-qrs-comprehensive-reference.md` (Part 1, instruments and external-standard crosswalks) and `cdisc-qrs-feature-space-design.md` (Part 2, the six-layer feature stack). This document tackles a problem the first two left implicit:

> A clinical "symptom" silently bundles two logically independent things — **the neurobehavioral dimension being measured** (the bearer: a behavior, emotion, motivation, perception, or cognitive function) and **the direction/type of deviation** on that dimension (decreased, increased, distorted, released, dysregulated, mistimed). To build a feature space that tracks *change* — especially subclinical change, and especially the positive/negative polarity we saw in schizophrenia — we must represent these two facets separately and recombine them by post-coordination.

This doc states the problem formally, gives the formal solution (an Entity–Quality / dimension–deviation model), assesses and **re-prioritizes** the source ontologies *specifically for this goal* (which reorders the Part 2 stack and adds three sources Part 2 never mentioned — **PATO, OBA, and SNOMED's interpretation post-coordination model**), proposes a controlled vocabulary for the direction axis, extends the Part 2 feature tuple, and works through decompositions of the major psychiatric syndromes.

Author: Cytognosis Foundation, drafted 2026-05-26. Status: living design doc.

---

## 0. TL;DR

1. **The conflation problem is real and pervasive.** "Anhedonia," "insomnia," "blunted affect," "psychomotor agitation," "hallucination" each fuse a *dimension* with a *direction*. Pre-coordinated clinical terms (HPO "Abnormal X," SNOMED "Decreased X") freeze the direction into the term, so you cannot ask "track the hedonic-capacity axis in either direction over time" without enumerating a different term per pole. For continuous monitoring and subclinical sensitivity this is fatal: the most informative early signal is *movement along an axis*, not the crossing of a clinical threshold into a named abnormal term.

2. **The formal fix already exists in the OBO world: the Entity–Quality (EQ) model.** A phenotype is decomposed as `E` (a bearer — a function, process, or trait) plus `Q` (a quality drawn from **PATO**, the Phenotype And Trait Ontology, whose entire job is to supply directional qualities: increased, decreased, abnormal, absent, fluctuating, mistimed). HPO, MP, ZP and others are *built* on EQ but ship only the pre-coordinated product. We should consume the **factored** form.

3. **The single most useful source Part 2 missed is OBA (Ontology of Biological Attributes).** OBA is explicitly a library of *unqualified* trait/attribute classes ("amount of sleep," "anxiety-related behavior trait") — i.e., the **dimension axis with the direction stripped out** — defined via EQ against PATO. OBA is to our dimension facet what HPO is to the pre-coordinated clinical leaf. Use OBA (+ ICF functions + RDoC constructs + Cognitive Atlas) as the **bearer/dimension** vocabulary, and PATO (+ SNOMED qualifier values) as the **direction** vocabulary.

4. **The clinical-terminology path is SNOMED post-coordination.** SNOMED natively factors a finding into `Interprets` (363714003 — the observable/function being judged) + `Has interpretation` (363713009 — the judgment: increased/decreased/present/absent). This is the EQ pattern in clinical clothing and the only such mechanism in any clinical terminology. It is the bridge from our factored features to billing/EHR systems.

5. **Recommended direction vocabulary: an 8-type psychiatric deviation typology**, each mapped to PATO and to SNOMED qualifier values: *deficit, excess, absence, distortion, release (false generation), dysregulation/lability, mistiming, context-decoupling.* This typology is what makes schizophrenia's positive/negative split — and depression-vs-mania, and the bidirectional DSM items (sleep, appetite, psychomotor) — fall out as `⟨same dimension, opposite direction⟩` rather than as unrelated symptoms.

6. **The dimension facet should be intrinsically bipolar/continuous, anchored in the normative range.** RDoC constructs (hypo/hyper by design), HiTOP spectra (bipolar factors), and PROMIS item banks (IRT-calibrated through the normal range, with *positive*-pole banks like Positive Affect and Meaning & Purpose) are the right sources for capturing **subclinical** variation. Deficit-framed vocabularies (HPO, SANS/SAPS) only see one tail.

7. **Historical grounding:** this is not a novel trick — it is Hughlings Jackson's 1884 positive/negative (release vs. deficit) distinction, carried into psychiatry by Crow's Type I/II (1980) and operationalized by Andreasen's SAPS/SANS. We are re-expressing a 140-year-old clinical insight in a computable EQ form.

8. **Net architectural change to Part 2:** replace the single pre-coordinated "clinical leaf" (Layer 4) with a **two-facet post-coordinated leaf**: `feature = ⟨dimension_id, direction_id⟩`. Every Part 2 five-tuple gains two fields (`dimension_facet`, `direction_facet`); the pre-coordinated HPO/SNOMED IDs are retained as *materialized convenience views* of common `⟨dimension, direction⟩` pairs, not as the primary representation.

---

## 1. The Problem, Stated Precisely

### 1.1 What a "symptom" actually is

Take the schizophrenia mapping we built. "Positive symptoms" (hallucinations, delusions, disorganization) and "negative symptoms" (blunted affect, alogia, avolition, anhedonia, asociality) read as two disjoint lists. But when you strip the polarity, they are perturbations of a shared, smaller set of dimensions:

| Dimension (bearer) | Negative-pole symptom | Positive-pole symptom |
|---|---|---|
| Affective expression / reactivity | Blunted affect (decreased) | (lability in mania; not a SCZ positive symptom) |
| Verbal output | Alogia (decreased) | Pressured speech (increased) |
| Goal-directed motivation | Avolition (decreased) | Hyperactivity / overcommitment (increased) |
| Hedonic capacity | Anhedonia (decreased) | (euphoria/heightened reward — mania) |
| Psychomotor activity | Retardation (decreased) | Agitation (increased) |
| Sensory perception | (hypo-perception, rare) | Hallucination (**release** — false generation) |
| Belief / reality testing | (over-rigid skepticism, rare) | Delusion (**distortion** + over-fixation) |
| Thought organization | Poverty of content (decreased) | Derailment/disorganization (loss of coherence) |

The clinical labels are `⟨dimension, direction⟩` pairs. The positive/negative dichotomy *is* the direction axis, observed on a particular menu of dimensions. Once you see this, three things follow:

- The "right" feature is the **dimension**, and "negative/positive" is a **value of the direction facet**, not a property of a different feature.
- A continuous-monitoring sensor should report a *signed* position on each dimension, not a basket of present/absent named symptoms.
- The same machinery explains the **bidirectional DSM items** that broke our earlier PHQ-9/GAD-7 mapping: PHQ-9 #3 (insomnia *or* hypersomnia), #5 (poor appetite *or* overeating), #8 (retardation *or* agitation) are single questions probing one *dimension* across both *directions*. The instrument designers already think dimension-first; our ontology should too.

### 1.2 Why the existing stack can't express it cleanly

Part 2's Layer 4 leaf vocabularies (HPO behavioral subtree, SNOMED mental-state findings) are **pre-coordinated**: the direction is fused into the atomic term.

- HPO HP:0000708's subtree is, by its own framing, a tree of *abnormalities*. "Anhedonia" already means "hedonic capacity, decreased." There is no HPO term for "hedonic capacity" as a bare, signable axis. (Indeed, the Part 2 doc's own §4.2 example carries `HP:0000718` labelled "Anhedonia" — but HP:0000718 is *Aggressive behavior*; the genuine anhedonia term is HP:0010522. Pre-coordinated trees invite exactly this kind of slip, because the human reaches for a label, not a `⟨dimension, direction⟩` coordinate. The factored model makes the error structurally impossible: you pick a dimension, then a direction.)
- SNOMED is better — it *can* post-coordinate — but the bulk of its mental-state findings are also shipped pre-coordinated, and the Part 2 stack consumes them that way.
- ICF is dimension-native (b-codes name functions, not abnormalities) but its **0–4 qualifier encodes severity, not direction** — it cannot distinguish hypersomnia from insomnia; both are "impairment of b134." So ICF gives us the bearer but no signed quality.

The net effect: Part 2 can tell you *that* sleep is abnormal and *how severely*, but not *in which direction*, and it represents "anhedonia" and a hypothetical "hyperhedonia" as unrelated leaves rather than ±poles of one axis.

### 1.3 The subclinical requirement sharpens the problem

The user's second requirement — *phenotypes subject to change in psychiatric clinical **and subclinical** manifestations* — is the dimensional-psychiatry thesis (RDoC, HiTOP): psychopathology is continuous with normal variation. A feature space for *change* must:

- represent each axis as **continuous and bipolar**, with a **normative midpoint**, so that movement in the normal range is visible before any threshold is crossed;
- prefer instruments **calibrated through the normal range** (PROMIS IRT theta, NIH Toolbox population norms) over clinical-cutoff scales;
- include **positive-pole constructs** (positive affect, meaning, vigor, sociability) that deficit-only vocabularies omit entirely.

Pre-coordinated abnormality terms are, by construction, blind to the subclinical range — they only instantiate once a deviation is large enough to be named. The dimension–direction model restores the full axis.

---

## 2. The Formal Solution: an Entity–Quality (Dimension–Deviation) Model

### 2.1 The EQ pattern, adapted

The OBO phenotype world long ago solved the general version of this problem with the **Entity–Quality (EQ)** decomposition: a phenotype = an **Entity** (`E`, the bearer) bearing a **Quality** (`Q`, from PATO). HPO, MP (mammalian), ZP (zebrafish), XPO, FYPO are all logically defined this way under the hood (UPHENO unifies them). We adopt the same pattern, specialized:

```
neurobehavioral_feature  ≡  Dimension (bearer)  +  Deviation (signed quality)

  Dimension  := a neurobehavioral function / trait / construct  (the axis)
  Deviation  := a PATO-style directional quality                (the sign + type of change)
```

- **Anhedonia** ≡ `hedonic capacity` + `decreased`
- **Hypersomnia** ≡ `sleep amount` + `increased`
- **Insomnia** ≡ `sleep continuity` + `decreased`
- **Hallucination** ≡ `sensory perception` + `aberrant/released (generation without stimulus)`
- **Affective lability** ≡ `affective regulation` + `increased variability (fluctuating)`
- **Delayed sleep phase** ≡ `circadian phase` + `delayed (mistimed)`

This is the same move SNOMED makes with `Interprets` + `Has interpretation`, and the same move OBA makes by defining unqualified attributes against PATO.

### 2.2 Two ontology facets, two source families

| Facet | What it holds | Primary sources | Role |
|---|---|---|---|
| **Dimension** (Entity / bearer) | the bare, sign-free neurobehavioral axis: "amount of sleep," "reward responsiveness," "affective expression," "sensory perception" | **OBA**, ICF Body-Functions b-codes, RDoC constructs, Cognitive Atlas concepts, MF/MFOEM processes & dispositions | the thing that *changes* |
| **Direction** (Quality / deviation) | the signed, typed deviation from the normative range | **PATO**, SNOMED qualifier values, the 8-type typology in §4 | *how* it changed |

A clinical leaf term (HPO "Anhedonia," SNOMED "Blunted affect") is then a **materialized view** = a named, commonly used `⟨Dimension, Direction⟩` pair. We keep those as convenience labels and as bridges to EHR/billing, but the *primary* representation is the factored pair.

### 2.3 Why factor rather than enumerate

- **Subclinical sensitivity:** a signed continuous value on `hedonic capacity` shows drift long before "anhedonia" is nameable.
- **Symmetry / completeness:** factoring forces you to consider both poles of every axis; enumeration leaves gaps (HPO has rich deficit terms, sparse excess terms).
- **Cross-syndrome unification:** depression and mania become opposite directions on a shared set of dimensions, not two unrelated symptom lists — exactly the schizophrenia positive/negative insight generalized.
- **Error resistance:** you cannot mislabel a coordinate the way you can mislabel a free-text leaf (cf. the HP:0000718/HP:0010522 slip in §1.2).
- **Measurement reuse:** one instrument item that probes a dimension bidirectionally (PHQ-9 #3/#5/#8) binds once to the dimension, with the response mapping to direction.

---

## 3. Source Assessment, Re-Prioritized for *This* Goal

Part 2 ranked sources for *universal coverage + DSM reconstruction*. For **dimension/direction separation + subclinical bidirectionality**, the priority order changes. New entries (not in Part 2) are flagged ★.

### 3.1 The direction-axis sources (the genuinely new layer)

**★ PATO — Phenotype And Trait Ontology.** The canonical quality ontology; ~2,400 quality classes. Backbone for the deviation facet. Relevant structure (verified):
- `PATO:0000001 quality` → `PATO:0000069 deviation (from normal or average)` → `PATO:0000460 abnormal` (opposite `PATO:0000461 normal`).
- Magnitude/rate relational qualities with explicit ± siblings: increased vs. decreased *amount*, *magnitude*, *rate*, *intensity*, *duration*, *frequency* (e.g., `PATO:0000911 decreased rate` "a rate which is relatively low"; mirror `increased` siblings).
- Variability/temporal qualities for the dysregulation and mistiming types (fluctuating, delayed, early).
- License CC BY; OBO PURL `http://purl.obolibrary.org/obo/pato.owl`; active maintenance. **This is the missing keystone — Part 2 never references PATO.**

**★ SNOMED CT interpretation post-coordination.** Attributes `363714003 Interprets` (points to the observable/function) + `363713009 Has interpretation` (the judgment), plus qualifier values such as `35105006 Increased`, `1250004 Decreased`, `281300000 Below reference range`, `263654008 Abnormal`, `2667000 Absent`, `52101004 Present`. This is the clinical-terminology EQ pattern and our bridge to EHR/billing. (Part 2 noted SNOMED's first-class *severity* attribute `246112005` but not the *interpretation* model that carries direction.)

**SNOMED severity attribute `246112005`** (already in Part 2) — orthogonal magnitude axis; keep, but distinguish from direction.

**ICF qualifier (0–4)** — severity only; explicitly *not* a direction source. Documented limitation.

### 3.2 The dimension-axis sources (bearers, sign-free)

**★ OBA — Ontology of Biological Attributes.** Species-independent library of *unqualified* trait classes, EQ-defined against PATO; the explicit design intent is "biological attributes" (bare traits) as distinct from HPO/MP "phenotypic effects vs. reference." This is the closest existing thing to a ready-made **dimension vocabulary**. Coverage of neuro/behavioral attributes is partial but growing; where OBA lacks a term, mint a Cytognosis dimension and EQ-define it ourselves (OBA-style) so it round-trips. License CC BY; PURL `http://purl.obolibrary.org/obo/oba.owl`. **The single highest-value addition for this goal.**

**ICF Body Functions b-codes** (Part 2 Layer 1) — promoted here: b-codes are *function* names (dimensions), not abnormalities. b134 (sleep), b152 (emotional functions), b1300/b1301 (energy/motivation), b1302 (appetite), b147 (psychomotor), b156/b2 (perception), b160 (thought), b140/b144/b164 (attention/memory/executive). The WHO-authoritative dimension scaffold.

**RDoC constructs** (Part 2 Layer 3a) — promoted: RDoC is *intrinsically dimensional and bidirectional* (each construct can be hypo- or hyper-active; Positive vs. Negative Valence Systems is literally a polarity framing). Best mechanistic dimension source; spans normal→abnormal by design.

**Cognitive Atlas concepts** — cognitive dimensions (working memory, attention, etc.) as bearers.

**MF + MFOEM** (Part 2 Layer 2) — supplies the formal *type* of each dimension (process vs. disposition vs. quality vs. appraisal/mood/emotion), which constrains which PATO qualities can legally apply (you can't sensibly say a *process* is "increased amount"; you say "increased rate").

**HiTOP spectra/sub-factors** (Part 2 Layer 3b) — bipolar psychometric dimensions; the detachment↔sociability, disinhibition↔conscientiousness axes are already signed. Best psychopathology dimension source and DSM bridge.

### 3.3 The subclinical / normative-range layer

**PROMIS** (Part 2 Layer 5) — promoted for this goal: IRT-calibrated *through the normal range*, and uniquely ships **positive-pole banks** (Positive Affect, Meaning & Purpose, Life Satisfaction, Self-Efficacy) that let a dimension be scored above as well as below the mean. The operational substrate for subclinical signing.

**NIH Toolbox** — population-normed performance (objective dimension values across the full range).

**★ Normal-personality + affect-structure models** — FFM/Big Five (bipolar trait axes) and the **circumplex model of affect** (valence × arousal — a clean 2-axis bidirectional affect geometry). These anchor the *normative midpoint* and the positive poles that clinical vocabularies omit. PID-5 is the validated bridge from normal FFM poles to maladaptive extremes (and is already in the HiTOP ecosystem).

### 3.4 Pre-coordinated leaves, demoted to "materialized views"

**HPO behavioral/cognitive subtree** and **SNOMED pre-coordinated findings** — still valuable as (a) EHR/genomics bridges and (b) ready-made labels for common `⟨dimension, direction⟩` pairs. But they are now *derived*, not primary. Mine their **logical definitions** (HPO `hp-edit.owl` EQ definitions; SNOMED stated `Interprets`/`Has interpretation`) to *recover* the dimension and direction each one encodes, then re-file them against our two facets.

### 3.5 Re-prioritized comparison (for dimension/direction separation + subclinical use)

| Source | New? | Provides | Sign-free dimension? | Native direction? | Subclinical range? | Priority for this goal |
|---|---|---|---|---|---|---|
| PATO | ★ | direction qualities | n/a | **yes** (±) | n/a | **A — keystone** |
| OBA | ★ | bare trait axes | **yes** | no | partial | **A — keystone** |
| SNOMED interpretation model | ★ (mech.) | clinical post-coord | via Interprets | **yes** (Has interp.) | no | A — clinical bridge |
| RDoC | promoted | mechanistic dimensions | yes | implicit (hypo/hyper) | yes | A |
| HiTOP | promoted | bipolar psychometric dims | yes (bipolar) | implicit (poles) | yes | A |
| PROMIS (+positive banks) | promoted | calibrated measurement | n/a (items) | response→direction | **yes** | A |
| ICF b-codes | reused | WHO function scaffold | yes | no (sev. only) | weak | B |
| MF/MFOEM | reused | dimension *typing* | yes | no | n/a | B |
| Cognitive Atlas | reused | cognitive dims | yes | no | n/a | B |
| FFM / circumplex affect | ★ | normative anchor, + poles | yes (bipolar) | yes (poles) | **yes** | B |
| NIH Toolbox | reused | objective dim values | n/a | response→direction | yes | B |
| HPO / SNOMED pre-coord | demoted | labels, EHR bridge | no (baked) | baked | no | C — materialized view |
| LOINC / CDISC items | reused | operational binding | n/a | item-dependent | item-dependent | C — binding |

---

## 4. The Direction Axis: an 8-Type Deviation Typology

PATO is comprehensive but generic. For psychiatric phenomenology we need a *small, clinically meaningful* controlled vocabulary on top of PATO. Proposed 8 types, each with its PATO anchor and SNOMED qualifier, and each is the **value of the `direction_facet`**:

| # | Direction type | Meaning | Psychiatric exemplars | PATO anchor | SNOMED qualifier |
|---|---|---|---|---|---|
| 1 | **Deficit / hypofunction** | level below normative range | anhedonia, avolition, blunted affect, alogia, psychomotor retardation, hyposomnia, hypophagia, hypoarousal, cognitive slowing | decreased amount/magnitude/rate (e.g. PATO:0000911) | 1250004 Decreased / 281300000 Below reference range |
| 2 | **Excess / hyperfunction** | level above normative range | euphoria, pressured speech, flight of ideas, hyperactivity, hypersomnia, hyperphagia, hyperarousal, increased libido | increased amount/magnitude/rate | 35105006 Increased / 281302008 Above reference range |
| 3 | **Absence / loss** | complete loss (limit of deficit) | mutism, akinesia, complete avolition/abulia, total anhedonia | PATO:0000462 absent | 2667000 Absent |
| 4 | **Distortion / qualitative aberration** | function runs but yields qualitatively wrong output | illusions, delusional content, perceptual distortion, thought derailment, dysmorphic body image | PATO:0000460 abnormal (qualitative) | 263654008 Abnormal |
| 5 | **Release / false generation** | output generated with no normal input (Jacksonian "positive") | hallucinations, intrusive thoughts, obsessions, compulsive urges, flashbacks, tics | abnormal + de-novo presence (PATO:0000467 present, in a normally-silent context) | 52101004 Present (context-inappropriate) |
| 6 | **Dysregulation / lability** | abnormal *variability*, not a fixed shift | affective lability, mood instability, emotional dysregulation, impulsivity | PATO:0001303 fluctuating / variability qualities | 25153009 Labile (where available) |
| 7 | **Mistiming / dyssynchrony** | temporal/phase disturbance | delayed sleep phase, circadian misalignment, sleep-onset vs. maintenance, diurnal mood variation | delayed/early/abnormal duration qualities | temporal-context qualifiers |
| 8 | **Context-decoupling / inappropriateness** | normal-magnitude function mismatched to context | inappropriate/incongruent affect, fear without threat, anxiety without stressor, situational vs. free-floating | abnormal (relational/contextual) | 263654008 Abnormal + finding-context |

Notes:
- Types 1–3 are the **magnitude** family (the "more/less/none" axis) — most negative symptoms are type 1, most manic symptoms type 2.
- Types 4–5 are the **quality** family and capture the classic "positive symptoms" of psychosis: distortion (delusions) vs. release (hallucinations). This is exactly **Hughlings Jackson's** positive (release) vs. negative (deficit) phenomena (1884), carried into psychiatry by **Crow's Type I/II** (1980) and operationalized by **Andreasen's SAPS/SANS**.
- Types 6–8 are the **dynamics** family — variability, timing, and context — which are invisible to a single cross-sectional severity score and are precisely where *continuous monitoring* adds value over episodic assessment.

This typology is the contribution that makes the positive/negative dichotomy computable and general: "positive symptom" ≈ {distortion, release, excess}; "negative symptom" ≈ {deficit, absence}.

---

## 5. The Augmented Feature Tuple

Extend the Part 2 §4.2 five-tuple with an explicit two-facet core. The pre-coordinated HPO/SNOMED IDs are retained but demoted to a `materialized_view` block.

```jsonc
{
  "cytognosis_id"   : "CYTO:0001234",
  "label"           : "Anhedonia",                 // human-friendly materialized label

  // --- PRIMARY: the factored representation ---
  "dimension_facet" : {
    "label"         : "Hedonic capacity / reward responsiveness",
    "oba_id"        : "OBA:VVVVVVV",               // bare trait (mint if absent)
    "icf_code"      : "b1522",                     // ICF range-of-emotion function
    "rdoc_construct": "Positive Valence Systems / Reward Responsiveness",
    "hitop_node"    : "Internalizing > Distress > (Anhedonia component dimension)",
    "mf_class"      : "MFOEM:NNNNNN",              // typed as appraisal/affect
    "cogatlas"      : null,
    "polarity"      : "bipolar",                   // can move + (heightened reward) or − (anhedonia)
    "normative_anchor": "PROMIS Positive Affect mean"
  },
  "direction_facet" : {
    "type"          : "deficit",                   // one of the 8 (§4)
    "pato_id"       : "PATO:0000911",              // decreased ...
    "snomed_interpretation": "1250004",            // Decreased
    "sign"          : -1
  },

  // --- DERIVED: pre-coordinated convenience labels & bridges ---
  "materialized_view": {
    "hpo_id"        : "HP:0010522",                // Anhedonia (NB: not HP:0000718)
    "snomed_id"     : "91138005",                  // Anhedonia (finding)
    "umls_cui"      : "C0178417",                  // verify in graph
    "snomed_postcoord": "404684003|Clinical finding| : 363714003|Interprets| = (hedonic capacity observable), 363713009|Has interpretation| = 1250004|Decreased|"
  },

  // --- measurement & hierarchy (as Part 2) ---
  "operational_bindings": {
    "promis_item"   : "PROMIS-Positive-Affect-xx (reverse) / PROMIS-Depression-xx",
    "loinc_item"    : "44250-9",                   // PHQ-9 Q1 (probes this dimension, deficit pole)
    "cdisc_qstestcd": "PHQ0101",
    "nih_toolbox"   : null,
    "language_signal": "Cytoscope anhedonia classifier (signed)"
  },
  "parents"         : ["CYTO:0001000"],
  "depth"           : 5,
  "modality"        : ["self_report","clinician_rated","performance","language_signal"]
}
```

Key consequences:
- A **dimension** node can exist with no direction (the bare axis), and a sensor emits a signed scalar on it.
- A **symptom** is the pair `⟨dimension, direction⟩`; "hyperhedonia/heightened reward" and "anhedonia" share one `dimension_facet` and differ only in `direction_facet.sign`.
- The **bidirectional DSM items** bind to the *dimension*; the patient's response selects the direction (PHQ-9 #3 → `sleep` dimension; "trouble sleeping" → deficit, "sleeping too much" → excess).
- Pre-coordinated clinical IDs remain queryable for EHR interop but are never the unit of *change-tracking*.

---

## 6. Worked Decompositions

### 6.1 Schizophrenia (the motivating case)

| Clinical symptom | Class | Dimension | Direction (§4) |
|---|---|---|---|
| Auditory hallucination | positive | sensory perception (auditory) | release (5) |
| Delusion | positive | belief / reality testing | distortion (4) |
| Disorganized speech | positive | thought/verbal organization | distortion (4) |
| Psychomotor agitation | positive | psychomotor activity | excess (2) |
| Blunted affect | negative | affective expression | deficit (1) |
| Alogia | negative | verbal output | deficit (1) |
| Avolition | negative | goal-directed motivation | deficit (1) |
| Anhedonia | negative | hedonic capacity | deficit (1) |
| Asociality | negative | affiliative motivation | deficit (1) |
| Catatonic stupor ↔ excitement | — | psychomotor activity | deficit (1) **or** excess (2) — same dimension, both poles |

"Positive" collapses to {release, distortion, excess}; "negative" to {deficit}. Catatonia's bidirectionality on one dimension is no longer paradoxical.

### 6.2 Depression vs. mania (one set of dimensions, opposite signs)

| Dimension | Depression direction | Mania direction |
|---|---|---|
| Mood/affect valence | deficit (low) | excess (elevated) |
| Energy / drive | deficit | excess |
| Psychomotor activity | deficit (retardation) | excess (agitation) |
| Sleep need/amount | deficit or excess (mistiming common) | deficit (reduced *need*) |
| Self-evaluation | deficit (worthlessness) | excess (grandiosity) → distortion at delusional extreme |
| Goal-directed activity | deficit (avolition) | excess (overcommitment) |
| Speech output | deficit | excess (pressured) |
| Thought rate | deficit (slowed) | excess (racing) → distortion (flight of ideas) |

Bipolar disorder becomes, literally, **sign reversal on a shared dimension bundle** — the cleanest possible demonstration of why factoring beats enumeration.

### 6.3 The bidirectional DSM items that broke the PHQ-9/GAD-7 mapping

| Item | Dimension | Directions the item spans |
|---|---|---|
| PHQ-9 #3 sleep | sleep amount/continuity | deficit (insomnia) **and** excess (hypersomnia); often mistiming (7) |
| PHQ-9 #5 appetite | appetite/eating drive | deficit **and** excess |
| PHQ-9 #8 psychomotor | psychomotor activity | deficit (retardation) **and** excess (agitation) |
| GAD-7 #5 restlessness | psychomotor/arousal | excess |
| GAD-7 #6 irritability | affective threshold | dysregulation (6) / context-decoupling (8) |

Binding these to a *dimension* (not a pre-coordinated symptom) is what lets one item carry two directions — which is exactly what the instrument intends.

---

## 7. Consolidation: How This Relates to Parts 1 and 2

- **Part 1 (comprehensive reference)** supplies the instruments and their LOINC/SNOMED/CDISC item codes — unchanged. Those items become `operational_bindings` on **dimension** nodes (an item probes a dimension; its response selects direction).
- **Part 2 (feature-space design)** supplies the six-layer stack. This doc **amends Layer 4**: instead of a single pre-coordinated clinical leaf, Layer 4 becomes a **post-coordinated pair** drawn from a *dimension* sub-layer (OBA + ICF + RDoC + Cognitive Atlas + MF/MFOEM) and a *direction* sub-layer (PATO + SNOMED interpretation + the §4 typology). Layers 0–3 and 5 are unchanged; HPO/SNOMED pre-coordinated terms move from "primary leaf" to "materialized view + EHR bridge."
- **Net additions to the source inventory** (append to Part 2 §7 bulk-download table): PATO (`http://purl.obolibrary.org/obo/pato.owl`, CC BY, monthly-ish), OBA (`http://purl.obolibrary.org/obo/oba.owl`, CC BY), UPHENO (`http://purl.obolibrary.org/obo/upheno.owl`, the EQ unifier), and the SNOMED interpretation reference set (already inside the SNOMED RF2 you ingest). All are OBO PURLs — wire to the existing PURL ingestion.

### 7.1 Build steps (delta over Part 2 §10)

1. **Ingest PATO + OBA + UPHENO** into the Neo4j graph alongside the existing OBO loads.
2. **Mine logical definitions** to recover `⟨E, Q⟩` for every HPO behavioral/cognitive term (`hp-edit.owl`) and every SNOMED mental-state finding (stated `Interprets`/`Has interpretation`). Populate `dimension_facet` and `direction_facet` from the recovered E and Q.
3. **Build the dimension registry**: deduplicate recovered E's against OBA + ICF + RDoC + Cognitive Atlas; mint Cytognosis dimensions (EQ-defined, OBA-style) where no public bearer exists. Target ~150–300 dimensions.
4. **Adopt the §4 8-type direction vocabulary**, each row mapped to PATO + SNOMED qualifier. Freeze it as a small controlled value set.
5. **Re-express every Cytognosis feature** as `⟨dimension, direction⟩`; auto-generate the pre-coordinated `materialized_view` (HPO/SNOMED) for the common pairs for EHR interop.
6. **Sign the measurement layer**: for each PROMIS/LOINC/CDISC binding, record which dimension it probes and the response→direction map (including the bidirectional-item case).
7. **Validate** by reconstructing the schizophrenia positive/negative split, the depression↔mania reversal, and the bidirectional PHQ-9 items purely from facets (the §6 tables are the acceptance test).

### 7.2 Cypher sketch — recover dimension+direction from HPO EQ definitions

```cypher
// HPO behavioral terms whose OWL logical definition references a PATO quality
MATCH (hp:Concept {sab:'HPO'})-[:PAR*0..15]->(:Concept {obo_id:'HP:0000708'})
OPTIONAL MATCH (hp)-[:HAS_LOGICAL_DEF]->(eq)
OPTIONAL MATCH (eq)-[:HAS_QUALITY]->(q:Concept {sab:'PATO'})     // direction facet
OPTIONAL MATCH (eq)-[:INHERES_IN]->(bearer)                       // dimension facet
RETURN hp.obo_id AS pheno, hp.str AS label,
       bearer.obo_id AS dimension_bearer, q.obo_id AS direction_quality
ORDER BY pheno;
// (Relationship names depend on how the EQ axioms are flattened on ingest;
//  if only OBO is loaded, parse the `intersection_of` / genus-differentia stanzas instead.)
```

---

## 8. Caveats, Gaps, Open Questions

1. **OBA's neuro/behavioral coverage is incomplete.** Expect to mint a meaningful fraction of dimensions ourselves (EQ-defined for round-tripping). Budget curation like Part 2's DSM decomposition effort.
2. **HPO/SNOMED logical definitions are uneven.** Not every pre-coordinated psychiatric term carries a clean machine-readable EQ axiom; many will need manual `⟨E,Q⟩` assignment. The HP:0000718-vs-HP:0010522 hazard shows why human-label-driven mapping is error-prone — drive it from logical definitions, not labels, and spot-check.
3. **PATO is generic; the §4 typology is a Cytognosis editorial layer.** Types 5–8 (release, dysregulation, mistiming, decoupling) don't all have crisp single PATO classes; they are *patterns* over PATO + temporal/context qualifiers. This is a genuine modeling commitment, not a lookup.
4. **"Direction" presumes a normative midpoint.** For some dimensions the normative range is age/sex/culture-dependent (sleep need, libido, sociability). The normative anchor must be a *distribution*, not a point — bind to PROMIS/NIH-Toolbox norms where they exist.
5. **Not every symptom is cleanly unidimensional.** Disorganized speech is arguably distortion of *several* dimensions at once; some features may need a small dimension *vector* + per-component direction. Allow multi-dimension features but prefer the minimal decomposition.
6. **SNOMED post-coordinated expressions need an expression repository / ECL**, and licensing for the PBC pathway (per Part 2 §9.3) still applies. Keep the factored Cytognosis representation primary so SNOMED-derived materializations can be swapped for HPO+PATO+OBA (all CC BY) in commercial outputs.
7. **Bidirectional ≠ symmetric.** A dimension's two poles may be clinically/biologically *non*-mirror (anhedonia is common and pathological; "hyperhedonia" is rarer and differently meaningful). Sign captures direction, not equivalence of significance — keep pole-specific metadata.
8. **Validation against real data is pending.** The acceptance test in §7.1.7 is internal-consistency only; external validation needs a labeled corpus (e.g., NDA/RDoCdb, All of Us PPI) scored both as named symptoms and as factored features.

---

## 9. Prioritized Sources for This Goal

Ordered by importance *to the dimension/direction problem specifically* (distinct from Part 2's ranking):

**Tier A — must-have (the factoring machinery):**
1. **PATO** — Phenotype And Trait Ontology — the direction/quality vocabulary. `http://purl.obolibrary.org/obo/pato.owl` (CC BY).
2. **OBA** — Ontology of Biological Attributes — the sign-free dimension/trait vocabulary. `http://purl.obolibrary.org/obo/oba.owl` (CC BY).
3. **SNOMED CT interpretation model** — `Interprets` (363714003) + `Has interpretation` (363713009) + qualifier values — clinical post-coordination + EHR bridge (within existing SNOMED RF2).
4. **UPHENO** — cross-species EQ unifier; the pattern library for factoring. `http://purl.obolibrary.org/obo/upheno.owl`.
5. **RDoC** — dimensional, bidirectional mechanistic constructs (NIMH; public domain).
6. **HiTOP** — bipolar psychometric spectra + DSM bridge.
7. **PROMIS (incl. positive-pole banks)** — subclinical/normative-range, signed measurement.

**Tier B — strong support:**
8. **ICF Body Functions b-codes** — WHO function (dimension) scaffold.
9. **MF + MFOEM** — formal typing of dimensions (process/disposition/quality/affect).
10. **Cognitive Atlas / CogPO** — cognitive dimensions + task paradigms.
11. **FFM/Big Five + PID-5 + circumplex affect model** — normative-range anchor and positive poles.
12. **NIH Toolbox** — objective, population-normed dimension values.

**Tier C — bridges / materialized views / theory:**
13. **HPO behavioral+cognitive subtree** (mine its EQ defs; keep as materialized labels + genomics bridge).
14. **MONDO / UMLS** — disorder & cross-vocab CUI bridge (unchanged from Part 2).
15. **LOINC + CDISC QRS items** — operational bindings to dimensions (Parts 1–2).
16. **Historical/theoretical**: Hughlings Jackson (1884, positive/negative as release/deficit); Crow (1980, Type I/II schizophrenia); Andreasen (SAPS/SANS); Berrios (descriptive psychopathology); Insel et al. (2010, RDoC); Kotov et al. (2017, HiTOP). These justify the §4 typology and the dimensional stance.

---

## 10. Recommended Next Steps

1. Ingest **PATO + OBA + UPHENO** (one sprint; all OBO PURLs, fits existing pipeline).
2. Run the **EQ-recovery mine** over HPO behavioral/cognitive + SNOMED mental-state findings; produce a draft `⟨dimension, direction⟩` table for every existing pre-coordinated leaf.
3. Curate the **dimension registry** (~150–300 sign-free axes) against OBA/ICF/RDoC/CogAt; mint and EQ-define gaps.
4. Freeze the **§4 8-type direction value set** with PATO + SNOMED qualifier mappings.
5. Re-express the feature space as factored pairs; auto-materialize HPO/SNOMED convenience labels.
6. Sign the measurement bindings (esp. bidirectional items).
7. Acceptance test: regenerate §6 tables purely from facets.
8. Publish the dimension registry + direction typology (CC BY) as the open-science contribution; it is novel and reusable beyond Cytognosis.

---

*Document version 1.0, 2026-05-26. Part 3 of the Cytognosis neurobehavioral phenotype reference set. Companions: `cdisc-qrs-comprehensive-reference.md` (Part 1), `cdisc-qrs-feature-space-design.md` (Part 2).*
