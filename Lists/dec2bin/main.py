def run(num: int) -> str:
    if num == 0:
        return '0'
    
    to_bin = ''
    while num > 0:
        residuo = num % 2
        to_bin = str(residuo) + to_bin
        num //= 2

    return to_bin

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
