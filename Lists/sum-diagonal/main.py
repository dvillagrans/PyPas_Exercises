# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(matrix: list) -> int:
    if not all(len(row) == len(matrix) for row in matrix):
        return None

    sum_diagonal = sum(matrix[i][i] for i in range(len(matrix)))

    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
