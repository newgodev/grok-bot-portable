# Scrubbed skill fragment — Liquid FAST / DEEP (EXAMPLE)

Drop into a public `skills/bot-memory/SKILL.md` under **Liquid memory**. No usernames, no live vendor paths.

## Liquid memory (fast vs deep)

- **Fast** — thin FTS, current-only, low latency. Use when a known workflow path already exists.
- **Deep** — prior-merge first; optional local FTS+embed RRF. Offline hash embed OK. No cloud embed as SSOT.

### DEEP rules (prior-first + cite-when-true)

When `mode="deep"` (or after `FAST_GATE_MISS`):

1. Prior-first — workflow / standing_rules / analysis / anti_pattern before web.
2. Cite when-true — quote `as_of` on every acted claim.
3. Act on CURRENT only — HISTORICAL stays labelled.
4. Reuse beats re-brainstorm when pack shows workflow / anti_pattern / analysis_id.
5. DEEP_EMPTY → `recall_bot` / `recall_shared`, then lead; research only after prior pass.

### CLI shape (sandbox placeholder)

```text
python recall_v2.py --root <your-ssot-root> --mode fast "query"
python recall_v2.py --root <your-ssot-root> --mode deep "query"
```

See optional page: `docs/17-liquid-fast-deep.md`.
