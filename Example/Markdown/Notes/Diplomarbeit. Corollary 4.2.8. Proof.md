---
Theorem: "[[Diplomarbeit. Corollary 4.2.8]]"
tags:
  - Proof
---

Recall the generating function of Dyck meanders with alternative catastrophes
$$
M_\mathcal{D}^\mathrm{alt}(z,1) = \frac{M_\mathcal{D}(z,1)}{1 - zM_\mathcal{D}(z,1)} = \frac{1-u_1(z)}{1 + (u_1(z) - 3)z}. 
$$
Due to the symmetric step set of Dyck paths we have $\delta = 0$. Hence we already know that the dominant singularity has to be a simple pole at a point $\rho_0 < \rho$. In fact, by setting the denominator zero we have $\rho_0 = 2/5 < 1/2$. Plugging these numbers into [[meanders_asymptotics]] we obtain
$$\begin{align*}
\frac{M_\mathcal{D}(\rho_0,1)}{\rho_0 \cdot Q_\mathcal{D}'(\rho)} &= \frac{5/2}{2/5 \cdot 25/3} = \frac{3}{4}.
\end{align*}$$
Hence, we have
$$
[z^{n}]M_\mathcal{D}^\mathrm{alt}(z,1) = \frac{3}{4}\left(\frac{5}{2}\right)^n + \mathcal{O}\left(\frac{2^n}{\sqrt{n^3}}\right).
$$
However, to get the full asymptotic expansion we need to dig deeper.
We subtract the simple pole in order to expand the function at the branching point $\rho = 1/2$. This gives 
$$
G(z) := M_\mathcal{D}^\mathrm{alt}(z,1) + \frac{3}{10} \left(z -\frac{2}{5}\right)^{-1} = 1 -2\sqrt{2}\sqrt{1-2z} + 7\left(1-2z\right) + \mathcal{O}\left(1-2z\right)^{3/2}.
$$
Now we apply the standard function scale (Theorem [[Standard function scale]]) to $\sigma(u) = 1-2\sqrt{2}\sqrt{1-u} + 7(1-u)$ and obtain 
$$
\sigma_{n} = [u^{n}]\sigma(u) = \frac{2\sqrt{2}}{\sqrt{\pi n^{3}}}\left(\frac{1}{2} + \mathcal{O}\left(\frac{1}{n}\right)\right).
$$
After translating the error $\tau(u) = (1-u)^{3/2}$ using the Transfer Theorem [[mathcalO-Transfer]] we finally get
$$\begin{equation*}
[z^{n}]G(z) = \frac{2^{n+1/2}}{\sqrt{\pi n^{3}}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right) + \mathcal{O}\left(\frac{2^{n}}{\sqrt{n^{5}}}\right)
= \frac{2^{n+1/2}}{\sqrt{\pi n^{3}}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right). {\qquad\blacksquare}
\end{equation*}$$

For the asymptotic behavior of Dyck excursions with alternative catastrophes we first recall their generating function to be
$$
E_\mathcal{D}^\mathrm{alt}(z) = \frac{E_\mathcal{D}(z)}{1 - zM_\mathcal{D}(z,1)} = \frac{u_1(z)(1 - 2z)}{z(1 + (u - 3)z)}. 
$$
We already observed that the dominant singularity is a simple pole at $\rho_0 = 2/5$. Now we can compute
$$
\frac{E_\mathcal{D}(\rho_0)}{\rho_0 Q_\mathcal{D}'(\rho_0)} = \frac{5/4}{2/5 \cdot 25/3} = \frac{3}{8}.
$$
and continue by subtracting the pole in order to get to the asymptotic behavior at the square root singularity at $\rho = 1/2$.
At $\rho = 1/2$ we develop 
$$
G(z) := E_\mathcal{D}^\mathrm{alt}(z) + \frac{3}{20} \left(z -\frac{2}{5}\right)^{-1}
$$
into a Puiseux series with critical exponent $\alpha = 1/2$: 
$$
G(z) = 3 - 2\sqrt{2}(1-2z)^{1/2}  + 13(1-2z) + \mathcal{O}((1-2z)^{3/2}).
$$
Translating this expansion to coefficient asymptotics using the standard function scale (Theorem [[Standard function scale]]) and the Transfer Theorem [[mathcalO-Transfer]] yields the claimed result.
