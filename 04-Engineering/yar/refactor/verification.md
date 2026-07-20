> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `refactor`, `verification`

# 07 — Yar + CAP — Verification

## V1 — Yar monorepo structure

| Check | Expected | Command |
|---|---|---|
| mise.toml present | yes | `test -f mise.toml` |
| UV workspace (pyproject.toml at root) | yes | `grep "tool.uv.workspace" pyproject.toml` |
| Python packages: yar-core, -backend, -cli, -tools | 4 | `ls packages \| wc -l` |
| apps/mobile, desktop, extension, web | 4 | `ls apps \| wc -l` |
| pnpm-workspace.yaml | yes | `test -f pnpm-workspace.yaml` |
| external/cytoskeleton submodule | v2.0.0-rc1 | `cd external/cytoskeleton && git describe --tags` |
| external/cyto-skills submodule | v1.0.0-rc1 | `cd external/cyto-skills && git describe --tags` |
| schemas symlinked | yes | `ls -la schemas \| grep "^l"` |

## V2 — Schema migration to LinkML

| Check | Expected | Command |
|---|---|---|
| yar/yar_object.yaml in cytoskeleton | yes | `test -f https://github.com/cytognosis/refactor/cytoskeleton/schemas/domains/yar/yar_object.yaml` |
| yar/capture.yaml | yes | (similar) |
| yar/guard_decision.yaml | yes | (similar) |
| yar/linkml_anytype_mapping.yaml | yes | (similar) |
| Codegen produces Pydantic | yes | `ls https://github.com/cytognosis/refactor/cytoskeleton/schemas/codegen/pydantic/yar/*.py` |

## V3 — CAP TypeScript port

| Check | Expected | Command |
|---|---|---|
| @cytognosis/cap package builds | green | `cd https://github.com/cytognosis/refactor/cyto-skills/cap && pnpm build` |
| Unit tests pass | green | `pnpm test` |
| Conformance suite: 28/28 PASS per binding | green | `pnpm test:conformance` |
| Hardening suite: 33/33 PASS | green | `pnpm test:hardening` |
| Parity vs Python ref impl | green | `pnpm test:parity` |
| HTTP/JSON binding starts | success | `pnpm start:http-json &` ; `curl http://localhost:7100/health` |
| gRPC binding starts | success | `pnpm start:grpc &` ; `grpcurl -plaintext localhost:7101 list` |
| Python ref preserved | yes | `test -d cap/docs/reference-python/cytognosis_cap_v01_production_candidate` |
| SUPERVISOR_REPORT.md preserved | yes | `test -f cap/docs/reference-python/SUPERVISOR_REPORT.md` |

## V4 — Yar backend → CAP server

| Check | Expected | Command |
|---|---|---|
| cap_lite_guard.py uses httpx | yes | `grep httpx packages/yar-backend/src/yar_backend/core/cap_lite_guard.py` |
| CAP_HTTP_URL config defined | yes | `grep CAP_HTTP_URL packages/yar-backend/src/yar_backend/config.py` |
| run_dev.sh starts CAP sidecar + backend | success | `timeout 30 scripts/run_dev.sh & sleep 10; curl http://localhost:8000/health; kill %1` |
| Capture endpoint returns CAP-Lite decision | success | `curl -X POST http://localhost:8000/capture -d '{...}'` returns valid response |

## V5 — Per-branch config

| Check | Expected | Command |
|---|---|---|
| .cytognosis-config.yaml at root | yes | `test -f .cytognosis-config.yaml` |
| app/mobile branch has branch-config | yes | `git show app/mobile:.cytognosis-config-branch.yaml` |
| app/desktop branch has branch-config | yes | (similar) |
| app/extension branch has branch-config | yes | (similar) |
| app/web branch has branch-config | yes | (similar) |
| `cytocast apply-branch-config` works on mobile | success | `git checkout app/mobile && cytocast apply-branch-config --dry-run` |

## V6 — Multi-language build

| Check | Expected | Command |
|---|---|---|
| Python tests pass | green | `uv run pytest packages/` |
| Flutter tests pass | green | `cd apps/mobile && flutter test` |
| TS/JS lint passes (extension, web) | green | `pnpm lint` |
| Rust build (desktop) | green | `cd apps/desktop/src-tauri && cargo build` |

## V7 — End-to-end

```bash
# Full smoke
cd ~/repos/cytognosis/refactor/Yar
scripts/run_dev.sh &
SLEEP_PID=$!
sleep 10

# Capture works
curl -X POST http://localhost:8000/capture -H "Content-Type: application/json" \
  -d '{"content":"Test note","type":"Note"}' | grep -E "(success\|allowed)"

# CAP denial works
curl -X POST http://localhost:8000/capture -H "Content-Type: application/json" \
  -d '{"content":"I have depression","type":"Note","mode":"diagnostic_claim"}' \
  | grep -i "deny\|refus"

kill $SLEEP_PID
```

## V8 — Git hygiene + originals

| Check | Expected | Command |
|---|---|---|
| Yar branch refactor/v2-multi-app-monorepo | yes | `git rev-parse --abbrev-ref HEAD` |
| Yar v0.2.0-rc1-refactor tag | yes (local) | `git tag --list 'v0.2.0-rc1*'` |
| cyto-skills v1.0.0-rc1 tag | yes (local) | `cd .../cyto-skills && git tag --list 'v1.0.0-rc1'` |
| Originals untouched | yes | `cd https://github.com/cytognosis/Yar && git status` |

## Halt criteria

- CAP TS conformance ≠ 28/28 per binding
- CAP TS hardening ≠ 33/33
- CAP TS parity tests fail (TS output differs from Python ref)
- Yar backend can't reach CAP server in smoke test
- Schema migration breaks Pydantic codegen
