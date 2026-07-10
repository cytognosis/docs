# TA3 Interoperable Experimental Procedures: Protocol Standards Deep Dive (Full)

**Document type:** Internal deep dive, IGoR proposal series
**Compiled:** 2026-06-14
**Scope:** TA3 protocol-interoperability layer, LabOP architecture, standards landscape, Cellanome relevance, mapping to our execution stack and to the IGoR TA3 objectives

> [!NOTE]
> **Internal only.** This document informs proposal drafting. It is not for distribution to partners or for inclusion verbatim in a submission. Cross-references to restricted sections (31, 32, 41) are conceptual only; those sections must not appear in any external build.

---

## Abstract / BLUF

TA3 in IGoR requires a layered, open, interoperable protocol stack that can carry heterogeneous experimental procedures across multiple laboratories, enforce parameter governance, and feed machine-readable execution records back to TA1. No single existing standard covers all four abstraction layers (Intent, Protocol, Calibration, Hardware) defined by the IGoR solicitation. The Laboratory Open Protocol Language (LabOP) is the most mature open candidate for the upper two layers and provides the architectural backbone SIFT will lead. SiLA 2 covers the hardware-interface layer; Autoprotocol and OpenTrons serve as hardware-specialization targets that LabOP compiles to. Cellanome contributes no TA3 protocol-representation capability and should be positioned exclusively as a TA4 laboratory provider. The main TA3 gaps are: (1) no existing open standard integrates all four layers end-to-end; (2) LabOP was developed and validated in synthetic-biology contexts, requiring explicit generalization work for mammalian iPSC, live-cell imaging, and scRNA-seq modalities; and (3) the RFC parameter-governance process has no precedent in any existing protocol standard, making it a genuine IGoR-specific contribution. These gaps are solvable and their solutions constitute defensible IGoR deliverables.

---

## 1. The TA3 Problem and the Four-Layer Stack

### 1.1 What TA3 must do

The IGoR Program and Technical Description (Appendix A, ARPA-H-SOL-26-155) identifies the reproducibility crisis as a primary motivator. A central finding is that inter-laboratory protocol variation is a leading source of non-reproducibility, and that reducing this variation requires **separating scientifically meaningful parameters from arbitrary local laboratory preference**. TA3 therefore must:

1. Represent experimental intent at a level of abstraction that is **independent of specific instruments or local SOPs**.
2. Provide machine-readable protocol specifications that can be compiled to heterogeneous execution backends.
3. Standardize calibration and quality-control parameters with **versioned, auditable governance**, the Request-for-Comments (RFC) process.
4. Interface with the hardware layer via **instrument-agnostic communication standards**.
5. Return **execution records with provenance** that are directly consumable by TA1 model updates.

### 1.2 The four-layer stack

Appendix A defines four abstraction layers. Our TA3 architecture maps precisely onto them:

| Layer | What it encodes | Existing standard(s) | Our implementation |
|---|---|---|---|
| **Intent** | Declarative scientific question, quality requirements, success criteria | LabOP intent primitives | LabOP protocol objects (SBOL3 RDF) |
| **Protocol** | Standard processes, control flow, error handling, versioned parameter sets | LabOP, Aquarium | LabOP + LinkML schemas for metadata |
| **Calibration** | Parameters and uncertainty standardized across devices; IV&V artifacts | Partial: SED-ML/KiSAO for computational; no lab-hardware equivalent | Our RFC process + IV&V calibration artifacts |
| **Hardware** | Machine-specific settings, isolated behind common interfaces | SiLA 2, Autoprotocol, OpenTrons API | LabOP specialization to Autoprotocol / OpenTrons OT2 / SiLA-based devices |

The central contribution of our TA3 is that **no existing standard spans all four layers**. We do not invent a new protocol language; instead, we adopt LabOP as the upper-layer backbone and wire it to the hardware-layer standards via LabOP's existing specialization mechanism.

### 1.3 The RFC parameter-governance mechanism

