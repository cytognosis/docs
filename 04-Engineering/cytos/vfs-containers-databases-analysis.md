# VFS Enhancement, Container Strategy, and Database Benchmarking

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (vfs-containers-databases-analysis.md in Obsidian vault: 04-Engineering/cytos/) - Agent (n/a)

> **Date**: 2026-05-26 · **Status**: ANALYSIS — Awaiting review

---

## Question 1: VFS — What to Adopt from DagsHub Client + TileDB

### Current Cytoskeleton VFS Strengths (Keep These)

Our VFS already has things neither DagsHub nor TileDB have:

| Feature | Only We Have It | Why It Matters |
|---|---|---|
| **SWHID content-addressing** on every `put()` | ✅ | Permanent, standards-backed identity (Software Heritage) |
| **W3C PROV-J sidecars** auto-generated | ✅ | Lineage tracking at the VFS layer |
| **7 diverse backends** (GitHub API, HF Hub, Zenodo, git-local) | ✅ | Scientific publishing ecosystem coverage |
| **Config resolution chain** (args → env → config → CWD → fallback) | ✅ | Zero-config + full control |
| **DOI resolution** (Zenodo driver) | ✅ | Immutable citable deposits |

These are non-negotiable. No other VFS in the biomedical space does provenance at the filesystem layer.

---

### What to Adopt from TileDB VFS

TileDB VFS is the performance benchmark. Three features would dramatically improve our cloud I/O:

#### Feature T1: Byte-Range Reads (HIGH PRIORITY)

**What it is**: Instead of downloading an entire 50GB file to read 100 bytes, fetch only the requested byte range via HTTP Range headers.

**Why we need it**: Our GCS and S3 drivers currently download the full object on every `open()`. For Parquet files (column-oriented), you often need only a few columns out of dozens. Byte-range reads turn a 50GB download into a 500KB fetch.

**TileDB's implementation**: `vfs.min_batch_size` and `vfs.min_batch_gap` group adjacent range requests to avoid excessive HTTP round-trips.

**Proposed implementation in cytoskeleton**:

```python
# New method on AbstractVFS
def open_range(self, uri: str, offset: int, length: int) -> bytes:
    """Read a byte range without downloading the full object."""
    raise NotImplementedError

# GCS implementation
class GCSVFS(AbstractVFS):
    def open_range(self, uri: str, offset: int, length: int) -> bytes:
        blob = self._bucket.blob(self._key(uri))
        return blob.download_as_bytes(start=offset, end=offset + length - 1)

# S3 implementation
class S3VFS(AbstractVFS):
    def open_range(self, uri: str, offset: int, length: int) -> bytes:
        resp = self._client.get_object(
            Bucket=self._bucket, Key=self._key(uri),
            Range=f"bytes={offset}-{offset + length - 1}"
        )
        return resp["Body"].read()
```

**Effort**: ~1 day. GCS and S3 both natively support Range headers.

#### Feature T2: In-Memory LRU Cache (MEDIUM PRIORITY)

**What it is**: Cache recently-read data in memory so repeated reads of the same file don't hit the network.

**TileDB's implementation**: `sm.tile_cache_size` configures an LRU cache for decompressed tiles.

**Proposed implementation**: Add an optional cache layer in `get_vfs()` that wraps any backend:

```python
from functools import lru_cache

class CachedVFS(AbstractVFS):
    """Wrapper that adds LRU caching to any VFS backend."""
    def __init__(self, inner: AbstractVFS, max_cache_mb: int = 512):
        self._inner = inner
        self._cache = {}  # uri → (bytes, timestamp)
        self._max_bytes = max_cache_mb * 1024 * 1024

    def open(self, uri, mode="r", **kw):
        if mode == "r" and uri in self._cache:
            return io.BytesIO(self._cache[uri])
        result = self._inner.open(uri, mode, **kw)
        if mode == "r":
            data = result.read()
            self._evict_if_needed(len(data))
            self._cache[uri] = data
            return io.BytesIO(data)
        return result
```

**Effort**: ~0.5 day for basic LRU, ~1.5 days for proper TTL + size-aware eviction.

#### Feature T3: Parallel I/O Thread Pool (LOWER PRIORITY)

**What it is**: When listing or fetching multiple objects, use a thread pool instead of sequential requests.

**TileDB's implementation**: `vfs.num_threads` and per-backend `max_parallel_ops`.

