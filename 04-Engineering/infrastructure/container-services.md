# Container Services

> Quick reference for Cytognosis Docker/Podman container stack.

## Available Stacks

| Stack | Services | Use Case |
|-------|----------|----------|
| `core` | Neo4j, SurrealDB | KG storage and query |
| `research` | Neo4j, JupyterLab, MLflow | Data science workbench |
| `neo4j-only` | Neo4j | Graph database only |

## Neo4j Configuration

| Parameter | Default | Notes |
|-----------|---------|-------|
| Image | `neo4j:5.18.1-community` | Community Edition |
| Auth | `neo4j/cytognosis2026` | Override via `$NEO4J_AUTH` |
| Heap | 2GB initial + max | Override via `$NEO4J_HEAP` |
| Page cache | 2GB | Override via `$NEO4J_PAGECACHE` |
| Ports | 7474 (HTTP), 7687 (Bolt) | |
| Health check | Every 30s, 5 retries | HTTP check on :7474 |
| GC | G1GC + ExitOnOutOfMemoryError | |
| Query log | INFO, threshold 1s | Slow queries logged |

## Quick Commands

```bash
# Navigate to the stack manager
cd ~/repos/cytognosis/infrastructure/container_framework

# List available stacks and services
python stack_manager.py list

# Generate docker-compose.yml for a stack
python stack_manager.py compose research

# Start a stack
python stack_manager.py up research

# Stop a stack
python stack_manager.py down research

# Check running containers
python stack_manager.py status

# Restart a specific service
python stack_manager.py restart research neo4j

# Build a custom image
python stack_manager.py build neo4j

# Push to Artifact Registry
python stack_manager.py push neo4j
```

## Container Runtime Detection

The stack manager auto-detects the container runtime:
1. Checks `$CONTAINER_RUNTIME` env var
2. Tries `podman` (rootless preferred)
3. Falls back to `docker`

## Artifact Registry

```
us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/
└── neo4j:latest
└── datascience:latest
```

## Memory Tuning for GCP Host

For the `cytohost` VM (n2d-standard-8, 32GB RAM):

| Service | Heap | Page Cache | Total |
|---------|------|------------|-------|
| Neo4j (small) | 2GB | 2GB | 4GB |
| Neo4j (full KG) | 8GB | 12GB | 20GB |
| Neo4j (max) | 12GB | 16GB | 28GB |

Adjust via environment variables:
```bash
export NEO4J_HEAP=8g
export NEO4J_PAGECACHE=12g
python stack_manager.py up neo4j-only
```
