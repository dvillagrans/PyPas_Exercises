# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    isalpha = True
    for letter in text:
        if letter.lower() not in ALPHABET:
            isalpha = False
            break
    return isalpha


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