**Proposed implementation**: Add a `get_many()` bulk-fetch method:

```python
from concurrent.futures import ThreadPoolExecutor

class AbstractVFS:
    def get_many(self, uris: list[str], local_dir: str, max_workers: int = 4):
        """Parallel download of multiple URIs."""
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {
                pool.submit(self.get, uri, Path(local_dir) / Path(uri).name): uri
                for uri in uris
            }
            return {uri: f.result() for f, uri in futures.items()}
```

**Effort**: ~0.5 day. Use `concurrent.futures` (stdlib, no new deps).

---

### What to Adopt from DagsHub Client

DagsHub Client's power is in **transparent interception**. Three features are worth adopting.

#### Feature D1: Lazy Materialization (Local Cache + Remote Fallback) (HIGH PRIORITY)

**What it is**: When you `open("cytognosis://datasets/umls/concepts.parquet")`, the VFS checks a local cache directory first. If the file is there, use it. If not, download from GCS, cache locally, then serve. Subsequent reads are instant.

**DagsHub's implementation**: Their filesystem hook checks `~/.dagshub/cache/` before making HTTP requests. Files persist across sessions.

**Proposed implementation**: Add a `DiskCachedVFS` wrapper (disk-backed cache with remote fallback):

```python
class DiskCachedVFS(AbstractVFS):
    """Disk cache with remote fallback. Like DagsHub, but explicit."""

    def __init__(self, inner: AbstractVFS, cache_dir: Path = Path("~/.cytoskeleton/cache")):
        self._inner = inner
        self._cache_dir = cache_dir.expanduser()
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def get(self, uri: str, local_path: str | Path) -> None:
        cached = self._cache_path(uri)
        if cached.exists():
            shutil.copy2(cached, local_path)  # instant local copy
            return
        self._inner.get(uri, local_path)
        shutil.copy2(local_path, cached)  # populate cache

    def open(self, uri: str, mode: str = "r", **kw):
        if mode.startswith("r"):
            cached = self._cache_path(uri)
            if not cached.exists():
                self._inner.get(uri, cached)
            return open(cached, mode, **kw)
        return self._inner.open(uri, mode, **kw)

    def _cache_path(self, uri: str) -> Path:
        # Content-addressed: hash the URI for flat cache structure
        key = hashlib.sha256(uri.encode()).hexdigest()
        return self._cache_dir / key[:2] / key
```

**Effort**: ~1 day. The cache invalidation strategy needs thought (TTL? hash-based? manual `cache clear`?).

#### Feature D2: Monkeypatching / Transparent Hook System (HIGH PRIORITY)

**What it is**: DagsHub intercepts Python builtins (`open()`, `stat()`, `os.path.exists()`, `listdir()`, `scandir()`) so that existing code can transparently access remote data without any URI changes. Call `install_hooks()` to activate, `uninstall_hooks()` to revert.

**Why we adopt it**: This is the foundation for automated provenance tracking later. When hooks are active, every `open()` call can be intercepted to record what was read/written, by whom, and when, feeding directly into our W3C PROV-J provenance system. Without hooks, provenance tracking requires explicit `vfs.open()` calls everywhere, which is unrealistic for third-party libraries.

**Known limitations** (accept and document):
- Does NOT work with C/C++ level I/O (TensorFlow's `tf.io`, OpenCV's `imread`, etc.)
- Not thread-safe during `install_hooks()`/`uninstall_hooks()` (safe once installed)
- Should never be active in production serving code; only in pipelines/notebooks

**Proposed implementation**: `cytoskeleton/vfs/hooks.py`

