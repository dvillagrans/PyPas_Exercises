# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(fullname: str) -> str:
    parts = fullname.split(',')
    surname = parts[0].strip()
    name = parts[1].strip()

    surname_parts = surname.split()
    name_parts = name.split()

    initials = name_parts[0][0].upper() + '.'
    for part in surname_parts:
        initials += part[0].upper() + '.'

    return initials

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
