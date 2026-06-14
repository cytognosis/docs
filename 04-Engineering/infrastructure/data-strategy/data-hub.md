# Cytognosis Central Data Hub (`cytognosis-data-hub`)

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, data scientists
> **Tags**: `gcs`, `dvc`, `data-hub`

**Last verified: 2026-06-14** — `gs://cytognosis-data-hub` confirmed in `cytognosis-infrastructure`, `us-central1`, with versioning ON and lifecycle rules (60d Nearline, 180d Coldline).

## Purpose

`gs://cytognosis-data-hub` is the canonical **collaborative data sharing** bucket for the
Cytognosis Foundation. It is the single source of truth for:

- Processed (de-identified) datasets shared with research collaborators
- Active working datasets for Purdue University collaborators
- Intermediate pipeline outputs consumed across projects
- Open/public datasets mirrored for reproducibility

This is distinct from `gs://cytognosis-phi-core` (Tier 4 raw PHI/DUC data) and
`gs://cytognosis-public-data` (fully open, no-auth public datasets).

---

## Location & Redundancy Decision

**Region**: `us-central1` (Council Bluffs, Iowa)
**Storage class**: Standard (hot), auto-tiered to Nearline/Coldline via lifecycle

### Why us-central1 (not dual-region or multi-region)

| Option | Storage cost | Egress cost | Latency to Purdue | Redundancy | Decision |
|---|---|---|---|---|---|
| `us-central1` single | $0.020/GB | $0.12/GB to internet | ~10ms (300mi) | 99.999999999% | ✅ **Selected** |
| `NAM4` dual-region (central+east) | $0.026/GB (+30%) | Same | ~10ms | 99.9999999999% | Overkill now |
| `US` multi-region | $0.026/GB (+30%) | Same | ~5ms avg | 99.9999999999% | No clear benefit |
| `us-east1` single | $0.020/GB | $0.12/GB | ~15ms (800mi) | 99.999999999% | Farther from Purdue |

**us-central1 is the optimal choice** because:

1. **Closest to Purdue** (West Lafayette, IN ≈ 300 miles from Iowa data center vs. 800+ miles to `us-east1`)
2. **All other Cytognosis GCP resources** (Artifact Registry, Cloud Run, compute) are already here — no cross-region transfer fees for internal pipelines
3. **Single-region is sufficient** at this data scale; add dual-region if data exceeds ~5 TB and uptime SLA becomes critical
4. **HIPAA-eligible** region ✅

---

## Storage Tiering & Auto-Lifecycle

Objects transition automatically via the lifecycle policy:

```
Upload (Standard) → 60 days untouched → Nearline → 180 days → Coldline
```

### Cost Model by Tier

| Class | Storage | Retrieval | Min duration | Best for |
|---|---|---|---|---|
| **Standard** | $0.020/GB/mo | Free | None | Active datasets, Purdue working data |
| **Nearline** | $0.010/GB/mo | $0.010/GB | 30 days | Last-quarter pipeline outputs |
| **Coldline** | $0.004/GB/mo | $0.020/GB | 90 days | Archived cohort snapshots |
| **Archive** | $0.0012/GB/mo | $0.050/GB | 365 days | Use `cytognosis-phi-core` for this |

### Example cost at 100 GB active + 500 GB warm

```
Standard: 100 GB × $0.020 = $2.00/mo
Nearline: 500 GB × $0.010 = $5.00/mo
Subtotal storage: $7.00/mo

Egress (10 GB/mo to Purdue via internet): 10 × $0.12 = $1.20/mo
Total estimated: ~$8.20/mo for 600 GB
```

### Force Standard class (prevent auto-tiering) for active paths

For data that students touch frequently, always write with the Standard class explicitly:

```bash
# Upload forcing Standard class (won't auto-tier)
gcloud storage cp dataset.tar.gz gs://cytognosis-data-hub/purdue/active/ \
  --storage-class=STANDARD
```

The lifecycle policy won't downgrade Standard objects from these prefixes
as long as they're accessed at least every 60 days. If they go 60 days
untouched, that's a signal they're no longer "active."

---

## Directory Structure

```
gs://cytognosis-data-hub/
├── purdue/                  # Purdue University collaborator workspace
│   ├── active/              # Currently used data (always Standard, refresh access to prevent tier-down)
│   ├── delivered/           # Finalized datasets delivered to collaborators
│   └── README.md            # Access instructions for Purdue students
│
├── shared/                  # Cross-project internal sharing
│   ├── soma/                # TileDB-SOMA processed single-cell datasets
│   ├── gwas/                # GWAS summary statistics (publicly-derived, de-id)
│   ├── embeddings/          # Model embeddings / feature vectors
│   └── reference/           # Reference genomes, GTF files, etc.
│
├── processed/               # Pipeline output artifacts (auto-tier OK)
│   ├── <project>/
│   │   ├── <date>/
│   │   └── latest -> symlink pattern via manifest
│
├── public-mirror/           # Public dataset mirrors for reproducibility
│   ├── 1000g/
│   ├── gnomad/
│   └── gtex/
│
└── manifests/               # JSON manifests describing each dataset
    └── <dataset>.manifest.json
```

---

## Access Control

### Cytognosis team (internal)
All `cytognosis.org` users get read access via a Google Workspace group:

