def run(nif: str) -> str:
    letras_nif = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = int(nif)
    modulo = nif % 23
    letra = letras_nif[modulo]
    return f"{nif}{letra}"


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
