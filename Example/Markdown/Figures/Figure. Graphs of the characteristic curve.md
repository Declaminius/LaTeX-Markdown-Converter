---
label: fig:characteristic_curve
subfigures:
  - "[[Subfigure. Graph of P(u)]]"
  - "[[Subfigure. Graph of 1P(u)]]"
  - "[[Subfigure. Graph of the two small branches u_1, u_2 of order pm z12 and the only real large branch v_1 of order]]"
tags:
  - Figure
---
#### Figure: Graphs of the characteristic curve

![[Graphs of the characteristic curve.PNG]]

#### Sourcecode

```
\begin{figure}
\centering
\begin{subfigure}{.47\textwidth}
\includegraphics[width=\textwidth]{images/P(u).eps}
\caption{Graph of $P(u)$.}
\end{subfigure}
\begin{subfigure}{.47\textwidth}
\includegraphics[width=\textwidth]{images/P(u)^-1.eps}
\caption{Graph of $1/P(u)$.}
\end{subfigure}
\vskip\baselineskip
\begin{subfigure}{.47\textwidth}
\centering
\includegraphics[width=\textwidth]{images/char_curve.eps}
\caption{Graph of the two small branches $u_1, u_2$ of order $\pm z^{1/2}$ and the only real large branch $v_1$ of order $z^{-1/3}$ of the characteristic curve.}
\end{subfigure}
\caption[Graphs of the characteristic curve.]{Graphs of $P(u) = u^{-2} + u^{-1} + 1 + u + u^2 + u^3$, the inverse $1/P(u)$ and the three real branches of the characteristic curve $1 - zP(u)$ associated with the set of jumps $\mathcal{S} = \{-2,-1,0,1,2,3\}$ {\[[[Basic analytic combinatorics of directed lattice paths|Banderier & Flajolet, 2002, Figure 3]]\]}.}
\label{fig:characteristic_curve}
\end{figure}
```