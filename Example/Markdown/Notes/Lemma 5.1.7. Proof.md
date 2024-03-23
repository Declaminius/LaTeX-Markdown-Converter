---
Theorem: "[[Lemma 5.1.7]]"
tags:
  - Proof
---

We already observed in [[Ps]] that the generating functions of these two combinatorial classes coincide. Now we present a combinatorial argument for this fact, by constructing an explicit bijection $\omega$.
Let $P$ be a strict pyramid. It either has zero right width and is thus a half-pyramid, or there exists a dimer exactly one step to the right of the minimal dimer at some height $h > 0$. In the first case, we already know how to construct $\omega(P)$ from Lemma [[Lemma 5.1.6]].
In the second case, we partition $P$ into a lower half-pyramid $Q$ and an upper pyramid $P$, by pushing the lowest non-minimal dimer in the column of the minimal dimer upwards; see Figure~[[Figure. The factorization of Motzkin excursions with only horizontal catastrophes]]. In this case we apply the recursive rule $\omega(P) = \omega(Q) {\color{catred} \textbf{E}}\, \omega(P')$.

For the reverse direction, consider a 2-Motzkin excursion $M$ with no red {\color{catred}**E**}-steps at positive height $h > 0$. If it has no red {\color{catred} **E**}-step, it is simply a regular Motzkin excursion and Lemma [[Lemma 5.1.6]] applies. In the other case, we recursively split it at the first red {\color{catred} **E**}-step into an initial Motzkin excursion, followed by a red {\color{catred} **E**}-step and a final 2-Motzkin excursion and apply Lemma [[Lemma 5.1.6]] to the first part.
