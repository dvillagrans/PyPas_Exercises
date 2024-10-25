# TODO
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    return cleaned_text == cleaned_text[::-1]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)
