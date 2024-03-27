---
tags:
  - Theorem
label: thm:transfer
Sources:
  - "[[Analytic combinatorics|Flajolet & Sedgewick, 2009]]"
Location: Theorem VI.3, p.~390
---
Let $\alpha \in \R$ be an arbitrary real number and let $f(z)$ be a function that is $\Delta$-analytic. 
Assume that $f(z)$ satisfies in the intersection of a neighborhood of one with its $\Delta$-domain the condition   
$$
f(z) = \mathcal{O}\left((1-z)^{-\alpha}\right).
$$
Then it holds that $[z^n]f(z) = \mathcal{O}(n^{\alpha-1}).$
> [!tip]+ Figure: The integration contour gamma in the domain Delta(phi,R)
> ![[Figure. The integration contour gamma in the domain Delta(phi,R)#Figure The integration contour gamma in the domain Delta(phi,R)|no-h4]]
`\begin{proof}`
![[mathcalO-Transfer. Proof|no-title]]
`\end{proof}`
