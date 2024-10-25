# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(intcolor: int) -> str:
    hexcolor = hex(intcolor)[2:].upper()
    if len(hexcolor) < 6:
        hexcolor = '0' * (6 - len(hexcolor)) + hexcolor
        
    return f'#{hexcolor}'



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
