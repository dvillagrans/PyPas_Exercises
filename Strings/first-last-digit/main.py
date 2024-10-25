# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(text: str) -> tuple:
    
    for i in text:
        if i.isdigit():
            first_digit = int(i)
            break
    for i in text[::-1]:
        if i.isdigit():
            last_digit = int(i)
            break
    
    return first_digit, last_digit


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
