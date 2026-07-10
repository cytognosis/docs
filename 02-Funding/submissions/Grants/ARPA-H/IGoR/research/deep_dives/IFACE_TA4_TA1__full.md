> [!WARNING]
> **Readout correction (2026-06-14):** the functional neuronal readout is **single-cell calcium imaging** (scalable, single-cell), not MEA. Calcium imaging is an optical/imaging modality covered by Cellanome's live-cell fluorescence imaging and high-content imaging, so **there is no electrophysiology-lab gap** and MEA is not required. Treat the 'MEA / electrophysiology gap' analysis below as superseded; the detailed MEA schema (formats, QC, encoders) is to be reworked to calcium imaging in the full-proposal build.

# TA4-to-TA1 Interface: Experimental Data Return and Model Update Loop

**Document type:** Internal research analysis, full version (publication-quality)
**Compiled:** 2026-06-14
**Authors:** Cytognosis research team
**Audience:** Internal; IGoR proposal development team only
**Paired doc:** `IFACE_TA4_TA1__brief.md` (ADHD-friendly companion)
**Feeds into:** IGoR full proposal, Appendix C.1 (Technical and Management Proposal), Section covering TA1 Objective 2 and TA4 Objective 2

> [!CAUTION]
> This document contains references to SPEAR (confidential, under anonymous NeurIPS 2026 review) and to the factorized-PRS (Pillar 2b, proprietary crown-jewel IP). Neither is described mechanistically here. External builds must omit all SPEAR and Pillar 2b technical content.

---

## Abstract

The ARPA-H IGoR program closes its Design-Build-Test-Learn loop at the TA4-to-TA1 interface: validated experimental results flowing back from the laboratory network to update the disease model. This document characterizes that interface in full technical depth, covering (1) the data-return contract and the PROV-O/SBOL3 provenance chain that links every result to the uncertainty entry that motivated the experiment; (2) the concordance and quality-control gating pipeline that guards the ingestion boundary; (3) the automated Bayesian model-update trigger and the feasibility of the Phase II latency target of 24 hours and the Phase III target of 4 hours; (4) an assessment of SIFT's Round Trip closed-loop pipeline (Bryce et al., ACS Synth Biol 2022, doi:10.1021/acssynbio.1c00305) and AutoGater (Eslami et al., Sci Reports 2024, doi:10.1038/s41598-024-66936-8) for reuse versus their synthetic-biology-specific components; and (5) how ingested data updates the three-latent structural causal model (basal, disease, treatment) of the IGoR TA1 architecture.

The central finding is that the interface is technically feasible but requires four new engineering deliverables in Phase I: (a) a LinkML-defined IGoR Common Data Model (CDM) package format; (b) an event-driven ingestion listener tied to the TA3 protocol repository; (c) modality-specific quality-control modules for morphological, transcriptomic, and electrophysiological returns; and (d) a Bayesian posterior-update API exposing TA1 Pillar 2 to incremental data. The 24-hour latency target is achievable in Phase II with an asynchronous compute pipeline. The 4-hour target requires sub-hour automated QC plus precompiled CUDA kernels for posterior update; it is feasible but tight and should be flagged as a Phase III engineering stretch.

A key architectural point established by Sections 31b and 32b of the Research Master governs how returned data is processed before reaching the model update step. Each returned modality (transcriptomic, morphological, electrophysiological, and any additional multi-omic) is encoded by a **modality-specific encoder** and the resulting embeddings are fused into a single **multimodal representation** via a **barycenter** (an optimal-transport-style average across modalities), before that representation updates the TA1 disease model. All modalities are featurized in a uniform coordinate system by operating on **delta pathways** rather than delta genes, which is what makes heterogeneous TA4 returns directly comparable and jointly ingestible. The fused, pathway-space representation then updates the **disease-effect operator** of the three-latent structural causal model (basal, disease, treatment) and refines the **deep structural causal model over disease axes** (Section 31b of the Research Master), reducing per-axis uncertainty in a way that is directly traceable to the returned experiment.

**Reading time:** approximately 25 minutes.
**If you read one section:** read Section 3 (the data-return contract and provenance chain) and Section 5 (the Bayesian update trigger and latency feasibility analysis).

---

## 1. Interface Context: Where This Fits in the IGoR Loop

### 1.1 The upstream chain

The TA4-to-TA1 interface is the downstream terminus of a four-step provenance chain established by the upstream interfaces described in `IFACE_TA2_TA3__full.md`:

1. TA1 emits a structured uncertainty map entry: an under-constrained parameter, an under-evidenced causal edge, or an inconsistent flux prediction in the Pillar 1 mechanistic network.
2. TA2 converts that entry into a ranked experiment-intent object (ExperimentIntent), carrying the TA1 uncertainty reference in the `ta1_gap_reference` slot and a Bayesian value-of-information score in `voi_score`.
3. TA3 (SIFT, LabOP) compiles the ExperimentIntent into a canonical LabOP Protocol object (SBOL3 RDF), generates laboratory-specific specializations (OpenTrons OT2, SiLA 2/R3200, Illumina SampleSheet, Markdown), and issues the protocol to the assigned TA4 laboratories.
4. TA4 executes under the locked LabOP protocol and returns a QC-rich, provenance-linked data package to TA1.

The TA4-to-TA1 interface governs step 4. Without this step, the loop does not close; without closing the loop, IGoR cannot demonstrate the Phase I walking-skeleton milestone.

### 1.2 Programmatic requirements from Appendix A

Two TA objectives govern this interface directly.

**TA1 Objective 2: Update the model from new experimental data in near-real-time.**

| Phase | Latency requirement | Interpretation |
|---|---|---|
| Phase II (18 months) | <= 24 hours from data receipt to model update | Triggered by a TA4 data-return event; full posterior update pipeline must complete within 24 hours |
| Phase III (24 months) | <= 4 hours | Full automation with no human-in-the-loop between data receipt and model update; requires sub-hour QC and fast posterior computation |

**TA4 Objective 2: Marketplace Operations.** The request-to-return interface in which TA4 returns a QC-rich, IGoR-common-data-model-formatted package to TA1. Phase III additionally requires >= 70% of TA4 exceptions handled autonomously, which implies the ingestion pipeline must also handle exception classification and routing without manual intervention.

### 1.3 Why this interface is harder than it looks

The apparent simplicity of "data flows from lab to model" conceals four structural challenges:

1. **Heterogeneous modalities.** Transcriptomic (AnnData h5ad), morphological (CellProfiler CSV plus TIFF image stacks), and electrophysiological (Axion Maestro HDF5 or MEA Binary) returns have no common schema; a modality-specific ETL layer is required before any modality-agnostic QC gating can run.
2. **Provenance linkage under asynchrony.** A multi-day Cellanome R3200 live-cell experiment generates streaming QC updates during the run before the final end-of-run data package is closed. The provenance chain must distinguish streaming partial updates from the authoritative final package; only the final package triggers the Bayesian update.
3. **Concordance computation across labs.** Phase I requires >= 80% intra-team concordance; Phase II requires >= 90% cross-team concordance. The concordance check runs before the data are ingested into TA1, not after. This means data from both TA4 laboratories executing the same experiment must arrive and pass individual QC before the concordance gate can fire.
4. **Identifiability constraints on the model-update step.** Not all data types can update all parts of the three-latent SCM. A morphological readout updates the basal and disease latent subspaces but provides limited information about the treatment latent. The ingestion logic must route returned data to the correct update target.

---

## 2. The TA4 Data-Return Package: Format and Contents

### 2.1 The IGoR Common Data Model (CDM) package

IGoR Appendix A requires that TA4 laboratories return data formatted to the "IGoR common data model." The CDM is not specified in Appendix A beyond its existence; it is a Phase I deliverable, to be defined at the Domain-Driven Design (DDD) workshop. Based on the TA1 and TA4 requirements, the CDM package must contain at minimum four components:

