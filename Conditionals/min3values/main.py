# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(value1: int | float, value2: int | float, value3: int | float) -> int | float:
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
