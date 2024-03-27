---
label: table:4paths
tags:
  - Table
---
#### Table
|  | ending anywhere | ending at$0$ |
| - | - | - |
| \makecell{unconstrained |
| (on$\Z$)} | \makecell{ |
| \includegraphics[width = 0.25\linewidth]{images/ipe/walk.pdf} |
| walk/path ($\mathcal{W}$) \vspace{2mm} |
| $W(z) = \frac{1}{1-zP(1)}$\vspace{2mm}} | \makecell{ |
| \includegraphics[width = 0.25\linewidth]{images/ipe/bridge.pdf} |
| bridge ($\mathcal{B}$) \vspace{2mm} |
| $B(z) = z \sum_{i=1}^c\frac{u_i'(z)}{u_i(z)}$\vspace{2mm}} |
| \makecell{constrained |
| (on$\Z_+$)} | \makecell{ |
| \includegraphics[width = 0.25\linewidth]{images/ipe/meander.pdf} |
| meander ($\mathcal{M}$) \vspace{2mm} |
| $M(z) = \frac{1}{1-zP(1)} \prod_{i=1}^c(1-u_i(z))$\vspace{2mm}} | \makecell{ |
| \includegraphics[width = 0.25\linewidth]{images/ipe/excursion.pdf} |
| excursion ($\mathcal{E}$) \vspace{2mm} |
| $E(z) = \frac{(-1)^{c-1}}{p_{-c}z}\prod_{i=1}^c u_i(z)$\vspace{2mm}} |
#### Sourcecode

```
\begin{table}[hbt!]
\centering
\begin{tabular}{|c|c|c|}
\hline
& ending anywhere & ending at $0$ \\ \hline
\makecell{unconstrained \\ (on $\Z$)} &
\makecell{\\ \includegraphics[width = 0.25\linewidth]{images/ipe/walk.pdf} \\ walk/path ($\mathcal{W}$) \vspace{2mm} \\ $W(z) = \frac{1}{1-zP(1)}$ \vspace{2mm}} &
\makecell{\\ \includegraphics[width = 0.25\linewidth]{images/ipe/bridge.pdf} \\ bridge ($\mathcal{B}$) \vspace{2mm} \\ $B(z) = z \sum_{i=1}^c\frac{u_i'(z)}{u_i(z)}$ \vspace{2mm}} \\ \hline
\makecell{constrained \\ (on $\Z_+$)} &
\makecell{\\ \includegraphics[width = 0.25\linewidth]{images/ipe/meander.pdf} \\ meander ($\mathcal{M}$) \vspace{2mm} \\ $M(z) = \frac{1}{1-zP(1)} \prod_{i=1}^c(1-u_i(z))$ \vspace{2mm}} &
\makecell{\\ \includegraphics[width = 0.25\linewidth]{images/ipe/excursion.pdf} \\ excursion ($\mathcal{E}$) \vspace{2mm} \\ $E(z) = \frac{(-1)^{c-1}}{p_{-c}z}\prod_{i=1}^c u_i(z)$ \vspace{2mm}} \\ \hline
\end{tabular}
\caption[The four types of directed paths.]{The four types of directed paths: walks, bridges, meanders and excursions and the corresponding generating functions \cite[Fig.~1]{Basic}.}
\label{table:4paths}
\end{table}
```