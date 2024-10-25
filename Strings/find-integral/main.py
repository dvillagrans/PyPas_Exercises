# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(symbol: str) -> str:
    symbol = symbol.split(',')
    integral = f"{int(symbol[0]) // (int(symbol[1]) + 1)}x^{int(symbol[1]) + 1}"
    return integral


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
