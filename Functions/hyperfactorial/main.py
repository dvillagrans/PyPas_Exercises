# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def hyperfactorial(n):
    if n == 1:
        return 1
    return (n ** n) * hyperfactorial(n - 1)



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(hyperfactorial)

# Made by DVS
