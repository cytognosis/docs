# Disease biotype docs: shared template and conventions

> Every per-disorder doc in this folder follows this exact structure so the 14 docs harmonize and the transdiagnostic synthesis is mechanical. Read this before writing any disease doc.

## Organizing reference

All 14 disorders come from Grotzinger, Werme, Peyrot, ... Smoller, "Mapping the genetic landscape across 14 psychiatric disorders," Nature 2025 (doi:10.1038/s41586-025-09820-3, 1,056,201 cases). That paper found 5 genomic factors explaining ~66% of genetic variance, with 238 pleiotropic loci:

1. **SB factor**: schizophrenia + bipolar disorder. Shared signal enriched in genes expressed in excitatory neurons.
2. **Internalizing factor**: major depression + PTSD + anxiety. Associated with oligodendrocyte biology.
3. **Neurodevelopmental factor**: ASD + ADHD + Tourette (childhood-onset), spans into others.
4. **Compulsive / eating factor**: OCD + anorexia nervosa + Tourette.
5. **Substance use factor**: alcohol + opioid + nicotine + cannabis use disorders.

Signal shared across all 14 was enriched for broad transcriptional regulation; factor-specific pathways are more specific. Cite this paper in the micro section of every disorder.

## The three scales (RDoC-matrix-style grouped columns)

### MICRO (molecular, genetic, cellular, immune) vs harmonize to Gene Ontology (GO)

Produce a table. For each molecular biotype/dysregulation, fill these columns:

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |

Rules:
- **Neurotransmitter family column**: mark each individually when implicated: GABA, Glutamate, Dopamine, Serotonin, Norepinephrine. Use "none reported" if none.
- **BDNF / neurotrophin column**: flag any neurotrophin signaling (BDNF, TrkB/NTRK2, NGF, NT-3), and note the plasticity implication. GO anchors: neurotrophin TRK receptor signaling (GO:0048011), BDNF signaling, regulation of synaptic plasticity (GO:0048167), positive regulation of long-term synaptic potentiation (GO:1900273).
- **E/I imbalance column**: if reported, mark the direction (E-up / I-down etc.) AND the brain region where it was observed (this is functionally important). Anchor GO/cell terms: GABAergic (parvalbumin) interneuron, glutamatergic synaptic transmission (GO:0035249), GABAergic synaptic transmission (GO:0051932).
- **Oxidative / mito column**: glutathione, ROS, mitochondrial dysfunction. GO anchors: response to oxidative stress (GO:0006979), mitochondrial ATP synthesis.
- **Immune column**: cytokines (IL-6, TNF, CRP), complement (C4), microglia, kynurenine. GO anchors: inflammatory response (GO:0006954), complement activation (GO:0006956), microglial cell activation (GO:0001774).
- Provide GO IDs where confident; mark "approx, needs curation" otherwise. Do not invent IDs.

### MESO (connectomic: fMRI, EEG, MEG) vs map to the Allen Human Reference Atlas, 3D (2020)

Reference atlas: Allen Human Reference Atlas 3D 2020, 141 anatomical regions spanning the full MRI reference brain (https://biccn.org/tools/atlas; Ding et al. and the Allen Institute). Use Allen anatomical structure names. Only add a region from another atlas (e.g., Glasser HCP-MMP, Harvard-Oxford, Brainnetome) if a critical reproducibly-referenced region is genuinely absent from the Allen 141-region set, and clearly flag it as a non-Allen addition with the reason.

Important nuance: many findings are reported for FUNCTIONAL regions/networks (dlPFC, sgACC, default mode network) that are not 1:1 with Allen ANATOMICAL parcels. For each finding, give the Allen anatomical structure that contains the functional region, plus the functional label in parentheses. Example: "cingulate gyrus, subgenual part (sgACC / BA25)".

Produce TWO tables.

NODES table (regions and observed changes):

| Allen region (functional label) | Observed change (hyper / hypo / atrophy / thinning / hyperconnectivity) | Modality (fMRI / EEG / MEG / structural) | Confidence | Source |

EDGES table (associations/connections between regions; the connectome edges):

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |

For the EDGES "Association sign" column use exactly one of: `positive`, `negative (anticorrelation)`, `mixed`. The canonical example is the dlPFC–sgACC anticorrelation used in Stanford SAINT/SNT (negative). Record both the normal sign and how the disorder perturbs it when known.

### MACRO (symptoms, behaviors, manifestations) vs map to SNOMED CT and/or Human Phenotype Ontology (HPO)

Produce a table:

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |

Rules:
- Provide concept IDs where confident (e.g., SNOMED CT "Major depressive disorder" 370143000; HPO "Anhedonia" HP:0033676). Mark "approx, needs curation" otherwise. Do not invent IDs.
- Describe the symptom dimension each biotype maps to (anhedonia, threat-reactivity, compulsivity, inattention, etc.).

### INTERVENTIONAL studies (consolidated, per biotype)

Produce a table linking biotypes to treatment-response evidence. Include pharmacology, neuromodulation (TMS, tES/tDCS/tACS/tTIS, focused ultrasound/LIFU, tVNS), DEEP BRAIN STIMULATION (DBS), and neuroplastogens (ketamine, psilocybin, MDMA, etc.):

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |

Always consider DBS where it has been trialed (e.g., sgACC DBS for TRD, NAc/ALIC DBS for OCD, anorexia, addiction).

## Cross-doc conventions

- Confidence ratings everywhere: HIGH (multi-cohort/multi-site replication), MEDIUM (single-consortium or moderate effect), LOW (single-lab or failed external replication). Flag replication failures explicitly.
- Style: no em dashes; active voice; no "revolutionary", "cure", "game-changing", "breakthrough". Person-first or identity-first as appropriate.
- Inline Vancouver-style citations with DOI/URL; reference list at end.
- End each doc with a "Most defensible biotypes" summary (3 to 6 biotypes integrating across scales) and a one-line statement of which genomic factor (from the 5 above) the disorder loads on.

## Document skeleton (copy this)

```
# Biotypes: [Disorder]

Genomic factor loading (Nature 2025): [which of the 5 factors]

## Seed papers
## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized
## MESO scale (connectomic) vs Allen Atlas nodes + edges
## MACRO scale (phenotype) vs SNOMED CT / HPO
## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)
## Most defensible biotypes (cross-scale synthesis)
## References
```
