# Cytos Foundation-Model Architecture

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (04_foundation_model_architecture.md in Obsidian vault: 04-Engineering/cytos/) - Agent (n/a)

Companion to `01_cytos_package_design.md`. Specifies the modeling arc that turns harmonized cytos data plus the cytos KG into a patient-foundation-model substrate: per-modality encoders, fusion strategies, training infrastructure, evaluation, and serving.

Source materials:

- `/home/mohammadi/Documents/Claude/Projects/Science and Platform/multimodal_coembedding_review_2025_2026.md` (51KB methods review).
- `/home/mohammadi/Documents/Claude/Projects/Science and Platform/multimodal_coembedding_addendum_deep_dives.md` (Q1 FGW-vs-paired, Q2 cross-attention, Q3 MoE, Q4 causal).
- `/home/mohammadi/Documents/Claude/Projects/Science and Platform/cytognosis_master_dataset_curation.md` (Cytoverse modalities, stage-wise stack, biobanks, federation).

## 1. The five Cytoverse modalities

Per the master dataset curation, every patient is represented by up to five modalities:

| Modality | Canonical containers | Primary substrates | Cytos features submodule |
|---|---|---|---|
| Phenotype | HPO codes, structured forms, FHIR Observation | mixed tabular (categorical + continuous + ordinal) | `cytos.features.modalities.phenotype` |
| Genotype | VCF, BGEN, PLINK | variant calls, polygenic risk scores, ancestry vectors | `cytos.features.modalities.genotype` |
| Single-cell omics | AnnData (.h5ad), MuData (.h5mu), TileDB-SOMA | counts, ATAC peaks, ADTs, spatial | `cytos.features.modalities.sc_omics` |
| Connectomics + imaging | NIfTI, BIDS, NWB, HDF5 | structural/functional adjacency tensors, 3D volumes, surface meshes, atlas-aligned ROIs | `cytos.features.modalities.connectomics`, `cytos.features.modalities.imaging` |
| EHR | FHIR, OMOP CDM | tokenized event sequences (visit + diagnosis + procedure + medication) | `cytos.features.modalities.ehr` |

Each modality's submodule produces: (1) a per-patient tensor or graph; (2) a tokenizer + vocab artifact under `data/features/<cohort>/<version>/<modality>/_tokenizer/`; (3) a missing-modality mask; (4) a normalization manifest (batch effects, scaler params, atlas version).

## 2. Per-modality encoders (`cytos.models.encoders`)

| Encoder | Backbone | Notes |
|---|---|---|
| `tabular.MLP`, `tabular.FTTransformer` | MLP, FT-Transformer | for phenotype + summary EHR features |
| `sequence.TokenTransformer` | encoder-only transformer with rotary or alibi pos | for tokenized EHR, genotype (treating variants as tokens), and BibTeX/OpenAlex text |
| `graph.GAT`, `graph.GraphSAGE`, `graph.RGCN` | PyG | for connectome graphs and KG-conditioned encoders |
| `image.ResNet3D`, `image.MONAINet`, `image.ViT3D` | torchvision / MONAI | for structural + functional MRI volumes |
| `singlecell.SCVI`, `singlecell.SCANVI`, `singlecell.TotalVI`, `singlecell.PeakVI`, `singlecell.MultiVI`, `singlecell.DestVI`, `singlecell.VeloVI` | scvi-tools | single-cell foundation backbones |
| `text.FrozenLM` | sentence-transformers or biogpt | frozen embedder for clinical notes + literature |

Every encoder is wrapped in a Lightning Module (`cytos.models.lightning_modules.encoder_module`) so it can be trained alone, jointly with a fusion head, or used as a frozen feature extractor.

## 3. Fusion strategies (`cytos.models.fusion`)

The cytos master design supports five fusion family lineups, ordered by complexity:

### 3.1 PoE / MoE / MoPoE VAE (`fusion.poe_vae`, `fusion.moe_vae`, `fusion.mope_vae`)

Product-of-Experts (Multigrate-style), Mixture-of-Experts, and Mixture-of-Product-of-Experts variational autoencoders. Joint posterior factorizes across modalities, allowing principled missingness. Encoders feed Gaussian experts; decoders reconstruct each modality.

