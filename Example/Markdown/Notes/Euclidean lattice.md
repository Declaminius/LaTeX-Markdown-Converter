---
tags:
  - Definition
---
The *Euclidean lattice* consists of the vertices $\mathbb{Z}^d$. The edges are defined indirectly via the step set $\mathcal{S} \subset \mathbb{Z}^d$. Two vertices $v, w \in \mathbb{Z}^d$ are connected by an edge $(v,w) \in E$ iff^["iff" is Paul Halmos' convenient abbreviation for "if and only if".] $w - v \in \mathcal{S}$.
An $n$-step lattice path on the Euclidean lattice from $s \in \Z^d$ to $t \in \Z^d$ is consequently equivalently characterized by a sequence $\omega = (\omega_0,\dots,\omega_n)$ of elements in $\Z^d$ such that
- $\omega_0 = s, \omega_n = t$ and
- $\omega_{i + 1} - \omega_i \in \mathcal{S}$ for $i = 0,\dots,n-1$.
