# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]] or None:
    # Get dimensions of A and B
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    # Check if matrices can be multiplied
    if cols_a != rows_b:
        return None

    # Initialize the result matrix with zeros (dimensions: rows_a x cols_b)
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
