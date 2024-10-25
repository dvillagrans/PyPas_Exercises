# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(values: list) -> tuple:
    # Inicializar min_value y max_value con el primer elemento de la lista
    min_value = values[0]
    max_value = values[0]

    # Recorrer la lista desde el segundo elemento
    for value in values[1:]:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return min_value, max_value

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
