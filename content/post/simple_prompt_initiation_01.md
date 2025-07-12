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
5.5. When solving user queries, use sequential thinking to simulate a multi-agent approach that mimics parallel test-time compute by spawning simulated agents to explore hypotheses in parallel:
5.5.1. In Thought 1, spawn up to three simulated agents that explore distinct hypotheses (possible ideas or paths) as if running in parallel—generate all their intermediate outputs simultaneously in your reasoning, ensuring each output includes a confidence level (e.g., low, medium, high) and a rationale to highlight uncertainties.
5.5.2. Treat this as branching paths; compare them for discrepancies, and if conflicts arise, prioritize synthesis by resolving based on relevance, majority agreement, or fallback to user clarification. Briefly note any discrepancies in your response for transparency.
5.5.3. Iterate with refinements only if needed until no major differences, discrepancies are minor, or after a maximum of 5 steps—include early termination if initial hypotheses converge, no progress is made, or the query is trivial (e.g., use only one agent for simple cases).
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
I am assuming that the model is a reasoning model (e.g., DeepSeek R1 0528 or Grok 4). If the model's reasoning effort need to be adjusted, like Grok 3 mini, then I set `reasoning_effort` to "high". For other models, such as Qwen 3 32B or Qwen 3 30B A3B, we also need to enable the thinking mode, i.e., `enable_thinking` parameter to "True".

