---
Theorem: "[[Generating function of bridges and walks ending at altitude k]]"
tags:
  - Proof
---

As the number of bridges is trivially upper-bounded by the number of walks, we see that the radius of convergence of $B(z)$ is at least $1/P(1)$. Further, in Proposition [[Properties of the characteristic curve]] we observed that the jump polynomial $P(u)$ is a convex function for $u > 0$ and that
$$
\lim_{u \to 0} \frac{1}{P(u)} = \lim_{u \to \infty} \frac{1}{P(u)} = 0.
$$
Hence, $1/P(u)$ attains its unique positive maximum at $\tau$ and we can find an interval such that for all $u \in [\alpha, \beta]$ it holds that
$r := \frac{1}{2P(1)} < \frac{1}{P(u)}$. Then, for $|z| < r$, one finds
$$
|z \cdot P(u)| \leq |z| P(|u|) \leq 1.
$$
Thus we observe that $W(z,u)$ is analytic in 
$$
\{\, z: |z| < r \,\} \times \{\, u: \alpha < |u| < \beta \,\}.
$$
Now choose $z$ sufficiently small such that all large branches lie outside and all small branches remain inside the circle $|u| \leq (\alpha + \beta)/2$. Note that due to
$$
W(z,u) = \frac{1}{1 - zP(u)} = \frac{u^c}{-zp_d \prod_{i=1}^{c+d}(u - u_i(z))} = \mathcal{O}(u^c), \qquad u \to 0,
$$
we see that $W(z,u)/u$ does not possess a singularity at $u = 0$ for any fixed $z \neq 0$.
Then, applying Cauchy's coefficient formula to $W(z,u)$ as a Laurent series in $u$ yields
$$ 
B(z) = [u^0] W(z,u) 
= \frac{1}{2\pi \mathrm{i}}\int_{|u| 
= (\alpha + \beta)/2} W(z,u) \frac{\mathrm{d}u}{u} 
= \sum_{j = 1}^c \mathrm{Res}_{u = u_j(z)}
\left(
\frac{1}{u(1-zP(u))}
\right). 
$$
To calculate the residue, we factor the characteristic curve 
$$
u^c(1 - zP(u)) = -z p_d\prod_{i = 1}^{c+d}(u - u_i(z)).
$$
Since the small branches only contribute simple poles, we obtain
$$
\mathrm{Res}_{u = u_j(z)}\left(\frac{1}{u(1-zP(u))}\right) 
= -\frac{u_j(z)^{c-1}}{p_d z}\frac{1}{\prod_{i\neq j}(u_j(z) - u_i(z))}.
$$
Next, we recognize that 
$$\begin{align*}
\prod_{i\neq j}(u_j(z) - u_i(z)) &= \sum_{k=1}^{c+d}\prod_{i\neq k}(u_j(z) - u_i(z))
= \left.\frac{\partial}{\partial u} \left(\prod_{i=1}^{c+d}(u - u_i(z))\right)\right|_{u=u_j(z)} \\
&= \frac{1}{p_d} \left.\frac{\partial}{\partial u} \left(u^cP(u) - \frac{u^c}{z}\right)\right|_{u=u_j(z)} \\
&= \frac{1}{p_d}\left(cu_j(z)^{c-1}P(u_j(z)) + u_j(z)^cP'(u_j(z)) - u_j(z)^{c-1}\frac{c}{z}\right).
\end{align*}$$
Using the kernel equation we further simplify
$$\begin{align*}
\prod_{i\neq j}(u_j(z) - u_i(z)) 
&= \frac{1}{p_d}\left(u_j(z)^cP'(u_j(z)) -\frac{cu_j(z)^{c-1}}{z}\left(1 - zP(u_j(z))\right)\right) \\
&= \frac{1}{p_d}u_j(z)^cP'(u_j(z)).
\end{align*}$$
Thus, our residue works out to be 
$$
\mathrm{Res}_{u = u_j(z)}\left(\frac{1}{u(1-zP(u))}\right) = -\frac{1}{zu_j(z)P'(u_j(z))}.
$$
Differentiating the characteristic equation we can further simplify
$$\begin{align*}
0 = \frac{\mathrm{d}}{\mathrm{d}z}(1 - zP(u(z))) = -P(u(z)) - zP'(u(z))u'(z)
\iff P'(u(z)) = - \frac{1}{z^2u'(z)}.
\end{align*}$$
This finally yields 
$$
B(z) = \sum_{j = 1}^c \mathrm{Res}_{u = u_j(z)}\left(\frac{1}{u(1-zP(u))}\right) 
= z\sum_{j=1}^{c}\frac{u'_j(z)}{u_j(z)}.
$$
The same procedure is applicable to 
$$
W_k(z) = [u^k]W(z,u) = \frac{1}{2\pi \mathrm{i}}\int_{|u| = (\alpha + \beta)/2} W(z,u) \frac{\mathrm{d}u}{u^{k+1}},
$$
where the additional factor $u^{-k}$ can simply be treated as a constant in the residue calculation as long as $k < c$. For $k \geq c$, Cauchy's residue theorem would need to account the additional polar singularity at zero, messing up our formula. 
For that reason, when $k > -d$, the residue calculation is completed by performing a change of variables; in this case, the large branches contribute. 
We note that $W(z,u)$ satisfies
$$
W(z,u) = \frac{1}{1 - zP(u)} = \frac{u^c}{-zp_d \prod_{i=1}^{c+d}(u - u_i(z))} = \mathcal{O}(u^{-d}), \qquad u \to \infty.
$$
Hence, applying Cauchy's residue theorem for $k > -d$ to $\overline{W}(z,u) := W(z,1/u)$ and performing an analogous residue calculation yields
$$\begin{align*}
W_k(z) &= [u^{-k}]\overline{W}\left(z,u\right)
= \frac{1}{2\pi \mathrm{i}} \int_{|u| = 2/(\alpha + \beta)} \overline{W}\left(z,u\right) \cdot u^{k+1}~\mathrm{d}u \\
&= \sum_{\ell = 1}^d \mathrm{Res}_{u = v_\ell(z)^{-1}}
\left(
\frac{u^{k+1}}{1-zP(u^{-1})}
\right) \\
&= \sum_{\ell = 1}^d \frac{v_\ell'(z)}{v_\ell(z)^{k+1}},
\end{align*}$$
as $\overline{W}\left(z,u\right) \cdot u^{k+1}$ does not possess a singularity at $u = 0$.
This argument shows the formulae to be valid in a small neighborhood of the origin, which then implies the identities between the formal Laurent series a posteriori.
The algebraic character of $B(z)$ and the $W_k(z)$ finally results from the well-known fact that algebraic functions are closed under sums, products and multiplicative inverses.
