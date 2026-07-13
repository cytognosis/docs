> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `containers`, `docker`, `self-hosted`, `cytohost`
> **Variants**: Technical (this doc) - Readable (same filename in Obsidian vault: 04-Engineering/infrastructure/) - Agent (n/a)
> **Last verified**: 2026-06-14 against gcloud

# Container Services — Quick Reference

## BLUF

11 containers run on `cytohost` (e2-highmem-2, 16 GB RAM, x86\_64). All are native x86\_64 — no QEMU emulation. Full deployment detail: see [deployment_walkthrough.md](self-hosted/deployment_walkthrough.md).

> [!WARNING]
> Prior references to `n2d-standard-8 / 32 GB RAM`, ARM64 images, or QEMU emulation for Cal.com/Excalidraw Room are stale. cytohost is x86\_64 with 16 GB RAM.

---

## Live Stack

| Container | Image | Mode | Port | Subdomain |
|---|---|---|---|---|
| `cyto-caddy` | `caddy:2-alpine` | Always-on | 80, 443 | — |
| `cyto-postgres` | `postgres:16-alpine` | Always-on | 5432 (internal) | — |
| `cyto-calcom` | `calcom/cal.com:latest` | Always-on | 3000 (internal) | `cal.cytognosis.org` |
| `cyto-excalidraw` | `excalidraw/excalidraw:latest` | Always-on | 80 (internal) | `whiteboard.cytognosis.org` |
| `cyto-excalidraw-room` | `excalidraw/excalidraw-room:latest` | Always-on | 3002 (internal) | — |
| `cyto-gitea` | `gitea/gitea:latest` | Always-on | 3000 (internal) | `code.cytognosis.org` |
| `cyto-mlflow` | `ghcr.io/mlflow/mlflow:v2.21.0` | Always-on | 5000 (internal) | `mlflow.cytognosis.org` |
| `cyto-wiki` | `requarks/wiki:2` | Always-on | 3000 (internal) | `wiki.cytognosis.org` |
| `cyto-prefect` | `prefecthq/prefect:3-python3.12` | Always-on | 4200 (internal) | `prefect.cytognosis.org` |
| `cyto-zoekt` | `ghcr.io/sourcegraph/zoekt:latest` | Always-on | 6070 (internal) | `search.cytognosis.org` |
| `cyto-neo4j` | `neo4j:5.18.1-community` | **On-demand** | 7474, 7687 (internal) | `kg.cytognosis.org` |

---

## Neo4j Configuration

| Parameter | Value | Notes |
|---|---|---|
| Image | `neo4j:5.18.1-community` | Community Edition |
| Auth | Set via `$NEO4J_AUTH` | Do NOT use default credentials in production |
| Heap | 2 GB initial + max | Override via `$NEO4J_HEAP` |
| Page cache | 2 GB | Override via `$NEO4J_PAGECACHE` |
| Ports | 7474 (HTTP), 7687 (Bolt) | Internal to Docker network |
| Mode | On-demand (`--profile on-demand`) | Not started with the default stack |
| GC | G1GC + ExitOnOutOfMemoryError | |

**Memory tuning for 16 GB cytohost:**

| Use case | Heap | Page Cache | Total |
|---|---|---|---|
| Neo4j small (KG dev) | 2 GB | 2 GB | 4 GB |
| Neo4j full KG | 4 GB | 6 GB | 10 GB |
| Neo4j max (leaves 6 GB for other containers) | 4 GB | 6 GB | 10 GB |

```bash
export NEO4J_HEAP=4g
export NEO4J_PAGECACHE=6g
sudo docker compose --profile on-demand up -d cyto-neo4j
```

---

## Quick Commands

```bash
# SSH into cytohost
gcloud compute ssh cytohost --zone=us-central1-b --project=cytognosis-infrastructure --tunnel-through-iap

# Check running containers
sudo docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'

# Start all always-on services
cd /opt/container_framework && sudo docker compose up -d

# Start on-demand neo4j
sudo docker compose --profile on-demand up -d cyto-neo4j

# Stop a service
sudo docker stop cyto-<service>

# View logs
sudo docker logs cyto-<service> --tail 100 -f

# Restart a service
sudo docker restart cyto-<service>
```

---

## Artifact Registry

Internal compute images push to:

```
us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/
```

This registry is empty as of 2026-06-14. Deployed containers pull from public registries (Docker Hub, GHCR).

---

## Cross-References

| Document | Relationship |
|---|---|
| [Deployment Walkthrough](self-hosted/deployment_walkthrough.md) | Full live state |
| [Container Framework](container-framework.md) | Framework management detail |
| [Architecture Overview](architecture.md) | System topology |
| [Compute: Node Types](compute/node-types.md) | VM specs |
