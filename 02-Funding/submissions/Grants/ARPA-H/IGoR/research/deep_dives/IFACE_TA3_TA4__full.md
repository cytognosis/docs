# TA3-to-TA4 Interface: Protocol Encodability, Calibration Artifacts, and Capability Manifests

**Document type:** Internal deep dive, IGoR proposal series
**Compiled:** 2026-06-14
**Scope:** The TA3-to-TA4 interface contract; per-candidate LabOP encodability analysis; Phase I standards-development work required; alignment to IGoR objectives and phases; gaps and risk register.

> [!NOTE]
> **Internal only.** This document informs proposal drafting and does not represent a commitment by any TA4 candidate. All citations should be verified before inclusion in any submission. Cross-references to restricted sections (31, 32, 41, 42) are conceptual only and must not appear in any external build.

---

## Abstract / BLUF

The TA3-to-TA4 interface is the most technically complex single boundary in the IGoR system. TA3 (SIFT, LabOP) must deliver machine-readable, hardware-specialized protocol specifications that four heterogeneous candidate platforms can ingest and execute; each platform returns QC-rich, provenance-linked data packages that TA1 ingests automatically. No existing open standard spans this gap end-to-end for any of the four candidates. LabOP can encode the Carpenter (OpenTrons-based morphological profiling) workflow today using existing primitives. LabOP can encode Illumina library preparation with modest, achievable extension work. Cellanome R3200 requires a new SiLA Feature Definition and new LabOP imaging primitives -- substantial Phase I engineering, but structurally tractable. Panome Bio operates as a contract service with no published automation API, making LabOP specialization unclear and dependent on a technical-disclosure exchange. The two-layer deliverable required by the interface is: (1) a capability manifest schema (per-laboratory, machine-readable, versioned) and (2) calibration artifact definitions (IV&V-aligned reference samples and measurement datasets). Both must be defined in Phase I. These two deliverables, combined with LabOP primitive extensions for the Cellanome and Illumina modalities, constitute the critical Phase I TA3 engineering path and the main risk to the Phase I walking-skeleton milestone.

---

## 1. The Interface Contract: What TA3 Delivers to TA4 and What TA4 Returns

### 1.1 Directional information flows

The IGoR Program and Technical Description (Appendix A, ARPA-H-SOL-26-155) requires a bidirectional TA3-to-TA4 communication. Appendix A, Section 4.1.4 specifies: "Two-way communication of laboratory capabilities, calibration data, experimental procedures, results, and exceptions." This bidirectional contract has two distinct channels with different cadences and formats.

**Outbound (TA3 to TA4):** Protocol delivery. TA3 generates a hardware-specialized protocol from the canonical LabOP representation and delivers it to the executing TA4 laboratory. The specialized protocol carries:

- The LabOP-specialized execution file (e.g., an OpenTrons OT2 Python script, a SiLA Feature call sequence, or a structured SampleSheet for Illumina).
- The locked parameter set (version-controlled, RFC-governed).
- Quality control specifications and acceptance thresholds for each execution step.
- Calibration status declarations (which instruments were validated against which IV&V artifact, when, and by whom).
- Provenance metadata linking the run to the canonical LabOP protocol via its SBOL3 URI.

**Inbound (TA4 to TA3/TA1):** Data and execution record return. Each TA4 laboratory returns, within the latency window specified for the current phase:

- Raw experimental data in the modality-specific format (CellProfiler feature matrix, Seurat `.rds` object, FASTQ/BAM files, LC/MS feature tables).
- A PROV-O conformant execution record documenting actual parameter values, instrument serial numbers, reagent lot identifiers, operator actions, timestamps, and any deviations from the locked specification.
- QC metrics and pass/fail assessments for each QC checkpoint in the executed protocol.
- Exception flags for any step that required human intervention, with a structured exception descriptor.

The TA3-to-TA4 interface is therefore not a single handoff but a paired transaction: outbound protocol delivery and inbound data/provenance return. The Phase I walking skeleton (Appendix A, Table 1) requires this full closed-loop cycle to be demonstrated within 18 months.

### 1.2 Protocol specialization: from LabOP canonical to hardware-specific

LabOP's specialization mechanism is the technical foundation of protocol delivery. As detailed in the TA3 deep dive (`TA3_protocols__full.md`), LabOP encodes a protocol once as a UML activity model serialized in SBOL3 RDF, then compiles hardware-specific execution files from that single canonical source. The specializers currently implemented in the `labop` Python library target:

- OpenTrons OT2 (Python protocol scripts).
- Autoprotocol (Strateos JSON format).
- SiLA-based automation (via SiLA Feature calls).
- Echo acoustic dispensing (Beckman Coulter).
- Human-readable Markdown.

For the four TA4 candidates, the specialization targets are:

| TA4 Candidate | Target specialization format | Current LabOP support |
|---|---|---|
| Carpenter / Broad (morphological) | OpenTrons OT2 Python scripts; CellProfiler pipeline YAML | OpenTrons: existing. CellProfiler: not yet in LabOP |
| Cellanome R3200 | SiLA Feature Definition calls (R3200 interface) | SiLA framework: existing. R3200 Feature Definition: does not exist publicly |
| Illumina BioInsight | SampleSheet.csv; DRAGEN pipeline configuration | No LabOP specializer; standard text-file format; achievable with modest extension |
| Panome Bio | LC/MS instrument control files; Panome proprietary LIMS intake | No LabOP specializer; API undisclosed; unclear feasibility |

