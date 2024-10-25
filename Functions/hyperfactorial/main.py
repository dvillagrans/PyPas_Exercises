# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
def hyperfactorial(n):
    if n == 1:
        return 1
    return (n ** n) * hyperfactorial(n - 1)



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(hyperfactorial)

# Developed by MASG
