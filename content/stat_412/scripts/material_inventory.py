#!/usr/bin/env python3
"""Inventory incremental homework materials and record a local ignored snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

QUESTION_MD = re.compile(r"q(\d+)\.md$", re.IGNORECASE)
NUMBERED_IMAGE = re.compile(
    r"^(?:q)?(\d+)(?:[-_](\d+))?\.(?:png|jpe?g|webp)$", re.IGNORECASE
)
HTML_TAG = re.compile(
    r"<(?:div|span|table|tr|td|p|a|button|input|math|img|br|strong|em)\b",
    re.IGNORECASE,
)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("homework", type=Path, help="Path such as content/stat_412/HW03")
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Print the inventory without updating the ignored snapshot.",
    )
    args = parser.parse_args()
    root = args.homework.resolve()
    if not root.is_dir():
        raise SystemExit(f"Homework directory not found: {root}")

    files = sorted(path for path in root.iterdir() if path.is_file())
    current = {
        path.name: {"size": path.stat().st_size, "sha256": digest(path)}
        for path in files
    }

    log_dir = root / ".worklogs"
    snapshot_path = log_dir / "material_snapshot.json"
    previous: dict[str, dict[str, object]] = {}
    if snapshot_path.exists():
        previous = json.loads(snapshot_path.read_text()).get("files", {})

    new = sorted(set(current) - set(previous))
    removed = sorted(set(previous) - set(current))
    changed = sorted(
        name
        for name in set(current) & set(previous)
        if current[name]["sha256"] != previous[name].get("sha256")
    )

    question_images: dict[int, list[str]] = {}
    unassigned_images: list[str] = []
    html_questions: list[tuple[int, int]] = []

    for path in files:
        image_match = NUMBERED_IMAGE.match(path.name)
        if image_match:
            number = int(image_match.group(1))
            question_images.setdefault(number, []).append(path.name)
        elif path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            unassigned_images.append(path.name)

        md_match = QUESTION_MD.match(path.name)
        if md_match:
            text = path.read_text(errors="replace")
            tags = len(HTML_TAG.findall(text))
            if tags:
                html_questions.append((int(md_match.group(1)), tags))

    print(f"Homework: {root}")
    print(f"New files: {', '.join(new) if new else 'none'}")
    print(f"Changed files: {', '.join(changed) if changed else 'none'}")
    print(f"Removed files: {', '.join(removed) if removed else 'none'}")
    print("\nNumbered screenshots by question:")
    if question_images:
        for number in sorted(question_images):
            names = sorted(
                question_images[number],
                key=lambda name: (
                    NUMBERED_IMAGE.match(name).group(2) is not None,
                    int(NUMBERED_IMAGE.match(name).group(2) or 1),
                    name,
                ),
            )
            marker = " MULTIPLE" if len(names) > 1 else ""
            print(f"  Q{number}: {', '.join(names)}{marker}")
    else:
        print("  none")
    print("\nMarkdown files containing pasted HTML:")
    if html_questions:
        for number, tags in sorted(html_questions):
            print(f"  Q{number}: {tags} recognized HTML tags")
    else:
        print("  none")
    print("\nUnassigned/timestamp screenshots:")
    for name in unassigned_images:
        print(f"  {name}")
    if not unassigned_images:
        print("  none")

    if not args.no_write:
        log_dir.mkdir(exist_ok=True)
        payload = {
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "files": current,
        }
        snapshot_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(f"\nSnapshot updated: {snapshot_path}")


if __name__ == "__main__":
    main()
