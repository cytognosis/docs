## 22. Landscape: TA3 protocol standards and TA4 lab automation

This section surveys the protocol standards ecosystem and lab-automation landscape relevant to IGoR TA3 (interoperable experimental procedures) and TA4 (validated-laboratory marketplace). The key finding is that no existing stack provides a layered intent-to-hardware abstraction with procedurally locked parameters and an open validated marketplace.

---

### 22.1 Protocol and standards efforts

#### Declarative/machine-readable protocol languages

**LabOP** (Laboratory Open Protocol language) is the most directly relevant open standard. LabOP provides a machine-readable, modality-agnostic protocol language based on RDF/OWL, supporting declarative specification of experimental intent that can be compiled to hardware-specific execution. It is the basis for our TA3 intent layer and is developed by partners at SIFT (Robert Goldman and Dan Bryce, automated-planning experts).

**SiLA 2** (Standardization in Lab Automation, version 2) provides an open gRPC-based communication standard for laboratory instrument interfaces, enabling software to control lab hardware across vendors. SiLA 2 addresses the hardware-interface layer but not the higher-level intent or protocol-semantic layers.

**Autoprotocol** (Transcriptic/Strateos) is a JSON-based protocol format targeting cloud-lab execution. It is vendor-specific and does not abstract across instrument types.

#### Data modeling and schema standards

**LinkML** (Linked data Modeling Language) provides a YAML-based schema-definition language that compiles to JSON Schema, OWL, SHACL, and other formats. We use LinkML to define open schemas for experiment metadata, QC parameters, and data-return packages in our TA3 stack.

**OMEX/COMBINE and SED-ML** provide standards for archiving and re-executing computational models alongside their experimental metadata. **KiSAO** (Kinetic Simulation Algorithm Ontology) supports reproducibility of simulation runs. These standards anchor the computational reproducibility layer of TA1 model archiving.

**FAIR principles and Bioregistry** underpin all data and metadata in our system, with persistent, resolvable identifiers for every entity.

#### Open data standards for imaging

The **Cell Painting Gallery** (Broad Institute / Carpenter lab) and **JUMP** (Joint Undertaking in Morphological Profiling) dataset provide open image-data standards and a reference compendium of morphological profiles for ~116,000 compounds across multiple cell lines, seeding the TA3 morphological-screening layer. The **OASIS/COBA** standards (Open Archive for Spatial Imaging/Serology) extend these principles to spatial omics data.

---

### 22.2 Cloud and automated labs

**Emerald Cloud Lab** (ECL) is the most established cloud-lab platform, providing remote automated execution of a broad set of experimental protocols. ECL demonstrates the feasibility of protocol-driven remote execution but uses a proprietary protocol stack, lacks an open validated marketplace, and is not designed around a mechanistic disease model.

**Lila Sciences** and **Periodic Labs** operate proprietary AI-directed robotic laboratory systems (see Section 21). Both emphasize autonomous active-learning loops without a mechanistic causal model grounding experiment selection.

**CROs (contract research organizations)** such as Panome Bio (TA4 partner; untargeted metabolomics, lipidomics, proteomics; CLIA-certified) provide validated experimental services but do not participate in open marketplace frameworks with machine-readable capability manifests.

---

### 22.3 Phenomics and morphological screening resources

**Cell Painting / JUMP** (Carpenter lab, Broad Institute; JUMP Consortium) provides the largest open reference compendium of cellular morphological profiles. The Carpenter lab's 2025 NeuroPainting paper (Tegtmeyer et al. Nat Commun 2025) directly demonstrates Cell Painting applied to 22q11.2 deletion iPSC-derived neurons, establishing morphological and transcriptomic signatures of the deletion; this directly de-risks our TA4 anchor experiment.

**Cellanome R3200** provides a programmable CellCage platform integrating live-cell imaging with same-cell pooled-CRISPR sequencing (Perturb-LINK), enabling simultaneous morphological and transcriptomic readouts in neuronal models. Cellanome is the industry experimental arm of TA4. The academic experimental arm is Matt Tegtmeyer's lab at Purdue, which runs all wet-lab experiments using the Element AVITI24 / Teton CytoProfiling platform for multi-modal same-cell readouts. Both arms together satisfy the program's requirement of at least two validated TA4 laboratories.

---

### 22.4 What is missing

The landscape lacks three capabilities that our TA3/TA4 stack provides:

1. **A layered intent-to-hardware abstraction with procedurally locked parameters.** Existing protocol languages (Autoprotocol, SiLA) address individual layers without integrating intent, protocol-semantic, calibration, and hardware layers into a unified stack. No existing system implements an RFC-governed process that treats parameter changes as requiring explicit scientific justification.

2. **An open validated marketplace.** Emerald Cloud Lab, Lila, and CROs are proprietary or point-to-point. No open, machine-readable marketplace exists where labs publish validated capability manifests and researchers can direct experiments to validated labs based on those capabilities.

3. **Alignment between protocol standards and a mechanistic disease model.** Existing standards treat protocols as self-contained; none are designed so that protocol outputs feed directly into an updating causal disease model, or so that the disease model drives which parameters the protocol must constrain. Our TA3/TA4 stack is designed around this closed-loop requirement from the start.

---

### 22.5 Our TA3/TA4 stack

The TA3 stack covers four abstraction layers: **intent** (declarative scientific question and quality requirements), **protocol** (standard processes with error handling), **calibration** (parameters and uncertainty standardized across devices, with independent IV&V calibration artifacts), and **hardware** (machine-specific settings isolated behind common interfaces). Parameters with weak scientific justification are locked by default; changes require RFC-governed justification. LinkML-based open schemas define all metadata. The stack supports at least four modalities: live-cell imaging, optical/morphological screening, sequencing-based assays, and functional assays.

TA4 provides the validated-laboratory network: Carpenter (optical pooled and Cell Painting morphological screening), Cellanome (live-cell imaging with same-cell pooled CRISPR sequencing for neuronal models), and Illumina (high-throughput sequencing and Billion Cell Atlas perturbation resource as in-kind resource sharing). Each lab publishes machine-readable capability manifests, validates against shared IV&V calibration artifacts, and demonstrates cross-laboratory concordance (Phase I target: 85%; Phase II and III: 90%).

> [!NOTE]
> **Related:** this section covers protocol-execution standards (how an experiment is run). The model and disease-knowledge representation standards (how disease mechanism is encoded) are in section 24, and the stack we adopt is in section 35.
