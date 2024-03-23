---
Theorem: "[[Lemma 2.3.10]]"
tags:
  - Proof
---

Let the radius of convergence be bounded and let $B := B_R(z_0)$ be the disk of convergence.
Assume that there are no singular points of $f$ on $B$.
For every $w \in \partial B$ there is a disc $B_r(w)$ of positive radius $r(w)$ and a holomorphic function $g$ in $B_r(w)$ such that $f$ and $g$ coincide in $B \cap B_r(w)$.
Choose a finite cover $B_r(w_1) \cup \dots \cup B_r(w_n) \supseteq \partial B$ of the compact boundary of the disk.
There exists an $\tilde{R} > R$ such that 
$$
\tilde{B} := B_{\tilde{R}}(z_0) \subseteq B \cup B_r(w_1) \cup \dots \cup B_r(w_n).
$$
Let $g_j$ be holomorphic in $B_r(w_j)$ with 
$$
f|(B \cap B_r(w_j)) = g|(B \cap B_r(w_j)).
$$
Now we define $\tilde{f}\colon \tilde{B} \to \mathbb{C}$ as an extension of $f$.
If $z \in \tilde{B} \setminus B$, choose a disk $B_r(w_j) \ni z$ and set $\tilde{f}(z) = g_j(z)$.
This function is well-defined, because for $B_r(w_j) \cap B_r(w_k) \neq \emptyset$ there is also 
$$
D := B_r(w_j) \cap B_r(w_k) \cap B  \neq \emptyset.
$$
By definition both $g_j$ and $g_k$ must coincide with $f$ in $D$ and due to the Identity Theorem~[[Theorem 1.4.3]] they must also coincide in $B_r(w_j) \cap B_r(w_k)$.
Now $\tilde{f}$ is a holomorphic function in $\tilde{B}$ coinciding with $f$ in $B$ with a larger radius of convergence than $f$ contradicting our assumption.
