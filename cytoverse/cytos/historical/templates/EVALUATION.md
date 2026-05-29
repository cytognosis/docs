# EVAL: [Technology/Library/Service Name]

> **Status**: In Progress | Complete | Superseded
> **Date**: YYYY-MM-DD
> **Author**: @handle
> **Decision**: Adopted | Rejected | Deferred
> **Related ADR**: [ADR-NNN] (created after evaluation)

## Objective

_What are we evaluating and why? What capability gap or problem prompted this evaluation?_

## Requirements

| # | Requirement | Priority | Weight |
|---|-----------|----------|--------|
| R1 | ... | Must-have | 3 |
| R2 | ... | Should-have | 2 |
| R3 | ... | Nice-to-have | 1 |

## Candidates Evaluated

| Candidate | Type | License | Cost | Maturity |
|-----------|------|---------|------|----------|
| [Name] | Library/API/SaaS | MIT/Apache/Proprietary | Free/$X/mo | Stable/Beta/Alpha |

## Evaluation Matrix

| Criterion | Weight | Candidate A | Candidate B | Candidate C |
|-----------|--------|-------------|-------------|-------------|
| Reliability | 3 | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Cost | 2 | ★★★★★ | ★★★★★ | ★★☆☆☆ |
| Coverage | 3 | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Maintenance | 2 | ★★★★☆ | ★☆☆☆☆ | ★★★★★ |
| Legal Risk | 3 | ★★★★★ | ★★☆☆☆ | ★★★★★ |
| **Total** | | **XX** | **XX** | **XX** |

## Hands-on Testing

### Candidate A: [Name]

**Setup**:
```bash
# Installation / configuration steps
```

**Test Results**:
| Test Case | Input | Expected | Actual | Pass |
|-----------|-------|----------|--------|------|
| ... | ... | ... | ... | ✅/❌ |

**Findings**: _What worked, what didn't, surprises._

### Candidate B: [Name]

_(Same structure as above)_

## What Worked

1. **[Finding]**: Description and evidence.

## What Did Not Work

1. **[Finding]**: Description, root cause, and how we addressed it.

## Lessons Learned

1. **[Lesson]**: Actionable insight for future evaluations.

## Recommendation

_State the recommended candidate with clear justification referencing the evaluation matrix._

**Recommended**: [Candidate Name]
**Rationale**: ...

## Implementation Impact

| Aspect | Impact |
|--------|--------|
| New dependencies | ... |
| Config changes | ... |
| API changes | ... |
| Cost projection | ... |

## References

- [Links to official docs, benchmark reports, relevant issues]
