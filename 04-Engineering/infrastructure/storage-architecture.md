# Storage Architecture: Hot/Cold Tiers, Local and Cloud, Unified Namespace

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, data scientists
> **Tags**: `storage`, `gcs`, `dvc`, `mergerfs`, `tiledb`, `cmek`

**Origin**: Imported from `/home/mohammadi/Claude/Projects/Infrastructure and Tooling/storage-architecture.md` (draft v0.1, 2026-05-10). Revised to ground truth (2026-06-14).

**Last verified: 2026-06-14**

> [!IMPORTANT]
> Ground-truth corrections applied:
> - Primary region is `us-central1` (confirmed by all existing buckets).
> - `cytognosis-data` project does NOT exist. All non-PHI buckets are in `cytognosis-infrastructure`.
> - `gs://cytognosis-mlflow-artifacts` NOW EXISTS (created 2026-06-14, `us-central1`).
> - The named buckets in §2.2 below are the planned target layout; the actual current bucket inventory is in [MASTER_INFRASTRUCTURE.md](MASTER_INFRASTRUCTURE.md) and [DNS_AND_GCP_ARCHITECTURE.md](DNS_AND_GCP_ARCHITECTURE.md).

---

## 0. What is already decided (do not re-litigate)

- **Cloud primary: GCP**, region `us-central1`, Google BAA in place.
- **AWS is secondary**: used only for Batch compute or AWS Open Data Sponsorship hosting.
- **Central vault: TileDB ecosystem** — TileDB-SOMA (single-cell), TileDB-VCF (variants), TileDB-BioImaging, TileDB-ML; Zarr is the secondary tensor route.
- **Versioning: DVC** on GCS. Artifact tracking via `gs://cytognosis-data-hub/dvc-cache/`.
- **PHI constraints**: PHI never leaves device; distributed storage (IPFS/Autonomi) prohibited; single-region only; mTLS with cert pinning; HIPAA-compliant DB; immutable audit log.
- **Local hot tier**: 4 TB NVMe in TB5/USB4-v2 enclosure. **Local cold tier**: 14–16 TB enterprise HDD in JBOD.
- **Local namespace**: `mergerfs` (FUSE union) with `mergerfs-cache-mover` for SSD→HDD demotion.

---

## 1. TL;DR — key decisions

| Question | Recommendation |
|---|---|
| Cloud primary | GCP `us-central1` (Iowa, BAA-eligible, cheapest GCS rates, lowest egress to most US compute) |
| Multi-region? | **No for PHI/instrument data** (HIPAA jurisdictional). Yes (`US` multi-region) only for fully open/published artifacts. |
| Hot cloud tier | GCS Standard in `us-central1`, Object Versioning ON, lifecycle Standard→Nearline @30d (non-PHI), Coldline @180d (PHI archival) |
| Cold cloud tier | GCS Coldline for warm-archive (≥90d retrieval); GCS Archive for raw instrument data and locked snapshots |
| AWS use | S3 only for (a) AWS Open Data Sponsorship-eligible datasets, (b) staging into AWS Batch jobs. Region: `us-east-1`. |
| Local hot | 4 TB NVMe — ext4 with `noatime,discard=async` |
| Local cold | 16 TB enterprise HDD; add SnapRAID when second drive arrives; XFS on cold |
| Unified namespace | Two-layer: (a) library-native URIs (`tiledb://`, `gs://`, `dvc://`) for bulk data; (b) `rclone mount` under `mergerfs` for unstructured browse/read |
| DVC remote | `gs://cytognosis-data-hub/dvc-cache/` (hot, existing). Add `gs://cytognosis-dvc-cold` (Coldline) for archived releases. |
| Multi-writer robustness | TileDB MVCC for arrays; GCS object generation preconditions (`If-Generation-Match`) for everything else |
| Encryption | CMEK (Cloud KMS) on every bucket; LUKS on local cold HDD; LUKS on local hot NVMe if device leaves the building |

---

## 2. Cloud (GCP) layout

### 2.1 Region

Use **`us-central1` (Iowa)** as the single primary region.

- BAA-covered region; single-region simplifies right-to-be-forgotten and audit scope.
- `us-central1` is GCP's cheapest US region and offers the best Cloud Run / Vertex AI availability for AI workloads.
- Same-region reads from Cloud Run, GKE, Vertex, BigQuery cost $0 egress.
- Avoid `US` multi-region for PHI: it stripes objects across `us-central1` / `us-east1` / `us-east4`, complicating jurisdiction tracking.

### 2.2 Bucket layout — planned target (two-bucket PHI/non-PHI invariant)

PHI and non-PHI **never share a bucket**. Bucket-level boundaries make CMEK rotation, audit log filtering, retention lock, and BAA scoping clean.

