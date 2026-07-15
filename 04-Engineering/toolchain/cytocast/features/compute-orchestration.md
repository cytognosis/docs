# Compute Orchestration & Resource Limits

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (compute-orchestration.md in Obsidian vault: 04-Engineering/toolchain/cytocast/features/) - Agent (n/a)

Cytocast includes a built-in resource orchestration layer that enforces CPU, memory, and GPU limits on all compute-intensive operations. This enables consistent behavior across laptops, workstations, shared servers, and cloud instances.

## Resource Orchestrator

The `resource_allocated_run()` function wraps all compute-intensive Nox sessions:

```python
def resource_allocated_run(session, *args, **kwargs):
    """Run command with strict resource limits if configured."""
    cpu_limit = os.environ.get("CYTO_LIMIT_CPUS")
    mem_limit = os.environ.get("CYTO_LIMIT_MEM")
    gpu_limit = os.environ.get("CYTO_LIMIT_GPUS")
    apu_override = os.environ.get("CYTO_APU_GFX_OVERRIDE")
```

### Environment Variables

| Variable | Purpose | Example |
|:---|:---|:---|
| `CYTO_LIMIT_CPUS` | Restrict to N CPU cores via `taskset` | `CYTO_LIMIT_CPUS=4` |
| `CYTO_LIMIT_MEM` | Limit virtual memory via `prlimit` | `CYTO_LIMIT_MEM=8589934592` |
| `CYTO_LIMIT_GPUS` | Isolate N GPUs via `CUDA_VISIBLE_DEVICES` | `CYTO_LIMIT_GPUS=1` |
| `CYTO_APU_GFX_OVERRIDE` | Force AMD APU GFX version for ROCm | `CYTO_APU_GFX_OVERRIDE=10.3.0` |

### Hands-on Examples

```bash
# Run tests on 4 CPU cores only
CYTO_LIMIT_CPUS=4 nox -s test

# Train with single GPU and 8GB memory limit
CYTO_LIMIT_GPUS=1 CYTO_LIMIT_MEM=8589934592 nox -s test

# JupyterLab with GPU isolation
CYTO_LIMIT_GPUS=2 nox -s jupyter_lab

# AMD APU override for ROCm compatibility
CYTO_APU_GFX_OVERRIDE=10.3.0 nox -s test
```

## CPU Limiting via taskset

When `CYTO_LIMIT_CPUS` is set and `taskset` is available, commands are wrapped:

```bash
# Internally runs:
taskset -c 0-3 uv run pytest ...
```

This pins the process to specific CPU cores, preventing it from consuming all available cores on shared machines.

## Memory Limiting via prlimit

When `CYTO_LIMIT_MEM` is set and `prlimit` is available:

```bash
# Internally runs:
prlimit --as=8589934592 uv run pytest ...
```

This sets a hard virtual memory limit, causing OOM errors early rather than silently swapping.

## GPU Isolation

When `CYTO_LIMIT_GPUS` is set:

```python
# Sets both NVIDIA and AMD GPU visibility
env["CUDA_VISIBLE_DEVICES"] = "0,1"  # For N=2
env["HIP_VISIBLE_DEVICES"] = "0,1"   # AMD equivalent
```

## APU Support (AMD Accelerated Processing Units)

For AMD APUs with integrated graphics, the GFX version override enables ROCm compatibility:

```python
env["HSA_OVERRIDE_GFX_VERSION"] = "10.3.0"
env["PYTORCH_HIP_ALLOC_CONF"] = "garbage_collection_threshold:0.6,max_split_size_mb:128"
```

## Sessions Using Resource Orchestrator

The following Nox sessions respect resource limits:

| Session | Category |
|:---|:---|
| `jupyter_lab` | Interactive computing |
| `marimo_edit` | Interactive computing |
| `quarto_preview` | Documentation |
| `quarto_build` | Documentation |
| `quarto_publish` | Documentation |
| `test` | Testing |

## DevContainer Resource Limits

For Docker-based development, resource limits can also be set in `devcontainer.json`:

```json
{
  "runArgs": [
    "--cpus=4",
    "--memory=8g",
    "--gpus=1"
  ]
}
```

## Design Decisions

**Why environment variables instead of config files?**
Environment variables are universal across local machines, CI/CD, Docker, and Kubernetes. They do not require any project-level configuration changes and can be set per-invocation.

**Why taskset/prlimit instead of cgroups?**
`taskset` and `prlimit` are available without root privileges, unlike cgroup-based solutions. They work on any Linux machine without special setup.

[← Back to the Comparative Study](comparative_study.md)
