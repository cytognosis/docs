> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `self-hosted`, `docker`, `containers`, `cytohost`
> **Last verified**: 2026-06-14 against gcloud

# Self-Hosted Stack — Deployment Walkthrough

## BLUF

11 containers running on `cytohost` (`e2-highmem-2`, x86\_64, us-central1-b). Current external IP is 34.171.23.255 (ephemeral; static IP attachment pending). All services route through `cyto-caddy` on ports 80/443. Production compose file: `container_framework/docker-compose.cytohost-v2.yml`.

> [!WARNING]
> All prior references to 8 containers, IP `34.122.154.49`, IP `34.61.134.177`, ARM64 images, or QEMU emulation are **stale** and describe the pre-v2 deployment. The current state is documented below.

---

## Live Container Stack

| Container | Image | Mode | Internal Port | External Subdomain |
|---|---|---|---|---|
| `cyto-caddy` | `caddy:2-alpine` | Always-on | 80, 443 | — (reverse proxy) |
| `cyto-postgres` | `postgres:16-alpine` | Always-on | 5432 (internal) | — |
| `cyto-calcom` | `calcom/cal.com:latest` | Always-on | 3000 (internal) | `cal.cytognosis.org` |
| `cyto-excalidraw` | `excalidraw/excalidraw:latest` | Always-on | 80 (internal) | `whiteboard.cytognosis.org` |
| `cyto-excalidraw-room` | `excalidraw/excalidraw-room:latest` | Always-on | 3002 (internal) | — (collab backend) |
| `cyto-gitea` | `gitea/gitea:latest` | Always-on | 3000 (internal) | `code.cytognosis.org` |
| `cyto-mlflow` | `ghcr.io/mlflow/mlflow:v2.21.0` | Always-on | 5000 (internal) | `mlflow.cytognosis.org` |
| `cyto-wiki` | `requarks/wiki:2` | Always-on | 3000 (internal) | `wiki.cytognosis.org` |
| `cyto-prefect` | `prefecthq/prefect:3-python3.12` | Always-on | 4200 (internal) | `prefect.cytognosis.org` |
| `cyto-zoekt` | `ghcr.io/sourcegraph/zoekt:latest` | Always-on | 6070 (internal) | `search.cytognosis.org` |
| `cyto-neo4j` | `neo4j:5.18.1-community` | **On-demand** | 7474, 7687 (internal) | `kg.cytognosis.org` |

All containers use Docker Compose restart policy `unless-stopped` (except neo4j, which is on-demand profile).

---

## Host Details

| Field | Value |
|---|---|
| VM | `cytohost` |
| Machine type | `e2-highmem-2` (2 vCPU, 16 GB RAM, x86\_64) |
| Zone | us-central1-b |
| Current external IP | **34.171.23.255** (ephemeral) |
| Reserved static IP | `cytohost-ip` = 136.111.39.188 (not yet attached) |
| Compose file | `container_framework/docker-compose.cytohost-v2.yml` |

---

## DNS Routing

All service subdomains point to 34.171.23.255 in the `cg-org` Cloud DNS zone. Caddy handles TLS termination and proxies to the correct container on the internal Docker network.

| Subdomain | Container |
|---|---|
| `cal.cytognosis.org` | cyto-calcom |
| `code.cytognosis.org` | cyto-gitea |
| `draw.cytognosis.org` | cyto-excalidraw |
| `hub.cytognosis.org` | cyto-gitea (alt route) |
| `kg.cytognosis.org` | cyto-neo4j |
| `mermaid.cytognosis.org` | (served via Caddy static or separate container — verify on host) |
| `mlflow.cytognosis.org` | cyto-mlflow |
| `notes.cytognosis.org` | (verify on host — logseq not in compose v2) |
| `prefect.cytognosis.org` | cyto-prefect |
| `search.cytognosis.org` | cyto-zoekt |
| `whiteboard.cytognosis.org` | cyto-excalidraw |
| `wiki.cytognosis.org` | cyto-wiki |

> [!NOTE]
> `mermaid.cytognosis.org` and `notes.cytognosis.org` DNS records exist in `cg-org`. The corresponding containers (`mermaid-live-editor` and `logseq`) are present in YAML stack configs but not in `docker-compose.cytohost-v2.yml`. Their live status on cytohost should be verified directly.

---

## Operations

```bash
# SSH into cytohost
gcloud compute ssh cytohost \
  --zone=us-central1-b \
  --project=cytognosis-infrastructure \
  --tunnel-through-iap

# Check running containers
sudo docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'

# Start full always-on stack
cd /opt/container_framework
sudo docker compose up -d

# Start on-demand neo4j
sudo docker compose --profile on-demand up -d cyto-neo4j

# Stop neo4j
sudo docker compose stop cyto-neo4j

# View container logs
sudo docker logs cyto-<service> --tail 100 -f

# Restart a container
sudo docker restart cyto-<service>
```

---

## GitHub Actions Runner

The self-hosted GitHub Actions runner runs as a systemd service on cytohost. Labels: `self-hosted, linux, X64, cytohost`. See [runner-setup.md](../ci-cd/runner-setup.md) for registration and maintenance.

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](../architecture.md) | Full topology and container table |
| [Container Framework](../container-framework.md) | YAML-driven stack management |
| [Container Services](../container-services.md) | Service-level quick reference |
| [CI/CD: Runner Setup](../ci-cd/runner-setup.md) | GitHub Actions runner |
| [Compute: Node Types](../compute/node-types.md) | VM specs and SSH |
| [DNS & GCP Architecture](../DNS_AND_GCP_ARCHITECTURE.md) | DNS records and pending remediation |
