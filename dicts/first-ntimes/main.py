# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(numbers: list, nrep: int) -> int:
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        if freq_dict[num] == nrep:
            return num

    return -1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
