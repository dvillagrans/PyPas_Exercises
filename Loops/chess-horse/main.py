# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(target_x: int, target_y: int) -> int:
    steps = 0
    x = target_x
    y = target_y
    flag = True
    while flag:
        if(x == 0 and y == 0):
            return 0
        if(x <= 2 and y <= 2):
            if(x == y): return -1
            steps += 1
            return steps
        if(x > y):
            x -= 2
            y -= 1
            steps += 1
        else:
            x -= 1
            y -= 2
            steps += 1
    return steps
    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
