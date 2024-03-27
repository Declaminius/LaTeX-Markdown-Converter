---
tags:
  - Example
---
Let $E_{\mathcal{M}_2}^\mathrm{alt}(z)$ denote the generating function of 2-Motzkin excursions with alternative catastrophes.
According to Theorem [[Generating function for meanders and excursions with catastrophes]] we have 
$$
E_{\mathcal{M}_2}^\mathrm{alt}(z) = D(z)M_0(z) = \frac{E(z)}{1 - Q(z)} = \frac{u_1(z)}{z\left(1 - z\frac{1 - u_1(z)}{1 - 4z}\right)} = \frac{u_{1}(z)(1 - 4z)}{z(1 + (u_{1}(z) - 5)z)}.
$$
Extracting the first few coefficients yields
$$\begin{align*}
E_{\mathcal{M}_2}^\mathrm{alt}(z) &= 1 + 3z + 11z^{2} + 44z^{3} + 184z^{4} + 789z^{5} + 3435z^{6} + 15100z^{7} + \mathcal{O}(z^{8}).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A059714}$](https://oeis.org/A059714).
For comparison, the generating function of 2-Motzkin excursions with catastrophes satisfies
$$\begin{align*}
E_{\mathcal{M}_2}^\mathrm{cat}(z) &= \frac{4 u_1(z) z - u_1(z)}{\left(4 u_1(z)^{2}+3 u_1(z) +5\right) z^{2}+\left(-u_1(z)^{2}-u_1(z) -1\right) z} \\
&= 1 + 2z + 5z^2 + 15z^3 + 51z^4 + 187z^5 + 716z^6 + 2811z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A073525}$](https://oeis.org/A073525).
