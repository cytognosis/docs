---
spec_id: SPEC-data-sovereignty
version: "0.1"
status: active
domain: privacy-security
owner: Shahin Mohammadi
created: 2026-07-06
last_updated: 2026-07-06
depends_on: [SPEC-storage-engine]
implements: []
---

# SPEC: Yar Data Sovereignty

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**BLUF:** Yar's data sovereignty architecture ensures the person owns, controls, and can export all their data at all times. The device is the primary trust boundary; the server is an optional, zero-knowledge relay. This spec defines the concrete privacy boundaries, encryption requirements, and consent gates that enforce data sovereignty from the op-log layer up through the UI.

---

## 1. Principles (Decided)

| Principle | Description |
|---|---|
| **P1: Device-first** | All data originates on the person's device. The device op-log is the single source of truth. No data leaves the device without explicit consent. |
| **P2: Server is optional** | The Yar server is an optional relay for multi-device sync. Disconnecting loses zero functionality. The person can delete their server-side data independently. |
| **P3: Zero-knowledge relay** | When sync is enabled, the server should hold encrypted op payloads (ciphertext). The server reducer operates on plaintext only during the transition period; E2E encryption is a launch gate. |
| **P4: Export as a right** | The person can export all their data (op-log + blobs) at any time in open formats (JSON, Markdown). Export is presented before any destructive action. |
| **P5: No dark patterns** | Privacy defaults are maximally protective. Consent is informed, granular, and revocable. No gamification pressure, no data collection without explicit opt-in. |

---

## 2. Trust Boundaries

