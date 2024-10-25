# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(nif: str) -> str:
    letras_nif = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = int(nif)
    modulo = nif % 23
    letra = letras_nif[modulo]
    return f"{nif}{letra}"


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
