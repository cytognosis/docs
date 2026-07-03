> **Status:** SUPERSEDED · **Archived:** 2026-07-01 · **Superseded by:** `03-Products/Cytonome/Cytoplex/cap-readme.md`
>
> ADHD restatement of CAP; the ADHD variant belongs in Obsidian. Kept for provenance; do not edit.

> **Status**: Active
> **Date**: 2026-05-29
> **Author**: \@mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `protocol`, `reference`

# 🛡️ CAP / Cytoplex — ADHD Summary

**BLUF:** CAP (Cytognosis Authority Protocol) is the safety and coordination layer for all Cytonome agents. It enforces *who can do what* using Directives, Guards, and cryptographic audit trails. v0.1 is production-ready; v0.2 adds sessions, privacy boundaries, and crisis escalation.

## ⚡ What CAP Does in One Table

| Concept | Plain English |
|---------|--------------|
| **Directive** | A formal request from one agent to another ("do this task") |
| **Guard** | The gatekeeper that evaluates every Directive (deny-wins) |
| **GuardDecision** | 7 possible outcomes (allow, deny, modify, escalate...) |
| **RefusalMessage** | 16 reason codes for why something was denied |
| **ExecutionReport** | Proof that a task was completed |
| **DecisionRecord** | Audit trail entry (hash-chained, tamper-evident) |
| **AuthorityChain** | Tracks who authorized what, all the way up |

## 📊 v0.1 Status — What's Done

| Capability | Status |
|-----------|--------|
| Directive lifecycle FSM | ✅ Production-ready |
| Guard with 7 outcomes + 16 refusal codes | ✅ Production-ready |
| Hash-chain audit store | ✅ Production-ready |
| Ed25519 mTLS + JWS + DSSE + in-toto | ✅ Production-ready |
| CAP-Lite (Yar) + CAP-Med (clinical) profiles | ✅ Production-ready |
| HTTP/JSON + gRPC transport bindings | ✅ 28/28 conformance |
| 89 conformance + hardening tests | ✅ All pass |

## 🧠 v0.2 — What's Coming

| New Module | Why It Matters |
|-----------|---------------|
| **Session Protocol** | TCP-like handshake for multi-device agent sessions |
| **Privacy Boundary** | Schema enforcement: raw audio, transcripts, PHI never cross the wire |
| **Persona Authority Binding** | Companion vs advisor vs specialist authority levels |
| **Crisis Escalation** | Pre-authorized safety actions (inject script, page clinician, warm handoff) |
| **A2A Bridge** | Maps CAP Directives into Google A2A Task/Message format |
| **Routing Policy** | Edge vs cloud execution decisions |

> [!warning] 12 Known Gaps in v0.1
> Critical: privacy boundary enforcement, crisis escalation protocol. High: persona binding, A2A integration, consent management, distributed sessions.

## 🔬 Supervision Injection (How Supervisors Guide Agents)

| Type | Frequency | Example |
|------|-----------|---------|
| Soft guidance | Every 3-5 turns | Update conversation direction |
| Hard interruption | Uncommon | Inject priority message |
| Direct audio override | Rare (crisis only) | Safety script injection |

> [!tip] Core Invariant
> No agent can execute anything without a valid, Guard-evaluated Directive. Even crisis escalations generate audit records.

## 📊 Development Phases

| Phase | Scope | Timeline |
|-------|-------|----------|
| v0.1.1 | Type safety cleanup, SQLite audit store, rate limiting | 1-2 weeks |
| v0.2.0 | Sessions + privacy + persona + crisis | 2-4 weeks |
| v0.2.1 | A2A bridge + routing + consent | 2-3 weeks |
| v0.3.0 | Standalone `cytognosis-cap` package, TypeScript + Rust bindings | 2-3 weeks |

## 🛡️ Standards CAP Integrates With

Transport: MCP, A2A, gRPC/HTTP · Policy: OPA/Rego, Cedar · Crypto: DSSE, in-toto, SLSA · Observability: OpenTelemetry, W3C PROV-O · Future: W3C DID, Verifiable Credentials