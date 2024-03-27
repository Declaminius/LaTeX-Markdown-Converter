---
tags:
  - Proposition
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: Figure VI.7, p.~394
---
Let $f(z)$ be a function, analytic at zero, whose coefficients are to be analyzed.
1. Determine the dominant singularity $\rho$ of $f(z)$ and check that $f(z)$ has no other singularities on its circle of convergence.
2. Establish that $f(z)$ is analytic in a $\Delta$-domain $\Delta_\rho$ around $\rho$.
3. Analyze the function $f(z)$ as $z \to \rho$ in $\Delta_\rho$ and determine a singular expansion of the form
$$
f(z) = \sigma(z/\rho) + \mathcal{O}(\tau(z/\rho)) 
\qquad \text{with}
\qquad \tau(z) = o(\sigma(z)),
\qquad \text{as $z \to \rho$}.
$$
In order to proceed to the next step, the functions $\sigma$ and $\tau$ should belong to the standard scale of functions.
11. Translate the main term $\sigma(z)$ using the standard function scale (Theorem [[Standard function scale]]), transfer the error term using the Transfer Theorem [[mathcalO-Transfer]] and conclude that
$$
[z^n] f(z) = \rho^{-n}\sigma_n + \mathcal{O}(\rho^{-n}\tau_n),
$$
where $\sigma_n = [z^n] \sigma(z)$ and $\tau_n = [z^n] \tau(z)$.
