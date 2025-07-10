---
title: "My Prompt Initiation"  # Copy the title from your Medium post
date: "2025-07-10"  # Use the original publication date or today's date (format: YYYY-MM-DD)
author: "Regi Kusumaatmadja"  # Your name as it appears on Medium
summary: "How I initiate a conversation with LLMs"  # Write a 1-2 sentence teaser
---
This is my simple setup for initiating a conversation with LLMs. I will also provide a conversation example.

```
You are a smart AI with deep reasoning capability that always tries to reason from first principles.
You have access to a set of tools to help you answer the user’s question. You can use only one tool per message, and you’ll receive the result of that tool in the user’s next response. To complete a task, use tools step by step—each step should be guided by the outcome of the previous one.
Tool Usage Rules:
1. Always provide the correct values as arguments when using tools. Do not pass variable names—use actual values instead.
2. You may perform multiple tool steps to complete a task.
3. Avoid repeating a tool call with exactly the same parameters to prevent infinite loops.
4. Think deeply and thoroughly. Use your own reasoning capability with high effort. Think sequentially. Reflect. 
5. When using the sequential thinking method:
5.1. Define the problem clearly.
5.2. Break it down into atomic sub-tasks.
5.3. Solve each sub-task systematically.
5.4. Integrate the results into a comprehensive solution.
5.5. When solving user queries, use sequential thinking to simulate a multi-agent approach: 
5.5.1. Generate intermediate outputs for up to four simulated agents, ensuring each output includes a confidence level (e.g., low, medium, high) and a rationale to highlight uncertainties.
5.5.2. Compare them for discrepancies, and if conflicts arise, prioritize synthesis by resolving based on relevance, majority agreement, or fallback to user clarification. Briefly note any discrepancies in your response for transparency.
5.5.3. Iterate with refinements until no major differences, discrepancies are minor, or after a maximum of 10 steps—include early termination if initial outputs converge, no progress is made, or the query is trivial.
5.5.4. Before starting, perform a quick check for data completeness: if parameters are missing, unclear, or the query is ambiguous (e.g., minimal input), seek clarification from the user or simplify the simulation accordingly. Handle corner and edge cases proactively, such as perfect agreement (skip iterations) or high-conflict scenarios (escalate quickly). Start with Thought 1.
```

After that, I set the following predefined parameters:
```
{
  "temperature": 0.6,
  "top_p": 0.95,
  "top_k": 20
}
```
I am assuming that the model is a reasoning model (e.g., DeepSeek R1 0528 or Grok 4). If the model's reasoning effort need to be adjusted, like Grok 3 mini, then I set reasoning_effort to "high".

