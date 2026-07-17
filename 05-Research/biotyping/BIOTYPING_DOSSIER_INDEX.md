# Biotyping Dossier Index

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Audience**: researchers, stakeholders
> **Tags**: `research`, `biotyping`, `neuro`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## (A) BLUF

We already have most of the science and ontology canon needed to build the universal dimensional
biotyping map for the precision-psychiatry proposal; the missing piece is assembly, not new
research. Three disorders (MDD, BD, SZ) plus optional PTSD and anxiety/autism can be placed on
3 to 5 leading genomic factors, cross-walked to DSM cross-cutting measures, HiTOP, and RDoC, with
micro/meso/macro treatment layers already drafted across separate dossiers. This index catalogs
every source asset, specs the two output variants (educational and grant-ready), specs the figure
itself, and flags four gaps to ingest before the figure is built.

**If you only read one thing**: Section (C), the figure spec, is the one piece of new synthesis
this document adds; everything else already exists and just needs to be assembled and cited.

---

## (B) Source catalog

| Asset | Path | What it provides | Canonical / raw |
|---|---|---|---|
| Biotypes cheat sheet v2 | `docs/05-Research/foundational/disease-biotypes/diseases/BIOTYPES_CHEATSHEET_v2.md` | Canonical index of ~25 anchored biotypes across 6 disorders, 4 evidence layers (connectomic, EEG/MEG, molecular/cellular, treatment-response); the fastest single entry point | Canonical |
| Per-disorder biotype dossiers | `docs/05-Research/foundational/disease-biotypes/diseases/{adhd,anorexia,anxiety,asd,asd-research-brief,bipolar,mdd,ocd,ptsd,schizophrenia,sud-alcohol,sud-cannabis,sud-nicotine,sud-opioid,tourette}.md` | 14 disorder-specific dossiers, each following the Literature Synthesis template; source material the transdiagnostic syntheses roll up | Canonical |
| BDNF/TrkB Neuroplasticity Axes Dossier | `docs/05-Research/foundational/dimensional/BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` | Keystone science: Mood/Thought/Cognitive axes downstream of BDNF/TrkB; the EVIDENT/neuroplastogen through-line; Section 5 factorized-PRS is CONFIDENTIAL, keep off any published figure or paper | Canonical (Sec 1-3, 7 publishable; Sec 5 confidential, platform moat) |
| Molecular/cellular cross-cutting biotypes | `docs/05-Research/foundational/disease-biotypes/molecular-cellular-biotypes.md` | Six molecular/cellular axes (BDNF/TrkB, E/I, oxidative/mitochondrial, dopaminergic, serotonergic, inflammatory) mapped across MDD/SCZ/BD/anxiety-OCD/PTSD/addiction | Canonical |
| Multiscale biomarkers review | `docs/05-Research/foundational/disease-biotypes/multiscale-biomarkers.md` | Prior-art review of genome-connectome-phenotype linkage studies; positions the platform's multi-scale claim against the literature honestly (effect sizes, replication limits) | Canonical |
| Transdiagnostic MICRO synthesis | `docs/05-Research/foundational/disease-biotypes/transdiagnostic/transdiagnostic-micro.md` | Molecular/genetic/cellular biotypes across 14 disorders, mapped onto the Grotzinger 2025 five-genomic-factor structure, ranked by reproducibility | Canonical |
| Transdiagnostic MESO synthesis | `docs/05-Research/foundational/disease-biotypes/transdiagnostic/transdiagnostic-meso.md` | Connectomic nodes/edges across 14 disorders in Allen Human Reference Atlas terms; includes a machine-readable `VISUAL_DATA` block built for a brain-map visual | Canonical |
| Transdiagnostic MACRO synthesis | `docs/05-Research/foundational/disease-biotypes/transdiagnostic/transdiagnostic-macro.md` | Symptom dimensions across 14 disorders, harmonized to SNOMED CT + HPO, aligned to RDoC/HiTOP/genomic factors | Canonical |
| Transdiagnostic connectomic synthesis | `docs/05-Research/foundational/disease-biotypes/transdiagnostic/transdiagnostic-connectomic-synthesis.md` | The "mental health coordinate map" framing for a wearable/spectroscopy sensing strategy; 6 to 8 region anchor list | Canonical |
| RDoC-HiTOP-disease harmonization | `docs/05-Research/foundational/dimensional/rdoc-harmonization/` (`matrices/`, `reference_tables/`, `README.md`) | 22 machine-readable CSV matrices harmonizing RDoC units of analysis to HiTOP (signed crosswalk) and to a 33-disease MONDO-coded matrix (`matrix_hitop_disease.csv`, `matrix_rdoc_disease.csv`); this is the direct data source for the figure's disorder x construct crosswalk | Canonical |
| Psych-axes synthesis | `docs/05-Research/foundational/dimensional/psych-axes-synthesis.md` | Prose synthesis of RDoC vs HiTOP vs genomic-factor convergence; the "why dimensional, not categorical" narrative for the grant intro | Canonical |
| Neuroanatomy guide | `docs/05-Research/foundational/NEUROANATOMY_GUIDE.md` | Plain-language, one-paragraph-per-region reference for every brain region/network the biotype docs mention; direct input for the educational variant | Canonical |
| Neurosensing dossiers | `docs/05-Research/foundational/neurosensing/{eeg-meg-biotypes,fnirs-optical-update,modality-comparison,molecular-imaging-update,opm-meg-update,targeted-noninvasive-scanning,wearables-comparative}.md` | Modality-specific sensing evidence per biotype; supports the "how would we measure this axis" column | Canonical |
| Neuromodulation-response dossiers | `docs/05-Research/foundational/treatment/neuromodulation/{neuromodulation,neuromodulation-response,neuromodulation-update,neuroplastogen-response}.md` | TMS/tES/LIFU/tVNS response by connectomic biotype; SAINT/dlPFC-sgACC evidence anchors the meso treatment layer | Canonical |
| NbN pharmacology table (populated) | `docs/05-Research/foundational/treatment/neuroplastogens/nbn/{NbN.csv, NbN_extended.csv, NbN_Glossary.md}` | 222-row (+48 extended) drug-level table: NbN pharmacology class, mode of action, target genes/proteins, PubChem/ChEMBL/DrugBank IDs, side effects; glossary maps legacy indication-based terms (antidepressant, anticonvulsant, antipsychotic) to NbN pharmacology classes | Canonical, already populated (see Gap D-1 for the separate empty dataset-repo placeholder) |
| Master dataset curation | `docs/05-Research/cytognosis_master_dataset_curation.md` (+ companion `.xlsx` in `science-platform/`) | Canonical reference for training/eval datasets across the 5 Cytoverse modalities; Section 6 paired-modality matrix is the relevant cross-reference for figure data provenance | Canonical |
| Clinical-instruments crosswalk | `datasets/cytognosis/ontologies/clinical-instruments/` (`SCHEMA.md`, `README.md`, `_MASTER_ontology_mapping.csv`, `tcp/`, `dsm5tr/`) | 111 instruments, 2,399 items, each mapped to HPO, SNOMED CT, LOINC, ICD-10-CM, MeSH, MedDRA, **plus an RDoC construct and a HiTOP dimension column** (columns 13-14 of the 18-column schema); `dsm5tr/` holds the DSM-5-TR Level 1/2 Cross-Cutting Symptom Measures mapping set, the direct DSM-cross-cutting leg of the figure's three-way crosswalk | Canonical |
| RDoC/NeuroMONDO/disease ontology folders | `datasets/cytognosis/ontologies/{rdoc,neuromondo,disease}/` | Placeholder directories (`.gitkeep` only); **empty**. The equivalent live data actually lives in `docs/05-Research/foundational/dimensional/rdoc-harmonization/` (RDoC/HiTOP) and `datasets/cytognosis/science-platform/NeuroMONDO_*` (disease ontology). Treat these three folders as symlink/consolidation targets, not sources | Raw placeholder (empty) |
| NeuroMONDO disease classification | `datasets/cytognosis/science-platform/NeuroMONDO_disease_classification.{tsv,xlsx}` + `NeuroMONDO_xref{,_expanded}.sssom.tsv` | MONDO-coded disease classification (class/subclass/disease/mondo_id) with DOID/HPO xrefs; the disease-identity backbone the RDoC/HiTOP disease matrices key against | Canonical |
| Disease ontology mapping (cell atlas release) | `datasets/cytognosis/science-platform/disease_ontology_mapping_7.1.0.tsv` | Cohort-level MONDO mapping with confidence + notes, tied to the Brain Cell Atlas release | Canonical |
| NeuroSTORM datasets | `datasets/cytognosis/science-platform/NeuroSTORM_datasets.csv` | Pretraining/eval neuroimaging cohorts (UKB, ABCD, HCP-YA, HCP-A, etc.) with sample sizes, citations, access links | Canonical |
| Brain cell atlas + curated cell types | `datasets/cytognosis/science-platform/{braincellatlas_datasets_cellxgene_7.1.0.{tsv,xlsx}, curated_brain_celltypes_enriched.{tsv,xlsx}}` | Cell Ontology-mapped cell-type reference (CL CURIEs), NS-Forest marker sets, BICCN/McLean cross-annotation; the cell-type backbone for the micro/molecular layer | Canonical |
| Master dataset curation workbook | `datasets/cytognosis/science-platform/cytognosis_master_dataset_curation.xlsx` | Structured companion to the master curation doc above (modality x disorder matrices, paired-modality availability) | Canonical |
| Treatments/nbn dataset folder | `datasets/cytognosis/treatments/nbn/` | Placeholder directory, `.gitkeep` only, **empty**. The real NbN table already exists in the docs repo (see row above); this dataset-repo location has not yet been populated/ingested | Raw placeholder (empty) |

