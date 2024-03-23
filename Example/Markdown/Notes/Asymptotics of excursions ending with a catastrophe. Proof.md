---
Theorem: "[[Asymptotics of excursions ending with a catastrophe]]"
tags:
  - Proof
---



1. We start with the case $\rho_0 < \rho$. Expanding the denominator for $z \to \rho_0$ yields
$$
1 - Q(z) = \underbrace{(1 - Q(\rho_0))}_{=0} + \rho_0 Q'(\rho_0)\left(1 - z/\rho_0\right) + \mathcal{O}\left(\left(1 - z/\rho_0\right)^2\right).
$$
Next, an elementary coefficient extraction gives
$$\begin{align*}
[z^{n}] \frac{1}{\rho_0 Q'(\rho_0)}\left(1 - z/\rho_0\right)^{-1} 
&= \frac{\rho_{0}^{-n}}{\rho_{0}Q'(\rho_{0})}.
\end{align*}$$
We now continue the asymptotic analysis by subtracting the simple pole.
For $\delta \leq 0$ we observe that $|Q(z)|$ is bounded for $|z| < \rho$ and monotonically increasing on the real axis. This implies that 
$\rho_0$ is the only zero of $1 - Q(z)$ with $|z| < \rho$.
Hence, the new dominant singularity must occur at the structural radius $\rho$, where the dominant small root becomes singular.
The new square-root singularity at $\rho$ thus contributes a summand of the type $n^{-3/2}\rho^{-n}$ to the asymptotic growth rate of $d_n$. 

For $\delta > 0$ the new dominant singularity instead happens to be a simple pole at $1/P(1) < \rho$ and thus we have
$$
d_n = \frac{\rho_0^{-n}}{\rho_0Q'(\rho_0)} + \mathcal{O}(P(1)^n).
$$
20. In the case that $\rho_0 = \rho$, the branching point of $u_1(z)$ leads to a square root behavior in the Puiseux expansion of $Q(z)$ for $z \to \rho$:
$$
1 - Q(z) = \underbrace{(1 - Q(\rho_0))}_{=0} +\, \eta\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho).
$$
Substituting $D(z) = (1-Q(z))^{-1}$ then yields
$$\begin{equation*}
D(z) = \frac{1}{\eta\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho)}
= \frac{1}{\eta\sqrt{1 - z/\rho}}\left(1 + \mathcal{O}\left(\sqrt{1 - z/\rho}\right)\right).
\end{equation*}$$
Finally, singularity analysis gives us
$$
d_n = [z^n]\frac{1}{\eta\sqrt{1 - z/\rho}}\left(1 + \mathcal{O}\left(\sqrt{1 - z/\rho}\right)\right)
= \frac{\rho^{-n}}{\eta\sqrt{\pi n}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right).
$$
34. In the case that $\mathcal{Z}$ is empty, the constant term does not vanish. Instead we expand the right-hand side into a geometric series:
$$\begin{align*}
D(z) &= \left(1 - \left(Q(\rho) - \eta\sqrt{1 - z/\rho} + \mathcal{O}(1-z/\rho_0)\right)\right)^{-1} \\
&= \sum_{k = 0}^\infty \left(Q(\rho) - \eta\sqrt{1 - z/\rho} + \mathcal{O}(1-z/\rho_0)\right)^k \\
&= \sum_{k=0}^\infty Q(\rho)^k - 
\left(
\sum_{k=1}^\infty k Q(\rho)^{k-1}
\right)  
\eta\sqrt{1 - z/\rho} + \mathcal{O}(1-z/\rho) \\
&= D(\rho) -\eta D^2(\rho)\sqrt{1 - z/\rho} + \mathcal{O}(1-z/\rho).
\end{align*}$$
Applying singularity analysis then yields
$$\begin{align*}
d_n &= [z^n]D(\rho) -\eta D^2(\rho)\sqrt{1 - z/\rho} + \mathcal{O}(1-z/\rho) \\ 
&= \frac{D(\rho)^2\eta \rho^{-n}}{2\sqrt{\pi n^3}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right). {\qquad\blacksquare}
\end{align*}$$
