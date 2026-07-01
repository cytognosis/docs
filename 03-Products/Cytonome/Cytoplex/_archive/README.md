> **Status:** SUPERSEDED · **Archived:** 2026-07-01 · **Superseded by:** `03-Products/Cytonome/Cytoplex/cytoplex-readme.md`
>
> Near-duplicate overview; kept for its cross-links and naming note. Kept for provenance; do not edit.

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cap`, `cytoplex`

# Cytoplex — Yar's Safety, Authority & Coordination Component

> [!IMPORTANT]
> **TL;DR**: Cytoplex is the home of **CAP (Controller-Authority Protocol)**, the hard safety and authority boundary that governs everything Yar does. It is a **standalone protocol** (its own spec, conformance suite, and future standalone repo) that is **integrated into Yar** as the guard between the model and any action. If Yar is the navigator, Cytoplex is the rulebook that says which moves are allowed.

## What Cytoplex is

Cytoplex is a Yar component, nested at `docs/cytonome/yar/cytoplex/`. It defines and documents **CAP**, the protocol that:

- decides whether any proposed action (a **Directive**) may execute, using a deny-wins **Guard**;
- keeps raw private data on-device by default;
- blocks diagnosis and treatment claims, and forces uncertainty language for unconfirmed social interpretations;
- records every decision in a tamper-evident **hash-chain audit** trail.

CAP ships in two profiles: **CAP-Lite** (the lightweight profile Yar's MVP uses) and **CAP-Med** (a stricter clinical profile). The v0.1 protocol covers the Directive lifecycle, Guard decisions, refusal messages, execution reports, decision records, the audit chain, Ed25519 / JWS / DSSE / in-toto signing, and HTTP and gRPC transport bindings, with a passing conformance suite.

## Standalone, but integrated

| Dimension | How it works |
|---|---|
| **Standalone** | CAP has its own specification (`spec/`), conformance and hardening tests, benchmarks, threat model, and a planned extraction to a standalone repo (`github.com/cytognosis/cap`). Other agents and organizations can adopt CAP without Yar. |
| **Integrated with Yar** | Yar runs **CAP-Lite** as the boundary before model routing and before any external write. See the Yar master `§8 Safety` and the architecture index. Nothing leaves the device or hits a tool without passing the Guard. |
| **Platform tie-in** | CAP is the Cytognosis platform's safety primitive (the open-science / Apache 2.0 half of the bifurcation). Cytoplex is its documentation home. |

## Doc-set map

**Start here, then go deep:**

| Area | Path | What is in it |
|---|---|---|
| Revision plan & deep-dive | [`overview.md`](overview.md) | Current CAP scope, gaps, v0.2 proposed scope, phased plan, target standalone package structure. |
| **Formal spec** | [`spec/`](spec/) | The narrative specification: `01_foundations` → `07_profiles_roadmap`, plus `architecture.md`, `claims.md`, `appendix_schemas.md`, conformance, and release gates. |
| Consolidated baseline | [`v1-baseline/00_INDEX.md`](v1-baseline/00_INDEX.md) | A single consolidated v1 baseline (status, foundations, architecture, primitives, security, integrations, conformance, schema appendix, examples). |
| Security | [`security/`](security/) | Threat model, security review, KMS/HSM, findings tracker. |
| Conformance & quality | [`compliance/`](compliance/) · [`quality/`](quality/) · [`interop/`](interop/) | Reviewer checklists, rubrics, report templates, interop reports. |
| Benchmarks | [`benchmarks/`](benchmarks/) | Mobile latency budget for CAP v1. |
| Research lineage | [`research/`](research/) | CAP comprehensive reference and protocol assessment. |

## How Cytoplex integrates with the rest of Yar

- **Yar master reference** (safety section): [`../yar-master-features-requirements.md`](../yar-master-features-requirements.md) `§8`.
- **Architecture index**: [`../architecture-index.md`](../architecture-index.md).
- **Product implementation**: [`../product-implementation.md`](../product-implementation.md).
- **Personas**: persona authority binding (a persona cannot assert clinical authority) is a CAP concern; see the Yar master `§4A`.
- **Sensors**: every sensor adapter in [`../sensors/`](../sensors/) is governed by CAP (per-sensor consent, on-device-by-default).

## Naming

**CAP = Controller-Authority Protocol.** This is the canonical expansion. Do not use "Communication Augmentation Protocol" or "Cognitive Architecture Protocol"; both are retired mistakes.

---

> [!NOTE]
> **ADHD-friendly variant**: a simplified reading copy of this overview lives at [`README-vault.md`](README-vault.md) (surfaced in the Obsidian vault via the symlinked docs repo). Edit this spec file; the vault variant links back here.
