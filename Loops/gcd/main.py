# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(a: int, b: int) -> int:
    gcd_value = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
