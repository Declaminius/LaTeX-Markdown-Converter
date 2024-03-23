---
Theorem: "[[Proposition 3.2.5]]"
tags:
  - Proof
---

By Theorem [[Theorem 2.2.5]] we know the generating function for excursions to be 
$$
E(z) = - \frac{u_{1}(z)u_{2}(z)}{z}.
$$
Further, we can generate an algebraic equation satisfied by $E(z)$ via computer algebra:
$$
z^{4}E^{4} - (2z^{3}+z^{2})E^{3} + (3z^{2}+2z)E^{2} - (2z+1)E + 1 = 0.
$$
We rewrite this equation in order to be amenable to Lagrange's inversion formula:
$$
zE(z) = z\left(\frac{1}{1-zE(z)}-zE(z)\right)^{2} = z\phi(zE(z)).
$$
Hence we have
$$\begin{align*}
[z^{n}]E(z) &= \frac{1}{n+1}[z^{n}]\left(\frac{1}{1-z}-z\right)^{2n+2} \\
&= \frac{1}{n+1}[z^n] \sum_{k=0}^{2n+2} \binom{2n+2}{k} (-z)^k \left(\frac{1}{1 - z}\right)^{2n+2-k} \\
&= \frac{1}{n+1}\sum_{k=0}^{n} (-1)^{n-k}  \binom{2n+2}{n - k}[z^k]\left(\frac{1}{1 - z}\right)^{n+k+2} \\
&= \frac{1}{n+1}\sum_{k=0}^{n}(-1)^{n+k}\binom{2n+2}{n-k}\binom{n+2k+1}{k}.
\end{align*}$$
The second expression can be derived by rewriting $\phi(z) = \left(1 + \frac{z^{2}}{1-z}\right)^2$.
