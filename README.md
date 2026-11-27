# Agentic Social Media

**A portable editorial skill for people who actually build things.**

Turn original engineering work, a verified research finding, or a useful analogy into credible LinkedIn, X and blog writing. It challenges the idea before drafting, keeps the voice natural, and can confidently recommend **not posting**.

**LinkedIn first · X second · Blog third · No forced cross-posting**

[Read the skill](skills/agentic-social-media/SKILL.md) · [Explore examples](examples/README.md) · [Understand the gates](skills/agentic-social-media/references/gates.md) · [Agent Skills specification](https://agentskills.io/specification)

## Install in one command

```bash
npx skills add priyam-jain-2002/agentic-social-media --skill agentic-social-media
```

For a global Claude Code installation:

```bash
npx skills add priyam-jain-2002/agentic-social-media --skill agentic-social-media -g -a claude-code -y
```

The **single distributable skill includes its own references and examples** under [skills/agentic-social-media](skills/agentic-social-media). You don't need to clone the full repository to use it.

For agents without an installer (including normal ChatGPT chats), share this repository and ask the assistant to read [AGENTS.md](AGENTS.md). Installation does not grant access to your social accounts or configure research integrations.

## How to use it

Ask your assistant to use the skill, then provide one observation or request a topic scan.

| Goal | Example prompt |
| --- | --- |
| Find new topics | "Find this week's strongest AI engineering and product topics. Give 3–5 with real source links, reader problem, proposed proof, and LinkedIn/X/blog fit. No drafts yet." |
| Turn a build into writing | "I moved our storefront to a custom frontend and managed commerce backend. Find the one useful engineering lesson. Ask for proof if needed." |
| Evaluate an analogy | "Could accelerator portability be analogous to cloud vendor lock-in? Check where the analogy is useful and where it fails." |
| Fix a draft | "Audit this for originality, early payoff, natural voice, evidence, useful hashtags and legitimate mentions. Tell me if it isn't worth posting." |
| Plan a graphic | "Only if a visual improves understanding, write a mobile-first diagram/screenshot brief with source and alt text." |
| Review performance | "Use the 72-hour results to distinguish weak distribution, poor reader fit and low-quality engagement. Don't infer causes from one post." |

### What the skill does

```text
Firsthand work / verified news
           |
      Idea + audience
           |
   Evidence + counterargument
           |
  Is this actually worth sharing?
           |
   +-------+---------+
   |       |         |
LinkedIn    X       Blog
   |       |         |
PASS / ADAPT / HOLD / SKIP
           |
   Natural voice, tags,
   proof & visual checks
           |
   Author approves publishing
```

**The system does not promise likes, fabricate source material, automatically schedule posts or send engagement messages.**

## See examples

- [Headless commerce: one insight, three different decisions](examples/README.md#sample-1--a-frontend-engineer-chooses-headless-commerce)
- [Workflow retries: why a release announcement isn't enough](examples/README.md#sample-2--a-performance-release-invites-a-correctness-question)

These contain *synthetic sample openings and routing decisions*, not real personal drafts or published engagement claims. Public post links are added only after verification and permission.

## Repository structure

| Path | Role |
| --- | --- |
| [skills/agentic-social-media](skills/agentic-social-media) | **Installable**, self-contained Agent Skill |
| [skills/](skills) | Expanded maintainer modules for research, editorial gates, platforms, human voice, visuals and analytics |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | Markdown instructions for ChatGPT / Claude |
| [PLAYBOOK.md](PLAYBOOK.md) / [WORKFLOW.md](WORKFLOW.md) | Full operating philosophy and weekly insight pipeline |
| [sources/RADAR.md](sources/RADAR.md) | Maintained primary-source watchlist |
| [examples/README.md](examples/README.md) | Safe illustrative usage, no personal content |
| [integrations/README.md](integrations/README.md) | Optional read-only GitHub MCP, web, private notes and analytics |
| [SECURITY.md](SECURITY.md) / [CONTRIBUTING.md](CONTRIBUTING.md) | Public repo boundaries and contributions |

## Optional integrations

No integrations are required. Verified public research helps current topics; approved read-only GitHub access helps inspect actual project code; a **private** notes/Notion ledger can keep editorial history; authorized analytics can support better learning. Configure permissions outside this repo. See [integrations guide](integrations/README.md).

## Privacy and quality

This repository contains only reusable skills, instructions, examples, source methods, and validation code. **Finished posts, editorial drafts, private work, raw analytics and generated weekly reports must not be committed here**, even on PR branches. The guard in [scripts/validate_public_repo.py](scripts/validate_public_repo.py) checks file layout and links.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Released under the [MIT License](LICENSE).

## Skills.sh distribution

The skill uses the open [Agent Skills format](https://agentskills.io/specification) and is installable with the community [skills CLI](https://github.com/vercel-labs/skills). There is no separate publish command; public discovery on skills.sh may depend on successful installations and indexing, and is **not guaranteed by a GitHub merge**.

---

*Research-first, useful before viral, written like someone who means it.*