```python
"""Opt-in transparent VFS hooks for automated provenance tracking.

Usage:
    from cytoskeleton.vfs.hooks import install_hooks, uninstall_hooks

    install_hooks(backend="gcs", provenance=True)  # Start intercepting
    # ... existing code using open(), os.path.exists() works transparently ...
    uninstall_hooks()  # Restore originals
"""
import builtins
import os
from contextlib import contextmanager

_original_open = builtins.open
_original_exists = os.path.exists
_original_stat = os.stat
_hooks_active = False

def install_hooks(
    vfs: "AbstractVFS | None" = None,
    provenance: bool = False,
    path_prefix: str = "/data/",
):
    """Patch builtins to route matching paths through our VFS.

    Args:
        vfs: VFS backend to use. If None, uses get_vfs() defaults.
        provenance: If True, log every open() to a ProvenanceRecord.
        path_prefix: Only intercept paths starting with this prefix.
    """
    global _hooks_active
    if _hooks_active:
        return  # Idempotent

    from cytoskeleton.vfs import get_vfs
    _vfs = vfs or get_vfs()

    def _hooked_open(file, mode="r", *args, **kwargs):
        if isinstance(file, str) and file.startswith(path_prefix):
            if provenance:
                _log_access(file, mode)
            return _vfs.open(file, mode)
        return _original_open(file, mode, *args, **kwargs)

    builtins.open = _hooked_open
    _hooks_active = True

def uninstall_hooks():
    """Restore original builtins."""
    global _hooks_active
    builtins.open = _original_open
    os.path.exists = _original_exists
    os.stat = _original_stat
    _hooks_active = False

@contextmanager
def hooked(vfs=None, provenance=False, path_prefix="/data/"):
    """Context manager for scoped hook activation."""
    install_hooks(vfs=vfs, provenance=provenance, path_prefix=path_prefix)
    try:
        yield
    finally:
        uninstall_hooks()
```

**Key design choices**:
- **Opt-in, not default**: Never active unless explicitly called
- **Path-prefix gated**: Only intercepts paths matching a configurable prefix, avoiding system file interference
- **Context manager**: `with hooked():` pattern for safe scoped activation
- **Provenance parameter**: When `True`, logs every access to a `ProvenanceRecord`

**Effort**: ~1.5 days (hooks + provenance logging + tests for install/uninstall safety).

#### Feature D3: MLflow Failsafe Patching Pattern (MEDIUM PRIORITY — for cytoskills)

**What it is**: DagsHub wraps MLflow's logging functions so network failures don't crash training runs. Instead of `mlflow.log_metric()` raising `ConnectionError`, it prints a warning and continues.

**This belongs in cytoskills, not cytoskeleton**. cytoskeleton is infrastructure; MLflow integration is a skill/workflow concern.

**Proposed location**: `cytoskills/skills/mlflow-failsafe/` — a skill that patches MLflow for resilient logging.

---

### What NOT to Adopt

| Feature | Why Skip |
|---|---|
| **DagsHub Data Engine** | SaaS-only feature, not open-source |
| **TileDB array tiling/compression** | We already use TileDB-SOMA and TileDB-VCF directly for array data; no need to reimplement tiling in our VFS |
| **TileDB async I/O** | Only in C++ API, not Python. Use `concurrent.futures` instead |
| **FUSE mount** (DagsHub experimental) | OS-specific (Linux/macOS), rootless FUSE has reliability issues, adds kernel dependency |

---

### Summary: VFS Enhancement Roadmap

| Priority | Feature | Source | Effort | Location |
|---|---|---|---|---|
| 🔴 **P0** | Byte-range reads (`open_range`) | TileDB | 1 day | `cytoskeleton/vfs/base.py` + GCS/S3 |
| 🔴 **P0** | Disk-backed cache (lazy materialization) | DagsHub | 1 day | `cytoskeleton/vfs/cache.py` (new) |
| 🔴 **P0** | Monkeypatching hooks (`install_hooks`) | DagsHub | 1.5 days | `cytoskeleton/vfs/hooks.py` (new) |
| 🟡 **P1** | In-memory LRU cache | TileDB | 1 day | `cytoskeleton/vfs/cache.py` |
| 🟡 **P1** | Parallel bulk `get_many()` | TileDB | 0.5 day | `cytoskeleton/vfs/base.py` |
| 🟢 **P2** | MLflow failsafe patching | DagsHub | 0.5 day | `cytoskills/skills/mlflow-failsafe/` |

**Total**: ~5.5 days to materially upgrade the VFS with the best ideas from both.

---

### Other DagsHub Client Features: Where They Fit

| DagsHub Feature | Adopt? | Where in Cytognosis |
|---|---|---|
| **Streaming filesystem** (lazy download) | ✅ As disk cache | `cytoskeleton/vfs/cache.py` |
| **Monkeypatching hooks** | ✅ As opt-in hooks module | `cytoskeleton/vfs/hooks.py` |
| **MLflow failsafe wrapper** | ✅ As a skill | `cytoskills/skills/mlflow-failsafe/` |
| **Content-addressed DVC storage** | Already have | DVC + `https://github.com/cytognosis/datasets/tree/main/.dvc/config` → GCS |
| **Label Studio integration** | ❌ Not now | Would go in cytos annotation module if ever needed |
| **Data Engine (SQL-over-datasets)** | ❌ Not now | DuckDB already fills this role (`KGStore`) |
| **Git+DVC hosting** | ❌ We use GitHub + GCS | No need for DagsHub SaaS |

