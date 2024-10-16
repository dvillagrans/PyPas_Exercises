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
