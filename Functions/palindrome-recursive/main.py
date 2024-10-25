# TODO
def is_palindrome(text, start=0, end=None):
    if end is None:
        text = ''.join(ch.lower() for ch in text if ch.isalnum())  
        end = len(text) - 1
    
    if start >= end:
        return True
    
    if text[start] != text[end]:
        return False
    
    return is_palindrome(text, start + 1, end - 1)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)
