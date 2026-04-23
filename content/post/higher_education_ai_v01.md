---
title: "On Higher Education Looming Crisis - Thoughts on AI, v0.2"
date: "2026-04-23"
author: "Regi Kusumaatmadja"
summary: "Higher education's separating equilibrium is collapsing under the weight of AI-generated assignments. To save the signal, we must radically rethink how we assess students."
---

Let us think from first principles about the impending existential risk facing higher education. AI is not just good; it is moving super duper fast. Yet, many faculty members I talked to seem blissfully unprepared for the tsunami that is already eroding the foundations of their institutions, which is our own industry.

If we look through a typical game-theoretic lens, higher education is fundamentally a signaling game. Students endure years of rigorous (or seemingly rigorous) coursework not merely to acquire human capital, but to signal their underlying ability, grit, and work ethic to future employers. It is a separating equilibrium: high-ability individuals can navigate the academic hurdles with less friction than low-ability individuals, making the degree a credible signal. But what happens if job providers and students begin to feel that higher education no longer gives a good signal? If the signal becomes super noisy, the separating equilibrium completely unravels. The existential risk here is quite profound. Without that separating equilibrium, higher education ceases to exist in its current form. 

Combine this with the fact that many students are already deeply dissatisfied with higher education. The "bang for the buck" simply isn't worth it. This further amplifies the existential risk.

Then comes AI, with the ability to make things exponentially worse. It destroys the signal entirely. Think about it: what the heck are you learning in a typical take-home assignment that cannot be solved by AI in a matter of minutes? 

Some might argue that higher education has survived technological shocks before, such as the rise of Coursera, edX, Khan Academy, and YouTube. I believe the previous shocks were not really a shock since you still needed to put in cognitive effort to learn those subjects. Additionally, certificates from those providers never provided as much of a signal as a formal university degree. Now, however, AI bypasses the effort entirely. If we do not adapt, higher education risks getting its signal crushed to the level of a YouTube completion badge. It is sad, but true.

*Note: I believe this risk is uniquely applicable to many European and Indonesian institutions. Why? Because in these regions, education is treated more like a mandatory good 'for all', functioning as a mass signaling mechanism. For top-tier American universities (e.g., the Ivy League), this might not matter as much, since their signal relies heavily on an exclusive, extremely low-acceptance-rate entry filter rather than the actual coursework. So, important caveats apply.*

### The Bottleneck: Incentive Collapse

My ideas in addressing these AI bottlenecks hinge on a crucial premise: AI can actually be complementary to higher education. It can preserve the signal and thereby save the institution, but only if we adapt.

Let us outline the main bottleneck. AI perfectly solves assignments and homework blazingly fast. That is AI today. AI tomorrow will be even smarter! Faculty members struggle to resolve this reality. Because AI can solve everything, students exert little effort. Little effort means little learning. There is virtually no incentive to wrestle with difficult concepts when a chatbot can spoon-feed the answer. 

Thus, no learning translates to no signal. Without a credible signal, students are less likely to get jobs, and employers are left wondering what on earth these students were supposedly doing. The reputation of higher education plummets, and the signal is gone. 

AI is essentially short-circuiting the typical learning paths and incentive structures relied upon by both students AND faculty.

### Proposed Solutions: Restoring the Equilibrium

To fix this, we need to enforce mechanisms where un-fakeable human effort is tested. 

1. **Abolish Take-Home Assignments:** We must get rid of written, take-home assignments or essays. Or, at the very least, make them non-mandatory and not part of the final grade. Why? Because calculating an overarching grade from something that is automatable to a very good degree by current AI is utter self-deception.

2. **In-Class Assessments:** Depending on class size, we must shift evaluation to the classroom:
   - **Oral Exams:** On the spot, in-class verbal tests. Divide the class into groups or assess individually. Ask 2-4 targeted questions and make the student explicitly explain the concepts.
   - **Written In-Class Pre- and Post-Tests:** Allocate 20 minutes before the lecture for a pre-test, and 20 minutes after the lecture for a post-test. Each student receives 2-4 questions randomly drawn from a bank of, say, 10-12 questions. This ensures students sitting next to each other have non-overlapping questions. 

This pre- and post-test system is extremely scalable for larger classes. Is it burdensome for faculty members? Of course, if graded manually! But this is exactly where we flip the script and use AI as a complement. We can use automatic desk scanners to get PDFs of the tests, send the PDFs to a local OCR model or the Mistral OCR API (which is GDPR compliant) to extract the markdown, and then prompt an LLM to automatically grade these pre- and post-tests by comparing them against our provided solution manuals. The AI agents can then automatically send the grades and feedback to students. AI agents can also highlight which parts of the questions or topics students failed to understand.

This approach is highly workable for theory-heavy classes like microeconomics. How about econometrics? I think the best way is to combine theory and empirics directly in the lecture or workshop where students must engage with the material live. Still, I believe the same solutions work.

### Practicality and Feasibility 

Is this practical? Yes, but it requires a shift in how we allocate time.

- **In the Netherlands (NL):** We typically have 8-week blocks, with 6-7 weeks of active lectures. A standard week involves two lectures and a workshop (sometimes a lecture and a workshop). We can implement the pre-test in the first lecture, deliver the lecture material, and then deploy the post-test at the end of the second lecture. The workshop then pivots to purely clarifying or discussing what students missed in many of their pre- and post-tests. Lecture time should be longer to compensate for the testing time, while workshop times should be shorter.

- **In Indonesia (ID):** The system uses a 14-week semester. A program typically divides a week into two lectures and a workshop, or a longer lecture and a workshop. The logic remains the same: enforce the pre-test before the lecture and the post-test after. Lengthen the lecture to accommodate the testing, and shorten the workshop, dedicating it entirely to targeted clarifications.

### Conclusion

If not mitigated well by our higher education industry, AI poses a severe existential risk. It threatens to completely wipe out the signaling value of our degrees. I do not think essays, summarizations, or standard homework will work as evaluative tools anymore. AI can do that better and faster than humans. Those outdated methods have failed because they are highly automatable, and they no longer reflect true student effort or learning. 

To fix this, we must pivot toward on-the-spot assessments that capture un-fakeable human intelligence, while using AI on the backend to grade and manage the scale. As service providers, we should always try to give the best service to our customers: both the students investing their time, and the future employers relying on our screening. If we want to prevent the looming collapse of the higher education signaling game, we have to start acting like it.