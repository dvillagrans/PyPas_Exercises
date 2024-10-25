# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
