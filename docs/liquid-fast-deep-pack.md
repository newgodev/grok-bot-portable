# Liquid FAST / DEEP pack contract (MUST layer 17)

Teaching page for the **same-feel** public pack. Scrubbed shape only — no personal vault.

**Live refuse:** never write a live vendor memory core. Point adapters at `<your-ssot-root>/` or env `SSOT_ROOT` / `LIVE_MEMORY_PATH` (stub name only).

## Why this page

Memory v2 feel is not “cards only”. Agents switch between:

| Mode | When | Pack |
|------|------|------|
| **FAST** | Known path already analysed | Thin tip ≤8 (cap 12), current-only |
| **DEEP** | Gate miss / unknown / high stakes | Prior-merge + hybrid RRF ≤20 (cap 32); cite `as_of` |

## FAST pack (thin)

**Gate:** at least one of — named known-path · current `kind=workflow|standing_rules` · `reuse_path` / `analysis_id` · lead says “fast pack”.

**Return:** ≤8 hits, all CURRENT. Rank: workflow → subject facts → delivery prefs.

**Omit:** open-ended topics · historical debates · full day dumps (at most one pointer).

**Fail:** `FAST_GATE_MISS` → escalate to DEEP. Do not invent.

**Event tip (optional in FAST):** newest 1–2 `kind=event` notes for the same path only.

## DEEP pack (prior-first)

1. Hybrid recall (FTS + local embed RRF; hash offline OK).
2. Prior boost: `{subject} workflow|standing_rules|analysis` and `anti_pattern|failure`.
3. Dedupe by uid; CURRENT before HISTORICAL; every hit keeps `as_of`.
4. Optional research **after** prior-merge only.
5. Event sample: same subject ≤3 newest CURRENT `kind=event|after_action`, each with `as_of`.

**Fail:** `DEEP_EMPTY` → `recall_bot` / `recall_shared`, then ask lead.

## CLI / MCP shape

```text
recall --root <your-ssot-root> --mode fast|deep "query"
recall_current(query, mode="fast"|"deep")
```

- FAST forces current-only; smaller limit.
- DEEP default current-only; history via explicit `--as-of` / `--include-historical`.
- Never strip temporal fields to save tokens.

## ALWAYS-ON vs FAST

ALWAYS-ON thin pack (≤6 structural verb cards) loads via skill / `recall_topest` — **not** via FAST RRF scan of `rules/`.

## Related MUST layers

1 INF files=SSOT · 2 thin ALWAYS-ON · 4 SAMPLE events · 6 bot-memory skill · 7 MCP contract · 11 gate story · 13 live-refuse · 15 temporal / supersede · **17 this page**

## CUT from this public page

Real personal rules · vault day dumps · HQ wake / room rosters · quiet-DR zips · private absolute paths.