```bash
# Add org-wide read access
gcloud storage buckets add-iam-policy-binding gs://cytognosis-data-hub \
  --member="domain:cytognosis.org" \
  --role="roles/storage.objectViewer" \
  --project=cytognosis-infrastructure

# Add write access for data engineers (specific group)
gcloud storage buckets add-iam-policy-binding gs://cytognosis-data-hub \
  --member="group:gcp-data-engineers@cytognosis.org" \
  --role="roles/storage.objectAdmin" \
  --project=cytognosis-infrastructure
```

### Purdue University collaborators (external)

**Method 1: Per-user GCP IAM (preferred for active students)**

```bash
# Grant individual Purdue student/PI read access to their sub-path
# (Requires them to have a Google account or link @purdue.edu to one)
gcloud storage buckets add-iam-policy-binding gs://cytognosis-data-hub \
  --member="user:student@purdue.edu" \
  --role="roles/storage.objectViewer" \
  --condition="expression=resource.name.startsWith('projects/_/buckets/cytognosis-data-hub/objects/purdue/'),title=purdue-access,description=Restrict to purdue/ prefix" \
  --project=cytognosis-infrastructure
```

**Method 2: Signed URLs (for one-off dataset delivery, no account needed)**

```bash
# Generate a 7-day signed URL for a specific dataset
gcloud storage sign-url \
  gs://cytognosis-data-hub/purdue/delivered/dataset-v1.tar.gz \
  --duration=7d \
  --private-key-file=<SA_KEY>

# Or using IAM credentials (no key file needed):
gcloud storage sign-url \
  gs://cytognosis-data-hub/purdue/delivered/dataset-v1.tar.gz \
  --duration=7d
```

**Method 3: Presigned URL via Python (for programmatic delivery)**

```python
from google.cloud import storage
from datetime import timedelta

client = storage.Client()
bucket = client.bucket("cytognosis-data-hub")
blob = bucket.blob("purdue/delivered/dataset-v1.tar.gz")

url = blob.generate_signed_url(
    expiration=timedelta(days=7),
    method="GET",
    version="v4",
)
print(url)  # Share this with Purdue student — no GCP account needed
```

### Access via Python (for pipeline code)

```python
import gcsfs

# Auth via ADC (automatic in Cloud Run / Compute Engine)
fs = gcsfs.GCSFileSystem()

# List available datasets
datasets = fs.ls("cytognosis-data-hub/shared/soma/")

# Stream a file (no full download needed)
with fs.open("cytognosis-data-hub/shared/soma/psychad/v1/manifest.json") as f:
    manifest = json.load(f)
```

### Access via CLI (for students)

```bash
# Install Google Cloud SDK, then:
gcloud auth login  # Use their @purdue.edu Google account

# List their data
gcloud storage ls gs://cytognosis-data-hub/purdue/active/

# Download a dataset
gcloud storage cp -r gs://cytognosis-data-hub/purdue/active/dataset-v1/ ./local-dir/

# Or with gsutil (also works)
gsutil -m cp -r gs://cytognosis-data-hub/purdue/active/ ./
```

---

## Monitoring & Cost Optimization

### Budget alert (set this now)

```bash
gcloud billing budgets create \
  --billing-account=$(gcloud billing accounts list --format="value(name)") \
  --display-name="cytognosis-data-hub monthly" \
  --budget-amount=50USD \
  --threshold-rule=percent=80 \
  --threshold-rule=percent=100 \
  --filter-projects=cytognosis-infrastructure
```

### Monitoring egress (the main cost driver)

```bash
# Check egress to internet (billed)
gcloud monitoring metrics list --filter="metric.type~egress" 2>/dev/null | head -5

# Use Storage Insights for detailed access patterns:
gcloud storage insights dataset-configs create \
  --location=us-central1 \
  --project=cytognosis-infrastructure \
  --source-projects=cytognosis-infrastructure
```

### DVC integration (for versioned datasets)

```bash
# In each project that uses data from this hub:
dvc remote add -d data-hub gs://cytognosis-data-hub/processed/<project>/dvc/

# Version a dataset
dvc add data/raw/cohort-v1.h5ad
dvc push  # → uploads to data-hub

# Collaborators pull the exact version
git pull && dvc pull
```

---

## Brand Buckets (Reserved Namespace)

The following buckets are **reserved as namespace placeholders** in
`cytognosis-infrastructure`. They are empty and exist solely to prevent
squatting on Cytognosis brand names in the global GCS namespace.

| Bucket | Brand purpose | Current use |
|---|---|---|
| `gs://cytognosis` | Primary brand | Reserved (org assets) |
| `gs://cytoverse` | Cytoverse platform | Reserved |
| `gs://cytonome` | Cytonome navigator | Reserved |
| `gs://cytoscope` | Cytoscope sensor | Reserved |
| `gs://cytopilot` | Cytopilot mobile app | Reserved |
| `gs://cytoexplorer` | CytoExplorer web interface | Reserved |
| `gs://cytomark` | Cytomark annotation | Reserved |
| `gs://cytoagent` | Cyto agent framework | Reserved |
| `gs://cytoskeleton` | Cytoskeleton env system | Reserved |
| `gs://neuroverse` | Neuroverse product | Reserved |

**These buckets cost $0** (empty Standard buckets in us-central1 have no storage charge).
When a product goes live, move the bucket to the appropriate GCP project.

---

## Document Version

- **Created**: 2026-05-19
- **Owner**: Data Engineering, Cytognosis Foundation
- **Review**: Quarterly, or when adding new collaborator access
