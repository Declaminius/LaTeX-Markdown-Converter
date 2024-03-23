---
Theorem: "[[Theorem 5.1.3]]"
tags:
  - Proof
---

Let $H$ be an arbitrary stacked pyramid. Either it has only one minimal piece and is thus a single pyramid, or it is the product of a pyramid $P$ with a stacked pyramid $H'$ placed above $P$. The number of ways that $P$ can be placed below $H'$ equals the right width of $H'$. Further, by definition the right width of $P$ determines the right width of $H$. Translating this construction into the language of generating functions yields
$$
S(z,u,t) = tP(z,u)\left(1 + \frac{\partial S}{\partial u}(z,1,t)\right).
$$
To compute the derivative $\frac{\partial S}{\partial u}(z,1,t)$, we differentiate the equation with respect to $u$ and set $u$ to 1:
$$
\frac{\partial S}{\partial u}(z,1,t) = t\frac{\partial P}{\partial u}(z,1)\left(1 + \frac{\partial S}{\partial u}(z,1,t)\right).
$$
Further, differentiating Equation [[gf_pyramids]] lets us calculate
$$
\frac{\partial P}{\partial u}(z,u) = \frac{Q(z)^2}{(1 - uQ(z))^2} = P(z,u)^2.
$$
Hence, we obtain
$$\begin{equation*}
S(z,u,t) = tP(z,u)\left(1 + \frac{t\frac{\partial P}{\partial u}(z,1)}{1 -  t\frac{\partial P}{\partial u}(z,1)}\right)
= \frac{tP(z,u)}{1 -  tP(z,1)^2}. {\qquad\blacksquare}
\end{equation*}$$
