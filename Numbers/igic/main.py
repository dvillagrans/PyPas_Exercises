# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(price_with_igic: float, igic: float) -> float:
    clean_price = price_with_igic / (1 + (igic / 100))
    clean_price = round(clean_price, 2)
    return clean_price


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
