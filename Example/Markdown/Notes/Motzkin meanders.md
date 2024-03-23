---
tags:
  - Corollary
label: cor:motzkin_meanders
---
The bivariate generating function $M_{\mathcal{M}}(z,u)$ for Motzkin meanders satisfies 
$$
M_{\mathcal{M}}(z,u) = \frac{2z(u + 1) - 1 + \sqrt{1 - 2z - 3 z^{2}}}{2z\left(u - z \left(u^{2}+u + 1\right)\right)}.
$$
Further, the generating function $M_{\mathcal{M}}(z, 1)$ of meanders ending at any altitude satisfies
$$\begin{align*}
M_{\mathcal{M}}(z, 1) &= \frac{1 - 3z - \sqrt{1 - 2z - 3z^2}}{6z^2 - 2z} \\
&= 1 + 2z + 5z^{2} + 13z^{3} + 35z^{3} + 96z^{5} + 267z^{6} + 750z^7 + \mathcal{O}(z^8).
\end{align*}$$
This counting sequence corresponds to [$\texttt{OEIS A005773}$](https://oeis.org/A005773), which tells us that it also counts the number of directed animals of size $n$. We will explore this connection further in the last chapter of this thesis.

`\begin{proof}`
![[Motzkin meanders. Proof|no-title]]
`\end{proof}`
