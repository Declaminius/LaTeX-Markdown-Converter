---
Theorem: "[[Asymptotics of [zn]G_1,1(z)]]"
tags:
  - Proof
---

In Proposition [[Closed-form expression for the coefficients of G_1,1(z)]] we derived the algebraic equation
$$
P(z,E) := z^{4}E^{4} - (2z^{3}+z^{2})E^{3} + (3z^{2}+2z)E^{2} - (2z+1)E + 1 = 0
$$
for the generating function $G_{1,1}(z)$. The candidates for its singular points are found within the exceptional set 
$$
\Xi[P] := \{\, z \mid \textbf{R}(P(z,E), \partial_E P(z,E), E) = 0 \,\},
$$
where $\textbf{R}(z)$ is the resultant defined in Definition [[Resultant]]. Solving the equation $\textbf{R}(z) = 0$ yields again $\rho = 1/4$ as the unique dominant singularity. Now we can let our favorite computer algebra system compute the Puiseux expansion
$$\begin{align*}
G_{1,1}(z) = 6 - 2\sqrt{5} &+ \frac{20 - 12\sqrt{5}}{5}\sqrt{1 - 4z} + \frac{250 - 94\sqrt{5}}{25}(1 - 4z) \\
&+ \frac{1000 - 536\sqrt{5}}{125}(1 - 4z)^{3/2} + \mathcal{O}\left((1-4z)^2\right).
\end{align*}$$
We determine the correct branch of the Puiseux expansion by guessing and checking the asymptotic approximations against the actual values of the counting sequence.
Applying the standard function scale (Theorem [[Standard function scale]]) in conjunction with the Transfer Theorem [[mathcalO-Transfer]] we finally obtain
$$\begin{align*}
[z^n] G_{1,1}(z) &= \frac{6\sqrt{5} - 10}{5}\frac{4^{n}}{\sqrt{\pi n^{3}}}
\left(
1 + \frac{3}{8n} + 
\mathcal{O}\left(\frac{1}{n^{2}}\right)
\right) \\
&+
\frac{1000 - 536\sqrt{5}}{125}\frac{4^{n}}{\sqrt{\pi n^{5}}}
\left(
\frac{3}{4} + \mathcal{O}\left(\frac{1}{n}\right)
\right) +
\mathcal{O}\left(\frac{4^{n}}{\sqrt{n^{5}}}\right) \\
&= \frac{6\sqrt{5} - 10}{5\sqrt{\pi}}\frac{4^n}{\sqrt{n^3}}
\left(
1 + \frac{48\sqrt{5}-381}{200n} + \mathcal{O}\left(\frac{1}{n^2}\right)
\right). {\qquad\blacksquare}
\end{align*}$$
