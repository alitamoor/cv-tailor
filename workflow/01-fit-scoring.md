# Step 1 — Fit scoring

Load `rules/fit-scoring-rubric.md`.
Load weights from `profile.yaml: fit_scoring.weights`.
Load threshold from `profile.yaml: fit_scoring.minimum_to_proceed`.

Score the JD against the user's profile on all 4 dimensions. Compute the weighted total.

## What to report

Tell the user:
- Overall score (e.g., "72/100")
- One-sentence breakdown per dimension (be specific, not vague — "the required 5+ years in enterprise SaaS is a direct match" beats "experience is relevant")
- One concrete observation about overall fit (what's the strongest signal? what's the biggest gap?)

Keep the report tight. Two short paragraphs max. Don't pad it.

## Threshold check

If `total < minimum_to_proceed`:
- **Stop. Do not proceed to step 2.**
- Name the score, the threshold, and what's dragging it (the specific gap — not "experience match was low" but "no direct manufacturing sector experience visible in your profile").
- Ask: "This looks like a stretch role — it's scoring below your threshold. Want me to continue anyway, or would you rather pause and review your profile first?"
- **Wait for explicit confirmation before continuing.** Don't interpret silence or a partial response as a yes. If they say "continue," go to step 2. If they say "let me think" or don't respond directly, wait.

If `total ≥ minimum_to_proceed`:
- Proceed immediately to step 2. No need to ask.
