# Person Schema & Intelligence Layer

## Schema: `person.yaml`

[person.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/person.yaml)

**9 classes, 121 attributes, 5 enums (46 values)**

### Key Design Decisions

1. **Person aggregates Position[] and EducationRecord[]** — not inline duplicates
2. **Position** links to Institution KG nodes via `organization_ref` CURIE, includes `seniority_level`, `position_type`, `topic_tags`, and computed `duration_months`
3. **EducationRecord** uses `AcademicDegreeEnum` (ISCED-standardized), includes `isced_level`, `is_terminal_degree`, `topic_tags`, and `specializations`
4. **Person** derives `highest_degree`, `highest_degree_field`, `highest_degree_institution`, and `career_stage` from its children

### Enums

| Enum | Values | Purpose |
|------|--------|---------|
| `AcademicDegreeEnum` | 12 (certificate → habilitation) | ISCED 2011 levels + academic stages |
| `JobSeniorityEnum` | 17 (intern → emeritus) | Academic + industry + founder tracks |
| `PositionTypeEnum` | 7 (academic → consulting) | Organization classification |
| `CareerStageEnum` | 5 (student → distinguished) | Composite career assessment |
| `LanguageProficiencyEnum` | 5 (elementary → native) | LinkedIn-aligned |

---

## Intelligence Module: `person_intelligence.py`

[person_intelligence.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/person_intelligence.py)

### Functions

| Function | Input | Output |
|----------|-------|--------|
| `standardize_degree(raw)` | "PhD", "M.S.", "BSc" | `{degree, isced_level, degree_full_name}` |
| `infer_job_seniority(title)` | "Staff Research Scientist" | `"staff"` |
| `infer_position_type(org)` | "MIT" | `"academic"` |
| `analyze_education(records)` | List of edu dicts | Enriched with ISCED + terminal degree |
| `analyze_positions(positions)` | List of position dicts | Enriched with seniority + type |
| `infer_career_stage(pos, edu, h)` | Positions, education, h-index | CareerStageEnum value |
| `enrich_person_intelligence(person)` | Person dict | Full intelligence analysis |
| `analyze_linkedin_profile(url)` | LinkedIn URL | Schema-mapped Person dict |

### Degree Standardization (verified)

| Raw Input | → Degree | ISCED |
|-----------|----------|-------|
| PhD | doctorate | 8 |
| M.S. | master | 7 |
| BSc (Hons) | bachelor | 6 |
| Doctor of Medicine | professional_doctorate | 7 |
| Postdoc | postdoc | 9 |
| MBA | master | 7 |
| JD | professional_doctorate | 7 |
| Habilitation | habilitation | 9 |
| Course | course | 4 |

### Job Seniority (verified)

| Title | → Seniority |
|-------|-------------|
| Staff Research Scientist | staff |
| Senior Research Scientist | senior |
| Founder and CEO | founder |
| CEO | c_suite |
| Assistant Professor | assistant_professor |
| Director of ML | director |
| VP of Research | vp |
| Postdoctoral Fellow | postdoctoral_researcher |

### End-to-End Test (Shahin Mohammadi)

```
Career stage: distinguished (h=22, 10yr post-PhD, founder-level seniority)
Highest degree: postdoc (CSAIL, MIT)

Education:
     U Tehran          bachelor  ISCED=6   59mo
     Purdue            doctorate ISCED=8   83mo
  ★  MIT               postdoc   ISCED=9   35mo
     CSH               course    ISCED=4   11mo

Positions:
  ●  Research Scientist / Collaborator   mid_level   academic    76mo
     Senior Research Scientist           senior      industry    59mo
     Staff Research Scientist            staff       industry    11mo
  ●  Founder and CEO                     founder     nonprofit    7mo
```

---

## Files Changed

| File | Change |
|------|--------|
| [person.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/person.yaml) | Rewritten: 9 classes, 5 enums, ISCED degrees, seniority, KG refs |
| [person_intelligence.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/person_intelligence.py) | New module: classification engine |
| [publication.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/publication.yaml) | Author class: +google_scholar_id, seniority, person_ref |
| [__init__.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/__init__.py) | Registered person_intelligence |
