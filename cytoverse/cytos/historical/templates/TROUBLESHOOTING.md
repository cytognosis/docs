# TROUBLESHOOT: [System/Module/Feature Area]

> **Last verified**: YYYY-MM-DD
> **Owner**: @handle
> **Applies to**: `cytos.[module]` vX.Y+

## Quick Reference

| Symptom | Likely Cause | Fix | Section |
|---------|-------------|-----|---------|
| `429 Rate Limited` | API quota exceeded | Wait or switch API key | [Rate Limiting](#rate-limiting) |
| `ImportError: scholarly` | Package not installed | `pip install scholarly` | [Dependencies](#dependencies) |

## Prerequisites

- Access to: _list required credentials, tools, or permissions_
- Environment: _Python version, OS, required env vars_

---

## Issue: [Descriptive Name]

### Symptoms

_What does the user see? Error messages, UI behavior, log entries._

```
ERROR 2026-05-14 12:00:00 - Module failed: [exact error message]
```

### Diagnosis

1. **Check [first thing]**:
   ```bash
   # Diagnostic command
   ```
   Expected output: ...

2. **Check [second thing]**:
   ```bash
   # Diagnostic command
   ```
   Expected output: ...

### Root Cause

_Why does this happen? Technical explanation._

### Resolution

1. **Step 1**: ...
   ```bash
   # Fix command
   ```

2. **Step 2**: ...

### Prevention

_How to avoid this issue in the future._

---

## Issue: [Next Issue]

_(Repeat the structure above for each known issue)_

---

## Escalation

If the issue persists after following the steps above:

1. Check [related logs/dashboards]: _location_
2. Search [issue tracker]: _URL_
3. Contact: _@owner or #channel_

## Environment-Specific Notes

### Local Development
- ...

### CI/CD
- ...

### Production
- ...
