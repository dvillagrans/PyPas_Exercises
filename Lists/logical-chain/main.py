# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
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

# Made by DVS
