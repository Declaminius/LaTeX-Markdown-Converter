---
tags:
  - Example
label: ex:G01,2
Sources:
  - "[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019]]"
Location: p.~92
---
We use the general formula [[G0k, Gjk]] to compute explicit expressions for $G_{0,1}(z)$ and $G_{0,2}(z)$. By substituting $k = 1, 2$ we get
$$\begin{align*}
G_{0,1}(z) &= u_{1}(z) + u_{2}(z), \\
G_{0,2}(z) &= u_{1}(z)^{2}+ u_{1}(z)u_{2}(z) + u_{2}(z)^{2}.
\end{align*}$$
We defer the remaining mechanical calculations to our favorite computer algebra system and see that
$$\begin{align*}
G_{0,1}(z) &= -\frac{1}{2} + \frac{1}{2}\sqrt{\frac{2-3z-2\sqrt{1-4z}}{z}}\\
&= z + z^{2} + 3z^{3} + 7z^{4} + 22z^{5} + 65z^{6} + 213z^{7} + \mathcal{O}(z^{8}).
\end{align*}$$
This corresponds to the sequence [$\texttt{OEIS A166135}$](https://oeis.org/A166135). 
Furthermore $G_{0,1}(z)$ is uniquely determined as the only solution having a power series expansion with non-negative coefficients at $z_{0} = 0$ of
$$
z u^{4}+ 2zu^{3}+ (3z-1)u^{2} + (2z-1)u + z = 0.
$$
For $G_{0,2}(z)$, the computer tells us that
$$\begin{align*}
G_{0,2}(z) &= \frac{3 - \sqrt{1-4z} - \sqrt{2+12z+2\sqrt{1-4z}}}{4z} \\
&= z + z^{2} + 4z^{3} + 9z^{4}+ 31z^{5} + 91z^{6} + 309z^{7} + \mathcal{O}(z^{8}).
\end{align*}$$
This corresponds to the sequence [$\texttt{OEIS A111160}$](https://oeis.org/A111160). 
Furthermore, $G_{0,2}(z)$ is uniquely determined as the only solution of
$$
z^3 u^{4} - 3z^{2}u^{3} - (z^{2} - 3z)u^{2} + (z-1)u + z = 0,
$$
having a power series expansion with non-negative coefficients at $z_{0} = 0$.
