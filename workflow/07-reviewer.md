# Step 7 — Reviewer pass

This step branches on `profile.yaml: environment.mode` (or the detected mode from SKILL.md).

---

## Agent mode — spawn general-purpose agent

1. Fill the template in `reviewer/reviewer-prompt-agent.md`:
   - Replace `[COMPANY_NAME]` with the company name from the JD.
   - Replace `[JD_TEXT]` with the full JD text.
   - Replace `[CV_DRAFT]` with the rewritten CV content from steps 4–5.

2. Spawn a `general-purpose` agent with the filled prompt.

3. When the agent returns:
   - **Part A edits (must-fix):** apply directly, without asking. These are objectively fixable — generic language, banned words, unverified claims.
   - **Part B edits (judgment calls):** apply with a brief note explaining what you changed and why. If a suggestion would significantly alter meaning or framing, flag it to the user instead of applying silently.
   - For any company-specific claim the reviewer flagged as unverified: fetch the company's website or recent news before including it. If you can't verify it, remove it.

---

## Inline mode — self-critique

1. Fill the template in `reviewer/reviewer-prompt-inline.md`:
   - Replace `[COMPANY_NAME]`, `[JD_TEXT]`, `[CV_DRAFT]` as above.

2. Run the critique yourself. Switch perspective — you are no longer the author. Read the CV as a skeptical recruiter seeing it for the first time with the JD in hand.

3. Use web search to find 2–3 facts about the company before critiquing. Verify any company-specific claims in the draft.

4. Apply corrections the same way as agent mode: Part A directly, Part B with a note.

---

Proceed to step 8 after applying reviewer changes.
