<!-- Last updated: 2026-05-22 | Source: Plans/design/11_reproducibility_strategy/ -->
**← [Back to Reproducibility Index](README.md)**

# 06 — Acceptance Gates and KPIs

**Reading order**: read `00_master_strategy.md` first; this file makes the implicit "done" criteria from every other doc explicit and measurable.

---

## 1. Acceptance gates (binary, per phase)

### 1.1 Phase 1 (cytoskeleton v2) — reproducibility additions

- [ ] `schemas/profiles/isa.yaml` validates via `linkml-validate`.
- [ ] `schemas/profiles/ro_crate.yaml`, `workflow_ro_crate.yaml`, `workflow_run_crate.yaml`, `process_run_crate.yaml`, `five_safes_crate.yaml` all validate.
- [ ] `schemas/profiles/bioschemas/computational_workflow.yaml` validates.
- [ ] `schemas/profiles/sosa_ssn.yaml` (migrated from cytos sensor universal) validates.
- [ ] `cytoskeleton.vfs.api` resolves a sha256 URI from local + DVC + GCS drivers; tests pass.
- [ ] `cytoskeleton.attest.swhid.compute_content_swhid` matches `swh:1:cnt:` from `swh-id` CLI on the same file.
- [ ] `cytoskeleton.crate.WorkflowRunCrateBuilder` emits a Crate that LinkML-validates against `workflow_run_crate.yaml`.
- [ ] `cytoskeleton.isa.serialize.to_isa_json` produces ISA-JSON that parses with the official `isatools` Python library.
- [ ] `containers/cytognosis-base/Dockerfile.cpu` builds successfully; image pushes to GCP Artifact Registry; cosign signature attaches.
- [ ] `envs/locked/cytognosis-base/python-3.13/cpu/oci.lock` exists and references a real registry digest.
- [ ] `cytoskeleton env containerfile cytognosis-base` returns the digest from oci.lock.
- [ ] `nox -s schemas_validate` passes 0 errors.
- [ ] `nox -s vfs_test` passes 0 errors.
- [ ] `nox -s crate_smoke` passes (end-to-end: run a stub task → emit Crate → validate).

### 1.2 Phase 5 (data + HIPAA) — hubs bring-up

- [ ] `hub.cytognosis.org` resolves; SEEK login works (Google OAuth + ELIXIR-AAI).
- [ ] `workflows.cytognosis.org` resolves; same auth.
- [ ] `lifemonitor.cytognosis.org` resolves; can register a workflow.
- [ ] A test SEEK Investigation can be created via REST API from `cytoskeleton.seek.client`.
- [ ] A test Workflow can be uploaded via REST API from `cytoskeleton.workflowhub.client`.
- [ ] GA4GH TRS endpoint `/ga4gh/trs/v2/tools` returns the test workflow.
- [ ] Cloud SQL backups configured; tested restore in staging.
- [ ] Cloud Run admission policy verifies sigstore signature; admission rejects unsigned images.
- [ ] BAA inventory + DUC IAM pattern + audit-log retention + risk assessment + incident response runbook + contingency plan + PIA template + member-inference eval all written.

### 1.3 Phase 6 (cytos transition) — first consumer

- [ ] `cytos/configs/sources/biolink.yaml` rewritten to SWHID-driven format.
- [ ] Remaining 10 source configs rewritten.
- [ ] `cytos/dvc.yaml` auto-generated from LinkML source configs; matches existing structure.
- [ ] `cytos.kg.builder` invocation emits a Workflow Run Crate to `.crates/<run-id>/`.
- [ ] Emitted Crate validates against `workflow_run_crate.yaml`.
- [ ] `cytoskeleton publish run .crates/<run-id>/ --to workflowhub` registers the workflow.
- [ ] Zenodo DOI minted for the release.
- [ ] SWHID minted for cytos code via Software Heritage.

### 1.4 Phase 7 (Yar) — second consumer

- [ ] Yar capture batch emits a Process Run Crate.
- [ ] Crate uploaded to hub.cytognosis.org as an ISA Study (per-user namespace).
- [ ] CAP attestation chain embedded in the Crate verifies cleanly.

### 1.5 Phase 11 (reproducibility hub bring-up — NEW phase)

