---
label: tab:asym_alt_cat
tags:
  - Table
---
#### Table
|  | **Meanders** | **Excursions** | **Ratio** |
| - | - | - | - |
| Dyck | $\sim 3/4 \cdot (5/2)^n$ | $\sim 3/8 \cdot (5/2)^n$ | $1/2$ |
| Motzkin | $\sim 3/4 \cdot (7/2)^n$ | $\sim 3/8 \cdot (7/2)^n$ | $1/2$ |
| 2-Motzkin | $\sim 3/4 \cdot (9/2)^n$ | $\sim 3/8 \cdot (9/2)^n$ | $1/2$ |
#### Sourcecode

```
\begin{table}[hbt!]
\centering
\begin{tabular}{|l|c|c|c|}
\hline
& **Meanders** & **Excursions** & **Ratio**\\ \hline
Dyck & $\sim 3/4 \cdot (5/2)^n $ & $\sim 3/8 \cdot (5/2)^n $ & $1/2$ \\ \hline
Motzkin & $\sim 3/4 \cdot (7/2)^n $ & $\sim 3/8 \cdot (7/2)^n $ & $1/2$ \\ \hline
2-Motzkin & $\sim 3/4 \cdot (9/2)^n $ & $\sim 3/8 \cdot (9/2)^n $ & $1/2$ \\ \hline
\end{tabular}
\caption[Asymptotics of lattice paths with alternative catastrophes.]{Table of asymptotic growth rates of lattice paths with alternative catastrophes.}
\label{tab:asym_alt_cat}
\end{table}
```