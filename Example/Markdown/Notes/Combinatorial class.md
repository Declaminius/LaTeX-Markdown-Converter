---
tags:
  - Definition
---
%%{\[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Definition I.1, p.~16]]\]}  %%
A *combinatorial class* $\mathcal{A}$, or simply a *class*, is a finite or denumerable set on which a size function is defined, satisfying the following conditions:
1. The size of an element is a non-negative integer.
2. The number of elements of any given size is finite.
The size of an element $\alpha \in \mathcal{A}$ is denoted by $|\alpha|$, or $|\alpha|_{\mathcal{A}}$ and we define 
$$
\mathcal{A}_n := \{\, \alpha \in \mathcal{A} : |\alpha| = n \,\}.
$$
We denote the cardinality of these subsets by $a_n := \mathrm{card}(\mathcal{A}_n)$ and call $(a_n)_{n\in\mathbb{N}}$ the *counting sequence* of $\mathcal{A}$.
Further, we define two elementary combinatorial classes:
- The *neutral class* $\mathcal{E}$ consists of a single object of size 0.
- The *atomic class* $\mathcal{Z}$ consists of a single object of size 1.
They form the basis from which all combinatorial structures are constructed.
