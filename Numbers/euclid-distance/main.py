# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
