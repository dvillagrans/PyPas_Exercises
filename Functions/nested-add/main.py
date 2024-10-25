# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
