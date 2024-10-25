# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(matrix: list) -> int:
    if not all(len(row) == len(matrix) for row in matrix):
        return None

    sum_diagonal = sum(matrix[i][i] for i in range(len(matrix)))

    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
