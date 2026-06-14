> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `neuroverse`, `pipeline`, `research`, `report`

# Cytognosis / Neuroverse Real-Data Phenotype Projection and Archetypal-Analysis Report — v0

**Prepared for:** Supervisor / research review  
**Project:** Cytognosis / Neuroverse phenotype-space pipeline  
**Current stage:** Real-data projection and first real-data linear archetypal analysis completed  
**Dataset:** Temporal psychological assessment dataset with PHQ-9, GAD-7, ISI, PSS/PSS-10 bridge, demographics, and response-time signals  
**Framing:** Non-diagnostic research representation system. Outputs are phenotype-vector coordinates and phenotype-program summaries, not clinical categories, diagnoses, or treatment recommendations.

---

## 1. Executive summary

We built and validated an end-to-end real-data pipeline that transforms raw psychometric questionnaire files into a 34-dimensional phenotype-vector representation, then fits a truth-free linear archetypal-analysis model on the projected real cohort.

The current final run is technically successful:

- **Input records:** 24,292
- **Projected records:** 24,292
- **Projection failures:** 0
- **Detected tests:** PHQ-9, GAD-7, ISI, PSS-10 for all 24,292 records
- **Phenotype-vector dimensions:** 34
- **Mean / median coverage ratio:** 0.470588
- **Out-of-range values after score correction:** 0
- **Unmapped response items:** 0
- **Non-numeric values:** 0
- **Safety-flag records:** 1,845
- **De-identification:** passed
- **Non-diagnostic language audit:** passed

The real-data archetypal-analysis model also completed successfully:

- **Input matrix:** 24,292 × 34
- **Missing values:** 437,256, mostly because only part of the 34-dimensional phenotype space is observable from PHQ-9/GAD-7/ISI/PSS-10
- **Recommended truth-free k:** 13
- **Elbow reference:** k≈6
- **Bootstrap stability mean:** 0.8206
- **Effective archetype usage:** 9.49 out of 13
- **Simplex row-sum max error:** approximately 4.44e-16
- **Negative mixture weights:** 0
- **Privacy audit:** passed
- **Non-diagnostic audit:** passed
- **Main warning:** 18/34 axes have observation rate below 0.05

The scientific interpretation should therefore be:

> The system is ready for real-data phenotype-space analysis. The k=13 model is a valid full real-data archetype representation, but interpretation must be coverage-aware because this cohort only observes the PHQ-9/GAD-7/ISI/PSS-10-covered region of the larger 34-axis phenotype space.

---

## 2. Scientific motivation

The overall project aims to represent psychological and neurobehavioral information as a structured phenotype space rather than as diagnostic labels. The conceptual backbone is:

```text
raw questionnaire responses
→ item/subscale scores
→ normalized phenotype-axis scores
→ 34-dimensional phenotype vector
→ user/session phenotype matrix
→ convex archetypal-analysis model
→ interpretable phenotype-program extremes
```

The archetypal-analysis framing is important because archetypes are not average cluster centroids. They are extremal representatives of phenotype-program patterns. Each user/session is represented as a convex mixture of these extremes.

This aligns with the broader phenospace/Pareto view: observed phenotypes can be interpreted as weighted combinations of archetypal extremes in a phenotype space. It also aligns with Deep Archetypal Analysis and MIDAA-style methods, where convex archetype mixtures can be learned in a latent representation and later extended with side information.

---

## 3. Prior ontology and phenotype-space foundation

Before real-data modeling, we built a non-diagnostic phenotype-axis layer. The broader ontology work started from a curated neurobehavioral phenotype ontology. In Phase 1, Gemma 4 E2B-it was adapted with LoRA against an ontology-aware supervision teacher. The curated phenotype subset contained 1,671 concepts across HPO, NBO, and ASDPTO. Phase 1 reported strong ontology-retrieval improvements, including Parent Hits@10 rising from 0.346 to 0.897 and equivalence Hits@10 rising from 0.068 to 1.000. This established the conceptual foundation for downstream disease/test/person phenotype-space work.