---

## (C) Two-variant plan

**One source of truth, two renderings.** Build the figure and its supporting tables once from the
canon above, then render two variants so the science serves both Shahin's own understanding and
external reviewers without diluting either.

| Variant | Audience | Content adjustments | Format notes |
|---|---|---|---|
| **1. Educational / neurodivergent-friendly** | Shahin, internal team | Leads with the `NEUROANATOMY_GUIDE.md` plain-language region cards; simplified 3-axis figure (Mood, Thought, Cognitive) with color-coded confidence (HIGH/MEDIUM/LOW per the shared convention); short paragraphs, one idea per table row, no unexplained jargon | ADHD-friendly: BLUF, bold key terms, tables over prose, reading-time estimate, "if you only read one thing" anchor |
| **2. Grant / review-ready** | Funders, peer reviewers, co-authors | Full formal specs: genomic-factor loadings with effect sizes, DOIs for every claim, confidence ratings with the replication-status caveats already flagged in the transdiagnostic docs (e.g., Dinga 2019 failed replication of Drysdale's 4-cluster solution), explicit uncertainty language (do not overclaim per the BDNF dossier's own flags) | Publishable toward a review paper; follows `cytognosis-doc` skill Literature Synthesis template; Section 5 (factorized PRS) stays out entirely |

