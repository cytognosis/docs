## 34. Our contribution: TA3 and TA4 execution stack

**Role in the loop:** TA3 translates TA2 experiment designs into instrument-agnostic, reproducible protocol specifications. TA4 executes those protocols across a network of validated laboratories and returns QC-rich, model-ready data to TA1.

---

### TA3: Layered Interoperable Protocol Stack (SIFT lead)

**Lead:** **SIFT** (Robert Goldman, PhD and Dan Bryce, PhD), developers of LabOP, leads TA3. SIFT engages equipment makers and standards bodies and participates in program bake-offs.

**Four-layer stack:** Each experiment design from TA2 traverses four abstraction layers:

| Layer | What it encodes |
|---|---|
| **Intent** | Declarative scientific question, quality requirements, success criteria |
| **Protocol** | Standard processes with error handling and versioned parameter sets |
| **Calibration** | Parameters and uncertainty standardized across devices; IV&V calibration artifacts |
| **Hardware** | Machine-specific settings, isolated behind common interfaces |

This layering separates scientifically meaningful parameters from arbitrary local lab preference, which is the core IGoR reproducibility requirement. Changes to locked-default parameters go through a **Request-for-Comments (RFC) process** backed by evidence; the RFC log is a durable audit trail.

**Open standards backbone:** The TA3 stack is built on the **LabOP** lineage with **LinkML-based open schemas** for all protocol representations. All protocol versions are archived and versioned. Carpenter's open image-data standards (Cell Painting Gallery, JUMP dataset, OASIS/COBA) and Cellanome's documented SOP-based workflows seed the TA3 standard at program start.

**Modality coverage (Phase I >=2; Phase II >=3; Phase III >=4):**

1. Live-cell imaging + same-cell scRNA-seq (Cellanome R3200 Perturb-LINK)
2. Optical pooled screening + Cell Painting morphological screening (Carpenter)
3. High-throughput sequencing-based assays (Illumina)
4. Functional and multi-omics assays (available as Phase III extension)

**Governance:** Changes to locked protocol parameters require RFC-governed process with documented justification. This is the mechanism by which the stack eliminates arbitrary procedural variation, a stated IGoR requirement.

**TA3 milestones:**

| Phase | Deliverable/milestone |
|---|---|
| Phase I | Protocol schema and calibration artifacts defined; same protocol run at two team labs with comparable outcomes on >=1 experiment; >=2 modalities |
| Phase II | RFC process operational with >=2 RFCs executed; protocols run at >=3 labs including >=1 cross-team, each executing >=3 experiments to predefined reproducibility thresholds; >=3 modalities |
| Phase III | Open data and metadata layer delivered; engagement with >=1 external standards body or manufacturer; protocols run at >=5 labs across teams; >=4 modalities; connect-a-thon interoperability demonstrated |

---

### TA4: Validated-Lab Marketplace (Matt Tegtmeyer lab, Cellanome, Illumina; Anne Carpenter computational)

**Structure:** TA4 has two experimental arms plus a shared computational analysis layer. The two experimental arms satisfy the IGoR ">= 2 TA4 labs" requirement; additional performers are additive.

**Two-arm model:**

| Arm | Performer | Role | Key platform |
|---|---|---|---|
| **Academic experimental arm** | **Matt Tegtmeyer lab (Purdue)** | All wet-lab experiments: iPSC-neuron disease models, multi-modal same-cell readouts | **Element AVITI24 / Teton CytoProfiling** (RNA 350-plex + protein/phospho 50-plex + Cell-Painting-style organelle morphology + in-situ CRISPR-guide DISS; neuroscience panel available); confirmed Purdue faculty 2026-06-15 |
| **Industry experimental arm** | **Cellanome** (Dwight Baker, SVP Product Development) | Live-cell imaging + same-cell scRNA-seq + pooled CRISPR; advancing as of 2026-06-17 | **R3200 programmable CellCage**, Perturb-LINK (longitudinal live imaging + same-cell scRNA-seq + CRISPR guide reads) |
| **Computational analysis layer** | **Anne Carpenter, PhD** (IPAI/Purdue, transitioning from Broad ~Sep 2026) | Interpretable morphology and cellular-imaging models; consumes readouts from both arms; TA4 analysis and TA1/TA2 interpretability bridge. **No wet-lab bench.** | CellProfiler, JUMP dataset (>116K compounds), Cell Painting open data infrastructure |
| **TA4 Lab 3** | **Illumina** | High-throughput sequencing + perturbation data | **Billion Cell Atlas** perturbation resource (in-kind resource sharing) |