```text
┌─────────────────────────────────────────────────────────────┐
│ DEVICE TRUST BOUNDARY                                       │
│                                                             │
│  ┌──────────────┐  ┌───────────────────┐  ┌──────────────┐ │
│  │ Op-Log       │  │ Privacy Settings  │  │ AI Runtimes  │ │
│  │ (plaintext   │  │ (privacy.json     │  │ (device-tier │ │
│  │  at rest)    │  │  mirrors op-log)  │  │  only by     │ │
│  │              │  │                   │  │  default)    │ │
│  └──────┬───────┘  └────────┬──────────┘  └──────────────┘ │
│         │                   │                               │
│         │ CONSENT GATE: "Connect to your Yar server"        │
│         │ (explicit user action required)                    │
│         │                                                   │
├─────────▼───────────────────────────────────────────────────┤
│ NETWORK BOUNDARY (optional)                                 │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Sync Protocol: push/pull operations                  │   │
│  │  - Future: E2E encrypted payloads                    │   │
│  │  - Current: plaintext (transition period)            │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ SERVER TRUST BOUNDARY (person's own server)                 │
│                                                             │
│  ┌──────────────┐  ┌───────────────────┐  ┌──────────────┐ │
│  │ Op Replica   │  │ Graph Projection  │  │ Blob Store   │ │
│  │ (server_seq  │  │ (FalkorDB         │  │ (SHA256      │ │
│  │  cursor)     │  │  rebuild from     │  │  content-    │ │
│  │              │  │  ops)             │  │  addressed)  │ │
│  └──────────────┘  └───────────────────┘  └──────────────┘ │
│                                                             │
│  Auth: device-token based (personal relay; only the         │
│  person's own devices are principals)                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Privacy Settings (Implemented)

| Setting | Default | Consent Model |
|---|---|---|
| `local_only` | **true** | Server sync requires explicit opt-in via Settings |
| `on_device_ai_only` | **true** | Cloud AI requires explicit opt-in |
| `voice_mood_awareness` | **false** | Experimental; opt-in; labeled "never a diagnosis" |
| `share_diagnostics` | **false** | Anonymous crash telemetry; opt-in |

Settings are mirrored to `privacy.json` for Rust-side boot-time enforcement without replaying the op-log. The op-log copy (`settings.updated`) is canonical; the JSON mirror is best-effort.

---

## 4. Encryption Requirements

### 4.1 At-Rest Encryption

| Component | Current | Target | Implementation |
|---|---|---|---|
| Op-log (device) | Plaintext JSONL | SQLCipher-encrypted SQLite | Migrate JSONL → rusqlite + SQLCipher |
| Privacy settings | Plaintext JSON | OS keychain or encrypted file | Use Tauri `tauri-plugin-store` with OS keychain |
| Blobs (audio) | Plaintext files | Encrypted at rest | SQLCipher or filesystem encryption |
| Server op replica | Plaintext Django models | E2E encrypted payloads | NaCl/libsodium box encryption |

### 4.2 In-Transit Encryption

| Path | Current | Target |
|---|---|---|
| Device ↔ Server | HTTPS (assumed) | HTTPS + E2E encrypted payloads |
| Device ↔ Device (P2P) | Not implemented | E2E via version-vector + encrypted DAG |

### 4.3 Key Management

| Concern | Design |
|---|---|
| **Key generation** | Device-local; NaCl keypair generated on first launch |
| **Key storage** | OS keychain (macOS Keychain, Windows DPAPI, Linux Secret Service) |
| **Key rotation** | Re-encrypt op-log and re-push to server; invalidate old device token |
| **Key recovery** | Export recovery key to user (paper/password manager); no server-side recovery |
| **Multi-device** | Key exchange via QR code or out-of-band secret during device pairing |

---

## 5. Consent Gates

| Gate | Trigger | UI |
|---|---|---|
| **Server connection** | User taps "Connect to your Yar server" | Confirmation dialog explaining what syncs and what stays local |
| **Server disconnection** | User taps "Disconnect" | Gentle confirmation: what pauses, what keeps working |
| **Cloud AI** | User toggles "On-device AI only" off | Warning that queries will leave the device |
| **Voice mood** | User toggles "Voice mood awareness" on | "This is experimental, never a diagnosis" + consent text |
| **Diagnostics** | User toggles "Share diagnostics" on | "Anonymous crash reports only" + opt-out anytime |
| **Data deletion** | User taps "Delete local data" | Export-first prompt → irreversibility warning → double-confirm |
| **Export** | User taps "Export my data" | Format chooser (JSON/Markdown) → download/clipboard |

---

## 6. HIPAA Pathway

| Requirement | Status | Gap |
|---|---|---|
| Encryption at rest | ⚠️ Planned | SQLCipher migration required |
| Encryption in transit | ⚠️ Partial | E2E encryption of sync payloads required |
| Access controls | ✅ | Device-token auth; single-user relay |
| Audit trail | ✅ | Op-log is a complete, append-only audit trail |
| Data retention policy | ⚠️ Planned | Automatic server-side purge after device confirmation |
| BAA-eligible hosting | ⚠️ Planned | GCP with BAA; or self-hosted relay |
| Minimum necessary | ✅ | Server holds only ops pushed by the person |

---

## 7. Data Portability

| Format | Content | Use Case |
|---|---|---|
| **JSON export** | Full op-log with metadata | Machine-readable backup; import to another Yar instance |
| **Markdown export** | Human-readable operation summary | Personal review; paper backup |
| **Op-log JSONL** | Raw append-only log | Developer access; migration |
| **Blob store** | Content-addressed files (SHA256) | Audio recordings; attachments |

---

## 8. Open Decisions

| # | Decision | Current Leaning | Blocker |
|---|---|---|---|
| **DS-1** | E2E encryption library | NaCl/libsodium via `crypto_box` | None; well-supported in Rust and JS |
| **DS-2** | Key exchange for multi-device | QR code pairing | UX design needed |
| **DS-3** | Server-side data purge policy | Purge after all devices confirm receipt | Sync protocol extension |
| **DS-4** | HIPAA BAA provider | GCP with BAA or self-hosted | Business decision |

---

## 9. Cross-References

- `SPEC-storage-engine.md` — Storage engine choice and encryption requirements
- `STORAGE-ENGINE-RECOMMENDATION.md` — SQLCipher recommendation
- `YAR-CLIENT-EVAL.md` — Privacy boundary assessment of the current codebase
- `yar-code-20260705-2354/ARCHITECTURE.md` — Trust boundaries
- `yar-code-20260705-2354/src-tauri/src/commands.rs` — PrivacyPrefs implementation
- `cytoplex/spec/privacy-boundary-spec.md` — Shared PAP decision
