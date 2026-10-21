---
name: live-refuse
kind: reference
temporal: standing
valid_from: 1970-01-01
valid_to: null
supersedes: null
description: EXAMPLE — never write a live vendor memory core.
---

# Live refuse (MUST layer 13) — EXAMPLE

## Do

1. Treat `LIVE_MEMORY_PATH` as a **stub name** for documentation only.
2. Point all adapters at **your** store: `SSOT_ROOT` / `<your-ssot-root>/`.
3. Prefer read-only tools against vendor cores; if a path looks live, **stop** and report.
4. Write events under your own SSOT before claiming done.

## Do not

- Write, patch, or “heal” a live vendor memory-core directory.
- Copy private absolute profile paths into public repos.
- Ship real vault exports, quiet-DR zips, or account rosters as “samples”.

## Adapter behaviour (shape)

When a tool is asked to touch a live vendor core → return `path_refuse` (see `mcp/bot-memory/TOOLS-CONTRACT.md`) and leave files unchanged.