```
gs://cytognosis-data-hot          # non-PHI active datasets, models, code artifacts
gs://cytognosis-data-cold         # non-PHI archive (Coldline / Archive lifecycle)
gs://cytognosis-data-hub          # EXISTING — DVC cache + shared data (Standard, versioning ON)
gs://cytognosis-mlflow-artifacts  # EXISTING (created 2026-06-14) — MLflow artifact root
gs://cytognosis-tiledb-arrays     # TileDB-SOMA / TileDB-VCF / TileDB-BioImaging vaults (planned)
gs://cytognosis-zarr              # Zarr/N5 stores (planned)
gs://cytognosis-phi-instruments   # PHI raw — CMEK, retention lock, audit, no public IAM (planned)
gs://cytognosis-phi-derived       # PHI processed — same controls (planned)
gs://cytognosis-public-data       # EXISTING — publicly readable, de-identified, multi-region
gs://cytognosis-audit-7yr         # EXISTING — immutable retention lock 7yr
gs://cytognosis-phi-core          # EXISTING — PHI vault, CMEK, versioning ON (cytognosis-phi-prod)
gs://cytognosis-phi-collab-nih    # EXISTING — restricted joint-analysis (cytognosis-phi-prod)
```

Per-bucket settings (apply uniformly):

- **Uniform Bucket-Level Access** = ON.
- **Object Versioning** = ON for `*-data-*`, `*-tiledb-*`, `*-dvc-*`, PHI buckets; OFF for `*-zarr`.
- **Soft delete** = 30 days minimum.
- **CMEK**: one Cloud KMS key per data class (PHI key = `phi-bucket-key` in phi-keyring; non-PHI key; public key). Rotate annually.
- **Retention lock**: PHI buckets = 7-year; archive bucket = 10-year for instrument provenance.
- **Public access prevention** = ENFORCED on every PHI bucket.

### 2.3 Storage classes

| Class | Min duration | Per-GB/mo (us-central1) | Retrieval cost | Use for |
|---|---|---|---|---|
| Standard | none | ~$0.020 | $0 | TileDB arrays, active Zarr, DVC cache, hot models |
| Nearline | 30 days | ~$0.010 | $0.01/GB | Papers, DVC datasets behind a versioned tag |
| Coldline | 90 days | ~$0.004 | $0.02/GB | Quarterly snapshots, archived experiments |
| Archive | 365 days | ~$0.0012 | $0.05/GB | Raw instrument data, immutable provenance copies |

---

## 3. Local layout (Strix Halo workstation)

### 3.1 Filesystem choice per drive

| Drive | Filesystem | Why |
|---|---|---|
| 4 TB NVMe (hot) | ext4 with `noatime,nodiratime,discard=async` | Lowest overhead; best PostgreSQL performance |
| 14–16 TB HDD (cold) | XFS with `noatime,inode64,largeio,allocsize=64m` | Better for large files (Zarr chunks, TileDB fragments) |

LUKS encryption is mandatory on the cold drive. LUKS on the hot NVMe is optional on desktop, mandatory on laptop.

### 3.2 mergerfs configuration

```
/mnt/nvme_hot:/mnt/hdd_cold /mnt/cytoverse fuse.mergerfs \
  defaults,allow_other,use_ino,cache.files=off,dropcacheonclose=true,\
  moveonenospc=true,minfreespace=200G,fsname=cytoverse,\
  category.create=ff,category.action=epall,category.search=ffwp,\
  posix_acl=true,xattr=passthrough 0 0
```

Key parameters:
- `minfreespace=200G` — TileDB writes can produce 100+ GB fragments; 50 G is insufficient.
- `category.action=epall` — chmod/chown/utimes apply to all branches that have the path.
- `xattr=passthrough` — needed for OME-Zarr xattr metadata.

### 3.3 SnapRAID — add when second cold HDD arrives

- 1 cold drive: skip SnapRAID. Back up to `gs://cytognosis-data-cold` nightly.
- 2+ cold drives: 1 parity drive (sized ≥ largest data drive). SnapRAID syncs nightly via systemd timer.
- Do NOT put the hot NVMe in SnapRAID — it churns too fast for SnapRAID's snapshot-parity model.

### 3.4 cache-mover exclusions (TileDB-safe)

Add to `EXCLUDED_DIRS`:
- `/mnt/cytoverse/tiledb/` — TileDB fragments are append-mostly; demoting mid-write corrupts the array.
- `/mnt/cytoverse/zarr/active/` — same reason.
- `/mnt/cytoverse/postgres/` — DB tablespace; must stay on NVMe.

---

## 4. Unified namespace across all four tiers

**Bright line**: bulk scientific data (TileDB, Zarr, DVC, BAM/CRAM, Parquet, OME-Zarr) never touches FUSE. Unstructured filesystem data (papers, code, configs, notebooks) gets a POSIX mount.

