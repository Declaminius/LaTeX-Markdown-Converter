---
Theorem: "[[Theorem 2.3.4]]"
tags:
  - Proof
---

Assume that $f$ is analytic in the domain $\Delta(\phi,R)$, let $1 < r < R$ and $\phi < \theta < \pi/2$. Then we define the contour $\gamma = \gamma_{1} \cup \gamma_{2} \cup \gamma_{3} \cup \gamma_{4}$ (see Figure [[Figure. The integration contour gamma in the domain Delta(phi,R)]]) through
$$\begin{align*}
\gamma_{1} &= \left\{\, z: |z-1| = 1/n, |\arg(z-1)| \geq \theta \,\right\}, \\
\gamma_{2} &= \left\{\, z: 1/n \leq |z-1|, |z| \leq r, \arg(z-1)=\theta \,\right\}, \\
\gamma_{3} &= \{\, z: |z| = r, |\arg(z-1)| = \theta \,\}, \\
\gamma_{4} &= \left\{\, z: 1/n \leq |z-1|, |z| \leq r, \arg(z-1) = -\theta \,\right\}.
\end{align*}$$
Under these assumption, the contour $\gamma$ lies entirely inside the domain of analyticity of $f$. Now we apply Cauchy's coefficient formula to obtain
$$
f_{n} = [z^{n}]f(z) = \frac{1}{2\pi \mathrm{i}}\int_{\gamma}f(z) \frac{\mathrm{d}z}{z^{n+1}}.
$$ 
Next, we proceed by bounding the absolute value of the integral along each of the four partial contours seperately. For that purpose we define
$$
f_n^{(j)} = \frac{1}{2 \pi \mathrm{i}} \int_{\gamma_j} f(z) \frac{\mathrm{d}z}{z^{n+1}}.
$$
By assumption, there exists a $K > 0$ such that $|f(z)| < K \cdot |1 - z|^{-\alpha}$ in the intersection of a neighborhood of one with $\Delta(\phi, R)$.

1. We start by considering the inner circle $\gamma_1$. Since the integrand is bounded by $K \cdot n^\alpha$ we obtain the simple estimate $\big|f_n^{(1)}\big| \leq K \cdot n^{\alpha - 1}$.
2. Next, we bound the rectilinear parts along $\gamma_2$ and $\gamma_4$. Setting $\omega = \exp(\mathrm{i} \theta)$ and performing the change of variable $z = 1 + \omega t / n$, we find
$$
\big|f_n^{(2)}\big| \leq \frac{n}{2\pi} \int_1^\infty K \cdot \left(\frac{t}{n}\right)^{-\alpha} \left| 1 + \frac{\omega t}{n}\right|^{-n-1} \mathrm{d}t.
$$
From the relation
$$
\left|1 + \frac{\omega t}{n} \right| \geq 1 + \mathfrak{R}\left(\frac{\omega t}{n}\right) = 1 + \frac{t}{n} \cos \theta,
$$
there results the inequality
$$
\big| f_n^{(2)}\big| \leq \frac{K \cdot n^{\alpha - 1}}{2 \pi} J_n, \qquad \text{with} \qquad J_n = \int_1^\infty t^{-\alpha}\left(1 + \frac{t \cos \theta}{n}\right)^{-n-1} ~\mathrm{d}t.
$$
For any given $\alpha$, the integrals $J_n$ are all bounded above by some constant since they admit the limit
$$
J_n \xrightarrow[n \to \infty]{} \int_1^\infty t^{-\alpha} \exp(-t \cos \theta) ~\mathrm{d}t < \infty,
$$
where the condition $0 < \theta < \pi/2$ ensures convergence of the integral. Thus, we obtain the bound
$$
\big| f_n^{(2)} \big| = \mathcal{O}(n^{\alpha - 1})
$$
and similar arguments show the same bound for $f_n^{(4)}$.
23. Finally we consider the contribution from the integral along the outer circle $\gamma_3$. There the integrand remains bounded while $z^{-n}$ is of order $\mathcal{O}(r^{-n})$. Hence, $f_n^{(3)}$ is exponentially small and negligible in the scale of the problem.

In summary, each of the four integrals of the split contour are bounded by $\mathcal{O}\left(n^{\alpha - 1}\right)$ and thus the statement of the theorem follows.
