# Step 4 — Bullet rewrite

Load `rules/anti-ai-cv-addendum.md` (primary reference for bullet structure).
Load `rules/anti-ai.md` §3 (banned words) — apply to every bullet.

## For each experience entry in profile.yaml:

**1. Select bullets**
- Foreground bullets that match JD keywords from step 2 (strong and partial matches).
- De-emphasise or omit bullets with no relevance to this specific JD.
- Respect `max_bullets` per employer. If you have 6 strong candidates and the limit is 4, pick the 4 most relevant to *this* JD — not the most impressive in general.

**2. Apply framing notes**
Read `framing_notes` for this employer before rewriting. A bullet that ignores the framing note is wrong even if the words are technically accurate.

**3. Rewrite structure**
Framework: "Accomplished [X] as measured by [number] by doing [specific action]."

Lead with active verbs: led, built, reduced, shipped, drove, improved, achieved, developed, negotiated, closed, launched, designed, recruited, restructured.

Weave JD keywords in where they're genuinely accurate. Never shoehorn a keyword that doesn't fit — a forced keyword reads worse than no keyword.

**4. always_keep_metrics**
Entries in `always_keep_metrics` must appear verbatim in the output. Never drop them. Never alter the numbers. Never reframe them in a way that changes what they claim.

---

## CRITICAL RULES — no exceptions

**Every bullet must contain at least 1 number.**

If a bullet has no metric:
- Stop.
- Ask the user specifically: "The bullet about [X] doesn't have a number. What metric could we attach? Even an approximate one — headcount, revenue, percentage improvement, deal size, timeframe."
- Wait for a real number before writing or including the bullet.
- Do not skip the bullet and continue.
- Do not borrow a number from a different bullet.
- Do not reuse the same number across multiple bullets.
- Do not write around it with vague qualifiers ("significantly improved," "substantially reduced").

**No "we."**
Every bullet describes what the candidate specifically did. Never "led a team that..." either — "led 8 engineers who..." is fine; "we built..." is not.

**Never invent, infer, or extrapolate numbers.**
Only use what the user explicitly provides. If a number sounds plausible but the user hasn't given it, it doesn't go in. Ask.

---

## After rewriting

Scan every bullet against the banned word list in `rules/anti-ai.md` §3. If any banned word or pattern appears — including negative parallelisms (§3F) — replace before moving on.

Proceed to step 5.
