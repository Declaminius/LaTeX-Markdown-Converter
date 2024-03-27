import re
import os
from pathlib import Path
import string
import warnings

# Local modules
import config
import parsing_utils
from convert_bib_to_markdown import write_bibliography

paths = [config.markdown_path, config.chapters_path, config.notes_path, config.figures_path, config.sources_path, config.equations_path, config.tables_path, config.dicts_path]
for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)

class Counter:
    chapter = 0
    section = 0
    subsection = 0
    subsubsection = 0

    theorem = 1
    equation = 1
    figure = 1
    table = 1

    def new_chapter(self):
        self.section = 0
        self.theorem = 1
        self.equation = 1
        self.figure = 1
        self.table = 1

    def new_section(self):
        self.theorem = 1
        self.subsection = 0

class Theorem:

    def __init__(self, env: str, filename: str, has_title: bool):
        self.env = env
        self.filename = filename
        self.has_title = has_title
        self.has_source = False
        self.has_label = False

    def add_source(self, source, location_in_source):
        self.source = source
        self.location_in_source = location_in_source
        self.has_source = True
    
    def add_label(self, label):
        self.label = label
        self.has_label = True

def translate_textstyles(content):
    math = False
    translated_content = ""
    current_block = ""
    i = 0
    while i < len(content):
        current_block += content[i]
        if content[i] != "$":
            i += 1
        else:
            if math:
                # Obsidian sometimes does not accept leading or trailing spaces in inline mathmode
                current_block = current_block.strip()
            else:
                # Todo: \textit{$x$ is ...}
                current_block = basic_textstyles_translation(current_block)
            translated_content += current_block
            math = not math
            if content[i + 1] == "$":
                current_block = "$"
                i += 2
            else:
                current_block = ""
                i += 1
    # don't forget the final block
    if math:
        current_block = current_block.strip()
    else:
        current_block = basic_textstyles_translation(current_block)
    translated_content += current_block
    return translated_content

def basic_textstyles_translation(content):
    content = re.sub("\\\\textit\{(.+?)\}", r"*\1*", content)
    content = re.sub("\\\\textbf\{(.+?)\}", r"**\1**", content)
    content = re.sub("\\\\emph\{(.+?)\}", r"**\1**", content)
    content = re.sub("(\\\\textsc\{.+?\})", r"$\1$", content)
    content = re.sub("(\\\\texttt\{.+?\})", r"$\1$", content)
    return content

def basic_syntax_translation(content):
    content = re.sub("%(.*)", r"%%\1 %%", content)
    content = re.sub("``(.+?)''", r'"\1"', content)
    content = re.sub("`(.+?)'", r"'\1'", content)
    content = re.sub("--", "–", content)
    content = re.sub("\\\\textelp\{\}", "...", content)
    content = re.sub("\\\\phantom\{\}", "\n", content)
    content = re.sub("(\\\\tag\*)", r"%\1\n", content)
    content = re.sub("\\\\chapter\*\{(.*?)\}", r"# \1", content)
    content = re.sub("\\\\section\*\{(.*?)\}", r"## \1", content)
    content = re.sub("\\\\subsection\*\{(.*?)\}", r"### \1", content)
    content = re.sub("\\\\subsubsection\*\{(.*?)\}", r"#### \1", content)
    content = re.sub("\\\\paragraph\*\{(.*?)\}", r"##### \1", content)
    content = re.sub("\\\\subparagraph\*\{(.*?)\}", r"###### \1", content)

    content = translate_textstyles(content)
    return content

