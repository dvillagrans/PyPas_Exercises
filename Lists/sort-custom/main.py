# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(numbers: list[int]) -> list[int]:
    # Make a copy of the input list to avoid modifying the original
    sorted_numbers = numbers[:]

    # Implementing Bubble Sort
    n = len(sorted_numbers)
    for i in range(n):
        # Last i elements are already sorted, no need to check them again
        for j in range(n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # Swap if the element is greater than the next one
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

    return sorted_numbers

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
