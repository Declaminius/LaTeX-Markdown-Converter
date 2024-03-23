---
tags:
  - Equation
---
$$\begin{equation} \tag{4.1}
    e_n = 
    \begin{cases}
      \frac{M(\rho_0)}{\rho_0 \cdot Q'(\rho_0)} \rho_0^{-n} + 
      \mathcal{O}(P(1)^n) & 
      \text{if $\rho_0 < \rho$ and $\delta > 0$}, \\[8pt]
      \frac{M(\rho_0)}{\rho_0 \cdot Q'(\rho_0)} \rho_0^{-n} + 
      \mathcal{O}(n^{-3/2}\rho^{-n}) & 
      \text{if $\rho_0 < \rho$ and $\delta \leq 0$}, \\[8pt]
      \frac{M(\rho)}{\eta}\frac{\rho^{-n}}{\sqrt{\pi n}}
      \left(1 + \mathcal{O}\left(1/n\right)\right) & 
      \text{if $\rho_0 = \rho$}, \\[8pt]
      \frac{C(\rho,1)}{2}\frac{\rho^{-n}}{\sqrt{\pi n^3}}
      \left(\frac{1}{\tau - 1}\sqrt{2\frac{P(\tau)}{P''(\tau)}} + \eta D(\rho)\right)
      \left(1 + \mathcal{O}\left(1/n\right)\right) & 
      \text{if $\mathcal{Z}$ is empty.}
    \end{cases}
  \end{equation}$$