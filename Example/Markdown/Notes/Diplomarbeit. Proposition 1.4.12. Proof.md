---
Theorem: "[[Diplomarbeit. Proposition 1.4.12]]"
tags:
  - Proof
---

We only prove the relevant direction for the thesis here. In particular, we only need to know that all common roots of $P(x)$ and $Q(x)$ can be found as zeroes of the resultants. 
Let $\xi$ be a common root of $P(x)$ and $Q(x)$. Then $w = (\xi^{l+m-1},\dots,\xi,1)$ solves the homogenous linear system $S\cdot w = 0$, since
$$
S \cdot \begin{pmatrix}\xi^{l+m-1}\\ \vdots \\ \xi \\ 1 \end{pmatrix}
= \begin{pmatrix} \xi^{m-1}P(\xi) \\ \vdots \\ P(\xi) \\ \xi^{l-1}Q(\xi) \\ \vdots \\ Q(\xi)\end{pmatrix}.
$$
This implies that $\ker(S) \neq \{0\}$ and hence $\mathbf{R}(P(x),Q(x),x) = \det(S) = 0$. The other direction can be found for example in \[[[Linear Algebra|Lang, 1966, V.~10]]\].
