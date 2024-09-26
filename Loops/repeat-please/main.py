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
