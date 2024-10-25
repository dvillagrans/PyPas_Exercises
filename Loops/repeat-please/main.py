# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run():
    while True:
        nombre_completo = input("¿Su nombre? ")

        if nombre_completo == nombre_completo.title():
            break
        else:
            print("Error. Debe escribirlo correctamente")

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)

# Made by DVS
