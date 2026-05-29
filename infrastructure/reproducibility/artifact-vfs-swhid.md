<!-- Last updated: 2026-05-22 | Source: Plans/design/11_reproducibility_strategy/ -->
**← [Back to Reproducibility Index](README.md)**

# 02 — Artifact Storage: VFS + SWHID

**Reading order**: read `00_master_strategy.md` §5 first; this file expands that section.

This document defines the Virtual File System (VFS) module that lives in cytoskeleton and makes artifacts location-independent, content-addressed, and verifiable. It also defines the SWHID-driven config conventions.

---

## 1. The problem (concrete)

Three concrete pain points motivate this layer:

1. **Path coupling**. cytos `dvc.yaml` references `${data_lake}/05-annotations/topic-areas/`; if the data lake moves from `~/datasets/` to `gs://cytognosis-data/datasets/`, the pipeline breaks until every config is rewritten.

2. **Provenance gaps**. cytos `ro-crate-metadata.json` records `nodes.tsv` and `edges.tsv` but doesn't hash them in the Crate; a third party can't verify "this is the same nodes.tsv". The Cytos sensor universal schema design §7 open question 5 calls out the same issue for waveform URIs.

3. **No re-runnability across machines**. The cytoskeleton 66-cell env matrix lets the env be reproduced, but the data inputs are referenced by path, and the executor image is pulled by tag (mutable) not digest.

The VFS + SWHID strategy fixes all three.

---

## 2. The substrate: cytognosis:// URI scheme

Every artifact in the Cytognosis world has a canonical identifier. We unify them under a `cytognosis://` URI scheme:

```
cytognosis://code/<swhid>                  # source code archived in Software Heritage
cytognosis://data/<algo>:<hash>            # data file content-addressed
cytognosis://data/dvc:md5:<hash>           # DVC-tracked data
cytognosis://data/sha256:<hash>            # raw blob
cytognosis://data/tiledb:<uri>             # TileDB group / array
cytognosis://image/sha256:<digest>         # OCI container image
cytognosis://crate/<doi-or-urn>            # published RO-Crate
cytognosis://model/hf:<org>/<repo>@<rev>   # Hugging Face model
cytognosis://model/sha256:<hash>           # ad-hoc model file (safetensors, GGUF, ONNX)
cytognosis://schema/<linkml-uri>@<ver>     # LinkML schema version
cytognosis://workflow/trs:<id>@<ver>       # GA4GH TRS-registered workflow
cytognosis://annotation/<wadm-uri>         # W3C Web Annotation
```

These URIs are stable across storage backends. A consumer never sees a file path; they see a URI.

### 2.1 Examples

```
cytognosis://code/swh:1:rev:2c79bff0a06f4cb1f6b3...
cytognosis://data/sha256:f5bf89d001459f5526daed52fb5e0c12745c5...
cytognosis://image/sha256:9001ab74dcba4a35b...
cytognosis://crate/doi:10.5281/zenodo.7777777
cytognosis://model/hf:cytognosis/cytoscope-foundation-v1@a1b2c3d
cytognosis://schema/https://w3id.org/cytognosis/cytos@2026.05.0
```

---

## 3. The VFS module

`cytoskeleton/src/cytoskeleton/vfs/` is a Python package with:

```
vfs/
├── __init__.py
├── api.py              # public functions: resolve(), open(), read_bytes(), exists(), hash(), put()
├── uri.py              # parse / build cytognosis:// URIs
├── chain.py            # the resolver chain (ordered list of drivers)
├── verify.py           # hash verification
├── drivers/
│   ├── base.py         # abstract Driver class
│   ├── local.py        # local data lake (~/datasets/, /tmp/cytognosis/)
│   ├── dvc.py          # DVC remote (reads .dvc/config + cache)
│   ├── gcs.py          # raw GCS bucket
│   ├── drive.py        # Google Drive (read-only, requires OAuth)
│   ├── swh.py          # Software Heritage API
│   ├── zenodo.py       # Zenodo records (read + write via deposition API)
│   ├── hf.py           # Hugging Face Hub
│   ├── tiledb.py       # TileDB groups
│   └── http.py         # generic HTTP fallback
├── config.py           # load VFS config from .cytognosis-config.yaml
└── tests/
```

