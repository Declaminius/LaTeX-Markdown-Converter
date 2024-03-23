---
Theorem: "[[Lemma 4.2.4]]"
tags:
  - Proof
---

Due to its combinatorial origin, $D(z) = (1-Q(z))^{-1}$ is a power series with positive coefficients. 
Hence, Pringsheim's theorem applies, which tells us that there exists a singularity on the intersection of its radius of convergence with the positive real axis. 
This singularity has to be either a singularity of $Q(z)$ or the smallest positive zero of $1 - Q(z)$. 
In both cases, it must be the only dominant singularity.
In the first case, let $\rho_Q$ denote the dominant singularity of $Q(z)$.
In this case, the argument above shows that $\rho_Q$ must coincide with the unique dominant singularity of $M(z)$ and thus we have $\rho_Q = \rho_M = \rho$.

In the second case, let $\rho_0$ be the smallest positive zero of $1 - Q(z)$. Now the aperiodicity of $Q(z)$, together with the fact that all its coefficients are positive implies that
$$
\forall z \in \C \colon (|z| = \rho_0, z \neq \rho_0) \implies |Q(z)| < Q(|z|) = 1
$$
and therefore the only dominant singularity has to lie on the positive real axis.
Now we will determine the location of the dominant singularity. This will depend on the sign of the drift $\delta := P'(1)$:
- 
For a positive drift $\delta \geq 0$ we observe that the prefactor $(1-zP(1))^{-1}$ in 
$$
M(z) = \frac{\prod_{j=1}^c (1 - u_j(z))}{1 - zP(1)}
$$ 
possesses a simple pole at $z = 1/P(1)$. We show now that this pole cannot be cancelled by the factors $(1 - u_j(z))$. First we want to evaluate $u_1$ at the structural constant $\tau$. By the definition of the structural radius and the kernel equation, one has
$$
P(\tau) = \frac{1}{\rho} = P(u_1(\rho))
$$
As $P(u)$ is injective on the interval $(0,\tau]$, this implies $u_1(\rho) = \tau$. Next, since $P'(1) \geq 0$ we observe that $\tau \leq 1$. Further, $u_1$ is monotonically increasing in $[0,\rho]$, so we have 
$$
u_1\left(1/P(1)\right) < u_1(\rho) = \tau \leq 1.
$$
Finally, all other small roots are dominated by $u_1$ and hence cannot reach one either.
Thus, the pole at $z = 1/P(1)$ of the prefactor is in fact also a pole of $M(z)$ and we have 
$$
\lim_{z \to (1/P(1))^-}Q(z) = +\infty.
$$
However, this pole cannot be the dominant singularity of $D(z) = (1 - Q(z))^{-1}$, since by the continuity of $Q(z)$, together with $Q(0) = 0$, there must be a solution $\rho_0$ of $1 - Q(z) = 0$ with
$$
0 < \rho_0 < \frac{1}{P(1)} \leq \rho.
$$ 
- 
In the case of a negative drift $\delta < 0$, the pole in the prefactor does cancel out with $1 - u_1(z)$.
This is due to the kernel equation for $u_1$, which yields
$$
P\left(u_1\left(1/P(1)\right)\right) = P(1),
$$
and the fact that for $u \in [0,\tau]$, with $\tau > 1$, the function $1/P(u)$ is continuously increasing.
Thus the kernel equation admits a unique positive solution, which coincides with the principal small branch $u_1(z)$.
Hence, we have that $|Q(z)|$ is bounded for $|z| < \rho$.
Since $u_1(z)$ has a square root singularity at $|z| = \rho$ we also have $\rho_Q = \rho$. Now we only need to compare whether $\rho_0$ or $\rho_Q$ yields the smaller singularity.
Finally, since $Q(z)$ is monotonically increasing on the real axis, it suffices to compare its value at its maximum $Q(\rho)$. {\qquad\blacksquare}
