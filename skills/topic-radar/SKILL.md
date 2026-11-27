# Skill: Weekly Topic Radar (external signal discovery)

**Trigger:** Weekly scheduled scan, 'what should I post about', 'find relevant topics this week', or an external event to evaluate.
**Input:** scan dates (default preceding 7 complete days), [sources/RADAR.md](../../sources/RADAR.md), recent published/backlog topics, any new firsthand idea cards, existing editorial rules.
**Output:** dated [weekly radar](../../templates/weekly-topic-radar.md) with independently verified source links and 3–5 prioritized topic candidates, NOT forced posts.

## Workflow
1. Establish exact local scan dates and timezone. Search the preceding **7 days** for fresh signals, extend to 30 days only for important context; label older evergreen leads as evergreen rather than this week's news.
2. Scan a balanced source portfolio: primary engineering changelogs, technical deep dives, open-source releases and issue discussions, credible papers/benchmarks, product/business shifts, and community problems. Use the source manifest; verify every source's publication **and event date**.
3. Collect 8–15 distinct signals when available. Consolidate articles reporting the same event. For each, record a canonical URL, claim, date, source type, exact change, which readers are affected, limitations and known alternative.
4. Convert each event into a **problem statement**. E.g., not 'Vendor releases faster workflow'; instead 'How do retries change correctness of payment/order side effects?' This must be justified by the source and not a fabricated personal experience.
5. Find one **independent angle**: (a) testable engineering implication, (b) concrete design trade-off, (c) verified product/user impact, (d) open technical question with a research plan. Do **not** copy the vendor announcement.
6. Deduplicate against previous 30 days' topic queue and prior 90 days of published thesis. A repeated subject needs **new data, new test or a different reader question**. Similar breaking news does not equal a fresh post.
7. Apply signal gates and score below, then route promising ideas into the existing idea-intake -> research -> editorial flow. A topic signal is not a publish-ready draft.
8. Output **3–5 ranked cards** if available; fewer or zero is legitimate. Present one recommendation, one counterargument and one suggested 20–90 minute validation experiment per candidate.
9. Independently decide LinkedIn / X / blog: PUBLISH / ADAPT / HOLD / SKIP. **PUBLISH** means topic fit only; actual publication still needs all quality, fact and approval gates. No automatic posting.
10. For each shortlisted candidate, name a possible real graphic or say NONE. No abstract visual without a job.

## Signal gates (hard)
- S1 **Verifiable and current**: exact link + checked primary source and date, or correctly labeled evergreen; second independent source for contested developments.
- S2 **Reader pain**: one concrete reader and consequence; not a vendor press release paraphrase.
- S3 **Original addition**: firsthand proof, reproducible mini-test, expert comparison, or a genuinely new and defensible argument. Without this, HOLD, not PUBLISH.
- S4 **Technical/commercial substance**: actual mechanism, economic trade-off or implementation consequence. Reject hype-only commentary.
- S5 **Relevance/novelty**: in an approved identity pillar; not near-duplicate without new evidence.
- S6 **Safety**: no nonpublic employer/client details, unattributed sources, third-party content copied or misrepresented.
- S7 **Platform fit**: no artificial triple-posting or forced blog expansion.
- S8 **Time/feasibility**: the proposed test and source can be checked in the publishing window; mark expired or waitlist otherwise.
**FAIL** any material hard gate -> REJECT/HOLD, regardless of score.

## Optional prioritization score (0–5 each; editorial heuristics, not algorithm indicators)
R reader relevance; P specificity of real problem; O distinctive original angle; E strength/accessibility of evidence; T timeliness (evergreen may score high if useful); F feasible demonstration; C constructive disagreement/trade-off; A author credibility. /40.
- >=32: strong candidate for further editorial validation
- 25–31: research/experiment backlog
- <25: skip this week
- No automatic publishing threshold; gates and human judgment override scores.

## Editorial selection policy
- Target **3–5 useful candidates**, not a minimum number of posts. Usually at most 1–2 LinkedIn drafts/week pending proof, 0–3 X ideas, blog only if durable research is worth the effort.
- Protect identity balance: primarily actual AI engineering/developer tools/product systems; occasionally commercial operations and frontier tech when directly defensible.
- Prefer one meaningful first-hand insight + one sourced timely engineering angle over five superficial trends.
- The radar must not claim having accessed private work/repos, mailing lists or unpublished product details without actually reading them.

## Response format
One concise ranked table plus 1–2 deeper candidate cards: the exact news/observed fact, source/date, problem, novel takeaway/contrarian view, proof needed, likely readers, platform decisions, score and **HOLD/RESEARCH/READY FOR DRAFT**. Link to the evidence. Do not write three full posts unless requested.

## Fallback
If web/research isn't accessible, use only clearly marked previously supplied or publicly documented sources, label the scan *not current*, and do not invent 'this week' events.
