---
Theorem: "[[Diplomarbeit. Corollary 2.2.7]]"
tags:
  - Proof
---

Since $M(z,u)$ is a rational function in $u$ with a simple product expression in terms of the large branches in [[gf_meanders]], its expansion with respect to $u$ is accessible via a partial fraction decomposition. 
Starting with the generating function 
$$
M(z,u) = - \frac{1}{p_{d}z}\prod_{\ell = 1}^{d} \frac{1}{u-v_{\ell}(z)}
$$
from [[gf_meanders]], we claim the following partial fraction decomposition via induction over $d$:
$$
\prod_{\ell=1}^{d} \frac{1}{u-v_{\ell}(z)} = \sum_{\ell=1}^{d} \frac{\xi_\ell^d(z)}{u-v_{\ell}(z)}.
$$
A single partial fraction decomposition shows the claim to be true for $d = 2$, as
$$
\frac{1}{(u-v_{1}(z))(u-v_{2}(z))} = \frac{1}{v_{1}(z) - v_{2}(z)} \cdot \frac{1}{u - v_{1}(z)} + \frac{1}{v_{2}(z) - v_{1}(z)} \cdot \frac{1}{u - v_{2}(z)}.  
$$
For the induction step, let the claimed formula hold for $d$. Then we have
$$\begin{align*}
\prod_{\ell = 1}^{d+1} \frac{1}{u-v_{\ell}(z)} &= 
\left(
\sum_{\ell=1}^{d}
\frac{\xi_\ell^d(z)}{u-v_{\ell}(z)}
\right) 
\frac{1}{u-v_{d+1}(z)} \\
&= \sum_{\ell=1}^{d}
\xi_\ell^d(z)
\left(
\frac{1}{v_{\ell}(z) - v_{d+1}(z)} \frac{1}{u - v_{\ell}(z)} + 
\frac{1}{v_{d+1}(z) - v_{\ell}(z)} \frac{1}{u - v_{d+1}(z)}
\right)\\
&= \sum_{\ell=1}^{d}
\left(
\frac{\xi_\ell^{d+1}(z)}{u - v_{\ell}(z)} + 
\frac{\xi_\ell^{d}(z)}{v_{d+1}(z) - v_{\ell}(z)} \cdot
\frac{1}{u - v_{d+1}(z)}
\right).
\end{align*}$$
Now we apply the induction hypothesis a second time with $v_{d+1}(z)$ replacing $u$ and obtain
$$\begin{align*}
\prod_{\ell = 1}^{d+1} \frac{1}{u-v_{\ell}(z)} &= 
\sum_{\ell=1}^{d}
\left(
\frac{\xi_\ell^{d+1}(z)}{u - v_{\ell}(z)} + 
\frac{\xi_\ell^{d}(z)}{v_{d+1}(z) - v_{\ell}(z)} \cdot
\frac{1}{u - v_{d+1}(z)}
\right) \\
&= 
\left(
\sum_{\ell=1}^{d}
\frac{\xi_\ell^{d+1}(z)}{u - v_{\ell}(z)}
\right) +
\left(
\prod_{\ell=1}^{d} \frac{1}{v_{d+1}(z) - v_{\ell}(z)}
\right) 
\frac{1}{u-v_{d+1}(z)} \\
&= \sum_{\ell=1}^{d+1}
\frac{\xi_\ell^{d+1}(z)}{u - v_{\ell}(z)}.
\end{align*}$$
Finally, we extract the coefficient of $u^{k}$ in this newly derived expression:
$$\begin{align*}
M_k(z) &= [u^{k}] M(z,u) = 
- \frac{1}{p_{d}z}[u^{k}] 
\left(
\sum_{\ell=1}^{d} \frac{\xi_\ell^d(z)}{u-v_{\ell}}
\right)
= \frac{1}{p_{d}z} \sum_{\ell=1}^{d} \xi_\ell^d(z) [u^{k}]
\left(
\frac{1}{v_{\ell}(1-\frac{u}{v_{\ell}})}
\right) \\
&= \frac{1}{p_{d}z} \sum_{\ell=1}^{d} \xi_\ell^d(z) v_{\ell}^{-k-1}(z).
{\qquad\blacksquare}
\end{align*}$$
