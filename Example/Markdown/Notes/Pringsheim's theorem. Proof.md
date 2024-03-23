---
Theorem: "[[Pringsheim's theorem]]"
tags:
  - Proof
---

Without loss of generality we assume $R = 1$.
Suppose $f$ were not singular at $z = 1$.
Then its Taylor series centered at $1/2$ would be holomorphic at one.
Hence, by Lemma [[Existence of singular points]] its radius of convergence would be $r > 1/2$.
Further, for every $\zeta$ with $|\zeta| = 1/2$ we have: 
$$ 
\left| 
\frac{1}{n!}f^{(n)}(\zeta)
\right| = 
\frac{1}{n!} \frac{\mathrm{d}^n}{\mathrm{d}\zeta^n}
\left|
\sum_{k = 0}^\infty a_k\zeta^k
\right| = 
\left|
\sum_{k = n}^\infty \binom{k}{n}a_k\zeta^{k - n}
\right| \leq 
\sum_{k = n}^\infty \binom{k}{n}a_{k}
\left(\frac{1}{2}\right)^{k - n} = 
\frac{1}{n!}f^{(n)}
\left(\frac{1}{2}\right). 
$$
Hence, for every $\zeta$ with $|\zeta| = 1/2$ the radius of convergence of the Taylor series centered at $\zeta$ would be at least $r > 1/2$.
As a result there would be no singular point of $f$ on $\partial \mathbb{E}$ contradicting the previous Lemma [[Existence of singular points]].
