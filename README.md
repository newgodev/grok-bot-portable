# grok-bot-portable

Portable **files=SSOT + INF** system for Grok Bot users — system, code, prompts/skills, and a few teaching artifacts in **one** repo.

**This week’s public ship = 1** (this monorepo). Portable Memory v2 / INF — not 15 repos, not a marketplace dump.

Clone → read → run one demo.

## Quick start

```bash
git clone <this-repo> grok-bot-portable
cd grok-bot-portable
pip install -e .
python -m grokbot_portable demo
```

Or without install:

```bash
PYTHONPATH=src python -m grokbot_portable demo
```

---

## 1. Use this repo

**System + Code** in one place:

- **Files = SSOT** — durable facts live in files you own, not chat scrollback (`examples/ssot-sample/`).
- **INF** — one event schema so humans and tools read the same records (`schemas/`).
- **Demo** — `python -m grokbot_portable demo` walks the sample tree.

Point your own bot at a folder you control (placeholder: `<your-ssot-root>/`). Never write into someone else’s live memory store.

Memory v2 (when you use it) is **one** system: topest rules, batch rules, self-map / rate / wake rules, recovery — not seven separate products.

---

## 2. Copy prompts / skills

**Prompt + skill** — thin cards in `cards/` (short when→then text you can paste into a Bot Description or skill).

Optional: `examples/walls/` holds **one scrubbed EXAMPLE** marketplace-style wall. Treat it as EXAMPLE only; keep ALWAYS-ON thin.

Related public skill patterns (cite, not ship): [obra/superpowers](https://github.com/obra/superpowers) · files=SSOT vibe [JoaquimLegal/mnemo](https://github.com/JoaquimLegal/mnemo).

---

## 3. Artifacts point you at this system

HTML stub (`stubs/deliverable-stub.html`) and sample events exist to **teach System / Code / Prompt+skill above** — not a second line of deliverables, and not a guide to opening other repos.

Run `demo` → see schema + card + stub. That’s the teaching loop.

---

## Ultra / plan (facts)

Using **Ultra ($200/mo, 50× vs Plus)** helped when many agents share one weekly pool. Numbers from official pages only — re-check before you rely on them:

- https://x.ai/pricing
- https://docs.x.ai/x-subscription/pricing

Human chapter: `docs/ultra-plan.md`. Machine-readable: `data/plans.yaml`.

---

## Layout

```
grok-bot-portable/
  README.md
  pyproject.toml
  src/grokbot_portable/     # Code
  schemas/                  # System (ONE INF schema)
  cards/                    # Prompt / skill
  data/plans.yaml           # Ultra facts
  docs/ultra-plan.md
  examples/ssot-sample/
  examples/walls/           # optional ONE EXAMPLE wall
  stubs/deliverable-stub.html
  docs/gotchas.md           # Desc / Bot Description gotchas
  cards/desc-gotchas.md
```

## Cut on purpose

Extra branding wrappers · multi-repo inventories · personal identity · school work · live Claude memory writes · public wake-budget playbooks · “how to post / open many GitHub repos” guides.

## Optional related

Windows desktop helpers (sshd orphan / Deskflow / ClipCursor) live in a **separate** repo — not part of this monorepo: `https://github.com/<OWNER>/desktop-healers`

## License

Public-safe teaching material. Non-personal.
