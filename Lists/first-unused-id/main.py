# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(ids: list) -> int:
    
    smallest_unused_id = min(set(range(1, max(ids) + 2)) - set(ids))

    return smallest_unused_id

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