### 4.1 Layer A — library-native URIs (parallel/distributed path)

A CURIE-style config map (`~/.config/cytoverse/storage.yaml`) maps a friendly prefix to four physical locations:

```yaml
prefixes:
  cv-soma:
    local_hot:  /mnt/cytoverse/tiledb/soma
    local_cold: /mnt/cytoverse/tiledb/soma-archive
    cloud_hot:  gs://cytognosis-tiledb-arrays/soma
    cloud_cold: gs://cytognosis-tiledb-arrays/soma-archive
  cv-zarr:
    local_hot:  /mnt/cytoverse/zarr/active
    cloud_hot:  gs://cytognosis-zarr/active
  cv-dvc:
    cloud_hot:  gs://cytognosis-data-hub/dvc-cache
  cv-phi:
    local_hot:  /mnt/cytoverse-phi/active
    cloud_hot:  gs://cytognosis-phi-core
```

A thin Python helper (`cytoverse.storage.resolve(curie, prefer="hot")`) returns the right physical URI. TileDB, Zarr v3, DVC, and fsspec-backed Parquet/Arrow all have first-class object-store readers that do parallel range-GETs; FUSE would serialize and break multi-writer guarantees.

### 4.2 Layer B — rclone+mergerfs POSIX mount for unstructured data

For papers, code repos, configs, manuscripts, research notes — anything opened by name in an editor:

```bash
rclone mount gcs:cytognosis-data-hot /mnt/cytoverse-cloud-hot \
  --vfs-cache-mode=full --vfs-cache-max-size=200G \
  --vfs-cache-max-age=72h --dir-cache-time=10m \
  --vfs-read-chunk-size=64M --transfers=16 --checkers=32 \
  --allow-non-empty
```

Stack the rclone mount under mergerfs so the user sees one unified tree at `/mnt/cytoverse/`. The upgrade path to JuiceFS applies when the team grows past 3–4 concurrent writers.

---

## 5. DVC integration

```bash
# hot remote (existing)
dvc remote add -d hot gs://cytognosis-data-hub/dvc-cache
dvc remote modify hot version_aware true

# cold remote (planned — for archived releases)
dvc remote add cold gs://cytognosis-dvc-cold
dvc remote modify cold version_aware true
```

Day-to-day: `dvc push/pull` use `hot`. Dataset releases: `dvc push -r cold` writes a Coldline copy tagged with a release tag.

| Artifact | Source of truth | DVC-tracked? |
|---|---|---|
| Code | GitHub (cytognosis org) | No (git) |
| Model weights | DVC on `cytognosis-data-hub` + DagsHub | Yes |
| Datasets (<100 GB) | DVC | Yes |
| Large datasets (TileDB/Zarr) | TileDB/Zarr cloud bucket | No (DVC pointer YAML) |
| Papers (PDFs) | `gs://cytognosis-papers` (planned) + Zotero | No (Zotero linked-files) |

---

## 6. Encryption summary

| Layer | Encryption | Notes |
|---|---|---|
| GCS objects | CMEK via Cloud KMS, key per data class | Annual rotation |
| PHI buckets (phi-prod) | CMEK with `phi-keyring`/`phi-bucket-key` | Confirmed deployed (2026-06-14) |
| GCS in transit | TLS 1.2+ enforced | mTLS for service-to-service |
| Cloud SQL (PHI metadata) | CMEK + private IP + IAM auth | Restore from PITR tested quarterly |
| Local cold HDD | LUKS2, key in YubiKey or sealed-to-TPM | Mandatory |
| Local hot NVMe | LUKS2 if portable; optional on desktop | |

---

## 7. Open questions / implementation roadmap

See the original source doc for the 4–6 week implementation roadmap and open questions. Current priorities:

1. Terraform the remaining planned buckets (§2.2) with CMEK, versioning, lifecycle, retention locks.
2. Add `gs://cytognosis-dvc-cold` cold remote for release workflow.
3. Provision Strix Halo workstation with mergerfs + cache-mover + TileDB exclusions.
4. Ship `cytoverse.storage.resolve()` Python helper + YAML config.
5. Attach `cytohost-ip` static IP (136.111.39.188) to cytohost VM to stabilize DNS.

---

## Related docs

- [MASTER_INFRASTRUCTURE.md](MASTER_INFRASTRUCTURE.md)
- [DNS_AND_GCP_ARCHITECTURE.md](DNS_AND_GCP_ARCHITECTURE.md)
- [data-strategy/dvc-configuration.md](data-strategy/dvc-configuration.md)
- [data-strategy/tiledbvcf-hail-assessment.md](data-strategy/tiledbvcf-hail-assessment.md)
- [service-accounts.md](service-accounts.md)
