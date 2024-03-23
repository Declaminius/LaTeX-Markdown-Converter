---
tags:
  - Definition
---
%% {\[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Definition I.4, p.~19]]\]}  %%
The *ordinary generating function (OGF)* of a sequence $(a_n)_{n \in \mathbb{N}}$ is the formal power series
$$
A(z) = \sum_{n=0}^\infty a_n z^n.
$$
The OGF of a combinatorial class $\mathcal{A}$ is the generating function for the counting sequence $a_n = \mathrm{card}(\mathcal{A}_n), n \geq 0.$ Equivalently, the combinatorial form 
$$
A(z) = \sum_{\alpha \in \mathcal{A}} z^{|\alpha|},
$$
is employed. We say the variable $z$ marks the size in the generating function.
Further, we introduce the coefficient extraction operator $[z^n]: R[[z]] \to \C$, defined via
$$
[z^n] \left( \sum_{n \geq 0} f_n z^n \right) = f_n.
$$
