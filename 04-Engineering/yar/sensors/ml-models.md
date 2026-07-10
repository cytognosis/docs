# Models: Schemas, Frameworks, and Ontologies

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Scope: how to describe a trained model so that another system can validate inputs, predict outputs, understand its effect, and decide whether to use it. Five sub-questions, each with its own contenders.

1. How is the input/output shape and dtype declared?
2. How is the *identity and ordering* of input/output features (genes, cells, tissues, etc.) declared?
3. How is the *type of model* (encoder, generator, classifier, density estimator) declared?
4. How are *distributional outputs* (variational/probabilistic models) declared and used?
5. How is the model packaged with its training data and provenance for FAIR sharing?

## 1. Tensor IO contracts (shape, dtype, ranges)

### ONNX

The Open Neural Network Exchange is a runtime exchange format. Its `ModelProto` IR has a `value_info` section that types every input, output, and named intermediate as a tensor, sparse tensor, sequence, map, or optional, each with a fixed type and shape. Free-text `metadata_props` (key-value, reverse-DNS prefixed) carry anything the IR cannot. Specific tensor categories can be tagged via Type Denotation (e.g., `IMAGE`), which then triggers consumer behavior.

Strengths:
- Mature, multi-runtime (ONNX Runtime, OpenVINO, TensorRT, CoreML).
- Graph and IO schema are co-located.
- Supports sequences and maps for non-tensor outputs.

Limitations:
- No native concept of "feature ontology" or "unit". You must encode it in `metadata_props` strings or a custom domain.
- No native distribution type. A VAE encoder typically exports `mu` and `logvar` as separate float tensors, leaving the consumer to know they parameterize a Gaussian.
- Quantitative ranges and value semantics are not part of the IR.

