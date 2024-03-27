---
tags:
  - Example
---
Let $M_\mathcal{M}^\mathrm{alt}(z,1)$ denote the generating function of Motzkin meanders with alternative catastrophes.
According to Theorem [[Generating function for meanders and excursions with catastrophes]] we have 
$$\begin{align*} 
M_\mathcal{M}^\mathrm{alt}(z,1) &= \frac{M(z,1)}{(1 - zM(z,1))} = \frac{1 - u_1(z)}{\left(1 - z\frac{1 - u_1(z)}{1 - 3z}\right)(1 - 3z)} = \frac{1 - u_{1}(z)}{1 + (u_{1}(z) - 4)z}, 
\end{align*}$$
with $u_1(z) = \frac{1 - z - \sqrt{1 - 2z - 3z^{2}}}{2z}$ being the only small solution to the kernel equation 
$$
u - z(1 + u + u^2) = 0.
$$
Furthermore, we can extract the first coefficients to see 
$$
M_\mathcal{M}^\mathrm{alt}(z,1) = 
1 + 3z + 10z^{2} + 34z^{3} + 117z^{4} + 405z^{5} + 1407z^{6} + 4899z^{7} + \mathcal{O}(z^{8}).
$$
This sequence corresponds to [$\texttt{OEIS A059738}$](https://oeis.org/A059738).
For comparison, the generating function of Motzkin meanders with catastrophes satisfies
$$\begin{align*}
M_\mathcal{M}^\mathrm{cat}(z) &= \frac{u_1(z) - 1}{u_1(z)^{2} \left(3 z - 1\right)+\left(2 z -1\right) u_1(z) + 4z -1} \\
&= 1 + 2z + 5z^2 + 14z^3 + 41z^4 + 123z^5 + 374z^6 + 1147z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence corresponds to [$\texttt{OEIS A054391}$](https://oeis.org/A054391), which appears as a interpolation between the famous Catalan and Motzkin numbers.
