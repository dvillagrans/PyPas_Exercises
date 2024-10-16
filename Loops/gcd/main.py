# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(a: int, b: int) -> int:
    gcd_value = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
