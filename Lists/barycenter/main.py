# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(A: list, B: list, C: list) -> tuple:
    
    x0 = (A[0] + B[0] + C[0]) / 3
    y0 = (A[1] + B[1] + C[1]) / 3

    x0 = round(x0, 4)
    y0 = round(y0, 4)

    return x0, y0


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
