# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
