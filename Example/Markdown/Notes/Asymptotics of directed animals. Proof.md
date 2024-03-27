---
Theorem: "[[Asymptotics of directed animals]]"
tags:
  - Proof
---

The dominant singularity of $P_s(z,1)$ is a square root singularity at $\rho = 1/3$, leading to the asymptotic expansion
$$
s_n = \frac{1}{\sqrt{3\pi}}\frac{3^n}{\sqrt{n}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right).
$$
To calculate the average right width, we differentiate [[gf_pyramids]] with respect to $u$ and apply singularity analysis to the function $\frac{1}{P(z,1)}\left(\frac{\partial}{\partial u} P(z,u)\right)\big|_{u=1}.$ By symmetry, the average width is then simply twice the average right width plus one. For general pyramids we have
$$\begin{equation*}
P_t(z,1) = P_s\left(\frac{z}{1-z},1\right)
= \frac{1}{2}\left(\frac{1}{\sqrt{1-4z}} - 1\right),
\end{equation*}$$
and thus a simple application of the standard function scale (Theorem [[Standard function scale]]) combined with the Transfer Theorem [[mathcalO-Transfer]] gives the desired result.
