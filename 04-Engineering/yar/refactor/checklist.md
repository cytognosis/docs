> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `refactor`, `checklist`

# 07 — Yar + CAP — Execution Checklist

Sandbox: `https://github.com/cytognosis/refactor/Yar/`. Also touches `/refactor/cyto-skills/cap/` and `/refactor/cytoskeleton/schemas/domains/yar/`.

## 1. Setup

### 1.1 Branch in Yar
```bash
cd ~/repos/cytognosis/refactor/Yar
git fetch upstream
git checkout -b refactor/v2-multi-app-monorepo upstream/firstVersion
```

### 1.2 Verify prerequisites
```bash
test -d ~/repos/cytognosis/refactor/cyto-skills/cap && echo OK cap dir
test -d ~/repos/cytognosis/refactor/cytoskeleton/schemas/domains && echo OK schemas dir
ls ~/repos/cytognosis/refactor/cytocast/profiles/yar-*.yaml
```

### 1.3 Setup mise + toolchains
```bash
cat > mise.toml << 'EOF'
[tools]
python = "3.13"
node = "22"
rust = "stable"
flutter = "3.22"

[env]
UV_HTTP_TIMEOUT = "300"
EOF

mise install
```

### 1.4 Python UV workspace setup
```bash
uv venv .venv && source .venv/bin/activate
# Workspace pyproject.toml at root + per-package
```

## 2. Reorganize directory structure

### 2.1 Move existing src/yar/ into packages/yar-backend/
```bash
mkdir -p packages/yar-backend/src
git mv src/yar packages/yar-backend/src/yar_backend
# Update imports throughout
bash 03_scripts/update_python_imports.sh packages/yar-backend
```

### 2.2 Create yar-core, yar-cli, yar-tools packages
```bash
mkdir -p packages/{yar-core/src/yar_core,yar-cli/src/yar_cli,yar-tools/src/yar_tools}

# Extract shared types from yar-backend to yar-core
bash 03_scripts/extract_yar_core.sh
```

### 2.3 Move mobile/ to apps/mobile/
```bash
mkdir -p apps
git mv mobile apps/mobile
```

### 2.4 Scaffold apps/desktop, apps/extension, apps/web
```bash
bash 03_scripts/scaffold_apps_desktop_extension_web.sh
```

Creates skeleton for:
- `apps/desktop/src-tauri/` (Cargo workspace)
- `apps/desktop/web/` (React + Vite + Tailwind, copies from cytoskeleton template)
- `apps/extension/` (MV3 + side panel, copies from cytoskeleton template)
- `apps/web/` (React + Vite + Tailwind, copies from cytoskeleton template)

### 2.5 Workspace manifests
```bash
# Python (UV workspace root)
cat > pyproject.toml << 'EOF'
[project]
name = "yar-workspace"
version = "0.2.0-rc1"
requires-python = ">=3.13"

[tool.uv.workspace]
members = ["packages/*"]
EOF

# pnpm workspace for TS/JS
cat > pnpm-workspace.yaml << 'EOF'
packages:
  - apps/extension
  - apps/desktop/web
  - apps/web
EOF

cat > package.json << 'EOF'
{
  "name": "yar-workspace",
  "version": "0.2.0-rc1",
  "private": true,
  "packageManager": "pnpm@9.0.0",
  "workspaces": ["apps/extension", "apps/desktop/web", "apps/web"]
}
EOF
```

### 2.6 Commit
```bash
git add -A
git commit -m "refactor(plan-phase-7-step-2): reorganize into multi-app monorepo (packages/, apps/, workspace manifests)"
```

## 3. Add cytoskeleton + cyto-skills submodules

```bash
mkdir -p external
git submodule add https://github.com/cytognosis/cytoskeleton.git external/cytoskeleton
cd external/cytoskeleton && git checkout v2.0.0-rc1 && cd ../..

git submodule add https://github.com/cytognosis/cyto-skills.git external/cyto-skills
cd external/cyto-skills && git checkout v1.0.0-rc1 && cd ../..

git add .gitmodules external/
git commit -m "feat(plan-phase-7-step-3): add cytoskeleton + cyto-skills submodules"
```

