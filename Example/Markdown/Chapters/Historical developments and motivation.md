The topic of lattice path combinatorics is a rich and active field of research. 
Its origins can be traced back as early as 1878, when the earliest known drawing of a lattice path is used by Whitworth^[William Allen Whitworth (1840–1905)] \[[[Arrangements of m things of one sort and n things of another sort, under certain conditions of priority|Whitworth, 1878]]\] to help picture a combinatorial problem. 
He uses a two-dimensional lattice path with steps in $\mathcal{S} = \{(1,0), (0,1)\}$ to solve a counting problem involving urns containing $m$ black and $n$ white balls, where the number of white balls drawn must never exceed the number of black balls. 
Today this problem is commonly known as Bertrand's ballot problem, as Bertrand^[Joseph Louis François Bertrand (1822–1900)] rediscovered the result nine years later in 1887 and published his answer in the Comptes Rendus de l'Academie des Sciences: 
The probability is simply $(m - n + 1)/(m + 1)$, provided that $m \geq n$. 
However, it was not until the start of the second half of the 20th century, when the study of lattice path combinatorics really took off.
Around this time the first papers appeared to study lattice path enumeration for the sake of counting lattice paths, see for example Bizley's work on the number of minimal lattice paths from $(0,0)$ to $(km,kn)$ having just $t$ contacts with the line $my = nx$ \[[[Bizley|Bizley, 1954]]\]. 
After this the scientific interest for this field has been steadily growing. 
In fact, Humphreys studied the counting sequence of the number of papers, pertaining to lattice path enumeration, published by decade, noting that the number of such papers more than doubled each decade from 1960 to 2010. 
For more details and a deep dive into the history of lattice path enumeration, the author recommends her thorough survey \[[[A history and a survey of lattice path enumeration|Humphreys, 2010]]\].

Consequently, it is fair to say that the study of lattice path combinatorics has emancipated itself from its parental roots in probability and statistics. Today, its applications reach far into fields like cryptanalysis, crystallography and sphere packing \[[[An invitation to analytic combinatorics and lattice path counting|Lackner & Wallner, 2015]]\]. Furthermore, lattice paths can be used to encode a variety of combinatorial objects, such as trees, maps, permutations, polyominoes, Young tableaux, queues and many, many more \[[[Walks with small steps in the quarter plane|Bousquet-Mélou & Mishna, 2010]]\].

