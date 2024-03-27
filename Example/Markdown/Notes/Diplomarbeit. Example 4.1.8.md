---
tags:
  - Example
label: ex:motzkin_excursions
---
Let $E_\mathcal{M}^\mathrm{alt}(z)$ denote the generating function of Motzkin excursions with alternative catastrophes. According to Theorem [[Generating function for meanders and excursions with catastrophes]] we have 
$$
E_\mathcal{M}^\mathrm{alt}(z) = D(z)M_0(z) = \frac{E(z)}{1 - Q(z)} = \frac{u_1(z)}{z\left(1 - z\frac{1 - u_1(z)}{1 - 3z}\right)} = \frac{u_{1}(z)(1 - 3z)}{z(1 + (u_{1}(z) - 4)z)}.
$$
Extracting the first few coefficients yields 
$$ 
E_\mathcal{M}^\mathrm{alt}(z) = 1 + 2z + 6z^{2} + 19z^{3} + 63z^{4} + 213z^{5} + 729z^{6} + 2513z^{7} + \mathcal{O}(z^{8}).
$$
This sequence corresponds to [$\texttt{OEIS A059712}$](https://oeis.org/A059712).
For comparison, the generating function of Motzkin excursions with catastrophes satisfies
$$\begin{align*}
E_\mathcal{M}^\mathrm{cat}(z) &= \frac{3 u z -u}{\left(3 u^{2}+2 u +4\right) z^{2}+\left(-u^{2}-u -1\right) z} \\
&= 1 + z + 2z^2 + 5z^3 + 14z^4 + 41z^5 + 123z^6 + 374z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A073525}$](https://oeis.org/A073525).