The IGoR solicitation explicitly requires that parameter changes be made through a documented, evidence-based process. Our implementation is an RFC-governed workflow in which:

- Parameters with weak scientific justification are **locked by default**.
- Proposed changes must be submitted as a versioned RFC with supporting evidence.
- Accepted RFCs update the versioned parameter set and produce a durable audit entry.
- The RFC log constitutes the calibration traceability record required for IV&V review.

This mechanism has no equivalent in any existing protocol standard (including LabOP itself, which does not define a parameter-governance process). It is therefore a novel, specifically IGoR-motivated contribution.

---

## 2. LabOP Deep Dive

### 2.1 Origins and naming history

LabOP originated as the **Protocol Activity Markup Language (PAML)**, described in Bartley et al. (2022; bioRxiv 2022.07.05.498808). The ACM JETC journal publication (Bartley et al. 2023; doi:10.1145/3604568) renamed the language to LabOP and extended its scope and tooling. The name change matters for proposal terminology: "PAML" appears in older DARPA/IARPA synthetic-biology program literature and in early SIFT presentations; "LabOP" is the current, correct name and should be used uniformly.

### 2.2 Architectural foundations

LabOP is built on three pre-existing formalisms, each of which contributes a distinct capability:

**UML Activity Model (control and data flow).** The core execution semantics of LabOP are rooted in the **Unified Modeling Language (UML) activity diagram** formalism. An activity diagram represents a computation as a directed graph of action nodes, control nodes (decision, fork, join, merge), and object/data nodes connected by control and object flows. LabOP maps laboratory protocols onto this formalism: protocol steps are action nodes; the transfer of labware or data between steps is captured in object flow; branching on conditions (e.g., "if OD > threshold") is a decision node. This is not an ad hoc design choice, UML activity semantics provide a well-defined, tool-supported execution model that enables formal simulation, verification, and automatic compilation to hardware-specific execution.

**SBOL3 RDF (identity, reuse, and semantic grounding).** The **Synthetic Biology Open Language version 3** (SBOL3) provides a W3C-compliant RDF representation for biological entities and their design relationships. In LabOP, SBOL3 serves two functions: (a) it provides the **persistent URI-based identity system** for protocol objects (primitives, activities, samples, measurements) so that protocols and their components can be unambiguously referenced and reused across laboratories; (b) it grounds biological entities referenced by a protocol (cell lines, reagents, labware) in the SBOL3 identity namespace, enabling interoperability with biological design databases. Every LabOP protocol is serialized as an RDF/OWL document conforming to the SBOL3 specification.

**PROV Ontology (execution records and provenance).** The **W3C PROV Ontology** (PROV-O) is the standard model for representing computational provenance. LabOP uses PROV to record **execution traces**: each protocol run produces a PROV-conformant record linking every action to its inputs, outputs, parameter values, timestamps, and instrument identities. This is precisely the metadata layer TA3 must produce, an execution record that TA1 can consume alongside the experimental data to perform model updates with full provenance.

### 2.3 Protocol primitives

A LabOP protocol is constructed from **primitives**, atomic, reusable building blocks defined in a typed primitive library. Each primitive encodes a single, unambiguous laboratory action and carries:

- A typed signature (input labware types, output labware types, required parameters).
- Semantic grounding via SBOL3 URIs.
- Default parameter values and parameter constraints.

The current LabOP primitive libraries are organized by domain:

| Library | Representative primitives |
|---|---|
| `sample_arrays` | `EmptyContainer`, `PlateCoordinates`, `TransferByParticipant` |
| `liquid_handling` | `Transfer`, `Provision`, `MeasureAbsorbance`, `MeasureFluorescence` |
| `cell_culture` | `Culture`, `Dilute`, `Incubate` |
| `pcr` | `PCR`, `GelElectrophoresis` |
| `flow_cytometry` | `FlowCytometry` |

