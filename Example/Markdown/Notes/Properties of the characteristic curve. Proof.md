---
Theorem: "[[Properties of the characteristic curve]]"
tags:
  - Proof
---



1. As the characteristic equation is a polynomial of degree $c + d$ (in its entire form) it generically admits $c + d$ roots that constitute the branches of a single algebraic curve.
We will now provide an argument from \[[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019, Proposition 6.9, p.~104]]\] that shows this conjugation principle for small roots. The case of large roots can then be handled analogously.
The kernel equation yields
$$
u = X(p_{-c} + p_{-c+1}u + \cdots + p_{d-1}u^{c+d-1} + p_d u^{c+d})^{1/c}
$$
with $X = \omega_c^j z^{1/c}$ for $j = 0,\dots, c - 1$. In this form, we see that the Lagrange inversion formula (Theorem [[Lagrange inversion formula]]) guarantees a unique power series solution $u(X)$ to this equation. Substituting $X = \omega_c^j z^{1/c}$ into this power series yields the claim.
2. Since we assumed all weights to be positive, we have
$$
P''(u) = \sum_{k = -c}^d k(k - 1) p_k u^{k - 2} > 0
$$
for $u > 0$. As $\lim_{u \to 0} P(u) = \lim_{u \to + \infty} P(u) = \infty$ it must admit a unique real, positive minimum attained at some $\tau > 0$. 
3. The proof given here follows the lines of \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Lemma 2, pp.~59–60]]\]. As $P(\tau)$ is the unique positive minimum of $P(u)$, it follows immediately that $1/P(u)$ is monotonically increasing for $u \in [0, \tau]$. 
Hence, there exists a unique function $u^+(z): [0, \rho] \to [0,\tau]$ satisfying
$$
z = \frac{1}{P(u^+(z))} \qquad \text{for $z \in [0,\rho]$}.
$$
Due to the reality condition on $u_1(z)$ we see that this positive solution $u^+(z)$ must coincide with the branch $u_1(z)$ of the characteristic curve for $z \to 0^+$. 
Further, the implicit function theorem [[Implicit function theorem]] guarantees the analyticity of $u^+(z)$ in the interval $(0, \rho)$ and with the identity theorem [[Identity theorem]] we obtain $u^+ \equiv u_1$ in $(0, \rho)$. 
Next, we use the fact that $P(u)$ is an aperiodic Laurent polynomial with positive coefficients, which according to Lemma [[Strong triangle inequality]] leads to the strict inequality
![[strong_triangle_inequality|no-title]]
Let $x \leq \rho$ be a real positive number and fix $z = x$. Then, let $w$ be an arbitrary solution of the kernel equation $1 - xP(w) = 0$ that is at most $\tau$ in modulus and **not** equal to $u_1(x)$. Hence $w \notin \R_{> 0}$ and by [[strong_triangle_inequality]] one has
$$
x = \frac{1}{P(u_1(x))} = \frac{1}{P(w)} > \frac{1}{P(|w|)},
$$
implying $|w| < u_1(x)$, since $1/P(u)$ monotonically increases in the interval $[0, \tau]$. Further, by construction all non-dominant small branches are majorized by $\tau$ for $x \to 0^+$. Thus, they must satisfy $|u_i(x)| < u_1(x)$ for $x$ sufficiently close to zero. By continuity of the modulus of any branch the domination property cannot cease to hold on $(0,\rho)$, as otherwise that would imply $u_1(x)$ reaches $\tau$ for some $x < \rho$, yielding a clear contradiction. Then, for $x = \rho$ we can apply [[strong_triangle_inequality]] again to see that the strict domination must continue to hold at $\rho$. 
Similar arguments can then be used to demonstrate $|v_j(z)| > v_1(|z|)$ for $|z| < \rho$.
Finally, we observe $|u_1(z)| < |v_1(z)|$, except for $z = \rho$, closing our chain of inequalities.
4. A part of the proof to \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 3]]\] gives insight 
into the conjugation principle for the dominant small and large root.
We start by considering the kernel equation
$$\begin{equation*}
z = \frac{1}{P(u)}
\end{equation*}$$
at the structural constant $\tau$. By construction one has $P'(\tau) = 0$ and $P''(\tau) > 0$. Then, the local expansion at $u = \tau$ reads^[The formula in the proof of \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 3, p.~62]]\] is missing the factor $\rho^2$.]
$$
z = \rho - \frac{\rho^2}{2}P''(\tau)(u - \tau)^2 + 
\mathcal{O}\left(
(u - \tau)^3
\right).
$$
Solving above equation for $u$ yields two local solutions
$$\begin{equation*}
\begin{split}
u_1(z) &= \tau - \sqrt{2\frac{P(\tau)}{P''(\tau)}}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho), \\
v_1(z) &= \tau + \sqrt{2\frac{P(\tau)}{P''(\tau)}}\sqrt{1 - z/\rho} + \mathcal{O}(1 - z/\rho),
\end{split} \qquad z \to \rho^{-},
\end{equation*}$$
corresponding to the dominant small root $u_1$ and the dominant large root $v_1$. In order to expand this informal discussion into a full proof, we refer to the theory of Newton-Puiseux expansions presented in Theorem [[Newton-Puiseux theorem]].
5. See \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 3, p.~61–64]]\] and \[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Theorem 6, pp.~72–75]]\]. {\qquad\blacksquare}
