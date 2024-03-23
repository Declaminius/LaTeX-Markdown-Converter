---
tags:
  - Theorem
label: thm:gf_bridges
---
Let 
$$
P(u) = \sum_{k = -c}^d p_k u^k
$$ 
be the characteristic polynomial of a simple set of jumps.
The generating function of bridges is an algebraic function given by 
$$\begin{equation*}
B(z) = z\sum_{j=1}^c\frac{u_j'(z)}{u_j(z)} = z \frac{\mathrm{d}}{\mathrm{d}z} \log(u_1(z)\cdots u_c(z)),
\end{equation*}$$
where $u_1(z),\dots,u_c(z)$ are the small branches of the characteristic curve.
Generally, the generating function $W_k(z)$ of paths ending at altitude $k$ for $-\infty < k < c$ is given by,
$$\begin{equation*}
W_k(z) = z\sum_{j=1}^c \frac{u'_j(z)}{u_j(z)^{k+1}} = 
-\frac{z}{k} \frac{\mathrm{d}}{\mathrm{d}z}
\left(
\sum_{j=1}^c u_j(z)^{-k}
\right)
\end{equation*}$$
and for $-d < k < \infty$,
![[Wk2|no-title]]
where $v_1, \dots, v_d$ are the large branches of the characteristic curve.

`\begin{proof}`
![[Theorem 2.2.2. Proof|no-title]]
`\end{proof}`
