---
Theorem: "[[Theorem 4.2.7]]"
tags:
  - Proof
---

The first three cases can be handled completely analogously to Theorem [[Theorem 4.2.6]]. For the final case we again rely on results from \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 4]]\]. From there we have the asymptotic expansion
$$\begin{align*}
M(z) &= M(\rho) + \sqrt{2\frac{P(\tau)^3}{P''(\tau)}}\frac{\prod_{j=2}^c (1 - u_j(\rho))}{P(\tau) - P(1)}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho) \\
&= M(\rho) + \sqrt{2\frac{P(\tau)^3}{P''(\tau)}}\frac{M(\rho)(1 - \rho P(1))}{(1 - u_1(\rho))(P(\tau) - P(1))}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho) \\
&= M(\rho) - \sqrt{2\frac{P(\tau)}{P''(\tau)}}\frac{M(\rho)}{\tau - 1}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho).
\end{align*}$$
The remaining calculations follow the line of the previous theorems.
