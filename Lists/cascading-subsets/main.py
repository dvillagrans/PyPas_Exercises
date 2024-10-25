# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(values: list, size: int) -> list:
    
    if not values or size > len(values):
        return []

    cascading = []

    for i in range(len(values) - size + 1):
        cascading.append(values[i:i + size])

    return cascading


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
