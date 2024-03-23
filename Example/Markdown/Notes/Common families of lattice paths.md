---
tags:
  - Definition
---
In this definition we give an overview over all the families of lattice paths used in this thesis. We state the specific simple step set and the corresponding kernel equation, which will be defined in the next section, respectively.
- *Dyck walks*: The step set is given by $\mathcal{D} := \{-1,1\}$ and the kernel equation reads 
$$
K(z,u) = u - z(1 + u^2).
$$
- *Motzkin walks:* The step set is given by $\mathcal{M} := \{-1,0,1\}$ and the kernel equation reads 
$$
K(z,u) = u - z(1 + u + u^2).
$$
- \textit{$k$-Motzkin walks:} The step multiset is given by $\mathcal{M}_k := \{-1,\underbrace{0,\dots,0}_{k \text{ times}},1\}$ and the kernel equation reads 
$$
K(z,u) = u - z(1 + k u + u^2).
$$
They are commonly interpreted as lattice paths with $k$ different colors for the horizontal step. Hence, we model them as simple lattice paths with a horizontal step of weight $p_0 = k$.
- *Basketball walks:* The step set is given by $\mathcal{B} := \{-2,-1,1,2\}$ and the kernel equation reads 
$$
K(z,u) = u^2 - z(1 + u + u^3 + u^4).
$$
Throughout this thesis, we will use the following notation rules for generating functions:
1. $W(z), B(z), M(z)$ and $E(z)$ denote the generating functions for walks, bridges, meanders and excursions, respectively.
2. The subscript encodes the corresponding step set.
3. Additional extensions, like catastrophes, will be noted in the superscript.
For example, $M_{\mathcal{D}}^{\mathrm{cat}}(z,u)$ will denote the bivariate generating function of Dyck meanders with catastrophes.
