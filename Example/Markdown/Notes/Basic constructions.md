---
tags:
  - Definition
---
%% {\[[[Analytic combinatorics|Flajolet & Sedgewick, 2009, Section I.2, pp.~24–26]]\]} %%
Here we introduce formally the basic constructions that form the core of a specification language for combinatorial structures. 
Let $\mathcal{B}$ and $\mathcal{C}$ be two combinatorial classes. For the combinatorial sum we assume $\mathcal{B}$ and $\mathcal{C}$ to be disjoint.
- Combinatorial sum (disjoint union) $\mathcal{A} = \mathcal{B} + \mathcal{C}$:
$$
\mathcal{A} := \mathcal{B} \cup \mathcal{C}, \qquad
|\alpha|_{\mathcal{A}} = \begin{cases}
|\alpha|_{\mathcal{B}} & \text{if $\alpha \in \mathcal{B}$} \\
|\alpha|_{\mathcal{C}} & \text{if $\alpha \in \mathcal{C}$}
\end{cases}.
$$
- Cartesian product $\mathcal{A} = \mathcal{B} \times \mathcal{C}$: 
$$
\mathcal{A} := \{\, \alpha = (\beta, \gamma) \mid \beta \in \mathcal{B}, \gamma \in \mathcal{C} \,\}, \qquad
|(\beta, \gamma)|_{\mathcal{A}} = |\beta|_{\mathcal{B}} + |\gamma|_{\mathcal{C}}.
$$
- Sequence construction $\mathcal{A} = \textsc{Seq}(\mathcal{B})$:
$$
\mathcal{A} := \{\, (\beta_1,\dots,\beta_n) \mid n \geq 0, \beta_j \in \mathcal{B} \,\}, \qquad
|(\beta_1,\dots,\beta_n)|_{\mathcal{A}} = \sum_{k = 1}^n |\beta_k|_{\mathcal{B}}.
$$
- Cycle construction $\mathcal{A} = \textsc{Cyc}(\mathcal{B})$:
$$
\mathcal{A} := (\textsc{Seq}(B) \setminus \{\varepsilon\}) / S,
$$
where $S$ is the equivalence relation between sequences defined by
$$
(\alpha_1,\dots,\alpha_r)\,S\,(\beta_1,\dots,\beta_r)
$$
iff there exists a circular shift $\tau$ such that for all $j \colon \alpha_j = \beta_{\tau(j)}$.
The size function carries over from $\textsc{Seq}(B)$.
- Multiset construction $\mathcal{A} = \textsc{MSet}(\mathcal{B})$:
$$
\mathcal{A} := \textsc{Seq}(\mathcal{B}) / R,
$$
where $R$ is the equivalence relation between sequences defined by
$$
(\alpha_1,\dots,\alpha_r)\,R\,(\beta_1,\dots,\beta_r)
$$
iff there exists an arbitrary permutation $\sigma$ such that for all $j \colon \alpha_j = \beta_{\sigma(j)}$.
The size function carries over from $\textsc{Seq}(B)$.
- Powerset construction $\mathcal{A} = \textsc{PSet}(\mathcal{B})$:
$$
\mathcal{A} := \{\, B \mid B \subset \mathcal{B} \,\}.
$$
As $\textsc{PSet}(\mathcal{B}) \subset \textsc{MSet}(\mathcal{B})$, the size function carries over from $\textsc{Seq}(B)$ as well.
