# IDE Configuration

Cytocast generates optimized IDE configurations for VS Code, Cursor, Windsurf, Positron, and Antigravity when `preferred_ide` is set. All configurations integrate with the project's Nox sessions, ruff rules, and ty type checker.

## Preferred IDE Selection (F69)

| IDE | Value | Generated Files |
|:---|:---|:---|
| Antigravity | `antigravity` | `.vscode/` (shared format) |
| VS Code | `vscode` | `.vscode/` |
| Cursor | `cursor` | `.vscode/` + `.cursor/rules/` |
| Windsurf | `windsurf` | `.vscode/` + `windsurf-configs/` |
| Positron | `positron` | `.vscode/` |
| None | `none` | No IDE files generated |

```bash
copier copy --trust gh:cytognosis/cytocast my-project \
  --data preferred_ide=vscode
```

## Generated VS Code Files

### settings.json (F65)

```json
{
  "python.defaultInterpreterPath": "./.venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "python.analysis.typeCheckingMode": "basic"
}
```

### extensions.json (F66)

Recommended extensions for the team:

```json
{
  "recommendations": [
    "charliermarsh.ruff",
    "ms-python.python",
    "ms-python.ty",
    "tamasfe.even-better-toml",
    "redhat.vscode-yaml",
    "quarto.quarto"
  ]
}
```

### tasks.json (F67)

Nox sessions mapped to VS Code tasks:

```json
{
  "tasks": [
    {
      "label": "Initialize Project",
      "command": "nox -s init_project",
      "type": "shell",
      "group": "build"
    },
    {
      "label": "Run Tests",
      "command": "nox -s test",
      "type": "shell",
      "group": "test"
    },
    {
      "label": "Format Code",
      "command": "nox -s format",
      "type": "shell"
    },
    {
      "label": "Lint (Sandbox)",
      "command": "nox -s lint_local",
      "type": "shell"
    }
  ]
}
```

### launch.json (F68)

Debug configurations:

```json
{
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}"
    },
    {
      "name": "Python: Tests",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "args": ["-v", "--tb=short"]
    }
  ]
}
```

## AI-Specific Configurations

### Cursor Rules (.cursor/rules/)

When `preferred_ide=cursor`, three rule files are generated:

- `python-healthcare-ai.md`: Healthcare coding standards, PyTorch guidelines
- `testing-standards.md`: Comprehensive testing requirements, markers
- `documentation.md`: Docstring format, API documentation standards

### Windsurf Rules (windsurf-configs/rules/)

When `preferred_ide=windsurf`, four rule files are generated:

- `healthcare-ai-development.md`: Development guidelines
- `testing-standards.md`: Testing philosophy
- `documentation-standards.md`: Documentation requirements
- `security-compliance.md`: Security practices

### .cascade.js (Windsurf)

AI behavior configuration for Windsurf's Cascade assistant:

```javascript
module.exports = {
  projectContext: {
    domain: "healthcare-ai",
    framework: "pytorch",
    testingFramework: "pytest",
  },
  preferences: {
    docstringFormat: "google",
    typeChecking: true,
  },
};
```

## .editorconfig

Cross-IDE editor settings (always generated regardless of `preferred_ide`):

```ini
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 119

[*.{yml,yaml,json}]
indent_size = 2
```

## Ignore Files

| File | IDE | Purpose |
|:---|:---|:---|
| `.cursorignore` | Cursor | Context exclusions |
| `.cursorindexingignore` | Cursor | Indexing exclusions |
| `.codeiumignore` | Windsurf | Indexing exclusions |
| `.windsurfignore` | Windsurf | Context exclusions |

[← Back to Feature Index](index.md)