- [ ] End-to-end test from a third-party machine:
   1. `cytoskeleton reproduce 10.5281/zenodo.<doi>` resolves a published Crate.
   2. Resolves code via SWHID.
   3. Pulls signed image by digest; cosign verification succeeds.
   4. Pulls input data by hash from VFS; sha256 matches.
   5. Re-runs the workflow in the pulled image.
   6. Diffs outputs against recorded hashes.
   7. Reports REPRODUCIBLE or DIVERGENT.
- [ ] At least one cytos workflow shows GREEN status in LifeMonitor.
- [ ] At least one Yar capture batch is registered as an ISA Study in SEEK.
- [ ] Public mirror to workflowhub.eu has at least one Cytognosis workflow visible.
- [ ] Public mirror to FAIRDOMHub has at least one Cytognosis Investigation visible.

---

## 2. KPIs (continuous, measured monthly)

### 2.1 Coverage

| KPI | Target by EOY 2026 | Measurement |
|---|---|---|
| % of cytos releases emitting WRROC | ≥95% | count of releases with attached Crate / total releases |
| % of Yar capture batches emitting Process Run Crate | ≥95% | same |
| % of neuro-* (when active) releases emitting WRROC | ≥95% | same |
| % of public artifacts with verifiable in-toto chain | 100% | `cytoskeleton verify <crate>` exit code on every published artifact |
| % of Tier 1 workflows using Five Safes Crate | 100% | inspection of safe_data field |

### 2.2 Reproducibility

| KPI | Target | Measurement |
|---|---|---|
| % of cytos pipeline runs that reproduce byte-identically on a clean clone | stretch 60% | nightly CI re-runs the previous build; compares output hashes |
| % of cytos pipeline runs that reproduce equivalently (within numerical tolerance) | ≥95% | same CI, with tolerance for floating-point divergence |
| Time-to-cite for a new run | ≤10 minutes | from `cytoskeleton publish` invocation to DOI URL response |
| Time-to-reproduce a published Crate (median) | ≤30 minutes for ≤1 GB inputs | nightly CI runs `cytoskeleton reproduce` on the previous N releases |

### 2.3 Quality

| KPI | Target | Measurement |
|---|---|---|
| LifeMonitor green rate on Cytognosis workflows | ≥90% | LifeMonitor dashboard |
| Schema validation pass rate (all repos) | 100% | `nox -s schemas_validate` in every repo's CI |
| Image signature verification rate (consumer side) | 100% | every `cytoskeleton run` verifies cosign before execution |
| SWH submission success rate (first attempt) | ≥80% | SWH save-code-now API response |
| Crate validation pass rate (first attempt) | ≥95% | `cytoskeleton.crate.validate` first-attempt success on emitted Crates |

### 2.4 Adoption

| KPI | Target | Measurement |
|---|---|---|
| Cytognosis workflows registered on workflows.cytognosis.org | ≥20 by EOY 2026 | SEEK count |
| Cytognosis workflows mirrored to workflowhub.eu | ≥10 by EOY 2026 | workflowhub.eu Programme view |
| Cytognosis Investigations on hub.cytognosis.org | ≥30 by EOY 2026 | SEEK count |
| Cytognosis Investigations mirrored to FAIRDOMHub | ≥10 by EOY 2026 | FAIRDOMHub Programme view |
| External citations to Cytognosis Crates (DOI lookups) | ≥5 by EOY 2026 | CrossRef Event Data |

### 2.5 Operational

| KPI | Target | Measurement |
|---|---|---|
| hub.cytognosis.org + workflows.cytognosis.org uptime | ≥99.5% | uptime monitor (Cloud Monitoring) |
| Median Crate publish latency (validate → DOI minted) | ≤5 minutes | publish receipt timestamps |
| Cloud Run cold start latency (SEEK) | ≤2s for cached, ≤10s cold | Cloud Run metrics |
| GCS egress cost from cytognosis-data per month | ≤$200 baseline | Billing export |

---

## 3. Definition of "Reproducible Run"

A run is **reproducible** only if:

