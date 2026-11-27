# Worked examples — illustrative, not published

These are deliberately generic synthetic scenarios demonstrating routing and gate decisions, not the author's experiences and not real engagement statistics.

## Example A: headless commerce
Input: A frontend engineer can build a custom storefront while a commerce platform manages catalog and orders.
Reader: small-team frontend engineers deciding what they must implement.
Insight: own the customer experience without rebuilding commodity commerce operations, but checkout, auth and API security remain engineering work.
Evidence needed: actual platform docs and a real screenshot before making first-person implementation claims.
LinkedIn: ADAPT until proof; can be a practical demo with real image.
X: PUBLISH as a general technical distinction, no personal impact claim.
Blog: HOLD for a documented system diagram and integration failure modes.
Sample opening: "A custom storefront doesn't require a custom order-management backend. But headless doesn't eliminate integration and checkout engineering."
Tags: none; merely discussing a vendor doesn't justify @mentioning it.

## Example B: new agent runtime release
Input: A vendor reports lower workflow orchestration overhead.
Reader: engineers running retries and long-lived processes.
Reader problem: a retried side effect might execute twice; performance alone isn't reliability.
Evidence needed: original release notes plus small mock retry/idempotency example.
LinkedIn: HOLD until the example is available.
X: ADAPT to an attributed, technically accurate observation.
Blog: HOLD until reproducible experiment and meaningful trade-offs.
Sample opening: "Retries are cheap for a read. For payment or order side effects, they need explicit idempotency."
Tags: none, unless actual collaborators should be credited.

## Public samples
Examples above demonstrate the algorithm without exposing unpublished work. Link only to **verified, already published** examples when permission and permanent URLs are available. The installed skill does not ship user-specific drafts and must not invent live post URLs.