def isolate_numbered_equations(block, counter):
    block = re.sub("\\\\qedhere", "{\\\\qquad\\\\blacksquare}", block)
    eq_envs = "(?:" + "|".join(config.math_environments) + ")"
    eq_regex = "(\\\\begin\{" + eq_envs + "\}.*?\\\\end\{" + eq_envs + "\})"
    eq_regex_no_capturing_groups = "\\\\begin\{" + eq_envs + "\}.*?\\\\label\{.+?\}.*?\\\\end\{" + eq_envs + "\}"
    equations = re.findall(eq_regex, block, flags = re.DOTALL)
    if len(equations) > 0:
        eq_links = []
        for eq in equations:
            # TODO
            eq_lines = eq.split("//")
            labels = re.findall(".*?\\\\label\{(.+?)\}.*?", eq, flags = re.DOTALL)
            if len(labels) > 0:
                names = []
                for label in labels:
                    names.append(label.split(":")[1])
                    eq = re.sub("\\\\label\{" + label + "\}", "\\\\tag{" + str(counter.chapter) + "." + str(counter.equation) + "}", eq)
                    counter.equation += 1
                name = ", ".join(names)
            else:
                name = "Equation " + str(counter.chapter) + "." + str(counter.equation) 
                warnings.warn("Numbered equation without label!")
            write_numbered_equation_markdown(eq, name, labels)
            eq_links.append("![["+ name + "|no-title]]")
        block_without_equations = re.split(eq_regex_no_capturing_groups, block, flags = re.DOTALL)
        return block_without_equations[0] + "".join([a + b for a, b in zip(eq_links, block_without_equations[1:])]) + "\n\n", counter
    else:
        return block, counter

def isolate_unnumbered_equations(block):
    eq_envs = "(?:" + "\*|".join(config.math_environments) + "\*)"
    eq_regex = "(\\\\begin\{" + eq_envs + "\}.*?\\\\end\{" + eq_envs + "\})"
    block = re.sub("\\\\qedhere", "{\\\\qquad\\\\blacksquare}", block)
    block = re.sub(eq_regex, r"$$\1$$", block, flags = re.DOTALL)
    return block

def isolate_figures(block, counter):
    fig_regex = "\\\\begin\{figure\}.+?\\\\end\{figure\}"
    subfig_regex = "\\\\begin\{subfigure\}.+?\\\\end\{subfigure\}"
    figures = re.findall("(" + fig_regex + ")", block, flags = re.DOTALL)
    if len(figures) > 0:
        fig_links = []
        for fig in figures:
            # Making sure to get the caption/label from the actual figure and not one of the subfigures
            fig_without_subfigs = "".join(re.split(subfig_regex, fig, flags = re.DOTALL))
            fig_name, fig_label = parse_label_and_caption("Figure", fig_without_subfigs, counter)
            subfig_links = []
            subfigures = re.findall("(" + subfig_regex + ")", fig, flags = re.DOTALL)
            if len(subfigures) > 0:
                for n, subfig in enumerate(subfigures):
                    subfig_name, subfig_label = parse_label_and_caption("Figure", subfig, counter, n)
                    subfig_links.append(subfig_name)
                    write_subfigure_markdown(subfig, fig_name, subfig_name, subfig_label)
            write_figure_markdown(fig, subfig_links, fig_name, fig_label)
            counter.figure += 1
            fig_links.append("> [!tip]+ Figure: " + fig_name + "\n" + "> ![[Figure. "+ fig_name + "#Figure " + fig_name + "|no-h4]]")
        block_without_figures = re.split(fig_regex, block, flags = re.DOTALL)
        return block_without_figures[0] + "\n".join([a + b for a, b in zip(fig_links, block_without_figures[1:])]) + "\n\n"
    else:
        return block

def isolate_tables(block, counter):
    # Todo: unnumbered tables
    table_regex = "\\\\begin\{table\}.+?\\\\end\{table\}"
    tables = re.findall("(" + table_regex + ")", block, flags = re.DOTALL)
    if len(tables) > 0:
        table_links = []
        for table in tables:
            table_name, table_label = parse_label_and_caption("Table", table, counter)
            rows = decompose_table(table)
            write_table_markdown(table, rows, table_name, table_label)
            counter.table += 1
            table_links.append("> [!tip]+ Table: " + table_name + "\n" + "> ![[Table. "+ table_name + "#Table|no-h]]")
            table_links.append("![["+ table_name + "#Table]]")
        block_without_tables = re.split(table_regex, block, flags = re.DOTALL)
        return block_without_tables[0] + "\n".join([a + b for a, b in zip(table_links, block_without_tables[1:])]) + "\n\n"
    else:
        return block

