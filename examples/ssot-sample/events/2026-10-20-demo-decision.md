---
id: evt-demo-decision-001
ts: 2026-10-20T12:00:00+08:00
kind: decision
summary: EXAMPLE — chose flat events/YYYY-MM-DD-slug.md (write-before-claim-done)
tags: [demo, events, layer-4]
refs: [../README.md, ../../../schemas/memory-event.schema.json]
valid_from: 2026-10-20T12:00:00+08:00
valid_to: null
supersedes: evt-demo-001
---

# Layer 4 SAMPLE — event log shape

**Flat folder.** Filename = `YYYY-MM-DD-<slug>.md` (never nest by month).

1. Write this file **before** you claim done.
2. Keep personal vault events out of the public pack — this file is fixture only.
3. Optional JSON twin: same stem `.json` with the frontmatter fields.

Machines may ignore the body; humans may read it.
