# OPTIONAL layer 12 — Account-loss checklist (EXAMPLE shape)

Public teaching only. **No quiet-DR / cutover zip** ships in this pack.

## Goal

Recover durable memory from **disk files** after account loss or tool switch.
MCP/skills are adapters — not the memory.

## First minutes

1. Confirm `<your-ssot-root>/` still exists.
2. If damaged, restore from **your** backup into a **new** folder — never unzip over a live vendor core.
3. Open markdown with any editor (no MCP required).
4. Re-point adapters only after files read clean.

## Must-have restore set

| Recover | Path under SSOT |
|---------|-----------------|
| Bot style | `<your-ssot-root>/bots/<bot>/style.md` |
| Journal | `<your-ssot-root>/bots/<bot>/journal.md` |
| Profile | `<your-ssot-root>/bots/<bot>/profile.md` |
| Always-on | `<your-ssot-root>/topest/ALWAYS-ON.md` |
| Rules shards | `<your-ssot-root>/topest/rules/*.md` |
| Events | `<your-ssot-root>/events/*.md` |

## Rebuildable (not the memory)

SQLite / embed indexes under `.v2/` — rebuild from md/jsonl if missing.

## Smoke

- [ ] New folder has `docs/`, `<your-ssot-root>/bots/`, `<your-ssot-root>/topest/`
- [ ] Style + ALWAYS-ON open as UTF-8
- [ ] Live vendor core untouched
- [ ] No secrets pasted into new docs

## Explicit non-goals (CUT)

- Quiet-DR / full vault zip as a public artifact
- School HW / class-notes dumps
- Personal identity / account allowlists
- Writing into live `~/.claude/memory-core` (or any vendor core)

## Temporal note

Keep `valid_from` / `valid_to` / `supersedes` on INF docs so restores stay time-honest.
