---
Theorem: "[[Generating function for meanders and excursions with catastrophes]]"
tags:
  - Proof
---

Begin by taking an arbitrary meander with catastrophes of length $n$.
We decompose the path into a final meander without any catastrophes, counted by $M(z,u)$, and a possibly empty initial part counted by $D(z)$.
The expression for the generating function $M(z,u)$ of the final meander has already been derived in Theorem [[Generating function of meanders and excursions]].
The initial part can then be further decomposed into a sequence of excursions containing exactly one catastrophe as their respective last step. The decomposition is illustrated in Figure [[Figure. The decomposition of a meander with catastrophes]].
Since each of the individual excursions are counted by $Q(z)$, we thus have $D(z) = 1/(1 - Q(z))$.
Finally, to describe $Q(z)$ we note that each of these individual excursions is simply a meander without any catastrophes, followed by a final catastrophe. 
In the case of regular catastrophes, we now need to subtract all heights from which by definition no catastrophe can occur, and we get 
$$
Q^\mathrm{cat}(z) = q z \left(M(z) - E(z) - \sum_{\substack{s > 0, \\ -s\in \mathcal{S}}} M_s(z)\right),
$$
with $q$ denoting the weight of a catastrophe. In the model of alternative catastrophes, catastrophes may occur at any altitude and thus we have
$$\begin{equation*}
Q^{\mathrm{alt}}(z) = q z \cdot M(z).
\end{equation*}$$
For the generating function of meanders with catastrophes ending at a fixed altitude $k$, it suffices to replace the bivariate generating function for meanders $M(z,u)$ with the generating function $M_k(z)$ of meanders ending at altitude $k$. The expression for $M_k(z)$ has been derived in Corollary [[Corollary 2.2.7]].