| Component | Format | Required fields |
|---|---|---|
| **Data payload** | Modality-specific (see Section 2.2) | Assay type, instrument identifier, run parameters, cell-type (CL term), perturbation (HGNC or ChEMBL) |
| **QC report** | JSON-LD, LinkML schema | Per-metric QC flags (PASS/FAIL/WARNING), viability score, concordance pre-check result, batch-effect score |
| **Provenance record** | PROV-O RDF, linked to LabOP Protocol URI | Lab identifier, execution timestamp, instrument serial, reagent lot numbers, data lineage |
| **Uncertainty reference** | URI | `ta1_gap_reference`: points back to the TA1 uncertainty map entry that generated the ExperimentIntent that generated this protocol |

The `ta1_gap_reference` field is the critical closure element. Without it, TA1 cannot determine which model uncertainty a given data return is intended to resolve.

### 2.2 Modality-specific data formats and encoding

The three Phase I modalities produce data in formats that differ substantially. A lightweight ETL step converts each to a CDM-compatible representation before QC gating. After ETL, each modality passes through its **modality-specific encoder** (Research Master, Section 32b extension 4) to produce a fixed-dimensional embedding. Critically, all modalities are featurized as **delta pathways** rather than delta genes: instead of reporting per-gene expression changes, the encoder outputs shifts in GO biological process pathway activity (using the SENA-delta encoder for transcriptomics and analogous pathway projections for other modalities). This **uniform cross-modality featurization** means embeddings from transcriptomic, morphological, and electrophysiological returns are directly comparable in the same pathway-space coordinate system, making heterogeneous TA4 returns jointly ingestible without separate harmonization steps.

Once per-modality embeddings are computed, they are fused via the **barycenter** of their embeddings, an optimal-transport-style average (Research Master, Section 32b extension 4), into a single **multimodal representation**. This fused representation is what is fit to the generative system and used to update the TA1 disease model. The barycenter formulation is strictly preferable to simple concatenation or mean-pooling because it preserves the distributional geometry of each modality's embedding space.

**Transcriptomic (scRNA-seq, Perturb-seq):**

| Source | Arm | Raw format | CDM target |
|---|---|---|---|
| **Element AVITI24 / Teton (Matt Tegtmeyer lab)** | Academic | DISS in-situ RNA reads + CRISPR-guide barcode reads (Element pipeline) | AnnData `.h5ad` with perturbation metadata in `.obs` and guide assignments in `.obs['guide_id']`; CZ CELLxGENE schema v5.0.0 conformant |
| Cellanome R3200 / Perturb-LINK | Industry | Seurat `.rds` export (per-CCE cell-barcode matrix, sgRNA reads) | AnnData `.h5ad` with perturbation metadata in `.obs` and guide assignments in `.obs['guide_id']`; CZ CELLxGENE schema v5.0.0 conformant |
| Illumina DRAGEN pipeline | Lab 3 | BAM plus Cell Ranger h5 matrix | AnnData `.h5ad` via scanpy `read_10x_h5`; DRAGEN QC report appended to `.uns['dragen_qc']` |

**Morphological (Cell Painting / live-cell imaging):**

| Source | Arm | Raw format | CDM target |
|---|---|---|---|
| **Element AVITI24 / Teton (Matt Tegtmeyer lab)** | Academic | Cell-Painting-style organelle features (nucleus, membrane, actin, ER, Golgi, mitochondria); onboard segmentation + feature extraction; Element proprietary but compatible with CellProfiler feature schema | Parquet feature matrix with CL-typed cell-type columns, perturbation metadata, and plate/well coordinates; fed directly into Anne Carpenter's computational morphology models |
| Carpenter CellProfiler (computational; applied to Element outputs) | Analysis | CSV of per-cell morphological features (>500 features/cell), compressed TIFF stacks | Parquet feature matrix with CL-typed cell-type columns, perturbation metadata, and plate/well coordinates; TIFF stacks retained as archived image data linked by URI |
| Cellanome AI morphotyping | Industry | Proprietary morphotype embedding JSON per CCE | Exportable as a dense embedding matrix; must be accompanied by the schema version of Cellanome's morphotyping model (a provenance dependency) |

**Electrophysiological (MEA / calcium imaging proxy):**

| Source | Raw format | CDM target |
|---|---|---|
| Axion Maestro MEA | HDF5 or AxIS binary | Extracted spike train statistics (mean firing rate, burst frequency, network synchrony index, inter-spike interval distribution) as a structured JSON per well; raw traces retained as linked HDF5 files |
| Cellanome calcium imaging | Fluorescence intensity timeseries per CCE (proprietary format) | Extracted calcium event statistics (event frequency, amplitude, rise/decay time) as structured JSON; raw timeseries linked by URI |

### 2.3 The streaming-versus-final-package distinction

Multi-day Cellanome R3200 runs generate continuous imaging data during the experiment. The CDM must distinguish two event types:

1. **Streaming QC update:** a partial data snapshot emitted during the run (e.g., at 24-hour intervals), containing live-cell imaging QC metrics (cell viability, imaging drift check, calcium activity baseline). This event updates the TA3 monitoring dashboard but does not trigger a TA1 model update.
2. **Final CDM package:** the authoritative end-of-run package emitted when RNA capture and sequencing are complete and all per-CCE data objects are linked. Only this event triggers the TA1 model-update pipeline.

The PROV-O record for the final package must include a `prov:wasDerivedFrom` link to all streaming QC update events that preceded it, so the full experimental timeline is recoverable.

---

## 3. The Provenance Chain: Closing the Loop with PROV-O and SBOL3

### 3.1 The full chain from TA1 uncertainty to TA1 update

The provenance chain established by the TA2-to-TA3 interface (documented in `IFACE_TA2_TA3__full.md`, Section 2.3) is extended here through execution to data return. The complete chain is:

```
TA1 uncertainty map entry (URI, JSON-LD)
  --> ExperimentIntent object (JSON-LD, LinkML schema; carries ta1_gap_reference)
    --> LabOP Protocol object (SBOL3 RDF; annotated with ExperimentIntent URI)
      --> Protocol specialization A (Carpenter, OpenTrons OT2 Python script)
      --> Protocol specialization B (Cellanome, SiLA 2 Feature calls)
    --> PROV-O execution record A (links to LabOP Protocol URI; carries instrument serial, timestamps, reagent lots)
    --> PROV-O execution record B
      --> CDM data package A (AnnData + QC report + PROV record; carries ta1_gap_reference)
      --> CDM data package B
        --> Concordance check (cross-package; produces concordance score)
          --> [PASS] Ingestion event (triggers TA1 Bayesian update pipeline)
              --> TA1 posterior update (reduces uncertainty in the referenced map entry)
                --> Updated uncertainty map entry (URI, JSON-LD; prov:wasDerivedFrom ingestion event)
```

Each arrow in this chain is a machine-readable, dereferenceable link. The PROV-O/SBOL3 grounding ensures that any downstream consumer, including the IV&V partner, can reconstruct the full lineage of any TA1 model state change back to the experiment that caused it.

### 3.2 SBOL3 as the protocol identity anchor

SBOL3 (McLaughlin et al., Frontiers Bioeng Biotech 2020, doi:10.3389/fbioe.2020.00486) provides persistent, dereferenceable URIs for LabOP Protocol objects. This URI is the common key that links the execution records from both TA4 laboratories back to the same canonical protocol, enabling the concordance check to compare two executions of an identical protocol specification rather than two independently authored protocols.

The SBOL3 URI is emitted by SIFT's LabOP toolchain when the Protocol object is created and stored in the version-controlled protocol repository. All downstream objects (specializations, execution records, CDM packages) carry this URI as a foreign key. Version control of the protocol repository means that if a protocol is revised (via the RFC change-control process), the old and new versions have distinct URIs and their respective data returns are not intermixed in concordance checks.

### 3.3 PROV-O execution record: required triples

