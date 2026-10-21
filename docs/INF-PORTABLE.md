---
title: INF-PORTABLE
kind: teaching
temporal: standing
valid_from: 1970-01-01
valid_to: null
supersedes: null
inf_portable: true
---

# INF portable memory (public EXAMPLE)

## Core

- **Files = SSOT.** Durable memory lives in folders you own (markdown + JSONL + rebuildable SQLite indexes).
- MCP / skills / CLI are **adapters** — they wrap files; they are not the memory.
- Readable by any AI stack.

## Open formats

| Artifact | Role |
|----------|------|
| `notes/*.md` | Standing facts / notes |
| `events/YYYY-MM-DD-<slug>.md` | Flat work log (write before claim done) |
| `*.schema.json` | Shared INF shapes |

## Hard rules

1. Point adapters at **your** store root (`<your-ssot-root>/` or env `SSOT_ROOT`).
2. Live vendor memory cores stay **refuse-write** (`LIVE_MEMORY_PATH` stub only).
3. No secrets, personal accounts, school homework, or private machine paths in public trees.
