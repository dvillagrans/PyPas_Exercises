# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(unsorted_items: dict) -> list:
    # TU CÓDIGO AQUÍ
    sorted_items = sorted(unsorted_items.items(), key=lambda item: item[1])

    return sorted_items



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
