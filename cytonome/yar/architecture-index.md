# YAR Architecture (v1.0)

YAR (Your AI Representative) is a cognitive companion.

## System Overview
- **Privacy-First & On-Device**: Built for local execution using the Cytonome paradigm.
- **Component Map**:
  - API Layer (16 routers)
  - Core Logic (coordinator, model_router, voice, affect, TTS)
  - Storage Layer (SQLite + Graph representations)
  - CAP (Cognitive Architecture Protocol for safety and guardrails)
- **Universal Sensor Architecture**: Defined in `sensor_architecture.md`.
- **Sensor Roadmap**:
  - v0.1 Voice -> v0.2 Text -> v0.3 Facial -> v0.4 Multimodal -> v1.0 Wearables

## Dependencies
- FastAPI, Pydantic, httpx, MCP.
