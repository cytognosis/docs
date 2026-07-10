# Element Bio Teton CytoProfiling vs. Cellanome R3200

**Technical competitive comparison · 2026-06-19**

---

## BLUF

These two systems are **not competitors; they solve opposite problems**. **Element Teton CytoProfiling** (on the AVITI24) is a **fixed-cell, high-plex endpoint readout** that profiles millions of dead, cross-linked cells per run; it cannot touch live function, calcium imaging, or electrophysiology. **Cellanome R3200** is a **live-cell, longitudinal platform** that keeps tens of thousands of cells alive in programmable microcompartments, images them over days (including neuronal calcium activity), perturbs them on-chip, then captures same-cell whole-transcriptome RNA-seq.

**If you only read one thing (reading time ~9 min):** For any functional or live-cell need, including calcium imaging, **only Cellanome qualifies**; Element is disqualified by its mandatory formaldehyde fixation. But **neither platform does true electrophysiology** (no MEA, no patch clamp), and Cellanome's calcium imaging is confirmed only for **slow, multi-day activity**, not yet for **sub-second neuronal firing**.

---

## The core distinction

| | **Element Teton CytoProfiling** | **Cellanome R3200** |
|---|---|---|
| **Paradigm** | Fixed-cell, high-plex spatial multiomics **readout** | Live-cell, longitudinal functional imaging + same-cell transcriptomics |
| **Best analogy** | A microscope-resolution "molecular photograph" of millions of cells at one instant | A programmable "live-cell movie + endpoint RNA-seq" of thousands of cells over days |
| **Runs on** | AVITI24 sequencer (sequencing-by-ABC) | R3200 instrument with CellCage chips (DMD photopolymerized enclosures) |
| **Decisive limit** | Cells are **dead before any data is collected** | **Throughput ceiling** (tens of thousands, not millions) |

---

## At-a-glance comparison

| Dimension | **Element Teton (AVITI24)** | **Cellanome R3200** |
|---|---|---|
| **Cell state** | **Fixed** (8% formaldehyde, mandatory first step) | **Live** throughout; viable and functional |
| **Throughput / run** | Up to ~2M adherent or ~10M suspension cells (dual flow cell) | "Tens of thousands" of CellCage enclosures per flow cell |
| **Parallel conditions** | 1-, 12-, or 48-well slide formats | 4-8 isolated lanes, programmable per lane |
| **RNA** | **350 targeted** transcripts (panel); whole-transcriptome only via separate Atlas/DISS cartridge | **Whole-transcriptome scRNA-seq**, same physical cell |
| **Protein** | 50-88 (up to ~138) targets, in situ | Surface markers + functional reporters by fluorescence; no ELISA-type cytokine quant |
| **Morphology** | 6 organelle markers (roadmap ~20) | Brightfield + 4-channel fluorescence + AI morphotyping, over time |
| **Detection** | Avidite Base Chemistry (ABC) **sequencing** of barcodes, in flow cell | **Live optical imaging** + off-chip NGS of recovered cDNA |
| **Spatial resolution** | <250 nm subcellular, single instant | Per-compartment (CCE address), tracked over time |
| **Live function / calcium imaging** | **None** (cells fixed) | **Calcium activity demonstrated** over days; fast firing unconfirmed |
| **Electrophysiology (MEA / patch clamp)** | **None** | **None** (calcium is an optical proxy, not ephys) |
| **Longitudinal** | No (single endpoint) | **Yes**, hours to weeks, time-lapse |
| **On-platform perturbation** | **No** (reads out screens perturbed elsewhere) | **Yes**: chemical dosing/washout + pooled CRISPR (Perturb-LINK) |
| **Native environment / 3D** | Dissociated cells or monolayer on flow cell | Coatings (laminin, PLO), co-culture, neurospheres; no dissociation step |
| **Time-to-result** | **<24 h** per run, ~45 min prep | Days to weeks (experiment-defined) + library/seq turnaround |
| **Cell types** | Lines, primary, co-culture; iPSC-neurons unconfirmed | Immune, cancer, **iPSC/primary neurons, astrocytes, microglia**, neurospheres |
| **Commercial status** | Generally available; $424K instrument | Launched (AGBT 2026); also via Psomagen as a service |
| **Validation** | 3 preprints (multiomics, NSCLC, CRISPR screen) | 1 peer-reviewed (JITC 2025) + 2 preprints (2026) + posters |

