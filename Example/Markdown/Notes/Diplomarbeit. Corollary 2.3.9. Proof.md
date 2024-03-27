---
Theorem: "[[Diplomarbeit. Corollary 2.3.9]]"
tags:
  - Proof
---

Due to Example [[Counting sequence of Dyck excursions]] we know the generating function of the Catalan numbers to be 
$$
C(z) = \sum_{n = 0}^\infty \frac{1}{n+1}\binom{2n}{n}z^n = \frac{1 - \sqrt{1 - 4z}}{2z}.
$$
Due to its simple form, we immediately recognize its dominant singularity at $\rho = 1/4$. 
Using the functional equation $C(z) - C^{2}(z) - 1 = 0$ we can now derive an asymptotic expansion at the singularity. Substituting $z = 1/4 - Z$ and $C(z) = 2 + Y$ we shift the singularity to zero and eliminate the constant term in the expansion. The functional equation now reads
$$
Q(Z,Y) = - \frac{1}{4}Y^{2} + 4Z + 4ZY + ZY^{2}.
$$
The theory of Puiseux expansions now gives us a priori the existence of solutions of the type 
$$
Y = cZ^{\alpha}(1 + o(1))
$$ 
for some $c \neq 0, \alpha \in \Q$. Plugging this asymptotic estimate into our functional equation yields 
$$
Q(Z,Y) \sim - \frac{c^{2}}{4}Z^{2\alpha} + 4Z + 4cZ^{1+\alpha} + cZ^{1+2\alpha}. 
$$
To satisfy this equation identically, two exponents need to coincide and the corresponding monomials need to cancel each other. This is only possible for $2\alpha = 1$ and $c^{2}= 16$. Hence, $Q(Z,Y) = 0$ is asymptotically consistent with
$$
Y \sim 4Z^{1/2}, \quad Y \sim -4Z^{1/2},
$$
corresponding to the two branches of the algebraic equation. Reversing the substitutions we thus obtain the asymptotic expansion
$$
C(z) = 2 - 2\sqrt{1 - 4z} + \mathcal{O}(1-4z).
$$
This process can be iterated upon subtracting dominant terms to obtain a complete asymptotic expansion.
For that we take the ansatz $Y \sim -4Z^{1/2} +  cZ$. Plugging this asymptotic estimate into $Q(Z,Y)$ we obtain
$$\begin{align*}
Q(Z,Y) &\sim - \frac{1}{4}\left(-4Z^{1/2}+cZ\right)^{2} + 4Z + 4Z\left(-4Z^{1/2} + cZ\right) + Z\left(-4Z^{1/2}+cZ\right)^{2} \\\\
&= - \frac{1}{4} \left(16Z + c^{2}Z^{2} - 8cZ^{3/2}\right) + 4Z - 16Z^{3/2}+ 4cZ^{2} + Z\left(16Z + c^{2}Z^{2} - 8cZ^{3/2}\right) \\\\
&= (2c-16)Z^{3/2} - \left(\frac{c^{2}}{4}+4c+16\right)Z^{2}- 8cZ^{5/2}+c^2Z^{3}.
\end{align*}$$
This then immediately yields $c = 8$. One more: 
$$
Y \sim -4Z^{1/2} + 8Z + cZ^{3/2}.
$$
We get
$$
Q(Z,Y) \sim (2c+32)Z^{2} + \mathcal{O}\left(Z^{3/2}\right).
$$
Finally, we get $c = -16$ and
$$
C(z) = 2 - 2\sqrt{1-4z} + 2(1-4z) - 2(1-4z)^{3/2} + \mathcal{O}((1-4z)^{2}).
$$
Define $\sigma(u) = 2 - 2\sqrt{1 - u} + 2(1-u) -2(1-u)^{3/2} + 2(1-u)^{2}$  and $\tau(u) = (1-u)^{5/2}$. Now that we have expanded $C(z)$ into the form 
$$
C(z) = \sigma(4z) + \mathcal{O}(\tau(4z)),
$$
we can start translating via the standard function scale (Theorem [[Standard function scale]]): 
$$\begin{align*}
\sigma_{n} &= [z^{n}]\sigma(z) = -2[z^{n}]\left(\sqrt{1 -4z} + (1-4z)^{3/2}\right) \\
&\sim -2\frac{n^{-3/2}}{\Gamma(-1/2)}\left(1 + \sum_{k \geq 0} \frac{e_{k}\left(-\frac{1}{2}\right)}{n^k}\right) -2\frac{n^{-5/2}}{\Gamma(-3/2)}\left(1 + \sum_{k \geq 0} \frac{e_{k}\left(- \frac{3}{2}\right)}{n^k}\right)\\
&= \frac{1}{\sqrt{\pi n^{3}}} \left(1 + \frac{3}{8n} + \mathcal{O}\left(\frac{1}{n^{2}}\right)\right) - \frac{3}{2\sqrt{\pi n^{5}}}\left(1 + \mathcal{O}\left(\frac{1}{n}\right)\right).\\
&= \frac{1}{\sqrt{\pi n^{3}}} \left(1 - \frac{9}{8n} + \mathcal{O}\left(\frac{1}{n^{2}}\right)\right).
\end{align*}$$
Similarly, we have
$$
\tau_n = [z^n] \tau(z) \sim \frac{n^{-7/2}}{\Gamma(-3/2)}\left(1 + \sum_{k \geq 0} \frac{e_k}{n^k}\right)
= \mathcal{O}\left(\frac{3}{4\sqrt{\pi n^{7}}}\right).
$$
After translating the error via the Transfer Theorem [[mathcalO-Transfer]], we thus get
$$\begin{align*}
[z^n]D(z) &= 4^n\sigma_n + 4^n \cdot \mathcal{O}(\tau_n)
= \frac{4^{n}}{\sqrt{\pi n^{3}}}\left(1 - \frac{9}{8n} + \mathcal{O}\left(\frac{1}{n^{2}}\right)\right). {\qquad\blacksquare}
\end{align*}$$
