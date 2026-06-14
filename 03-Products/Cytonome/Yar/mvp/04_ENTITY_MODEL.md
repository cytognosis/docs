> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytonome`, `mvp`, `yar`

# 04 — Entity Model: Research KG + Personalization Layer

## Two-layer model

Yar should separate the domain knowledge graph from the personalization/memory graph.

```text
Domain Entity Graph
  Paper, Dataset, Code, Method, Model, Author, Project, Annotation

Personalization / Memory Graph
  UserCapture, UserInterest, UserPriority, UserAnnotation, UserTask, UserContext, Session, Reminder
```

The personalization layer references domain entities instead of duplicating them.

## Current implementation status — 2026-05-17

Implemented domain object types in `YarObjectType`:

- Paper, Author, Dataset, Code, Method, Model, Project, Task, Annotation, Collection, Concept, Note, Reflection, Webpage, Decision, MessageDraft.

Implemented storage:

- SQLite objects, links, captures, execution reports, schema metadata, Anytype write plans, and voice conversation turns.
- Object updates, soft archive, local relation/link creation, local graph reads, and search.
- Voice turns store transcript, assistant message, inferred intent, created object IDs, model report, and CAP report.

Not implemented yet:

- Dedicated personalization graph types such as `UserInterest`, `UserPriority`, retrieval profiles, temporal memory, or relationship memory.
- Rich retrieval endpoint beyond local object search.
- Production migration and conflict-resolution semantics.

## Domain entity graph

### Paper

Represents a scholarly paper, preprint, report, or article.

Key properties:

- title
- abstract
- doi
- url
- venue
- year
- authors
- datasets
- methods
- code
- annotations

Example links:

- Paper `authored_by` Author
- Paper `uses_dataset` Dataset
- Paper `uses_method` Method
- Paper `has_code` Code
- Paper `has_annotation` Annotation

### Author

Represents a researcher, engineer, or contributor.

Key properties:

- name
- orcid
- affiliation
- homepage
- github
- google_scholar

Example links:

- Author `authored` Paper
- Author `maintains` Code
- Author `belongs_to` Organization

### Dataset

Represents a dataset or data source.

Key properties:

- name
- url
- license
- domain
- modality
- access_level
- description

Example links:

- Dataset `used_by` Paper
- Dataset `processed_by` Code
- Dataset `supports_method` Method

### Code

Represents code repositories, packages, notebooks, or scripts.

Key properties:

- name
- repository_url
- language
- license
- package_manager
- documentation_url

Example links:

- Code `implements` Method
- Code `analyzes` Dataset
- Code `supports` Project

### Method

Represents an algorithm, experimental method, computational method, or protocol.

Key properties:

- name
- description
- method_type
- assumptions
- limitations

Example links:

- Method `implemented_by` Code
- Method `used_in` Paper
- Method `applies_to` Dataset

### Model

Represents a machine learning model, architecture, checkpoint, or embedding model.

Key properties:

- name
- architecture
- parameters
- license
- model_url
- training_data
- task

Example links:

- Model `trained_on` Dataset
- Model `implements` Method
- Model `described_by` Paper

### Annotation

Represents a W3C Web Annotation-style comment, highlight, or note.

Key properties:

- body
- target
- selector
- motivation
- creator
- created_at
- source_capture_id

Example links:

- Annotation `targets` Paper/Webpage/Code/Dataset
- Annotation `created_by` User
- Annotation `belongs_to` Collection/Project

### Project

Represents a user or team project.

Key properties:

- name
- goal
- status
- priority
- deadline

Example links:

- Project `contains` Task
- Project `uses` Paper/Dataset/Code/Method
- Project `has_annotation` Annotation

### Task

Represents an action item.

Key properties:

- title
- status
- priority
- due_date
- source_capture_id

Example links:

- Task `belongs_to` Project
- Task `references` Paper/Dataset/Code/Method
- Task `created_from` UserCapture

## Personalization / memory graph

### UserCapture

Raw or semi-raw captured input from the user.

Key properties:

- capture_id
- source_type
- content_hash
- raw_local_path
- raw_local_only
- timestamp
- transcription_confidence

Important rule:

Raw capture text should stay local by default. Objects can store summaries and references, but raw capture should not be synced or written externally without confirmation.

### UserInterest

Represents user-specific interest in a domain entity.

Example:

- User is currently interested in `scvi-tools` for `Yar architecture`.

### UserPriority

Represents current priority weight.

Example:

- `Gemma submission` has high priority this week.

### UserAnnotation

User-specific annotation that references a domain Annotation or directly targets an entity.

### Session

Represents a capture or work session.

Key properties:

- session_id
- started_at
- ended_at
- source_device
- created_objects
- execution_reports

## Example capture-to-graph result

Input:

```text
I found HCA Pilot Dataset and scvi-tools. It looks like scvi-tools might implement the method we need for single-cell modeling. Add it to the Research space.
```

Output objects:

```json
{
  "objects": [
    {
      "type": "Dataset",
      "title": "HCA Pilot Dataset",
      "summary": "Dataset mentioned as relevant to the user's research space."
    },
    {
      "type": "Code",
      "title": "scvi-tools",
      "summary": "Code package mentioned as potentially implementing a relevant single-cell method."
    },
    {
      "type": "Task",
      "title": "Review scvi-tools for single-cell modeling method",
      "summary": "Check whether scvi-tools implements the method needed for the current research project."
    }
  ],
  "links": [
    {
      "source": "scvi-tools",
      "relation": "may_implement",
      "target": "single-cell modeling method",
      "confidence": 0.55
    },
    {
      "source": "Review scvi-tools for single-cell modeling method",
      "relation": "references",
      "target": "scvi-tools",
      "confidence": 0.9
    }
  ]
}
```