[ONNX IR spec](https://onnx.ai/onnx/repo-docs/IR.html), [MetadataProps](https://github.com/onnx/onnx/blob/main/docs/MetadataProps.md), [ONNX Concepts](https://onnx.ai/onnx/intro/concepts.html).

### MLflow Model Signature

An MLflow signature has three parts: `inputs`, `outputs`, `params`, each either a list of `ColSpec` (named, typed, optionally nested Array/Object/Map) or `TensorSpec` (named, numpy dtype, shape). It lives in the `MLmodel` file alongside the model artifact. The `params` schema is for inference-time knobs like `temperature`, `n_samples`, threshold cutoffs.

Strengths:
- More expressive than ONNX for tabular/structured outputs.
- Native nesting (`Array`, `Object`, `Map`, `AnyType`).
- The `params` schema is the right slot for "draw N samples from the variational posterior" or "return mean vs. samples".
- Tied to a tracking server, registry, and deployment endpoints.

Limitations:
- Same gap on feature ontology and units.
- Distribution semantics still implicit.

[MLflow signatures](https://mlflow.org/docs/latest/ml/model/signatures/), [signature.py](https://github.com/mlflow/mlflow/blob/master/mlflow/models/signature.py).

### Apache Arrow / Parquet schema

For non-tensor data (variant calls, EHR rows, observation streams), the Arrow schema is the de facto wire format. Field-level metadata is a `Map<String, String>`, supports nullability, dictionary/categorical types, and timestamp types with timezone. Parquet inherits this.

Strengths: language-independent, columnar, zero-copy, dominant in modern data infra.
Limitations: not a model contract on its own; pair with MLflow ColSpec.

[Arrow Columnar Format](https://arrow.apache.org/docs/format/Columnar.html).

### JSON Schema and DLPack

JSON Schema is fine for simple HTTP-served models (pydantic + FastAPI), and DLPack covers in-process tensor handoff between PyTorch / JAX / TensorFlow / CuPy. Neither is sufficient as a full model contract.

### Recommendation

Use **MLflow signatures as the canonical authored contract**, **export to ONNX for runtime portability**, and treat Arrow as the bulk-data interchange when the model serves over a streaming endpoint. The contract is authored once in MLflow, which writes the `MLmodel` file; the ONNX export inherits shapes and dtypes; and a HuggingFace Model Card (next section) is generated from the same source.

## 2. Feature identity, ordering, and ontology

The hardest IO problem is not "shape (1, 19318)"; it is "which gene is at position 0, in which annotation version, and what identifier scheme". This is where ontologies do the work.

### Ontologies for biological feature identity

| Ontology | Use | Example identifier |
|---|---|---|
| **Ensembl IDs** | The de facto canonical for gene-axis features in scRNA-seq | `ENSG00000141510` (TP53) |
| **NCBI Entrez Gene** | Older but still common | `7157` |
| **HGNC** | Approved gene symbols | `HGNC:11998` |
| **Sequence Ontology (SO)** | Genomic feature classes (promoter, UTR, exon, variant types) | `SO:0000167` (promoter) |
| **EDAM** | Generic data-type tags for "this axis is a Gene ID" | `data:2295` (gene ID), `data:2810` (Ensembl gene ID) |
| **Cell Ontology (CL)** | Cell types | `CL:0000236` (B cell) |
| **UBERON** | Anatomical entities and tissues | `UBERON:0002107` (liver) |
| **NCBITaxon** | Species | `NCBITaxon:9606` (human) |
| **ChEBI** | Chemical entities and metabolites | `CHEBI:15903` (glucose) |
| **EFO** | Experimental factors; integrates UBERON, ChEBI, CL | `EFO:0009655` |
| **MONDO** | Disease ontology | `MONDO:0007254` (breast cancer) |
| **HPO** | Human phenotypes | `HP:0001250` (seizure) |

The [single-cell-curation 7.x schema](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html) (CZ CELLxGENE) is the working reference for "how to use these together in an AnnData": it requires `cell_type_ontology_term_id` (CL), `tissue_ontology_term_id` (UBERON), `assay_ontology_term_id` (EFO/OBI), `disease_ontology_term_id` (MONDO), `organism_ontology_term_id` (NCBITaxon), and pins gene IDs to specific Ensembl/GENCODE versions per species.

### Bioregistry and CURIEs

[Bioregistry](https://bioregistry.io) is the metaregistry. It normalizes prefixes across MIRIAM, OBO, identifiers.org, and provider variants, so `chebi:138488` resolves consistently. For a Cytognosis model card, every feature ID and metadata term should be expressed as a Bioregistry-validated CURIE.

### What to put in the model card

The minimum a model card must declare for the gene axis:
- Identifier scheme (`ensembl.gene` CURIE prefix per Bioregistry)
- Annotation version (`Ensembl 111`, `GENCODE v45`)
- Canonical ordering (a content-addressed manifest, e.g., a SHA256 of the sorted ID list, exposed as a side-channel artifact)
- Species (`NCBITaxon:9606`)
- The intersection rule when input data is missing genes (drop, zero-impute, or mean-impute, depending on the model's training distribution)

This is the missing piece from ONNX and MLflow, and it is where Croissant's ML semantics layer plus a LinkML-backed profile fills the gap.

### Croissant for ML datasets and (extended) for models

[Croissant](https://docs.mlcommons.org/croissant/) is MLCommons' JSON-LD metadata format. It builds on schema.org and adds an "ML semantics" layer that names the role of each field (input, label, weight) and the dataset's intended task. Croissant 1.1 in development adds provenance/lineage/versioning. There is a life-sciences extension. Critically, Croissant is the bridge between dataset cards and model cards: a model card can cite a Croissant dataset and a Croissant dataset can carry the canonical feature manifest.

[Croissant spec](https://docs.mlcommons.org/croissant/docs/croissant-spec.html), [Croissant on GitHub](https://github.com/mlcommons/croissant).

### Recommendation

Author the feature manifest in **LinkML** with classes referencing **OBO/EFO/SO ontologies via Bioregistry CURIEs**, expose the manifest as a **Croissant `RecordSet`** that the model card and dataset card both reference, and pin the Ensembl/GENCODE annotation version explicitly. The model's MLflow signature carries the *positional* contract (shape, dtype) and the Croissant manifest carries the *semantic* contract (which gene, in which order).

## 3. High-level model type / effect

This is the "what does this model do to the data" question, before architectural details. EDAM is the cleanest answer here.

### EDAM Operation, Topic, Data, Format

[EDAM](https://edamontology.org) is structured in four parallel hierarchies. Three are useful here:

- `Topic`: the application domain (`topic:3170` RNA-Seq, `topic:3474` Machine learning, `topic:3170` Transcriptomics).
- `Operation`: what the function does (`operation:2426` Modelling and simulation, `operation:3659` Regression analysis, `operation:3937` Feature extraction, `operation:3935` Dimensionality reduction, `operation:2238` Statistical calculation).
- `Data` and `Format`: what flows in and out.

EDAM does not natively distinguish "encoder" from "decoder" from "generator"; those are architectural patterns. But for the practical-effect question (does this thing reduce dimensionality, predict a label, generate a sample, impute missing entries) Operation maps cleanly. For the architectural pattern itself, no single ontology dominates; Bioschemas + custom LinkML enumeration is the pragmatic path.

### Model type taxonomy from MLflow / HuggingFace `pipeline_tag`

[HuggingFace's pipeline_tag](https://huggingface.co/docs/hub/en/model-cards) is a controlled vocabulary at the task level (`text-classification`, `feature-extraction`, `image-segmentation`, `tabular-regression`, etc.). It is not bio-aware but is widely supported.

### scvi-tools / scverse model categories

scvi-tools registers models by class (`SCVI`, `SCANVI`, `TOTALVI`, `MULTIVI`, `PEAKVI`, `DESTVI`, `LinearSCVI`, `CondSCVI`, `AmortizedLDA`, `JaxSCVI`, `MRVI`). Each implies a clear effect: SCVI is a generative VAE for counts; SCANVI is SCVI with a label classifier; totalVI is multi-modal RNA+ADT; etc. [scvi-hub](https://huggingface.co/scvi-tools) materializes this on Hugging Face with model cards that point at the training AnnData. This is the closest existing template for what a Cytognosis "cellular model" entry might look like.

### DOME-ML

[DOME](https://registry.dome-ml.org/) (Data, Optimization, Model, Evaluation) is a community recommendation set for reporting supervised ML in biology. It is not a serialization schema; it is a checklist with curated annotations and a Wizard. Adopt it as the publication-time review checklist, not as the runtime contract.

### Recommendation

Tag every Cytognosis model with:
- An EDAM **Operation** term for high-level effect.
- A LinkML enumeration for architectural pattern (`encoder`, `decoder`, `autoencoder`, `vae`, `gan`, `diffusion`, `transformer`, `gnn`, `linear`, `tree_ensemble`, `mechanistic`).
- A HuggingFace `pipeline_tag` for ecosystem discoverability.
- A DOME-ML score at publication time.

This combination keeps the model discoverable in EDAM-aware bioinformatics registries, in HuggingFace search, and in the DOME registry, with no single tag system carrying more weight than its scope warrants.

## 4. Distributional outputs

This is where standards thin out. None of ONNX, MLflow, Croissant, or HuggingFace Model Cards has a first-class type for "the output is a parameterized distribution". The pragmatics are:

### How frameworks handle it

- **Pyro / NumPyro** (`numpyro.distributions`): a registry of distribution classes (`Normal`, `LogNormal`, `Poisson`, `NegativeBinomial`, `ZeroInflatedNegativeBinomial`, `Categorical`, `Dirichlet`, `MultivariateNormal`, etc.) with `sample`, `log_prob`, `mean`, `variance` methods, plus reparameterized gradients via `rsample`. The API mirrors `torch.distributions`. NumPyro can wrap TFP distributions directly. [NumPyro distributions](https://num.pyro.ai/en/stable/distributions.html).
- **TensorFlow Probability** (`tfp.distributions`): same conceptual API, JAX-compatible via `tfp.substrates.jax`.
- **PyTorch** (`torch.distributions`): identical lineage. `rsample()` for reparameterized draws.
- **scvi-tools** uses these directly: an SCVI decoder returns a `NegativeBinomial` (or `ZeroInflatedNegativeBinomial`) distribution object whose parameters (μ, θ, π) are tensors of shape `(n_cells, n_genes)`. The user then samples or computes posterior expectations.

### How to declare this in a model card

Two pragmatic options:

1. **MLflow params + named output convention.** Declare outputs as the distribution's natural parameters with a convention like:

   ```
   outputs:
     - name: nb_mean
       type: tensor(float32, [n_cells, n_genes])
       semantics: NegativeBinomial.mean
     - name: nb_dispersion
       type: tensor(float32, [n_genes])
       semantics: NegativeBinomial.dispersion
   params:
     - name: return_distribution
       type: enum[mean, samples, parameters]
     - name: n_samples
       type: int32
   ```

2. **A custom Croissant ML extension** that adds an `outputDistribution` field with a controlled vocabulary referencing the Pyro/TFP class names. This is what is needed but does not exist as a standard yet, and is one of the gaps Cytognosis would either contribute upstream or maintain as an internal LinkML extension.

### The reparameterization trick at training time

When the variational posterior is part of the training loss, the backward pass needs `rsample` (reparameterized sampling) so gradients flow through the noise variable. This is not part of the inference-time contract. It belongs in the training notebook / training-job spec, not in the deployed model card. Document it in the DOME-ML "Optimization" section, not the model signature.

### Recommendation

Until a standard emerges, adopt **option 1 (MLflow params + named convention)** for the deployed contract, plus a small LinkML extension on the model card declaring `output_distribution_class: "NegativeBinomial"` so downstream tooling can reconstruct the distribution object. Contribute the spec to Croissant ML as a community proposal once the convention has settled internally.

## 5. Model packaging, registry, and provenance

### scvi-hub

The scverse model hub [scvi-tools on Hugging Face](https://huggingface.co/scvi-tools) is the working template: a Hugging Face repo holds the model weights plus a [HubModelCardHelper](https://docs.scvi-tools.org/en/stable/api/reference/scvi.hub.HubModelCardHelper.html)-generated Model Card plus a link to the training AnnData (often a CELLxGENE Census slice). It already does most of what a Cytognosis model registry would need.

### BioModels / SBML / CellML

[BioModels](https://www.ebi.ac.uk/biomodels/) is the canonical registry for *mechanistic* models in systems biology. SBML and CellML are the exchange formats. These are not ML formats but are essential when a Cytognosis project wraps a mechanistic prior into an ML loop or compares an ML predictor against a literature mechanistic model. The COMBINE archive bundles SBML + simulation experiment + figures.

### Workflow Run RO-Crate

[Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) packages a single execution: inputs, outputs, code, intermediate provenance, environment. Already supported by Nextflow (nf-prov), Snakemake, Galaxy. This is the right packaging for "the experiment that produced this checkpoint", as distinct from the checkpoint itself.

### Recommendation

The Cytognosis model packaging stack:
- **Weights**: ONNX (portable runtime) + native framework (PyTorch / JAX state dict).
- **Contract**: MLflow MLmodel + LinkML feature manifest.
- **Card**: HuggingFace Model Card YAML frontmatter, generated from a single LinkML source so it can also emit a DOME-ML annotation.
- **Distribution**: Hugging Face Hub repo (private during development, public at release).
- **Training run**: Workflow Run RO-Crate, optionally indexed in the DOME registry at publication time.
- **Mechanistic comparators**: BioModels references where applicable.

## Sources

- [ONNX IR spec](https://onnx.ai/onnx/repo-docs/IR.html), [ONNX MetadataProps](https://github.com/onnx/onnx/blob/main/docs/MetadataProps.md), [ONNX Concepts](https://onnx.ai/onnx/intro/concepts.html)
- [MLflow Model Signatures](https://mlflow.org/docs/latest/ml/model/signatures/), [MLflow signature.py](https://github.com/mlflow/mlflow/blob/master/mlflow/models/signature.py)
- [Croissant site](https://docs.mlcommons.org/croissant/), [Croissant 1.1 announce](https://mlcommons.org/2024/03/croissant_metadata_announce/), [Croissant + MCP](https://mlcommons.org/2025/10/croissant-mcp/), [Croissant arXiv 2403.19546](https://arxiv.org/pdf/2403.19546)
- [DOME paper, Nat Methods 2021](https://www.nature.com/articles/s41592-021-01205-4), [DOME Registry paper, arXiv 2408.07721](https://arxiv.org/abs/2408.07721), [DOME Registry](https://registry.dome-ml.org/intro)
- [Hugging Face Model Cards](https://huggingface.co/docs/hub/en/model-cards), [Model Card annotated template](https://huggingface.co/docs/hub/en/model-card-annotated)
- [scvi-tools docs](https://docs.scvi-tools.org/en/stable/), [scvi-hub on HF](https://huggingface.co/scvi-tools), [HubModelCardHelper](https://docs.scvi-tools.org/en/stable/api/reference/scvi.hub.HubModelCardHelper.html)
- [BioModels](https://www.ebi.ac.uk/biomodels/), [SBML.org](https://sbml.org/)
- [EDAM ontology](https://edamontology.org), [EDAM on BioPortal](https://bioportal.bioontology.org/ontologies/EDAM), [EDAM GitHub](https://github.com/edamontology/edamontology)
- [single-cell-curation latest schema](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html), [single-cell-curation repo](https://github.com/chanzuckerberg/single-cell-curation)
- [Bioregistry](https://bioregistry.io/), [Bioregistry paper, Sci Data 2022](https://www.nature.com/articles/s41597-022-01807-3)
- [NumPyro distributions](https://num.pyro.ai/en/stable/distributions.html), [NumPyro repo](https://github.com/pyro-ppl/numpyro), [Pyro VAE tutorial](https://pyro.ai/examples/vae.html)
- [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/), [Workflow Run paper, PLOS One 2024](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309210)
- [Virtual Cell Challenge](https://virtualcellchallenge.org/), [Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)
