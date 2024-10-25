# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(values: list) -> int:

    if len(values) < 3:
        return 0
    
    max_val = max(values)
    min_val = min(values)

    tsum = sum(v for v in values if v != max_val and v != min_val)

    return tsum

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
