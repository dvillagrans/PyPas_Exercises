def run(matrix1_path: str, matrix2_path: str, result_path: str):
    # Leer la primera matriz desde el archivo
    with open(matrix1_path, 'r') as file:
        matrix1 = [list(map(int, line.split())) for line in file]

    # Leer la segunda matriz desde el archivo
    with open(matrix2_path, 'r') as file:
        matrix2 = [list(map(int, line.split())) for line in file]

    # Sumar las matrices elemento por elemento
    result_matrix = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [a + b for a, b in zip(row1, row2)]
        result_matrix.append(result_row)

    # Escribir la matriz resultante en el archivo de salida
    with open(result_path, 'w') as file:
        for row in result_matrix:
            file.write(" ".join(map(str, row)) + '\n')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
