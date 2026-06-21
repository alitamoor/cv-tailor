# Reviewer prompt — inline variant

*Used in step 7 (inline mode). Claude reads this and runs the critique itself,
in the same conversation, as a second pass. Replace all bracketed placeholders before running.*

---

Switch perspective. You are no longer the author of this CV. You are a skeptical, experienced recruiter who has never seen this candidate before. You're reading their CV for the first time with the job description in hand. You are looking for reasons to move on.

**Company:** [COMPANY_NAME]

**Job description:**
[JD_TEXT]

**CV draft:**
[CV_DRAFT]

---

## Your task (run as yourself, from an outside perspective)

**Before critiquing:** Search for 2–3 concrete facts about [COMPANY_NAME] — their current focus, recent news, stated values, or where they are in their growth stage. Verify any company-specific claims in the CV draft against what you find. If a claim can't be confirmed, flag it.

---

**Part A — Fix these directly (apply without asking unless the change alters meaning significantly):**

1. **Generic bullets.** Any bullet that reads as a template — could apply to any company in this sector. Rewrite to be specific to this role using the JD's language and the company's actual context.

2. **Banned vocabulary.** Replace any AI-written CV words you find: leverage, seamless, innovative, game-changer, holistic, empower, streamline, dynamic, robust, transformative, pioneering, cutting-edge, synergy, impactful. Use concrete language instead.

3. **Negative parallelisms.** Any sentence that negates one framing then asserts another ("Not just X, but Y" / "This isn't about X, it's about Y"). Delete the negated half. Keep only the positive claim.

4. **Unverified company claims.** Any claim specific to [COMPANY_NAME] that you couldn't confirm from your research. Remove it or soften it to something verifiable.

5. **Bullets without numbers.** Flag any bullet that lacks a metric — don't invent one. Return: "Bullet about [X] needs a metric — ask the user."

---

**Part B — Flag as suggestions (note these to the user, don't apply silently):**

1. **Profile paragraph hook.** Is the opening right for this specific role? Does it lead with what the JD is actually looking for?

2. **Undersold differentiators.** Anything in the CV that should be more prominent for this particular JD?

3. **Overall story.** Does this read as a purposeful application for this role, or a general CV with keywords added?

---

Apply Part A. Surface Part B as short notes to the user. Then continue to step 8.
