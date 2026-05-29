# CAP References and Standards Map

This file consolidates the main external standards CAP composes with. URLs were verified during preparation of the v0.1-candidate supervisor package.

## Agent interoperability

- Model Context Protocol overview: https://modelcontextprotocol.io/specification/2025-06-18/basic/index
- MCP tools: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- MCP resources: https://modelcontextprotocol.io/specification/2025-06-18/server/resources
- A2A core specification: https://agent2agent.info/specification/core/
- A2A concepts: https://agent2agent.info/docs/concepts/

## Policy and identity

- Open Policy Agent / Rego policy language: https://www.openpolicyagent.org/docs/policy-language
- SPIFFE concepts and SVID: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- SPIRE concepts: https://spiffe.io/docs/latest/spire-about/spire-concepts/

## Attestation and provenance

- DSSE specification: https://github.com/secure-systems-lab/dsse
- SLSA provenance: https://slsa.dev/spec/v1.2/provenance
- in-toto attestations: https://github.com/in-toto/attestation
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/concepts/semantic-conventions/
- OpenTelemetry trace semantic conventions: https://opentelemetry.io/docs/specs/semconv/general/trace/
- W3C PROV-O: https://www.w3.org/TR/prov-o/

## Health, assessment, and phenotype artifacts

- FHIR QuestionnaireResponse: https://fhir.hl7.org/fhir/questionnaireresponse.html
- GA4GH Phenopackets: https://www.ga4gh.org/product/phenopackets/
- RO-Crate: https://www.researchobject.org/ro-crate/
- ReproSchema: https://www.repronim.org/reproschema/

## CAP delegation rule

CAP should reference these standards rather than duplicate them. CAP Core is justified where it defines Controller-to-Executor authority, Guard decisions, typed refusal, evidence binding, privacy boundaries, interruption, execution reporting, and lifecycle observation. Profile-specific non-diagnostic psychometric assessment semantics belong in CAP-Med or another profile, not in CAP Core.