def decompose_table(table):
    table_match = re.search("\\\\begin\{(tabular|array)\}.*?\n(.+?)\\\\end\{(?:tabular|array)\}", table, flags = re.DOTALL)
    rows = []
    if table_match is not None:
        table_contents = table_match.group(2)
        table_contents = re.sub("\\\\hline", "", table_contents)
        table_contents = re.sub("\n", "", table_contents)
        table_contents = re.sub("\$\s+", "$", table_contents)
        table_contents = re.sub("\s+\$", "$", table_contents)
        raw_rows = table_contents.split("\\\\")
        for row in raw_rows:
            if table_match.group(1) == "tabular":
                rows.append([cell.strip() for cell in row.split("&")])
            elif table_match.group(1) == "array":
                parsed_row = []
                for cell in row.split("&"):
                    cell = cell.strip()
                    if (cell == "") or (cell[0] == "*"):
                        parsed_row.append(cell)
                    else:
                        parsed_row.append("$" + cell.strip() + "$")
                rows.append(parsed_row)
    if len(rows[-1]) == 1:
        rows = rows[:-1]
    return rows

def isolate_proofs(block, theorem_name):
    proofs = re.findall("\\\\begin\{proof\}(.+?)\\\\end\{proof\}", block, flags = re.DOTALL)
    if len(proofs) > 0:
        proof_filenames = []
        for n, proof in enumerate(proofs):
            filename = write_proof_markdown(proof, theorem_name, n + 1)
            proof_filenames.append(filename)
        block_without_proofs = re.split("\\\\begin\{proof\}.+?\\\\end\{proof\}", block, flags = re.DOTALL)
        return block_without_proofs, proof_filenames
    else:
        return block, []

def isolate_titlepage(block):
    titlepage_regex = "(.+?\\\\begin\{titlepage\}.+?\\\\end\{titlepage\})"
    titlepage_match = re.search(titlepage_regex, block, flags = re.DOTALL)
    if titlepage_match is not None:
        titlepage = titlepage_match.group(1)
        write_titlepage_markdown(titlepage)
        return re.sub(titlepage_regex, "# [[Titlepage]]", block, flags = re.DOTALL)
    else:
        return block

def convert_lists(block):
    new_block = ""
    nested_counter = 0
    numbered = False
    number = 1
    for line in block.splitlines():
        line = line.lstrip()
        begin_match = re.search("\\\\begin\{itemize\}", line)
        begin_match_number = re.search("\\\\begin\{enumerate\}", line)
        end_match = re.search("\\\\end\{itemize\}", line)
        end_match_number = re.search("\\\\end\{enumerate\}", line)
        if (begin_match is not None) or (begin_match_number is not None):
            nested_counter += 1
            if begin_match_number is not None:
                numbered = True
        elif (end_match is not None) or (end_match_number is not None):
            nested_counter -= 1
            if end_match_number is not None:
                numbered = False
                number = 1
        else:
            if numbered:
                new_block += re.sub("\\\\item", "\t"*(nested_counter - 1) + str(number) + ".", line) + "\n"
                number += 1
            else:
                new_block += re.sub("\\\\item", "\t"*(nested_counter - 1) + "-", line) + "\n"
    return new_block

def convert_quotes(block):
    matchy  = re.search("\\\\epigraph\s*\{", block)
    converted_block = ""
    while matchy is not None:
        quote, new_start = parsing_utils.match_until_closing_curly_brace(matchy.end(), block)
        author, end = parsing_utils.match_until_closing_curly_brace(new_start + 1, block)
        converted_block += block[:matchy.start()] + "> " + quote.replace("\n", "\n> ") + "\n> " + author
        block = block[end:]
        matchy = re.search("\\\\epigraph\s*\{", block)
    return converted_block + block

def convert_footnotes(block):
    matchy  = re.search("\\\\footnote\s*\{", block)
    converted_block = ""
    while matchy is not None:
        footnote, end_of_footnote = parsing_utils.match_until_closing_curly_brace(matchy.end(), block)
        converted_block += block[:matchy.start()] + "^[" + footnote + "]"
        block = block[end_of_footnote:]
        matchy = re.search("\\\\footnote\s*\{", block)
    return converted_block + block

