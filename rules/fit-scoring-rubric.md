# Fit scoring rubric

Four dimensions. Weighted total. Score before writing anything.

## Dimensions and default weights

Default weights are set in `profile.yaml: fit_scoring.weights`. Users can adjust them.

| Dimension | Default weight | What it measures |
|---|---|---|
| Skills match | 40% | Direct overlap between JD-required skills/tools and what's documented in `profile.yaml` |
| Experience match | 30% | Relevance of past roles, industries, and seniority level to the JD |
| Culture fit | 15% | Alignment between the user's behavioral tone profile and the company's signals (stage, pace, values) |
| Career alignment | 15% | Whether this role is a plausible next step in the direction the user is heading |

## Scoring per dimension (0–100 each)

**Skills match:**
- 90–100: 80%+ of required skills are documented in the profile, including the top 3–5 non-negotiables
- 70–89: Most required skills present; 1–2 non-negotiable gaps
- 50–69: Core skills present but several secondary requirements missing or only partially met
- 30–49: Some relevant skills; material gaps in the primary requirements
- 0–29: Minimal overlap

**Experience match:**
- 90–100: Prior roles in the same industry, comparable scope, appropriate seniority level
- 70–89: Related industry or slightly different level; story is coherent
- 50–69: Transferable experience but requires extrapolation; hiring manager will need to see the connection
- 30–49: Adjacent background — possible with strong framing, not obvious from the CV alone
- 0–29: Little direct experience; this is a significant pivot

**Culture fit:**
- 90–100: Strong match between tone profile and company signals (e.g., the user is a builder, the company is Series B, the JD says "hands-on"); or no strong culture signals to conflict with
- 70–89: Minor friction (e.g., user prefers autonomy, JD says "collaborative team environment") — manageable
- 50–69: Some tension (e.g., user has enterprise background, company is early-stage, JD reads like they want a founder-type)
- 0–49: Clear mismatch — note it explicitly when flagging to the user

**Career alignment:**
- 90–100: Role is a natural step in the direction `profile.yaml: person.target_role_family` points
- 70–89: Close to target; minor deviation
- 50–69: Off the stated path but not contradictory — the user may have a reason
- 0–49: The role goes against the direction the user has indicated they're heading

## Weighted total

```
total = (skills × skills_weight/100)
      + (experience × experience_weight/100)
      + (culture × culture_weight/100)
      + (career × career_weight/100)
```

Example with default weights:
```
total = (skills × 0.40) + (experience × 0.30) + (culture × 0.15) + (career × 0.15)
```

## Threshold

If `total < profile.yaml: fit_scoring.minimum_to_proceed` (default: 55):
- **Stop. Do not proceed.**
- Report the score, per-dimension breakdown, and what's dragging it down.
- Ask: "This looks like a stretch role. Want me to continue anyway, or would you rather review your profile first?"
- Wait for an explicit "yes, continue" before proceeding. Don't auto-continue.

If `total ≥ minimum_to_proceed`: proceed to step 2 without asking.
