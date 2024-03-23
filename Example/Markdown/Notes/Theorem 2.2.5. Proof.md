---
Theorem: "[[Theorem 2.2.5]]"
tags:
  - Proof
---

Let $m_{n,k}$ be the number of meanders of size $n$ that end at altitude $k$. 
By the combinatorial origin of the problem, $M(z,u) = \sum_{n,k \in \mathbb{N}} m_{n,k}u^kz^n$ is bivariate analytic for $|u| \leq 1$ and $z < 1/P(1)$. 
Decomposing a path based on the last step added yields the recurrence $$
m_0(u) = 1, \quad m_{n+1}(u) = P(u)m_n(u) - \{u^{<0}\}P(u)m_n(u).
$$
Multiplying both sides by $z^{n+1}$ and summing over $n$ then leads to the fundamental functional equation defining meanders:
![[fundamental_functional_equation_meanders|no-title]]
Since the characteristic polynomial $P(u)$ involves only a finite number of negative powers it can be rewritten to 
$$
M(z,u)(1 - zP(u)) = 1 - z\sum_{k=0}^{c-1}r_k(u)M_k(z).
$$
The Laurent polynomials $r_k(u)$ are immediately computable from $P(u)$ via $$
r_k(u) := \{u^{<0}\}(u^k P(u)) = \sum_{j=-c}^{-k-1}p_j u^{j+k}.
$$
For instance, if $P(u) = p_{-2}u^{-2} + p_{-1}u^{-1} + \mathcal{O}(1)$, one has
$$
r_0(u) = \frac{p_{-2}}{u^2} + \frac{p_{-1}}{u}, \qquad
r_1(u) = \frac{p_{-2}}{u}.
$$
The fundamental functional equation [[fundamental_functional_equation_meanders]] appears to be grossly underdetermined with one unknown bivariate generating function and $c$ unknown ordinary generating functions involved. 
Luckily, the kernel method comes to the rescue. In order to substitute the small branches into the functional equation we choose $|z| < 1/P(1)$ sufficiently small such that
- all small branches are distinct and
- all small branches satisfy $|u_i(z)| \leq 1$.
Under these conditions it is analytically legitimate to substitute any small branch of the characteristic equation in the fundamental functional equation in [[fundamental_functional_equation_meanders]] to reduce the number of unknowns.
The substitution yields the following system of $c$ equations for the $c$ unknown functions $M_0, \dots, M_{c-1}$:
$$\begin{equation*}
z \cdot
\underbrace{\begin{pmatrix}
u_1(z)^c r_0(u_1(z)) & \cdots & u_1(z)^c r_{c-1}(u_1(z)) \\
\vdots & \ddots & \vdots \\
u_c(z)^c r_0(u_c(z)) & \cdots & u_c(z)^c r_{c-1}(u_c(z)) \\
\end{pmatrix}}_{:= A}
\begin{pmatrix}
M_0(z) \\ \vdots \\ M_{c-1}(z)
\end{pmatrix}
=
\begin{pmatrix}
u_1(z)^c \\ \vdots \\ u_c(z)^c
\end{pmatrix}.
\end{equation*}$$
If we expand the Laurent polynomials $r_k(u)$ in the matrix $A$ we get a clearer picture of its structure, as 
$$\begin{equation*}
A = \begin{pmatrix}
p_{-c} + p_{-c+1}u_1(z) + \cdots + p_{-2}u_1(z)^{c-2} + p_{-1}u_1(z)^{c-1} & \cdots & p_{-c} u_1(z)^{c-1} \\
\vdots & \ddots & \vdots \\
p_{-c} + p_{-c+1}u_c(z) + \cdots + p_{-2}u_c(z)^{c-2} + p_{-1}u_c(z)^{c-1} & \cdots & p_{-c} u_c(z)^{c-1} \\
\end{pmatrix}.
\end{equation*}$$
In this form, we can see that the matrix $A$ can be transformed into a Vandermonde matrix by iteratively adding $-p_{-c + (j - k)}/p_{-c}$ times the $j$-th column to the $k$-th column, starting from the rightmost column.
Since the determinant is invariant under these elementary column operations and we have chosen $z$ such that all small branches are distinct, we find that 
$$
\det(A) = p_{-c}^c \prod_{1 \leq i \leq j \leq c}(u_j(z) - u_i(z)) \neq 0.
$$
Thus, the system is non-singular and admits a unique solution.
To avoid further determinantal calculation, we make use of a cute observation by Bousquet-Mélou, introduced in~\[[[Linear recurrences with constant coefficients the multivariate case|Bousquet-Mélou & Petkovšek, 2000]]\], and define
![[constant_term1|no-title]]
We observe that the roots of $N(z,u)$ are precisely $u_1,\dots,u_c$ and the leading monomial of $N(z,u)$ is $u^c$, hence we obtain the alternative expression of
![[constant_term2|no-title]]
Now we compare the constant terms in both equations. 
Due to [[constant_term2]] the constant term of $N(z,u)$ equals $\prod_{j=1}^c (-u_j(z))$. 
On the other hand, [[constant_term1]] implies that the constant term equals $-zp_{-c}M_0(z)$.
Hence, we find that $M_0(z)$ satisfies 
$$
M_0(z) = \frac{(-1)^{c-1}}{zp_{-c}}\prod_{j=1}^cu_j(z)
$$
and finally we get
$$\begin{equation*}
M(z,u) = \frac{N(z,u)}{u^c(1 - zP(u))}. {\qquad\blacksquare}
\end{equation*}$$
