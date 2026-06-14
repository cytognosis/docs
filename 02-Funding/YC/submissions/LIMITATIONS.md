# Limitations

## Intentionally Stubbed or Limited

- Stub mode is still the default for deterministic tests and demos.
- Real central Gemma routing is available through Ollama/local model server configuration, but not required for tests.
- On-device Gemma E2B is implemented in the Flutter app but requires a capable physical device and model download.
- Anytype real writes are guarded and environment-dependent; they require explicit confirmation and discovered MCP write tooling.
- Browser extension capture is represented by manual WADM payloads and a bookmarklet draft.

## Production Hardening Needed

- Authentication and local network access controls.
- Structured audit logs and retention controls.
- More complete schema migration behavior.
- Better conflict handling for graph edits.
- Stronger import/export and backup flows.

## Privacy and Security Considerations

- Raw captures are local by default, but production builds need stronger redaction, encryption, and device trust boundaries.
- Any external model provider must be opt-in and clearly labeled.
- Anytype write execution depends on local MCP configuration and should remain explicitly confirmed.

## Model Quality Limitations

- The stub is deterministic and useful for testing, but it does not measure real extraction quality.
- The local `gemma4:e4b` Ollama smoke test proves runtime connectivity and JSON parsing, not extraction quality.
- Future Gemma evaluation should test JSON validity, object accuracy, relation precision, and refusal reliability.

## Mobile Limitations

- Mobile API tests and analyzer pass, but on-device E2B inference still needs physical-device validation.
- The app is a vertical slice, not production app-store packaging.
- Platform STT availability varies by device, OS, locale, and permissions; manual transcript editing remains the reliable fallback.

## Anytype MCP Uncertainties

- Tool names and write capabilities may differ across Anytype MCP versions.
- Type/property synchronization may be partial or unsupported.
- Confirmed writes must be tested against a disposable Anytype space before production use.

## WADM Coverage Limitations

- Current support covers webpage-style text selections.
- PDF anchoring, DOM ranges, Hypothesis import, and Memex import are roadmap items.

## CAP-Lite Limitations Compared to Full CAP

- CAP-Lite is a small local guard, not a full policy protocol.
- It blocks known high-risk operations but does not prove comprehensive safety.
- It should be expanded with formal policies, evidence records, and conformance tests before sensitive deployments.