---

## Dimension-by-dimension

### 1. Throughput and scale

**Element wins on raw cell count by ~100x.** Teton images an entire 10 cm² flow cell with no field-of-view selection, profiling **up to 2 million adherent or 10 million suspension cells** across a dual-flow-cell run, in **48-well, 12-well, or 1-well** formats. This makes it well suited to population-scale endpoint screens.

**Cellanome trades count for depth and time.** Each flow cell holds **"tens of thousands"** of CellCage enclosures across **4 to 8 physically isolated lanes**. One published run tracked tens of thousands of A549 cells; a neuro run held **hundreds of neurospheres** (100-200 cells each). The unit of throughput is **a tracked living cell over time**, not a snapshot.

### 2. Multimodal profiling

**Both are genuinely multimodal, but on different axes.**

- **Element** co-detects, from the **same fixed cell in one run**: 350 RNA targets, 50-88 proteins (including phosphoproteins), and 6 morphology markers, all at <250 nm subcellular resolution. The modalities are **molecular and static**.
- **Cellanome** links, to the **same physical living cell**: longitudinal morphology and functional behavior (proliferation, killing, phagocytosis, calcium activity), then **whole-transcriptome scRNA-seq** at endpoint, plus CRISPR guide identity (Perturb-LINK). The modalities are **functional-plus-genomic and temporal**.

**Key gap each way:** Element gives you **deeper static plex** (targeted RNA + high-plex protein at subcellular resolution) but **zero dynamics**. Cellanome gives you **behavior-to-transcriptome linkage over time** but **no high-plex in-situ protein panel and no spatial in-situ transcriptomics**; its protein readout is fluorescence imaging, not ELISA/Olink-style quantification.

### 3. Readout modalities and detection chemistry

**Element = sequencing-based.** Probes (RNA) and antibody-oligo conjugates (protein) are amplified into polonies and read by **Avidite Base Chemistry sequencing** directly in the AVITI24 flow cell. It is an imaging instrument, but the signal is **sequenced barcodes**, not live fluorescence. Output is a single high-resolution molecular map per cell.

**Cellanome = live optical imaging plus off-chip NGS.** Readout is **brightfield + 4-channel fluorescence time-lapse** with onboard AI morphotyping, followed by **in-compartment lysis, barcoded reverse transcription, and pooled library prep** for standard scRNA-seq (Seurat-compatible output). Embedded fiducials let third-party imagers re-register to individual compartments.

### 4. Electrophysiology and calcium imaging (the decisive dimension)

This is where the platforms separate hardest, and where precision matters.

| Capability | Element Teton | Cellanome R3200 |
|---|---|---|
| **Calcium imaging** | **Impossible.** Cells are formaldehyde-fixed first; no ion flux, no live sensor signal. | **Demonstrated.** Neurosphere "calcium activity tracked over multiple days" on the official neurobiology page and AGBT 2026 coverage. |
| **GCaMP (by name)** | N/A | **Not named** in public materials; 4-channel fluorescence is compatible with GCaMP (green), so plausible but unconfirmed. |
| **Fast firing (sub-second spikes)** | N/A | **Unconfirmed.** Demonstrated use is slow, multi-day activity; sub-second action-potential-linked transients not shown. |
| **MEA / patch clamp** | **None** | **None.** No electrodes or recording hardware exist on the platform. |
| **Voltage indicators (optical ephys)** | **None** | **Not mentioned;** plausible given fluorescence channels, unconfirmed. |

**Bottom line on function:** If you need **any** live functional readout, **Element is out**. Cellanome **can** do calcium imaging as an **optical proxy for neuronal activity**, confirmed at the slow/multi-day scale. **Neither platform does true electrophysiology.** If the experiment requires fast spike-resolved firing or membrane-potential recording, that needs an **external MEA, patch clamp, or fast GCaMP confocal/light-sheet rig** regardless of which of these two you pick.

### 5. Experimentation time and longitudinal capability

**Element is fast and terminal:** ~45 min hands-on prep, **<24 h** instrument run, one time point. You get a result the next day, but only a single snapshot.

