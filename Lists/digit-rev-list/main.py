# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(number: int) -> list:
    
    reversed_str = str(number)[::-1]
    
    rev_digits = [int(char) for char in reversed_str]
    return rev_digits

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