### 3.1 The public API

```python
from cytoskeleton import vfs

# Resolve to a local path (downloads if needed)
local_path = vfs.resolve("cytognosis://data/sha256:f5bf89d0014...")
# Returns: PosixPath("/tmp/cytognosis-cache/f5/bf/f5bf89d0014...bin")

# Open as a file-like handle
with vfs.open("cytognosis://data/sha256:...", mode="rb") as f:
    data = f.read()

# Read bytes directly
data = vfs.read_bytes("cytognosis://data/sha256:...")

# Check existence (across all drivers in the chain)
if vfs.exists("cytognosis://data/sha256:..."):
    ...

# Compute / verify hash
h = vfs.hash("cytognosis://data/sha256:...")  # returns the sha256

# Put a new artifact (uploads to the configured primary driver; returns the cytognosis:// URI)
uri = vfs.put(local_path, content_type="application/octet-stream")
# uri = "cytognosis://data/sha256:..."
```

### 3.2 Driver chain

The chain is configured per environment in `.cytognosis-config.yaml`:

```yaml
# .cytognosis-config.yaml
vfs:
  chain:
    - driver: local
      roots:
        - ~/datasets
        - /tmp/cytognosis-cache
    - driver: dvc
      remote: cytognosis-data
    - driver: gcs
      buckets:
        - cytognosis-data
        - cytognosis-public
    - driver: zenodo
    - driver: swh
    - driver: http
  cache:
    location: ~/.cache/cytognosis/vfs
    max_size_gb: 100
    eviction: lru
  hipaa:
    forbid_drivers: [drive, http]
    tier: 1
```

A `resolve()` call walks the chain top-to-bottom. The first driver that returns a hit wins. Hits are cached locally for the configured size.

### 3.3 HIPAA mode

For Tier 1 (PHI) workflows, the chain forbids `drive`, `http`, and `hf` drivers. The `gcs` driver is restricted to `cytognosis-phi-prod` and `cytognosis-phi-staging` buckets. The cache directory is configured to be inside the VPC SC perimeter.

### 3.4 Put semantics

`vfs.put(local_path)` computes the sha256, uploads to the primary writable driver, returns the cytognosis:// URI. For HIPAA data, "primary writable" is the appropriate PHI bucket. For non-PHI, it's `cytognosis-data` by default; researcher can override.

