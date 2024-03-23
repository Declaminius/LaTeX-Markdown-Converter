---
tags:
  - Example
---
One of the first known applications of this technique appears in Knuth's *The Art of Computer Programming* \[[[The Art of Computer Programming Vol 1; Fundamental algorithms|Knuth, 1997, Answer to Exercise 2.2.1.4, pp.~536–537]]\], 
where he counts permutations obtainable via admissible sequences of operations on stacks. The two operations on a stack are to move an element from the input into the stack and to move an element from the stack into the output. We note that this counting problem is equivalent to counting the number of Dyck meanders, as the number of removals from the stack may never exceed the number of insertions. 
The special case that the total number of insertions equals the total number of removals then fits neatly into the long list of objects counted by the Catalan numbers, as we have shown in [[André’s reflection principle]].
To address the general case, Knuth introduces a new technique that we now call the kernel method.

Let $g_{n,k}$ be the number of admissible sequences of stack operations of length $n$, with $k$ more insertions than removals and define the bivariate generating function $G(z,u) := \sum_{n, k = 0}^\infty g_{n,k} u^k z^n$.
By partitioning these sequences based on whether their last operation is an insertion or a removal, we see that the counting sequence satisfies, for $n, m \geq 0$,
$$
g_{n+1,m} = g_{n,m-1} + g_{n,m+1}, \qquad g_{0,m} = \delta_{0,m},
\qquad g_{n,-1} := 0,
$$
where $\delta_{0,m}$ denotes the Kronecker^[Leopold Kronecker (1823–1891)] symbol defined via
$$
\delta_{i,j} = 
\begin{cases}
1, & i = j, \\
0, & i \neq j.
\end{cases}
$$
We multiply the recurrence relation with $z^n u^k$ and sum over $n$ and $k$. This yields the functional equation
$$\begin{align*}
\frac{1}{z}(G(z,u) - 1) = u \cdot G(z,u) + \frac{1}{u}(G(z,u) - G(z,0)).
\end{align*}$$
Rearranging the terms of this equation and multiplying to get rid of the denominators, the kernel structure of this equation becomes apparent, as
![[functional_equation_knuth|no-title]]
We are now looking to find an expression for $G(z,0)$ such that $G(z,u)$ admits a power series expansion in $z$ and $u$ at $(z,u) = (0,0)$. The most straightforward ansatz is to set the kernel $K(z,u) = 0$.
Solving this equation for $u$ yields two conjugated solutions
$$
u_1(z) = \frac{1 - \sqrt{1 - 4z^2}}{2z}, \qquad
v_1(z) = \frac{1 + \sqrt{1 - 4z^2}}{2z}.
$$
Plugging them into the functional equation [[functional_equation_knuth]] we get
the two candidate solutions $u_1(z)/z$ and $u_2(z)/z$ for $G(z,0)$.
By expanding 
$$
\sqrt{1 - 4z^2} = 1 - 2z^2 + \mathcal{O}(z^4)
$$
we see that only $u_1(z)/z$ admits a proper power series expansion at $z = 0$. Hence, only $G(z,0) = u_1(z)/z$ conforms with the fact that $G(z,0)$ is a generating function of a combinatorial class. 
Further, we observe that
$$
u_1(z) + u_2(z) = \frac{1}{z}, \qquad u_1(z) \cdot u_2(z) = 1.
$$
Thus, together with $G(z,0) = u_1(z)/z$, we find
$$
G(z,u) = \frac{zu_1(z) - u}{z(u^2 + 1) - u}
= \frac{zu_1(z) - u}{z(1 - u_1(z) \cdot u)(1 - u_2(z) \cdot u)} = \frac{u_1(z)}{z(1 - u_1(z) \cdot u)},
$$
which can then be used in conjunction with the expansion
$$
u_1(z) = \sum_{n = 0}^\infty \frac{1}{2n + 1}\binom{2n + 1}{n}z^{2n+1}
$$
to determine the general solution
$$\begin{alignat*}{3}
&g_{2n,2k} &&= \frac{2k + 1}{2n + 1}\binom{2n + 1}{n - k} 
&&= \binom{2n}{n - k} - \binom{2n}{n - k - 1}, \\
&g_{2n + 1, 2k + 1} &&= \binom{2k + 2}{2n + 2}
&&= \binom{2n + 1}{n - m} - \binom{2n + 1}{n - k - 1}. %\tag*
{{\qquad\blacksquare}}
\end{alignat*}$$
