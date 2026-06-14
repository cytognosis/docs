<!-- Last updated: 2026-06-14 | Source: Plans/design/11_reproducibility_strategy/ -->

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `reproducibility`, `provenance`, `ro-crate`, `in-toto`

**← [Back to Reproducibility Index](README.md)**

# 04 — Provenance and Lineage

**Reading order**: read `00_master_strategy.md` §7 first.

This document defines the provenance plane: how a single workflow run produces a complete citable bundle that links code (SWHID) → container image (digest) → input data (hashes) → parameters → output data (hashes) → metrics → attestation, and how that bundle becomes a Workflow Run Crate.

---

## 1. Architectural commitments

| Decision | What | Why |
|---|---|---|
| **Four tools cooperate** | DVC + redun + LaminDB + MLflow | Each does one thing well; metadata cross-references unite them |
| **Workflow Run Crate is the carrier** | Every run emits a WRROC | Standard format, federates with WorkflowHub ecosystem |
| **in-toto + DSSE for attestation** | DSSE-wrapped in-toto layouts | SLSA Level 3+; composes with sigstore |
| **One emitter library** | `cytoskeleton.crate` | Engine-agnostic; redun, Nextflow, Snakemake, Galaxy, Kedro plug-in |
| **OTel for traces** | Every stage execution is an OTel span | Cross-system observability; trace IDs end up in Crates |

---

## 2. Tool responsibilities (in detail)

### 2.1 DVC

- Tracks data versioning: stages have `deps:` and `outs:`, each with content hash.
- Pipeline graph: `dvc.yaml` declares the DAG; `dvc repro` walks it; cache prevents re-execution.
- Remote storage: pushes/pulls content-addressed blobs to GCS via DVC remote.
- Cytos already has this working with 10 stages.
- **Limitation**: dvc.yaml is path-coupled (the SWHID-driven config strategy fixes this — see `02_artifact_vfs_swhid.md` §5).

### 2.2 redun (Insitro)

Per `tools_infra_stack.md` §6.4, redun is "the single most important internal artifact in the Cytognosis build backlog (its RO-Crate plugin)."

- AST-aware: hashes Python function source so any code change invalidates the cached result.
- Data hashing: every input is hashed; identical inputs + identical fn → cache hit.
- Lineage graph: every Result has a parent (the Task call that produced it).
- Executors: local, AWS Batch, k8s, GCP Cloud Run, HPC slurm.
- Plugin model lets us hook in a Workflow Run Crate emitter.

**The Cytognosis redun + crate-emitter plugin** is the central artifact:

```python
# cytoskeleton/src/cytoskeleton/redun_plugin/__init__.py
from redun.executors import Executor
from cytoskeleton.crate import WorkflowRunCrateBuilder
from cytoskeleton.attest import InTotoChainBuilder
from cytoskeleton.vfs import vfs

class CytognosisExecutor(Executor):
    """Redun executor that emits Workflow Run Crates per run."""

    def submit(self, job):
        # 1. Resolve all inputs via VFS, verify hashes
        for uri in job.inputs.uris:
            vfs.verify(uri)
        # 2. Pull image by digest, verify signature
        image = self.pull_signed(job.env.image_digest)
        # 3. Execute in container
        result = self.run(job, image)
        # 4. Hash outputs
        for path in result.outputs:
            vfs.put(path)
        # 5. Emit Crate
        crate = WorkflowRunCrateBuilder()
        crate.set_main_entity(job.code_swhid)
        crate.add_action(
            instrument=job.code_swhid,
            object=[v.uri for v in job.inputs],
            result=[v.uri for v in result.outputs],
            container_image=image.digest,
            start_time=job.start_time,
            end_time=job.end_time,
            parameters=job.params,
        )
        # 6. Attestation
        chain = InTotoChainBuilder()
        chain.add_source(job.code_swhid, signer=job.author_key)
        chain.add_build(image.digest, signer=ci_oidc_token)
        chain.add_run(image.digest, job.inputs, result.outputs, signer=runner_key)
        crate.attach_attestation(chain.build_dsse())
        crate.write(f".crates/{job.run_id}/")
        # 7. LaminDB + MLflow
        log_to_lamindb(job, result, crate)
        log_to_mlflow(job, result)
```

### 2.3 LaminDB

LaminDB is "Artifact registry + Run/Transform lineage + Feature curation. Default catalog layer." (`tools_infra_stack.md` §6.5)

- Every output is registered as `ln.Artifact` with: cytognosis:// URI, hash, type, ontology-grounded features.
- Every run is registered as `ln.Run(transform=ln.Transform(swhid=...), input=..., output=...)`.
- `bionty` plugin grounds features in OBO ontologies.
- UI exposes the lineage graph.

### 2.4 MLflow

