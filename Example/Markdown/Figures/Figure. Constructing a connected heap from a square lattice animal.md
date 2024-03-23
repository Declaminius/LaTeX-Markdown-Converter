---
label: fig:connected_heap
subfigures:
  - "[[Subfigure. A lattice animal on the square grid]]"
  - "[[Subfigure. Rotate the animal by 45circ degrees and replace each cell by a dimer]]"
  - "[[Subfigure. Replace each cell by a dimer]]"
  - "[[Subfigure. Let the dimers fall]]"
tags:
  - Figure
---
#### Figure: Constructing a connected heap from a square lattice animal

![[Constructing a connected heap from a square lattice animal.PNG]]

#### Sourcecode

```
\begin{figure}[hbt!]
\centering
\begin{subfigure}{0.45 \textwidth}
\centering
\includegraphics{images/ipe/general polyomino}
\caption{A lattice animal on the square grid.}
\end{subfigure}
\hfill
\begin{subfigure}{0.45 \textwidth}
\centering
\includegraphics{images/ipe/rotated animal}
\caption{Rotate the animal by $45^\circ$ degrees and replace each cell by a dimer.}
\end{subfigure}
\vskip\baselineskip
 \begin{subfigure}{0.4 \textwidth} 
   \centering 
   \includegraphics{images/ipe/transformation to heap} 
   \caption{Replace each cell by a dimer.} 
 \end{subfigure} 
\centering
\begin{subfigure}{0.45 \textwidth}
\centering
\includegraphics{images/ipe/drop}
\caption{Let the dimers fall.}
\end{subfigure}
\caption[Constructing a connected heap from a square lattice animal.]{Constructing the connected heap $V(A)$ from an animal $A$ on the square grid.}
\label{fig:connected_heap}
\end{figure}
```