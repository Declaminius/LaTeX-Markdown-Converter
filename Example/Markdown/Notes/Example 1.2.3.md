---
tags:
  - Example
label: ex:formal_topology
---
Let $f \in R[[z]]$ be a formal power series with $f_0 = 0$. 
Then, the infinite sum $Q(f) := \sum_{k = 0}^\infty f^k$ converges in the formal topology. 
Let $Q_n(f) = \sum_{k=0}^n f^k$ be the partial sum terminating at index $n$. We notice that $\mathrm{val}(f^k) \geq k$ and thus we have
$$
d(Q_n,Q_m) =  2^{-(\min(n,m)+1)}.
$$
Hence, $(Q_n)_{n \in \N}$ is a Cauchy sequence and consequently converges.
