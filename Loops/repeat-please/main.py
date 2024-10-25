# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
