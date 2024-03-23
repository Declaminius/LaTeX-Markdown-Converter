---
subfigures:
  - "[[Subfigure. Plane tree]]"
  - "[[Subfigure. Łukasiewicz excursion]]"
tags:
  - Figure
---
#### Figure: Łukasiewicz correspondence

![[Łukasiewicz correspondence.PNG]]

#### Sourcecode

```
\begin{figure}[hbt!]
\centering
\begin{subfigure}{0.45 \textwidth}
\centering
\includegraphics{images/ipe/plane_tree}
\caption[Plane tree.]{A plane tree, with its vertices labeled according to their prefix order.}
\label{fig:plane_tree}
\end{subfigure}
\hfill
\begin{subfigure}{0.45 \textwidth}
\centering
\includegraphics{images/ipe/luka_correspondence}
\caption[Łukasiewicz excursion.]{The corresponding Łukasiewicz excursion.}
\label{fig:Łukasiewicz correspondence}
\end{subfigure}
\caption[Łukasiewicz correspondence.]{The bijection between plane trees and Łukasiewicz excursions.}
\end{figure}
```