"""Smoke: INF schema exposes Layer-15 temporal / supersede fields."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "memory-event.schema.json"


class TestSchemaTemporal(unittest.TestCase):
    def test_schema_file_exists(self) -> None:
        self.assertTrue(SCHEMA.is_file(), f"missing {SCHEMA.relative_to(ROOT)}")

    def test_temporal_fields_present(self) -> None:
        data = json.loads(SCHEMA.read_text(encoding="utf-8"))
        props = data.get("properties") or {}
        for key in ("valid_from", "valid_to", "supersedes", "superseded_by"):
            self.assertIn(key, props, f"schema missing Layer-15 field: {key}")

    def test_required_core_fields(self) -> None:
        data = json.loads(SCHEMA.read_text(encoding="utf-8"))
        required = set(data.get("required") or [])
        self.assertTrue({"id", "ts", "kind", "summary"}.issubset(required))


if __name__ == "__main__":
    unittest.main()
