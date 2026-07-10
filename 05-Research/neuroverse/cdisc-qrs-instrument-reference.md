> **Status:** Active · **Date:** 2026-05-13 (authored), 2026-07-01 (canonicalized) · **Author:** Cytognosis Foundation
> **Canonical home:** `05-Research/neuroverse/cdisc-qrs-instrument-reference.md` · **Consolidated from:** `Science and Platform/cdisc-qrs-comprehensive-reference.md` (2026-07 Neuroverse consolidation).
> **Companion:** [neurobehavioral-phenotype-feature-space.md](neurobehavioral-phenotype-feature-space.md) (consumes this instrument vocabulary).

# CDISC Questionnaires, Ratings and Scales (QRS): Comprehensive Reference

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

A working reference for the CDISC QRS standard, where its files and supplemental terminology are published, what each psychiatric / behavioural instrument actually measures (including item text where public domain), and how to map QRS instruments and their individual items to external standards: LOINC, SNOMED CT, HPO, MONDO, DOID, ICD-10 / ICD-11, DSM-5-TR, NIH CDEs, RDoC, HiTOP, PROMIS / NIH Toolbox, PhenX, ICF, UMLS, and OMOP / OHDSI.

Author: drafted for Cytognosis Foundation, 2026-05-13. Status: living reference.

---

## 0. TL;DR

CDISC publishes a **QRS Supplement** for each clinical instrument used in regulated trials. Each supplement is a small bundle: an SDTMIG specification (how the instrument is coded into the QS, FT, or RS domain), an instrument-specific Controlled Terminology codelist that ships inside `SDTM Terminology`, an annotated CRF (when copyright allows), and often an ADaMIG analysis supplement.

The QRS terminology itself is **versioned quarterly**, distributed by NCI EVS via anonymous HTTP at `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/`, and exposed programmatically through the **CDISC Library REST API** at `https://library.cdisc.org/api`. Standalone QRS terminology files were retired on 18 December 2015 and folded into `SDTM Terminology`; historical standalone QRS files remain in the FTP archive.

The CDISC catalogue today lists ~500+ supplements at `https://www.cdisc.org/qrs/all`. The supplement is a **mapping specification, not a license**: instruments with copyright (PANSS, MoCA, MMSE, BDI-II / BAI, SF-36 / SF-12, Conners) still require a separate license from the rightsholder; CDISC reflects this through its seven-level permission status field (Public Domain, Exempt from Copyright, Granted, Author Permission Required, No Response Received, Denied, Pending).

For harmonising QRS data across studies, four layers of identifier should be carried in parallel:
- **CDISC QRS code** (e.g., `QSTESTCD = "PHQ0101"`) for SDTM submission;
- **LOINC** at panel, item, and Answer-List granularity for interoperability (FHIR, OMOP);
- **SNOMED CT** for clinical findings (the symptoms / phenotypes implied by each item);
- A **construct tag** in either RDoC (mechanistic), HiTOP (dimensional psychometric), DSM-5-TR / ICD-11 (categorical / regulatory), or a combination, so that downstream analyses can roll up.

The remainder of this document gives the operational detail: where the files live, what each major psychiatric instrument measures item by item, and exactly how those items cross-walk to each external vocabulary.

---

## Part 1. The CDISC QRS Standard

### 1.1 What QRS is

The CDISC Questionnaires, Ratings and Scales (QRS) standard prescribes how clinical-assessment instruments are represented in submission datasets:

- **Questionnaires (QS) domain**: self-administered or clinician-administered named scored instruments (PHQ-9, GAD-7, HAM-D, MADRS, PCL-5).
- **Functional Tests (FT) domain**: performance-based tests (6-Minute Walk, 10-Meter Walk / Run, COWAT, MoCA performance items, MMSE performance items, ADAS-Cog performance components).
- **Disease Response and Clinical Classifications (RS) domain**: clinician-rated structured ratings and classifications (CGI-S / CGI-I, ECOG, Karnofsky, Glasgow Coma, EDSS, AJCC TNM staging, Child-Pugh, PANSS).

The standard also aligns with FDA's Clinical Outcome Assessment (COA) program (PRO, ClinRO, ObsRO, PerfO).

### 1.2 The QRS Supplement bundle

For each instrument CDISC develops a **supplement**, which typically contains:

1. **SDTMIG supplement**: the SDTM-domain-specific specification (which test codes, supplemental qualifiers, and scoring rules apply).
2. **Controlled Terminology codelist** for that instrument: published inside `SDTM Terminology.*` at NCI EVS. Examples:
   - Category codelists: `QSCAT`, `FTCAT`, `RSCAT` (one row per instrument).
   - Test codes / names: `QSTESTCD` / `QSTEST`, `FTTESTCD` / `FTTEST`, `RSTESTCD` / `RSTEST` (one row per item).
   - Result codelists: instrument-specific codelists such as `HAMD17R1`, `CGI1R`, `PHQ9R`, named after the instrument short name plus a suffix.
3. **Annotated CRF** (where copyright permits).
4. **ADaMIG supplement (ADQRS)** with sample analysis datasets and metadata (when applicable).

The test-code naming convention is: `[QRS short name] + numeric or item suffix` (e.g., `PHQ0101` for PHQ-9 item 1, `GAD7-01` style varies by supplement vintage).

### 1.3 Permission Status taxonomy

CDISC tags every supplement with a permission status:

| Status | Meaning |
|--------|---------|
| Public Domain | Free to use the instrument and the CDISC supplement. |
| Exempt from Copyright | Instrument is not under copyright; the rightsholder's terms-of-use policy still applies. |
| Granted | Copyright holder approved CDISC publishing the standardized mapping. **Sponsors still need a separate license from the copyright holder** to administer the instrument. |
| Author Permission Required | CDISC publishes nothing public; users must obtain the supplement directly from the rightsholder. |
| Denied | Rightsholder refused; no CDISC supplement exists. |
| No Response Received | Rightsholder unresponsive; no supplement (current status for several common scales such as YMRS, PSQI, BDI-II historically). |
| Pending | Under review. |

Practical implication: a QRS supplement is a **mapping / scoring specification**, not a license to use instrument text in a CRF, EDC, ePRO, or model-training corpus. Verbatim item wording is included only when the instrument is Public Domain or distribution rights were granted.

For copyrighted instruments outside CDISC coverage, CDISC points users to **Mapi Research Trust's PROQOLID** ( `https://eprovide.mapi-trust.org/` ), which brokers licensing for hundreds of PRO instruments.

---

## Part 2. Access Map: Where Everything Lives

### 2.1 The CDISC web properties

| Source URL | Content | Refresh | Access |
|---|---|---|---|
| `https://www.cdisc.org/standards/questionnaires-ratings-and-scales-qrs` | QRS standards landing page; introduction, principles, FAQs | as needed | free |
| `https://www.cdisc.org/standards/foundational/qrs` | QRS standard description; per-instrument supplement bundles | as supplements ship | free |
| `https://www.cdisc.org/qrs/all` | **Master catalogue** of all 500+ published QRS supplements (name, short name, type, permission, version, date) | continuous | free |
| `https://www.cdisc.org/standards/terminology/controlled-terminology` | CT landing page; **Supplemental Files** tabs (see below) | quarterly | free |
| `https://www.cdisc.org/cdisc-library` | CDISC Library UI; browse standards metadata, run version diffs, export CSV / Excel | continuous | free (cdiscID account); richer for members |
| `https://library.cdisc.org/api` | CDISC Library **REST API**; QRS supplements exposed under Clinical Classification, Functional Testing, and Questionnaires branches | continuous | API key required (free from developer portal) |
| `https://api.developer.library.cdisc.org/` | Library developer portal (API keys, OAS3 spec, usage docs) | continuous | free signup |
| `https://wiki.cdisc.org/display/QRSSUPP/` | QRS development workspace (Team / Internal / Public Review pages, templates, draft supplements) | continuous | free; login for editing |

### 2.2 The CDISC Controlled Terminology page and its tabs

The page `https://www.cdisc.org/standards/terminology/controlled-terminology` ends with a **Supplemental Files** section organized as several tabs. The first tab is **NCI FTP Links**, which is the canonical distribution channel. Subsequent tabs typically include CDISC Library links (for paying members), archive tarballs, and a Changes Tracker.

The most current quarterly release seen on the FTP is **2026-03-27** (carrying roughly 248 new QRS terms among ~1,124 new terms across ADaM, CDASH, DDF, Define-XML, SDTM, and SEND). Quarterly releases land at the end of March, June, September, and December.

### 2.3 NCI EVS FTP folder tree

Root: `https://evs.nci.nih.gov/ftp1/CDISC/`

```
/ftp1/CDISC/
  ADaM/
    ADaM Terminology.{xls, txt, html, odm.xml, pdf, OWL.zip}
    ADaM Terminology Changes.{txt, xls}
    ADaM Publication Date Stamp.txt
    ADaM CDISC ReadMe.doc
    ReadMe.txt
    Archive/           (all prior ADaM CT releases by date)
  SDTM/
    SDTM Terminology.{xls, txt, html, odm.xml, pdf, OWL.zip}    *** contains all QRS codelists ***
    SDTM Terminology Changes.{txt, xls}
    SDTM Publication Date Stamp.txt
    SDTM CDISC ReadMe.doc
    ReadMe.txt
    Archive/
      SDTM Terminology YYYY-MM-DD.{xls, txt, html, odm.xml, pdf, OWL.zip}    (every quarterly release)
      QRS Terminology 2015-06-26.{...}            (legacy, pre-merge)
      QRS Terminology 2015-09-25.{...}            (final standalone QRS file)
      CDASH / COA legacy files
  CDASH/, SEND/, DDF/, Define-XML/, Glossary/,
  MRCT Center Clinical Research Glossary/,
  Protocol/, TMF/                                  (same Current + Archive pattern)
  schema/, xsl/                                    (technical XML schemas)
  Archive/
    Questionnaire/Archive/
      QS CDISC ReadMe 2012-03-23.doc, 2012-12-21.doc
      QS-FT CDISC ReadMe 2014-06-27.doc
      QS Terminology {2012-03-23, 2012-06-29, 2012-08-03, 2012-12-21,
                      2013-04-12, 2013-06-28, 2013-10-04, 2013-12-20, 2014-03-28}
        in .html, .odm.xml, .pdf, .txt, .xls (+ .OWL.zip from 2013-06-28 onward)
      QS-FT Terminology {2014-06-27, 2014-09-26} in all formats
      QS Terminology Changes (per release), QS Publication Date Stamp files
  ControlledTerminologyODM.pdf, ControlledTerminologyODM_v1.pdf
  Change Request Tracker.xls
  ReadMe.txt
```

Notes:
- The root `ReadMe.txt` documents the **18 December 2015 deprecation** of the standalone QRS terminology file and the move into `SDTM Terminology`.
- "Latest" files are the unsuffixed `*Terminology.*` at the top of each standard folder; dated versions live in `Archive/`.
- For programmatic ingest, the `.odm.xml` (Define-XML ODM 1.3) format is the most structured; `.OWL.zip` is for ontology tooling; `.xls` is the analyst's working copy.

### 2.4 Concrete file names at the SDTM FTP (2026-03-27 release)