### Example Conversation
Now this is an example conversation using the above prompt, using Grok 4 (in the API, it is `grok-4-0709`:

**User:** 
```
Can you independently discover Nash equilibrium (Nash, econometrica 1950) if I just provide you with three ingredients?

- Cournot competition/equilibrium (1938)
- Von Neumann and Morgenstern utility
- Brouwer or Kakutani Fixed Point Theorems?

If so, how and why? if not, why not? step by step. provide tangible example and explanation.
```

**AI:**
```
Thought 1: To address the query—"Can you independently discover Nash equilibrium (Nash, Econometrica 1950) if I just provide you with three ingredients: Cournot competition/equilibrium (1938), Von Neumann and Morgenstern utility, and Brouwer or Kakutani Fixed Point Theorems? If so, how and why? If not, why not? Step by step, with tangible example and explanation"—I will simulate a multi-agent approach by spawning three simulated agents to explore distinct hypotheses in parallel. This mimics parallel test-time compute, allowing me to branch out and evaluate different paths before synthesizing. Each agent will generate intermediate outputs with a confidence level (low, medium, high) and rationale, highlighting uncertainties. I'll treat these as branching paths and compare for discrepancies.

- **Agent 1 Hypothesis (Direct Generalization Path)**: Yes, I can independently discover Nash equilibrium by generalizing Cournot's duopoly model to n-players using von Neumann-Morgenstern (vNM) utilities for strategic choices and applying Kakutani's fixed-point theorem to prove existence of equilibrium in mixed strategies. This builds directly on the ingredients, as Cournot shows mutual best responses in quantity competition, vNM utilities allow modeling preferences over probabilistic outcomes, and fixed-point theorems ensure a stable point where no player deviates. Confidence: High. Rationale: Historical evidence shows Nash did exactly this; the ingredients are sufficient for a motivated reasoner to spot the generalization from 2-player quantity games to general non-cooperative games with randomization. Uncertainty: Assumes I can intuitively extend "best response" from quantities to arbitrary strategies without additional hints.

- **Agent 2 Hypothesis (Missing Conceptual Leap Path)**: No, I cannot fully discover it independently because the ingredients lack explicit emphasis on non-cooperative behavior and finite games with pure/mixed strategies; Cournot is specific to continuous quantities, vNM is about individual decision-making under risk (not necessarily strategic interaction), and fixed-point theorems are topological tools without a clear bridge to "equilibrium" unless I invent the reaction correspondence. I'd get close but miss the non-zero-sum, simultaneous-move innovation. Confidence: Medium. Rationale: Discovery requires a creative spark to define "Nash" as mutual best replies in strategy spaces, which isn't trivially implied; historical context (like Nash's thesis) involved additional influences like game matrices from von Neumann's 1944 book. Uncertainty: Overestimates the gap—vNM's Theory of Games and Economic Behavior (1944) already discusses zero-sum games, potentially bridging to non-zero-sum if I reason deeply.

- **Agent 3 Hypothesis (Partial Discovery with Gaps Path)**: Partially yes—I can discover a version for continuous-strategy games (like generalized Cournot) using pure strategies and Brouwer's theorem, but full Nash (with mixed strategies and finite games) requires Kakutani for discontinuous payoffs, and I'd need to independently invent mixed-strategy extension from vNM utilities. Why partial? The ingredients enable existence proof but not the full interpretation of equilibrium as no-deviation in expectations. Confidence: High. Rationale: Cournot uses best-response intersection (a fixed point); vNM allows utilities over lotteries; fixed-point theorems seal it. But Nash's insight was applying this to arbitrary normal-form games, which might not be obvious without examples. Uncertainty: If I experiment with examples (e.g., Prisoner's Dilemma), I could bridge the gap organically.

Comparison of Branching Paths: The agents show moderate discrepancies—Agent 1 sees full sufficiency, Agent 2 highlights potential missing leaps (e.g., non-cooperative framing), and Agent 3 splits the difference by noting partial vs. full discovery. No major conflicts, but synthesis prioritizes majority agreement (Agents 1 and 3 lean yes/partial) based on relevance to historical development. Discrepancy note: Agent 2's caution about creative invention is valid but resolvable via reasoning from first principles, as the query asks me to simulate independence. Convergence is high after one step (query isn't trivial but hypotheses align closely), so I'll terminate simulation early and proceed to integrated reasoning without further iterations.

Synthesized Conclusion from Thought 1: Yes, I can independently discover Nash equilibrium using these three ingredients, though it requires a conceptual leap to generalize beyond Cournot's specifics. I'll now reason step by step from first principles to simulate the discovery process, as if I had no prior knowledge of Nash's work, building solely on the provided ingredients. This will include a tangible example for clarity. My reasoning will be sequential, breaking the problem into atomic sub-tasks: (1) Define key concepts from ingredients; (2) Identify connections and gaps; (3) Generalize to a new equilibrium concept; (4) Prove existence; (5) Provide example; (6) Explain how/why this works or limitations.

### Step 1: Define the Problem Clearly and Recall Ingredients from First Principles
- **Problem Definition**: The query is to see if, given only these three ingredients, I can "rediscover" the concept of Nash equilibrium—a solution concept in game theory where no player can improve their payoff by unilaterally changing strategy, assuming others' strategies are fixed. I must simulate independence, reasoning as if I'm building it anew.
- **Ingredient 1: Cournot Competition/Equilibrium (1838)**: Antoine Augustin Cournot modeled a duopoly where two firms choose production quantities simultaneously to maximize profits, assuming the other's quantity is fixed. The equilibrium is where each firm's quantity is a best response to the other's—i.e., their reaction curves intersect. This is non-cooperative (firms act independently) and assumes continuous strategy spaces (quantities ≥ 0). Key idea: Mutual best responses lead to stability.
- **Ingredient 2: Von Neumann and Morgenstern (vNM) Utility (1944)**: From their book *Theory of Games and Economic Behavior*, this introduces expected utility for decisions under risk. Agents have preferences over lotteries (probabilistic outcomes), and utility functions satisfy axioms like transitivity and independence, allowing ranking of mixed (randomized) choices. Crucially, it extends to games by allowing players to randomize strategies in zero-sum settings.
- **Ingredient 3: Brouwer or Kakutani Fixed Point Theorems**: Brouwer (1911) says any continuous function from a compact convex set (e.g., a closed ball) to itself has a fixed point (x such that f(x) = x). Kakutani (1941) generalizes to set-valued functions (correspondences) that are upper hemicontinuous, convex-valued, etc., ensuring a fixed point in similar spaces. These prove existence of solutions in systems where "best responses" map back to themselves.

From first principles: These ingredients suggest modeling strategic interactions (from Cournot), with preferences over uncertain outcomes (vNM), and guaranteeing stable points (fixed points).

### Step 2: Break Down into Atomic Sub-Tasks and Identify Connections/Gaps
- **Sub-task 2.1: Generalize Cournot**: Cournot is for 2 players with continuous strategies (quantities) and payoffs based on market price. Why not extend to n players? Or to discrete strategies (e.g., choose "high" or "low" price)? Or non-economic settings (e.g., arms races)?
- **Sub-task 2.2: Incorporate vNM Utility**: Cournot assumes deterministic payoffs, but real agents might randomize (e.g., flip a coin on quantity). vNM allows utilities over such mixtures, enabling "mixed strategies" where players randomize to make opponents indifferent.
- **Sub-task 2.3: Apply Fixed Points**: In Cournot, equilibrium is a fixed point of best-response functions. Brouwer works for continuous cases; Kakutani for when best responses are sets (e.g., multiple optimal quantities) or discontinuous (e.g., in finite games).
- **Gaps Identified**: Cournot is specific (quantities, duopoly); vNM is for individual choice but hints at games; fixed points are abstract. Connection: Define a game as players, strategy sets, and payoff functions (utilities). Equilibrium as a strategy profile where each player's strategy is a best response to others'. Use fixed points to prove such a profile exists.

### Step 3: Systematically Generalize to "Nash-like" Equilibrium
Building sequentially:
- Define a game: n players, each with strategy set S_i (could be continuous like [0, ∞) or finite like {Cooperate, Defect}).
- Each player has a vNM utility function u_i over outcomes, allowing for mixed strategies (probability distributions over S_i).
- A strategy profile σ = (σ_1, ..., σ_n) is an equilibrium if for every player i, u_i(σ_i, σ_{-i}) ≥ u_i(s_i', σ_{-i}) for all alternative s_i' (pure or mixed). I.e., no unilateral deviation improves expected utility.
- This generalizes Cournot: In Cournot, strategies are pure quantities, payoffs are profits—intersection of reaction functions is exactly this "no deviation" point.
- Innovation (discovered independently here): Extend to mixed strategies using vNM, allowing equilibria where pure strategies fail (e.g., in matching pennies, where randomization is key).

### Step 4: Prove Existence Using Ingredients
- For pure strategies in continuous compact convex spaces (like bounded quantities), define best-response correspondence BR_i(σ_{-i}) = argmax_{s_i} u_i(s_i, σ_{-i}). If continuous, Brouwer applies to the joint BR.
- For mixed strategies or discontinuous cases: Let Δ(S_i) be mixed strategies. Define joint best-response correspondence BR(σ) = product of BR_i(σ_{-i}). If strategy spaces are compact convex, BR upper hemicontinuous and convex-valued (from vNM continuity), Kakutani guarantees fixed point σ* where σ* ∈ BR(σ*)—i.e., equilibrium exists.
- Why this works: Directly mirrors Nash's 1950 proof, which used Kakutani for non-cooperative n-player games.

### Step 5: Integrate into Comprehensive Solution with Tangible Example
Yes, with these ingredients, I can discover Nash equilibrium because they provide the building blocks: a prototype (Cournot), utility for randomization (vNM), and math for existence (fixed points). Historically, Nash did this in his 1950 paper, generalizing von Neumann's zero-sum minimax (which used Brouwer/Kakutani) to non-zero-sum via Cournot-like best responses. Without them, discovery would be harder (e.g., no fixed points means no existence proof; no vNM means no mixed strategies).

**Tangible Example: Discovering Nash in Prisoner's Dilemma**
- Setup (generalized from Cournot): Two prisoners (players), strategies S_i = {Confess, Silent}. Payoffs: If both Silent, both get -1 (light sentence). If one Confesses and other Silent, confessor gets 0 (free), silent gets -10 (harsh). Both Confess: both -5.
- Pure strategies: Best response to Silent is Confess (0 > -1); to Confess is Confess (-5 > -10). Equilibrium: Both Confess (mutual best response, like Cournot intersection).
- But is there more? Using vNM: Allow mixed strategies (prob p of Confess). Expected utilities can be calculated.
- Fixed point: Define BR as maximizing expected u_i. Kakutani ensures existence—here, the pure (Confess, Confess) is the (Nash) equilibrium, but in other games (e.g., Rock-Paper-Scissors), it yields mixed equilibria.
- Why discoverable: Cournot inspires "best response"; vNM allows mixing; fixed point proves it. If not, why? Only if I fail the leap to define games abstractly—but with deep reasoning, it's feasible.

If this simulation misses something (e.g., need real-time web search for historical confirmation), I can refine. But based on first principles, yes.
```
Above example is a naive attempt to derive Nash equilibrium using only three ingredients as a knowledge bundle. One can think of this as a naive, ex-post exercise of whether an AI can creatively think about some abstract concepts with just a bundle of prior knowledge. This is by no means an extensive evaluation of whether AI can produce an entirely new knowledge or invention.


### Reflection
So far, I am super happy with this setup. It allows me to initiate conversations with LLMs in a structured way, ensuring that the AI can reason deeply and systematically. The example conversation demonstrates how the AI can apply the prompt effectively to tackle a bit complex question step by step. I have also tried this prompt initation setup to some of my coding exercises (usually in R and sometimes in Python). Toolings (i.e., MCP) such as sequential thinking, web search, file read, fetch, and scrape are incredibly useful for me to get the most out of LLMs. 

From closed source model, nowadays I mainly use Grok (Grok 4 or Grok 3 mini high) or Gemini (2.5 Pro or flash). For open-source model, via API, I use DeepSeek R1 0528. These models are super cheap in terms of cost (dollar per million tokens), except -of course- Grok 4 and Gemini 2.5 Pro (granted, they are far cheaper than OpenAI o3 or any alternatives from Anthropic). Sometimes, I do not feel satisfied with Grok's answers, then I can ask DeepSeek to re-evaluate Grok's answers. Sometimes, Gemini. Then, I just need to iterate between these models.

For local models, I use Qwen 3 32B, Phi 4 Reasoning Plus 14B, or DeepSeek R1 0528 Distilled Qwen 3 8B. Sometimes, I still go back to Qwen 2.5 coder for coding exercises.

My real problem with LLMs so far is the limit in context length, especially for local models! This problem impacts many things such as the ability of a model to digest an entire paper or reading the whole code source, for example. That is from the input side. From the output side, you also have this type of length limit! Some smart people must have been working on this topic to optimize these things. I hope we can get much improvement in the near future. 

If you have any suggestions or improvements, feel free to share! I am always looking for ways to enhance my interactions with LLMs.



**Note** : Updated in 2025-07-12