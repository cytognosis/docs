# The Human Body as Reference: HRA, HuBMAP, and the Spatial Scaffold

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (human-body-systems.md in Obsidian vault: 04-Engineering/cytos/sensing-schema/) - Agent (n/a)

Scope: how to describe *where in the body* a measurement was taken, *what biological structures* it covers, and *how it relates to canonical references* of healthy human anatomy. This is the missing scaffold layer in the previous documents, and it is what makes "match a model to a dataset" a tractable question across micro, meso, and macro scales.

Two coupled efforts dominate this space:

- The **Human Reference Atlas (HRA)**: standard terminologies, 3D reference organs, and a Common Coordinate Framework that gives every cell in the healthy adult body a unique address. [humanatlas.io](https://humanatlas.io).
- The **Human BioMolecular Atlas Program (HuBMAP)**: the multi-consortium effort that builds the HRA and operates the data portal hosting the experimental data. [HuBMAP Portal](https://portal.hubmapconsortium.org/), [HuBMAP Consortium](https://hubmapconsortium.org/).

## What HRA actually is

The HRA is a multiscale, multimodal, three-dimensional atlas of the anatomical structures, cells, and biomarkers in the healthy adult human body. As of May 2025 the HRA Knowledge Graph (KG) v2.2 covers:

- **71 organs** with **5,800 anatomical structures**
- **2,268 cell types**
- **2,531 biomarkers**
- **10,064,033 nodes** and **171,250,177 edges** in the KG
- ~126 GB of linked open data
- **13 types of Digital Objects** under the Common Coordinate Framework (CCF) Ontology

The KG aggregates into five thematic subgraphs:

1. **2D Illustrations** (FTU and organ-level diagrams)
2. **3D Spatial Reference** (reference organs as meshes)
3. **Biological Structure** (the ASCT+B nesting)
4. **Experimental Data** (HuBMAP datasets registered into the CCF)
5. **Experiment Settings** (donor, protocol, sample provenance)

Sources: [HuBMAP HRA Nature Methods 2024](https://www.nature.com/articles/s41592-024-02563-5), [HRA KG paper, Sci Data 2025](https://www.nature.com/articles/s41597-025-05183-6), [HRA portal "About"](https://humanatlas.io/about).

## The five things HRA gives you

### 1. ASCT+B tables (Anatomical Structures, Cell Types, plus Biomarkers)

The ASCT+B tables capture, per organ, the nested `part_of` structure of anatomical entities, the cell types found in each, and the biomarkers (genes, proteins, lipids, metabolites) used to identify the cell types. Each entry is linked to canonical ontologies:

| Entity | Canonical ontology |
|---|---|
| Anatomical structure | UBERON, FMA |
| Cell type | CL (Cell Ontology) |
| Biomarker (gene) | HGNC |
| Biomarker (protein, lipid, metabolite) | UniProt, ChEBI, etc. |

Each ASCT+B table is authored by domain experts across consortia and is reviewed by anatomists, pathologists, and physicians. This is the most curated, cross-walked spatial-cellular vocabulary in existence for human anatomy. Source: [ASCT+B Nature Cell Biology 2021](https://www.nature.com/articles/s41556-021-00788-6), [3D Reference Organs paper, PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10079270/).

### 2. CCF Ontology and 3D reference objects

The Common Coordinate Framework (CCF) Ontology gives a standard vocabulary for describing **specimens, biological structures, and spatial positions** of tissue blocks and organs. Every reference organ has a 3D mesh; every tissue block can be registered into that mesh; every cell type and biomarker can be referenced to a position. The analogy is explicit: CCF is a latitude-longitude system for the human body. Source: [CCF Ontology paper, Sci Data 2023](https://www.nature.com/articles/s41597-023-01993-8), [HRA CCF Ontology page](https://humanatlas.io/ccf-ontology).

### 3. RUI (Registration User Interface)

The [RUI](https://hubmapconsortium.github.io/ccf-ui/rui) is a web tool where a researcher:

1. Picks the relevant 3D reference organ.
2. Specifies the tissue block's size, position, and rotation in that organ's coordinate space.
3. Reviews automatically assigned anatomical structure annotations (computed from surface mesh collisions against UBERON/FMA-linked structures).
4. Adjusts annotations.

The output is a registered tissue block: a JSON record with size, 3D placement, and a list of UBERON/FMA-linked anatomical structures it intersects. As of HRA v2.0 the RUI supported >50 organs. Source: [Tissue registration RUI paper, Comm Biology 2022](https://www.nature.com/articles/s42003-022-03644-x).

### 4. Vasculature CCF (VCCF)

The [HRA-VCCF](https://github.com/hubmapconsortium/hra-vccf) extends the CCF with the blood vasculature: every tissue block can be characterized by its distance to named vessels, which becomes a coordinate axis in itself. This matters because vessel proximity is a known driver of oxygenation, immune-cell trafficking, and drug penetration: a non-trivial fraction of cellular phenotype is "where in the vascular tree are you". Source: [HRA-VCCF Sci Data 2023](https://www.nature.com/articles/s41597-023-02018-0).

### 5. Organ Mapping Antibody Panels (OMAPs)

[OMAPs](https://humanatlas.io/omap) are community-curated, validated antibody panels for multiplexed tissue imaging (CODEX, IBEX, Cell DIVE, MIBI/SIMS), each tied to a specific organ and a specific list of anatomical structures and cell types it can resolve. The inaugural release covers 171 anatomical structures and 155 cell types across 7 organs using 203 validated antibodies. OMAPs are the spatial-proteomics analog of ASCT+B: they make a panel-organ pairing into a citable, reusable artifact. Source: [OMAPs Nature Methods 2023](https://www.nature.com/articles/s41592-023-01846-7).

## What HuBMAP gives you

The HuBMAP Data Portal serves as the experimental data layer paired with HRA's reference layer. As of October 2025:

- **5,032 datasets**
- **22 data types** (assay types)
- **27 organ classes**
- **310 donors**
- **3 dominant modalities**: mass spectrometry, microscopy, sequencing
- **>1,500 datasets visualizable in-browser via Vitessce** (2D and 3D spatial)
- **Jupyter workspace integration** for interactive analysis

Each HuBMAP dataset has:

- A **donor** record (de-identified demographic, consent)
- One or more **samples** (tissue blocks, with RUI registration into the CCF where applicable)
- One or more **datasets** (assay outputs: FASTQs, OME-TIFFs, count matrices, spatial transcriptomics tables)
- **Provenance graph** linking donor → sample → assay → dataset → derived data

Source: [HuBMAP Data Portal arXiv 2511.05708](https://arxiv.org/abs/2511.05708), [HuBMAP Portal](https://portal.hubmapconsortium.org/), [HRA construction Nature Methods 2024](https://www.nature.com/articles/s41592-024-02563-5).

## Why HRA is the right scaffold for "any sensor anywhere in the body"

This is the central claim of this document and the reason the user asked to integrate HRA into the previous research. The argument:

### HRA is the spatial scaffold across scales

The CCF gives a single coordinate system that accommodates:

- **Cell scale**: every cell type from 2,268 known types is referenced to its `part_of` anatomical structure.
- **Tissue scale**: every tissue block can be registered into a 3D reference organ via the RUI.
- **Organ scale**: 71 organs as 3D meshes with named substructures.
- **Body scale**: organs are positioned within the whole-body reference (Whole Body 3D model).
- **Sub-cellular scale**: biomarker locations can be attached to cell-type entries (membrane vs. nucleus vs. cytoplasm via PATO/GO-CC).
- **Vascular scale**: VCCF gives every position a distance-to-vessel coordinate.

So a single sensor reading (whether scRNA-seq, fluorescence intensity, MERFISH puncta, or a CGM glucose value) can in principle be attached to a CCF coordinate triple plus an organ mesh ID plus a list of intersected anatomical structures plus a vascular distance, all from canonical ontologies.

### HRA covers what the bio noun ontologies do not

The OBO Foundry ontologies (UBERON, CL, HGNC, ChEBI) name *what* things are. They do not give you spatial coordinates, they do not give you `part_of` nesting at the resolution needed to register a 50 µm tissue section, and they do not co-locate cells with the biomarkers used to identify them. ASCT+B does all three. The CCF ontology adds the 3D reference geometry. Together they give you the missing geometric scaffold under the OBO terminology.

### HRA bridges single-cell and clinical settings

HRA's reference organ meshes can be co-registered with patient imaging (MRI, CT, ultrasound) by anatomically corresponding structures. A patient's MRI can be mapped to a "patient-specific CCF" where each voxel has UBERON/FMA-linked anatomical labels; a snapshot biopsy from that patient can then be registered into both the patient-specific CCF and the HRA reference. This means an EEG channel position, an MRI ROI mask, a CGM (positioned subcutaneously near a known vascular site), and a tissue biopsy all become referenceable in the same coordinate system. This is the path to truly multimodal longitudinal subject records.

### HRA is FAIR linked open data

The HRA KG is a SPARQL endpoint over RDF, with PROV-O provenance, Bioregistry-validated CURIEs, and 13 named Digital Object types. It composes natively with everything else in the survey: SOSA `FeatureOfInterest` slots can carry CCF coordinates; LinkML `SubjectManifest` classes can subclass `ccf:Donor`; AnnData `obs` can carry a `ccf_spatial_id` linking to a registered tissue block.

## Integration with the rest of the survey

### HRA + SOSA/SSN

The HRA scaffold populates SOSA's `FeatureOfInterest` and `Sample` slots with maximum specificity:

```turtle
:obs_xenium_lung_42 a sosa:Observation ;
  sosa:hasFeatureOfInterest :tissue_block_donor_038_lung_segment_3 ;
  sosa:observedProperty :gene_expression ;
  sosa:madeBySensor :xenium_instrument_5 ;
  sosa:usedProcedure :proc_xenium_lung_panel_v2 ;
  sosa:hasResult :result_zarr_uri ;
  sosa:phenomenonTime "2026-04-12T11:30:00Z"^^xsd:dateTime .

:tissue_block_donor_038_lung_segment_3 a sosa:Sample, ccf:TissueBlock, fhir:Specimen ;
  sosa:isSampleOf :donor_038 ;
  ccf:registeredInto <http://purl.obolibrary.org/obo/UBERON_0008952> ;  # lower lobe of left lung
  ccf:rui_location [
    ccf:dimension_x_mm 8.4 ;
    ccf:dimension_y_mm 6.1 ;
    ccf:dimension_z_mm 0.8 ;
    ccf:placement_translation [3.21, -2.05, 1.03] ;
    ccf:placement_rotation_quaternion [...] ;
  ] ;
  ccf:intersects_anatomical_structure
    <http://purl.obolibrary.org/obo/UBERON_0002048> ,    # lung
    <http://purl.obolibrary.org/obo/UBERON_0008952> ,    # lower lobe
    <http://purl.obolibrary.org/obo/UBERON_0002187> .    # bronchiole
```

The CCF coordinate triple plus the intersection list plus the RUI placement metadata is exactly what SOSA's `FeatureOfInterest` slot needs to be unambiguous. No other ontology system gives this level of spatial anchoring for human tissue.

### HRA + AnnData / SpatialData

SpatialData already supports coordinate-system transformations and can carry CCF coordinates as a named coordinate system. A HuBMAP-style CCF-registered tissue block becomes a `SpatialData` element where:

- `obs` carries `ccf_anatomical_structure[]` (UBERON CURIEs from RUI intersection)
- `obs` carries `ccf_donor_id` (links to donor manifest)
- `uns` carries `ccf_rui_metadata` (the RUI block placement)
- `obsm` can include `X_ccf_coordinates` (cell-level CCF triples for spatial assays)

This is straightforward to implement and gives every existing scverse pipeline access to CCF queries without additional tooling.

### HRA + ASCT+B + scRNA-seq cell-type annotation

The standard cell-type annotation flow for a new scRNA-seq dataset is: cluster, find marker genes, assign cell type using a reference. ASCT+B turns this into a **constrained classification** problem: given the organ (UBERON CURIE), the candidate cell types are bounded to the ASCT+B-listed types for that organ, and the relevant biomarkers are bounded to the listed biomarkers. This is dramatically more powerful than free-form cell-type calling because it bakes in domain-validated priors. Models that consume ASCT+B tables (CellTypist, popV, Decoupler) already do this implicitly; making it explicit means a `ModelManifest` for a cell-type classifier can declare `expected_organ: UBERON:...; uses_asctb_table: HRA-v2.2-lung-v3` and the platform's match function knows precisely how to validate compatibility.

### HRA + matching across modalities for the same donor

The most practical payoff: a single donor in a Cytognosis longitudinal study contributes a snapshot biopsy (registered via RUI), periodic bloodwork (no spatial location), an EEG session (electrode positions in MNI/Talairach, mappable to UBERON brain regions via FMA cross-walks), and a CGM stream (subcutaneous abdomen, with a known approximate UBERON region). All four can be tied to one `sosa:FeatureOfInterest` (the donor) with HRA-aware spatial annotations on the three modalities that have spatial extent. The platform can then ask cross-modal queries like "for cells in the lower lobe of left lung in donor 038, do their scRNA-seq embeddings predict the donor's CGM time-in-range over the next month?" Without the HRA scaffold, this question requires per-modality spatial-handling code; with it, the spatial join is a CCF query.

## Where the user said "spatial scaffold for sensors across scales", concretely

| Scale | Sensor example | What HRA contributes |
|---|---|---|
| Sub-cellular (organelle, complex) | Cryo-EM, super-res microscopy, FISH puncta | Biomarker localization annotations (membrane/nucleus/cytoplasm), via PATO + GO-CC linked to CL types |
| Single-cell | scRNA-seq, scATAC, Xenium, MERFISH | ASCT+B cell-type catalog per organ, VCCF distances |
| Cell population / micro-anatomy | IHC, IF, multiplex imaging (CODEX/IBEX) | ASCT+B AS nesting, OMAPs, FTU (functional tissue unit) catalogs |
| Tissue block | Bulk RNA-seq, proteomics, lipidomics, spatial T | CCF/RUI registration, organ mesh intersection |
| Organ | MRI, CT, PET, ultrasound | 3D reference organ meshes, UBERON/FMA cross-walks |
| Body region | Wearable position, ECG lead placement | Whole-body 3D model, named anatomical regions |
| Body | CGM, oxygen sat, total-body PET | Donor-level annotations, HuBMAP-style donor demographics |
| Vascular | Angiography, CGM (vessel-relative position) | VCCF distance coordinates, named vessel hierarchy |
| Population | Cohort GWAS, cohort imaging | Donor metadata schema; not spatial per se but compatible |

Every row above can be expressed as a `sosa:Observation` with a CCF-aware `FeatureOfInterest` annotation. The HRA scaffold is what makes the rows commensurable.

## Practical adoption sequence for Cytognosis

1. **Adopt the HRA KG as a Cytognosis ontology dependency.** Pin a release (HRA v2.2 as of writing); subscribe to HRA release notifications; refresh per Cytognosis ontology snapshot cadence.
2. **Add CCF slots to `SubjectManifest`, `SampleManifest`, and `ObservationManifest`**: `ccf_donor_id` (HuBMAP-style UUID), `ccf_rui_location` (the RUI JSON block), `ccf_anatomical_structures[]` (UBERON CURIEs), `ccf_intersects[]` (full intersection list), `ccf_vccf_distance_mm` (when applicable).
3. **For any spatial assay, run RUI registration** at sample intake. For non-RUI-registerable modalities (CGM, EEG, blood draw), record the closest applicable UBERON CURIE plus a free-text laterality/position field.
4. **Mirror the HuBMAP donor / sample / dataset provenance graph** in the LinkML schema. The structure is already PROV-O aligned.
5. **Use ASCT+B-aware cell-type calling** in the scRNA-seq pipeline. Models that emit cell-type predictions should constrain their output vocabulary to the relevant organ's ASCT+B table.
6. **Use OMAP-validated panels** for multiplex imaging where applicable; cite the OMAP ID in the `ProcedureManifest`.
7. **Mirror HuBMAP-style portal browsing** internally: every Cytognosis dataset gets a CCF-aware donor/sample/dataset card that surfaces the spatial registration plus the assay metadata.
8. **Bridge to Vitessce** for in-browser visualization where useful; Vitessce already understands AnnData, OME-Zarr, and CCF coordinates.

## What HRA does not yet give you

- **Disease-state references.** HRA is the *healthy* adult. Disease-state atlases (Tabula Sapiens, HCA, GTEx, disease-specific consortia) extend the framework but are not unified under one CCF yet.
- **Developmental atlases.** HRA covers adult; developing-organism atlases (HuBMAP-D, Allen Brain Atlas developmental, MOSCOT) are parallel efforts.
- **Cross-species references.** HRA is human. Mouse Cell Atlas, MoNA, etc. are separate; cross-species cell-type alignment is open research (CL is the bridge but coverage is uneven).
- **Functional dynamics.** HRA captures structure and steady-state cell types; it does not capture dynamic state transitions, perturbation responses, or longitudinal physiology. Those belong in the assay/observation layer described elsewhere in this survey.

These gaps are noted, not blockers: HRA composes additively. Cytognosis can register healthy-baseline data into HRA and disease/developmental data into HRA-extension subgraphs without changing the base.

## Sources

- [HRA portal humanatlas.io](https://humanatlas.io/), [HRA About](https://humanatlas.io/about), [CCF Ontology](https://humanatlas.io/ccf-ontology)
- [HuBMAP Portal](https://portal.hubmapconsortium.org/), [HuBMAP Consortium](https://hubmapconsortium.org/), [NIH Common Fund HuBMAP](https://commonfund.nih.gov/HuBMAP)
- [HuBMAP HRA construction, Nature Methods 2024](https://www.nature.com/articles/s41592-024-02563-5)
- [HRA Knowledge Graph paper, Sci Data 2025](https://www.nature.com/articles/s41597-025-05183-6)
- [Specimen, biological structure, spatial ontologies, Sci Data 2023](https://www.nature.com/articles/s41597-023-01993-8)
- [ASCT+B, Nature Cell Biology 2021](https://www.nature.com/articles/s41556-021-00788-6), [3D Reference Organs paper, PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10079270/)
- [Tissue registration RUI, Comm Biology 2022](https://www.nature.com/articles/s42003-022-03644-x)
- [Vasculature CCF, Sci Data 2023](https://www.nature.com/articles/s41597-023-02018-0), [HRA-VCCF GitHub](https://github.com/hubmapconsortium/hra-vccf)
- [OMAP, Nature Methods 2023](https://www.nature.com/articles/s41592-023-01846-7), [HRA OMAP](https://humanatlas.io/omap)
- [HuBMAP Portal paper, arXiv 2511.05708](https://arxiv.org/abs/2511.05708)
- [HRA UI source](https://github.com/hubmapconsortium/hra-ui)
