#!/usr/bin/env python3
"""Validate the skill collection layout, frontmatter names, eval JSON, and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*['\"]?([^\s'\"]+)['\"]?\s*$", re.MULTILINE)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_skill_packages(errors: list[str]) -> None:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("skills/: no */SKILL.md entrypoints found")
        return

    for skill_file in skill_files:
        relative = skill_file.relative_to(ROOT)
        content = skill_file.read_text(encoding="utf-8")
        frontmatter = FRONTMATTER_RE.match(content)
        if not frontmatter:
            errors.append(f"{relative}: missing YAML frontmatter")
            continue
        name = NAME_RE.search(frontmatter.group(1))
        if not name:
            errors.append(f"{relative}: frontmatter has no simple name field")
            continue
        if name.group(1) != skill_file.parent.name:
            errors.append(
                f"{relative}: directory name {skill_file.parent.name!r} "
                f"does not match frontmatter name {name.group(1)!r}"
            )

        eval_file = skill_file.parent / "evals" / "evals.json"
        if eval_file.is_file():
            try:
                parsed = json.loads(eval_file.read_text(encoding="utf-8"))
                if not isinstance(parsed, list):
                    errors.append(f"{eval_file.relative_to(ROOT)}: expected a JSON array")
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{eval_file.relative_to(ROOT)}: invalid JSON: {exc}")


def check_markdown_links(errors: list[str]) -> None:
    for source in ROOT.rglob("*.md"):
        relative = source.relative_to(ROOT)
        if any(part.startswith(".") for part in relative.parts):
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
                parsed = urlparse(target)
                if parsed.scheme or target.startswith("//") or target.startswith("#"):
                    continue
                local_path = unquote(parsed.path)
                if not local_path:
                    continue
                resolved = (source.parent / local_path).resolve()
                if not resolved.exists():
                    errors.append(f"{relative}:{line_number}: local link target not found: {local_path}")


def main() -> int:
    errors: list[str] = []
    for required in (ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "agent/README.md"):
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")
    check_skill_packages(errors)
    check_markdown_links(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed (entrypoints, names, eval JSON, local Markdown links).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
