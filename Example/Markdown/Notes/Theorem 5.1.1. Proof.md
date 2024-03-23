---
Theorem: "[[Theorem 5.1.1]]"
tags:
  - Proof
---

The factorization of strict half-pyramids, depicted in Figure [[Subfigure. The factorization of strict half-pyramids]], directly yields the functional equation $Q_s(z) = z + Q_s(z) + Q_s(z)^2$. Solving this quadratic equation yields 
$$
Q_s(z) = \frac{1 - z - \sqrt{(1+z)(1-3z)}}{2z},
$$ 
which we recognize as the generating function of the Motzkin numbers; see [$\texttt{OEIS A001006}$](https://oeis.org/A001006). 

For the generating function of general heaps we simply note that a general heap can be built from a strict heap by replacing each dimer with $k \geq 1$ dimers lying on top of each other. This expansion operation does not change the right width and thus preserves the property of being a half-pyramid. This immediately gives 
$$
Q_t(z) = Q_s\left(\frac{z}{1-z}\right) = \frac{1 - 2z - \sqrt{1 - 4z}}{2z},
$$ 
which again corresponds to the generating function of a famous combinatorial sequence: the Catalan numbers, see [$\texttt{OEIS A000108}$](https://oeis.org/A000108). 

The factorization of pyramids shown in Figure [[Subfigure. The factorization of strict pyramids]] leads us to the functional equation $P(z,u) = Q(z)(1 + uP(z,u))$, where we observe that the half-pyramids involved do not contribute to the right width of the pyramid. Further, the factorization is also valid for general pyramids, if we exchange strict half-pyramids for general half-pyramids.

For strict pyramids we thus obtain
$$\begin{align*}
P_s(z,1) &= \frac{1 - z -\sqrt{-3 z^{2}-2 z +1}}{2 z + z - 1 + \sqrt{-3 z^{2}-2 z +1}} \\
&= \frac{\left(z -1+\sqrt{-3 z^{2}-2 z +1}\right) \left(-3 z +1+\sqrt{-3 z^{2}-2 z +1}\right)}{4 z \left(3 z -1\right)} \\
&= \frac{1}{2}\left( \sqrt{\frac{1+z}{1-3z}} - 1\right) \\
&= z + 2z^2 + 5z^3 + 13z^4 + 35z^5 + 96z^6 + 267z^7 + \mathcal{O}(z^{8}).
\end{align*}$$
The counting sequence corresponds to [$\texttt{OEIS A005773}$](https://oeis.org/A005773) shifted by one unit. In Corollary [[Motzkin meanders]] we already observed this sequence to count the number of Motzkin meanders. Hence, the class of strict pyramids of size $n + 1$ corresponds not only to the class of directed animals of size $n + 1$, but also to the class of Motzkin meanders of length $n$.