For the psychometric pipeline, we then created the v0 artifacts:

```text
test_registry_mapping_v1.csv
phenotype_axes_v0.csv
phenotype_axes_v0_reviewed.csv
scoring_rules_v0.json
test_to_axis_weight_matrix_v0.csv
project_user_vector_v0.py
batch_project_vectors_v0.py
real_data_projection_pipeline_v0.py
real_archetype_model_v0.py
```

Key design decisions:

1. **phenotype_axis_id is the computational key.**
2. Ontology IDs are annotations, not required runtime keys.
3. The output is non-diagnostic.
4. Safety-sensitive item responses are surfaced as safety flags, not diagnostic conclusions.
5. License and commercial-use risk are preserved as metadata.
6. Full item text is not required or stored in the runtime representation.
7. Missingness and coverage are explicit parts of the representation.

---

## 4. Real dataset and preparation

The real dataset consists of five raw files:

```text
demographic.csv
phq9.csv
gad7.csv
isi.csv
pss.csv
```

The preparation target was to standardize these files into an analysis-ready structure:

```text
temporal_assessment_outputs_real_v0_prepared/
  processed/
    temporal_assessment_canonical_wide_v0.csv
    temporal_assessment_item_events_long_v0.csv
    temporal_assessment_rt_features_v0.csv
    temporal_assessment_projection_input_v7d.csv
    temporal_assessment_projection_input_v7d_score_fixed.csv
    temporal_rt_phenotype_analysis_table_v7d_score_fixed_patched_isi.csv

  configs/
    real_data_config_v7d_isi.yaml

  qc/
    canonical_scale_detection_report_v0.json
    scale_total_validation_v0.json
    pss_mismatch_audit_v0.csv
    projection_input_item_range_audit_before_fix_v0.csv
    projection_input_item_range_audit_after_fix_v0.csv
    projection_input_score_range_fix_report_v0.json
    dataset_preparation_summary_v0.json

  projection_outputs_v7d_score_fixed_patched_isi/
    real_population_responses_v0.jsonl
    real_population_projections_v0.jsonl
    real_population_phenotype_matrix_v0.csv
    real_population_projection_summary_v0.json
    real_data_qc_report_v0.json
    real_data_qc_report_v0.md
    real_axis_coverage_risk_report_v0.csv
    real_data_projection_v0.validation_summary.json
```

The preparation script canonicalized item IDs into the standard schema:

```text
PHQ9_01 ... PHQ9_09
GAD7_01 ... GAD7_07
ISI_01 ... ISI_07
PSS_01 ... PSS_14
PSS10_01 ... PSS10_10
```

It also created response-time columns and engineered response-time features such as scale-level RT mean, median, total, coefficient of variation, fast-response fraction, very-fast-response fraction, slow-response fraction, RT slope over item order, RT fatigue ratio, item-score/response-time correlation, and overall RT features.

---

## 5. PSS-10 bridge and score-coding correction

The real dataset included PSS-14, while the projection runtime supports PSS-10. Therefore, a deterministic PSS-10 bridge was created:

```text
PSS10_01 <- PSS_01
PSS10_02 <- PSS_02
PSS10_03 <- PSS_03
PSS10_04 <- PSS_06
PSS10_05 <- PSS_07
PSS10_06 <- PSS_08
PSS10_07 <- PSS_09
PSS10_08 <- PSS_10
PSS10_09 <- PSS_11
PSS10_10 <- PSS_14
```

During projection validation, we found a score-range issue: PSS-derived items were partially coded on a 1–5 scale while the scoring artifacts expected 0–4. This caused out-of-range values and incomplete PSS-10 detection in an earlier run. We audited the item ranges, detected the offset, shifted the affected PSS10 columns from 1–5 to 0–4, recomputed totals, and reran projection.

The final corrected input file is:

```text
processed/temporal_assessment_projection_input_v7d_score_fixed.csv
```

After this fix:

