# Claude Design Brief: Desktop Template (Delta)

> Read `templates_general_brief.md` first. Read `template_web_delta.md` second; the desktop template wraps the web template via Tauri v2.
> Output destination: `cytoskeleton/templates/app-desktop/`.

## 1. What this template is for

The desktop template is the base for Cytognosis products that run natively on Windows, macOS, and Linux. Planned products derived from this template:

- The internal Cytognosis hub for researchers and clinicians (asset management, longitudinal review, KG exploration).
- The local-first asset-hub editor with offline support via Iroh CRDT.
- The **supervisor-agent host**: the desktop app is where the laptop-tier Gemma 4 26B-A4B supervisor runs as a Tauri sidecar. This is one of the headline reasons the desktop template exists.

Cytognosis chose Tauri over Electron deliberately. The desktop template must stay light (target under 25 MB shipped), fast (sub-second cold start), and native-feeling.

## 2. Framework and platform

- **Shell**: Tauri v2 (latest stable).
- **Frontend**: same React 19 + Vite + Tailwind + shadcn stack as the web template. The desktop template literally depends on `templates/app-web/` for the frontend; it adds Rust for native bridges.
- **Native language**: Rust (latest stable).
- **Build targets**: Windows (MSI + NSIS), macOS (DMG, universal binary including Apple Silicon), Linux (AppImage, deb, rpm).
- **Sidecar**: Tauri sidecar API for the supervisor-agent process (the local LLM lives as a sidecar binary, not inside Rust).

## 3. Relationship to the web template

The desktop template's frontend code is the web template's frontend code. Concretely:

- `templates/app-desktop/src-tauri/` contains the Rust + Tauri config.
- `templates/app-desktop/src/` is either a thin shim that imports from `templates/app-web/src/` (when bundled together) or a re-publish of `app-web` as a workspace dependency (when bundled separately).
- The desktop template overrides only the pieces that are genuinely different: app menus, native dialogs, deep-link handling, tray, notifications, keychain, supervisor sidecar.

When the web template changes, the desktop template inherits it automatically. The desktop template only diffs on the native shell.

## 4. Mandatory artifacts (desktop-specific)

In addition to the cross-template mandatory artifacts and to the web-template-delta mandatory artifacts that flow through.

### 4.1 Tauri configuration

**Mandatory.** A working `tauri.conf.json` (or `Tauri.toml`) that:

- Names the bundle (overridable per downstream product at scaffold time).
- Pins window dimensions and minimum size.
- Sets the icon set (re-exported from `design-system/iconography/`).
- Configures app updaters via Tauri's built-in updater pointing at a release endpoint the template scaffolds.
- Lists the precise allowlist of Tauri APIs the frontend can call (default to least-privilege; expand explicitly).

### 4.2 Native bridges

**Mandatory.** Each bridge is a small Rust module exposing typed commands to the frontend:

- `filesystem`: read and write inside an app-data directory plus user-selected files (via native picker). No general filesystem access.
- `system_tray`: Cytognosis tray icon with a small menu (Open, Voice loop, Pause listening, Settings, Quit).
- `notifications`: native OS notifications routed by category (agent message, crisis, system).
- `deep_links`: register a `cytognosis://` scheme for product-specific deep links.
- `keychain`: OS-native secret storage (macOS Keychain, Windows Credential Manager, GNOME Keyring / KWallet on Linux).
- `clipboard`: scoped to in-app actions only.
- `local_ipc`: localhost-only channel for talking to the supervisor sidecar.

Each bridge is documented in `docs/bridges.md` with the typed command signatures.

### 4.3 Supervisor-sidecar host

**Mandatory.** The desktop template launches and manages the supervisor agent as a Tauri sidecar process. Concretely:

