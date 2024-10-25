# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(input_list: list[list]) -> dict:
    # Crear un diccionario para almacenar el resultado
    result_dict = {}

    # Iterar sobre cada sublista en la lista de entrada
    for sublist in input_list:
        # La clave será el primer elemento
        key = sublist[0]
        # El valor será el resto de los elementos de la sublista
        value = sublist[1:]

        # Añadir la clave y el valor al diccionario
        result_dict[key] = value

    return result_dict

# Ejemplo de uso:
input_data = [['Item1', 'A', 'B'], ['Item2', 'C', 'D'], ['Item3', 'E', 'F']]
print(run(input_data))  # {'Item1': ['A', 'B'], 'Item2': ['C', 'D'], 'Item3': ['E', 'F']}

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
