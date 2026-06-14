# 02 — Architecture Scope

## High-level architecture

```text
Phone Capture App / Mobile Web Shell
        ↓
Capture API + Voice API
        ↓
Desktop / Local Coordinator
        ↓
Edge Gemma E2B VoiceIntent + Central Gemma E4B Structured Router
        ↓
CAP-Lite Guard
        ↓
Schema Registry + LinkML Mapper
        ↓
Graph Adapter Interface
        ↓
Anytype MCP Adapter
        ↓
Anytype Object Graph

Fallback path:
Graph Adapter Interface → Local SQLite/JSON Graph Store
```

## Implemented Product Milestone 1 overlay

The implemented voice path uses:

```text
Flutter mobile app
  → platform STT or editable transcript
  → optional on-device Gemma E2B VoiceIntent JSON
  → POST /voice/turn
  → CAP-Lite pre-check and CAPMobileDirective
  → central Coordinator
  → stub/http_json/Ollama object router
  → SQLite graph + voice conversation history
  → POST /voice/plan-anytype-write
  → explicit mobile confirmation
  → POST /voice/confirm-anytype-write
  → guarded Anytype MCP write attempt
```

Central model configuration:

```env
YAR_CENTRAL_MODEL_PROVIDER=ollama
YAR_CENTRAL_MODEL_ENDPOINT=http://127.0.0.1:11434
YAR_CENTRAL_MODEL_NAME=gemma4:e4b
YAR_CENTRAL_MODEL_FALLBACK_TO_STUB=true
```

## Component 1 — Phone Capture App

### Purpose

Provide a low-friction capture surface.

### MVP responsibilities

- Accept voice transcript or text.
- Attach source metadata.
- Send capture payload to local coordinator.
- Show whether capture was processed successfully.

### Payload

```json
{
  "capture_id": "uuid",
  "source": "phone",
  "capture_type": "voice_transcript",
  "content": "I found a dataset for HCA and maybe scvi-tools code implements the method we need.",
  "created_at": "2026-05-16T18:00:00Z",
  "raw_local_only": true
}
```

## Component 2 — Capture API

### Purpose

Receive capture payloads from phone and forward them to the coordinator pipeline.

### Endpoints

```text
POST /capture
GET /product/status
POST /voice/turn
POST /voice/plan-anytype-write
POST /voice/confirm-anytype-write
GET /voice/conversations/{conversation_id}
```

## Component 3 — Desktop / Local Coordinator

### Purpose

Main orchestration service.

### Responsibilities

- Validate capture payload.
- Call Gemma 4 structured router.
- Validate structured output.
- Apply CAP-Lite guard.
- Invoke schema registry.
- Write/read/update/link objects through graph adapter.
- Return an execution report.

## Component 4 — Gemma 4 Structured Router

### Purpose

Turn unstructured capture into typed object proposals.

### Input

Raw capture text plus optional current graph context.

### Output

Strict JSON object proposal.

```json
{
  "objects": [
    {
      "type": "Dataset",
      "title": "HCA Pilot Dataset",
      "summary": "A dataset mentioned as relevant to current research work.",
      "confidence": 0.78,
      "properties": {
        "domain": "single-cell biology",
        "source_phrase": "HCA Pilot Dataset"
      }
    },
    {
      "type": "Code",
      "title": "scvi-tools",
      "summary": "A code package mentioned as potentially implementing a relevant method.",
      "confidence": 0.84,
      "properties": {
        "language": null,
        "repository_url": null
      }
    }
  ],
  "links": [
    {
      "source_title": "scvi-tools",
      "source_type": "Code",
      "relation": "may_implement",
      "target_title": "Method",
      "target_type": "Method",
      "confidence": 0.52
    }
  ],
  "needs_user_confirmation": true
}
```

## Component 5 — CAP-Lite Guard

### Purpose

Constrain what the coordinator is allowed to do.

### Guard checks

- Is this action allowed?
- Is the target store local or external?
- Does the action require confirmation?
- Is the model output valid against schema?
- Does the output include unsupported/unsafe claims?
- Does the operation attempt to expose raw capture data?

### Guard output

```json
{
  "guard_decision": "allow_with_constraints",
  "constraints": [
    "user_confirmation_required_before_anytype_write",
    "raw_capture_must_not_be_written_as_public_property",
    "low_confidence_links_marked_as_suggestions"
  ],
  "allowed_operations": [
    "create_object",
    "create_link",
    "read_object"
  ],
  "blocked_operations": [],
  "reason": "Structured research capture is within allowed local graph operations."
}
```

## Component 6 — Schema Registry + LinkML Mapper

### Purpose

Maintain the canonical entity schemas and map them to Anytype.

### Responsibilities

- Load LinkML YAML schemas.
- Extract classes, slots, enums, relationships.
- Convert to internal schema registry.
- Map to Anytype Type/Property definitions.
- Validate object proposals before execution.

## Component 7 — Graph Adapter Interface

### Purpose

Provide one interface for both Anytype and fallback storage.

### Required methods

```python
class GraphAdapter:
    def list_spaces(self): ...
    def list_types(self): ...
    def ensure_type(self, schema): ...
    def create_object(self, object_payload): ...
    def read_object(self, object_id): ...
    def search_objects(self, query, type=None): ...
    def update_object(self, object_id, patch): ...
    def create_link(self, source_id, relation, target_id): ...
    def export_graph(self): ...
```

## Component 8 — Anytype MCP Adapter

### Purpose

Translate graph adapter calls into Anytype MCP tool calls.

### MVP behavior

- Discover available spaces/types/properties.
- Create or map target object type.
- Create object in selected Anytype space.
- Update object properties.
- Search/read object.

### Important constraint

Do not make the MVP depend entirely on Anytype MCP. Keep the fallback graph store fully working.

## Component 9 — Local Fallback Graph Store

### Purpose

Reliable demo execution when Anytype MCP is unavailable.

### Storage options

- SQLite database with tables: `objects`, `links`, `captures`, `execution_reports`.
- JSON files for simplest possible implementation.

### Requirement

The fallback must use the same schema and adapter interface as Anytype.
