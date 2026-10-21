---
name: bot-memory
description: >-
  Local files=SSOT recall (fast/deep) without touching a live vendor
  memory core. Use for recall_current, recall_bot, recall_chatvault_day
  (alias recall_chatvault), recall_shared against your own store root.
---
# Skill: bot-memory (portable Memory v2 shape)

Use when an agent needs **local memory** from a folder you own.
MCP/skill are **adapters**. The files are the memory.

## Hard rules — LOCAL / portable / vendor-lock free

- **SSOT = local open files** (md / JSONL / rebuildable SQLite). Not a cloud product DB.
- **Any AI stack** must read the same tree after copy/export.
- Account loss must not lose: notes, styles, day traces, event log.
- Scale: store may exceed **100GB**; prefer appendable files over proprietary blobs.
- Point tools at `<your-ssot-root>/`. Never write into someone else’s live vendor memory (`LIVE_MEMORY_PATH` stub).

## When to use

| Situation | Tool / mode |
|-----------|-------------|
| Known path already analysed | `recall_current(query, mode="fast")` |
| Unknown path / avoid repeating mistakes | `recall_current(query, mode="deep")` |
| New chat forgot a bot’s voice/style/journal | `recall_bot(bot="<bot-id>", query=...)` |
| Recover a day transcript pointer | `recall_chatvault_day(day="YYYY-MM-DD", query=...)` |
| Shared facts across bots | `recall_shared(query=...)` |

## MCP args (contract)

| Tool | Required | Optional (defaults) |
|------|----------|---------------------|
| `recall_current` | `query` | `mode`=`fast`\|`deep`; `limit`=10 (cap 40); `root` |
| `recall_bot` | `bot` | `query`="" (empty → style pack); `limit`=12; `include_style`=true; `root` |
| `recall_shared` | `query` | `limit`=12; `bot`; `root` |
| `recall_chatvault_day` | `day`=`YYYY-MM-DD` | `query`=""; `limit`=20 |
| `recall_chatvault` | same | **alias** of `recall_chatvault_day` |

Notes:
- All tools **read-only** on live vendor cores.
- Prefer quoting `as_of` / `temporal` from hits.
- Pass `bot` (not `bot_name`) on `recall_bot`.

## Liquid memory (fast vs deep)

Thin pack contract (MUST layer 17): `docs/liquid-fast-deep-pack.md` (alias `docs/17-liquid-fast-deep.md`). MCP contract: `mcp/bot-memory/TOOLS-CONTRACT.md`.

- **Fast** — thin FTS, current-only, low latency; known-path gate.
- **Deep** — prior-merge first, then hybrid FTS + **local** embeddings (RRF); offline hash fallback OK.

### DEEP rules (prior-first + cite-when-true)

1. **Prior-first** — pull workflow / standing_rules / analysis / `anti_pattern` before web.
2. **Cite when-true** — every acted-on claim quotes an `as_of` line.
3. **Act on CURRENT only** — HISTORICAL stays labelled unless user asked for history.
4. **Reuse beats re-brainstorm** — follow `workflow` / `analysis_id` when present.
5. **DEEP_EMPTY** → try `recall_bot` / `recall_shared`, then ask the lead.

## New-chat recovery recipe (EXAMPLE)

1. `recall_bot(bot="example-lead", query="style OR journal OR profile")`
2. Optional: `recall_chatvault_day(day=<today or last active>, query=<topic>)`
3. Optional: `recall_current(topic, mode="fast")` for durable shared facts
4. Speak in recovered style; **do not invent** missing shards — say what was found.

## Topest (always-on)

1. Read `topest/ALWAYS-ON.md` every session (thin pack ≤6 structural siblings).
2. Keyword-match only → pull `topest/rules/<name>.md` (never dump all rules).
3. After interesting work → write `events/YYYY-MM-DD-<slug>.md`, **then** claim done.

## Mixing day sync + bot style

Treat day notes and bot shards as **context inputs**, then answer as the active agent. Do not dual-write two memory systems.
