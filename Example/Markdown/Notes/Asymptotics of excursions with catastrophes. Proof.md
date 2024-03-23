---
Theorem: "[[Asymptotics of excursions with catastrophes]]"
tags:
  - Proof
---

Since the generating function $C_0(z)$ of excursions with (alternative) catastrophes satisfies $C_0(z) = D(z)E(z)$, the dominant singularity is either a simple pole of $D(z)$ at $\rho_0$, or a square root singularity at the structural radius $\rho = 1/P(\tau)$. Note that the cases $\rho_0 = \rho$ and $\mathcal{Z} = \emptyset$ are only possible for $\delta < 0$. In the case of $\rho_{0} < \rho$ we have
$$\begin{align*}
\frac{E(z)}{1-Q(z)} &= \frac{E(\rho_{0}) + \mathcal{O}\left(1 - z/\rho_{0}\right)}{\rho Q'(\rho_{0})\left(1- z/\rho_{0}\right) + \mathcal{O}\left(\left(1-z/\rho_{0}\right)^{2}\right)} 
= \frac{E(\rho_{0})}{\rho Q'(\rho_{0})}\left(1- z/\rho_{0}\right)^{-1} + \mathcal{O}(1).
\end{align*}$$
Applying singularity analysis then yields
$$
e_{n} = \frac{E(\rho_{0})\rho_{0}^{-n}}{\rho_{0}Q'(\rho_{0})} + \mathcal{O}(\rho^{n}).
$$
In the case of $\rho_{0}= \rho$ we have analogously to the proof of Theorem [[Asymptotics of excursions ending with a catastrophe]] that
$$
C_0(z) = \frac{E(\rho_{0})}{\eta\sqrt{1- z/\rho}}\left(1 + \mathcal{O}\left(\sqrt{1 - z/\rho}\right)\right).
$$
The process of singularity analysis then gives
$$
e_{n} = \frac{E(\rho)}{\eta}\frac{\rho^{-n}}{\sqrt{\pi n}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right).
$$
In the final case that $\mathcal{Z}$ is empty, the results in the proof of \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 3]]\] give us the asymptotic expansion
$$\begin{align*}
E(z) &= E(\rho) - \frac{(-1)^{c-1}}{p_{-c}\rho} \prod_{j=2}^c u_j(\rho)\sqrt{2\frac{P(\tau)}{P''(\tau)}}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho) \\
&= E(\rho) - \frac{E(\rho)}{u_1(\rho)}\sqrt{2\frac{P(\tau)}{P''(\tau)}}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho).
\end{align*}$$
Combined with the results from Theorem [[Asymptotics of excursions ending with a catastrophe]] and the fact that $u_1(\rho) = \tau$ we thus have
$$
C_0(z) = \frac{E(z)}{1 - Q(z)} = \frac{E(\rho) - \frac{E(\rho)}{\tau}\sqrt{2\frac{P(\tau)}{P''(\tau)}}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho)}{(1 - Q(\rho_0)) + \eta\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho)}.
$$
Like in the previous theorem, we develop the denominator into a geometric series and obtain
$$\begin{align*}
C_0(z) &= \frac{E(\rho)}{1 - Q(\rho)} - 
\left(
\frac{
\frac{E(\rho)}{\tau}\sqrt{2\frac{P(\tau)}{P''(\tau)}}}
{1 - Q(\rho)
} + 
\eta \frac{E(\rho)}{(1 - Q(\rho))^2}\sqrt{1 - z/\rho} + 
\mathcal{O}(1 - z/\rho)
\right). \\
&= C_0(\rho) - C_0(\rho)\left(
\frac{1}{\tau}\sqrt{2\frac{P(\tau)}{P''(\tau)}} + \eta D(\rho)
\right)\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho).
\end{align*}$$
Now the results follow from the standard function scale (Theorem [[Standard function scale]]) and the Transfer Theorem [[Theorem 2.3.4]].
