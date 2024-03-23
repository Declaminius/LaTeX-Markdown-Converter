---
Theorem: "[[Proposition 3.1.5]]"
tags:
  - Proof
---

In Lemma [[Lemma 3.1.2]] we derived the formula
$$
G_{j}(z,u) = \frac{u^{j} - z\left(G_{j,1}(z) + G_{j,2}(z) + \frac{G_{j,1}(z)}{u}\right)}{1-zP(u)}
$$
for the bivariate generating function of positive basketball walks starting at $(0,j)$. To obtain an expression for $G_{j,k}(z)$ we extract the coefficient of $u^{k}$ in the left-hand side of this equation. After simplifying the numerator using equations [[Gj1, Gj2, Gj]], [[Gj1, Gj2, Gj]] and [[G0k, Gjk]], together with the linearity of the coefficient extraction operator, we are left with
$$
G_{j,k}(z) = [u^{k}] \frac{u^{j}}{1-zP(u)} - G_{0,j}(z) \cdot [u^{k}]\frac{1}{1 - zP(u)} - z G_{1,1}(z) G_{0,j-1}(z) \cdot [u^{k}]\frac{u^{-1}}{1-zP(u)}.
$$
Next we can recognize $W(z,u) = \frac{1}{1-zP(u)}$. Together with the time reversal identity $W_{\ell} = W_{-\ell}$, we obtain the formula
$$
G_{j,k}(z) = W_{j-k} -\frac{u_{1}^{j+1}-u_{2}^{j+1}}{u_{1}-u_{2}}W_{-k} + \frac{u_{1}u_{2}(u_{1}^{j}-u_{2}^{j})}{u_{1}-u_{2}}W_{-k-1}.
$$
Now it only remains to derive the desired expression for $W_{\ell}$. For this we apply Cauchy's coefficient formula with a curve $\gamma$ encircling the origin, shrunk sufficiently such that only the small roots remain inside. Cauchy's residue theorem then yields
$$\begin{align*}
W_{\ell}(z) &= [u^{\ell}] \frac{1}{1-zP(u)}
= \frac{1}{2\pi \mathrm{i}}\int_{\gamma} \frac{\mathrm{d}u}{u^{\ell+1}(1-zP(u))} \\
&= \mathrm{Res}_{u=u_{1}(z)}\left(\frac{1}{u^{\ell+1}(1-zP(u))}\right) + \mathrm{Res}_{u=u_{2}(z)}\left(\frac{1}{u^{\ell+1}(1-zP(u))}\right).
\end{align*}$$
To calculate these residues, we make use of the identities $1/z = P(u_i(z))$, as well as $zP'(u_i(z)) = - P(u_i(z))/u_i'(z)$, which are immediate consequences of the kernel equation and its derivative. With that in mind we compute
$$\begin{align*}
\mathrm{Res}_{u=u_{i}(z)}\left(\frac{1}{u^{\ell+1}(1-zP(u))}\right)
%% &= \lim_{u\to u_{i}(z)} \frac{u - u_i(z)}{u^{\ell+1}(1-zP(u))}\\ %%
%% &= \frac{1}{u_{i}(z)^{\ell+1}(u_{i}(z) - u_{2}(z))(u_{i}(z) - v_{1}(z))(u_{i}(z)-v_{2}(z))}\\ %%
&= \left(u_{i}(z)^{\ell+1} \left(\frac{\mathrm{d}}{\mathrm{d}u}(1-zP(u))\right)\Bigg|_{u=u_{i}(z)}\right)^{-1}\\
&= -\frac{1}{u_{i}(z)^{\ell+1}zP'(u_{i}(z))} \\
&= \frac{u_{i}'(z)}{u_{i}(z)^{\ell+1}P(u_{i}(z))}
= z\frac{u_{i}'(z)}{u_{i}(z)^{\ell+1}}. {\qquad\blacksquare}
\end{align*}$$ 
