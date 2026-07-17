# Universal Dimensional Map v1: Figure Specification

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Audience**: researchers, stakeholders, design/plotting implementer
> **Tags**: `research`, `biotyping`, `neuro`

## Purpose

This spec describes exactly what `universal_dimensional_map_v1.mmd` encodes as a structural
relationship diagram, and what a designer or a plotting script (matplotlib/plotly/D3) should render
as the polished, publication-quality SVG version. The Mermaid file is a reviewable proxy for the
relationships; it is not laid out on true continuous axes because Mermaid does not support a
scatter/axis coordinate system. The publication figure should use true continuous axes as described
below.

---

## 1. What the figure must show (four layers, one diagram)

1. **A 2D or 3D continuous coordinate space** whose axes are genomic factors (Section 2).
2. **Disorders plotted as points or small glyphs** in that space, sized/styled by evidence
   confidence, with core-scope disorders visually distinct from extension-scope disorders.
3. **Three treatment layers** (micro, meso, macro) shown as an adjacent panel or as a layered
   annotation attached to each disorder point, not as a fourth competing axis.
4. **A legend** covering: axis identity, confidence encoding, core vs. extension encoding, and
   treatment-layer color key.

---

## 2. Axes

- **Primary figure (core scope): 2 axes.**
  - X axis: **SB factor loading** (schizophrenia + bipolar genomic factor; excitatory-neuron
    cell-type signature). Range: 0 (no loading) to 1 (maximal loading), unitless composite score.
  - Y axis: **Internalizing factor loading** (MDD + PTSD + anxiety genomic factor; oligodendrocyte/
    myelin cell-type signature). Same 0-1 range.
  - Rationale: these are the two largest and best-characterized factors (Grotzinger et al. 2025) and
    the two the three core disorders anchor most cleanly.
- **Extended figure (5-factor version): use a radar/spider chart instead of a 2D scatter.**
  - 5 spokes: SB, Internalizing, Neurodevelopmental, Compulsive/eating, Substance-use.
  - Each disorder is a closed polygon across the 5 spokes rather than a single point.
  - Use this version only when the figure needs to show all 14-disorder scope; the 2-axis scatter is
    preferred for the MDD/BD/SCZ (+PTSD/anxiety) core scope because it is easier to read.
- **Do not fabricate precise loading values.** As flagged in the review document (Section 2), exact
  per-disorder loadings from the Grotzinger et al. supplementary tables have not yet been extracted.
  Until they are, position disorders using the qualitative tiers below rather than invented decimals:
  - **High loading**: 0.75-0.90 on the relevant axis.
  - **Primary/shared loading** (SB factor for both SCZ and BD): both placed at 0.70-0.85 on the X
    axis, near-zero to low on the Y axis.
  - **Extension loading** (Internalizing factor for PTSD, anxiety): 0.40-0.60 on the Y axis, lower
    than MDD's own placement (MDD at 0.80-0.90 on Y), reflecting that MDD is the factor's primary
    disorder and PTSD/anxiety are secondary.

---

## 3. Nodes (disorders)

| Disorder | Approx. position (X = SB, Y = Internalizing) | Marker style | Scope |
|---|---|---|---|
| Schizophrenia (SCZ) | X: 0.80-0.85, Y: 0.05-0.15 | Filled circle, solid outline | Core |
| Bipolar disorder (BD) | X: 0.70-0.80, Y: 0.20-0.30 (BD carries some internalizing-adjacent depressive-episode signal) | Filled circle, solid outline | Core |
| Major depressive disorder (MDD) | X: 0.05-0.15, Y: 0.80-0.90 | Filled circle, solid outline | Core |
| PTSD | X: 0.05-0.10, Y: 0.45-0.55 | Open circle, dashed outline | Extension |
| Anxiety | X: 0.05-0.10, Y: 0.40-0.50 | Open circle, dashed outline | Extension |

Marker size encodes cross-scale evidence density (how many of the micro/meso/macro layers have
HIGH-confidence findings for that disorder in the canon docs): SCZ and MDD are the largest markers
(HIGH confidence at all three layers); BD is medium-large; PTSD and anxiety are medium (HIGH at
meso, MEDIUM at micro).

---

## 4. Treatment layer panel (micro / meso / macro)

Render as three stacked horizontal bands below or beside the main axis plot, each in its own color
family, each containing labeled anchor items connected by thin leader lines back to the disorder
point(s) they apply to:

