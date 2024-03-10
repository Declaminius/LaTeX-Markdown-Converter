---
Theorem: [[Theorem 1.1.5]]
tags:
  - Proof
---

Let $E_{\mathcal{M}}(z)$ be the generating function of Motzkin excursions and $Q_s(z)$ be the generating function of strict half-pyramids.
Then, Theorem [[Generating functions of directed animals]] shows that 
![[Qs]]
Furthermore, for the bivariate generating function of strict pyramids $P_s(z,u)$, with $u$ marking the right width of the pyramid we have 
$$
P_s(z,u) = \frac{Q_s(z)}{1-uQ_s(z)} = \frac{zE_\mathcal{M}(z)}{1-uzE_\mathcal{M}(z)}.
$$
%% This generating function can also be interpreted as the generating function for the set of Motzkin excursions ending with their first catastrophe with $u$ counting the height of the catastrophe. %%
This generating function also has a lattice path interpretation.
Let $\omega$ be a Motzkin excursion, with catastrophes only at altitude zero and let $u$ count the number of catastrophes in~$\omega$. We split $\omega$ before each catastrophe. This partitions $\omega$ into a Motzkin excursion without catastrophes, counted by $E_\mathcal{M}(z)$, followed by a possibly empty sequence of Motzkin excursions without catastrophes, each preceded by a catastrophe, counted by $u z \cdot E_\mathcal{M}(z)$.
Hence, their generating function $F(z,u)$ satisfies
![[Ps]]
%% Differentiating the equation with respect to $u$ yields  %%
%% $$ %%
%%   \frac{\partial P_s(z,u)}{\partial u} = \frac{Q(z)^2}{(1-uQ(z))^{2}} = P_s(z,u)^2. %%
%% $$ %%
%% This equation can also be interpreted with the symbolic method. Multiplying both sides with $u$ yields the pointing-operator $u \frac{\partial}{\partial u}(\cdot)$ on the left hand side. %%
%% In this case, the pointing operator points on the height $k$ of the catastrophe and we can point at each of the $k$ up-steps visible from the catastrophe, which is the last time the path leaves a given altitude before the catastrophe. %%
%% We cut the path after the marked up-step and turn the up-step into a catastrophe. This yields two Motzkin excursions ending with their first catastrophe. %%
%% The sum of the height of the two catastrophes is exactly one less than the height of the original catastrophe. %%
Further, the generating function for stacked directed animals reads 
![[S]]
Next, we observe that the generating function of Motzkin meanders satisfies
![[motzkin_meanders_animals]]
To wit, consider a last passage decomposition of a Motzkin meander $\omega$. This splits $\omega$ into an initial excursion, counted by $E_{\mathcal{M}}(z)$, followed by a sequence of paths going from altitude $i$ to altitude $i + 1$, while staying above the line $y = i$, counted by $z E_\mathcal{M}(z)$.
Finally, combining [[S]], [[Qs]] and [[motzkin_meanders_animals]], we obtain
$$\begin{equation*}
S(z,1,1) = \frac{Q_s(z)}{1 - \frac{Q_s(z)}{1 - Q_s(z)}} = \frac{zE_\mathcal{M}(z)}{1 - z\frac{E_\mathcal{M}(z)}{1-zE_\mathcal{M}(z)}} = \frac{zE_\mathcal{M}(z)}{1 - zM_\mathcal{M}(z)} = zM_\mathcal{M}(z). {\qquad\blacksquare}
\end{equation*}$$
%% which coincides with the generating function for Motzkin excursions with alternative catastrophes derived in Example \ref{ex:motzkin_excursions} except for an additional factor $z$. %%
