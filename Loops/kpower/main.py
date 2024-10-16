# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(n: int) -> tuple:
    left_side = sum(range(1, n + 1)) ** 2

    right_side = sum(i ** 3 for i in range(1, n + 1))

    return left_side, right_side

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)

# Hecho por: Miguel Sanchez
