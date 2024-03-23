---
Theorem: "[[Theorem 2.2.1]]"
tags:
  - Proof
---

Let $w_n(u) = [z^n]W(z,u)$ count the number of paths ending at altitude $k$ after a total of $n$ steps. By decomposing a path before its very last step, we find the recursive description
$$
w_0(u) = 1, \qquad w_1(u) = P(u), \qquad w_{n+1}(u) = w_n(u) \cdot P(u).
$$
Hence, we have $w_n(u) = P(u)^n$ for all $n$. Therefore it holds that
$$
W(z,u) = \sum_{n = 0}^\infty z^n w_n(u) = \sum_{n=0}^\infty z^nP(u)^n = \frac{1}{1 - zP(u)},
$$
converging for $|z| < 1/P(|u|)$.
