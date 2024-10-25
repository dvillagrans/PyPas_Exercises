# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    found_letters = set(char.lower() for char in text if char.isalpha())
    
    return alphabet <= found_letters


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)

# Made by DVS
