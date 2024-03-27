---
tags:
  - Definition
Sources:
  - "[[Lattice path combinatorics|Wallner, 2013]]"
Location: Definition 1.8
---
Let $R$ be a ring with unity. The ring of *formal power series* $R[[z]]$ consists of all formal sums of the form 
$$
\sum_{n \geq 0} a_n z^n = a_0 + a_1z + a_2z^2 + \cdots,
$$
with coefficients $a_n \in R$.
The sum of two formal power series $\sum_{n \geq 0} a_n z^n, \sum_{n \geq 0} b_n z^n$ is defined by 
$$
\sum_{n \geq 0} a_n z^n + \sum_{n \geq 0} b_n z^n = \sum_{n \geq 0}(a_n + b_n)z^n
$$
and their product by 
$$
\sum_{n \geq 0}a_n z^n \cdot \sum_{n \geq 0} b_n z^n = \sum_{n \geq 0} \left(\sum_{k=0}^n a_k b_{n-k}\right)z^n.
$$
