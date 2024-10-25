# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(num: int) -> str:
    if num == 0:
        return '0'
    
    to_bin = ''
    while num > 0:
        residuo = num % 2
        to_bin = str(residuo) + to_bin
        num //= 2

    return to_bin

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