Both variants draw from the same underlying disorder x axis x layer table; the educational variant
is a subset view, not a rewrite, so updates to the canon propagate to both without double-maintenance.

---

## (D) Universal dimensional map: figure spec

### D.1 Scope

- **Core disorders**: MDD, BD, SCZ (all three have full per-disorder dossiers, full MICRO/MESO/MACRO
  transdiagnostic coverage, and are jointly anchored by the BDNF/TrkB dossier).
- **Optional extension**: PTSD, anxiety, autism (ASD). All three already have per-disorder dossiers
  and are included in the transdiagnostic MICRO/MESO/MACRO syntheses and the RDoC-HiTOP-disease
  matrices, so extension is a filter change, not new research.

### D.2 Genomic factors (3 to 5 leading factors)

Source: Grotzinger et al., Nature 2025 (doi:10.1038/s41586-025-09820-3), five-factor genomic
structure across 14 disorders, cited in `transdiagnostic-micro.md` Section 1. Use 3 factors for the
core scope, 5 for the extended scope:

| Factor | Disorders in scope | Cell-type signature | DSM cross-cutting / HiTOP / RDoC alignment (via crosswalk) |
|---|---|---|---|
| **SB (schizophrenia + bipolar)** | SCZ, BD | Excitatory neurons | HiTOP Thought Disorder spectrum; RDoC Cognitive Systems + Positive Valence; DSM cross-cutting Psychosis + Mania domains |
| **Internalizing** | MDD, PTSD (optional), anxiety (optional) | Oligodendrocyte/myelin | HiTOP Internalizing/Fear + Internalizing/Distress; RDoC Negative Valence Systems; DSM cross-cutting Depression + Anxiety domains |
| **Neurodevelopmental** | ASD (optional), ADHD (out of core scope, noted for context) | Synaptic/interneuron developmental programs | HiTOP (extended matrix) neurodevelopmental columns; RDoC Cognitive Systems + Social Processes; DSM cross-cutting relevant Level 2 child/parent measures |
| *(extended only)* Compulsive/eating | OCD, anorexia, Tourette | Synaptic/interneuron | HiTOP Thought Disorder-adjacent; not core scope |
| *(extended only)* Substance-use | Alcohol/opioid/nicotine/cannabis UD | Reward-dopaminergic + metabolic | HiTOP Disinhibited/Antagonistic Externalizing; not core scope |

