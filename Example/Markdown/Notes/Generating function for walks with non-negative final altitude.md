---
tags:
  - Corollary
Sources:
  - "[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002]]"
Location: p.~51
---
Let $W^+(z,u) = \sum_{k,n = 0}^\infty w_{n,k} z^n u^k$ denote the bivariate generating function of paths, whose intermediate steps may be negative, but that end at a non-negative final altitude $k \geq 0$. Then $W^+(z)$ satisfies
$$
W^+(z,u) = z \sum_{\ell = 1}^d \frac{v_\ell'(z)}{u - v_\ell(z)}
= 1 + z \frac{\mathrm{d}}{\mathrm{d}z}(\log M(z,u)),
$$
where $v_1, \dots, v_d$ are the large branches of the characteristic curve.

`\begin{proof}`
![[Generating function for walks with non-negative final altitude. Proof|no-title]]
`\end{proof}`
