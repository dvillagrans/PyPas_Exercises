# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(text1: str, text2: str) -> int:
    if len(text1) != len(text2):
        return -1
    dhamming = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            dhamming += 1
    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
