---
tags:
  - Corollary
---
The bivariate generating function $M_{\mathcal{D}}(z,u)$ for Dyck meanders satisfies 
$$
M_{\mathcal{D}}(z,u) = \frac{1 - 2zu - \sqrt{1 - 4z^2}}{2z(z(1 + u^2) - u)}.
$$
Further, the generating function $M_{\mathcal{D}}(z, 1) = \sum_{n=0}^\infty m_n z^n$ of meanders ending at any altitude satisfies
$$
M_{\mathcal{D}}(z, 1) = \frac{1 - 2z - \sqrt{1 - 4z^2}}{4z^2-2z} = 1 + z + 2z^2 + 3z^3 + 6z^4 + 10z^5 + 20z^6 + 35z^7 + \mathcal{O}(z^8).
$$
and its coefficients $m_n = \binom{n}{\lfloor n/2 \rfloor}$ correspond to [$\texttt{OEIS A001405}$](https://oeis.org/A001405).
Even further, the generating functions 
$$
G_{\mathcal{D}}(z) = \sum_{n=0}^\infty m_{2n}z^n, \qquad U_{\mathcal{D}}(z) = \sum_{n=0}^\infty m_{2n+1}z^n
$$
of even and odd meanders, respectively, satisfy
$$
G_\mathcal{D}(z) = \frac{1}{\sqrt{1 - 4z^2}}, \qquad U_{\mathcal{D}}(z) = \frac{1}{2z}\left(\frac{1}{\sqrt{1 - 4z^2}} - 1\right).
$$

`\begin{proof}`
![[Dyck meanders. Proof|no-title]]
`\end{proof}`