For ML-specific runs: log metrics, params, model files. The MLflow run ID is embedded in the WRROC's parameters. MLflow's model registry is the canonical home for in-progress model versions; published models also go to Hugging Face Hub.

---

## 3. Workflow Run Crate emission (concrete)

The `cytoskeleton.crate` library emits Crates conforming to `profiles/workflow_run_crate.yaml`. Layout of an emitted Crate:

```
.crates/<run-id>/
├── ro-crate-metadata.json       # the JSON-LD descriptor
├── ro-crate-preview.html        # generated preview
├── README.md                    # auto-generated narrative
├── workflow/
│   ├── main.py                  # symlink to code (SWHID-resolvable)
│   └── workflow.cwl             # optional CWL description
├── inputs/
│   └── <input-name>.{ext}       # symlinks or hashes
├── outputs/
│   └── <output-name>.{ext}      # symlinks or hashes
├── logs/
│   ├── stdout.log
│   ├── stderr.log
│   └── otel-trace.json
└── attestation/
    └── envelope.dsse.json       # DSSE envelope
```

The `ro-crate-metadata.json` for a representative run:

```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {"@id": "./"},
      "conformsTo": [
        {"@id": "https://w3id.org/ro/crate/1.2"},
        {"@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"},
        {"@id": "https://w3id.org/ro/wfrun/process/0.5"},
        {"@id": "https://w3id.org/ro/wfrun/workflow/0.5"}
      ]
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "biolink ingest run 2026-05-18T08:30Z",
      "description": "Ingestion of biolink-model.owl into KG nodes + edges",
      "datePublished": "2026-05-18T08:35:00Z",
      "license": "https://www.apache.org/licenses/LICENSE-2.0",
      "version": "0.1.0",
      "mainEntity": {"@id": "workflow/main.py"},
      "hasPart": [
        {"@id": "workflow/main.py"},
        {"@id": "inputs/biolink-model.owl"},
        {"@id": "outputs/biolink_nodes.tsv"},
        {"@id": "outputs/biolink_edges.tsv"},
        {"@id": "logs/stdout.log"},
        {"@id": "attestation/envelope.dsse.json"}
      ]
    },
    {
      "@id": "workflow/main.py",
      "@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"],
      "name": "biolink ingest",
      "programmingLanguage": {"@id": "https://w3id.org/cytognosis/workflow-ro-crate#redun"},
      "subjectOf": {"@id": "swh:1:rev:2c79bff0a06f4cb1f6b3..."},
      "input": [
        {"@id": "#biolink-owl-input"}
      ],
      "output": [
        {"@id": "#biolink-nodes-output"},
        {"@id": "#biolink-edges-output"}
      ]
    },
    {
      "@id": "inputs/biolink-model.owl",
      "@type": ["File"],
      "name": "biolink-model.owl",
      "contentSize": "1245678",
      "encodingFormat": "application/rdf+xml",
      "sha256": "91d4abf0...",
      "cytognosis:uri": "cytognosis://data/sha256:91d4abf0..."
    },
    {
      "@id": "outputs/biolink_nodes.tsv",
      "@type": ["File"],
      "name": "biolink_nodes.tsv",
      "contentSize": "8739811",
      "encodingFormat": "text/tab-separated-values",
      "sha256": "80d1d8...",
      "dvc:md5": "80d1d8...",
      "cytognosis:uri": "cytognosis://data/dvc:md5:80d1d8..."
    },
    {
      "@id": "#run-action-2026-05-18-08-30",
      "@type": "CreateAction",
      "name": "redun-run",
      "instrument": {"@id": "workflow/main.py"},
      "object": [{"@id": "inputs/biolink-model.owl"}],
      "result": [
        {"@id": "outputs/biolink_nodes.tsv"},
        {"@id": "outputs/biolink_edges.tsv"}
      ],
      "agent": {"@id": "#agent-shahin"},
      "startTime": "2026-05-18T08:30:00Z",
      "endTime": "2026-05-18T08:34:23Z",
      "cytognosis:containerImage": "sha256:9001ab74dcba4a35b...",
      "cytognosis:envName": "cytognosis-base",
      "cytognosis:envVersion": "v2.1.0",
      "cytognosis:runId": "...",
      "cytognosis:laminDbRunId": "...",
      "cytognosis:mlflowRunId": "...",
      "cytognosis:otelTraceId": "...",
      "cytognosis:dsseAttestation": {"@id": "attestation/envelope.dsse.json"}
    },
    {
      "@id": "#agent-shahin",
      "@type": "Person",
      "name": "Shahin Mohammadi",
      "email": "mohammadi@cytognosis.org",
      "@orcid": "0000-0001-XXXX-XXXX"
    },
    {
      "@id": "attestation/envelope.dsse.json",
      "@type": ["File", "MediaObject"],
      "name": "DSSE-wrapped in-toto attestation",
      "encodingFormat": "application/json"
    },
    {
      "@id": "https://w3id.org/cytognosis/workflow-ro-crate#redun",
      "@type": "ComputerLanguage",
      "name": "redun",
      "url": "https://insitro.github.io/redun/"
    }
  ]
}
```

