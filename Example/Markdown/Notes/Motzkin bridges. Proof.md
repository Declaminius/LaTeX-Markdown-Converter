---
Theorem: "[[Motzkin bridges]]"
tags:
  - Proof
---

The characteristic curve of Motzkin paths reads $u - z - zu - zu^{2} = 0$.
Solving this quadratic function for $u$ yields the two branches
$$\begin{equation*} 
u_1(z) = \frac{1}{2z}\left(1 - z - \sqrt{1-2z-3z^{2}}\right), \qquad 
u_2(z) = \frac{1}{2z}\left(1 - z + \sqrt{1-2z-3z^{2}}\right). 
\end{equation*}$$
Due to $\sqrt{1-2z-3z^{2}} = 1 - z + \mathcal{O}(z^2)$, we conclude that $u_1(z)$ is the only small branch of the characteristic curve.
Now we may apply Theorem [[Theorem 2.2.2]] to obtain the generating function 
$$\begin{equation*} 
B_\mathcal{M}(z) = z\frac{u_1'(z)}{u_{1}(z)}
= z\frac{1-z-\sqrt{1-2z-3z^{2}}}{2z^{2}\sqrt{1-2z-3z^{2}}} \frac{2z}{1-z-\sqrt{1-2z-3z^{2}}} 
= \frac{1}{\sqrt{1-2z-3z^{2}}}.
\end{equation*}$$
Further, recalling that the generating function for bridges is simply the coefficient of $u^0$ in the generating function of all walks $W_{\mathcal{M}}(z,u)$, we see that
$$\begin{equation*}
b_n = [z^n u^0] W(z,u) = [z^n u^0] \frac{1}{1 - z(1/u + 1 + u)}
%% = [u^0] (1/u + 1 + u)^n  %%
= [u^n] (1 + u + u^2)^n. {\qquad\blacksquare}
\end{equation*}$$
