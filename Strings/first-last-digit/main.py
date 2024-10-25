# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(text: str) -> tuple:
    
    for i in text:
        if i.isdigit():
            first_digit = int(i)
            break
    for i in text[::-1]:
        if i.isdigit():
            last_digit = int(i)
            break
    
    return first_digit, last_digit


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
