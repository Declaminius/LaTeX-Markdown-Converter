---
tags:
  - Proposition
label: prop:kernel_method
---
Let $K(z,u)$ be the kernel equation corresponding to a simple step set $\mathcal{S} = \{s_1, \dots, s_m\}$ augmented with a system of weights $\Pi = \{\, p_s \mid s \in \mathcal{S} \,\}$ and let $c = - \min_j s_j$ and $d = \max_j s_j$ denote the two extremal vertical amplitudes of any jump.
Further, let $\omega_c = \exp\left(2 \pi i/c\right)$ and $\omega_d = \exp\left(2 \pi i / d\right)$ denote the respective roots of unity. 
Then, the following statements hold:
1. The kernel equation $K(z,u) = 0$ defines $c + d$ branches of a single algebraic curve. Of these branches, there are $c$ distinct *small roots* $u_1, \dots, u_c$, conjugated to each other at zero, satisfying
$$\begin{equation*}
u_j(z) \sim \omega_c^{j-1}(p_{-c})^{1/c}z^{1/c} \qquad \text{as $z \to 0$.}
\end{equation*}$$
More precisely, this means that there exists a function $A$ analytic at zero, such that, in a neighborhood of zero, one has
$$\begin{equation*}
u_j(z) = \omega_c^{j-1} z^{1/c} 
A\left(
\omega_c^{j-1}z^{1/c}
\right) , \quad j = 1, \dots, c.
%% = u_1\left(\omega_c^{j-1} z\right), \quad j = 1, \dots, c. %%
\end{equation*}$$
The remaining $d$ distinct *large roots* are conjugated to each other at $\infty$ and satisfy
$$\begin{equation*}
v_k(z) \sim \omega_d^{1-k}(p_d)^{-1/d}z^{-1/d} \qquad \text{as $z \to 0$.}
\end{equation*}$$
More precisely, there exists an analytic function $B$, such that, in a neighborhood of zero, one has
$$\begin{equation*}
v_k(z) = \omega_d^{1-k}z^{-1/d} 
B\left(
\omega_d^{1-k}z^{1/d}
\right), \quad k = 1, \dots, d.
%% = v_1\left(\omega_d^{k-1}z\right), \quad k = 1, \dots, d. %%
\end{equation*}$$
In summary, the $u_j$ and $v_k$ organize themselves into two cycles of $c$ and $d$ elements; see Figure [[Figure. Graphs of the characteristic curve]] for an example.
For determinacy, one restricts attention to the complex plane slit along the negative real axis, which allows us to talk freely of the individual branches in the sequel.
27. The characteristic polynomial $P(u)$ admits a unique positive minimum at a real number $\tau > 0$, called the *structural constant*. This value then defines the *structural radius* $\rho := 1/P(\tau)$. 
28. There is a *dominant small root* $u_1(z)$ and a *dominant large root* $v_1(z)$, determined by the reality conditions
$$
u_1(z) \sim \gamma z^{1/c}, \qquad v_1(z) \sim \delta z^{-1/d}, \qquad (z \to 0^+)
$$
with $\gamma := (p_{-c})^{1/c}, \delta := (p_d)^{-1/d} \in \R_{> 0}$,
such that, for $|z| < \rho, ~ i = 2,\dots,c$ and $j = 2,\dots,d$, one has
$$\begin{equation*}
|u_i(z)| < u_1(|z|) < v_1(|z|) < |v_j(z)|.
\end{equation*}$$
Further, on the circle of convergence $|z| = \rho$ we have
$$
|u_i(z)| < u_1(\rho) = v_1(\rho) < |v_j(z)|.
$$
41. The dominant small root $u_1(z)$ and the dominant large root $v_1(z)$ are conjugated to each other at their dominant singularity occuring at the structural radius $\rho$:
$$\begin{equation*}
u_1(z) \sim \tau + \sum_{n = 1}^\infty a_n (\rho - z)^{n/2}, \qquad 
v_1(z) \sim \tau + \sum_{n = 1}^\infty (-1)^n a_n (\rho - z)^{n/2}.
\end{equation*}$$
46. The product 
$$
Y_1(z) := \prod_{i=2}^c u_i(z)
$$ 
of the non-dominant small roots, as well as the product 
$$
\overline{Y_1}(z,u) := \prod_{j = 2}^d \frac{1}{u - v_j(z)}
$$
of the non-dominant large roots, is analytic in the closed disk including the structural radius $|z| \leq \rho$.
> [!tip]+ Figure: Graphs of the characteristic curve
> ![[Figure. Graphs of the characteristic curve#Figure Graphs of the characteristic curve|no-h4]]
`\begin{proof}`
![[Properties of the characteristic curve. Proof|no-title]]
`\end{proof}`
