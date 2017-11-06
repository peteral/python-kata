import re

def loc(code):
    mess = [
        ("^\s*", re.MULTILINE),     # remove leading white space
        ("\/\/.*$", re.MULTILINE),  # remove single line comments
        ("\/\*.*?\*\/", re.DOTALL), # remove multi line comments
        ("^\n", re.MULTILINE),      # remove empty lines
    ]

    cleaned_up = code
    
    for exp, mode in mess:
        e = re.compile(exp, mode)
        cleaned_up = e.sub("", cleaned_up)

    return len(cleaned_up.splitlines())
