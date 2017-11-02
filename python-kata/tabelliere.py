"""
My module
"""
import numpy as np

def tabelliere(unformatted):
    lines = unformatted.splitlines()
    cells = [line.split(';') for line in lines]
    widths = np.array([[len(text) for text in line] for line in cells]).transpose()
    max_widths = [max(column) for column in widths]

    formatted = [[row[i].ljust(max_widths[i]) + "|" for i in range(len(row))] for row in cells]
    formatted = [''.join(row) for row in formatted]
    formatted.insert(1, ''.join(['-' * width + '+' for width in max_widths]))

    return formatted

result = tabelliere("""Name;Strasse;Ort;Alter
Peter Pan;Am Hang 5;12345 Einsam;42
Maria Schmitz;Kölner Straße 45;50123 Köln;43
Paul Meier;Münchener Weg 1;87654 München;65""")

for row in result: 
    print(row)

