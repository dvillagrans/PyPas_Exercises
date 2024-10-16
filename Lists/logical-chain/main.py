# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(values: list, oper: str) -> bool:
    if oper == 'and':
        result = all(values)
    elif oper == 'or':
        result = any(values)
    else:
        raise ValueError("Operador no soportado")

    return result



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
