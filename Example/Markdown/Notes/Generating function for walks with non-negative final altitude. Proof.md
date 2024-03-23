---
Theorem: "[[Generating function for walks with non-negative final altitude]]"
tags:
  - Proof
---

We start with the formula [[Wk2]] for the generating function for walks ending at altitude $-d < k < \infty$ and derive
$$\begin{align*}
W^+(z,u) &= \sum_{k = 0}^\infty W_k(z)u^k
= -z \sum_{k = 0}^\infty 
\left(
\sum_{\ell = 1}^d \frac{v_\ell'(z)}{v_\ell(z)^{k+1}}
\right)
u^k \\
&= -z \sum_{\ell = 1}^d 
\left(
\frac{v_\ell'(z)}{v_\ell(z)}
\sum_{k = 0}^\infty \frac{u^k}{v_j(z)^k}
\right)
= -z \sum_{\ell = 1}^d \frac{v_\ell'(z)}{v_\ell(z)} \frac{1}{1 - u/v_\ell(z)} \\
&= z \sum_{\ell = 1}^d \frac{v_\ell'(z)}{u - v_\ell(z)}.
\end{align*}$$
Further, using formula [[gf_meanders]], we note that
$$\begin{align*}
\frac{\mathrm{d}}{\mathrm{d}z} M(z,u) &= 
\left(\frac{1}{p_d z^2} - \frac{1}{p_d z} \sum_{\ell = 1}^d \frac{v_\ell'(z)}{u - v_\ell(z)}\right) \prod_{\ell = 1}^d \frac{1}{u - v_\ell(z)} \\
&= -\frac{1}{z}\left(1 - \sum_{\ell = 1}^d \frac{v_\ell'(z)}{u - v_\ell(z)}\right)M(z,u)
\end{align*}$$
and thus
$$\begin{equation*}
1 + z \frac{\mathrm{d}}{\mathrm{d}z}(\log M(z,u)) = z \sum_{j = 1}^d \frac{v_j'(z)}{u - v_j(z)}. {\qquad\blacksquare}
\end{equation*}$$
