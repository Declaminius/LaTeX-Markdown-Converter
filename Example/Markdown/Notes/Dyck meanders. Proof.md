---
Theorem: "[[Dyck meanders]]"
tags:
  - Proof
---

The kernel equation for Dyck walks reads $1 - z\left(\frac{1}{u} + u\right) = 0.$
Solving this equation for $u$ yields the unique small branch 
$$
u_{1} = \frac{1 - \sqrt{1 - 4z^{2}}}{2z}.
$$
Applying Theorem [[Generating function of meanders and excursions]] we find the generating function for Dyck meanders to be 
$$
M_\mathcal{D}(z,u) = \frac{u - u_1(z)}{u(1 - zP(u))}
= \frac{1 - 2zu - \sqrt{1 - 4z^2}}{2z(z(1 + u^2) - u)}.
$$
Setting $u = 1$ then yields
$$\begin{equation*}
M_\mathcal{D}(z,1) = \frac{1 - 2z - \sqrt{1 - 4z^2}}{4z^2 - 2z}.
\end{equation*}$$
To obtain the generating function for meanders of even length, we apply a last passage decomposition. Let $\omega_0$ be an arbitrary meander of even length. Hence, it must end at an even altitude. Now we split $\omega_0$ every time it leaves altitude $2k$ for a last time. That means, $\omega_0$ is composed of a Dyck excursion, followed by a sequence of subpaths, starting at altitude~$k$ and ending at $k + 2$ without returning to altitude $k$ at any point after the start. Each of these subpaths can thus be described as a **NE**-step up to altitude $k + 1$, followed by an excursion and finally another **NE**-step up to altitude $k + 2$. Considering that the variable $z$ counts twice the length of a meander (or equivalently the number of **NE**-steps of a meander) the generating function for one of these subpaths reads $z(uD(z))^2$. Thus, we obtain the generating function
$$
G(z,u) = \frac{D(z)}{1 - z(uD(z))^2}.
$$
Setting $u = 1$ yields
$$\begin{equation*}
G(z,1) = \frac{D(z)}{1 - zD(z)^2} = \frac{D(z)}{2 - D(z)} = \frac{1 - \sqrt{1 - 4z}}{\sqrt{1 - 4z} - (1 - 4z)} = \frac{1}{\sqrt{1 - 4z}}
= \sum_{n = 0}^\infty \binom{2n}{n} z^n.
\end{equation*}$$
Further, a last passage decomposition on Dyck meanders of odd length splits $\omega_0$ into a Dyck excursion, followed by the last **NE**-step to leave from altitude $0$ and a final Dyck meander of even length. This translates to the formula
$$
U(z,u) = u D(z) G(z,u).
$$
Setting $u = 1$ yields
$$\begin{equation*}
U(z,1) = \frac{D(z)}{\sqrt{1 - 4z}} = \frac{1}{2z}\left(\frac{1}{\sqrt{1 - 4z}} - 1\right)
= \sum_{n = 0}^\infty \frac{1}{2} \binom{2n + 2}{n + 1} z^n
= \sum_{n = 0}^\infty \binom{2n + 1}{n} z^n. {\qquad\blacksquare}
\end{equation*}$$