- The sidecar binary is the laptop-tier Cytoagent supervisor (built from cytoagent's reference implementations).
- The sidecar starts on app launch (lazy: only when the user has signed in and granted the consent to run a local supervisor) and exits on app quit.
- The frontend talks to the sidecar over a local IPC channel (NATS via localhost or a Unix-socket / named-pipe bridge; pick one in the first revision and document).
- The sidecar's working directory is inside the app-data path; never in the user's home root.
- A small "Supervisor status" panel in settings shows the sidecar process state, recent activity (redacted appropriately), and a kill / restart button.

### 4.4 App menu

**Mandatory.** A platform-idiomatic app menu (macOS menubar; Windows / Linux menu bar) with the standard entries (File, Edit, View, Window, Help) plus a "Cytognosis" entry containing About, Settings, Sign Out, Quit. Microcopy from the brand voice.

### 4.5 Auto-update

**Mandatory.** Tauri's built-in updater wired to a Cytognosis update endpoint (scaffolded). The updater respects the user's preference: prompt on update, auto-update silently, or never auto-update (in settings). Default: prompt.

### 4.6 Crash reporting

**Mandatory.** Sentry-compatible Rust crash reporter (or an equivalent that respects privacy defaults). Crashes are reported anonymously by default and the user can opt out. No symbols leaking PII.

### 4.7 Code signing

**Mandatory.** The release workflow signs the binaries for each platform:

- macOS: Apple notarization + hardened runtime.
- Windows: Authenticode signature.
- Linux: GPG-signed AppImage; deb / rpm signed with the Cytognosis package signing key.

The template scaffolds the workflow with placeholders for the signing keys (stored as GitHub secrets in downstream repos).

### 4.8 Offline mode

**Mandatory.** The desktop template is local-first by design (Iroh CRDT is the state layer). Offline mode is not a separate feature; it is the default behavior. The template ships:

- A clearly visible network-status indicator.
- Sync-conflict resolution UI for CRDT documents (when present; rare since Iroh is conflict-free by design).
- An offline-only build flag for environments that cannot reach Cytognosis cloud at all.

## 5. Optional artifacts (desktop-specific)

- **Touch Bar / dock icon menu** (macOS only; low priority).
- **Jump List** (Windows; low priority).
- **Quick Look extension** (macOS, for `.cytognosis` asset files; future).
- **Global shortcut** (e.g., `Cmd/Ctrl + Shift + Space` to summon the voice loop from anywhere on the OS). Recommended but consent-gated.

## 6. Folder layout (desktop-specific)

```
app-desktop/
├── package.json                       (frontend; depends on app-web as workspace dep)
├── src-tauri/
│   ├── Cargo.toml
│   ├── tauri.conf.json
│   ├── build.rs
│   ├── icons/                         (re-exported from design-system; PNG + ICO + ICNS)
│   ├── src/
│   │   ├── main.rs
│   │   ├── commands/                  (typed Tauri commands; one file per bridge)
│   │   │   ├── filesystem.rs
│   │   │   ├── system_tray.rs
│   │   │   ├── notifications.rs
│   │   │   ├── deep_links.rs
│   │   │   ├── keychain.rs
│   │   │   ├── clipboard.rs
│   │   │   └── local_ipc.rs
│   │   ├── sidecar.rs                 (supervisor sidecar lifecycle)
│   │   ├── updater.rs
│   │   ├── menu.rs
│   │   └── lib.rs
│   └── binaries/                      (sidecar binary, per-platform; downloaded at build time)
├── src/                               (thin frontend shell over app-web)
│   ├── main.tsx
│   ├── platform/                      (desktop-only React components: TrayPresence, GlobalShortcut, etc.)
│   └── microcopy.desktop.json         (desktop-specific microcopy; merges with app-web's)
├── tests/                             (Rust unit tests + Tauri integration)
└── docs/
    ├── bridges.md
    ├── code-signing.md
    ├── sidecar.md
    └── (cross-template required docs)
```

## 7. Code style (desktop-specific)

- Rust: `rustfmt` defaults; `clippy --deny warnings`; no `unsafe` without an inline justification.
- One module per bridge; bridges export typed commands and own their state.
- All async via `tokio`; explicit timeouts on every external call.
- No global `static mut` state; use `OnceLock` or actor patterns.
- Logging via `tracing`, never `println!` in non-test code.

## 8. Quality gates (desktop-specific)

- **Bundle size**: under 25 MB for the installer on each platform; hard fail above 40 MB.
- **Cold start**: under 1 s to first frame on a 2020-class laptop (i5-class CPU, SSD).
- **Memory**: under 200 MB resident with the sidecar idle; under 1.5 GB with the supervisor model loaded.
- **Rust unit tests**: 80% coverage on `src-tauri/src/`.
- **Cross-platform CI**: matrix build on Windows, macOS (Intel + ARM), Linux (Ubuntu LTS).

## 9. Definition of done (desktop-specific)

In addition to the cross-template definition of done:

1. The app builds and runs on Windows, macOS (both architectures), and Linux.
2. The signing pipeline produces signed installers for each platform.
3. The auto-updater installs an update in the integration test.
4. The supervisor sidecar starts, accepts a frontend command, returns a result, and shuts down cleanly.
5. The tray, notifications, deep links, and keychain bridges work on each platform's integration test.
6. The native menu uses platform-idiomatic placement.
7. The accessibility scanner reports zero issues; the menu and keyboard shortcuts are fully accessible.

## 10. What to NOT produce (desktop-specific)

- Do not use Electron, ever, for this template.
- Do not duplicate the web template's frontend code; depend on it or re-export it.
- Do not write platform-specific UI that breaks brand parity. Native idioms (menu, dialogs) yes; widget-level theming no.
- Do not request broad filesystem permissions. Scope is least-privilege.
- Do not run the supervisor model inside the Rust process. Sidecar only.
- Do not introduce a Node.js runtime inside the app for any reason. Tauri's whole point is no Node.

## 11. Open questions for the Cytognosis team

1. The supervisor sidecar binary: built and shipped per platform by the desktop release workflow, or downloaded on first launch? Recommendation: ship in the installer (predictable; works offline); downside is installer size grows with the model.
2. The global shortcut for the voice loop: opt-in default, or off until enabled? Recommendation: opt-in (privacy-respecting).
3. Auto-update default behavior: prompt vs silent. Recommendation: prompt.
4. Crash reporter: Sentry-hosted vs self-hosted (Sentry on-prem) vs none. Recommendation: self-hosted on Cytognosis infrastructure for sovereignty.
5. Linux distribution: AppImage + deb + rpm, or just AppImage? Recommendation: all three; AppImage as the universal fallback.
