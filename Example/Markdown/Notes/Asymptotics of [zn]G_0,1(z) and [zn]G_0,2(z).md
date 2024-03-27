---
tags:
  - Theorem
Sources:
  - "[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019]]"
Location: Theorem 6.3
---
Let $G_{0,1}(z)$ and $G_{0,2}(z)$ be the generating functions for positive basketball walks starting at the origin and ending at altitude one, respectively, at two. Then, as $n \to \infty$ the coefficients are asymptotically equal to
$$\begin{align*}
[z^{n}]G_{0,1}(z) &= \frac{1}{\sqrt{5\pi}} \frac{4^{n}}{\sqrt{n^3}}
\left(
1 - \frac{81}{200n}+ \mathcal{O}
\left(\frac{1}{n^{2}}\right)
\right), \\
[z^{n}]G_{0,2}(z) &= \frac{5+\sqrt{5}}{10\sqrt{\pi}} \frac{4^{n}}{\sqrt{n^3}}
\left(
1 - \frac{201+24\sqrt{5}}{200n} + 
\mathcal{O}\left(\frac{1}{n^{2}}\right)
\right),
\end{align*}$$
with $C_1 := \frac{1}{\sqrt{5\pi}} \approx 0.25231$ and
$C_2 := \frac{5+\sqrt{5}}{10\sqrt{\pi}} \approx 0.40825$.

`\begin{proof}`
![[Asymptotics of [zn]G_0,1(z) and [zn]G_0,2(z). Proof|no-title]]
`\end{proof}`
