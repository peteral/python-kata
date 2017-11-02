"""
Coding kata http://ccd-school.de/coding-dojo/function-katas/csv-tabellieren/
"""
import numpy as np

def tabelliere(unformatted):
    cells = [line.split(';') for line in unformatted.splitlines()]
    widths = np.array([[len(text) for text in line] for line in cells]).transpose()
    max_widths = [max(column) for column in widths]
    formatted = [''.join([row[i].ljust(max_widths[i]) + "|" for i in range(len(row))]) for row in cells]
    formatted.insert(1, ''.join(['-' * width + '+' for width in max_widths]))

    return formatted

result = tabelliere("""Name;Strasse;Ort;Alter
Peter Pan;Am Hang 5;12345 Einsam;42
Maria Schmitz;Kölner Straße 45;50123 Köln;43
Paul Meier;Münchener Weg 1;87654 München;65""")

for row in result: 
    print(row)

