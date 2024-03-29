---
tags:
  - Proposition
label: prop:G11
Sources:
  - "[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019]]"
Location: Proposition 6.7
---
The number $G_{1,n,1}$ of basketball excursions of length $n$ (allowed to return to altitude $0$ anywhere) is given by
$$
G_{1,n,1} = \frac{1}{n+1}\sum_{k=0}^{n}(-1)^{n+k}\binom{2n+2}{n-k}\binom{n+2k+1}{k} = 
\frac{1}{n+1} \sum_{i=0}^{\lfloor n/2 \rfloor} \binom{2n+2}{i}\binom{n-i-1}{n-2i}.
$$

`\begin{proof}`
![[Closed-form expression for the coefficients of G_1,1(z). Proof|no-title]]
`\end{proof}`