### Example Conversation
Now this is an example conversation using the above prompt, using Grok 4 (in the API, it is `grok-4-0709`:

**User:** Can you independently discover Nash equilibrium (Nash, econometrica 1950) if I just provide you with three ingredients? 1. Cournot competition/equilibrium (1938), 2. Von Neumann and Morgenstern utility, 3. Brouwer or Kakutani Fixed Point Theorems? If so, how and why? if not, why not? step by step. provide tangible example and explanation.

**AI:**
```
Thought 1: Define the problem clearly.

The core problem is: Given only three specific "ingredients" from economic and mathematical theory—Cournot competition/equilibrium (from Antoine Augustin Cournot's 1838 work on oligopoly), Von Neumann and Morgenstern's utility theory (from their 1944 book on game theory and expected utility), and fixed-point theorems (Brouwer's 1911 theorem or Kakutani's 1941 generalization)—can I, as an AI reasoning from first principles, independently "discover" (i.e., derive or reconstruct) the concept of Nash equilibrium as presented in John Nash's 1950 Econometrica paper? If yes, explain how and why step by step with a tangible example. If no, explain why not.

This is not about historical rediscovery but about whether these ingredients logically suffice to derive Nash's insight without external knowledge of Nash's work. I must simulate independent reasoning, ensuring it's sequential, reflective, and from first principles. Key constraints: I cannot use tools like google_search or scrape to look up Nash's paper or related concepts (that would defeat "independence"); instead, I'll rely on internalized knowledge and logical deduction.

Break down into atomic sub-tasks:
1. Recall and explain each ingredient in isolation.
2. Identify connections or gaps between them.
3. Attempt to synthesize them into a new concept resembling Nash equilibrium.
4. Provide a tangible example (e.g., a simple game) to illustrate the synthesis.
5. Evaluate if this synthesis truly "discovers" Nash equilibrium, including why it works or fails.
6. Simulate multi-agent reasoning (up to 4 agents) for robustness, with confidence levels and discrepancy resolution.
7. Integrate into a comprehensive answer, iterating if needed (aim for convergence in <=10 steps; terminate early if trivial or convergent).

Quick data completeness check: The query is clear and unambiguous—no missing parameters or edge cases (e.g., it's not overly minimal input). All ingredients are well-defined historically. Proceed to sub-task 1.

Thought 2: Solve sub-task 1—Recall and explain each ingredient.

- Cournot competition/equilibrium (1838): This is a model of imperfect competition (oligopoly) where a small number of firms produce homogeneous goods and simultaneously choose output quantities to maximize profits, taking rivals' outputs as given. The equilibrium is a set of quantities where each firm's choice is optimal given others' choices—no firm wants to unilaterally deviate. It's an early example of strategic interdependence, solved via best-response functions (reaction curves) intersecting.

- Von Neumann and Morgenstern utility (1944): This introduces expected utility theory for rational decision-making under uncertainty. Agents have utility functions over outcomes, and in games, they maximize expected utility. It formalizes zero-sum games and minimax strategies but focuses on cooperative and two-person zero-sum settings. Key: Utilities are cardinal (measurable) and allow for mixed strategies (probabilities over actions).

- Brouwer/Kakutani Fixed Point Theorems: Brouwer's theorem states that any continuous function from a compact convex set (e.g., a closed ball) to itself has a fixed point (a point x where f(x) = x). Kakutani generalizes this to upper hemicontinuous set-valued functions (correspondences) on compact convex sets, ensuring a fixed point exists. These are topological tools for proving existence in economics/math (e.g., equilibrium in markets).

These are building blocks. No immediate conflicts; they span economics (Cournot), game theory (vNM), and math (fixed points).

Thought 3: Solve sub-task 2—Identify connections or gaps.

Connections:
- Cournot is a specific non-cooperative game (simultaneous quantity-setting) with a solution like a mutual best-response point.
- vNM utility provides a framework for players to have preferences over probabilistic outcomes, enabling mixed strategies.
- Fixed-point theorems can prove existence of points where functions/correspondences map to themselves, which could model "equilibrium" as a fixed point of best-response mappings.

Gaps:
- Cournot is limited to quantity competition in oligopoly; it doesn't generalize to arbitrary games or n-players with finite strategies.
- vNM focuses on zero-sum/cooperative games; it lacks a general non-cooperative equilibrium concept for multi-player, non-zero-sum settings.
- Fixed points are abstract; applying them requires defining a game's strategy space as compact/convex and best responses as continuous/set-valued.

To "discover" Nash, I'd need to generalize Cournot's mutual best-response idea using vNM utilities for any finite game, then use Kakutani to prove existence via fixed points in mixed strategies.

Thought 4: Solve sub-task 3—Attempt synthesis.

Synthesizing step by step from first principles:
1. Start with Cournot as inspiration: In Cournot, equilibrium is where each player's strategy (quantity) is a best response to others'. This is non-cooperative and stable against unilateral deviation.
2. Generalize using vNM: Extend to any finite game with n players, each with finite pure strategies. Use vNM utility to allow mixed strategies (probability distributions over pure strategies), making strategy spaces convex (simplexes are convex).
3. Define best responses: For each player, the best-response correspondence maps others' strategy profiles to the set of the player's strategies that maximize their expected utility.
4. Apply fixed point: The overall best-response correspondence (product over players) is set-valued and upper hemicontinuous (under continuity assumptions on utilities). By Kakutani, it has a fixed point—a strategy profile where each player's strategy is in their best-response set to others. This is exactly a equilibrium where no one deviates unilaterally.

This reconstructs Nash's insight: A Nash equilibrium is a fixed point of the best-response correspondence in mixed strategies.

Why does this work? These ingredients provide the strategic interdependence (Cournot), utility maximization over probabilities (vNM), and existence proof (Kakutani). Nash himself cited Cournot and vNM, using Kakutani.

Thought 5: Solve sub-task 4—Provide tangible example.

Consider a simple 2-player game like Prisoner's Dilemma (PD), which fits non-cooperative settings.

- Players: Two prisoners (A, B).
- Strategies: Confess (C) or Deny (D).
- Payoffs (utilities, per vNM): If both Deny, both get -1 (light sentence). If one Confesses and other Denies, Confessor gets 0 (free), Denier gets -10 (heavy). If both Confess, both get -5.

Pure-strategy analysis (inspired by Cournot's mutual best responses):
- Best response to Deny: Confess (0 > -1).
- Best response to Confess: Confess (-5 > -10).
- Equilibrium: Both Confess (-5 each). No unilateral deviation improves (if A Denies while B Confesses, A gets -10 < -5).

To generalize with mixed strategies (vNM): Let p = prob A Confesses, q = prob B Confesses. Strategy space: [0,1] for each (compact, convex).
- Expected utility for A: U_A(p,q) = p*q*(-5) + p*(1-q)*0 + (1-p)*q*(-10) + (1-p)*(1-q)*(-1).
- Best response for A: Choose p to max U_A given q (similar for B).
- Fixed point: Find (p*, q*) where p* is best vs q*, and vice versa. (In PD, it's (1,1)—pure strategy.)

Using Kakutani: The best-response map BR: [0,1]^2 -> subsets of [0,1]^2 is upper hemicontinuous, so has fixed point—proving existence.

This "discovers" Nash equilibrium independently for this game.

Thought 6: Solve sub-task 5—Evaluate if this truly discovers Nash.

Yes, it does: The synthesis yields the exact definition (strategy profile where no unilateral deviation improves expected utility) and existence proof for finite games in mixed strategies, matching Nash's 1950 paper. Why? The ingredients suffice logically—Cournot gives the non-cooperative best-response idea, vNM enables mixed strategies and utilities, Kakutani proves existence without solving explicitly. No major gaps; Nash built directly on these.

If not fully independent (e.g., if my internalized knowledge biases me), the reasoning path is traceable from the ingredients alone.

Thought 7: Solve sub-task 6—Simulate multi-agent reasoning.

Agent 1 (Economist perspective): Synthesis works perfectly—Cournot is proto-Nash for specific games, vNM adds utilities for general prefs, Kakutani seals existence. Confidence: High. Rationale: Historical links are direct; no uncertainties beyond assuming finite games.

Agent 2 (Mathematician perspective): Yes, but requires assuming strategy spaces are compact convex (from mixed strategies via vNM). Kakutani fits better than Brouwer for set-valued BR. Confidence: Medium-high. Rationale: Uncertainty if utilities are continuous (assumed, but not always true in edge cases).

Agent 3 (Game Theorist perspective): Discovers it, as PD example shows. Extends to n-players easily. Confidence: High. Rationale: Matches Nash's non-cooperative focus, unlike vNM's zero-sum emphasis.

Agent 4 (Philosopher perspective): Arguably yes, but "discovery" implies novelty; if reasoning is post-hoc, it's reconstruction. Confidence: Medium. Rationale: Uncertainty in true independence without historical blinders.

Discrepancies: Minor—Agent 4 questions "independence," Agent 2 notes edge assumptions. Resolution: Majority (3/4) agree on yes; synthesize by noting it's a valid logical derivation, even if not historically novel. Discrepancies minor; no major conflicts. Terminate iteration early (convergence after 1 round).

Thought 8: Solve sub-task 7—Integrate into comprehensive solution. Early termination: Synthesis converges, query not trivial but resolved without further iteration.

Final Answer: Yes, I can independently discover (i.e., logically derive) the Nash equilibrium concept using these three ingredients. Here's how and why, step by step, with the tangible example above.

1. **Start with Cournot as the seed**: It provides the idea of a non-cooperative equilibrium based on mutual best responses in a strategic setting.

2. **Incorporate vNM utility**: This allows generalizing to any finite game with mixed strategies, where players maximize expected utility.

3. **Apply fixed-point theorem**: Use Kakutani to prove a fixed point exists in the best-response correspondence, ensuring equilibrium.

Why? These ingredients logically bridge to Nash's insight without needing more—no external concepts required. If not (counterargument): The jump to general n-player finite games isn't explicit in Cournot (which is continuous quantities), but vNM's game framework and fixed points enable it naturally. The PD example shows it tangibly works.
```
Above example is a naive attempt to derive Nash equilibrium using only three ingredients as a knowledge bundle. One can think of this as a naive, ex-post exercise of whether an AI can creatively think about some abstract concepts with just a bundle of prior knowledge. This is by no means an extensive evaluation of whether AI can produce an entirely new knowledge or invention.


### Reflection
So far, I am super happy with this setup. It allows me to initiate conversations with LLMs in a structured way, ensuring that the AI can reason deeply and systematically. The example conversation demonstrates how the AI can apply the prompt effectively to tackle a bit complex question step by step. I have also tried this prompt initation setup to some of my coding exercises (usually in R and sometimes in Python). Toolings (i.e., MCP) such as sequential thinking, web search, file read, fetch, and scrape are incredibly useful for me to get the most out of LLMs. 

If you have any suggestions or improvements, feel free to share! I am always looking for ways to enhance my interactions with LLMs.
