# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(symbol: str) -> str:
    symbol = symbol.split(',')
    integral = f"{int(symbol[0]) // (int(symbol[1]) + 1)}x^{int(symbol[1]) + 1}"
    return integral


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
