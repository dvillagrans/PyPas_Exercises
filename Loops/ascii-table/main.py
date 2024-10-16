# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(start_code: int, end_code: int) -> None:
    step = 0
    for i in range (start_code, end_code + 1):
        if(step == 5):
            print(' ')
            if(i < 100):
                print('0' + str(i) + ' ' + chr(i), end = '   ')
            else:
                print(str(i) + ' ' + chr(i), end = '   ')
            step = 1
        else:
            if(i < 100):
                print('0' + str(i) + ' ' + chr(i), end = '   ')
            else:
                print(str(i) + ' ' + chr(i), end = '   ')
            step += 1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
