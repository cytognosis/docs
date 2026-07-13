# Cytos Pipeline Automation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (02_pipeline_automation.md in Obsidian vault: 04-Engineering/cytos/) - Agent (n/a)

Companion to `01_cytos_package_design.md`. Specifies the exact automation surfaces (nox sessions, Prefect flows, GitHub Actions workflows, CLI subcommands) and the IO contract per stage.

## 1. Stage IO contracts

| Stage | Producer | Consumer | Inputs | Outputs | Failure mode |
|---|---|---|---|---|---|
| download | `cytos.sources.<source>.fetch()` | parse | `configs/sources/<id>.yaml` (descriptor), env (`UMLS_API_KEY`, etc.) | `data/raw/<source>/<version>/<files>`, `_manifest.json` (sha256, retrieval_ts, license) | non-zero exit on auth, checksum, license-renewal failure |
| parse | `cytos.ingest.parsers.<format>` | linkmlize | `data/raw/<source>/<version>/` | `data/interim/<source>/<version>/` (Parquet, JSONL, rdflib dump) | non-zero on schema-mismatch in raw |
| linkmlize | `cytos.ingest.linkmlize.<source>` | validate | `data/interim/...`, `schemas/...` | `data/normalized/<source>/<version>/<TargetClass>.parquet`, `data/linkml/<source>/<version>/...yaml`, optional `schemas/auto/<source>.yaml` | non-zero on unknown target class |
| validate | `cytos.validate.<engine>` | harmonize | normalized tables + LinkML schemas | `results/validation/<source>/<version>.json` | block: refuses to advance if any structural or semantic error |
| harmonize | `cytos.harmonize.tiered_resolver` | kg_build | normalized tables, OAK SQLite cache, SSSOM sets | `data/normalized/<source>/<version>/_harmonized/`, `schemas/mappings/sssom/<pair>.sssom.tsv`, `schemas/mappings/sssom/_provenance/<pair>.sssom.tsv`, optional `results/curator_queue/<pair>.csv` | non-blocking if "manual" rows queued; tiered resolver records confidences |
| kg_build | `cytos.kg.{biocypher, koza}.runner` + `cytos.kg.merge` | qc_kg | harmonized normalized + sssom + biocypher config | `kg/working/<release>/{nodes.tsv, edges.tsv, by_source/}` | non-zero on adapter raise |
| qc_kg | `cytos.validate.{referential, shacl, kgx}` | publish | KG working dir + schemas | `results/coverage/<release>.json`, `results/validation/kg-<release>.json` | block: refuses publish on errors |
| featurize | `cytos.features.<modality>` | train | harmonized normalized tables + `configs/cohorts/<cohort>.yaml` | `data/cohorts/<cohort>/<version>/master.parquet`, `data/features/<cohort>/<version>/<modality>/`, `data/splits/<cohort>/<split>.yaml` | block: missing-modality-mask must be present; ancestry/sex/age columns required |
| train | `cytos.train.lightning` or `cytos.train.jax` | evaluate, infer | feature store + `configs/training/<recipe>.yaml` | `checkpoints/<run>/`, MLflow run, `results/training/<run>.json` | non-zero on NaN loss, OOM, divergence |
| evaluate | `cytos.evaluate.{integration,pairing,downstream,fairness,robustness}` | publish (graduate) | trained snapshot + held-out splits + benchmark fixtures | `results/eval/<run>.json`, leaderboard.md update | block: fairness gate refuses publish on >X% subgroup gap |
| kg_embed | `cytos.models.kg_embed.pyg` | publish, infer | published KG subgraph | `data/embeddings/<run>/kg/`, checkpoint | non-zero on link-prediction MRR collapse |
| infer | `cytos.models.serve.batch` | (downstream consumers) | trained model + cohort or single-patient bundle | `data/embeddings/<run>/<modality>/`, `results/inference/<run>/<batch>.parquet` | runtime errors per request |
| publish | `cytos.publish.snapshot` | (downstream) | KG working dir + schemas + sssom + prov + graduated models + cards + reference embeddings | `kg/snapshots/<release>/`, `locked/LOCK_MANIFEST.json` updated | block: SHACL pass required, zero controlled rows, every graduated model has a card |
| serve_rag | `cytos.rag.langgraph_router` | (consumer) | published snapshot | running service (FastAPI, Cypher, semsimian, retrieval) | runtime errors, not pipeline-blocking |

