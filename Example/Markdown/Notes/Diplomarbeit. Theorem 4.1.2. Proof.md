---
Theorem: "[[Diplomarbeit. Theorem 4.1.2]]"
tags:
  - Proof
---

Let $\omega_\mathcal{M}$ be an arbitrary 2-Motzkin excursion. 
Start by transforming every blue {\color{lightblue} **E**}-step in $\omega_\mathcal{M}$ into a **NE**-step. 
The **NE**-step and **SE**-steps in $\omega_\mathcal{M}$ remain unchanged.
Finally, transform every red {\color{catred}**E**}-step in $\omega_\mathcal{M}$ into a catastrophe.
This process clearly yields a valid Dyck meander with alternative catastrophes, since the height at each point may only increase in this procedure and alternative catastrophes may occur at any height.

For the inverse mapping we consider an arbitrary Dyck meander $\omega_\mathcal{D}$ with alternative catastrophes. Clearly, every catastrophe in $\omega_\mathcal{D}$ needs to map to a {\color{catred}**E**}-step and every **SE**-step needs to remain unchanged.
Hence, it only remains to determine, which **NE**-steps get mapped to a blue {\color{lightblue} **E**}-step and which **NE**-steps stay unchanged. For that, we first split $\omega_\mathcal{D}$ into a sequence of meanders without catastrophes, with a catastrophe separating them, and a final meander without any catastrophes at the end.
Then, for each meander in the sequence, we apply a last passage decomposition and turn the last **NE**-step to leave altitude $i = 0, \dots, k - 1$ into a blue {\color{lightblue} **E**}-step, where $k$ is the final height of the meander. This procedure ensures that all **E**-steps occur only at height $0$.
For an illustration of this procedure we refer to Figure [[Figure. Bijection involving Dyck meanders with alternative catastrophes]].
