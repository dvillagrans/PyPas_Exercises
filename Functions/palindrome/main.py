# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    return cleaned_text == cleaned_text[::-1]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)

# Developed by MASG
