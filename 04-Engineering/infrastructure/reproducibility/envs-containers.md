<!-- Last updated: 2026-05-22 | Source: Plans/design/11_reproducibility_strategy/ -->
**← [Back to Reproducibility Index](README.md)**

# 03 — Environments and Containers

**Reading order**: read `00_master_strategy.md` §6 first.

This document extends the cytoskeleton `envs/` matrix with: containerization, multi-arch builds, sigstore signing, OCI digest pinning, and SLSA-level attestation. The result is that every workflow stage can be invoked against a specific env, and the env materializes as a reproducible container that consumers verify before pulling.

---

## 1. Current state (Phase 0)

Cytoskeleton v0.4.0 (`feat/component-restructure` branch):

- 78 Python components, 4 R components.
- 14 named environments (cytognosis-base, cytognosis-genomics, cytognosis-neuro, cytognosis-singlecell, cytognosis-sensor, cytognosis-llm, …).
- 66-cell resolution matrix (14 envs × Python 3.11/3.12/3.13 × cpu/cuda/rocm), all passing.
- Lockfiles per env-cell: uv.lock, requirements.txt, pyproject.toml, package.json.
- Component graph resolver with `when:` blocks for backend-conditional deps.
- 19+ nox sessions, 6 GH Actions workflows.

What's missing: containers, multi-arch builds, image signing, image-digest pinning.

---

## 2. Target structure

```
cytoskeleton/
├── envs/
│   ├── components/
│   │   ├── python/         # 78 components (existing)
│   │   ├── r/              # 4 components (existing)
│   │   ├── js/             # NEW (Phase 1)
│   │   ├── dart/           # NEW (Phase 1)
│   │   └── rust/           # NEW (Phase 1)
│   ├── environments/       # 14+ named env YAMLs
│   ├── activation_hooks/
│   └── locked/             # NEW: per env-cell locks
│       └── <env>/
│           ├── python-3.13/
│           │   ├── cpu/
│           │   │   ├── uv.lock
│           │   │   ├── requirements.txt
│           │   │   ├── pyproject.toml
│           │   │   └── oci.lock           # NEW: pinned image digest
│           │   ├── cuda/
│           │   │   └── ...
│           │   └── rocm/
│           │       └── ...
│           └── ...
├── containers/             # NEW
│   ├── README.md
│   ├── _base/
│   │   ├── Dockerfile.cpu       # debian:bookworm + Python 3.13 + uv + system deps
│   │   ├── Dockerfile.cuda      # nvidia/cuda:12.4-runtime-ubuntu24.04 + Python + uv
│   │   ├── Dockerfile.rocm      # rocm/dev-ubuntu-24.04 + Python + uv
│   │   └── build-args.yaml
│   ├── cytognosis-base/
│   │   ├── Dockerfile           # FROM cytognosis-base-{backend}; copies env's locked deps
│   │   └── manifest.yaml
│   ├── cytognosis-genomics/
│   ├── cytognosis-neuro/
│   ├── cytognosis-singlecell/
│   ├── cytognosis-sensor/
│   ├── cytognosis-llm/
│   ├── cytognosis-r/            # R-based env
│   ├── cytognosis-bids-apps/    # mirrors of 7 BIDS-App images
│   └── _build.py                # tooling that drives buildx for all envs × backends
└── _shared/                     # (lives in cytocast; Cytoskeleton inherits these workflows)
    └── .github/workflows/
        ├── build-images.yml     # multi-arch buildx + sigstore signing + SLSA provenance
        ├── refresh-locks.yml
        └── deps.yml
```

---

## 3. Image design principles

### 3.1 Layer separation

A two-tier image structure minimizes rebuild cost:

- **Base image** (`cytognosis-base-cpu:debian-bookworm-py3.13-2026.05`, etc.): debian-slim + Python 3.13 + uv + system libs that almost all envs need. Rebuilt monthly via Renovate.
- **Env image** (`cytognosis-genomics:py3.13-cuda-v2.1.0`, etc.): `FROM cytognosis-base-{backend}`; copies the env's `uv.lock`; runs `uv sync --frozen --no-dev`. Rebuilt on env lock change.