## 4. Migrate schemas to LinkML in cytoskeleton

### 4.1 Convert JSON Schemas to LinkML
```bash
SCRIPTS=~/Documents/Cytognosis/Plans/design/07_yar/03_scripts
python $SCRIPTS/jsonschema_to_linkml.py \
  --source ~/repos/cytognosis/refactor/Yar/schemas/yar_object.schema.json \
  --output ~/repos/cytognosis/refactor/cytoskeleton/schemas/domains/yar/yar_object.yaml \
  --domain yar
# Repeat for capture.schema.json, guard_decision.schema.json, linkml_anytype_mapping.schema.json
```

### 4.2 Validate in cytoskeleton
```bash
cd ~/repos/cytognosis/refactor/cytoskeleton
nox -s schemas_validate
nox -s schemas_codegen
```

### 4.3 Commit in cytoskeleton (separate branch)
```bash
git checkout refactor/v2-content-hub
git add schemas/domains/yar/
git commit -m "feat(plan-phase-7-step-4): add Yar LinkML schemas (migrated from Yar/schemas/)"
```

### 4.4 Replace Yar schemas/ with reference
```bash
cd ~/repos/cytognosis/refactor/Yar
git rm -rf schemas/
ln -s external/cytoskeleton/schemas/domains/yar schemas
git add schemas
git commit -m "refactor(plan-phase-7-step-4): migrate Yar schemas to cytoskeleton (symlink)"
```

## 5. Port CAP to TypeScript

### 5.1 Preserve Python reference
```bash
cd ~/repos/cytognosis/refactor/cyto-skills
mkdir -p cap/docs/reference-python
cp -r "~/Documents/Cytognosis/Infra and design/CAP/cytognosis_cap_v01_production_candidate" \
      cap/docs/reference-python/
cp "~/Documents/Cytognosis/Infra and design/CAP/CAP_v0.1_Production_Candidate_Supervisor_Report.md" \
   cap/docs/reference-python/SUPERVISOR_REPORT.md
cp "~/Documents/Cytognosis/Infra and design/CAP/01_MVP_SCOPE.md" \
   cap/docs/reference-python/MVP_SCOPE.md
cp "~/Documents/Cytognosis/Infra and design/CAP/07_ARCHITECTURE_SCOPE.md" \
   cap/docs/reference-python/ARCHITECTURE_SCOPE.md
# Add Yar-style reference
mkdir -p cap/docs/reference-python/yar-style
cp -r ~/repos/cytognosis/Yar/CAP/* cap/docs/reference-python/yar-style/
```

### 5.2 Scaffold @cytognosis/cap workspace package
```bash
cd ~/repos/cytognosis/refactor/cyto-skills/cap
mkdir -p src/{primitives,guard/profiles,bindings/{grpc,http_json},crypto,audit,policies,opa,otel}
mkdir -p conformance/fixtures hardening/fixtures tests/{unit,integration,parity} examples docs/{integration-patterns,policies}

cat > package.json << 'EOF'
{
  "name": "@cytognosis/cap",
  "version": "1.0.0-rc1",
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "test": "vitest run",
    "test:conformance": "tsx conformance/runner.ts",
    "test:hardening": "tsx hardening/runner.ts",
    "test:parity": "vitest run tests/parity"
  },
  "dependencies": {
    "zod": "^3.23.0",
    "jose": "^5.6.0",
    "@noble/ed25519": "^2.1.0",
    "@noble/hashes": "^1.4.0",
    "fastify": "^4.28.0",
    "@grpc/grpc-js": "^1.10.0",
    "@grpc/proto-loader": "^0.7.10",
    "@opentelemetry/api": "^1.9.0"
  },
  "devDependencies": {
    "typescript": "^5.6.0",
    "vitest": "^2.0.0",
    "tsx": "^4.16.0",
    "@types/node": "^22.0.0"
  }
}
EOF
```