Primitives compose into activities via UML activity semantics. A protocol author instantiates primitives as activity nodes, connects them with control and object flows, and specifies parameter values or leaves them as open variables for specialization.

### 2.4 Specialization: one protocol to many backends

The most strategically important property of LabOP for IGoR TA3 is **protocol specialization**: a single abstract LabOP protocol can be compiled to multiple hardware-specific execution backends without modifying the canonical protocol representation. The `labop` Python library implements specializers for:

- **Autoprotocol** (Strateos/Transcriptic): JSON-based cloud-lab execution format.
- **OpenTrons OT2**: Python protocol scripts for the OpenTrons liquid-handling robot.
- **SiLA-based automation**: via SiLA-compliant feature descriptions.
- **Echo (Labcyte/Beckman Coulter)**: acoustic dispensing.
- **Human-readable Markdown**: formatted step-by-step paper-protocol output.

This means that a TA3 protocol defined once in LabOP can execute at Carpenter (OpenTrons or Cell Painting liquid handlers), Cellanome (SiLA-based automation within the R3200), and an external IV&V site, all from the same canonical representation. The canonical protocol is version-controlled; specializations are generated outputs, not the source of truth.

### 2.5 Tooling ecosystem

**`labop` (Python library).** The primary developer tool. Installed via `pip install pylabop`. A protocol is authored in Python by importing `labop`, `uml`, and `sbol3` modules, initializing an SBOL3 document, instantiating a `Protocol` object, adding `PrimitiveStep` nodes, and connecting them. Serialization to RDF (Turtle or N-Triples) produces the canonical protocol document. Execution in native UML activity semantics runs the protocol in a Python interpreter, checking type constraints and producing PROV execution records. Specializers are called on the executed protocol to produce backend-specific outputs.

**`laboped` (web editor, formerly PAMLED).** A low-code visual authoring tool hosted as a web application. Protocol authors create protocols as visual activity diagrams; the editor stores protocols in cloud storage and exports specializations on demand. The editor lowers the barrier for experimental scientists who are not Python programmers to define and share protocols.

### 2.6 Governance

LabOP is maintained by the **Bioprotocols Working Group**, an open community organization with an elected Chair and Finance Committee. Current Chair (term October 2024 to October 2025): **Tim Fallon, UCSD**, the other leading LabOP developer alongside Dan Bryce and Bryan Bartley (now at Raytheon BBN Technologies). The working group holds biannual workshops and weekly development calls; governance decisions require a two-thirds majority vote of the mailing-list membership. The standard is published under permissive, free, and open licenses. Standards changes go through a proposal-and-vote process.

For IGoR, this governance structure is directly relevant: the solicitation requires engagement with external standards bodies, and the Bioprotocols Working Group is the natural venue for that engagement. SIFT's Dan Bryce is a founding member and current Finance Committee member; this gives our consortium standing to propose TA3-motivated extensions to the standard through official channels.

### 2.7 Relationship to SBOL3 and the broader synthetic-biology standards stack

LabOP is deliberately embedded in the SBOL/COMBINE standards ecosystem rather than positioned as an independent, standalone standard. This has two consequences:

1. **Interoperability with biological design databases.** SynBioHub and other SBOL3-compliant repositories can store and retrieve LabOP protocols and execution records alongside biological part definitions. For IGoR, this means that iPSC lines, CRISPR constructs, and assay reagents referenced in a TA3 protocol can be unambiguously identified via their SBOL3 URIs.
2. **Dependency on SBOL3 tooling maturity.** The `sbol3` Python library is the required companion to `labop`, and its maturity level constrains the maturity of the LabOP toolchain. As of 2026, SBOL3 Python tooling is stable and actively maintained, but the ecosystem is smaller than alternatives like JSON Schema or OpenAPI.

---

## 3. Protocol and Lab-Automation Standards Landscape

### 3.1 Standards comparison matrix

