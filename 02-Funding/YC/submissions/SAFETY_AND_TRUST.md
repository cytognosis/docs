# Safety and Trust

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Defaults

- Yar is local-first by default.
- The default model provider is a deterministic offline stub.
- External model providers require explicit environment configuration.
- Anytype writes require explicit user confirmation.
- Voice Anytype writes use the same plan-before-confirm boundary as web/API writes.
- `/product/status` redacts secrets and does not expose API keys.
- Raw captures are not stored in browser `localStorage`.
- Execution reports track `raw_data_shared: false`.

## CAP-Lite Boundaries

CAP-Lite refuses:

- diagnosis or clinical conclusions,
- treatment or medication recommendations,
- health-risk scoring,
- unsupported certainty about another person's true intent or emotion,
- raw data sharing without consent,
- unconfirmed external writes.

Yar is not a clinical product, diagnostic product, treatment recommender, or mental-health chatbot.

## Examples

**User:** "Diagnose me from my notes"  
**Yar:** Refuses diagnostic conclusions.

**User:** "Tell me what treatment I need"  
**Yar:** Refuses treatment recommendation.

**User:** "Why did this person message me that way?"  
**Yar:** Can help preserve context or draft uncertainty-aware alternatives, but must not claim to know the person's real intent.

## External Writes

Anytype write planning is separate from execution:

```text
plan -> guard -> user confirmation -> execute
```

The hackathon demo stops at a visible dry-run plan unless the environment is explicitly configured and the user confirms execution.

For the mobile voice slice:

```text
voice turn -> local objects -> write plan -> mobile warning -> explicit confirm -> guarded MCP write
```

If Anytype is unavailable, Yar returns a refusal/failure report and keeps the local SQLite objects.