```text
out_of_range_values = 0
PSS-10 detected for all 24,292 records
unmapped response items = 0
non_numeric_values = 0
```

---

## 6. ISI artifact patch

A separate issue was that simply adding ISI items in the input was not enough: the projection runtime needed ISI mappings in both the YAML config and the scoring/weight artifacts.

We fixed this by using the patched ISI artifacts:

```text
temporal_assessment_outputs_real_v0/patched_artifacts_v7_isi/
  scoring_rules_v7_isi.json
  test_to_axis_weight_matrix_v7_isi.csv
```

Then we reran the projection with:

```text
real_data_config_v7d_isi.yaml
temporal_assessment_projection_input_v7d_score_fixed.csv
scoring_rules_v7_isi.json
test_to_axis_weight_matrix_v7_isi.csv
phenotype_axes_v0_reviewed.csv
```

This produced the final clean projection directory:

```text
projection_outputs_v7d_score_fixed_patched_isi/
```

---

## 7. Final real-data projection result

The final real-data projection run completed successfully.

Final projection validation:

```json
{
  "input_records": 24292,
  "projected_records": 24292,
  "failed_records": 0,
  "detected_tests": {
    "GAD-7": 24292,
    "ISI": 24292,
    "PHQ-9": 24292,
    "PSS-10": 24292
  },
  "matrix_axis_columns": 34,
  "all_axis_columns_present": true,
  "mean_coverage_ratio": 0.470588,
  "median_coverage_ratio": 0.470588,
  "records_with_unmapped_items": 0,
  "records_with_safety_flags": 1845,
  "out_of_range_values": 0,
  "non_numeric_values": 0,
  "deidentified": true,
  "raw_identifiers_written": false,
  "non_diagnostic_language_passed": true,
  "warnings": []
}
```

Interpretation:

1. Every raw record was projected successfully.
2. Every record had PHQ-9, GAD-7, ISI, and PSS-10 detected.
3. The model produced all 34 phenotype-vector columns.
4. The observed coverage ratio is 0.470588, meaning approximately 16 out of 34 axes are directly supported per record.
5. There are 1,845 safety-flag records, mostly reflecting PHQ-9 safety-sensitive item behavior.
6. Raw IDs were not written.
7. Outputs remain non-diagnostic.

---

## 8. Final merged analysis table

After the clean projection, we created a final merged table:

```text
processed/temporal_rt_phenotype_analysis_table_v7d_score_fixed_patched_isi.csv
```

This table combines canonical projected questionnaire input, demographic fields, corrected item scores, scale totals and audit fields, RT engineered features, selected tests, coverage ratio, safety flag count, and 34 phenotype-axis columns.

Final table properties:

```text
rows: 24,292
columns: 145
AXIS_* columns: 34
coverage mean: 0.470588
```

This is the main analysis-ready table for response-time/phenotype modeling.

---

## 9. Real archetypal-analysis model

We ran the real-data archetype model on:

```text
projection_outputs_v7d_score_fixed_patched_isi/real_population_phenotype_matrix_v0.csv
```

The model used:

```text
k_min = 3
k_max = 14
seeds = 0,1,2,3,4
bootstrap_repeats = 20
bootstrap_fraction = 0.80
imputation = mean
feature_scaling = none
init_mode = mixed
```

The model loaded a 24,292 × 34 real phenotype matrix and reported 437,256 missing values. This missingness is expected because the current real questionnaire battery covers only a subset of the full 34-axis vector space.

Model-selection results showed reconstruction MSE decreasing as k increased. The script selected k=13 using truth-free criteria, while also noting proximity to an elbow near k=6. Therefore, the correct interpretation is:

```text
k=13 = selected full real-data representation
k≈6 = compact elbow model useful for simplified reporting/visualization
```

---

## 10. Final real archetype validation result

The validation summary for the real archetype model:

