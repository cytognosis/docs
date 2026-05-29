# Infrastructure Walkthrough

## Container Framework

Built a composable, YAML-driven container framework at [`container_framework/`](../../container_framework/):

- **9 service definitions** — `caddy`, `calcom`, `excalidraw`, `jupyter`, `logseq`, `mermaid`, `mlflow`, `neo4j`, `zotero` (zotero retained as optional, not in deployed `core` stack — see [paper library architecture](../data-strategy/paper-library-architecture.md))
- **3 stack definitions** — `core`, `research`, `neo4j-only`
- **`stack_manager.py`** — CLI for `list`, `compose`, `up`, `down`, `build`, `push`
- Auto-detects Podman vs Docker runtime

## Docker vs Podman Evaluation

Tested Neo4j OLS4 (24GB) with both runtimes:

| | Docker | Podman |
|---|---|---|
| Volume mounts | ✅ Works (sudo) | ⚠️ UID mapping `chown` errors |
| Image names | Short names OK | Needs `docker.io/library/` prefix |
| Security | Root daemon | Rootless by default |

## Unified Core Services (Deployed)

8 containers running on `cytohost` (34.122.154.49):

| Container | Status | Internal Routing |
|---|---|---|
| Caddy (reverse proxy) | ✅ Running | Ports 80/443 |
| Cal.com | ✅ Running | `cal.cytognosis.org` → :3000 |
| Excalidraw | ✅ Running | `whiteboard.cytognosis.org` → :80 |
| Excalidraw Room | ✅ Running | Collab backend |
| Mermaid Live Editor | ✅ Running | `mermaid.cytognosis.org` → :8080 |
| Logseq Web | ✅ Running | `notes.cytognosis.org` → :80 |
| MLflow | ✅ Running | `mlflow.cytognosis.org` → :5000 |
| Postgres (Cal.com DB) | ✅ Healthy | Internal :5432 |

**Verified:** Caddy correctly routes to all services via Docker internal network.

## Research Stack (Deployed)

Running on `research-stack-server` (34.61.134.177):
- Neo4j ✅ (ports 7474, 7687)
- Mermaid ✅ (port 8081)

## GitHub Actions CI/CD

Created `.github/workflows/build-containers.yml`:
- Triggers on push to main when Dockerfiles change
- Builds neo4j + datascience images via matrix strategy
- Pushes to GCP Artifact Registry + optionally Docker Hub
- Uses existing Workload Identity Federation

## DNS Setup Needed

To complete the deployment, create these DNS A records pointing to `34.122.154.49`:
- `cal.cytognosis.org`
- `whiteboard.cytognosis.org`
- `mermaid.cytognosis.org`
- `notes.cytognosis.org`
- `mlflow.cytognosis.org`

Once DNS propagates, Caddy will auto-provision Let's Encrypt HTTPS certificates.
