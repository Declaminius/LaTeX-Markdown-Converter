# Usage

- Set config.latex_main_file to the path of your LaTeX file
- and execute convert_to_markdown.py.
# Status of the project
## Syntax

- [x] Headings to chapter/section/subsection ⏬ ✅ 2024-02-21
- [x] italics/boldface ⏬ ✅ 2024-02-21
- [x] Footnotes ⏬ ✅ 2024-02-21
- [x] Comments ✅ 2024-02-21
- [x] define a similar textsc command for mathjax 🔽 ✅ 2024-02-22
- [x] itemize/enumerate 🔼 ✅ 2024-02-21
- [x] epigraph -> blockquote 🔽 ✅ 2024-02-22
- [x] detect inline mathmode 🔼 ✅ 2024-02-22
- [ ] whitespace checks

## Structure

- [ ] Level -1: Part
- [x] Level 0: Chapter ✅ 2024-02-23
- [x] Level 1: Section ✅ 2024-02-23
- [x] Level 2: Subsection ✅ 2024-02-24
- [ ] Level 3: Subsubsection
- [x] Level 4: Paragraph ✅ 2024-02-23
- [x] Level 5: Subparagraph ✅ 2024-02-23
- [x] Title page ✅ 2024-02-23
- [ ] table of contents
- [ ] bibliography
- [x] Counter -> class ✅ 2024-02-23
- [x] amsthm-environments ✅ 2024-02-23
	- [ ] source as a property
	- [ ] citation in the title
	- [ ] unnumbered environments
- [x] Proofs 🔼 ✅ 2024-02-24
- [x] Figures 🔽 ✅ 2024-02-22
	- [ ] Add Figure to filenames
	- [x] maintain sourcecode in separate file ✅ 2024-02-21
	- [x] Figures with multiple labels (subfigures) ✅ 2024-02-22
	- [x] do not overwrite manually placed screenshots 🔽 ✅ 2024-02-22
- [/] Tables 🔼
- [x] Math environments 🔼 ✅ 2024-02-22
	- [x] unnumbered equations ✅ 2024-02-22
- [ ] allow manual moving of notes in Obsidian 🔼 
## Linking

- [x] Equation references ⏫ ✅ 2024-02-22
- [ ] multiple labels per math-environment 🔺
- [x] Theorem references 🔼 ✅ 2024-02-21
- [x] hrefs ✅ 2024-02-24
- [ ] switch to cleverrefs
- [-] include path in links ❌ 2024-02-22
- [ ] determine, which Links are Markdown-only and which links carry over to LaTeX🔺
- [ ] prevent breaking links (and creating new files), when renaming stuff in LaTeX 🔼
- [x] Citation references ✅ 2024-02-22
	- [x] APA-like citations ✅ 2024-02-22
- [x] Bibliography 🔼 ✅ 2024-02-22

## Preamble

- [ ] Extract macros from preamble
	- [ ] \newcommand
		- [ ] aber nicht alle: z.B. \includegraphicsboxed
		- [ ] include a range of "safe" commands (mathbb, mathbbm, mathrm, mathcal, 
		- [ ] vielleicht nur manuell möglich
	- [ ] \DeclareMathOperator
	- [ ] \definecolor