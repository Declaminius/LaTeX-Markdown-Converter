---
tags:
  - Theorem
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: Theorem VI.2, p.~385
---
Let $\alpha \in \C \setminus \Z_{\leq 0}$. Then, the coefficient of $z^n$ in the function
$$
f(z) = (1 - z)^{-\alpha} \left(\frac{1}{z} \log \frac{1}{1-z}\right)^\beta
$$
admits for large $n$ a full asymptotic expansion in descending powers of $\log n$ with
$$
f_n = [z^n] f(z) \sim \frac{n^{\alpha - 1}}{\Gamma(\alpha)}(\log n)^\beta \left(1 + \frac{C_1}{\log n} + \frac{C_2}{\log^2 n} + \cdots\right),
$$
where
$$
C_k = \binom{\beta}{k} \Gamma(\alpha) \left.\left(\frac{\mathrm{d}^k}{\mathrm{d}s^k} \frac{1}{\Gamma(s)}\right)\right|_{s = \alpha}.
$$
