---
tags:
  - Theorem
label: thm:asym_excursions
---
The number of excursions with (alternative) catastrophes $e_n$ is asymptotically equal to
$$\begin{equation*}
e_n = 
\begin{cases}
\frac{E(\rho_0)}{\rho_0 \cdot Q'(\rho_0)} \rho_0^{-n} + 
\mathcal{O}(P(1)^n) & 
\text{if $\rho_0 < \rho$and $\delta > 0$}, \\[8pt]
\frac{E(\rho_0)}{\rho_0 \cdot Q'(\rho_0)} \rho_0^{-n} + 
\mathcal{O}(n^{-3/2}\rho^{-n}) & 
\text{if $\rho_0 < \rho$and $\delta \leq 0$}, \\[8pt]
\frac{E(\rho)}{\eta}\frac{\rho^{-n}}{\sqrt{\pi n}}
\left(1 + \mathcal{O}\left(1/n\right)\right) & 
\text{if $\rho_0 = \rho$}, \\[8pt]
\frac{C_0(\rho)}{2}\frac{\rho^{-n}}{\sqrt{\pi n^3}}
\left(\frac{1}{\tau}\sqrt{2\frac{P(\tau)}{P''(\tau)}} + \eta D(\rho)\right)
\left(1 + \mathcal{O}\left(1/n\right)\right) & 
\text{if $\mathcal{Z}$is empty.}
\end{cases}
\end{equation*}$$

`egin{proof}`
![[Asymptotics of excursions with catastrophes. Proof|no-title]]
`\end{proof}`