| Standard | Layer(s) covered | Openness | Execution semantics | Provenance support | Cross-vendor? | Key limitation for TA3 |
|---|---|---|---|---|---|---|
| **LabOP** | Intent, Protocol, partial Calibration | Open (CC BY 4.0) | UML activity model, formal | PROV-O conformant | Yes (specialization) | Synthetic-biology origin; no RFC governance; mammalian workflow coverage immature |
| **SiLA 2** | Hardware (device control) | Open (SiLA Consortium) | gRPC + Protocol Buffers, runtime | None | Yes (vendor-neutral) | Hardware-only; no semantic protocol layer above device control |
| **Autoprotocol** | Protocol, Hardware (Strateos/Transcriptic) | Partial open (spec public; platform proprietary) | JSON-based; Strateos execution engine | None | No (Strateos-specific) | Vendor-locked to Strateos cloud lab |
| **Aquarium** | Protocol (Aquarium LIMS) | Open (MIT) | Ruby-based operation scripts | None | No (Aquarium LIMS-specific) | Tied to University of Washington Aquarium LIMS |
| **OpenTrons API** | Hardware (OT2 robot) | Open (Apache 2.0) | Python scripts; OT2 execution | None | No (OT2-specific) | Robot-specific; no semantic layer |
| **SED-ML** | Computational experiments | Open (COMBINE) | XML-based; links to simulators | Partial (OMEX/COMBINE) | Yes (simulator-dependent) | Computational only; no wet-lab coverage |
| **Opentrons Protocol Library** | Protocol templates | Open | Python; OT2-only | None | No | No abstraction above OT2 |
| **Emerald Cloud Lab (ECL) protocol language** | Protocol, Hardware (ECL platform) | Proprietary | ECL execution engine | Internal only | No | Proprietary; no open export |

### 3.2 Why LabOP is the best-fit open standard

Three properties distinguish LabOP from all alternatives for IGoR TA3:

**Separation of intent from implementation.** LabOP is the only open standard that explicitly models the intent layer as distinct from the protocol layer. Autoprotocol and OpenTrons operate at protocol-execution level; SiLA 2 operates at device-communication level. LabOP's abstract activity model allows a biologist to specify what must happen (transfer 10 µL of reagent X to plate Y, incubate at 37C for 24 h) independently of which robot executes it.

**Formal execution semantics with provenance.** The UML activity model gives LabOP formal, well-defined execution semantics that support verification and simulation prior to physical execution. PROV-O execution records are generated natively, meeting the TA3 requirement for machine-readable execution logs.

**Specialization to multiple backends.** No other open standard provides a principled compilation pathway from one abstract representation to multiple hardware-specific backends. This is the property that enables the same protocol to run at Carpenter (OT2-based), Cellanome (SiLA-based R3200), and a third IV&V site.

### 3.3 Key limitations and risks

**Synthetic-biology origin.** LabOP was designed and validated primarily for genetic-circuit assembly workflows (iGEM protocols, LUDOX calibration, absorbance plate-reader assays). Its primitive library does not currently cover: iPSC differentiation protocols; live-cell imaging time-series protocols; same-cell scRNA-seq library preparation (Perturb-LINK); or CRISPR pooled screening workflows. Extending LabOP to cover these modalities is both necessary and feasible, and it is a concrete, fundable TA3 deliverable.

**Tooling maturity.** The `labop` Python library is actively developed but has not reached a 1.0 stable release. The `laboped` web editor is in early development. For IGoR, this means Phase I must include tooling hardening and packaging for the specific modalities we use.

**Community size.** The Bioprotocols Working Group is a small community (dozens of active members). The standard's long-term sustainability depends on adoption by additional groups and on funding continuity. SIFT's IGoR engagement is an opportunity to grow this community.

**No built-in parameter governance.** LabOP has no RFC mechanism. Parameter locking and versioned governance are not part of the LabOP specification. These must be implemented as a TA3-specific overlay on top of LabOP.

### 3.4 SiLA 2 as the hardware interface