def convert_hrefs(block):
    matchy  = re.search("\\\\href\s*\{", block)
    converted_block = ""
    while matchy is not None:
        link, new_start = parsing_utils.match_until_closing_curly_brace(matchy.end(), block)
        alias, end = parsing_utils.match_until_closing_curly_brace(new_start + 1, block)
        converted_block += block[:matchy.start()] + "[" + alias + "]" + "(" + link + ")"
        block = block[end:]
        matchy = re.search("\\\\href\s*\{", block)
    return converted_block + block

def convert_refs(block):
    refs = re.findall("\\\\ref\{(.+?)\}", block)
    if len(refs) > 0:
        label_filename_dict = parsing_utils.read_linking_dictionary(config.label_dictionary_file)
        for ref in refs:
            if ref in label_filename_dict.keys():
                link_to_file = "[[" + label_filename_dict[ref] + "]]"
                block = block.replace("\\ref{" + ref + "}", link_to_file)
            else:
                warnings.warn(f"{ref} not found!")
    return block

def convert_eqrefs(block):
    eqrefs = re.findall("\\\\eqref\{(.+?)\}", block)
    if len(eqrefs) > 0:
        label_filename_dict = parsing_utils.read_linking_dictionary(config.eqlabel_dictionary_file)
        for eqref in eqrefs:
            if eqref in label_filename_dict.keys():
                link_to_file = "[[" + label_filename_dict[eqref] + "]]"
                alias_match = re.search("\{(.+?)\\\\eqref\{" + eqref + "\}\}", block)
                if alias_match:
                    alias = alias_match.group(1)
                    link_to_file = "[[" + label_filename_dict[eqref] + "|" + alias + "]]"
                    block = re.sub("\{.+?\\\\eqref\{" + eqref + "\}\}", link_to_file, block)
                else:
                    link_to_file = "[[" + label_filename_dict[eqref] + "]]"
                    block = re.sub("\\\\eqref\{" + eqref + "\}", link_to_file, block)
    return block

def convert_citations(block):
    citations = re.findall("(\\\\cite(?:\[(.*?)\])?\{(.+?)\})", block)
    if len(citations) > 0:
        linking_dict = parsing_utils.read_linking_dictionary(config.cite_keys_dictionary_file)
        for citation in citations:
            if citation[2] in linking_dict.keys():
                if citation[1] != "":
                    link_to_file = "[[" + linking_dict[citation[2]] + ", " + citation[1] + "]]"
                else:
                    link_to_file = "[[" + linking_dict[citation[2]] + "]]"
                block = block.replace(citation[0], "\[" + link_to_file + "\]")
    return block


def convert_block(block: str, counter: Counter):
    block = block.strip()
    block = isolate_titlepage(block)
    block = isolate_unnumbered_equations(block)
    block, counter = isolate_numbered_equations(block, counter)
    block = basic_syntax_translation(block)
    block = convert_quotes(block)
    block = convert_footnotes(block)
    block = convert_hrefs(block)
    block = convert_refs(block)
    block = convert_eqrefs(block)
    block = convert_lists(block)
    block = isolate_tables(block, counter)
    block = isolate_figures(block, counter)

    match_env = re.match("\\\\begin\{(.+?)\}", block)
    if match_env is not None:
        env = match_env.group(1)
        theorem = parse_theorem_label_and_name(block, env, counter)
        if theorem.has_label:
            parsing_utils.write_linking_dictionary(theorem.label, theorem.filename, config.label_dictionary_file)
        if env in config.amsthm_environments:
            block = re.sub("\\\\begin\{" + env + "\}.*", "", block)
            block = re.sub("\\\\end\{" + env + "\}", "", block)
            block = re.sub("\\\\label\{.+?\}", "", block)
    else:
        theorem = None

    block = convert_citations(block)
    return block, theorem

