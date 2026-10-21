# bot-memory MCP — tools contract (MUST layer 7)

Public-safe **adapter** contract. Files under `<your-ssot-root>/` are the memory; this MCP is optional.

**No keys · no absolute personal paths · no live vendor core writes.**

## Hard rules

| Rule | Meaning |
|------|---------|
| Local SSOT | Durable memory = open files (md / JSONL / rebuildable SQLite). |
| Any AI can read | Same tree after copy/export. Losing one vendor account must not lose memory. |
| Live refuse | Hard-block writes to any live vendor memory path (`LIVE_MEMORY_PATH` stub). |
| Root | Pass `root` or env `SSOT_ROOT` → `<your-ssot-root>/`. |

## Tools

| Tool | Required | Optional (defaults) | Role |
|------|----------|---------------------|------|
| `recall_current` | `query` | `mode`=`fast`\|`deep`; `limit`=10 (cap 40); `root` | Liquid current recall |
| `recall_bot` | `bot` | `query`=""; `limit`=12; `include_style`=true; `root` | One bot’s shards / style |
| `recall_shared` | `query` | `limit`=12; `bot`; `root` | Shared facts across bots |
| `recall_chatvault_day` | `day`=`YYYY-MM-DD` | `query`=""; `limit`=20 | Day transcript pointer |
| `recall_chatvault` | same | alias of `recall_chatvault_day` | |

All tools are **read-only** on live vendor cores. Prefer quoting `as_of` / temporal fields from hits.

## Error contract (stable codes)

| Code | Meaning |
|------|---------|
| `path_refuse` | Root outside allowed store / live core blocked |
| `empty_recall` | Index ok, zero hits (`ok=true` + code) |
| `not_indexed` | Rebuildable index missing / unreadable |
| `bad_input` | Invalid args |
| `recall_failed` | Unexpected failure (message scrubbed) |

Failure envelope shape:

```json
{ "ok": false, "error": { "code": "path_refuse", "message": "..." } }
```

Empty-success shape:

```json
{ "ok": true, "code": "empty_recall", "hits": [], "count": 0 }
```

Scrub secrets and absolute user-profile paths from every message before return.

## Minimal client wire (EXAMPLE)

Point your client at a local stdio server you run against **your** store:

```text
command: <your-python> <path-to-your-adapter>/server.py
env: SSOT_ROOT=<your-ssot-root>
```

Deleting a client config must **not** delete memory files.

## Related

- Skill: `skills/bot-memory/SKILL.md`
- Liquid FAST/DEEP: `docs/liquid-fast-deep-pack.md`
- Live refuse: `examples/topest/live-refuse.md`
- Temporal fields: `docs/TEMPORAL-FRONTMATTER.md`
