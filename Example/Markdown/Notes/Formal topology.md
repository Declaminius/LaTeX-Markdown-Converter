---
tags:
  - Definition
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: p.~731
---
We define the valuation of a non-zero formal power series $f(z) = \sum_{n = 0}^\infty f_n z^n$ as the smallest $r \in \N$ such that $f_r \neq 0$ and denote it by $\mathrm{val}(f)$. Further, we set $\mathrm{val}(0) = \infty$. Then, one defines a metric on $R[[z]]$ via
$$\begin{equation*}
d(f,g) = 2^{-\mathrm{val(f-g)}}.
\end{equation*}$$
With this distance, the space of all formal power series becomes a complete metric space.
