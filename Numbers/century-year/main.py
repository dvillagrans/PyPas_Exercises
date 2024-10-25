# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(year: int) -> int:
    if(year % 100 == 0):
        century = year // 100
    else:
        century = year // 100 + 1
    return century


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