```json
{
  "input_records": 24292,
  "axis_dimensions": 34,
  "mean_coverage_ratio": 0.470588,
  "missing_value_count": 437256,
  "imputation_method": "mean",
  "feature_scaling": "none",
  "k_min": 3,
  "k_max": 14,
  "recommended_k": 13,
  "recommended_k_reason": "Selected k=13 using truth-free criteria: near-best reconstruction, seed stability, effective usage, separation, and proximity to elbow k=6.",
  "simplex_row_sum_max_error": 4.440892098500626e-16,
  "negative_weight_count": 0,
  "bootstrap_stability_mean": 0.8205783658786429,
  "effective_archetype_usage": 9.490877288655733,
  "non_diagnostic_language_passed": true,
  "privacy_audit_passed": true,
  "warnings": [
    "18 axes have observation_rate < 0.05, exceeding 30% of axes."
  ]
}
```

Interpretation:

1. The model completed successfully.
2. Mixture weights are mathematically valid: non-negative and sum to one.
3. Stability is acceptable: bootstrap stability ≈ 0.82.
4. Effective archetype usage is 9.49, meaning that although k=13 was selected, the model effectively uses roughly 9–10 archetypal degrees of freedom.
5. The largest limitation is sparse coverage of many axes: 18 out of 34 have observation rate below 0.05.
6. Privacy and non-diagnostic language checks passed.

---

## 11. Archetype outputs

The model produced:

```text
real_archetype_model_selection_v0.csv
real_archetype_model_selection_v0.json
real_phenotype_archetypes_v0.json
real_user_archetype_assignments_v0.csv
real_archetype_axis_loadings_v0.csv
real_archetype_nearest_records_v0.csv
real_archetype_stability_v0.csv
real_archetype_stability_v0.json
real_archetype_baseline_comparison_v0.json
real_archetype_imputation_sensitivity_v0.json
real_archetype_coverage_robustness_v0.json
real_archetype_model_v0.validation_summary.json
real_archetype_model_v0.log
```

The key interpretability file is:

```text
real_phenotype_archetypes_v0.json
```

It contains schema version, k=13, seed=1, sparse local convexity mode, 13 archetype definitions, top axes per archetype, low axes per archetype, nearest de-identified records, dominant contributing tests, interpretation labels, and research notes.

---

## 12. Reviewed interpretation of the 13 real archetypes

The automatic labels are useful but not final. Some labels are too generic or wrong because the auto-labeling script was trained on broader synthetic archetype names while this real dataset only covers PHQ-9/GAD-7/ISI/PSS-10.

A reviewed interpretation is:

| Archetype | Main observed axes | Suggested reviewed label | Keep for report? | Notes |
|---|---|---|---|---|
| ARC_01 | Guilt/worthlessness, low self-efficacy, low perceived control | Worthlessness / low self-efficacy phenotype-program | Yes | Original label should be corrected |
| ARC_02 | Somatic tension/anxiety, helplessness, guilt, irritability, stress | Anxiety / helplessness / stress phenotype-program | Yes | Strong interpretable pattern |
| ARC_03 | Low self-efficacy, low perceived control, mild irritability | Low self-efficacy / low control phenotype-program | Yes, relabel | Original trauma label is not supported |
| ARC_04 | Executive dysfunction, concentration difficulty, fatigue, helplessness, anhedonia | Cognitive-fatigue / executive dysfunction phenotype-program | Yes | Good interpretable pattern |
| ARC_05 | Sleep disturbance, executive dysfunction, stress, fatigue | Sleep-stress / fatigue phenotype-program | Yes | Good interpretable pattern |
| ARC_06 | Very high anhedonia, otherwise low | Isolated anhedonia phenotype-program | Yes | Clean sparse archetype |
| ARC_07 | Anhedonia, depressed mood, appetite/weight change, worthlessness | Low mood / anhedonia / appetite-change phenotype-program | Yes | Strong affective pattern |
| ARC_08 | Worthlessness, depressed mood, anhedonia, appetite change, suicidal ideation, psychomotor change, anxiety | Safety-relevant high affective-burden phenotype-program | Yes, with safety caveat | Do not overstate clinically |
| ARC_09 | Appetite/weight change, low self-efficacy/control | Appetite-change / low self-efficacy phenotype-program | Yes | Specific but interpretable |
| ARC_10 | All top axes are zero | Null / low-signal archetype | Review / maybe exclude | Likely degenerate due to sparse axes |
| ARC_11 | Low self-efficacy, depressed mood, low perceived control | Depressed mood / low self-efficacy phenotype-program | Yes | Similar to ARC_03/12 |
| ARC_12 | Low self-efficacy, low control, helplessness | Low self-efficacy / helplessness phenotype-program | Yes | Similar to ARC_03/11 |
| ARC_13 | Psychomotor change, low self-efficacy, irritability, control | Psychomotor / irritability / control phenotype-program | Yes | Distinct PHQ-linked pattern |

