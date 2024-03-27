---
Theorem: "[[Diplomarbeit. Corollary 4.2.10]]"
tags:
  - Proof
---
 %%
%%   Since we are still dealing with symmetric step sizes, the dominant singularity is still guaranteed to be a simple pole. In this case, we find $\rho_0 = 2/9$. An application of Theorem [[Asymptotics of excursions with catastrophes]] %%
%%   together with some computer algebra yields %%
%%   $$ %%
%%   [z^n] M_{\mathcal{M}_2}^\mathrm{alt}(z) = \frac{3}{4} \left(\frac{9}{2}\right)^n + o(K^n). %%
%%   $$ %%
%%   for some $K < 9/2$. %%
%%   We continue by subtracting the pole in order to get to the asymptotic behavior at the square root singularity at $\rho = 1/4$. %%
%%   At $\rho = 1/4$ we develop  %%
%%   $$ %%
%%     G(z) := M_{\mathcal{M}_2}^\mathrm{alt}(z) + \frac{1}{6} \left(z -\frac{2}{9}\right)^{-1} %%
%%   $$ %%
%%   into a Puiseux series with critical exponent $\alpha = 1/2$:  %%
%%   $$ %%
%%     G(z) = 6 - 8(1-4z)^{1/2}  + 46(1-4z) + \mathcal{O}\left((1-4z)^{3/2}\right). %%
%%   $$ %%
%%   Translating this result with the standard function scale [[Standard function scale]] leads to the claimed result. %%
%% 