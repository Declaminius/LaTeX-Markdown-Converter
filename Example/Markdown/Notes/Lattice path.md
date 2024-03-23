---
tags:
  - Definition
---
A *lattice* $\Lambda = (V,E)$ is a mathematical model of a discrete space. It consists of a set $V \subset \mathbb{R}^n$ of vertices and a set $E \subset V^2$ of directed edges. An $n$-step *lattice path* or *lattice walk* or *walk* in $\Lambda$ from $s \in V$ to $t \in V$ is a sequence $\omega = (\omega_0,\omega_1,\dots,\omega_n)$ of elements in $V$ such that 
- $\omega_0 = s, \omega_n = t$ and
- $(\omega_i,\omega_{i+1}) \in E$ for $i = 0, \dots, n - 1$.
The *length* $|\omega|$ of a lattice path is the number of edges in the sequence $\omega$.
A lattice $\Lambda$ is called *homogenous*, if the number of $n$-step walks starting from $s \in V$ is independent from the starting point $s$ for all values of $n$.
