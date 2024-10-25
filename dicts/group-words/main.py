# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(words: list) -> dict:
    group_words = {}

    for word in words:
        first_letter = word[0].lower() 

        if first_letter not in group_words:
            group_words[first_letter] = [word]
        else:
            group_words[first_letter].append(word)

    return group_words




# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