### 1.3 The capability manifest: defining what each laboratory can execute

Appendix A, Table 1 (TA4, Phase I) requires "two-way communication of capabilities established" and "all laboratory capability manifests current and publicly queryable" by Phase III. No open standard for laboratory capability manifests currently exists. This is a novel TA3 deliverable.

A capability manifest is a machine-readable document, versioned and signed by the laboratory, that declares:

- Instruments currently active and calibrated, with model, serial number, and calibration date against IV&V artifacts.
- Experimental modalities the laboratory can execute, with associated LabOP protocol URIs for each qualified modality.
- Current capacity constraints (available plate slots per week, throughput limits, scheduled downtime).
- QC performance statistics on completed runs (mean concordance, exception rate, data return latency).
- Data-format versions for each modality's output (CellProfiler pipeline version, Seurat version, DRAGEN version, etc.).

The recommended serialization format is a LinkML schema (consistent with the TA3 metadata recommendation in `TA3_protocols__full.md`, Section 7.4). LinkML allows the schema to be published as JSON Schema, RDF, or YAML -- covering the range of TA1 and TA3 tooling preferences without vendor lock-in.

**Phase I deliverable:** Define the LinkML capability manifest schema for at least two TA4 laboratories (Carpenter and Cellanome). Validate the schema by populating a complete manifest for each laboratory and confirming that the TA3 planning-and-scheduling layer can query it to select the appropriate specialization target.

### 1.4 Calibration artifacts: IV&V-aligned reference materials

Appendix A, Section 4.1.3 states: "Calibration layer conformance will be established by creating, in collaboration with the IV&V partner, a set of required calibration artifacts." These artifacts are physical reference materials and associated measurement datasets that establish instrument equivalence across laboratories.

For the four TA4 candidates, calibration artifacts must be defined per modality:

| Modality | Calibration artifact | Reference standard |
|---|---|---|
| Morphological profiling (Carpenter) | JUMP-CP standard cells (U2OS + DMSO control); CellProfiler pipeline output on reference plate | Cimini et al. *Nat Methods* 2023; JUMP-CP consortium reference dataset |
| Live-cell imaging (Cellanome R3200) | Standard fluorescent bead suspension; reference brightfield resolution target; CCE loading efficiency reference | No published IV&V standard; must be defined with Cellanome |
| Transcriptomics (Cellanome; Illumina) | Reference RNA spike-in (ERCC or Lexogen SIRV); fixed-composition synthetic cell reference (e.g., TrUE-seq RNA standards) | ERCC RNA Spike-In Mix (Thermo Fisher); SIRV-Set (Lexogen) |
| Library preparation / sequencing (Illumina) | PhiX control library; known-genotype reference sample (e.g., NA12878 Genome in a Bottle); standard sequencing run QC metrics | Illumina PhiX Control v3; Zook et al. GIAB benchmarks |
| Multi-omics (Panome Bio) | NIST certified reference material SRM 1950 (metabolites in human plasma); LIPID MAPS reference standard | NIST SRM 1950; LIPID MAPS database standards |

The IV&V partner reviews calibration artifact definitions and validates that executing the artifact protocol at two independent laboratories produces concordant results within the stated tolerance. IV&V artifact execution is gated on instrument validation: until a laboratory's instruments are validated against the artifact, that laboratory cannot be designated as a TA4 marketplace participant.

---

## 2. Per-Candidate LabOP Encodability Analysis

### 2.1 Carpenter Laboratory (morphological profiling and optical pooled CRISPR screening)

**Platform summary:** Carpenter's primary workflows are Cell Painting (six-dye multiplex morphological profiling using automated epifluorescence microscopy and CellProfiler image analysis) and optical pooled CRISPR screening (guide delivery by lentiviral transduction followed by in situ sequencing and CellProfiler morphological readout). Both workflows depend on two sub-systems: a liquid-handling robot (OpenTrons OT2 or similar for plate preparation and staining) and an imaging platform (high-content imager, typically an Opera Phenix or ImageXpress, with CellProfiler as the analysis back-end).

**Layer-by-layer encodability assessment:**

*Intent layer:* LabOP's existing Protocol intent primitives can encode the Cell Painting experimental intent directly. A Protocol object with typed inputs (cell line, perturbation library, timepoint) and typed outputs (morphological feature matrix, per-cell measurements) maps cleanly onto the Cell Painting experimental design. No new LabOP constructs are required at this layer.

*Protocol layer:* Cell Painting liquid handling (media changes, staining steps, fixation, permeabilization, nuclear staining) uses a sequence of Transfer, Provision, Incubate, and MeasureFluorescence LabOP primitives, all of which exist in the current library. The optical pooled screening ISS cycles (amplification, ligation, imaging per cycle) can be represented using existing Incubate and Transfer primitives for the biochemical steps, with a new imaging primitive required for the cyclic imaging acquisition.

*Calibration layer:* The JUMP-CP reference dataset (Chandrasekaran et al. *Nat Methods* 2023) provides the open calibration baseline for morphological profiling. LUDOX absorbance calibration (already in the LabOP standard) covers plate-reader QC. Fluorescence bead calibration for imaging channels requires a new LabOP calibration primitive, but this is a straightforward extension of the existing `MeasureFluorescence` primitive.

