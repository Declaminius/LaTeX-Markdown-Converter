import os

### Important conventions:

# 1. Labels: eq:label, thm:label, ...
# The prefixes may be chosen arbitrarily, but the format x:y needs to be maintained.
# Further, the second part has to be a valid filename, i.e. not containing any of :,*,?,/,\,",<,>,| and not ending with a dot.
# In order for all references to work properly, the script needs to be run twice


highest_level_of_document_structure = 0
# Defines, which elements of document structure are present in the LaTeX document
# Options:
# 0 (for books/reports) or 
# 1 (for articles)

# Latex Structure Hierarchy:
# Level -1: Part
# Level  0: Chapter
# Level  1: Section
# Level  2: Subsection
# Level  3: Subsubsection
# Level  4: Paragraph
# Level  5: Subparagraph

# LaTeX files

latex_path = "Example/LaTeX"
latex_main_file = "Analytic Combinatorics and Bijections for Directed Lattice Paths.tex"
title = "Diplomarbeit"
bib_file = "literature.bib"

# Markdown Paths

markdown_path = "Example/Markdown"
chapters_path = os.path.join(markdown_path, "Chapters")
notes_path = os.path.join(markdown_path, "Notes")
figures_path = os.path.join(markdown_path, "Figures")
sources_path = os.path.join(markdown_path, "Sources")
equations_path = os.path.join(markdown_path, "Equations")
tables_path = os.path.join(markdown_path, "Tables")
dicts_path = os.path.join(markdown_path, ".dicts")

# Files to save dictionaries between LaTeX labels and corresponding markdown file names

label_dictionary_file = os.path.join(dicts_path, "label_filename.txt")
eqlabel_dictionary_file = os.path.join(dicts_path, "eqlabel_filename.txt")
cite_keys_dictionary_file = os.path.join(dicts_path, "cite_keys_filename.txt")

# LaTeX environments, adapt for your need

amsthm_environments = ["definition", "theorem", "lemma", "proposition", "corollary", "remark", "example"]
math_environments = ["equation", "align", "alignat", "gather", "multiline"]
extra_environments = ["figure", "table", "proof"]

# Markdown templates (using the Dataview plugin)

source_template = """
# [[Link to PDF here|PDF]]

# Table of contents


```dataview 
table file.tags as tags, sources, length(file.outlinks) as outlinks, length(file.inlinks) as inlinks
where contains(sources, this.file.link)
sort length(file.inlinks) desc
```
"""