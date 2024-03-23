---
tags:
  - Definition
label: def:resultant
---
Consider a field of coefficients $\K$ and two polynomials 
$$
P(x) = \sum\limits_{j=0}^{\ell} a_{j}x^{\ell-j}, \qquad Q(x) = \sum\limits_{k=0}^m b_{k}x^{m-k},
$$
in $\K[X]$. We define their *resultant* with respect to the variable $x$ as the determinant of order $(\ell + m)$, 
$$
\mathbf{R}(P(x),Q(x),x) = \det \begin{vmatrix} a_{0} & a_{1} & a_{2} & \cdots & 0 & 0 \\
0 & a_{0}& a_{1} & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \cdots & a_{\ell-1} & a_{\ell}  \\ 
b_{0} & b_{1} & b_{2} & \cdots & 0 & 0 \\
0 & b_{0} & b_{1} & \ddots & \vdots & \vdots \\ 
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \cdots & b_{m-1} & b_{m} 
\end{vmatrix},
$$
also called the *Sylvester determinant*. By its definition, the resultant is a polynomial in the coefficients of $P$ and $Q$.
