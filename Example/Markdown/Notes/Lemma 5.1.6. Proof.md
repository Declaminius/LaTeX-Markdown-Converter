---
Theorem: "[[Lemma 5.1.6]]"
tags:
  - Proof
---

We already observed in [[Qs]] that strict half-pyramids are counted by the Motzkin numbers. Now we will make the combinatorial origin of this connection explicit, by recursively constructing a bijection $\omega$ between these combinatorial classes. The recursive descriptions of both classes are pictured in Figure [[Figure. The factorizations of half-pyramids and Motzkin excursions]].

Let $Q$ be a strict half-pyramid. It is either just a minimal dimer, or it consists of multiple dimers. In the first case, we set $\omega(Q)$ to be the empty path. 
In the latter case, we further distinguish whether there is more than one dimer in the rightmost column of the half-pyramids. If there is just one, then $Q$ is just the product of its minimal dimer and a half-pyramid $Q'$ lying above the minimal dimer on its left side. In this case, we define $\omega(Q) := \textbf{E}\, \omega(Q')$.
Otherwise, we push the lowest non-minimal dimer of the rightmost column upwards to obtain a factorization into the minimal dimer and two half-pyramids $Q_1$ and $Q_2$. This leads to the recursive rule $\omega(Q):= \textbf{NE}\,\omega(Q_1) \textbf{SE}\, \omega(Q_2)$.

For the inverse direction, let $M$ be a Motzkin excursion. It is either just the empty walk or it consists of at least one step. In the first case, we set $\omega^{-1}(M)$ to be a single dimer.
In the latter case, we further distinguish by the first step in $M$.
If $M = \textbf{E}\, M'$, we place a single dimer on the $x$-axis and recursively build $\omega^{-1}(M')$ diagonally right above the minimal dimer.
If otherwise $M$ starts with a **NE**-step, we identify the first **SE**-step that returns to the $x$-axis and partition $M = \textbf{NE}\, M_1 \textbf{SE}\, M_2$. Here we again start by placing a dimer on the $x$-axis and recursively building $\omega^{-1}(M_1)$ diagonally left above it. Once the construction of $\omega^{-1}(M_1)$ is complete, we place $\omega^{-1}(M_2)$ in the same column as the minimal dimer, diagonally right above $\omega^{-1}(M_1)$.
