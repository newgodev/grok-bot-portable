# OPTIONAL layer 8 — Client wire (EXAMPLE)

How any AI client talks to a **bot-memory** MCP adapter. Files remain SSOT; MCP is only an adapter.

Live vendor memory cores: **refuse-write**.

## Env placeholders

| Name | Meaning |
|------|---------|
| `LIVE_MEMORY_PATH` | Your sandbox store root (never a live vendor core) |
| `BOT_MEMORY_SERVER` | Path to `server.py` under your checkout |

## Cursor / Claude Desktop (stdio EXAMPLE)

```json
{
  "mcpServers": {
    "bot-memory": {
      "command": "python",
      "args": ["BOT_MEMORY_SERVER/server.py"],
      "env": {
        "MEMORY_CORE_V2_ROOT": "LIVE_MEMORY_PATH"
      }
    }
  }
}
```

Restart the client after save. Expected tool **names** (contract only):
`recall_current`, `recall_bot`, `recall_shared`, `recall_chatvault` (optional day bridge).

## Multi-client note

Grok Bot / Claude / Codex / Cursor differ only in **how** they launch the same adapter.
Point every client at the **same** `LIVE_MEMORY_PATH` so the feel stays identical.

## CUT

Hardcoded `E:\…` / `C:\Users\…` · API keys · allowlists · agent UUIDs · HQ wake boards.
