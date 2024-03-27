---
Theorem: "[[Closed-form expression for the coefficients of G_0,1(z)]]"
tags:
  - Proof
---

In Example [[Diplomarbeit. Example 3.1.4]] we derived the functional equation
$$
zG_{0,1}^{4}(z) + 2zG_{0,1}^{3}(z) + (3z-1)G_{0,1}^{2}(z) + (2z-1)G_{0,1}(z) + z = 0.
$$
We rewrite the equation to
$$
z(1+G_{0,1}(z) + G_{0,1}^{2}(z))^{2} - G_{0,1}(z) - G_{0,1}^{2}(z) = 0.
$$
Comparing with the functional equation $C(z) = 1 + zC(z)^{2}$ for the Catalan numbers yields the striking identity
$$
G_{0,1}(z) + G_{0,1}^{2}(z) = C(z) - 1.
$$
Define $H(z)$ implicitly as the functional inverse of $H + H^{2}$. Then we have 
$$
G_{0,1}(z) = H(C(z) - 1).
$$
Since $H(z) = z/(1+H)$ and $\tilde{C}(z) := C(z) - 1$ satisfies $\tilde{C}(z) = z(1 + \tilde{C}(z))^2$ we can apply Lemma~[[Variant of Lagrange inversion formula]] and obtain
$$\begin{align*}
[z^{n}]G_{0,1}(z) &= 
\frac{1}{n}\sum_{k=1}^{n}
\left(
[z^{k-1}] \frac{1}{(1+z)^{k}}
\right)
\left(
[z^{n-k}](1+z)^{2n}
\right) \\
&= \frac{1}{n}\sum_{k=1}^{n}\binom{-k}{k-1}\binom{2n}{n-k} \\
&= \frac{1}{n}\sum_{k=1}^{n}(-1)^{k-1}\binom{2k-2}{k-1}\binom{2n}{n-k}.
\end{align*}$$
The alternative expression without the $(-1)^{k-1}$ factors comes from the Lagrange inversion formula for $u_{1}$ applied to the equation $G_{0,1}(z) = u_{1}(z) + u_{2}(z)$, using the fact that 
$$
u_{1}(z)^{2}= z u_{1}(z)^2P(u_{1}(z))
$$ 
in conjunction with the conjugation property of the small roots. By the properties of the kernel method [[Properties of the characteristic curve]] we know that $u_1(z)$ admits an expansion of the form
$$
u_1(z) = \sum_{n = 0}^\infty a_n z^{n/2}.
$$
In order to apply Lagrange's inversion formula to $u_1(z)$ we thus define $$
U(x) := u_1\left(x^2\right) = \sum_{n = 0}^\infty a_{n} x^n
$$
Thus, $U$ is a power series in $x$ and satisfies the equation
$$
U(x) = x \sqrt{U(x)^2 P(U(x))}.
$$
This leads to
$$\begin{align*}
[z^{n}]G_{0,1}(z) &= 
[z^{n}](u_{1}(z) + u_{2}(z)) = 
2[x^{2n}]U(x) \\
&= \frac{1}{n} [t^{2n-1}] (t^2P(t))^n \\
&= \frac{1}{n} [t^{2n-1}] ((1+t)(1+t^3))^n \\
&= \frac{1}{n}\sum_{k=0}^{n}\binom{n}{k}\binom{n}{2n+1-3k}.
\end{align*}$$
The last closed-form expression can also be explained indirectly via counting the number of unrestricted basketball walks from altitude zero to altitude one in $n$ steps. We simply extract the coefficient of $[u^{1}]$ in the generating function $W(z,u)$ and obtain
$$
[u^{1}z^{n}] W(z,u) = 
[u^{1}]P(u)^{n} = 
[u^{1}]\left(\frac{(1+u^{3})(1+u)}{u^{2}}\right)^{n} = 
\sum_{k=0}^{n}\binom{n}{k}\binom{n}{2n+1-3k}.
$$
Now we establish a $1$-to-$n$ correspondence between walks of length $n$ counted by $G_{0,1}(z)$ and those counted by $W_{0,1}(z)$. 
Each walk $\omega$ counted by $G_{0,1}(z)$ can be decomposed into $\omega = \omega_{\ell}B\omega_r$ with $B$ being any point in the walk. Now we obtain a new unconstrained walk by $\omega' = B\omega_r\omega_\ell$. If $\omega$ is of length $n$ there are $n$ choices for $B$. Finally we remark that all new walks obtained in this way are in fact different walks. This is due to the fact that there are no walks from altitude zero to altitude one, which are formed as concatenation of several copies of one and the same walk.
Conversely, given a walk $\tau$ of length $n$ counted by $W_{0,1}(z)$, we decompose $\tau$ into $\tau = \tau_{\ell}B\tau_r$ with $B$ being the right-most lowest point of $\tau$. Then, $\tau' = B\tau_{r}\tau_\ell$ is a walk of length $n$ counted by $G_{0,1}(z)$.
