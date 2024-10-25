# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path

def run(matrix1_path: str, matrix2_path: str, result_path: str) -> bool:
    # Leer la primera matriz desde el archivo
    with open(matrix1_path, 'r', encoding='utf-8') as file:
        matrix1 = [list(map(int, line.split())) for line in file]

    # Leer la segunda matriz desde el archivo
    with open(matrix2_path, 'r', encoding='utf-8') as file:
        matrix2 = [list(map(int, line.split())) for line in file]

    # Sumar las matrices elemento por elemento
    result_matrix = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [a + b for a, b in zip(row1, row2)]
        result_matrix.append(result_row)

    # Escribir la matriz resultante en el archivo de salida
    with open(result_path, 'w', encoding='utf-8', newline='\n') as file:
        for row in result_matrix:
            file.write(" ".join(map(str, row)) + '\n')

    # Comparar el archivo generado con el archivo esperado
    expected_path = Path(result_path).with_suffix('.expected')
    if expected_path.exists():
        # Leer el contenido del archivo generado y el archivo esperado
        with open(result_path, 'r', encoding='utf-8') as gen_file:
            generated = gen_file.read().strip()
        with open(expected_path, 'r', encoding='utf-8') as exp_file:
            expected = exp_file.read().strip()

        # Imprimir los contenidos para diagnóstico si no coinciden
        if generated != expected:
            print(f"\nGenerated:\n{generated}\n")
            print(f"Expected:\n{expected}\n")

        # Retornar True si los archivos coinciden, de lo contrario False
        return generated == expected

    return False

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
