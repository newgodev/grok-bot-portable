---
title: TEMPORAL-FRONTMATTER
kind: teaching
temporal: standing
valid_from: 1970-01-01
valid_to: null
supersedes: null
---

# Temporal / supersede frontmatter (INF feel)

| Field | Meaning |
|-------|---------|
| `valid_from` | When this record became current |
| `valid_to` | When it stopped (`null` = still current) |
| `supersedes` | Id or path this replaces |

## Rules

1. Do not delete history — add a new file and point `supersedes` at the old id.
2. Readers / adapters pick the newest valid record for a subject.
3. Same field names in `notes/`, `events/`, and MCP write payloads.

Sample: `examples/ssot-sample/events/1970-01-02-supersede-demo.md`.
