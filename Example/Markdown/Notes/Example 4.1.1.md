---
tags:
  - Example
label: ex:dyck_meanders_alt_cats
---
Let $M_\mathcal{D}^\mathrm{alt}(z,1)$ denote the generating function of Dyck meanders with alternative catastrophes.
According to Theorem [[Theorem 4.1.11]] we have 
$$\begin{equation*} 
M_\mathcal{D}^\mathrm{alt}(z,1) = D(z)M(z,1) = D(z) \frac{1 - u_1(z)}{1 - zP(1)}
= \frac{1 - u_1(z)}{(1 - Q^\mathrm{alt}(z))(1 - 2z)}, 
\end{equation*}$$
with $u_1(z) = \frac{1 - \sqrt{1 - 4z^2}}{2z}$ being the solution to the kernel equation $1 - z(u^{-1} + u) = 0$.
Plugging in the formula for the generating function $M(z,1)$, derived in Theorem [[Theorem 2.2.5]], then yields
$$ 
Q^\mathrm{alt}(z) = zM(z,1) = z\frac{1 - u_1(z)}{1 - zP(1)} = z\frac{1 - \frac{1 - \sqrt{1 - 4z^{2}}}{2z}}{1-2z}. 
$$
With the help of our favorite computer algebra system we finally arrive at
$$\begin{align*} 
M_\mathcal{D}^\mathrm{alt}(z,1) &= \frac{1 - u_1(z)}{(1-Q^\mathrm{alt}(z))(1-2z)} 
= \frac{1 - u_{1}(z)}{1 + (u_{1}(z) - 3)z} \\
&= 1 + 2z + 5z^{2} + 12z^{3} + 30z^{4} + 74z^{5} + 185z^{6} + 460z^{7} + \mathcal{O}(z^{8}). 
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A054341}$](https://oeis.org/A054341).
For the generating function of Dyck meanders with regular catastrophes,
we need to compute 
$$
Q^\mathrm{cat}(z) = z(M(z) - E(z) - M_1(z))
$$
instead. The formulae
$$
M(z) = \frac{1 - u_1(z)}{1 - zP(1)}, \qquad E(z) = \frac{u_1(z)}{z}
$$
are already known from Theorem [[Theorem 2.2.5]] and the remaining unknown $M_1(z)$ can be determined using a simple last passage decomposition.
Let $\omega_M$ be an arbitrary meander ending at altitude 1. Split $\omega_M$ into two parts by cutting at the point when it leaves the $x$-axis for the last time. The first part is then simply an excursion counted by $E(z)$. The final part is also an excursion, if we discard the first up-step. This decomposition shows that $M_1(z) = zE(z)^2$. The remaining calculations remain in the hands of our favorite computer algebra system, which returns
$$\begin{align*}
M_\mathcal{D}^\mathrm{cat}(z,1) &= \frac{z(u_1(z) - 1)}{z^2 + (z^2 + z - 1)u_1(z)} \\
&= 1 + z + 2z^2 + 4z^3 + 8z^4 + 17z^5 + 35z^6 + 75z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A274115}$](https://oeis.org/A274115).
