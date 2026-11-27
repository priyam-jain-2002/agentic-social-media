# Evidence base and research protocol

Last checked: 2026-11-27. This is **editorial evidence**, not a list of guaranteed ranking tricks. Recheck external pages and publication dates before claiming current rules.

## First-party / primary sources
1. [LinkedIn Engineering — Engineering the next generation of LinkedIn's Feed (2026-03-12)](https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed). Describes sequence-based Generative Recommenders and interest-relevance modeling. **Supports:** audience/topic relevance. **Does not establish:** a precise optimal word count, hashtag count, image format or a reach guarantee.
2. [LinkedIn News — Improving the Feed (2026)](https://news.linkedin.com/2026/ImprovingTheFeed). Explains prioritization of relevant, authentic professional content and quality controls. **Supports:** authenticity and professional relevance.
3. [LinkedIn Engineering — Leveraging dwell time](https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed). Studies short dwell as a negative signal; **supports:** useful opening and readability as editorial hypotheses, not clickbait or a quantified '2-second rule'.
4. [X — For You timeline](https://help.x.com/en/using-x/x-timeline). Recommends based on interests and engagement history. **Supports:** reader and conversation fit.
5. [X — Conversations and reply ranking](https://help.x.com/en/using-x/x-conversations). Reply visibility depends on relevance and relationship among other signals. **Supports:** substantive conversation, not fake engagement.
6. [X — Limits on reach](https://help.x.com/en/rules-and-policies/x-reach-limited). Behavior and safety signals affect distribution.
7. [xAI open-source x-algorithm](https://github.com/xai-org/x-algorithm). Public code offers partial insight into current recommendation implementation; validate repository state/date before interpreting. Not a deterministic playbook or guarantee.
8. [Google Search Central — Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Prioritizes original experience, satisfying information, accuracy and trust.
9. [Google Search Central — AI search optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). Recommends useful non-commodity content; SEO fundamentals still apply.
10. [Google Search Central — SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). Supports descriptive titles, technical indexability and human-useful organization.

## Directly checked discoverability and mentions documentation
- [LinkedIn feed Q&A by Gyanda Sachdeva (Dec 2025)](https://www.linkedin.com/pulse/top-linkedin-feed-questions-2025-gyanda-sachdeva-anl2e/): "Hashtags do not impact distribution". This is a first-party statement about LinkedIn's feed, not proof hashtags lack all search/discovery or organizational utility.
- [LinkedIn Help: mentions](https://www.linkedin.com/help/linkedin/answer/a525082/mention-people-in-your-posts): select real accounts in the suggestions list; typed @names are not a verified live tag.
- [LinkedIn Help: mentions, tags and collaborations settings](https://www.linkedin.com/help/linkedin/answer/a522861): account settings may affect whether a member can be mentioned or collaborate.
- [X Help: how to use hashtags](https://help.x.com/en/using-x/how-to-use-hashtags): hashtags help categorize and be discoverable in X search; X recommends no more than two.
- [X Authenticity policy](https://help.x.com/en/rules-and-policies/authenticity): prohibits trending-hashtag abuse or coordinated inauthentic engagement.
- [Google Search: article structured data](https://developers.google.com/search/docs/appearance/structured-data/article): use valid, accurately implemented structured data where appropriate.

## What we can / cannot conclude
- **Reasonably grounded:** relevance to readers, authentic expertise, useful originals, specific evidence and trust matter.
- **Authorial experiments, not platform directives:** 80–140 word LinkedIn starting range; hook in first two lines; 0–3 hashtags; infographic minimalism; 72h analysis; selective cross-posting.
- **Not established:** 'image posts always win', 'external links always get penalized', 'a specific posting hour guarantees reach', 'the algorithm loves one-line paragraphs', or '3 hashtags outperform 4'.
- **Avoid cherry-picking:** public viral post screenshots have survivor bias. Compare a cohort of posts from creators with similar follower levels and topics, include misses, and document denominators, dates, and attribution. If this dataset has not been gathered, say so. This repository is grounded primarily in public platform guidance plus the author's observed post results, **not** a verified dataset of top-performing small creators.
- **No false causal inference:** low impressions could reflect distribution; low interaction rate could reflect topic/audience/proof/packaging. No single post isolates causality.

## Future research backlog
- Build a consent- and rights-respecting comparison set: 20–30 comparable creators per platform in AI/product engineering and founder-operator niches, ~5–10 posts each, including low-performing posts. Record follower counts, post age, impressions if visible, engagements, hook, proof type, content length, visual type, source link and notes. **Do not fabricate invisible impressions or claim these samples are representative.**
- Extract only patterns that survive within-account comparisons; record uncertainty and seasonality.
- Periodically re-audit changing platform UI/features and algorithm statements.

## Personal observations to test, not generalize
- Prior professional/event posts and practical tooling posts showed stronger impressions than two thesis-first posts. The latter lacked an immediately inspectable artifact and delayed a clear reader payoff. This is a plausible editorial diagnosis, not proof of feed suppression.
- Track results with [analytics skill](../skills/analytics/SKILL.md); never encode user metrics as guaranteed benchmarks.
