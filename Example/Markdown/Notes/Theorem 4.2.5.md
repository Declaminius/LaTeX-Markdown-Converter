---
tags:
  - Theorem
label: thm:asym_D(z)
---
Let $d_n$ be the number of excursions ending with a(n alternative) catastrophe. Their asymptotics depend on the structural radius $\rho = 1/P(\tau)$ and the possible polar singularity $\rho_0$ of $Q(z)$:
$$\begin{equation*}
d_n =
\begin{cases}
\frac{\rho_0^{-n}}{\rho_0 \cdot Q'(\rho_0)} + 
\mathcal{O}(P(1)^n) 
& \text{if $\rho_0 < \rho$and $\delta > 0$}, \\[8pt]
\frac{\rho_0^{-n}}{\rho_0 \cdot Q'(\rho_0)} + 
\mathcal{O}(n^{-3/2}\rho^{-n}) & 
\text{if $\rho_0 < \rho$and $\delta \leq 0$}, \\[8pt]
\frac{\rho^{-n}}{\eta\sqrt{\pi n}}
\left(1 + \mathcal{O}\left(1/n\right)\right) 
& \text{if $\rho_0 = \rho$}, \\[8pt]
\frac{D(\rho)^2\eta\rho^{-n}}{2\sqrt{\pi n^3}}
\left(1 + \mathcal{O}\left(1/n\right)\right) & 
\text{if $\mathcal{Z}$is empty},
\end{cases}
\end{equation*}$$
where $\eta$ is given by the Puiseux expansion of 
$$
Q(z) = Q(\rho) - \eta\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho)
$$ 
for $z \to \rho$. The last two cases occur only when $\delta < 0$.

`\begin{proof}`
![[Theorem 4.2.5. Proof|no-title]]
`\end{proof}`
