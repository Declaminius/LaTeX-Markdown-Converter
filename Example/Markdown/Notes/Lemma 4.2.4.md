---
tags:
  - Lemma
label: lemma:radius_conv
---
Let $P(u)$ be an aperiodic characteristic polynomial and let $\rho =  1/P(\tau)$ be the structural radius defined in Proposition [[Properties of the characteristic curve]].
Further, consider the set 
$$
\mathcal{Z} := \{\, z \in \C \mid 1  - Q(z) = 0, |z| \leq \rho \,\}.
$$
The set is either empty, or it contains exactly one real positive element, in which case we denote it with $\rho_0$.
In any case, the generating function $D(z)$ of excursions ending with a catastrophe possesses exactly one dominant singularity on its radius of convergence $\rho_D$. The sign of the drift $\delta := P'(1)$ of the walk then dictates the location $\rho_D$:

- If $\delta \geq 0,$ we have $\rho_D = \rho_0 < 1/P(1) \leq \rho.$
- If $\delta < 0$, it also depends on the value $Q(\rho):$
$$\begin{align*}
\begin{cases}
Q(\rho) > 1 & \iff \rho_D = \rho_0 < \rho, \\
Q(\rho) = 1 & \iff \rho_D = \rho_0 = \rho, \\
Q(\rho) < 1 & \iff \text{$\rho_D = \rho$and $\mathcal{Z}$is empty.} \\
\end{cases}
\end{align*}$$

`\begin{proof}`
![[Lemma 4.2.4. Proof|no-title]]
`\end{proof}`
