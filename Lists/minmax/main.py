# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
