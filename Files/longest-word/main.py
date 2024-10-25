# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
import re
from pathlib import Path

def run(input_path: Path) -> str:
    delimiters = r'[ ,.;:()\n]'
    
    longest_word = ''
    max_length = 0
    
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.split(delimiters, line)
            for word in words:
                if len(word) >= max_length:
                    longest_word = word
                    max_length = len(word)

    return longest_word
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
