---
Theorem: "[[Theorem 2.1.5]]"
tags:
  - Proof
---

Let $P(z,y)$ be an irreducible polynomial of degree $d$ in $y$ with 
$$
P(z,y) = p_{0}(z)y^{d}+ p_{1}(z)y^{d-1} + \dots + p_{d}(z).
$$
For each $z$ there are exactly $d$ distinct values for $y$ such that $P(z,y) = 0$ except for two cases:
- Firstly, if $p_{0}(z_0) = 0$, then there is a reduction in the degree of $y$ and hence a reduction in the number of finite $y$-solutions for that particular value.
- Secondly, $P(z_0,y)$ may have a multiple root in $y$ and some of the values of $y$ will coalesce.
Hence, we define the exceptional set $\Xi[P]$ of $P$ as 
$$
\Xi[P] := \{\, z \mid p_{0}(z) = 0 \lor \exists y: P(z,y) = \partial_{y}P(z,y) = 0 \,\}.
$$
For each $z \notin \Xi[P]$ the implicit function theorem [[Theorem 1.4.10]] guarantees that each of the solutions $y_j$ lifts into a locally analytic function $y_j(z)$.
The exceptional set thus provides a set of possible candidates for the singularities of an algebraic function.
Any $y(z)$, analytic at the origin, satisfying $P(z,y) = 0$, can be analytically continued along any simple path emanating from the origin that does not cross any point of $\Xi[P]$.
Consider an exceptional point at the origin and assume that $P(0,y)$ has $k$ equal roots $y_1,\dots,y_k$ at $y = 0$.
Consider a punctured disk $|z| < r$ that does not include any other exceptional point relative to $P$.
Continue $y_1(z)$ analytically along a curve starting from an arbitrary value $z$ in the interior of $(0,r)$, encircling the origin and returning to $z$.
By permanence of analytic relations $y_1(z)$ will be taken into another root.
Repeat this process until one has obtained a collection of roots $y_{1}(z) = y_1^{(0)}(z), y_{1}^{(1)}(z), \dots, y_{1}^{(\kappa)}(z) = y_{1}(z)$.
In this case, $y_{1}(t^\kappa)$ is an analytic function in $t$ except possibly at zero where it is continuous and has value zero.
By general principles (Morera's theorem) it is in fact analytic at zero.
This implies the existence of a convergent power series expansion at zero: $$y_{1}(t^{\kappa}) = \sum\limits_{n=1}^{\infty}c_{n}t^{n}.$$
Each determination of $z^{1/\kappa}$ yields one of the branches of the multivalued analytic function:
%% $$ %%
%%   y_{1}(z) = \sum\limits_{n=1}^{\infty}c_{n}z^{n/\kappa}. %%
%% % $$ %%
%% Alternatively, with $\omega = \exp(2\pi \mathrm{i}/\kappa)$ the $\kappa$ determinations are obtained as  %%
$$
y_{1}^{(j)}(z) = \sum\limits_{n=1}^{\infty}c_{n}\omega^n z^{n/\kappa}, \qquad j = 0,\dots,\kappa - 1,
$$
with $\omega = \exp(2\pi \mathrm{i}/\kappa)$.
If $\kappa = k$, then the cycle accounts for all the roots which tend to zero. 
Otherwise, we repeat the process with another root and, in this fashion, eventually exhaust all roots that tend to zero. 
Thus, all the $k$ roots that have value zero at $z = 0$ are grouped into cycles of size $\kappa_{1},\dots,\kappa_\ell$.
Finally, values of $y$ at infinity are brought to zero by means of the change of variables $y = 1/u$, leading to negative exponents in the expansion of $y$.
