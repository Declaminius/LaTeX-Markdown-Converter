---
Theorem: "[[Theorem 2.3.1]]"
tags:
  - Proof
---

We start by applying Cauchy's coefficient formula, with a sufficiently small contour $\mathcal{C}_0$ encircling the origin, to obtain
$$
f_{n} = \frac{1}{2\pi \mathrm{i}}\int_{\mathcal{C}_{0}}(1-z)^{-\alpha} \frac{\mathrm{d}z}{z^{n+1}}.
$$
We now deform $\mathcal{C}_0$ to a large circle with radius $R > 1$ that does not cross the half-line $[1,\infty[$.
More precisely, the new contour $\mathcal{C}_{R}(n)$ consists of the following parts (see Figure~[[Figure. The contours mathcalC_R(n) and mathcalH(n)]]):
1. $\mathcal{C}_{R}^{\circ}(n) := \{\, z \in \C: |z| = R \,\} \setminus \{\, z \in \C: (\mathfrak{I}(z) < 1/n) \land (\mathfrak{R}(z) > 0) \,\}$
2. $\mathcal{H}_R^{+}(n) := \{\, z \in \C: z = x + i/n, x \in [1,R] \,\}$
3. $\mathcal{H}_R^{-}(n) := \{\, z \in \C: z = x - i/n, x \in [1,R] \,\}$
4. $\mathcal{H}^{\circ}(n) := \{\, z \in \C: z = 1 - (1/n) \cdot \exp(i\varphi), \varphi \in [-\pi/2,\pi/2]\,\}$
As $R$ tends to infinity the integrand along $C_{R}^{\circ}(n)$ decreases as $\mathcal{O}(R^{-n-1-\alpha})$.
Hence the limit process produces the Hankel contour $\mathcal{H}(n)$ consisting of
1. $\mathcal{H}^{+}(n) := \{\, z \in \C: z = x + i/n, x \geq 1 \,\}$
2. $\mathcal{H}^{-}(n) := \{\, z \in \C: z = x - i/n, x \geq 1 \,\}$
3. $\mathcal{H}^{\circ}(n) := \{\, z \in \C: z = 1 - (1/n) \cdot \exp(i\varphi), \varphi \in [-\pi/2,\pi/2] \,\}$
We apply a change of variables by introducing $z = 1 + t/n$. This leads to 
$$
f_{n} = \frac{n^{\alpha-1}}{2\pi \mathrm{i}}\int_{\mathcal{H}(n)} (-t)^{-\alpha}\left(1 + \frac{t}{n}\right)^{-n-1}\mathrm{d}t.
$$
Next we calculate the asymptotic estimate
![[asymptotic_expansion|no-title]]
Hence, we can see that the integrand converges pointwise to $\exp(-t)$ and even uniformly in any bounded domain.
Applying Hankel's formula for the Gamma function \[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Theorem B.1, p.~745]]\] yields 
$$
\frac{1}{\Gamma(\alpha)} =
\frac{1}{2\pi \mathrm{i}} \int_{\mathcal{H}(n)}(-t)^{-\alpha}\exp(-t)~\mathrm{d}t.
$$
Hence, it only remains to argue that integration and limit can be interchanged.
For that purpose we split the contour at the half-line $\mathfrak{R}(z)  = \log^{2}(n)$. Firstly, we establish that the part corresponding to $\mathfrak{R}(z) \geq \log^{2}(n)$ is indeed negligible in the scale of the problem. 
%% We have  %%
%% $$ %%
%% \lim_{n \to \infty} (1 + t/n)^{-n-1} = \exp(-t), %%
%% $$ %%
%% and due to the estimate %%
%% $$ %%
%%   |f_n(t)| := \left|(-t)^{-\alpha} \left(1 + \frac{t}{n}\right)^{-n-1}\right| \leq\left| \frac{t}{1 + t/n}\right|^{-\alpha} \cdot \left(1 + \frac{t}{n}\right)^2 \leq C \left(1 + \frac{t}{n}\right)^2 =: g(t) %%
%% $$ %%
After substituting $u = t + \log^2 n$ and observing
$$\begin{align*}
\exp(\log^2 n) \left(1 + \frac{u + \log^2 n}{n}\right)^{-n-1} &=
\exp\left(\log^2 n - (n+1) \log\left(1 + \frac{u + \log^2 n}{n}\right)\right) \\
&= \exp\left(\log^2 n - (n+1) \left(\frac{u + \log^2 n}{n} + \mathcal{O}\left(\frac{\log^4 n}{n^2}\right) \right) \right) \\
&= \exp\left(- u + \mathcal{O}\left(\frac{\log^4 n}{n}\right) \right) \\
&\xrightarrow[n \to \infty]{} \exp(-u),
\end{align*}$$
we may apply the dominated convergence theorem. This yields, for $\alpha < 0$,
$$\begin{align*}
&\lim_{n \to \infty} \left|\, \exp(\log^2 n) \log^{2\alpha} n\int_{\log^2 n}^\infty (-t)^{-\alpha} \left(1 + \frac{t}{n}\right)^{-n-1} \mathrm{d}t\, \right| \\
%% \lim_{n \to \infty}  \exp(\log^2 n) \int_{0}^\infty (-u -\log^2 n)^{-\alpha} \left(1 + \frac{u + \log^2 n}{n}\right)^{-n} \mathrm{d}u \\ %%
&\leq \lim_{n \to \infty} \left(\int_{0}^\infty u^{-\alpha} \exp(\log^2 n) \left(1 + \frac{u + \log^2 n}{n}\right)^{-n-1} \mathrm{d}u\right)
\\
&= \int_{0}^\infty u^{-\alpha} \exp(-u)~\mathrm{d}u
= \Gamma(1 - \alpha) < \infty.
\end{align*}$$
For $\alpha \geq 0$, we have 
$$\begin{align*}
&\lim_{n \to \infty} \left|\, \exp(\log^2 n) \int_{\log^2 n}^\infty (-t)^{-\alpha} \left(1 + \frac{t}{n}\right)^{-n-1} \mathrm{d}t\, \right| \\
%% \lim_{n \to \infty}  \exp(\log^2 n) \int_{0}^\infty (-u -\log^2 n)^{-\alpha} \left(1 + \frac{u + \log^2 n}{n}\right)^{-n} \mathrm{d}u \\ %%
&\leq \lim_{n \to \infty} \left(\int_{0}^\infty \exp(\log^2 n) \left(1 + \frac{u + \log^2 n}{n}\right)^{-n-1} \mathrm{d}u\right)
\\
&= \int_{0}^\infty \exp(-u)~\mathrm{d}u
= 1 < \infty.
\end{align*}$$
Finally, we observe that
$$
\exp\left(-\log^2 n\right) = o(\exp( - k \log n)) = o\left(n^{-k}\right)
$$
for any fixed $k$. Further, $f_n(t)$ converges uniformly to $(-t)^{-\alpha}\exp(-t)$ for $|t| \leq \log^2(n)$ and thus we have the asymptotic estimate
$$\begin{align*}
f_{n} 
%% &= \frac{n^{\alpha-1}}{2\pi \mathrm{i}}\int_\mathcal{H} (-t)^{-\alpha}\left(1 + \frac{t}{n}\right)^{-n-1} \mathrm{d}t \\ %%
&= \frac{n^{\alpha-1}}{2\pi \mathrm{i}}
\left(
\int_{\mathcal{H}(n)_{< \log^2 n}} (-t)^{-\alpha}\left(1 + \frac{t}{n}\right)^{-n-1}\mathrm{d}t +
\int_{\mathcal{H}(n)_{\geq \log^2 n}} (-t)^{-\alpha}\left(1 + \frac{t}{n}\right)^{-n-1} \mathrm{d}t
\right) \\
&= \frac{n^{\alpha-1}}{2\pi \mathrm{i}}
\left(
\left(
1 + \mathcal{O}\left(\frac{\log^2 n}{n}\right)
\right)
\left(
\int_{\mathcal{H}(n)_{< \log^2 n}} (-t)^{-\alpha}\exp(-t)~\mathrm{d}t
\right) +
o\left(n^{-k} \log^{2|\alpha|} n \right)
%% \int_{\mathcal{H}_{\geq \log^2 n}} (-t)^{-\alpha}\left(1 + \frac{t}{n}\right)^{-n-1} \mathrm{d}t %%
\right) \\
&\xrightarrow[n \to \infty]{} \frac{n^{\alpha-1}}{\Gamma(\alpha)}\left(1 + \mathcal{O}\left(\frac{\log^2 n}{n}\right)\right).
\end{align*}$$
Now we can use a terminating form of the asymptotic expansion in [[asymptotic_expansion]] to develop an expansion to any predetermined order. This is possible because $t/n = \mathcal{O}((\log^2 n) /n)$ is small.
To simplify the expansion we make use of the property of the Gamma function that 
$$
\frac{1}{\Gamma(\alpha - k)} = \frac{1}{\Gamma(\alpha)}(\alpha - 1)\cdots(\alpha - k).
$$
We develop it as an example up to $\mathcal{O}\left(n^{-2}\right)$:
$$\begin{align*}
f_{n} &\sim \frac{n^{\alpha-1}}{2\pi \mathrm{i}}\int_\mathcal{H} (-t)^{-\alpha}\exp(-t)\left(1+\frac{t^{2}-2t}{2n}\right)\mathrm{d}t\\
&= \frac{n^{\alpha-1}}{\Gamma(\alpha)}\left(1 + \frac{1}{2n}(\alpha - 1)\left(\alpha -2\right) + \frac{1}{n}(\alpha - 1)\right)\\
&= \frac{n^{\alpha-1}}{\Gamma(\alpha)}\left(1 + \frac{\alpha(\alpha-1)}{2n}\right). {\qquad\blacksquare}
\end{align*}$$
