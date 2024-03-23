---
tags:
  - Example
---
Let $E_\mathcal{D}^\mathrm{alt}(z)$ denote the generating function of Dyck excursions with alternative catastrophes.
According to Theorem [[Theorem 4.1.11]] we have $$
E_\mathcal{D}^\mathrm{alt}(z) = D(z)M_0(z) = \frac{E(z)}{1 - Q(z)} = \frac{u_1(z)}{z\left(1 - z\frac{1 - u_1(z)}{1- 2z}\right)} = \frac{u_1(z)(1-2z)}{z(1+z(u_1(z)- 3))}.
$$
Extracting the first few coefficients then gives 
$$ 
E_\mathcal{D}^\mathrm{alt}(z) = 1 + z + 3z^{2} + 6z^{3} + 16z^{4} + 37z^{5} + 95z^{6} + 230z^{7} + \mathcal{O}(z^{8}).
$$
This sequence was not contained in the OEIS before writing this thesis, but it can now be found at [$\texttt{OEIS A369432}$](https://oeis.org/A369432).
For comparison, the generating function of Dyck excursion with catastrophes satisfies
$$\begin{align*}
E_\mathcal{D}^\mathrm{cat}(z) &= \frac{(2z-1)u_1(z)}{z^2 + (z^2+z-1)u_1(z)}
= 1 + z^2 + z^3 + 3z^4 + 5z^5 + 12z^6 + 23z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A224747}$](https://oeis.org/A224747).
