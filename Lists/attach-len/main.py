# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
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

# Made by DVS
