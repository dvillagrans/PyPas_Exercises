# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path

def run(input_path: Path) -> tuple:
    num_lines = num_words = num_bytes = 0

    if isinstance(input_path, str):
        input_path = Path(input_path)
    
    with input_path.open('r', encoding='utf-8') as file:
        for line in file:
            num_lines += 1
            num_words += len(line.split())  
            num_bytes += len(line.encode('utf-8')) 

    return num_lines, num_words, num_bytes

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