---

## Question 2: Container Runtime + Cytohost Strategy

### Runtime Decision: Podman preferred, Docker fallback (already implemented)

| Runtime | Role | Status |
|---|---|---|
| **Podman** | Primary. Rootless, no daemon, 65-70% less idle memory | ✅ Already preferred in `stack_manager.py` |
| **Docker** | Fallback for volume-heavy workloads (Neo4j volume permissions) | ✅ Already available with `sudo` |
| **Toolbx** | Skip | Not relevant (Fedora Silverblue interactive tool) |
| **Distrobox** | Optional for local dev | Not installed, not needed for services |

### Performance Numbers That Matter

| Metric | Podman vs Docker | Impact on Us |
|---|---|---|
| Idle memory | Podman saves 100-180 MB (no daemon) | Matters on resource-constrained hosts |
| Container startup | Docker ~0.4s faster | Irrelevant for long-running services |
| I/O throughput | Identical (both near-native) | No difference |
| Rootless overhead | 25-30% startup penalty only | Only matters for CI, not services |

### Cytohost: Shift to On-Demand Service Model

**Current reality**: None of the 8 services on cytohost are actively used (except cal.com, sporadically). All 8 are consuming resources for nothing.

**New model**: Services should be on-demand. All down by default, brought up when needed.

#### Required Infrastructure Tooling

`stack_manager.py` already supports `start`/`stop`/`restart`/`status`. Extend to support:

| Command | What It Does |
|---|---|
| `stack_manager.py up <service>` | Start a specific service (alias for `start`) |
| `stack_manager.py down <service>` | Stop a specific service cleanly |
| `stack_manager.py down --all` | Stop ALL services (default state) |
| `stack_manager.py up --stack <name>` | Start a named stack (e.g., `research` = neo4j + jupyter + mlflow) |
| `stack_manager.py down --stack <name>` | Stop a named stack |
| `stack_manager.py ls` | List what's currently running |

This frees all 8 GB for whichever service you actually need at the moment.

#### Cytohost Sizing Options

| Instance | vCPU | RAM | Monthly (On-Demand) | Monthly (1yr CUD) | Note |
|---|---|---|---|---|---|
| **t2a-standard-2** (current) | 2 | 8 GB | ~$45 | ~$29 | Tight for databases |
| **e2-highmem-2** (x86, cheapest 16GB) | 2 | 16 GB | **~$66** | ~$43 | Best bang-per-buck for 16 GB |
| **t2a-standard-4** (ARM, 16 GB) | 4 | 16 GB | ~$112 | ~$73 | 2× more CPU than needed |
| **n2-highmem-2** (x86, 16 GB) | 2 | 16 GB | ~$77 | ~$50 | Higher consistent perf than E2 |

> [!IMPORTANT]
> **Recommendation**: Switch to **`e2-highmem-2`** ($66/mo, 2 vCPU, 16 GB). With the on-demand model (all services default off), 16 GB is enough to run Neo4j (4-8 GB) or SurrealDB (2-4 GB) alongside cal.com when needed. The $21/mo increase over current buys 2× the RAM. Loses ARM64 (moves to x86), but this eliminates the QEMU emulation penalty for Cal.com and Excalidraw Room that currently run as amd64 under emulation on ARM.
>
> The ARM→x86 switch also simplifies container management (no more `platform: linux/amd64` overrides) and gives access to a wider Docker image ecosystem.

#### Alternative: Keep ARM, Add Spot for Databases

If keeping ARM64 matters, keep the current `t2a-standard-2` for always-on cal.com and use on-demand spot instances for database work:

| Purpose | Instance | Cost |
|---|---|---|
| Always-on (cal.com only) | `t2a-standard-2` (8 GB) | ~$45/mo |
| Database benchmarking | `e2-highmem-2` spot (16 GB) | ~$0.045/hr (~$3/day) |
| Heavy ETL/imports | `n2-standard-8` spot (32 GB) | ~$0.10/hr |

---

## Question 3: Neo4j vs SurrealDB — Benchmarking Plan

### Current State

