"""Print a short walkthrough of files=SSOT and INF."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run_demo() -> int:
    print("=== grok-bot-portable demo ===\n")
    print("1) Files = SSOT")
    print("   Durable facts live in files YOU own (repo / store / vault).")
    print("   Chat scrollback is ephemeral. Agents re-read files, not memory guesses.\n")

    print("2) INF (Interchange / event layer)")
    schema = ROOT / "schemas" / "memory-event.schema.json"
    if schema.is_file():
        data = json.loads(schema.read_text(encoding="utf-8"))
        print(f"   Schema: {schema.relative_to(ROOT)}")
        print(f"   Title:  {data.get('title', '(none)')}")
        required = data.get("required", [])
        print(f"   Required fields: {', '.join(required) if required else '(none)'}")
        print("   Idea: one JSON shape so humans + bots log the same event.\n")
    else:
        print(f"   (schema missing at {schema})\n")

    print("3) Cards-as-code (thin)")
    card = ROOT / "cards" / "safe-outbound.md"
    if card.is_file():
        first = card.read_text(encoding="utf-8").strip().splitlines()[:4]
        print(f"   Sample: {card.relative_to(ROOT)}")
        for line in first:
            print(f"   | {line}")
        print()
    else:
        print(f"   (card missing at {card})\n")

    print("4) Plans (official prices — re-check docs.x.ai)")
    plans = ROOT / "data" / "plans.yaml"
    if plans.is_file():
        print(f"   See: {plans.relative_to(ROOT)}")
        # Print ultra line without inventing
        for line in plans.read_text(encoding="utf-8").splitlines():
            if "ultra:" in line.lower() or line.strip().startswith("ultra"):
                print(f"   {line.strip()}")
                break
        print("   Ultra = $200/mo, 50x vs Plus. Weekly shared pool; credits separate.\n")
    else:
        print(f"   (plans missing at {plans})\n")

    ssot = ROOT / "examples" / "ssot-sample"
    print("5) Sample SSOT tree")
    if ssot.is_dir():
        print(f"   {ssot.relative_to(ROOT)}/ — notes/ + events/ placeholders")
        ev = ssot / "events" / "1970-01-01-demo.json"
        if ev.is_file():
            print(f"   Event JSON: {ev.relative_to(ROOT)}")
    else:
        print("   (ssot-sample missing)")
    print()
    stub = ROOT / "stubs" / "deliverable-stub.html"
    print("6) Few artifacts")
    print(f"   HTML stub: {stub.relative_to(ROOT) if stub.is_file() else '(missing)'}")
    print()
    print("Done. Next: copy cards/ into your own bot rules; keep schemas/ stable.")
    print("Do NOT write into any live Claude ~/.claude/memory-core path.")
    return 0
