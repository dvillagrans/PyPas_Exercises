# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def rslice(texto, wsize):
    if not texto:
        return []

    return [texto[:wsize]] + rslice(texto[wsize:], wsize)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(rslice)

# Made by DVS
