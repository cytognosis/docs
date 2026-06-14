<!-- Last updated: 2026-05-22 | Source: Plans/design/11_reproducibility_strategy/ -->
**← [Back to Reproducibility Index](README.md)**

# 05 — FAIRDOM-SEEK + WorkflowHub Integration

**Reading order**: read `00_master_strategy.md` §8 first.

This document defines: how we adopt FAIRDOM-SEEK and WorkflowHub (rather than building parallel registries), how we deploy our own instances alongside cytoskeleton's `publish` flow, how we federate with the public FAIRDOM ecosystem, and how PHI workflows stay isolated.

---

## 1. Why SEEK and WorkflowHub

The strategy commits to *not* building a parallel registry. The FAIRDOM stack (https://fair-dom.org/) is:

- **FAIRDOM-SEEK** (Ruby/Rails, BSD-3, https://github.com/seek4science/seek) — web-based registry for ISA Investigations / Studies / Assays / SOPs / Models / DataFiles / Samples / Publications / Programmes / Projects. ISA-extended and configurable beyond biology. Used in FAIRDOMHub, WorkflowHub, DataHub, IBISBAKHub, NextSEEK.
- **WorkflowHub** (the workflows.cytognosis.org instance) — SEEK configured with the Workflow RO-Crate profile + LifeMonitor + GA4GH TRS. Domain-agnostic FAIR workflow registry, EU-wide, EOSC-Life sponsored.
- **LifeMonitor** (https://lifemonitor.eu/) — workflow test health monitor; consumes Workflow Testing RO-Crates.
- **FAIRSCAPE** — reference RO-Crate emitter + ARK minter + FAIR-assessment dashboard.

Adopting these gives us federation for free: our public artifacts mirror to fairdomhub.org and workflowhub.eu without bespoke code; consumers discover via standard search APIs (Bioschemas / Schema.org); the existing community of practices is reused.

---

## 2. Two self-hosted instances

### 2.1 hub.cytognosis.org (Cytognosis SEEK)

Hosts:

- **Programmes**: top-level org units (e.g., "Cytognosis Foundation" with sub-programs like Cytoverse, Cytonome, Cytoscope).
- **Projects**: scoped collaborations (e.g., "ABCD HRV models", "Cytoscope assay panel v1").
- **Investigations**: ISA top-level grouping (one paper or one major analysis = one Investigation).
- **Studies**: ISA Study (one hypothesis/cohort).
- **Assays**: ISA Assay Streams + Assays (per-modality processing chains).
- **SOPs**: protocols (linked to Yar SOPs, protocols.io, lab notebook entries).
- **Models**: ML model artifacts (separate from Workflows — these are static model files).
- **DataFiles**: dataset metadata records (data lives in VFS; SEEK records the metadata + URI).
- **Samples**: biological / observational samples tied to Studies + Assays.
- **Publications**: papers with DOI + linked to Investigations.
- **Annotations**: through self-hosted Hypothes.is, federated via WADM.

### 2.2 workflows.cytognosis.org (Cytognosis WorkflowHub)

Same FAIRDOM-SEEK code, different config:

- Hosts **Workflows** (Workflow RO-Crate uploads).
- Exposes the GA4GH TRS endpoint.
- Wires to a local LifeMonitor instance.
- Mirrors public workflows to workflowhub.eu via the TRS federation API.

### 2.3 Deployment topology

```
GCP project: cytognosis-infrastructure
├── Cloud Run (us-central1)
│   ├── seek-rails       (FAIRDOM-SEEK Rails app, hub.cytognosis.org)
│   ├── seek-sidekiq     (background jobs)
│   ├── workflowhub-rails  (FAIRDOM-SEEK Rails app, workflows.cytognosis.org)
│   ├── workflowhub-sidekiq
│   ├── lifemonitor      (LifeMonitor Flask app)
│   ├── fairscape        (FAIRSCAPE)
│   └── solr             (managed Solr or self-hosted Cloud Run with persistent volume)
├── Cloud SQL (Postgres)
│   ├── seek-db
│   ├── workflowhub-db
│   ├── lifemonitor-db
│   └── fairscape-db
├── GCS buckets
│   ├── cytognosis-seek-uploads     (DataFile blob storage)
│   ├── cytognosis-workflowhub-crates  (Workflow RO-Crate zips)
│   └── cytognosis-fairscape         (FAIRSCAPE artifacts)
├── Artifact Registry (Docker)
│   └── us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute  (env images)
└── ELIXIR-AAI / Google OAuth
    └── Identity Platform federation for SEEK + WorkflowHub auth
```

PHI bucket access is gated by ELIXIR-AAI groups; non-PHI is public.

### 2.4 Backups

- Cloud SQL: daily automated backups + cross-region replica.
- GCS uploads: object versioning + retention-locked for HIPAA records.
- Solr index: rebuilt nightly from Postgres + GCS; loss tolerance ~24h.
- Configurations: stored as Terraform in `org/infrastructure/services/seek/`.

---

## 3. Workflow Run Crate → SEEK + WorkflowHub publish flow

`cytoskeleton publish run <crate-dir>` does the following:

```
1. Validate Crate against profiles/workflow_run_crate.yaml.
2. Verify in-toto attestation chain.
3. Determine tier (public / Tier 2 / Tier 1) from safe_data field.
4. For tier == public:
   a. Mint Zenodo DOI for the Crate (zenodo deposition API).
   b. POST workflow metadata to WorkflowHub /api/workflows (multipart, .crate.zip body).
      - Receives TRS ID and SEEK record ID.
   c. POST run metadata to SEEK /api/investigations/{inv}/studies/{study}/assays.
   d. Update Crate's cite_as field with the minted DOI.
   e. Mirror to public workflowhub.eu via TRS federation endpoint.
   f. Submit code to Software Heritage (if not already submitted).
   g. Update GitHub release with Zenodo DOI + SWHID + WorkflowHub TRS ID.
5. For tier == Tier 2:
   a. Same as public, but skip step (e) — do NOT mirror to public.
   b. Restrict access via SEEK Project ACLs.
6. For tier == Tier 1:
   a. Crate is a Five Safes RO-Crate; further restrictions apply.
   b. POST only to hub.cytognosis.org (not workflows.cytognosis.org).
   c. SEEK Project ACL bound to DUC IAM group.
   d. Zenodo NOT used; archival within Cytognosis cytognosis-phi-prod bucket only.
7. Register the workflow's test crate (if present) with LifeMonitor.
8. Emit a publish receipt: minted IDs + URLs + timestamps.
```

### 3.1 The SEEK REST API

SEEK exposes a JSON:API-compliant REST API. Key endpoints we use:

```
POST /api/investigations               # create
POST /api/studies                      # create + link to investigation
POST /api/assays                       # create + link to study
POST /api/sops                         # upload SOP
POST /api/data_files                   # upload DataFile (or reference external URI)
POST /api/models                       # upload Model
POST /api/samples                      # create Sample
POST /api/sample_types                 # create SampleType
GET  /api/projects/{id}                # list project assets
PUT  /api/investigations/{id}          # update
GET  /api/investigations/{id}/snapshot # mint citable snapshot

# ISA-JSON specific
POST /api/investigations/{id}/import_isajson   # import full ISA-JSON
GET  /api/investigations/{id}/export_isajson   # export ISA-JSON
```

Cytoskeleton's `cytoskeleton.seek.client` is a thin wrapper. It maps LinkML ISA profile instances to ISA-JSON via `cytoskeleton.isa.serialize.to_isa_json`, then POSTs.

### 3.2 The WorkflowHub TRS API

GA4GH TRS v2 endpoints exposed by the WorkflowHub instance:

```
GET  /ga4gh/trs/v2/tools                          # list all workflows
GET  /ga4gh/trs/v2/tools/{id}                     # workflow detail
GET  /ga4gh/trs/v2/tools/{id}/versions            # versions
GET  /ga4gh/trs/v2/tools/{id}/versions/{v}/files  # download Crate or specific file
POST /api/workflows                                # upload (SEEK proprietary)
```

cytoskeleton's `cytoskeleton.workflowhub.client` is the analogous wrapper.

---

## 4. ISA-JSON-compliant Experiment authoring

Per `docs.seek4science.org/help/user-guide/isa-json-compliant-experiment.html`:

- **ISA Investigation**: enabled by ticking "Make Investigation compliant to ISA-JSON schemas?". Becomes the root.
- **ISA Study**: must contain Source(s), Protocol(s), Sample(s). Only attaches to an ISA Investigation.
- **Assay Stream**: a sequence of sequential Assays connected by sample flow. Aligns with one ISA Assay in the formal model; usually one technology/technique.
- **ISA Assay**: requires Inputs (Sample or prior Assay output), Protocol, Outputs (material samples or data file samples).
- **Experiment Sample Templates**: blueprints for Sample Types. Platform-wide templates from admin OR Project-specific ones from researchers. Levels: ISA Study Source Template, ISA Study Sample Template, ISA material output Assay Template, ISA data file Assay Template.

This shape is what our LinkML `profiles/isa.yaml` produces.

### 4.1 mcPHASES as a worked example

The Cytos universal sensor schema demonstrated representing the mcPHASES PhysioNet dataset (Mathai et al. 2025) — 19 sensor/self-report CSV files from three vendor devices over two longitudinal intervals. The ISA mapping:

- **Investigation**: "mcPHASES longitudinal multi-device study"
- **Study**: "mcPHASES participant cohort 2022-2024"
  - **Source**: each participant (with demographic Characteristics).
  - **Protocol** (sampling): "Wearable + CGM + Mira + self-report enrollment".
  - **Sample**: per-participant data-collection batches.
- **Assay Stream**: one per modality.
  - **Wearable Assay**: Fitbit-recorded HR / HRV / steps / sleep / temperature / etc. (17 CSV → 17 sub-Assays).
  - **CGM Assay**: Dexcom 5-min glucose readings.
  - **Hormone + Self-report Assay**: Mira LH/E3G/PDG + 13 Likert symptoms.
- **Sample Types**: each Sample Type instantiated from a Cytognosis-provided Experiment Sample Template tied to the Universal Sensor Schema profile.
- **DataFiles**: each CSV referenced by VFS URI with sha256 + DVC md5.

Per `cytoskeleton publish` invocation:

```bash
$ cytoskeleton publish dataset \
    --schema cytoskeleton/schemas/profiles/sensor/profile_mcphases.yaml \
    --data ~/datasets/mcphases/ \
    --to seek \
    --investigation-title "mcPHASES longitudinal multi-device study"
# 1. Validates dataset against Universal Sensor + mcPHASES profiles.
# 2. Produces ISA-JSON via LinkML serializer.
# 3. POSTs to hub.cytognosis.org SEEK as ISA-JSON-compliant Investigation.
# 4. Each CSV stays in VFS; SEEK records URI + hash, doesn't duplicate the blob.
```

### 4.2 Cytos KG as an ISA-JSON-compliant Investigation

Even the cytos KG build is an ISA Investigation:

- **Investigation**: "Cytos KG v0.4.0".
- **Study**: "Source ingestion 2026-05".
  - **Source**: each ontology / KG source (Biolink, Monarch, PrimeKG, Open Targets, …).
  - **Protocol**: "License-gated ingest" (linked to `data/manifest.yaml`).
  - **Sample**: each parsed dataset version.
- **Assay Stream** (per stage in dvc.yaml):
  - Topic ingest, Monarch merge, PrimeKG convert, OT ingest, UniChem xrefs, Predicate normalize, Node reclassify, Neo4j export, RO-Crate gen.
  - Each stage is an ISA Assay with Inputs (prior outputs) → Protocol (the script SWHID + image digest) → Outputs (TSVs + Neo4j export).
- **DataFiles**: `data/kg/nodes.tsv`, `data/kg/edges.tsv`, etc., with sha256 + DVC md5.

The existing cytos `ro-crate-metadata.json` (already generating dataset descriptions for 9 sources + 17 artifacts) becomes the input to `cytoskeleton publish` → ISA-JSON → SEEK.

---

## 5. LifeMonitor

LifeMonitor watches workflow tests and reports health. Setup:

1. Deploy LifeMonitor (Flask + Postgres) on Cloud Run as `lifemonitor.cytognosis.org`.
2. Configure LifeMonitor to pull workflow test crates from workflows.cytognosis.org.
3. Register supported test engines:
   - PlanemoTest (Galaxy)
   - NextflowTest
   - SnakemakeTest
   - Pytest (used for redun + Kedro tests)

When a workflow is published with a `test/` directory and a recognized test engine config, LifeMonitor schedules nightly test runs and shows status badges on the WorkflowHub workflow page.

For Cytognosis-specific engines (redun, Kedro), we contribute test-engine plugins upstream to LifeMonitor.

---

## 6. Federation strategy

### 6.1 Public mirroring

- **fairdomhub.org**: Cytognosis is registered as a Programme. Public Investigations replicate from hub.cytognosis.org to fairdomhub.org on release.
- **workflowhub.eu**: Cytognosis is registered as a Programme. Public workflows replicate from workflows.cytognosis.org to workflowhub.eu on release. nf-core's existing federation pattern (auto-sync) is the model.
- **Zenodo**: per-release DOI; the canonical archival home.
- **Software Heritage**: per-release source code archival; SWHIDs registered.

### 6.2 Discoverability

Both SEEK instances expose Schema.org / Bioschemas JSON-LD on every resource page. This is what Google Dataset Search, OpenAIRE, and EOSC use to index. No extra work needed.

### 6.3 TRS federation

The TRS endpoint at workflows.cytognosis.org is GA4GH-compliant. workflowhub.eu's TRS federation regularly indexes registered TRS endpoints. Once registered, our workflows appear in workflowhub.eu queries.

---

## 7. Authentication

- **hub.cytognosis.org**: Google OAuth + ELIXIR-AAI dual-stack. Researchers in cytognosis.org use Google; external collaborators use ELIXIR-AAI.
- **workflows.cytognosis.org**: same.
- **PHI gating**: ELIXIR-AAI groups bound to DUC IAM groups via SAML attribute mapping. Researcher must be in the DUC group AND on the SEEK Project ACL to view Tier 1/2 records.

---

## 8. Plugin / customization scope

FAIRDOM-SEEK is Ruby on Rails; we minimize forking. Customizations we accept:

- ELIXIR-AAI + Google OAuth dual config.
- Cytognosis branding (logo, primary color via existing SEEK CSS variables).
- Custom Experiment Sample Templates (configured via admin UI, exported as YAML).
- Custom controlled vocabularies (configured via admin UI).
- Webhook for `cytoskeleton publish` callback.

Customizations we avoid:

- Forking SEEK code.
- Changing core ISA semantics.
- Changing the data model.

If something can't be done via plugin / config, we open an upstream issue at github.com/seek4science/seek.

---

## 9. Migration: existing artifacts → SEEK

| Artifact today | Where it lives | Migration target |
|---|---|---|
| Cytos schemas | cytos/schemas | cytoskeleton/schemas + SEEK Investigation "Cytos schema versions" |
| Cytos KG dvc + ro-crate | cytos/data/kg | SEEK Investigation "Cytos KG v0.4.0" with DataFiles + Assays |
| Papers (Drive Library/) | Drive + Zotero | SEEK Publications (referencing Drive URLs); Zotero stays as personal library |
| Models (TBD) | gs://cytognosis-data/models/ | SEEK Models (with HF mirror) |
| Workflows (cytos pipelines) | cytos/src + dvc.yaml | workflows.cytognosis.org Workflow records (one per Kedro pipeline → Workflow RO-Crate) |
| Annotations | self-hosted Hypothes.is | unchanged; SEEK links to annotation IDs |
| Decisions | design docs / 09_decision_log.md | SEEK Programme-level documents |

Migration is incremental: we don't bulk-import. We register an artifact when it goes through `cytoskeleton publish`.

---

## 10. Open questions

1. **Start self-hosted or use FAIRDOMHub directly?** Recommendation: register Cytognosis as a Programme on FAIRDOMHub from day one; deploy hub.cytognosis.org once volume / privacy needs justify the operational cost (~$200/month).

2. **WorkflowHub.eu vs self-hosted**: register on workflowhub.eu from day one (nf-core does this); self-host once we have PHI workflows.

3. **OpenBIS integration**: SEEK has an OpenBIS connector. Do we need OpenBIS for lab samples / inventory? Recommendation: defer; revisit if Cytoscope wet-lab work scales.

4. **GA4GH DRS endpoint**: should hub.cytognosis.org expose DRS for VFS URIs? Recommendation: yes, post-v0.1; gives a standard way for external tools to fetch our data.

5. **Experiment Sample Templates ownership**: templates platform-wide vs Project-specific. Recommendation: platform-wide templates for canonical types (Sample, Subject, Wearable observation, CGM observation, Survey response); Project-specific for cohort-particulars.

6. **JERM templates**: SEEK has JERM (Just Enough Results Model) templates for transcriptomics, proteomics, etc. Do we adopt these or use our LinkML-driven templates? Recommendation: use JERM where it exists (it's already configured in SEEK); add LinkML templates for areas JERM doesn't cover (sensor data, KG snapshots).

7. **Long-term: cytoskeleton ↔ SEEK two-way sync**: today flow is one-way (cytoskeleton publishes; SEEK is the read-side). Eventually: SEEK changes (e.g., editing a Sample's metadata) should round-trip back to LinkML instances. Recommendation: design v0.2; out of scope for v0.1.
