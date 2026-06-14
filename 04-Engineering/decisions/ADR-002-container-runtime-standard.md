# ADR-002: Container Runtime Standard

- **Status**: Decided
- **Date**: 2026-06-01
- **Decision**: Docker (Docker Compose) is the primary container runtime

## Context

Both Docker (v29.3.1) and Podman (v5.7.0) are installed on the development
workstation. The `infrastructure/container_framework/` directory contains Docker
Compose files for all services (Neo4j, PostgreSQL, Caddy, HedgeDoc/Wiki.js,
Prefect, MLflow, SurrealDB).

## Decision

**Use Docker Compose as the primary container orchestration tool.**

- All service definitions use `docker-compose.*.yml` format
- The `cyto-service` CLI wraps Docker Compose
- Podman is available as a fallback but not the default
- CI/CD workflows use Docker

## Consequences

- No migration from Docker Compose to Podman Compose is needed
- New services should be added as Docker Compose service definitions
- Existing `container_framework/` structure is the canonical location
