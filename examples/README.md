# Examples: from one idea to a platform decision

These are **illustrative, synthetic examples** designed to show how the framework responds, not the maintainer's unpublished drafts, not posts published to real accounts, and not evidence of performance.

The installable skill ships equivalent examples in [its self-contained reference](../skills/agentic-social-media/references/examples.md).

## Sample 1 — A frontend engineer chooses headless commerce

**Raw input:** "A frontend developer can deliver a fully custom storefront without maintaining a custom order/catalog backend."

**Gate finding:** The word *fully* overstates checkout and integration freedom. The useful observation is selecting which backend responsibilities to own, not eliminating all backend work.

| Platform | Verdict | Why |
| --- | --- | --- |
| LinkedIn | ADAPT | Show an actual storefront demo/screenshot and explain boundaries |
| X | PUBLISH | A concise technical distinction stands alone |
| Blog | HOLD | Needs a real architecture walkthrough, code-level integration details, trade-offs |

**LinkedIn opening example (not a finished post):**

> You can customize the entire storefront experience without building an order-management system. But headless commerce doesn't eliminate backend engineering—it changes which parts you own.

**X example (not a live post):**

> Headless commerce lets a frontend team own the storefront while a platform manages catalog and orders. Auth, checkout constraints, API security and failure handling still need engineering. It’s a boundary decision, not “no backend.”

**Blog outline:** What the team owned, catalog/order API boundaries, checkout/security, failure modes, deployment constraints, actual screenshots and what they would do differently.

**Tags:** zero until a specific community or verified collaborator makes one genuinely useful.

## Sample 2 — A performance release invites a correctness question

**Raw input:** "A workflow engine's orchestration overhead dropped."

**Gate finding:** A vendor's faster-workflow claim is neither an independent measurement nor a reason to publish a recap. A useful angle is how retry behavior interacts with external side effects.

| Platform | Verdict | Why |
| --- | --- | --- |
| LinkedIn | HOLD | Needs a tiny reproducible idempotency example |
| X | ADAPT | A sourced, accurate warning can be useful to operators |
| Blog | HOLD | Needs a test harness, traces and caveats, not padded news |

**Sample opening (not a finished post):**

> Retries are cheap when a step only reads data. When it calls a payment or order API, idempotency becomes part of correctness.

**Suggested proof:** Demonstrate duplicate calls from a retried mock external service, then show safe idempotency with a stable operation key. Do not imply the test was run until it actually is.

## Links to real published posts

We deliberately **do not invent public LinkedIn/X URLs** or republish personal drafts as examples. Verified public posts can be linked here in a future change, with the creator's permission and correct attribution. Until then, the linked examples above are usable, transparent demonstrations.

For real source material, [public primary-source research guidance](../sources/RADAR.md) lists original engineering articles, release notes and technical projects; they are research inputs, **not** claimed outputs of this skill.
