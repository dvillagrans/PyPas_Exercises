# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
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

# Made by DVS
