# Phase 1: Anytype Submodule Refactor Report

> **Status**: ✅ Complete (core structure), remaining items: REST route wiring, live tests
> **Scope**: Decompose the 1,283-line monolith into a clean subpackage with REST client

## Problem

The original `anytype_adapter.py` was a single 1,283-line file containing:
- MCP stdio transport management (process lifecycle, JSON-RPC framing)
- Result parsing and error handling
- Schema mapping (LinkML → Anytype types)
- Payload construction
- PII/PHI redaction
- CAP guard integration
- All Anytype API operations

This made it impossible to test individual concerns, add REST transport, or understand the data flow.

## Solution

Decomposed into `src/yar/integrations/anytype/` with 10 focused modules:

| Module | Lines | Responsibility |
|---|---|---|
| `__init__.py` | 27 | Public API surface |
| `adapter.py` | 558 | High-level MCP adapter (was 1,283 — 57% reduction) |
| `client.py` | 385 | **New**: Direct REST client, 36 typed endpoints |
| `_config.py` | 132 | Port auto-discovery, env var loading |
| `_payload_mapper.py` | 253 | LinkML range → Anytype property type mapping |
| `_rate_limiter.py` | 42 | Token bucket rate limiter |
| `_redaction.py` | 36 | PII/PHI field redaction |
| `_result_parser.py` | 87 | MCP JSON-RPC response parsing |
| `_schema_mapper.py` | 120 | `NormalizedSchema` → Anytype type/property mapping |
| `_tool_discovery.py` | 89 | MCP tool capability discovery |
| `_transport.py` | 147 | stdio/REST transport abstraction |
| **Total** | **1,875** | (vs. 1,283 monolith — more code, but fully testable) |

## REST Client (`client.py`)

The new `AnytypeClient` directly calls the Anytype local HTTP API via `httpx`, bypassing MCP stdio overhead. It covers all Anytype REST endpoints:

- **Spaces**: list, get
- **Search**: global, per-space (with type filters, sorting, pagination)
- **Objects**: list, get, create, update, delete
- **Types**: list, get, create, delete
- **Properties**: list, create, delete
- **Tags**: list, create (nested under properties)
- **Lists/Collections**: add to, remove from
- **Templates**: list
- **Members**: list

All methods are:
- Async (`async def`)
- Rate-limited (token bucket, 1 req/s sustained, 60 burst)
- Typed (`-> dict[str, Any]`)
- Documented with the HTTP method and path

## Port Auto-Discovery (`_config.py`)

The Anytype desktop app assigns a random port to its local API on each launch. The config module:

1. Checks `ANYTYPE_API_BASE_URL` env var first
2. Falls back to scanning `~/.config/anytype/` for the middleware config JSON
3. Extracts the port from the running anytypeHelper process
4. Constructs `http://127.0.0.1:{port}` base URL

## Test Coverage

35 dedicated Anytype tests across 7 files:

| File | Tests | Coverage |
|---|---|---|
| `test_anytype_client.py` | 35 | REST client, rate limiter, error handling |
| `test_anytype_adapter.py` | 1 | Adapter initialization |
| `test_anytype_gap_regressions.py` | 7 | Edge cases from gap analysis |
| `test_anytype_mapping.py` | 3 | Schema mapping |
| `test_anytype_readonly_integration.py` | 7 | Read-only MCP operations |
| `test_anytype_write_execution.py` | 5 | Write plan execution |
| `test_anytype_write_guard.py` | 3 | CAP guard for writes |
| `test_anytype_write_planning.py` | 3 | Write plan generation |

## Remaining Work

| Task | Priority | Notes |
|---|---|---|
| Wire REST client into API routes | P0 | Dual-mode: prefer REST, fallback to MCP stdio |
| Live integration tests | P0 | Anytype API is now accessible, ready to test |
| Extract `anytype_service.py` | P1 | Business logic currently in route handlers |
| Split `models/anytype.py` | P1 | Status, search, write models into sub-files |
| `_ensure_connected()` decorator | P1 | DRY connection check across adapter methods |