def parse_label_and_caption(type, fig, counter, subfig_counter = None):
    if type == "Figure":
        block_counter = counter.figure
    elif type == "Table":
        block_counter = counter.table

    short_caption_match = re.search("\\\\caption\[(.+?)\]\{", fig)
    caption_match = re.search("\\\\caption\{", fig)
    if short_caption_match is not None:
        caption = short_caption_match.group(1)
    elif caption_match is not None:
        caption, _ = parsing_utils.match_until_closing_curly_brace(caption_match.end(),fig)
    else:
        if subfig_counter is not None:
            caption = type + " " + str(counter.chapter) + "." + str(block_counter) + string.ascii_lowercase[subfig_counter]
        else:
            caption = type + " " + str(counter.chapter) + "." + str(block_counter)
        # warnings.warn(f"Figure without caption: {caption}. \nUsing figure number instead of caption as the filename.")
    label_match = re.search("\\\\label\{(.+?)\}", fig)
    caption = parsing_utils.sanitize_filename(caption)
    if label_match is not None:
        label = label_match.group(1)
    else:
        label = None
        # warnings.warn(f"Figure {caption} has no label!")
    return caption, label

def parse_theorem_label_and_name(block, env, counter):
    name_match = re.match("\\\\begin\{.+?\}\[", block)
    filename = ""

    if name_match:
        content = parsing_utils.match_until_closing_square_bracket(block)

        filename = re.sub("\\\\cite(?:\[.*?\])?\{.*?\}", "", content)
        filename = re.sub("[\{\}]+", "", filename)
        filename = parsing_utils.sanitize_filename(filename)
        theorem = Theorem(env, filename, has_title = True)

        citation = re.search("\\\\cite(?:\[(.*?)\])?\{(.*?)\}", content)
        if citation is not None:
            location_in_source = citation.group(1)
            source = citation.group(2)
            theorem.add_source(source, location_in_source)
    
    if filename.strip() == "":
        filename = config.title + ". " + env.capitalize() + " " + str(counter.chapter) + "." + str(counter.section) + "." + str(counter.theorem) 
        theorem = Theorem(env, filename, has_title = False)

    label_match = re.search("\\\\label\{(.+?)\}", block)
    if label_match is not None:
        label = label_match.group(1)
        theorem.add_label(label)

    return theorem

def write_subfigure_markdown(subfigure, figure_name, name, label):
    with open(os.path.join(config.figures_path, "Subfigure. " + name + ".md"), "w", encoding="utf-8") as file:
        file.write("---\n")
        if label is not None:
            parsing_utils.write_linking_dictionary(label, "Subfigure. " + name, config.label_dictionary_file)
            file.write("label: " + label + "\n")
        file.write("Figure: " + '"[[' + figure_name + ']]"' + "\n")
        file.write("tags:\n")
        file.write("  - Figure\n")
        file.write("---\n")
        file.write("#### Figure: " + name + "\n")
        file.write("\n")
        file.write("![[" + name + ".PNG]]\n")
        file.write("\n")
        file.write("#### Sourcecode\n")
        file.write("\n")
        file.write("```\n")
        file.write(subfigure.replace("%",""))
        file.write("\n")
        file.write("```")

def write_figure_markdown(figure, subfigures, name, label):
    with open(os.path.join(config.figures_path, "Figure. " + name + ".md"), "w", encoding="utf-8") as file:
        file.write("---\n")
        if label is not None:
            file.write("label: " + label + "\n")
            parsing_utils.write_linking_dictionary(label, "Figure. " + name, config.label_dictionary_file)      
        file.write("subfigures:\n")
        for subfig in subfigures:
            file.write("  - " + '"[[Subfigure. ' + subfig + ']]"' + "\n")
        file.write("tags:\n")
        file.write("  - Figure\n")
        file.write("---\n")
        file.write("#### Figure: " + name + "\n")
        file.write("\n")
        file.write("![[" + name + ".PNG]]\n")
        file.write("\n")
        file.write("#### Sourcecode\n")
        file.write("\n")
        file.write("```\n")
        file.write(figure.replace("%",""))
        file.write("\n")
        file.write("```")

