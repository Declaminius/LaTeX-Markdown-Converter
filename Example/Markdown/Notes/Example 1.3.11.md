---
tags:
  - Example
label: ex:catalan_numbers
---
In Example~[[André’s reflection principle]] we already derived the counting sequence of Dyck excursions to be $d_{2n} = \frac{1}{n + 1}\binom{2n}{n}$, also known as the Catalan numbers. Now we will present an alternative way to derive this result, using the symbolic method:

Let $\mathcal{D}$ denote the combinatorial class of Dyck excursions, let $\omega_0 \in \mathcal{D}$ be an arbitrary Dyck excursion and let $D(z)$ be the corresponding generating function. We now partition $\omega_0$ into two (possibly empty) shorter Dyck excursions via a technique called a first passage decomposition. If $\omega$ is not the empty path, there exists a second point of contact $x_0$ with the $x$-axis. Now we decompose $\omega$ into the path $\omega_1$ starting from the origin and ending at $x_0$ and the (possibly empty) path $\omega_2$ from $x_0$ to the endpoint of $\omega$. Since the first passage $\omega_1$ is non-empty, we can describe it as a sequence of an initial **NE**-step, a (possibly empty) Dyck excursion starting and ending at altitude one, and a final **SE**-step back down to the $x$-axis.
Hence, the formal symbolic specification for the class of Dyck excursions $\mathcal{D}$ reads
$$
\mathcal{D} = \mathcal{E} \cup (\mathcal{Z}_{\mathrm{NE}} \times \mathcal{D} \times \mathcal{Z}_{\mathrm{SE}}) \times \mathcal{D}.
$$
Using the translation schemes of Theorem [[Theorem 1.3.10]] we obtain the functional equation
$$
D(z) = 1 + z^2D(z)^2.
$$
This quadratic equation admits the two possible solutions
$$
D_\pm(z) = \frac{1 \pm \sqrt{1 - 4z^2}}{2z^2}.
$$
An expansion of the square root term around zero shows that only $D_-(z)$ admits a power series expansion around zero, with $D_+(z)$ possessing a polar singularity at zero. Hence, we conclude
$$\begin{align*}
D(z) &= \sum_{n=0}^\infty d_n z^n = \frac{1 - \sqrt{1 - 4z^2}}{2z^2} \\
&= 1 + z^2 + 2z^4 + 5z^6 + 14z^8 + 42z^{10} + 132z^{12} + 429z^{14} + \mathcal{O}(z^{16}).
\end{align*}$$
In order to extract the coefficients of $D(z)$, we use the double factorial notation $n!!$ to denote the product of all positive integers up to $n$ that have the same parity as $n$.
Then, using Newton's generalized binomial theorem [[Newton's generalized binomial theorem]], we rederive the formula
$$\begin{align*}
d_{2n} &= [z^{2n}] \left(\frac{1 - \sqrt{1 - 4z^2}}{2z^2}\right)
= -\frac{1}{2}[z^{2n+2}]\left(\sum_{k \geq 0} \binom{\frac{1}{2}}{k} (-4z)^{2k}\right) \\
&= (-1)^n\frac{1}{2} \frac{(1/2)\cdot(-1/2)\cdot(-3/2)\cdots(-(2n-1)/2)}{(n+1)!}4^{n+1} \\
&= \frac{1}{4} \cdot \frac{1}{2^n} \cdot \frac{(2n-1)!!}{(n+1)!}\cdot 4^{n+1}
%% &= \frac{1}{2^n} \cdot \frac{(2n)!}{(n+1)!(2n)!!} \cdot 4^n \\ %%
= \frac{1}{4^n} \cdot \frac{(2n)!}{(n+1)!n!} \cdot 4^n
= \frac{1}{n+1}\binom{2n}{n}. {\qquad\blacksquare}
\end{align*}$$
