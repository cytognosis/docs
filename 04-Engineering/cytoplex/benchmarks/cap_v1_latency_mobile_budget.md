# CAP v1 Latency and Mobile Resource Budget Benchmark

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Generated:** 2026-05-25T08:17:39+00:00
**Benchmark id:** `cap-v1-latency-mobile-resource-local`
**Scope:** local deterministic microbenchmark evidence, not production certification.

## Environment

| Field | Value |
|---|---|
| Python | `3.12.12` |
| Platform | `macOS-26.3-arm64-arm-64bit` |
| Machine | `arm64` |
| Processor | `arm` |
| CPU count | `8` |
| Implementation | `CPython` |

## Configuration

| Field | Value |
|---|---|
| Iterations | `50` |
| Warmup | `5` |
| Command | `cap-run-v1-benchmarks --iterations 50 --warmup 5` |
| Local only | `True` |
| Dependencies | `Python stdlib plus repository runtime modules` |

## Results

| Benchmark | Path | p50 ms | p95 ms | CPU ms / 1000 ops | Tracemalloc peak KiB |
|---|---|---:|---:|---:|---:|
| direct_mcp_tool_handler | direct_tool | 0.019 | 0.020 | 20.880 | 5.2 |
| cap_mediated_mcp_tools_call | cap_mediated_tool | 4.607 | 5.108 | 4604.520 | 81.3 |
| edge_pep_verify_envelope | edge_pep | 3.010 | 3.366 | 2988.940 | 31.8 |
| direct_user_output_emit | direct_output | 0.000 | 0.001 | 1.740 | 2.1 |
| local_pep_user_output_gate | local_pep | 0.021 | 0.025 | 23.040 | 73.1 |
| direct_stream_concat | direct_stream | 0.001 | 0.001 | 2.160 | 1.9 |
| cap_live_stream_gate | cap_stream | 0.303 | 0.385 | 319.480 | 37.9 |
| android_mobile_proxy_user_output | mobile_android | 0.026 | 0.029 | 27.680 | 79.5 |
| ios_mobile_proxy_user_output | mobile_ios | 0.026 | 0.031 | 28.920 | 79.5 |

## CAP Overhead Comparisons

| Comparison | p50 overhead ms | p95 overhead ms | p50 ratio |
|---|---:|---:|---:|
| mcp_tools_call_cap_over_direct | 4.587 | 5.088 | 238.00x |
| user_output_local_pep_over_direct_emit | 0.021 | 0.024 | 46.40x |
| streaming_cap_gate_over_direct_concat | 0.302 | 0.384 | 519.40x |

## Streaming Delay

| Metric | Value |
|---|---:|
| Observed frame delay p50 ms | `0.000` |
| Observed frame delay p95 ms | `0.000` |
| Deterministic timer-release delay ms | `250.000` |
| Configured max buffer tokens | `50` |
| Configured max buffer chars | `500` |
| Configured max buffer ms | `250` |

Observed frame delay is from the local scripted stream path. The deterministic timer-release row advances a manual clock to the configured buffer limit to verify the default CAP v1 hold budget.

## Resource and Battery Proxies

CPU and memory columns are process-local Python measurements. Battery is represented by `cpu_time_ms_per_1000_ops`; this is a relative proxy only and not measured device power or battery drain.

## Caveats

- Numbers are local microbenchmarks from this checkout and machine.
- The mobile measurements are Python proxy-path measurements, not native Android/iOS device telemetry.
- Battery is represented only by CPU-time proxy units; no power rail, OS battery API, or device profiler is sampled.
- The direct MCP/tool path intentionally bypasses CAP checks and is not a safe execution recommendation.
- Production model providers, native UI wrappers, service meshes, registries, and networked PDPs can change latency substantially.
