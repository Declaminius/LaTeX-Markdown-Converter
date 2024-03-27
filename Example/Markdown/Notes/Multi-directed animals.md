---
tags:
  - Definition
label: def:multi_directed_animals
---
Let $H$ be an arbitrary connected heap. We now construct an extension of $\overline{V}$ to connected heaps via induction over the number of minimal dimers $k$ of $H$:
- For $k = 1$, the heap $H$ reduces to a simple pyramid and thus, according to Remark~[[Diplomarbeit. Remark 5.1.13]], $\overline{V}(H)$ is already well-defined.
- If instead $H$ has $k > 1$ minimal dimers, we push the $(k-1)$ leftmost pyramids upwards, producing a connected heap $H'$ with $k-1$ minimal dimers, placed far above the remaining pyramid $P_k$. Now recursively replace $H'$ by $\overline{V}(H')$ and $P_k$ by $\overline{V}(P_k)$.
- Finalize the construction by pushing $\overline{V}(H')$ downwards until it connects to $\overline{V}(P_k)$.
We define $\overline{V}(H)$ as the resulting animal and call the class of triangular lattice animals obtainable in this way *triangular multi-directed animals*.
The case of square lattice animals is a bit more delicate, since $V$ does not necessarily map them to strict heaps, as illustrated in Figure [[Figure. Constructing a connected heap from a square lattice animal]]. However, the converse is still valid: If we apply $\overline{V}$ to a strict heap $H$, we obtain a square lattice animal. This is guaranteed by the fact that $\overline{V}$ maps strict pyramids to directed square animals. 
Hence, we restrict the above procedure to strict, connected heaps to obtain the class of *square multi-directed animals*; see Figure [[Figure. Constructing a square lattice animal from a strict, connected heap]].
