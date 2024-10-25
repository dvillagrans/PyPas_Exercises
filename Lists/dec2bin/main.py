# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(num: int) -> str:
    if num == 0:
        return '0'
    
    to_bin = ''
    while num > 0:
        residuo = num % 2
        to_bin = str(residuo) + to_bin
        num //= 2

    return to_bin

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
