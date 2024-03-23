---
tags:
  - Definition
---
%% {\[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Definition III.3, p.~163]]\]} %%
Let $\mathcal{A}$ be a combinatorial class equipped with a (multidimensional) *parameter* $\chi = (\chi_1,\dots,\chi_d): \mathcal{A} \to \N^d$. Let $\textbf{u} = (u_1,\dots,u_d)$ denote a vector of $d$ formal variables and let $\textbf{k} = (k_1,\dots,k_d) \in \N^d$ denote an integer-valued vector of parameters. We make use of the multi-index convention and introduce the shorthand notation $\textbf{u}^\textbf{k}$ for the multipower
$$
\textbf{u}^\textbf{k} := u_1^{k_1} u_2^{k_2} \cdots u_d^{k_d}.
$$
The counting sequence of $\mathcal{A}$ with respect to size and the parameter $\chi$ is then defined by
$$
a_{n,\textbf{k}} = \big|\{\, \alpha \in \mathcal{A}_n \mid \chi_1(\alpha) = k_1, \dots, \chi_d(\alpha) = k_d \,\}\big|.
$$
Further, the *multivariate generating function (MGF)* of the sequence $(a_{n,\textbf{k}})_{n \in \N, \textbf{k} \in \N^d}$ is defined as the formal power series
$$
A(z,\textbf{u}) = \sum_{n, \textbf{k}} a_{n,\textbf{k}}\textbf{u}^{\textbf{k}} z^n. 
$$
One also says that $A(z,\textbf{u})$ is the MGF of the combinatorial class $\mathcal{A}$, with the formal variable $u_j$ marking the parameter $\chi_j$ and $z$ marking size.
This function can formally be interpreted as a formal power series in $z$ with coefficients in $\mathbb{Q}[\textbf{u}]$.
In addition, one easily recovers the ordinary generating function of the combinatorial class $\mathcal{A}$ by setting $A(z) = A(z,\textbf{1}).$