SiLA 2 (Standardization in Lab Automation, version 2; SiLA Consortium) is the open standard for device-level communication in laboratory automation. It uses gRPC over HTTP/2 with Protocol Buffers for serialization, and defines a standard interface description language (Feature Definitions, expressed as FDL YAML) that device manufacturers use to describe the commands their instruments support. SiLA 2 version 1.1 was released in 2022; the standard is maintained by the SiLA Consortium and has broad vendor adoption (Tecan, Hamilton, HPST, and others).

In our TA3 stack, SiLA 2 provides the **hardware layer**: LabOP protocols specialized for SiLA-based devices are translated into SiLA Feature calls at runtime. This is the integration path for Cellanome's R3200 (which uses SiLA-based automation internally) and for any SiLA-compliant liquid handler at Carpenter or a cross-team site.

SiLA 2 does not address protocol semantics, intent, or calibration governance; it provides only device-level command execution. This is the correct role for SiLA 2 in our stack: the semantic and governance work is all in the LabOP layers above it.

---

## 4. Cellanome and TA3: Relevance Assessment

### 4.1 What Cellanome does

Cellanome is a life-sciences instrument company that develops the **R3200 platform**: a fully integrated system combining proprietary CellCage microenvironments, time-lapse fluorescent live-cell imaging, pooled CRISPR perturbation delivery, and same-cell scRNA-seq transcriptomics (Perturb-LINK workflow). The platform is positioned for multimodal, dynamic single-cell biology across neurobiology, immunology, oncology, and aging. The company launched publicly in December 2025.

### 4.2 Cellanome's relationship to TA3

**Cellanome has no publicly described or documented role in protocol representation, protocol interoperability standards, or the LabOP ecosystem.** A review of Cellanome's website (cellanome.com, accessed 2026-06-14), publications, posters, and public presentations finds:

- No mention of LabOP, PAML, SiLA, Autoprotocol, or any comparable protocol standard.
- No API documentation, protocol-format specification, or interoperability SDK published as of this date.
- Internal SOP-based workflows are referenced as the basis for the Perturb-LINK workflow, but these are described in human-readable terms only.

**Verdict: Cellanome contributes zero TA3 protocol-representation capability.** Their contribution to our consortium is entirely at the TA4 layer: a high-value, specialized experimental platform generating multimodal single-cell data that TA3 protocols must target.

### 4.3 What Cellanome does contribute to TA3 (indirectly)

Cellanome's SOP-based Perturb-LINK workflow is a **seed dataset** for TA3 protocol development. In section 34 of the Research Master, we note that "Cellanome's documented SOP-based workflows seed the TA3 standard at program start." This means:

- Cellanome provides the reference human-readable protocols for the live-cell imaging / same-cell scRNA-seq modality.
- SIFT converts those SOPs into LabOP protocol representations as the first Phase I TA3 deliverable for that modality.
- Cellanome validates the LabOP-specialized execution against their own SOP-based baseline.

This is a TA4-to-TA3 knowledge-transfer process, not a TA3 contribution by Cellanome itself. The distinction matters for proposal framing: Cellanome should not be described as a TA3 performer.

---

## 5. Mapping LabOP to Our TA3 and to the Phenotypic-Triage Assays

### 5.1 Assays that TA3 must carry

Our Phase I/II TA4 execution covers four modality lanes, each requiring a distinct LabOP protocol representation:

| Modality | TA4 laboratory | Key workflow steps | LabOP challenge |
|---|---|---|---|
| Cell Painting morphological screening | Carpenter (Broad/IPAI) | CellProfiler plate prep, staining, imaging, feature extraction | Imaging protocol primitives; multi-step liquid handling; image-data provenance |
| Optical pooled CRISPR screening | Carpenter | Library lentiviral delivery, selection, in-situ sequencing | Multi-day protocol with conditional steps; cell-state gating |
| Live-cell imaging + same-cell scRNA-seq (Perturb-LINK) | Cellanome (R3200) | CellCage loading, time-lapse imaging, CRISPR delivery, library prep | SiLA-based hardware specialization; longitudinal imaging time-series; CellCage-specific consumables |
| High-throughput sequencing | Illumina | Perturb-seq library prep, sequencing run, demultiplexing | Sequencing run parameters; FASTQ provenance |

