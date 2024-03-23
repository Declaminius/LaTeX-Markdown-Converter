---
Theorem: "[[Theorem 3.1.3]]"
tags:
  - Proof
---

Since positive basketball walks must stay strictly above the $x$-axis, the first step of a walk can only go up.
Thus, removing this first step and shifting the origin, we have
$$
G_{0,k}(z) = z(G_{1,k}(z) + G_{2,k}(z)).
$$
We can rewrite this equation using the time reversal equation [[time_reversal]] to obtain
$$
G_{0,k}(z) = z(G_{k,1}(z) + G_{k,2}(z)).
$$
In this form, plugging in the formulae [[Gj1, Gj2, Gj]] and [[Gj1, Gj2, Gj]] derived in the preceding lemma instantly yields 
$$
G_{0,k}(z) = \frac{u_{1}^{k+1}(z) - u_{2}^{k+1}(z)}{u_{1}(z) - u_{2}(z)}.
$$
To derive the formula for $G_{j,k}(z)$ for general $j > 0$ we make use of a first passage decomposition with respect to the minimal altitude of the walk. 
By time reversal, we have $G_{0,m}(z)$ as the generating function for basketball walks starting at $(0,m)$, staying strictly above the $x$-axis, but ending on the $x$-axis.
Furthermore, we recognize
$$
E(z) = G_{1,1}(z) = -\frac{u_{1}(z) u_{2}(z)}{z}
$$ 
as the generating function of basketball excursions. Note that in contrast to the positive basketball walks counted by $G_{0,0}(z)$, basketball excursions are allowed to touch the $x$-axis at any point. 
Positive basketball walks starting from height $j$ and ending at height $k$ can then be decomposed into three parts; see Figure [[Figure. The decomposition of a basketball walk counted by G_j,k(z)]]:

> [!tip]+ Figure: The decomposition of a basketball walk counted by G_j,k(z)
> ![[Figure. The decomposition of a basketball walk counted by G_j,k(z)#Figure The decomposition of a basketball walk counted by G_j,k(z)|no-h4]]

1. The walk starts at altitude $j$ and continues until it hits the lowest altitude of the entire walk $i$ for the first time. This part is counted by $G_{0,j-i}(z)$.
2. The second part then continues to the last time the path reaches altitude $i$. Consequently, this part is counted by $E(z)$.
3. The last part runs from altitude $i$ to altitude $k$ without ever returning to altitude $i$. By time reversal, this part is counted by $G_{0,k-i}(z)$.
Summing over all possible values for $i$ then yields [[G0k, Gjk]].
