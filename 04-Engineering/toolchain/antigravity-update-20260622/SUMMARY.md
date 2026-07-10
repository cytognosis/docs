# Antigravity Update + Launcher Consolidation — 2026-06-22

**BLUF:** Both apps are updated to the newer builds you extracted (**Antigravity agent 2.0.6 to 2.1.4**, **Antigravity IDE 2.0.3 to 2.0.4**), with root ownership and the setuid `chrome-sandbox` restored. Your launcher customizations were preserved and consolidated into one aligned set, and a **broken path in your patch script was fixed and re-applied**. Full rollback backups are saved; nothing is lost.

## Done

- [x] Backed up both `/opt` installs and all configs (reversible)
- [x] Updated **Antigravity agent** to 2.1.4 (`/opt/antigravity`)
- [x] Updated **Antigravity IDE** to 2.0.4 (`/opt/antigravity-ide`, commit `def9583a`)
- [x] Restored `root:root` ownership and `chrome-sandbox` setuid `4755` on both
- [x] Consolidated and optimized all 3 launcher `.desktop` files (validated clean)
- [x] Fixed the patch script path and re-applied it (added 10 missing PR-extension proposals)
- [x] Verified versions, JSON validity, symlinks, and sandbox permissions

## Versions

| App | Before | After | Notes |
|-----|--------|-------|-------|
| Antigravity agent | 2.0.6 | **2.1.4** | `productName` Antigravity, minor-version bump |
| Antigravity IDE | 2.0.3 | **2.0.4** | VS Code base 1.107.0, new commit `def9583a` |

## Launcher consolidation and optimizations

| Change | Rationale |
|--------|-----------|
| Kept short names **AG**, **AG IDE**, keywords, MIME types, URL scheme, icons | Your customizations, left intact |
| Kept GPU flag set (ANGLE-GL, gpu-rasterization, zero-copy, OOP raster, ignore-blocklist, SkiaRenderer) | Your tuning, left intact |
| Added `--password-store=gnome-libsecret` to the full-suite launcher | It was missing there; now consistent across all three |
| **Switched `--ozone-platform=wayland` to `--ozone-platform-hint=auto`** | Keeps native Wayland on your current session, but auto-falls back to X11 instead of failing to launch. **Decision flagged: revert to `=wayland` if you want it pinned.** |
| Moved the full-suite combo logic into `/usr/local/bin/antigravity-suite` | The inline `bash -c '... & ...'` failed `desktop-file-validate` (reserved characters). The helper is spec-compliant and easier to maintain. |
| Made Comments version-agnostic ("Antigravity 2.0" to "Antigravity") | Apps auto-update; avoids stale version labels in the menu |
| Agent category set to a single main category `Development;` | Cleared the "more than one main category" validator hint |
| Added a "New Empty Window" right-click action to the IDE launcher | Matches upstream VS Code launcher behavior |

**Final flag set (all launchers):**
`--ozone-platform-hint=auto --enable-features=WaylandWindowDecorations,CanvasOopRasterization,UseSkiaRenderer --use-angle=gl --enable-gpu-rasterization --enable-zero-copy --ignore-gpu-blocklist --password-store=gnome-libsecret`

## Patch script fix

Your `/usr/local/bin/antigravity-patch-product.sh` pointed at `/usr/share/antigravity/resources/app/product.json`, which **does not exist** on this machine, so it would have errored out. Corrected to the real IDE location `/opt/antigravity-ide/resources/app/product.json`. Re-running added the 10 missing GitHub PR-extension API proposals (now 32 total). Only the path was changed; the patch logic is untouched.

**Reminder:** re-run after every IDE update, since updates overwrite `product.json`:
`sudo bash /usr/local/bin/antigravity-patch-product.sh`

## Rollback (if needed)

```bash
sudo rm -rf /opt/antigravity /opt/antigravity-ide
sudo mv /opt/antigravity.bak-2.0.6-20260622     /opt/antigravity
sudo mv /opt/antigravity-ide.bak-2.0.3-20260622 /opt/antigravity-ide
cp ~/Claude/Projects/"Infrastructure and Tooling"/antigravity-update-20260622/config-backup/*.desktop ~/.local/share/applications/
sudo cp ~/Claude/Projects/"Infrastructure and Tooling"/antigravity-update-20260622/config-backup/antigravity-patch-product.sh /usr/local/bin/
update-desktop-database ~/.local/share/applications
```

## Cleanup (optional, when satisfied)

- Delete rollback backups: `sudo rm -rf /opt/antigravity.bak-2.0.6-20260622 /opt/antigravity-ide.bak-2.0.3-20260622`
- Delete the source extracts in `~/Downloads/Antigravity` and `~/Downloads/Antigravity IDE`

## File inventory (this folder)

- `SUMMARY.md` — this document
- `config-backup/` — original 3 `.desktop` files and the original patch script, as they were before today