- `SDTM Terminology.xls` (~12 MB), `.txt` (~13 MB), `.html` (~20 MB), `.odm.xml` (~24 MB), `.pdf` (~5.4 MB), `.OWL.zip` (~2.3 MB)
- `SDTM Terminology Changes.txt` (~341 KB), `.xls` (~4.6 MB)
- `SDTM CDISC ReadMe.doc`, `SDTM Publication Date Stamp.txt`, `ReadMe.txt`

### 2.5 The CDISC Library REST API

Base: `https://library.cdisc.org/api`. Default JSON; supports XML, ODM, CSV, Excel via Accept-header or `?format=` parameter. Path syntax: versions use dashes (e.g., `/mdr/sdtm/1-6`), case-sensitive, no trailing slashes.

QRS supplements are exposed under three branches: Clinical Classification (RS), Functional Testing (FT), and Questionnaires (QS). Each supplement is retrievable with codelist metadata, item lists, and example mappings.

Getting-started guide: `https://wiki.cdisc.org/display/LIBSUPRT/Getting+Started:+Programmatically+connect+to+CDISC+Library+API`.

### 2.6 When to grab what

| Need | Get this | From here |
|------|----------|-----------|
| Build an ETL parser for one trial's QS / FT / RS data | The instrument's QRS Supplement (PDF + Define-XML fragment) | `cdisc.org/qrs/all` |
| Programmatic catalogue ingestion | CDISC Library API JSON dumps | `library.cdisc.org/api` |
| Quarterly CT diff for change control | `SDTM Terminology Changes.xls` | NCI EVS FTP |
| Authoritative codelist values | `SDTM Terminology.xls` or `.odm.xml` | NCI EVS FTP |
| Older / retired QRS terminology snapshots | Archive folder | NCI EVS FTP `Archive/` |
| Ontology integration via OWL | `SDTM Terminology.OWL.zip` | NCI EVS FTP |
| Drafts and team review | Wiki workspace | `wiki.cdisc.org/display/QRSSUPP/` |
| Licensed instrument item text | Mapi Trust ePROVIDE / PROQOLID | `eprovide.mapi-trust.org` |

---

## Part 3. Catalogue of Published QRS Supplements (Selected)

The full catalogue is at `https://www.cdisc.org/qrs/all` (~500+ rows). A representative slice across therapeutic areas follows. Items in **bold** are covered in detail in Part 4.

### Psychiatry, depression, anxiety, suicidality

- **Patient Health Questionnaire-9 (PHQ-9)**, Exempt from Copyright, v2.0 (29 May 2023)
- **Generalized Anxiety Disorder-7 (GAD-7 V2)**, Exempt from Copyright, v1.0 (29 Aug 2022)
- **Hamilton Depression Rating Scale (HAMD-17 / 21 / 24)**, Public Domain, v2.1 (21 Apr 2026)
- **Hamilton Anxiety Rating Scale (HAMA)**, Public Domain, v2.1 (19 May 2020)
- **Clinical Global Impression (CGI-S / CGI-I)**, Public Domain, v2.1
- **Brief Psychiatric Rating Scale, Anchored (BPRS-A)**, Public Domain
- **Columbia Suicide Severity Rating Scale (C-SSRS Baseline / Baseline-Screening / Already Enrolled)**, Granted
- **PANSS**, Granted (licensed via MHS)
- Covi Anxiety Scale (COVI), Public Domain
- Beck Depression Inventory II (BDI-II), No Response Received
- Young Mania Rating Scale (YMRS), No Response Received
- Pittsburgh Sleep Quality Index (PSQI), No Response Received
- Abnormal Involuntary Movement Scale (AIMS), Public Domain
- Barnes Akathisia Rating Scale (BARS), Public Domain
- Children's Depression Rating Scale, Revised (CDRS-R), Granted (18 Feb 2025)
- Combat Exposure Scale (CES), Public Domain

### Neurology / cognition

- **Mini-Mental State Examination (MMSE)**, v1.0 (12 Dec 2024)
- Unified Parkinson's Disease Rating Scale (UPDRS), v2.0 (29 Aug 2022)
- Glasgow Coma Scale (GCS), v2.0 (27 Feb 2023)
- Kurtzke Expanded Disability Status Scale (EDSS), v2.0 (21 Nov 2024)
- Alzheimer's Disease Assessment Scale, Cognitive (ADAS-Cog 11 / 13), Granted
- ADCS-ADL MCI, Granted
- Brooke Upper Extremity Rating Scale (BUERS), Public Domain
- Controlled Oral Word Association Test (COWAT), Public Domain (21 Sep 2021)
- Brief Assessment of Cognition in Schizophrenia (BACS), Granted (1 Mar 2015)

### Oncology / performance status / staging

- ECOG Performance Status, v1.2 (23 Jan 2024)
- Karnofsky Performance Scale (KPS), v2.0 (3 Apr 2021)
- AJCC TNM 7th Edition (AJCC V7), Granted (28 Jun 2024)
- EORTC QLQ-C30 V3, v1.0 (11 Mar 2025)

### Quality of life / generic PRO

- EQ-5D-5L, v1.3 (31 May 2022); EQ-5D-3L
- SF-36, SF-12 (Optum / QualityMetric license)
- WHOQOL-BREF
- Brief Pain Inventory (BPI) and BPI Short Form, Granted

### Respiratory / cardiology / hepatology

- Airway Questionnaire (AQ20), Granted
- Baseline Dyspnea Index (BDI), Granted
- BODE Index, Public Domain
- Borg CR-10 Scale (BORG CR10), Granted
- Clinical COPD Questionnaire 1 Week / 24 Hour (CCQ), Granted
- Asthma Daytime / Nighttime Symptom Diary (ADSD, ANSD), Granted (27 Aug 2024)
- Chronic Respiratory Questionnaire (CRQ-SAS), Author Permission Required
- ASCVD 10-Year Risk, Public Domain
- ASSIGN CVD 10-Year Risk, Public Domain
- Child-Pugh Classification, Public Domain
- Acute Physiology and Chronic Health Evaluation II (APACHE II), Public Domain

### Substance use / sexual function / GU

- AUDIT-C, AUDIT-SR, Public Domain
- Arizona Sexual Experiences Scale (ASEX Female / Male), Granted
- Bladder Control Scale (BLCS), Bowel Control Scale (BWCS), Granted

### Functional tests / movement

- 6 Minute Walk Test, Public Domain (21 May 2014)
- 10-Meter Walk / Run, Public Domain (18 Jan 2022)
- 4-Stair Ascend / 4-Stair Descend, Public Domain (30 Sep 2024)

### Pediatrics

- Comfort Behavior Scale (COMFORT-B), Granted (28 Jun 2024)

### Infectious disease

- CDC Classification System for HIV, Public Domain

---

## Part 4. Psychiatric Instruments: Item-Level Deep Dive

Each entry below gives: construct, format, scoring bands, population, copyright, CDISC code, LOINC anchors, **verbatim items when public domain or otherwise widely cleared for reproduction**, and key notes.

### 4.1 PHQ-9 (Patient Health Questionnaire-9)

- **Construct**: Major depressive symptoms aligned to DSM-IV / DSM-5 Criterion A.
- **Items / format**: 9 symptom items + 1 functional-impairment item; self-report; 4-point Likert (0 Not at all, 1 Several days, 2 More than half the days, 3 Nearly every day); recall window = past 2 weeks.
- **Scoring**: Sum 0 to 27. Bands: 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 moderately severe, 20–27 severe. Cutoff ≥10 for probable MDD (sens ~88%, spec ~88%).
- **Population**: Adolescents (age ≥12) and adults; primary care, psychiatry, general medical.
- **Copyright**: Developed by Spitzer, Williams, Kroenke (Pfizer educational grant). Free to reproduce, no permission required. Distributed by `https://www.phqscreeners.com`.
- **CDISC QRS code**: PHQ-9 (QS domain, v2.0; Exempt from Copyright).
- **LOINC**:
  - Panel: `44249-1` (PHQ-9 quick depression assessment panel)
  - Total: `44261-6` (PHQ-9 total score)
  - Items: `44250-9` (Q1), `44255-8` (Q2), `44259-0` (Q3), `44254-1` (Q4), `44251-7` (Q5), `44258-2` (Q6), `44252-5` (Q7), `44253-3` (Q8), `44260-8` (Q9), `69722-7` (functional impairment item)
  - Answer List: `LL358-3` (LA6568-5, LA6569-3, LA6570-1, LA6571-9)
  - Interpretation Answer List: `LL382-3`
- **Items (verbatim, public domain). Over the last 2 weeks, how often have you been bothered by any of the following problems?**
  1. Little interest or pleasure in doing things
  2. Feeling down, depressed, or hopeless
  3. Trouble falling or staying asleep, or sleeping too much
  4. Feeling tired or having little energy
  5. Poor appetite or overeating
  6. Feeling bad about yourself, or that you are a failure or have let yourself or your family down
  7. Trouble concentrating on things, such as reading the newspaper or watching television
  8. Moving or speaking so slowly that other people could have noticed; or the opposite, being so fidgety or restless that you have been moving around a lot more than usual
  9. Thoughts that you would be better off dead or of hurting yourself in some way
- **Reference**: Kroenke, Spitzer, Williams (2001) JGIM 16:606.
- **Notes**: Item 9 is a regulatory-relevant suicidality flag; if endorsed, escalate to C-SSRS.

### 4.2 PHQ-2 and PHQ-8

- **PHQ-2**: First 2 PHQ-9 items (depressed mood + anhedonia). Cutoff ≥3 triggers full PHQ-9 (sens 83%, spec 92%). LOINC panel `55758-7`, total `58148-8`.
- **PHQ-8**: PHQ-9 minus item 9 (suicidality). Used in epidemiologic surveys (BRFSS). LOINC total `73831-0`.

### 4.3 PHQ-15 (somatic symptom severity)

- 15 somatic complaints (stomach pain, back pain, chest pain, dizziness, fatigue, sleep, headaches, etc.); 3-point Likert (0–2); 4-week recall.
- Total 0–30; cutoffs 5 / 10 / 15 = mild / moderate / severe.
- LOINC panel: `71967-4`. Public domain (Pfizer grant; Kroenke 2002).

### 4.4 GAD-7 (Generalized Anxiety Disorder 7)

- **Construct**: Generalized anxiety symptoms; also screens panic, social anxiety, PTSD reasonably well.
- **Items / format**: 7 items; 4-point Likert (0–3); recall = past 2 weeks.
- **Scoring**: 0–21. Bands: 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe. Cutoff ≥10 (sens 89%, spec 82%).
- **Population**: Adults; primary care.
- **Copyright**: Public domain (Spitzer, Kroenke, Williams, Löwe; Pfizer grant, Arch Intern Med 2006;166:1092).
- **CDISC QRS code**: GAD-7 V2 (QS / ADaM v1.0; Exempt from Copyright).
- **LOINC**:
  - Panel: `69737-5`
  - Total: `70274-6`
  - Items: `69725-0` (Q1), `69726-8` (Q2), `69727-6` (Q3), `69728-4` (Q4), `69729-2` (Q5), `69730-0` (Q6), `69731-8` (Q7)
