# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(stock: dict, merch: str, amount: int) -> bool:
    
    available = stock.get(merch, 0) >= amount


    return available

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
