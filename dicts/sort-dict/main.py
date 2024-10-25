# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(unsorted_items: dict) -> list:
    # TU CÓDIGO AQUÍ
    sorted_items = sorted(unsorted_items.items(), key=lambda item: item[1])

    return sorted_items



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
