---
Theorem: "[[Proposition 3.2.4]]"
tags:
  - Proof
---

The idea of the proof is the build up a chain of dependencies between the actual series of interest, $G_{0,2}(z)$, and several auxiliary series, so that repeated application of Lagrange inversion formula can be applied to provide an explicit expression for the coefficients of the series of interest.
As the first auxiliary series we define $F(z)$ by
$$
-\frac{1}{F(z)} = G_{0,2}(z) - \frac{1}{z}.
$$
Substituting $F(z)$ into the functional equation
$$
z^{3}G_{0,2}^{4}(z) - 3z^{2}G_{0,2}^{3}(z) -(z^{2}-3z)G_{0,2}^{2}(z) + (z-1)G_{0,2}(z) + z = 0
$$
yields
$$
(F^{3}(z) - zF(z))(1+F(z)) + z^{2} = 0.
$$
We rewrite this equation further to
$$
\left(F^{2}(z) - \frac{z}{2}\right)^{2} = 
\frac{z^{2}(1-3F(z))}{4(1+F(z))}. 
$$
Next, we take the square root on both sides. The sign is decided by observing the first terms in the counting sequence associated with $G_{0,2}(z)$ and concluding $F^{2}(z) = z^{2} + \mathcal{O}(z^{3})$. Hence, we have
$$
F^{2}(z) - \frac{z}{2} = -\frac{z}{2}\sqrt{\frac{1-3F(z)}{1+F(z)}}.
$$
We define
$$
B(z) = \frac{1}{2}\left(1 - \sqrt{\frac{1-3z}{1+z}}\right)
$$
and finally obtain an equation suitable for the application of Lagrange inversion formula:
$$
F(z) = z \frac{B(F(z))}{F(z)}.
$$
Hence, for $n \geq 1$ we have
$$
[z^{n}]G_{0,2}(z) = -[z^{n}] \frac{1}{F(z)} = 
\frac{1}{n}[z^{n-1}]z^{-2}\left(\frac{B(z)}{z}\right)^{n} = 
\frac{1}{n}[z^{2n+1}]B^{n}(z).
$$
To proceed, we derive an equation amenable to Lagrange's inversion formula for $B(z)$. Firstly, we note that $B(z)$ solves the quadratic equation
$$
(z+1)B^{2}(z) - (z+1)B(z) + z = 0,
$$
which can be rewritten to
$$
B(z) = z\left(\frac{1}{1-B(z)} - B(z)\right) = z \phi(B(z)).
$$
Now, we apply Lagrange's inversion formula again with $H(z) = z^{n}$ and obtain
$$\begin{align*}
[z^{n}]G_{0,2}(z) &= \frac{1}{n}[z^{2n+1}]B^{n}(z)
= \frac{1}{n(2n+1)}[z^{2n}]\left(n z^{n-1}\left(\frac{1}{1-z} - z\right)^{2n+1}\right) \\
&= \frac{1}{2n+1}[z^{n+1}]\left(\frac{1}{1-z} - z\right)^{2n+1}.
\end{align*}$$
Finally, all that remains is to apply Newton's generalized binomial theorem to calculate
$$\begin{align*}
[z^{n}]G_{0,2}(z) &= \frac{1}{2n+1}[z^{n+1}]\sum_{k=0}^{2n+1}(-1)^{k+1}\binom{2n+1}{k}z^{2n+1-k}\left(\frac{1}{1-z}\right)^{k} \\
&= \frac{1}{2n+1}[z^{n+1}]\sum_{\ell=0}^{\infty}\sum_{k=0}^{2n+1}(-1)^{k+1}\binom{2n+1}{k}\binom{k+\ell-1}{\ell}z^{2n+1-k+\ell} \\
&= \frac{1}{2n+1}\sum_{k=n}^{2n+1}(-1)^{k+1}\binom{2n+1}{k}\binom{2k-n-1}{k-n} \\
&= \frac{1}{2n+1}\sum_{k=0}^{n+1}(-1)^{n+k+1}\binom{2n+1}{k+n}\binom{2k-1}{k}. {\qquad\blacksquare}
\end{align*}$$
