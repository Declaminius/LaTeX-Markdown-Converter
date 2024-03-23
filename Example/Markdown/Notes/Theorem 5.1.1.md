---
tags:
  - Theorem
label: thm:gf_directed_animals
---
The generating functions $Q_s(z)$ and $Q_t(z)$ for strict and general half-pyramids, respectively, are given by
$$\begin{align*}
Q_s(z) &= \frac{1 - z - \sqrt{(1+z)(1-3z)}}{2z}, \\
Q_t(z) &= Q_s\left(\frac{z}{1-z}\right) = \frac{1 - 2z - \sqrt{1 - 4z}}{2z}.
\end{align*}$$
The generating function for strict and general pyramids, with $z$ counting their number of dimers and $u$ counting their right width is
![[gf_pyramids|no-title]]
with $Q$ denoting the respective generating function for strict or general half-pyramids.
In particular, the generating functions $P_s(z,1)$ and $P_t(z,1)$ for directed animals on the square and the triangular lattice, respectively, are given by
$$\begin{align*}
P_s(z,1) &= \frac{1}{2}\left(\sqrt{\frac{1+z}{1-3z}}-1\right), \\
P_t(z,1) &= P_s\left(\frac{z}{1-z},1\right) = \frac{1}{2}\left(\frac{1}{\sqrt{1-4z} - 1}\right).
\end{align*}$$
> [!tip]+ Figure: The factorizations of strict half-pyramids and pyramids
> ![[Figure. The factorizations of strict half-pyramids and pyramids#Figure The factorizations of strict half-pyramids and pyramids|no-h4]]
`\begin{proof}`
![[Theorem 5.1.1. Proof|no-title]]
`\end{proof}`
