---
tags:
  - Theorem
label: thm:symbolic_method
---
The constructions of union, Cartesian product, sequence, powerset, multiset and cycle are all admissible. The associated operators are as follows:
$$\begin{equation*}
\def\arraystretch{1.5}
\begin{array}{cllll}
\text{Combinatorial sum:} & \mathcal{A} = \mathcal{B} + \mathcal{C} & \implies & A(z) = B(z) + C(z), \\
\text{Cartesian product:} & \mathcal{A} = \mathcal{B} \times \mathcal{C} & \implies & A(z) = B(z) \cdot C(z), \\
\text{Sequence:} & \mathcal{A} = \textsc{Seq}(\mathcal{B}) & \implies & A(z) = (1 - B(z))^{-1}, \\
\text{Powerset:} & \mathcal{A} = \textsc{PSet}(\mathcal{B}) & \implies & A(z) = \exp\left(\sum_{k=1}^\infty \frac{(-1)^{k-1}}{k}B(z^k)\right), \\
\text{Multiset:} & \mathcal{A} = \textsc{MSet}(\mathcal{B}) & \implies & A(z) = \exp\left(\sum_{k=1}^\infty \frac{1}{k} B(z^k)\right), \\
\text{Cycle:} & \mathcal{A} = \textsc{Cyc}(\mathcal{B}) & \implies & A(z) = \sum_{k=1}^\infty \frac{\phi(k)}{k} \log \frac{1}{1 - B(z^k)},
\end{array}
\end{equation*}$$
where $\phi$ denotes Euler's totient function.
For the sequence, powerset, multiset and cycle translations, it is assumed that $b_0 = 0$.

`egin{proof}`
![[Basic admissibility. Proof|no-title]]
`\end{proof}`
