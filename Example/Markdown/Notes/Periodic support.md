---
tags:
  - Definition
---
We say that a function $F(z)$ has periodic support of period $p$ or for short $F(z)$ is $p$-*periodic* if there exists an integer $b$ and a function $H(z)$ such that 
$$
F(z) = z^b H(z^p).
$$
The largest such $p$ is called the *period* of $F$ and is denoted by $\mathrm{per}(F)$. If this holds only for $p = 1$, the function is said to be *aperiodic*.
A simple walk defined by the set of jumps $\mathcal{S}$ is said to have period $p$ if the characteristic polynomial $P(u) = \sum_{s \in \mathcal{S}} p_s u^s$ has period $p$. 
In this case, the period can also be defined via 
$$
\mathrm{per}(P) = \mathrm{gcd}(b_2-b_1,\dots,b_m - b_1).
$$
Further, a simple walk is said to be *reduced*, if the greatest common divisor of the jumps is equal to one.
Note that aperiodic walks are by their definition automatically reduced.
