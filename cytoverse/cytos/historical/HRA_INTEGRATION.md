# Human Reference Atlas (HRA) Integration

> Last updated: 2026-05-12 | HRA version: v2.4 | Graph: **Ontology Graph**

## Overview

The Human Reference Atlas (HRA) is a first-class component of the **Ontology Graph**. It provides the spatial scaffold that maps every measurement, sensor reading, and assay output to a precise anatomical location in the human body.

> [!IMPORTANT]
> HRA is the "GPS coordinate system" for the body. The Sensor Triple (Assay × Location × Schema) uses HRA/UBERON for the Location dimension, making every Cytoscope measurement anatomically grounded.

## What Was Integrated

### Data Sources

| Source | Format | Location | Size |
|--------|--------|----------|------|
| CCF Ontology (ccf.owl) | OWL/RDF-XML | `datasets/01-ontologies/owl/ccf.owl` | 43 MB |
| HRA-KG repo | Git (shallow) | `cytos/third_party/hra-kg/` | Reference |
| HRA-VCCF repo | Git (shallow) | `cytos/third_party/hra-vccf/` | Vascular data |
| LOD endpoint | JSON-LD | `https://lod.humanatlas.io` | 13 object types |

### KG Contribution (Ontology Graph)

| Metric | Count |
|--------|-------|
| **Total HRA nodes** | **9,493** |
| Anatomical structures (AS) | 4,496 |
| Cell types (CT) | 1,195 |
| Biomarker genes (BM/gene) | 1,865 |
| Biomarker proteins (BM/protein) | 199 |
| Biomarker chemicals (BM/lipid+metabolite) | 20 |
| 3D reference organs (RO) | 1,713 |
| **Total HRA edges** | **26,444** |
| `ccf_located_in` (cell → structure) | 13,904 |
| `subClassOf` (ontological hierarchy) | 7,451 |
| `ccf_part_of` (anatomical hierarchy) | 5,089 |
| **Spatial placements** | **3,481** |

## Role in Three Constituent Graphs

### Ontology Graph (Primary Home)

HRA entities ARE definitional: they describe anatomical structures, cell type locations, and spatial coordinates that exist independent of any measurement. All HRA nodes and edges live in the Ontology Graph.

```
Ontology Graph
├── UBERON (anatomy)  ←→  HRA ASCT+B (extended anatomy)
├── CL (cell types)   ←→  HRA cell types (ccf_located_in)
├── HGNC (genes)      ←→  HRA biomarkers (ccf_characterizes)
└── CCF 3D (spatial)  ←→  HRA reference organs (meshes + coordinates)
```

### Sensor Triple Integration

Every measurement device in Cytoscope maps to an HRA location:

| Sensor Scale | HRA Mapping | Resolution |
|-------------|-------------|-----------|
| **Molecular** (sequencer) | Tissue biopsy site → `UBERON:*` | Organ/tissue level |
| **Cellular** (scRNA-seq) | Cell type → `CL:*` → `ccf_located_in` → `UBERON:*` | Cell type in tissue |
| **Cellular** (spatial transcriptomics) | Cell → `ccf:SpatialPlacement` (x,y,z coordinates) | Micron-level in 3D organ |
| **Connectomic** (fMRI) | Voxel → MNI coordinates → `UBERON:*` brain region | Brain atlas crosswalk |
| **Connectomic** (EEG) | Channel → 10-20 system → scalp region | Surface mapping |
| **Clinical** (blood draw) | Venipuncture site → `UBERON:0000178` (blood) | Fluid |
| **Physiological** (CGM) | Sensor placement → `UBERON:*` subcutaneous tissue | Body site |
| **Physiological** (PPG) | Wrist → `UBERON:0004088` | Specific anatomy |

### Observation Graph Links

HRA provides the anatomical anchor for observed associations:

```
Gene (Ontology Graph) ──expressed_in──→ Cell (Ontology Graph) ──ccf_located_in──→ Structure (Ontology Graph)
         ↑                                                                              ↑
         │                                                                              │
  gene_associated_with_condition (Observation Graph)               sensor_measures_at (Catalog Graph)
         │                                                                              │
         ↓                                                                              ↓
Disease (Ontology Graph)                                          Sensor (Catalog Graph)
```

### Catalog Graph Links

Dataset and Sensor nodes in the Catalog Graph reference HRA locations:

