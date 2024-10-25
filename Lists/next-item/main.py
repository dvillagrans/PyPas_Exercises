# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(lst, item):
    if item in lst:
        if lst.index(item) == len(lst) - 1:
            return None
        else:
            return lst[lst.index(item) + 1]
    else:
        return None
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
