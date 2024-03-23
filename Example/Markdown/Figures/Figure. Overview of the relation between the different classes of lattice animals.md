---
label: fig:commutative_diagram
subfigures:
tags:
  - Figure
---
#### Figure: Overview of the relation between the different classes of lattice animals

![[Overview of the relation between the different classes of lattice animals.PNG]]

#### Sourcecode

```
\begin{figure}[hbt!] 
   \centering 
   \begin{tikzcd}[remember picture] 
     \mathcal{D}_A \arrow[r, bend left, "V"] & \mathcal{P}_s \arrow[l, bend left, "\overline{V}"]\\ 
     \mathcal{S}_A & \mathcal{S}_s \arrow[l, "\overline{V}"']\\ 
     \mathcal{M}_A & \mathcal{H} \arrow[l, "\overline{V}"']\\ 
   \end{tikzcd} 
   \begin{tikzpicture}[overlay,remember picture] 
     \path (\tikzcdmatrixname-1-1) to node[midway,sloped]{$\subset$} 
     (\tikzcdmatrixname-2-1); 
     \path (\tikzcdmatrixname-1-2) to node[midway,sloped]{$\subset$} 
     (\tikzcdmatrixname-2-2); 
     \path (\tikzcdmatrixname-2-1) to node[midway,sloped]{$\subset$} 
     (\tikzcdmatrixname-3-1); 
     \path (\tikzcdmatrixname-2-2) to node[midway,sloped]{$\subset$} 
     (\tikzcdmatrixname-3-2); 
   \end{tikzpicture} 
   \caption{Overview of the relation between the different classes of lattice animals.} 
   \label{fig:commutative_diagram} 
 \end{figure}
```