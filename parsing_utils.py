import os
import re
import warnings

def sanitize_filename(filename):
    filename = re.sub('[\\\\/:"*?<>|\{\}$]+', "", filename)
    if len(filename) > 240:
        filename = filename[:240]
    while filename[-1] in (".", " "):
        filename = filename[:-1]
    return filename

def match_until_closing_curly_brace(start_index, paragraph):
    level = 1
    i = start_index
    matched_text = ""
    while level > 0:
        char = paragraph[i]
        if char == "{":
            level += 1
        elif char == "}":
            level -= 1
        i += 1
        matched_text += char
    return matched_text[:-1], i

def read_linking_dictionary(dict_file):
    linking_dict = {}
    if os.path.exists(dict_file):
        with open(dict_file, "r", encoding="utf-8") as file:
            content = file.read()
            for line in content.splitlines():
                l, f = line.split("?")
                linking_dict[l] = f
    else:
        open(dict_file, "a", encoding="utf-8").close()
    return linking_dict

def write_linking_dictionary(label, filename, dict_file):
    linking_dict = read_linking_dictionary(dict_file)
    linking_dict[label] = filename
    with open(dict_file, "w", encoding="utf-8") as file:
        for l, f in linking_dict.items():
            file.write(l + "?" + f + "\n")