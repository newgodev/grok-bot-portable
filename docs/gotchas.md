# Gotchas (Desc / Bot Description)

Short rules you can paste into a Bot **Description**. Keep ALWAYS-ON thin.

## Do

- Treat **files as SSOT** — durable facts live in folders you own; re-read files, don’t invent from chat scrollback.
- Use **one INF event shape** (`schemas/memory-event.schema.json`) when logging events.
- Keep prompt cards **thin** (`cards/`). Prefer short when→then text over fat walls.
- Draft outbound messages; **send only** when the user names who + what (see `cards/safe-outbound.md`).
- Treat `examples/walls/` as **EXAMPLE only** — not a second product line.

## Don’t

- Don’t write into anyone else’s live Claude `~/.claude/memory-core` (or equivalent live store).
- Don’t ship personal emails, allowlists, school homework, or private machine paths in public material.
- Don’t publish wake-budget / HQ rate-limit playbooks as public “how to” docs.
- Don’t bolt desktop recovery utilities (sshd / Deskflow / ClipCursor) into this monorepo — those stay a **separate linked** repo when published.

## Ultra (facts only)

Ultra pricing lives in `docs/ultra-plan.md` and `data/plans.yaml`. Re-check official xAI pages before you rely on numbers.