| | Neo4j | SurrealDB |
|---|---|---|
| **Container config** | ✅ `neo4j.yaml` in container_framework | ❌ No config exists |
| **Native install** | ❌ Not installed | ⚠️ Binary downloaded but import failed |
| **Python client** | ✅ `cytos/db/neo4j/client.py` (working) | ⚠️ `cytos/db/surrealdb/client.py` (has bugs) |
| **KG data on disk** | ✅ `neo4j_nodes.csv` (810 MB) + `neo4j_edges.csv` (5.1 GB) | ⚠️ `nodes.surql` (852 MB) + `edges.surql` (7.1 GB) — import broken |
| **Architecture decision** | Current production | Future target (ADR-005, ADR-007) |

### Our KG Size

| Metric | Value |
|---|---|
| Nodes | 9.2M (dev) → 10.7M (target) |
| Edges | 52.4M (dev) → 118.5M (target) |
| Raw TSV on disk | ~15 GB |
| Neo4j CSV exports | ~6 GB |
| SurrealDB .surql exports | ~8 GB |

### Resource Requirements

| Config | Engine | RAM Needed | Disk | Notes |
|---|---|---|---|---|
| Neo4j container (dev) | Neo4j 5.18 CE | 4-8 GB (heap 2G + pagecache 2-6G) | ~10 GB | G1GC, APOC |
| Neo4j container (prod) | Neo4j 5.18 CE | 8-16 GB (heap 4G + pagecache 4-8G) | ~10 GB | Pagecache should cover dataset |
| Neo4j native | Same | Same | Same | Docker overhead is negligible for Neo4j |
| SurrealDB container (dev) | SurrealDB 3.x | 2-4 GB | ~12 GB | SurrealKV backend, block_cache |
| SurrealDB native | Same | Same | Same | No JVM; lighter baseline |

> [!IMPORTANT]
> Docker vs native overhead for databases is **negligible** in both cases. The bottleneck is always disk I/O and memory allocation, not container overhead. The benchmark should still measure it to confirm, but expect <5% difference.

### Laptop Resources (Estimated)

From SurrealDB logs (block_cache set to ~48 GB), this machine likely has:
- **RAM**: ~64 GB
- **CPU**: x86_64 multi-core
- **Disk**: NVMe SSD (based on the I/O patterns)

> [!NOTE]
> Need to verify with `free -h`, `nproc`, `lscpu`, `df -h` before benchmarking.

### Proposed Benchmark Configurations

With the on-demand model, cytohost resources are freed up. Run benchmarks with services stopped.

| Label | Engine | Deploy | Where | Memory Config |
|---|---|---|---|---|
| **A** | Neo4j 5.18 | Podman container | Laptop | heap=4G, pagecache=8G |
| **B** | Neo4j 5.18 | Native JVM | Laptop | heap=4G, pagecache=8G |
| **C** | Neo4j 5.18 | Podman container | cytohost (services down) | heap=2G, pagecache=4G |
| **D** | SurrealDB 3.x | Podman container | Laptop | block_cache=16G |
| **E** | SurrealDB 3.x | Native binary | Laptop | block_cache=16G |
| **F** | SurrealDB 3.x | Podman container | cytohost (services down) | block_cache=4G |

### Benchmark Categories

| # | Test | Queries | Measures |
|---|---|---|---|
| 1 | **Bulk Import** | Full KG load (nodes + edges) | Wall-clock time, peak memory |
| 2 | **Point Lookups** | 100 random node fetches | p50/p95/p99 latency |
| 3 | **1-Hop Traversal** | 100 random `neighbors(n)` | p50/p95/p99 latency |
| 4 | **2-Hop Traversal** | 50 random 2-hop expansions | p50/p95/p99 latency, result count |
| 5 | **Shortest Path** | 20 random pairs | p50/p95/p99 latency |
| 6 | **Aggregation** | Count nodes by type/label | Wall-clock time |
| 7 | **Cold Start** | Time from `start` → first query | Seconds |
| 8 | **Network Latency** | Same queries, laptop → cytohost | p50/p95 latency over network |

### Pre-Benchmark Steps

1. **Verify laptop specs**: `free -h`, `nproc`, `lscpu`, `df -h`
2. **Fix SurrealDB import**: Add `OPTION IMPORT;` header to `.surql` files
3. **Fix SurrealDB client**: The `__aenter__`/`__aexit__` bug needs fixing
4. **Create SurrealDB container config**: Add `surrealdb.yaml` to `container_framework/configs/services/`
5. **Install Neo4j native**: Download Community Edition tarball
6. **Write benchmark script**: Python script with `time.perf_counter()`, `psutil` for memory, structured JSON output