*Hardware layer:* The OpenTrons OT2 specializer is production-ready in the `labop` Python library. The CellProfiler pipeline is invoked after imaging, not as a LabOP hardware action, but the pipeline invocation can be represented as a SoftwareAction primitive that calls CellProfiler with a specified pipeline YAML. No SoftwareAction primitive currently exists in LabOP -- this is a new primitive required, but it is architecturally straightforward (it mirrors the existing instrument-action primitive pattern).

**Encodability verdict -- Carpenter:**

| Layer | Status | Work required |
|---|---|---|
| Intent | Possible now | None |
| Protocol (liquid handling) | Possible now | None; existing Transfer/Provision/Incubate primitives sufficient |
| Protocol (ISS imaging cycles) | Possible with work | New CyclicImagingStep primitive; estimated 2 person-weeks |
| Calibration | Possible with work | Fluorescence bead calibration primitive; JUMP reference dataset integration; estimated 1 person-week |
| Hardware (OT2) | Possible now | OpenTrons OT2 specializer production-ready |
| Hardware (CellProfiler) | Possible with work | New SoftwareAction primitive for pipeline invocation; estimated 1 person-week |

**Overall Carpenter verdict: largely possible now; 4 person-weeks of Phase I LabOP extension work to reach full encodability.**

**Risk:** Low. The OpenTrons path is established. CellProfiler integration via a SoftwareAction primitive is architecturally standard. No proprietary API dependencies.

---

### 2.2 Cellanome R3200

**Platform summary:** The R3200 integrates cell loading and selection, longitudinal live-cell fluorescence imaging (brightfield plus four-channel fluorescence at 4X and 10X), programmable reagent and media delivery, RNA capture, and cloud data integration -- all within a single walk-away instrument using CellCage microenvironment enclosures. The Perturb-LINK workflow adds pooled CRISPR guide delivery and end-point scRNA-seq library preparation from the same CCE-enclosed cells. The R3200 is a proprietary platform launched publicly in December 2025; Cellanome's control software and API are not publicly documented.

**Layer-by-layer encodability assessment:**

*Intent layer:* LabOP's intent primitives can express the Perturb-LINK experimental intent: perturbation library delivered to CCE-enclosed cells of specified type, longitudinal imaging over a defined timeframe, end-point RNA capture. The intent encoding is modality-agnostic and requires no new LabOP constructs.

*Protocol layer:* The Perturb-LINK protocol has several sub-steps that currently lack LabOP primitives:

- CCE loading (seeding cells into CellCage microenvironments): requires a new `LoadCellCage` primitive capturing loading volume, cell density, coating substrate, and CCE well-plate address. No equivalent exists in the current library.
- Longitudinal imaging (time-series fluorescence acquisition with temperature and CO2 control): requires a new `AcquireTimeLapseImage` primitive specifying imaging channels, frame interval, total duration, and environmental conditions. The existing `FlowCytometry` primitive is not analogous; live-cell imaging time series is architecturally distinct.
- Programmable reagent delivery to CCEs (media replacement, CRISPR guide addition, drug treatment): the existing `Transfer` primitive may partially cover this, but CCE-specific delivery (which preserves cell enclosure) differs from standard plate-based transfer and requires a `CCEDelivery` sub-type.
- RNA capture from CCEs and on-device library preparation: this is a multi-step process that partially overlaps existing library-preparation primitives but requires CCE-specific lysis and capture steps.

*Calibration layer:* No published IV&V calibration standard exists for the R3200. Phase I requires collaborative definition of: CCE loading efficiency reference (expected cells per CCE), fluorescence channel calibration using fluorescent bead standards, RNA capture efficiency reference using ERCC spike-ins, and concordance criteria for the morphological embeddings generated by Cellanome's AI morphotyping pipeline. These must be co-defined with Cellanome under NDA.

*Hardware layer:* This is the highest-risk layer. The R3200 does not have a publicly documented SiLA Feature Definition or equivalent open API. Cellanome's control software is proprietary. TA3 (SIFT/LabOP) cannot develop an R3200 SiLA specializer without access to the control interface specification, which requires: (a) Cellanome technical disclosure under NDA, and (b) either Cellanome authoring or approving a SiLA Feature Definition for the R3200 that SIFT can target from LabOP's specialization layer.

The SiLA 2 standard (Ulrich et al. *SLAS Technology* 2022, doi:10.1177/24726303221085635) provides the framework for device Feature Definitions, and the SiLA Consortium includes instrument vendors in negotiation for Feature Definition development. However, no Cellanome SiLA registration or Feature Definition is listed in the SiLA public registry as of 2026-06-14.

**Encodability verdict -- Cellanome R3200:**

| Layer | Status | Work required |
|---|---|---|
| Intent | Possible now | None |
| Protocol (CCE loading) | Possible with work | New `LoadCellCage` primitive; ~3 person-weeks; requires Cellanome technical disclosure |
| Protocol (time-lapse imaging) | Possible with work | New `AcquireTimeLapseImage` primitive; ~3 person-weeks |
| Protocol (CCE reagent delivery) | Possible with work | `CCEDelivery` sub-type of Transfer; ~2 person-weeks |
| Protocol (RNA capture/library prep) | Possible with work | Extend existing library-prep primitives; ~3 person-weeks |
| Calibration | Unclear / risk | No published standard; must be defined with Cellanome; timeline dependent on Cellanome cooperation |
| Hardware (SiLA specializer) | Unclear / risk | R3200 SiLA Feature Definition does not exist publicly; requires Cellanome technical exchange; highest-risk item; Phase I dependency |

