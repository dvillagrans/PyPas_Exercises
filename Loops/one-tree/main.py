# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run():
    
    for i in range(1, 10):
        print(''.join(str(j) for j in range(1, i + 1)), end='')
        print(''.join(str(j) for j in range(i - 1, 0, -1)))

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
