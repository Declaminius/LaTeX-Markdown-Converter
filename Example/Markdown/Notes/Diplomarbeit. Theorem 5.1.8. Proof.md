---
Theorem: "[[Diplomarbeit. Theorem 5.1.8]]"
tags:
  - Proof
---

Let $H$ be the connected heap of dimers representing a stacked directed animal on the square grid and denote with $P_1,P_2,\dots,P_k$ the corresponding pyramidal factors of $H$. We start our translation into lattice paths with the rightmost pyramid $P_k$. If $k = 1$, we simply apply Lemma [[Diplomarbeit. Lemma 5.1.7]] to translate $H$ into a Motzkin excursion with catastrophes only occurring at height $h = 0$.
%% With the help of the previous two lemmata we can already translate pyramids into Motzkin excursions with catastrophes only at height $0$, where we reinterpret the {\color{catred} red} **E**-steps in Lemma [[Diplomarbeit. Lemma 5.1.7]] as horizontal catastrophes.  %%
Otherwise, if $k > 1$, after we have drawn $P_k$,
the so far unused catastrophes from heights $h > 0$ will now encode the position where $P_k$ is placed below $P_{k-1}$. 
Recall that the number of ways that $P_k$ can be placed equals the right width of $P_{k-1}$. 
We will now define the distance between the two pyramids as the horizontal distance between the leftmost dimer of $P_k$ and the minimal dimer of $P_{k-1}$. Let us denote this distance with $\ell$, which will correspond to the height of the following catastrophe. 
We now make the first $\ell$ recursive factorizations of $P_{k-1}$ explicit. This yields $\ell$ half-pyramids $Q_{k-1,1},\dots,Q_{k-1,\ell}$ stacked diagonally to the right on top of each other and a final pyramid $P_{k-1}^\prime$ above them as illustrated in Figure [[Figure. Recursive construction of stacked pyramids]]. Note that the minimal dimer of $P_{k-1}^\prime$ is the first dimer whose horizontal projection intersects with the horizontal projection of $P_k$, thus connecting the pyramids.
Now we need to deviate from the construction presented in Lemma [[Diplomarbeit. Lemma 5.1.7]], as we need to introduce $\ell$ additional **NE**-steps in order to offset the height lost with the new catastrophe. 
Hence, the start of each of the half-pyramids $Q_i$ will be marked with a **NE**-step instead of with a horizontal catastrophe, like in Lemma [[Diplomarbeit. Lemma 5.1.7]]. 
In particular, this means that the start of a new pyramid is always marked with an additional **NE**-step. 
This additional step is important, as otherwise each pyramid consisting of $m$ dimers would be translated to a lattice path of length $m - 1$, and the final length of the lattice path would depend on the number of pyramids.
%% In particular, this means that the minimal dimer of $P_{k-1}$ will be translated to a **NE**-step. %%
The half-pyramids themselves are then simply translated according to the recursion rules from Lemma [[Diplomarbeit. Lemma 5.1.6]]. 
Note that these rules remain legitimate on altitude $i > 0$, as they do not involve horizontal catastrophes, which may only happen at height $0$.
%% The horizontal projection of the right vertex of the minimal dimer of $P_{k-1}^\prime$ then equals the horizontal projection of the left vertex of the leftmost dimer of $P_k$. A distance of $n$ thus translates to a catastrophe from height $n$. %%
Thus, the last half-pyramid $Q_{k-1,\ell}$ before $P_{k-1}'$ will be represented by a Motzkin excursion starting and ending at height $\ell$. 
After that, a catastrophe from height $\ell$ will usher in the start of the image of $P_{k-1}'$, which can now again be drawn according to the rules of Lemma [[Diplomarbeit. Lemma 5.1.7]], as it no longer starts at a positive height.
This procedure, illustrated in Figure [[Figure. Recursive construction of stacked pyramids]], can now be iterated over all pyramidal factors of $H$ to obtain the final lattice path image of $H$.


> [!tip]+ Figure: Recursive construction of stacked pyramids
> ![[Figure. Recursive construction of stacked pyramids#Figure Recursive construction of stacked pyramids|no-h4]]

For the inverse mapping, let $M$ be a Motzkin excursion with alternative catastrophes. If $M$ does not contain any non-horizontal catastrophes, we may simply apply Lemma [[Diplomarbeit. Lemma 5.1.7]] to translate $M$ to a single pyramid. Otherwise, we split $M$ at every non-horizontal catastrophe. This yields a set of excursions $E_1,E_2,\dots,E_k$, with $k > 1$, each having exactly one non-horizontal catastrophe at their very end.
Consider the first of these excursions $E_1$, which will correspond to the rightmost pyramid $P_k$ of $H$ and the start of the next pyramid $P_{k-1}$. To recover $P_k$, it suffices to apply the procedure described in Lemma [[Diplomarbeit. Lemma 5.1.7]].
However, this alone does not yet tell us, at which point we need to start drawing $P_{k-1}$. For that we need to look ahead to the non-horizontal catastrophe, which signals the end of $E_1$. The start of $P_{k-1}$ then corresponds to the last time $E_1$ leaves altitude zero before its final catastrophe, which can be intuitively described as the first **NE**-step visible from the viewpoint of the next catastrophe. The next question we need to answer is where to place the minimal dimer of $P_{k-1}$. 
For this we start at the horizontal projection of the leftmost dimer of $P_k$ and move $\ell + 1$ units to the left, where $\ell$ is the height of the catastrophe at the end of $E_1$. This is where we place the minimal dimer of $P_{k-1}$ and start building the first half-pyramid $Q_{k-1,1}$.
Similarly, the last time $E_1$ leaves altitude one marks the start of the next half-pyramid $Q_{k-1,i+1}$. The minimal dimer of $Q_{k-1,i+1}$ needs to be placed diagonally right above the highest dimer in the rightmost column of $Q_{k-1,i}$.
Now we can iterate this process until we hit the catastrophe, which marks the start of the pyramid $P_{k-1}'$. 
Now the process repeats, as we draw $P_{k-1}'$ until we reach the first **NE**-step visible from the next non-horizontal catastrophe; see Figure [[Figure. Bijection involving stacked directed animals]] for an example of this correspondence.

In the case of stacked directed animals on the triangular grid, we are now working with general pyramids. We reduce this case to strict pyramids by simply inserting a blue {\color{blue}**E**}-step for every dimer lying directly above another dimer.
