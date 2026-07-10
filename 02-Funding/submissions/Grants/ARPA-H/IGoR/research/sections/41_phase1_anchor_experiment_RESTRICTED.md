## 41. Phase I anchor experiment (RESTRICTED: personal genomic data)

> [!CAUTION]
> **RESTRICTED. Internal only.** This section describes a Phase I anchor experiment built on the founder's personal genomic variant. It contains personal health and genomic information and must not appear in the `shareable` build, partner-facing materials, or public submission text. In external materials, refer only to "a patient-derived 22q11.2-region validation line" with no personal attribution.

### The line

A paired, isogenic induced-pluripotent-stem-cell (iPSC) design built from a patient-derived line carrying an ultra-rare **32 bp CNV in TBX1 exon 2**, a 22q11.2-deletion-superclass model, with a **CRISPR-corrected isogenic control** as the matched healthy comparator. The pair is differentiated to **NGN2 neurons (about 14 days)**, giving a clean genotype-to-phenotype contrast with the genetic background held constant.

### Why it anchors Phase I

- **It de-risks TA1 validation.** The paired lines define a concrete set of disease axes (section 10) that the model must recover, and TA4 returns the cellular and morphological readouts that update TA1.
- **It has a built-in falsifiability test.** Whether **vitamin B12 (methylcobalamin) reverts the mutant phenotype** is a sharp, pre-registered prediction drawn from Tbx1-mutant mouse rescue (Life Sci Alliance 8(2):e202403075). A clean reversion supports the causal chain; no reversion falsifies that arm. Note: this test is present in the v3 draft and was dropped in v4; section 90 flags the decision to reinstate it.
- **It connects to a validated assay.** The NeuroPainting morphological assay on 22q11.2 iPSC neurons (Tegtmeyer et al. 2025) is the published precedent and a natural TA4 readout via the Carpenter optical screening lane.

### Execution notes

- **Line generation** can be run fee-for-service by the Broad Center for the Development of Therapeutics; subclone the starting line first to control clonal variation.
- **Optional follow-on:** targeted Perturb-seq of methylation-cycle genes to test the mechanistic arm directly.
- **Disease-axis definition** uses the paired lines to fix the cellular shift-space coordinates that the clinical cohorts (section 40) are then projected onto.

### Decision

Decide whether to fold this anchor into IGoR as a Phase I validation deliverable or to run it as a parallel, independent study. Section 90 carries this as an open decision.
