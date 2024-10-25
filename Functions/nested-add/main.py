# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def add(lista):
    total = 0
    for elemento in lista:
        if isinstance(elemento, list):
            total += add(elemento)  
        else:
            total += elemento  
    return total



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(add)

# Made by DVS
