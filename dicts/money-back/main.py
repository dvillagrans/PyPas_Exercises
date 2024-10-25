# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(to_give_back: float, available_currencies: list) -> dict:
    if to_give_back == 0:
        return {}
    available_currencies.sort(reverse=True)

    money_back = {}

    for currency in available_currencies:
        if to_give_back >= currency:
            count = int(to_give_back // currency)
            money_back[currency] = count
            to_give_back -= currency * count

    if to_give_back > 0:
        return None  

    return money_back


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
