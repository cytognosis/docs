> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `mvp`, `implementation`

# Yar Central And Mobile Setup

This guide covers:

- Setting up the Yar backend and `YAR_CENTRAL_*` model route on macOS.
- Setting up the Yar backend and `YAR_CENTRAL_*` model route on Ubuntu.
- Connecting iPhone/iPad to the backend.
- Connecting Android devices to the backend.
- Running the helper scripts.

Note: the correct environment variable prefix is `YAR_CENTRAL_*`. If you wrote
`YAR_CENTERAL`, treat it as a typo and use `YAR_CENTRAL`.

## Repository Layout

```text
/Users/ali/Documents/Yas
├── .env
├── src/yar
├── mobile
├── scripts/setup_yar_central_macos.sh
├── scripts/setup_yar_central_ubuntu.sh
├── scripts/install_ios.sh
└── scripts/install_android.sh
```

## Shared Environment

The backend reads `.env` when you load it into the shell:

```bash
cd /path/to/Yas
set -a
source .env
set +a
```

Minimum central model settings:

```bash
YAR_CENTRAL_MODEL_PROVIDER=ollama_cli
YAR_CENTRAL_MODEL_ENDPOINT=http://127.0.0.1:11434
YAR_CENTRAL_MODEL_NAME=gemma4:e4b
YAR_CENTRAL_MODEL_TIMEOUT_SECONDS=20
YAR_CENTRAL_MODEL_FALLBACK_TO_STUB=true
```

Recommended Anytype MCP settings:

```bash
ANYTYPE_MCP_ENABLED=true
ANYTYPE_MCP_COMMAND=/Users/ali/.npm-global/bin/anytype-mcp
ANYTYPE_MCP_ARGS=
ANYTYPE_API_KEY=your-anytype-api-key
ANYTYPE_VERSION=2025-11-08
ANYTYPE_DEFAULT_SPACE_ID=
ANYTYPE_MCP_TIMEOUT_SECONDS=45
ANYTYPE_MCP_MAX_RETRIES=2
```

On Ubuntu, `ANYTYPE_MCP_COMMAND` is usually:

```bash
ANYTYPE_MCP_COMMAND=anytype-mcp
```

Do not commit `.env`. It is ignored by git.

## macOS Backend Setup

Run:

```bash
cd /Users/ali/Documents/Yas
bash scripts/setup_yar_central_macos.sh
```

The script:

- Checks required CLIs.
- Installs Homebrew packages when Homebrew is available.
- Creates `venv` if missing.
- Installs Yar Python dependencies.
- Installs `@anyproto/anytype-mcp` globally.
- Starts Ollama if needed.
- Pulls `gemma4:e4b`.
- Creates `.env` from `.env.example` if missing.
- Writes safe central model defaults into `.env`.
- Prints the backend run command.

Start the backend:

```bash
cd /Users/ali/Documents/Yas
set -a
source .env
set +a
source venv/bin/activate
uvicorn yar.main:app --host 0.0.0.0 --port 8000 --reload
```

Check it:

```bash
curl http://127.0.0.1:8000/product/status
curl http://127.0.0.1:8000/anytype/tools
```

## Ubuntu Backend Setup

Run:

```bash
cd /path/to/Yas
bash scripts/setup_yar_central_ubuntu.sh
```

The script:

- Installs system packages with `apt`.
- Installs Ollama using the official installer when missing.
- Installs Node.js/npm when missing.
- Creates `venv`.
- Installs Yar Python dependencies.
- Installs `@anyproto/anytype-mcp` globally.
- Pulls `gemma4:e4b`.
- Creates/updates `.env`.

Start the backend:

```bash
cd /path/to/Yas
set -a
source .env
set +a
source venv/bin/activate
uvicorn yar.main:app --host 0.0.0.0 --port 8000 --reload
```

If Ubuntu is running on another machine, find its LAN IP:

```bash
hostname -I | awk '{print $1}'
```

Use that IP as the mobile backend URL, for example:

```text
http://192.168.1.50:8000
```

## iPhone And iPad Setup

Requirements:

- macOS.
- Xcode installed.
- iPhone or iPad trusted by the Mac.
- Flutter installed.
- Backend running with `--host 0.0.0.0`.
- iOS device and Mac on the same network.

Find backend LAN IP on the Mac:

```bash
ipconfig getifaddr en0
```

Find iOS devices:

```bash
flutter devices
xcrun devicectl list devices
```

