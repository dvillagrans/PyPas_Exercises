# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run():
    
    for i in range(1, 10):
        print(''.join(str(j) for j in range(1, i + 1)), end='')
        print(''.join(str(j) for j in range(i - 1, 0, -1)))

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
