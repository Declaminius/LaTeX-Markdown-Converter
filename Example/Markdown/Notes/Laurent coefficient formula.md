---
tags:
  - Theorem
Sources:
  - "[[Funktionentheorie Eine Einführung Sechste Auflage|Jänich, 2004]]"
Location: Satz 16
---
Let $f(z) = \sum_{n=-\infty}^{\infty}c_{n}z^{n}$ be a convergent Laurent series on a open annulus 
$$
\{\, z: r < |z| < R \,\}.
$$ 
Then the coefficients $c_{n}$ are given via
$$
c_{n} = \frac{1}{2\pi \mathrm{i}} \int_{|z|=\rho}\frac{f(z)}{z^{n+1}}~\mathrm{d}z
$$
for all $n \in \Z$ and $r < \rho < R$.
