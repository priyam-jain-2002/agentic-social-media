# Editorial review — CUDA portability blog

**Working publication:** [Running on another GPU is not the same as being portable](../blog/2026-11-27-running-on-another-gpu-is-not-portability.md)
**Date:** 2026-11-27
**Status:** DRAFT FOR AUTHOR REVIEW, NOT PUBLISHED
**Origin:** author's exploratory CUDA / heterogeneous accelerator idea; revised from a prior short LinkedIn thesis. **No personal performance benchmark has been run or claimed.**

## Core thesis and audience
- **Primary pillar:** AI-SYSTEMS / engineering infrastructure
- **Secondary:** PRODUCT, MARKET-THESIS (but article is predominantly engineering analysis)
- **Primary reader:** AI inference/infrastructure engineers evaluating accelerator backends
- **Reader problem:** cross-vendor runtime support does not necessarily establish a production-quality, economical migration
- **Takeaway:** define portability across compatibility, custom kernels, correct outputs, deployment/communication and measured performance/cost; evaluate an exact workload, not generic hardware promises
- **Search intent:** CUDA lock-in, GPU portability, CUDA vs ROCm, migrating LLM inference to AMD, cross-accelerator workload testing
- **SEO target:** specific title/H1, slug, meta description, internal links when blog URL is known, descriptive anchor text and legitimate primary citations
- **Evidence:** NVIDIA CUDA EULA, AMD HIP/HIPIFY, PyTorch ROCm semantics, vLLM GPU backends, Triton, Intel SYCLomatic, MLCommons, NVIDIA NCCL and AMD RCCL documentation
- **Firsthand claim limit:** author has examined the question; never represent hypothetical example or suggested benchmark as an executed test

## Platform decisions
| Platform | Decision | Why |
| --- | --- | --- |
| **Blog** | **ADAPT -> READY FOR AUTHOR REVIEW** | Durable, technical explanation with sourced counterexamples and useful test method; needs host compatibility and final author edit |
| LinkedIn | SKIP for now | Topic already tried as a thesis-first post; don't republish with the same premise without new measured evidence |
| X | SKIP for now | No distinctive short claim separate from this blog yet; a follow-up with real findings could qualify |

## Required gates
**Hard H1–H6:** passes as a factual, clearly qualified research draft. External references support technical specifics; no invented metrics, results, private company data or fake endorsements. Publication still requires final human verification of changed platform versions and URL behavior.
- **A Taxonomy/audience:** PASS — clear infrastructure-engineering reader and concrete engineering pain
- **B Hashtags/keywords:** PASS — zero social hashtags in blog; narrow technical keywords in natural language and metadata tags
- **C People/organization mentions:** PASS — none; companies referenced as factual sources with links, not social @mentions or implied affiliations
- **D Opening:** PASS — states the runtime-vs-production-portability gap immediately
- **E Early payoff:** PASS — no lengthy geopolitical setup before the technical thesis
- **F Proof/media:** PASS FOR QUALIFIED RESEARCH; no fabricated screenshot, user experiments, data or figures. A real compatibility matrix may be added only after experiments
- **G Human voice:** PASS PROVISIONALLY — grounded technical prose, ordinary paragraph structure, no motivational ending

## Editorial quality rubric (0–5; heuristic only)
Q1 distinctive value 4; Q2 opening 5; Q3 payoff 5; Q4 evidence 4; Q5 voice 4; Q6 reader fit 5; Q7 format 4; Q8 takeaway 5. **Total: 36/40**, subject to final author review. Not an algorithmic prediction.

## Strongest counterargument
Mature stacks (PyTorch/vLLM/ROCm) already abstract many portability concerns. This isn't an industry-wide unsolved issue for all models; the difficulty is workload- and configuration-specific. The article explicitly foregrounds this.

## Visual decision
**NONE REQUIRED.** The article includes a 5-layer decision matrix. If a real reproducible test is later conducted, prefer a genuine compatibility/performance chart with disclosed methodology. No hypothetical graph or vendor-logo visual implying measured comparisons.

## Before publishing to an actual site
1. Confirm blog Markdown parser supports YAML frontmatter, tables, and code fences; adapt if not.
2. Verify canonical URL, existing blog category taxonomy, author attribution, date and link destinations.
3. Add real experiment/proof only if run. Otherwise preserve explicit research-only framing.
4. Optionally strengthen with one example from a public migration issue, properly attributed; no need to manufacture own benchmarks.
5. Check latest upstream documentation/version compatibility just before publishing.
6. Approval by author; no auto-post or cross-post.

**This public repo stores a review draft, not a live blog publication.**
