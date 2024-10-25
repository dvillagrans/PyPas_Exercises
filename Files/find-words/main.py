# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path
import re

def run(data_path: Path, target_word: str) -> list:
    # Preparar la expresión regular para buscar la palabra con delimitadores y manejo de mayúsculas/minúsculas
    regex = re.compile(r'\b' + re.escape(target_word) + r'\b', re.IGNORECASE)
    
    matches = []
    with open(data_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # Buscar todas las ocurrencias de la palabra en la línea
            for match in regex.finditer(line):
                # La columna se determina por la posición del inicio del match
                column_number = match.start() + 1  # Ajuste para que la columna empiece en 1, no en 0
                matches.append((line_number, column_number))

    return matches


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