```yaml
# Example: scRNA-seq dataset with HRA anchor
Dataset:
  id: CXG:283d65eb
  name: "Human Brain Cell Atlas"
  uses_assay: EFO:0010183           # scRNA-seq
  samples_tissue: UBERON:0000955     # brain (HRA anatomical structure)
  hra_registration: true             # registered with HRA RUI
  spatial_placement:                 # if tissue block was registered
    x: 12.5
    y: 8.3
    z: 5.1
    rotation: [0, 0, 0]
    reference_organ: ccf:VHFBrain    # HRA 3D brain mesh
```

## Spatial Data Schema

### SpatialPlacement (3,481 entries in Parquet)

```yaml
SpatialPlacement:
  source: ccf:SpatialPlacement
  fields:
    placement_for: ccf:SpatialEntity   # Reference organ
    x_translation: float               # mm from origin
    y_translation: float
    z_translation: float
    x_rotation: float                  # degrees
    y_rotation: float
    z_rotation: float
    x_scaling: float                   # scale factors
    y_scaling: float
    z_scaling: float
    dimension_units: "millimeter"
    rotation_units: "degree"
    reference_organ: ccf:*             # Which 3D mesh
```

### SpatialEntity (1,713 reference organs)

```yaml
SpatialEntity:
  source: ccf:SpatialEntity
  fields:
    id: ccf:VHFBrain
    label: "3D Reference Brain (Female)"
    x_dimension: 160.0                 # mm
    y_dimension: 200.0
    z_dimension: 155.0
    organ: UBERON:0000955              # Link to UBERON
    sex: female
    representation_of: UBERON:0000955
    object_file: "VH_F_Brain.glb"      # 3D mesh file
```

## ASCT+B Coverage (41 Organs)

The CCF Ontology contains ASCT+B tables for:

```
allen-brain, anatomical-systems, blood-pelvis, blood-vasculature,
bone-marrow, eye, fallopian-tube, heart, kidney, knee,
large-intestine, liver, lung, lymph-node, lymph-vasculature,
main-bronchus, mouth, muscular-system, ovary, palatine-tonsil,
pancreas, peripheral-nervous-system, placenta, prostate, skeleton,
skin, small-intestine, spinal-cord, spleen, thymus, trachea,
ureter, urinary-bladder, uterus
+ crosswalk tables (pathway, musculoskeletal, lymph-vasculature, PNS)
```

## Cross-Modal Queries Enabled

With HRA in the Ontology Graph, the KG supports queries like:

```cypher
// What cell types are in the lower lobe of the left lung?
MATCH (ct:Cell)-[:ccf_located_in]->(as:AnatomicalEntity)
WHERE as.name CONTAINS 'lower lobe' AND as.name CONTAINS 'lung'
RETURN ct.name, ct.id

// What genes characterize hepatocytes?
MATCH (bm:Gene)-[:ccf_characterizes]->(ct:Cell {name: 'hepatocyte'})
RETURN bm.name, bm.id

// What sensors measure from the brain?
MATCH (s:Sensor)-[:measures_at]->(loc:AnatomicalEntity)
WHERE loc.id STARTS WITH 'UBERON:' 
  AND (loc)-[:ccf_part_of*]->(:AnatomicalEntity {id: 'UBERON:0000955'})
RETURN s.name, loc.name
```

## Next Steps

### Immediate (Phase D10 in Execution Plan)

- [ ] Update `hra.yaml` schema with SpatialPlacement coordinate fields
- [ ] Download per-organ ASCT+B JSON-LD tables from LOD for richer biomarker associations
- [ ] Parse OMAP antibody panels and add to KG
- [ ] Parse VCCF vascular geometry data
- [x] Cross-ontology SSSOM mappings available via Monarch SSSOM layer (1.26M edges)

### Medium Term

- [ ] Build SOSA `FeatureOfInterest` → CCF coordinate resolver
- [ ] Add `ccf_rui_location` slots to LinkML `SampleManifest`
- [ ] Bridge to Vitessce for in-browser 3D visualization
- [ ] Integrate HuBMAP experimental datasets via HRA-KG API

### Long Term

- [ ] Disease-state extensions (map pathological findings to HRA scaffold)
- [ ] Patient-specific CCF (co-register patient imaging with HRA)
- [ ] Cross-species alignment (mouse atlases via CL/UBERON crosswalks)
