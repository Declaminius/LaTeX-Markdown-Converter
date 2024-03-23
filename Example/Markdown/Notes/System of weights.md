---
tags:
  - Definition
---
For a given step set $\mathcal{S}$ we define the respective *system of weights* as $\Pi = \{\, p_s \mid s \in \mathcal{S} \,\}$, where $p_s > 0$ is the weight associated to step $s \in \mathcal{S}$.
The *weight* of a lattice path is then defined as the product of the weights of its individual steps.
Some useful choices are:
- $\forall \, s \in \mathcal{S} \colon p_s = 1$, representing combinatorial paths in the standard sense.
- $\forall \, s \in \mathcal{S} \colon p_s \in \mathbb{N}$, representing paths with colored steps, for example, $p_s = 2$ means that the associated step has two possible colors.
- $\sum_{s \in \mathcal{S}} p_s = 1$, representing a probabilistic model of paths, where step $s$ is chosen with probability $p_s$.
