def count_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú')
    
    if len(text) == 0:
        return 0

    return (1 if text[0] in vowels else 0) + count_vowels(text[1:])

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(count_vowels)
