---
tags:
  - Theorem
label: thm:gf_walks_bridges_catastrophes
---
Let $r_{n,k}$ be the number of walks with resets to zero of length $n$ from altitude $0$ to altitude $k$. Then the generating function $R(z,u)$ is algebraic and satisfies
$$\begin{equation*}
R(z,u) = D(z) \cdot W(z,u) = \frac{1}{1 - Q(z)} \cdot \frac{1}{1 - zP(u)},
\end{equation*}$$
with $Q(z)$ depending on the model of resets to zero:
$$\begin{equation*}
Q^\mathrm{cat}(z) = q z \left(W(z) - W_0(z) - \sum_{\substack{s > 0, \\ -s\in \mathcal{S}}} W_s(z)\right), \qquad
Q^\mathrm{alt}(z) = q z \cdot W(z).
\end{equation*}$$
In addition, the generating functions for walks with resets to zero, ending at altitude $k$ satisfy
$$\begin{equation*}
R_k(z) = D(z)W_k(z) = \frac{1}{1 - Q(z)} \cdot
\begin{cases}
z\sum_{j=1}^c \frac{u_j'(z)}{u_j(z)^{k+1}}, & \text{for $-\infty < k < c$}, \\[5pt]
-z\sum_{j=1}^c \frac{v_j'(z)}{v_j(z)^{k+1}}, & \text{for $-d < k < +\infty$}.
\end{cases}
\end{equation*}$$

`\begin{proof}`
![[Generating  function of walks and bridges with resets to zero. Proof|no-title]]
`\end{proof}`
