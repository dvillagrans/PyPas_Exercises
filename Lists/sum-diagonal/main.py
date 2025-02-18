def run(matrix: list) -> int:
    if not all(len(row) == len(matrix) for row in matrix):
        return None

    sum_diagonal = sum(matrix[i][i] for i in range(len(matrix)))

    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
