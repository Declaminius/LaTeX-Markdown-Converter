---
tags:
  - Example
label: ex:ballot_problem
---
The formula for the number $d_{2n}$ of Dyck excursions consisting of $2n$ steps can be derived using a counting argument that is now referred to as André’s reflection principle, even though André himself never employed the method \[[[Lost (and found) in translation André's actual method and its application to the generalized ballot problem|Renault, 2008]]\].
The idea is the following: We count lattice paths consisting of $n$ **NE**-steps and $n$ **SE**-steps and then subtract the number of such paths that are not Dyck paths.

A lattice path consisting of $n$ **NE**-steps and $n$ **SE**-steps can be uniquely identified by the position of the **NE**-steps, which yields $\binom{2n}{n}$ possible such lattice paths.
Hence, the number of Dyck bridges of length $2n$ is given by $\binom{2n}{n}$. Now we subtract all paths that go below the $x$-axis at some point.

> [!tip]+ Figure: The reflection principle
> ![[Figure. The reflection principle#Figure The reflection principle|no-h4]]

Let $p$ be a lattice path with $n$ **NE**-steps and $n$ **SE**-steps that is not a Dyck path. Then pick the first step that lies beneath the $x$-axis and change all **NE**-steps occurring afterwards into **SE**-steps and vice-versa. 
These reflected paths must all end at $(2n,-2)$ since we reflect the path after the point when it hits $y = -1$ for the first time; see Figure [[Figure. The reflection principle]]. This means that one net **NE**-step gets flipped to one net **SE**-step. The number of paths consisting of $(n-1)$ **NE**-steps and $(n+1)$ **SE**-steps can be counted via $\binom{2n}{n-1}.$ By subtracting these unwanted reflected paths we see that the number of Dyck excursions with $2n$ steps satisfies
$$
d_{2n} = \binom{2n}{n} - \binom{2n}{n-1} = \binom{2n}{n} - \frac{n}{n+1}\binom{2n}{n} = \frac{1}{n+1}\binom{2n}{n}.
$$
In addition, if we interpret a **NE**-step as a vote for candidate $A$ and a **SE**-step as a vote for candidate $B$ we see that we rederived the solution to Bertrand's ballot problem for the special case that the total number of votes for candidate $A$ equals the number of votes for candidate $B$.
