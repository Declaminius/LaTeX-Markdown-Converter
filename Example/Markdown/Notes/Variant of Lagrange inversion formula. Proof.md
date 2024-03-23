---
Theorem: "[[Variant of Lagrange inversion formula]]"
tags:
  - Proof
---

The classical Lagrange inversion formula of Theorem [[Lagrange inversion formula]] yields
$$
[z^{n}]H(F(z)) = \frac{1}{n}[z^{n-1}]H'(z)\phi^{n}(z).
$$
Applying the Cauchy product formula allows us to apply Lagrange's inversion formula a second time:
$$\begin{align*}
[z^{n}]H(F(z)) &= 
\frac{1}{n}\sum_{k=0}^{n-1}
\left(
[z^{k}]H'(z)
\right)
\left(
[z^{n-1-k}]\phi^{n}(z)
\right) \\
&= \frac{1}{n}\sum_{k=1}^{n}
\left(
k[z^{k}]H(z)
\right)
\left(
[z^{n-k}]\phi^{n}(z)
\right) \\
&= \frac{1}{n}\sum_{k=1}^{n}
\left(
[z^{k-1}]\psi^{k}(z)
\right)
\left(
[z^{n-k}]\phi^{n}(z)
\right). {\qquad\blacksquare}
\end{align*}$$