This is conformant with Workflow Run Crate 0.5; LinkML-validates against `profiles/workflow_run_crate.yaml`.

---

## 4. in-toto + DSSE attestation chain

Per `tools_infra_stack.md` Standards Inventory §3, CAP already uses in-toto-style chains. We extend the same pattern to every workflow run.

The chain has three signed steps:

### 4.1 Source step

```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "swh:1:rev:2c79bff0a06f4cb1f6b3...",
      "digest": {"sha1-git": "2c79bff0a06f4cb1f6b3..."}
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://github.com/cytognosis/cytoskeleton/source-step"
    },
    "runDetails": {
      "builder": {"id": "https://github.com/cytognosis/cytoskeleton/.github/workflows/release.yml"}
    }
  }
}
```

Signed by the cytoskeleton-publisher OIDC token (sigstore keyless).

### 4.2 Build step

```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "cytognosis-base:py3.13-cuda-v2.1.0",
      "digest": {"sha256": "9001ab74dcba4a35b..."}
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://docker.com/buildkit",
      "externalParameters": {
        "source": {"digest": {"sha1-git": "2c79bff0a06f4cb1f6b3..."}}
      },
      "resolvedDependencies": [
        {"uri": "pkg:debian/bookworm@2026.05", "digest": {"sha256": "..."}},
        {"uri": "pkg:pypi/uv@0.4.20", "digest": {"sha256": "..."}}
      ]
    },
    "runDetails": {
      "builder": {"id": "https://github.com/cytognosis/cytoskeleton/.github/workflows/build-images.yml"},
      "metadata": {
        "invocationId": "...",
        "startedOn": "2026-05-07T03:00:00Z",
        "finishedOn": "2026-05-07T03:42:18Z"
      }
    }
  }
}
```

Signed by the GH Actions OIDC token.

### 4.3 Run step

```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "outputs/biolink_nodes.tsv",
      "digest": {"sha256": "80d1d8..."}
    },
    {
      "name": "outputs/biolink_edges.tsv",
      "digest": {"sha256": "f4eb2c..."}
    }
  ],
  "predicateType": "https://w3id.org/cytognosis/run-provenance/v1",
  "predicate": {
    "instrument": {
      "swhid": "swh:1:rev:2c79bff0a06f4cb1f6b3...",
      "envName": "cytognosis-base",
      "envVersion": "v2.1.0",
      "containerImageDigest": "sha256:9001ab74dcba4a35b..."
    },
    "inputs": [
      {"uri": "cytognosis://data/sha256:91d4abf0...", "digest": {"sha256": "91d4abf0..."}}
    ],
    "parameters": {
      "biolink_version": "4.0.3",
      "include_subclass": true
    },
    "agent": {"identity": "shahin@cytognosis.org"},
    "startTime": "2026-05-18T08:30:00Z",
    "endTime": "2026-05-18T08:34:23Z"
  }
}
```

Signed by the runner's Ed25519 identity key (per CAP's mTLS + Ed25519 stack).

All three are wrapped in a DSSE envelope:

```json
{
  "payloadType": "application/vnd.in-toto+json",
  "payload": "<base64 of the three statements bundled>",
  "signatures": [
    {"keyid": "cytoskeleton-publisher", "sig": "..."},
    {"keyid": "gh-actions-oidc", "sig": "..."},
    {"keyid": "runner-shahin", "sig": "..."}
  ]
}
```

Verification (by a consumer) reads the envelope, checks each signature against the named identity's public key (sigstore keyless lookup or the cytoskeleton-published public key set), and walks the chain to confirm SLSA L3.

---

## 5. Process Run Crate (lightweight)

For one-off scripts that aren't workflows, Process Run Crate is the lighter option. It's a Workflow Run Crate where the instrument is `SoftwareSourceCode` (not `ComputationalWorkflow`). Used by:

- Yar's daily capture batches (small, frequent, not parameterized workflows).
- Ad-hoc notebooks promoted from experimentation.
- Single-file scripts in `scripts/`.

Same emission machinery, profile is `process_run_crate.yaml`.

---

## 6. Five Safes Run Crate (HIPAA)

For PHI-affected runs, the Crate is a Five Safes RO-Crate that adds:

- `safe_projects`: project-level governance record (the IRB protocol, the institutional ethics approval).
- `safe_people`: list of authorized researchers (per DUC IAM group).
- `safe_settings`: which TRE / Cloud Run env this ran in.
- `safe_data`: data-tier classification + DUC + de-id rubric.
- `safe_outputs`: per-output disclosure controls (cell-suppression thresholds, DP epsilon).

