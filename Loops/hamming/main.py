# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(text1: str, text2: str) -> int:
    if len(text1) != len(text2):
        return -1
    dhamming = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            dhamming += 1
    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