**Cellanome is slow and temporal by design:** experiments run **hours to weeks** (32 h for an EGFR-inhibitor study; 12 h for microglial phagocytosis; multiple days for neurospheres), with programmable media exchange and walk-away operation between imaging sessions. The rate-limiter for iPSC-neuron work is **cell differentiation time**, not the instrument. Add library prep and sequencing turnaround for the transcriptomic endpoint.

### 6. Live cells and native environment

**Element requires death.** **8% formaldehyde fixation is the mandatory first step** for both adherent and suspension inputs (a former optional permeabilization step was recently removed). Cells can be cultured on the flow cell beforehand, but no viable readout exists after the assay begins. Tissue sections (FFPE/fresh-frozen) are a **2026 roadmap item, not shipping**.

**Cellanome keeps cells alive in tunable microenvironments.** CellCage enclosures are **permeable, biocompatible** compartments; cells attach, divide, fire, and extend axons inside them. It supports **surface coatings (fibronectin, laminin, poly-L-ornithine)**, **co-culture** with defined effector-to-target ratios, and **intact neurospheres** with axon extension and synapse formation between spheres. Critically, it **eliminates the dissociation step**, preserving temporal and lineage continuity. True large organoids (beyond ~200-cell neurospheres) are not yet demonstrated.

### 7. Genetic and chemical perturbations

**Element does not perturb; it reads out perturbations done elsewhere.** The AVITI24 has no fluidic, optical, or genetic delivery mechanism. Its strength is **reading out pooled or arrayed screens at scale**: a 500-gene CRISPR screen with simultaneous guide-RNA sequencing, transcriptome, protein, and morphology has been demonstrated (DISS/optical pooled screening). The 48-well format is positioned for arrayed drug screens, each well one condition. All perturbation happens **before fixation**.

**Cellanome perturbs on-platform, programmatically.**

- **Chemical:** small molecules, cytokines, and antibodies delivered with **programmable timing and washout**, including sequential pulsing, via the isolated-lane architecture.
- **Genetic:** **pooled CRISPR screens (Perturb-LINK)**, linking sgRNA identity to same-cell transcriptome and live morphology; demonstrated to genome-wide scale.
- **Limits:** delivery is **per-lane, not per-individual-compartment** (no addressable single-CCE dosing described); on-chip viral transduction/transfection is not described and likely requires pre-transduction before caging.

### 8. Sample and cell types

**Element:** immortalized lines (HeLa validated), primary cells, co-cultures, suspensions (incl. PBMCs), Matrigel-coated cultures. Neuroscience panel is validated for **neural cell lines**; **iPSC-derived neurons are not explicitly validated**.

**Cellanome:** broad immune, cancer, epithelial/endothelial, and mesenchymal panels, plus an explicit **neuronal/glial set: primary and iPSC neurons, astrocytes, microglia, neural stem cells, Schwann cells**, with functional neurosphere assays demonstrated.

### 9. Commercial status

**Element Teton:** Announced April 2024 at AACR; **generally available**; AVITI24 instrument **$424K new / $150K upgrade**; consumable model (cartridge + panel kits per run); Certified Service Provider program live (OMAPiX, Cornell). Mature and orderable.

**Cellanome R3200:** Founded ~2020 by **ex-Illumina leadership (Ronaghi, Flatley, Ostadan)**; **~$213.75M raised** (Series B $150M, Jan 2024; DFJ Growth, Premji Invest, 8VC, General Catalyst). Platform **launched and showcased at AGBT 2026**; also available **as a service via Psomagen** (subsidized pilot through June 30, 2026). Newer, less third-party-validated, instrument list price not public.

### 10. Validation

**Element:** three 2025 bioRxiv preprints (high-throughput multiomics; NSCLC TKI-resistance same-cell multiomics; DISS optical pooled screens). No peer-reviewed journal paper yet, consistent with a late-2024 launch.

**Cellanome:** one **peer-reviewed** paper (Li et al., *J. Immunother. Cancer*, Nov 2025, EGFR-inhibitor resistance), two 2026 platform/method preprints (Khurana et al. on CCE imaging+transcriptomics; Orcutt-Jahns et al. on Perturb-LINK), plus neuro and immune posters. Named collaborators include the Spitzer Lab (UCSF).

