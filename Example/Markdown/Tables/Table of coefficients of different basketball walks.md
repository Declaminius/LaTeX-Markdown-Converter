---
label: table:basketball_walks
tags:
  - Table
---
#### Table
|  | **OEIS** | **First terms** | **Growth rate** |
| - | - | - | - |
| $G_{0,1}(z)$ | $[$\texttt{A166135}$](https://oeis.org/A166135)$ | $z+z^2+3z^3+7z^4+22z^5+65z^6$ | $\approx 0.25231 \cdot 4^n \cdot n^{-3/2}$ |
| $G_{1,1}(z)$ | $[$\texttt{A187430}$](https://oeis.org/A187430)$ | $1+2z^2+2z^3+11z^4+24z^5+93z^6$ | $\approx 0.38550 \cdot 4^n \cdot n^{-3/2}$ |
| $G_{0,2}(z)$ | $[$\texttt{A111160}$](https://oeis.org/A111160)$ | $z+z^2+4z^3+9z^4+31z^5+91z^6$ | $\approx 0.40825 \cdot 4^n \cdot n^{-3/2}$ |
#### Sourcecode

```
\begin{table}[hbt!]
\centering
\[ \def\arraystretch{1.25}
\begin{array}{|c|c|c|c|}
\hline
& **OEIS** & **First terms** & **Growth rate** \\ \hline
G_{0,1}(z) & [$\texttt{A166135}$](https://oeis.org/A166135) & z+z^2+3z^3+7z^4+22z^5+65z^6 & \approx 0.25231 \cdot 4^n \cdot n^{-3/2} \\ \hline
G_{1,1}(z) & [$\texttt{A187430}$](https://oeis.org/A187430) & 1+2z^2+2z^3+11z^4+24z^5+93z^6 & \approx 0.38550 \cdot 4^n \cdot n^{-3/2} \\ \hline
G_{0,2}(z) & [$\texttt{A111160}$](https://oeis.org/A111160) & z+z^2+4z^3+9z^4+31z^5+91z^6 & \approx 0.40825 \cdot 4^n \cdot n^{-3/2} \\ \hline
\end{array}
\]
\caption{Table of coefficients of different basketball walks.}
\label{table:basketball_walks}
\end{table}
```