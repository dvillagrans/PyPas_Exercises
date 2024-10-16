# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(farm: list) -> str:
    lobo_index = farm.index('lobo')

    if lobo_index == len(farm) - 1:
        msg = "No te quiero ver más por aquí, lobo"
    else:
        ovejas_despues = len(farm) - lobo_index - 1
        msg = f"Cuidado oveja {ovejas_despues}, el lobo te va a comer"

    return msg
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
