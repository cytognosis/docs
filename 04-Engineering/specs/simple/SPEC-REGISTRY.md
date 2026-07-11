# Spec Registry, in Plain Words

**Reading time: 1 minute.**

> **If you only read one thing:** every planned change now has a one-page "spec" that says what must be true when it's done. This table is the master list of all of them, across every repo.

**Spec 101**: a spec is a short contract for one change: what it must do (requirements), and how we prove it works (checks). A different session verifies the checks than the one that built it, like a second pair of eyes.

## What's on the list right now

| Area | What it covers | State |
|---|---|---|
| Website (2 specs) | Bring back the old site's features (forms, CV upload, candidates, events) on the new stack; make the site use the official design template | Approved, ready to build |
| Branding (3 specs) | Recover the brand assets the rewrite dropped; reconnect Claude Design so design changes flow automatically; publish the website template package | Approved, ready to build |
| Memory system (3 specs) | Sync tasks with the new mission board; smarter memory (lessons learned, fixes linked to failures); make the memory system understand specs | Drafts |

## The rules, shortly

Specs live next to the code they govern. Changing a finished spec means adding a dated change note, never silently editing. The mission board shows one card per spec with just its name and status; the real content stays in git.

## Your one next step

Nothing here; the main chat summary has the single action for this round.
