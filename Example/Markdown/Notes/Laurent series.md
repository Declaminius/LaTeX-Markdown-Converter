---
tags:
  - Definition
---
Let $z_{0} \in \C$. A *Laurent series* around $z_{0}$ is a series of the form
$$
\sum_{n=-\infty}^{\infty}c_{n}(z-z_{0})^{n},
$$
consisting of the *principal part* $\sum_{n=1}^{\infty}c_{-n}(z-z_{0})^{-n}$ and the *Taylor part* $\sum_{n=0}^{\infty}c_{n}(z-z_{0})^{n}$ of the Laurent series. For the principal part we introduce the convenient notation
$$
\{u^{<0}\} 
\left(
\sum_{n=-\infty}^{\infty}c_{n}(z-z_{0})^{n}
\right) := 
\sum_{n=1}^{\infty}c_{-n}(z-z_{0})^{-n}.
$$
A Laurent series converges iff both subseries converge. In this case, the limit is defined as the sum of the limits of the two subseries. 
Let $1/r$ be the radius of convergence of $\sum_{n=1}^{\infty}c_{-n}(z-z_{0})^n$ and $R$ be the radius of convergence of the Taylor part. Then, the Laurent series converges on the open annulus $\{\, z: r < |z| < R \,\}$ and for all $r < \rho_{1} < \rho_{2} < R$ it converges uniformly on $\{\, z: \rho_{1} < |z| < \rho_{2} \,\}$.