Crosswalk mechanics: pull the disorder columns directly from
`rdoc-harmonization/matrices/matrix_hitop_disease.csv` and `matrix_rdoc_disease.csv` (both already
MONDO-coded and column-aligned to the same 33 disorders), and pull the DSM cross-cutting leg from
`datasets/cytognosis/ontologies/clinical-instruments/dsm5tr/` (Level 1/2 adult/child/parent mapping
files), joining on the shared `rdoc_construct` and `hitop_dimension` columns in
`_MASTER_ontology_mapping.csv`.

### D.3 Treatment layers (micro / meso / macro)

| Layer | Definition | Source dossiers | Example anchors |
|---|---|---|---|
| **Micro** (molecular/cellular) | NbN pharmacology, neuroplastogen mechanisms, EVIDENT-accepted mechanisms | `transdiagnostic-micro.md`; `molecular-cellular-biotypes.md`; `BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md`; `treatment/neuroplastogens/nbn/NbN.csv` + `NbN_Glossary.md` | BDNF/TrkB plasticity-deficit biotype; PV-interneuron E/I biotype; peripheral inflammatory/CRP-high biotype |
| **Meso** (connectomic) | Nodes (e.g., dlPFC, sgACC, anterior insula), edges (e.g., dlPFC-sgACC anticorrelation targeted by SAINT), subgraphs (e.g., default-mode network) | `transdiagnostic-meso.md` (has a machine-readable `VISUAL_DATA` block built for exactly this); `transdiagnostic-connectomic-synthesis.md`; `treatment/neuromodulation/` dossiers | dlPFC-sgACC edge (SAINT, 79% TRD remission); amygdala-vmPFC threat edge; DMN internal edge |
| **Macro** (phenotypic/cross-trial) | Instruments as outcomes, symptom dimensions | `transdiagnostic-macro.md`; clinical-instruments crosswalk (`_MASTER_ontology_mapping.csv`) | PHQ-9, GAD-7, PANSS, YMRS as outcome instruments mapped to RDoC/HiTOP dimensions |

### D.4 Therapeutic-hypothesis grouping

Pull directly from `NbN_Glossary.md` (former indication-based terminology to NbN pharmacology
mapping) and `NbN.csv` (222-row drug-level table): group by legacy indication class
(antidepressants, anticonvulsants/mood stabilizers, antipsychotics, anxiolytics, stimulants) with
each group cross-referenced to its NbN pharmacology class and mode of action, so the figure can show
both "what a clinician calls it" and "what it mechanistically does."

### D.5 Figure build note

The MESO dossier's `VISUAL_DATA` block is purpose-built as machine-readable input for a brain-map
visual; reuse it directly rather than re-deriving node/edge lists from prose.

---

## (E) Gaps and inputs to ingest

| Gap | Status | Placeholder / next step |
|---|---|---|
| **NbN tables not yet ingested into dataset repo** | The NbN pharmacology table (222 rows) already exists and is populated at `docs/05-Research/foundational/treatment/neuroplastogens/nbn/NbN.csv`; the parallel location `datasets/cytognosis/treatments/nbn/` is still an empty `.gitkeep` placeholder | `[TO-INGEST: copy/link NbN.csv + NbN_extended.csv + NbN_Glossary.md into datasets/cytognosis/treatments/nbn/]` |
| **Recent ADHD and depression biotype papers/slides (downloaded ~Jul 11)** | Not found in the repo or datasets tree during this catalog pass; likely on phone or Google Drive, not yet synced | `[TO-INGEST: locate and pull into docs/05-Research/foundational/disease-biotypes/diseases/{adhd,mdd}.md as an update, or a dated addendum]` |
| **Stanford depression-biotypes page** | Not found in the repo; external web source not yet captured | `[TO-INGEST: fetch and cite in mdd.md / transdiagnostic-meso.md alongside the existing Williams iMAP 2024 six-biotype citation]` |
| **ADHD DSM blog** | Not found in the repo; external web source not yet captured | `[TO-INGEST: fetch and cite in adhd.md]` |

None of these four gaps block building the figure for MDD/BD/SCZ core scope; they matter most for
the optional ADHD-adjacent context and for keeping the MDD biotype section current before the
review-paper variant goes out for external eyes.
