# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
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

# Hecho por: Miguel Sanchez
