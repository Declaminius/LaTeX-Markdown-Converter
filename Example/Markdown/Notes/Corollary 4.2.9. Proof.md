---
Theorem: "[[Corollary 4.2.9]]"
tags:
  - Proof
---

Since we are still dealing with symmetric step sizes, the dominant singularity is still guaranteed to be a simple pole. In this case, we find $\rho_0 = 2/7$. An application of Theorem [[Theorem 4.2.6]]
together with some computer algebra yields
$$
[z^n] M_\mathcal{M}^\mathrm{alt}(z,1) = \frac{3}{4} \left(\frac{7}{2}\right)^n + \mathcal{O}\left(\frac{P(1)^n}{\sqrt{n^3}}\right).
$$
We continue by subtracting the pole in order to get to the asymptotic behavior at the square root singularity at $\rho = 1/3$.
At $\rho = 1/3$ we develop 
$$
G(z) := M_\mathcal{M}^\mathrm{alt}(z,1) + \frac{3}{14} \left(z -\frac{2}{7}\right)^{-1}
$$
into a Puiseux series with critical exponent $\alpha = 1/3$: 
$$
G(z) = \frac{9}{2} - 3\sqrt{3}(1-3z)^{1/2}  + 27(1-3z) + \mathcal{O}((1-3z)^{3/2}).
$$
Translating this expansion to coefficient asymptotics using the standard function scale (Theorem [[Theorem 2.3.1]]) and the Transfer Theorem [[Theorem 2.3.4]] yields the claimed result.

For excursions, an application of Theorem [[Theorem 4.2.6]] yields
$$
[z^{n}]E_\mathcal{M}^\mathrm{alt}(z) = \frac{3}{8} \left(\frac{7}{2}\right)^n + o(K^n)
$$
for some $K < 7/2$. Now we can continue by subtracting the pole in order to get to the asymptotic behavior at the square root singularity at $\rho = 1/3$.
At $\rho = 1/3$ we develop 
$$
G(z) := E_\mathcal{M}^\mathrm{alt}(z) + \frac{3}{28} \left(z -\frac{2}{7}\right)^{-1}
$$
into a Puiseux series with critical exponent $\alpha = 1/3$: 
$$
G(z) = \frac{9}{4} - 3\sqrt{3}(1-3z)^{1/2}  + \frac{45}{4}(1-3z) + \mathcal{O}((1-3z)^{3/2}).
$$
Translating this expansion to coefficient asymptotics using the standard function scale (Theorem [[Theorem 2.3.1]]) and the Transfer Theorem [[Theorem 2.3.4]] yields the claimed result.
