# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(n: int) -> int:
    if n >= 0 and n <= 9:
        str_n = str(n)
        result = int(str_n ) + int(str_n + str_n) + int(str_n + str_n + str_n)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
