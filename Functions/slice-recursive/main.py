# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
def rslice(texto, wsize):
    if not texto:
        return []

    return [texto[:wsize]] + rslice(texto[wsize:], wsize)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(rslice)

# Developed by MASG
