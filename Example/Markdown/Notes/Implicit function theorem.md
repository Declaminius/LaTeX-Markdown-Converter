---
tags:
  - Theorem
label: thm:implicit_function
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: Appendix B.5
---
Let $F(z,u)$ be bivariate analytic in two complex variables $(z.u)$ near $(0,0)$ in the sense that it admits a convergent power series in a polydisk
$$
F(z,u) = \sum_{n, k \geq 0} f_{n,k} z^n u^k, \qquad |z| < R, \quad |u| < S.
$$
Further, assume that $F(0,0) = 0$ and $\frac{\partial F}{\partial u}(0,0) \neq 0$. 
Then there exists a unique function $f(z)$ analytic in a neighborhood of zero such that $f(0) = 0$ and
$$
F(z,f(z)) = 0, \qquad |z| < \rho.
$$
