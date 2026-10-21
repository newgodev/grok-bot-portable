# Promote / useful-gate story (MUST layer 11) — EXAMPLE

Teaching story only. Paths below are placeholders. **Do not** treat this as a live gate stamp.

## Flow

```text
_draft / stage  →  useful-gate checks  →  PASS or FAIL
                         │
            FAIL → fix on stage → re-gate
            PASS → promote into public tree (user GO) → optional undo note
```

## Roles (EXAMPLE)

| Role | Does |
|------|------|
| Author | Stages scrubbed EXAMPLE content under a **stage** copy (never push from a private vault root). |
| Tester | Runs useful-gate; tester ≠ fixer. Reports PASS/FAIL + evidence path. |
| Gate | Confirms walls stay EXAMPLE, cue/recovery packages stay **out**, leak scan clean. |
| Ship | Push only after Gate PASS **and** user GO. |

## Useful-gate checklist (EXAMPLE shape)

1. Demo / smoke command exits 0 (if the repo ships a demo).
2. No personal / school / family / account bodies.
3. Paths are `<your-ssot-root>/` or `LIVE_MEMORY_PATH` stubs — not private absolute disks.
4. No quiet-DR / cutover zip artifacts in the tree.
5. Third-party cue/recovery packages **absent** from this portable monorepo.
6. Walls / rules marked EXAMPLE only.
7. Evidence written as an event md **before** claiming done.

## Promote vs undo

- **Promote:** copy or merge the staged, gated tree into the public branch the user named.
- **Undo:** keep the prior commit; write an event noting what rolled back and why.
- Never silently rewrite the thing under test during the gate.

## Live refuse

Useful-gate never authorizes writing a live vendor memory core. See `examples/topest/live-refuse.md`.

## Related MUST

1 INF · 2 ALWAYS-ON · 4 SAMPLE events · 6 skill · 7 MCP contract · 13 live-refuse · 15 temporal · 17 Liquid FAST/DEEP
