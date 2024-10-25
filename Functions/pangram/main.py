# TODO

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    found_letters = set(char.lower() for char in text if char.isalpha())
    
    return alphabet <= found_letters


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)
