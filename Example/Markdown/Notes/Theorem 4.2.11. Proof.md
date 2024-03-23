---
Theorem: "[[Theorem 4.2.11]]"
tags:
  - Proof
---

We start with the asymptotic growth rate of $[z^n]E_{\mathcal{M}_k}^\mathrm{alt}(z)$. 
According to Theorem [[Theorem 4.1.11]], we have 
$$ 
E_{\mathcal{M}_k}^\mathrm{alt}(z) = \frac{E(z)}{1 - Q(z)} = \frac{1}{1-z\frac{1-u_{1}(z)}{1-P(1)z}}\frac{u_{1}(z)}{z}.
$$
In order to determine the exponential growth rate of $[z^n]E_{\mathcal{M}_k}^\mathrm{alt}(z)$, we need to localize its dominant singularity.
By solving the quadratic kernel equation, one finds a square root singularity  at $\rho = 1/(k+2)$.
However, as it turns out there always exists a smaller, polar singularity $\rho_{0} < \rho$. This is vindicated by the fact that the drift of our step set is zero.
Hence, the dominant singularity can always be found as a zero of the denominator 
$$
g(z) := 1-P(1)z - z(1-u_{1}(z)).
$$
To find the zero, we use the kernel equation to observe 
$$
P\left(\frac{1}{2}\right) = \frac{2k+5}{2} = P\left(u_{1}\left(\frac{2}{2k+5}\right)\right).
$$
In particular, since $P(u)$ is injective on the interval $(0,\tau)$, with $\tau = 1$, this implies $u_1(2/(2k+5)) = 1/2$ and therefore
$$
g\left(\frac{2}{2k+5}\right) = 1 - \frac{2(k+2)}{2k+5} - \frac{1}{2k+5} = 0.
$$
Hence $E_{\mathcal{M}_k}^\mathrm{alt}(z)$ has a polar singularity at $\rho_0 := 2/(2k+5)$ and, according to Theorem [[Theorem 4.2.6]], admits the asymptotic expansion
$$
[z^n]E_{\mathcal{M}_k}^\mathrm{alt}(z) \sim \frac{E(\rho_0)}{\rho_0 Q'(\rho_0)} \left(\frac{2k+5}{2}\right)^n.
$$
To determine the constant factor, we firstly note that 
$$
E(\rho_0) = \frac{u_1(\rho_0)}{\rho_0} = \frac{1}{2\rho_0}.
$$
Secondly, we calculate
$$\begin{align*}
Q'(\rho_0) &= \frac{1 - u_1(\rho_0)}{1 - P(1)\rho_0} + \frac{P(1)\rho_0(1 - u_1(\rho_0))}{(1 - P(1)\rho_0)^2} - \frac{\rho_0 }{1 - P(1)\rho_0}u_1'(\rho_0) \\
&= M(\rho_0) + \frac{(k+2)/(2k+5)}{(1 - (2k+2)/(2k+5))^2} - \frac{2/(2k+5)}{1/(2k+5)}u_1'(\rho_0) \\
&= M(\rho_0) + (2k+4)\frac{1}{\rho_0} - 2 u_1'(\rho_0).
\end{align*}$$
To compute $M(\rho_0)$, we note that 
$$
\frac{M(\rho_0)}{E(\rho_0)} = 
\frac{1 - u_1(\rho_0)}{u_1(\rho_0)} \cdot \frac{\rho_0}{1 - P(1) \rho_0}
= \frac{2/(2k+5)}{1 - 2(k+2)/(2k+5)} = 2
$$
and therefore $M(\rho_0) = 1/\rho_0$.
Hence, it only remains to determine $u_1'(\rho_0)$. For that, we use the derivative of the kernel equation, which yields
$$
u_1'(\rho_0) = - \frac{P(u_1(\rho_0))}{\rho_0 P'(u_1(\rho_0))} 
= \frac{1}{\rho_0^2(u_1(\rho_0)^{-2} - 1)}
= \frac{1}{3\rho_0^2}.
$$
This implies
$$
Q'(\rho_0) = \frac{2k+5}{\rho_0} - \frac{2}{3\rho_0^2} 
= \frac{4}{3\rho_0^2} 
$$
and finally we obtain
$$
\frac{E(\rho_0)}{\rho_0 Q'(\rho_0)} = 
\frac{1}{2 \rho^2} \cdot \frac{3 \rho^2}{4} = \frac{3}{8}.
$$
The constant factor for the asymptotic growth of $[z^n]M_{\mathcal{M}_k}^\mathrm{alt}(z)$ is then, according to Theorem [[Theorem 4.2.7]], given by
$$\begin{equation*}
\frac{M(\rho_0)}{\rho_0 Q'(\rho_0)} = 2 \frac{E(\rho_0)}{\rho_0 Q'(\rho_0)} = \frac{3}{4}. {\qquad\blacksquare}
\end{equation*}$$
