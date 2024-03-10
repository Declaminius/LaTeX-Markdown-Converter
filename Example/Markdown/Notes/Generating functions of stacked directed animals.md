---
tags:
  - Theorem
---
Let $Q(z)$ denote the generating function for strict and general half-pyramids, respectively. Let $P(z,u)$ denote the bivariate generating function for strict and general pyramids, respectively, with $u$ counting the right width of the pyramid. Then, the generating function for square and triangular stacked directed animals, respectively, with $z$ enumerating the number of dimers, $u$ the right width and $t$ the number of minimal dimers, is given by
$$
S(z,u,t) = \frac{t P(z,u)}{1 - t P(z,1)^2} 
= \frac{t Q(1 - Q)^2}{(1 - uQ)((1- Q)^2 - tQ^2)}.
$$
In particular, the generating function for square and triangular stacked directed animals, respectively, is given by 
$$\begin{align*}
S_s(z) &= \frac{(1-z)(1-3z) - (1-4z)\sqrt{(1-3z)(1+z)}}{2z(2 - 7z)}, \\
S_t(z) &= S_s\left(\frac{z}{1-z}\right) = \frac{(1-3z)(1-4z) - (1-5z)\sqrt{1-4z}}{2z(2-9z)}.
\end{align*}$$

#### Proof

![[Generating functions of stacked directed animals Proof]]
