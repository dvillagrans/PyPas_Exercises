# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(target_number: int) -> None:
    guess = 0   
    steps = 0
    while guess != target_number:
        guess = int(input('Introduzca número: '))
        steps += 1
        if guess < target_number:
            print('Mayor') 
        elif guess > target_number:
            print('Menor')
        else:
            print('Enhorabuena has encontrado el número en', steps, 'intentos')
            break


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
