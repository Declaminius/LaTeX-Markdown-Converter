---
tags:
  - Theorem
Sources:
  - "[[Funktionentheorie Eine Einführung Sechste Auflage|Jänich, 2004]]"
Location: Satz 3
---
Let $f: U \to \C$ be a holomorphic function and let $z_{0} \in U$. Then there exists exactly one power series $\sum_{n=0}^{\infty}c_{n}(z-z_{0})^{n}$ with positive radius of convergence that represents $f$ in a neighborhood of $z_{0}$. Further, the coefficients $c_{n}$ are given via
$$
c_{n} = \frac{1}{2\pi \mathrm{i}}\int_{|z-z_{0}|=r} \frac{f(z)}{(z-z_{0})^{n+1}}~\mathrm{d}z,
$$
with $r > 0$ sufficiently small such that $\{\, z: |z - z_{0}| \leq r \,\} \subset U$. 
The power series converges for every open disk fully contained in $U$ and represents the function $f(z)$. In particular, this shows that every holomorphic function is also analytic.