def write_table_markdown(table, rows, name, label):
    with open(os.path.join(config.tables_path, name + ".md"), "w", encoding="utf-8") as file:
        file.write("---\n")
        if label is not None:
            file.write("label: " + label + "\n")
            parsing_utils.write_linking_dictionary(label, name, config.label_dictionary_file)
        file.write("tags:\n")
        file.write("  - Table\n")
        file.write("---\n")
        # Todo write actual markdown table
        file.write("#### Table\n")
        headers = rows[0]
        file.write("| " + " | ".join(headers) + " |\n")
        file.write("| - "*len(headers) + "|\n")
        for row in rows[1:]:
            file.write("| " + " | ".join(row) + " |\n")
        file.write("#### Sourcecode\n")
        file.write("\n")
        file.write("```\n")
        file.write(table.replace("%",""))
        file.write("\n")
        file.write("```")

def write_proof_markdown(proof, theorem_name, n):
    filename = theorem_name + ". Proof"
    if n > 1:
        filename += " " + str(n)
        
    with open(os.path.join(config.notes_path, filename + ".md"), "w", encoding="utf-8") as file:
        file.write("---\n")
        file.write('Theorem: "[[' + theorem_name + ']]"\n')
        file.write("tags:\n")
        file.write("  - Proof\n")
        file.write("---\n")
        file.write(proof)
    
    return filename

def write_titlepage_markdown(titlepage):
    with open(os.path.join(config.markdown_path, "Titlepage.md"), "w", encoding="utf-8") as file:
        file.write("#### Sourcecode\n")
        file.write("\n")
        file.write("```\n")
        file.write(titlepage)
        file.write("\n")
        file.write("```")

def write_numbered_equation_markdown(equation, name, labels):
    with open(os.path.join(config.equations_path, name + ".md"), "w", encoding="utf-8") as file:
        for label in labels:
            parsing_utils.write_linking_dictionary(label, name, config.eqlabel_dictionary_file)
        file.write("---\n")
        file.write("tags:\n")
        file.write("  - Equation\n")
        file.write("---\n")
        file.write("$$")
        file.write(equation)
        file.write("$$")

def write_block_markdown(theorem: Theorem, block):
    with open(os.path.join(config.notes_path, theorem.filename + ".md"), "w", encoding="utf-8") as file:
        file.write("---\n")
        file.write("tags:\n")
        file.write("  - " + theorem.env.capitalize() + "\n")
        if theorem.has_label:
            file.write("label: " + theorem.label + "\n")
        if theorem.has_source:
            linking_dict = parsing_utils.read_linking_dictionary(config.cite_keys_dictionary_file)
            if theorem.source in linking_dict.keys():
                file.write('Sources:\n  - "[[' + linking_dict[theorem.source] + ']]"\n')
            else:
                file.write("Sources:\n  - " + theorem.source + "\n")
            file.write("Location: " + theorem.location_in_source + "\n")
        file.write("---\n")
        file.write(block.strip())
        file.write("\n")

def write_proof_to_theorem(block, prev_thm_name):
    block_without_proofs, proof_filenames = isolate_proofs(block, prev_thm_name)
    with open(os.path.join(config.notes_path, prev_thm_name + ".md"), "a", encoding="utf-8") as file:
        for block, filename in zip(block_without_proofs, proof_filenames):
            file.write(block.strip())
            file.write("\n")
            file.write("`\\begin{proof}`\n")
            file.write("![[" + filename + "|no-title]]\n")
            file.write("`\\end{proof}`\n")

    return block_without_proofs[-1]

def write_block_to_section(file, block, prev_thm_name, counter):
    block, theorem = convert_block(block, counter)
    if theorem is None or (theorem.env not in config.amsthm_environments):
        proof_match = re.search("\\\\begin\{proof\}", block)
        if proof_match is not None:
            block = write_proof_to_theorem(block, prev_thm_name)
        file.write(block)
        file.write("\n")
        return None
    else:
        if theorem.has_title:
            file.write("> [!" + theorem.env  + "]+ " + theorem.filename + "\n")
        else:
            file.write("> [!" + theorem.env  + "]+ " + "\n")
        file.write("> ![[" + theorem.filename + "|no-title]]\n\n")
        write_block_markdown(theorem, block)
        counter.theorem += 1
        return theorem.filename

