def run(intcolor: int) -> str:
    hexcolor = hex(intcolor)[2:].upper()
    if len(hexcolor) < 6:
        hexcolor = '0' * (6 - len(hexcolor)) + hexcolor
        
    return f'#{hexcolor}'



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
