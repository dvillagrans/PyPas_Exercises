# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García

def run(values: list) -> int:
    
    min_value = values[0]

    for value in values[1:]:
        if value < min_value:
            min_value = value

    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