def split_into_blocks(section_content):
    blocks = [section_content]
    for env in config.amsthm_environments:
        new_blocks = []
        for block in blocks:
            split_envs = re.split("(\\\\begin\{" + env + "\}.*?\\\\end\{" + env + "\})", block, flags=re.DOTALL)
            new_blocks += split_envs
        blocks = [x for x in new_blocks if x != ""]
    return blocks

def write_subsection_markdown(counter, subsection_content, subsection_title):
    if (heading_match := re.search("\\\\subsection\{(.*?)\}", subsection_title)) is not None:
        counter.subsection += 1
        subsection_filename = f"{str(counter.chapter)}.{str(counter.section)}.{str(counter.subsection)} {heading_match.group(1)}"
    elif (heading_match := re.search("\\\\section\*\{(.*?)\}", subsection_title)) is not None:
        subsection_filename = f"{heading_match.group(1)}"

    label_match = re.match("\s*\\\\label\{(.*?)\}", subsection_content)
    if label_match is not None:
        label = label_match.group(1)
        parsing_utils.write_linking_dictionary(label, subsection_filename, config.label_dictionary_file)
        subsection_content = re.sub("\s*\\\\label\{.*?\}", "", subsection_content, 1)
    else:
        label = None

    blocks = split_into_blocks(subsection_content)
    prev_thm_name = None
    with open(os.path.join(config.chapters_path, subsection_filename + ".md"), "w", encoding="utf-8") as file:
        if label is not None:
            file.write("---\n")
            file.write("label: " +  label + "\n")
            file.write("---\n")
        for block in blocks:
            prev_thm_name = write_block_to_section(file, block, prev_thm_name, counter)
    
    print(f"Chapter {counter.chapter}, Section {counter.section}, Subsection {counter.subsection} done!")
    return subsection_filename, counter

def write_section_markdown(counter, section_content, section_title):
    # Initialize counters per section
    counter.new_section()

    if (heading_match := re.search("\\\\section\{(.*?)\}", section_title)) is not None:
        counter.section += 1
        section_filename = f"{str(counter.chapter)}.{str(counter.section)} {heading_match.group(1)}"
    elif (heading_match := re.search("\\\\section\*\{(.*?)\}", section_title)) is not None:
        section_filename = f"{heading_match.group(1)}"

    label_match = re.match("\s*\\\\label\{(.*?)\}", section_content)
    if label_match is not None:
        label = label_match.group(1)
        parsing_utils.write_linking_dictionary(label, section_filename, config.label_dictionary_file)
        section_content = re.sub("\s*\\\\label\{.*?\}", "", section_content, 1)
    else:
        label = None
    
    split_content =  re.split("(\\\\subsection\*?\{.*?\})", section_content)
    intro, titles, contents = split_content[0], split_content[1::2], split_content[2::2]

    subsection_filenames = []
    for content, title in zip(contents, titles):
        filename, counter = write_subsection_markdown(counter, content, title)
        subsection_filenames.append(filename)

    # Write the markdown file for this section
    with open(os.path.join(config.chapters_path, section_filename + ".md"), "w", encoding="utf-8") as file:
        label_match = re.match("\s*\\\\label\{(.*?)\}", intro)
        if label_match is not None:
            label = label_match.group(1)
            parsing_utils.write_linking_dictionary(label, section_filename, config.label_dictionary_file)
            file.write("---\n")
            file.write("label: " +  label + "\n")
            file.write("---\n")
            intro = re.sub("\s*\\\\label\{.*?\}", "", intro, 1)

        blocks = split_into_blocks(intro)
        prev_thm_name = None
        for block in blocks:
            prev_thm_name = write_block_to_section(file, block, prev_thm_name, counter)

        for filename in subsection_filenames:
            file.write("## " + filename + "\n")
            file.write("\n")
            file.write("![[" + filename + "]]\n")
            file.write("\n")
    
    print(f"Chapter {counter.chapter}, Section {counter.section} done!")
    return section_filename, subsection_filenames, counter

