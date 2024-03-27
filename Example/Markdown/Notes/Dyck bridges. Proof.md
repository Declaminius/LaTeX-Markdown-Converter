---
Theorem: "[[Dyck bridges]]"
tags:
  - Proof
---

The characteristic polynomial of Dyck bridges is given by $P(u) = 1/u + u$ and hence the kernel equation reads 
$$
K(z,u) = 1 - z\left(\frac{1}{u} + u \right) = 0.
$$
There exists one small and one large branch of the characteristic curve: 
$$
u_1(z) = \frac{1- \sqrt{1 - 4z^2}}{2z} \sim_{z \to 0} z, \quad
u_2(z) = \frac{1 + \sqrt{1 - 4z^2}}{2z} \sim_{z \to 0} \frac{1}{z},
$$
since 
$$
\sqrt{1 - 4z^2} = \sum_{n \geq 0} \binom{1/2}{n} (-4)^n z^{2n} = 1 - 2z^2 + \mathcal{O}(z^4).
$$
After applying Theorem [[Generating function of bridges and walks ending at altitude k]] we get 
$$\begin{align*}
B_\mathcal{D}(z) &= z \frac{u_1'(z)}{u_1(z)} 
= \frac{1}{\sqrt{1 - 4z^2}} \\
&= 1 + 2z^2 + 6z^4 + 20z^6 + 70z^8 + 252z^{10} + 924z^{12} + 3432z^{14} + \mathcal{O}(z^{16}).
\end{align*}$$
Using Newton's generalized binomial theorem [[Newton's generalized binomial theorem]] we extract
$$\begin{align*}
[z^n] \frac{1}{\sqrt{1 - 4z}} &=
[z^n] \left(\sum_{k \geq 0} \binom{-1/2}{k}(-4z)^k\right) 
= \frac{(-1/2)\cdot(-3/2)\cdots  (-(2n-1)/2)}{n!}(-4)^n \\
&= 2^n \frac{(2n-1)!!}{n!} 
= 2^n \frac{(2n)!}{n!(2n)!!}
= \binom{2n}{n}
= [t^n](1+t^2)^n.
\end{align*}$$
The coefficients are called the central binomial numbers and are closely related to the Catalan numbers. This result can be explained very easily: In order to uniquely characterize a Dyck bridge consisting of $n$ **NE**-steps and $n$ **SE**-steps, we simply need to choose the positions of the  **NE**-steps (or equivalently of the **SE**-steps). For this, there are $\binom{2n}{n}$ possibilities.
