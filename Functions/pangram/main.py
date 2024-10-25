# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    found_letters = set(char.lower() for char in text if char.isalpha())
    
    return alphabet <= found_letters


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)

# Developed by MASG
