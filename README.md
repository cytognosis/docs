# Cytognosis Documentation

Central documentation repository for the Cytognosis Foundation platform.

## Product Map

```
Cytognosis Platform = "GPS for Health"
├── Cytonome (The Navigator)     → on-device causal AI <5mW
│   ├── Yar                      → workspace/task management
│   ├── Sensors (Cytoscope)      → programmable continuous biosensing
│   └── Cytoplex (formerly CAP)  → authority protocol + agent system
├── Cytoverse (The Map)          → AI health coordinate system
│   └── Cytos                    → scholarly KG, domain schemas, registries
└── Toolchain
    ├── Cytoskeleton             → environment/asset management
    ├── Cytocast                 → project scaffolding (Copier-based)
    ├── Cytoskills               → agent skill system
    └── CytoExplorer             → data exploration UI
```

## Documentation Structure

| Section | Contents |
|---------|----------|
| [`strategy/`](strategy/) | Platform design, data strategy, tool landscape, fundraising |
| [`cytonome/`](cytonome/) | Yar, sensors, Cytoplex spec docs |
| [`cytoverse/`](cytoverse/) | Cytos architecture, schemas, grants |
| [`toolchain/`](toolchain/) | Cytoskeleton, Cytocast, Cytoskills, CytoExplorer |
| [`infrastructure/`](infrastructure/) | GCP, CI/CD, containers, self-hosted, hardware |
| [`schemas/`](schemas/) | LinkML playbook, resource schemas, SSSOM |
| [`org/`](org/) | Naming conventions, compliance, operations |
| [`standards/`](standards/) | Coding standards, documentation standards, DVC |

## Repo-to-Docs Map

| Repo | Docs Section |
|------|-------------|
| Yar | `cytonome/yar/` |
| CAP → cytoplex | `cytonome/cytoplex/` |
| cytos | `cytoverse/cytos/` |
| cytoskeleton | `toolchain/cytoskeleton/` |
| cytocast | `toolchain/cytocast/` |
| cytoskills | `toolchain/cytoskills/` |
| cytoexplorer | `toolchain/cytoexplorer/` |
| infrastructure | `infrastructure/` |
| datasets | `strategy/data-strategy/` |
| branding | `org/branding.md` |
| website | `org/website.md` |
| strix-halo | `infrastructure/hardware/` |

## Conventions

- **Spec/design docs** live here (single source of truth)
- **User-facing docs** (tutorials, API refs, getting-started) stay in their repos
- **ADHD-friendly variants** live in the Obsidian vault (not git-tracked)
- All docs follow [documentation standards](standards/documentation-standards.md)
