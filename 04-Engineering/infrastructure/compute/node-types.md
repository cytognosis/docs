> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `compute`, `gcp`, `vm`, `cytohost`
> **Last verified**: 2026-06-19 against gcloud

# Compute Node Types & Provisioning

## BLUF

`cytohost` is an `e2-highmem-2` (x86\_64) VM in `us-central1-b`. It is NOT ARM64/t2a, those references are stale. The VM has static IP `cytohost-static` (34.171.23.255) attached. Service account `cytohost-sa` is attached with OS Login enabled. Business-hours auto-stop is not implemented.

---

## Region

All persistent Cytognosis compute is in **`us-central1`**, zone **`us-central1-b`**.

---

## Deployed Nodes

| Name | Type | Zone | vCPU | RAM | Architecture | External IP | Service Account |
|---|---|---|---|---|---|---|---|
| **`cytohost`** | `e2-highmem-2` | us-central1-b | 2 | 16 GB | **x86\_64** | 34.171.23.255 (`cytohost-static`) | `cytohost-sa` (OS Login enabled) |

> [!NOTE]
> Static IP `cytohost-static` (34.171.23.255) is attached to the VM. DNS is stable across VM restarts. Orphaned IPs (`cytohost-ip`, `core-services-ip`, `cytognosis-ip`) were deleted 2026-06-19.

> [!IMPORTANT]
> All prior references to `t2a-standard-2`, ARM64, or 8 GB RAM for cytohost are **stale and incorrect**. The VM was migrated to `e2-highmem-2` x86\_64 (16 GB RAM).

> [!NOTE]
> **Business-hours auto-start/stop is roadmap only.** Cloud Scheduler API and Cloud Functions API are disabled in `cytognosis-infrastructure`. cytohost runs 24/7. The `automaticRestart: true` setting means GCP will restart it after host maintenance, but no scheduled shutdowns are configured.

### Services Running on cytohost

11 containers via `docker-compose.cytohost-v2.yml`. Full list: see [architecture.md](../architecture.md).

### Service Account Note

The default Compute Engine SA (`517562623935-compute@developer.gserviceaccount.com`) is **disabled**. It has been replaced by `cytohost-sa@cytognosis-infrastructure.iam.gserviceaccount.com`, which is attached to the VM with OS Login enabled (2026-06-19). CI/CD workflows authenticate via OIDC.

---

## SSH Access

```bash
# Via IAP (no public SSH port needed)
gcloud compute ssh cytohost \
  --zone=us-central1-b \
  --project=cytognosis-infrastructure \
  --tunnel-through-iap

# Check container status
sudo docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'

# Restart a specific container
sudo docker restart cyto-<service>

# Bring up full stack (after reboot or changes)
cd /opt/container_framework && sudo docker compose up -d
```

---

## On-Demand Research Compute Tiers

Ephemeral spot instances spun up when needed. All in `us-central1`.

| Profile | Type | vCPU | RAM | VRAM | Est. spot cost | Use case |
|---|---|---|---|---|---|---|
| CPU-heavy ETL | `n2-standard-8` spot | 8 | 32 GB | — | ~$0.10/hr | BioCypher, TileDB ingest |
| Memory-heavy | `n2-highmem-8` spot | 8 | 64 GB | — | ~$0.13/hr | Large AnnData, SOMA |
| GPU small | `n1-standard-4` + T4 spot | 4 | 15 GB | 16 GB | ~$0.22/hr | Embedding, small inference |
| GPU medium | `a2-highgpu-1g` spot | 12 | 85 GB | 40 GB | ~$0.90/hr | A100 — fine-tuning |
| GPU large | `a3-highgpu-1g` spot | 26 | 170 GB | 80 GB | ~$1.80/hr | H100 — foundation models |

Name ephemeral nodes `research-<purpose>-YYYYMMDD` and terminate when done.

---

## Naming Convention

| Name | Type | Purpose |
|---|---|---|
| `cytohost` | `e2-highmem-2` | Core services stack + GitHub Actions runner |
| `research-<purpose>-YYYYMMDD` | Ephemeral spot | On-demand research workloads |

All new persistent compute goes in `us-central1-b`.

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](../architecture.md) | Full system topology |
| [Self-Hosted Stack](../self-hosted/deployment_walkthrough.md) | 11-container deployment detail |
| [CI/CD: Runner Setup](../ci-cd/runner-setup.md) | GitHub Actions runner on cytohost |
| [GCP Setup](../gcp-setup.md) | IAM and project config |
