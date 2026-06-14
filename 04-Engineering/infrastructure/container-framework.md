# Container Framework

> v1.0 | Last updated: 2026-05-26

A composable, YAML-driven framework for managing Dockerized infrastructure. Service definitions live in `configs/services/*.yaml`; stacks compose them into runnable bundles.

## On-Demand Service Model

Services default **OFF** and start when needed. This keeps the host lean and avoids wasting memory on idle processes.

| Stack | Services | Mode | Memory |
|-------|----------|------|--------|
| **core** | Caddy, Cal.com, Excalidraw, Mermaid, Logseq, MLflow | Always-on | ~2 GB |
| **research** | Neo4j, Jupyter, MLflow | On-demand | ~6 GB |
| **neo4j-only** | Neo4j | On-demand | ~4 GB |

## Quick Reference

```bash
# Start a single service
python container_framework/stack_manager.py up neo4j
python container_framework/stack_manager.py up surrealdb

# Stop a service
python container_framework/stack_manager.py down neo4j

# Start a named stack
python container_framework/stack_manager.py up --stack research

# List all services and status
python container_framework/stack_manager.py ls

# Stop everything
python container_framework/stack_manager.py down --all
```

## Service Catalog

| Service | Image | Port | Credentials | Min RAM |
|---------|-------|------|-------------|---------|
| **Caddy** | Custom | 80, 443 | N/A | 128 MB |
| **Cal.com** | calcom/cal.com | 3000 | N/A | 512 MB |
| **Excalidraw** | excalidraw/excalidraw | 8080 | N/A | 256 MB |
| **Mermaid** | ghcr.io/mermaid-js/mermaid-live-editor | 8081 | N/A | 256 MB |
| **Logseq** | logseq/logseq | 8082 | N/A | 256 MB |
| **MLflow** | Custom | 5000 | N/A | 512 MB |
| **Neo4j** | neo4j:5.18.1 | 7474, 7687 | neo4j / cytognosis2026 | 2 GB |
| **SurrealDB** | surrealdb/surrealdb:v2 | 8000 | root / cytognosis2026 | 2 GB |
| **Jupyter** | Custom | 8888 | Token-based | 2 GB |

## Neo4j

```bash
# Start
python container_framework/stack_manager.py up neo4j

# Verify
docker exec cytos-neo4j cypher-shell -u neo4j -p cytognosis2026 \
    "MATCH (n) RETURN count(n)"

# Access: http://localhost:7474 (browser) or bolt://localhost:7687 (driver)
```

## SurrealDB

```bash
# Start
python container_framework/stack_manager.py up surrealdb

# Access: http://localhost:8000
# Credentials: root / cytognosis2026
```

Data persists in the `surrealdb_data` Docker volume. Uses SurrealKV embedded engine.

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

2. Optionally add it to a stack in `configs/stacks/mystack.yaml`
3. Start: `python stack_manager.py up myservice`

## Runtime Detection

The framework auto-detects Docker vs Podman:

| Runtime | Pros | Cons |
|---------|------|------|
| **Docker** | Volume mounts work with sudo | Requires root daemon |
| **Podman** | Rootless, daemonless, safer | UID mapping issues with volumes |

Override: `CONTAINER_RUNTIME=docker` or `CONTAINER_RUNTIME=podman`

## Image Management

```bash
# Build images
make build-neo4j
make build-all

# Push to Artifact Registry
make auth
make push-all

# Registry: us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/
```

## Related Documentation

- [Architecture Overview](architecture.md)
- [GCP Setup](gcp-setup.md)
