---
Theorem: "[[Strong triangle inequality]]"
tags:
  - Proof
---

Firstly we note that
$$ |Q(z)| = \Big|\sum_{n \geq 0}q_n z^n\Big| \leq \sum_{n \geq 0}|q_n z^n| = \sum_{n \geq 0}q_n|z|^n = Q(|z|).
$$
The strict version of this inequality clearly holds for any $z$ such that $z/|z|$ is not a root of unity since no two summands can be collinear in this case.
Now assume that $(z/|z|)^k = 1$ and suppose that $|Q(z)| = Q(|z|)$. Hence the equality condition of the triangle inequality tells us that all summands must be collinear, i.e.~there must be an $i < k$ with $q_n = 0$ for all $n \in \mathbb{N}: n \not\equiv j \mod k$. However, that would imply
$$
Q(z) = z^j\sum_{n \in N}q_{k n + j}z^{k n} = z^jH(z^k),
$$
contradicting the aperiodicity of $Q(z)$.
