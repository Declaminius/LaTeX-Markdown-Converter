---
label: fig:stacked_directed_animals
subfigures:
  - "[[Subfigure. A strict, connected heap H with three minimal dimers]]"
  - "[[Subfigure. We partition the heap into three pyramids by iteratively pushing all minimal dimers except the right]]"
  - "[[Subfigure. Replace each cell by a dimer]]"
  - "[[Subfigure. We construct V(overlineH) by iteratively translating the separated pyramids to directed lattice anim]]"
tags:
  - Figure
---
#### Figure: Constructing a square lattice animal from a strict, connected heap

![[Constructing a square lattice animal from a strict, connected heap.PNG]]

#### Sourcecode

```
\begin{figure}
\centering
\begin{subfigure}{0.48 \textwidth}
\centering
\includegraphics{images/ipe/connected heap elephant}
\caption{A strict, connected heap $H$ with three minimal dimers.}
\end{subfigure}
\hfill
\begin{subfigure}{0.48 \textwidth}
\centering
\includegraphics{images/ipe/stacked pyramids elephant}
\caption{We partition the heap into three pyramids by iteratively pushing all minimal dimers except the rightmost one up.}
\end{subfigure}
\vskip\baselineskip
 \begin{subfigure}{0.4 \textwidth} 
   \centering 
   \includegraphics{images/ipe/transformation to heap} 
   \caption{Replace each cell by a dimer.} 
 \end{subfigure} 
\centering
\begin{subfigure}{0.6 \textwidth}
\centering
\includegraphics{images/ipe/elephant}
\caption{We construct $V(\overline{H})$ by iteratively translating the separated pyramids to directed lattice animals and pushing them together to obtain a connected lattice animal.}
\end{subfigure}
\caption[Constructing a square lattice animal from a strict, connected heap.]{Constructing the square lattice animal $\overline{V}(H)$ from a strict, connected heap $H$.}
\label{fig:stacked_directed_animals}
\end{figure}
```