# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def f(x: int) -> int:
    return (x ** 2) - (6 * x) + 3

def run(x1: int, x2: int) -> tuple:
    xmin = x1
    fmin = f(xmin)
    for x in range(x1, x2 + 1):
        if f(x) <= fmin:
            xmin = x
            fmin = f(xmin)
    return xmin, fmin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
