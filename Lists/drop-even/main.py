# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(items: list) -> list:
    # Filtra los elementos que están en posiciones impares (las posiciones impares no son pares)
    return [item for index, item in enumerate(items) if index % 2 != 0]

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
