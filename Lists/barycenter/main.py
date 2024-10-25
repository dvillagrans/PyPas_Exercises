# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(A: list, B: list, C: list) -> tuple:
    
    x0 = (A[0] + B[0] + C[0]) / 3
    y0 = (A[1] + B[1] + C[1]) / 3

    x0 = round(x0, 4)
    y0 = round(y0, 4)

    return x0, y0


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
