# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    return cleaned_text == cleaned_text[::-1]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)

# Made by DVS