The W3C PROV Data Model (PROV-O, https://www.w3.org/TR/prov-o/) defines three core classes: Entity, Activity, and Agent. For the TA4-to-TA1 interface, the minimum required PROV-O triples per execution record are:

| Relation | Subject | Object | Notes |
|---|---|---|---|
| `prov:wasGeneratedBy` | CDM data package (Entity) | Execution activity (Activity) | Links data to the run that produced it |
| `prov:used` | Execution activity (Activity) | LabOP Protocol specialization (Entity) | Links run to the protocol that governed it |
| `prov:wasAssociatedWith` | Execution activity (Activity) | TA4 laboratory (Agent) | Identifies which lab ran the protocol |
| `prov:hadMember` | LabOP Protocol specialization (Entity) | LabOP Protocol (canonical, SBOL3 URI) | Links the specialization to the canonical source |
| `prov:wasDerivedFrom` | CDM data package (Entity) | ExperimentIntent object (Entity) | Closes the loop: data was produced in response to this intent |
| `prov:atLocation` | Execution activity (Activity) | Instrument serial URI | Machine-level instrument identification for IV&V |
| `prov:startedAtTime` / `prov:endedAtTime` | Execution activity (Activity) | ISO 8601 timestamps | Run duration; required for latency computation |

The `prov:wasDerivedFrom` triple between the CDM package and the ExperimentIntent object is the most critical for the feedback loop: it allows TA1 to identify which uncertainty entry to update when it receives the data. Without this triple, automated routing is impossible.

### 3.4 Continuing the upstream SBOL3-PROV chain

The TA2-to-TA3 interface established that the ExperimentIntent object is stored as an annotation on the SBOL3 LabOP Protocol object (see `IFACE_TA2_TA3__full.md`, Section 2.3). This means the provenance chain from TA4 data all the way back to the TA2 tournament record and the TA1 uncertainty entry is fully recoverable by traversing SBOL3 annotations and PROV-O links:

- CDM data package `prov:wasDerivedFrom` ExperimentIntent (via the LabOP Protocol SBOL3 annotation)
- ExperimentIntent `ta1_gap_reference` --> TA1 uncertainty map entry URI
- TA1 uncertainty map entry URI --> Pillar 4 hub-selector output that identified the gap
- Pillar 4 hub-selector output --> Pillar 1 mechanistic network state at the time of gap detection

This chain enables full causal attribution of any model change: given an updated TA1 parameter, it is possible to trace back through the chain to the original mechanism gap that motivated the experiment.

---

## 4. Concordance and Quality-Control Gating

### 4.1 Architecture of the QC gate

QC gating is a two-stage process: per-laboratory QC runs first and is a necessary condition for a data package to advance to the concordance stage; cross-laboratory concordance runs second and is the gate for TA1 ingestion.

```
Lab A CDM package --> [Per-lab QC module A] --> PASS/FAIL
Lab B CDM package --> [Per-lab QC module B] --> PASS/FAIL
                                              |
                    [Both PASS] --> [Cross-lab concordance module] --> PASS/FAIL --> TA1 ingestion
                    [Either FAIL] --> Exception handler --> RFC revision queue
```

### 4.2 Per-laboratory QC thresholds (Phase I defaults)

The following thresholds are derived from published standards for each modality. They are starting points for the Phase I DDD workshop; the RFC process governs all subsequent changes.

**Transcriptomic QC:**

| Metric | Threshold | Basis |
|---|---|---|
| Median genes per cell | >= 500 (neurons); >= 1000 (standard cell lines) | Established single-cell QC community practice; CZ CELLxGENE ingestion standards |
| Percent mitochondrial reads | <= 20% (neurons); <= 15% (dividing cells) | Consensus QC threshold; neurons have naturally higher mitochondrial transcription |
| Doublet rate (Scrublet/Solo estimate) | <= 5% | Standard threshold; higher rates indicate loading problems |
| Guide assignment rate (Perturb-seq) | >= 80% of sequenced cells carry exactly one guide | TA3 protocol specification requirement |
| Sequencing depth (mean UMI per cell) | >= 2000 | Saturation threshold for gene-level detection in scRNA-seq |

**Morphological QC:**

| Metric | Threshold | Basis |
|---|---|---|
| Cell viability (live/dead stain or nuclear morphology) | >= 70% viable cells per well | Minimum for interpretable morphological profiles; below 70% indicates culture failure |
| Image focus score (Brenner gradient or equivalent) | >= 0.85 of images passing focus threshold | CellProfiler built-in focus QC; below 0.85 indicates imaging drift |
| Cell count per well | >= 200 cells per well (384-well plate) | Minimum for population-level morphological statistics |
| Batch-effect score (UMAP dispersion of well controls) | Z-score <= 2.0 relative to historical plate controls | CellProfiler-based batch QC; extreme outliers indicate reagent or plate failure |

**Electrophysiological QC (MEA):**

| Metric | Threshold | Basis |
|---|---|---|
| Active electrode fraction | >= 25% of electrodes active (>= 0.1 Hz mean firing rate) | Standard iPSC-neuron MEA maturation threshold; Axion Biosystems application note |
| Network synchrony index | Present (>= 0.05) | Confirms network-level activity rather than isolated firing |
| Spontaneous mean firing rate | >= 0.5 Hz across active electrodes | Minimum for statistical analysis of perturbation effects |

### 4.3 Cross-laboratory concordance computation

The concordance check compares the same experiment executed at two TA4 laboratories. The metric is modality-specific:

**Transcriptomic concordance:** Pearson correlation of log2-fold-change (log2FC) of top 500 differentially expressed genes (DEGs) between the perturbed and isogenic control conditions, computed independently at each lab. Concordance score = Pearson r(log2FC_lab_A, log2FC_lab_B).

Phase I threshold: >= 0.80. Phase II threshold: >= 0.90.

This metric is directly analogous to the cross-lab reproducibility metric used in the Perturb-seq community (Norman et al., Science 2019; Replogle et al., Cell 2022, doi:10.1016/j.cell.2022.05.013) and is defensible to the ARPA-H IV&V partner.

**Morphological concordance:** Pearson correlation of mean morphological feature vectors (>500 CellProfiler features) for the perturbed condition relative to the isogenic control, computed at each lab after median-absolute-deviation (MAD) normalization. Concordance score = Pearson r(delta_features_lab_A, delta_features_lab_B).

Phase I threshold: >= 0.80. Alternative metric: cosine similarity between median morphological embedding vectors (Cellanome AI morphotyping), which is dimensionality-independent.

**Electrophysiological concordance:** Pearson correlation of the mean firing rate, burst frequency, and network synchrony index change (perturbed minus control) between labs. A composite concordance score is computed as the mean of the three pairwise correlations.

Phase I threshold: >= 0.75 (relaxed relative to transcriptomic and morphological because MEA is highly sensitive to culture conditions and replicate variance is inherently higher in electrophysiology).

### 4.4 Exception handling

When a CDM package fails either the per-lab QC gate or the cross-lab concordance gate, the exception handler:

1. Classifies the exception by root cause (instrumentation failure, culture failure, protocol deviation, batch effect, or biological signal below detection).
2. Routes to the RFC change-control process if the root cause is a protocol parameter (e.g., reagent lot substitution, cell density change).
3. Returns the failed package to the data repository with a `QC_FAIL` provenance annotation (PROV-O `prov:wasInvalidatedBy`) rather than deleting it, so the failure is auditable.
4. Notifies the TA2 engine that the targeted uncertainty entry was not resolved; the uncertainty entry remains in the uncertainty map and may be re-nominated in the next experimental cycle.

The Phase III milestone requires >= 70% of exceptions handled autonomously. Achieving this requires that the exception classifier be trained on historical exception records from Phase I and Phase II operations.

---

## 5. Automated Ingestion and the Bayesian Model-Update Trigger

### 5.1 The ingestion event architecture

The TA1 model-update pipeline is triggered by an event, not a polling loop. This is architecturally important for meeting the latency targets: polling introduces a latency floor equal to the polling interval, whereas event-driven triggering begins the update pipeline within seconds of the concordance gate firing.

The recommended event architecture uses the following components:

1. **TA4 data-upload event:** when a TA4 laboratory uploads a CDM package to the shared data repository (e.g., an S3-compatible object store), the upload emits a webhook or message-queue event.
2. **Ingestion listener:** a lightweight service subscribes to the message queue. On receiving an upload event for a CDM package, it retrieves the package's QC report and provenance record.
3. **Per-lab QC module:** the ingestion listener runs the per-lab QC checks (Section 4.2) against the package. If QC fails, the exception handler is invoked. If QC passes, the package is added to a concordance-pending queue.
4. **Concordance trigger:** when both packages for a given ExperimentIntent arrive in the concordance-pending queue (identified by their shared LabOP Protocol SBOL3 URI), the concordance check runs. If concordance passes, the ingestion event is fired.
5. **Bayesian update worker:** the ingestion event triggers a compute job that retrieves the validated CDM packages, routes the data to the correct TA1 Pillar update target, and runs the posterior update. On completion, the updated uncertainty map entry is written to the uncertainty map store, and a new message is emitted to TA2 signaling that the uncertainty entry has been resolved.

The EMMAA (Ecosystem of Machine-Maintained Models with Automated Analysis; Gyori Lab, gyorilab.github.io) daily update loop, which triggers an AWS pipeline on each INDRA model update, provides the closest published precedent for this event-driven model-update architecture. EMMAA achieves sub-24-hour daily update cycles driven by literature-ingestion events, not experimental data events. Our pipeline extends this to experimental data ingestion by replacing EMMAA's NLP-based statement assembly step with the CDM-to-Bayesian-likelihood conversion module.

### 5.2 Routing data to the correct TA1 update target

Different data modalities update different components of the TA1 four-pillar architecture. Before routing to any update target, all returned modalities pass through the encoding and fusion pipeline described in Section 2.2: modality-specific encoders produce delta-pathway embeddings, and the barycenter of those embeddings is the multimodal representation that enters the disease model update. Single-modality returns (e.g., a transcriptomic-only return) skip the barycenter fusion step and enter the update pipeline directly as a single-modality delta-pathway embedding.

The fused representation updates the **disease-effect operator** of the three-latent SCM, specifically the `z^d` subspace, and refines the **deep structural causal model over disease axes** (Research Master, Section 31b, step 5). This is the mechanism by which a returned experiment closes the loop onto specific disease axes: the disease-axis conditioners (genomic factors from Section 31b) enter as the disease-effect operator of the three-latent SCM, and the returned data reduces per-axis uncertainty by updating the parameters of that operator.

| Modality | Encoder | Delta-pathway representation | Update target | Method |
|---|---|---|---|---|
| **Transcriptomic (scRNA-seq / Perturb-seq)** | SENA-delta encoder | GO biological process activity shifts (per-perturbation delta pathways) | Pillar 2 (SAMS-VAE posterior): update the sparse mechanism shift mask `m_t` and effect vector `e_t` for the tested perturbation; disease-effect operator of three-latent SCM | Amortized variational update: new cells are encoded into pathway space, ELBO is maximized on the new data added to the training batch; targeted single-perturbation gradient update |
| **Transcriptomic (Perturb-seq, pathway level, via Pillar 1)** | SENA-delta encoder | Same pathway activity shifts as above, now used for network scoring | Pillar 1 (mechanistic network): update edge belief scores via INDRA statement scoring on the new pathway activity data | INDRA belief propagation on the mechanistic network; edges supported by new data have belief scores increased; edges contradicted have belief scores decreased |
| **Morphological (Cell Painting / live-cell imaging)** | Morphological pathway encoder (projects CellProfiler features into pathway-activity space via gene-set enrichment mapping) | Delta-pathway representation of morphological state shifts (e.g., neurite morphology --> cytoskeletal pathway activity, nuclear morphology --> cell-cycle pathway activity) | Pillar 2 (basal state `z^b` and disease effect `z^d`): morphological delta-pathway embedding updates the basal state estimate for the cell type and the disease-specific deviation from basal; contributes to barycenter when co-returned with transcriptomics | Projection update: morphological features projected into pathway space via trained encoder; the projected delta-pathway embedding updates the Pillar 2 posterior via the CFGen/CellFlow decoder |
| **Electrophysiological (MEA)** | Electrophysiological pathway encoder (maps activity metrics to signaling pathway activity estimates, e.g., firing rate --> glutamate signaling pathway activity) | Delta-pathway representation of circuit-level state shifts | Pillar 1 (circuit-scale mechanistic network edges) and the Disease Map (MaBoSS attractor mapping); disease-effect operator of three-latent SCM (indirectly via Pillar 1 constraints) | The electrophysiological pathway embedding is compared to MaBoSS attractor predictions; agreements increase edge belief scores; disagreements flag edges for revision; contributes to barycenter in multi-modality returns |
| **Protein/PPI (SPOC SPR kinetics)** | Direct biochemical evidence (no pathway encoder; edge-level evidence) | Not delta-pathway featurized; treated as direct evidence for specific causal edges | Pillar 1 (specific mechanistic edges): direct biochemical evidence updates edge confidence | INDRA belief update with a high-weight biochemical evidence type |

### 5.3 The Bayesian update step: SAMS-VAE posterior update

For transcriptomic returns, the update target is the SAMS-VAE posterior over the sparse mechanism shift mask `m_t` and effect vector `e_t` for perturbation `t`. The update follows the standard variational inference update rule: the ELBO is computed on the new data combined with the existing data, and the variational parameters of the encoder are updated via gradient descent.

In practice, for incremental data returns (a single TA4 experiment rather than a full dataset retraining), this update is implemented as:

1. **Encode new cells:** the SENA-delta encoder maps the new Perturb-seq cells to GO biological process activity levels (alpha_k), then to per-perturbation SAMS-VAE latent states.
2. **Compute the ELBO increment:** the ELBO on the new data is computed against the current variational posterior. The gradient points in the direction of the parameters that reduce the uncertainty in `m_t` and `e_t`.
3. **Perform a targeted update:** gradient steps are taken only on the parameters associated with perturbation `t` (the tested perturbation), not on all perturbation parameters simultaneously. This is an online learning update, not a full retraining.
4. **Update the uncertainty map entry:** the posterior variance of the mechanism shift parameters for perturbation `t` is recomputed; if it falls below the phase-gated threshold (>= 20% variance reduction, Phase I milestone), the TA1 uncertainty map entry is marked as resolved.

The online SAMS-VAE update is analogous to the sequential Bayesian update demonstrated in the SMC (Sequential Monte Carlo) literature for online Bayesian inference (Chopin 2002; Del Moral et al. 2006). For the variational inference setting, the closest precedent is the incremental ELBO update in online scVI (Lopez et al. NeurIPS 2020 workshop). A Phase I software deliverable is to implement and validate this online update module on the Phase I anchor dataset (22q11DS vs. isogenic control in NGN2 neurons).

### 5.4 The Bayesian update step: Pillar 1 mechanistic network update

For morphological and electrophysiological returns, the primary update target is the Pillar 1 mechanistic network. The update follows the INDRA belief propagation framework (Gyori et al., Mol Syst Biol 2017):

1. **Convert experimental result to INDRA statement:** the per-perturbation pathway activity shifts (from SENA-delta encoder output) are converted to typed INDRA statements. For example: if SETD1A knockout produces a significant reduction in H3K4me3-related transcriptional activity, this becomes an INDRA `Inhibition(SETD1A, H3K4me3_target_gene_set)` statement with the experimental effect size and p-value encoded as belief evidence.
2. **Score the statement:** INDRA's belief model assigns an evidence score based on evidence type (experimental = high weight; literature = variable weight based on source quality). The new experimental statement is added to the network with its evidence score.
3. **Propagate the belief update:** INDRA's CoGEx module propagates the belief change upstream and downstream along the causal network, updating edges that are logically dependent on the newly evidenced edge.
4. **Flag newly contradicted edges:** if the new evidence contradicts an existing edge (e.g., literature predicted SETD1A activates H3K4me3 targets, but experiment shows inhibition), the contradicted edge is flagged in the uncertainty map as a high-priority gap requiring resolution.

### 5.5 Update-latency feasibility analysis

The Phase II latency target of 24 hours from data receipt to model update is achievable. The Phase III target of 4 hours is feasible but requires careful pipeline design.

**Phase II (24-hour) feasibility:**

| Step | Estimated duration | Bottleneck |
|---|---|---|
| CDM package upload and event emission | < 5 minutes | Network bandwidth for large imaging datasets |
| Per-lab QC module (transcriptomic) | 10-30 minutes | Doublet detection (Scrublet) and DEG computation on a 100K-cell dataset on a 32-core machine |
| Per-lab QC module (morphological) | 15-45 minutes | CellProfiler batch processing on TIFF image stacks; GPU-accelerated with a single NVIDIA A100 |
| Cross-lab concordance check | < 10 minutes | Pearson correlation computation on DEG vectors is trivially fast |
| SAMS-VAE online update (targeted) | 1-3 hours | Gradient descent on the SENA-delta encoder and SAMS-VAE variational parameters; GPU-accelerated |
| INDRA belief update and CoGEx propagation | 15-60 minutes | INDRA belief propagation on a ~50K-node network; Python-based; parallelizable |
| Uncertainty map write and TA2 notification | < 5 minutes | Database write |
| **Total (worst case)** | **~5 hours** | Well within 24-hour target |

The 24-hour target is comfortably achievable. Empirically, EMMAA demonstrates sub-24-hour daily update cycles on its COVID-19 and ALS models using similar INDRA-based pipelines running on AWS; our transcriptomic update adds the SAMS-VAE step, which is the new bottleneck.

**Phase III (4-hour) feasibility:**

| Step | Estimated duration (with optimization) | Required optimization |
|---|---|---|
| CDM package upload | < 2 minutes | Pre-partitioned upload (multipart S3 upload for large TIFF stacks) |
| Per-lab QC (transcriptomic) | < 15 minutes | GPU-accelerated doublet detection; pre-indexed reference embedding for cell typing |
| Per-lab QC (morphological) | < 20 minutes | Precompiled CellProfiler GPU pipeline; incremental image processing (images checked as they upload) |
| Cross-lab concordance | < 5 minutes | Parallelized across both labs |
| SAMS-VAE online update | < 45 minutes | Precompiled CUDA kernels for the targeted ELBO update; single-perturbation update (not full retraining) |
| INDRA belief update | < 15 minutes | C-based INDRA backend; belief propagation pruned to the directly affected subgraph |
| Uncertainty map write | < 2 minutes | In-memory graph database (e.g., Memgraph or RedisGraph) |
| **Total (optimized)** | **~100 minutes (~1.7 hours)** | Within 4-hour target with margin |

The 4-hour target is feasible with the optimizations listed. The critical path is the SAMS-VAE online update step. The 45-minute estimate assumes a targeted, single-perturbation gradient update (not a full model retraining) using precompiled CUDA kernels on a single NVIDIA A100 GPU. This assumption must be validated empirically in Phase II before committing to the Phase III milestone.

**Risk flag:** imaging data (TIFF stacks from CellProfiler) can exceed 1 TB per plate. For very large imaging experiments, the upload step alone may approach 30-60 minutes on a 1 Gbps link, which would stress the 4-hour pipeline. Mitigation: (a) implement streaming QC on images as they upload, rather than waiting for the full TIFF stack; (b) store raw images at the TA4 laboratory and transmit only the extracted feature matrix (CSV) as the CDM payload, with image stacks linked by URI rather than included in the package.

---

## 6. The SIFT Round Trip Closed-Loop Assessment

### 6.1 What Round Trip is

Bryce, Goldman, DeHaven, Beal, Bartley et al. (ACS Synth Biol, 2022, 11(2):608-622, doi:10.1021/acssynbio.1c00305, PMID 35099189) describe the Round Trip as "an open architecture that automates many of the key steps in the Test and Learn phases of a Design-Build-Test-Learn loop for high-throughput laboratory science." Its primary contribution is automated metadata creation, curation, standardization, and linkage with experimental data. The paper reports speedups of "2 orders of magnitude over prior ad hoc methods" for experimental analysis time and a large increase in data product volume. The system was developed under the DARPA SD2 (Synergistic Discovery and Design) program, operating on yeast logic-circuit genetic designs.

AutoGater (Eslami, Moseley, Eramian, Bryce, Haase et al., Sci Reports 2024, 14:23581, doi:10.1038/s41598-024-66936-8) is a weakly supervised neural network for automated flow-cytometry gating, developed in the same DARPA SD2 context. AutoGater identifies live versus dead yeast cells from flow-cytometry scatter/fluorescence data without requiring viability stains, using a novel objective function that harmonizes event-level and population-level evidence.

### 6.2 Genuinely reusable components for our mammalian disease loop

| Component | What it does in Round Trip | Reuse potential | Adaptation required |
|---|---|---|---|
| **Metadata schema and provenance linkage** | Formal knowledge representation linking experiment metadata to data; PROV-based lineage | **High.** The core insight that metadata must be structured before analysis can be automated is domain-independent. The metadata schema architecture (typed fields, ontology bindings, provenance links) maps directly onto our CDM package and PROV-O record design. | Replace synthetic-biology ontologies (SBOL, SO) with biomedical ontologies (CL, GO, MONDO, HPO); adapt field types for cell culture, transcriptomics, and imaging rather than genetic-part assembly |
| **Event-driven pipeline architecture** | Experiment completion triggers automated downstream analysis; no manual handoffs | **High.** The event-driven trigger model is domain-independent. Round Trip's architecture (upload triggers analysis pipeline) is the architectural template for our ingestion listener. | Replace flow-cytometry analysis with modality-specific QC modules for scRNA-seq, CellProfiler, and MEA |
| **Experimental situational awareness** | Real-time monitoring of experiment status; exception detection during the run | **Medium-High.** The concept of streaming monitoring versus final-package triggering maps onto our streaming-versus-final-package distinction (Section 2.3). | Adapt monitoring metrics from flow-cytometry scatter to live-cell imaging metrics (imaging drift, calcium activity baseline) |
| **Cross-experiment comparability** | Standardized metadata enables automated comparison of results across experimental campaigns | **Medium.** The Round Trip's emphasis on metadata standardization as the prerequisite for automated comparison is directly applicable; our CDM package serves the same role. | Concordance computation must be extended to multi-modality returns; Round Trip's flow-cytometry domain does not address multi-modality concordance |
| **Open software architecture (SBOL integration)** | Round Trip is built on SBOL for genetic design representation and PROV for provenance | **High.** Our use of SBOL3 (via LabOP) and PROV-O directly inherits this architectural choice. The Round Trip paper validates that SBOL+PROV is a workable foundation for automated lab loops. | SBOL3 (our version) supersedes SBOL2 (Round Trip's version); conversion is backward-compatible |

### 6.3 Synthetic-biology-specific components that do NOT transfer

| Component | Why it is domain-specific | What we need instead |
|---|---|---|
| **AutoGater flow-cytometry gating** | AutoGater is trained on yeast flow-cytometry scatter/fluorescence for live/dead discrimination. The weak supervision objective (harmonizing event-level and population-level death signal) is specific to yeast viability assays. iPSC-derived neurons do not use flow-cytometry viability gates in the same sense; viability is assessed by nuclear morphology (CellProfiler), calcium imaging, or live/dead staining in imaging wells. | Modality-specific per-lab QC modules: (a) CellProfiler-based nucleus morphology QC for imaging; (b) Seurat/scanpy percent-mitochondrial-reads and doublet detection for scRNA-seq; (c) Axion Maestro built-in spike detection QC for MEA |
| **Design-Build phases (genetic construct assembly)** | Round Trip's Design and Build phases automate genetic-part selection and physical construct assembly (yeast logic circuits). This has no analog in our iPSC culture and phenotyping workflow; we are not assembling genetic constructs on-the-fly. | TA3 (SIFT LabOP) handles protocol generation; the "Build" phase in our loop is iPSC differentiation and CRISPR delivery under the locked LabOP protocol |
| **Learn phase (genetic-part parameter inference)** | The Learn phase in Round Trip infers genetic-part performance parameters (e.g., promoter strength, RBS efficiency) from the measured circuit output. This is a synthetic-biology-specific model class. | Our Learn phase is the SAMS-VAE Bayesian posterior update on disease mechanism shift parameters (Section 5.3); structurally analogous but operating on a completely different model class |
| **Yeast-specific biological assumptions** | Round Trip assumes discrete, well-characterized genetic-part performance; the biological "signal" is circuit output (fluorescence, growth rate). iPSC-neuron experiments have continuous, high-dimensional gene expression outputs with far larger noise and batch-effect dimensions. | Multi-modality batch-effect correction (scVI / SCVI-tools harmony) must be added to the QC pipeline; this is not needed in Round Trip because yeast synthetic circuits have low batch effects relative to mammalian primary cell systems |
| **SD2 program-specific data formats** | Round Trip uses SD2 program-specific data representations that are not portable outside the DARPA SD2 context. | Our CDM is built on CZ CELLxGENE schema v5.0.0, AnnData, and CellProfiler CSV standards that are community-standard and IV&V-auditable |

### 6.4 Overall reusability assessment

Round Trip provides three directly reusable architectural principles for our mammalian disease loop: (1) the metadata-first approach to enabling automated analysis; (2) the event-driven pipeline that triggers computation on data upload rather than polling; and (3) the SBOL+PROV identity and provenance architecture. These principles are domain-independent and are already incorporated into our CDM design and ingestion architecture.

The specific algorithms (AutoGater), biological models (genetic-part parameter inference), and data formats (SD2-specific) are synthetic-biology-specific and cannot be reused directly. SIFT's track record of building a working end-to-end automated pipeline (speedup of 2 orders of magnitude over ad hoc methods) is strong credibility evidence, but our team must author new QC modules, new biological model update logic, and new domain-specific data schemas.

The honest framing for the proposal: Round Trip demonstrates that SIFT can build automated, provenance-linked, event-driven laboratory loops; it does not demonstrate that the specific components work in mammalian iPSC contexts. That generalization is a Phase I validation task.

---

## 7. How Returned Data Updates the Three-Latent SCM

### 7.1 The three-latent factorization

The three-latent structural causal model (Research Master, Section 30.5; described in `TA1_disease_models__full.md`, Section 7.2) decomposes each cell's latent state:

```
z_i = z^b_i  +  z^d_i  +  z^t_direct_i  +  f(z^d_i, z^t_indirect_i)
```

where:
- `z^b` (basal) = the cell's healthy intrinsic state, encoding cell-type identity and baseline biological process activities
- `z^d` (disease effect) = the sparse additive shift caused by disease-associated genetic variation; parameterized by the SAMS-VAE effect vector `e_t` and mask `m_t` for the disease perturbation `t`; the **disease-effect operator** is the causal mechanism that links the disease axes (Section 31b) to this latent subspace
- `z^t_direct` (treatment, direct path) = off-target/side-effect route of an experimental or therapeutic perturbation
- `f(z^d, z^t_indirect)` (treatment, disease-modulating path) = the therapeutically relevant path, where the treatment modulates the disease effect

The disease-axis conditioners from the genomic front-end (Research Master, Section 31b) enter as **exogenous variables** of this SCM and supply the structure of the **deep structural causal model over axes** (Section 31b, step 5). Updating the disease-effect operator of the three-latent SCM -- by ingesting a returned TA4 experiment -- simultaneously refines the deep SCM over axes, reducing per-axis uncertainty and improving the genomic front-end's causal coordinate system.

### 7.2 From raw modality return to model update: the encoding and fusion pipeline

Before any modality updates the three-latent SCM, it passes through the **modality-specific encoder and delta-pathway featurization pipeline** described in Section 2.2 and specified in Research Master Sections 32b extensions 3 and 4. This pipeline is the critical architectural addition that makes multi-modal returns directly ingestible:

1. **ETL to CDM format.** Each modality's raw data is converted to its CDM representation (Section 2.2 tables).
2. **Modality-specific encoder.** Each CDM payload is encoded by a modality-specific neural encoder that maps raw modality features into a fixed-dimensional embedding. The transcriptomic encoder is the SENA-delta encoder (GO biological process activity space). The morphological encoder projects CellProfiler features into a pathway-space representation via gene-set enrichment mapping (cell morphology features are mapped to the cytoskeletal, cell-cycle, and organelle-biogenesis pathway programs they reflect). The electrophysiological encoder maps circuit-activity metrics (firing rate, synchrony, burst frequency) into a signaling-pathway representation (glutamate signaling, GABA signaling, calcium signaling pathways).
3. **Delta-pathway featurization.** All encoders output **delta pathways** -- shifts in biological process pathway activity relative to the isogenic control -- rather than delta genes. This is the uniformity step that makes the representations cross-modality comparable (Research Master, Section 32b extension 3). Two modalities can now be compared in the same pathway-space coordinate system without a separate harmonization model.
4. **Barycenter fusion.** When two or more modalities are returned from the same experiment, the delta-pathway embeddings are fused via the **barycenter** (an optimal-transport-style average; Research Master Section 32b extension 4). The barycenter is the single **multimodal representation** that enters the generative system for the model update step. For single-modality returns, this step is skipped and the single embedding enters directly.
5. **Disease-effect operator update.** The fused (or single-modality) delta-pathway representation updates the disease-effect operator of the three-latent SCM, adjusting `z^d` and the corresponding disease-axis conditioners, thereby reducing per-axis uncertainty in the deep SCM over axes.

### 7.3 How each modality reduces parameter uncertainty in the three-latent SCM

**Transcriptomic return (Perturb-seq, isogenic disease vs. control):**

This is the primary data type for updating the disease effect `z^d`. The return provides direct measurement of the gene-expression shift caused by the disease-associated variant in a controlled isogenic background. The SENA-delta encoder maps per-cell gene expression shifts into GO biological process pathway activity changes, producing the delta-pathway embedding. The SAMS-VAE update:

- Reduces uncertainty in the mask `m_t`: which biological processes (pathways) are shifted by the disease-associated variant
- Reduces uncertainty in the effect vector `e_t`: the direction and magnitude of the shift in each affected biological process
- Indirectly informs `z^b`: the isogenic control cells provide a better estimate of the basal state for the specific cell type
- Updates the disease-effect operator of the three-latent SCM, propagating the per-axis uncertainty reduction into the deep SCM over axes

After the update, the TA1 model can generate more accurate counterfactual predictions: "if cells with this variant are shifted toward healthy with intervention X, how does the gene expression change?" This is the basis for PDGrapher's inverse-design step.

**Morphological return (Cell Painting / live-cell imaging):**

Morphological features update a complementary, modality-specific view of `z^b` and `z^d`. The morphological encoder first projects CellProfiler features into a delta-pathway representation (e.g., reduced neurite length maps to reduced cytoskeletal organization pathway activity; reduced nuclear area maps to altered cell-cycle pathway activity). This delta-pathway embedding is then either used alone or entered into the barycenter fusion with the transcriptomic embedding, depending on whether both modalities were returned from the same experiment.

Critically, morphological data provides evidence that is relatively independent of the transcriptomic pathway-space representation, even though both are expressed in pathway coordinates after encoding. A transcriptomically subtle disease variant may still produce a detectable morphological pathway signature (as demonstrated by the 22q11DS NeuroPainting study, Tegtmeyer et al., Nat Commun 2025, doi:10.1038/s41467-025-61547-x), or vice versa. Combining both via barycenter fusion reduces uncertainty in `z^d` more than either alone, and the pathway-space common coordinate system makes the combination geometrically meaningful.

The morphological return does not directly update `z^t` (treatment effect) unless a treatment is also included in the experiment (e.g., a rescue experiment comparing disease cells with and without a candidate therapeutic perturbation).

**Electrophysiological return (MEA / calcium imaging):**

Electrophysiological data updates the circuit-scale component of the disease model, specifically the attractor states in the SBML-qual/MaBoSS Boolean model (the Pillar 4 Disease Map layer). The electrophysiological encoder maps activity metrics (mean firing rate, burst frequency, network synchrony index) into a signaling-pathway representation: for example, reduced NMDA-receptor-mediated spontaneous firing maps to reduced glutamate signaling pathway activity, which is a delta-pathway feature directly comparable with the transcriptomic pathway embedding for the same perturbation.

For GRIN2A (NMDA receptor) and GRIA3 (AMPA receptor) variants in the SCHEMA panel, the electrophysiological readout is the most direct test of the predicted disease mechanism: reduced NMDA-receptor function predicts reduced spontaneous firing rates and reduced network synchrony in iPSC-neuron networks. A concordant MEA result would strongly reduce uncertainty in the GRIN2A-to-network-activity causal chain in Pillar 1. The electrophysiological delta-pathway embedding contributes to the barycenter when co-returned with transcriptomic and morphological data, and its consistency with the transcriptomic delta-pathway embedding on the glutamate signaling pathway is a direct test of model coherence.

The electrophysiological return updates the disease effect `z^d` indirectly, by constraining the Pillar 1 mechanistic network edges that link molecular perturbation to circuit-level phenotype. This is an important but less direct update than the transcriptomic return.

**Protein/PPI return (SPOC SPR kinetics):**

PPI validation data updates specific, predicted causal edges in the Pillar 1 mechanistic network. SPOC's SPR kinetics (on-rate, off-rate, affinity, residence time) for a predicted protein-protein interaction are the highest-quality biochemical evidence for an edge's existence and strength. These are treated as direct evidence updates in the INDRA belief scoring system, with a high evidence weight (higher than any literature evidence type).

PPI data is not delta-pathway featurized in the same sense as the cell-state modalities; it provides edge-level biochemical evidence rather than state-level pathway activity shifts. It does not enter the barycenter fusion. This update does not directly modify the SAMS-VAE latent structure; it operates one level deeper, at the level of which mechanistic edges are real and which are artifacts of incomplete biological knowledge. Over Phase II and III, as more PPI validation data accumulates, the Pillar 1 mechanistic network should converge toward a smaller, more confident set of edges, which in turn improves the causal structure that the deep SCM over axes learns from.

### 7.4 Cross-modality coherence and identifiability

A potential risk is that updates from different modalities produce incoherent estimates: transcriptomics may say that biological process A is shifted, while morphology provides no signal on process A. This is expected and not a failure: the three modalities access different aspects of the disease biology, and they may validly disagree on which biological processes are most affected.

The delta-pathway featurization (Section 7.2, step 3) is the key that makes disagreements interpretable rather than irreconcilable: because all modalities express their disease-effect estimates in the same GO biological process pathway-activity coordinate system, a disagreement between the transcriptomic and morphological pathway embeddings on a given biological process becomes a model prediction to be resolved by a targeted follow-up experiment, not an uninterpretable conflict between incompatible feature spaces. The SENA-discrepancy-VAE pathway-space encoder (de la Fuente et al., ICLR 2025, arXiv:2506.12439) grounds this common coordinate system.

The barycenter fusion (Section 7.2, step 4) does not suppress inter-modality disagreement: each modality's contribution to the barycenter is weighted by its embedding confidence, so a modality with high uncertainty contributes less to the fused representation. Modalities that strongly agree on a pathway shift reinforce each other's contribution to the barycenter; modalities that disagree reduce the barycenter's confidence on that pathway, which is the correct signal for flagging it as an unresolved model gap for TA2.

This cross-modality coherence property is a key feature of the three-latent SCM that would be lost if modalities were updated independently in separate model instances.

---

## 8. Alignment to TA1 and TA4 ISO Objectives and Phases

### 8.1 Phase I (18 months): Concept and Component Validation

| IGoR requirement | How the TA4-to-TA1 interface addresses it | Evidence of feasibility |
|---|---|---|
| Walking-skeleton closed loop | CDM package from Cellanome and Carpenter ingested and used to update TA1 within <= 24 hrs for the TBX1 exon 2 CNV anchor experiment | EMMAA precedent for event-driven model update; SAMS-VAE online update is a standard variational inference step |
| >= 20% variance reduction in TA1 parameter uncertainty from first TA4 return (Phase I milestone) | SAMS-VAE online update on TBX1-specific mechanism-shift mask `m_t` | Lopez et al. CLeaR 2023 demonstrates variance reduction from Perturb-seq data in the sVAE framework |
| Phase I concordance >= 80% | Concordance check on morphological + transcriptomic returns from Carpenter and Cellanome on the same isogenic lines | NeuroPainting study (Tegtmeyer et al. 2025) demonstrates cross-well concordance of Cell Painting features in 22q11DS neurons |
| 100% TA1 artifacts containerized for IV&V | The CDM package format and ingestion pipeline are containerized as part of the TA1 software stack | LinkML schema generates Python validators; PROV-O records are RDF serializations with no platform dependencies |
| CDM package format defined | LinkML CDM schema v1.0 ratified at DDD workshop | This document provides the template; DDD workshop refines it |

### 8.2 Phase II (18 months): Integration and Interoperability

| IGoR requirement | How the TA4-to-TA1 interface addresses it |
|---|---|
| Update latency <= 24 hours | Full pipeline validated on >= 10 ingested experiments; latency distribution tracked; P95 <= 24 hours |
| Cross-team concordance >= 90% | Carpenter, Cellanome, and Illumina all executing from the same canonical LabOP Protocol; concordance computed on the shared variant panel |
| Three-latent SCM integrated | Disease, basal, and treatment latent subspaces each updated by at least one confirmed TA4 data return; the joint posterior is computed |
| >= 10 sub-models | Each ingested experiment contributes to one or more sub-models (variant-specific, cell-type-specific, pathway-specific) |

### 8.3 Phase III (24 months): Scaling and Generalization

| IGoR requirement | How the TA4-to-TA1 interface addresses it |
|---|---|
| Update latency <= 4 hours | Pipeline fully optimized (GPU-accelerated QC, precompiled SAMS-VAE CUDA kernels, in-memory graph database for INDRA); Phase III target is met |
| >= 70% exceptions handled autonomously | Exception classifier trained on Phase I-II exception history; autonomous root-cause classification for common failure modes |
| Extension to idiopathic schizophrenia | CDM package format extended to PGC GWAS soft-intervention parameterization; SCHEMA rare-variant returns ingested by same pipeline with extended perturbation vocabulary |
| Open data release | CDM packages, QC reports, and PROV-O execution records published under CC BY 4.0 at each phase milestone; schema published under Apache 2.0 |

---

## 9. Gaps and Best-Fit Composition

### 9.1 Gap summary

| Gap | Severity | Owner | Resolution path | Phase target |
|---|---|---|---|---|
| CDM package format (LinkML schema) not yet defined | High | Cytognosis + SIFT | DDD workshop; draft is in this document | Phase I Month 3 |
| SAMS-VAE online update module not implemented | High | Cytognosis | Phase I software deliverable; model on Lopez et al. CLeaR 2023 online update | Phase I Month 12 |
| Modality-specific QC modules not implemented | High | Cytognosis (transcriptomic), Carpenter (morphological), Axion/Cellanome (electrophysiological) | Phase I engineering deliverables; use community-standard tools (Scrublet, CellProfiler QC, Axion built-in QC) | Phase I Month 6 |
| Concordance computation module not implemented | High | Cytognosis | Phase I software deliverable; straightforward once CDM format is defined | Phase I Month 9 |
| Ingestion listener (event-driven trigger) not implemented | High | Cytognosis | Phase I software deliverable; standard message-queue architecture | Phase I Month 9 |
| PROV-O execution records not generated by TA4 labs | High | SIFT + TA4 labs | LabOP execution engine generates PROV-O natively; require TA4 labs to run the LabOP execution engine or an equivalent PROV emitter | Phase I Month 6 |
| Exception classifier (autonomous exception handling) not trained | Medium | Cytognosis | Requires Phase I-II exception history for training; Phase III deliverable | Phase III |
| Streaming QC versus final-package distinction not formalized | Medium | Cytognosis + Cellanome | Specify in CDM schema; implement as separate event types in the message queue | Phase I Month 6 |
| SAMS-VAE 4-hour update latency not empirically validated | Medium | Cytognosis | Phase II validation experiment; instrument the pipeline and measure end-to-end latency | Phase II Month 6 |
| Morphological CDM format (Parquet feature matrix) not defined | Medium | Cytognosis + Carpenter | Extend CDM schema to include CellProfiler-specific columns; validate against JUMP dataset format | Phase I Month 6 |
| **Morphological pathway encoder not implemented** | High | Cytognosis | Phase I software deliverable; train encoder to project CellProfiler features into GO biological process pathway-activity space; validate on JUMP Cell Painting dataset | Phase I Month 9 |
| **Electrophysiological pathway encoder not implemented** | High | Cytognosis | Phase I software deliverable; train encoder to map MEA activity metrics into signaling-pathway activity space; validate on published iPSC-neuron MEA datasets (Axion Biosystems reference datasets) | Phase I Month 9 |
| **Barycenter fusion module not implemented** | High | Cytognosis | Phase I software deliverable; implement optimal-transport barycenter of per-modality delta-pathway embeddings; validate that barycenter of transcriptomic and morphological embeddings outperforms single-modality update on Phase I anchor dataset | Phase I Month 12 |
| **Deep SCM over disease axes not yet coupled to disease-effect operator update** | High | Cytognosis | Phase I engineering deliverable; implement the coupling of disease-axis conditioners (Research Master Section 31b step 5) to the three-latent SCM disease-effect operator; validate per-axis uncertainty reduction on Phase I anchor dataset | Phase I Month 12 |

### 9.2 Best-fit component summary

| Component | Role at the interface | Justification |
|---|---|---|
| LinkML | CDM schema definition; generates validators, Python dataclasses, JSON-LD | Bidirectional serialization; ontology binding; RDF compatibility; NCATS-maintained |
| PROV-O (W3C) | Execution record provenance; traceability of data lineage | W3C standard; native LabOP output; required for IV&V audit trail |
| SBOL3 (via LabOP) | Protocol identity anchor; SBOL3 URI is the common key for concordance linkage | Required for TA2-to-TA3 chain continuity; SIFT LabOP generates natively |
| AnnData / CZ CELLxGENE schema v5.0.0 | CDM format for transcriptomic returns | Community standard; directly consumable by Seurat, scanpy, and the Pillar 2 encoder |
| CellProfiler feature CSV / Parquet | CDM format for morphological returns | Community standard; directly aligned with JUMP dataset format |
| **SENA-delta encoder (transcriptomic modality-specific encoder)** | Encodes per-cell gene expression into GO biological process delta-pathway features; produces the transcriptomic delta-pathway embedding | Established in de la Fuente et al. ICLR 2025; provides the uniform pathway-space coordinate system for cross-modality comparison |
| **Morphological pathway encoder** | Projects CellProfiler morphological features into pathway-activity delta-pathway features (cytoskeletal, cell-cycle, organelle-biogenesis programs) | Phase I software deliverable; grounds morphological returns in the same pathway-space coordinate system as transcriptomics |
| **Electrophysiological pathway encoder** | Maps MEA activity metrics (firing rate, synchrony, burst frequency) into signaling-pathway delta-pathway features | Phase I software deliverable; enables electrophysiological returns to enter the barycenter fusion pipeline |
| **Barycenter fusion module** | Computes the optimal-transport-style barycenter of per-modality delta-pathway embeddings to produce the multimodal representation for the disease-model update | Research Master Section 32b extension 4; Phase I software deliverable; replaces ad hoc modality concatenation |
| SAMS-VAE online update (adapted from Lopez et al. CLeaR 2023) | Bayesian posterior update for the disease-effect operator of the three-latent SCM; updates the disease-axis conditioners via the fused multimodal representation | Proven framework for sparse mechanism shift inference; online update extension is a straightforward variational inference step |
| INDRA + CoGEx (Gyori Lab) | Mechanistic network belief update for all modalities | Published, maintained knowledge-assembly system; EMMAA demonstrates production-scale daily update cycles |
| EMMAA architecture (AWS-triggered pipeline) | Event-driven model-update architecture template | Only published precedent for event-driven Bayesian model update in a biomedical AI context |
| Scrublet / Solo | Transcriptomic per-lab QC (doublet detection) | Community-standard tools; widely validated on scRNA-seq datasets |
| CellProfiler built-in QC (focus score, viability) | Morphological per-lab QC | Established in the JUMP dataset and NeuroPainting study |
| Axion Maestro built-in spike detection | Electrophysiological per-lab QC | Standard iPSC-neuron MEA QC; validated in published iPSC-MEA studies |

---

## Consolidated References

**Round Trip and AutoGater:**
- Bryce D, Goldman RP, DeHaven M, Beal J, Bartley B, et al. Round Trip: An Automated Pipeline for Experimental Design, Execution, and Analysis. ACS Synth Biol. 2022 Feb 18;11(2):608-622. doi:10.1021/acssynbio.1c00305. PMID: 35099189.
- Eslami M, Moseley RC, Eramian H, Bryce D, Haase S, et al. AutoGater: a weakly supervised neural network model to gate cells in flow cytometric analyses. Sci Reports. 2024;14:23581. doi:10.1038/s41598-024-66936-8.

**Standards:**
- McLaughlin JA et al. SBOL version 3: Simplified data exchange for biodesign. Front Bioeng Biotechnol. 2020. doi:10.3389/fbioe.2020.00486.
- W3C PROV Data Model. https://www.w3.org/TR/prov-o/ (accessed 2026-06-14).
- Bartley B et al. Building an Open Representation for Biological Protocols. ACM JETC 19(3), 2023. doi:10.1145/3604568.
- Moxon S et al. The LinkML Modeling Language. 2021. https://linkml.io.

**INDRA and EMMAA:**
- Gyori BM et al. From word models to executable models of signaling networks using automated assembly. Mol Syst Biol. 2017;13:954. doi:10.15252/msb.20177651.
- EMMAA GitHub: https://github.com/gyorilab/emmaa (accessed 2026-06-14).

**TA1 disease model and SAMS-VAE:**
- Bereket M, Karaletsos T. Modelling Cellular Perturbations with the Sparse Additive Mechanism Shift Variational Autoencoder. NeurIPS 2023. arXiv:2311.02794.
- Lopez R, Tagasovska N, Ra S, Cho K, Pritchard J, Regev A. Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling. CLeaR 2023. arXiv:2301.12946.
- de la Fuente J et al. Interpretable Causal Representation Learning in Pathway Space. ICLR 2025. arXiv:2506.12439.
- Zhang J et al. Identifiability Guarantees for Causal Disentanglement from Soft Interventions. NeurIPS 2023. arXiv:2307.06250.

**TA4 experimental platforms:**
- Tegtmeyer M et al. NeuroPainting precedent, 22q11DS. Nat Commun. 2025. doi:10.1038/s41467-025-61547-x.
- Replogle JM et al. Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. Cell. 2022. doi:10.1016/j.cell.2022.05.013.

**IGoR program materials:**
- ARPA-H. IGoR Program and Technical Description. Appendix A, ARPA-H-SOL-26-155. 2026.

**Internal cross-references:**
- `TA4_labs__full.md` - TA4 laboratory roster and data types
- `TA1_disease_models__full.md` - TA1 four-pillar architecture and three-latent SCM
- `IFACE_TA2_TA3__full.md` - upstream provenance chain established at TA2-to-TA3
- `SIFT_capabilities_analysis.md` - SIFT Round Trip and LabOP assessment

**Citations flagged for verification before submission:**
- Tegtmeyer et al. Nat Commun 2025 doi:10.1038/s41467-025-61547-x: verify authorship includes Carpenter lab.
- Replogle et al. Cell 2022: confirm DOI resolves to the Mapping information-rich Perturb-seq paper.
- EMMAA (Gyori Lab): confirm latest production-deployment update-latency figures from gyorilab.github.io.
- AutoGater doi:10.1038/s41598-024-66936-8: confirmed via PubMed search 2026-06-14.
- Round Trip doi:10.1021/acssynbio.1c00305, PMID 35099189: confirmed via PubMed 2026-06-14.
