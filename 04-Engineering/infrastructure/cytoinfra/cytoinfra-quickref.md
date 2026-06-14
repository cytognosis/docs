> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: engineers, operators
> **Tags**: `quick-reference`, `cytoinfra`, `cli`
> **Last verified**: 2026-06-14 against source at `infrastructure/src/cytoinfra`

# cytoinfra CLI — Quick Reference

> **One line**: `cytoinfra` manages Cytognosis containers, services, compute jobs, and Cloud Run deploys; install via `pip install -e .` from the `infrastructure` repo.
> **Full doc**: [cytoinfra.md](cytoinfra.md)

---

## Key Concepts

| Term | Definition |
|---|---|
| **ContainerRegistry** | YAML manifest (`assets/containers/manifest.yaml`) tracking all container images and their metadata |
| **ComputePool** | Named pool config (machine type, GPU, spot/on-demand) used by `cytoinfra run` to submit Cloud Batch jobs |
| **CYTOINFRA_COMPOSE_FILE** | Env var to override the docker-compose file location (default: auto-resolved from infrastructure repo root) |
| **Cloud Run path** | Manual/emergency only; normal deploys use GitHub Actions OIDC + `website-deployer` SA |

---

## Commands

### container

| Command | What It Does |
|---|---|
| `cytoinfra container list` | Print all registered container entries |
| `cytoinfra container add <name> --image <img>` | Register new container in manifest |
| `cytoinfra container remove <name>` | Remove entry (prompts unless `--yes`) |
| `cytoinfra container build <name>` | Build container image |
| `cytoinfra container push <name>` | Push image to registry |
| `cytoinfra container pull <name>` | Pull image from registry |

### service

| Command | What It Does |
|---|---|
| `cytoinfra service deploy <name>` | Deploy via local docker-compose |
| `cytoinfra service deploy <name> --host user@host` | Deploy over SSH to remote host |
| `cytoinfra service status` | Show all running containers (Rich table) |
| `cytoinfra service status <name>` | Show single service status |
| `cytoinfra service stop <name>` | Stop a service |

### wiki-js

| Command | What It Does |
|---|---|
| `cytoinfra wiki-js setup` | Deploy Wiki.js to `wiki.cytognosis.org` |
| `cytoinfra wiki-js sync-config` | Print JSON git sync config for Wiki.js Admin > Storage |

### compute

| Command | What It Does |
|---|---|
| `cytoinfra compute pools` | List available compute pools |
| `cytoinfra compute init` | Write default pool config to `compute-pools.yaml` |

### run

| Command | What It Does |
|---|---|
| `cytoinfra run <cmd>` | Submit job to Prefect + Cloud Batch (default pool: `cpu-light`) |
| `cytoinfra run <cmd> --pool <pool>` | Submit to named pool |
| `cytoinfra run <cmd> --dry-run` | Print config without submitting |

### cloud-run

| Command | What It Does |
|---|---|
| `cytoinfra cloud-run deploy <image>` | Deploy container image to Cloud Run |
| `cytoinfra cloud-run deploy <image> --dry-run` | Print gcloud command; do not execute |

---

## Options / Parameters

### container add

| Option | Type | Default | Description |
|---|---|---|---|
| `--image` | `str` | (required) | Full container image reference |
| `--version` | `str` | `latest` | Image tag/version |
| `--source` | `str` | `docker-hub` | Image source: `docker-hub`, `ghcr`, `quay`, `internal`, `custom` |
| `--ports` | `str` | — | Port mapping `host:container`; repeatable |
| `--manifest` | `path` | auto | Path to `manifest.yaml` |

### cytoinfra run

| Option | Type | Default | Description |
|---|---|---|---|
| `--name` / `-n` | `str` | auto | Job name |
| `--pool` / `-p` | `str` | `cpu-light` | Compute pool |
| `--env` / `-e` | `str` | — | `KEY=VALUE` env var; repeatable |
| `--dry-run` | `bool` | False | Preview config only |

### cloud-run deploy

| Option | Type | Default | Env var |
|---|---|---|---|
| `--service` | `str` | `cytognosis-website-v2` | `CYTOINFRA_CLOUD_RUN_SERVICE` |
| `--project` | `str` | `cytognosis-phi-prod` | `CYTOINFRA_CLOUD_RUN_PROJECT` |
| `--region` | `str` | `us-central1` | `CYTOINFRA_CLOUD_RUN_REGION` |
| `--max-instances` | `int` | `10` | — |
| `--memory` | `str` | `512Mi` | — |
| `--cpu` | `str` | `1` | — |
| `--env-var` | `str` | — | `KEY=VALUE`; repeatable |
| `--dry-run` | `bool` | False | — |

---

## Environment Variables

| Variable | Default | Purpose |
|---|---|---|
| `CYTOINFRA_COMPOSE_FILE` | auto-resolved | Override path to docker-compose file |
| `WIKI_DB_PASSWORD` | (required) | PostgreSQL password for Wiki.js setup |
| `CYTOINFRA_CLOUD_RUN_PROJECT` | `cytognosis-phi-prod` | Cloud Run GCP project |
| `CYTOINFRA_CLOUD_RUN_REGION` | `us-central1` | Cloud Run region |
| `CYTOINFRA_CLOUD_RUN_SERVICE` | `cytognosis-website-v2` | Cloud Run service name |

---

## Common Patterns

```bash
# Deploy one service locally
cytoinfra service deploy cyto-wiki

# Deploy Wiki.js with password from env
WIKI_DB_PASSWORD=secret cytoinfra wiki-js setup

# Submit CPU job
cytoinfra run python process.py --pool cpu-medium

# Submit GPU job (dry run first)
cytoinfra run python train.py --pool gpu-t4 --dry-run
cytoinfra run python train.py --pool gpu-t4

# Emergency Cloud Run deploy (dry run first)
cytoinfra cloud-run deploy \
  us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:latest \
  --dry-run

cytoinfra cloud-run deploy \
  us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:latest
```

---

## Error Quick-Fix

| Error / Symptom | Fix |
|---|---|
| `Entry '<name>' not found in registry.` | Run `cytoinfra container list` to check exact name; re-run with `--manifest` if using a non-default manifest path |
| `gcloud not found on PATH` | Install Google Cloud CLI: https://cloud.google.com/sdk/docs/install |
| `gcloud` exits non-zero on cloud-run deploy | Check ADC credentials (`gcloud auth application-default login`) or OIDC setup |
| `WIKI_DB_PASSWORD` not set — deploy fails | Set env var: `export WIKI_DB_PASSWORD=...` or pass `--db-password` |
| Compose file not found | Set `CYTOINFRA_COMPOSE_FILE` or ensure you're running from the infrastructure repo root |

---

## See Also

- [cytoinfra.md](cytoinfra.md) — full module documentation, architecture diagram, and design notes
- [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) — master infrastructure quick reference
- [container-framework.md](../container-framework.md) — self-hosted docker-compose stack
