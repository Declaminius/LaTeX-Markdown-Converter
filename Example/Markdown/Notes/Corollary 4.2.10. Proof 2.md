---
Theorem: "[[Corollary 4.2.10]]"
tags:
  - Proof
---
 %%
%%   Since we are still dealing with symmetric step sizes, the dominant singularity is still guaranteed to be a simple pole. In this case, we find $\rho_0 = 2/9$. An application of Theorem [[Theorem 4.2.6]] %%
%%   together with some computer algebra yields %%
%%   $$ %%
%%   [z^n] E_{\mathcal{M}_2}^\mathrm{alt}(z) = \frac{3}{8} \left(\frac{9}{2}\right)^n + o(K^n). %%
%%   $$ %%
%%   for some $K < 9/2$. %%
%%   We continue by subtracting the pole in order to get to the asymptotic behavior at the square root singularity at $\rho = 1/4$. %%
%%   At $\rho = 1/4$ we develop  %%
%%   $$ %%
%%     G(z) := E_{\mathcal{M}_2}^\mathrm{alt}(z) + \frac{1}{12} \left(z -\frac{2}{9}\right)^{-1} %%
%%   $$ %%
%%   into a Puiseux series with critical exponent $\alpha = 1/2$:  %%
%%   $$ %%
%%     G(z) = 3 - 8(1-4z)^{1/2}  + 19(1-4z) + \mathcal{O}\left((1-4z)^{3/2}\right). %%
%%   $$ %%
%%   Translating this result with the standard function scale [[Theorem 2.3.1]] leads to the claimed result. %%
%% 