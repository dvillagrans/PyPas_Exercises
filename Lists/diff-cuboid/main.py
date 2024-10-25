# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(cuboid1: list, cuboid2: list) -> float:
    
    volume1 = cuboid1[0] * cuboid1[1] * cuboid1[2]
    
    volume2 = cuboid2[0] * cuboid2[1] * cuboid2[2]
    
    vol_diff = abs(volume1 - volume2)
    
    return vol_diff

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