| Layer | Color family | Anchor items to include |
|---|---|---|
| **Micro** | Green | BDNF/TrkB plasticity axis (NbN neuroplastogens: ketamine, psilocybin); E/I imbalance / PV-interneuron axis (NbN antipsychotics, D2/5-HT2 antagonism); oxidative/mitochondrial axis (NAC-responsive subgroup) |
| **Meso** | Orange | dlPFC-sgACC edge (SAINT/SNT TMS target, ~79% TRD remission); amygdala-vmPFC edge (threat regulation); thalamus-sensorimotor/prefrontal edges (SCZ reciprocal pattern); default-mode network subgraph (PCC/precuneus-mPFC) |
| **Macro** | Purple | PHQ-9 (MDD), YMRS (BD mania), PANSS (SCZ), GAD-7 (anxiety/PTSD extension) |

Leader lines: MDD connects to BDNF/TrkB (micro), dlPFC-sgACC edge and DMN subgraph (meso), PHQ-9
(macro). BD connects to BDNF/TrkB and oxidative axis (micro), YMRS (macro). SCZ connects to E/I axis
(micro), thalamus edges (meso), PANSS (macro). PTSD/anxiety connect (dashed leader lines, matching
their dashed node style) to the amygdala-vmPFC edge (meso) and GAD-7 (macro).

---

## 5. Color and style conventions

- **Genomic factor axes**: neutral gray gridlines; axis labels in factor-specific accent colors
  (SB axis label in muted purple `#7a4c7a`, Internalizing axis label in muted blue `#2b6777`),
  matching the Mermaid file's `factor` classDef so the two artifacts read as a matched pair.
- **Core-scope disorders**: solid fill, solid outline, full opacity.
- **Extension-scope disorders (PTSD, anxiety)**: open/hollow marker, dashed outline, 70 percent
  opacity, to visually subordinate them without hiding them.
- **Confidence encoding**: marker border thickness scales with confidence (HIGH = 2pt border,
  MEDIUM = 1pt border, LOW = 0.5pt dotted border). Do not use red/green for confidence; reserve color
  for the treatment-layer legend to avoid double-encoding collisions.
- **Treatment layer colors**: green (micro), orange (meso), purple (macro), consistent with the
  Mermaid file's `micro`/`meso`/`macro` classDefs (`#4c7a3f`, `#a8622a`, `#5c4c8a` respectively).
- **Do not use red/green together as a pass/fail encoding anywhere in the figure**; this figure
  communicates evidence structure, not a scored outcome.

---

## 6. Legend (required, bottom-right or as a separate panel)

Legend must contain, in this order:
1. Axis definitions (SB factor, Internalizing factor) with one-line plain description each.
2. Marker style key: filled/solid = core scope; open/dashed = extension scope.
3. Confidence key: border thickness to confidence-tier mapping.
4. Treatment layer color key: green = micro, orange = meso, purple = macro.
5. A one-line caveat: "Disorder positions reflect qualitative factor-loading tiers pending extraction
   of exact per-disorder loadings from Grotzinger et al. (2025) supplementary data; not a fitted
   statistical projection."

---

## 7. Data provenance for implementation

- Disorder-to-factor categorical assignments: `BIOTYPING_DOSSIER_INDEX.md` Section D.2 and
  `transdiagnostic-micro.md` Section 1.
- Micro anchor items: `transdiagnostic-micro.md` Sections 2.1-2.3; `NbN_Glossary.md`.
- Meso anchor items and edge list: `transdiagnostic-meso.md` `VISUAL_DATA` block (already
  machine-readable; reuse directly rather than re-deriving from prose).
- Macro anchor instruments: `transdiagnostic-macro.md`; `_MASTER_ontology_mapping.csv`.
- Confidence tiers: as rated in the source docs (HIGH/MEDIUM/LOW convention, defined in each
  transdiagnostic synthesis's opening section).

## 8. Deliberately out of scope for this figure

- The confidential factorized-PRS genome-only reconstruction method (BDNF/TrkB dossier Section 5)
  must not appear on this figure, in its legend, or in any caption derived from this spec.
- OCD, autism, ADHD, Tourette syndrome, eating disorders, and substance use disorders are not
  plotted in v1; adding them is a scope change for a v2 figure (radar chart version per Section 2),
  not an edit to this spec.
