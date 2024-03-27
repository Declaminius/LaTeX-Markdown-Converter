---
label: tab:standard_function_scale
tags:
  - Table
---
#### Table
| **Function** | **Coefficients** |
| - | - |
| $(1 - z)^{3/2}$ | $\frac{1}{\sqrt{\pi n^{5}}}\left(\frac{3}{4} + \frac{45}{32n} + \frac{1155}{512n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)\right)$ |
| $(1 - z)$ | $(0)$ |
| $(1 - z)^{1/2}$ | $- \frac{1}{\sqrt{\pi n^{3}}}\left(\frac{1}{2} + \frac{3}{16n} + \frac{25}{256n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)\right)$ |
| $1$ | $(0)$ |
| $(1 - z)^{-1/2}$ | $\frac{1}{\sqrt{\pi n}}\left(1 - \frac{1}{8n} + \frac{1}{128n^{2}} + \frac{5}{1024n^{3}} + \mathcal{O}\left(\frac{1}{n^{4}}\right)\right)$ |
| $(1 - z)^{-1}$ | $1$ |
| $(1 - z)^{-3/2}$ | $\sqrt{\frac{n}{\pi}}\left(2 + \frac{3}{4n}- \frac{7}{64n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)\right)$ |
| $(1 - z)^{-2}$ | $n + 1$ |
| $(1 - z)^{-3}$ | $\frac{n^2}{2} + \frac{3n}{2} + 1$ |
#### Sourcecode

```
\begin{table}[hbt!]
\centering
\[\def\arraystretch{1.5}
\begin{array}{c|c}
\hline
\hline
**Function** & **Coefficients** \\ \hline
(1 - z)^{3/2} & \frac{1}{\sqrt{\pi n^{5}}}
\left(
\frac{3}{4} + \frac{45}{32n} + \frac{1155}{512n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)
\right)  \\
(1 - z) & (0) \\ 
(1 - z)^{1/2} & - \frac{1}{\sqrt{\pi n^{3}}}\left(\frac{1}{2} + \frac{3}{16n} + \frac{25}{256n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)\right) \\
1 & (0) \\
(1 - z)^{-1/2} & \frac{1}{\sqrt{\pi n}}\left(1 - \frac{1}{8n} + \frac{1}{128n^{2}} + \frac{5}{1024n^{3}} + \mathcal{O}\left(\frac{1}{n^{4}}\right)\right) \\
(1 - z)^{-1} & 1 \\
(1 - z)^{-3/2} & \sqrt{\frac{n}{\pi}}\left(2 + \frac{3}{4n}- \frac{7}{64n^{2}} + \mathcal{O}\left(\frac{1}{n^{3}}\right)\right) \\
(1 - z)^{-2} & n + 1 \\
(1 - z)^{-3} & \frac{n^2}{2} + \frac{3n}{2} + 1 \\
\hline
\hline
\end{array}
\]
\caption[Table of standard function scale.]{Table of commonly encountered functions within the standard function scale \cite[Figure VI.5, p.~388]{AnalyticCombinatorics}.}
\label{tab:standard_function_scale}
\end{table}
```