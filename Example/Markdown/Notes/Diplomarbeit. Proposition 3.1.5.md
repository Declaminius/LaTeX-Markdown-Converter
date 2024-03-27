---
tags:
  - Proposition
label: thm:new_proof_basketball
---
Let $G_{j,k}(z)$ be the generating function for positive basketball walks starting at altitude $j > 0$ and ending at altitude $k > 0$. Then^[The formula in \[[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019, Proposition 6.4]]\] contains some typos, as some signs are incorrectly flipped.]
![[Gjk_alternative|no-title]]
where
$$
W_{i}(z) = z\left(\frac{u_{1}'}{u_{1}^{i+1}}+ \frac{u_{2}'}{u_{2}^{i+1}}\right)
$$
is the generating function of unconstrained walks starting at the origin and ending at altitude $i$ derived in Theorem [[Generating function of walks]].
We will present two proofs of this proposition. The first one, introduced in \[[[Explicit formulas for enumeration of lattice paths basketball and the kernel method|Banderier et. al., 2019]]\], uses contour integrals and a residue calculation.
Our new, second proof, will present a combinatorial argument that does not require any complex analysis.
`\begin{proof}`
![[Diplomarbeit. Proposition 3.1.5. Proof|no-title]]
`\end{proof}`
Another way to prove this result without needing to dive into complex analysis is to use the symbolic method to translate equation [[Gjk_alternative]]
into a specification for the class of general basketball walks.
`\begin{proof}`
![[Diplomarbeit. Proposition 3.1.5. Proof 2|no-title]]
`\end{proof}`