### 5.3 Author primitives
```bash
bash $SCRIPTS/seed_cap_primitives.sh
```

Per `01_plan_prose.md` §6.2. Each primitive as a Zod schema + inferred TS type.

### 5.4 Author Guard engine + profiles
```bash
bash $SCRIPTS/seed_cap_guard.sh
```

`src/guard/engine.ts` — evaluate Directive against policy JSON. `src/guard/profiles/cap_lite.ts` and `cap_med.ts` import from `policies/`.

### 5.5 Author HTTP/JSON binding
```bash
bash $SCRIPTS/seed_cap_http_binding.sh
```

Fastify server with /directive, /health endpoints.

### 5.6 Author gRPC binding
```bash
cp cap/docs/reference-python/cytognosis_cap_v01_production_candidate/cap.proto src/bindings/grpc/cap.proto
npx --yes @bufbuild/protoc-gen-ts cap.proto --output_dir src/bindings/grpc/generated/
bash $SCRIPTS/seed_cap_grpc_binding.sh
```

### 5.7 Author crypto layer
```bash
bash $SCRIPTS/seed_cap_crypto.sh
```

mtls.ts (Ed25519 certs via @noble/ed25519), jws.ts (detached JWS via jose), dsse.ts (custom), in_toto.ts (custom).

### 5.8 Author audit (hash-chain)
```bash
bash $SCRIPTS/seed_cap_audit.sh
```

### 5.9 Author OPA adapter (optional)
```bash
bash $SCRIPTS/seed_cap_opa_adapter.sh
```

Subprocess call to `opa eval` OR @openpolicyagent/opa-wasm (in-process WASM). Subprocess default.

### 5.10 Author conformance suite
```bash
bash $SCRIPTS/seed_cap_conformance.sh
```

Port each of 28 Python checks. Each check is a vitest test that reads fixtures from `conformance/fixtures/` (same fixtures as Python ref), runs through TS impl, asserts expected output.

### 5.11 Author hardening suite
```bash
bash $SCRIPTS/seed_cap_hardening.sh
```

33 checks. Same pattern.

### 5.12 Parity tests
```bash
bash $SCRIPTS/seed_cap_parity_tests.sh
```

Tests that run BOTH Python ref impl (via subprocess) AND TS impl on same inputs, assert outputs match.

### 5.13 Validate
```bash
cd cap
pnpm install
pnpm build
pnpm test
pnpm test:conformance
pnpm test:hardening
pnpm test:parity
```
Verification: all green.

### 5.14 Commit (in cyto-skills repo)
```bash
cd ~/repos/cytognosis/refactor/cyto-skills
git add cap/
git commit -m "feat(plan-phase-7-step-5): TypeScript port of CAP v0.1 production-candidate (conformance + hardening parity with Python ref)"
```

## 6. Wire Yar backend to CAP TS server

### 6.1 Add httpx-based CAP client to yar-backend
```bash
cd ~/repos/cytognosis/refactor/Yar/packages/yar-backend
# Update src/yar_backend/core/cap_lite_guard.py:
cp $SCRIPTS/cap_lite_guard_v2.py src/yar_backend/core/cap_lite_guard.py
```

### 6.2 Add CAP_HTTP_URL config
```bash
# In yar-backend's settings
cat >> src/yar_backend/config.py << 'EOF'

CAP_HTTP_URL = os.environ.get("CAP_HTTP_URL", "http://localhost:7100")
EOF
```

### 6.3 Add CAP sidecar to dev scripts
```bash
cat > scripts/run_dev.sh << 'EOF'
#!/usr/bin/env bash
# Run CAP sidecar in background
(cd ../../cyto-skills/cap && pnpm --silent start:http-json) &
CAP_PID=$!
trap "kill $CAP_PID" EXIT

# Run Yar backend
cd packages/yar-backend
uv run uvicorn yar_backend.main:app --reload
EOF
chmod +x scripts/run_dev.sh
```

