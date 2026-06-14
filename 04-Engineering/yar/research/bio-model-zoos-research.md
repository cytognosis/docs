---
title: "Biological Model Zoos and Registries: Deep Analysis for LEGO Registry Design"
date: "2026-05-25"
source: "migrated from org/plans"
category: "research"
status: "current"
tags:
  - cytognosis
  - research
---

# Biological Model Zoos and Registries: Deep Analysis for LEGO Registry Design

> **Author**: Cytognosis Foundation Research Team
> **Date**: 2026-05-24
> **Status**: Research Document
> **Purpose**: Inform the design of the Cytognosis LEGO Biological Model Registry

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [MONAI Model Zoo](#2-monai-model-zoo)
3. [Kipoi](#3-kipoi)
4. [sfaira](#4-sfaira)
5. [scvi-hub](#5-scvi-hub)
6. [Bioimage.IO](#6-bioimageio)
7. [Comprehensive Comparison](#7-comprehensive-comparison)
8. [Deep Structural Causal Models and Composable Modules](#8-deep-structural-causal-models-and-composable-modules)
9. [LEGO Registry Design Implications](#9-lego-registry-design-implications)
10. [Conclusions and Recommendations](#10-conclusions-and-recommendations)

---

## 1. Executive Summary

This document analyzes five prominent biological model zoos and registries to inform the design of the Cytognosis LEGO Biological Model Registry. Each zoo addresses different aspects of the model sharing challenge in computational biology and biomedical AI. The analysis focuses on nine dimensions: model description format, biological entity typing, input/output schemas, versioning, reproducibility, benchmarking, composability, distribution, and code architecture.

The key finding is that no single existing zoo provides a complete solution for Cytognosis's needs. The optimal LEGO Registry design combines MONAI's bundle structure and configuration system, Bioimage.IO's rigorous tensor typing and preprocessing specification, Kipoi's biological entity awareness, scvi-hub's HuggingFace integration patterns, and sfaira's ontology-driven metadata harmonization. Additionally, the registry must support deep structural causal models with invertible architectures and multi-scale gradient surgery for Pareto-optimal multi-task learning.

### Key Design Principles

| Principle | Source Zoo | LEGO Application |
|---|---|---|
| Bundle structure with config-driven composition | MONAI | `lego.yaml` + `configs/` directory layout |
| Biological entity typing (DNASeq, GenomicRanges) | Kipoi | LinkML BioEntity schemas (protein.yaml, gene.yaml, cell.yaml) |
| Ontology-driven metadata harmonization | sfaira | Cell Ontology, EFO, NCBITaxon via bionty |
| HuggingFace hub integration patterns | scvi-hub | HubModel + HubMetadata for model distribution |
| Rigorous tensor I/O typing with axes semantics | Bioimage.IO | Input/output tensor specs with shape constraints |
| Multi-weight format support | Bioimage.IO | PyTorch, ONNX, TorchScript export |
| Posterior predictive checks for evaluation | scvi-hub | scvi-criticism integration for generative models |
| Standardized pre/postprocessing pipelines | Bioimage.IO | Transform chains in model manifests |

---

## 2. MONAI Model Zoo

### 2.1 Overview

MONAI (Medical Open Network for Artificial Intelligence) provides the most mature bundle-based model sharing format in biomedical AI. The MONAI Model Zoo hosts **39+ pre-trained models** primarily focused on medical imaging tasks (segmentation, classification, generative). The core framework repository has approximately **8.2k GitHub stars** and over **5.5 million downloads**, with adoption by major institutions including Siemens Healthineers, NHS, Mayo Clinic, UCSF, and Cincinnati Children's Hospital. The ecosystem has powered over 3,000 research papers.

### 2.2 Bundle Format

The MONAI Bundle (MB) format is a standardized directory structure:

```
my_model_bundle/
├── configs/
│   ├── metadata.json      # Model metadata, versioning, dependencies
│   ├── inference.yaml     # Inference pipeline configuration
│   ├── train.yaml         # Training pipeline configuration
│   └── common.yaml        # Shared definitions
├── models/
│   ├── model.pt           # PyTorch weights
│   ├── model.ts           # TorchScript (optional)
│   └── model.onnx         # ONNX export (optional)
├── docs/
│   └── README.md
└── LICENSE
```

### 2.3 Metadata Schema (`metadata.json`)

The `metadata.json` file serves as the descriptive core of each bundle:

```json
{
  "schema": "https://github.com/Project-MONAI/MONAI-extra-test-data/releases/download/0.8.1/meta_schema_20240725.json",
  "version": "0.2.7",
  "changelog": {
    "0.2.7": "enhance metadata with improved descriptions"
  },
  "monai_version": "1.4.0",
  "pytorch_version": "2.4.0",
  "name": "Spleen CT Segmentation",
  "task": "Volumetric (3D) segmentation of the spleen from CT image",
  "description": "A UNet-based model for spleen segmentation.",
  "required_packages_version": {
    "nibabel": "3.2.2",
    "numpy": "1.21.0"
  }
}
```

Key metadata fields:
- **Version**: Semantic versioning string (mandatory)
- **Model Information**: `name`, `task`, `description`
- **Compatibility**: `monai_version`, `pytorch_version`, `numpy_version`
- **Schema Validation**: `schema` field pointing to JSON schema URL
- **I/O Definitions**: Input/output tensor shapes and data types
- **Changelog**: Version history

### 2.4 Configuration System

MONAI's configuration system uses special directives for composability:

- **`_target_`**: Specifies the Python class or function to instantiate
- **`@` (Reference)**: References other components defined within the configuration
- **`$` (Expression)**: Evaluates as a Python expression at runtime
- **`%` (Macro)**: Textual replacement for reusable configuration elements

#### Example: Inference Pipeline Configuration

```yaml
# inference.yaml
imports:
  - "$import torch"

# Network definition
network:
  _target_: monai.networks.nets.BasicUNet
  spatial_dims: 3
  in_channels: 1
  out_channels: 2

# Pre-processing transforms
preprocessing:
  _target_: Compose
  transforms:
    - _target_: LoadImaged
      keys: ["image"]
    - _target_: EnsureChannelFirstd
      keys: ["image"]
    - _target_: ScaleIntensityd
      keys: ["image"]

# Post-processing transforms
post_transforms:
  _target_: Compose
  transforms:
    - _target_: Invertd
      keys: ["pred"]
      transform: "@preprocessing"
    - _target_: AsDiscreted
      keys: ["pred"]
      argmax: True
      to_onehot: 2

# Evaluator / Inference Engine
evaluator:
  _target_: monai.engines.SupervisedEvaluator
  device: "$torch.device('cuda' if torch.cuda.is_available() else 'cpu')"
  val_data_loader: "@val_loader"
  network: "@network"
  inferer:
    _target_: monai.inferers.SlidingWindowInferer
    roi_size: [96, 96, 96]
    sw_batch_size: 4
  postprocessing: "@post_transforms"
```

### 2.5 Composability

MONAI achieves composability through:

1. **Modular Configs**: Split configurations (`common.yaml`, `inference.yaml`, `train.yaml`) merged at runtime
2. **Component References**: The `@` directive enables passing instantiated objects between pipeline stages
3. **CLI Overrides**: Parameters overridden at runtime via CLI or Python API
4. **Hybrid Programming**: `ConfigParser` in Python for complex chaining beyond YAML capabilities

```python
from monai.bundle import ConfigParser

config = ConfigParser()
config.read_config("inference.yaml")

# Instantiate and chain models
det_net = config.get_parsed_content("model_detection", instantiate=True)
seg_net = config.get_parsed_content("model_segmentation", instantiate=True)

def run_pipeline(input_data):
    detection = det_net(input_data)
    return seg_net(detection)
```

### 2.6 Strengths and Limitations

**Strengths**:
- Most mature bundle format with strong tooling
- Config-driven composition reduces code duplication
- Excellent clinical adoption and community support
- Built-in support for ONNX export

**Limitations**:
- Medical imaging focused; no biological entity type system
- No standardized benchmarking framework
- No ontology integration for metadata harmonization
- Limited to MONAI's transform ecosystem

---

## 3. Kipoi

### 3.1 Overview

Kipoi was a standardized repository and API for predictive models in genomics. At its peak, it hosted **2,206 models** with approximately **242 GitHub stars**. The project was **archived and sunset in July 2022**, though the Kipoiseq library and webinar series remain active. Despite being archived, Kipoi introduced critical patterns for biological entity typing that remain influential.

### 3.2 Model Specification (`model.yaml` + `dataloader.yaml`)

Kipoi uses a paired YAML specification:

#### `dataloader.yaml`

```yaml
defined_as: kipoiseq.dataloaders.SeqIntervalDl
args:
  intervals_file:
    doc: BED file with genomic intervals
    example: example_files/intervals.bed
  fasta_file:
    doc: Reference FASTA file
    example: example_files/hg38.fa
output_schema:
  inputs:
    name: seq
    shape: (1000, 4)
    special_type: DNASeq       # Biological entity typing
    doc: One-hot encoded DNA sequence
    associated_metadata: ranges
  metadata:
    ranges:
      type: GenomicRanges       # Genomic coordinate metadata
      doc: Genomic intervals (chr, start, end)
```

#### `model.yaml`

```yaml
defined_as: kipoi.model.PyTorchModel
args:
  module_file: model.py
  module_obj: MyModel
  weights:
    url: https://zenodo.org/record/.../model.pt
    md5: abc123...
default_dataloader:
  defined_as: kipoiseq.dataloaders.SeqIntervalDl
  default_args:
    auto_resize_len: 1000
schema:
  inputs:
    name: seq
    shape: (1000, 4)
    special_type: DNASeq
  targets:
    name: binding_prob
    shape: (1,)
    doc: Predicted TF binding probability
```

### 3.3 Biological Entity Typing

Kipoi's most distinctive contribution is its biological entity type system:

- **`DNASeq`** (`special_type`): Flags one-hot encoded DNA sequence inputs
- **`DNAStringSeq`**: String-format DNA sequence inputs
- **`GenomicRanges`**: Metadata type carrying chromosome, start, end coordinates
- **Associated metadata**: Links model inputs to genomic coordinates via `associated_metadata` field

This typing system enables:
1. Automatic variant effect prediction via the `kipoi-veff` plugin
2. In-silico mutagenesis with reference/alternative allele comparison
3. Unified interface across genome-wide and region-specific models
4. Scoring functions: `diff`, `logit`, `logit_ref`, `logit_alt`

### 3.4 Composability

- **Standardized APIs**: Unified data-loader and model interfaces enable pipeline chaining
- **Model Composition**: Framework supports combining models (e.g., splicing models linked to pathogenicity predictors)
- **Python/R APIs**: Custom wrapper scripts chain model outputs as inputs to downstream analyses
- **kipoi-veff**: Plugin architecture for variant effect prediction

### 3.5 Benchmarking

Kipoi implemented systematic benchmarking of variant effect prediction models:
- Publication of benchmarks comparing 2,206 models
- Unified evaluation on standardized variant effect prediction tasks
- Cross-model comparison using shared metrics and datasets

### 3.6 Lessons for LEGO Registry

Kipoi's sunset offers cautionary lessons:
- The field evolved faster than the infrastructure could adapt
- Archived status means no maintenance or security updates
- HuggingFace and other platforms absorbed the model-sharing use case
- **Key takeaway**: The biological entity typing concept is essential but needs modern implementation

---

## 4. sfaira

### 4.1 Overview

sfaira, developed by Theis Lab, provides a unified data zoo and model zoo for single-cell RNA sequencing. The repository has approximately **136 GitHub stars**. While functional, it is being superseded by CZ CELLxGENE Census for large-scale data access. sfaira's primary innovation is ontology-driven metadata harmonization.

### 4.2 Organization

sfaira organizes data loaders by scientific study (DOI):

```
sfaira/
├── data/
│   ├── dataloaders/
│   │   ├── loaders/
│   │   │   ├── d10_1038_s41586_020_2157_4/  # Organized by DOI
│   │   │   │   ├── __init__.py
│   │   │   │   ├── ID.py          # load() function
│   │   │   │   ├── ID.yaml        # Metadata
│   │   │   │   └── ID_*.tsv       # Ontology maps
│   │   │   └── ...
│   └── ...
├── models/
│   ├── embedding/                  # Autoencoder models
│   └── celltype/                   # Cell type classifiers
└── ...
```

### 4.3 Ontology Integration

sfaira's strongest feature is Cell Ontology-based annotation:

- **Cell Ontology (CL)**: Standardized cell type identifiers (e.g., `CL:0000236`)
- **UBERON**: Anatomical tissue identifiers
- **TSV mapping files**: Per-dataset ontology mappings ensure unified vocabulary
- **Automated harmonization**: Different dataset annotations mapped to common ontology terms

This enables:
1. Cross-dataset comparison without manual curation
2. Automated cell type annotation using harmonized labels
3. Consistent metadata across diverse experimental protocols
4. Integration with broader biomedical ontology ecosystems

### 4.4 Model Zoo

- **Architecture**: Autoencoders for embeddings, classifiers for cell type annotation
- **Access**: Single API abstracting model settings; users switch between architectures easily
- **Privacy**: Local execution; no data upload required
- **Interoperability**: Designed for integration with scanpy workflows

### 4.5 Versioning

- **Git-based**: Data loaders versioned through GitHub repository
- **Community contributions**: Pull request workflow for updates and new loaders
- **Reproducibility**: Specific loader versions tracked via Git commits

### 4.6 Context and Future

- Being superseded by **CZ CELLxGENE Discover Census** for large-scale data access (tens of millions of cells)
- Census hosts modern AI models (scGPT, Geneformer, scVI) and integrated datasets
- sfaira's ontology patterns remain valuable even as the platform fades
- **Key takeaway**: Ontology-driven harmonization is essential for any biological model registry

---

## 5. scvi-hub

### 5.1 Overview

scvi-hub is the model sharing submodule within scvi-tools, the most widely-adopted probabilistic framework for single-cell genomics. The `scverse/scvi-tools` repository has approximately **1.6k GitHub stars** and is a core component of the scverse ecosystem. Active development continues with v1.4 released in July 2025, expanding to spatial omics, cytometry, and multi-omics.

### 5.2 Key Components

#### `HubModel`

The core class representing a pre-trained model on HuggingFace Hub:

```python
from scvi.hub import HubModel

# Load a pre-trained model from HuggingFace
hub_model = HubModel.pull_from_huggingface_hub(
    repo_name="scvi-tools/my-scvi-model",
    cache_dir="./models"
)

# Lazy loading - model and data loaded only when accessed
model = hub_model.model       # Loads model weights
adata = hub_model.adata       # Loads associated AnnData

# Push a trained model to HuggingFace
hub_model.push_to_huggingface_hub(
    repo_name="myorg/my-new-model",
    repo_token="hf_...",
    repo_create=True
)
```

#### `HubModelCardHelper`

Auto-generates Model Cards with metadata, training details, and evaluation metrics:

```python
from scvi.hub import HubModelCardHelper

card_helper = HubModelCardHelper(
    model=trained_model,
    model_cls_name="SCVI",
    data_modalities=["rna"],
    tissues=["brain"],
    data_is_annotated=True,
    description="scVI model trained on brain atlas data"
)
model_card = card_helper.generate_model_card()
```

#### `HubMetadata`

Encapsulates required metadata for hub interoperability:
- Model parent module identifier
- Minified data status
- Training data URLs
- AnnData schema information

### 5.3 Benchmarking: scvi-criticism

scvi-criticism provides Posterior Predictive Checks (PPCs) for evaluating generative model fit:

- **Gene-level metrics**: Coefficient of variation, mean expression comparison
- **Cell-level metrics**: Reconstruction quality, zero fraction
- **Differential expression**: Comparison between simulated and observed DE results
- **Calibration error**: Quantile-based calibration assessment

Additional benchmarking via `scib-metrics`:
- Batch correction metrics (silhouette score, kBET, graph connectivity)
- Biological conservation metrics (NMI, ARI, isolated label scores)
- JAX-accelerated computation for large-scale evaluation

### 5.4 Model Registry and Versioning

- **HuggingFace Hub**: Primary distribution channel
- **Minified data**: Models stored with minimal AnnData representation
- **Version alignment**: Documentation and tutorials versioned to match scvi-tools releases
- **Reproducibility**: Model weights + minified data + metadata enables exact reproduction

### 5.5 Key Integration Patterns

The scverse model hub on HuggingFace is the working template for biological model registries:
- HuggingFace repo holds model weights + HubModelCardHelper-generated Model Card
- Link to training AnnData (often a CELLxGENE Census slice)
- Standardized metadata format enabling programmatic discovery
- **Key takeaway**: HuggingFace integration provides battle-tested infrastructure for model distribution

---

## 6. Bioimage.IO

### 6.1 Overview

Bioimage.IO is a community-driven initiative making deep learning models for bioimage analysis FAIR (Findable, Accessible, Interoperable, and Reusable). Supported by a global consortium (AI4Life, Euro-BioImaging), it provides the most rigorous input/output typing system among biological model zoos.

### 6.2 Resource Description File (RDF)

The `bioimageio.yaml` (or `rdf.yaml`) is the central metadata manifest:

```yaml
format_version: 0.5.0
type: model
name: "U-Net Nuclei Segmentation"
description: "2D U-Net for nuclear segmentation in fluorescence microscopy"
authors:
  - name: "Jane Doe"
    affiliation: "Example University"
license: MIT
git_repo: https://github.com/example/nuclei-unet
tags:
  - segmentation
  - nuclei
  - fluorescence

# Input tensor specification
inputs:
  - id: input_image
    description: "Raw fluorescence microscopy image"
    axes: bcyx
    data_type: float32
    shape:
      min: [1, 1, 64, 64]
      step: [0, 0, 16, 16]
    preprocessing:
      - name: zero_mean_unit_variance
        kwargs:
          mode: per_sample
          axes: yx
      - name: scale_range
        kwargs:
          mode: percentiles
          axes: cyx
          min_percentile: 1
          max_percentile: 99.8

# Output tensor specification
outputs:
  - id: segmentation_mask
    description: "Binary segmentation mask"
    axes: bcyx
    data_type: float32
    shape:
      reference_tensor: input_image
      scale: [1, 1, 1, 1]
      offset: [0, 0, 0, 0]
    postprocessing:
      - name: sigmoid
      - name: binarize
        kwargs:
          threshold: 0.5

# Multi-weight support
weights:
  pytorch_state_dict:
    source: ./weights/model.pt
    architecture:
      source: model.py
      callable: UNet
      kwargs:
        in_channels: 1
        out_channels: 1
  onnx:
    source: ./weights/model.onnx
    opset_version: 12
  torchscript:
    source: ./weights/model.ts

# Test data for validation
test_inputs:
  - test_input.npy
test_outputs:
  - test_output.npy
```

### 6.3 Axes and Shape System

The axes system provides explicit tensor semantics:

| Axis | Meaning | Usage |
|---|---|---|
| `b` | Batch | Batch dimension |
| `c` | Channel | Feature channels |
| `x`, `y` | Spatial 2D | Image width/height |
| `z` | Spatial 3D | Depth dimension |
| `t` | Time | Temporal dimension |

Shape specification supports:
- **Fixed shapes**: Absolute integer values
- **Dynamic shapes**: `min` + `step` for variable input sizes (fully convolutional networks)
- **Reference shapes**: Output shape derived from input via `scale` and `offset`

### 6.4 Preprocessing/Postprocessing

Standardized transform pipelines defined declaratively:

**Preprocessing operations**: `binarize`, `clip`, `scale_linear_range`, `sigmoid`, `zero_mean_unit_variance`, `scale_range`, `scale_mean_variance`

**Postprocessing operations**: `binarize`, `clip`, `scale_linear_range`, `sigmoid`, `scale_mean_variance`

These operations are implemented in `bioimageio.core`, ensuring identical processing regardless of consumer software.

### 6.5 Multi-Weight Format Support

Bioimage.IO supports multiple weight formats per model:

| Format | Key | Usage |
|---|---|---|
| PyTorch State Dict | `pytorch_state_dict` | Native PyTorch models |
| TorchScript | `torchscript` | Cross-platform deployment |
| ONNX | `onnx` | Interoperability standard |
| TensorFlow SavedModel | `tensorflow_saved_model_bundle` | TensorFlow ecosystem |
| TensorFlow.js | `tensorflow_js` | Browser-based execution |
| Keras HDF5 | `keras_hdf5` | Legacy Keras models |

Consumer software automatically selects the appropriate format based on its capabilities.

### 6.6 Consumer Software Ecosystem

Models are executable across a wide range of bioimage analysis tools:
- **Fiji/ImageJ** (via deepImageJ plugin)
- **ilastik**
- **ImJoy**
- **QuPath**
- **ZeroCostDL4Mic**
- **Icy**
- **Napari**
- **Galaxy**
- **Leica Aivia** (commercial)

### 6.7 BioEngine

Cloud-powered infrastructure for the Bioimage.IO ecosystem:
- In-browser model testing via the bioimage.io website
- Scalable inference via hypha + Ray/Ray Serve
- HTTP/WebSocket API for software integration
- Deployable across laptops, workstations, and HPC clusters

### 6.8 Key Takeaway

Bioimage.IO provides the gold standard for tensor I/O typing, preprocessing specification, and multi-weight format support. Its declarative approach to defining model interfaces, shape constraints, and transform pipelines is directly applicable to the LEGO Registry design.

---

## 7. Comprehensive Comparison

### 7.1 Overview Table

| Dimension | MONAI | Kipoi | sfaira | scvi-hub | Bioimage.IO |
|---|---|---|---|---|---|
| **Domain** | Medical imaging | Genomics | Single-cell RNA | Single-cell omics | Bioimage analysis |
| **License** | Apache 2.0 | MIT | BSD 3-Clause | BSD 3-Clause | Various (per model) |
| **Language** | Python | Python/R | Python | Python | Python/Java |
| **Framework** | PyTorch/MONAI | Keras/PyTorch/TF | PyTorch | PyTorch/JAX | Multi-framework |
| **Models** | 39+ | 2,206 (archived) | ~20 | Growing (HF Hub) | Growing |
| **GitHub Stars** | ~8.2k (core) | ~242 | ~136 | ~1.6k | ~38 (core) |
| **Status** | Active, production | Archived (July 2022) | Low activity | Very active | Active |
| **Clinical Adoption** | High (Siemens, NHS) | Academic | Academic | Academic | Academic/Industry |

### 7.2 Technical Comparison

| Dimension | MONAI | Kipoi | sfaira | scvi-hub | Bioimage.IO |
|---|---|---|---|---|---|
| **Format** | metadata.json + YAML configs | model.yaml + dataloader.yaml | Python code + YAML | HuggingFace Model Card | bioimageio.yaml (RDF) |
| **Entity Typing** | None (tensor-only) | DNASeq, GenomicRanges | Cell Ontology (CL) | AnnData-native | Tensor axes (bcyx) |
| **I/O Typing** | JSON tensor specs | Shape + special_type | AnnData schema | AnnData + minified data | Axes + shape + preprocessing |
| **Versioning** | Semantic (metadata.json) | Git-based (model repo) | Git-based | HuggingFace versioning | Semantic (format_version) |
| **Reproducibility** | Bundle self-contained | Docker + conda environments | Git commits | Minified data + weights | Test inputs/outputs |
| **Benchmarking** | None standardized | kipoi-veff (VEP) | None standardized | scvi-criticism PPCs | Test validation |
| **Composability** | ConfigParser + @ references | kipoi-veff plugin | Limited | scverse ecosystem | BioEngine |
| **Distribution** | MONAI CLI + GitHub | pip install + kipoi CLI | pip install | HuggingFace Hub | bioimage.io website |
| **ONNX Support** | Yes (export) | No | No | No | Yes (multi-weight) |
| **Ontology** | None | None | Cell Ontology, UBERON | bionty (via scverse) | None |

### 7.3 Best-in-Class Features

| Feature | Best Zoo | Why |
|---|---|---|
| Bundle/package structure | MONAI | Most mature, config-driven, CLI tooling |
| Biological entity typing | Kipoi | DNASeq, GenomicRanges — explicit bio-awareness |
| Ontology integration | sfaira | Cell Ontology maps, harmonized annotations |
| Hub integration | scvi-hub | HuggingFace patterns, Model Cards, minified data |
| Tensor I/O specification | Bioimage.IO | Axes semantics, shape constraints, pre/postprocessing |
| Multi-weight formats | Bioimage.IO | PyTorch, ONNX, TF, TorchScript in one manifest |
| Cross-software interop | Bioimage.IO | 10+ consumer applications |
| Generative model evaluation | scvi-hub | scvi-criticism PPCs, scib-metrics |
| Config composability | MONAI | `_target_`, `@`, `$` directive system |
| Community/adoption | MONAI | 8.2k stars, 5.5M downloads, clinical use |

---

## 8. Deep Structural Causal Models and Composable Modules

### 8.1 Pearl's Three-Step Counterfactual Procedure

Deep Structural Causal Models (DSCMs) implement Judea Pearl's three-step procedure for counterfactual reasoning, operating at the highest level of the "Ladder of Causation":

1. **Abduction (Updating)**: Use observed evidence ($X=x, Y=y$) to update the probability distribution of exogenous (unobserved) noise variables $U$. This step "explains" the past by identifying background conditions that led to observed outcomes.

2. **Action (Intervention)**: Modify the SCM by replacing the structural equation for $X$ with the intervention $do(X=x^*)$. This creates a "mutilated" model representing the hypothetical world.

3. **Prediction (Projection)**: Use the updated distribution of $U$ and the modified SCM to predict the outcome $Y$ in the counterfactual world.

### 8.2 Normalizing Flows in DSCMs

Normalizing Flows (NFs) are the preferred architecture for DSCMs due to their invertibility:

- **Invertibility for Causality**: The bijection provided by NFs enables exact mapping between observed data ($X$) and exogenous noise variables ($Z$), crucial for the abduction step
- **Tractable Abduction**: If structural mechanisms are modeled as invertible functions, noise inference is efficient via the inverse of the flow network
- **Composable Modules**: NFs are compositions of simpler invertible functions that can mirror the causal graph, where each layer/module corresponds to a causal mechanism
- **Tractable Likelihood**: NFs provide exact density evaluation via the change of variables formula

### 8.3 Continuous Normalizing Flows in Single-Cell Biology

CNFs and Flow Matching have emerged as powerful tools for single-cell data:

- **cellFlow and CFGen**: Use flow-based architectures to model raw single-cell count data directly, avoiding biases from standard normalization
- **Trajectory Inference**: CNFs model continuous cell state transformations over time for developmental/differentiation processes
- **Counterfactual Prediction**: PO-Flow framework uses CNFs for causal inference, jointly modeling potential outcome distributions and factual-conditioned counterfactuals
- **Causally Consistent Normalizing Flows (CCNF)**: Maintain consistency between the generative model and the specified causal graph

### 8.4 Gradient Surgery for Multi-Task Learning

When training multi-scale biological models with multiple objectives, gradient interference is a central challenge:

#### PCGrad (Projecting Conflicting Gradients)

PCGrad addresses gradient conflicts by projecting each task's gradient onto the normal plane of conflicting tasks' gradients. When two task gradients have negative cosine similarity (conflict), the conflicting component is removed:

$$g_i' = g_i - \frac{g_i \cdot g_j}{\|g_j\|^2} g_j \quad \text{if } g_i \cdot g_j < 0$$

#### CAGrad (Conflict-Averse Gradient)

CAGrad finds the gradient direction that maximizes the minimum improvement across all tasks, providing stronger theoretical guarantees:

$$\min_d \max_i \langle d, g_i \rangle \quad \text{s.t.} \quad \|d\| \leq 1$$

#### GradNorm

GradNorm normalizes gradient magnitudes across tasks by:
- Rescaling gradient norms to a target based on relative training rates
- Ensuring no single scale dominates model updates
- Dynamic task weighting via gradient magnitude balancing

#### Dynamic Weight Averaging (DWA)

DWA adjusts task weights based on training progress:
- Monitors relative loss decrease rates per task
- Increases weight for tasks falling behind
- Temperature parameter controls adaptation speed

### 8.5 Pareto-Optimal Multi-Task Learning

When tasks conflict, no single "best" solution exists. Instead, the goal is to find Pareto-optimal solutions:

- **Pareto Front**: The set of solutions where no objective can be improved without degrading another
- **Multiple Gradient Descent Algorithm (MGDA)**: Finds the minimum-norm element in the convex hull of task gradients
- **Multi-Objective Bayesian Optimization**: Explores the Pareto front efficiently using Bayesian surrogates
- **Application to Biology**: Multi-scale models spanning molecular interactions, cellular behavior, and tissue dynamics benefit from Pareto-optimal balancing

### 8.6 Implications for LEGO

The LEGO system's `TaskManager` with detached evaluation heads maps directly to these concepts:

- **TaskManager**: Multi-objective orchestration with uncertainty weighting (Kendall) as default
- **Detached heads**: Enable independent evaluation without gradient interference
- **Hierarchical optimization**: Grid search over scientific hyperparameters × Bayesian optimization over nuisance parameters
- **Gradient surgery integration**: PCGrad/CAGrad can be applied within the `HierarchicalOptimizer`

---

## 9. LEGO Registry Design Implications

### 9.1 Existing Cytognosis LEGO Architecture

The Cytognosis codebase already contains foundational LEGO components:

#### 4-Layer Architecture

```
┌──────────────────────────────────────────────────────────┐
│  ⚡ EXECUTORS                                            │
│  ExperimentConfig → CytoverseExecutor                    │
│  Hydra configs, hierarchical hyperopt, redun DAGs        │
├──────────────────────────────────────────────────────────┤
│  📊 EVALUATION                                           │
│  TaskManager with detached heads                         │
│  scib-metrics (JAX-accelerated)                          │
│  Grassmannian/intrinsic metrics                          │
├──────────────────────────────────────────────────────────┤
│  🏗️ MODELS                                               │
│  LEGOModel.compile() + LEGOFactory                       │
│  scvi BaseModuleClass integration                        │
│  Pretrained encoder wrapping (ESM, ChemBERTA)            │
├──────────────────────────────────────────────────────────┤
│  🧩 MODULES                                              │
│  LEGOPiece + BioRegistry + FeatureAdaptor                │
│  Transformer attention (flex_attention)                   │
│  Flow/Diffusion backends (zuko, TorchCFM, TorchDiff)     │
│  GNN (UnifiedConv)                                       │
├──────────────────────────────────────────────────────────┤
│  💾 DATA                                                  │
│  InteractomeDataset (HeteroData-first)                   │
│  SOMAExperiment, LazyAnnData, IdMapper                   │
│  scDataLoader (LaminDB/Census)                           │
└──────────────────────────────────────────────────────────┘
```

#### Key LEGO Patterns

| Pattern | Implementation | Purpose |
|---|---|---|
| `LEGOPiece` | `nn.Module` + `FeatureInfo` (entity_type, identifier_type, dimension) + frozen/detached flags | Core composable unit |
| `BioRegistry` | Extended with CL, EFO, NCBITaxon via bionty | Entity ID management |
| `FeatureAdaptor` | Dimension alignment between pieces | Glue layer |
| `TaskManager` | Multi-objective orchestration | Multi-task handling |
| `LEGOModel.compile()` | Validates bio-entity compatibility, creates adaptors, initializes lazy modules | Assembly validation |
| `LEGOFactory` | Creates model instances from configuration | Factory pattern |
| `HierarchicalOptimizer` | Grid(scientific) × Bayesian(nuisance) | Hyperparameter search |

#### Existing LinkML Schemas

The codebase already has LinkML schemas for biological entities:

**`biomodeling.yaml`** (root schema):
```yaml
id: https://cytognosis.org/schemas/bio/biomodeling
name: cytognosis_biomodeling
description: |
  Root LinkML schema for the Cytognosis biological "Lego Piece" framework.
  Skills declare their inputs and outputs against the entity classes defined
  in this schema (and its imports). The Model Compiler validates wiring at
  compile time.
imports:
  - linkml:types
  - protein
  - gene
  - cell
classes:
  BioEntity:
    description: |
      Abstract root for every "Lego Piece" the Model Compiler can route
      between skills.
    abstract: true
    slots: [id, source, provenance]
```

**Supporting schemas**: `protein.yaml` (ProteinSequence, Protein with UniProt cross-refs), `gene.yaml` (Gene, Transcript with Ensembl/HGNC IDs), `cell.yaml` (Cell, CellType with CL IDs, Tissue with UBERON IDs).

### 9.2 Proposed `lego.yaml` Model Manifest

Combining best elements from all five zoos:

```yaml
# lego.yaml — Cytognosis LEGO Model Manifest
format_version: "1.0.0"
type: lego_model

# ── Metadata (from MONAI) ──
name: "CellType Classifier v2"
description: "Cell type annotation model for scRNA-seq data"
version: "0.3.1"
authors:
  - name: "Cytognosis Foundation"
    orcid: "0000-0000-0000-0000"
license: Apache-2.0
tags: [single-cell, cell-type, annotation, scRNA-seq]
changelog:
  "0.3.1": "Improved rare cell type recall"
  "0.3.0": "Added ontology-aware loss function"

# ── Biological Entity Typing (from Kipoi + LinkML) ──
bio_entities:
  input_entities:
    - type: bio:Gene
      schema: https://cytognosis.org/schemas/bio/gene
      identifier_type: ensembl_id
      required_fields: [ensembl_id, hgnc_symbol]
    - type: bio:Cell
      schema: https://cytognosis.org/schemas/bio/cell
      identifier_type: barcode
  output_entities:
    - type: bio:CellType
      schema: https://cytognosis.org/schemas/bio/cell
      identifier_type: cl_id
      ontology: CL  # Cell Ontology

# ── Tensor I/O Specification (from Bioimage.IO) ──
inputs:
  - id: expression_matrix
    description: "Gene expression count matrix"
    axes: "cells x genes"
    data_type: float32
    shape:
      min: [1, 2000]
      step: [1, 0]
    preprocessing:
      - name: log1p_normalize
        kwargs:
          target_sum: 10000
      - name: highly_variable_genes
        kwargs:
          n_top_genes: 2000
          flavor: seurat_v3

  - id: gene_ids
    description: "Ensembl gene identifiers"
    axes: "genes"
    data_type: string
    shape: [2000]

outputs:
  - id: cell_type_probabilities
    description: "Cell type classification probabilities"
    axes: "cells x cell_types"
    data_type: float32
    shape:
      reference_tensor: expression_matrix
      scale: [1, null]
    postprocessing:
      - name: softmax
        kwargs:
          axis: -1
      - name: argmax_to_ontology
        kwargs:
          ontology: CL
          mapping_file: celltype_mapping.tsv

# ── Ontology Metadata (from sfaira) ──
ontology_metadata:
  organism: NCBITaxon:9606        # Homo sapiens
  assay: EFO:0009922              # 10x 3' v3
  tissue: UBERON:0000955          # brain
  cell_ontology_version: "2024-01-01"

# ── LEGO Piece Specification ──
lego_piece:
  module_class: cytoverse.modules.CellTypeClassifier
  feature_info:
    entity_type: Cell
    identifier_type: barcode
    input_dimension: 2000
    output_dimension: 50
  frozen: false
  detached_eval: true  # Evaluation head is detached from gradient flow

# ── Model Weights (from Bioimage.IO multi-weight) ──
weights:
  pytorch_state_dict:
    source: ./weights/model.pt
    pytorch_version: "2.4.0"
    architecture:
      source: model.py
      callable: CellTypeClassifier
  onnx:
    source: ./weights/model.onnx
    opset_version: 17

# ── Dependencies ──
dependencies:
  python: ">=3.10"
  packages:
    cytoverse: ">=0.1.0"
    torch: ">=2.0"
    anndata: ">=0.9"
    scanpy: ">=1.9"

# ── Benchmarking (from scvi-criticism) ──
benchmarks:
  posterior_predictive_checks:
    metrics: [gene_cv, cell_cv, de_correlation, calibration]
  integration_metrics:
    suite: scib-metrics
    metrics: [silhouette_batch, nmi, ari, isolated_label_f1]
  custom_metrics:
    - name: grassmannian_distance
      module: cytoverse.evaluation.grassmannian
  test_data:
    inputs: test_expression.h5ad
    expected_outputs: test_celltypes.csv

# ── Provenance (RO-Crate wrapping MLflow) ──
provenance:
  ro_crate_profile: "https://w3id.org/ro/wfrun/workflow/1.0"
  mlflow:
    tracking_uri: "https://mlflow.cytognosis.org"
    experiment_id: "cell-type-annotation-v2"
    run_id: "abc123def456"
  training_data:
    source: "CZ CELLxGENE Census 2024-01-01"
    slice_query: "tissue == 'brain' and assay == '10x 3p v3'"
    n_cells: 1_500_000
    n_genes: 33_000
```

### 9.3 Multi-Scale Model Handling

For models operating across biological scales (molecular → cellular → tissue):

```yaml
# Multi-scale LEGO configuration
multi_scale:
  strategy: pareto_optimal
  gradient_surgery: pcgrad  # or cagrad, gradnorm, dwa
  scales:
    - name: molecular
      lego_piece: GeneExpressionEncoder
      loss_weight: auto  # GradNorm-managed
    - name: cellular
      lego_piece: CellStateClassifier
      loss_weight: auto
    - name: tissue
      lego_piece: TissueCompositionPredictor
      loss_weight: auto
  pareto:
    algorithm: mgda  # Multiple Gradient Descent Algorithm
    n_solutions: 5   # Points on Pareto front
```

### 9.4 ONNX Integration

Standard export pathway for cross-platform interoperability:

```python
import torch

# Export LEGO model to ONNX
model = LEGOModel.from_yaml("lego.yaml")
model.eval()

dummy_input = torch.randn(1, 2000)  # batch_size x n_genes
torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    opset_version=17,
    input_names=["expression_matrix"],
    output_names=["cell_type_probabilities"],
    dynamic_axes={
        "expression_matrix": {0: "batch_size"},
        "cell_type_probabilities": {0: "batch_size"}
    }
)
```

### 9.5 RO-Crate Provenance

Wrapping MLflow run metadata in Research Object Crates for FAIR compliance:

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "CellType Classifier v2 Training Run",
      "conformsTo": {"@id": "https://w3id.org/ro/wfrun/workflow/1.0"}
    },
    {
      "@id": "mlflow://mlflow.cytognosis.org/experiments/cell-type-annotation-v2/runs/abc123def456",
      "@type": "CreateAction",
      "instrument": {"@id": "lego.yaml"},
      "object": [
        {"@id": "weights/model.pt"},
        {"@id": "weights/model.onnx"}
      ],
      "result": {
        "metrics": {
          "nmi": 0.92,
          "ari": 0.88,
          "silhouette_batch": 0.85,
          "calibration_error": 0.03
        }
      }
    }
  ]
}
```

### 9.6 HuggingFace Distribution

Following scvi-hub patterns for model distribution:

```python
from cytoverse.hub import LEGOHubModel

# Push to HuggingFace
hub_model = LEGOHubModel(
    lego_yaml="lego.yaml",
    weights_dir="./weights",
    test_data="test_expression.h5ad"
)
hub_model.push_to_hub(
    repo_id="cytognosis/celltype-classifier-v2",
    commit_message="v0.3.1: Improved rare cell type recall"
)

# Pull from HuggingFace
model = LEGOHubModel.from_hub("cytognosis/celltype-classifier-v2")
predictions = model.predict(adata)
```

---

## 10. Conclusions and Recommendations

### 10.1 Key Findings

1. **No single zoo is sufficient**: Each addresses different aspects of the model sharing challenge. The LEGO Registry must synthesize best-in-class features from all five.

2. **Biological entity typing is essential but underserved**: Only Kipoi (archived) and sfaira (low activity) address biological semantics. The LEGO Registry fills a critical gap with LinkML-based entity schemas.

3. **HuggingFace is the distribution standard**: scvi-hub demonstrates that HuggingFace Hub provides battle-tested infrastructure for biological model distribution.

4. **Tensor typing matters**: Bioimage.IO's axes/shape/preprocessing system prevents integration errors and enables cross-software interoperability.

5. **Causal models require special support**: DSCMs with normalizing flows need invertibility guarantees, gradient surgery support, and Pareto-optimal multi-task orchestration.

### 10.2 Priority-Ordered Implementation Plan

| Priority | Component | Source | Effort |
|---|---|---|---|
| P0 | `lego.yaml` manifest format | MONAI + Bioimage.IO | 2 weeks |
| P0 | LinkML bio-entity typing in manifests | Kipoi + existing schemas | 1 week |
| P1 | `LEGOHubModel` for HuggingFace | scvi-hub patterns | 2 weeks |
| P1 | Ontology metadata in manifests | sfaira patterns + bionty | 1 week |
| P1 | Tensor I/O specification | Bioimage.IO axes system | 1 week |
| P2 | ONNX export pipeline | MONAI + Bioimage.IO | 1 week |
| P2 | scvi-criticism PPC integration | scvi-hub | 1 week |
| P2 | Multi-weight format support | Bioimage.IO | 1 week |
| P3 | RO-Crate provenance wrapping | RO-Crate + MLflow | 2 weeks |
| P3 | Gradient surgery (PCGrad/CAGrad) | Literature | 2 weeks |
| P3 | Pareto-optimal multi-task config | Literature | 1 week |
| P4 | CLI tools (validate, export, publish) | MONAI CLI patterns | 2 weeks |
| P4 | BioEngine-style cloud inference | Bioimage.IO | 3 weeks |

### 10.3 Architecture Mapping

```
Existing LEGO Layer          → Registry Extension
─────────────────────────────────────────────────
Data Layer (LazyAnnData)     → lego.yaml input specs + ontology metadata
Modules Layer (LEGOPiece)    → lego.yaml lego_piece section + bio_entities
Models Layer (LEGOModel)     → lego.yaml weights + dependencies + multi_scale
Evaluation Layer (TaskMgr)   → lego.yaml benchmarks + PPC integration
Executors Layer (Executor)   → lego.yaml provenance + HuggingFace distribution
```

### 10.4 Open Questions

1. **Schema evolution**: How to handle breaking changes in `lego.yaml` format across versions?
2. **Private models**: Should the registry support private/internal models alongside public HuggingFace distribution?
3. **Model composition**: How to specify LEGO model graphs (encoder → backbone → task heads) in YAML without losing the power of `compile()`?
4. **Validation**: Should `lego.yaml` validation be a pre-commit hook, CI step, or both?
5. **Backward compatibility**: How to wrap existing scvi-tools models in `lego.yaml` format?

---

*This document synthesizes research from MONAI Model Zoo, Kipoi, sfaira, scvi-hub, Bioimage.IO, and the deep structural causal model literature to inform the Cytognosis LEGO Biological Model Registry design. All code examples are illustrative and subject to refinement during implementation.*
