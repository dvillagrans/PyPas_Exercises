# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García

def run(numbers: list) -> list:
    if not numbers:
        return []
    sorted_numbers = sorted(numbers)
    fnumbers = []

    for i in range(len(sorted_numbers) - 1):
        current = sorted_numbers[i]
        next_num = sorted_numbers[i + 1]
        fnumbers.append(current)

        while current + 1 < next_num:
            current += 1
            fnumbers.append(current)

    fnumbers.append(sorted_numbers[-1])

    return fnumbers
# Hecho por: Miguel Sanchez
