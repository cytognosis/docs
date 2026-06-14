# Dependency Strategy and Storage

As standard across Cytognosis, reproducibility is a core tenet of our deployment infrastructure. Rather than relying on transient network pings to PyPI or mapping ambiguous version tags, `cytoskeleton` strictly resolves and anchors all dependency trees downstream.

## 1. Local Commit Artifacts (`locked/`)

The core repository stores exact cryptographic manifestations of all tested compatibility permutations internally.

- **Storage Method**: Standard Git LFS / Tree commits.
- **Path**: `locked/environments/*.uv.lock` and `locked/matrix/*.uv.lock`.
- **Primary Use**: Zero-configuration bootstrapping for `strix-halo` and `cookiecutter` projects checking out submodules. Running `uv pip sync modules/cytoskeleton/locked/environments/ml-linux-cuda.uv.lock` safely installs exactly the environment audited by our `generate_all_locks.py` suite.
- **Integrity**: `LOCK_MANIFEST.json` contains SHA-256 validation sums to detect accidental/manual mutations.

## 2. Remote Distribution (prefix.dev)

For non-developer installations (i.e., deployed nodes, end-users leveraging Pixi or Conda natively without cloning git repos), environments are additionally synced and managed seamlessly through `prefix.dev`.

### 2.1 Why Prefix.dev?

- **Binary Caching**: PyTorch and ROCm/CUDA binaries are immense (>2GB). Recompiling or redownloading them over raw PyPI fetches is inefficient. Prefix.dev channels host compiled binaries and strictly resolved conda environments that can be pulled simultaneously in sub-seconds using `pixi` or `micromamba`.
- **Ecosystem Integration**: Prefix natively understands `.uv.lock` mappings and integrates them with `conda-forge`/`pytorch` registries to synthesize unified Conda distributions safely circumventing `pip`'s native shortcomings handling native C++ bindings.

### 2.2 Channel Structure

Cytognosis maintains the following explicit channels on `prefix.dev`:

- `https://prefix.dev/channels/cytognosis-stack`: The bleeding-edge development channel automatically updated by our Github Actions (`refresh-locks.yml`).
- `https://prefix.dev/channels/cytognosis-stable`: Manually promoted lock matrices bound to explicit version tags (e.g., `v1.2.0`).

### 2.3 Consumption via Pixi

Downstream users seeking to establish a specific `cytoskeleton` generated environment can achieve it trivially using `pixi.toml`:

```toml
[project]
name = "my_analysis_project"
channels = ["conda-forge", "cytognosis-stack"]
platforms = ["linux-64", "osx-arm64"]

[dependencies]
cytognosis-ml = "==0.1.0" # This implicitly fetches the entire pre-locked dependency array
```

## 3. Ephemeral Workflow & CI Maintenance

The overall strategic architecture depends exclusively on Git actions ensuring these artifacts are never stale.

1. **Monday 6:00 AM Cron**: `refresh-locks.yml` rebuilds all 80 permutations, identifying any newly patched packages that unpinned constraints shifted slightly for.
2. **Review**: Dependencies are diffed structurally via `dep_diff.py` and presented as a Pull Request.
3. **Merge**: Once merged into `main`, the `.github/workflows/tag-locks.yml` mechanism detects `locked/` changes and dynamically increments semantic tags (e.g., publishing `v1.3.1`).
4. **Broadcast**: This tag syncs implicitly down to the `cytoskeleton` submodule in `cookiecutter` instances globally.