> [!NOTE]
> **Reproducibility design:** the academic arm (Matt's lab + Element AVITI24; fixed-cell in-situ at massive scale) and the industry arm (Cellanome R3200; live-cell + same-cell temporal readouts) are **orthogonal/complementary**, not redundant. Running the same iPSC-neuron variant lines on both platforms provides a built-in **cross-arm concordance check** that maps directly onto the program's concordance gates (85% intra-team, 90% cross-team). Anne's computational morphology models are the common analysis layer that makes the two arms comparable.

> [!NOTE]
> **Cellanome operating model (open, 2026-06-17):** Options under discussion include placing an R3200 in a PsychIGoR lab (capex, in-house capability) versus sending cells/samples to Cellanome for execution (opex). Pricing pending. The Phase I cross-arm comparison (Element AVITI24 vs. Cellanome R3200) is framed as a designed concordance milestone, not the standing model.

**Note on Panome Bio:** Earlier drafts listed **Panome Bio** (Adam Richardson, VP Operations) as a fourth warm TA4 performer providing CLIA-certified untargeted metabolomics, lipidomics, and proteomics. Panome is held as an optional Phase II extension. The current base team uses Illumina as Lab 3.

**Phase I anchor experiment:** Paired isogenic iPSC lines carrying a **22q11.2-region lesion** (a patient-derived 22q11.2-region TBX1 exon 2 CNV validation line; see restricted section 41), CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons. TA2 designs the discriminating screen; Matt's lab and Cellanome execute multi-modal readouts across both experimental arms; Anne's computational models provide the morphological analysis layer; TA1 defines the disease axes and ingests the results, establishing the cycle-time baseline. Cell-type morphological and molecular signatures of the 22q11.2 deletion are experimentally established as a precedent by Tegtmeyer et al. *Nat Commun* 2025 (DOI: 10.1038/s41467-025-61547-x).

**Phase concordance gating:** Data ingestion into TA1 is conditional on passing concordance thresholds.

| Phase | Concordance threshold | Scope |
|---|---|---|
| Phase I | >=80% (intra-team) | Same experiment at two team labs |
| Phase II | >=90% (cross-team) | >=3 experiments; multicellular systems |
| Phase III | >=90% across marketplace | Unified marketplace; external-researcher use; >=3 labs |

**Data return format:** QC-rich packages formatted to the IGoR common data model. All data are released openly at each phase milestone, consistent with the open-science license (Apache 2.0 code; CC BY 4.0 documentation).

**Resource sharing (in-kind, ~$4.0M):**

- Illumina: Billion Cell Atlas perturbation data access + sequencing credits
- Cellanome: discounted R3200 instrument access
- Cloud compute research credits for TA1/TA2
- JUMP Cell Painting reference data (open; leverages prior public investment)

**TA4 milestones:**

| Phase | Milestone |
|---|---|
| Phase I | >=1 cell line and instrument validated on IV&V artifacts at each of two labs; intra-team reproducibility at >=80% concordance; two-way capability communication established |
| Phase II | >=2 additional instruments validated per lab; marketplace request/return interface operational; cross-team experiment at >=90% concordance across >=3 experiments; exceptions per experiment reduced >=50% vs. Phase I |
| Phase III | Unified marketplace across teams; experiments ordered and executed across teams; >=90% concordance; >=70% of exceptions handled autonomously; connect-a-thon completed |
