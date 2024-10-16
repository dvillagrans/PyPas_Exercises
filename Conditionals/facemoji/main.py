# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(feeling: str) -> str:
    emoji = ""
    feeling = feeling.lower()
    if feeling == "happy":
        emoji = "😀"
    elif feeling == "sad":
        emoji = "😔"
    elif feeling == "angry":
        emoji = "😡"
    elif feeling == "pensive":
        emoji = "🤔"
    elif feeling == "surprised":
        emoji = "😮"
    else:
        emoji = None
    return emoji


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
