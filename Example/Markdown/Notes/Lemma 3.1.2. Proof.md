---
Theorem: "[[Lemma 3.1.2]]"
tags:
  - Proof
---

To derive a functional equation for the generating function of all positive basketball walks starting at $(0,j)$, we split them before their last step. A positive basketball walk is then either the single initial point at altitude $j$, or a positive basketball walk followed by a step not reaching altitude $0$ or below. 
This leads to the functional equation 
![[fundamental_functional_equation|no-title]]
which already implies [[Gj1, Gj2, Gj]].
To solve for the remaining unknowns $G_{j,1}$ and $G_{j,2}$ we 
substitute the small roots $u_{1}(z)$ and $u_{2}(z)$ of the kernel equation into [[fundamental_functional_equation]] and get the linear system
$$\begin{align*}
u_{1}^{j}(z) &= z\left(G_{j,1}(z) + G_{j,2}(z) + \frac{G_{j,1}(z)}{u_{1}(z)}\right),\\
u_{2}^{j}(z) &= z\left(G_{j,1}(z) + G_{j,2}(z) + \frac{G_{j,1}(z)}{u_{2}(z)}\right).
\end{align*}$$
Solving this system for $j > 0$ immediately yields the formulae [[Gj1, Gj2, Gj]] and [[Gj1, Gj2, Gj]].
