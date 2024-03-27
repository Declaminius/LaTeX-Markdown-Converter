---
Theorem: "[[Diplomarbeit. Proposition 3.1.5]]"
tags:
  - Proof
---

First, we isolate $W_{j-k}(z)$ from equation [[Gjk_alternative]] and substitute $j = k + \ell$ to obtain
$$
W_{\ell}(z) = G_{k,k + \ell}(z) + W_{-k}(z) G_{0,k + \ell}(z) + W_{-k-1}(z)zG_{1,1}(z)G_{0,k + \ell -1}(z).
$$
To prove this formula using the symbolic method we thus need to show that any basketball walk starting from $(0,0)$ and ending at altitude $\ell$ falls into one of three categories:
1. $G_{k,k + \ell}(z)$: A walk that never touches nor crosses altitude $-k$.
2. $W_{-k}(z) \cdot G_{0,k + \ell}(z)$: A walk to altitude $-k$, followed by a walk from altitude $-k$ to altitude $\ell$ that never returns to altitude $-k$.
3. $W_{-k-1}(z) \cdot z \cdot G_{1,1}(z) \cdot G_{0,k + \ell -1}(z)$: A walk to altitude $-k - 1$, followed by a step to altitude $-k + 1$, then an excursion at altitude $-k + 1$, until it ends with a walk from altitude $-k + 1$ to altitude $\ell$ that never returns to altitude $-k + 1$.

> [!tip]+ Figure: Decompositions of a basketball walk ending at altitude ell
> ![[Figure. Decompositions of a basketball walk ending at altitude ell#Figure Decompositions of a basketball walk ending at altitude ell|no-h4]]

We argue this with a modified last passage decomposition of $W_\ell(z)$.
We define the last traversal of an altitude $j$ as the last step that either leaves from altitude $j$ or crosses from altitude $j - 1$ to $j + 1$.
Let $\omega$ be an arbitrary basketball walk ending at altitude $\ell$.
We split $\omega$ at its last traversal of altitude $-k$. If this traversal does not exist, then $\omega$ falls into the first category.
Otherwise, if the last traversal of altitude $-k$ leaves from altitude $-k$, $\omega$ falls into the second category.
Finally, in the case that the last traversal crosses over altitude $-k$ we need to be a little more delicate. Since the final part is forced to start with a $+2$ step, we cannot simply describe it as a positive basketball walk from altitude $0$ to altitude $k + \ell + 1$. Hence, we need to split off the first $+2$ step. Now the remaining part is still not yet a positive basketball walk, as it still may return to the line $y = -k + 1$. Hence, we apply a second last passage decomposition to partition the remaining part into an excursion at altitude $(-k + 1)$, followed by a walk from altitude $-k + 1$ to altitude $\ell$ that never returns to altitude $-k + 1$. For a visual representation of these three cases, we refer to Figure [[Figure. Decompositions of a basketball walk ending at altitude ell]].
