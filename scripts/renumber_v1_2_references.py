#!/usr/bin/env python3
"""Renumber v1.2 references by first appearance and update its figure-source trace."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "final" / "manuscript_v1.2.md"
TRACE = ROOT / "figures" / "figure_sources_v1.2.md"
MAP_FILE = ROOT / "final" / "reference_number_map_v1.2.json"


def replace_numbers(text: str, mapping: dict[int, int]) -> str:
    return re.sub(r"\[(\d+)\]", lambda m: f"[{mapping[int(m.group(1))]}]", text)


def main() -> None:
    source = MANUSCRIPT.read_text(encoding="utf-8")
    marker = "## 参考文献"
    body, refs_part = source.split(marker, 1)

    order: list[int] = []
    for match in re.finditer(r"\[(\d+)\]", body):
        old = int(match.group(1))
        if old not in order:
            order.append(old)

    refs: dict[int, str] = {}
    for line in refs_part.splitlines():
        match = re.match(r"^\[(\d+)\]\s+(.*)$", line)
        if match:
            refs[int(match.group(1))] = match.group(2)

    if set(order) != set(refs):
        raise RuntimeError(
            f"Citation/reference mismatch: uncited={sorted(set(refs)-set(order))}, "
            f"missing={sorted(set(order)-set(refs))}"
        )

    mapping = {old: new for new, old in enumerate(order, 1)}
    new_body = replace_numbers(body, mapping)
    new_refs = "\n\n".join(f"[{mapping[old]}] {refs[old]}" for old in order)
    MANUSCRIPT.write_text(f"{new_body}{marker}\n\n{new_refs}\n", encoding="utf-8")

    if TRACE.exists():
        TRACE.write_text(replace_numbers(TRACE.read_text(encoding="utf-8"), mapping), encoding="utf-8")

    MAP_FILE.write_text(
        json.dumps(
            {
                "description": "v1.2 reference renumbering: old number to new first-appearance number",
                "old_to_new": {str(old): new for old, new in sorted(mapping.items())},
                "first_appearance_old_numbers": order,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Renumbered {len(order)} references")


if __name__ == "__main__":
    main()