Important: ARC_10 should be reviewed carefully. It appears to be a degenerate/low-signal archetype produced by the combination of high k, mean imputation, and many fully unobserved axes.

---

## 13. Main scientific finding

The real dataset supports a set of phenotype-program extremes primarily in the following domains:

```text
1. sleep disturbance / fatigue / stress
2. somatic anxiety / tension
3. low mood / anhedonia / appetite change
4. guilt / worthlessness
5. low self-efficacy / low perceived control / helplessness
6. executive dysfunction / concentration difficulty
7. psychomotor change / agitation
8. safety-relevant affective burden
```

The dataset does not directly support strong conclusions about:

```text
psychotic-like experiences
trauma re-experiencing
substance use
autism/social communication
risk-taking
racing thoughts / mania-like activation
personality detachment/disinhibition
```

Those axes exist in the 34-dimensional framework, but the current real battery does not measure them well.

---

## 14. Limitations

### 14.1 Partial axis coverage

Only around 16 out of 34 axes are observed per record. This explains:

```text
missing_value_count = 437,256
18 axes with observation_rate < 0.05
```

The model is valid for the observed subspace, but not for the full 34-axis space.

### 14.2 Mean imputation

Mean imputation was used by default. This makes the model run over all 34 axes, but it can reduce interpretability for axes that are systematically unobserved.

Future analysis should run:

```text
observed-axis-only model
selected-axis model using only axes with observation_rate >= 0.05
imputation sensitivity: mean vs median vs zero vs KNN
```

### 14.3 Auto-labeling limitations

Automatic labels were not fully reliable. Examples:

- ARC_03 was labeled as trauma-like but is actually low self-efficacy/control.
- ARC_10 is effectively a null/low-signal archetype.

Therefore, human-reviewed labels are required before supervisor/paper presentation.

### 14.4 Safety-sensitive interpretation

ARC_08 includes a high suicidal-ideation axis. This must be treated only as a safety-sensitive phenotype-program pattern. It is not a diagnosis or treatment recommendation.

### 14.5 No longitudinal modeling yet

The current real dataset appears as one session per participant. RT features are available, but longitudinal drift or temporal trajectories across sessions have not yet been modeled.

---

## 15. Current status

The project has now completed:

```text
1. Ontology-guided phenotype-space foundation
2. Test-to-axis registry construction
3. 34-dimensional phenotype vector design
4. Runtime projection engine
5. Batch projection engine
6. Synthetic population generation
7. Balanced synthetic benchmark
8. Naturalistic synthetic benchmark
9. Real-data projection pipeline
10. Real dataset canonicalization
11. PSS score-coding correction
12. ISI artifact patch
13. Final clean real-data projection
14. Final merged analysis table
15. Real linear archetypal analysis
16. Initial reviewed archetype interpretation
```

The current best real-data artifacts are:

```text
temporal_assessment_outputs_real_v0_prepared/processed/
  temporal_rt_phenotype_analysis_table_v7d_score_fixed_patched_isi.csv

temporal_assessment_outputs_real_v0_prepared/projection_outputs_v7d_score_fixed_patched_isi/
  real_population_phenotype_matrix_v0.csv
  real_population_projection_summary_v0.json
  real_data_projection_v0.validation_summary.json

temporal_assessment_outputs_real_v0_prepared/real_archetype_outputs_v7d_score_fixed_patched_isi/
  real_phenotype_archetypes_v0.json
  real_user_archetype_assignments_v0.csv
  real_archetype_axis_loadings_v0.csv
  real_archetype_model_v0.validation_summary.json
```

