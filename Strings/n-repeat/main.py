# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(n: int) -> int:
    if n >= 0 and n <= 9:
        str_n = str(n)
        result = int(str_n ) + int(str_n + str_n) + int(str_n + str_n + str_n)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
