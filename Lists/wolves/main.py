# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(farm: list) -> str:
    lobo_index = farm.index('lobo')

    if lobo_index == len(farm) - 1:
        msg = "No te quiero ver más por aquí, lobo"
    else:
        ovejas_despues = len(farm) - lobo_index - 1
        msg = f"Cuidado oveja {ovejas_despues}, el lobo te va a comer"

    return msg
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