This gives ~2-5 GB per env image (mostly Python wheels + CUDA libs) on top of a ~500 MB base.

### 3.2 Multi-arch (amd64, arm64)

Edge devices (Cytoscope, Yar Tauri) run arm64. The sensor env image builds for both amd64 + arm64 via buildx and pushes a manifest list under one tag.

### 3.3 Reproducible builds

Build with `SOURCE_DATE_EPOCH` pinned to the cytoskeleton release commit's timestamp; `uv sync --frozen` for deterministic dep resolution; locked apt package versions in the base image (via `apt-pinning.yaml`). The resulting image digest is stable across rebuilds with the same source.

### 3.4 SLSA Level 3 + sigstore

The build workflow runs in GH Actions with OIDC ID-token signing. Every pushed image gets:

- A sigstore signature (`cosign sign --keyless`).
- A SLSA Build Provenance attestation (in-toto layout linking source SWHID → builder → image digest).
- A SBOM (CycloneDX) attached as an OCI artifact.

Consumers verify before pull:

```bash
$ cosign verify --certificate-identity-regexp \
    "^https://github.com/cytognosis/cytoskeleton.*" \
    us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/cytognosis-genomics:py3.13-cuda-v2.1.0
$ cosign verify-attestation --type slsaprovenance ...
```

`cytoskeleton run` does this verification automatically.

### 3.5 Vulnerability scans

Renovate-driven monthly rebuilds keep base images patched. Each push triggers a Trivy scan; CRITICAL CVEs block the publish until a workaround is found.

---

## 4. Image manifest

Every env has a `containers/{env}/manifest.yaml` declaring:

```yaml
# containers/cytognosis-genomics/manifest.yaml
env: cytognosis-genomics
version: v2.1.0
backends:
  - cpu
  - cuda
  - rocm
python_versions:
  - "3.13"
arch:
  - amd64
build:
  source_date_epoch: 1746540000   # 2026-05-07T00:00:00Z
  build_args:
    PYTHON_VERSION: "3.13"
    UV_VERSION: "0.4.20"
base_image:
  cpu: cytognosis-base-cpu:debian-bookworm-py3.13-2026.05@sha256:abc123...
  cuda: cytognosis-base-cuda:debian-bookworm-py3.13-cu124-2026.05@sha256:def456...
  rocm: cytognosis-base-rocm:debian-bookworm-py3.13-rocm6.2-2026.05@sha256:789abc...
registry: us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute
signing:
  enabled: true
  identity: cytoskeleton-publisher@cytognosis-infrastructure.iam.gserviceaccount.com
sbom:
  enabled: true
  format: cyclonedx
extra_apt_packages:
  - tabix
  - bcftools
  - samtools
extra_pip_packages:
  - pysam
  - cyvcf2
```

The build orchestrator (`_build.py`) reads this manifest and drives buildx for every combination.

---

## 5. oci.lock

Alongside `uv.lock` etc., each env-cell has an `oci.lock`:

```yaml
# envs/locked/cytognosis-genomics/python-3.13/cuda/oci.lock
env: cytognosis-genomics
version: v2.1.0
backend: cuda
python: "3.13"
images:
  primary:
    registry: us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute
    repository: cytognosis-genomics
    tag: py3.13-cuda-v2.1.0
    digest: sha256:9001ab74dcba4a35b87f4c8e3d2a1f0e9b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1
    architectures:
      - linux/amd64
    build_provenance: oci-artifact://.../sha256:abc123...
    sigstore_signature: oci-artifact://.../sha256:def456...
  fallback:
    # in case primary registry is down, allow pulling from a mirror
    registry: ghcr.io/cytognosis
    repository: cytognosis-genomics
    digest: sha256:9001ab74dcba4a35b...
```

Consumers reference an env by name + version; the runner reads `oci.lock` to get the exact digest.

---

## 6. JavaScript / Dart / Rust components

Per the cytoskeleton refactor plan, JS/Dart/Rust components are scoped narrowly: they declare deps for app-templates (Flutter, React, Tauri). The resolver doesn't lock JS/Dart/Rust the way it locks Python; instead, each language gets a "manifest snapshot" file listing resolved versions at template-build time:

```yaml
# envs/components/dart/yar_mobile_runtime.yaml
component: yar_mobile_runtime
language: dart
deps:
  flutter_gemma:
    version: 0.13.6
  http:
    version: 1.2.1
  path_provider:
    version: 2.1.4
snapshot:
  # this snapshot is generated by `dart pub get` against pub.dev at lock-refresh time
  generated_at: 2026-05-07T12:00:00Z
  pubspec_lock_path: envs/locked/yar_mobile/dart/pubspec.lock
```

The Flutter / Tauri / React templates run `flutter pub get` / `pnpm install` / `cargo build --locked` at the generated project's level, using `pubspec.lock` / `pnpm-lock.yaml` / `Cargo.lock` for their own determinism. Cytoskeleton's role is to vendor consistent lockfiles into the template's seed.

---

## 7. Container consumption

Three patterns for using the images:

### 7.1 Local development

```bash
$ cytoskeleton env activate cytognosis-genomics --backend cuda --python 3.13
# Pulls the image (digest from oci.lock), runs a container with $PWD mounted,
# drops the user into bash inside the container.
```

### 7.2 redun stage execution

`redun run` reads the stage's `env: cytognosis-genomics@v2.1.0` annotation; resolves to digest via cytoskeleton's `envs/locked/.../oci.lock`; submits to the configured executor (local docker, Cloud Run, GKE, HPC).

### 7.3 Nextflow / Snakemake / Galaxy

Cytoskeleton exposes a `cytoskeleton env containerfile <env>` CLI that prints the digest-pinned image reference suitable for Nextflow `container 'image:digest'` or Snakemake `container:` directives. Workflow authors don't manage image references; they reference an env name + version.

---

## 8. PHI / HIPAA image admission

For Tier 1 workloads, Cloud Run / Vertex AI / GKE admission policy verifies:

1. Image is from the Cytognosis registry (not a public mirror).
2. Image has a valid sigstore signature signed by a Cytognosis identity.
3. Image's SLSA provenance has the expected source SWHID.
4. Image was built within the last 90 days (rotation policy).

Failed admissions are logged to Cloud Audit Logs (7-yr retention per `audit-log-retention.md`) and Pager-Duty-paged.

---

## 9. Lock refresh cycle

Monthly Renovate-driven cycle:

1. Renovate proposes Python/Node/Dart/Rust dep bumps.
2. `nox -s refresh_locks` regenerates uv.lock / requirements.txt / oci.lock per env-cell.
3. CI rebuilds + tests every changed env (the 66-cell matrix).
4. PR auto-merges if all matrix cells pass.
5. Release-please opens a release PR for affected envs.
6. On merge to main, GH Actions builds + signs + pushes new images; cytoskeleton publishes a new env version.
7. Downstream packages (cytos, Yar, neuro-*) get a Renovate PR bumping their `.cytognosis-config.yaml` `env:` reference.

---

## 10. Open questions

1. **Base image distro**: debian vs ubuntu vs distroless? Recommendation: debian-bookworm-slim for both base and env images; distroless for production runtime images that don't need apt.

2. **Docker Hub mirror**: should we mirror our images to Docker Hub for offline / network-constrained users? Recommendation: no by default; mirror on-demand if a collaborator asks.

3. **ROCm coverage**: rocm/dev-ubuntu-24.04 is heavy (~12 GB). For sensor/edge envs that don't need GPU, we don't ship a rocm variant. Recommendation: rocm is opt-in per env via the env's `backends:` list in `manifest.yaml`.

4. **arm64 build cost**: arm64 builds are 2-3× slower on emulated x86 runners. Recommendation: use buildx + native arm64 runners (GH Actions arm64 runners landed Q4 2024); fall back to emulation for envs that rarely change.

5. **Image size targets**: cytognosis-llm is currently ~25 GB (cuda + torch + transformers). Recommendation: split into cytognosis-llm-inference (lighter, runtime only) and cytognosis-llm-train (full).

6. **Apptainer / Singularity coverage**: HPC sites want SIF. Recommendation: ship an apptainer-build job alongside docker-build; publish .sif to the registry too.