These crates do NOT mirror to public Zenodo / FAIRDOMHub. They register only in the internal SEEK behind ELIXIR-AAI auth.

---

## 7. OpenTelemetry integration

Every stage execution produces an OTel span with:

- `service.name`: cytoskeleton-runner
- `service.version`: v2.1.0
- `cytognosis.env`: cytognosis-genomics
- `cytognosis.env_version`: v2.1.0
- `cytognosis.image_digest`: sha256:9001ab...
- `cytognosis.run_id`: ...
- `cytognosis.workflow_swhid`: swh:1:rev:...

The trace ID is recorded in the Crate's `cytognosis:otelTraceId`. Cloud Trace / Tempo retains the trace for 30 days; the Crate's reference lets us re-correlate after-the-fact.

---

## 8. Engine-specific plugins

Each engine gets a thin plugin that emits the same Crate format:

| Engine | Plugin | Provenance source |
|---|---|---|
| redun | `cytoskeleton.redun_plugin` | redun's lineage graph |
| Nextflow | `cytoskeleton.nextflow_plugin` (extends nf-prov) | Nextflow's trace + nf-prov |
| Snakemake | `cytoskeleton.snakemake_plugin` | Snakemake's report + report-html |
| Galaxy | `cytoskeleton.galaxy_plugin` | Galaxy's history export (already RO-Crate emitter exists upstream) |
| Kedro | `cytoskeleton.kedro_plugin` | Kedro's session store + DataCatalog |
| DVC | `cytoskeleton.dvc_plugin` | dvc.lock + dvc.yaml |

All five normalize into the same WRROC schema. cytos's Kedro pipelines and redun pipelines emit interoperable Crates.

---

## 9. LifeMonitor integration

LifeMonitor (https://lifemonitor.eu/) consumes a Workflow Testing RO-Crate (an extension of Workflow RO-Crate with test-engine metadata). Our `profiles/workflow_run_crate.yaml` adds an optional `cytognosis:tests` slot for test crates. The Cytognosis WorkflowHub instance is wired to LifeMonitor so any published workflow with tests gets automatically monitored.

Test engines supported: PlanemoTest (Galaxy), NextflowTest (Nextflow), SnakemakeTest, Pytest (for redun + Kedro).

---

## 10. Failure modes

| Failure | Symptom | Detection | Response |
|---|---|---|---|
| Input hash mismatch | input file at expected URI returns different sha256 | VFS verify at run start | Fail fast; print diff URI; require explicit refresh |
| Output hash divergence | run produced different output than recorded baseline | post-run verify against `expected_dvc_md5` | Mark run "DIVERGENT"; emit Crate with status; require `--accept-divergence` to publish |
| Image signature invalid | cosign verify fails | pre-pull check in `cytoskeleton run` | Fail; never run unsigned images for PHI envs |
| SWH submission lag | SWHID minting takes >24h | release CI polls; if not ingested, raise warning | Continue with local SWHID; CI retries on schedule |
| LaminDB outage | log_to_lamindb raises | best-effort logging | Run continues; queue retry log |
| MLflow outage | log_to_mlflow raises | best-effort logging | Run continues; queue retry log |
| Crate validation failure | LinkML validate fails on emitted Crate | post-emit step | Fail; write a `crate-issues.txt` next to Crate; require manual fix |

---

## 11. Open questions

1. **DSSE key management**: Ed25519 keys for runners. Are they per-user (researcher's key, like a git signing key) or per-machine? Recommendation: per-user; stored in Cloud KMS for centralized rotation.

2. **Crate size**: a single ML training run might output 50 GB of checkpoints. Do we inline outputs into the Crate, or reference them with content-hash + external URI? Recommendation: reference-only by default; inline only for small outputs (<100 MB total).

3. **Publishing cadence**: do we publish every run, only releases, or both? Recommendation: emit Crate per run locally; only publish on release tag or explicit `cytoskeleton publish`. Per-run Crates stay in `.crates/` for diffing.

4. **Public vs internal**: a public workflow with internal runs (e.g., the cytos KG build code is public, but specific runs may use PHI). Recommendation: WRROC marks `safe_data` tier; publish-to-public route filters out Tier 1/2 runs.

5. **Crate diff**: two runs of the same workflow produce two Crates. We want a `cytoskeleton crate diff` command. Recommendation: implement post v0.1; useful for "what changed between cytos KG v0.4.0 and v0.5.0".

6. **Provenance Run Crate vs Workflow Run Crate**: Provenance Run Crate is a strict superset of Workflow Run Crate with more activity-level detail (per RO-Crate community profiles). Do we always emit Provenance Run Crate? Recommendation: yes for redun + Nextflow (which capture per-task lineage); WRROC-only for DVC stages that don't have per-stage agent provenance.