## 2. Nox sessions

Top-level sessions (`noxfile.py`) and what they wrap:

```
nox -s setup_venv            # uv sync + nox -s install_skills (cytocast hook)
nox -s install_skills        # vendors agent skills from sibling agents/

# Quality gates (inherited tiers from cytoskeleton)
nox -s format
nox -s lint_local
nox -s lint_dev
nox -s lint_ci
nox -s lint_release
nox -s typecheck
nox -s security
nox -s deps_check
nox -s doctor_deps
nox -s audit
nox -s pr_verify             # runs all gates + policy/rego/

# Tests
nox -s test                  # all
nox -s test_unit
nox -s test_integration
nox -s test_platform

# Docs
nox -s docs_build
nox -s docs_serve
nox -s docs_publish
nox -s notebooks_check       # executes notebooks under notebooks/

# Cytos data arc
nox -s download              # cytos sources fetch --all
nox -s parse                 # cytos ingest parse --all
nox -s linkmlize             # cytos ingest linkmlize --all
nox -s schema_generate       # cytos schema generate --all
nox -s validate              # cytos validate linkml --all + sssom + cellxgene
nox -s harmonize             # cytos harmonize resolve --all
nox -s kg_build              # cytos kg build $(date -u +cytos-%Y.%m)
nox -s kg_validate           # qc_kg suite
nox -s kg_publish            # cytos publish snapshot $RELEASE
nox -s release               # version bump + tag + ci

# Cytos modeling arc (NEW)
nox -s featurize             # cytos features build $COHORT
nox -s split                 # cytos features split $COHORT --stratify ancestry,sex,age
nox -s train                 # cytos train run configs/training/recipes/<RECIPE>.yaml
nox -s train_jax             # cytos train jax  configs/training/recipes/<RECIPE>.yaml
nox -s resume                # cytos train resume $RUN_ID
nox -s hpo                   # cytos train hpo  configs/training/recipes/<RECIPE>.yaml
nox -s evaluate              # cytos evaluate report $RUN_ID (runs all subtracks)
nox -s kg_embed              # cytos kg-embed train + export
nox -s infer                 # cytos infer batch $RUN_ID $COHORT
nox -s pretrain_smoke        # tiny-fixture smoke: features -> train (3 epochs) -> evaluate -> infer

# Build
nox -s build_wheel
nox -s docker_build
nox -s version_bump
```

## 3. Prefect flow inventory

Modules in `src/cytos/pipelines/` and YAML manifests in `configs/pipelines/`:

| Flow module | Manifest | Purpose | Schedule |
|---|---|---|---|
| `fetch_sources.py` | `configs/pipelines/nightly_fetch.yaml` | refresh open-license sources | nightly 02:00 UTC |
| `validate_raw.py` | `configs/pipelines/validate_raw.yaml` | per-source structural validation | runs after fetch |
| `transform_to_linkml.py` | `configs/pipelines/linkmlize.yaml` | parse + linkmlize all interim data | weekly Mon 03:00 UTC |
| `merge_kg.py` | `configs/pipelines/weekly_kg_build.yaml` | full kg_build + qc + publish dry-run | weekly Mon 06:00 UTC |
| `qc_kg.py` | `configs/pipelines/qc.yaml` | referential + SHACL + KGX validate | runs after merge |
| `build_cohort.py` | `configs/pipelines/cohort_assembly.yaml` | featurize across modalities, ancestry-stratified split | monthly first Mon |
| `pretrain.py` | `configs/pipelines/monthly_pretrain.yaml` | train + evaluate baseline + PoE-VAE recipes | monthly first Mon, manual approval |
| `kg_embed.py` | `configs/pipelines/kg_embed.yaml` | RGCN/GraphSAGE refresh on the new KG | per release |
| `publish_release.py` | `configs/pipelines/release.yaml` | snapshot (data + KG + models + cards + embeddings) + lock manifest + zenodo + optional HF upload (manual approve) | on tag push |

