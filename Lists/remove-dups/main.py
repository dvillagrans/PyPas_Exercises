# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(nums_dups: list) -> list:
    nums_unique = []
    seen = set()
    for num in nums_dups:
        if num not in seen:
            nums_unique.append(num)
            seen.add(num)
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
