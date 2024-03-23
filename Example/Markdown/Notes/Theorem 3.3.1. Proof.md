---
Theorem: "[[Theorem 3.3.1]]"
tags:
  - Proof
---

In Example [[Example 3.1.4]] we derived the expressions
$$\begin{align*}
G_{0,1}(z) &= -\frac{1}{2} + \frac{1}{2}\sqrt{\frac{2-3z-2\sqrt{1-4z}}{z}}, \\
G_{0,2}(z) &= \frac{3 - \sqrt{1-4z} - \sqrt{2+12z+2\sqrt{1-4z}}}{4z}.
\end{align*}$$
The dominant singularity of both of these functions is at $\rho_{0} = 1/4$. Computing the Puiseux series at $\rho_0$ yields
$$\begin{align*}
G_{0,1}(z) &= - \frac{1-\sqrt{5}}{2} - \frac{2}{\sqrt{5}}(1-4z)^{1/2} + \frac{6}{5\sqrt{5}}(1-4z) - \frac{26}{25\sqrt{5}}(1-4z)^{3/2} + \mathcal{O}((1-4z)^{2}), \\
G_{0,2}(z) &= \left(3 - \sqrt{5}\right) - \frac{5 + \sqrt{5}}{5}(1-4z)^{1/2} + \frac{75-17\sqrt{5}}{25}(1-4z) \\
&- \frac{125 +  33\sqrt{5}}{125}(1 - 4z)^{3/2} + \mathcal{O}\left((1 - 4z)^2\right).
\end{align*}$$
Applying the standard function scale (Theorem [[Theorem 2.3.1]]) in conjunction with the Transfer Theorem [[Theorem 2.3.4]] we obtain
$$\begin{align*}
[z^{n}]G_{0,1}(z) &= \frac{4^{n}}{\sqrt{5\pi n^{3}}}
\left(
1 + \frac{3}{8n} + 
\mathcal{O}\left(\frac{1}{n^{2}}\right)
\right) - 
\frac{26}{25\sqrt{5}}\frac{4^{n}}{\sqrt{\pi n^{5}}}
\left(
\frac{3}{4} + \mathcal{O}\left(\frac{1}{n}\right)
\right) + 
\mathcal{O}\left(\frac{4^{n}}{\sqrt{n^{7}}}\right) \\
&= \frac{4^{n}}{\sqrt{5\pi n^{3}}}
\left(
1 - \frac{81}{200n} + 
\mathcal{O}\left(\frac{1}{n^{2}}\right)
\right),
\end{align*}$$
as well as
$$\begin{align*}
[z^{n}]G_{0,2}(z) &= \frac{5 + \sqrt{5}}{10}\frac{4^{n}}{\sqrt{\pi n^{3}}}
\left(
1 + \frac{3}{8n} + 
\mathcal{O}\left(\frac{1}{n^{2}}\right)
\right) \\
&-
\frac{125 + 33\sqrt{5}}{125}\frac{4^{n}}{\sqrt{\pi n^{5}}}
\left(
\frac{3}{4} + \mathcal{O}\left(\frac{1}{n}\right)
\right) +
\mathcal{O}\left(\frac{4^{n}}{\sqrt{n^{7}}}\right) \\
&= \frac{5 + \sqrt{5}}{10\sqrt{\pi}}\frac{4^n}{\sqrt{n^3}}
\left(
1 - \frac{201 + 24\sqrt{5}}{200n} + \mathcal{O}\left(\frac{1}{n^2}\right)
\right). {\qquad\blacksquare}
\end{align*}$$
