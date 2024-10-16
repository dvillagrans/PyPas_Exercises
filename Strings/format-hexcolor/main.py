# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(intcolor: int) -> str:
    hexcolor = hex(intcolor)[2:].upper()
    if len(hexcolor) < 6:
        hexcolor = '0' * (6 - len(hexcolor)) + hexcolor
        
    return f'#{hexcolor}'



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
