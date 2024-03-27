---
tags:
  - Theorem
label: thm:standard_function_scale
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: Theorem VI.1, p.~381
---
Let $\alpha$ be an arbitrary complex number in $\mathbb{C} \setminus \mathbb{Z}_{\leq 0}$. The coefficient of $z^n$ in $f(z) = (1-z)^{-\alpha}$ admits for large $n$ a complete asymptotic expansion in descending powers of $n$:
$$
[z^n]f(z) \sim \frac{n^{\alpha -1}}{\Gamma(\alpha)}\left(1 + \sum_{k=1}^{\infty} \frac{e_k}{n^k}\right),
$$
where $e_k$ is a polynomial in $\alpha$ of degree $2k$. In particular: 
$$\begin{equation*}
\begin{split}
[z^n]f(z) \sim \frac{n^{\alpha-1}}{\Gamma(\alpha)}\left(1 + \frac{\alpha(\alpha - 1)}{2n} + \frac{\alpha(\alpha - 1)(\alpha - 2)(3\alpha - 1)}{24n^2} \right. \\
\left. + \ \frac{\alpha^2(\alpha -1)^2(\alpha -2)(\alpha - 3)}{48n^3} + \mathcal{O}\left(\frac{1}{n^4}\right)\right).
\end{split}
\end{equation*}$$
The quantity $e_k$ is a polynomial in $\alpha$ that is divisible by $\alpha(\alpha - 1)\cdots(\alpha -k)$, in accordance with the fact that the asymptotic expansion terminates when $\alpha \in \mathbb{Z}_{\geq 0}$. The formula is even valid (but not very meaningful) for $\alpha \in \Z_{\leq 0}$, as $1/\Gamma(\alpha) = 0$ and the coefficients $[z^n](1-z)^{-\alpha}$ are zero for $n > -\alpha$.

`\begin{proof}`
![[Standard function scale. Proof|no-title]]
`\end{proof}`
