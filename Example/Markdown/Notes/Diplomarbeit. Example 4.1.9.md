---
tags:
  - Example
---
Let $M_{\mathcal{M}_2}^\mathrm{alt}(z)$ denote the generating function for 2-Motzkin meanders with alternative catastrophes.
According to Theorem [[Generating function for meanders and excursions with catastrophes]] we have 
$$
M_{\mathcal{M}_2}^\mathrm{alt} = D(z)M(z) = \frac{M(z)}{1 - Q(z)} = \frac{1 - u_1(z)}{\left(1 - z\frac{1 - u_1(z)}{1 - 4z}\right)(1 - 4z)} = \frac{1 - u_{1}(z)}{1 + (u_{1}(z) - 5)z},
$$
with $u_1(z) = \frac{1 - 2z - \sqrt{1-4z}}{2z}$ being the solution to 
the kernel equation 
$$
u - z(u^{2} + 2u + 1) = 0.
$$
Extracting the first few coefficients yields 
$$ 
M_{\mathcal{M}_2}^\mathrm{alt}(z) = 1 + 4z + 17z^{2} + 74z^{3} + 326z^{4} + 1446z^{5} + 6441z^{6} + 28770z^{7} + \mathcal{O}(z^{8}).
$$
This sequence corresponds to [$\texttt{OEIS A049027}$](https://oeis.org/A049027), which appears as a row sum of a generalized Pascal's triangle.
For comparison, the generating function of 2-Motzkin meanders with catastrophes satisfies
$$\begin{align*}
M_{\mathcal{M}_2}^\mathrm{cat}(z) &= \frac{u_1(z) - 1}{u_1(z)^{2} \left(1 - 4z\right)+\left(1 - 3 z\right) u_1(z) + 5 z -1} \\
&= 1 + 3z + 10z^2 + 36z^3 + 136z^4 + 529z^5 + 2095z^6 + 8393z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence was not contained in the OEIS before writing this thesis, but it can now be found at [$\texttt{OEIS A369436}$](https://oeis.org/A369436).
