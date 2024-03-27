---
Theorem: "[[Diplomarbeit. Theorem 4.1.6]]"
tags:
  - Proof
---

The proof follows the arguments in Theorem [[Diplomarbeit. Theorem 4.1.3]] almost word for word and the procedure is illustrated in Figure [[Figure. Bijection involving Motzkin meanders with alternative catastrophes]].
Let $\omega_E$ denote an arbitrary 3-Motzkin excursion. 
Simply transform every blue {\color{lightblue} **E**}-step in $\omega_E$ to a **NE**-step.
Each **NE**-step, black **E**-step and **SE**-step stays unchanged.
Finally, we map every red {\color{catred} **E**}-step to a catastrophe.

Hence, for the inverse mapping, it only remains to determine, which **NE**-steps get mapped to a blue {\color{lightblue} **E**}-step and which **NE**-steps stay unchanged.
For that, we first split $\omega_\mathcal{D}$ into a sequence of meanders without catastrophes, with a catastrophe separating them, and a final meander without any catastrophes at the end.
Then, for each meander in the sequence, we apply a last passage decomposition and turn the last **NE**-step to leave altitude $i = 0, \dots, k - 1$ into a blue {\color{lightblue} **E**}-step, where $k$ is the final height of the meander. This procedure ensures that all **E**-steps occur only at height zero.
