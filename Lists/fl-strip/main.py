# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(numbers: str) -> str:
    
    if not numbers or numbers.count(',') < 2:
        return ""
    number_list = numbers.split(',')

    middle_numbers = number_list[1:-1]

    strip_numbers = ' '.join(middle_numbers)

    return strip_numbers

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
