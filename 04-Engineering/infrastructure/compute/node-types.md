# Compute Node Types & Provisioning

## Region

All Cytognosis compute is in **`us-central1`**, zone **`us-central1-b`** (required for ARM t2a instances).

## Deployed Nodes

| Name | Type | Zone | vCPU | RAM | External IP | Cost | Purpose |
|---|---|---|---|---|---|---|---|
| **`cytohost`** | `t2a-standard-2` (ARM64) | us-central1-b | 2 | 8 GB | 136.111.39.188 | ~$45/mo | Core services stack + GitHub Actions runner |


**Services running on cytohost** (core stack, all `unless-stopped`):

| Service | URL | Image |
|---|---|---|
| Caddy (reverse proxy + TLS) | — | `caddy:2-alpine` (ARM64) |
| Cal.com | `cal.cytognosis.org` | `calcom/cal.com:latest` (x86, QEMU) |
| Cal.com PostgreSQL | — | `postgres:15` (ARM64) |
| Excalidraw | `whiteboard.cytognosis.org` | `excalidraw/excalidraw:latest` (ARM64) |
| Excalidraw Room | — | `excalidraw/excalidraw-room:latest` (x86, QEMU) |
| Mermaid Live | `mermaid.cytognosis.org` | `ghcr.io/mermaid-js/mermaid-live-editor:latest` (ARM64) |
| Logseq | `notes.cytognosis.org` | `ghcr.io/logseq/logseq-webapp:latest` (ARM64) |
| MLflow | `mlflow.cytognosis.org` | `ghcr.io/mlflow/mlflow:latest` (ARM64) |

> **x86 via QEMU**: Cal.com and Excalidraw Room lack ARM64 images; they run under QEMU
> emulation (`platform: linux/amd64` in their service YAML). Performance is adequate for
> scheduling tools — not recommended for CPU-intensive workloads.

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
sudo docker restart generated-<service>-1

# Bring up full stack (after reboot or changes)
cd /opt/container_framework && sudo python3 stack_manager.py up core
```

## On-Demand Research Compute Tiers

Spin up as spot instances when needed; terminate immediately after. All in `us-central1-b`.

| Profile | Type | vCPU | RAM | VRAM | Est. spot cost | Use case |
|---|---|---|---|---|---|---|
| Neo4j always-on | `e2-standard-2` | 2 | 8 GB | — | ~$49/mo | Knowledge graph + OLS4 |
| CPU-heavy ETL | `n2-standard-8` spot | 8 | 32 GB | — | ~$0.10/hr | BioCypher, TileDB ingest |
| Memory-heavy | `n2-highmem-8` spot | 8 | 64 GB | — | ~$0.13/hr | Large AnnData, SOMA |
| GPU small | `n1-standard-4` + T4 spot | 4 | 15 GB | 16 GB | ~$0.22/hr | Embedding, small inference |
| GPU medium | `a2-highgpu-1g` spot | 12 | 85 GB | 40 GB | ~$0.90/hr | A100 — fine-tuning |
| GPU large | `a3-highgpu-1g` spot | 26 | 170 GB | 80 GB | ~$1.80/hr | H100 — foundation models |

## Naming Convention

Persistent nodes follow the pattern `cytonode-NN`:
- `cytohost` — current core services node (ARM64, us-central1-b)
- `cytonode-02` — future second node if needed (use same `t2a-standard-2` type)

Ephemeral research nodes are named `research-<purpose>-YYYYMMDD` (auto-deleted when done).

**All new persistent compute goes in `us-central1-b`** (t2a ARM64 availability zone).