### 5.2 Layer-by-layer mapping

**Intent layer.** Each experiment design from TA2 arrives as a structured specification: cell type, perturbation target, timepoint(s), readout modality, and success criteria. LabOP's Protocol object encodes this as an activity with typed inputs and named outputs. The intent layer is deliberately modality-agnostic, a Perturb-seq experiment and a Cell Painting experiment differ at the Protocol layer (the specific primitives used) but share the same Intent-layer structure (perturbation to target X in cell type Y, readout Z at time T).

**Protocol layer.** The protocol layer encodes the modality-specific sequence of primitives: which liquid transfers, which incubations, which instrument activations, in what order, with what parameters. Phase I TA3 deliverable: LabOP protocol definitions for at least two modalities (Cell Painting and Perturb-LINK). Phase II adds optical pooled screening and Perturb-seq. Each protocol is version-controlled in a shared repository.

**Calibration layer.** The calibration layer is the layer with the most novel TA3 work. Our implementation:

- Defines calibration primitives (e.g., LUDOX absorbance calibration for plate readers; bead-based fluorescence calibration for imaging) as LabOP activities.
- Produces IV&V calibration artifacts: physical reference materials and associated measurement datasets that can be transferred to a new laboratory to verify instrument equivalence.
- Implements the RFC process as a versioned changelog layer on top of the calibration parameter set.

**Hardware layer.** LabOP's specialization mechanism compiles the abstract protocol to backend-specific execution:

- Carpenter: specialization to OpenTrons OT2 Python scripts and to CellProfiler pipeline definitions.
- Cellanome R3200: specialization to SiLA Feature calls (once the R3200 SiLA Feature Definition is documented; this is a Phase I dependency to resolve with Cellanome).
- Illumina: specialization to Illumina run-parameter files (SampleSheet.csv format; DRAGEN pipeline configuration).

### 5.3 The TA2-to-TA3 interface

TA2 outputs a structured experiment design. TA3 must translate that design into an executable LabOP protocol. The interface format (section 34, Research Master) specifies: cell type, perturbation target, timepoint(s), and readout modality, plus success criteria (the quality thresholds that determine whether the experiment is accepted into TA1). This structured handoff enables SIFT's planning-and-scheduling component to allocate the experiment to an available TA4 laboratory, verify resource availability, and generate the LabOP protocol in a single automated step.

The TA2-to-TA3 interface is one of the interfaces to be formalized at the Phase I Domain-Driven Design workshop. LabOP's typed primitive system provides the natural representation for experiment designs at this interface.

### 5.4 The TA3-to-TA4 interface

TA3 delivers to TA4: the LabOP-specialized protocol (e.g., an OT2 Python script), calibration artifacts, parameter values, and quality-control specifications. TA4 returns: raw data, QC metrics, and a PROV execution record. The execution record is linked to the canonical LabOP protocol via its SBOL3 URI, so the full chain from TA2 experiment design through TA3 protocol to TA4 execution to TA1 data ingestion is traceable.

---

## 6. Alignment to TA3 ISO Objectives and IGoR Program Phases

### 6.1 TA3 objectives (from Appendix A)

Appendix A states two TA3 objectives:

**Objective TA3-1:** Develop and implement a layered interoperable protocol stack that enables experimental procedures to be specified at a level of abstraction independent of specific instruments or local SOPs, then compiled to hardware-specific execution with full provenance tracking.

**Objective TA3-2:** Engage with external standards bodies and equipment manufacturers to ensure that the protocol standards developed within IGoR have adoption potential beyond the program.

### 6.2 Phase alignment