### 6.4 Tests with CAP TS server running
```bash
# In CI: start CAP server as service
# Locally: scripts/run_dev.sh
```

### 6.5 Commit
```bash
git add packages/yar-backend/src/yar_backend/core/cap_lite_guard.py scripts/run_dev.sh
git commit -m "feat(plan-phase-7-step-6): Yar backend uses CAP TS server (cytognosis-cap @ HTTP/JSON binding)"
```

## 7. Per-branch config

### 7.1 Root config
```bash
bash $SCRIPTS/seed_cytognosis_config_yar_root.sh
```

`.cytognosis-config.yaml` at Yar root: profile=yar-backend, env=agentic, schemas=core+yar.

### 7.2 Per-app branch configs
```bash
# Create app/mobile branch with appropriate config
git checkout -b app/mobile
bash $SCRIPTS/seed_cytognosis_config_branch_mobile.sh
git add .cytognosis-config-branch.yaml
git commit -m "feat: yar-mobile branch config (Flutter, app-phone env)"
git checkout refactor/v2-multi-app-monorepo

git checkout -b app/desktop
bash $SCRIPTS/seed_cytognosis_config_branch_desktop.sh
git add .cytognosis-config-branch.yaml
git commit -m "feat: yar-desktop branch config (Tauri, app-desktop env)"
git checkout refactor/v2-multi-app-monorepo

# Similarly for app/extension, app/web
```

## 8. Cytocast adoption

### 8.1 Generate .cytognosis-config + .copier-answers
Already done in step 7.1 + 8.x.

### 8.2 Run cytocast adopt
```bash
cd ~/repos/cytognosis/refactor/Yar
uvx --from ~/repos/cytognosis/refactor/cytocast copier copy \
  ~/repos/cytognosis/refactor/cytocast . \
  --data profile=yar-backend --data project_name=Yar \
  --skip-if-exists --vcs-ref v2.0.0-rc1
```

### 8.3 Inherit _shared/ workflows
```bash
bash $SCRIPTS/update_workflows_to_shared.sh
```

## 9. Final validation

### 9.1 Tests across all packages
```bash
# Python packages
cd ~/repos/cytognosis/refactor/Yar
uv run pytest packages/

# CAP (in cyto-skills)
cd ~/repos/cytognosis/refactor/cyto-skills/cap
pnpm test:conformance && pnpm test:hardening && pnpm test:parity

# Flutter (mobile)
cd ~/repos/cytognosis/refactor/Yar/apps/mobile
flutter test
```

### 9.2 End-to-end smoke
```bash
cd ~/repos/cytognosis/refactor/Yar
bash scripts/run_dev.sh &
sleep 5
curl -X POST http://localhost:8000/capture \
  -H "Content-Type: application/json" \
  -d '{"content":"test note","type":"Note"}'
# Should succeed with CAP-allowed
```

### 9.3 Originals untouched
```bash
cd ~/repos/cytognosis/Yar && git status
cd ~/repos/cytognosis/cytoagent && git status   # NOTE: this dir; cyto-skills is the rename target
```

### 9.4 Tag
```bash
cd ~/repos/cytognosis/refactor/Yar
git tag v0.2.0-rc1-refactor -m "Phase 7: multi-app monorepo + CAP TS server"
cd ~/repos/cytognosis/refactor/cyto-skills
git tag v1.0.0-rc1 -m "Phase 7: CAP TypeScript port"
```

### 9.5 Summary
```bash
bash $SCRIPTS/final_state_summary.sh > scratch/phase-7-summary.txt
```

## Halt criteria

- CAP TS conformance fails any check (parity broken)
- CAP TS hardening fails any check
- Yar backend can't reach CAP server (config issue)
- Schema migration fails (LinkML codegen errors)
- Multi-app workspace build fails on any one stack (Python uv, Node pnpm, Flutter, Rust cargo)
