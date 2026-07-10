# Cytognosis Interface and Fabric Design

This folder holds the consolidated architectural design for the Cytognosis platform repo topology: which repos exist, what they own, how skills flow, how CI/CD works, and how upstream template changes propagate to downstream packages.

> **Update 2026-05-13**: this design has been **finalized** with the addition of concrete repo organizations, two new master skills, and three Claude Design instruction prompts. The concrete production layouts live in `../../design-system-consolidation-2026-05/`. See "Related work, finalization layer" below.

## Documents

1. [`00_master_architecture.md`](00_master_architecture.md): full design. Naming register, repo inventory, dependency graphs (mermaid), per-repo scopes (`branding`, `cytoskeleton`, `cytocast`, `cytos`, `cytoagent`, `neuros`, `neuro*`), four-phase skill model with manifest schema, Claude Design data flow, CI/CD posture (branches, tags, publishing, signing, provenance, tracker integration), template change propagation, prioritized roadmap, open questions, appendices.
2. [`01_refactor_brief.md`](01_refactor_brief.md): coding-agent-ready brief to refactor `cytoskeleton`, `cytocast`, and `cytoagent`. Pre/post state per repo, execution sequencing, per-repo refactor tasks, full change-propagation mechanism with concrete workflow YAML (the `notify-downstream.yml` upstream + the `template-update.yml` downstream listener + GitHub-topic auto-discovery), CI/CD scaffolds, migration of existing downstream repos, testing checkpoints / definition of done, risks.

## Briefs for Claude Design

[`claude_design_briefs/`](claude_design_briefs/) holds self-contained briefs to share with Claude Design (the external tool that authors the Cytognosis Design System and the four interface templates). One brief for the Design System; one general brief plus four short deltas for the templates. Each brief states mandatory and optional artifacts, folder layout, naming and styling conventions, quality gates, and a definition of done.

For more **focused iteration prompts** (current icons, current profiles, current reorganization), see `../../design-system-consolidation-2026-05/03_claude_design_prompts/`.

## Related work, finalization layer

The architecture in this folder is the **strategic** picture. The finalization layer in `../../design-system-consolidation-2026-05/` carries the **operational** picture: concrete file layouts for branding and cytoskeleton, two new master skills, five revised core skills, and three Claude Design iteration prompts.

| Strategic doc here | Operational counterpart |
|---|---|
| `00_master_architecture.md` (repo inventory) | `02_repo_organization/branding_repo_plan.md`, `cytoskeleton_repo_plan.md` |
| Four-phase skill model in `00_master_architecture.md` | The 7 concrete skills in `04_skills_new/` + `05_skills_revised/` |
| Claude Design data flow in `00_master_architecture.md` | The 3 iteration prompts in `03_claude_design_prompts/` |

Together, this folder + the consolidation folder finalize the design through to the next implementation step.

## What's finalized (post-consolidation)

The following decisions, sketched in the prior version of this doc, are now **settled**:

- **`brand-repo` → `branding`**: the production repo name is `branding`. Cytognosis already maintains it. The `org/branding/` clone has been the working copy. The concrete layout is in `branding_repo_plan.md`.
- **The four interface templates**: confirmed Flutter (phone), React 19 + Vite + Tailwind + shadcn (web), Tauri v2 wrapping the web template (desktop), Manifest V3 + side panel (extension). Stack locked.
- **The seven-skill family**: design-system-master, template-master, branding (deep refs), orchestrator, dev, org, writer. Locked.
- **The four use-case profiles** (Foundation, Clinical, Research, Lab): named, scoped via `[data-profile=...]` CSS overlays, **preliminary** in their specifics. The `prompt_profiles.md` carries the refinement brief.
- **The 48-icon set in 7 categories**: confirmed structure. Canonical line + solid variants per icon. **Preliminary** for ~10 voice/crisis/sensor icons that need to be added or revised. The `prompt_icons.md` carries the refinement brief.
- **The CI/CD posture**: trunk-based with PR-only merges, Conventional Commits, release-please, OIDC publishing, sigstore + SBOM + SLSA + Software Heritage. Locked.
- **Template change propagation**: `notify-downstream.yml` upstream + `template-update.yml` downstream, GitHub-topic auto-discovery, weekly cron, `copier update --conflict skip`. Locked.