### Proposed Script Layout

```
~/repos/cytognosis/infrastructure/benchmarks/
├── README.md
├── configs/
│   ├── neo4j_local.yaml
│   ├── neo4j_remote.yaml
│   ├── surreal_local.yaml
│   └── surreal_remote.yaml
├── import/
│   ├── neo4j_import.sh
│   └── surreal_import.sh
├── queries/
│   ├── benchmark.py          # Main runner
│   ├── neo4j_queries.py      # Neo4j Cypher queries
│   └── surreal_queries.py    # SurrealQL queries
├── analyze/
│   └── compare.py            # Generate comparison tables
└── results/
    └── .gitkeep
```

### What We Expect to Find

| Dimension | Neo4j Likely Wins | SurrealDB Likely Wins |
|---|---|---|
| **Deep traversals** (2+ hops) | ✅ Graph-native index-free adjacency | |
| **Graph algorithms** (PageRank, centrality) | ✅ GDS library | |
| **Cold start time** | | ✅ No JVM warmup |
| **Memory efficiency** | | ✅ No JVM overhead |
| **Bulk import speed** | ✅ `neo4j-admin import` is highly optimized | |
| **Mixed workloads** (graph + document + search) | | ✅ Multi-model |
| **Operational simplicity** | | ✅ Single binary, no JVM tuning |
| **Point lookups** | Tie | Tie |
| **Container overhead** | Negligible | Negligible |

---

## Impact on Implementation Plan v4

### Additions to Plan

| Phase | New Task | Effort | Priority |
|---|---|---|---|
| **New Phase 1.5** | VFS enhancements: byte-range reads + disk cache + hooks | 3.5 days | 🔴 P0 |
| **Phase 2 (extended)** | `stack_manager.py` on-demand tooling (`up`/`down`/`ls` polish) | 0.5 day | 🔴 P0 |
| **Phase 2 (extended)** | Evaluate `e2-highmem-2` pricing + migration plan | 0.5 day | 🟡 P1 |
| **New Phase 4.5** | Create SurrealDB container config (`surrealdb.yaml`) | 0.5 day | 🟡 P1 |
| **New Phase 4.5** | Fix SurrealDB import + client bugs | 1 day | 🟡 P1 |
| **New Phase 4.5** | Write benchmark script + run 6 configurations | 2 days | 🟡 P1 |
| **Phase 4A (existing)** | Neo4j load test (now part of benchmark) | Merged | Merged |

### Items NOT Changing

- Container runtime strategy: already correct (Podman → Docker fallback)
- DVC tracking plan: unaffected
- Data/code separation: unaffected
- Schema cleanup: unaffected
- Deferred items (LaminDB, redun, SEEK): still deferred

### Revised Total Estimate

Original v4: ~8 hours
New additions: ~8 days (VFS 3.5d + stack tooling 0.5d + pricing 0.5d + SurrealDB fix 1d + benchmarks 2d + buffer 0.5d)
**Revised total**: ~8 hours immediate (DVC/schemas/docs) + 8 days VFS/benchmark/infra work

VFS and benchmark work can be parallelized across sessions. The DVC/schema/docs work is independent.

---

## Open Questions for Your Review

1. **VFS byte-range reads**: Implement for GCS + S3 only, or also for GitHub/HF Hub? (GitHub raw CDN doesn't support Range headers reliably)

2. **Disk cache location**: `~/.cytoskeleton/cache/` (user-level, persistent) or `$XDG_CACHE_HOME/cytoskeleton/` (XDG-compliant)?

3. **SurrealDB investment**: ADR-005/007 target SurrealDB as the future KG backend, but it's currently broken (import failed, client has bugs). Is benchmarking it now the right use of time, or should we get Neo4j working perfectly first and revisit SurrealDB when it's more mature?

4. **Cytohost migration**: Switch from `t2a-standard-2` (8GB ARM, $45/mo) to `e2-highmem-2` (16GB x86, $66/mo)? The $21/mo increase doubles RAM and eliminates QEMU emulation for Cal.com/Excalidraw.

5. **VFS parallel I/O**: Should `get_many()` be on `AbstractVFS` (all backends) or only on cloud backends (GCS, S3)?
