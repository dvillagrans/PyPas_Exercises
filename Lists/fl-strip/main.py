# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(numbers: str) -> str:
    
    if not numbers or numbers.count(',') < 2:
        return ""
    number_list = numbers.split(',')

    middle_numbers = number_list[1:-1]

    strip_numbers = ' '.join(middle_numbers)

    return strip_numbers

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
