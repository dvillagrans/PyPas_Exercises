# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(values: list) -> int:
    max_valor = values[0]  
    for valor in values[1:]: 
        if valor > max_valor:
            max_valor = valor
    return max_valor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
