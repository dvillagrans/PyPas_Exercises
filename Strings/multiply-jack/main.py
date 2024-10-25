# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(n: int) -> int:
    
    digit = str(n)
    if digit[0] == '-':
        digit = digit[1:]
        
    
    
    leng= len(digit)
    
    result = n * 5 ** leng

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
