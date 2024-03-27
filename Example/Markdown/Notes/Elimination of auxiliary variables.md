---
tags:
  - Remark
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: p.~740
---
Given a system of polynomial equations
$$
P_j(z,y_1,\dots,y_m) = 0, \qquad j = 1, \dots, m,
$$
defining an algebraic curve we can systematically eliminate one of the auxiliary variables $y_i$ until we are left with a single equation in $z$.
We start by taking resultants with $P_m$ and eliminate all occurrences of the variable $y_m$ from the first $m - 1$ equations by replacing $P_j$ with $\textbf{R}(P_j, P_m, y_m)$.
Then, we repeat this process until all auxiliary variables have been eliminated and we are left with a single polynomial equation over $z$.
The resulting polynomial is in general not minimal, in fact, the complexity of elimination is exponential in the resulting degree, in the worst-case. Hence, additional polynomial factorization techniques are required, when dealing with a large system of equations.
