---
tags:
  - Example
---
According to Theorem [[Generating  function of walks and bridges with resets to zero]] we have
$$
B_\mathcal{D}^\mathrm{cat}(z) = \frac{W_0(z)}{1 - z(W(z) - W_0(z) - W_1(z) - W_{-1}(z))}.
$$
With the help of a computer algebra system we calculate
$$\begin{align*}
B_\mathcal{D}^\mathrm{cat}(z) &= -\frac{\left(2 z - 1\right) \left(1+\sqrt{1 - 4z^{2}}\right)^{2}}{\left(4 z^{3}-4 z^{2}-4 z +2\right) \sqrt{1 - 4z^{2}}+8 z^{4}+12 z^{3}-8 z^{2}-4 z +2} \\
&= -\frac{2z\left(2z - 1\right) v_1(z)^{2}}{\left(4 z^{3}-4 z^{2}-4 z +2\right)v_1(z) +4 z^{3}+4 z^{2}-2 z} \\
&= 1 + 2z^2 + 2z^3 + 8z^4 + 14z^5 + 40z^6 + 84z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence was not contained in the OEIS before writing this thesis, but it can now be found at [$\texttt{OEIS A369316}$](https://oeis.org/A369316).
Further, $B_\mathcal{D}^\mathrm{cat}(z)$ can be characterized as the only solution, having a power series expansion with non-negative coefficients at zero, of the quadratic equation
$$\begin{equation*}
\left(4z^{3} + 4z^{2} - 1\right) B^{2} + 2z \left(2z +1\right) B + 2z + 1.
\end{equation*}$$
For comparison, the generating function of Dyck bridges with alternative resets to zero satisfies
$$\begin{align*}
B_\mathcal{D}^\mathrm{alt}(z) &= \frac{W_0(z)}{1 - zW(z)} 
= \frac{\sqrt{1 - 4z^2}}{(1 - 3z)(1 + 2z)}\\
&= 1 + z + 5z^2 + 11z^3 + 39z^4 + 105z^5 + 335z^6 + 965z^7 + \mathcal{O}(z^8).
\end{align*}$$
This sequence was not contained in the OEIS before writing this thesis, but it can now be found at [$\texttt{OEIS A369982}$](https://oeis.org/A369982).
