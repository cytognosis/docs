> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `containers`, `docker`, `framework`, `cytohost`
> **Last verified**: 2026-06-14 against gcloud

# Container Framework

## BLUF

A YAML-driven framework for managing the 11-container Docker stack on `cytohost` (e2-highmem-2, x86\_64). Service definitions in `configs/services/*.yaml`; stacks compose them into runnable bundles. Production compose: `container_framework/docker-compose.cytohost-v2.yml`.

---

## Stack Model

Services run in two modes on the 16 GB cytohost host:

| Stack | Services | Mode | Approx. Memory |
|---|---|---|---|
| **Always-on** | caddy, postgres, calcom, excalidraw, excalidraw-room, gitea, mlflow, wiki, prefect, zoekt | `unless-stopped` | ~8–10 GB |
| **On-demand** | neo4j | `--profile on-demand` | ~4–6 GB additional |

Start on-demand services when needed; stop when done to free memory for other workloads.

---

## Quick Reference

```bash
# Start full always-on stack (from compose file)
cd /opt/container_framework
sudo docker compose up -d

# Start on-demand neo4j
sudo docker compose --profile on-demand up -d cyto-neo4j

# Stop neo4j
sudo docker compose stop cyto-neo4j

# Stop entire stack
sudo docker compose down

# List running containers
sudo docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'

# View logs
sudo docker logs cyto-<service> --tail 100 -f
```

---

## Service Catalog

| Service | Image | Ports | Min RAM | Notes |
|---|---|---|---|---|
| `cyto-caddy` | `caddy:2-alpine` | 80, 443 | 128 MB | Reverse proxy + automatic TLS |
| `cyto-postgres` | `postgres:16-alpine` | 5432 (internal) | 256 MB | Shared DB for calcom and other services |
| `cyto-calcom` | `calcom/cal.com:latest` | 3000 (internal) | 512 MB | HIPAA-aware scheduling |
| `cyto-excalidraw` | `excalidraw/excalidraw:latest` | 80 (internal) | 256 MB | Collaborative whiteboarding |
| `cyto-excalidraw-room` | `excalidraw/excalidraw-room:latest` | 3002 (internal) | 128 MB | Real-time collaboration backend |
| `cyto-gitea` | `gitea/gitea:latest` | 3000 (internal) | 256 MB | Self-hosted Git |
| `cyto-mlflow` | `ghcr.io/mlflow/mlflow:v2.21.0` | 5000 (internal) | 512 MB | Experiment tracking and model registry |
| `cyto-wiki` | `requarks/wiki:2` | 3000 (internal) | 256 MB | Team wiki (replaced HedgeDoc) |
| `cyto-prefect` | `prefecthq/prefect:3-python3.12` | 4200 (internal) | 512 MB | Workflow orchestration |
| `cyto-zoekt` | `ghcr.io/sourcegraph/zoekt:latest` | 6070 (internal) | 256 MB | Code search |
| `cyto-neo4j` | `neo4j:5.18.1-community` | 7474, 7687 (internal) | 4 GB | Knowledge graph (on-demand only) |

> [!NOTE]
> HedgeDoc was replaced by Wiki.js (`cyto-wiki`). Do not re-add HedgeDoc. SurrealDB, Logseq, Mermaid Live, and Jupyter are present in YAML stack configs but not in the deployed v2 compose file; their current deployment status should be verified before adding to production.

---

## Neo4j

```bash
# Start (on-demand)
sudo docker compose --profile on-demand up -d cyto-neo4j

# Verify
sudo docker exec cyto-neo4j cypher-shell -u neo4j \
    "MATCH (n) RETURN count(n)"

# Access: http://kg.cytognosis.org (browser) or bolt://localhost:7687 (driver)
```

Neo4j data persists in the `cyto-neo4j_data` Docker volume.

---

## Adding a New Service

1. Create `configs/services/myservice.yaml`:

```yaml
name: myservice
description: "What it does"
image: myimage:latest
ports:
  - "8080:8080"
resources:
  min_memory: "1g"
  recommended_memory: "4g"
```

2. Add a Caddy route for the subdomain (if web-facing).
3. Add to `docker-compose.cytohost-v2.yml`.
4. Optionally add to a stack in `configs/stacks/`.

---

## Runtime

All containers use Docker on cytohost. The framework YAML supports Podman detection but Docker is the deployed runtime.

| Runtime | Status |
|---|---|
| Docker | **Used in production** |
| Podman | Supported in code; not deployed |

Override: `CONTAINER_RUNTIME=docker` or `CONTAINER_RUNTIME=podman`

---

## Image Management

```bash
# Build custom images
make build-<service>
make build-all

# Push to Artifact Registry
make auth
make push-all

# Registry: us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/
```

---

## Cross-References

| Document | Relationship |
|---|---|
| [Container Services](container-services.md) | Service-level quick reference |
| [Deployment Walkthrough](self-hosted/deployment_walkthrough.md) | Live deployment state |
| [Architecture Overview](architecture.md) | System topology |
| [GCP Setup](gcp-setup.md) | Artifact Registry |