- **Items (verbatim, public domain). Over the last 2 weeks, how often have you been bothered by the following problems?**
  1. Feeling nervous, anxious, or on edge
  2. Not being able to stop or control worrying
  3. Worrying too much about different things
  4. Trouble relaxing
  5. Being so restless that it is hard to sit still
  6. Becoming easily annoyed or irritable
  7. Feeling afraid, as if something awful might happen

### 4.5 BPRS (Brief Psychiatric Rating Scale)

- 18-item Overall & Gorham (1962) or 24-item expanded (BPRS-E, Lukoff / Ventura). Clinician-rated 1–7 (not present to extremely severe).
- 18-item sum 18–126; 24-item 24–168. No fixed severity cutoffs; commonly used to track symptom change.
- Public domain (original 18-item).
- Items (BPRS-18): Somatic concern; Anxiety; Emotional withdrawal; Conceptual disorganization; Guilt feelings; Tension; Mannerisms and posturing; Grandiosity; Depressive mood; Hostility; Suspiciousness; Hallucinatory behaviour; Motor retardation; Uncooperativeness; Unusual thought content; Blunted affect; Excitement; Disorientation.
- BPRS-18 is the precursor to PANSS; many BPRS items appear in PANSS-G.

### 4.6 PANSS (Positive and Negative Syndrome Scale)

- **Construct**: Schizophrenia symptom severity across Positive (P1–P7), Negative (N1–N7), and General Psychopathology (G1–G16) dimensions.
- **Items / format**: 30 items, clinician-rated semi-structured interview; each item 1 (absent) to 7 (extreme); recall ~7 days. Administration ~45–50 min.
- **Scoring**: Total 30–210; P-scale 7–49; N-scale 7–49; G-scale 16–112. Composite = positive minus negative. Severity bands (Leucht et al.): ~58 mildly ill, 75 moderately, 95 markedly, 116 severely ill.
- **Population**: Adults with schizophrenia spectrum disorders.
- **Copyright**: Licensed via Multi-Health Systems (MHS); fee required. PANSS-6 (Østergaard) is a brief subset used royalty-free in some research contexts.
- **CDISC QRS code**: PANSS (RS domain, v1.0; Granted).
- **LOINC**: Panel + individual items registered (e.g., panel-level codes in the 89205-x range; verify current LOINC version).
- **Items (NOT verbatim; structural list)**:
  - Positive (P1 Delusions, P2 Conceptual disorganization, P3 Hallucinatory behaviour, P4 Excitement, P5 Grandiosity, P6 Suspiciousness / persecution, P7 Hostility);
  - Negative (N1 Blunted affect, N2 Emotional withdrawal, N3 Poor rapport, N4 Passive / apathetic social withdrawal, N5 Abstract thinking difficulty, N6 Lack of spontaneity / flow of conversation, N7 Stereotyped thinking);
  - General (G1 Somatic concern, G2 Anxiety, G3 Guilt feelings, G4 Tension, G5 Mannerisms / posturing, G6 Depression, G7 Motor retardation, G8 Uncooperativeness, G9 Unusual thought content, G10 Disorientation, G11 Poor attention, G12 Lack of judgement / insight, G13 Disturbance of volition, G14 Poor impulse control, G15 Preoccupation, G16 Active social avoidance).
- **Reference**: Kay, Fiszbein, Opler (1987) Schizophr Bull 13:261. Rater certification typically required for trials.

### 4.7 HAM-D / HDRS (Hamilton Depression Rating Scale)

- 17-item canonical (HDRS-17); 21- and 24-item extended versions exist. Item scales vary (0–4 or 0–2). Clinician interview; recall = past week.
- HDRS-17 total 0–52. Bands: 0–7 normal, 8–13 mild, 14–18 moderate, 19–22 severe, ≥23 very severe. Response = ≥50% reduction; remission ≤7.
- Public domain (Hamilton 1960 J Neurol Neurosurg Psychiatry 23:56).
- CDISC QRS code: HAMD (RS / ADaM; v2.1 / v1.0; Public Domain) covering 17, 21, 24-item versions.
- LOINC: panel `89204-8` and individual item codes registered. The GRID-HAMD standardized variant has separate item conventions.
- **Items (verbatim, public domain)**: (1) Depressed mood; (2) Feelings of guilt; (3) Suicide; (4) Insomnia early; (5) Insomnia middle; (6) Insomnia late; (7) Work and activities; (8) Retardation (psychomotor); (9) Agitation; (10) Anxiety psychic; (11) Anxiety somatic; (12) Somatic symptoms gastrointestinal; (13) Somatic symptoms general; (14) Genital symptoms; (15) Hypochondriasis; (16) Loss of weight; (17) Insight. Items 18–24 (extended): diurnal variation, depersonalization / derealization, paranoid symptoms, obsessional / compulsive, helplessness, hopelessness, worthlessness.
- Criticized for heavy weighting of somatic / sleep items relative to mood, which partly motivated MADRS.

### 4.8 HAM-A (Hamilton Anxiety Rating Scale)

- 14 items; each 0–4. Roughly half psychic, half somatic anxiety. Past-week recall.
- 0–56. Bands: ≤17 mild, 18–24 mild-moderate, 25–30 moderate-severe.
- Public domain (Hamilton 1959).
- CDISC code: HAM-A (RS v2.1; Public Domain).
- **Items**: Anxious mood; Tension; Fears; Insomnia; Intellectual (cognitive); Depressed mood; Somatic muscular; Somatic sensory; Cardiovascular symptoms; Respiratory symptoms; Gastrointestinal symptoms; Genitourinary symptoms; Autonomic symptoms; Behaviour at interview.

### 4.9 MADRS (Montgomery-Åsberg Depression Rating Scale)

- **Construct**: Depression severity, designed to be sensitive to treatment change.
- **Items / format**: 10 items; each scored 0–6 (anchors at 0, 2, 4, 6 with intermediate 1, 3, 5); clinician interview (MADRS-S is the patient-reported version); past-week recall.
- **Scoring**: 0–60. Bands: 0–6 normal, 7–19 mild, 20–34 moderate, 35–60 severe. Remission ≤10; response = ≥50% reduction.
- **Population**: Adults with MDD / bipolar depression. The predominant scale in modern antidepressant and ketamine / esketamine trials.
- **Copyright**: Public domain with attribution (Montgomery & Åsberg 1979 Br J Psychiatry 134:382). Translations licensed via Mapi.
- **CDISC QRS code**: MADRS (status varies historically).
- **LOINC**: Panel and total registered.
- **Items (public domain)**: (1) Apparent sadness; (2) Reported sadness; (3) Inner tension; (4) Reduced sleep; (5) Reduced appetite; (6) Concentration difficulties; (7) Lassitude; (8) Inability to feel; (9) Pessimistic thoughts; (10) Suicidal thoughts.

### 4.10 YMRS (Young Mania Rating Scale)

- 11 clinician-rated items. Seven items scored 0–4; four items (Irritability, Speech, Thought Content, Disruptive / Aggressive Behaviour) double-weighted 0–8. Recall ~48 hours.
- Total 0–60. Cutoffs: ≤11 remission, 12–25 mild, 26–37 moderate, ≥38 severe.
- Public domain (Young, Biggs, Ziegler, Meyer 1978 Br J Psychiatry 133:429).
- **Items (public domain)**: (1) Elevated mood; (2) Increased motor activity / energy; (3) Sexual interest; (4) Sleep; (5) Irritability\*; (6) Speech (rate & amount)\*; (7) Language / thought disorder; (8) Content\*; (9) Disruptive / aggressive behaviour\*; (10) Appearance; (11) Insight. (\* double-weighted)

### 4.11 C-SSRS (Columbia Suicide Severity Rating Scale)