1. **Identity**: every input + output has a canonical ID (SWHID for code, sha256/md5 for data, OCI digest for image, DOI for published Crates).
2. **Integrity**: every input/output hash matches the recorded value at verification time.
3. **Attestation**: in-toto chain verifies cleanly from source → build → run.
4. **Environment**: the exact env (lockfile + image digest) is recorded and pullable.
5. **Discoverability**: the run's Crate is registered in either hub.cytognosis.org (SEEK) or workflows.cytognosis.org (WorkflowHub), with DOI minted at release.
6. **Citability**: the run's Crate produces a BibTeX / CFF entry with at least DOI + SWHID.
7. **Re-runnability**: `cytoskeleton reproduce <crate-ref>` from a clean machine completes within the time budget and produces outputs whose hashes match (REPRODUCIBLE) or are within numerical tolerance (EQUIVALENT) — DIVERGENT outputs require explicit acknowledgement.

---

## 4. Definition of "FAIR Workflow"

A workflow is **FAIR** if it:

1. Is packaged as a Workflow RO-Crate per the WorkflowHub 1.0 profile.
2. Has a `programmingLanguage` from one of: CWL, Galaxy, KNIME, Nextflow, Snakemake (or Cytognosis-defined: redun, Kedro — for internal-only).
3. Has a `README.md` at the Crate root explaining inputs / outputs / usage.
4. Has a `test/` directory with at least one test that LifeMonitor can run.
5. Has an `examples/` directory with at least one runnable example.
6. Carries a valid SPDX license.
7. Is registered in workflows.cytognosis.org (or workflowhub.eu for public-tier).
8. Has a working LifeMonitor health badge.

---

## 5. Definition of "FAIR Dataset"

A dataset is **FAIR** if it:

1. Is a `Dataset` entity in an RO-Crate (root or referenced) with `license`, `datePublished`, `creator`, `version`, `hasPart` listing all File entities with `contentSize` + content hash (sha256 or DVC md5).
2. Has a Datasheet (LinkML `profiles/datasheet.yaml` instance) embedded in or linked from the Crate.
3. Is referenced from at least one ISA Study or ISA Assay in SEEK (hub.cytognosis.org).
4. Has at least one persistent identifier: DOI for public, ARK for internal.
5. Conforms to a domain schema profile where applicable (e.g., BIDS for neuroimaging, NWB for ephys, Universal Sensor Schema for wearables, CELLxGENE for single-cell).

---

## 6. Definition of "FAIR Model"

A model is **FAIR** if it:

1. Has a Model Card (LinkML `profiles/model_card.yaml` instance).
2. Is stored in one of: Hugging Face (public), MLflow Model Registry (internal), GCS with content-addressed key.
3. Is referenced from at least one ISA Assay in SEEK.
4. Has a persistent identifier (DOI for public; HF revision + sha256 internally).
5. The training run is published as a Workflow Run Crate; the Crate's `result` references the model artifact.

---

## 7. Verification commands

The cytoskeleton CLI exposes verification commands consumers run to check claims:

```bash
# Validate a Crate against its profile
$ cytoskeleton verify crate <path-or-doi>
# Verifies LinkML schema, RO-Crate context, in-toto chain, file hashes.

# Reproduce a Crate
$ cytoskeleton reproduce <doi-or-crate-ref>
# Fetches Crate, resolves code/data/image, re-runs, diffs outputs.

# Verify a code SWHID matches a checkout
$ cytoskeleton verify swhid /path/to/repo
# Computes local SWHID, compares to upstream SWH archive.

# Verify a container image
$ cytoskeleton verify image us-central1-docker.pkg.dev/.../cytognosis-base:py3.13-cuda-v2.1.0
# cosign verify + SLSA provenance + Trivy CVE scan.

# Audit a run
$ cytoskeleton audit run .crates/<run-id>/
# Reports: identity OK, integrity OK, attestation OK, env OK, discoverability OK, citability OK.
```

---

## 8. What "done" looks like at EOY 2026

A research community member outside Cytognosis can:

1. Find a Cytognosis paper on Zenodo / Google Scholar.
2. Click through to the cite-as DOI, land on the Workflow Run Crate in workflows.cytognosis.org or fairdomhub.org.
3. Run `cytoskeleton reproduce <doi>` on their laptop.
4. Have the workflow re-execute (pulling code by SWHID, image by digest, data by sha256) and produce outputs whose hashes match within tolerance.
5. See LifeMonitor green badge confirming the workflow's tests still pass.
6. Cite the workflow in their own paper using the BibTeX produced by `cytoskeleton cite`.

That's the bar. Every doc in this folder is in service of clearing it.
