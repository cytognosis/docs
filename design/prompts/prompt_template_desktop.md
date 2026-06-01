# Claude Design Prompt: Create the `app-desktop` Template

> Paste this prompt into Claude Design when you want it to produce the **initial scaffold** of the Cytognosis desktop template (`cytoskeleton/templates/app-desktop/`). This template is the basis for native Cytognosis desktop apps (internal hub, supervisor-agent host, local-first asset editor).
> Cytognosis context: full spec in `cytognosis-branding/references/desktop.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_template_desktop.md`
> **Changes**: replaced `cytognosis-template-master` with `cytognosis-branding`, added ND-friendly keyboard shortcuts section, added Focus mode / distraction-free mode, removed em dashes.

---

## Brief

Produce the initial scaffold for the Cytognosis desktop template. Native desktop apps on Windows, macOS, Linux, built with Tauri v2 (Cytognosis chose Tauri over Electron deliberately: keep it light, fast, native-feeling). The headline use case is the internal Cytognosis hub plus the supervisor-agent sidecar host (the laptop-tier Gemma 4 26B-A4B "thinking" model runs here as a Tauri sidecar).

Relationship to `app-web`: the desktop template's frontend code IS the web template's frontend code, wrapped in Tauri. The desktop template only diffs on the native shell.

## 1. Stack (mandatory choices)

- **Shell**: Tauri v2, latest stable.
- **Frontend**: React 19 + Vite + Tailwind + shadcn (same as `app-web`). The desktop template depends on `app-web`'s frontend as a workspace dependency or vendored re-publish.
- **Native language**: Rust, latest stable.
- **Build targets**: Windows (MSI + NSIS), macOS (DMG, universal binary), Linux (AppImage, deb, rpm).
- **Sidecar**: Tauri sidecar API for the supervisor-agent process.

## 2. Mandatory artifacts in the scaffold

### 2.1 Tauri configuration

`src-tauri/tauri.conf.json` that:

- Names the bundle (overridable per downstream product at scaffold).
- Pins window dimensions + minimum size (e.g., 1280x800 minimum).
- Sets the icon set (re-exported from `design-system/iconography/`).
- Configures auto-updater pointing at a Cytognosis update endpoint.
- Lists a precise allowlist of Tauri APIs the frontend can call (least-privilege default; expand explicitly).

### 2.2 Native bridges (one Rust module per bridge, typed commands)

```
src-tauri/src/commands/
├── filesystem.rs               app-data directory + user-selected files via native picker
├── system_tray.rs              Cytognosis tray icon + menu (Open, Voice loop, Pause listening, Focus mode, Settings, Quit)
├── notifications.rs            native OS notifications routed by category (agent, crisis, system)
├── deep_links.rs               cytognosis:// scheme
├── keychain.rs                 OS-native secret storage (Keychain / Credential Manager / GNOME Keyring / KWallet)
├── clipboard.rs                in-app actions only
└── local_ipc.rs                localhost-only channel for supervisor sidecar
```

Each bridge ships with typed command signatures documented in `docs/bridges.md`.

### 2.3 Supervisor-sidecar host

