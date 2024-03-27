---
Theorem: "[[sim-Transfer]]"
tags:
  - Proof
---

It suffices to observe that, with $g(z) = (1 - z)^{-\alpha}$, one has
$$
f(z) \sim g(z) \qquad \iff \qquad f(z) = g(z) + o(g(z)).
$$
Then we apply the $\mathcal{O}$-Transfer Theorem [[mathcalO-Transfer]] to the first term and the $o$-Transfer Theorem~[[o-Transfer, logarithms]] to the remainder, yielding the claim.