Flow tasks call CLI subcommands via `cytos.cli.programmatic.run(...)` rather than shell-out, so failures bubble as Python exceptions and Prefect can retry.

## 4. GitHub Actions workflows

`.github/workflows/`:

```
ci.yaml              # PR + push to main; ruff, ty, pytest (unit + integration), schema codegen smoke, docs build
deploy-docs.yaml     # on docs/** change; mkdocs gh-deploy
release.yaml         # on tag push; full release flow (data + KG + models)
kg-build.yaml        # cron weekly; nightly_fetch + weekly_kg_build flows
pretrain.yaml        # cron monthly (manual approval); cohort_assembly + monthly_pretrain
pretrain_smoke.yaml  # PR + nightly; tiny-fixture pretrain smoke (3 epochs, CPU)
hf_upload.yaml       # manual; uploads a graduated model to Hugging Face
sync_contracts.yaml  # nightly; refreshes locked/VERSION_POLICY.yaml from upstream sources
```

## 5. Source registry contract

Every file under `configs/sources/<id>.yaml` is a `SourceDescriptor` instance:

```yaml
id: biolink                              # matches filename stem
name: Biolink Model
homepage: https://biolink.github.io/biolink-model/
license: BSD-3-Clause                    # spdx
license_class: open                      # open | open-restricted | controlled
citation: "Unni et al. 2022, doi:10.1111/cts.13302"
version_policy:
  current: "4.2.6"                       # pinned
  upgrade_cadence: monthly
download:
  uris:
    - https://github.com/biolink/biolink-model/raw/v{version}/src/biolink_model/schema/biolink_model.yaml
  format: linkml-yaml
  checksum: ""                           # populated on first fetch
  expected_size_bytes: 0
ingest:
  parser: linkml                         # one of: rdf, jsonschema, rrf, parquet, bibtex, owl, hdmf, linkml
  linkml_target_class: ""                # blank when source itself IS the schema
  bridge: null                           # one of: jsonld_to_ttl, yamljs_to_jsonjs, proto_to_jsonjs, parquet_to_linkml, rrf_to_rdf, hdmf_namespace_walker
kg:
  framework: biocypher                   # biocypher | koza | none
  adapter_path: cytos.kg.biocypher.adapters.biolink
  emit_to: working
update_cadence: monthly
contacts:
  maintainer: cytognosis-eng@cytognosis.org
notes: ""
```

A 21-source baseline (matching the playbook):

`biolink`, `umls`, `snomed_ct`, `ols4_mappings`, `biothings_mygene`, `biothings_myvariant`, `biothings_mychem`, `biothings_mydisease`, `biothings_dde`, `ga4gh_vrs`, `ga4gh_phenopackets`, `ga4gh_beacon`, `cellxgene_5_2`, `nwb_core`, `opentargets`, `monarch_kg`, `openalex`, `bibtex`, `schema_org`, `bioschemas`, `sosa_ssn`.

## 6. Release cadence

* Monthly snapshot tag `cytos-YYYY.MM` (e.g. `cytos-2026.05`). Each carries data + KG + (optional) graduated models.
* Patch tags `cytos-YYYY.MM.N` for SSSOM, schema, or model card fixes against a released snapshot.
* Each snapshot ships a `RELEASE_NOTES.md` with: source-version table, SSSOM diff vs. previous snapshot, KG coverage diff, validation report summary, controlled-subset disclosure, graduated-model registry slice (arch + version + parent + MLflow run id + fairness summary), and download links (Zenodo DOI, Hugging Face URLs).

## 7. Local developer loop

```bash
# scratch on a single source
cytos sources fetch biolink
cytos ingest linkmlize biolink
cytos schema generate pydantic
cytos validate linkml --source biolink

# full integration smoke (small fixture)
nox -s test_integration -- --kg-fixture mini
```

The `mini` fixture is a curated 10k-node open-license KG kept under `tests/data/reference_kg/` and rebuilt quarterly.