- **Construct**: Suicidal ideation and behaviour, with frequency, intensity, severity, lethality.
- **Items / format**: Semi-structured interview; multiple versions (Baseline / Screening, Since Last Visit, Children's, Cognitively Impaired). Yes / No screen items plus open-ended.
- **Scoring**: Ideation severity 1–5 (wish to be dead → active intent with plan). Behaviour tally (actual, interrupted, aborted attempts; preparatory acts; suicidal / self-injurious behaviour without intent). Lethality 0–5 (medical).
- **Population**: All ages (≥6 with pediatric versions).
- **Copyright**: Owned by The Research Foundation for Mental Hygiene / Columbia. Free for clinical / non-commercial use after brief registration at `https://cssrs.columbia.edu`. Required by FDA for any trial with suicidality risk since 2012 (FDA Draft Guidance).
- **CDISC QRS code**: C-SSRS (QS v1.0 to 1.2; Granted). Separate supplements for Baseline, Since-Last-Visit, Children's.
- **LOINC**:
  - `93373-9` C-SSRS Screener Recent
  - `93245-9` C-SSRS Lifetime / Recent
  - `93485-1` C-SSRS Very Young Child / Cognitively Impaired
- **Items (verbatim screener, publicly available)**:
  1. Have you wished you were dead or wished you could go to sleep and not wake up?
  2. Have you actually had any thoughts of killing yourself?
  3. Have you been thinking about how you might do this? (method)
  4. Have you had these thoughts and had some intention of acting on them?
  5. Have you started to work out or worked out the details of how to kill yourself? Do you intend to carry out this plan?
  6. Have you ever done anything, started to do anything, or prepared to do anything to end your life? If yes, how long ago did you do any of these?
- Reference: Posner et al. 2011 Am J Psychiatry 168:1266. The C-CASA classification framework underlies it.

### 4.12 Y-BOCS (Yale-Brown Obsessive Compulsive Scale)

- 10 clinician-rated items across 5 dimensions (time, interference, distress, resistance, control) × 2 symptom types (obsessions 1–5, compulsions 6–10). Each item 0–4. Plus a Symptom Checklist (~58 items) for OC content.
- Total 0–40 (obsessions 0–20, compulsions 0–20). Bands: 0–7 subclinical, 8–15 mild, 16–23 moderate, 24–31 severe, 32–40 extreme. Response = ≥25–35% reduction.
- Goodman, Rasmussen, Price et al. 1989 Arch Gen Psychiatry 46:1006. Free for clinical / research use; Y-BOCS-II (2006) is more recent.
- CY-BOCS for children.
- **Items (public summary)**: Q1 time occupied by obsessions; Q2 interference from obsessions; Q3 distress from obsessions; Q4 resistance against obsessions; Q5 control over obsessions; Q6–Q10 same five ratings applied to compulsions.

### 4.13 PCL-5 (PTSD Checklist for DSM-5)

- 20 self-report items; 0 (Not at all) to 4 (Extremely); recall = past month (standard) or past week (weekly). Optional LEC-5 trauma index.
- Total 0–80. Provisional PTSD: ≥1 B (Q1–5), ≥1 C (Q6–7), ≥2 D (Q8–14), ≥2 E (Q15–20) items rated ≥2. Probable PTSD cutoff: 31–33. Clinically meaningful change ~10 points.
- Public domain (US Government work, VA National Center for PTSD); free at `https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp`.
- CDISC QRS code: PCL-5 (QS / ADaM v1.0; Public Domain).
- LOINC: PCL-5 panel and items registered.
- **Items (verbatim, public domain). In the past month, how much were you bothered by:**
  1. Repeated, disturbing, and unwanted memories of the stressful experience
  2. Repeated, disturbing dreams of the stressful experience
  3. Suddenly feeling or acting as if the stressful experience were actually happening again
  4. Feeling very upset when something reminded you of the stressful experience
  5. Having strong physical reactions when something reminded you of the stressful experience
  6. Avoiding memories, thoughts, or feelings related to the stressful experience
  7. Avoiding external reminders of the stressful experience
  8. Trouble remembering important parts of the stressful experience
  9. Having strong negative beliefs about yourself, other people, or the world
  10. Blaming yourself or someone else for the stressful experience or what happened after it
  11. Having strong negative feelings such as fear, horror, anger, guilt, or shame
  12. Loss of interest in activities that you used to enjoy
  13. Feeling distant or cut off from other people
  14. Trouble experiencing positive feelings
  15. Irritable behaviour, angry outbursts, or acting aggressively
  16. Taking too many risks or doing things that could cause you harm
  17. Being "superalert" or watchful or on guard
  18. Feeling jumpy or easily startled
  19. Having difficulty concentrating
  20. Trouble falling or staying asleep

### 4.14 CAPS-5 (Clinician-Administered PTSD Scale for DSM-5)

- 30 items: 20 DSM-5 symptom items rated for frequency + intensity combined as 0–4 severity, plus onset / duration, subjective distress, social / occupational impairment, validity, global severity, global improvement, and dissociative subtype indicators. ~45–60 min.
- Diagnosis follows DSM-5 algorithm.
- Public domain (VA NCPTSD); brief registration required.
- CAPS-CA-5 for children / adolescents.

### 4.15 BDI-II and BAI (Beck Inventories)

- BDI-II: 21 items, 0–3, past 2 weeks. 0–13 minimal, 14–19 mild, 20–28 moderate, 29–63 severe. **Proprietary (Pearson Assessment)**, license fee per administration.
- BAI: 21 items, 0–3, past week. 0–7 minimal, 8–15 mild, 16–25 moderate, 26–63 severe. Proprietary (Pearson).
- CDISC has no open supplement; LOINC has no per-item codes due to copyright.

### 4.16 EPDS (Edinburgh Postnatal Depression Scale)

- 10 self-report items; 0–3 (with reverse scoring on items 3, 5–10); past 7 days.
- 0–30. Cutoff ≥10 possible, ≥13 probable. Item 10 = self-harm / suicidality flag.
- Cox, Holden, Sagovsky 1987 Br J Psychiatry 150:782. Royal College of Psychiatrists holds copyright; free for non-commercial clinical use with attribution.
- LOINC panel: `71354-5`.

### 4.17 MMSE (Mini-Mental State Examination)

- 30-point clinician-administered exam; orientation (10), registration (3), attention / calculation (5), recall (3), language and praxis (9).
- 24–30 normal, 18–23 mild impairment, 0–17 severe (education-adjusted norms).
- Folstein, Folstein, McHugh 1975. **Owned by PAR Inc since 2001; licensing required.**
- CDISC code: MMSE v1.0 (FT / QS, Dec 2024).
- LOINC: panel `72106-8`, total `72172-0`.

### 4.18 MoCA (Montreal Cognitive Assessment)

- 30-point clinician-administered exam: visuospatial / executive (5), naming (3), attention (6), language (3), abstraction (2), delayed recall (5), orientation (6). +1 if ≤12 years education.
- <26 = MCI (original cutoff); revised guidance suggests 23 for better specificity in some populations.
- Nasreddine 2005. **Owned by MoCA Test Inc; mandatory certification (paid) since September 2020.**
- LOINC panel: `72133-2`.

### 4.19 ADAS-Cog

- 11-item original (ADAS-Cog 11), expanded 13 and 14. Includes word recall, naming, commands, constructional praxis, ideational praxis, orientation, word recognition, language ability, comprehension, word-finding difficulty, recall of instructions (+ delayed recall, number cancellation in v13 / 14).
- ADAS-Cog 11: 0–70 (higher = worse); ADAS-Cog 13: 0–85.
- Rosen, Mohs, Davis 1984. Distributed via trial-sponsor consortia and Mapi.
- CDISC supplements available for ADAS-Cog 11 and 13.

### 4.20 AIMS (Abnormal Involuntary Movement Scale)

- 12 clinician-rated items: 7 movement severity items (face / oral / extremity / trunk), 3 global judgements (severity, incapacitation, patient awareness), 2 dental items. Each movement item 0 (none) to 4 (severe).
- Sum of items 1–7 (0–28); Schooler-Kane criteria for "probable" tardive dyskinesia.
- Public domain (NIMH, Guy 1976 ECDEU Assessment Manual).
- CDISC code: AIMS v2.0 (Public Domain).

### 4.21 ESRS (Extrapyramidal Symptom Rating Scale)

- ESRS (Chouinard 1980) and ESRS-A (abbreviated 2005). Multi-part: parkinsonism questionnaire, parkinsonism exam, dystonia, dyskinesia, akathisia, plus CGI per category.
- Chouinard & Margolese 2005; permission required for trials.
- No open CDISC supplement.

### 4.22 CGI-S / CGI-I (Clinical Global Impression)

- Each is a single 7-point clinician rating.
  - **CGI-S**: 1 normal; 2 borderline ill; 3 mildly ill; 4 moderately ill; 5 markedly ill; 6 severely ill; 7 among the most extremely ill (relative to clinician's experience with the disease population).
  - **CGI-I**: 1 very much improved; 2 much improved; 3 minimally improved; 4 no change; 5 minimally worse; 6 much worse; 7 very much worse (relative to baseline).
- Public domain (Guy 1976 NIMH ECDEU Manual).
- CDISC code: CGI (QS / ADaM v2.1 / v1.1; Public Domain).
- Universally paired with disease-specific scales (HAM-D, MADRS, PANSS, YMRS, Y-BOCS, PCL-5) as a global anchor.

### 4.23 WHODAS 2.0 (WHO Disability Assessment Schedule)

- 6 domains (Cognition, Mobility, Self-care, Getting along, Life activities, Participation).
- 36-item (full) and 12-item short; self-, proxy-, or interviewer-administered; 30-day recall; 5-point Likert (none–extreme).
- Simple sum (0–144 for 36-item) or IRT scoring producing 0–100 normalized score.
- WHO, free with attribution.
- LOINC: `75274-1` WHODAS panel.

### 4.24 SF-36 / SF-12

- 8 domains: Physical Functioning, Role-Physical, Bodily Pain, General Health, Vitality, Social Functioning, Role-Emotional, Mental Health; aggregated into Physical (PCS) and Mental (MCS) Component Summaries.
- SF-36 v2 = 36 items; SF-12 v2 = 12 items; recall = 4 weeks (standard) or 1 week (acute).
- Norm-based 0–100 (or T-score mean 50, SD 10). Requires licensed scoring algorithm.
- Optum (formerly QualityMetric). License required.
- CDISC: SF-36 and SF-12 supplements published.
- LOINC: `62393-7` SF-36 panel.

### 4.25 WHOQOL-BREF

- 4 domains: physical, psychological, social relationships, environment.
- 26 items; 5-point Likert; 2-week recall.
- Domain scores transformed to 0–100. No total score.
- WHO; free for non-commercial use with permission.

### 4.26 EQ-5D-3L / EQ-5D-5L

- 5 descriptive items (Mobility, Self-Care, Usual Activities, Pain / Discomfort, Anxiety / Depression), each 3 levels (3L) or 5 levels (5L), plus EQ VAS (0–100, "today's health").
- Health state coded as 5-digit string; country-specific value sets convert to single utility index (often −0.5 to 1.0). EQ VAS scored separately.
- EuroQol Group; registration required (free academic / non-commercial; fee commercial).
- CDISC: EQ-5D-3L and EQ-5D-5L supplements published (Granted).
- LOINC: EQ-5D-5L panel `96538-3`.

### 4.27 ASRS (Adult ADHD Self-Report Scale)

- 18 items mapped to DSM-IV / 5 inattention + hyperactivity-impulsivity. ASRS-v1.1 Screener (Part A) uses 6 items with weighted Likert and shaded-box scoring.
- Screener: ≥4 darkened boxes = highly consistent with adult ADHD.
- Free; developed for WHO by Kessler et al.
- LOINC panel: `78033-5`.

### 4.28 Conners CBRS / Conners 3, SNAP-IV

- Conners 3: parent (110 items), teacher (115), self-report ages 8–18 (99). T-scores normed. **MHS Inc; licensed.**
- SNAP-IV: 26 items (or extended 90); 4-point Likert. Public domain. Inattention (1–9), hyperactivity-impulsivity (10–18), ODD (19–26).

### 4.29 AUDIT and DUDIT

- **AUDIT**: 10 items by WHO; 1–8 scored 0–4, 9–10 scored 0/2/4; past-year recall.
  - 0–7 low risk, 8–14 hazardous / harmful, 15–19 likely dependence, ≥20 severe dependence.
  - AUDIT-C = first 3 items, 0–12.
  - WHO public domain (Babor 2001).
  - LOINC: panel `75624-7`, total `75626-2`, AUDIT-C panel `75618-9`.
  - **Items (verbatim, WHO 2001)**:
    1. How often do you have a drink containing alcohol?
    2. How many drinks containing alcohol do you have on a typical day when you are drinking?
    3. How often do you have six or more drinks on one occasion?
    4. How often during the last year have you found that you were not able to stop drinking once you had started?
    5. How often during the last year have you failed to do what was normally expected from you because of drinking?
    6. How often during the last year have you needed a first drink in the morning to get yourself going after a heavy drinking session?
    7. How often during the last year have you had a feeling of guilt or remorse after drinking?
    8. How often during the last year have you been unable to remember what happened the night before because you had been drinking?
    9. Have you or someone else been injured as a result of your drinking?
    10. Has a relative or friend, or a doctor or other health worker, been concerned about your drinking or suggested you cut down?
- **DUDIT**: 11 items; same scoring shape. Berman, Bergman, Palmstierna, Schlyter 2005. Free with attribution.

### 4.30 ISI and PSQI

- **ISI**: 7 self-report items; 5-point Likert (0–4); 2-week recall. 0–7 no insomnia, 8–14 subthreshold, 15–21 moderate, 22–28 severe. Bastien, Vallières, Morin 2001. Permission via the authors. LOINC panel `89218-8`.
- **PSQI**: 19 self-rated items + 5 partner items; past month. 7 component scores; global 0–21; >5 = poor sleep. Buysse 1989. Permission via University of Pittsburgh.

### 4.31 ECOG and Karnofsky

- **ECOG**: Single clinician rating 0–5: 0 fully active; 1 restricted in strenuous activity, ambulatory; 2 capable of self-care, unable to work; 3 limited self-care, confined to bed / chair >50% waking hours; 4 completely disabled; 5 dead. Public domain (Oken 1982). LOINC `89262-6`.
- **Karnofsky**: 0–100 in 10-point increments (100 normal, 0 dead). Public domain (Karnofsky 1948). LOINC `89243-6`.

### 4.32 Cross-cutting observations

- **Public-domain core for psychiatric trials**: PHQ-9 / 2 / 8 / 15, GAD-7, CGI-S / I, HAM-D, HAM-A, MADRS, YMRS, BPRS-18, AIMS, PCL-5, CAPS-5, EPDS, ASRS, AUDIT, DUDIT, SNAP-IV, ECOG, KPS, WHODAS 2.0, WHOQOL-BREF are all freely usable (some require attribution / registration but no fee).
- **Licensed but trial-standard**: PANSS (MHS), MoCA (MoCA Test Inc, certification required since 2020), MMSE (PAR), BDI-II / BAI (Pearson), SF-36 / SF-12 (Optum), EQ-5D (EuroQol; free academic), Conners (MHS), ISI / PSQI (permission only). C-SSRS is technically licensed but free for non-commercial use.
- **FDA suicidality requirement**: Per FDA Guidance (September 2012), any CNS-active drug trial must monitor treatment-emergent suicidal ideation / behaviour using either C-SSRS or an equivalent prospective measure. This is the single most universally required psychiatric instrument in modern trials regardless of indication.

---

## Part 5. External Standards: What They Are and How to Map QRS Into Them

### 5.1 LOINC (Logical Observation Identifiers Names and Codes)

LOINC is the dominant standard for identifying clinical observations including survey / PRO instruments. Maintained by the Regenstrief Institute. Survey instruments live in the Survey Class (`PANEL.SURVEY` and `SURVEY.*` subclasses). LOINC encodes:

- **Panel codes**: the instrument as a whole.
- **Question codes**: one per item.
- **Total / sub-score codes**: numeric aggregates.
- **Answer Lists (LL / LA codes)**: enumerated value sets for response options.

**Worked example: PHQ-9 panel `44249-1` members**

| LOINC | Item |
|-------|------|
| 44250-9 | Little interest or pleasure in doing things |
| 44255-8 | Feeling down, depressed, or hopeless |
| 44259-0 | Trouble falling or staying asleep, or sleeping too much |
| 44254-1 | Feeling tired or having little energy |
| 44251-7 | Poor appetite or overeating |
| 44258-2 | Feeling bad about yourself, or that you are a failure |
| 44252-5 | Trouble concentrating on things |
| 44253-3 | Moving / speaking slowly or fidgety / restless |
| 44260-8 | Thoughts that you would be better off dead, or of hurting yourself |
| 69722-7 | Functional impairment item |
| 44261-6 | PHQ-9 total score |

Resolve any LOINC code at `https://loinc.org/{code}` (e.g., `https://loinc.org/44249-1`, `https://loinc.org/69737-5/panel`).

### 5.2 SNOMED CT

A comprehensive clinical terminology covering Findings, Disorders, Observable entities, Procedures, and Situations. Psych-relevant top-level hierarchies:

- `404684003 |Clinical finding|` (with subhierarchy `106131003 |Mental state finding|`)
- `363787002 |Observable entity|` (the locus for instrument-style "observable" items)
- `71388002 |Procedure|` for the act of administering an assessment

**Mapping approach for QRS items**:
- Instrument-level: the assessment as a Procedure (e.g., `715252007 |Depression screening using Patient Health Questionnaire Nine Item score|`).
- Total score: an Observable entity post-coordinated with a measurement scale.
- Item-level questions: typically picked up via the LOINC-SNOMED Cooperation expressions (LOINC Term → SNOMED CT Expression Reference Set, anchored on `363787002 |Observable entity|`).
- Clinical findings derived from items (the phenotype-level mapping target):
  - `84379007 |Anhedonia|`
  - `366979004 |Depressed mood|`
  - `48694002 |Anxiety|`
  - `6471006 |Suicidal thoughts|`
  - `193462001 |Insomnia|`
  - `271782001 |Loss of appetite|`
  - `60862001 |Tiredness|`
  - `27822003 |Psychomotor agitation|`
  - `19890001 |Psychomotor retardation|`

**Worked example**: PHQ-9 item 1 "Little interest or pleasure in doing things" (LOINC `44250-9`) maps to SNOMED finding `84379007 |Anhedonia|` and is expressible as an observable-entity expression of the form `363787002 |Observable entity| : 704319004 |inheres in| = ( 84379007 |Anhedonia| ), 370132008 |scale type| = 117363000 |Ordinal value|`.

### 5.3 HPO (Human Phenotype Ontology)

HPO ( `http://purl.obolibrary.org/obo/HP_*`, browser `https://hpo.jax.org/browse/term/HP:0000708` ) standardizes phenotypic abnormalities. The relevant subtree is **HP:0000708 Behavioral abnormality** (under HP:0000707 Abnormality of the nervous system). Granularity is patient-level phenotype, not item-level.

Selected behavioural HPO terms (IDs revise between releases; verify against the current OBO release):

| HPO ID | Label |
|--------|-------|
| HP:0000708 | Behavioral abnormality |
| HP:0000716 | Depressivity |
| HP:0000718 | Anhedonia (current release) |
| HP:0000739 | Anxiety |
| HP:0000737 | Irritability |
| HP:0000746 | Delusions |
| HP:0000738 | Hallucinations |
| HP:0031589 | Suicidal ideation |
| HP:0031969 | Psychomotor agitation |
| HP:0030223 | Apathy |
| HP:0000752 | Hyperactivity |
| HP:0000729 | Autistic behavior |
| HP:0002367 | Visual hallucinations |
| HP:0000745 | Paranoia |
| HP:0100753 | Schizophrenia |
| HP:0030212 | Inappropriate behavior |
| HP:0000744 | Abnormal social behavior |
| HP:0000751 | Personality changes |

**Worked QRS-to-HPO examples**:
- PHQ-9 Q1 "Little interest or pleasure in doing things" → HP:0000718 Anhedonia.
- PHQ-9 Q2 "Feeling down, depressed, or hopeless" → HP:0000716 Depressivity.
- PHQ-9 Q9 "Thoughts that you would be better off dead" → HP:0031589 Suicidal ideation.
- GAD-7 Q1 "Feeling nervous, anxious, or on edge" → HP:0000739 Anxiety.
- GAD-7 Q6 "Becoming easily annoyed or irritable" → HP:0000737 Irritability.
- YMRS Q1 Elevated mood → may map to HP:0030177 Elated mood (verify current ID).
- PANSS P3 Hallucinatory behaviour → HP:0000738 Hallucinations.
- PANSS P1 Delusions → HP:0000746 Delusions.

### 5.4 MONDO and DOID (disease ontologies)

MONDO (Monarch Disease Ontology) unifies OMIM, Orphanet, DOID, ICD, NCIT, SNOMED, etc. DOID is the Disease Ontology. Both are useful for the **disorder** an instrument targets, not the items themselves.

| Disorder | MONDO | DOID |
|---|---|---|
| Major depressive disorder | MONDO:0002009 | DOID:1470 |
| Generalized anxiety disorder | MONDO:0005618 | DOID:14320 |
| Bipolar disorder | MONDO:0004985 | DOID:3312 |
| Schizophrenia | MONDO:0005090 | DOID:5419 |
| Post-traumatic stress disorder | MONDO:0005711 | DOID:2055 |
| Obsessive-compulsive disorder | MONDO:0005491 | DOID:10933 |
| Attention deficit hyperactivity disorder | MONDO:0007743 | DOID:1094 |

MONDO terms carry cross-references to UMLS CUIs, ICD-10, ICD-11, and SNOMED. Browse at `https://www.ebi.ac.uk/ols4/ontologies/mondo`.

### 5.5 ICD-10 / ICD-10-CM / ICD-11

The diagnostic backbone for billing, regulatory submissions, and EHR interoperability. ICD-11 introduces refined psych categories (Complex PTSD `6B41`, Bodily distress disorder `6C20`, dimensional severity specifiers) and a chapter for "Mental, behavioural or neurodevelopmental disorders" (Chapter 06).

| Disorder | ICD-10-CM | ICD-11 |
|---|---|---|
| MDD, single episode, moderate | F32.1 | 6A70.1 |
| Recurrent MDD | F33.* | 6A71.* |
| Generalized anxiety disorder | F41.1 | 6B00 |
| Panic disorder | F41.0 | 6B01 |
| PTSD | F43.10 | 6B40 |
| Complex PTSD | N/A | 6B41 |
| OCD | F42.* | 6B20 |
| Bipolar I | F31.* | 6A60 |
| Schizophrenia | F20.* | 6A20 |

Browse ICD-11 at `https://icd.who.int/browse11/`.

### 5.6 DSM-5 / DSM-5-TR

APA's diagnostic manual, closely tied to ICD code stems. DSM-5-TR (2022) retains DSM-5 disorder structure with updated text and ICD-10-CM codes.

**PHQ-9 ↔ DSM-5 MDD A-criteria (canonical worked mapping)**:

| PHQ-9 item (LOINC) | DSM-5 MDD A-criterion |
|--------------------|------------------------|
| 44250-9 anhedonia | A2 markedly diminished interest / pleasure |
| 44255-8 depressed mood | A1 depressed mood |
| 44259-0 sleep | A4 insomnia / hypersomnia |
| 44254-1 fatigue | A6 fatigue / loss of energy |
| 44251-7 appetite | A3 weight / appetite change |
| 44258-2 worthlessness | A7 worthlessness / inappropriate guilt |
| 44252-5 concentration | A8 diminished concentration |
| 44253-3 psychomotor | A5 psychomotor agitation / retardation |
| 44260-8 suicidality | A9 recurrent thoughts of death |

**GAD-7 ↔ DSM-5 GAD**: GAD-7 items align with DSM-5 GAD Criterion B (restlessness, fatigue, concentration, irritability, muscle tension, sleep) and the global worry construct of criterion A.

**C-SSRS ↔ DSM-5**: Ideation severity items correspond to elements of DSM-5 suicidal-behaviour-disorder criteria.

### 5.7 NIH Common Data Elements (CDEs)

NIH CDE Repository at `https://cde.nlm.nih.gov/` curates standardized data elements and forms. Each form has a `tinyId` permalink.

- PHQ-9 form: `https://cde.nlm.nih.gov/formView?tinyId=myG8MkTbwg`
- GAD-7, C-SSRS, AUDIT, PROMIS short forms, and dozens of QRS instruments are catalogued.
- NINDS, NCI, NICHD, NIMH each maintain disease-specific CDE collections (NINDS CDEs for TBI include PHQ-9, GAD-7, NeuroQoL).

This is the closest US-government-curated registry to a working QRS ↔ LOINC ↔ SNOMED crosswalk.

### 5.8 RDoC (Research Domain Criteria, NIMH)

A mechanistic dimensional framework spanning units of analysis from genes to behaviour. Constructs index: `https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc/constructs`.

**Six domains and selected constructs**:

- **Negative Valence Systems**: Acute Threat ("Fear"); Potential Threat ("Anxiety"); Sustained Threat; Loss; Frustrative Nonreward.
- **Positive Valence Systems**: Reward Responsiveness (Anticipation, Initial Response, Satiation); Reward Learning (Probabilistic / RL, Reward Prediction Error, Habit-PVS); Reward Valuation (Probability, Delay, Effort).
- **Cognitive Systems**: Attention; Perception (Visual, Auditory, Olfactory / Somatosensory / Multimodal); Declarative Memory; Language; Cognitive Control (Goal Selection / Updating; Response Selection / Inhibition; Performance Monitoring); Working Memory.
- **Social Processes**: Affiliation and Attachment; Social Communication (Facial / Non-Facial); Perception and Understanding of Self (Agency, Self-Knowledge); Perception and Understanding of Others (Animacy Perception, Action Perception, Mental State Understanding).
- **Arousal and Regulatory Systems**: Arousal; Circadian Rhythms; Sleep-Wakefulness.
- **Sensorimotor Systems**: Motor Actions (Planning / Selection; Sensorimotor Dynamics; Initiation; Execution; Inhibition / Termination); Agency and Ownership; Habit-Sensorimotor; Innate Motor Patterns.

**Worked QRS-to-RDoC mappings**:

| QRS source | RDoC construct |
|---|---|
| GAD-7 (anticipatory worry) | Negative Valence / Potential Threat ("Anxiety") |
| GAD-7 / panic items | Negative Valence / Acute Threat ("Fear") |
| PHQ-9 anhedonia (Q1, 44250-9) | Positive Valence / Reward Responsiveness (deficit) |
| PHQ-9 depressed mood / worthlessness | Negative Valence / Loss |
| YMRS (mania) | Positive Valence / Reward Anticipation; Approach Motivation |
| PANSS positive (hallucinations) | Cognitive Systems / Perception |
| PANSS positive (paranoia) | Social Processes (paranoid ideation) |
| PHQ-9 sleep (Q3, 44259-0) | Arousal and Regulatory / Sleep-Wakefulness |
| PHQ-9 concentration (Q7, 44252-5) | Cognitive Systems / Attention or Cognitive Control |
| PHQ-9 psychomotor (Q8, 44253-3) | Sensorimotor Systems / Initiation, Execution |

### 5.9 PhenX Toolkit

PhenX ( `https://www.phenxtoolkit.org/` ) catalogs consensus phenotype protocols for cross-study use. Mental Health Research (MHR) supplement compiles a Core MH collection. Each protocol has a stable Protocol ID with permalink `https://www.phenxtoolkit.org/protocols/view/{ID}`. PhenX protocols cover PHQ-9, GAD-7, C-SSRS, ASRS, AUDIT-C, CES-D, PROMIS short forms, and many others. The MHR collection lives at `https://www.phenxtoolkit.org/collections/mhr`. PhenX provides per-protocol data dictionaries with field-level LOINC and dbGaP variable mappings.

PhenX harmonizes **how** an instrument is administered across studies (protocol-level); LOINC harmonizes **what** the data fields are.

### 5.10 HiTOP (Hierarchical Taxonomy of Psychopathology)

Consortium-driven empirical dimensional taxonomy. Primary site: `https://www.hitop-system.org/`; SBU portal: `https://renaissance.stonybrookmedicine.edu/HITOP`.

**Hierarchy (top-down)**: Super-spectra → Spectra → Subfactors → Syndromes → Symptom components / Maladaptive traits → individual symptoms / behaviours.

**Six spectra**:

| Spectrum | Subfactors and example syndromes |
|---|---|
| **Internalizing** | Distress (MDD, dysthymia, GAD, PTSD), Fear (panic, social anxiety, specific phobia, agoraphobia), Eating Pathology (anorexia, bulimia), Sexual Problems |
| **Disinhibited Externalizing** | Substance use disorders, ADHD, conduct / antisocial behaviour, impulse-control problems |
| **Antagonistic Externalizing** | Antisocial PD, narcissistic PD, histrionic features, aggressive behaviours |
| **Thought Disorder** | Positive psychotic symptoms, mania, dissociation (mania cross-loads with internalizing) |
| **Detachment** | Schizoid features, social withdrawal, anhedonia traits, schizotypy negative features |
| **Somatoform** (proposed) | Somatic complaints, illness anxiety, malaise |

**Three superspectra**: Emotional Dysfunction (Internalizing + Somatoform); Externalizing (Disinhibited + Antagonistic); Psychosis (Thought Disorder + Detachment); with a general **p-factor** at the apex.

**HiTOP measurement tools**: HiTOP-SR (self-report), HiTOP-CRT (clinician-rated), Brief HiTOP (B-HiTOP), plus expansions for personality.

**Legacy QRS-to-HiTOP rollups**:

| QRS instrument | HiTOP spectrum / subfactor / syndrome |
|---|---|
| PHQ-9 | Internalizing / Distress / MDD (anhedonia cross-loads on Detachment) |
| GAD-7 | Internalizing / Distress / GAD |
| BAI, panic measures | Internalizing / Fear |
| MADRS, HAM-D | Internalizing / Distress / MDD |
| YMRS | Thought Disorder / Mania (with Internalizing cross-load) |
| PANSS positive | Thought Disorder |
| PANSS negative | Detachment |
| AUDIT, DUDIT, DAST | Disinhibited Externalizing / Substance |
| PCL-5 | Internalizing / Distress (trauma-specific structure) |
| Y-BOCS | Internalizing / Distress (with thought-disorder cross-load) |
| ASRS, Conners, SNAP-IV | Disinhibited Externalizing / ADHD |
| AIMS, ESRS (motor) | Sensorimotor (HiTOP does not yet model motor symptoms uniformly; ancillary) |

HiTOP is the most tractable framework for **measurement-error-reduced** dimensional rollups from heterogeneous QRS data.

### 5.11 NIH Toolbox and PROMIS (HealthMeasures)

HealthMeasures ( `https://www.healthmeasures.net/` ) hosts:

- **PROMIS** (Patient-Reported Outcomes Measurement Information System): IRT-calibrated item banks. Mental-health-relevant banks include Depression, Anxiety, Anger, Psychosocial Illness Impact (Positive and Negative), Cognitive Function, Sleep Disturbance, Sleep-Related Impairment, Substance Use modules. Each bank has full CAT, item-bank, and fixed short forms (e.g., PROMIS Depression 4a / 6a / 8a / 8b). Scoring uses IRT theta converted to T-score (mean 50, SD 10).
- **NIH Toolbox**: performance-based cognitive (Flanker, Dimensional Change Card Sort, Picture Vocabulary, List Sorting), emotion (Emotion Battery), and motor measures with normative data.
- **Neuro-QoL, ASCQ-Me, TBI-QOL**: condition-specific PRO systems.

**PROsetta Stone** ( `http://www.prosettastone.org/` ) publishes IRT-linked crosswalks between PROMIS banks and legacy instruments:
- PROMIS Depression ↔ PHQ-9, BDI-II, CES-D, HADS-D
- PROMIS Anxiety ↔ GAD-7, HADS-A, STAI
- TBI-QOL Anxiety / Depression ↔ PHQ-9 / GAD-7 for TBI populations
- PROMIS Anger, Sleep Disturbance, Sleep-Related Impairment to their respective legacy scales.

The linking method (fixed-parameter calibration, Stocking-Lord, concurrent calibration with anchor items) produces a deterministic mapping from a legacy raw score to a PROMIS T-score with measurement-error bounds. A harmonization pipeline should retain both raw and linked T-scores.

### 5.12 ICF (International Classification of Functioning, Disability and Health)

WHO's framework for functioning: Body Functions (b-codes), Body Structures (s-codes), Activities and Participation (d-codes), Environmental Factors (e-codes). Hub: `https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health`.

WHODAS 2.0 maps directly to ICF Activities and Participation across six domains (Cognition, Mobility, Self-care, Getting along, Life Activities, Participation). Each item links at concept level to ICF d-codes (e.g., d175 Solving problems; d160 Focusing attention; d750 Informal social relationships). WHODAS 2.0 is the canonical bridge between symptom-level QRS and functional-impact mapping.

Use case: PHQ-9 functional-impairment item (LOINC `69722-7`) → ICF d-domain composite (work, household, social) ≈ WHODAS 2.0 short-form composite.

### 5.13 UMLS

US NLM's metathesaurus integrating ~200 source vocabularies under common CUIs. `https://www.nlm.nih.gov/research/umls/`. Role for QRS work:

- Aligns LOINC PHQ-9 item codes with their SNOMED finding analogues and MeSH descriptors.
- Provides CUIs for instrument names (e.g., "Patient Health Questionnaire-9" has a CUI used by NLP pipelines like MetaMap, cTAKES, QuickUMLS).
- Hosts MRCONSO, MRREL, MRSTY tables for programmatic crosswalk extraction.

Caveat: UMLS does not natively encode item-level question text in a fully harmonized way; LOINC and CDISC remain authoritative for item granularity.

### 5.14 OMOP CDM and OHDSI Vocabulary

OHDSI's Observational Medical Outcomes Partnership Common Data Model standardizes longitudinal health data. The OHDSI Vocabulary integrates LOINC, SNOMED, RxNorm, ICD, etc. under OMOP `concept_id` integers.

PRO instrument handling:
- Assessment scales encoded with LOINC route to the **MEASUREMENT** table.
- Assessment results encoded with SNOMED route to the **OBSERVATION** table.
- The OHDSI CDM Survey Sub-Work Group has prioritized PHQ-9, GAD-7, SF-36, Asthma Control Test, and PROMIS for standardized OMOP representation: one `concept_id` per panel; one per item question; one per Answer List value; mapping rules for raw scores, sub-scores, total scores.
- Survey responses populate `value_as_concept_id` (categorical) or `value_as_number` (Likert / score).

References: OHDSI CDM Survey Sub-Work Group deliverables; Book of OHDSI Chapter 5 ( `https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html` ).

---

## Part 6. Harmonization Strategy

### 6.1 Three granularities

1. **Instrument-level**. What disorder or construct does the scale measure as a whole? Maps to MONDO / DOID / ICD / DSM (disorder), to HiTOP spectrum / subfactor, to RDoC domain, to LOINC panel code, to NIH CDE form, to PhenX protocol ID. Useful for catalogue / registry metadata.
2. **Item-level**. What does each question ask? Maps to LOINC per-item code, to SNOMED Observable / Finding, to HPO phenotype term (for symptom presence above threshold), to a single RDoC construct, to a single HiTOP symptom component, to ICF d-code (functional items only). Required for federated analyses where instruments differ across cohorts but items overlap conceptually.
3. **Response-level**. What does the answer mean? Maps to LOINC Answer List codes (LL / LA), to SNOMED finding presence / absence with severity qualifiers, to numeric IRT theta on a calibrated bank (PROMIS metric), to score-band interpretation (mild / moderate / severe per DSM-5 severity dimensions or HiTOP percentile).

A pragmatic architecture stores all three layers and supports rollups: response → item → instrument → construct.

### 6.2 Categorical vs dimensional vs mechanistic worlds

- **DSM-5-TR / ICD-11 (categorical)**: best for billing, regulatory submissions, clinical-trial eligibility, EHR interoperability. Weak on comorbidity overlap, within-category heterogeneity, and mechanism.
- **HiTOP (dimensional, psychometric)**: best for measurement-error-reduced harmonization across instruments, transdiagnostic analysis, biomarker discovery where the signal is graded. Limited regulatory and payer support today.
- **RDoC (mechanistic, neuroscience-aligned)**: best for translational neuroscience, target identification, biomarker-construct alignment. Deliberately disorder-agnostic; does not support diagnostic claims directly.

A mature platform represents each subject's data in all three frames in parallel rather than picking one:

- Categorical ↔ Dimensional: HiTOP scores can be derived from DSM-criterion-aligned items using published factor weights.
- Dimensional ↔ Mechanistic: HiTOP subfactors align to RDoC constructs at moderate fidelity (HiTOP Fear ↔ RDoC Acute Threat; HiTOP Distress overlaps Negative Valence Loss + Sustained Threat).
- Categorical ↔ Mechanistic: weak / indirect; mediate through HiTOP or item-level mapping.

### 6.3 Crosswalks via IRT linking (PROsetta Stone pattern)

The dominant empirical method for cross-instrument harmonization is IRT co-calibration. PROsetta Stone has produced score-to-score crosswalks for PROMIS Depression ↔ PHQ-9 (r ~0.74), BDI-II, CES-D, HADS-D; PROMIS Anxiety ↔ GAD-7 (r ~0.72), HADS-A, STAI; TBI-QOL anxiety / depression ↔ PHQ-9 / GAD-7; PROMIS Anger, Sleep Disturbance, Sleep-Related Impairment to their respective legacy scales.

The linking method (fixed-parameter calibration, Stocking-Lord, or concurrent calibration with anchor items) produces a deterministic mapping from a legacy raw score to a PROMIS T-score with measurement-error bounds. A harmonization pipeline should retain both raw and linked T-scores so downstream models can choose.

### 6.4 Recent harmonization efforts worth leveraging

- **All of Us Research Program**: Administers PHQ-9, GAD-7, and other PROs at enrollment with field-level OMOP / LOINC mapping; supports cross-state psychiatric phenotype consistency studies.
- **PsychENCODE / BrainCODE**: Standardized clinical metadata alongside molecular data; aligns to DSM and RDoC.
- **ENIGMA Consortium**: Cross-cohort meta-analyses; working groups (PTSD, MDD, OCD, Bipolar, ADHD, Schizophrenia, Anxiety, Suicidal Thoughts and Behaviours) publish harmonization protocols including how to convert PHQ-9, BDI, HAM-D, MADRS scores to a common depression-severity metric for meta-analysis.
- **GENDAAR** and other autism networks reuse PhenX MH protocols.
- **PROMIS** as the cross-condition PRO backbone in NIH-funded trials.
- **NINDS / NIMH CDE collections** provide pre-curated forms with embedded LOINC mappings.
- **HL7 FHIR Questionnaire / PCO IG**: HL7 Person-Centered Outcomes Implementation Guide publishes FHIR Questionnaire resources for LOINC-coded instruments (e.g., GAD-7 = `Questionnaire-69737-5`).

### 6.5 Recommended platform architecture

For a Cytognosis-style harmonization layer:

1. **Anchor identifiers per QRS instrument**: CDISC QRS supplement ID + LOINC panel code + NIH CDE tinyId + PhenX Protocol ID + (where applicable) PROMIS item-bank ID.
2. **Per-item record**: LOINC question code, SNOMED Observable expression, HPO phenotype term (when symptom is present at threshold), RDoC construct tag, HiTOP component tag, ICF d-code (functional items only).
3. **Per-response record**: LOINC Answer List code, SNOMED finding presence / severity, ordinal value, IRT-linked T-score (when bank supports it).
4. **Per-subject derivations**: computed totals / subscale scores; computed HiTOP factor scores; computed RDoC construct intensities; DSM / ICD probable-diagnosis flags; ICF functioning summary.
5. **Provenance**: every derived value carries source instrument, version, scoring-rule version, and crosswalk source (e.g., "PROsetta Stone v2.1, PHQ-9 → PROMIS-Depression").
6. **Update cadence**: LOINC releases ~2x / year; SNOMED CT monthly; HPO monthly; MONDO weekly; ICD-11 annual; DSM less frequent. CI should re-resolve identifier validity at each release.

This architecture lets analysts query "all subjects in the negative-valence / loss construct with severity above HiTOP-Distress 60th percentile" regardless of which legacy instrument was administered, while preserving the original PHQ-9 (or BDI-II, or CES-D) raw data for regulatory / clinical use.

---

## Part 7. Quick Reference Tables

### 7.1 Psychiatric instrument summary

| Instrument | Construct | Items | Recall | Total | Severity bands | LOINC panel | Copyright | CDISC status |
|---|---|---|---|---|---|---|---|---|
| PHQ-9 | Depression | 9 (+1) | 2 wk | 0–27 | 5/10/15/20 | 44249-1 | Public | Exempt from Copyright |
| PHQ-2 | Depression screen | 2 | 2 wk | 0–6 | ≥3 trigger | 55758-7 | Public | (PHQ-9 family) |
| GAD-7 | Anxiety | 7 | 2 wk | 0–21 | 5/10/15 | 69737-5 | Public | Exempt from Copyright |
| HAM-D 17 | Depression | 17 | 1 wk | 0–52 | 8/14/19/23 | 89204-8 | Public | Public Domain |
| HAM-A | Anxiety | 14 | 1 wk | 0–56 | 17/24/30 | (panel reg) | Public | Public Domain |
| MADRS | Depression | 10 | 1 wk | 0–60 | 7/20/35 | reg | Public attrib | published |
| YMRS | Mania | 11 | 48 h | 0–60 | 12/26/38 | reg | Public | No response (historical) |
| BPRS-18 | General psychopath | 18 | varies | 18–126 | none fixed | reg | Public | rolled into RS |
| PANSS | Schizophrenia | 30 | 1 wk | 30–210 | 58/75/95/116 | reg | Licensed (MHS) | Granted |
| C-SSRS | Suicidality | varies | lifetime / since-last | scaled | severity 1–5 | 93373-9 / 93245-9 | Free non-comm | Granted |
| Y-BOCS | OCD | 10 | 1 wk | 0–40 | 8/16/24/32 | reg | Free research | (varies) |
| PCL-5 | PTSD | 20 | 1 mo | 0–80 | 31–33 cutoff | reg | Public | Public Domain |
| CAPS-5 | PTSD (interview) | 30 | per criterion | DSM algo | n/a | reg pending | Public | listed |
| BDI-II | Depression | 21 | 2 wk | 0–63 | 14/20/29 | n/a | Pearson | n/a |
| BAI | Anxiety | 21 | 1 wk | 0–63 | 8/16/26 | n/a | Pearson | n/a |
| EPDS | Postnatal depression | 10 | 7 d | 0–30 | ≥10 / ≥13 | 71354-5 | Free attrib | listed |
| MMSE | Cognition | 30 pts | now | 0–30 | 17/23 | 72106-8 | PAR licensed | v1.0 (Dec 2024) |
| MoCA | MCI | 30 pts | now | 0–30 | 26 (or 23) | 72133-2 | Cert required | constrained |
| ADAS-Cog 11 | AD cognition | 11 tasks | now | 0–70 | n/a | reg | Mapi etc | Granted |
| AIMS | Tardive dyskinesia | 12 | now | 0–28 (1–7) | Schooler-Kane | reg | Public | Public Domain |
| ESRS | EPS | multi | per visit | varies | n/a | limited | Permission | n/a |
| CGI-S/I | Global severity / change | 1 + 1 | now | 1–7 each | 4 = moderate | reg | Public | Public Domain |
| WHODAS 2.0 | Disability | 36 / 12 | 30 d | 0–144 / 0–100 IRT | n/a | 75274-1 | WHO free | listed |
| SF-36 / SF-12 | Generic QoL | 36 / 12 | 4 wk | norm-based | n/a | 62393-7 | Optum licensed | published |
| WHOQOL-BREF | QoL | 26 | 2 wk | 0–100 / domain | n/a | reg | WHO permission | published |
| EQ-5D-5L | Generic utility | 5 + VAS | now | utility index | n/a | 96538-3 | EuroQol | Granted |
| ASRS v1.1 | Adult ADHD | 18 (6 screener) | 6 mo | shaded boxes | ≥4 shaded | 78033-5 | Free | listed |
| Conners 3 | Child ADHD / behaviour | 99–115 | varies | T-scores | n/a | n/a | MHS licensed | n/a |
| SNAP-IV | ADHD / ODD | 26 / 90 | varies | subscale means | percentile | reg | Public | not published |
| AUDIT | Alcohol | 10 | 1 yr | 0–40 | 8/15/20 | 75624-7 | WHO public | listed |
| AUDIT-C | Alcohol (brief) | 3 | 1 yr | 0–12 | 4–5 cutoff | 75618-9 | WHO public | Public Domain |
| DUDIT | Drugs | 11 | 1 yr | 0–44 | 6 / 25 | reg | Free attrib | n/a |
| ISI | Insomnia | 7 | 2 wk | 0–28 | 8/15/22 | 89218-8 | Permission | (varies) |
| PSQI | Sleep quality | 19 + 5 | 1 mo | 0–21 | >5 poor | 65560-8 | Permission | listed |

### 7.2 PHQ-9 ↔ multi-ontology, item-level worked example

| PHQ-9 item | LOINC | SNOMED finding | HPO | DSM-5 MDD A | RDoC | HiTOP |
|---|---|---|---|---|---|---|
| Q1 Anhedonia | 44250-9 | 84379007 Anhedonia | HP:0000718 Anhedonia | A2 | Positive Valence / Reward Responsiveness | Internalizing / Distress; Detachment cross-load |
| Q2 Depressed mood | 44255-8 | 366979004 Depressed mood | HP:0000716 Depressivity | A1 | Negative Valence / Loss | Internalizing / Distress |
| Q3 Sleep | 44259-0 | 193462001 Insomnia (or 77692006 Hypersomnia) | HP:0002360 Sleep disturbance | A4 | Arousal-Regulatory / Sleep-Wakefulness | (Sleep facet, internalizing) |
| Q4 Fatigue | 44254-1 | 60862001 Tiredness | HP:0012378 Fatigue | A6 | Arousal-Regulatory / Arousal | Internalizing / Distress |
| Q5 Appetite | 44251-7 | 271782001 Loss of appetite / 271798003 Increased appetite | HP:0002039 Anorexia / HP:0002591 Polyphagia | A3 | Positive Valence / Reward Valuation | Internalizing |
| Q6 Worthlessness | 44258-2 | 247776008 Feelings of worthlessness | HP:0500152 Worthlessness (if available) | A7 | Social Processes / Self-Knowledge | Internalizing |
| Q7 Concentration | 44252-5 | 60032008 Impaired concentration | HP:0000721 Diminished concentration / HP:0007018 Attention deficit | A8 | Cognitive Systems / Attention or Cognitive Control | Internalizing / Distress |
| Q8 Psychomotor | 44253-3 | 27822003 Psychomotor agitation / 19890001 Psychomotor retardation | HP:0000752 Hyperactivity / HP:0025427 Psychomotor retardation | A5 | Sensorimotor / Initiation, Execution | Internalizing; Externalizing cross-load |
| Q9 Suicidality | 44260-8 | 6471006 Suicidal thoughts | HP:0031589 Suicidal ideation | A9 | Negative Valence (clinical compound) | Internalizing / Distress (Suicide subfactor) |

(SNOMED and HPO IDs above are illustrative; resolve against current release versions. Some HPO IDs vary release-to-release.)

### 7.3 GAD-7 ↔ multi-ontology

| GAD-7 item | LOINC | SNOMED finding | HPO | DSM-5 GAD | RDoC | HiTOP |
|---|---|---|---|---|---|---|
| Q1 Nervous / anxious / on edge | 69725-0 | 48694002 Anxiety | HP:0000739 Anxiety | B2 / global | Negative Valence / Potential Threat | Internalizing / Fear / Distress |
| Q2 Cannot stop or control worrying | 69726-8 | 225444004 Worry | HP:0000739 Anxiety | A worry | Negative Valence / Potential Threat | Internalizing / Distress |
| Q3 Worrying too much about different things | 69727-6 | 225444004 Worry | HP:0000739 Anxiety | A worry | Negative Valence / Potential Threat | Internalizing / Distress |
| Q4 Trouble relaxing | 69728-4 | 271705004 Inability to relax | (no exact HPO) | B muscle tension proxy | Negative Valence / Potential Threat | Internalizing |
| Q5 Restless that hard to sit still | 69729-2 | 55929007 Restlessness | HP:0000711 Restlessness | B1 restlessness | Sensorimotor / Initiation | Internalizing; Disinhibited Ext cross-load |
| Q6 Easily annoyed / irritable | 69730-0 | 55929007 Irritability (or 22253000 Pain qualifier; verify) | HP:0000737 Irritability | B4 irritability | Negative Valence / Frustrative Nonreward | Internalizing; Antagonistic Ext cross-load |
| Q7 Feeling afraid as if something awful might happen | 69731-8 | 271595006 Fearful | HP:0000746 Fear (verify ID) | B-context | Negative Valence / Acute Threat ("Fear") | Internalizing / Fear |

### 7.4 Permission / copyright legend (CDISC)

- Public Domain: free reproduction and use.
- Exempt from Copyright: not under copyright; honour rightsholder terms of use.
- Granted: CDISC may distribute the supplement; instrument use still needs a license.
- Author Permission Required: get supplement directly from rightsholder.
- Denied / No Response Received / Pending: no CDISC supplement currently available.

---

## Part 8. Operational Playbook

### 8.1 Setting up a new study or platform

1. Decide what is being measured (depression, anxiety, suicidality, mania, psychosis, cognition, function, sleep, substance use).
2. Pick instruments from the public-domain core where possible (PHQ-9, GAD-7, MADRS, YMRS, HAM-D / A, AIMS, BARS, PCL-5, C-SSRS, AUDIT, ASRS, ECOG, KPS, WHODAS, EQ-5D-3L if budget tight; CGI-S / I as global anchor).
3. Pull the CDISC QRS supplement for each instrument from `cdisc.org/qrs/all`.
4. Resolve LOINC panel + item codes for every instrument.
5. Build a per-item table that carries: CDISC QSTESTCD; LOINC question code; LOINC Answer List code; SNOMED Observable expression; SNOMED finding; HPO phenotype; RDoC construct; HiTOP component; ICF d-code if applicable.
6. Decide which dimensional metric to roll up to: PROMIS T-score via PROsetta Stone, or HiTOP factor score, or both.

### 8.2 Ingesting existing CDISC-formatted trial data

1. Pull current `SDTM Terminology.odm.xml` from NCI EVS FTP.
2. Parse out QSCAT / FTCAT / RSCAT category codelists and their child QSTESTCD / FTTESTCD / RSTESTCD codelists.
3. Match each QSTESTCD to a known instrument; cross-walk to LOINC item codes via a maintained lookup table.
4. Compute scores and bands per the supplement's scoring algorithm.
5. Apply IRT-linked crosswalks (PROsetta Stone) to convert legacy raw scores to PROMIS T-scores where banks exist.
6. Tag each row with disease (MONDO / DSM / ICD) and construct (RDoC, HiTOP).

### 8.3 Quarterly maintenance

- Re-pull SDTM Terminology and SDTM Terminology Changes once per quarter (March / June / September / December).
- Re-resolve LOINC, SNOMED, HPO, MONDO IDs against the latest releases; flag any deprecations.
- Diff against your fixed catalogue; update item-mapping rows where new codelist values appeared.
- Check the QRS supplements catalogue at `cdisc.org/qrs/all` for newly published instruments relevant to your therapeutic area.

### 8.4 Suicide-risk monitoring

- For any CNS trial, the FDA expects prospective monitoring via C-SSRS or equivalent (FDA Guidance, September 2012).
- PHQ-9 item 9 (LOINC 44260-8) is a screen, not a substitute.
- Encode each C-SSRS administration as both ideation severity (1–5) and behaviour history; preserve both in OMOP OBSERVATION (SNOMED 6471006 Suicidal thoughts, plus severity numeric).
- Map to HPO HP:0031589 Suicidal ideation for phenotype reasoning.

---

## Part 9. Consolidated URLs and Resources

**CDISC**

- QRS landing page: `https://www.cdisc.org/standards/questionnaires-ratings-and-scales-qrs`
- QRS standards page: `https://www.cdisc.org/standards/foundational/qrs`
- All published QRS supplements (master catalogue): `https://www.cdisc.org/qrs/all`
- Controlled Terminology page (with Supplemental Files tabs): `https://www.cdisc.org/standards/terminology/controlled-terminology`
- CDISC Library UI: `https://www.cdisc.org/cdisc-library`
- CDISC Library API base: `https://library.cdisc.org/api`
- Library developer portal: `https://api.developer.library.cdisc.org/`
- Library OAS3 spec: `https://www.cdisc.org/cdisc-library/api-documentation/oas3`
- API getting-started: `https://wiki.cdisc.org/display/LIBSUPRT/Getting+Started:+Programmatically+connect+to+CDISC+Library+API`
- QRS wiki workspace: `https://wiki.cdisc.org/display/QRSSUPP/`
- FAQ on QRS Supplement contents: `https://www.cdisc.org/faq/qrs/what-included-qrs-supplement`

**NCI EVS (CDISC controlled-terminology distribution)**

- FTP root: `https://evs.nci.nih.gov/ftp1/CDISC/`
- Current SDTM CT: `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/`
- Current ADaM CT: `https://evs.nci.nih.gov/ftp1/CDISC/ADaM/`
- SDTM archive: `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/Archive/`
- Legacy Questionnaire archive: `https://evs.nci.nih.gov/ftp1/CDISC/Archive/Questionnaire/Archive/`
- Legacy QRS Terminology 2015-09-25 (HTML): `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/Archive/QRS%20Terminology%202015-09-25.html`
- SDTM Terminology PDF (current): `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.pdf`

**LOINC**

- Resolver: `https://loinc.org/{code}`
- Users' Guide: `https://loinc.org/kb/users-guide/`
- PHQ-9 panel: `https://loinc.org/44249-1`
- GAD-7 panel: `https://loinc.org/69737-5/panel`
- SNOMED-LOINC Cooperation: `https://loinc.org/collaboration/snomed-international/`

**SNOMED CT**

- Editorial Guide (Observable Entity): `https://confluence.ihtsdotools.org/display/DOCEG/Observable+Entity`
- Browser (SNOMED International): `https://browser.ihtsdotools.org/`

**Phenotype / disease ontologies**

- HPO browser: `https://hpo.jax.org/browse/term/HP:0000708`
- OLS HPO: `https://www.ebi.ac.uk/ols4/ontologies/hp`
- MONDO MDD: `https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?short_form=MONDO_0002009`
- DOID: `https://disease-ontology.org/`

**Diagnostic codes**

- ICD-11: `https://icd.who.int/browse11/`
- ICD-10-CM: `https://www.cms.gov/medicare/icd-10/2024-icd-10-cm`
- DSM-5-TR (APA): `https://www.psychiatry.org/psychiatrists/practice/dsm`

**CDEs**

- NIH CDE Repository: `https://cde.nlm.nih.gov/`
- PHQ-9 form example: `https://cde.nlm.nih.gov/formView?tinyId=myG8MkTbwg`

**Construct frameworks**

- NIMH RDoC: `https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc`
- RDoC constructs: `https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc/constructs`
- HiTOP system site: `https://www.hitop-system.org/`
- HiTOP at Stony Brook: `https://renaissance.stonybrookmedicine.edu/HITOP`

**Phenotype protocols and PRO ecosystems**

- PhenX Toolkit: `https://www.phenxtoolkit.org/`
- PhenX MHR collection: `https://www.phenxtoolkit.org/collections/mhr`
- HealthMeasures (PROMIS / NIH Toolbox / Neuro-QoL): `https://www.healthmeasures.net/`
- PROsetta Stone: `http://www.prosettastone.org/`

**Functioning**

- ICF / WHODAS: `https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health/who-disability-assessment-schedule`

**Crosswalks / models**

- UMLS: `https://www.nlm.nih.gov/research/umls/`
- OHDSI Vocab (Book of OHDSI Ch 5): `https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html`
- OMOP CDM v5.4: `https://ohdsi.github.io/CommonDataModel/cdm54.html`
- HL7 PCO IG GAD-7 Questionnaire: `https://build.fhir.org/ig/HL7/pco-ig/Questionnaire-69737-5.html`

**Instrument owners and registries**

- PHQ Screeners: `https://www.phqscreeners.com/`
- C-SSRS: `https://cssrs.columbia.edu/`
- VA NCPTSD (PCL-5 etc.): `https://www.ptsd.va.gov/professional/assessment/`
- WHO AUDIT: `https://www.who.int/publications/i/item/WHO-MSD-MSB-01.6a`
- EuroQol EQ-5D: `https://euroqol.org/`
- Mapi Trust ePROVIDE / PROQOLID: `https://eprovide.mapi-trust.org/`

---

## Part 10. Caveats and Open Items

- **Verify HPO IDs at the current release.** HPO has occasionally renumbered terms; `HP:0000718 Anhedonia` is the current canonical, but older crosswalks reference `HP:0100716`. Anchor mappings to a release identifier.
- **LOINC item codes may change with edition.** New panel versions are sometimes published with new codes (especially for new short forms of PROMIS banks).
- **SNOMED CT is monthly.** Identifier deprecation is rare but possible; carry the SNOMED Edition date with each mapping.
- **CDISC submission values do not always equal item text.** The QSTESTCD value (e.g., `PHQ0101`) is a compact code; the QSTEST value is a short label; verbatim item text is governed by copyright.
- **PROMIS T-score crosswalks assume sample equivalence.** PROsetta Stone calibrations are valid in clinical samples similar to the calibration sample; consider re-calibration for very different populations.
- **HiTOP is empirically derived and revises every few years.** The 2024–2026 revisions consolidated the Somatoform spectrum and updated personality coverage.
- **Some highly cited instruments have no CDISC supplement** (BDI-II, BAI, MoCA in some contexts, ISI, PSQI) because copyright holders did not respond. Use commercial equivalents through Mapi or replace with open instruments (PROMIS, PHQ-9, ISI alternative).
- **C-SSRS administration**: requires the most recent version (currently 2008/2014 forms by version); FDA expects use of the licensed Columbia form.

---

*Document version 1.0, 2026-05-13.*
