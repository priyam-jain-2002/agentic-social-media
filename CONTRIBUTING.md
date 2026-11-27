# Contributing

This is a Markdown-first editorial **framework**, not a repository of social posts.

## Acceptable contributions
- Portable skills under `skills/<feature>/SKILL.md`, with trigger, required inputs, output format, hard gates and limitations.
- Reusable templates in `templates/`.
- Cross-client instructions, integrations guidance, source manifests and policy improvements.
- Small validation scripts/tests that help keep the repository clean.
- Public primary-source methodology, with links, dates and appropriately bounded claims.

## Not accepted
- Finished LinkedIn/X/blog posts, editorial drafts, generated weekly reports, personal project notes, analytics, screenshots, tokens or customer/employer data.
- Unsupported claims about platform ranking algorithms or guarantees of reach.
- Vendor-specific integration snippets containing credentials or broad write permissions.

## Pull request checklist
1. Explain the reader problem and how the rule or tool improves reliability.
2. Preserve platform-specific PUBLISH/ADAPT/HOLD/SKIP decisions.
3. Prefer authoritative source links and note uncertainty.
4. Check instructions in both `AGENTS.md` and `CLAUDE.md` remain interoperable.
5. Run `python3 scripts/validate_public_repo.py`.
6. Confirm no unapproved private data or generated editorial output is committed.

Do not claim a tool/source was connected or executed unless it actually was.
