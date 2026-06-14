> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytoplex`, `cap`, `steering`

---
inclusion: always
version: 1.0.0
category: product
description: Product vision and success metrics for Cytoplex (CAP)
last_updated: 2026-05-29
---

# Product Steering: Cytoplex (CAP)

## Vision

Cytoplex implements the Cytognosis Authority Protocol (CAP), a multi-layer communication protocol for interviewer/supervisor agent architectures. It defines how AI agents negotiate authority, enforce policies, maintain audit trails, and operate within trust boundaries. Cytoplex is a component of Cytonome (the Navigator) and governs all agent-to-agent communication across the Cytognosis ecosystem.

## User Personas

| Persona | Role | Primary Goal | Pain Point |
|---------|------|-------------|------------|
| Agent developer | Engineer building AI agents for health applications | Integrate authority-aware communication into agent workflows | No standard protocol for agent authority negotiation; ad-hoc trust |
| Safety engineer | Reviewer validating agent behavior in clinical contexts | Verify that agents respect authority boundaries and produce audit trails | No conformance testing framework for agent safety claims |
| Platform integrator | Engineer connecting CAP to MCP/A2A/gRPC transports | Bridge CAP primitives to existing agent communication standards | Transport-agnostic protocol layer is missing from the ecosystem |
| Healthcare compliance officer | Regulatory stakeholder | Ensure agent interactions comply with HIPAA and clinical safety standards | No structured evidence of agent authority decisions |

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Conformance test pass rate | 100% on v1 baseline | `plex-check-v1-conformance` runner output |
| Schema drift detection | Zero undetected drift | `plex-check-v1-schema-drift` CI gate |
| Authority enforcement latency | < 10ms for PEP decisions | Benchmark suite in `benchmarks.py` |
| Audit trail completeness | 100% of authority decisions logged | Observability module coverage |
| Transport coverage | HTTP JSON + gRPC + edge PEP | Binding implementation count |

## Roadmap Priorities (Current Quarter)

1. Complete v1 conformance suite and lock the v1 baseline schema
2. Ship therapist-supervisor scenario as the reference CAP deployment
3. Harden security layer (crypto, certificates, transparency logs)
4. Implement MCP and A2A interop bindings for cross-ecosystem compatibility

## Non-Goals

- Cytoplex is not an agent framework; it is a protocol and enforcement library
- No built-in LLM inference (agents bring their own models)
- No user-facing UI (protocol is consumed by developer APIs and CLIs)
- No proprietary extensions; the protocol specification is fully open
