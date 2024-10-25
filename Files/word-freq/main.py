# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path # type: ignore


def run(input_path: Path, lower_bound: int) -> dict:
    if not isinstance(input_path, Path):
        input_path = Path(input_path)
    # Abrimos y leemos el archivo
    with input_path.open('r', encoding='utf-8') as file:
        text = file.read().lower()

    # Contamos las frecuencias de cada palabra manualmente
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # Filtramos las palabras
    freq = {word: count for word, count in word_counts.items() if count >= lower_bound}

    return freq


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