- Sidecar binary: the laptop-tier cytoagent supervisor (built from cytoagent's reference implementations).
- Lifecycle: starts on app launch (lazy, only after user signs in and grants consent to run a local supervisor); exits on app quit.
- Frontend talks to sidecar over local IPC (NATS over localhost OR Unix-socket / named-pipe bridge; pick one in the first revision and document).
- Working directory: inside app-data path; never user's home root.
- "Supervisor status" panel in Settings: process state, recent activity (redacted), kill / restart button.

### 2.4 App menu (platform-idiomatic)

- macOS menubar; Windows / Linux menu bar.
- Standard entries: File, Edit, View, Window, Help.
- Plus a "Cytognosis" entry: About, Settings, Focus Mode, Sign Out, Quit.
- Microcopy from brand voice rules.

### 2.5 ND-friendly keyboard shortcuts (NEW)

The desktop template ships with a comprehensive keyboard shortcut system designed for neurodivergent users:

| Shortcut | Action | Category |
|---|---|---|
| `Cmd/Ctrl + Shift + F` | Toggle Focus mode (distraction-free) | Focus |
| `Cmd/Ctrl + /` | Open/close voice/chat side panel | Agent |
| `Cmd/Ctrl + Shift + Space` | Start voice loop (global, opt-in) | Voice |
| `Cmd/Ctrl + .` | Quick-switch density (compact/comfortable/spacious) | Display |
| `Cmd/Ctrl + Shift + M` | Toggle motion preference | Display |
| `Cmd/Ctrl + Shift + P` | Open profile switcher | Display |
| `Cmd/Ctrl + J` | Jump to recent item (command palette style) | Navigation |
| `Cmd/Ctrl + K` | Open command palette | Navigation |
| `Escape` | Close current overlay, panel, or modal | Navigation |
| `Cmd/Ctrl + Shift + N` | Create new note/entry (context-dependent) | Action |

Design principles for ND-friendly shortcuts:

- Consistent modifier patterns (Cmd/Ctrl + Shift for toggles, Cmd/Ctrl alone for actions).
- No shortcuts that require three modifier keys simultaneously.
- All shortcuts visible in a discoverable cheat sheet (`Cmd/Ctrl + ?`).
- Shortcuts are fully rebindable in Settings > Keyboard.
- High-frequency actions (Focus mode, voice loop) use memorable key combos.
- No shortcut conflicts with common screen reader bindings.

### 2.6 Focus mode / distraction-free mode (NEW)

A dedicated Focus mode that reduces visual noise for users who benefit from minimal distraction:

**When Focus mode activates:**
- Side panels collapse to icon-only state.
- System tray notifications suppress non-crisis categories.
- Nav bar minimizes to a thin strip with logo + clock + Focus indicator.
- All decorative animations stop regardless of motion preference setting.
- Background dims to a solid neutral (no gradients, no glassmorphism).
- Only the primary content area remains fully visible.
- A subtle "Exit Focus" affordance remains accessible (bottom-left corner).

**Focus mode settings (in Settings > Focus):**
- Duration: unlimited, 25 min (pomodoro), 50 min, custom.
- Timer visibility: visible countdown, hidden, or progress ring.
- Break reminder: gentle notification or none.
- Auto-start: on app launch, on schedule, or manual only.
- Allowed interruptions: crisis-only (default), crisis + agent, none.

**Integration with Companion profile:**
- When Companion profile is active, Focus mode uses muted 300-shade pastels instead of the Research profile's cooler tones.
- Focus mode respects the active profile's typography and density settings.
- Streak tracking: Focus sessions can count toward gamification tokens if the user opts in.

### 2.7 Auto-update

- Tauri built-in updater wired to a Cytognosis update endpoint (scaffolded).
- User preference: prompt / silent / never.
- Default: prompt.

### 2.8 Crash reporting

- Sentry-compatible Rust crash reporter (or equivalent that respects privacy defaults).
- Crashes anonymous by default; user can opt out.
- No symbols leaking PII.

### 2.9 Code signing

Release workflow signs binaries per platform:

- macOS: Apple notarization + hardened runtime.
- Windows: Authenticode signature.
- Linux: GPG-signed AppImage; signed deb / rpm.

Workflow scaffolded with placeholders for signing keys (stored as GitHub secrets in downstream repos).

### 2.10 Offline mode

The desktop template is local-first by design (Iroh CRDT via `fabric-client-package` is the state layer). Offline mode is the default, not a separate feature.

- Visible network-status indicator.
- Sync-conflict resolution UI for CRDT documents (rare since Iroh is conflict-free).
- Offline-only build flag for environments unable to reach Cytognosis cloud.

## 3. File layout

```
app-desktop/
├── package.json                frontend; depends on app-web as workspace dependency or vendored copy
├── src-tauri/
│   ├── Cargo.toml
│   ├── tauri.conf.json
│   ├── build.rs
│   ├── icons/                  re-exported from design-system (PNG + ICO + ICNS)
│   ├── src/
│   │   ├── main.rs
│   │   ├── commands/           per §2.2
│   │   ├── sidecar.rs          supervisor sidecar lifecycle
│   │   ├── updater.rs
│   │   ├── menu.rs
│   │   ├── focus_mode.rs       (NEW: Focus mode native integration)
│   │   └── lib.rs
│   └── binaries/               sidecar binary per platform; downloaded at build time
├── src/                        thin frontend shell over app-web
│   ├── main.tsx
│   ├── platform/               desktop-only React components: TrayPresence, GlobalShortcut, FocusMode, etc.
│   └── microcopy.desktop.json  desktop-specific microcopy; merges with app-web's microcopy.json
├── tests/                      Rust unit + Tauri integration
└── docs/
    ├── README.md
    ├── architecture.md
    ├── bridges.md
    ├── code-signing.md
    ├── sidecar.md
    ├── accessibility.md
    ├── keyboard-shortcuts.md   (NEW: documents all shortcuts and rebinding)
    ├── focus-mode.md           (NEW: documents Focus mode behavior and settings)
    └── deployment.md
```

## 4. Brand alignment

- Profile default: Research (`data-profile="research"`).
- Inherits app-web's styling via the workspace dependency; desktop-specific tweaks via `microcopy.desktop.json`.
- Logo mark in tray icon, app icon, About panel.
- Native menu and dialog text follows Cytognosis voice rules.
- Focus mode uses profile-appropriate tokens (Research defaults, Companion overrides when active).

## 5. Quality gates

- Installer bundle: < 25 MB per platform; hard fail > 40 MB.
- Cold start: < 1 s to first frame on a 2020-class laptop.
- Memory: < 200 MB resident with sidecar idle; < 1.5 GB with supervisor model loaded.
- Rust test coverage: 80% on `src-tauri/src/`.
- CI matrix: Windows + macOS Intel + macOS ARM + Linux LTS.
- Focus mode toggle: < 200 ms to enter/exit.
- Keyboard shortcut response: < 50 ms from keypress to action.

## 6. Hard rules

- Rust: `rustfmt` defaults; `clippy --deny warnings`; no `unsafe` without inline justification.
- One module per bridge; bridges export typed commands and own their state.
- All async via `tokio` with explicit timeouts on every external call.
- No global `static mut`. Use `OnceLock` or actor patterns.
- Logging via `tracing`, never `println!` in non-test code.
- Frontend re-uses `app-web` code; no duplication.
- All keyboard shortcuts are rebindable and conflict-free with accessibility tools.

## 7. What to NOT produce

- No Electron. Ever.
- No duplication of `app-web` frontend code; depend on it or re-export it.
- No platform-specific UI that breaks brand parity. Native idioms (menu, dialogs) yes; widget-level theming no.
- No broad filesystem permissions. Scope is least-privilege.
- Do not run the supervisor model inside the Rust process. Sidecar only.
- No Node.js runtime inside the app. Tauri's whole point is no Node.
- No tracking pixels in the About panel or anywhere else.

## 8. Definition of done

1. The app builds and runs on Windows, macOS (Intel + ARM), Linux.
2. The signing pipeline produces signed installers for each platform (placeholders for keys are OK).
3. The auto-updater installs an update in the integration test.
4. The supervisor sidecar starts, accepts a frontend command, returns a result, and shuts down cleanly.
5. The tray, notifications, deep-links, keychain bridges work on each platform's integration test.
6. The native menu uses platform-idiomatic placement.
7. The accessibility scanner reports zero critical or serious issues; menu and keyboard shortcuts are fully accessible.
8. Focus mode activates and deactivates cleanly, suppressing non-crisis notifications.
9. All keyboard shortcuts work and are rebindable via Settings.
10. `docs/README.md` walks a new developer from clone to running the app in under 15 minutes.
11. No em dashes anywhere.

## 9. Deliverables to ship back

1. The complete `app-desktop/` tree.
2. A `MIGRATION.md` describing how the supervisor sidecar binary is built and bundled (from the cytoagent repo's reference implementations).
3. Per-platform installer test artifacts (or clear documentation of how to produce them).
4. The first PR-ready commit message in Conventional Commits format.

## 10. Open questions to surface back to Cytognosis

1. Supervisor sidecar binary: ship in the installer (predictable, works offline, bigger installer) or download on first launch?
2. Global shortcut (e.g., Cmd/Ctrl+Shift+Space for the voice loop): opt-in default?
3. Auto-update default behavior: prompt (scaffold default) vs silent.
4. Crash reporter: Sentry hosted vs self-hosted on Cytognosis infrastructure. Recommendation: self-hosted.
5. Linux distribution: AppImage + deb + rpm (scaffold default) or AppImage only?
6. App-web dependency: workspace dependency (preferred, monorepo-friendly) vs vendored copy (looser coupling, more drift risk)?
7. Focus mode pomodoro timer: should it integrate with external pomodoro apps (e.g., via system notifications) or stay self-contained?
8. Should Focus mode sessions be logged for personal analytics (opt-in), or is that too surveillance-like? Recommendation: opt-in only, with clear data-ownership messaging.
