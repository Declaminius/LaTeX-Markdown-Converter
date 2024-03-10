import re
import os
import config
from parsing_utils import match_until_closing_curly_brace, write_linking_dictionary

def convert_special_symbols_bibtex(bib_content):
    bib_content = re.sub('\\\\"u', "ü", bib_content)
    bib_content = re.sub('\\\\"a', "ä", bib_content)
    bib_content = re.sub('\\\\"o', "ö", bib_content)
    bib_content = re.sub("\\\\'e", "é", bib_content)
    bib_content = re.sub("\\\\`e", "è", bib_content)
    bib_content = re.sub("\\\\ss", "ß", bib_content)
    bib_content = re.sub("\\\\v\{s\}", "š", bib_content)
    bib_content = re.sub('\\\\&', "&", bib_content)

    return bib_content

def parse_bib_entry(entry_match, bib_content):
    key = re.match("(\w+?),", bib_content[entry_match.end():]).group(1)
    fields_dict = {"Entry type": entry_match.group(1), "Key": key}
    bib_entry, _ = match_until_closing_curly_brace(entry_match.end(),bib_content)
    for line in bib_entry.splitlines():
        field_match = re.search("\s*(\w*?)\s*=\s*\{", line)
        if field_match:
            field = field_match.group(1)
            field_value, _ = match_until_closing_curly_brace(field_match.end(), line)
            fields_dict[field] = field_value
    if len(fields_dict["title"]) < 240:
        filename = fields_dict["title"]
        filename = re.sub('[\\/:"*?<>|\.\{\}]+', "", filename)
    else:
        filename = key  
    
    return key, filename, fields_dict

def generate_apa_like_citations(fields_dict):
    # Generates APA-like aliases in the style of [Author, Year] / [Author 1 & Author 2, Year] / [Author 1 et. al., Year]
    # to be used as inline aliases for Markdown links
    alias = ""
    for key, value in fields_dict.items():
        if key == "author":
            authors = re.sub("[\{\}]+","", value).split(" and ")
            if len(authors) == 1:
                surname = authors[0].split(",")[0]
                alias += surname
            if len(authors) == 2:
                surname1 = authors[0].split(",")[0]
                surname2 = authors[1].split(",")[0]
                alias += surname1 + " & " + surname2
            if len(authors) >= 3:
                surname = authors[0].split(",")[0]
                alias += surname + " et. al."
        elif key == "year":
            alias += ", " + value
    return alias

def write_bib_entry_to_markdown(filename, fields_dict):
    with open(os.path.join(config.sources_path, filename + ".md"), "w") as file:
        file.write("---\n")
        for key, value in fields_dict.items():
            if key == "author":
                file.write("Authors:\n")
                authors = re.sub("[\{\}]+","", value).split(" and ")
                for author in authors:
                    file.write("  - " + author + "\n")
            else:
                file.write(key.capitalize() + ": " + value + "\n")
        file.write("tags:\n")
        file.write("  - Source\n")
        file.write("---\n")
        file.write(config.source_template)

def write_bibliography(bib_file):
    with open(os.path.join(config.latex_path, bib_file), "r", encoding = "utf-8") as file:
        bib_content = file.read()
        bib_content = convert_special_symbols_bibtex(bib_content)
        for entry_match in re.finditer("@(.+?)\{", bib_content):
            key, filename, fields_dict = parse_bib_entry(entry_match, bib_content)
            write_bib_entry_to_markdown(filename, fields_dict)
            alias = generate_apa_like_citations(fields_dict)
            write_linking_dictionary(key, filename + "|" + alias, config.cite_keys_dictionary_file)