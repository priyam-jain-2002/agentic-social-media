# Weekly radar source policy and watchlist

Sources below are **monitoring inputs**, not automatic endorsements. Website feeds/pages may move; re-verify URLs, publication dates and applicable terms on every scan.

## Tier 1 — preferred primary sources
| Pillar / reader | Sources to check | Signals worth exploring |
| --- | --- | --- |
| Agent engineering / reliability | [OpenAI Developers changelog](https://developers.openai.com/api/docs/changelog), [OpenAI engineering](https://openai.com/research/), [Anthropic engineering](https://www.anthropic.com/engineering), [GitHub Changelog](https://github.blog/changelog/) | durable state, retries, evals, failure modes, observability, context portability, tool security |
| Open-source AI / inference | [Hugging Face Blog](https://huggingface.co/blog), [PyTorch Blog](https://pytorch.org/blog/), [vLLM releases](https://github.com/vllm-project/vllm/releases), [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases) | model serving correctness, model/agent/harness portability, profiling, production benchmarks |
| Infra / application runtime | [Cloudflare Blog](https://blog.cloudflare.com/), [Vercel Changelog](https://vercel.com/changelog), [Kubernetes Blog](https://kubernetes.io/blog/), [CNCF](https://www.cncf.io/blog/) | resilience, deployment safety, inference cost, edge trade-offs, emerging standards |
| Frontend / product engineering | [web.dev](https://web.dev/blog), [Next.js blog](https://nextjs.org/blog), [GitHub engineering](https://github.blog/engineering/) | practical frontend architecture, UX/perf, AI developer tooling |
| Commerce / B2B product | [Shopify developer changelog](https://shopify.dev/changelog), [Wix developers](https://dev.wix.com/docs), [Google Search Central](https://developers.google.com/search/blog) | headless commerce, product discovery, procurement UX, agent-search answerability, practical SEO |
| Security / standards | [CISA advisories](https://www.cisa.gov/news-events/alerts), [IETF RFCs](https://www.rfc-editor.org/), [OWASP](https://owasp.org/) | actionable deployment and agent security implications |

## Tier 2 — corroboration and real problems
- [arXiv recent CS](https://arxiv.org/list/cs/recent) and cited peer-reviewed work (evaluate methodology, date, benchmarks and bias).
- [Hacker News](https://news.ycombinator.com/) and relevant [Reddit](https://www.reddit.com/) discussions for **user pain, criticism and counterexamples**, not factual confirmation.
- Maintainer release notes, GitHub issues and credible reproduction repos; track actual versions and open issues.
- Founder/operator field reports with concrete implementation and constraints, marked anecdotal.

## Tier 3 — weak signals only
Viral tweets, startup hype, unsourced charts, rumor accounts, promotional newsletters and press releases without technical detail. They can prompt investigation but cannot stand as final evidence.

## Topic coverage weights (editorial starting point, not algorithm)
- 35% production AI systems: evals, tracing, tool calling, retries, infrastructure, models.
- 25% developer productivity: agents, context/skill portability, open-source practices, CI.
- 20% product/UX/full-stack: custom frontends, managed backends, answerability, distribution.
- 15% business/commercial engineering: B2B workflow, economics and usable market gaps.
- 5% frontier exploration: GPU portability, space/ocean extreme reliability **only if proof and relevance clear**.
These are **scanning-effort targets**, not quotas for public posts. Adjust after 6–8 weeks of observed qualified audience engagement.

## Source verification rubric
Record exact URL, publication date, underlying event date, and whether the writer has a direct role or commercial incentive. Seek original technical detail. For 'X is 10x faster', preserve baseline, workload, metric definition and version; do not claim universal performance. For market access or export controls, distinguish proposal, law, enforcement, selected products and geography.
Deduplicate syndicated articles into one event. Don't copy long passages; synthesize and link.