`vfs.put_dvc(local_path, dvc_yaml_stage=...)` is the DVC-specific variant that adds the artifact as a DVC `outs:` entry, computes the md5 (DVC's algorithm), and stages it for `dvc push`.

---

## 4. SWHID minting

`cytoskeleton/src/cytoskeleton/attest/swhid.py` provides:

```python
from cytoskeleton.attest import swhid

# Compute a SWHID locally (no network call needed for swh:1:cnt:<sha1_git>)
sha1git = swhid.compute_content_swhid("/path/to/file")
# Returns: "swh:1:cnt:abcdef1234..."

# Compute a directory SWHID
dir_swhid = swhid.compute_directory_swhid("/path/to/repo")
# Returns: "swh:1:dir:..."

# Compute a revision (commit) SWHID from a git repo
rev_swhid = swhid.compute_revision_swhid("/path/to/repo", ref="HEAD")
# Returns: "swh:1:rev:..."

# Submit to Software Heritage (idempotent — checks before re-submitting)
swhid_url, status = swhid.archive_to_swh("/path/to/repo", origin_url="https://github.com/cytognosis/cytos")
# Returns: ("swh:1:rev:...", "scheduled" | "ingested")
```

SWH submission goes through their save-code-now API (https://archive.softwareheritage.org/api/1/origin/save/). The CI workflow on `release` tags triggers this; the resulting SWHID is annotated on the GitHub release.

### 4.1 Why SWHID

Per ISO 18670:2025, SWHID is a perceptually deterministic hash of code that any actor can compute locally and verify against the public archive. It's the right primitive for citing code at a specific revision; DOIs are too coarse (one per release), commit hashes are too repository-coupled.

---

## 5. SWHID-driven configs (worked example)

Today's cytos source config:

```yaml
# cytos/configs/sources/biolink.yaml (today)
id: biolink
description: Biolink Model ontology
url: https://github.com/biolink/biolink-model
license: CC0
files:
  - path: ${data_lake}/01-ontologies/owl/biolink-model.owl
    expected_sha256: 91d4...
parser: owl_to_kgx
```

Rewritten with VFS + SWHID:

```yaml
# cytos/configs/sources/biolink.yaml (target)
id: biolink
description: Biolink Model ontology
license: CC0-1.0
upstream:
  code_swhid: swh:1:rev:de7af67c91...           # biolink-model repo at a specific revision
  download_origin: https://github.com/biolink/biolink-model
inputs:
  - id: biolink_model_owl
    uri: cytognosis://data/sha256:91d4abf0...
    encoding_format: application/rdf+xml
parser:
  language: python
  module: cytos.ingest.parsers.owl
  swhid: swh:1:rev:2c79bff0a06f4cb1f6b3...      # this repo at the parser revision
  env: cytognosis-base@v2.1.0
  image: cytognosis://image/sha256:9001ab74dcba4a35b...
outputs:
  - id: biolink_nodes
    expected_dvc_md5: 80d1d8...
  - id: biolink_edges
    expected_dvc_md5: f4eb2c...
runner: redun
emit_crate: workflow_run_crate
```

The runner (redun in this case) reads this, resolves every cytognosis:// URI via the VFS, verifies every expected hash, and runs the parser inside the pinned image. Outputs are uploaded with computed hashes; if they don't match `expected_dvc_md5`, the run is flagged DIVERGENT.

### 5.1 Generating dvc.yaml

`cytoskeleton.dvc.generate` reads these LinkML-typed source configs and emits a `dvc.yaml` stage spec:

```yaml
# generated dvc.yaml stage (auto)
stages:
  biolink:
    cmd: cytoskeleton run configs/sources/biolink.yaml
    deps:
      - configs/sources/biolink.yaml
    outs:
      - data/kg/biolink_nodes.tsv:
          md5: 80d1d8...
      - data/kg/biolink_edges.tsv:
          md5: f4eb2c...
    meta:
      cytognosis:
        runner: redun
        env: cytognosis-base@v2.1.0
        image_digest: sha256:9001ab74dcba4a35b...
        parser_swhid: swh:1:rev:2c79bff0a06f...
```

Humans don't edit dvc.yaml directly; they edit the LinkML source configs. CI regenerates dvc.yaml on commit.

---

## 6. Hashing strategy

Different artifact classes use different hashes by convention:

| Class | Algorithm | Why |
|---|---|---|
| Source code | SWHID (sha1-git) | Software Heritage ISO standard |
| DVC-tracked data | md5 | DVC's algorithm; can't change |
| Other data files | sha256 | broadly standard, fast |
| OCI images | sha256 (digest) | OCI registry standard |
| Models on HF | HF revision (sha1-git) | git-based |
| Models off-HF | sha256 | as above for data |
| RO-Crates (zipped) | sha256 of zip | downstream verification |
| TileDB groups | TileDB fragment URIs + checksum | TileDB-native |
| Schemas | LinkML URL + SemVer | versioned not hashed |

For belt-and-suspenders integrity, every RO-Crate File entity carries both the algorithm's canonical hash AND a sha256 in metadata extras.

---

## 7. Driver implementations

### 7.1 Local driver

Resolves URIs against the local filesystem cache. Cache layout:

```
~/.cache/cytognosis/vfs/
├── sha256/
│   └── f5/bf/f5bf89d001459f5526daed52fb5e0c12745c5...
├── dvc-md5/
│   └── 80/d1/80d1d8...
├── swh-cnt/
│   └── ab/cd/abcdef1234...
└── manifest.db   # SQLite mapping URI → cache path + last_used + size
```

The cache is LRU-evicted to stay under the configured size limit.

### 7.2 DVC driver

Reads `.dvc/config` to find the active remote, then uses `dvc fetch --remote <name>` to pull the artifact by md5 into the DVC cache. The cache path becomes the resolved path.

### 7.3 GCS driver

Standard `gcsfs` + `google-cloud-storage` client. Auth via Application Default Credentials. Reads from buckets listed in the config; respects HIPAA tier restrictions.

### 7.4 SWH driver

Calls the SWH API:

```
GET https://archive.softwareheritage.org/api/1/content/sha1_git:{hash}/raw/
GET https://archive.softwareheritage.org/api/1/revision/{swhid}/
```

Caches the result locally; SWH downloads can be slow.

### 7.5 Zenodo driver

For published Crates: calls Zenodo deposition API to read by DOI. For internal publish: uses the deposition API to upload new records.

### 7.6 HF driver

`huggingface_hub` client; resolves `hf:<org>/<repo>@<rev>` to `hf_hub_download(repo_id="<org>/<repo>", filename=..., revision="<rev>")`.

### 7.7 TileDB driver

Resolves `tiledb:` URIs to TileDB `Array` or `Group` URIs (which can themselves be `s3://`, `gs://`, or `file://`). Verifies TileDB fragment integrity via `tiledb.array_consolidate_metadata` checksums.

---

## 8. Migration plan

### 8.1 Today → SWHID-driven (per repo)

| Step | What | Effort |
|---|---|---|
| 1 | Add `cytoskeleton/src/cytoskeleton/vfs/` package | 1 week |
| 2 | Implement local + DVC + GCS drivers | 1 week |
| 3 | Implement SWH + Zenodo + HF drivers | 3 days |
| 4 | Add `cytoskeleton.vfs` CLI: `cytoskeleton vfs resolve <uri>`, `cytoskeleton vfs put <path>`, `cytoskeleton vfs hash <path>` | 2 days |
| 5 | Migrate one cytos source config (biolink) end-to-end | 2 days |
| 6 | Auto-rewrite remaining cytos configs (10 sources) | 1 day |
| 7 | Migrate cytos dvc.yaml to generated-from-LinkML | 3 days |
| 8 | Migrate one Yar capture config | 2 days |
| 9 | Update cytoskeleton.crate emitter to write VFS URIs | 2 days |
| 10 | Documentation + cytognosis-data skill update | 2 days |

Total: ~5 weeks for the VFS layer + first migration.

### 8.2 Phase ordering

This is part of Phase 1 (cytoskeleton v2) per the master plan extension, with the cytos migration landing in Phase 6 (cytos transition).

---

## 9. Verification semantics

`cytoskeleton run <config>` does at start:

1. For every `inputs[].uri`, resolve via VFS, compute hash, compare to expected. Fail fast if mismatch.
2. For every code SWHID, verify the local checkout matches (compute revision SWHID via `swhid.compute_revision_swhid`). Fail if drift.
3. For every container image digest, pull (or check locally cached) and verify against digest. Fail if mismatch.
4. For every schema reference, verify the LinkML schema parses and matches the pinned version.

At end:

5. For every output, compute hash, compare to `expected_dvc_md5` / `expected_sha256` (after first successful run, before subsequent runs).
6. If divergence, write a `divergence-report.json` to the run directory listing every mismatched output with old/new hashes.

The run still succeeds if outputs diverge from expectation (researcher might be testing changes); but `cytoskeleton publish` blocks unless the researcher explicitly approves the new hashes ("snapshot baseline").

---

## 10. Open questions

1. **Per-bucket key rotation**: GCS CMEK keys rotate every 90 days. Does the VFS cache invalidation handle "old key was used to encrypt this object on storage; new key needed to read"? Recommendation: GCS handles this transparently for the consumer; VFS doesn't need to know.

2. **TileDB group hashing**: TileDB doesn't expose a stable "group-level" hash; you have to fingerprint fragments. Do we accept "fragment-set hash" as the canonical identity, or treat TileDB groups as opaque-but-named (no hash verification)? Recommendation: opaque + named (with version), document the limitation.

3. **Long-running Drive ingest**: when fetching from Drive, OAuth flow is non-trivial. Should VFS support service-account auth into a "Cytognosis Library" shared drive? Recommendation: yes, but Drive driver stays read-only; writes go via Drive's web UI.

4. **Cache size on edge devices**: a phone-side Yar agent can't host 100 GB cache. Cache config supports per-device profiles. Recommendation: ship a `cytognosis-config-edge.yaml` template with 1 GB cache + aggressive eviction.

5. **HF revision pinning**: HF supports pinning by commit hash but not by tree-hash; trees can be mutated without changing the commit hash via cache LFS quirks. Recommendation: always store the HF commit hash AND the file's sha256 in the Crate.
