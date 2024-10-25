# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
