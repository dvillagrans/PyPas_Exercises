def run(items: list) -> list:
    # Filtra los elementos que están en posiciones impares (las posiciones impares no son pares)
    return [item for index, item in enumerate(items) if index % 2 != 0]

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