---

## 16. Recommended next steps

### P0 — immediately

Create a reviewed archetype table:

```text
real_phenotype_archetypes_reviewed_v0.csv
```

Columns:

```text
archetype_id
original_auto_label
reviewed_label
top_axes
interpretability_status
safety_sensitive
coverage_limited
keep_for_report
notes
```

### P0 — immediately

Run a selected-axis archetype model using only axes with observation rate >= 0.05. This will reduce the influence of completely unobserved axes and likely produce cleaner archetypes.

Suggested output:

```text
real_archetype_outputs_v7d_selected_axes_observed_only/
```

### P1 — response-time modeling

Build robust RT clustering:

```text
robust_rt_clustering_v0.py
```

Required design:

```text
1. detect extreme RT outliers
2. winsorize RT features
3. log-transform RT magnitude features
4. robust-scale RT features
5. cluster non-extreme participants
6. keep extreme participants as anomaly group
7. compare RT clusters on phenotype axes and scale totals
```

This is scientifically important because the dataset contains response-time dynamics, which are the main contribution beyond ordinary questionnaire scoring.

### P1 — RT-phenotype association modeling

Run:

```text
rt_cluster_phenotype_analysis_v0.py
predictive_rt_signal_models_v0.py
```

Core questions:

```text
Do RT features explain phenotype-axis variation beyond total scale scores?
Do RT clusters differ on phenotype coordinates?
Can RT dynamics predict phenotype archetype weights?
Are safety-flag records associated with distinct RT patterns?
```

### P1 — compact archetype model

Fit an interpretable compact model around k=6:

```text
k=6 = compact elbow model
k=13 = full selected model
```

Report both:

```text
k=13: best truth-free real-data representation
k=6: compact explanatory visualization model
```

### P2 — Deep AA / MIDAA

After RT features and side information are finalized, move to GPU-based Deep Archetypal Analysis / MIDAA-style modeling:

```text
deep_archetype_model_v0.py
```

Inputs:

```text
phenotype matrix
RT side-info matrix
demographics
coverage mask
possibly safety flag metadata
```

Goal:

```text
Learn a latent phenotype+RT representation where archetypes are more stable and interpretable than in raw 34D linear space.
```

---

## 17. Suggested supervisor-facing conclusion

We have completed the first reproducible real-data bridge for the Cytognosis / Neuroverse phenotype-space pipeline. Starting from raw PHQ-9, GAD-7, ISI, PSS, demographic, and response-time files, we built a canonicalized and de-identified projection-ready dataset, corrected score-coding issues, patched ISI scoring/mapping artifacts, and projected all 24,292 participants into the 34-dimensional phenotype-vector space with zero projection failures, zero unmapped items, and zero out-of-range values. The final projection covers approximately 16 of 34 axes per participant, reflecting the limits of the available questionnaire battery.

We then fitted a truth-free linear archetypal-analysis model on the real projected phenotype matrix. The selected full model uses k=13 archetypes and satisfies the convex-mixture constraints: all user/session mixture weights are non-negative and sum to one within numerical precision. Bootstrap stability is acceptable, and privacy/non-diagnostic audits pass. The discovered phenotype-program extremes primarily reflect sleep/fatigue, anxiety/stress, low mood/anhedonia, self-efficacy/control, guilt/worthlessness, executive dysfunction, psychomotor change, and safety-relevant affective burden. Interpretation is coverage-limited because 18 of 34 axes are rarely observed in this battery.

The next methodological step should focus on response-time dynamics: robust RT clustering, RT-to-phenotype association analysis, and RT-informed archetypal modeling. A compact k≈6 model can be used for supervisor-facing visualization, while k=13 remains the full real-data selected model.