**Overall Cellanome verdict: intent layer encodable now; protocol layer possible with substantial Phase I work (approximately 11 person-weeks of LabOP primitive development); hardware layer is the critical dependency and requires Cellanome to disclose or co-develop a SiLA Feature Definition. This is the single highest-risk TA3-to-TA4 interface item.**

**Risk:** High at hardware layer. Medium at protocol layer (structurally tractable but requires Cellanome technical knowledge transfer). The NDA between Cytognosis and Cellanome (currently in legal review per project-cellanome-nda-igor.md) is the prerequisite gate for this technical exchange.

---

### 2.3 Illumina BioInsight (Billion Cell Atlas; perturbation-scale scRNA-seq)

**Platform summary:** Illumina's TA4 contribution is perturbation-scale single-cell and bulk RNA sequencing on NovaSeq X / NovaSeq X Plus instruments, processed through the DRAGEN hardware-accelerated pipeline and hosted on Illumina Connected Analytics. The Billion Cell Atlas (announced January 13, 2026) provides reference neurological cell-line perturbation data as an in-kind resource. Library preparation follows Illumina Single Cell 3' RNA Prep (or equivalent 10X Genomics library prep). Demultiplexing uses DRAGEN BaseSpace with SampleSheet.csv format.

**Layer-by-layer encodability assessment:**

*Intent layer:* LabOP can encode the perturbation-scale scRNA-seq experimental intent using existing Protocol primitives: cell line, perturbation target, readout modality (scRNA-seq), timepoint, library prep kit, and sequencing depth. No new constructs required.

*Protocol layer:* Single-cell library preparation (cell dissociation, barcoding, cDNA amplification, library indexing) is a multi-step wet-lab procedure that partially overlaps existing LabOP primitives (Transfer, Incubate, PCR) but lacks dedicated single-cell library preparation primitives for the GEM encapsulation (10X Chromium-style droplet step) and barcode ligation. New primitives needed:

- `DropletEncapsulation` for the GEM generation step (compatible with 10X Chromium and Illumina's equivalent).
- `LibraryIndexing` for the combinatorial indexing or sample-tagging step.

These are targeted additions (approximately 3-4 person-weeks) that would serve multiple scRNA-seq platforms and would be valuable LabOP community contributions.

*Calibration layer:* Illumina's sequencing platforms have well-established calibration references: PhiX Control v3 is the canonical sequencing run QC reference, and the GIAB NA12878 reference genome provides alignment and variant-calling QC benchmarks. ERCC RNA spike-ins calibrate library complexity and RNA quantification. All of these are open and publishable as calibration artifact definitions in the Phase I TA3 calibration layer. This is the best-documented calibration baseline of the four candidates.

*Hardware layer:* Illumina sequencing runs are controlled through SampleSheet.csv files (a structured text format describing sample identifiers, lane assignments, index sequences, and DRAGEN pipeline parameters). This is not a SiLA interface; it is a file-based configuration format. LabOP can specialize to a SampleSheet.csv generator as a text-output specializer -- architecturally simpler than SiLA Feature calls, achievable with a lightweight specializer extension (approximately 2 person-weeks). Illumina Connected Analytics and DRAGEN configuration files add a second output target (JSON/YAML pipeline config) that also requires a specializer but is similarly tractable.

**Encodability verdict -- Illumina BioInsight:**

| Layer | Status | Work required |
|---|---|---|
| Intent | Possible now | None |
| Protocol (standard liquid handling) | Possible now | Existing Transfer/Incubate/PCR primitives cover cell culture and PCR steps |
| Protocol (GEM encapsulation) | Possible with work | New `DropletEncapsulation` primitive; ~2 person-weeks |
| Protocol (library indexing) | Possible with work | New `LibraryIndexing` primitive; ~2 person-weeks |
| Calibration | Possible now | PhiX, ERCC, GIAB references are open and directly usable; zero new development |
| Hardware (SampleSheet specializer) | Possible with work | Text-output specializer for SampleSheet.csv and DRAGEN config; ~2 person-weeks; no proprietary API dependency |

**Overall Illumina verdict: largely possible with modest work; approximately 6 person-weeks of Phase I LabOP extension; no proprietary API dependencies; best-documented calibration baseline of the four candidates.**

**Risk:** Low. Illumina's file-based interface is open and well-documented. The new LabOP primitives are modular additions applicable to any droplet-based scRNA-seq platform.

---

### 2.4 Panome Bio (untargeted metabolomics, lipidomics, phosphoproteomics)

**Platform summary:** Panome Bio is a CLIA-certified multi-omics CRO offering untargeted LC/MS-based metabolomics, lipidomics, and phosphoproteomics, targeted proteomics, and integrated multi-omic bioinformatics. Panome operates as a service provider: clients submit samples, Panome performs the analysis, and results are returned in report format or as feature matrices. Panome's instrument control software, sample intake API, and LIMS are proprietary and not publicly documented (panomebio.com, accessed 2026-06-14).

**Layer-by-layer encodability assessment:**

*Intent layer:* LabOP can encode the multi-omics experimental intent: sample type, analyte classes (metabolites, lipids, phosphopeptides), chromatography mode, detection method, and analysis pipeline. No new LabOP constructs required at this layer.

*Protocol layer:* Metabolomics sample preparation (extraction, protein precipitation, derivatization, reconstitution) uses existing LabOP primitives (Transfer, Incubate, Centrifuge -- though Centrifuge is not currently in the LabOP primitive library). LC/MS acquisition itself is not represented in any current LabOP primitive. New primitives needed:

- `Centrifuge` action for protein precipitation and cell pellet steps.
- `LCMSAcquisition` for instrument-triggered data acquisition with specified chromatography gradient, ionization mode, and scan parameters.

Neither of these is architecturally novel, but `LCMSAcquisition` requires knowledge of the specific instrument control interface (which varies across Thermo Fisher, Waters, Agilent, and Sciex platforms). Without knowing which specific instrument platforms Panome uses, the specializer cannot be developed.

*Calibration layer:* NIST SRM 1950 (Metabolites in Frozen Human Plasma) is the canonical metabolomics calibration reference material. LIPID MAPS standards cover lipidomics QC. Both are open and can be defined as calibration artifacts without Panome-specific disclosure. However, Panome's bioinformatics pipeline (proprietary database, retention-time alignment parameters, compound identification thresholds) introduces calibration parameters that are specific to Panome's internal SOP and are not publicly accessible.

*Hardware layer:* Panome Bio does not publish a public API, SiLA Feature Definition, or automated sample intake interface. As a service CRO, their intake model is email/portal-based sample submission, not machine-to-machine protocol delivery. Developing a LabOP specializer for Panome requires either: (a) Panome disclosing their sample tracking and instrument control API under NDA, or (b) accepting that TA3 protocol delivery to Panome will remain semi-manual (human-readable Markdown specialization + operator-driven LIMS entry) for the duration of Phase I and into Phase II.

**Encodability verdict -- Panome Bio:**

| Layer | Status | Work required |
|---|---|---|
| Intent | Possible now | None |
| Protocol (sample preparation) | Possible with work | New `Centrifuge` primitive (~1 person-week); existing Transfer/Incubate cover extraction steps |
| Protocol (LC/MS acquisition) | Unclear | `LCMSAcquisition` primitive requires instrument model knowledge; Panome instrument platform undisclosed |
| Calibration (open references) | Possible now | NIST SRM 1950 and LIPID MAPS standards directly usable |
| Calibration (Panome pipeline parameters) | Unclear | Proprietary bioinformatics pipeline parameters not publicly accessible |
| Hardware (instrument specializer) | Unclear / risk | No public API; service-CRO model incompatible with machine-to-machine protocol delivery; human-readable Markdown specialization is the only currently feasible path |

**Overall Panome verdict: intent and calibration (open references) possible now; sample preparation protocol possible with modest work; LC/MS acquisition protocol and hardware layer are unclear and dependent on Panome disclosing their instrument platform and intake API. The CRO service model is structurally incompatible with fully automated TA3-to-TA4 protocol delivery, making Panome unsuitable as a primary Phase I TA4 laboratory from a TA3 interface perspective. Appropriate as a Phase II optional extension with a manual-specialist handoff model explicitly scoped and documented.**

**Risk:** High at hardware and LC/MS acquisition layers. The CRO service model is the fundamental constraint, not a technical gap that can be bridged with primitive development alone.

---

## 3. Consolidated LabOP Encodability Matrix

The following matrix summarizes encodability status across the four-layer stack for all four candidates.

### Legend
- **Now:** existing LabOP primitives and specializers are sufficient; no new development required.
- **Work:** new LabOP primitive(s) or specializer required; architecturally tractable; development effort estimated in person-weeks.
- **Unclear:** feasibility depends on information not currently available (undisclosed API, proprietary interface, no precedent); risk to Phase I milestone.

### Matrix

| Layer | Carpenter / Broad | Cellanome R3200 | Illumina BioInsight | Panome Bio |
|---|---|---|---|---|
| **Intent** | Now | Now | Now | Now |
| **Protocol: standard liquid handling** | Now | Now (Transfer applies to reagent delivery) | Now | Work (Centrifuge primitive missing) |
| **Protocol: modality-specific steps** | Work (CyclicImagingStep for ISS; ~2 pw) | Work (LoadCellCage, AcquireTimeLapseImage, CCEDelivery, RNA capture; ~11 pw total) | Work (DropletEncapsulation, LibraryIndexing; ~4 pw) | Unclear (LCMSAcquisition; instrument platform undisclosed) |
| **Calibration: open references** | Now (JUMP-CP, LUDOX) | Work (no published R3200 calibration standard; must define with Cellanome) | Now (PhiX, ERCC, GIAB) | Now (NIST SRM 1950, LIPID MAPS) |
| **Calibration: IV&V artifact definition** | Work (fluorescence bead calibration primitive; ~1 pw) | Unclear (CCE loading efficiency and AI morphotyping concordance undefined; Cellanome cooperation required) | Now (PhiX protocol is directly IV&V-usable) | Unclear (Panome pipeline parameters proprietary) |
| **Hardware: specializer** | Work (CellProfiler SoftwareAction; ~1 pw; OT2 specializer exists) | Unclear / Risk (R3200 SiLA Feature Definition does not exist publicly; highest-risk item) | Work (SampleSheet.csv text-output specializer; ~2 pw) | Unclear / Risk (No public API; CRO service model; human-readable Markdown is only feasible path) |

**pw = person-weeks of Phase I engineering effort estimated.**

### Summary verdicts by candidate

| Candidate | Overall verdict | Primary risk | Phase I readiness |
|---|---|---|---|
| Carpenter / Broad | Strong: mostly possible now; 4 pw to full encodability | Low | Ready; walking skeleton achievable in Phase I Month 3 |
| Cellanome R3200 | Conditional: possible with work; ~11 pw plus hardware-layer resolution | High (R3200 SiLA Feature Definition) | Conditional; hardware-layer resolution requires NDA and technical exchange in Phase I Month 1-3 |
| Illumina BioInsight | Good: possible with modest work; 6 pw; no proprietary API | Low | Ready; walking skeleton achievable in Phase I Month 4-6 |
| Panome Bio | Partial: intent and open calibration possible now; LC/MS and hardware layer unclear | High (CRO service model; undisclosed API) | Not suitable for Phase I core; Phase II optional with manual specialist handoff |

---

## 4. Phase I Work Required: Primitives, SiLA Feature Definitions, and Calibration Artifacts

### 4.1 New LabOP primitives

The following new LabOP primitives are required to achieve full encodability for the Phase I anchor pair (Carpenter and Cellanome) and the Illumina extension. Each primitive should be authored in Phase I as a LabOP Python library contribution and submitted to the Bioprotocols Working Group as a proposal for inclusion in the official primitive library.

| Primitive | Needed for | Estimated effort | Priority |
|---|---|---|---|
| `CyclicImagingStep` | Carpenter optical pooled CRISPR ISS imaging cycles | 2 pw | P1 |
| `SoftwareAction` | Carpenter CellProfiler pipeline invocation; general-purpose software pipeline step | 1 pw | P1 |
| `LoadCellCage` | Cellanome R3200 CCE loading | 3 pw | P1 |
| `AcquireTimeLapseImage` | Cellanome R3200 longitudinal live-cell imaging | 3 pw | P1 |
| `CCEDelivery` | Cellanome R3200 programmable reagent delivery to enclosed cells | 2 pw | P1 |
| `FluorescenceCalibration` | Imaging channel calibration (Carpenter and Cellanome) | 1 pw | P1 |
| `DropletEncapsulation` | Illumina (and 10X-compatible) single-cell GEM generation | 2 pw | P2 |
| `LibraryIndexing` | Illumina single-cell library indexing | 2 pw | P2 |
| `Centrifuge` | Panome Bio sample preparation (Phase II) | 1 pw | P3 |
| `LCMSAcquisition` | Panome Bio LC/MS acquisition (Phase II, if API disclosed) | 3 pw | P3 |

**Total Phase I primitive development (P1 + P2):** approximately 16 person-weeks. Assignable to SIFT (LabOP co-developers) as the TA3 lead; Cellanome-specific primitives require technical input from Cellanome under NDA.

### 4.2 SiLA Feature Definition: Cellanome R3200

The Cellanome R3200 SiLA Feature Definition is the highest-priority single deliverable in the Phase I TA3-to-TA4 interface. Without it, LabOP cannot specialize to the R3200 hardware layer, and the Phase I walking-skeleton milestone for the Cellanome TA4 lane cannot be achieved.

A SiLA Feature Definition (SiLA FDL YAML) for the R3200 must describe at minimum:

- `LoadCellCage`: parameters specifying cell suspension volume, concentration, coating substrate, and target CCE well addresses.
- `StartImagingSession`: parameters for channels, frame interval, total duration, environmental conditions (temperature, CO2, humidity), and objective magnification.
- `DeliverReagent`: parameters for reagent identity, volume per CCE, delivery timing, and delivery confirmation.
- `EndSessionAndCapture`: trigger for RNA capture from CCEs, specifying capture buffer, incubation time, and library preparation initiation.
- `ExportData`: parameters for cloud export destination, file format, and encryption.

This Feature Definition can be co-authored by SIFT (SiLA expertise) and Cellanome (R3200 control interface knowledge) and submitted to the SiLA Consortium as a new Feature Definition for imaging/multi-modal integrated platforms. This submission would satisfy the Appendix A Objective TA3-2 requirement to engage with equipment manufacturers.

**Prerequisite:** Cellanome NDA finalized (currently pending Duane Valz review). Technical disclosure session with Cellanome engineering team scheduled no later than Phase I Month 2. Feature Definition draft completed by Phase I Month 6.

### 4.3 Illumina SampleSheet specializer

The Illumina SampleSheet.csv specializer is a text-output specializer (not a SiLA interface). Implementation requires:

- A LabOP specializer class that traverses the executed LabOP protocol and generates a SampleSheet.csv from the LibraryIndexing and protocol metadata.
- A DRAGEN pipeline configuration generator (JSON format) from the sequencing run parameters encoded in the protocol.

This is achievable in approximately 2 person-weeks and requires no Illumina API access -- the SampleSheet format is publicly documented. The DRAGEN configuration format is publicly available in Illumina's documentation.

### 4.4 Capability manifest schema

Defined in Section 1.3 above. Phase I deliverable: LinkML schema, validated against two laboratory manifests (Carpenter and Cellanome). The schema must be parseable by SIFT's TA3 planning-and-scheduling layer for laboratory selection. Estimated effort: 3 person-weeks (schema definition, validation, integration with scheduling layer).

### 4.5 Calibration artifact definitions

Phase I calibration artifact definitions required for IV&V alignment:

1. **Carpenter morphological calibration artifact:** JUMP-CP standard cell plate (U2OS + DMSO control wells + CRISPR perturbation controls) plus CellProfiler pipeline version and parameter hash. Definition: 2 person-weeks; datasets available from JUMP-CP open repository.

2. **Cellanome R3200 calibration artifact:** CCE loading efficiency reference; fluorescent bead calibration for each imaging channel; ERCC spike-in reference for RNA capture efficiency. Definition: 3 person-weeks; physical reference materials must be sourced and sent to Cellanome for co-validation. Requires Cellanome cooperation and NDA coverage.

3. **Illumina sequencing calibration artifact:** PhiX Control v3 run on NovaSeq X at standard parameters; ERCC RNA spike-in in library; minimum read quality (Q30) and cluster density specifications. Definition: 1 person-week; all references are open and well-documented.

4. **Panome Bio calibration artifact (Phase II):** NIST SRM 1950 metabolite panel; LIPID MAPS reference standards panel. Definition: 1 person-week for open references; Panome pipeline calibration deferred to NDA-gated Phase II scoping.

---

## 5. Alignment to TA3 and TA4 ISO Objectives and Phases

### 5.1 TA3 objectives (Appendix A, Section 4.1.3)

**Objective TA3-1 (Layered Protocol Architecture):** The per-candidate encodability analysis maps directly to this objective. Achieving full encodability for Carpenter and Cellanome by Phase I Month 12 satisfies "same protocol executed at two TA4 laboratories with comparable outcomes across at least one experiment." The primitive development and SiLA Feature Definition work constitutes the protocol schema definition required by Table 1 (Phase I, TA3).

**Objective TA3-2 (Standards Development and Interoperability):** The R3200 SiLA Feature Definition submission to the SiLA Consortium satisfies the equipment-manufacturer engagement requirement. The new LabOP primitives submitted to the Bioprotocols Working Group satisfy the external-standards-body engagement requirement. The capability manifest LinkML schema is a novel open-standards contribution with adoption potential beyond IGoR.

### 5.2 TA4 objectives (Appendix A, Section 4.1.4)

**Objective TA4-1 (Validated Reproducible Experimentation):** IV&V artifact definitions for Carpenter and Cellanome, executed at both laboratories, satisfy the "at least one cell line and instrument validated on IV&V test artifacts at each of the team's two laboratories" Phase I milestone (Table 1, TA4, Phase I). The 80% intra-team concordance threshold is evaluated on morphological and transcriptomic features from the same 22q11.2 isogenic variant lines run at both laboratories.

**Objective TA4-2 (Marketplace Operations):** The capability manifest schema and the two-way protocol delivery / data return cycle constitute the "two-way communication of capabilities established" Phase I milestone. Phase II requires the marketplace interface to be operational for experiment request and result return (Table 1, TA4, Phase II); the capability manifest and protocol specialization infrastructure developed in Phase I enables this directly.

### 5.3 Phase alignment summary

| Phase | TA3-to-TA4 interface deliverable | Critical dependencies |
|---|---|---|
| Phase I (Months 1-3) | NDA finalized; Cellanome technical disclosure initiated; R3200 SiLA Feature Definition scoped | Cellanome NDA completion; Duane Valz review |
| Phase I (Months 3-6) | R3200 SiLA Feature Definition v0.1; LoadCellCage + AcquireTimeLapseImage primitives drafted; Carpenter primitives complete; capability manifest schema v0.1 | SIFT engineering capacity; Cellanome cooperation |
| Phase I (Months 6-12) | R3200 SiLA Feature Definition v1.0 submitted to SiLA Consortium; full Carpenter and Cellanome LabOP encodability; IV&V calibration artifact definitions finalized | SiLA Consortium review timeline; IV&V partner |
| Phase I (Months 12-18) | Walking skeleton demonstrated: Carpenter and Cellanome executing same protocol from same LabOP canonical source; 80% intra-team concordance demonstrated on at least one 22q11.2 variant line | LabOP specializer operational; both labs calibrated |
| Phase II (Months 19-36) | Illumina SampleSheet specializer; DropletEncapsulation + LibraryIndexing primitives; RFC process operational; cross-team protocol execution at Carpenter, Cellanome, Illumina | Illumina scoping call (scheduled 2026-06-16) |
| Phase III (Months 37-60) | Panome Bio Phase II deliverables validated if engaged; marketplace fully operational; connect-a-thon participation; all capability manifests publicly queryable | Panome API disclosure (if engaged) |

---

## 6. Gaps, Risks, and Recommended Mitigations

### 6.1 Risk register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Cellanome declines to disclose R3200 control interface | Medium | Critical (blocks Cellanome hardware-layer encodability; Phase I milestone at risk) | Escalate to CEO-level; frame as IGoR program requirement; SiLA Feature Definition co-authorship gives Cellanome a standards-visibility benefit; fallback is human-readable Markdown specialization for Phase I with automated path in Phase II |
| R3200 SiLA Feature Definition development takes longer than Phase I | Medium | High (delays walking skeleton) | Allocate 2x engineering buffer; SIFT SiLA expertise reduces timeline; fallback: human-readable specializer for Phase I bake-off, automated in Phase II |
| Panome Bio API remains undisclosed through Phase II | High | Low-Medium (Panome is optional Phase II extension; not Phase I core) | Accept manual specialist handoff for Panome lane; document explicitly in proposal; do not include Panome in Phase I concordance metric |
| JUMP-CP calibration reference plates unavailable at Cellanome | Low | Medium | Carpenter provides reference plates from their existing JUMP-CP inventory; Cellanome ships plates to their facility under standard MTA |
| LabOP tooling instability disrupts specializer development | Low | Medium | Budget Phase I tooling hardening per SIFT SAFT analysis; SIFT is the LabOP maintainer and can triage instability rapidly |
| Sub-performer overlap rule: Carpenter or Illumina overlap with another IGoR team | Medium | Medium (ARPA-H may fund overlapping work once or require election) | Identify backup TA4 morphological lab (academic imaging core at Purdue/IPAI); document in proposal; Illumina Atlas in-kind contribution is distinct from sequencing service and may not trigger overlap rule |

### 6.2 Best-fit TA3-to-TA4 composition

The analysis supports the following best-fit composition for the TA3-to-TA4 interface at each program phase:

**Phase I:** Carpenter (OT2 + CellProfiler; mostly encodable now) plus Cellanome R3200 (SiLA-path; highest engineering investment but highest scientific return for same-cell multimodal data). These two laboratories together satisfy the Phase I requirement for at least two TA4 laboratories, at least two modalities, and 80% intra-team concordance, provided the R3200 hardware-layer dependency is resolved in Phase I Months 1-6.

**Phase II:** Carpenter, Cellanome, and Illumina. Illumina's SampleSheet specializer and library-prep primitives are achievable in Phase I-to-II transition, enabling Illumina to join as the third laboratory for the Phase II cross-team experiment and the Billion Cell Atlas concordance check.

**Phase III:** Full marketplace with Carpenter, Cellanome, and Illumina as primary TA4 performers; Panome Bio as optional multi-omic extension if Phase I variant lines produce mechanistically informative metabolic or lipidomic signals.

---

## 7. References

**LabOP / PAML:**
- Bartley B et al. Building an Open Representation for Biological Protocols. *ACM Journal on Emerging Technologies in Computing Systems* 19(3), 2023. doi:10.1145/3604568.
- Bartley B et al. Building an Open Representation for Biological Protocols (preprint). bioRxiv 2022.07.05.498808. doi:10.1101/2022.07.05.498808.
- LabOP GitHub: https://github.com/bioprotocols/labop (accessed 2026-06-14).

**SiLA 2:**
- Ulrich D et al. SiLA 2: The Next Generation Lab Automation Standard. *SLAS Technology* 2022. PubMed: 35639108. doi:10.1177/24726303221085635.
- SiLA documentation: https://sila2.gitlab.io/sila_base/ (accessed 2026-06-14).
- SiLA Feature Definition Registry: https://github.com/SiLA2/feature-definitions (accessed 2026-06-14; Cellanome R3200 not listed).

**Calibration references:**
- JUMP-CP / Cell Painting Gallery: Chandrasekaran SN et al. Jump cell painting dataset: morphological impact of 136,000 chemical and genetic perturbations. *bioRxiv* 2023.03.23.534023. Published as Chandrasekaran et al. *Nat Methods* 2023. **Verify DOI before submission.**
- ERCC RNA spike-ins: Jiang L et al. Synthetic spike-in standards for RNA-seq experiments. *Genome Res* 2011. doi:10.1101/gr.121095.111.
- GIAB benchmarks: Zook JM et al. An open resource for accurately benchmarking small variant and reference calls. *Nat Biotechnol* 2019. doi:10.1038/s41587-019-0074-6.
- NIST SRM 1950: NIST Certificate of Analysis, Standard Reference Material 1950, Metabolites in Frozen Human Plasma. https://www.nist.gov/srm (accessed 2026-06-14).
- PhiX Control v3: Illumina product documentation. https://www.illumina.com (accessed 2026-06-14).

**TA4 candidate primary references:**
- Tegtmeyer M et al. 22q11.2 deletion morphological signatures (NeuroPainting). *Nat Commun* 2025. DOI: 10.1038/s41467-025-61547-x. **Verify authorship includes Carpenter lab.**
- Illumina Billion Cell Atlas press release. January 13, 2026. https://investor.illumina.com (accessed 2026-06-14).
- Panome Bio phosphoproteomics launch. PRNewswire. April 2025. **Verify exact date.**
- Cellanome website: https://www.cellanome.com (accessed 2026-06-14). No public API, SiLA documentation, or protocol standardization claims found.

**IGoR program:**
- ARPA-H. IGoR Program and Technical Description. Appendix A, ARPA-H-SOL-26-155. 2026.

**LinkML:**
- LinkML specification: https://linkml.io (NCATS/open community; accessed 2026-06-14).

**SBOL3:**
- McLaughlin JA et al. Synthetic biology open language (SBOL) version 3. *Frontiers in Bioengineering and Biotechnology* 2020. doi:10.3389/fbioe.2020.00486.

**SIFT TA3 references:**
- Bryce D et al. Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis. *ACS Synthetic Biology* 2022. doi:10.1021/acssynbio.1c00305.
- Eslami M et al. AutoGater. *Scientific Reports* 2024.

---

*Document version: 2026-06-14. Internal only. Paired with `IFACE_TA3_TA4__brief.md`.*
