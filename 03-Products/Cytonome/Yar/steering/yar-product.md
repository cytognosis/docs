> **Status**: Active
> **Date**: 2026-05-29
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `steering`, `agents`

---
inclusion: always
version: 1.0.0
category: product
description: Product vision and success metrics for Yar
last_updated: 2026-05-29
---

# Product Steering: Yar

## Vision

Yar is a cognitive companion built by neurodivergent minds, for everyone. It captures personal knowledge through voice-first interaction, organizes it as a structured knowledge graph, and retrieves it contextually through natural conversation. Yar transforms fleeting thoughts into persistent, searchable, interconnected knowledge.

## User Personas

| Persona | Role | Primary Goal | Pain Point |
|---------|------|-------------|------------|
| Neurodivergent professional | Knowledge worker with ADHD/ASD | Capture ideas at the speed of thought without losing context | Traditional note-taking tools require too much executive function overhead |
| Researcher | Scientist managing complex reading and experimental notes | Link observations, papers, and hypotheses into a navigable graph | Information silos across tools; no semantic connections between notes |
| Clinician | Healthcare provider tracking people across encounters | Voice-capture clinical reasoning and retrieve relevant history instantly | EHR friction; critical context lost between visits |
| Developer | Engineer maintaining complex codebases and decisions | Record architectural decisions and retrieve rationale later | Decision context evaporates; ADRs are never written |

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Capture latency | < 2s from voice trigger to confirmed storage | P95 latency on voice capture endpoint |
| Knowledge retrieval relevance | > 0.85 MRR on semantic search | Mean Reciprocal Rank against test queries |
| Voice recognition accuracy | > 95% WER on conversational speech | Whisper transcription error rate on test corpus |
| Daily active captures | > 10 captures per active user per day | Backend analytics on capture events |
| Graph connectivity | > 3 edges per node average | Neo4j graph density metrics |

## Roadmap Priorities (Current Quarter)

1. Stabilize voice capture pipeline (Whisper STT, Kokoro TTS on-device, affect detection; ElevenLabs remains design-time voice-design tooling only)
2. Ship Anytype integration for bi-directional knowledge sync
3. Implement CAP-governed agent communication for supervisor/interviewer flows
4. Harden semantic search with contextual retrieval using embedding-based similarity

## Non-Goals

- Yar is not a general-purpose chatbot or LLM wrapper
- No cloud-only dependency; on-device inference (Gemma) is the target architecture
- No social features or multi-user collaboration (single-person knowledge graph)
- No real-time transcription of third-party conversations without consent
