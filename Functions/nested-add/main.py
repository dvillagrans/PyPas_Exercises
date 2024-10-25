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
