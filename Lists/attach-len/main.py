# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(text: str) -> list:
    # Split the input text into words
    words = text.split()

    # Create a list where each element is in the format "word:length"
    words_length = [f"{word}:{len(word)}" for word in words]

    # Return the list of formatted strings
    return words_length

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