| Phase | IGoR TA3 milestone | Our TA3 deliverable | LabOP role |
|---|---|---|---|
| **Phase I** (18 mo) | Protocol schema and calibration artifacts defined; same protocol run at two team labs with comparable outcomes on >=1 experiment; >=2 modalities | LabOP primitive library for Cell Painting and Perturb-LINK; calibration artifact set; RFC process v1; SBOL3 protocol repository established | LabOP as backbone; initial specializations to OT2 and SiLA/R3200 |
| **Phase II** (18 mo) | RFC process operational with >=2 RFCs executed; protocols run at >=3 labs including >=1 cross-team; >=3 protocols; >=3 modalities | LabOP primitive library extended to Perturb-seq and optical pooled screening; cross-team protocol execution; >=2 RFCs with documented evidence | LabOP cross-team execution; specialization validated at independent sites |
| **Phase III** (24 mo) | Open data and metadata layer delivered; engagement with >=1 external standards body or manufacturer; protocols at >=5 labs; >=4 modalities; connect-a-thon | Bioprotocols Working Group RFC proposals for neuronal-assay primitives; LabOP published extensions; open data layer | LabOP extensions published as official Working Group proposals; connect-a-thon interoperability |

### 6.3 The bake-off and RFC process

The IGoR program includes TA3 bake-offs in Phases I and II, in which all funded teams compare protocol representations. Our participation strategy:

- Phase I bake-off: demonstrate LabOP canonical protocol executing identically at Carpenter and Cellanome via different specializations from the same source.
- Phase II bake-off: demonstrate RFC-governed parameter change, showing the versioned audit trail and comparable experimental outcomes before and after the RFC.
- Phase III connect-a-thon: demonstrate cross-team protocol execution using the LabOP open data layer.

---

## 7. Gaps, Risks, and Best-Fit Components

### 7.1 Gap analysis

| Gap | Severity | Resolution path |
|---|---|---|
| LabOP primitive library does not cover iPSC, live-cell imaging, or scRNA-seq workflows | High | Phase I deliverable: author and contribute new primitive libraries for these modalities; SIFT + Carpenter + Cellanome as knowledge sources |
| R3200 SiLA Feature Definition not publicly documented | High | Phase I dependency: NDA-gated technical exchange with Cellanome to document the R3200 SiLA interface; required for LabOP specialization |
| No RFC parameter-governance mechanism in any existing protocol standard | Medium | This gap is an opportunity: the RFC process is a novel TA3 contribution; implement as a lightweight Git-based version-controlled overlay on the LabOP parameter set |
| LabOP tooling not at 1.0 stable release | Medium | Budget Phase I engineering effort for `labop` library hardening; contribute upstream; SIFT is the natural maintainer |
| LabOP community is small; long-term sustainability unclear | Low-Medium | IGoR engagement grows the community; Bioprotocols Working Group governance provides institutional continuity |
| SiLA 2 Feature Definitions for imaging instruments (R3200, high-content imagers) lag liquid-handling vendors | Medium | Engage SiLA Consortium and Cellanome; draft R3200 Feature Definition as Phase I output |
| No cross-team protocol execution precedent in mammalian-disease context | Medium | First demonstrated at Phase II cross-team milestone; IV&V partner provides independent validation site |

### 7.2 Best-fit components summary

| Component | Best-fit role | Where it lives in the four-layer stack |
|---|---|---|
| LabOP | Canonical protocol representation, specialization engine, PROV execution records | Intent and Protocol layers |
| SiLA 2 | Hardware device communication | Hardware layer |
| Autoprotocol | Specialization target for Strateos/cloud-lab compatibility (optional Phase II extension) | Hardware layer |
| OpenTrons OT2 API | Specialization target for Carpenter liquid handling | Hardware layer |
| LinkML | Open schema definition for protocol metadata, QC parameters, data-return packages | Protocol and Calibration layers (metadata) |
| OMEX/COMBINE | Archiving of TA1 computational models with their experiment metadata | TA1/TA3 interface |
| PROV-O | Execution record provenance | Calibration layer (traceability) |
| RFC process (novel) | Parameter governance and change management | Calibration layer |
| Cell Painting Gallery / JUMP standards | Open image-data standards, morphological-profiling reference | TA3 data layer for Carpenter modality |