## Archived

[`archive/`](archive/) holds the previous design documents (`01_cytoderma_design.md`, `02_cytoplasma_design.md`) that proposed two separate repos. Their scope has been absorbed into `cytoskeleton` and `cytoagent` respectively; the docs remain as historical reference.

## What changed since the archived design

- The proposed `cytoderma` and `cytoplasma` names are retired.
- Interface templates now live inside `cytoskeleton` (alongside its existing env-lock role).
- Agent orchestration, fabric (mDNS / NATS / Tailscale / Iroh), privacy, reliability, and crisis rails now live inside an expanded `cytoagent`, not a separate fabric repo.
- The cytocast to cytoagent dependency is removed. Cytocast owns its own dev skills (language- and framework-specific skills for coding agents).
- The `branding` repo (formerly proposed as `brand-repo`) is light, nox-driven, and backs up the Cytognosis Design System authored in Claude Design while exposing Cytognosis-wide skills.
- The four-phase skill model (brand / template-usage / dev / runtime) replaces the previous single-source skill registry. The brand phase now has two routing-entry skills (design-system-master, template-master) plus the deep-reference home (branding).
- Shared CI/CD machinery lives in `cytocast/templates/_shared/` and is inherited by every cytocast-generated package.
- Template change propagation is wired via `repository_dispatch` + GitHub topics + `copier update` so downstream packages get an auto-PR when cytocast or cytoskeleton releases.

## Where the deliverables will live

| Artifact | Path |
|---|---|
| Cytocast new profiles | `/home/mohammadi/repos/cytognosis/cytocast/profiles/{cytoagent,neuros,neuro-scale,library,tool,interface-template}.yaml` |
| Cytocast shared payload | `/home/mohammadi/repos/cytognosis/cytocast/templates/_shared/` |
| Cytocast dev skills | `/home/mohammadi/repos/cytognosis/cytocast/skills/` |
| Cytoskeleton templates | `/home/mohammadi/repos/cytognosis/cytoskeleton/templates/{app-phone,app-web,app-desktop,app-extension,shared}/` |
| Cytoskeleton template-usage skills | `/home/mohammadi/repos/cytognosis/cytoskeleton/skills/{pick-template,update-template,port-token,env-doctor}/` |
| Cytoagent repo (re-scaffolded) | `/home/mohammadi/repos/cytognosis/cytoagent` |
| Branding repo | `/home/mohammadi/repos/cytognosis/branding` |
| Cytognosis skills (final home, post-migration) | `/home/mohammadi/repos/cytognosis/branding/skills/` (7 skills) |
| Cytognosis skills (current location) | `/home/mohammadi/repos/cytognosis/cytoagent/skills/cytognosis/` (5 skills; 2 new pending) |

## Source materials

- `/home/mohammadi/Documents/Sorted/infra/tools/tools_infra_stack.md` (the 16-layer architecture; §9.4 multi-agent voice flow; §10 component summary).
- `/home/mohammadi/Documents/Sorted/infra/tools/tools_master.md` (full tool catalog).
- `/home/mohammadi/repos/cytognosis/cytocast/` (templating engine).
- `/home/mohammadi/repos/cytognosis/cytoskeleton/` (env locks).
- `/home/mohammadi/repos/cytognosis/cytoagent/` (current scope, to be expanded).
- `/home/mohammadi/repos/cytognosis/org/design/` (Claude Design v10 export of the Design System, ingested 2026-05-13).
- `/home/mohammadi/repos/cytognosis/org/branding/` (current working clone of the branding repo).
- `/home/mohammadi/Documents/Claude_design_chat.md` (Claude Design conversation history).
- The four-tier Cytognosis naming register (see `MEMORY.md` -> Neuroverse repo naming).
- Prior conversations on tiered agent architecture, empathic voice interface, copier-template propagation, and Claude Design as the Design System tool.
