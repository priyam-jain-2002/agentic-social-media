#!/usr/bin/env python3
"""No-dependency hygiene check for the public, framework-only repository.

Run: python3 scripts/validate_public_repo.py
It checks committed file paths and relative Markdown links (not external URLs).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TOP_LEVEL = {
    ".github", ".gitignore", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md",
    "PLAYBOOK.md", "README.md", "SECURITY.md", "WORKFLOW.md", "LICENSE",
    "examples", "integrations", "research", "scripts", "skills", "sources", "templates",
}
OUTPUT_COMPONENTS = {
    "drafts", "posts", "content", "outputs", "out", "private",
    "insights", "reports", "radars", "weeks",
}
PERMITTED_RESEARCH = {"research/evidence.md"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
TOKEN_RE = re.compile(r"(?i)\b(?:github_pat_[a-z0-9_]{20,}|ghp_[a-z0-9]{30,}|sk-[a-z0-9]{30,})\b")


def git_paths() -> list[Path]:
    data = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [Path(x.decode("utf-8")) for x in data.split(b"\0") if x]


def main() -> int:
    errors: list[str] = []
    paths = git_paths()
    for path in paths:
        parts = path.parts
        if parts[0] not in ALLOWED_TOP_LEVEL:
            errors.append(f"Not framework-only: {path}")
        if any(part.lower() in OUTPUT_COMPONENTS for part in parts):
            errors.append(f"Generated/personal content folder is tracked: {path}")
        if parts[0] == "research" and path.as_posix() not in PERMITTED_RESEARCH:
            errors.append(f"Only durable methodology belongs in research/: {path}")
        if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ".json", ""}:
            errors.append(f"Unexpected file format: {path}")
        fp = ROOT / path
        if not fp.is_file():
            errors.append(f"Missing tracked file: {path}")
            continue
        if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ".json"}:
            continue
        text = fp.read_text(encoding="utf-8")
        if TOKEN_RE.search(text):
            errors.append(f"Possible credential pattern: {path}")
        if path.suffix.lower() != ".md":
            continue
        for dest in LINK_RE.findall(text):
            dest = dest.strip()
            if not dest or dest.startswith(("#", "http://", "https://", "mailto:", "data:")):
                continue
            # Anchor and optional Markdown title are irrelevant to local path existence.
            target = unquote(dest.split("#", 1)[0].split(" ", 1)[0].strip("<>"))
            if not target:
                continue
            resolved = (fp.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Link escapes repository in {path}: {dest}")
                continue
            if not resolved.exists():
                errors.append(f"Broken local link in {path}: {dest}")

    # Validate the one self-contained distributable Agent Skill.
    installed = ROOT / "skills" / "agentic-social-media" / "SKILL.md"
    if not installed.exists():
        errors.append("Missing installable skill: skills/agentic-social-media/SKILL.md")
    else:
        body = installed.read_text(encoding="utf-8")
        lines = body.splitlines()
        if not lines or lines[0] != "---":
            errors.append("Distributable SKILL.md has no YAML frontmatter")
        else:
            try:
                closing = lines.index("---", 1)
            except ValueError:
                errors.append("Distributable skill frontmatter is not closed")
                closing = 1
            fields = lines[1:closing]
            if "name: agentic-social-media" not in fields:
                errors.append("Distributable skill name must match folder")
            if not any(line.startswith("description: ") and len(line) > 45 for line in fields):
                errors.append("Distributable skill needs a meaningful description")
        for required in ("research.md", "platforms.md", "gates.md", "visuals.md", "examples.md"):
            if not (installed.parent / "references" / required).is_file():
                errors.append(f"Missing bundled reference: {required}")

    if errors:
        print("Public repository hygiene FAIL:")
        for issue in errors:
            print(" -", issue)
        return 1
    print(f"Public repository hygiene PASS ({len(paths)} tracked files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
