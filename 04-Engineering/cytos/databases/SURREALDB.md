# SurrealDB — Status and Known Issues

> Running at: `ws://localhost:8000`
> Container: `cytos-surrealdb` (Docker)
> Version: surrealdb/surrealdb:latest

---

## Current State

SurrealDB is running but has no genomics schema defined yet.
The client has a known async context manager bug.

### What Works
- Docker container starts and stays up (34+ hours uptime)
- Basic SurrealDB queries work via raw `surrealdb` Python client
- Benchmark results (vs Neo4j) show SurrealDB is **faster** for simple lookups:
  - Lookup: Neo4j 0.35s vs SurrealDB 0.001s
  - 1-hop traversal: Neo4j 0.006s vs SurrealDB 0.001s
  - Aggregation: Neo4j 0.006s vs SurrealDB 0.001s

### What Doesn't Work
1. **`SurrealClientManager` async context manager bug**
   ```python
   # This fails:
   async with SurrealClientManager() as db:
       ...
   # Error: 'SurrealClientManager' object does not support async context manager protocol
   ```
   **Fix:** Add `__aenter__` and `__aexit__` to `src/cytos/db/surrealdb/client.py`

2. **No genomics schema tables** — tables for Variant, SNP, GWASHit, Trait not defined

3. **`linkml_to_surreal.py` not implemented** — planned translator from LinkML to SurrealQL DDL

---

## Architecture Role

SurrealDB is designed as a **parallel store** to Neo4j, with different specialization:

| Data type | Store | Reason |
|-----------|-------|--------|
| Population genomics (Gene, GWASHit, Trait) | Neo4j | Graph traversal, Cypher queries |
| Sensor/clinical/personal data | SurrealDB | Document + graph hybrid, fast lookup |
| Schema definitions | SurrealDB | SCHEMAFULL tables from LinkML |

**Open question:** Should SurrealDB also mirror the genomics graph (Gene, Variant, GWASHit)?
Benchmark shows SurrealDB is faster. But Neo4j has richer graph query capabilities.

---

## Connecting from Python

```python
# Once async CM bug is fixed:
import asyncio
from cytos.db.surrealdb.client import SurrealClientManager

async def query():
    async with SurrealClientManager() as db:
        await db.use("cytos", "main")
        result = await db.query("SELECT * FROM Trait LIMIT 5")
        return result

asyncio.run(query())

# Environment variables:
# SURREAL_URL=ws://localhost:8000
# SURREAL_USER=root
# SURREAL_PASS=root
# SURREAL_NS=cytos
# SURREAL_DB=main
```

---

## Fix Required: Async Context Manager

In `src/cytos/db/surrealdb/client.py`, add:

```python
class SurrealClientManager:
    def __init__(self, url=None, user=None, password=None, ns=None, db=None):
        ...

    async def __aenter__(self):
        from surrealdb import Surreal
        self._client = Surreal(self.url)
        await self._client.connect()
        await self._client.signin({"user": self.user, "pass": self.password})
        await self._client.use(self.ns, self.db)
        return self._client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.close()
```

---

## Schema DDL (to be implemented)

Once `linkml_to_surreal.py` is built, run:
```surql
DEFINE TABLE Variant SCHEMAFULL;
DEFINE FIELD rsid ON Variant TYPE string;
DEFINE FIELD chrom ON Variant TYPE string;
DEFINE FIELD pos ON Variant TYPE int;
DEFINE FIELD ref ON Variant TYPE string;
DEFINE FIELD alt ON Variant TYPE string;
DEFINE FIELD vrs_id ON Variant TYPE option<string>;

DEFINE TABLE Trait SCHEMAFULL;
DEFINE FIELD name ON Trait TYPE string;
DEFINE FIELD efo_id ON Trait TYPE string;
DEFINE FIELD mondo_id ON Trait TYPE option<string>;

DEFINE TABLE GWASHit SCHEMAFULL;
DEFINE FIELD rsid ON GWASHit TYPE string;
DEFINE FIELD chrom ON GWASHit TYPE string;
DEFINE FIELD pos ON GWASHit TYPE int;
DEFINE FIELD pval ON GWASHit TYPE float;
DEFINE FIELD beta ON GWASHit TYPE float;
```

---

## Docker Start Command

```bash
docker run -d \
  --name cytos-surrealdb \
  -p 8000:8000 \
  -v /home/mohammadi/datasets/15-databases/surrealdb:/data \
  surrealdb/surrealdb:latest \
  start --user root --pass root surrealkv:///data/cytos.db

# Or via docker-compose (planned):
docker-compose up -d surrealdb
```
