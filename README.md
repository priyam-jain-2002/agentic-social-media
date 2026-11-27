# Agentic Social Media

**An evidence-first, Markdown-based editorial operating system for LinkedIn, X and a personal blog.** It turns one real observation or verified external signal into **zero to three platform-native decisions**—never automatic cross-posting.

Works with ChatGPT, Claude Code or another assistant that can read Markdown. No account connection, API key, hosted service or build step is required.

> **Framework-only repository.** Finished posts, drafts, dated weekly radar outputs, analytics and private project notes belong in chat or a separate private workspace—not in this repository. [Privacy rules](SECURITY.md).

## Quick start

1. Ask your assistant to read [AGENTS.md](AGENTS.md) (Claude Code also reads [CLAUDE.md](CLAUDE.md)).
2. Share a project observation, source article, technical claim or analogy. Alternatively request a current [weekly topic scan](skills/topic-radar/SKILL.md).
3. The agent researches and challenges the idea, identifies reader value, and checks evidence and confidentiality.
4. It independently chooses `PUBLISH / ADAPT / HOLD / SKIP` for LinkedIn, X and blog.
5. Only appropriate channels receive drafts **in the conversation or user-approved private destination**. No automatic publication.

Try:

```text
Read AGENTS.md and WORKFLOW.md. Research the last 7 days using
sources/RADAR.md, then propose 3–5 topics with primary sources,
one concrete reader problem, counterargument and experiment each.
Independently assess LinkedIn, X and blog. Do not draft or post yet.
```

For a firsthand insight:

```text
Read AGENTS.md and skills/insight-extraction/SKILL.md.
Here's what I built / discovered: ...
Find the specific claim we can prove and the reader who benefits.
Keep the record private; don't commit content to this repository.
```

## Structure

| Location | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md) | Cross-client editorial contract |
| [PLAYBOOK.md](PLAYBOOK.md) | Identity, taxonomy, audience, platform routing |
| [WORKFLOW.md](WORKFLOW.md) | Weekly signal + firsthand insight pipeline |
| [skills/](skills) | Independent research, publishing, editing, discovery, visuals and analytics skills |
| [sources/RADAR.md](sources/RADAR.md) | Public-source watchlist |
| [research/evidence.md](research/evidence.md) | Durable primary-source evidence about platform behavior |
| [templates/](templates) | Blank reusable private-workspace templates |
| [integrations/README.md](integrations/README.md) | Optional MCP/source connections and privacy boundaries |
| [scripts/validate_public_repo.py](scripts/validate_public_repo.py) | Repo-only hygiene and Markdown link validation |
| [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md) | Safety policy and contribution process |

## Operating principles

- **Reader payoff first.** Explain a concrete result, problem, experiment or useful difference before generic context.
- **Original evidence matters.** Never pretend to have run code, spoken to a customer or observed metrics without proof.
- **Critical editing.** Every claim, platform choice, visual, keyword, hashtag and person tag must earn its place.
- **No AI-slop.** Natural engineering prose; no fake suspense, slogans, or manufactured virality.
- **Independent channel decisions.** A topic can suit a durable blog article but not a LinkedIn post (or vice versa).
- **No publishing without approval.** Research connectors are read-only by default; no unapproved posting, DMs or repo writes.
- **No algorithm myths.** Length and hashtag guidance are editorial experiments, not reach guarantees.

## Optional integrations

The core needs no MCP connection. For stronger results, the most useful **optional** inputs are verified public web research, approved read-only GitHub project evidence, a private Notion/notes ledger, and first-party platform analytics. See [integrations/README.md](integrations/README.md) for scope, security, limitations and example capability policy. Connections are configured **outside this repo**.

## Contributing and verification

This repository intentionally contains **no finished example posts or personal performance records**. To propose a new skill, add a reusable `skills/<name>/SKILL.md`, cite supported claims, and run:

```bash
python3 scripts/validate_public_repo.py
```

The same check runs on pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md). The framework does not itself publish articles or run weekly jobs; those actions require a separately configured assistant/scheduler and explicit approval.