---

## Bottom line: when to use which

| If you need... | Use |
|---|---|
| Millions of cells, deep static RNA+protein+morphology at one time point | **Element Teton** |
| High-plex readout of a pooled/arrayed CRISPR or drug screen | **Element Teton** |
| Subcellular spatial molecular detail | **Element Teton** |
| Live cells kept alive in a native-like microenvironment | **Cellanome R3200** |
| Functional behavior over time linked to same-cell transcriptome | **Cellanome R3200** |
| **Calcium imaging** or any live functional neuronal readout | **Cellanome R3200** (only option here) |
| On-platform, programmable chemical or genetic perturbation | **Cellanome R3200** |
| **True electrophysiology (MEA / patch clamp / spike-resolved firing)** | **Neither** (needs a dedicated external rig) |

The honest framing: **they are complementary**. A mature workflow could use Cellanome for live functional discovery and perturbation, then Element for high-throughput, high-plex molecular readout of fixed endpoints at population scale.

---

## Open questions to resolve

1. **Cellanome calcium-imaging temporal resolution.** Confirmed for slow, multi-day activity. Whether the standard R3200 pipeline captures **sub-second, spike-linked GCaMP transients** is unconfirmed and should be confirmed directly with the vendor before committing to it as a fast-firing functional readout.
2. **iPSC-neuron validation on Element.** Neural cell lines are supported; iPSC-derived neuron cultures are not explicitly validated.
3. **Cellanome instrument list price** is not public; the Psomagen service route is the near-term access path.

---

## Sources

**Element Biosciences (primary, vendor docs):**
- [Teton CytoProfiling product page](https://www.elementbiosciences.com/products/aviti24/cytoprofiling)
- [Teton CytoProfiling Product Sheet, Rev. B, Oct 2025](https://www.elementbiosciences.com/hubfs/element_biosciences_2025/resources_assets/bofu/LT_00053_Product_Sheet_Teton_Cytoprofiling_Kits.pdf)
- [Teton CytoProfiling User Guide MA-00053 Rev. F](https://www.elementbiosciences.com/hubfs/element_biosciences_2025/resources_assets/pdfs/Teton_CytoProfiling_User_Guide_MA_00053_E.pdf)
- [AVITI24 availability press release, April 2024](https://www.elementbiosciences.com/news/element-biosciences-announces-availability-of-aviti24-the-first-benchtop-sequencer-capable-of-direct-cell-profiling)
- [DISS / optical pooled screening blog, Dec 2025](https://www.elementbiosciences.com/blog/connecting-guides-genes-and-morphology-with-direct-in-sample-sequencing)
- [bioRxiv: high-throughput multiomics on AVITI24, May 2025](https://www.biorxiv.org/content/10.1101/2025.05.03.651997v1)
- [bioRxiv: DISS optical pooled screens, Oct 2025](https://doi.org/10.1101/2025.10.11.681797)

**Cellanome (primary + independent):**
- [Cellanome R3200 products page](https://www.cellanome.com/products)
- [CellCage technology page](https://www.cellanome.com/technology)
- [Cellanome neurobiology page (calcium activity)](https://www.cellanome.com/neurobiology)
- [Cellanome CRISPR / Perturb-LINK page](https://www.cellanome.com/crispr-screen)
- [Cellanome publications](https://www.cellanome.com/resources-publications)
- [GenomeWeb: Cellanome at AGBT 2026](https://www.genomeweb.com/sequencing/agbt-cellanome-showcases-live-cell-analysis-platform-marrying-imaging-sequencing)
- [Psomagen: understanding the Cellanome R3200](https://www.psomagen.com/blog/understanding-the-cellanome-r3200)
- [DFJ Growth: Cellanome Series B](https://dfjgrowth.com/story/cellanome-powering-the-era-of-cell-biology/)
- Li et al. (2025), *Journal for Immunotherapy of Cancer* (peer-reviewed; EGFR-inhibitor resistance)

*Internal IGoR TA4 deep-dive files in this repo provide additional non-public context and the live vendor-contact status; they are intentionally not cited here so this document is shareable-clean.*