### 7.3 TA2-TA3 interface gaps

The TA2 experiment-design output format and the TA3 protocol-generation input format must be formally defined by end of Phase I. The current Research Master (section 34) states the logical content (cell type, perturbation target, timepoint, readout modality, success criteria) but does not specify the serialization format. **Recommendation:** define this interface as a LinkML schema; LabOP protocol generation is then a transformation from that schema to a LabOP Protocol object. This is the most tractable path given the tooling available.

### 7.4 TA3-TA4 interface gaps

TA4 laboratories must publish machine-readable capability manifests describing which modalities they can execute, which instruments are calibrated, and what their current availability is. No existing open format for laboratory capability manifests exists. **Recommendation:** define a lightweight LinkML schema for capability manifests as a Phase I deliverable; this is a small, achievable contribution that addresses a genuine gap and gives TA3 an additional open-standards deliverable.

---

## References

**LabOP / PAML:**
- Bartley B, Beal J, Rogers M, Bryce D, Goldman RP, Keller B, Lee P, Biggers V, Nowak J, Weston M. Building an Open Representation for Biological Protocols. bioRxiv 2022.07.05.498808. doi:10.1101/2022.07.05.498808. Published July 8, 2022.
- Bartley B et al. Building an Open Representation for Biological Protocols. *ACM Journal on Emerging Technologies in Computing Systems* 19(3), 2023. doi:10.1145/3604568.
- LabOP website: https://bioprotocols.github.io/labop (accessed 2026-06-14).
- LabOP About / Bioprotocols Working Group: https://bioprotocols.github.io/labop/about (accessed 2026-06-14).
- GitHub: https://github.com/bioprotocols/labop

**SIFT (LabOP co-development and TA3 lead):**
- Bryce D et al. Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis. *ACS Synthetic Biology* 2022. doi:10.1021/acssynbio.1c00305.
- Goldman R, Trivedi N, Bryce D et al. A Bayesian Model for Experiment Choice in Synthetic Biology. AAAI Fall Symposium.
- Eslami M, Moseley M, Eramian H, Bryce D, Haase H. AutoGater. *Scientific Reports* 2024.

**SiLA 2:**
- Ulrich D et al. SiLA 2: The Next Generation Lab Automation Standard. *SLAS Technology* 2022. PubMed: 35639108. doi:10.1177/24726303221085635.
- SiLA standard documentation: https://sila2.gitlab.io/sila_base/ (accessed 2026-06-14).

**SBOL3:**
- McLaughlin JA et al. Synthetic biology open language (SBOL) version 3: Simplified data exchange for biodesign. *Frontiers in Bioengineering and Biotechnology* 2020. doi:10.3389/fbioe.2020.00486.

**IGoR program:**
- ARPA-H. IGoR Program and Technical Description. Appendix A, ARPA-H-SOL-26-155. 2026.

**Cellanome:**
- Cellanome website: https://www.cellanome.com (accessed 2026-06-14). No TA3-relevant publications identified.

**Standards reviewed:**
- Autoprotocol specification: https://autoprotocol.org (Strateos).
- Aquarium: Klavins E et al. (University of Washington). Open-source LIMS with built-in protocol language.
- OpenTrons API: https://opentrons.com (Apache 2.0).
- LinkML: https://linkml.io (NCATS/open community).
- OMEX/COMBINE: Bergmann FT et al. COMBINE archive and OMEX format. *J Biomed Semant* 2014. PMC4272562.
- SED-ML: Scharm M, Waltemath D. A fully featured COMBINE archive of a simulation study. *F1000Research* 2016. PMID:38613325.
- PROV-O: W3C PROV Data Model. https://www.w3.org/TR/prov-o/ (accessed 2026-06-14).