Run/install on a connected iPhone or iPad:

```bash
cd /Users/ali/Documents/Yas
bash scripts/install_ios.sh 00008030-000448693EB8202E http://172.30.4.21:8000
```

Arguments:

```text
scripts/install_ios.sh <device-id> <backend-url>
```

Example:

```bash
bash scripts/install_ios.sh 00008030-000448693EB8202E http://172.30.4.21:8000
```

What it does:

- Runs `flutter pub get`.
- Builds iOS release with `YAR_BACKEND_URL`.
- Tries `flutter install`.
- Falls back to `xcrun devicectl device install app` when needed.

If iOS says the developer is not trusted, open:

```text
Settings -> General -> VPN & Device Management
```

Trust the developer profile, then open Yar again.

## Android Setup

Requirements:

- Android SDK.
- USB debugging enabled.
- Android device and backend machine on the same network.
- Backend running with `--host 0.0.0.0`.

Find devices:

```bash
flutter devices
adb devices
```

Run/install:

```bash
cd /Users/ali/Documents/Yas
bash scripts/install_android.sh <device-id> http://172.30.4.21:8000
```

If only one Android device is connected, the device id may be omitted:

```bash
bash scripts/install_android.sh "" http://172.30.4.21:8000
```

What it does:

- Runs `flutter pub get`.
- Builds Android release APK with `YAR_BACKEND_URL`.
- Installs `build/app/outputs/flutter-apk/app-release.apk` with `adb install -r`.

## Manual Mobile Build Commands

iOS:

```bash
cd /Users/ali/Documents/Yas/mobile
flutter pub get
flutter build ios --release \
  --dart-define=YAR_BACKEND_URL=http://172.30.4.21:8000
flutter install -d 00008030-000448693EB8202E
```

Android:

```bash
cd /Users/ali/Documents/Yas/mobile
flutter pub get
flutter build apk --release \
  --dart-define=YAR_BACKEND_URL=http://172.30.4.21:8000
adb install -r build/app/outputs/flutter-apk/app-release.apk
```

## Verification Checklist

Backend:

```bash
curl http://127.0.0.1:8000/product/status
curl http://127.0.0.1:8000/anytype/tools
```

Mobile:

1. Open Yar.
2. Confirm the status screen has no `127.0.0.1` connection error.
3. Create a voice capture.
4. Confirm it appears in Library.
5. Create an Anytype write plan.
6. Confirm write.
7. Search Anytype through backend:

```bash
curl -sS -X POST http://127.0.0.1:8000/anytype/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"Save capture to any type","limit":5}'
```

Expected result:

- `results` contains at least one object.
- The object has a title/snippet matching the capture.

## Common Issues

### iOS connects to `127.0.0.1`

`127.0.0.1` on iPhone/iPad means the device itself, not your Mac.

Use the Mac LAN IP:

```bash
ipconfig getifaddr en0
```

Then rebuild with:

```bash
--dart-define=YAR_BACKEND_URL=http://<mac-lan-ip>:8000
```

### Anytype write says it succeeded but object is not visible

Search through the backend first:

```bash
curl -sS -X POST http://127.0.0.1:8000/anytype/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"your title","limit":5}'
```

If backend search finds it, Anytype created it. It may be in another Space or view.

### Anytype MCP timeout

Use an installed binary instead of `npx`:

```bash
npm install -g @anyproto/anytype-mcp
which anytype-mcp
```

Set:

```bash
ANYTYPE_MCP_COMMAND=anytype-mcp
ANYTYPE_MCP_ARGS=
```

On this Mac the command is:

```bash
ANYTYPE_MCP_COMMAND=/Users/ali/.npm-global/bin/anytype-mcp
```

### Central model is slow

First Ollama call can be slow. Keep:

```bash
YAR_CENTRAL_MODEL_FALLBACK_TO_STUB=true
YAR_CENTRAL_MODEL_TIMEOUT_SECONDS=20
```

For stricter no-fallback testing:

```bash
YAR_CENTRAL_MODEL_FALLBACK_TO_STUB=false
YAR_CENTRAL_MODEL_TIMEOUT_SECONDS=180
```

### Android cannot reach backend

Use the backend machine LAN IP, not `127.0.0.1`.

If using an Android emulator, use:

```text
http://10.0.2.2:8000
```

For a physical Android phone, use:

```text
http://<backend-lan-ip>:8000
```
