# 3-Minute Demo Script

## 0:00-0:20 Problem

"Neurodivergent attention does not fit rigid task apps. A thought while walking, a task that needs breaking down, a mood that needs naming before it can be planned around: most tools force it into a single rigid shape too early, and punish you when the shape does not fit."

## 0:20-0:40 Product

"Yar is a local-first cognitive companion. It structures messy capture into a private, typed personal knowledge graph, keeps raw data on-device by default, and plans in two tracks: the ideal version and a lighter baseline that still counts."

## 0:40-1:10 Capture and Task

Open the Capture screen. Type or record a stray thought.

"This capture stays private by default, no forced sorting. Turning it into a task calls the local op-log directly: a `task.created` operation, deterministically replayed into the Plan projection, no server required."

Show the task landing on the Plan screen in a lane, with a lighter baseline version alongside the ideal one.

## 1:10-1:35 Focus and Mood

Open Focus; start a session.

"This is a body-doubling companion, not a countdown you can fail. Stopping early is a supported, non-punished outcome."

Open Mood & Energy; check in.

"Fourteen days of texture, not a score. No color-only information, and no clinical vocabulary."

## 1:35-2:00 Thought Map

Open the Map. Place a thought; link two thoughts together.

"The graph is not just extracted text. The person can review, repair, and link objects locally before anything ever leaves the machine."

## 2:00-2:25 Assistant, Sync, and Convergence

Open the Assistant. Ask a grounded question about something just captured.

"The assistant only ever talks about what the person themselves captured. It retrieves from their own graph and shows its sources."

Open Settings, connect the optional personal server, and trigger a sync.

"Sync exchanges operations, never database files. After a sync round, the device and server compare a deterministic projection hash; if they match, everyone sees 'Projections match.'"

## 2:25-2:50 Safety Refusal

Return to the Assistant. Submit "Diagnose me, do I have ADHD."

"This is CAP-Lite: a deterministic gate that blocks diagnosis, treatment, and crisis language before any model call, in English and Persian, and points to real human support instead. Yar is not a clinical or diagnostic product."

## 2:50-3:00 Closing

"Yar is fully free, with no subscription, indefinitely. The submission proves a safe local loop: capture, structure, plan, focus, check in, retrieve, and sync, all behind a hard safety boundary."

## Note on Mobile

There is no mobile demo in this submission. The shipped build is Tauri v2 desktop only; mobile is on the roadmap, with the long-term cross-platform framework still under evaluation.
