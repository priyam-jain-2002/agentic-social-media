# Weekly editorial operating rhythm

**Goal:** maintain a fresh, evidence-based pool of useful ideas without becoming a generic technology-news repost account.

## Two input streams
```
                     PUBLIC SIGNALS                  FIRSTHAND WORK
                news / papers / releases     commits / decisions / users / bugs
                         |                               |
                  weekly topic radar              insight extraction
                         |                               |
                         +-----------> IDEA BACKLOG <----+
                                            |
                              source/novelty/reader gates
                                            |
                                small experiment or proof
                                            |
                         platform routing -> writing -> QA
                                            |
                                explicit approval only
                                            |
                                    publish -> review
```

## Suggested schedule (Asia/Kolkata)
- **Monday morning:** public-source scan for prior 7 days, surface 3–5 candidates, label contradictions and stale items. This is the only scheduled content task; no blind publication.
- **Wednesday:** select one idea that can be supported through a screenshot, tiny benchmark, repo example or specific external argument. User may drop raw first-hand notes at any time.
- **Thursday/Friday:** approve one high-quality LinkedIn post if READY; only then adapt for X; blog only after evidence warrants a durable article.
- **72 hours / 7 days after publication:** collect results and write a learning note, without pretending small samples prove causation.

## Operational loop
1. Read [AGENTS.md](AGENTS.md), [skills/topic-radar/SKILL.md](skills/topic-radar/SKILL.md) and [sources/RADAR.md](sources/RADAR.md).
2. Current news scan -> a dated [weekly research record](templates/weekly-topic-radar.md) **returned in chat or stored privately outside this repository**; no invented 'this week' sources.
3. Review [insight card](templates/insight-card.md) submissions from actual work **privately**; confidentiality first.
4. Pick **one reader problem, one source-backed claim, one proof**. A weekly radar link alone does not pass the originality gate.
5. Apply [idea intake](skills/idea-intake/SKILL.md), [research](skills/research/SKILL.md), [discovery](skills/discoverability/SKILL.md), [packaging](skills/packaging/SKILL.md), and [editorial gates](skills/editorial-gates/SKILL.md).
6. Suggest platform-native angles; `SKIP` is a success when the audience doesn't fit.
7. Ask user to explicitly approve final copy and image before publishing. Never auto-post.

## Quality / business outcomes
North star: number of **original, credible, genuinely useful posts** generating qualified engineering or founder conversations, not raw likes. Supporting indicators: 3–5 verified candidates/week, at least one proof-backed draft when possible, meaningful audience replies, bookmarks/reposts, demos/read-throughs and consistency of claimed technical identity. Review after 6–8 weeks.

## Automation boundary
- A recurring ChatGPT task can send the weekly digest. **It does not automatically commit Markdown back into GitHub, run code, or publish social posts.** A connected agent may store reviewed topic cards only in a **separate, explicitly approved private destination**—never in this public framework repository.
- This public repository is a reusable ruleset and source manifest; use a private location for sensitive project notes and raw analytics.
- If an automation is unavailable, run the same prompt manually:
  > Read https://github.com/priyam-jain-2002/agentic-social-media/AGENTS.md and skills/topic-radar/SKILL.md; research the past 7 days using sources/RADAR.md; return 3–5 verified topics with reader problem, novel angle, experiment, source/date and independent LinkedIn/X/blog fit. No drafts or posts unless selected.
