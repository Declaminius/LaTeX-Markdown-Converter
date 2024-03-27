---
tags:
  - Theorem
label: thm:gf_catastrophes
Sources:
  - "[[Lattice paths with catastrophes|Banderier & Wallner, 2017]]"
Location: Theorem 2.1
---
Let $c_{n,k}$ be the number of meanders with catastrophes of length $n$ ending at altitude $k$, relative to a simple step set $\mathcal{S}$, with characteristic polynomial $P(u) = \sum_{k=-c}^d p_ku^k$.
Further, let $u_1,\dots,u_c$ denote the small roots and $v_1,\dots,v_d$ the large roots of the kernel equation.
Then the generating function 
$$
C(z,u) = \sum_{n,k = 0}^\infty c_{n,k} u^k z^n
$$ 
is algebraic and satisfies 
$$\begin{equation*}
C(z,u) = D(z) \cdot M(z,u) = \frac{1}{1 - Q(z)} \cdot \frac{\prod_{i=1}^c(u - u_i(z))}{u^c(1 - zP(u))},
\end{equation*}$$
where $D(z)$ denotes the generating function of excursions ending with a catastrophe and $Q(z)$ counts the number of excursions with exactly one catastrophe occurring as the last step of the path.
In addition, the generating functions for meanders with catastrophes ending at altitude $k$ satisfy
$$\begin{equation*}
C_k(z) = D(z) \cdot M_k(z) = \frac{1}{1 - Q(z)} \cdot \frac{1}{p_d z} \sum_{\ell = 1}^d v_\ell^{-k-1} \prod_{\substack{1 \leq j \leq d, \\ j \neq \ell}} \frac{1}{v_j - v_\ell}, \quad \text{for $k \geq 0$}.
\end{equation*}$$
The generating function $Q(z)$ in both cases depends on the model of catastrophes:
$$\begin{equation*}
Q^\mathrm{cat}(z) = q z \left(M(z) - E(z) - \sum_{\substack{s > 0, \\ -s\in \mathcal{S}}} M_s(z)\right), \qquad
Q^\mathrm{alt}(z) = q z \cdot M(z). 
\end{equation*}$$

`\begin{proof}`
![[Generating function for meanders and excursions with catastrophes. Proof|no-title]]
`\end{proof}`
