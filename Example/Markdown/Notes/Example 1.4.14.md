---
tags:
  - Example
---
Consider again the function $E(z)$ defined via
$$
E(z) = - \frac{u_1(z)u_2(z)}{z}
$$
and let $K(z,u) = z(1 + u + u^3 + u^4)$.
In this case, the system of polynomial equations can be defined as
$$\begin{align*}
P_1(E, z, u_1, u_2) &:= z E + u_1(z)u_2(z), \\
P_2(E, z, u_1, u_2) &:= K(z,u_1), \\
P_3(E, z, u_1, u_2) &:= K(z,u_2).
\end{align*}$$
We begin by eliminating $u_2$:
$$\begin{equation*}
Q(E,z,u_1) := \textbf{R}(P_1,P_3,u_2) = -z \left(E^{4} z^{4}-E^{3} u_{1} z^{3}-E^{2} u_{1}^{2} z -E \,u_{1}^{3} z +u_{1}^{4}\right).
\end{equation*}$$
Next, we eliminate $u_1$ and obtain the desired polynomial equation in $E$ and $z$:
$$\begin{align*}
P(E,z) := \textbf{R}(Q,P_2,u_2) &= z^{8} \left(z E +1\right)^{4}\left(E^{4} z^{4}+E^{3} z^{3}+2 E^{3} z^{2}+E^{2}+z E +2 E +1\right) \\
&\left(E^{4} z^{4}-2 E^{3} z^{3}-E^{3} z^{2}+3 E^{2} z^{2}+2 E^{2} z -2 z E -E +1\right)^{2}. {\qquad\blacksquare}
\end{align*}$$