def write_chapter_markdown(chapter, heading, counter):
    counter.new_chapter()

    check_if_numbered = re.search("\\\\chapter\{", heading)
    if check_if_numbered is not None:
        counter.chapter += 1
        markdown_file = str(counter.chapter) + " "
    else:
        markdown_file = ""

    markdown_file += re.search("\\\\chapter\*?\{(.+?)\}", heading).group(1)
    split_content =  re.split("(\\\\section\*?\{.*?\})", chapter)
    intro, titles, contents = split_content[0], split_content[1::2], split_content[2::2]
    
    section_filenames = []
    for section_content, section_title in zip(contents, titles):
        filename, subsection_filenames, counter = write_section_markdown(counter, section_content, section_title)
        section_filenames.append((filename, subsection_filenames))

    # Write the markdown file for this chapter
    with open(os.path.join(config.chapters_path, markdown_file + ".md"), "w", encoding="utf-8") as file:
        label_match = re.match("\s*\\\\label\{(.*?)\}", intro)
        if label_match is not None:
            label = label_match.group(1)
            parsing_utils.write_linking_dictionary(label, markdown_file, config.label_dictionary_file)
            file.write("---\n")
            file.write("label: " +  label + "\n")
            file.write("---\n")
            intro = re.sub("\s*\\\\label\{.*?\}", "", intro, 1)

        blocks = split_into_blocks(intro)
        prev_thm_name = None
        for block in blocks:
            prev_thm_name = write_block_to_section(file, block, prev_thm_name, counter)

        for filename, subsection_filenames in section_filenames:
            file.write("## " + filename + "\n")
            file.write("\n")
            file.write("![[" + filename + "|no-title]]\n")
            file.write("\n")
    
    with open(os.path.join(config.markdown_path, "Table of contents" + ".md"), "a", encoding="utf-8") as file:
        file.write("# [[" + markdown_file + "]]\n\n")
        for filename, subsection_filenames in section_filenames:
            file.write("## [[" + filename + "]]\n")
            file.write("\n")
            for subfilename in subsection_filenames:
                file.write("### [[" + subfilename + "]]\n")
                file.write("\n")

    return markdown_file

def write_markdown():
    counter = Counter()
    # Reset table of contents
    open(os.path.join(config.markdown_path, "Table of contents" + ".md"), "w", encoding="utf-8").close()

    with open(os.path.join(config.latex_path, config.latex_main_file), "r", encoding="utf-8") as file:
        content = file.read()
        interesting_content = content.split("\\begin{document}")[1]
        input_match = re.search("\\\\input\{(.+?)\}", interesting_content)
        flattened_content = ""
        while input_match is not None:
            input_filename = input_match.group(1)
            if input_filename[-4:] != ".tex":
                input_filename += ".tex"
            input_content = ""
            with open(os.path.join(config.latex_path, input_filename), "r", encoding="utf-8") as input_file:
                input_content += input_file.read()
            flattened_content += interesting_content[:input_match.start()] + input_content
            interesting_content = interesting_content[input_match.end():]
            input_match = re.search("\\\\input\{(.+?)\}", interesting_content)
            
    split_content = re.split("(\\\\chapter\*?\{.*?\})", flattened_content)
    intro, headings, chapters = split_content[0], split_content[1::2], split_content[2::2]

    # Clear the main file

    chapter_filenames = []
    for chapter, heading in zip(chapters, headings):
        filename = write_chapter_markdown(chapter, heading, counter)
        chapter_filenames.append(filename)
    
    # Write the main markdown file for this project
    filename = Path(config.latex_main_file).stem
    with open(os.path.join(config.markdown_path, filename + ".md"), "w", encoding="utf-8") as file:
        blocks = split_into_blocks(intro)
        prev_thm_name = None
        for block in blocks:
            prev_thm_name = write_block_to_section(file, block, prev_thm_name, counter)

        for filename in chapter_filenames:
            file.write("# " + filename + "\n")
            file.write("\n")
            file.write("![[" + filename + "]]\n")
            file.write("\n")

write_bibliography(config.bib_file)
write_markdown()