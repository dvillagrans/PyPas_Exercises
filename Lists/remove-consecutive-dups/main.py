# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(items: list) -> list:
    result = []
    for i in range(len(items)):
        if i == 0 or items[i] != items[i - 1]:
            result.append(items[i])
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