### 3.2 Contrastive cross-modal (`fusion.contrastive`)

InfoNCE and CLIP-style heads over per-patient pairs. Encoders share or align a common embedding space; positives are same-patient cross-modality, negatives are within-batch mixings. Supports modality dropout regularization.

### 3.3 Optimal transport (`models.ot.*`)

Wasserstein, Gromov-Wasserstein, Fused-Gromov-Wasserstein, and FGW-barycenter modules. Barycenter is the proposed N+1-th consensus space when modalities live in genuinely incomparable spaces (per the addendum's Q1 analysis: for paired patients, CKA/RV/dCor are often the correct metrics, but FGW is necessary when spaces are non-isomorphic; cytos supports both flows).

### 3.4 MOFA / MOFA-FLEX (`fusion.mofa`)

Sparse Bayesian factor decomposition. Cheapest, most interpretable, handles missing modalities natively. Used as a baseline that every more complex model must beat.

### 3.5 Cross-attention transformer (`fusion.cross_attention`) and MoE (`fusion.mixture_of_experts`)

Q-Former / Perceiver IO / Flamingo-gated patterns (per addendum Q2), Multiway transformer / LIMoE / Soft MoE (per addendum Q3). Cross-attention compresses per-modality token sets into a small set of latents; MoE routes tokens to modality-specific or content-specific experts. Both used for the largest pretraining recipes.

### 3.6 Archetype head (`fusion.archetype`)

MIDAA-style archetypal heads on top of any fused latent, producing interpretable extreme phenotype axes.

## 4. Causal representation (`cytos.models.causal`)

Optional. Implements identifiable VAE (iVAE), content-style splits, slot attention, and intervention-aware encoders, per addendum Q4. Used where the downstream goal is to disentangle disease etiology from confounds (batch, ancestry, age).

## 5. KG embedding (`cytos.models.kg_embed`)

The cytos KG (published in `kg/snapshots/<release>/`) is consumed as a graph signal:

- `pyg.RGCN` and `pyg.GraphSAGE` train node and relation embeddings over the published KG subgraph (e.g., disease + variant + drug + gene + pathway slices).
- `transE_rotE.py` covers TransE / RotE / RotatE classical KGE baselines.
- `kge_eval.py` runs link-prediction harness (MRR, Hits@k).
- Outputs are saved to `data/embeddings/<run>/kg/` as Parquet plus a Lightning checkpoint, then fed back into the fusion stage as a per-patient KG-conditioned feature (one row per patient, with KG-derived comorbidity prior summed over their diagnosis CURIEs).

## 6. Training infrastructure (`cytos.train`)

### 6.1 Lightning (default path)

`cytos.train.lightning.trainer.Trainer` wraps `pytorch_lightning.Trainer` with:

- MLflow callback (URI from `mlflow_tracking_uri`, defaults to `https://mlflow.cytognosis.org`).
- Checkpoint callback writing to `checkpoints/<run>/` with `lineage.json` updates.
- Early stopping + LR monitor + GPU stats callbacks.
- Strategies: DDP single-node, DDP multi-node, FSDP for >1B params, deepspeed-zero3 if FSDP underperforms.
- ROCm-specific plugins for GPU memory ceilings, MIOpen tuning, and AMD-specific NCCL alternatives.

### 6.2 JAX (research path)

`cytos.train.jax.loop.Loop` wraps a Flax model + Optax optimizer + pjit sharding. Used for experimental modalities (large GNNs over the KG, OT flows with very large batches).

### 6.3 DataModules

Per-stage Lightning DataModules under `cytos.train.data/`:

- `coembed_dm.CoEmbedDataModule` joins per-modality feature stores by patient id and emits batched dicts with missing-modality masks.
- `singlecell_dm.SingleCellDataModule` wraps AnnData-backed scvi-tools dataloaders.
- `kg_dm.KGDataModule` produces RGCN-friendly batches from `kg/snapshots/`.

### 6.4 Hyperparameter search

`cytos.train.hpo.optuna` and `cytos.train.hpo.ray` wrappers; both consume the same Hydra recipe and log every trial to MLflow.

### 6.5 Training recipes (`configs/training/recipes/`)

One YAML per pretraining recipe. Examples:

- `recipes/poe_vae_pilot.yaml`: PoE-VAE on the neuro-pilot cohort with phenotype + genotype + sc_omics modalities, batch size 256, 200 epochs, AMP-bfloat16 on ROCm.
- `recipes/mofa_baseline.yaml`: MOFA-FLEX baseline matched-cohort, CPU-only, ~5 minutes.
- `recipes/multiway_xattn.yaml`: full Multiway transformer with cross-attention over all five modalities; multi-node DDP.
- `recipes/kg_rgcn.yaml`: RGCN on cytos-2026.05 KG subgraph.

Recipes are version-controlled; every Recipe yields a deterministic run when seeded.

## 7. Evaluation (`cytos.evaluate`)

### 7.1 Integration metrics

`cytos.evaluate.integration.scib` runs scIB's bio-conservation + batch-correction suite over the joint embedding.

### 7.2 Pairing-preservation metrics (per addendum Q1)

When patients are already paired:

- `cka.py`: Centered Kernel Alignment between each pair of modality embeddings (modern default).
- `rv.py`: RV coefficient (the classical analogue).
- `dcor.py`: distance correlation.
- `procrustes.py`: Procrustes alignment + residual error.
- `pairing.py`: kNN-overlap and graph alignment on the joint vs per-modality embeddings.

### 7.3 Downstream probing (`evaluate.downstream`)

Disease prediction, trait prediction, survival probing, all using held-out splits. Logistic/linear probes by default; small MLP probes when needed.

### 7.4 Modality attribution (`evaluate.attribution`)

Shapley values and leave-one-modality-out experiments to measure each modality's contribution to a downstream task.

### 7.5 Fairness (`evaluate.fairness`)

Ancestry / age / sex stratified metrics; subgroup leaderboards. Required for every cohort that includes population biobanks.

### 7.6 Robustness (`evaluate.robustness`)

Modality dropout, feature corruption, OOD shifts. Stress-tested across all evaluation tracks.

### 7.7 Report

`evaluate.report` aggregates per-track JSON into `results/eval/<run>.json` and writes a Markdown summary to `results/eval/<run>.md`. The leaderboard at `benchmarks/leaderboard.md` is updated.

## 8. Inference and serving (`cytos.models.serve`)

### 8.1 FastAPI service

`cytos.models.serve.fastapi` exposes:

- `POST /embed/<modality>` returns per-modality embedding for an input bundle.
- `POST /embed/joint` returns the consensus N+1 embedding (PoE or FGW barycenter).
- `POST /score/<task>` runs a registered downstream head (disease, trait, survival).
- `POST /generate/cypher` calls `cytos.rag.cypher_generator` if the `llm` extra is installed.

Endpoints emit OpenAPI; backend selected from `cytos.models.registry` by `(arch, version)` tuple.

### 8.2 Batch inference

`cytos.models.serve.batch.embed_cohort(cohort, run)` writes per-patient embeddings to `data/embeddings/<run>/<modality>/`.

### 8.3 Streaming

`cytos.models.serve.streaming` provides chunked-batch streaming for very large cohorts.

## 9. Model registry, model cards, and lineage

`cytos.models.registry.ModelRegistry` tracks every model snapshot in `models/pretrained/` and `models/finetuned/`. Each entry records:

- arch id (e.g., `poe_vae`), version (`2026.05`), training recipe path, MLflow run id.
- parent ancestor (which pretrained encoder was fine-tuned).
- training data fingerprint: cytos data release tag, cohort id, splits hash, total samples per modality.
- evaluation summary (pulled from `results/eval/<run>.md`).
- license (Apache-2.0 default; OpenRAIL-M when downstream restrictions apply).

`cytos.models.card.generate(arch, version)` emits a Hugging Face style model card with Cytognosis extensions for ancestry/age/sex coverage and known limitations.

`cytos.publish.snapshot` includes the active model registry slice; `cytos publish hf-upload <arch>-<version>` pushes the encoder weights + tokenizer + model card to Hugging Face under the Cytognosis org.

## 10. Recommended pretraining cadence

| Cadence | Trigger | Outputs |
|---|---|---|
| Monthly | nightly KG build on first Monday | `cytos-YYYY.MM` data snapshot + MOFA baseline + PoE-VAE pilot retrain |
| Quarterly | manual approval | full Multiway-xAttn pretraining on the master cohort + leaderboard update |
| Per-release | tag push | RGCN refresh on the new KG snapshot + smoke evaluation |

All cadences are encoded in `configs/pipelines/*.yaml` and `.github/workflows/{kg-build,pretrain,release}.yaml`. Pretraining workflows require manual approval to spend GPU time.

## 11. Recipes summary (Hydra YAML excerpts)

`configs/training/recipes/poe_vae_pilot.yaml`:

```yaml
seed: 42
data:
  cohort: neuro-pilot
  cytos_release: cytos-2026.05
  splits: data/splits/neuro-pilot/ancestry-stratified.yaml
  modalities: [phenotype, genotype, sc_omics]
model:
  arch: cytos.models.fusion.poe_vae
  latent_dim: 64
  encoders:
    phenotype: cytos.models.encoders.tabular.FTTransformer
    genotype: cytos.models.encoders.sequence.TokenTransformer
    sc_omics: cytos.models.encoders.singlecell.SCVI
trainer:
  strategy: ddp
  precision: bf16
  max_epochs: 200
  callbacks: [mlflow, checkpoint, early_stop]
  batch_size: 256
  accelerator: rocm
optim:
  optimizer: adamw
  lr: 2e-4
  weight_decay: 1e-2
  scheduler: cosine
```

`configs/training/recipes/kg_rgcn.yaml`:

```yaml
seed: 42
data:
  cytos_release: cytos-2026.05
  subgraph: kg/snapshots/cytos-2026.05/subgraphs/disease_variant_drug.parquet
  splits: kg/snapshots/cytos-2026.05/splits/edge_split.yaml
model:
  arch: cytos.models.kg_embed.pyg.RGCN
  num_layers: 3
  hidden: 256
  num_bases: 30
trainer:
  strategy: single_device
  precision: 32
  max_epochs: 50
  accelerator: rocm
optim:
  optimizer: adam
  lr: 1e-3
```

## 12. Connection to Cytognosis ecosystem

Cytos is the **substrate**, not the destination. Trained encoders graduate into the scale-tier `neuro*` repos (per the four-tier register):

- `neurogeno` consumes the genotype encoder for genomic-scale tasks.
- `neurocyto` consumes the sc_omics encoder + scvi-tools wrappers.
- `neurotopo` consumes the connectomics encoder + RGCN KG embeddings.
- `neurophysio` consumes the imaging encoder.
- `neuroetho` consumes the EHR encoder and behavioral phenotype features.

Each neuro-scale repo loads cytos pretrained checkpoints by `(arch, version)` and adapts them via thin task heads under their own `models/` tree. Cytos owns the foundation; neuro-scale repos own the application.

## 13. Open questions

1. **scvi-tools vs custom VAE**: should cytos write a thin wrapper around scvi-tools (which itself is a Lightning-based VAE framework) or reimplement PoE-VAE natively? Recommendation: wrap scvi-tools for single-cell; reimplement PoE-VAE natively for multimodal so we can plug in non-scvi modalities cleanly.
2. **JAX**: keep as a research path or invest? Recommendation: keep as a research path until a multimodal-OT or pjit sharding case proves it pays off; do not duplicate Lightning recipes for now.
3. **Hugging Face**: upload all pretrained encoders or only "graduated" ones? Recommendation: graduate via the model registry, with a `card.graduate: true` flag; only graduated models get Hugging Face uploads.
4. **Distributed training infra**: rely on the lab's existing ROCm cluster, or design cytos for SkyPilot bursts to AMD-hosted spot? Recommendation: support both via the `cytos.train.lightning.plugins` layer, default to local cluster, document SkyPilot path.
