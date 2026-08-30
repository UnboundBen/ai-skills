#!/usr/bin/env python3
"""Validate every skill entrypoint in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SCAFFOLD_MARKERS = (
    "TODO: Complete",
    "[TODO",
    "<skill-name>",
    "Replace this",
)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]

    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            errors.append(f"malformed top-level frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')

    if end == len(lines) - 1 or not any(line.strip() for line in lines[end + 1 :]):
        errors.append("SKILL.md has no instruction body")
    for marker in SCAFFOLD_MARKERS:
        if marker in text:
            errors.append(f"unfinished scaffold marker: {marker!r}")
    return fields, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    name = skill_dir.name
    if len(name) > 63 or not NAME_RE.fullmatch(name):
        errors.append("folder name must be lowercase hyphenated text under 64 characters")

    fields, frontmatter_errors = parse_frontmatter(skill_file)
    errors.extend(frontmatter_errors)
    if fields.get("name") != name:
        errors.append(f"frontmatter name must equal folder name {name!r}")
    if not fields.get("description"):
        errors.append("frontmatter description is required")

    for path in skill_dir.rglob("*"):
        if path.is_symlink():
            errors.append(f"public skill contains symlink: {path.relative_to(skill_dir)}")
    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: missing skills directory", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        print("ERROR: no skills found", file=sys.stderr)
        return 1

    failures = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"FAIL {skill_dir.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {skill_dir.name}")

    print(f"\nValidated {len(skill_dirs)} skill(s); {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
