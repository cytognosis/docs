> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytonome`, `mvp`, `yar`

# 06 — WADM Annotation Integration Plan

## Goal

Yar should reuse the W3C Web Annotation Data Model pattern for browser/page/paper annotations instead of inventing a new annotation model.

The user already has relevant Cytognosis code paths:

- LinkML version of W3C WADM:
  - `schemas/domains/annotation.yaml`
- Python annotation implementation:
  - `src/cytos/scholarly/annotation.py`
- AnnotationStore implementation
- Reference projects:
  - Hypothesis
  - Memex

## Why WADM matters for Yar

Yar needs to capture not only raw notes, but also the relationship between a note and what it refers to.

Examples:

- A highlight on a paper PDF.
- A note on a GitHub repository.
- A comment on a webpage.
- A question about a dataset.
- A decision linked to a method.

WADM gives a standard structure:

```text
Annotation = Body + Target + Motivation + Selector + Provenance
```

## Current implementation status — 2026-05-17

Implemented:

- WADM-inspired Pydantic request/response models.
- `/annotations/wadm` preview endpoint.
- `/annotations/capture` endpoint that creates Annotation/Webpage-oriented captures through the coordinator.
- Deterministic routing support for webpage annotation captures.
- Local graph links such as `Annotation annotates Webpage`.

Still future work:

- Real browser extension capture.
- PDF anchoring and DOM-range selectors.
- Hypothesis/Memex import/export.
- Importing the full Cytognosis WADM LinkML schema as the runtime validator.

## Minimum annotation object

```json
{
  "type": "Annotation",
  "body": {
    "type": "TextualBody",
    "value": "This method may be useful for our Anytype schema mapping."
  },
  "target": {
    "type": "Webpage",
    "source": "https://example.com/page",
    "selector": {
      "type": "TextQuoteSelector",
      "exact": "LinkML schema mapping"
    }
  },
  "motivation": "commenting",
  "creator": "user",
  "created_at": "2026-05-16T18:00:00Z",
  "source_capture_id": "uuid"
}
```

## Mapping WADM to Yar entities

| WADM concept | Yar concept | Anytype concept |
|---|---|---|
| Annotation | Annotation object | Type: Annotation |
| Body | Note/Comment content | Text property or linked Note |
| Target | Paper/Webpage/Code/Dataset | Relation to target object |
| Motivation | Annotation purpose | Select property |
| Selector | Highlight location | JSON/text property |
| Creator | User/Author | Person/User relation |
| Created | Timestamp | Date property |

## Supported motivations for MVP

Use a small controlled vocabulary:

- commenting
- highlighting
- questioning
- tagging
- linking
- summarizing
- todo

## Browser capture flow

```text
User highlights text on webpage/paper
        ↓
Browser capture payload sent to coordinator
        ↓
Gemma classifies capture as Annotation + target entity
        ↓
CAP-Lite checks write permissions
        ↓
Yar creates Annotation object
        ↓
Yar links Annotation → target Paper/Webpage/Code/Dataset
```

## Example: paper annotation

Input:

```text
Highlight from paper: "Graph neural networks can model cell-cell interactions." Note: this may connect to our phenotype modeling stack.
```

Output:

```json
{
  "objects": [
    {
      "type": "Annotation",
      "title": "GNNs for cell-cell interaction modeling",
      "body": "This may connect to our phenotype modeling stack.",
      "motivation": "commenting",
      "target_type": "Paper",
      "selector": {
        "type": "TextQuoteSelector",
        "exact": "Graph neural networks can model cell-cell interactions."
      }
    },
    {
      "type": "Task",
      "title": "Review GNN method for phenotype modeling stack",
      "summary": "Check whether the highlighted paper's GNN method is relevant to phenotype modeling."
    }
  ],
  "links": [
    {
      "source": "GNNs for cell-cell interaction modeling",
      "relation": "targets",
      "target": "Paper"
    },
    {
      "source": "Review GNN method for phenotype modeling stack",
      "relation": "created_from",
      "target": "GNNs for cell-cell interaction modeling"
    }
  ]
}
```

## Integration phases

### Phase 1 — Internal compatible schema

- Define Annotation class locally.
- Match WADM names where possible.
- Store selectors as JSON.

### Phase 2 — Import Cytognosis LinkML schema

- Load `annotation.yaml`.
- Map WADM classes to Yar schema registry.
- Validate annotation objects against LinkML-derived schema.

### Phase 3 — Browser extension compatibility

- Accept Hypothesis-like annotation export.
- Accept Memex-like webpage capture export.
- Normalize into Yar Annotation objects.

## MVP acceptance criteria

- Yar can create one Annotation object from a webpage or paper capture.
- Annotation has body, target, motivation, selector, timestamp.
- Annotation links to a Paper/Webpage object.
- Annotation can be retrieved by target object.
