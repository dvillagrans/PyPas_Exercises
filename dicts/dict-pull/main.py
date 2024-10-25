# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(input_dict: dict, keys: tuple) -> dict:
    # Utilizar comprensión de diccionarios para extraer solo las claves presentes
    extracted_dict = {key: input_dict[key] for key in keys if key in input_dict}
    return extracted_dict

# Ejemplo de uso:
data = {
    'math': 9.75,
    'biology': 6.83,
    'art': 5.42,
    'english': 7.50
}
keys_to_extract = ('biology', 'art')

print(run(data, keys_to_extract))  # {'biology': 6.83, 'art': 5.42}

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
