# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(z: float) -> float:
    PI = 3.14
    area1 = PI * ((z + (z / 2)) ** 2)
    area2 = PI * ((z / 2) ** 2)
    gray_area = area1 - area2
    gray_area = round(gray_area, 2)
    return gray_area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
