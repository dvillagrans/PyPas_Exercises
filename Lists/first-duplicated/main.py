# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(values: list) -> int:
    seen = set()  # A set to keep track of seen values

    for value in values:
        if value in seen:
            return value  # Return the first duplicate we find
        seen.add(value)

    return None  # If no duplicates are found, return None

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
