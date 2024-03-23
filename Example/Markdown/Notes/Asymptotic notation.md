---
tags:
  - Definition
---
%% {\[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Appendix A.2, pp.~722–723]]\]} %%
Let $S$ be a set equipped with a neighborhood topology $\mathcal{N}$ and let $s_0 \in S$. Further, two functions $\phi, g \colon S \setminus \{s_0\} \to \C$ are given. Then we write 
- $f(s) = \mathcal{O}(g(s))$, if $|f(s)| \leq C\cdot|g(s)|$ for all $s \neq s_0$ in a neighborhood $V \in \mathcal{N}(s_0)$,
- $f(s) \sim g(s)$, if $\lim_{s \to s_0} f(s)/g(s) = 1$ and
- $f(s) = o(g(s))$, if $\lim_{s \to s_0} f(s)/g(s) = 0$.
