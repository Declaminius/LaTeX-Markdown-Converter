---
Theorem: "[[Motzkin meanders]]"
tags:
  - Proof
---

Solving the kernel equation
$$
1 - z(1 + u + u^2) = 0
$$
for the Motzkin family of directed lattice paths yields the unique small branch
$$
u_1(z) = \frac{1 - z - \sqrt{1 - 2z - 3z^2}}{2z}.
$$
Now, all that remains is to plug $u_1(z)$ into Equation [[gf_meanders]] and we obtain
$$
M_{\mathcal{M}}(z,u) = \frac{u - u_1(z)}{u(1 - zP(u))} = \frac{2z(u + 1) - 1 + \sqrt{1 - 2z - 3 z^{2}}}{2z\left(u - z \left(u^{2}+u + 1\right)\right)}.
$$
Setting $u = 1$ then yields
$$\begin{equation*}
M_{\mathcal{M}}(z,1) = \frac{1 - 3z - \sqrt{1 - 2z - 3z^2}}{6z^2 - 2z}. {\qquad\blacksquare}
\end{equation*}$$
